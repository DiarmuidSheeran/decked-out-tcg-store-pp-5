from product.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        if product_id in self.cart:
            self.cart[product_id] += product_qty
        else:
            self.cart[product_id] = product_qty

        self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
		
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.on_special_offer:
                        total = total + (product.discounted_price * value)
                    else:
                        total = total + (product.price * value)

        return total

    def get_prods(self):
        product_ids = self.cart.keys()

        quantities = self.cart
        products_with_quantities = {}

        for product_id in product_ids:
            product_id = int(product_id)
            product = Product.objects.get(id=product_id)
            products_with_quantities[product] = quantities[str(product_id)]

        return products_with_quantities

    def __len__(self):
        return sum(self.cart.values())

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def clear(self):
        self.session['session_key'] = {}
        self.session.modified = True