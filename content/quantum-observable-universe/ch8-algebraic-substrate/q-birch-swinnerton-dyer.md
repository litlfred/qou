**Conjecture ($q$-BSD).**
Let $(\mathbf{C}, \theta, G, \mathcal{S})$ be a QOU with substrate
parameter $q$ and Descartes elliptic curve
$\mathcal{E}_q$ ([Descartes elliptic curve](#prop:descartes-elliptic-curve)).
Define the **categorical Mordell--Weil group** as the abelian group of
$\mathbf{1}$-rational points:

$$
\mathcal{E}_q(\mathbf{1})
\;:=\; \mathrm{Hom}_{\mathbf{C}}(\mathbf{1},\, E_q)
$$

where $E_q \in \mathrm{Ob}(\mathbf{C})$ is the object whose fibre
functor image $\tau(E_q) = H^1(\mathcal{E}_q, \mathbb{Z})$ is the
first cohomology of the elliptic fiber, and the group law is induced
by the chord-tangent addition on $\mathcal{E}_q$.  Set
$r_q := \mathrm{rank}\,\mathcal{E}_q(\mathbf{1})$.

**The $q$-deformed $L$-function.**
The Frobenius eigenvalues $\alpha_1, \ldots, \alpha_8$ of the local
$q$-zeta function
([local $q$-zeta](#def:local-q-zeta-function)) act on $H^1(\mathcal{B})$,
the first etale cohomology of Bring's curve.  The elliptic fiber
$\mathcal{E}_q \hookrightarrow \mathcal{B}$ is a genus-$1$ sub-curve,
so the restriction of Frobenius to
$H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ yields a conjugate
pair $\alpha_{\mathcal{E}}, \bar{\alpha}_{\mathcal{E}}$ with
$|\alpha_{\mathcal{E}}| = q^{1/2}$ (by the Hasse--Weil bound).
Define:

$$
L(\mathcal{E}_q, s)
\;:=\; \prod_{\mathfrak{m} \in \mathrm{Spec}(R_q)}
  \frac{1}{1 - \alpha_{\mathcal{E}}(\mathfrak{m})\,
  N(\mathfrak{m})^{-s}
  + N(\mathfrak{m})^{1-2s}}
$$

where the product runs over the maximal ideals of the coordinate ring
$R_q$ of Bring's curve and $N(\mathfrak{m}) = q^{f(\mathfrak{m})}$ is
the norm.  At the central point $s = 1$:

$$
L(\mathcal{E}_q, 1)
\;=\; \prod_{\mathfrak{m}}
  \frac{1}{1 - \alpha_{\mathcal{E}}(\mathfrak{m})/q^{f(\mathfrak{m})}
  + q^{-f(\mathfrak{m})}}
\;=\; \prod_{\mathfrak{m}}
  \frac{|\mathcal{E}_q(\mathbb{F}_{q^f})|}{q^f}.
$$

**The $q$-Tate--Shafarevich group.**
The fibre functor atlas of the QOU forms a $G$-gerbe over the
spectral base.  For each Reeb eigenvalue
$\rho \in \mathrm{Spec}(\xi_q)$, let $\mathbf{C}_\rho$ be the
localization of $\mathbf{C}$ at $\rho$ (the full subcategory of
objects whose spectral support contains $\rho$).  Define the
**$q$-Tate--Shafarevich group** as the kernel of the local-global
map:

$$
\text{\textcyr{Sh}}_q(\mathcal{E}_q)
\;:=\; \ker\!\left(
  H^1_{\otimes}(\mathbf{C},\, E_q)
  \;\longrightarrow\;
  \prod_{\rho \,\in\, \mathrm{Spec}(\xi_q)}
  H^1_{\otimes}(\mathbf{C}_\rho,\, E_q)
\right)
$$

where $H^1_{\otimes}$ denotes the first cohomology of the
monoidal category (classifying torsors under $E_q$ in $\mathbf{C}$).
This measures the failure of the local-global principle at the
$q$-scale: torsors that are trivial at every spectral localization
but globally non-trivial.

**Statement.**
The conjecture has two parts, mirroring the classical BSD:

**(Weak $q$-BSD).**
The order of vanishing of $L(\mathcal{E}_q, s)$ at $s = 1$ equals
the categorical rank:

$$
\mathrm{ord}_{s=1}\, L(\mathcal{E}_q, s) \;=\; r_q
$$

**(Full $q$-BSD).**
The leading Taylor coefficient satisfies a $q$-deformed
Birch--Swinnerton-Dyer formula:

$$
\frac{L^{(r_q)}(\mathcal{E}_q, 1)}{[r_q]_q!}
\;=\;
\frac{\Omega_q \;\cdot\; \mathrm{Reg}_q(\mathcal{E}_q)
  \;\cdot\; |\text{\textcyr{Sh}}_q(\mathcal{E}_q)|
  \;\cdot\; \displaystyle\prod_{\mathfrak{m}} c_{\mathfrak{m}}(q)}
{|\mathcal{E}_q(\mathbf{1})_{\mathrm{tors}}|^2_q}
$$

where:

- $[r_q]_q! = [1]_q \cdot [2]_q \cdots [r_q]_q$ is the $q$-factorial,
  with $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ the $q$-integer from
  the explicit formula
- $\Omega_q$ is the Reeb period (the natural period of
  $\mathcal{E}_q$ in the contact geometry)
- $\mathrm{Reg}_q(\mathcal{E}_q)$ is the **$q$-regulator**: the
  determinant of the $q$-deformed Neron--Tate height pairing
  $\langle\cdot, \cdot\rangle_q$ on
  $\mathcal{E}_q(\mathbf{1}) / \mathrm{tors}$
- $c_{\mathfrak{m}}(q) = [\mathcal{E}_q(\mathbb{F}_{q^f}) :
  \mathcal{E}_q^0(\mathbb{F}_{q^f})]$ is the Tamagawa number at
  $\mathfrak{m}$ (index of the connected component of the identity)
- $|\cdot|_q^2$ denotes the squared $q$-cardinality (using $q$-integers
  for the group order)

**The $q$-height pairing.**
The Neron--Tate height admits a $q$-deformation via the spectral
trace.  For $P, Q \in \mathcal{E}_q(\mathbf{1})$, define:

$$
\langle P, Q \rangle_q
\;:=\; \lim_{n \to \infty}
  \frac{\hat{h}_q([q^n]_q P,\, Q)}{[n]_q^2}
$$

where $\hat{h}_q$ is the naive $q$-Weil height on
$\mathcal{E}_q$ and $[q^n]_q P$ denotes the $q$-integer
multiplication-by-$n$ map on $\mathcal{E}_q$.  The regulator
$\mathrm{Reg}_q = \det(\langle P_i, P_j \rangle_q)$ for a basis
$\{P_i\}$ of $\mathcal{E}_q(\mathbf{1}) / \mathrm{tors}$.

**Categorical content.**
The conjecture is purely categorical in the following sense.  Every
term in the formula is determined by the rigid monoidal category
$\mathbf{C}$ and the Frobenius--Hopf object $A$:

| Classical BSD | $q$-BSD | Categorical source |
|--------------|---------|-------------------|
| $E(\mathbb{Q})$ | $\mathcal{E}_q(\mathbf{1}) = \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q)$ | Unit-object morphisms |
| $L(E, s)$ | $L(\mathcal{E}_q, s)$ | Frobenius on $H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ |
| $\text{\textcyr{Sh}}(E)$ | $\text{\textcyr{Sh}}_q(\mathcal{E}_q)$ | Monoidal $H^1$ localized at Reeb spectrum |
| $\Omega_E$ | $\Omega_q$ | Reeb period of the contact structure |
| $\mathrm{Reg}(E)$ | $\mathrm{Reg}_q(\mathcal{E}_q)$ | $q$-Neron--Tate determinant |
| $|E(\mathbb{Q})_{\mathrm{tors}}|$ | $|\mathcal{E}_q(\mathbf{1})_{\mathrm{tors}}|_q$ | Torsion in $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q)$ |

**Relation to the Riemann hypothesis.**
The weak $q$-BSD and the Riemann hypothesis
([RH](#conj:classical-riemann-hypothesis)) are **independent**
millennium problems at the $q$-scale but **coupled** in the classical
limit.  Both concern the behavior of $L$-functions at special points:

- **RH**: $\zeta(s) = 0 \implies \mathrm{Re}(s) = 1/2$
  (location of zeros of the degree-$0$ $L$-function)
- **BSD**: $\mathrm{ord}_{s=1} L(\mathcal{E}_q, s) = r_q$
  (order of vanishing of the degree-$1$ $L$-function)

At the $q$-scale, the Hasse--Weil bound gives the analogue of RH
unconditionally.  For BSD, the $q$-scale analogue remains conjectural
because the **categorical rank** $r_q$ depends on the global structure
of $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q)$ --- a property not
determined by local Frobenius data alone.

**Classical limit.**
As $q \to 1$ (the adelic assembly), the $q$-BSD formula recovers
the classical Birch--Swinnerton-Dyer conjecture for
$E_1 : y^2 = x^3 + \frac{2}{3}x + \frac{20}{27}$.
The $q$-integers degenerate to ordinary integers
($[n]_q \to n$), the Reeb period $\Omega_q$ collapses to
the real period $\Omega_{E_1}$, and the spectral localizations
assemble into the adelic completions.  The $q$-Tate--Shafarevich
group $\text{\textcyr{Sh}}_q$ maps to the classical
$\text{\textcyr{Sh}}(E_1/\mathbb{Q})$ under the classical
limit functor $\mathcal{L}$.
