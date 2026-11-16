import Mathlib.Tactic

/-!
# The body-order recurrence: depth ≥ 3 is forced, and three terms cannot test it

`thm:binding-closure-conditional` writes the per-isotope binding as a body-order
series `B(K) = m_e ∑_n a_D^(n)`, and `prop:prolonged-periods-fixed-depth` proves
— by Cayley–Hamilton on the jet-prolongation operator `M` acting on the
Gauss–Manin period space `V` of the SW family over Bring's surface — that the
periods satisfy a depth-`d` linear recurrence with `n`-independent kernel,

    a^(n+d) = ∑_{j<d} c_j · a^(n+j)   for every n,     d ≤ rank V ≤ 2g = 8.

The **identification half** (that `d` and `c` are the Bring Picard–Fuchs
operator) is open, and bean `qou-i5yp` proposes to test it against the measured
body-order ratio

    a₂ : a₃ : a₄ = 1 : −0.519787 : +4.45038

(convention D, proton pin, `he4_body_order_shortfall_location_probe.py`,
2026-08-29). This file establishes what such a test can and cannot decide,
*before* the Picard–Fuchs computation is attempted.

## Results

Write `B_n = m_e · a^(n)` for the `n`-body term (obligation (B) of
`thm:binding-closure-conditional`). A system of zero or one nucleon has no
binding, so `B₀ = B₁ = 0`, hence `a⁰ = a¹ = 0`; the deuteron binds, so
`a² ≠ 0`.

* `eq_zero_of_initial_eq_zero` — a depth-`d` recurrence whose first `d` terms
  vanish is identically zero. (Strong induction; no hypotheses on `c`.)
* `three_le_depth` — therefore **`d ≥ 3` is forced**. The depth is not merely
  bounded above by the rank; it is bounded *below* by the vanishing of the
  one-body term.
* `depth_three_kernel_reaches` — at `d = 3`, the map `(c₁, c₂) ↦ (a³, a⁴)` is
  **surjective**: for a nonzero `a²`, *every* pair of 3- and 4-body values is
  realised by some kernel. So the three-term ratio above **cannot falsify the
  identification**; it can only solve for `c₁` and `c₂`. Using it as a target is
  an anchor inversion, i.e. a fit.
* `a_five_free` / `a_six` — `c₀` is still unconstrained after `a³` and `a⁴`, so
  `a⁵` is free too, and `a⁶` is the first value the kernel determines. **At
  depth `d` the first genuine prediction sits at body order `2d`**, hence at
  body order ≥ 6 here — requiring `A ≥ 6` (⁶Li), not the `A ≤ 4` the measurement
  covers.

## The dichotomy with S₅-equivariance

`QOU/ArchimedeanUniverse/s5_bring_hodge_depth.lean` proves (sorry-free) that
`χ_{H¹} = 2·χ_{W₍₄,₁₎}` with `W₍₄,₁₎` irreducible, i.e. `H¹(Bring) ≅ W₍₄,₁₎^{⊕2}`
as an `S₅`-representation. By Schur, an `S₅`-equivariant endomorphism of
`W^{⊕2}` is an element of the `2 × 2` matrix algebra over the multiplicity
space, so it satisfies a degree-≤ 2 characteristic polynomial — i.e. `d ≤ 2`.

`no_equivariant_prolongation` records the consequence: `d ≤ 2` is inconsistent
with the vanishing one-body term. So **at least one of the following fails**:
the prolongation operator `M` is `S₅`-equivariant; the operator-power index is
the body order (obligation (B)); or the one-body binding term vanishes. This is
a **scope-(b) structural exclusion of the conjunction**, citing Schur's lemma
and `eq_zero_of_initial_eq_zero` — it is *not* a refutation of the
prolongation-symbol conjecture, which survives with a non-equivariant `M`.

Everything here is stated over a generic ring or field per AGENTS.md §7c; no
archimedean construct appears, and the measured ratio enters only as an explicit
rational in `measured_target_reachable`, never as a hypothesis.
-/

namespace QOU.MassTheory.BodyOrderRecurrenceDepth

variable {R : Type*}

