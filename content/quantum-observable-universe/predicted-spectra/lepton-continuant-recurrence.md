The charged lepton tower $T_{2,n}$ for $n = 3, 5, 7$ describes the $e^-, \mu^-, \tau^-$ generations. It possesses a closed-form normal form in $H_2(q) \subset H_3(q)$. A Morgan–Voyce continuant recurrence defines this form.

## Statement

Let $h = q - q^{-1}$ be the Hecke parameter. Let $T_{2,n} = \sigma_0^n$ be the $(2, n)$-torus knot braid in $B_2$. The Gröbner–Shirshov normal form in $H_2(q)$ is:

$$
  \mathrm{NF}(\sigma_0^n)
  = 
  a_n \cdot \mathbf{1}
  + 
  b_n \cdot \sigma_0
$$

The sequences $\{a_n\}$ and $\{b_n\}$ satisfy:

$$
  a_{n+1} = b_n,
  \qquad
  b_{n+1} = h  b_n + b_{n-1},
  \qquad
  b_0 = 0,   b_1 = 1.
$$

The second relation is the Morgan–Voyce continuant. This three-term recurrence features a positive sign on $b_{n-1}$. It contrasts with the Chebyshev polynomials of the second kind $U_n(\cos\varTheta)$, which follow $b_{n+1} = 2\cos\varTheta \cdot b_n - b_{n-1}$.

The net coefficient is the sum of all normal form terms. It is $\mathrm{net}(T_{2,n}) = a_n + b_n$.
