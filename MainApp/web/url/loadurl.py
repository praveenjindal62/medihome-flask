
from web.url.url import addURLToList,printURLList
from web.views import MainView
from web.views import AbortView

def loadurllist():
    #GET URL
    addURLToList(r'main(\/)?$','GET',MainView.MainView)
    addURLToList(r'faveicon.ico(\/)?$','GET',AbortView.AbortView404)
    addURLToList(r'signup(\/)?$','GET',MainView.SignupView)
    addURLToList(r'signin(\/)?$','GET',MainView.SigninView)
    addURLToList(r'viewcart(\/)?$','GET',MainView.ViewCartView)
    addURLToList(r'checkout(\/)?$','GET',MainView.CheckOutView)
    addURLToList(r'clearcart(\/)?$','GET',MainView.ClearCartView)
    addURLToList(r'logout(\/)?$','GET',MainView.LogOutView)
    addURLToList(r'search(\/)?$','GET',MainView.SearchView)
    addURLToList(r'product(\/)?$','GET',MainView.ProductView)

    #POST URL 
    addURLToList(r'signup(\/)?$','POST',MainView.SignupView)
    addURLToList(r'signin(\/)?$','POST',MainView.SigninView)
    #
    printURLList()


