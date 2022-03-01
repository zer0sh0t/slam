import numpy as np
import matplotlib.pyplot as plt

# b -> a
def concatenate_transform(a, b):
    laa, ca, sa, txa, tya = a
    lab, cb, sb, txb, tyb = b

    # New lambda is multiplication.
    la = laa * lab

    # New rotation matrix uses trigonometric angle sum theorems.
    c = ca*cb - sa*sb
    s = sa*cb + ca*sb

    # New translation is a translation plus rotated b translation.
    tx = txa + laa * ca * txb - laa * sa * tyb
    ty = tya + laa * sa * txb + laa * ca * tyb

    return (la, c, s, tx, ty)

def apply_transform(trafo, p):
    la, c, s, tx, ty = trafo
    lac = la * c
    las = la * s
    x = lac * p[0] - las * p[1] + tx
    y = las * p[0] + lac * p[1] + ty
    return (x, y)

a = (20, np.cos(34), np.sin(34), 5, 43)
b = (2, 1/(2**0.5), 1/(2**0.5), 3, 4)
c = (2, np.cos(213), np.sin(341), 2, 65)

p = (2, 3)
con = concatenate_transform(b, a)
con = concatenate_transform(c, con)

p_ = apply_transform(con, p)
p__ = apply_transform(b, apply_transform(a, p))
p__ = apply_transform(c, p__)

print(p_)
print(p__)
plt.scatter(p_[0], p_[1], marker='x')
plt.scatter(p__[0], p__[1], marker='o')
plt.show()
