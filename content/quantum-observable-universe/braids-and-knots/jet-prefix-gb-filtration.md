Upstream `pure_hecke_binding.py` and `pure_hecke_binding_prefix.py`
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

| convention | D | T | ³He | ⁴He |
|---|---|---|---|---|
| nucleon-cumulative ($A$-step prefix) | $-65\%$ | $-91\%$ | $-91\%$ | degenerate |
| strand-cumulative (first $k$ strands) | $-99\%$ | $-99\%$ | $-99\%$ | degenerate |
| generator-bounded (gen $\leq k-2$) | $3.1 \times 10^{-6}$ (essentially zero) | $\sim 0$ | $\sim 0$ | $\sim 0$ |

*All three converge to zero rather than a "correction near 1",
suggesting a structural mis-identification of the prefix.*

**Proposition (candidate: GB-filtration-indexed prefix).**
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
is the symbol map to the $\ell$-th graded piece.  The jet-level
prefix formula then reads*

$$
  a_k(\beta_k^{\mathrm{GS}})
  \;=\;
  \frac{\mathrm{tr}_M^{[\ell]}\bigl(\beta_k^{\mathrm{GS}}\bigr)}
       {\sum_\lambda w_\lambda\,\dim\mathrm{Res}^{H_k}_{H_3}(V_\lambda)},
$$

*where $\mathrm{tr}_M^{[\ell]}$ is the Markov trace restricted to
the level-$\ell$ graded piece.*

**Why GB filtration and not geometric cutoffs.**
*The three failed conventions all use geometric cutoffs
(nucleon count, strand count, generator index).  The GB filtration
is **algebraically** defined by the knot-operator energies
$E_\ell(q)$, so the prefix $\beta_k^{\mathrm{GS}}$ respects the
Hecke-algebra structure.  Each filtration level has a well-defined
$\dim\mathrm{Res}^{H_k}_{H_3}$ because the graded piece
$J^\ell/J^{\ell+1}$ is itself a semisimple $H_3$-bimodule.*

**Predictions of the GB-filtration prefix.**

1. *At level $0$: $\beta_0^{\mathrm{GS}} = $ descended Markov-trace
   part.  $a_0 = 1$ trivially (the ratio is $\mathrm{tr}_M/\mathrm{tr}_M = 1$).*
2. *At level $\ell \geq 1$: $\beta_\ell^{\mathrm{GS}}$ picks up the
   corresponding root-of-unity residue
   ([GB residue spectral sum](#prop:gb-residue-spectral-sum)).*
3. *Product $\prod_\ell a_\ell = 1 + $ (corrections from higher
   strata) — matches the "near 1" shape expected.*

**Status: candidate, not verified.**
*This proposition proposes the GB-filtration indexed prefix as the
**algebraically-natural** candidate to replace the three failed
geometric conventions.  A computational verification requires
implementing the symbol map $\sigma_\ell$ and the graded Markov
trace $\mathrm{tr}_M^{[\ell]}$ numerically.  This is significantly
heavier than the upstream attempts (needs filtration-level
projection on each atomic braid word at each $k$).  The proposition
is a **research direction**, not a proof; its value is in flagging
the geometric-cutoff conventions as structurally wrong and
pointing to the algebraic alternative.*

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
  ([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients))
  give the A≥3 specialisation that the prefix formula must
  reproduce.*

**Open questions.**

1. *Is the GB-filtration-indexed prefix the **unique** algebraically-
   natural choice, or are there other filtration-based options?*
2. *Does the product formula $a = \prod_k a_k$ converge for all $A$?*
3. *What is the numerical verification cost for $A = 3, 4$?*
4. *Does the jet-level prefix recover paper's BW+chirality at
   $A = 3$?*
