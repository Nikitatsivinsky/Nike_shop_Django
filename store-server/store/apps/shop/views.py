from django.shortcuts import render
from django.apps import apps
from django.core.mail import send_mail

from apps.auth.models import MailDistribution
from .forms import SubscribeForm
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, ListView
from django.views.generic.list import MultipleObjectMixin
from .models import MainBanner, NewesBanner, SaleBanner, ExclusiveBanner, PopularBanner, Item, Category, SubCategory, \
    Color
from django.db.utils import IntegrityError



def get_model(name:str, app = 'shop'):
    context = apps.get_model(app, name)
    return context.objects.all()


def mail_send(request):
    if request.method == 'POST':
        name = request.POST.get('subject', '')
        # Save the email to the database
        email = get_model('MailDistribution', app='auth')(name=name)
        email.save()

        # Send the email
        # send_mail(subject, message, sender, [recipient])
        return render(request, '/')

    return render(request, '/')

def get_famous_dict():
    return {
        'famous':
            {
                'title': {
                    'main':
                        {
                            'title': 'Найпопулярніші',
                            'description': 'Найпопулярніші товари зі скидкою.'
                        }
                },
                'shoes': PopularBanner.objects.all()
            }
    }


class MyBaseView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['famous'] = {}
        context.update(get_famous_dict())
        return context

    def post(self, request, *args, **kwargs):
        form = SubscribeForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            try:
                mail_dis = MailDistribution()
                mail_dis.email = email
                mail_dis.save()
                messages.add_message(request, messages.INFO, 'Ви успішно підписались!')
            except IntegrityError:
                messages.add_message(request, messages.INFO, 'Ви вже є в базі!')
            finally:
                return self.get(request, *args, **kwargs)

