import Mathlib.Tactic
import QOU.MassTheory.LeadingOrderTraceCoefficient

/-!
# The leading-order mirror asymmetry, and its sign

Bean `qou-z4ba`. Probe: `computations/probes/c1_mirror_asymmetry_sign_probe.py`.

`LeadingOrderTraceCoefficient` derives the leading `ℏ_q` coefficient of the trace
difference as

    c₁(Z,N) = (3Z − 2N)(2^{−A−1} − 4^{−A}) − 4(I_pp − I_nn)·4^{−A},   A = Z + N,

with `I_pp = Z−1`, `I_nn = N−1` truncated in `ℕ`. This file extracts its **isospin
content**: the difference between a nucleus and its mirror collapses to a single
bracket,

    c₁(Z,N) − c₁(N,Z) = (Z − N)·(5·2^{−A−1} − 13·4^{−A})
                      = (Z − N)·4^{−A}·(5·2^{A−1} − 13)                        [★]

so the whole `(Z,N)`-dependence of the mirror asymmetry is `5·2^{A−1} − 13`. That
is **negative at `A = 2`** (`10 < 13`) and **positive for every `A ≥ 3`**
(`20, 40, 80, …`).

## Why the sign is the interesting part

The framework does not derive the energy scale that turns `c₁` into MeV (bean
`qou-59j5`; `log Z` is an entropy with no temperature, `qou-ssz6`), so every
magnitude claim in this lane is a ratio against a chosen unit. **A sign is not.**
Any positive scale `E` maps `c₁ ↦ E·c₁` and preserves order, so `mirror_pos`
below is a scale-free prediction: for `A ≥ 3` the trace channel says the
**proton-rich** member of a mirror pair binds **more**.

Measured against AME 2020, over all **230** mirror pairs with `Z > N` and
`A ≥ 3`, the observed sign is the opposite in **every** case — Coulomb repulsion
makes the proton-rich mirror the less bound one.

## Scope (a), stated as such

This is a scope-limited negative: the trace channel *alone*, at *leading order in
`ℏ_q`*, gets the mirror asymmetry backwards. No invariant is cited and none is
claimed, so it is not a structural exclusion of the channel or of anything in it.
What it localises is that the missing term must be charge-dependent and
**repulsive**, and large enough to overturn `[★]` rather than merely to supply the
observed gap — i.e. the Coulomb term that `CoulombFromCrossingCounts` records as
*"`a_C` is nowhere"* and `SaturationPeakStructure` as *"Nothing here derives
`a_V`, `a_S` or `a_C`"*.

Nothing about `c₂` or higher is claimed: those have exact values for six words
only and no closed form in `(Z,N)`.

-- Ref: [leitner2026] bean qou-z4ba; computations/probes/c1_mirror_asymmetry_sign_probe.py
-/

namespace QOU.MassTheory

/-- The mirror bracket `5·2^{−A−1} − 13·4^{−A}`, which carries the entire
`(Z,N)`-dependence of the leading-order mirror asymmetry.

**This file survived the 2026-09-06 `c1Closed` repair unchanged, and that is not
luck.** Owner ruling `qou-hu1f` reordered the atom word and `c₁`'s per-nucleon
coefficients moved from `(21, 16)` to `(3, −2)` — every one of the six recorded
values changed, by up to `163×`. Nothing here moved, because the mirror
difference cancels everything except the coefficient *gap*:

    c₁(Z,N) − c₁(N,Z) = (Z − N)·[ (P − Q)·(2^(−A−1) − 2^(−2A)) − 8·2^(−2A) ]

so `mirrorBracket` depends on `P − Q` alone, and `P − Q = (S_p − S_n)/2` is `5`
under **both** orderings — `(42 − 32)/2` and `(6 − (−4))/2`. The `13` below is
`(P − Q) + 8`, likewise fixed by it. That equality of gaps is **measured on the
two words, not derived**: nothing shown here forces a third ordering to give `5`
as well, so treat this file's invariance as verified-for-these-two rather than
structural, and re-check `P − Q` before quoting it for any new word. Contrast
`PairwiseChainLeadingOrder.chain_over_atom_He4_of_letters`, whose `24/7` **is**
structural — there the letter weights cancel identically, for every `(a, b)`. -/
noncomputable def mirrorBracket (A : ℕ) : ℚ :=
  5 * (1 / 2 : ℚ) ^ (A + 1) - 13 * (1 / 4 : ℚ) ^ A

