**Remark (Möbius integration limit — algebraic structure).**
*The categorical integration limit for the baryon period is the
Möbius transformation $a: q \mapsto (4-q)/(4q+3)$
([Möbius limit from thimble](#prop:mobius-limit-from-thimble)),
acting on substrate parameter $q$ via its
$\mathrm{PGL}_2(\mathbb{Z})$ matrix:*

$$
  M \;=\; \begin{pmatrix} -1 & 4 \\ 4 & 3 \end{pmatrix},
  \qquad
  M \cdot \binom{q}{1} \;=\; \binom{4 - q}{4q + 3}.
$$

**Matrix invariants.**

| Invariant | Value | Factorisation |
|-----------|-------|---------------|
| $\det M$ | $-19$ | prime, orientation-reversing |
| $\operatorname{tr} M$ | $2$ | |
| Char.\ poly | $\lambda^2 - 2\lambda - 19$ | discriminant $80 = 16 \cdot 5$ |
| Eigenvalues | $1 \pm 2\sqrt{5}$ | $= 4\varphi - 1$ and $3 - 4\varphi$ |
| Fixed points | $\{1/\varphi, -\varphi\}$ | roots of $q^2 + q - 1 = 0$ |

*See
([Möbius golden fixed points](#prop:mobius-golden-fixed-points)) for
the closed-form fixed-point derivation and
([morse-wall-q-moduli](#prop:morse-wall-q-moduli)) for the
substrate-region interpretation of the fixed-point locus as the
golden Morse wall in $q$-moduli.*

**Origin of coefficients $\{-1, 4; 4, 3\}$.**
*From the color-tube cubic
$F(z, c) = c^3 + (4z+1)c^2 + (6z^2+3z+1)c + (4z^3+3z^2+2z+1)$
([color-tube cubic](#rem:color-tube-cubic)):*

- *$\binom{4}{1} = 4$: leading $z$-coefficient of the $c^2$-term.*
- *$\binom{4}{3} = 4$: leading $z$-coefficient of the linear term,
  equivalently $\deg_c F = 3$.*
- *$+3$: constant in the $c$-coefficient $6z^2 + 3z + 1$.*
- *$-1$: orientation sign for the conjugate-paired discriminant
  roots $z_c^\pm$.*

*The Möbius pencil is intrinsic to the binomial structure of the
cubic on Bring's surface — purely $R$-side, no archimedean input.*

**Proximity to the golden degeneration threshold.**
*At substrate $q_0 \approx 1.110$:*

$$
  a(q_0) \;=\; \frac{4 - q_0}{4q_0 + 3} \;\approx\; 0.3884,
  \qquad
  q_{\mathrm{gold}} \;=\; 1/\varphi^2 \;\approx\; 0.3820.
$$

*The fixed-point locus $\{1/\varphi, -\varphi\}$ and the elliptic-
curve degeneration $1/\varphi^2$ are related by squaring:
$(\mathrm{Fix}\,M)^2 = \{1/\varphi^2, \varphi^2\}$
([morse-wall-q-moduli](#prop:morse-wall-q-moduli)).*

**Categorical status.**
*All ingredients — cubic, binomials, Möbius matrix, fixed-point
equation, golden ratio, golden node — are derived from $q$ and the
Descartes axioms over $\mathbb{Z}[q^{\pm 1}, \zeta_5]$
($\sqrt{5} \in \mathbb{Z}[\zeta_5]$ via the Gauss sum). No
empirical input.*

**Open follow-up.**
*Open question #2 ("Why Möbius vs golden node") is **resolved**
([mobius-limit-from-thimble Step 3](#prop:mobius-limit-from-thimble),
[morse-wall-q-moduli](#prop:morse-wall-q-moduli)). Open question #1
("Why product $\prod_k dc_k/dz$ rather than sum") is the
$\mathrm{Alt}^3$ projector — derived in
([baryon product from Alt](#prop:baryon-product-from-alt)).*
