import Mathlib.Tactic

/-!
# The pairwise chain's leading-order error, exactly

Bean `qou-zrx2`, re-derived under `qou-j1e5`. Probes:
`computations/probes/binding_chain_floor_corrected_probe.py`,
`computations/probes/c1_leading_coefficient_derived_probe.py`,
`computations/probes/c1_letter_coefficients_are_ordering_dependent_probe.py`.

## What this certifies

`derive_binding_chain_cooperative` models nuclear binding as a sum over the
`(A−1)` bonds of a chain, each bond a **2-nucleon** sub-braid, and compares that
sum against the exact `H_{3A}` trace. How good is the pairwise approximation?

Once the classical floor is removed (`QOU.MassTheory.ClassicalTraceFloor`), the
corrected observable `Δtr − c₀(A)` is `ℏ_q^1`, and its leading coefficient
`c₁ = lim (Δtr − c₀)/ℏ_q` is an **exact dyadic rational** in every measured case.

## 🛑 RE-DERIVED UNDER THE BORROMEAN RULING (2026-09-06)

`7db032fb48` (owner ruling, bean `qou-hu1f`) changed `atom_braid_word_3A`'s
default intra-nucleon ordering from `grouped` to `borromean`. The six values
below are the **Borromean** ones. The previous grouped values are superseded but
recorded here, because two of the three ratios move and a reader coming from the
older audit documents needs to see both:

    ordering    pp      pn      nn     T        ³He     ⁴He
    grouped     19/8    37/16   9/4    163/64   85/32   259/128   (SUPERSEDED)
    borromean   1/8     1/16    0      1/64     1/8     7/128     (current)

All six Borromean values are measured, and `⁴He` twice over — the probe computes
it by exact series and by the permutation count, and both give `7/128`.

**`c1_nn = 0` is a vanishing coefficient, not a small one.** The neutron–neutron
leading coefficient is exactly zero under the Borromean word, which is why
`chain_T` below is `c1_pn` alone.

## The three ratios

    T    (1/16 + 0)          / (1/64)    = 4
    ³He  (1/8  + 1/16)       / (1/8)     = 3/2
    ⁴He  (1/8  + 1/16 + 0)   / (7/128)   = 24/7

## The ⁴He `24/7` is STRUCTURAL — and that is the substantive change here

An earlier version of this file called `24/7` "the striking one — `259 = 7·37`
and `888 = 24·37`, so the `37` cancels", i.e. read it as a coincidence among six
measured rationals. **It is not a coincidence.** The `37` is `a + b`, the sum of
the two per-letter weights in the closed form

    c₁(Z,N) = (a·Z + b·N)(2^-(A+1) − 2^-2A) − 4(i_pp − i_nn)·2^-2A

and `chain_over_atom_He4_of_letters` below proves that the ratio is `24/7` for
**every** `(a, b)` with `a + b ≠ 0`, the `(a+b)` cancelling identically. So
`259 = 7·37` held by construction, and `24/7` is invariant under the ordering
change — it is the same number under `(21, 16)` and under `(3, −2)`.

The `T` and `³He` ratios are **not** invariant (`292/163 → 4`, `30/17 → 3/2`),
which is what makes the `⁴He` cancellation worth naming rather than a general
fact about all three.

## ⚠ What the numbers say, and it is not flattering — unchanged

At **leading order** the three ratios are `4`, `1.5`, `3.429`. The chain
over-counts the exact trace by `24/7` at ⁴He as `ℏ_q → 0`.

So **pairwise additivity of the signed trace functor is not a controlled
approximation.** Its good behaviour at `q₀` comes from higher-order terms
partially cancelling a large leading-order error, not from a structural property
that would survive to other `q`. `chain_over_atom_He4_gt_three` below is the
formal version of that: the leading-order ratio exceeds 3. **That conclusion
survives the ordering change intact**, and now with a stronger warrant, since the
`⁴He` ratio is proved rather than measured.

This concerns the **signed** functor `tr_free − tr_atom`. The exact-additivity
result in `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md` is about the
**log** functor `α·ln(tr_free/tr_atom)` — a different object, not contradicted
here, but easy to conflate.

-- Ref: [leitner2026] beans qou-zrx2, qou-j1e5, qou-hu1f;
-- computations/probes/c1_letter_coefficients_are_ordering_dependent_probe.py
-/

namespace QOU.MassTheory

/-! ### The measured leading coefficients (Borromean word)

Definitions, not theorems: these are the `ℏ_q → 0` limits of
`(Δtr − c₀(A))/ℏ_q`. Every denominator is a power of two — the same shape as the
classical floor `c₀`, which *is* derived
(`ClassicalTraceFloor.classical_floor_of_cycle_counts`). -/

