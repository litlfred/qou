/-
Copyright (c) 2026 litlfred. All rights reserved.

# Universal Habiro closure for m_μ + Q_β c_3 — categorical scaffolding

This file scaffolds the empirical L2 closures of both m_μ (R9 + V9
two-rung structure) and Q_β c_3 (3-rung structure) discovered in
PR #1781. The headline finding: both observables close via Habiro-
element structures that share the **`[3]_q / 25 = [3]_q / 5²`**
universal building block.

## Empirical closures (PR #1781)

| Observable | Closure formula | L2 miss |
|---|---|---|
| m_μ | `m_e · Vol(4_1) / ℏ_q² · (1 - δ_R9 - δ_V9)` | 0.036× |
| Q_β c_3 | `-(q² + q⁻²) · (1 + ℏ_q·[3]_q/25 + ℏ_q³/[2]_q)` | 2.65 ppm |

with
  - `δ_R9 = ℏ_q⁶ · q / 5`        (m_μ rung 1, h³ jet)
  - `δ_V9 = ℏ_q⁸ · [3]_q / 25`   (m_μ rung 2, h⁴ jet)

The `[3]_q / 25` factor appears in BOTH `δ_V9` (m_μ V9 rung 2) and the
inner correction of Q_β c_3 (rung 1) at very different jet orders.

## Status — NEAR-MATCH tier (per qbeta-style ladder discipline)

Each closure is empirically validated against the L2 100× target but
NOT YET DERIVED from categorical first principles. Promotion from
`near-match` → `derived` requires the 5 theorems below.

All 13 theorems are **proved here**: Theorems 1-3 establish the
structural identities (`ring` / `rfl`); Theorems 4-5 establish the
formal-existence claims (explicit-witness, `rfl`); Theorems 6-9
extend to cross-observable and classical-limit identities;
Theorems 10-13 formalize the general T(2,n) framing-ladder family.
The DEEP categorical derivations (Wenzl-Hoefsmit Markov-trace
operator, cinquefoil framing) remain conjectural and are captured
as opaque marker fields in `UniversalHabiroStructure` (no class
instance constructed).

## Cross-refs

- Empirical witnesses: `mmu-r9-two-rung-v2-probe.witness.json`,
  `qbeta-c3-three-rung-probe.witness.json`
- Synthesis audit: `docs/audits/2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`
- Q_β parallel: `QBetaCategoricalPrecisionLadder.lean`
- L2 dashboard: `per-observable-100x-status.witness.json`

-/

import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.BraidKnot.QBetaCategoricalPrecisionLadder

open Real

namespace QOU.BraidKnot

/-! ## Building blocks -/

/-- Quantum integer `[n]_q = (q^n - q^(-n)) / (q - q^(-1))`. -/
noncomputable def quantumInt (n : ℕ) (q : ℝ) : ℝ :=
  (q ^ (n : ℤ) - q ^ (-(n : ℤ))) / (q - q⁻¹)

/-- Substrate `ℏ_q = (q - 1) / q`, reused from
`QBetaCategoricalPrecisionLadder` via `hbarQ'`. -/
noncomputable def hbarQ (q : ℝ) : ℝ := hbarQ' q

/-- **Universal Habiro building block** `T_{25}(q) = [3]_q / 25 = [3]_q / 5²`.

Empirically discovered in PR #1781 to appear in BOTH m_μ V9 (rung 2,
h⁴ jet) and Q_β c_3 (rung 1, h¹ jet). The `5²` denominator parallels
the m_μ R9 `/5` denominator. Conjectural origin: T(2,5) cinquefoil
framing factor of the substrate (see Theorem 5 below). -/
noncomputable def habiroT25 (q : ℝ) : ℝ := quantumInt 3 q / 25

/-! ## m_μ closure components (R9 + V9) -/

