**Proposition (candidate: GB-filtration-indexed prefix; conditional on [`conj:confinement-grading-correspondence`](#conj:confinement-grading-correspondence)).**
*Define the **Gröbner–Shirshov-filtered prefix** $\beta_k^{\mathrm{GS}}$
of an atomic braid word $T_w \in H_{3A}(q)$ as the projection of
$T_w$ onto the filtration stratum*

$$
  \beta_k^{\mathrm{GS}}
  \;:=\;
  \sigma_{k-3}\bigl(T_w\bigr)
  \;\in\;
  J^{k-3}(q) / J^{k-2}(q),
$$

*where $J^\ell(q)$ is the confinement filtration
([confinement level](#def:confinement-level)) and $\sigma_\ell$
is the symbol map to the $\ell$-th graded piece. The jet-level
prefix formula then reads*

$$
  a_k(\beta_k^{\mathrm{GS}})
  \;=\;
  \frac{\mathrm{tr}_M^{[\ell]}\bigl(\beta_k^{\mathrm{GS}}\bigr)}
       {\sum_\lambda w_\lambda\,\dim\mathrm{Res}^{H_k}_{H_3}(V_\lambda)},
$$

*where $\mathrm{tr}_M^{[\ell]}$ is the Markov trace restricted to
the level-$\ell$ graded piece.*

**GB filtration versus geometric cutoffs.**
*The geometric cutoffs (nucleon count, strand count, generator index)
do not respect the Hecke-algebra structure. The GB filtration
is **algebraically** defined by the knot-operator energies
$E_\ell(q)$, so the prefix $\beta_k^{\mathrm{GS}}$ respects the
Hecke-algebra structure. Each filtration level has a well-defined
$\dim\mathrm{Res}^{H_k}_{H_3}$ because the graded piece
$J^\ell/J^{\ell+1}$ is itself a semisimple $H_3$-bimodule.*

**KLR grading interpretation.**
*Under the
[confinement–grading correspondence](#conj:confinement-grading-correspondence),
the confinement level $\ell(K, q)$ of a closed braid $K$ coincides
with the top non-zero $\mathbb{Z}$-grading degree of its KLR-module
lift $\mathfrak{M}_K$ on the cyclotomic KLR algebra; the symbol
$\sigma_\ell(T_w) \in J^\ell / J^{\ell+1}$ is that top graded
component. Truncating $T_w$ at jet order $k$ therefore keeps the
graded components of $\mathfrak{M}_K$ in degrees $\leq k$ of the KLR complex;
the residual error $E(k)$ is the homological remainder supported in
degrees $k < d \leq \ell(K, q)$, and the truncation is exact
precisely when $k \geq \ell(K, q)$. The candidate prefix
$\beta_k^{\mathrm{GS}}$ inherits its restriction multiplicities
$\dim\mathrm{Res}^{H_k}_{H_3}$ from this graded structure.*

**Predictions of the GB-filtration prefix.**

1. *At level $0$: $\beta_0^{\mathrm{GS}} = $ descended Markov-trace
 part. $a_0 = 1$ by definition (the ratio is $\mathrm{tr}_M/\mathrm{tr}_M = 1$).*
2. *At level $\ell \geq 1$: $\beta_\ell^{\mathrm{GS}}$ picks up the
 corresponding root-of-unity residue
 ([GB residue spectral sum](#prop:gb-residue-spectral-sum)).*
3. *Product $\prod_\ell a_\ell = 1 + $ (corrections from higher
 strata) — matches the "near 1" shape expected.*
