import Mathlib.Data.Rat.Defs
import Mathlib.Algebra.Ring.Parity
import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Tactic

/-!
# The bar-odd D-ladder 2-adic parity grading — verified anchor + open target

The bar-odd `S = h·D(ũ)` ladder has exact coefficients `d_k = a_k + b_k√3 ∈ ℚ(√3)`
(the `ser_sqrt`/`ser_div` construction in
`computations/qbeta/qbeta_dladder_generating_function_structure_probe.py`; witness
`qbeta-barodd-d-ladder-ord17`). Result 2 of
`docs/audits/2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`
found an **exact 2-adic parity grading** of the `√3`-component:

  the 2-adic valuation of `den(b_k)` vanishes **iff `k` is odd**

— equivalently the reduced denominator `den(b_k)` is **odd iff `k` is odd** — the
arithmetic shadow of the sinh/cosh (bar-odd/bar-even) split
(`QOU.QBeta.bar_parity_decomposition`). Structural origin (audit §"Structural
origin"): the `√3` is the Hoefsmit `b = √(q⁴+q²+1)/(q²+1)` (`q⁴+q²+1 = 3` at the
branch point), the 2-powers come from `(q²+1)`, the `½` in `α`, and `2q³` in `Q_A`;
the bar-odd projection `φ : ũ ↦ −ũ` sorts them by ũ-parity.

This file provides, per the **formalize-first** discipline:

1. a **sorry-free verified anchor** — the grading holds for the first exact
   coefficients, machine-checked by `decide` on their exact reduced denominators
   (as ℕ — ℚ-division does not kernel-reduce under `decide`);
2. the **open target** as a §3b conjecture class carrying the real content (the
   grading law for the full sequence) — *not* proved: the general proof needs the
   `ser_sqrt`/`ser_div` construction formalized, which is not yet in Lean. Per the
   anti-laundering rule, axiomatizing the class is **not** a proof of the law.

-- Ref: [leitner2026] docs/audits/2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md
-/

namespace QOU.QBeta.DLadderTwoAdicGrading

/-- The exact `√3`-component `b_k` of the bar-odd D-ladder `d_k = a_k + b_k√3`,
    tabulated from the exact ℚ(√3) compute. This is an **illustrative sample** —
    the first five values, kept in full so a reader can check `bDen` against real
    fractions; `bDen` itself carries all 21 committed orders. The full sequence is
    the `ser_sqrt`/`ser_div` build, not yet in Lean. Indices `0` and `> 5` pad
    with `0`. -/
def bComp : ℕ → ℚ
  | 1 => -1
  | 2 => 5 / 288
  | 3 => -676 / 27
  | 4 => 15055 / 1741824
  | 5 => -252241 / 243
  | _ => 0

/-- The **reduced denominators** `den(b_k)` of the exact D-ladder coefficients,
    `k = 1 … 21`, as ℕ data from the compute. Kept as explicit ℕ so the grading is
    a pure decidable ℕ fact (ℚ-division does not kernel-reduce under `decide`).

    **Provenance.** Each entry is `Fraction(b_k).denominator` for the exact
    `b_k ∈ ℚ` recorded in
    `computations/qbeta/qbeta-dladder-generating-function-structure.witness.json`,
    field `data.b_k_sqrt3_coeff` (21 orders, `ORD = 43`). The denominators were
    recomputed from those exact fractions rather than copied from the witness's
    own `v2_den_b` field, so the two are an independent cross-check of each other
    and they agree at every order.

    Sample, matching `bComp`: `b₁` den 1; `b₂ = 5/288` den `288 = 2⁵·3²`;
    `b₃ = -676/27` den 27; `b₄ = 15055/1741824` den `1741824 = 2¹⁰·3⁴·…`;
    `b₅ = -252241/243` den `243 = 3⁵`. -/
def bDen : ℕ → ℕ
  | 1 => 1
  | 2 => 288
  | 3 => 27
  | 4 => 1741824
  | 5 => 243
  | 6 => 827714764800
  | 7 => 32805
  | 8 => 3286780084224000
  | 9 => 2657205
  | 10 => 24215354899944387379200
  | 11 => 167403915
  | 12 => 213767192353964450088222720000
  | 13 => 4519905705
  | 14 => 62426860717512946288163857367040000
  | 15 => 122037454035
  | 16 => 42428041325493368867072836676364533760000000
  | 17 => 12081707949465
  | 18 => 1919403858645647533912262741315522197349990400000000
  | 19 => 12722038470786645
  | 20 => 5051932376878820969978160727550176520135489932492800000000
  | 21 => 343495038711239415
  | _ => 0

/-- **2-adic parity grading predicate.** The reduced denominator is odd
    (equivalently `v₂(den) = 0`) exactly on odd indices `1 ≤ k ≤ K`. -/