/-- m_μ R9 first-rung correction: `δ_R9 = ℏ_q⁶ · q / 5`. NEAR-MATCH form. -/
noncomputable def delta_R9 (q : ℝ) : ℝ :=
  hbarQ q ^ 6 * q / 5

/-- m_μ V9 second-rung correction: `δ_V9 = ℏ_q⁸ · [3]_q / 25`. NEAR-MATCH form. -/
noncomputable def delta_V9 (q : ℝ) : ℝ :=
  hbarQ q ^ 8 * quantumInt 3 q / 25

/-- Total m_μ categorical correction. -/
noncomputable def delta_total_mmu (q : ℝ) : ℝ :=
  delta_R9 q + delta_V9 q

/-- m_μ prediction with R9 + V9 correction. -/
noncomputable def m_mu_R9_V9 (q m_e vol_4_1 : ℝ) : ℝ :=
  m_e * vol_4_1 / hbarQ q ^ 2 * (1 - delta_total_mmu q)

/-! ## Q_β c_3 closure components -/

/-- Categorical base for Q_β c_3: `-(q² + q⁻²)`. Empirically identified
in PR #1773's 15-candidate single-formula re-run as the best base
(9,109 ppm without further correction). -/
noncomputable def qbetaC3Base (q : ℝ) : ℝ := -(q ^ 2 + q⁻¹ ^ 2)

/-- Q_β c_3 first rung: `ℏ_q · [3]_q / 25 = ℏ_q · T_{25}(q)`. -/
noncomputable def qbetaC3Rung1 (q : ℝ) : ℝ :=
  hbarQ q * quantumInt 3 q / 25

/-- Q_β c_3 second rung (T7 cleanest): `ℏ_q³ / [2]_q`. Pure quantum-
integer ratio, no empirical coefficient. -/
noncomputable def qbetaC3Rung2 (q : ℝ) : ℝ :=
  hbarQ q ^ 3 / quantumInt 2 q

/-- Q_β c_3 3-rung closure prediction. Closes 2.65 ppm at proton-pinned q₀. -/
noncomputable def qbetaC3Closure (q : ℝ) : ℝ :=
  qbetaC3Base q * (1 + qbetaC3Rung1 q + qbetaC3Rung2 q)

/-! ## Promotion theorems (Theorems 1-5)

Five theorems gating the `near-match` → `derived` promotion.
Theorems 1-3 establish the structural identities by ring algebra.
Theorems 4-5 establish the formal-existence claims via explicit
witnesses; the DEEP categorical derivations are captured as opaque
marker fields in `UniversalHabiroStructure` below (no instance). -/

/-- **Theorem 1 (proved).** The m_μ V9 rung factors through the
universal Habiro building block `T_{25}(q) = [3]_q / 25`:

  `δ_V9(q) = ℏ_q⁸ · T_{25}(q)`

This makes the shared Habiro factor explicit in the m_μ closure. -/
theorem delta_V9_factors_via_habiroT25 (q : ℝ) :
    delta_V9 q = hbarQ q ^ 8 * habiroT25 q := by
  unfold delta_V9 habiroT25
  ring

/-- **Theorem 2 (proved).** The Q_β c_3 rung 1 factors through the
SAME universal Habiro building block `T_{25}(q) = [3]_q / 25`:

  `qbetaC3Rung1(q) = ℏ_q · T_{25}(q)`

Combined with Theorem 1, this establishes that BOTH observables'
closures contain `T_{25}` as a factor — the empirical "shared
building block" finding made categorically explicit. -/
theorem qbetaC3Rung1_factors_via_habiroT25 (q : ℝ) :
    qbetaC3Rung1 q = hbarQ q * habiroT25 q := by
  unfold qbetaC3Rung1 habiroT25
  ring

/-- **Theorem 3 (proved).** Unfold the Q_β c_3 base to its canonical
definitional form `-(q² + q⁻¹²)`.

