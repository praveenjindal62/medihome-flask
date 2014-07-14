from django.conf.urls import include, url, patterns
from MainApp import views
urlpatterns = patterns(
	'',
    url(r'^$',views.HomePage,name="main"),
	url(r'^search/(?P<query>[A-Za-z0-9]+)/$',views.SearchPage,name="search" ),
	url(r'^product/(?P<id>[A-Za-z0-9]+)/$',views.ProductPage,name="search" ),
	url(r'^cookie/$',views.CheckCookie,name="cookie" ),
	url(r'^login/$',views.Login,name="login" ),
	url(r'^logout/$',views.Logout,name="logout" ),
	url(r'^signup/$',views.Signup,name="signup" ),
	url(r'^addtobasket/(?P<id>[A-Za-z0-9]+)/(?P<count>[1-9][0-9]*)/$',views.AddBasket,name="basket" ),
	url(r'^clearcart/$',views.ClearCart,name="clearcart" ),
	url(r'^removeitem/(?P<id>[1-9][0-9]*)-(?P<redirect>\S+)/$',views.RemoveItem,name="remove" ),
	url(r'^checkout/$',views.Checkout,name="checkout" ),
	url(r'^thanks/$',views.OrderProcess,name="complete" ),
)