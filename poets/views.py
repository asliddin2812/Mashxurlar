from django.shortcuts import render

poets = [
    {
        'name': 'Alisher Navoiy',
        'birth_year': 1441,
        'img': 'Navoiy.jpg',
        'profession': 'Shoir',
        'bio': 'Alisher Navoiy – o‘zbek adabiyoti va jahondagi eng mashhur shoirlardan biri.'
    },
    {
        'name': 'Amir Temur',
        'birth_year': 1336,
        'img': 'temur.jpg',
        'profession': 'Sarkarda',
        'bio': 'Amir Temur – buyuk sarkarda, yirik imperiya asoschisi.'
    },
    {
        'name': 'Islom Karimov',
        'birth_year': 1938,
        'img': 'Karimov.jpg',
        'profession': 'Prezident',
        'bio': 'Islom Karimov – O‘zbekiston Respublikasining birinchi prezidenti.'
    },
    {
        'name': "Mirzo Ulug'bek",
        'birth_year': 1394,
        'img': 'Mirzo_U.jpg',
        'profession': 'Astronom, hukmdor',
        'bio': 'Mirzo Ulug‘bek – buyuk astronom, olim va davlat arbobi.'
    },
    {
        'name': 'Zahiriddin Muhammad Bobur',
        'birth_year': 1483,
        'img': 'Bobur.jpg',
        'profession': 'Shoir, hukmdor',
        'bio': 'Bobur – Boburiylar sulolasining asoschisi, shoiri va yozuvchisi.'
    }
]

def poets_view(request):
    return render(request, 'home.html', context={'poets': [c['name'] for c in poets]})

def poets_detail_view(request, pk):
    poet = poets[pk]
    poet['img'] = 'images/' + poet['img']
    return render(request, 'poet.html', context={'poet': poet})