This is the **definitional unfolding** (proof is `rfl` after `unfold`),
recorded as a named identity so downstream files can reference the
canonical form directly without repeating the `unfold`. Identifies
`qbetaC3Base` with the negative symmetric q²-block eigenvalue sum
(which equals `-[2]_{q²}` where `[2]_x := x + x⁻¹`; this stronger
factorization is NOT proved here and would require `field_simp +
ring` over `q ≠ 0`). -/
theorem qbetaC3Base_unfold (q : ℝ) :
    qbetaC3Base q = -(q ^ 2 + q⁻¹ ^ 2) := by
  rfl

/-- **Theorem 4 (proved, formal-existence form).**

The jet-order family appearing across both closures is realised by
the explicit function `f n r := ℏ_q r ^ n`:
  - `f 6 q = ℏ_q⁶` (m_μ R9 ℏ_q⁶ factor, h³ jet)
  - `f 8 q = ℏ_q⁸` (m_μ V9 ℏ_q⁸ factor, h⁴ jet)
  - `f 3 q = ℏ_q³` (Q_β c_3 rung 2 ℏ_q³ factor)

**Proven** via the explicit witness; the formal existence of a function
realising these jet indices is trivial.

The DEEP CATEGORICAL CLAIM — that this family IS the Markov-trace
expansion of a specific Wenzl-Hoefsmit operator (rather than a mere
indexing function) — is conjectural and absent from the present Lean
infrastructure. It is captured by the `markov_trace_origin` field of
`UniversalHabiroStructure` below (whose instance remains the open
work). -/
theorem hbar_q_jet_orders_family_exists (q : ℝ) :
    ∃ (f : ℕ → ℝ → ℝ),
      f 6 q = hbarQ q ^ 6 ∧
      f 8 q = hbarQ q ^ 8 ∧
      f 3 q = hbarQ q ^ 3 := by
  -- Ref: [wenzl1988] doi:10.1007/BF01239526 (target Markov-trace operator)
  -- Ref: [kassel1995] doi:10.1007/978-1-4612-0783-2 §V.7
  exact ⟨fun n r => hbarQ r ^ n, rfl, rfl, rfl⟩

/-- **Theorem 5 (proved, formal-existence form).**

The `1/n²` framing-ladder family is realised by
`framing n r := [3]_r / (n : ℝ)²`:
  - `framing 5 q = [3]_q / 25 = T_{25}(q) = habiroT25 q` (muon T(2,5))
  - `framing n q = [3]_q / n²` for all n (cross-lepton testable)

**Proven** via the explicit witness.

The DEEP CATEGORICAL CLAIM — that this family IS the T(2,n) cinquefoil
framing factor at the substrate level, with the n=5 selection matching
the muon's torus-knot assignment from
[`lepton_t2n_torus_tower.py`](../../../../../computations/lepton_t2n_torus_tower.py)
— is conjectural. It is captured by the `cinquefoil_framing_t25_origin`
field of `UniversalHabiroStructure` below. -/
theorem habiroT25_framing_family_exists (q : ℝ) :
    ∃ (framing : ℕ → ℝ → ℝ),
      framing 5 q = habiroT25 q ∧
      ∀ n, framing n q = quantumInt 3 q / (n : ℝ) ^ 2 := by
  -- Ref: [jones1985] doi:10.2307/1971403 (Jones polynomial of T(2,n))
  -- Ref: [habiro2004cyclotomic] arXiv:math/0209324 (Habiro ring of unity)
  refine ⟨fun n _ => quantumInt 3 q / (n : ℝ) ^ 2, ?_, fun _ => rfl⟩
  unfold habiroT25
  norm_num

/-! ## Cross-observable identities (proved)

These additional algebraic identities (Theorems 6-9) extend the
universal Habiro structure with concrete consistency checks at the
classical limit `q = 1` and quantify the jet-order ratio between
m_μ V9 and Q_β c_3 rung 1. -/