/-- A depth-`d` linear recurrence with `n`-independent kernel `c`:
`a (n + d) = ∑_{j < d} c j * a (n + j)` for every `n`. This is the shape
`prop:prolonged-periods-fixed-depth` derives from Cayley–Hamilton on the
prolongation operator. -/
def IsDepthRecurrence [Semiring R] (d : ℕ) (c a : ℕ → R) : Prop :=
  ∀ n, a (n + d) = ∑ j ∈ Finset.range d, c j * a (n + j)

section Semiring

variable [Semiring R] {d : ℕ} {c a : ℕ → R}

/-- A depth-`d` recurrence whose first `d` terms all vanish is identically zero.
No hypothesis on the kernel: the vanishing propagates through any `c`. -/
theorem eq_zero_of_initial_eq_zero (h : IsDepthRecurrence d c a)
    (h0 : ∀ j, j < d → a j = 0) : ∀ n, a n = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    by_cases hn : n < d
    · exact h0 n hn
    · push_neg at hn
      obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
      rw [add_comm d m, h m]
      refine Finset.sum_eq_zero fun j hj => ?_
      have hjd : j < d := Finset.mem_range.mp hj
      have hlt : m + j < d + m := by omega
      rw [ih (m + j) hlt, mul_zero]

/-- **Depth ≥ 3 is forced.** A vanishing zero- and one-body term together with a
nonzero two-body term put a *lower* bound on the recurrence depth. -/
theorem three_le_depth (h : IsDepthRecurrence d c a)
    (h0 : a 0 = 0) (h1 : a 1 = 0) (h2 : a 2 ≠ 0) : 3 ≤ d := by
  by_contra hd
  push_neg at hd
  refine h2 (eq_zero_of_initial_eq_zero h (fun j hj => ?_) 2)
  have hj2 : j < 2 := by omega
  interval_cases j
  · exact h0
  · exact h1

/-- The `S₅`-equivariance dichotomy: an equivariant prolongation operator on
`H¹(Bring) ≅ W₍₄,₁₎^{⊕2}` has `d ≤ 2` by Schur, which is inconsistent with the
vanishing one-body term. See the module docstring. -/
theorem no_equivariant_prolongation (h : IsDepthRecurrence d c a)
    (h0 : a 0 = 0) (h1 : a 1 = 0) (h2 : a 2 ≠ 0) (hd : d ≤ 2) : False := by
  have := three_le_depth h h0 h1 h2
  omega

end Semiring

section DepthThree

variable [CommRing R] {c a : ℕ → R}

/-- At depth 3 with vanishing 0- and 1-body terms, `a³` is `c₂ · a²`. -/
theorem a_three (h : IsDepthRecurrence 3 c a) (h0 : a 0 = 0) (h1 : a 1 = 0) :
    a 3 = c 2 * a 2 := by
  have h' := h 0
  simp [Finset.sum_range_succ, h0, h1] at h'
  simpa using h'

/-- At depth 3 with a vanishing one-body term, `a⁴ = c₁ · a² + c₂ · a³`. -/
theorem a_four (h : IsDepthRecurrence 3 c a) (h1 : a 1 = 0) :
    a 4 = c 1 * a 2 + c 2 * a 3 := by
  have h' := h 1
  simp [Finset.sum_range_succ, h1] at h'
  simpa using h'

/-- `a⁵` involves `c₀`, which `a³` and `a⁴` leave unconstrained. -/
theorem a_five (h : IsDepthRecurrence 3 c a) :
    a 5 = c 0 * a 2 + c 1 * a 3 + c 2 * a 4 := by
  have h' := h 2
  simpa [Finset.sum_range_succ] using h'

/-- `a⁶` is the first value determined by earlier terms once the whole kernel is
pinned — the first genuinely falsifiable body order at depth 3. -/
theorem a_six (h : IsDepthRecurrence 3 c a) :
    a 6 = c 0 * a 3 + c 1 * a 4 + c 2 * a 5 := by
  have h' := h 3
  simpa [Finset.sum_range_succ] using h'

