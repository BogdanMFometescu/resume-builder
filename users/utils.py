from .models import Profile

from django.db.models import Q


def search_profile(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    all_profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(bio__icontains=search_query))

    return all_profiles, search_query