/-- **Theorem 6 (proved).** Cross-observable jet-order identity:
the m_μ V9 correction is exactly ℏ_q⁷ times the Q_β c_3 rung 1.

This makes the **shared `habiroT25` factor** with **different jet
orders** explicit as a single identity. -/
theorem delta_V9_eq_hbarQ_seven_times_qbetaC3Rung1 (q : ℝ) :
    delta_V9 q = hbarQ q ^ 7 * qbetaC3Rung1 q := by
  unfold delta_V9 qbetaC3Rung1
  ring

/-- **Theorem 7 (proved).** All categorical corrections vanish at the
classical limit `q = 1`.

Each correction is proportional to `hbarQ 1 = (1-1)/1 = 0`. -/
theorem corrections_vanish_at_q_one :
    delta_R9 1 = 0 ∧ delta_V9 1 = 0 ∧ qbetaC3Rung1 1 = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · unfold delta_R9 hbarQ hbarQ'; norm_num
  · unfold delta_V9 hbarQ hbarQ'; norm_num
  · unfold qbetaC3Rung1 hbarQ hbarQ'; norm_num

/-- **Theorem 8 (proved).** Classical-limit consistency: the empirical
3-rung Q_β c_3 closure formula reduces to `J_Hopf(q=1) = -2` at q = 1.

This is a structural check — the empirical Habiro closure is consistent
with the (proven) categorical conjecture `c_3 → J_Hopf` at the
classical limit. Connects to `QbetaC3StructuralFormClass` in
`QBetaCategoricalPrecisionLadder.lean` line 410. -/
theorem qbetaC3Closure_at_q_one_equals_neg_two :
    qbetaC3Closure 1 = -(2 : ℝ) := by
  unfold qbetaC3Closure qbetaC3Base qbetaC3Rung1 qbetaC3Rung2 hbarQ hbarQ'
  norm_num

/-- **Theorem 9 (proved).** Classical-limit consistency for m_μ: at
q = 1, the R9+V9 corrected prediction reduces to the bare
`m_e · vol_4_1 / hbarQ q²` formula evaluated at q = 1 (modulo the
hbarQ singularity).

Specifically, `1 - delta_total_mmu 1 = 1`, so the closure factor
collapses to unity at the classical limit. -/
theorem mmu_closure_factor_at_q_one :
    (1 : ℝ) - delta_total_mmu 1 = 1 := by
  unfold delta_total_mmu delta_R9 delta_V9 hbarQ hbarQ'
  norm_num

/-! ## Bridge to QBetaCategoricalPrecisionLadder (proved)

The empirical 3-rung Q_β c_3 closure (q-dependent) and the precision
ladder's `c_3 = jonesHopfClassicalLimit` (q-independent, conjectural)
must agree at the classical limit q = 1. -/

/-- **Bridge theorem (proved).** At the classical limit q = 1, the
empirical 3-rung Q_β c_3 closure equals the precision ladder's
`jonesHopfClassicalLimit = -2`.

Direct consequence of `qbetaC3Closure_at_q_one_equals_neg_two`
(Theorem 8) and the definition `jonesHopfClassicalLimit := -2`
(line 58 of QBetaCategoricalPrecisionLadder.lean).

This is the formal Lean record of the empirical-vs-categorical
consistency at the classical limit: two different formulas
(empirical 3-rung Habiro at q-dependent vs. q-independent J_Hopf
conjecture) give the same value at q = 1. -/
theorem qbetaC3Closure_at_q_one_equals_jonesHopfClassicalLimit :
    qbetaC3Closure 1 = jonesHopfClassicalLimit := by
  rw [qbetaC3Closure_at_q_one_equals_neg_two]
  rfl

/-! ## Lepton T(2,n) framing-ladder family

The empirical `habiroT25 = [3]_q / 25 = [3]_q / 5²` factor at the muon
level (T(2,5) cinquefoil) suggests a general family:

    habiroT_{n²}(q) := [3]_q / n²

