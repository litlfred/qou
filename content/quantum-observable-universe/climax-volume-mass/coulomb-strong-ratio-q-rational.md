**Proposition (Coulomb/strong ratio as a q-rational).**

*For every real $q > 0$ (the substrate-anchor regime,
$\operatorname{Im}(q) = 0$ at the archimedean place),*

$$
  \tanh(\ln q) \;=\; \frac{q - q^{-1}}{q + q^{-1}} \;=\; \frac{q^2 - 1}{q^2 + 1}.
$$

*In particular, the Coulomb/strong ratio from $\operatorname{def:coulomb-charge}$,
which is the analytic value $\tanh(\ln q_0)$, equals the q-rational
expression $(q_0^2 - 1)/(q_0^2 + 1)$ at the substrate anchor — they are the
SAME object, not two different choices.*

## Why this matters

`def:coulomb-charge` introduces the Coulomb-to-strong ratio as $\tanh(\ln q)$.
This proposition records that the analytic and the algebraic forms coincide
identically over real $q > 0$, removing any potential ambiguity about whether
the framework uses a "classical-$\tanh$" vs a "$q$-deformed $\tanh_q$"
realization at the substrate anchor.

The forms are equal because $\exp(\ln q) = q$ for $q > 0$, so

$$
  \tanh(\ln q)
  \;=\; \frac{e^{\ln q} - e^{-\ln q}}{e^{\ln q} + e^{-\ln q}}
  \;=\; \frac{q - q^{-1}}{q + q^{-1}}
  \;=\; \frac{q^2 - 1}{q^2 + 1}
  \quad\text{(multiply numerator and denominator by $q$).}
$$

## Proof (Lean-formalised)

Two-step in `coulomb-strong-ratio-q-rational.lean`:

1. **Algebraic identity** (`qDiffOverSum_eq_qSqDiff_over_qSqSum`): for any real
   $q \ne 0$,

   $$
     \frac{q - q^{-1}}{q + q^{-1}} = \frac{q^2 - 1}{q^2 + 1}.
   $$

   Closed by `field_simp; ring` — pure-algebraic, generic-ring style.

2. **Transcendental bridge** (`Real.tanh_log_eq_qDiffOverSum`): for any real
   $q > 0$,

   $$
     \tanh(\ln q) = \frac{q - q^{-1}}{q + q^{-1}}.
   $$

   Uses `Real.exp_log` and the definitions of `Real.sinh`, `Real.cosh`,
   `Real.tanh` in Mathlib.

The composite (`prop:coulomb-strong-ratio-q-rational`) is the immediate
corollary: $\tanh(\ln q) = (q^2-1)/(q^2+1)$ for $q > 0$.

## q-usage discipline

The identity is stated and proved over $\mathbb{R}_{>0}$ (the archimedean
substrate-anchor regime). The fibre-level q-rational form
$(q-q^{-1})/(q+q^{-1})$ is a Laurent-polynomial ratio over $\mathbb{Z}[q,q^{-1}]$,
realised at $q = q_0 \in \mathbb{R}_{>0}$ where it agrees with the
archimedean $\tanh(\ln q_0)$. There is no $|q| = 1$ step (the identity
involves $q^{-1}$ algebraically, not as conjugation; both $q_0$ and $q_0^{-1}$
are real positive points). Compliant with the `lusztig_q_0_imaginary_part_zero`
invariant. See [CLAUDE.md §7c "Base ring convention"](../../../CLAUDE.md).
