**Remark.**
*Each residue
$\operatorname{Res}_{q=\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\,\ell}(T_w)]$
in the spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) has a
gauge-theoretic interpretation: it is the **holonomy of the braid
loop $T_w$ around the singular fibre** at $q = \zeta_\ell$.*

**Gauge-theoretic picture.**
*Specialise the indeterminate $q$ of
$R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$ via a ring map
$\iota \colon R \to \mathbb{C}$, viewing $q$ as a parameter labelling
the family of Hecke algebras $\{H_n(\mathbb{C}, q)\}_{q \in \mathbb{C}^\times}$.  The map
$q \mapsto H_n(\mathbb{C}, q)$ is a flat holomorphic bundle of algebras over
$\mathbb{C}^\times \setminus \{\zeta_\ell\}$, with **singular
fibres** at each $\zeta_\ell$ where the algebra fails to be
semisimple.  A braid word $T_w$ defines a section of this bundle:*

- *On the regular locus it picks out a specific element
  $T_w(q) \in H_n(\mathbb{C}, q)$.*
- *Around a singular fibre $\zeta_\ell$, the section acquires
  **monodromy** encoded by how the Gröbner–Shirshov reduction of
  $T_w$ would change if $q$ were analytically continued once
  around $\zeta_\ell$.*

*The residue at $\zeta_\ell$ is precisely this monodromy, paired
with the Markov trace.  In the notation of
([rho, $S^3$ holonomy](#rem:rho-s3-holonomy-exposition)), the
residue is the $q$-deformed analogue of the Chern–Simons holonomy
of a Wilson loop in $S^3$ around an obstruction divisor.*

**Connection to Reshetikhin–Turaev.**
*At $q = \zeta_\ell$ the category of representations of $H_n(\mathbb{C}, q)$
truncates to a modular tensor category, and the Markov trace
becomes the Reshetikhin–Turaev invariant evaluated on the closed
braid. The residue $\operatorname{Res}_{q=\zeta_\ell}$ extracts
precisely this RT invariant from the Laurent expansion of
$\mathrm{tr}_M(T_w, q)$ at the pole. In the Habiro framework
([Habiro completion](#prop:full-pole-structure-mass-trace)) the
RT invariants assemble as the cyclotomic coefficients $a_m$ of
the Habiro expansion of $\mathrm{tr}_M(T_w)$: each $a_m$ encodes
the contribution of the $m$-th cyclotomic stratum, with the
total mass functional
$\mathfrak{m}(K, q_0) = |\mathrm{tr}_M(T_w, q_0)|$ realised as
the Habiro evaluation at $q_0$, not as a complex-analytic
partial-fraction sum.*

**Why the empirical regular-value tower misses this.**
*The regular-value formula
([mass endomorphism tower](#prop:mass-endomorphism-tower))
evaluates $\Phi_{q_0}$ on $|\hat V_i^{\mathrm{full}}|$ without
knowledge of where each $\hat V_i$ sits in the confinement
filtration.  For braids occupying deep filtration strata
(confinement level $\ell(K, q_0) \geq 2$), the regular-value
expansion converges too slowly and the residues at $\zeta_\ell$
for $\ell \geq 2$ supply the missing contributions.*

**Exceptional divisor and the singular fibre.**
*The singular fibre at $\zeta_\ell$ is the categorical shadow of
the $\ell$-th exceptional divisor in the brane tower
([exceptional divisor](#def:exceptional-divisor)): blowing up
the singular locus resolves the degeneration of the Hecke
eigenvalues $(q, -q^{-1})$ at $\zeta_\ell$, and the holonomy of
$T_w$ around the resulting exceptional $\mathbb{P}^1$-fibre
encodes the residue.  In this sense the spectral sum recovers
the brane-tower contribution algebraically, **without** invoking
the external geometry of the blow-up: the filtration on $H_n(\mathbb{C}, q)$
is enough.*

**Example: trefoil at $q_0 \approx 1.11$.**
*The trefoil knot has confinement level $\ell = 1$ at $q_0$.
Only $\zeta_1 = 1$ contributes a nonzero residue, and
$|q_0 - 1| \approx 0.11$ is small — so the level-$1$ residue is
a dominant correction to the descended Markov trace.  This is
consistent with the observed breakdown of the
$\hat V_i^{\mathrm{full}}$-product approximation when the
descended term is itself small (confer the $\lesssim 1\%$ binding
residuals on $^2$H, $^3$H, and the degradation toward $^{40}$Ca
where $\ell(K, q_0)$ grows).*