with the lepton T(2,n) assignments (per
[`lepton_t2n_torus_tower.py`](../../../../../computations/lepton_t2n_torus_tower.py)):

| Lepton | Knot   | n | Factor      |
|--------|--------|---|-------------|
| e⁻     | T(2,3) | 3 | `[3]_q / 9` |
| μ⁻     | T(2,5) | 5 | `[3]_q / 25` ★ EMPIRICALLY MATCHES |
| τ⁻     | T(2,7) | 7 | `[3]_q / 49` (testable) |

The n=5 cinquefoil case is the empirical anchor (m_μ V9). Theorems
10-12 below formalize the general family. -/

/-- General lepton framing-ladder factor: `[3]_q / n²`. -/
noncomputable def habiroTnSq (n : ℕ) (q : ℝ) : ℝ :=
  quantumInt 3 q / (n : ℝ) ^ 2

/-- **Theorem 10 (proved).** The empirical muon factor `habiroT25` is
the n=5 case of the general framing-ladder family. -/
theorem habiroT25_eq_habiroTnSq_five (q : ℝ) :
    habiroT25 q = habiroTnSq 5 q := by
  unfold habiroT25 habiroTnSq
  norm_num

/-- **Theorem 11 (proved).** Electron framing factor at T(2,3) trefoil:
`habiroTnSq 3 q = [3]_q / 9`. -/
theorem habiroTnSq_three_explicit (q : ℝ) :
    habiroTnSq 3 q = quantumInt 3 q / 9 := by
  unfold habiroTnSq
  norm_num

/-- **Theorem 12 (proved).** Tau framing factor at T(2,7) septafoil:
`habiroTnSq 7 q = [3]_q / 49`. Cross-lepton testable prediction:
if the universal Habiro structure derives from the T(2,n) framing,
then the tau analog of m_μ V9 should involve a `[3]_q / 49` factor. -/
theorem habiroTnSq_seven_explicit (q : ℝ) :
    habiroTnSq 7 q = quantumInt 3 q / 49 := by
  unfold habiroTnSq
  norm_num

/-- **Theorem 13 (proved).** The framing-ladder family at the
classical limit q = 1: `habiroTnSq n 1` is finite for n ≥ 1.

This follows because at q = 1, the quantumInt formula has indeterminate
`0/0`, which Lean's field instance resolves to 0. (The categorical
limit `[3]_q → 3` as q → 1 holds via L'Hôpital; in Lean's pointwise
algebra, `quantumInt 3 1 = (1 - 1)/(1 - 1) = 0/0 = 0`.) -/
theorem habiroTnSq_at_q_one (n : ℕ) (hn : 0 < n) :
    habiroTnSq n 1 = 0 := by
  unfold habiroTnSq quantumInt
  norm_num

/-! ## Cross-lepton framing-ladder ratios (proved)

These pure algebraic identities encode the cross-lepton predictions
testable across the T(2,n) tower. -/

/-- **Theorem 14 (proved).** Cross-lepton framing ratio
e/μ: `habiroTnSq 3 q × 25 = habiroTnSq 5 q × 9` for all q.

Stated as the `n²`-normalisation `9·T(3) = 25·T(5)` (both sides equal
`[3]_q`). Equivalently the ratio `habiroTnSq 5 q / habiroTnSq 3 q =
9/25 = (3/5)²` when the numerator `[3]_q` cancels. -/
theorem habiroTnSq_three_five_ratio_identity (q : ℝ) :
    habiroTnSq 3 q * 9 = habiroTnSq 5 q * 25 := by
  unfold habiroTnSq
  ring

/-- **Theorem 15 (proved).** Cross-lepton framing ratio
μ/τ, as the `n²`-normalisation `25·T(5) = 49·T(7)` (both sides equal
`[3]_q`). Equivalently `habiroTnSq 7 q / habiroTnSq 5 q = 25/49 = (5/7)²`.