def TwoAdicParityGraded (den : ℕ → ℕ) (K : ℕ) : Prop :=
  ∀ k, 1 ≤ k → k ≤ K → (Odd (den k) ↔ Odd k)

/-- **Verified anchor (sorry-free).** The 2-adic parity grading holds for **all
    21 committed exact D-ladder coefficients**: `den(b_k)` is odd iff `k` is odd.

    Extended from `K = 5` to `K = 21` on 2026-08-19. The `k = 21` data was already
    committed and the previous docstring already said "compute extends this to
    `k=21`" — the formalized window simply had not caught up with it. Nothing new
    was computed; the denominators were re-derived from the committed exact
    fractions and cross-checked against the witness's own valuation field.

    This is evidence, not a proof: `DLadderGradingConjecture` below remains the
    open target, and 21 orders of `decide` do not establish a law for all `k`. -/
theorem bDen_two_adic_graded : TwoAdicParityGraded bDen 21 := by
  intro k hk1 hk21
  interval_cases k <;> decide

/-- The `K = 5` window, as a corollary of the extended anchor. Retained because
    the audit and the surrounding prose cite the five-term result by name. -/
theorem bDen_two_adic_graded_five : TwoAdicParityGraded bDen 5 :=
  fun k hk1 hk5 => bDen_two_adic_graded k hk1 (hk5.trans (by norm_num))

/-- **Contrast: p = 3 is NOT graded (sorry-free).** `3` divides `den(b_k)` at
    both an **even** index (`k=2`, den `288 = 2⁵·3²`) and an **odd** index
    (`k=3`, den `27 = 3³`), so no parity rule `3 ∣ den(b_k) ⟺ (parity of k)`
    can hold — unlike `2`, whose grading is `bDen_two_adic_graded`. Together they
    witness that **`2` is the *unique* graded prime**: only the prime of the ℤ/2
    bar-involution sees the parity grading (p=3 is factorial-smooth growth on both
    parities). -/
theorem three_not_parity_graded : 3 ∣ bDen 2 ∧ 3 ∣ bDen 3 := by decide

/-- **Open target (§3b conjecture class).** The full bar-odd D-ladder
    `√3`-component `b : ℕ → ℚ` (the `ser_sqrt`/`ser_div` object) is 2-adically
    parity-graded for **all** `k ≥ 1`. Content-bearing (a parameter-quantified
    equivalence in the shape of the claim, not `True`); the class instance is the
    single open input. Proving it needs the D-ladder construction in Lean —
    axiomatizing this class is **not** a proof of the law (anti-laundering). -/
class DLadderGradingConjecture where
  b : ℕ → ℚ
  /-- The 2-adic parity grading, for all `k ≥ 1`. Machine-verified for
      `k ≤ 21` by `bDen_two_adic_graded`; open beyond. -/
  graded : ∀ k, 1 ≤ k → (Odd (b k).den ↔ Odd k)

/-- Conditional consequence (§3b-cond): *given* the grading class, the finite
    window predicate holds at every `K` — the anchor theorem is the `K=5`
    instance of what the class asserts unconditionally. Derives the conclusion
    from the class hypothesis (not a self-assuming projection). -/
theorem graded_window [G : DLadderGradingConjecture] (K : ℕ) :
    TwoAdicParityGraded (fun k => (G.b k).den) K := by
  intro k hk1 _; exact G.graded k hk1

/-- **q-Borel scalar-transport invariance of the grading gap (sorry-free).**
    Every member of the scalar acceleration family — classical Borel `÷k!`,
    Borel–Leroy `÷(k!)^s` (integer `s`), Jackson q-Borel `÷[k]_Q!` /
    `÷(Q;Q)_k` — acts diagonally on the ℚ(√3) components of
    `d_k = a_k + b_k√3`: both are divided by the *same* scalar `f ∈ ℚ^×`.
    Since `padicValRat p` is a valuation, the signed component gap
    `v_p(a_k) − v_p(b_k)` is exactly invariant under the whole family: the
    ℤ/2 bar-parity grading (gap form) survives into every accelerated
    plane — the invariant is *permissive*, it obstructs no resummation
    shape. Compute twin (exact, k ≤ 21, six bases):
    `computations/qbeta/qbeta_dladder_qborel_2adic_transport_probe.py`
    (witness `qbeta-dladder-qborel-2adic-transport`). -/
theorem gap_invariant_under_scalar_transform (p : ℕ) [Fact p.Prime]
    (a b f : ℚ) (ha : a ≠ 0) (hb : b ≠ 0) (hf : f ≠ 0) :
    padicValRat p (a / f) - padicValRat p (b / f)
      = padicValRat p a - padicValRat p b := by
  rw [padicValRat.div (p := p) ha hf, padicValRat.div (p := p) hb hf]
  ring

end QOU.QBeta.DLadderTwoAdicGrading
