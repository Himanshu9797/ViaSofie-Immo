from webapp.models import Data


def header(request):
    cover = Data.objects.all()
    return {
        'data': cover,
    }