A predicted ratio testable when m_τ Habiro analog is wired. -/
theorem habiroTnSq_five_seven_ratio_identity (q : ℝ) :
    habiroTnSq 5 q * 25 = habiroTnSq 7 q * 49 := by
  unfold habiroTnSq
  ring

/-- **Theorem 16 (proved).** The m_μ R9 + V9 total correction
factors as `delta_total_mmu q = hbarQ q^6 · (q/5 + hbarQ q² · [3]_q / 25)`.

This makes the R9-out-front factoring explicit: the V9 rung is the
first-order categorical correction to the R9 leading rung. Connects to
the S11 factored Habiro form (`mmu_simpler_form_search_probe.py`):
`δ_total = (ℏ_q^6 × q / 5) × (1 + ℏ_q² × [3]_q / 5)` modulo the q
factor on `[3]_q` (which makes S11 slightly less accurate than V9). -/
theorem delta_total_mmu_factored (q : ℝ) :
    delta_total_mmu q = hbarQ q ^ 6 * (q / 5 + hbarQ q ^ 2 * quantumInt 3 q / 25) := by
  unfold delta_total_mmu delta_R9 delta_V9
  ring

/-- **Theorem 17 (proved).** Substrate `ℏ_q` is strictly positive on
the physical regime `q > 1`. Foundational positivity lemma needed for
downstream sign-tracking in the closure formulas. -/
theorem hbarQ_pos_of_one_lt_q (q : ℝ) (hq : 1 < q) : 0 < hbarQ q := by
  unfold hbarQ hbarQ'
  apply div_pos
  · linarith
  · linarith

/-- **Theorem 18 (proved).** Clearing the `25` denominator from
`habiroT25`: multiplying by 25 recovers the bare quantum integer.

  `25 · T_{25}(q) = [3]_q`

A direct cancellation identity used downstream when normalising
closure formulas. -/
theorem habiroT25_times_25_eq_quantumInt_three (q : ℝ) :
    25 * habiroT25 q = quantumInt 3 q := by
  unfold habiroT25
  ring

/-- **Theorem 19 (proved).** General framing-ladder normalisation:
for `n ≥ 1`, multiplying `habiroTnSq n q` by `n²` recovers `[3]_q`.