/-- **[★]** The mirror difference of the derived `c₁`, exactly. Stated for
`1 ≤ Z` and `1 ≤ N` so that both truncated interface counts are honest
subtractions (`I_pp = Z−1`, `I_nn = N−1`). -/
theorem c1Closed_mirror_diff (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    c1Closed 3 (-2) Z N - c1Closed 3 (-2) N Z
      = ((Z : ℚ) - (N : ℚ)) * mirrorBracket (Z + N) := by
  obtain ⟨z, rfl⟩ : ∃ z, Z = z + 1 := ⟨Z - 1, by omega⟩
  obtain ⟨n, rfl⟩ : ∃ n, N = n + 1 := ⟨N - 1, by omega⟩
  unfold c1Closed mirrorBracket
  have e : n + 1 + (z + 1) = z + 1 + (n + 1) := by omega
  -- `PairwiseChainLeadingOrder.c1Closed` writes the second scale as `(2⁻¹)^(2A)` while
  -- `mirrorBracket` writes it as `(1/4)^A`. They are equal, but not syntactically, so
  -- `pow_mul` has to fire before `ring` can see one expression.
  simp only [Nat.add_sub_cancel, e, pow_mul]
  norm_num
  ring

/-- `4^A = 2^A · 2^A`, the one rewrite both proofs below need. -/
private theorem four_pow_eq (A : ℕ) : (4 : ℚ) ^ A = 2 ^ A * 2 ^ A := by
  rw [show (4 : ℚ) = 2 * 2 by norm_num, mul_pow]

/-- `4^{−A}·(5·2^{A−1} − 13)` is the bracket: the sign is that of `5·2^{A−1} − 13`. -/
theorem mirrorBracket_eq (A : ℕ) (hA : 1 ≤ A) :
    mirrorBracket A = (1 / 4 : ℚ) ^ A * (5 * 2 ^ (A - 1) - 13) := by
  obtain ⟨m, rfl⟩ : ∃ m, A = m + 1 := ⟨A - 1, by omega⟩
  simp only [mirrorBracket, Nat.add_sub_cancel, div_pow, one_pow, four_pow_eq,
    pow_succ]
  have hm : (2 : ℚ) ^ m ≠ 0 := by positivity
  field_simp
  ring

/-- **The A = 2 boundary case: the bracket is negative.** `5·2 = 10 < 13`. Mirror
pairs at `A = 2` are the diproton and dineutron, neither of which is bound, so
nothing is measured here — but the sign genuinely flips and the general claim
below must exclude it. -/
theorem mirrorBracket_neg_two : mirrorBracket 2 < 0 := by
  norm_num [mirrorBracket]

/-- **The general sign.** For every `A ≥ 3` the bracket is positive. -/
theorem mirrorBracket_pos {A : ℕ} (hA : 3 ≤ A) : 0 < mirrorBracket A := by
  have ht : (0 : ℚ) < 2 ^ A := by positivity
  -- `2^A ≥ 8` for `A ≥ 3`, so `5·2^A > 26`: exactly the `5·2^{A−1} > 13` of [★].
  have key : (26 : ℚ) < 5 * 2 ^ A := by
    have h8 : (8 : ℚ) ≤ 2 ^ A := by
      calc (8 : ℚ) = 2 ^ 3 := by norm_num
      _ ≤ 2 ^ A := pow_le_pow_right₀ (by norm_num) hA
    linarith
  have hne : (2 : ℚ) ^ A ≠ 0 := ne_of_gt ht
  -- Clear the denominators once, as an equation: `bracket · 2·4^A = 5·2^A − 26`,
  -- whose right side is exactly `key`. Multiplying rather than dividing keeps this
  -- off the `div_lt_div_iff` family, whose names move between Mathlib versions.
  have hmul : mirrorBracket A * (2 * (2 ^ A * 2 ^ A)) = 5 * 2 ^ A - 26 := by
    simp only [mirrorBracket, div_pow, one_pow, four_pow_eq, pow_succ]
    field_simp
    ring
  have hc : (0 : ℚ) < 2 * (2 ^ A * 2 ^ A) := by positivity
  nlinarith [hmul, key, hc]

/-- **The prediction.** For `A ≥ 3` and more protons than neutrons, the derived
leading-order coefficient is strictly larger for the proton-rich member: the trace
channel says it binds MORE. Measured against AME 2020 this is the wrong sign in
all 230 mirror pairs — see the module docstring and the probe. -/
theorem c1Closed_mirror_pos {Z N : ℕ} (hZ : 1 ≤ Z) (hN : 1 ≤ N)
    (hA : 3 ≤ Z + N) (hZN : N < Z) :
    c1Closed 3 (-2) N Z < c1Closed 3 (-2) Z N := by
  have h := c1Closed_mirror_diff Z N hZ hN
  have hb : 0 < mirrorBracket (Z + N) := mirrorBracket_pos hA
  have hd : (0 : ℚ) < (Z : ℚ) - (N : ℚ) := by
    have : (N : ℚ) < (Z : ℚ) := by exact_mod_cast hZN
    linarith
  nlinarith [h, mul_pos hd hb]

/-- The same statement as a strict monotonicity in the proton excess: at fixed
`A ≥ 3`, moving a neutron to a proton strictly increases `c₁`. (Corollary of
`c1Closed_step` and the bracket's sign; recorded because it is the form the
isospin reading uses.) -/
theorem c1Closed_mirror_ne {Z N : ℕ} (hZ : 1 ≤ Z) (hN : 1 ≤ N)
    (hA : 3 ≤ Z + N) (hZN : Z ≠ N) :
    c1Closed 3 (-2) Z N ≠ c1Closed 3 (-2) N Z := by
  rcases lt_or_gt_of_ne hZN with h | h
  · exact ne_of_lt (c1Closed_mirror_pos hN hZ (by omega) h)
  · exact ne_of_gt (c1Closed_mirror_pos hZ hN hA h)

end QOU.MassTheory
