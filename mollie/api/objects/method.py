from .base import ObjectBase
from .issuer import Issuer
from .list import ObjectList


class Method(ObjectBase):
    @classmethod
    def get_resource_class(cls, client):
        from ..resources.methods import Methods

        return Methods(client)

    BANCONTACT = "bancontact"
    BANKTRANSFER = "banktransfer"
    BELFIUS = "belfius"
    CREDITCARD = "creditcard"
    DIRECTDEBIT = "directdebit"
    EPS = "eps"
    GIFTCARD = "giftcard"
    GIROPAY = "giropay"
    IDEAL = "ideal"
    IN3 = "in3"
    KBC = "kbc"
    KLARNAPAYLATER = "klarnapaylater"
    KLARNAPAYNOW = "klarnapaynow"
    KLARNASLICEIT = "klarnasliceit"
    MEALVOUCHER = "mealvoucher"
    MISTERCASH = "mistercash"
    MYBANK = "mybank"
    PAYPAL = "paypal"
    PAYSAFECARD = "paysafecard"
    PODIUMCADEAUKAART = "podiumcadeaukaart"
    PRZELEWY24 = "przelewy24"
    SOFORT = "sofort"

    @property
    def description(self):
        return self._get_property("description")

    @property
    def id(self):
        return self._get_property("id")

    @property
    def minimum_amount(self):
        return self._get_property("minimumAmount")

    @property
    def maximum_amount(self):
        return self._get_property("maximumAmount")

    @property
    def pricing(self):
        return self._get_property("pricing")

    @property
    def image_svg(self):
        images = self._get_property("image")
        return images["svg"]

    @property
    def image_size1x(self):
        images = self._get_property("image")
        return images["size1x"]

    @property
    def image_size2x(self):
        images = self._get_property("image")
        return images["size2x"]

    @property
    def issuers(self):
        """Return the list of available issuers for this payment method."""
        issuers = self._get_property("issuers") or []
        result = {
            "_embedded": {
                "issuers": issuers,
            },
            "count": len(issuers),
        }
        return ObjectList(result, Issuer)