The n-parametric form of Theorem 18 — the framing factor *always*
clears to `[3]_q` via the squared T(2,n) crossing index, for any
positive lepton index. -/
theorem habiroTnSq_times_n_sq_eq_quantumInt_three (n : ℕ) (hn : 0 < n) (q : ℝ) :
    (n : ℝ) ^ 2 * habiroTnSq n q = quantumInt 3 q := by
  unfold habiroTnSq
  have hne : (n : ℝ) ^ 2 ≠ 0 := pow_ne_zero 2 (Nat.cast_ne_zero.mpr hn.ne')
  -- `field_simp` clears the `/ n²` and closes `n² * [3]_q = [3]_q * n²`.
  field_simp

/-- **Theorem 20 (proved).** Cross-rung product identity for Q_β c_3.

The rung 1 (containing `habiroT25 q`) and the m_μ V9 rung
(containing the same `habiroT25 q`) can be related directly:

  `qbetaC3Rung1 q · hbarQ q^7 = delta_V9 q`

A restatement of Theorem 6 (`delta_V9_eq_hbarQ_seven_times_qbetaC3Rung1`)
in product form. -/
theorem qbetaC3Rung1_times_hbarQ_seven_eq_delta_V9 (q : ℝ) :
    qbetaC3Rung1 q * hbarQ q ^ 7 = delta_V9 q := by
  rw [delta_V9_eq_hbarQ_seven_times_qbetaC3Rung1]
  ring

/-! ## Conditional closure theorem (§3b-cond pattern)

The formal-existence claims (Theorems 4 + 5) are proved above; the
DEEP categorical claims (that those existence witnesses ARE the
Markov-trace operator and cinquefoil framing respectively) remain
conjectural. This class captures the deep claims as opaque marker
fields (no constructive content yet) so downstream theorems can carry
them as hypotheses per AGENTS.md §3b-cond. -/

/-- Conditional class axiomatizing the two open categorical claims:

- `markov_trace_origin` (Theorem 4 deep claim): the function family
  `fun n r => ℏ_r^n` is the Markov-trace expansion of a specific
  Wenzl-Hoefsmit operator (currently unidentified in Lean).
- `cinquefoil_framing_t25_origin` (Theorem 5 deep claim): the framing
  family `fun n r => [3]_r / n²` is the T(2,n) cinquefoil framing
  factor at the substrate level. -/
class UniversalHabiroStructure (q : ℝ) : Prop where
  /-- The function `fun n r => ℏ_r^n` is the Markov-trace expansion of
  a Wenzl-Hoefsmit operator (opaque marker for the open derivation).

  The Markov-trace *infrastructure* is not the gate: `QOU.Machinery.
  MarkovTraceOnHecke` realizes the H₃(q) Markov trace concretely (`trM`)
  with (M1) linearity, (M2) cyclicity (`trM_cyclic`) and (M3) reduction
  (`trM_markov_σ₁`) all proved sorry-free, and names itself the bridge for
  discharging this marker "once Step 4 names the residue-A element." The
  open gate is that operator identification (Step 4) plus extending the
  trace beyond H₃. -/
  markov_trace_origin : True
  /-- The function `fun n r => [3]_r / n²` is the substrate-level T(2,n)
  cinquefoil framing factor (opaque marker for the open derivation). -/
  cinquefoil_framing_t25_origin : True

/-- **Theorem (conditional on [UniversalHabiroStructure]).**

If the universal Habiro structure holds at `q`, then both the m_μ
R9+V9 closure and the Q_β c_3 3-rung closure represent genuine
categorical derivations of their respective L2 observables at `q`.

**Corrected 2026-08-21** (vacuity ledger,
`proof-no-unused-hypothesis-rfl`, verdict genuine).  This was billed as
"the §3b-cond conditional-class theorem: its conclusion is the L2
closure of both observables, conditional on the class instance."  It is
not, and never was:

- both conjuncts are closed by `rfl`, so the statement is two
  *definitional unfoldings* joined by `∧` — it says that
  `m_mu_R9_V9` and `qbetaC3Closure` unfold to their own definitions;
- neither `hq : 0 < q` nor the `[UniversalHabiroStructure q]` instance
  was used, and the instance in particular was advertised as the
  structure supplying the closure while contributing nothing.  Both
  unused binders have been dropped, which is what makes the remaining
  content honest: unfolding lemmas that do not pretend to be
  conditional on an open structure.

The instance could not have contributed: `UniversalHabiroStructure`'s
two fields are `markov_trace_origin : True` and
`cinquefoil_framing_t25_origin : True`, both self-described opaque
markers, so the class constrains nothing.

**A universal Habiro closure is therefore NOT established here.**  It
remains one of the framework's open targets (Theorems 4 + 5); the
empirical position is unchanged — witnesses show the closures hold to
within their L2 100× gates at proton-pinned q₀, the class instance has
NOT been constructed, NEAR-MATCH tier, production wiring untouched. -/
theorem universal_habiro_closure
    (q m_e vol_4_1 : ℝ) :
    m_mu_R9_V9 q m_e vol_4_1 =
      m_e * vol_4_1 / hbarQ q ^ 2 * (1 - delta_total_mmu q) ∧
    qbetaC3Closure q =
      qbetaC3Base q * (1 + qbetaC3Rung1 q + qbetaC3Rung2 q) :=
  ⟨rfl, rfl⟩

end QOU.BraidKnot
