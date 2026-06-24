Direct expansion:

$$
  (x^2 - x - 1)(x^2 + x - 1)
  = x^4 + x^3 - x^2 - x^3 - x^2 + x - x^2 - x + 1
  = x^4 - 3x^2 + 1.
$$

The two quadratic factors are the minimal polynomials of $\varphi$
and $1/\varphi$ over $\mathbb{Q}$ respectively, so their roots are
$Q_+$ and $Q_-$.

For $\tau \in \mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q})$ acting by $\sqrt{5}
\mapsto -\sqrt{5}$:

$$
  \tau(\varphi) = \tau\!\left(\tfrac{1 + \sqrt{5}}{2}\right)
   =  \tfrac{1 - \sqrt{5}}{2}  =  -1/\varphi,
$$

$$
  \tau(1/\varphi) = \tau\!\left(\tfrac{-1 + \sqrt{5}}{2}\right)
   =  \tfrac{-1 - \sqrt{5}}{2}  =  -\varphi.
$$

Hence $Q_+$ and $Q_-$ are the two Galois orbits.

For the bar involution: $\iota(\varphi) = 1/\varphi \in Q_-$, so
$\iota$ does not preserve $Q_+$. It exchanges $Q_+$ and $Q_-$
because $\varphi \cdot 1/\varphi = 1$ and $-\varphi \cdot (-1/\varphi)
= 1$, so $\iota(\varphi) = 1/\varphi$, $\iota(-\varphi) = -1/\varphi$.

The product action of $G$ on $Q$ has orbit $G \cdot \varphi = Q$:

| element of $G$ | image of $\varphi$ |
|----------------|-------------------|
| $(\mathrm{id}, \mathrm{id})$ | $\varphi$ |
| $(\tau, \mathrm{id})$ | $-1/\varphi$ |
| $(\mathrm{id}, \iota)$ | $1/\varphi$ |
| $(\tau, \iota)$ | $-\varphi$ |

All four elements appear; $|G| = 4 = |Q|$, so the action is 
transitive.
$\qquad\blacksquare$
