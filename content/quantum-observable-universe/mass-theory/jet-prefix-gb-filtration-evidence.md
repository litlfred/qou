**Failed prefix conventions (pre-history).**
Upstream attempts implemented the paper's jet-level prefix formula

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

**Caveat.** A first candidate prefix — the height-based heuristic — fails the test below; the GB-filtration prefix of [prop:jet-prefix-gb-filtration](#prop:jet-prefix-gb-filtration) replaces it.

*A first-pass version uses the heuristic filtration level $\ell(\lambda) = \mathrm{len}(\lambda) - 1$
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

*The "research direction" label on the candidate proposition therefore
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
