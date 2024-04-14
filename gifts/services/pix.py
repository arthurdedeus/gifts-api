import os

from pypix import Pix
from pypix.pix import get_qrcode


class PixService(Pix):
    def __init__(self):
        super().__init__()
        self.set_name_receiver(os.environ.get("PIX_NAME_RECEIVER"))
        self.set_city_receiver(os.environ.get("PIX_CITY_RECEIVER"))
        self.set_key(os.environ.get("PIX_KEY"))

    def create_qr_code(self, *, amount):
        amount_in_reais = amount / 100
        self.set_amount(amount_in_reais)
        return self.get_qr_code()

    def get_qr_code(self, color="#74b8cf"):
        try:
            self.qr = get_qrcode(border=1)
            self.qr.add_data(self.get_br_code())
            self.qr.make(fit=True)
            return self.qr.make_image(fill_color=color, back_color="white").convert(
                "RGB"
            )
        except ValueError:
            return
