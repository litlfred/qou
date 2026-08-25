/-
  Does the Gröbner–Shirshov (GS) "jet-order" valuation / Lusztig a-function
  `n(λ)` FORCE the single-degree (top-cohomology) concentration that makes
  `Δ_λ = (-1)^{n(λ)}·dim V_λ`?
  — the SOLE remaining crux left open by PRs #4553 → #4559 → #4570.
  Epic `qou-r2nh`, bean `qou-71ma`.

  Where the crux comes from (all sorry-free).

    • #4553 (`DeltaLambdaDTIndex`): `Δ_λ` is the graded Euler characteristic of
      the SINGLE-DEGREE Springer object `G_λ = V_λ` concentrated in degree
      `n(λ)` — `Σ_i (-1)^i (G_λ)_i = (-1)^{n(λ)}·dim V_λ = Δ_λ`.

    • #4559 (`DeltaLambdaDTModuliUnderdetermined`): matching `Δ_λ` as a
      Behrend-signed DT COUNT under-determines the moduli (pins only parity +
      count `dim V_λ`).  The single-degree concentration is the load-bearing
      residual.  **Count route dead.**

    • #4570 (`DeltaLambdaTopDegreeConcentration`, `sdp_cannot_force_top_degree`):
      the confinement SDP / canonical `T_w` / `tr_M` are functionals of the
      UNGRADED Wedderburn dim `dim V_λ` alone — no cohomological-degree variable —
      so they cannot force the top-degree object.  **SDP route dead.**  Its audit
      names the PRECISE next obstruction:

        > whether the a-function = GS jet-order valuation that already supplies
        > the grade VALUE `n(λ)` can be promoted to SELECT the single graded
        > degree.  That map, not the SDP, is where a substrate-derivation must
        > now be attempted.

  THE crux (bean `qou-71ma`).  Does the GS jet-order valuation FORCE the
  single-degree selection?

  Corpus fact fixing the setup (`docs/audits/2026-07-11-deltalambda-grho-jet-order-derivation.md`;
  `PrincipalGradingJetOrder.lean`).  The GS jet-order valuation is, by the
  classical fake-degree/principal-specialisation theorem (Steinberg / Lusztig;
  Macdonald I.5),

        `n(λ) = min_{T ∈ SYT(λ)} maj(T)`
              = the LOWEST jet-order (= q-adic VALUATION of the fake-degree
                polynomial `f_λ(q) = Σ_T q^{maj T}`) at which `V_λ` enters.

  So the jet-order structure supplies a VALUATION — the bottom grade `n(λ)` — and
  its parity `(-1)^{n(λ)}` is the (already-derived, sorry-free
  `deltaSign_eq_nStat_parity`) chirality sign.  The question is whether that
  VALUATION also forces the CONCENTRATION of the full `dim V_λ` at that one grade.

  Answer proved here (NEGATIVE, sharply bounded — scope-(a) LIMITATIVE).  NO.
  A valuation is degree-BLIND: it reads only the bottom grade, not the shape above
  it.  We formalize this at the `n = 5` anchor by exhibiting, for every block, TWO
  graded objects that AGREE on everything the jet-order valuation + Wedderburn data
  can read — the SAME valuation `n(λ)` AND the SAME ungraded dimension `dim V_λ` —
  yet DIFFER in signed Euler characteristic, with only the concentrated one equal
  to `Δ_λ`:

    • `G_λ = singleCoeffs` — `dim V_λ` concentrated in the single degree `n(λ)`
      (Euler char `(-1)^{n(λ)}·dim = Δ_λ`);
    • `H_λ = fakeCoeffs`   — the honest jet-order/coinvariant graded object
      (graded dims = coefficients of the fake-degree polynomial `f_λ(q)`; Euler
      char `f_λ(-1) ≠ Δ_λ` on every non-trivial block).

  THE SHARP MECHANISM (`fakeCoeff_at_valuation_eq_one`).  At the valuation degree
  `n(λ)` the honest graded object `H_λ` carries coefficient **1** — the MONIC
  leading term of `f_λ(q)` at `q^{n(λ)}` — NOT `dim V_λ`.  So "read the object off
  at the a-function grade" recovers magnitude `1`, never `dim`; recovering the full
  `dim V_λ` there is an AD-HOC collapse of all the higher-grade mass, not any
  operation the valuation performs.  The valuation fixes WHERE the bottom is; it is
  silent about the shape above it.  (The two dim-1 blocks are monomials, so there
  `1 = dim` and concentration is vacuous — hence the `dim ≠ 1` hypothesis.)

  Reading / verdict.  The GS jet-order valuation supplies the grade VALUE `n(λ)`
  (hence, via its parity, the derived chirality SIGN) but does NOT force the
  single-degree SELECTION: the concentration `H^{top}(𝓑_λ) = V_λ` is a genuinely
  INDEPENDENT input, invisible to any functional of `(valuation, ungraded dim)` —
  exactly the data the promoted a-function + Wedderburn algebra provide.  This is
  the third and last of the candidate forcing mechanisms to fall (count #4559 /
  SDP #4570 / jet-order valuation, here), so — as a scope-(a) limitative fact —
  none of the QOU driver-level maps that were on the table force the concentration.

  IMPORTANT (anti-fake-closure, and the honest positive it does NOT threaten).
  This NEGATIVE does not reopen `Δ_λ`'s VALUE.  `Δ_λ = (-1)^{n(λ)}·dim V_λ` is a
  function of two substrate SCALARS — the jet-order valuation parity (sorry-free
  `deltaSign_eq_nStat_parity`) and the Wedderburn dimension — both substrate-derived
  without any graded/geometric object.  It is only the DT/Springer GEOMETRIC
  categorification (a single-degree cohomology object) whose concentration is the
  independent input; the algebraic two-scalar formula for the NUMBER stands on its
  own legs.  So the crux is answered NEGATIVELY for the geometric-realization
  program while leaving the number's derivation untouched.

  Scope / discipline (STRICT).  Nothing fitted; `Δ_λ`, AME, CODATA, `q₀` never
  inverted; the fake-degree polynomials `f_λ(q)` are the standard coinvariant
  graded dimensions (hook-length; `f_λ(1) = dim V_λ` machine-checked).  No `sorry`,
  no `True`-conclusion, no `native_decide` (the `decide`s discharge genuinely-finite
  concrete integer computations at `n = 5`; base ring `ℤ` / `ℕ`, §7c — no
  archimedean construct).  No instance of the open realization conjecture is
  fabricated: the proved content is LIMITATIVE (the valuation does not force the
  concentration), not a closure.  Companion, ungraded-side: #4570
  `sdp_cannot_force_top_degree`.  Converges with #4554 (`A_ω=3` structurally-open).

  Primary sources:
  Macdonald, Symmetric Functions and Hall Polynomials, 2nd ed., OUP 1995, §I.5
    (fake degree `R_λ(q) = Σ_T q^{maj T}`, lowest term `q^{n(λ)}`).
  Springer, A construction of representations of Weyl groups,
    Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165
  -- Ref: [macdonald1995] Macdonald, Symmetric Functions and Hall Polynomials
  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
-/
import QOU.BraidsAndKnots.DeltaLambdaTopDegreeConcentration

namespace QOU.BraidsAndKnots

/-! ## Graded objects reused from `DeltaLambdaTopDegreeConcentration` (#4570)

    `gradedEuler` / `gradedEulerAux`, `PartitionOf5.singleCoeffs` / `fakeCoeffs`,
    the ungraded-dimension lemmas (`singleTotalDim_eq_dim`, `fakeTotalDim_eq_dim`,
    `same_ungraded_dim`), and the two signed-Euler-characteristic facts
    (`single_gradedEuler_eq_deltaLambda`, `fake_gradedEuler_ne_deltaLambda`) all
    live in `#4570` (same `QOU.BraidsAndKnots` namespace) and are imported, NOT
    redeclared here (they would collide in the `QOU` umbrella).  This file adds
    only the jet-order VALUATION and the degree-blindness crux. -/

/-! ## Jet-order valuation of a graded object

    The valuation = the LOWEST degree carrying nonzero dimension = the number of
    leading zeros.  This is exactly what the GS jet-order structure reads off a
    graded object: the bottom grade `n(λ)` at which the block enters.  It is
    manifestly degree-BLIND above the bottom (any rearrangement of the nonzero
    tail leaves it fixed). -/
def valuation : List ℕ → ℕ
  | [] => 0
  | c :: cs => if c = 0 then valuation cs + 1 else 0

/-! ## Both objects carry the SAME jet-order valuation `n(λ)`

    THE new content beyond #4570: the honest graded object `H_λ` and the
    concentrated object `G_λ` share not only the ungraded dimension but also the
    jet-order VALUATION `n(λ)`.  Hence adding the a-function/jet-order valuation to
    the SDP's ungraded data (#4570) still does not separate them. -/

theorem PartitionOf5.single_valuation_eq_nStat (p : PartitionOf5) :
    valuation p.singleCoeffs = p.nStat := by cases p <;> decide

theorem PartitionOf5.fake_valuation_eq_nStat (p : PartitionOf5) :
    valuation p.fakeCoeffs = p.nStat := by cases p <;> decide

theorem PartitionOf5.same_valuation (p : PartitionOf5) :
    valuation p.singleCoeffs = valuation p.fakeCoeffs := by
  rw [p.single_valuation_eq_nStat, p.fake_valuation_eq_nStat]

/-! ## THE SHARP MECHANISM: at the valuation grade the honest object reads `1`, not `dim`

    The single-degree object puts `dim V_λ` at degree `n(λ)`; the honest
    fake-degree object puts `1` (the monic leading coefficient of `f_λ(q)`) there.
    So the valuation cannot be "read off × dim" to recover the concentrated object:
    at its own grade the natural object has magnitude `1`, and the missing
    `dim − 1` sits spread across higher grades.  This is WHY a valuation cannot
    force concentration. -/

/-- `H_λ` carries coefficient `1` at the valuation degree `n(λ)` — the monic
    leading term of the fake-degree polynomial. -/
theorem PartitionOf5.fakeCoeff_at_valuation_eq_one (p : PartitionOf5) :
    (p.fakeCoeffs).getD p.nStat 0 = 1 := by cases p <;> decide

/-- `G_λ` carries coefficient `dim V_λ` at the valuation degree `n(λ)`. -/
theorem PartitionOf5.singleCoeff_at_valuation_eq_dim (p : PartitionOf5) :
    (p.singleCoeffs).getD p.nStat 0 = p.dim := by cases p <;> decide

/-- On every non-trivial block the two objects DIFFER at the valuation grade
    (`1 ≠ dim V_λ`): concentrating `dim` at `n(λ)` is not what the natural graded
    object does. -/
theorem coeff_at_valuation_differs (p : PartitionOf5) (h : p.dim ≠ 1) :
    (p.singleCoeffs).getD p.nStat 0 ≠ (p.fakeCoeffs).getD p.nStat 0 := by
  rw [p.singleCoeff_at_valuation_eq_dim, p.fakeCoeff_at_valuation_eq_one]
  exact h

/-! ## THE CRUX: the GS jet-order valuation cannot force single-degree selection

    (`single_gradedEuler_eq_deltaLambda` and `fake_gradedEuler_ne_deltaLambda`,
    used just below, are the two signed-Euler facts imported from #4570.) -/

/-- **THE CRUX (limitative — bean `qou-71ma`).**  There exist two graded
    assignments `single = G_λ` and `fake = H_λ` such that:

      • they carry the SAME jet-order VALUATION `n(λ)` at every block (`val`) —
        the bottom grade the GS jet-order structure supplies;
      • they carry the SAME ungraded Wedderburn dimension `dim V_λ` at every
        block (`dim`) — the datum the confinement SDP / `T_w` / `tr_M` read (#4570);
      • yet their signed Euler characteristics DIFFER on every non-trivial block
        (`differ`), with only the concentrated object equal to `Δ_λ` (`is_delta`).

    Since the promoted a-function supplies exactly `(valuation, ungraded dim)` and
    both objects share BOTH, no functional of that data — in particular the GS
    jet-order valuation — can distinguish, hence cannot FORCE, the single-degree
    (top-cohomology) concentration.  The concentration `H^{top}(𝓑_λ) = V_λ` is a
    genuinely INDEPENDENT input.  This is the NEGATIVE answer to `qou-71ma`: the
    jet-order valuation supplies the grade VALUE, never the single-degree
    SELECTION.  Companion (ungraded side): #4570 `sdp_cannot_force_top_degree`. -/
theorem jetorder_valuation_cannot_force_single_degree :
    ∃ single fake : PartitionOf5 → List ℕ,
      -- same jet-order valuation n(λ) (the bottom grade the GS structure gives):
      (∀ p : PartitionOf5, valuation (single p) = valuation (fake p)) ∧
      -- same ungraded Wedderburn dimension (all the SDP / T_w / tr_M can read):
      (∀ p : PartitionOf5, (single p).sum = (fake p).sum) ∧
      -- but different signed Euler characteristics on every non-trivial block:
      (∀ p : PartitionOf5, p.dim ≠ 1 →
          gradedEuler (single p) ≠ gradedEuler (fake p)) ∧
      -- and only the single-degree (top-cohomology) object equals Δ_λ:
      (∀ p : PartitionOf5, gradedEuler (single p) = p.deltaLambda) :=
  ⟨PartitionOf5.singleCoeffs, PartitionOf5.fakeCoeffs,
    fun p => p.same_valuation,
    fun p => p.same_ungraded_dim,
    fun p h => by
      have hs := p.single_gradedEuler_eq_deltaLambda
      have hf := p.fake_gradedEuler_ne_deltaLambda h
      rw [hs]; exact fun hbad => hf hbad.symm,
    fun p => p.single_gradedEuler_eq_deltaLambda⟩

/-! ## Degree-blindness is generic (not an `n = 5` artifact)

    A valuation reads only the bottom grade; knowing it, together with the total
    (ungraded) dimension, never pins the signed Euler characteristic.  Witnesses:
    `[d+2]` vs `[d+1, 1]` — same valuation `0`, same total `d+2`, Euler chars
    `d+2` vs `d` differ, for every `d`. -/
theorem gradedEuler_singleton (a : ℕ) : gradedEuler [a] = (a : ℤ) := by
  simp [gradedEuler, gradedEulerAux]

theorem gradedEuler_pair (a b : ℕ) : gradedEuler [a, b] = (a : ℤ) - (b : ℤ) := by
  have h : gradedEuler [a, b] = (a : ℤ) + (-1 : ℤ) * (b : ℤ) := by
    simp [gradedEuler, gradedEulerAux]
  rw [h]; omega

theorem valuation_and_totalDim_do_not_determine_gradedEuler (d : ℕ) :
    ∃ L₁ L₂ : List ℕ,
      valuation L₁ = valuation L₂ ∧ L₁.sum = L₂.sum ∧
      gradedEuler L₁ ≠ gradedEuler L₂ := by
  refine ⟨[d + 2], [d + 1, 1], by simp [valuation], ?_, ?_⟩
  · simp only [List.sum_cons, List.sum_nil]; omega
  · rw [gradedEuler_singleton, gradedEuler_pair]; push_cast; omega

end QOU.BraidsAndKnots
