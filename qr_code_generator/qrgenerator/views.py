from django.shortcuts import render
from django.http import HttpResponse
from .models import QRCodeInfo
import qrcode


def generate_qr_code(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        color = request.POST.get('color', 'black')
        size = int(request.POST.get('size', 200))

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=color, back_color="white")

        img_path = f'media/{data}_qr.png'
        img.save(img_path)

        QRCodeInfo.objects.create(data=data, color=color, size=size)

        return render(request, 'qrgenerator/generate_qr_code.html',
                      {'img_path': img_path})

    return render(request, 'qrgenerator/generate_qr_code.html')


def display_qr_codes(request):
    qr_codes = QRCodeInfo.objects.all()
    return render(request, 'qrgenerator/display_qr_codes.html',
                  {'qr_codes': qr_codes})