/-- Closed-form expression for `a 4` as a polynomial in the kernel coefficients
multiplying `a 2` when `a 0 = 0` and `a 1 = 0` (`bean qou-i5yp`). -/
theorem a_four_in_terms_of_a_two (h : IsDepthRecurrence 3 c a)
    (h0 : a 0 = 0) (h1 : a 1 = 0) :
    a 4 = (c 1 + c 2 ^ 2) * a 2 := by
  rw [a_four h h1, a_three h h0 h1]
  ring

/-- Closed-form expression for `a 5` as a polynomial in the kernel coefficients
multiplying `a 2` when `a 0 = 0` and `a 1 = 0` (`bean qou-i5yp`). -/
theorem a_five_in_terms_of_a_two (h : IsDepthRecurrence 3 c a)
    (h0 : a 0 = 0) (h1 : a 1 = 0) :
    a 5 = (c 0 + 2 * c 1 * c 2 + c 2 ^ 3) * a 2 := by
  rw [a_five h, a_four_in_terms_of_a_two h h0 h1, a_three h h0 h1]
  ring

end DepthThree

section Reachability

variable {R : Type*} [Field R]

/-- **The three-term target carries no information.** For a nonzero two-body
term, every pair of 3- and 4-body values is realised by some depth-3 kernel, via
`c₂ = t₃/a₂` and `c₁ = (t₄ − t₃²/a₂)/a₂`. Matching the measured ratio therefore
*solves for* the kernel rather than testing it. -/
theorem depth_three_kernel_reaches {a2 : R} (ha2 : a2 ≠ 0) (t3 t4 : R) :
    ∃ c1 c2 : R, c2 * a2 = t3 ∧ c1 * a2 + c2 * t3 = t4 := by
  refine ⟨(t4 - t3 * t3 / a2) / a2, t3 / a2, by field_simp, ?_⟩
  field_simp
  ring

/-- `c₀` remains free after `a³` and `a⁴` are fixed, so `a⁵` is reachable too. -/
theorem a_five_free {a2 a3 a4 : R} (ha2 : a2 ≠ 0) (c1 c2 t5 : R) :
    ∃ c0 : R, c0 * a2 + c1 * a3 + c2 * a4 = t5 := by
  refine ⟨(t5 - c1 * a3 - c2 * a4) / a2, ?_⟩
  field_simp
  ring

/-- The measured body-order target of 2026-08-29, normalised to `a₂ = 1`:
`a₃ = −0.519787`, `a₄ = +4.45038`. It is reachable, hence not a test. -/
theorem measured_target_reachable :
    ∃ c1 c2 : ℚ, c2 * 1 = (-519787 / 1000000 : ℚ) ∧
      c1 * 1 + c2 * (-519787 / 1000000 : ℚ) = (445038 / 100000 : ℚ) :=
  depth_three_kernel_reaches one_ne_zero _ _

/-- **Uniqueness of the inverted depth-3 kernel (`bean qou-i5yp`).**
For `a2 ≠ 0`, any two pairs `(c1, c2)` and `(c1', c2')` reproducing the same
`(t3, t4)` target coincide (`c2 = c2' ∧ c1 = c1'`), proving that matching `(a₂, a₃, a₄)`
is an exact bijection onto `(c₁, c₂)`. -/
theorem depth_three_kernel_unique {a2 t3 t4 c1 c2 c1' c2' : R} (ha2 : a2 ≠ 0)
    (h3 : c2 * a2 = t3) (h3' : c2' * a2 = t3)
    (h4 : c1 * a2 + c2 * t3 = t4) (h4' : c1' * a2 + c2' * t3 = t4) :
    c2 = c2' ∧ c1 = c1' := by
  have hc2_sub : (c2 - c2') * a2 = 0 := by linear_combination h3 - h3'
  have hc2 : c2 = c2' := by
    rcases mul_eq_zero.mp hc2_sub with h0 | h0
    · exact sub_eq_zero.mp h0
    · exact False.elim (ha2 h0)
  refine ⟨hc2, ?_⟩
  rw [hc2] at h4
  have hc1_sub : (c1 - c1') * a2 = 0 := by linear_combination h4 - h4'
  rcases mul_eq_zero.mp hc1_sub with h0 | h0
  · exact sub_eq_zero.mp h0
  · exact False.elim (ha2 h0)

end Reachability

end QOU.MassTheory.BodyOrderRecurrenceDepth