/-- Leading `ℏ_q` coefficient for the `pp` bond. -/
def c1_pp : ℚ := 1 / 8

/-- Leading `ℏ_q` coefficient for the `pn` bond. -/
def c1_pn : ℚ := 1 / 16

/-- Leading `ℏ_q` coefficient for the `nn` bond. **Exactly zero** under the
Borromean word — a vanishing coefficient, not a small one. -/
def c1_nn : ℚ := 0

/-- Leading `ℏ_q` coefficient for the whole tritium braid. -/
def c1_T : ℚ := 1 / 64

/-- Leading `ℏ_q` coefficient for the whole `³He` braid. -/
def c1_He3 : ℚ := 1 / 8

/-- Leading `ℏ_q` coefficient for the whole `⁴He` braid. -/
def c1_He4 : ℚ := 7 / 128

/-- **Every one of them is dyadic**: multiplying by the right power of two gives
an integer. Stated as `c₁ · 2^k = m` rather than via `Rat.den`, which does not
reduce under `decide` for a division literal. -/
theorem c1_dyadic :
    c1_pp * 8 = 1 ∧ c1_pn * 16 = 1 ∧ c1_nn * 4 = 0
      ∧ c1_T * 64 = 1 ∧ c1_He3 * 8 = 1 ∧ c1_He4 * 128 = 7 := by
  unfold c1_pp c1_pn c1_nn c1_T c1_He3 c1_He4
  norm_num

/-! ### The chain sums, and the exact ratios

`CHAIN` in `derive_binding_chain_cooperative` is `T = pn + nn`,
`³He = pp + pn`, `⁴He = pp + pn + nn`. -/

/-- The tritium chain sum at leading order. With `c1_nn = 0` this is the `pn`
bond alone. -/
theorem chain_T : c1_pn + c1_nn = 1 / 16 := by
  unfold c1_pn c1_nn; norm_num

/-- The `³He` chain sum at leading order. -/
theorem chain_He3 : c1_pp + c1_pn = 3 / 16 := by
  unfold c1_pp c1_pn; norm_num

/-- The `⁴He` chain sum at leading order. Equal to the `³He` sum, since the `nn`
bond contributes nothing. -/
theorem chain_He4 : c1_pp + c1_pn + c1_nn = 3 / 16 := by
  unfold c1_pp c1_pn c1_nn; norm_num

/-- **Tritium: the chain over-counts by exactly `4`.** -/
theorem chain_over_atom_T : (c1_pn + c1_nn) / c1_T = 4 := by
  rw [chain_T]; unfold c1_T; norm_num

/-- **`³He`: exactly `3/2`.** -/
theorem chain_over_atom_He3 : (c1_pp + c1_pn) / c1_He3 = 3 / 2 := by
  rw [chain_He3]; unfold c1_He3; norm_num

/-- **`⁴He`: exactly `24/7`.** Proved structurally below
(`chain_over_atom_He4_of_letters`) — it is the same value under the grouped
weights and under the Borromean ones. -/
theorem chain_over_atom_He4 : (c1_pp + c1_pn + c1_nn) / c1_He4 = 24 / 7 := by
  rw [chain_He4]; unfold c1_He4; norm_num

/-- **The leading-order error is large.** At `⁴He` the pairwise chain exceeds the
exact `H_{3A}` trace by more than a factor of three as `ℏ_q → 0`.

This is the formal statement of the warning in the header: the ratio measured at
`q₀` is not a leading-order property, so the pairwise approximation is not
controlled. -/
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

/-! ### The closed form, and why `24/7` is not a coincidence

The six coefficients are generated by one formula with two per-letter weights
`(a, b)` — see `QOU.MassTheory.LeadingOrderTraceCoefficient` for the derivation
of its shape from the permutation count. The ordering ruling moves `(a, b)` from
`(21, 16)` to `(3, −2)` and changes nothing else. -/

/-- The closed form of the leading coefficient at letter weights `(a, b)`:

    c₁(Z,N) = (a·Z + b·N)(2^-(A+1) − 2^-2A) − 4(i_pp − i_nn)·2^-2A

with `A = Z + N`, `i_pp = max(Z−1, 0)`, `i_nn = max(N−1, 0)`. Natural subtraction
already truncates at zero, so `Z - 1` *is* `i_pp`. -/
def c1Closed (a b : ℚ) (Z N : ℕ) : ℚ :=
  (a * Z + b * N) * ((2⁻¹ : ℚ) ^ (Z + N + 1) - (2⁻¹ : ℚ) ^ (2 * (Z + N)))
    - 4 * (((Z - 1 : ℕ) : ℚ) - ((N - 1 : ℕ) : ℚ)) * (2⁻¹ : ℚ) ^ (2 * (Z + N))

