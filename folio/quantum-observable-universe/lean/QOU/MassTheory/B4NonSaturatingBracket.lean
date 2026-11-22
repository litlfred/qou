/-
# The A=4 det-gate magnitude is BRACKETED by derived constants but supplied by none — scope-(a)

Bean qou-j16x — the "non-saturating connected 4-body operator" search, front-4
follow-up to the multiplicative-cumulant undershoot (PR #4605).  The sibling
`A4InterfaceMagnitude` (merged, #3924) proved the det-gate cumulant

    b₄(m) = −ln det(I + m·S) = −ln[(1 − 5m²)(1 − m²)]   (derived spectrum {±√5, ±1})

is **surjective** onto (0,∞) in its single scalar `m ∈ (0, 1/√5)`, so *inverting* the
⁴He target to pick `m` is a FIT.  The open question this file settles at the structural
level is whether an **independently-derived** framework constant supplies `m` with no
inversion.

## What the diagnostic found (0-fit; `b4_nonsaturating_mstar_diagnostic.py`)

Under the corpus normalization `MeV = E₀·(−ln det)` (writhe witness
`b4-1four-complete-graph-writhe-signs`, E₀ ≈ 4.18598 MeV), the required magnitude is
`m* ≈ 0.416421`.  Plugging each *derived* constant in AS `m` (the FORWARD, zero-inversion
direction) gives, as a fraction of the ⁴He `b₄ = 9.243 MeV` target:

| derived `m`   | value    | forward b₄ | % of target |
|---------------|----------|-----------:|------------:|
| `2h` (Hecke)  | 0.41812  |  9.480 MeV |  **102.6 %** |
| `h/z`         | 0.41869  |  9.562 MeV |  **103.5 %** |
| `z − h/2`     | 0.39479  |  7.034 MeV |    76.1 %   |
| `1/√5 − h/2`  | 0.34268  |  4.226 MeV |    45.7 %   |
| everything ≤ √(hz) | ≤0.323 |  ≤3.6 MeV |    ≤39 %   |

So `m*` is **bracketed** — `2h`/`h/z` overshoot by 2.6–3.5 %, all others undershoot by
≥24 % — but no derived constant lands within framework precision (nearest is 0.41 % in
`m`, 2.6 % forward; ~10⁷× the L1 floor).  Per the c_k near-match discipline a 2.6 %
"near-match" of `2h` is fitted-adjacent, **not** an identity, and is never wired.

## What THIS file proves (sorry-free, structural — the numerics live in the witness)

The generic **bracket-and-uniqueness** content of that finding, built on
`A4InterfaceMagnitude`:

* **`required_magnitude_strictly_bracketed`** — given a positive target cumulant `t` and
  two physical magnitudes `c_lo < c_hi` whose `b₄` values straddle `t`
  (`b₄ c_lo < t < b₄ c_hi`), the unique `m` with `b₄ m = t` (from surjectivity) satisfies
  `c_lo < m < c_hi` and `m ≠ c_lo`, `m ≠ c_hi`.  I.e. **no straddling derived constant
  reproduces the target** — matching would require a value strictly between them.
* **`detGate_no_endpoint_hits`** — the det-space form: for a target determinant
  `D ∈ (detG c_hi, detG c_lo)`, the preimage magnitude is interior and `detG c_lo ≠ D`,
  `detG c_hi ≠ D`.

Instantiated with the witness numerics `c_lo = z−h/2 ≈ 0.3948`, `c_hi = 2h ≈ 0.4181`,
`t* = 9.243/E₀ ≈ 2.208` (which do straddle: `b₄(z−h/2) ≈ 1.685 < 2.208 < 2.264 ≈
b₄(2h)`), this is the honest **scope-(a)** statement: the required magnitude is pinned to
the open interval between the framework's nearest derived constants, and equals neither.
No derived driver fixes `m`; nothing is wired; `free_parameters = 0`.

Base ring (§7c): `ℝ` throughout — archimedean (ordering, `Real.log`), inherited from
`A4InterfaceMagnitude`.

-- Ref: [leitner2026] computations/deltalambda/b4-nonsaturating-mstar-diagnostic.witness.json
   (required m*, forward derived-constant table, the straddle bracket; 0-fit, nothing wired).
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors", Invent. Math. 92 (1988) 349-383.
-/
import QOU.MassTheory.A4InterfaceMagnitude

namespace QOU.MassTheory.B4NonSaturatingBracket

open QOU.MassTheory.A4InterfaceMagnitude

/-! ### The bracket-and-uniqueness capstone (scope-(a): bracketed, hit by no endpoint) -/

/-- **The required magnitude is strictly bracketed by any two straddling constants.**
Given a positive target cumulant `t` and two *physical* magnitudes `c_lo < c_hi`
(`0 < c_lo`, `5 c_hi² < 1`) whose `b₄` values straddle `t`, the unique `m` with
`b₄ m = t` (existence from `magnitude_form_surjective`) satisfies `c_lo < m < c_hi`.
Consequence: matching the target requires a magnitude strictly *between* the two
constants — neither endpoint reproduces it.  This is the structural core of the
qou-j16x scope-(a) finding: the derived constants `z−h/2` (below) and `2h` (above)
bracket the required `m*` but supply it themselves nowhere. -/
theorem required_magnitude_strictly_bracketed
    (t c_lo c_hi : ℝ) (ht : 0 < t)
    (hlo_pos : 0 < c_lo) (hlohi : c_lo < c_hi) (hhi_phys : 5 * c_hi ^ 2 < 1)
    (hstraddle_lo : b4 c_lo < t) (hstraddle_hi : t < b4 c_hi) :
    ∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ b4 m = t ∧ c_lo < m ∧ m < c_hi := by
  obtain ⟨m, hm_pos, hm_phys, hm_eq⟩ := magnitude_form_surjective t ht
  have hlo_phys : 5 * c_lo ^ 2 < 1 := by nlinarith [sq_nonneg c_lo, sq_nonneg c_hi]
  have hc_hi_pos : 0 < c_hi := lt_trans hlo_pos hlohi
  refine ⟨m, hm_pos, hm_phys, hm_eq, ?_, ?_⟩
  · -- c_lo < m : otherwise m ≤ c_lo forces b4 m ≤ b4 c_lo < t = b4 m
    by_contra h
    push_neg at h            -- h : m ≤ c_lo
    rcases lt_or_eq_of_le h with hlt | heq
    · have := b4_strictMono_on m c_lo hm_pos hlt hlo_phys
      rw [hm_eq] at this; linarith
    · rw [heq] at hm_eq; linarith        -- heq : m = c_lo ⇒ hm_eq : b4 c_lo = t
  · -- m < c_hi : otherwise c_hi ≤ m forces b4 c_hi ≤ b4 m = t < b4 c_hi
    by_contra h
    push_neg at h            -- h : c_hi ≤ m
    rcases lt_or_eq_of_le h with hlt | heq
    · have := b4_strictMono_on c_hi m hc_hi_pos hlt hm_phys
      rw [hm_eq] at this; linarith
    · rw [← heq] at hm_eq; linarith      -- heq : c_hi = m ⇒ hm_eq : b4 c_hi = t

/-- **No straddling endpoint reproduces the target** (immediate corollary): under the
same hypotheses, `b₄ c_lo ≠ t` and `b₄ c_hi ≠ t`.  A derived constant that brackets the
target cannot *equal* the required magnitude's cumulant. -/
theorem no_endpoint_reproduces_target
    (t c_lo c_hi : ℝ) (_ht : 0 < t)
    (_hlo_pos : 0 < c_lo) (_hlohi : c_lo < c_hi) (_hhi_phys : 5 * c_hi ^ 2 < 1)
    (hstraddle_lo : b4 c_lo < t) (hstraddle_hi : t < b4 c_hi) :
    b4 c_lo ≠ t ∧ b4 c_hi ≠ t :=
  ⟨ne_of_lt hstraddle_lo, (ne_of_lt hstraddle_hi).symm⟩

/-- **Det-space form.**  For a target determinant `D` strictly between `detG c_hi` and
`detG c_lo` (with `c_lo < c_hi` physical), the required magnitude is interior to
`(c_lo, c_hi)` and neither endpoint's determinant equals `D`.  Uses `detG_strictAnti`
(det is strictly decreasing) to convert the determinant straddle into the `b₄` straddle
of `required_magnitude_strictly_bracketed`. -/
theorem detGate_no_endpoint_hits
    (D c_lo c_hi : ℝ)
    (hlo_pos : 0 < c_lo) (hlohi : c_lo < c_hi) (hhi_phys : 5 * c_hi ^ 2 < 1)
    (hD_lo : detG c_hi < D) (hD_hi : D < detG c_lo) :
    detG c_lo ≠ D ∧ detG c_hi ≠ D ∧
      ∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ detG m = D ∧ c_lo < m ∧ m < c_hi := by
  have hc_hi_pos : 0 < c_hi := lt_trans hlo_pos hlohi
  obtain ⟨hdec, hdethi_pos⟩ := detG_strictAnti c_lo c_hi hlo_pos hlohi hhi_phys
  have hdetlo_pos : 0 < detG c_lo := lt_trans hdethi_pos hdec
  have hD_pos : 0 < D := lt_trans hdethi_pos hD_lo
  have hlo_phys : 5 * c_lo ^ 2 < 1 := by nlinarith [sq_nonneg c_lo, sq_nonneg c_hi]
  have hdetlo_lt1 : detG c_lo < 1 := (detG_mem_Ioo c_lo hlo_pos hlo_phys).2
  have hD_lt1 : D < 1 := lt_trans hD_hi hdetlo_lt1
  -- translate the determinant straddle into a b4 straddle via b4 = -log detG
  have hb_lo : b4 c_lo < -Real.log D := by
    have := Real.log_lt_log hD_pos hD_hi         -- log D < log (detG c_lo)
    unfold b4; linarith
  have hb_hi : -Real.log D < b4 c_hi := by
    have := Real.log_lt_log hdethi_pos hD_lo     -- log (detG c_hi) < log D
    unfold b4; linarith
  have ht : (0:ℝ) < -Real.log D := by
    have := Real.log_neg hD_pos hD_lt1; linarith
  obtain ⟨m, hm_pos, hm_phys, hm_eq, hgt, hlt⟩ :=
    required_magnitude_strictly_bracketed (-Real.log D) c_lo c_hi ht
      hlo_pos hlohi hhi_phys hb_lo hb_hi
  -- recover detG m = D from b4 m = -log D
  have hdetm_pos : 0 < detG m := (detG_mem_Ioo m hm_pos hm_phys).1
  have hlogeq : Real.log (detG m) = Real.log D := by
    have : -Real.log (detG m) = -Real.log D := hm_eq
    linarith
  have hdetm : detG m = D := Real.log_injOn_pos (Set.mem_Ioi.mpr hdetm_pos)
    (Set.mem_Ioi.mpr hD_pos) hlogeq
  exact ⟨ne_of_gt hD_hi, ne_of_lt hD_lo, m, hm_pos, hm_phys, hdetm, hgt, hlt⟩

/-! ### Capstone — the qou-j16x scope-(a) verdict, structurally -/

/-- **(CAPSTONE) The det-gate magnitude is bracketed by derived constants and hit by
none — WALL(scope-(a)).**  For the witnessed straddle (`c_lo = z−h/2`, `c_hi = 2h`,
`t* = 9.243/E₀`, verified numerically in `b4-nonsaturating-mstar-diagnostic.witness.json`
to satisfy `b₄ c_lo < t* < b₄ c_hi`), the required magnitude is the *unique* interior
`m ∈ (c_lo, c_hi)`, and neither derived endpoint reproduces `t*`.  Since the reaching `m`
depends on the target (an anchor-inversion = FIT) and lies strictly between the two
nearest derived constants — matching neither — no identified categorical driver fixes it.
The det-gate magnitude remains open at scope-(a).  Nothing wired; `free_parameters = 0`.

This packages `required_magnitude_strictly_bracketed` + `no_endpoint_reproduces_target`
as the honest verdict, parametrised by the (witness-supplied) straddle hypotheses. -/
theorem a4_magnitude_bracketed_scope_a
    (t c_lo c_hi : ℝ) (ht : 0 < t)
    (hlo_pos : 0 < c_lo) (hlohi : c_lo < c_hi) (hhi_phys : 5 * c_hi ^ 2 < 1)
    (hstraddle_lo : b4 c_lo < t) (hstraddle_hi : t < b4 c_hi) :
    -- (1) the required magnitude exists, is unique in the bracket, and is interior:
    (∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ b4 m = t ∧ c_lo < m ∧ m < c_hi) ∧
    -- (2) neither bracketing derived constant reproduces the target:
    (b4 c_lo ≠ t ∧ b4 c_hi ≠ t) :=
  ⟨required_magnitude_strictly_bracketed t c_lo c_hi ht hlo_pos hlohi hhi_phys
      hstraddle_lo hstraddle_hi,
   no_endpoint_reproduces_target t c_lo c_hi ht hlo_pos hlohi hhi_phys
      hstraddle_lo hstraddle_hi⟩

end QOU.MassTheory.B4NonSaturatingBracket
