from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
    ('DERMA', 'Dermatology'),
    ('DIAB', 'Diabetes'),
    ('DEP', 'Depression'),
    ('DEN', 'Dental'),
    ('FRAC', 'Fracture'),
    ('EYE', 'Eyecare'),
    ('WOM', 'Womens'),
    ('HAIR', 'Hairfall'),
    ('BP', 'Blood'),
    ('COVID', 'Corona'),
    ('OXY', 'Oxygen'),
)


class Product(models.Model):
    med_name = models.CharField(max_length=100,default="")
    indications = models.TextField(default="")
    dosage = models.TextField(default="")
    side_effects = models.TextField(default="")
    selling_price = models.FloatField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20,default="")
    product_image = models.ImageField(upload_to='prodimg',default="")

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    # extra part written for checkout page individual amount we want
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price          

STATE_CHOICES = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh ", "Arunachal Pradesh "),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"),
    ("National Capital Territory of Delhi",
     "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"),
)


class Customer(models.Model):
    # many to one relationship bana raha han user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    # state field is choice field
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    # __str__ -> returns only string value so when we use id we have to convert it into str
    def __str__(self):
        return str(self.id)        


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    # for show person email who is sending in db
    def __str__(self):
        return self.email
                        
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

   # extra part written for orders page individual amount we want
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price               