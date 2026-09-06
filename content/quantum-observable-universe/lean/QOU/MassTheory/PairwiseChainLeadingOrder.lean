import Mathlib.Tactic

/-!
# The pairwise chain's leading-order error, exactly

Bean `qou-pdg9` (successor to `qou-zrx2`). Probe:
`computations/probes/canonical_c1_closed_form_probe.py`.

## What this certifies

`derive_binding_chain_cooperative` models nuclear binding as a sum over the
`(A−1)` bonds of a chain, each bond a **2-nucleon** sub-braid, and compares that
sum against the exact `H_{3A}` trace. How good is the pairwise approximation?

Once the classical floor is removed (`QOU.MassTheory.ClassicalTraceFloor`), the
corrected observable `Δtr − c₀(A)` is `ℏ_q^1`, and its leading coefficient
`c₁ = lim (Δtr − c₀)/ℏ_q` is an exact dyadic rational in every case.

## ⚠ REPAIRED 2026-09-06 — the previous six values were the OLD atom word's

This file used to carry

    pp   19/8      pn   37/16     nn   9/4
    T    163/64    ³He  85/32     ⁴He  259/128

Those are the **pre-2026-09-05 (`grouped`) word's**. Owner ruling `qou-hu1f`
reordered each nucleon's confinement core from `σ₀³σ₁⁻³` to the alternating
`(σ₀σ₁⁻¹)³`, and `c₁` moved by up to `163×`
(`docs/audits/2026-09-06-c1-is-stale-on-the-reordered-atom-word.md`). The
canonical values are

    pp   1/8       pn   1/16      nn   0
    T    1/64      ³He  1/8       ⁴He  7/128

## The structure that makes this a repair rather than a number swap

`c₁` has a closed form whose only ordering-dependent input is the pair of
**per-nucleon deletion sums** `(S_p, S_n)`, each computed on that nucleon's own
three strands:

    c₁(Z,N) = (Z·S_p + N·S_n)/2 · (2^(−A−1) − 2^(−2A)) − 4·(I_pp − I_nn)·2^(−2A)

    borromean (canonical)   (S_p, S_n) = ( 6, −4)
    grouped   (superseded)  (S_p, S_n) = (42, 32)

So this file is now written **generically in `(S_p, S_n)`** and the six values are
instantiations. `c1_canonical_values` and `c1_grouped_values` below check that the
generic forms reproduce both columns exactly, which is what makes the genericity
a verified claim rather than a reformatting.

## The three ratios, and the one that does not move

    T    (c₁_pn + c₁_nn) / c₁_T             292/163  →  4
    ³He  (c₁_pp + c₁_pn) / c₁_He3            30/17   →  3/2
    ⁴He  (c₁_pp + c₁_pn + c₁_nn) / c₁_He4    24/7    →  24/7   ← UNCHANGED

**The ⁴He ratio is `24/7` for every `(S_p, S_n)`** — `chain_over_atom_He4_generic`
proves the symbols cancel identically, so it is invariant under *any*
intra-nucleon reordering, not merely under the two that have been computed. The
reason is visible in the algebra: ⁴He has `Z = N = 2`, so its own interface term
`−4(I_pp − I_nn)` vanishes, and across the three `A = 2` bonds the `pp` term
`−4` and the `nn` term `+4` cancel in the sum. Both sides are then proportional
to `(S_p + S_n)`, which divides out.

`T` and `³He` have no such cancellation — their interface terms survive — and
their ratios do move.

## ⚠ What the numbers say, and it is not flattering

At leading order the chain over-counts the exact `H_{3A}` trace by `4`, `3/2` and
`24/7`. **Pairwise additivity of the signed trace functor is not a controlled
approximation**, and `chain_over_atom_He4_gt_three` is the formal version: the
leading-order ratio exceeds 3. That conclusion is now *stronger* than it was
before the repair, because the ⁴He ratio carrying it is ordering-invariant.

This concerns the **signed** functor `tr_free − tr_atom`. The exact-additivity
result in `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md` is about the
**log** functor `α·ln(tr_free/tr_atom)` — a different object, not contradicted
here, but easy to conflate.

-- Ref: [manuscript] beans qou-pdg9, qou-zrx2, qou-hu1f;
--      computations/probes/canonical_c1_closed_form_probe.py
-/

namespace QOU.MassTheory

