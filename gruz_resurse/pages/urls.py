from django.urls import path
from pages.views import (
    IndexView,
    ContactsView,
    ServicesView,
    ComputerDiagnosticView,
    FuelView,
    DangerousCargoTransportationView,
    TradeInView,
    LeasingView,
    SemiTrailersAttentionView,
    ProductView,
    TrucksView,
    AboutUsView,
    GoogleVerification,
    SiteMapView
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("services/", ServicesView.as_view(), name="services"),
    path(
        "computer-diagnostic/",
        ComputerDiagnosticView.as_view(),
        name="computer-diagnostic",
    ),
    path("fuel/", FuelView.as_view(), name="fuel"),
    path(
        "dangerous-cargo-transportation/",
        DangerousCargoTransportationView.as_view(),
        name="danger",
    ),
    path(
        "trade-in/",
        TradeInView.as_view(),
        name="trade-in",
    ),
    path("leasing/", LeasingView.as_view(), name="leasing"),
    path(
        "semi-trailers-attention/",
        SemiTrailersAttentionView.as_view(),
        name="attention",
    ),
    path("product/", ProductView.as_view(), name="product"),
    path("trucks/", TrucksView.as_view(), name="trucks"),
    path("about-us/", AboutUsView.as_view(), name="about"),
    path("google38a66c0f5b25b022.html", GoogleVerification.as_view()),
    path("sitemap.xml", SiteMapView.as_view()),
]
