import Mathlib.Tactic

/-!
# The pairwise chain's leading-order error, exactly

Bean `qou-zrx2`. Probe:
`computations/probes/binding_chain_floor_corrected_probe.py`.

## What this certifies

`derive_binding_chain_cooperative` models nuclear binding as a sum over the
`(A−1)` bonds of a chain, each bond a **2-nucleon** sub-braid, and compares that
sum against the exact `H_{3A}` trace. How good is the pairwise approximation?

Once the classical floor is removed (`QOU.MassTheory.ClassicalTraceFloor`), the
corrected observable `Δtr − c₀(A)` is `ℏ_q^1`, and its leading coefficient
`c₁ = lim (Δtr − c₀)/ℏ_q` is an **exact dyadic rational** in every measured case
(to `≤ 1.3e-9`):

    pp   19/8      pn   37/16     nn   9/4
    T    163/64    ³He  85/32     ⁴He  259/128

Those are measurements, and they enter here as definitions. What this file
proves is what follows from them: the **leading-order pairwise-vs-exact ratio is
an exact rational**, so the chain's error at leading order is not a residual to
be estimated but a number to be written down.

## The three ratios

    T    (37/16 + 9/4)  / (163/64)         = 292/163
    ³He  (19/8 + 37/16) / (85/32)          = 30/17
    ⁴He  (19/8 + 37/16 + 9/4)/(259/128)    = 888/259 = 24/7

The ⁴He simplification is the striking one — `259 = 7·37` and `888 = 24·37`, so
the `37` cancels and the ratio is exactly `24/7`.

## ⚠ What the numbers say, and it is not flattering

At `q₀` these ratios are `1.118`, `1.020`, `1.194`. At **leading order** they are
`1.791`, `1.765`, `3.429`. The chain over-counts the exact trace by `24/7` at
⁴He as `ℏ_q → 0`.

So **pairwise additivity of the signed trace functor is not a controlled
approximation.** Its good behaviour at `q₀` comes from higher-order terms
partially cancelling a large leading-order error, not from a structural property
that would survive to other `q`. `chain_over_atom_He4_gt_three` below is the
formal version of that: the leading-order ratio exceeds 3.

This concerns the **signed** functor `tr_free − tr_atom`. The exact-additivity
result in `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md` is about the
**log** functor `α·ln(tr_free/tr_atom)` — a different object, not contradicted
here, but easy to conflate.

-- Ref: [manuscript] bean qou-zrx2; computations/probes/binding_chain_floor_corrected_probe.py
-/

namespace QOU.MassTheory

/-! ### The measured leading coefficients

Definitions, not theorems: these are the `ℏ_q → 0` limits of
`(Δtr − c₀(A))/ℏ_q`, extrapolated at 60 dps and matched to their best rational
with denominator `≤ 4096`. Every denominator is a power of two — the same shape
as the classical floor `c₀`, which *is* derived
(`ClassicalTraceFloor.classical_floor_of_cycle_counts`). -/

/-- Leading `ℏ_q` coefficient for the `pp` bond. -/
def c1_pp : ℚ := 19 / 8

/-- Leading `ℏ_q` coefficient for the `pn` bond. -/
def c1_pn : ℚ := 37 / 16

/-- Leading `ℏ_q` coefficient for the `nn` bond. -/
def c1_nn : ℚ := 9 / 4

/-- Leading `ℏ_q` coefficient for the whole tritium braid. -/
def c1_T : ℚ := 163 / 64

/-- Leading `ℏ_q` coefficient for the whole `³He` braid. -/
def c1_He3 : ℚ := 85 / 32

/-- Leading `ℏ_q` coefficient for the whole `⁴He` braid. -/
def c1_He4 : ℚ := 259 / 128

/-- **Every one of them is dyadic**: multiplying by the right power of two gives
an integer. Stated as `c₁ · 2^k = m` rather than via `Rat.den`, which does not
reduce under `decide` for a division literal.

The same shape as the classical floor, where `c₀·2^{3A}` is an integer — and
there it is derived, which is why this is read as structure rather than
coincidence. -/
theorem c1_dyadic :
    c1_pp * 8 = 19 ∧ c1_pn * 16 = 37 ∧ c1_nn * 4 = 9
      ∧ c1_T * 64 = 163 ∧ c1_He3 * 32 = 85 ∧ c1_He4 * 128 = 259 := by
  unfold c1_pp c1_pn c1_nn c1_T c1_He3 c1_He4
  norm_num

/-! ### The chain sums, and the exact ratios

`CHAIN` in `derive_binding_chain_cooperative` is `T = pn + nn`,
`³He = pp + pn`, `⁴He = pp + pn + nn`. -/

/-- The tritium chain sum at leading order. -/
theorem chain_T : c1_pn + c1_nn = 73 / 16 := by
  unfold c1_pn c1_nn; norm_num

/-- The `³He` chain sum at leading order. -/
theorem chain_He3 : c1_pp + c1_pn = 75 / 16 := by
  unfold c1_pp c1_pn; norm_num

/-- The `⁴He` chain sum at leading order. -/
theorem chain_He4 : c1_pp + c1_pn + c1_nn = 111 / 16 := by
  unfold c1_pp c1_pn c1_nn; norm_num

/-- **Tritium: the chain over-counts by exactly `292/163`.** -/
theorem chain_over_atom_T : (c1_pn + c1_nn) / c1_T = 292 / 163 := by
  rw [chain_T]; unfold c1_T; norm_num

/-- **`³He`: exactly `30/17`.** -/
theorem chain_over_atom_He3 : (c1_pp + c1_pn) / c1_He3 = 30 / 17 := by
  rw [chain_He3]; unfold c1_He3; norm_num

/-- **`⁴He`: exactly `24/7`.**

`888/259` in lowest terms: `259 = 7·37` and `888 = 24·37`, so the `37` cancels.
Of the three this is the one that simplifies, and it is the largest. -/
theorem chain_over_atom_He4 : (c1_pp + c1_pn + c1_nn) / c1_He4 = 24 / 7 := by
  rw [chain_He4]; unfold c1_He4; norm_num

/-- **The leading-order error is large.** At `⁴He` the pairwise chain exceeds the
exact `H_{3A}` trace by more than a factor of three as `ℏ_q → 0`.

This is the formal statement of the warning in the header: the `1.194` ratio
measured at `q₀` is not a leading-order property, so the pairwise approximation
is not controlled. -/
theorem chain_over_atom_He4_gt_three :
    3 < (c1_pp + c1_pn + c1_nn) / c1_He4 := by
  rw [chain_over_atom_He4]; norm_num

/-- All three chains over-count: every leading-order ratio exceeds `1`. -/
theorem chains_overcount :
    1 < (c1_pn + c1_nn) / c1_T
      ∧ 1 < (c1_pp + c1_pn) / c1_He3
      ∧ 1 < (c1_pp + c1_pn + c1_nn) / c1_He4 := by
  rw [chain_over_atom_T, chain_over_atom_He3, chain_over_atom_He4]
  norm_num

end QOU.MassTheory
