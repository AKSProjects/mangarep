from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.db.utils import OperationalError
from django.shortcuts import render, get_object_or_404
from .models import Manga
import json



# Create your views here.

def home(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT manga_id, title, type, chapters, status, score, main_picture FROM manga WHERE sfw = 'True' AND score IS NOT NULL AND main_picture IS NOT NULL ORDER BY score DESC LIMIT 5")
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

        cursor.execute('''SELECT manga_id, title, type, chapters, status, score, main_picture, scored_by FROM manga WHERE sfw = 'True' AND score IS NOT NULL AND main_picture IS NOT NULL ORDER BY scored_by DESC LIMIT 5''')
        rows = cursor.fetchall()
        if rows:
            mangas1 = []
            for row in rows:
                manga = {
                    'manga_id': row[0],
                    'title': row[1],
                    'type': row[2],
                    'chapters': row[3],
                    'status': row[4],
                    'score': row[5],
                    'main_picture': row[6],
                    'scored_by': row[7]
                }
                mangas1.append(manga)

    context = {'mangas': mangas, 'mangas1': mangas1}
    return render(request, 'main/home.html', context)

    


   
   

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
                return render(request, 'main/top_mangas.html', context)
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
                return render(request, 'main/seinen_mangas.html', context)
            else:
                return HttpResponse('No mangas found')
    except OperationalError:
        return HttpResponse('Table access failed')
    
def access_top_shounen(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT manga_id, title, type, chapters, status, score, main_picture FROM manga WHERE sfw = 'True' AND demographics LIKE '%Shounen%' AND main_picture IS NOT NULL AND score IS NOT NULL ORDER BY score DESC LIMIT 100''')
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
                return render(request, 'main/shounen_mangas.html', context)
            else:
                return HttpResponse('No mangas found')
    except OperationalError:
        return HttpResponse('Table access failed')

def access_top_manhua(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT manga_id, title, type, chapters, status, score, main_picture FROM manga WHERE sfw = 'True' AND type='manhua' AND main_picture IS NOT NULL AND score IS NOT NULL ORDER BY score DESC LIMIT 100''')
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
                return render(request, 'main/manhuas.html', context)
            else:
                return HttpResponse('No mangas found')
    except OperationalError:
        return HttpResponse('Table access failed')
    
def access_top_shoujo(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT manga_id, title, type, chapters, status, score, main_picture FROM manga WHERE sfw = 'True' AND demographics LIKE '%Shoujo%' AND main_picture IS NOT NULL AND score IS NOT NULL ORDER BY score DESC LIMIT 100''')
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
                return render(request, 'main/shoujo_mangas.html', context)
            else:
                return HttpResponse('No mangas found')
    except OperationalError:
        return HttpResponse('Table access failed')


def fetch_manga_data_from_database(manga_id):
    try:
        with connection.cursor() as cursor:
            query = '''
                SELECT main_picture, manga_id, synopsis, title, type, chapters, status, score, genres, themes, demographics, authors, background, title_english
                FROM manga
                WHERE sfw = 'True'
                AND score IS NOT NULL
                AND main_picture IS NOT NULL
                AND manga_id = %s
                ORDER BY score DESC
            '''
            cursor.execute(query, [manga_id])
            row = cursor.fetchone()
            if row:
                author_data = row[11]  # Assuming the author data is in the 12th position
                first_name_start = author_data.find("'first_name':") + len("'first_name': '")
                first_name_end = author_data.find("'", first_name_start)
                first_name = author_data[first_name_start:first_name_end]

                last_name_start = author_data.find("'last_name':") + len("'last_name': '")
                last_name_end = author_data.find("'", last_name_start)
                last_name = author_data[last_name_start:last_name_end]

                author_name = f"{first_name} {last_name}"

                manga_data = {
                    'main_picture': row[0],
                    'manga_id': row[1],
                    'synopsis': row[2],
                    'title': row[3],
                    'type': row[4],
                    'chapters': row[5],
                    'status': row[6],
                    'score': row[7],
                    'genres': row[8],
                    'themes': row[9],
                    'demographics': row[10],
                    'authors': author_name,
                    'background': row[12],
                    'title_english': row[13],
                    
                }
                return manga_data
            else:
                return None
    except Exception as e:
        return None



def manga_template(request, manga_id):
    manga_data = fetch_manga_data_from_database(manga_id)
    if manga_data:
        context = {'manga': manga_data}
        return render(request, 'main/manga_template.html', context)
    else:
        return HttpResponse('Manga not found')
    


def classics(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT manga_id, title, type, chapters, status, score, main_picture, scored_by FROM manga WHERE sfw = 'True' AND score IS NOT NULL AND main_picture IS NOT NULL ORDER BY scored_by DESC LIMIT 100''')
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
                        'main_picture': row[6],
                        'scored_by': row[7]
                    }
                    mangas.append(manga)
                context = {'mangas': mangas}
                return render(request, 'main/classics.html', context)
            else:
                return HttpResponse('No mangas found')
    except OperationalError:
        return HttpResponse('Table access failed')