/-- The three pair terms sum to `3(a+b)/16`, the `+1` and `−1` interface
contributions of `pp` and `nn` cancelling. -/
theorem pairSum_of_letters (a b : ℚ) :
    c1Closed a b 2 0 + c1Closed a b 1 1 + c1Closed a b 0 2 = 3 * (a + b) / 16 := by
  unfold c1Closed
  norm_num
  try ring

/-- The `⁴He` atom term is `7(a+b)/128`. This is where the `7` in `259 = 7·37`
comes from — it is `2^-5 − 2^-8` times two, not a property of `37`. -/
theorem he4_of_letters (a b : ℚ) :
    c1Closed a b 2 2 = 7 * (a + b) / 128 := by
  unfold c1Closed
  norm_num
  try ring

/-- **The `⁴He` chain-over-atom ratio is `24/7` for every `(a, b)`.**

The `(a + b)` cancels identically, so the ratio does not depend on the letter
weights at all — hence it is the same under the grouped weights `(21, 16)` and
the Borromean weights `(3, −2)`, and the `37` that appeared to cancel
"strikingly" in the older reading is simply `a + b`. -/
theorem chain_over_atom_He4_of_letters (a b : ℚ) (hab : a + b ≠ 0) :
    (c1Closed a b 2 0 + c1Closed a b 1 1 + c1Closed a b 0 2) / c1Closed a b 2 2
      = 24 / 7 := by
  rw [pairSum_of_letters, he4_of_letters]
  field_simp
  try ring

/-- The closed form at the Borromean weights reproduces all six definitions
above. -/
theorem c1_defs_eq_closed_borromean :
    c1Closed 3 (-2) 2 0 = c1_pp ∧ c1Closed 3 (-2) 1 1 = c1_pn
      ∧ c1Closed 3 (-2) 0 2 = c1_nn ∧ c1Closed 3 (-2) 1 2 = c1_T
      ∧ c1Closed 3 (-2) 2 1 = c1_He3 ∧ c1Closed 3 (-2) 2 2 = c1_He4 := by
  unfold c1Closed c1_pp c1_pn c1_nn c1_T c1_He3 c1_He4
  norm_num

/-- The same closed form at the **superseded** grouped weights reproduces the
six grouped values, which is what makes the ordering change a change of two
coefficients rather than of the derivation. Kept as a check on that claim, not
as a live model. -/
theorem c1_grouped_values_eq_closed :
    c1Closed 21 16 2 0 = 19 / 8 ∧ c1Closed 21 16 1 1 = 37 / 16
      ∧ c1Closed 21 16 0 2 = 9 / 4 ∧ c1Closed 21 16 1 2 = 163 / 64
      ∧ c1Closed 21 16 2 1 = 85 / 32 ∧ c1Closed 21 16 2 2 = 259 / 128 := by
  unfold c1Closed
  norm_num

/-- **The `T` and `³He` chain-over-atom ratios really do depend on the ordering.**

Stated as a **disequality** so it cannot be read as a claim about which value is
right — both are correct, for their own word.

    T     292/163 ≈ 1.7914  (grouped)  →  4      (Borromean)
    ³He    30/17  ≈ 1.7647  (grouped)  →  3/2    (Borromean)

This is the counterpoint that gives `chain_over_atom_He4_of_letters` its force.
There the `(a + b)` cancels identically, so ⁴He's `24/7` holds for **every**
letter weighting and survives any intra-nucleon reordering. `T` and `³He` have
`Z ≠ N`, no such cancellation, and move — so the ⁴He invariance is a property of
that combination, not a general feature of the chain ratios.

Added on top of the `qou-j1e5` derivation rather than alongside it: a parallel
branch (`qou-pdg9`, PR #6920) reached the same generic `24/7` independently and
deferred to this file, and this disequality is the one statement that branch had
which this file did not. -/
theorem chain_ratios_T_He3_not_invariant :
    (c1Closed 3 (-2) 1 1 + c1Closed 3 (-2) 0 2) / c1Closed 3 (-2) 1 2
      ≠ (c1Closed 21 16 1 1 + c1Closed 21 16 0 2) / c1Closed 21 16 1 2
    ∧ (c1Closed 3 (-2) 2 0 + c1Closed 3 (-2) 1 1) / c1Closed 3 (-2) 2 1
      ≠ (c1Closed 21 16 2 0 + c1Closed 21 16 1 1) / c1Closed 21 16 2 1 := by
  unfold c1Closed
  norm_num

end QOU.MassTheory
