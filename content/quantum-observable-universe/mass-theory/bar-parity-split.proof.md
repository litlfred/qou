**Proof.** The mathematical content is the elementary fact that a linear
involution splits its space into a fixed ($+1$) and an anti-fixed ($-1$)
eigenspace; the physics is the identification of those two parities with
binding and $\beta$-decay.

*Algebraic decomposition.* Let $\sigma$ be the bar-involution
([`def:bar-involution`](#def:bar-involution)), a linear map with
$\sigma^2 = \mathrm{id}$. For any element $x$ set
$$
\mathrm{even}(x) = x + \sigma x, \qquad \mathrm{odd}(x) = x - \sigma x .
$$
Then $\mathrm{even}(x)$ is $\sigma$-fixed and $\mathrm{odd}(x)$ is
$\sigma$-anti, using $\sigma^2 = \mathrm{id}$:
$$
\sigma\,\mathrm{even}(x) = \sigma x + \sigma^2 x = \sigma x + x = \mathrm{even}(x),
\qquad
\sigma\,\mathrm{odd}(x) = \sigma x - \sigma^2 x = \sigma x - x = -\,\mathrm{odd}(x),
$$
and the two parts recover the element, $\mathrm{even}(x) + \mathrm{odd}(x) = 2x$.
These three identities are the sorry-free Lean witnesses
`QOU.Mass.evenPart_add_oddPart`, `QOU.Mass.evenPart_fixed`, and
`QOU.Mass.oddPart_anti`.

*Identification of the two parities.* Apply the decomposition to the fibre
Habiro element $F$ that controls the substrate. By
[`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence) the
bar-symmetric ($\cosh$) combination $(q+q^{-1})/2$ is the curvature-free
transport whose trace $\tau = \operatorname{tr} B$ is the binding keystone;
this is exactly the $\sigma$-fixed part. The bar-antisymmetric ($\sinh$)
combination $(q-q^{-1})/2$ is the curvature defect carried by the
$\mathfrak{Q}_\beta$ residue-A / $c_k$ ladder — the $\sigma$-anti part, the
bar-odd Habiro dual of $\alpha_{\mathrm{EM}}$. Since $F$ is a single
element, $\mathrm{even}(F)$ and $\mathrm{odd}(F)$ are not independent
data: fixing either parity (the keystone $\tau$ or the $c_k$ kernel)
determines the other through the shared $F$. Hence binding (the
mass-average) and $\beta$-decay ($\mathfrak{Q}_\beta$) are the two
bar-parities of one bar-graded element, as claimed. $\blacksquare$
