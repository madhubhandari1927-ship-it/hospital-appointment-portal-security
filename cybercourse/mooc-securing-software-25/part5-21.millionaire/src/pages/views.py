from django.shortcuts import render, redirect

from .models import questions


def find_topic(tid):
    for q in questions:
        if q['id'] == tid:
            return q
    return None


def quizView(request, tid):
    topic = find_topic(tid)

    if topic is None:
        return redirect('/cheater/')

    # If a game is already active, do not allow
    # the player to change the topic or restart the game.
    if 'topic' in request.session and 'level' in request.session:

        current_topic = request.session['topic']
        level = request.session['level']

        # Trying to change the topic is cheating
        if current_topic != tid:
            request.session['cheater'] = True
            return redirect('/cheater/')

        # Trying to access the quiz after completing it is cheating
        if level >= len(topic['questions']):
            request.session['cheater'] = True
            return redirect('/cheater/')

        # Continue the current game
        question = topic['questions'][level]

        return render(
            request,
            'pages/question.html',
            {
                'topic': topic,
                'question': question
            }
        )

    # Start a new game
    request.session['topic'] = tid
    request.session['level'] = 0
    request.session['cheater'] = False

    return render(
        request,
        'pages/question.html',
        {
            'topic': topic,
            'question': topic['questions'][0]
        }
    )


def answerView(request, tid, aid):
    topic = find_topic(tid)

    # Invalid topic
    if topic is None:
        return redirect('/cheater/')

    # Check whether the player has already been caught
    if request.session.get('cheater', False):
        return redirect('/cheater/')

    # There must be an active game
    if 'topic' not in request.session or 'level' not in request.session:
        return redirect('/cheater/')

    # Player cannot change topic during the game
    if request.session['topic'] != tid:
        request.session['cheater'] = True
        return redirect('/cheater/')

    level = request.session['level']

    # Invalid question level
    if level < 0 or level >= len(topic['questions']):
        request.session['cheater'] = True
        return redirect('/cheater/')

    question = topic['questions'][level]

    # Invalid answer number
    if aid < 0 or aid >= len(question['answers']):
        request.session['cheater'] = True
        return redirect('/cheater/')

    # Correct answer
    if question['correct'] == aid:
        level += 1
        request.session['level'] = level

        # Game completed
        if level == len(topic['questions']):
            return redirect('/finish/')

        return render(
            request,
            'pages/question.html',
            {
                'topic': topic,
                'question': topic['questions'][level]
            }
        )

    # A wrong answer ends the game
    request.session['cheater'] = True

    return redirect('/incorrect/')


def incorrectView(request):
    return render(
        request,
        'pages/incorrect.html'
    )


def finishView(request):
    # The finish page can only be reached after
    # answering all questions correctly.
    topic_id = request.session.get('topic')
    level = request.session.get('level')

    if request.session.get('cheater', False):
        return redirect('/cheater/')

    if topic_id is None or level is None:
        return redirect('/cheater/')

    topic = find_topic(topic_id)

    if topic is None:
        return redirect('/cheater/')

    if level != len(topic['questions']):
        return redirect('/cheater/')

    return render(
        request,
        'pages/finish.html'
    )


def cheaterView(request):
    return render(
        request,
        'pages/cheater.html'
    )


def thanksView(request):
    return render(
        request,
        'pages/thanks.html'
    )


def topicView(request, tid):
    topic = find_topic(tid)

    if topic is None:
        return redirect('/cheater/')

    return render(
        request,
        'pages/topic.html',
        {
            'topic': topic
        }
    )


def topicsView(request):
    return render(
        request,
        'pages/topics.html',
        {
            'questions': questions
        }
    )