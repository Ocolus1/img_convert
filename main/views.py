from django.shortcuts import render
from .utils import Convert
from django.http import FileResponse, JsonResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        img_type  = request.POST["image_type"]
        image  = request.FILES["image"]

        mutate = Convert(image, img_type)
        file = mutate.convert()
        filename = image.name.split(".")[0] + "." + img_type
        data = {
            "file": file.split("/")[-1],
            "filename": filename
        }
        return JsonResponse(data, safe=False)
    context = {}
    return render(request, "main/index.html", context)


def download_file(request, file, filename):
    img = open(f"./download/{file}", 'rb')
    response = FileResponse(img, as_attachment=True, filename=filename)
    return response