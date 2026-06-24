The Hecke relation $\sigma_0^2 = (q - q^{-1}) \sigma_0
+ \mathbf{1}$ gives:

$$
  \sigma_0^{n+1}
  = \sigma_0 \cdot \sigma_0^n
  = \sigma_0 (a_n \cdot \mathbf{1} + b_n \cdot \sigma_0)
  = a_n  \sigma_0 + b_n  \sigma_0^2
  = a_n  \sigma_0 + b_n ((q - q^{-1}) \sigma_0 + \mathbf{1})
  = b_n \cdot \mathbf{1} + (a_n + h  b_n) \cdot \sigma_0.
$$

Reading off: $a_{n+1} = b_n$ and $b_{n+1} = a_n + h
b_n = b_{n-1} + h b_n$. The initial conditions
$a_0 = 1, b_0 = 0$ (identity) and $a_1 = 0, b_1 = 1$
(single generator) complete the induction. $\square$
