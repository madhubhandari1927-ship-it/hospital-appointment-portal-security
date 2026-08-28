from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor, PatientProfile


def doctor_list(request):
    search = request.GET.get('search', '').strip()

    if search:
        doctors = Doctor.objects.filter(
            name__icontains=search
        )
    else:
        doctors = Doctor.objects.all()

    return render(
        request,
        'appointments/doctor_list.html',
        {
            'doctors': doctors,
            'search': search
        }
    )


@login_required
def patient_medical_record(request, patient_id):
    profile = get_object_or_404(
        PatientProfile,
        user_id=patient_id
    )

    # Only the patient themselves or a staff user can see the record
    if request.user != profile.user and not request.user.is_staff:
        return render(
            request,
            'appointments/access_denied.html',
            status=403
        )

    medical_record = profile.get_medical_record()

    return render(
        request,
        'appointments/medical_record.html',
        {
            'profile': profile,
            'medical_record': medical_record
        }
    )