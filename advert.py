import json
import keyword


class JsonToObject:
    def __init__(self, d):
        self._json_to_object(d)

    def _json_to_object(self, d):
        for k, v in d.items():
            if isinstance(v, dict):
                obj = JsonToObject(v)
            else:
                obj = v
            kw = k if not keyword.iskeyword(k) else k + '_'
            setattr(self, kw, obj)


class BaseAdvert(JsonToObject):
    def __init__(self, mapping):
        self._price_init(mapping)
        super().__init__(mapping)

    def _price_init(self, mapping):
        if 'price' not in mapping:
            self.price = 0
        elif mapping.get('price') < 0:
            raise ValueError("must be >= 0")
        else:
            self.price = mapping.get('price')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:
    def __repr__(self):
        return f"\033[{self.repr_color_code}m{super().__repr__()}\033[00m"


class Advert(ColorizeMixin, BaseAdvert):
    repr_color_code = 93


if __name__ == "__main__":
    test1_str = """{
                        "title": "python",
                        "price": 12,
                        "location": {
                        "address": "город Москва, Лесная, 7",
                        "metro_stations": ["Белорусская"]
                        }
                    }"""
    test1 = json.loads(test1_str)
    ad1 = Advert(test1)
    print(ad1)
    print(ad1.title, ad1.price, ad1.location.address,
        ad1.location.metro_stations, sep=' - ')
    print()


    test2_str = """{
                        "title": "Вельш-корги",
                        "price": 1000,
                        "class": "dogs",
                        "location": {
                        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                        }
                    }"""
    test2 = json.loads(test2_str)
    ad2 = Advert(test2)
    print(ad2)
    print(ad2.title, ad2.price, ad2.class_, ad2.location.address, sep=' - ')
