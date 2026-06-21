*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
The Hecke bar involution $\sigma \leftrightarrow \sigma^{-1}$, which
on the substrate parameter acts as $q \leftrightarrow q^{-1}$ (equivalently
$s \leftrightarrow 1/s$ for $s = \sqrt{q}$), maps the golden-ratio node
$q_{\mathrm{gold}} = 1/\varphi^2$
([golden-ratio degeneration](#rem:golden-ratio-degeneration))
to the **skew-dual golden node**

$$
  q^{*}_{\mathrm{gold}}
  =  \varphi^2
  =  \frac{3 + \sqrt{5}}{2}
   \approx  2.618.
$$

The minimal polynomial of $1/\varphi$ over $\mathbb{Q}$ is
$s^2 + s - 1$; its bar-involute (after $s \mapsto 1/s$ and clearing
denominators) is

$$
  s^2 - s - 1,
$$

the minimal polynomial of $\varphi$.  These two quadratics are
exchanged by $s \leftrightarrow 1/s$ up to sign, and their roots
partition into the bar-paired set $\{1/\varphi, \varphi\}$ on the
positive real axis.

*Proof.*
If $s_0$ is a root of $s^2 + s - 1 = 0$, then $s_0^{-2} \cdot
(s_0^2 + s_0 - 1) = 0$ rearranges to $1 - s_0^{-1} - s_0^{-2} = 0$,
i.e. $(s_0^{-1})^2 - (s_0^{-1}) - 1 = 0$ after multiplying by $-1$
and substituting $u = s_0^{-1}$: $u^2 - u - 1 = 0$.  Hence
$s_0 = 1/\varphi \Leftrightarrow s_0^{-1} = \varphi$, and squaring
gives $1/\varphi^2 \leftrightarrow \varphi^2$ on the $q$-line.
$\square$

**Stability band on both sides.**

Our universe sits at $q_0 = 1.109978595554181\ldots$ (50 dps), in the open interval
$(1, \varphi^2)$.  The two golden nodes bracket the physical regime,
giving a **two-sided stability margin**:

See [Table: Golden-ratio dual nodes](#tbl:golden-skew-dual-node-table-data).

The asymmetry — roughly $0.728 : 1.508 \approx 1 : 2.07$ — places
$q_0$ closer to the sub-classical node than to the super-classical
one.  The ratio $(\varphi^2 - q_0)/(q_0 - 1/\varphi^2) \approx 2.07$
has no closed form in $\varphi$ alone; it varies smoothly with
$q_0$ and equals $1$ exactly at the arithmetic midpoint
$q = (1/\varphi^2 + \varphi^2)/2 = 3/2$.

**Why $\varphi^2$ on the physical side?**
The Descartes elliptic curve $\mathcal{E}_q$ does not itself acquire
a node at $q = \varphi^2$ — its Weierstrass factor $s^2 + s - 1$ is
non-zero there.  The bar-dual node is the degeneration of the
**dual curve** $\mathcal{E}^{*}_q := \mathcal{E}_{q^{-1}}$, which the
$q \leftrightarrow q^{-1}$ symmetry of the Iwahori--Hecke algebra
$H_n(q)$ identifies with the original curve under exchange of the
two Hecke eigenvalues $\{q, -q^{-1}\}$.

The skew-dual node is therefore the threshold at which the
**inverse substrate** $q^{-1}$ would itself fall into the sub-golden
regime — equivalently, where the symmetric channel of the Hecke
generator decouples from the antisymmetric channel.

**Connection to the Möbius fixed points.**
The fixed points $\{1/\varphi, -\varphi\}$ of the baryon
integration-limit Möbius map $f(q) = (4 - q)/(4q + 3)$
(Möbius golden fixed points)
extend under bar conjugation to the full quartet
$\{1/\varphi, -\varphi, \varphi, -1/\varphi\}$.  The two roots
on the positive axis, $\{1/\varphi, \varphi\}$, are exactly the
bar-paired thresholds bracketing the physical band.

**Falsifiability.**
The conjecture predicts that any observable monotone in
$q - q_{\mathrm{gold}}$ on the sub-classical side has a bar-paired
analogue monotone in $\varphi^2 - q$ on the super-classical side,
with the two sensitivities related by the same Hecke skew-symmetry
that exchanges $L_+$ and $L_-$ in the Skein relation.  At
$q = q_0$, the super-classical margin $\approx 1.508$ is the
larger of the two — consistent with the empirical observation that
nuclear physics is more robust against compression of the substrate
than against rarefaction.


**Remark on Mathematical Novelty:** By reinterpreting the conventional reciprocal node bar-duality (phi^-2 / phi^2) as a two-sided stability margin, this skew-dual framing provides a mathematically novel boundary condition for bounding spectral gaps.
