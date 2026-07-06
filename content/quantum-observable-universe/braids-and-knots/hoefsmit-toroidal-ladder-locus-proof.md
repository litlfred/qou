*Proof.* Expanding the ladder factor,

$$
(d + \alpha - \beta)(d + \alpha + \beta + 1)
= d^2 + (2\alpha + 1)\, d + (\alpha - \beta)(\alpha + \beta + 1).
$$

Equality with $d^2 - 1$ for all $d$ matches coefficients: the linear
coefficient gives $2\alpha + 1 = 0$, so $\alpha = -\tfrac{1}{2}$
(characteristic zero); the constant coefficient then gives

$$
\bigl(-\tfrac{1}{2} - \beta\bigr)\bigl(\tfrac{1}{2} + \beta\bigr) = -1
\;\Longleftrightarrow\;
\bigl(\beta + \tfrac{1}{2}\bigr)^2 = 1
\;\Longleftrightarrow\;
\bigl(\beta - \tfrac{1}{2}\bigr)\bigl(\beta + \tfrac{3}{2}\bigr) = 0,
$$

so $\beta = \tfrac{1}{2}$ or $\beta = -\tfrac{3}{2}$. In a field the
product vanishes only if a factor does, giving the two stated solutions,
which are exchanged by the Legendre reflection $\mu \mapsto -\mu - 1$
about $\mu = -\tfrac{1}{2}$. The validity direction is the polynomial
identity $(d - 1)(d + 1) = d^2 - 1$. $\blacksquare$

The Lean formalization (`toroidal_locus_forced`,
`toroidal_locus_valid`) carries exactly this argument over a generic
field of characteristic zero via `linear_combination`: the linear
coefficient is extracted as $\tfrac{1}{4}\bigl(h(1) - h(-1)\bigr)$ and
the constant one as $-h(0)$.
