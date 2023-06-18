from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.db.utils import OperationalError


# Create your views here.



def access_table(request, manga_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM manga WHERE manga_id = %s', [manga_id])
            row = cursor.fetchone()
            if row:
                return HttpResponse(f'Manga info for ID {manga_id}: {row}')
            else:
                return HttpResponse('Manga not found')
    except OperationalError:
        return HttpResponse('Table access failed')

def access_top_100(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT manga_id, title, type, chapters, status, score, main_picture FROM manga WHERE sfw = 'True' AND score IS NOT NULL AND main_picture IS NOT NULL ORDER BY score DESC LIMIT 100''')
            rows = cursor.fetchall()
            if rows:
                mangas = []
                for row in rows:
                    manga = {
                        'manga_id': row[0],
                        'title': row[1],
                        'type': row[2],
                        'chapters': row[3],
                        'status': row[4],
                        'score': row[5],
                        'main_picture': row[6]
                    }
                    mangas.append(manga)
                context = {'mangas': mangas}
                return render(request, 'top_mangas.html', context)
            else:
                return HttpResponse('No mangas found')
    except OperationalError:
        return HttpResponse('Table access failed')
    
def access_top_seinen(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT manga_id, title, type, chapters, status, score, main_picture FROM manga WHERE sfw = 'True' AND demographics LIKE '%Seinen%'AND main_picture IS NOT NULL AND score IS NOT NULL ORDER BY score DESC  LIMIT 100''')
            rows = cursor.fetchall()
            if rows:
                mangas = []
                for row in rows:
                    manga = {
                        'manga_id': row[0],
                        'title': row[1],
                        'type': row[2],
                        'chapters': row[3],
                        'status': row[4],
                        'score': row[5],
                        'main_picture': row[6]
                    }
                    mangas.append(manga)
                context = {'mangas': mangas}
                return render(request, 'seinen_mangas.html', context)
            else:
                return HttpResponse('No mangas found')
    except OperationalError:
        return HttpResponse('Table access failed')