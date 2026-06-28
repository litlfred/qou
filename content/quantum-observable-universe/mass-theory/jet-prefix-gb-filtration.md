Upstream the formal derivation and the formal derivation
(branch `claude/1ppb-handover-docs-cyFlQ`) attempted to implement
the paper's jet-level prefix formula

$$
  a_k(\beta_k)
  \;=\;
  \frac{\sum_\lambda w_\lambda\, \chi_\lambda^{(k)}(\beta_k)}
       {\sum_\lambda w_\lambda\,\dim\mathrm{Res}^{H_k}_{H_3}(V_\lambda)},
  \qquad
  a(Z, N)
  \;=\;
  \prod_{k = 3}^{3A} a_k(\beta_k),
$$

where $\beta_k$ is the **prefix** of the atomic braid word at Hecke
level $k$, and $\mathrm{Res}^{H_k}_{H_3}$ is the restriction functor.
Three prefix conventions were tested — all failed to reproduce AME
bindings:

| convention | D | T | ${}^{3}\mathrm{He}$ | ${}^{4}\mathrm{He}$ |
|---|---|---|---|---|
| nucleon-cumulative ($A$-step prefix) | $-65\%$ | $-91\%$ | $-91\%$ | degenerate |
| strand-cumulative (first $k$ strands) | $-99\%$ | $-99\%$ | $-99\%$ | degenerate |
| generator-bounded (gen $\leq k-2$) | $3.1 \times 10^{-6}$ (essentially zero) | $\sim 0$ | $\sim 0$ | $\sim 0$ |

*All three converge to zero rather than a "correction near 1",
suggesting a structural mis-identification of the prefix.*

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
*The three failed conventions all use geometric cutoffs
(nucleon count, strand count, generator index). The GB filtration
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

**Caveat.** A first candidate prefix — the height-based heuristic — fails the test below; the argument that follows replaces it.

*formalism the formal derivation implements a first-pass version
using the heuristic filtration level $\ell(\lambda) = \mathrm{len}(\lambda) - 1$
(diagram height minus one) to group partitions. Results:*

| isotope | $\prod_k a_k$ (free) | $\prod_k a_k$ (atom) |
|---|---|---|
| $\mathfrak{p}$ | $+0.924$ | — |
| $\mathfrak{n}$ | $-0.647$ | — |
| D | $+0.015$ | $-3.9 \times 10^{-4}$ |
| T | $-2 \times 10^{-6}$ | $+1.5 \times 10^{-11}$ |
| ${}^{3}\mathrm{He}$ | $-7 \times 10^{-7}$ | $-1.8 \times 10^{-11}$ |

*Products collapse rapidly with $A$, have arbitrary signs, and
differ from the expected "correction near 1" shape. This
heuristic filtration level does not reproduce Term 6.*

*Four candidate prefix conventions have now been tested (three
upstream + this one), all fail. This is **structural evidence**
that the jet-level prefix formula — as stated in the
paper — is either wrong or requires a different filtration
definition entirely. Possibilities:*

1. *The filtration index must use the **true confinement-level**
 $\ell(K, q)$ (energy-sorted $J^\bullet$), not a combinatorial
 proxy. Implementing this requires solving the LP at each
 $k$, a substantially heavier computation.*
2. *The prefix formula should use **restriction** $\mathrm{Res}^{H_k}_{H_3}$
 in a different basis (not classical dim but $\dim_q$).*
3. *Term 6 may not be a multiplicative prefix at all, but an
 additive correction in the spectral-sequence
 ([$E_\infty$ page identifications](#prop:e-infinity-page-identifications))
 from $E_\infty^{\ell \geq 3, *}$ pages directly.*

*The "research direction" label on this proposition therefore
upgrades: the prefix formula requires **structural reformulation**,
not just better implementation.*

**Relation to existing blocks.**

- *The GB residue spectral sum
 ([GB residue spectral sum](#prop:gb-residue-spectral-sum)) is
 the **output** of the prefix formula: the sum $\sum_\ell
  a_\ell$ of level contributions.*
- *The Schur–Weyl decomposition
 ([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition))
 is the **full** Markov trace; the prefix formula computes it
 level-by-level.*
- *Paper's figure-eight BW coefficients
 ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
 give the A$\ge$3 specialisation that the prefix formula must
 reproduce.*

**Open questions.**

1. *Is the GB-filtration-indexed prefix the **unique** algebraically-
 natural choice, or are there other filtration-based options?*
2. *Does the product formula $a = \prod_k a_k$ converge for all $A$?*
3. *What is the canonical structural verification cost for $A = 3, 4$?*
4. *Does the jet-level prefix recover paper's BW+chirality at
 $A = 3$?*
