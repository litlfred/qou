**Proposition (per-block character closed forms, antipode pairing,
vanishing at $q = 1$).**
*For all $q > 0$,*

$$
  \chi_{(3)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q},
$$
$$
  \chi_{(2,1)}(\Delta_{T_\beta})(q)
  \;=\; \frac{(q^2 - 1)(-q^4 - 1)}{4q^3},
$$
$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q^5}.
$$

*Each block vanishes at $q = 1$ (the classical point), and the
antipode pairing*

$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; q^{-4} \cdot \chi_{(3)}(\Delta_{T_\beta})(q)
$$

*holds for all $q > 0$.*

**Proof.** Each closed form is a definitional rational expression
in $q$; the vanishing at $q = 1$ follows from the $(q^2 - 1)$
factor present in all three; the antipode pairing is the rational
identity $-(q^2-1)(q^2+1)^2/(4q^5) = q^{-4} \cdot [-(q^2-1)(q^2+1)^2/(4q)]$,
which simplifies to $1/q^5 = q^{-4} \cdot 1/q$, true. All three
parts are discharged in Lean by `field_simp; ring` after positivity
witnesses for the denominators ($q > 0$). $\square$

## Scope and discipline notes

This proposition establishes the **per-block source data** that
feeds the Q$_\beta$ precision-ladder derivation. Each per-block
character is an exact rational function of $q$, pre-archimedean,
sorry-free.

**What this proposition does NOT establish.**