/-! ### The closed form, generic in the per-nucleon deletion sums

Each definition is `c₁(Z,N)` at that `(Z,N)`, with `A`, `I_pp` and `I_nn`
already substituted. Writing them out rather than defining a general `c₁` keeps
the interface counts `max(Z−1,0)` out of the statements, where they would need
truncated subtraction and buy nothing: only six instances are ever used. -/

/-- `c₁` for the `pp` bond: `Z = 2, N = 0, A = 2`, so `I_pp = 1`, `I_nn = 0`. -/
def c1PP (Sp : ℚ) : ℚ := Sp / 16 - 1 / 4

/-- `c₁` for the `pn` bond: `Z = N = 1`, so both interface counts vanish. -/
def c1PN (Sp Sn : ℚ) : ℚ := (Sp + Sn) / 32

/-- `c₁` for the `nn` bond: `Z = 0, N = 2`, so `I_pp = 0`, `I_nn = 1`. -/
def c1NN (Sn : ℚ) : ℚ := Sn / 16 + 1 / 4

/-- `c₁` for the whole tritium braid: `Z = 1, N = 2, A = 3`, `I_nn = 1`. -/
def c1T (Sp Sn : ℚ) : ℚ := 3 * (Sp + 2 * Sn) / 128 + 1 / 16

/-- `c₁` for the whole `³He` braid: `Z = 2, N = 1, A = 3`, `I_pp = 1`. -/
def c1He3 (Sp Sn : ℚ) : ℚ := 3 * (2 * Sp + Sn) / 128 - 1 / 16

/-- `c₁` for the whole `⁴He` braid: `Z = N = 2, A = 4`, so `I_pp = I_nn = 1` and
the interface term vanishes. This is the vanishing that makes the ⁴He ratio
ordering-invariant. -/
def c1He4 (Sp Sn : ℚ) : ℚ := 7 * (Sp + Sn) / 256

/-! ### The two instantiations

The canonical word and the superseded one. Both are checked, because a generic
form that reproduces only the column it was written for has not been shown to be
generic. -/

/-- Canonical: `intra_order = "borromean"`, `(S_p, S_n) = (6, −4)`. -/
theorem c1_canonical_values :
    c1PP 6 = 1 / 8 ∧ c1PN 6 (-4) = 1 / 16 ∧ c1NN (-4) = 0
      ∧ c1T 6 (-4) = 1 / 64 ∧ c1He3 6 (-4) = 1 / 8 ∧ c1He4 6 (-4) = 7 / 128 := by
  unfold c1PP c1PN c1NN c1T c1He3 c1He4
  norm_num

/-- Superseded: `intra_order = "grouped"`, `(S_p, S_n) = (42, 32)`. These are the
six values this file carried before 2026-09-06; they are kept as a *check on the
generic form*, not as live coefficients. -/
theorem c1_grouped_values :
    c1PP 42 = 19 / 8 ∧ c1PN 42 32 = 37 / 16 ∧ c1NN 32 = 9 / 4
      ∧ c1T 42 32 = 163 / 64 ∧ c1He3 42 32 = 85 / 32 ∧ c1He4 42 32 = 259 / 128 := by
  unfold c1PP c1PN c1NN c1T c1He3 c1He4
  norm_num

/-- Every canonical value is dyadic: multiplying by the right power of two gives
an integer. Stated as `c₁ · 2^k = m` rather than via `Rat.den`, which does not
reduce under `decide` for a division literal.

The same shape as the classical floor, where `c₀·2^{3A}` is an integer — and
there it is derived (`ClassicalTraceFloor.classical_floor_of_cycle_counts`),
which is why this is read as structure rather than coincidence. -/
theorem c1_dyadic_canonical :
    c1PP 6 * 8 = 1 ∧ c1PN 6 (-4) * 16 = 1 ∧ c1NN (-4) * 1 = 0
      ∧ c1T 6 (-4) * 64 = 1 ∧ c1He3 6 (-4) * 8 = 1 ∧ c1He4 6 (-4) * 128 = 7 := by
  unfold c1PP c1PN c1NN c1T c1He3 c1He4
  norm_num

/-! ### The chain sums, and the exact ratios

`CHAIN` in `derive_binding_chain_cooperative` is `T = pn + nn`,
`³He = pp + pn`, `⁴He = pp + pn + nn`. -/

