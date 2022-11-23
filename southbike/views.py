from django.shortcuts import render


def Home(request):
    return render(request, 'southbike/pages/home.html')


def Company(request, company):
    return render(request, 'southbike/pages/company-south.html')


def Gallery(request, gallery):
    return render(request, 'southbike/pages/gallerySouth.html')


def GalleryOne(request, galleryone):
    return render(request, 'southbike/pages/galleryOne.html')


def GalleryTwo(request, gallerytwo):
    return render(request, 'southbike/pages/galleryTwo.html')


def Record(request, record):
    return render(request, 'southbike/pages/bicycle.html')


def Representative(request, representative):
    return render(request, 'southbike/pages/representative.html')


def Urbans(request, urbans):
    return render(request, 'southbike/pages/urbans.html')


def Freeride(request, freeride):
    return render(request, 'southbike/pages/freeride.html')


def InfantilOne(request, infantilone):
    return render(request, 'southbike/pages/infantilPageOne.html')


def InfantilTwo(request, infantiltwo):
    return render(request, 'southbike/pages/infantilPageTwo.html')


def MountainBikeOne(request, mountainbikeone):
    return render(request, 'southbike/pages/mountainBike.html')


def MountainBikeTwo(request, mountainbiketwo):
    return render(request, 'southbike/pages/mountainBikeTwo.html')


def MountainBikeThree(request, mountainbikethree):
    return render(request, 'southbike/pages/mountainBikethree.html')