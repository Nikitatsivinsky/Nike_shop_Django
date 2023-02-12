from django.shortcuts import render

table_famous_dict = {
    'famous':
        {
            'title': {
                'main':
                    {
                        'title': 'Найпопулярніші',
                        'description': 'Найпопулярніші товари зі скидкою.'
                    }
            },
            'shoes': [
                {
                    'name': 'KD Trey 5 X',
                    'price': '$210.00',
                    'discount_price': '$170.00',
                    'image': 'img/r1.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6 mb-20',

                },
                {
                    'name': 'Nike Dunk High Retro SE',
                    'price': '$310.00',
                    'discount_price': '$239.00',
                    'image': 'img/r2.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6 mb-20',
                },
                {
                    'name': 'Nike Air Force 1 LV8',
                    'price': '$250.00',
                    'discount_price': '',
                    'image': 'img/r3.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6 mb-20',
                },
                {
                    'name': 'Nike Air Max Penny',
                    'price': '$250.00',
                    'discount_price': '$149.00',
                    'image': 'img/r5.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6 mb-20',
                },
                {
                    'name': 'Nike Air Trainer SC High',
                    'price': '$190.00',
                    'discount_price': '$129.00',
                    'image': 'img/r6.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6 mb-20',
                },
                {
                    'name': 'Air Jordan 11 CMFT Low',
                    'price': '$119.00',
                    'discount_price': '$230.00',
                    'image': 'img/r7.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6 mb-20',
                },
                {
                    'name': 'Nike Air Max 95 N7',
                    'price': '$220.00',
                    'discount_price': '$199.00',
                    'image': 'img/r9.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6',
                },
                {
                    'name': 'Nike LeBron XX',
                    'price': '$310.00',
                    'discount_price': '$289.00',
                    'image': 'img/r10.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6',
                },
                {
                    'name': 'Nike Free Metcon 4',
                    'price': '$280.00',
                    'discount_price': '$229.00',
                    'image': 'img/r11.jpg',
                    'class': 'col-lg-4 col-md-4 col-sm-6',
                }
            ]
        }
}


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
            ],
        'category':
            [
                {
                    'name': 'Nike Court Vision Mid Next Nature',
                    'link_photo': 'img/category/c1.jpg',
                    'link_category': 'single_product',
                    'class': 'col-lg-8 col-md-8',
                },
                {
                    'name': 'Nike Court Vision Low Next Nature',
                    'link_photo': 'img/category/c2.jpg',
                    'link_category': 'single_product',
                    'class': 'col-lg-4 col-md-4',
                },
                {
                    'name': "Nike Air Force 1 '07",
                    'link_photo': 'img/category/c3.jpg',
                    'link_category': 'single_product',
                    'class': 'col-lg-4 col-md-4',
                },
                {
                    'name': 'Air Jordan 1 Low',
                    'link_photo': 'img/category/c4.jpg',
                    'link_category': 'single_product',
                    'class': 'col-lg-8 col-md-8',
                },
            ],
        'sales':
            {
                'name': 'Розпродаж',
                'link_photo': 'img/category/c5.jpg',
                'link_category': 'single_product',
            },
        'product_slider_new':
            {
                'name_slide':
                    {
                        'title': 'Новинки магазину', 'discription': 'Останнє надходження магазину!'
                    },
                'shoes':
                    [
                        {
                            'name': 'Nike New Hammer sole for Sports person',
                            'price': '$250.00',
                            'link_photo': 'img/product/p1.jpg',
                        },
                        {
                            'name': 'Nike Air Jordan 1 Retro High OG',
                            'price': '$170.00',
                            'link_photo': 'img/product/p2.jpg',
                        },
                        {
                            'name': 'Nike Blazer Low Platform',
                            'price': '$150.00',
                            'link_photo': 'img/product/p3.jpg',
                        },
                        {
                            'name': 'Nike Blazer Mid Next Nature',
                            'price': '$180.00',
                            'link_photo': 'img/product/p4.jpg',
                        },
                        {
                            'name': 'Nike Air Max 90',
                            'price': '$210.00',
                            'link_photo': 'img/product/p5.jpg',
                        },
                        {
                            'name': 'Nike Metcon 8',
                            'price': '$180.00',
                            'link_photo': 'img/product/p6.jpg',
                        },
                        {
                            'name': 'Nike Pegasus Turbo Next Nature',
                            'price': '$280.00',
                            'link_photo': 'img/product/p7.jpg',
                        },
                        {
                            'name': 'Nike Dri-FIT Unlimited D.Y.E.',
                            'price': '$350.00',
                            'link_photo': 'img/product/p8.jpg',
                        },
                    ]
            },
        'product_slider_sale':
            {
                'name_slide':
                    {
                        'title': 'Розпродаж', 'discription': 'Шалені ціни, на шалені кросовки!'
                    },
                'shoes':
                    [
                        {
                            'name': 'Nike Dunk Low SE',
                            'price': '$210.00',
                            'discount_price': '$150.00',
                            'link_photo': 'img/product/p8.jpg',
                        },
                        {
                            'name': 'Nike Dunk High Retro',
                            'price': '$260.00',
                            'discount_price': '$190.00',
                            'link_photo': 'img/product/p10.jpg',
                        },
                        {
                            'name': 'Nike Dunk Low Next Nature',
                            'price': '$360.00',
                            'discount_price': '$290.00',
                            'link_photo': 'img/product/p11.jpg',
                        },
                        {
                            'name': 'Air Jordan 7 Retro SE',
                            'price': '$350.00',
                            'discount_price': '$270.00',
                            'link_photo': 'img/product/p12.jpg',
                        },
                        {
                            'name': 'Jordan 6 Rings',
                            'price': '$320.00',
                            'discount_price': '$220.00',
                            'link_photo': 'img/product/p13.jpg',
                        },
                        {
                            'name': "Nike Air Force 1 '07 LV8",
                            'price': '$200.00',
                            'discount_price': '$120.00',
                            'link_photo': 'img/product/p14.jpg',
                        },
                        {
                            'name': "Nike Air Force 1 '07",
                            'price': '$290.00',
                            'discount_price': '$240.00',
                            'link_photo': 'img/product/p15.jpg',
                        },
                        {
                            'name': 'Nike Zoom Fly 5',
                            'price': '$280.00',
                            'discount_price': '$230.00',
                            'link_photo': 'img/product/p16.jpg',
                        },
                    ]
            },
        'exclusive':
            {
                'deal':
                    {
                        'title': 'Скидка на эксклюзиный товар магазина до - 50%',
                        'description': 'Наш магазин взуття пропонує виняткову знижку 50% на ексклюзивний товар від '
                                       'відомого бренду Nike! Це особлива можливість купити популярні моделі взуття '
                                       'Nike за надзвичайно вигідними цінами. Не пропустіть цю можливість зробити '
                                       'свої покупки за найкращими цінами!',
                        'days': '1',
                        'hours': '3',
                        'minutes': '2',
                        'sec': '37'
                    },
                'product':
                    [
                        {
                            'name': 'Nike Air Max 270',
                            'price': '$230.00',
                            'discount_price': '$220.00',
                            'image_link': 'img/product/e-p1.png',
                        },
                        {
                            'name': 'Nike Dunk High Retro',
                            'price': '$220.00',
                            'discount_price': '$130.00',
                            'image_link': 'img/product/e-p2.png'
                        },
                        {
                            'name': 'Nike Air Jordan 1 Low',
                            'price': '$280.00',
                            'discount_price': '$200.00',
                            'image_link': 'img/product/e-p3.png'
                        }
                    ]
            },
        'brands':
            [
                {'link': 'img/brand/1.png'},
                {'link': 'img/brand/2.png'},
                {'link': 'img/brand/3.png'},
                {'link': 'img/brand/4.png'},
                {'link': 'img/brand/5.png'},
            ],
        'famous': {}
    }
    context.update(table_famous_dict)
    return render(request, 'shop/index.html', context)


def category(request):
    return render(request, 'shop/category.html', table_famous_dict)  # need to give context, not just famous_dict


def single_product(request):
    return render(request, 'shop/single-product.html', table_famous_dict)  # need to give context, not just famous_dict
