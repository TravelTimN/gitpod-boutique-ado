from django.shortcuts import render


def view_bag(request):
    """ View to return the bag contents page """

    return render(request, 'bag/bag.html')
