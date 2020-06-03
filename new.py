import random
import string

spec = "!@#$%^&*()~"
random = ''.join([random.choice(string.ascii_letters+ string.ascii_uppercase + string.ascii_lowercase + spec
                                + string.digits) for n in range(5)])

print(random)