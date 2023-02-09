from django.shortcuts import render


def index(request):
    context = {
        'banner':
            [
                {
                    'name_shoes': 'Nike LeBron',
                    'name_model': 'Zoom Soldier',
                    'description': 'Nike LeBron Zoom Soldier 8 Flyease Cavs - це модель кросівок, створена спеціально '
                                   'для команди Cleveland Cavaliers, в якій грає Леброн Джеймс. Вони особливо '
                                   'виділяються своєю технологією Flyease, яка забезпечує легке і швидке застегнення '
                                   'через спеціальну систему застібки.',
                    'image_link': 'img/banner/banner-img.png'
                },
                {
                    'name_shoes': 'Nike Air Max',
                    'name_model': '270 React',
                    'description': 'Модель особливо виділяється своїм високим комфортом та динамічною амортизацією, '
                                   'яку забезпечує технологія Air Max. Дизайн кросівок містить чисті лінії та '
                                   'мінімалістичний стиль, що дозволяє їм виглядати елегантно та модно. Вони також '
                                   'мають високу міцність та довговічність, що робить їх прекрасним вибором для '
                                   'спорту та повсякденного носіння.',
                    'image_link': 'img/banner/banner-img2.png'

                }
            ],
        'features':
            [
                {
                    'name_feature': 'Безкоштовна доставка',
                    'description_futures': 'Безкоштовна доставка на всі замовлення',
                    'link_feature': 'img/features/f-icon1.png'
                },
                {
                    'name_feature': 'Політика повернення',
                    'description_futures': 'Безкоштовне повернення на всі замовлення',
                    'link_feature': 'img/features/f-icon2.png'
                },
                {
                    'name_feature': '24/7 підтримка',
                    'description_futures': 'Цілодобова підтримка',
                    'link_feature': 'img/features/f-icon3.png'
                },
                {
                    'name_feature': 'Безпечна оплата',
                    'description_futures': 'Безпечна оплата всіх товарів',
                    'link_feature': 'img/features/f-icon4.png'
                }
            ]
    }
    return render(request, 'shop/index.html', context)


def category(request):
    return render(request, 'shop/category.html')


def single_product(request):
    return render(request, 'shop/single-product.html')