/-- **The ⁴He chain sum is `3(S_p + S_n)/32` for every `(S_p, S_n)`.** The `pp`
bond's `−1/4` and the `nn` bond's `+1/4` — the two interface terms — cancel. -/
theorem chain_He4_generic (Sp Sn : ℚ) :
    c1PP Sp + c1PN Sp Sn + c1NN Sn = 3 * (Sp + Sn) / 32 := by
  unfold c1PP c1PN c1NN; ring

/-- **⁴He: the chain over-counts by exactly `24/7`, for every `(S_p, S_n)`.**

This is the file's headline claim and it is *ordering-invariant*: the deletion
sums cancel between numerator and denominator, so no intra-nucleon reordering can
move it — not the two that have been computed, and not any other. `S_p + S_n ≠ 0`
is needed only because division by zero in `ℚ` is `0`. -/
theorem chain_over_atom_He4_generic (Sp Sn : ℚ) (h : Sp + Sn ≠ 0) :
    (c1PP Sp + c1PN Sp Sn + c1NN Sn) / c1He4 Sp Sn = 24 / 7 := by
  rw [chain_He4_generic]
  unfold c1He4
  field_simp
  ring

/-- The ⁴He ratio at the canonical `(S_p, S_n) = (6, −4)`. -/
theorem chain_over_atom_He4 :
    (c1PP 6 + c1PN 6 (-4) + c1NN (-4)) / c1He4 6 (-4) = 24 / 7 :=
  chain_over_atom_He4_generic 6 (-4) (by norm_num)

/-- **Tritium: the chain over-counts by `4`** at the canonical word — where the
superseded word gave `292/163 ≈ 1.791`. Unlike ⁴He this ratio is *not* invariant:
`T` has `Z ≠ N`, so its interface term survives and the deletion sums do not
cancel. -/
theorem chain_over_atom_T : (c1PN 6 (-4) + c1NN (-4)) / c1T 6 (-4) = 4 := by
  unfold c1PN c1NN c1T; norm_num

/-- **`³He`: exactly `3/2`** at the canonical word, against `30/17 ≈ 1.765`
before. Not invariant, for the same reason as tritium. -/
theorem chain_over_atom_He3 : (c1PP 6 + c1PN 6 (-4)) / c1He3 6 (-4) = 3 / 2 := by
  unfold c1PP c1PN c1He3; norm_num

/-- **The T and ³He ratios really do depend on the ordering** — the two words give
different values, which is what distinguishes them from ⁴He above. Stated as a
disequality so it cannot be read as a claim about which value is right. -/
theorem chain_ratios_T_He3_not_invariant :
    (c1PN 6 (-4) + c1NN (-4)) / c1T 6 (-4)
      ≠ (c1PN 42 32 + c1NN 32) / c1T 42 32
    ∧ (c1PP 6 + c1PN 6 (-4)) / c1He3 6 (-4)
      ≠ (c1PP 42 + c1PN 42 32) / c1He3 42 32 := by
  unfold c1PP c1PN c1NN c1T c1He3
  norm_num

/-- **The leading-order error is large.** At ⁴He the pairwise chain exceeds the
exact `H_{3A}` trace by more than a factor of three as `ℏ_q → 0`, for **every**
`(S_p, S_n)`.

This is the formal statement of the warning in the header: the pairwise
approximation is not controlled. Because it is proved generically it survives the
`qou-hu1f` ruling, and any future intra-nucleon reordering, without recomputation. -/
theorem chain_over_atom_He4_gt_three (Sp Sn : ℚ) (h : Sp + Sn ≠ 0) :
    3 < (c1PP Sp + c1PN Sp Sn + c1NN Sn) / c1He4 Sp Sn := by
  rw [chain_over_atom_He4_generic Sp Sn h]; norm_num

/-- All three chains over-count at the canonical word: every leading-order ratio
exceeds `1`. -/
theorem chains_overcount :
    1 < (c1PN 6 (-4) + c1NN (-4)) / c1T 6 (-4)
      ∧ 1 < (c1PP 6 + c1PN 6 (-4)) / c1He3 6 (-4)
      ∧ 1 < (c1PP 6 + c1PN 6 (-4) + c1NN (-4)) / c1He4 6 (-4) := by
  rw [chain_over_atom_T, chain_over_atom_He3, chain_over_atom_He4]
  norm_num

end QOU.MassTheory