- A closed form for $\Delta\tau_M(q) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(q)$.
  Why: the canonical Wenzl–Markov weights $y_\lambda(q)$ from
  `markov_weights_symbolic.solve_y_lambda(3)` involve $\sqrt q$ (via
  the Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$) and are NOT
  rational in $q$. A first version of this file attempted to prove
  a closed form for $\Delta\tau_M$ using an incorrect rational guess
  for $y_\lambda$; that version was retracted. The companion probe
  `qbeta_c3_multiblock_recursion_attack.py` does emit a Δτ_M closed
  form, but using a **non-canonical rational surrogate** for $y_\lambda$
  (marked in the script's docstring and witness JSON) — it is
  a NEAR-MATCH diagnostic, not a derivation. Proving the actual
  $\Delta\tau_M$ identity requires square-root handling beyond the
  `ring` tactic and is open.
- The empirical $c_3 \approx -2$ identity. Per the 1ppQ-Q$_\beta$
  ledger ([`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md)),
  $c_3 = -2$ is settled as a NEAR-MATCH with non-zero cross-anchor
  swing, NOT a Taylor-exact closure.
- The f-map identification. The Habiro element scaling map
  $f : \Delta\tau_M(\sqrt u) \mapsto \mathfrak{Q}_\beta(c_3 \text{ at } u^3)$
  remains the keystone of the 1ppQ closure.

**Structural insight from the vanishing-at-1 theorem.** All three
blocks have a $(q^2 - 1)$ factor, so each contributes at order $w$
or higher in the Taylor expansion around $q = 1$, where $w = q - 1$.
The per-block $\varepsilon^1$-order coefficients (witness key
`taylor_coefficients_per_block_*_order`, where `*` is the Greek letter
$\varepsilon$) are
$\{(3): -2, (2,1): -1, (1,1,1): -2\}$. The shared $-2$ at order $w$
between the $(3)$ and $(1,1,1)$ blocks is the algebraic signature
of the antipode pairing — under $q \mapsto 1/q$, the order-$w$
expansion picks up the same leading coefficient up to the $q^{-4}$
framing weight.

## Lean extensions

The accompanying Lean file goes beyond the per-block $\chi_\lambda$
identities above. Four extension sections build the structural
infrastructure that any future $\Delta\tau_M$ closure attack will
consume.

**Extension #1 — surrogate $\Delta\tau_M$ closed form.** Defines
the non-canonical rational surrogate weights $y_\lambda^{\text{surr}}(q)$
(reproducing the per-block dimension structure
$\{q^2, q, 1\}/((1+q)(1+q+q^2))$) and the resulting closed form

$$
  \Delta\tau_M^{\text{surr}}(q) =
  \frac{-q^{11}+q^{10}-2q^9+q^8+q^6-q^5-q^3+2q^2-q+1}{4q^5(q^2+q+1)}.
$$

The Lean theorem `delta_tau_M_surrogate_eq_sum` discharges this
identity sorry-free via `field_simp; ring`. The surrogate is NOT the
canonical Markov trace — the canonical $y_\lambda(q)$ involves
$\sqrt q$ (see Extension #4).

**Extension #2 — Taylor coefficients at $q = 1$.** Locks the
order-0 coefficient as a sorry-free vanishing theorem
($\Delta\tau_M^{\text{surr}}(1) = 0$) and the order-1 coefficient
as a sorry-free `HasDerivAt` theorem
($D \Delta\tau_M^{\text{surr}}(1) = -5/6$, proven by explicit
quotient-rule chaining: $N'(1) = -10$, $D(1) = 12$,
$N(1) = 0$ $\Rightarrow$ derivative $= -10/12$). Higher orders ($5/6$, $-41/9$, ...)
are recorded in the witness JSON; each requires an n-th derivative
computation that is tractable but bulky.

**Extension #3 (skipped).** The "$\Delta\tau_M$ has no $\sqrt q$
atoms" invariant from the witness is vacuous at the Lean type level
once $\Delta\tau_M^{\text{surr}} : \mathbb{R} \to \mathbb{R}$ is built
from polynomial inputs — Lean's type system enforces the rationality
by construction.

**Extension #4 — canonical $\sqrt q$-bearing $\Delta\tau_M$ (conditional
class).** Defines the Markov parameter $z(q) = \sqrt q / (1+q)$ as a
genuine archimedean construction; proves the symmetric identity
$z(q) = 1 / (\sqrt q + 1/\sqrt q)$ sorry-free via
`Real.mul_self_sqrt`. Axiomatises the canonical Wenzl–Markov weights
via `class CanonicalMarkovWeightsH3` with a single dimension-
normalisation axiom (CLAUDE.md §3b-cond pattern). A conditional
`def delta_tau_M_canonical` consumes the class as `[Instance]`;
the conditional theorem `delta_tau_M_canonical_vanish_at_one` is
sorry-free (reduces to `chi_blocks_vanish_at_one`).

**Extension #5 — z-recursion class.** Axiomatises the 3-term
recursion
$4(n+1)\,a_{n+1} + 6n\,a_n + (2n-1)\,a_{n-1} = 0$
on the Taylor coefficients of $z(q)$ at $q = 1$, with seeds
$a_0 = 1/2$, $a_1 = 0$. Proves the `ZRecursionCoeffs.unique`
uniqueness theorem sorry-free via strong induction
(`Nat.strong_induction_on`) with a linear-solve step at each
inductive case. This is the auxiliary z-Taylor recursion;
the GENERAL c_k ladder recursion is the sibling
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
(landed 2026-06-03), which provides the depth-$d$ linear recursion
structure on the ladder coefficients themselves.

**Cross-references to sibling Lean blocks** (landed 2026-06-03 on
main):

- [`QOU.QBeta.CKRecursion.CKRecursion`](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.lean)
  — general depth-$d$ c_k ladder recursion (this PR's
  `ZRecursionCoeffs` is one specific candidate to instantiate).
- [`QOU.QBeta.OverE0ClassicalVanishing.qbeta_over_e0_at_one_eq_zero`](../mass-theory/q-beta-over-e0-classical-vanishing.lean)
  — proves $S(q) = \mathfrak{Q}_\beta/E_0$ vanishes at $q = 1$ (different
  upstream object from `delta_tau_M_canonical`, but same
  classical-point vanishing structure).

**Sorry tally: zero.** All theorems are sorry-free, locally verified
against `lean v4.24.0` + Mathlib commit
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The three originally-
deferred sorries (derivative-at-$q=1$, Markov-parameter symmetric
form, z-recursion uniqueness) were each subsequently discharged once
local Lean verification became available.

## Cross-references

- The probe computation:
  [`computations/qbeta/qbeta_c3_multiblock_recursion_attack.py`](../../../computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
  (witness `qbeta-c3-multiblock-recursion-attack.witness.json`).
- The pre-archimedean recursion for $z$: 
  [`computations/qbeta/qbeta_prearchimedean_z_recursion.py`](../../../computations/qbeta/qbeta_prearchimedean_z_recursion.py).
- The downstream c$_k$ conjectures:
  [`conj:qbeta-c-k-closed-forms`](#conj:qbeta-c-k-closed-forms)
  (axiomatised; conditional on the Habiro element identification).
- The 1ppQ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
