from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.medicine_store),

    path('covid/', views.covid, name='covid'),

    path('oxygen/', views.oxygen, name='oxygen'),

    path('diabetes/', views.diabetes, name='diabetes'),

    path('dermatology/', views.dermatology, name='dermatology'),

    path('depression/', views.depression, name='depression'),

    path('dental/', views.dental, name='dental'),

    path('fracture/', views.fracture, name='fracture'),

    path('eyecare/', views.eyecare, name='eyecare'),

    path('womenscare/', views.womenscare, name='womenscare'),

    path('hairfall/', views.hairfall, name='hairfall'),

    path('blood/', views.blood, name='blood'),

    path('product-detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product-detail'),

    path('covid-detail/<int:pk>',
         views.CovidDetailView.as_view(), name='covid-detail'),

    path('oxygen-detail/<int:pk>',
         views.OxygenDetailView.as_view(), name='oxygen-detail'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),     

    path('orders/', views.orders, name='orders'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),


    path('cart/', views.show_cart, name='show_cart'),

    path('pluscart/', views.plus_cart, name='plus_cart'),

    path('minuscart/', views.minus_cart, name='minus_cart'),

    path('removecart/', views.remove_cart, name='remove_cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),
    
    path('privacy/', views.privacy, name='privacy'),

    path("search/", views.search, name="search"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='medicine/login.html',
                                                         authentication_form=LoginForm), name='login'),

    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='medicine/passwordchange.html',
                                                                  form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='medicine/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='medicine/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='medicine/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='medicine/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='medicine/password_reset_complete.html'),
         name='password_reset_complete'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                