class IndexView(MyBaseView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = MainBanner.objects.all()
        context['features'] = [
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
        context['category'] = [
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
                ]
        context['sales'] = {
                    'name': 'Розпродаж',
                    'link_photo': 'img/category/c5.jpg',
                    'link_category': 'single_product',
                }
        context['product_slider_new'] = {
            'name_slide':
                {
                    'title': 'Новинки магазину', 'discription': 'Останнє надходження магазину!'
                },
            'shoes': NewesBanner.objects.all()
        }

        context['product_slider_sale'] = {
            'name_slide':
                {
                    'title': 'Розпродаж', 'discription': 'Шалені ціни, на шалені кросовки!'
                },
            'shoes': SaleBanner.objects.all()
            }

        context['exclusive'] = {
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
            'product': ExclusiveBanner.objects.all()
        }

        context['brands'] = [
            {'link': 'img/brand/1.png'},
            {'link': 'img/brand/2.png'},
            {'link': 'img/brand/3.png'},
            {'link': 'img/brand/4.png'},
            {'link': 'img/brand/5.png'},
            ]
        context.update({'subscribe_form': SubscribeForm()})
        print(context)
        return context


    # def post(self, request, *args, **kwargs):
    #     form = SubscribeForm(data=request.POST)
    #     if form.is_valid():
    #         email = request.POST['email']
    #         try:
    #             mail_dis = MailDistribution()
    #             mail_dis.email = email
    #             mail_dis.save()
    #             messages.add_message(request, messages.INFO, 'Ви успішно підписались!')
    #         except IntegrityError:
    #             messages.add_message(request, messages.INFO, 'Ви вже є в базі!')
    #         finally:
    #             return self.get(request, *args, **kwargs)



# def index(request):
#     main_banner = MainBanner.objects.all()
#     print(main_banner)
#
#     context = {
#         'banner': MainBanner.objects.all(),
#         'features':
#             [
#                 {
#                     'name_feature': 'Безкоштовна доставка',
#                     'description_futures': 'Безкоштовна доставка на всі замовлення',
#                     'link_feature': 'img/features/f-icon1.png'
#                 },
#                 {
#                     'name_feature': 'Політика повернення',
#                     'description_futures': 'Безкоштовне повернення на всі замовлення',
#                     'link_feature': 'img/features/f-icon2.png'
#                 },
#                 {
#                     'name_feature': '24/7 підтримка',
#                     'description_futures': 'Цілодобова підтримка',
#                     'link_feature': 'img/features/f-icon3.png'
#                 },
#                 {
#                     'name_feature': 'Безпечна оплата',
#                     'description_futures': 'Безпечна оплата всіх товарів',
#                     'link_feature': 'img/features/f-icon4.png'
#                 }
#             ],
#         'category':
#             [
#                 {
#                     'name': 'Nike Court Vision Mid Next Nature',
#                     'link_photo': 'img/category/c1.jpg',
#                     'link_category': 'single_product',
#                     'class': 'col-lg-8 col-md-8',
#                 },
#                 {
#                     'name': 'Nike Court Vision Low Next Nature',
#                     'link_photo': 'img/category/c2.jpg',
#                     'link_category': 'single_product',
#                     'class': 'col-lg-4 col-md-4',
#                 },
#                 {
#                     'name': "Nike Air Force 1 '07",
#                     'link_photo': 'img/category/c3.jpg',
#                     'link_category': 'single_product',
#                     'class': 'col-lg-4 col-md-4',
#                 },
#                 {
#                     'name': 'Air Jordan 1 Low',
#                     'link_photo': 'img/category/c4.jpg',
#                     'link_category': 'single_product',
#                     'class': 'col-lg-8 col-md-8',
#                 },
#             ],
#         'sales':
#             {
#                 'name': 'Розпродаж',
#                 'link_photo': 'img/category/c5.jpg',
#                 'link_category': 'single_product',
#             },
#         'product_slider_new':
#             {
#                 'name_slide':
#                     {
#                         'title': 'Новинки магазину', 'discription': 'Останнє надходження магазину!'
#                     },
#                 'shoes': get_model('NewesBanner', app='other')
#             },
#         'product_slider_sale':
#             {
#                 'name_slide':
#                     {
#                         'title': 'Розпродаж', 'discription': 'Шалені ціни, на шалені кросовки!'
#                     },
#                 'shoes': get_model('SaleBanner', app='other')
#             },
#         'exclusive':
#             {
#                 'deal':
#                     {
#                         'title': 'Скидка на эксклюзиный товар магазина до - 50%',
#                         'description': 'Наш магазин взуття пропонує виняткову знижку 50% на ексклюзивний товар від '
#                                        'відомого бренду Nike! Це особлива можливість купити популярні моделі взуття '
#                                        'Nike за надзвичайно вигідними цінами. Не пропустіть цю можливість зробити '
#                                        'свої покупки за найкращими цінами!',
#                         'days': '1',
#                         'hours': '3',
#                         'minutes': '2',
#                         'sec': '37'
#                     },
#                 'product': get_model('ExclusiveBanner', app='other')
#             },
#         'brands':
#             [
#                 {'link': 'img/brand/1.png'},
#                 {'link': 'img/brand/2.png'},
#                 {'link': 'img/brand/3.png'},
#                 {'link': 'img/brand/4.png'},
#                 {'link': 'img/brand/5.png'},
#             ],
#         'famous': {}
#     }
#     context.update(get_famous_dict())
#
#     if request.method == 'POST':
#         print(request)
#         form = SubscribeForm(data=request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             try:
#                 mail_dis = MailDistribution()
#                 mail_dis.email = email
#                 mail_dis.save()
#                 messages.add_message(request, messages.INFO, 'Ви успішно підписались!')
#                 return render(request, 'shop/index.html', context)
#             except Exception:
#                 messages.add_message(request, messages.INFO, 'Ви вже є в базі!')
#                 return render(request, 'shop/index.html', context)
#
#     else:
#         context.update({'subscribe_form': SubscribeForm()})
#         return render(request, 'shop/index.html', context)


class CategoryView(MyBaseView):
    template_name = 'shop/category.html'
    paginate_by = 5
    queryset = Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'subscribe_form': SubscribeForm()})
        context['shoes'] = Item.objects.all()
        context['categories'] = Category.objects.all()
        context['sub_categories'] = SubCategory.objects.all()
        context['colors'] = Color.objects.all()
        print(context)
        return context


class SingleProductView(MyBaseView):
    template_name = 'shop/single-product.html'
    queryset = Item.objects.all()

# def category(request):
#     context = {}
#     context.update(get_famous_dict())
#     context.update({'subscribe_form': SubscribeForm()})
#     return render(request, 'shop/category.html', context)  # need to give context, not just famous_dict


# def single_product(request):
#     return render(request, 'shop/single-product.html', get_famous_dict())  # need to give context, not just famous_dict
