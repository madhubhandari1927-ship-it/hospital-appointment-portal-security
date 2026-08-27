from django.http import HttpResponse, HttpResponseForbidden
from django.middleware.csrf import get_token

from .models import Appointment, PatientProfile, Review, Doctor


def home(request):
    return HttpResponse(
        """
        <html>
        <head>
            <title>Hospital Appointment Portal</title>
        </head>

        <body>

            <h1>Hospital Appointment Portal</h1>

            <h2>Test Application</h2>

            <p>Django server is working.</p>

            <hr>

            <h3>Appointments</h3>

            <p>
                <a href="/appointment/1/">
                    View Appointment 1
                </a>
            </p>

            <p>
                <a href="/appointment/2/">
                    View Appointment 2
                </a>
            </p>

            <hr>

            <h3>Patient Information</h3>

            <p>
                <a href="/patient/2/">
                    View Patient 1
                </a>
            </p>

            <p>
                <a href="/patient/3/">
                    View Patient 2
                </a>
            </p>

            <hr>

            <p>
                <a href="/login/">
                    Login
                </a>
            </p>

            <hr>

            <p>
                <a href="/review/">
                    Add Doctor Review
                </a>
            </p>

        </body>
        </html>
        """
    )


def appointment_detail(request, appointment_id):

    # ==========================================
    # FLAW 1 - FIXED
    # BROKEN ACCESS CONTROL
    # ==========================================

    if not request.user.is_authenticated:
        return HttpResponseForbidden("Login required")

    try:
        appointment = Appointment.objects.get(
            id=appointment_id,
            patient=request.user
        )

    except Appointment.DoesNotExist:
        return HttpResponseForbidden(
            "You are not authorized to view this appointment."
        )

    return HttpResponse(
        f"""
        <html>
        <head>
            <title>Appointment Details</title>
        </head>

        <body>

            <h1>Appointment Details</h1>

            <p>
                <strong>Appointment ID:</strong>
                {appointment.id}
            </p>

            <p>
                <strong>Patient:</strong>
                {appointment.patient.username}
            </p>

            <p>
                <strong>Doctor:</strong>
                {appointment.doctor.name}
            </p>

            <p>
                <strong>Date:</strong>
                {appointment.date}
            </p>

            <p>
                <strong>Time:</strong>
                {appointment.time}
            </p>

            <p>
                <strong>Reason:</strong>
                {appointment.reason}
            </p>

            <p>
                <strong>Status:</strong>
                {appointment.status}
            </p>

            <br>

            <a href="/">
                Back to Home
            </a>

        </body>
        </html>
        """
    )


def public_patient_information(request, patient_id):

    # ==========================================
    # FLAW 2 - FIXED
    # SENSITIVE INFORMATION EXPOSURE
    # ==========================================

    if not request.user.is_authenticated:
        return HttpResponseForbidden("Login required")

    if request.user.id != patient_id:
        return HttpResponseForbidden(
            "You are not authorized to view this patient information."
        )

    try:
        profile = PatientProfile.objects.get(
            user_id=patient_id
        )

    except PatientProfile.DoesNotExist:
        return HttpResponse(
            "Patient profile not found",
            status=404
        )

    return HttpResponse(
        f"""
        <html>
        <head>
            <title>Patient Information</title>
        </head>

        <body>

            <h1>Patient Information</h1>

            <hr>

            <p>
                <strong>Username:</strong>
                {profile.user.username}
            </p>

            <p>
                <strong>Phone:</strong>
                {profile.phone}
            </p>

            <p>
                <strong>Medical Record:</strong>
                {profile.medical_record}
            </p>

            <hr>

            <a href="/">
                Back to Home
            </a>

        </body>
        </html>
        """
    )


# ==========================================
# FLAW 4 - FIXED
# IMPROPER INPUT VALIDATION
# ==========================================

# ==========================================
# FLAW 5 - FIXED
# CSRF PROTECTION
# ==========================================

def add_review(request):

    if not request.user.is_authenticated:
        return HttpResponseForbidden("Login required")

    if request.method == "POST":

        doctor_id = request.POST.get("doctor_id")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        try:

            doctor = Doctor.objects.get(
                id=doctor_id
            )

            rating = int(rating)

            # ==========================================
            # FLAW 4 SECURITY FIX
            # ==========================================

            if rating < 1 or rating > 5:

                return HttpResponse(
                    """
                    <html>
                    <head>
                        <title>Invalid Rating</title>
                    </head>

                    <body>

                        <h1>Invalid Rating</h1>

                        <p>
                            Rating must be between 1 and 5.
                        </p>

                        <br>

                        <a href="/review/">
                            Try Again
                        </a>

                    </body>
                    </html>
                    """,
                    status=400
                )

            Review.objects.create(
                patient=request.user,
                doctor=doctor,
                rating=rating,
                comment=comment
            )

            return HttpResponse(
                f"""
                <html>
                <head>
                    <title>Review Submitted</title>
                </head>

                <body>

                    <h1>Review Submitted</h1>

                    <p>
                        <strong>Doctor:</strong>
                        {doctor.name}
                    </p>

                    <p>
                        <strong>Rating:</strong>
                        {rating}
                    </p>

                    <p>
                        <strong>Comment:</strong>
                        {comment}
                    </p>

                    <br>

                    <a href="/">
                        Back to Home
                    </a>

                </body>
                </html>
                """
            )

        except Doctor.DoesNotExist:

            return HttpResponse(
                "Doctor not found.",
                status=400
            )

        except (ValueError, TypeError):

            return HttpResponse(
                "Rating must be a number between 1 and 5.",
                status=400
            )

    # ==========================================
    # CSRF TOKEN
    # ==========================================

    csrf_token = get_token(request)

    return HttpResponse(
        f"""
        <html>
        <head>
            <title>Add Doctor Review</title>
        </head>

        <body>

            <h1>Add Doctor Review</h1>

            <form method="post">

                <input
                    type="hidden"
                    name="csrfmiddlewaretoken"
                    value="{csrf_token}"
                >

                <p>
                    <label>Rating (1-5):</label>
                </p>

                <input
                    type="number"
                    name="rating"
                >

                <p>
                    <label>Comment:</label>
                </p>

                <textarea
                    name="comment"
                    rows="5"
                    cols="40"
                ></textarea>

                <br><br>

                <input
                    type="hidden"
                    name="doctor_id"
                    value="1"
                >

                <button type="submit">
                    Submit Review
                </button>

            </form>

        </body>
        </html>
        """
    )