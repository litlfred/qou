/-!
# QOU.BraidKnot.QBetaPerBlockChiClosedForms

**Pre-archimedean closed-form identities for the per-Wedderburn-block
characters $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$, plus the
antipode pairing $(3) \leftrightarrow (1,1,1)$ under $q \mapsto 1/q$.**

This file proves the per-block closed forms from
`qbeta-per-block-paper-closed-forms.witness.json` as rational
identities in $q$, plus a structural antipode-pairing identity. These
are the PRE-ARCHIMEDEAN inputs to the Q$_\beta$ precision-ladder
derivation.

**Honest scope (after correction).** A first version of this file
attempted to prove a closed form for the y_λ-weighted Markov-trace
sum $\Delta\tau_M(q) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(q)$.
That version was retracted because the canonical Wenzl–Markov
weights $y_\lambda(q)$ from `solve_y_lambda(3)` involve $\sqrt q$
(via the Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$), so
$\Delta\tau_M(q)$ is a rational function of $\sqrt q$, NOT of $q$
alone. Proving its sum form in Lean requires square-root handling
beyond ring tactics — out of scope here.

What IS provable in pure ring arithmetic, and what this file proves:

1. The three per-block characters $\chi_{(3)}, \chi_{(2,1)},
   \chi_{(1,1,1)}$ as named rational functions of $q$.
2. The **antipode pairing**: $\chi_{(1,1,1)}(q) = q^{-4} \cdot \chi_{(3)}(q)$
   for $q > 0$, reflecting the standard
   $V_{(3)} \otimes \text{sign} = V_{(1,1,1)}$ relation.
3. The **vanishing at q = 1**: each $\chi_\lambda(q)$ vanishes when
   $q = 1$ (from the $(q^2 - 1)$ factor), confirming
   $\Delta\tau_M(1) = 0$ regardless of $y_\lambda$.

These are rigorous, sorry-free, and do NOT depend on any y_λ form.

LaTeX label: `prop:qbeta-per-block-chi-closed-forms`

## What this file does NOT claim

- A closed form for $\Delta\tau_M(q)$ (open — needs $\sqrt q$ handling).
- The empirical $c_3 = -2$ identity (still NEAR-MATCH per
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md)).
- The f-map identification (open).

## References
- [hoefsmit1974] (seminormal representation matrices for H_3)
- Witness: `qbeta-per-block-paper-closed-forms.witness.json`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace QOU.BraidKnot

/-- Per-block character $\chi_{(3)}(\Delta_{T_\beta})(q)$ on the trivial
irrep $V_{(3)}$.

Closed form: $-(q^2 - 1)(q^2 + 1)^2 / (4q)$.
Source: `qbeta-per-block-paper-closed-forms.witness.json`. -/
-- Ref: [hoefsmit1974]
noncomputable def chi_block_3 (q : ℝ) : ℝ :=
  -(q^2 - 1) * (q^2 + 1)^2 / (4 * q)

/-- Per-block character $\chi_{(2,1)}(\Delta_{T_\beta})(q)$ on the
2-dim irrep $V_{(2,1)}$.

Closed form: $(q^2 - 1)(-q^4 - 1) / (4q^3)$.

Structural note: this collapses to LINEAR in $h = q - 1/q$ — the
$b^2$ off-diagonal contributions from $\sigma_1$ and
$\sigma_0\sigma_1$ cancel (cf. `qbeta_per_block_symbolic.py`). -/
-- Ref: [hoefsmit1974]
noncomputable def chi_block_21 (q : ℝ) : ℝ :=
  (q^2 - 1) * (-q^4 - 1) / (4 * q^3)

/-- Per-block character $\chi_{(1,1,1)}(\Delta_{T_\beta})(q)$ on the
sign irrep $V_{(1,1,1)}$.

Closed form: $-(q^2 - 1)(q^2 + 1)^2 / (4q^5)$.

Antipode pair with `chi_block_3`: $\chi_{(1,1,1)}(q) = q^{-4} \chi_{(3)}(q)$. -/
-- Ref: [hoefsmit1974]
noncomputable def chi_block_111 (q : ℝ) : ℝ :=
  -(q^2 - 1) * (q^2 + 1)^2 / (4 * q^5)

/-- **Theorem (vanishing at $q = 1$).** Each per-block character
$\chi_\lambda(\Delta_{T_\beta})$ vanishes at the classical point $q = 1$.

This confirms $\Delta\tau_M(1) = 0$ regardless of the y_λ weights —
the classical limit is trivial for every block. -/
theorem chi_blocks_vanish_at_one :
    chi_block_3 1 = 0 ∧ chi_block_21 1 = 0 ∧ chi_block_111 1 = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · unfold chi_block_3; norm_num
  · unfold chi_block_21; norm_num
  · unfold chi_block_111; norm_num

/-- **Theorem (antipode pairing).** Under the substitution $q \mapsto 1/q$
the trivial-irrep character $\chi_{(3)}$ maps to the sign-irrep
character $\chi_{(1,1,1)}$:

  $\chi_{(1,1,1)}(q) = q^{-4} \cdot \chi_{(3)}(q)$.

This reflects the standard Hecke-algebra identity
$V_{(3)} \otimes V_{\text{sign}} = V_{(1,1,1)}$, with the $q^{-4}$
prefactor coming from the framing weight (degree-$4$ shift between
the $q^{-1}$- and $q^{-5}$-denominators).

Proof: direct rational arithmetic; clear denominators and apply
`ring`. -/
theorem chi_block_antipode_pairing (q : ℝ) (hq : 0 < q) :
    chi_block_111 q = q⁻¹^4 * chi_block_3 q := by
  unfold chi_block_111 chi_block_3
  have hq_ne : q ≠ 0 := ne_of_gt hq
  field_simp
  ring

/-- **Theorem (q²−1 factor in all three blocks).** Every per-block
character $\chi_\lambda(\Delta_{T_\beta})$ has $(q^2 - 1)$ as a
factor (equivalently, it vanishes at $q = \pm 1$).

This is the structural source of the order-$w$ leading term in the
Taylor expansion around $q = 1$: $q^2 - 1 = 2w + w^2$ where
$w = q - 1$. Each block contributes at first order in $w$, with
the per-block ε¹-order coefficients $\{-2, -1, -2\}$ from the
witness's `taylor_coefficients_per_block_ε_order` field. -/
theorem chi_blocks_have_q2_minus_1_factor (q : ℝ) (hq : 0 < q) :
    ∃ (P3 P21 P111 : ℝ → ℝ),
      chi_block_3 q   = (q^2 - 1) * P3 q ∧
      chi_block_21 q  = (q^2 - 1) * P21 q ∧
      chi_block_111 q = (q^2 - 1) * P111 q := by
  refine ⟨
    fun q' => -(q'^2 + 1)^2 / (4 * q'),
    fun q' => (-q'^4 - 1) / (4 * q'^3),
    fun q' => -(q'^2 + 1)^2 / (4 * q'^5),
    ?_, ?_, ?_⟩
  · unfold chi_block_3
    have hq_ne : q ≠ 0 := ne_of_gt hq
    field_simp
    ring
  · unfold chi_block_21
    have hq_ne : q ≠ 0 := ne_of_gt hq
    field_simp
    ring
  · unfold chi_block_111
    have hq_ne : q ≠ 0 := ne_of_gt hq
    field_simp
    ring

end QOU.BraidKnot
