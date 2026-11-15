Because all terms involving $\alpha$ cancel, $\sum_i c_i = 0$. Then:

$$
  f = c_1 a_1 \cdot \frac{1}{a_1} f_1 + \cdots + c_n a_n \cdot \frac{1}{a_n} f_n.
$$

Telescoping:

$$
  f = c_1 a_1\, S_{1,2}
    + (c_1 a_1 + c_2 a_2)\, S_{2,3}
    + \cdots
    + (c_1 a_1 + \cdots + c_{n-1} a_{n-1})\, S_{n-1,n}
    + \underbrace{(c_1 a_1 + \cdots + c_n a_n)}_{= 0} \cdot \frac{1}{a_n} f_n,
$$

giving the desired result.
