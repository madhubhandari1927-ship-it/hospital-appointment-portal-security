def appointment_detail(request, appointment_id):

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