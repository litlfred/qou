The charged lepton tower $T_{2,n}$ ($n = 3, 5, 7$ for $e^-,
\mu^-, \tau^-$) has a closed-form normal form in $H_2(q) \subset
H_3(q)$ given by a **Morgan–Voyce continuant recurrence**.

## Statement

Let $h = q - q^{-1}$ be the Hecke parameter and
$T_{2,n} = \sigma_0^n$ the $(2, n)$-torus knot braid in $B_2$.
The Gröbner--Shirshov normal form in $H_2(q)$ is

$$
  \mathrm{NF}(\sigma_0^n)
  = 
  a_n \cdot \mathbf{1}
  + 
  b_n \cdot \sigma_0
$$

where the sequences $\{a_n\}$, $\{b_n\}$ satisfy:

$$
  a_{n+1} = b_n,
  \qquad
  b_{n+1} = h  b_n + b_{n-1},
  \qquad
  b_0 = 0,   b_1 = 1.
$$

The second relation is the **Morgan–Voyce continuant** — a
three-term recurrence with positive sign on $b_{n-1}$, in
contrast to the Chebyshev polynomials of the second kind
$U_n(\cos\varTheta)$ which have $b_{n+1} = 2\cos\varTheta \cdot
b_n - b_{n-1}$.

The **net coefficient** (sum of all NF terms) is
$\mathrm{net}(T_{2,n}) = a_n + b_n$.
