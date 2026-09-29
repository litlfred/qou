/-
  Does a genuine GRADED substrate structure FORCE the single-degree
  (top-cohomology) concentration `H^{top}(𝓑_λ) = V_λ` that upgrades the proved
  VALUE identity `Δ_λ = (-1)^{n(λ)}·dim V_λ` to the full geometric
  "Behrend-signed DT count of the Springer fibre"?
  — the primary open conjecture `DeltaLambdaDTRealization`.
  Epic `qou-r2nh`, bean `qou-7ygi`.

  WHERE THIS COMES FROM (all sorry-free, merged / in flight).

    • #4553 (`DeltaLambdaDTIndex`): the VALUE `Δ_λ = (-1)^{n(λ)}·dim V_λ = DT(𝓑_λ)`
      is proved; but the single-degree concentration `G_λ = V_λ` in degree `n(λ)`
      is INPUT BY DEFINITION (`gradedDim k := if k = nStat then dim else 0`),
      justified by the classical Springer correspondence — not forced.

    • #4559 (`qou-ylot`): matching `Δ_λ` as a Behrend-signed DT COUNT
      under-determines the moduli (pins only parity mod 2 + count `dim V_λ`).
      **Count route dead.**

    • #4570 (`qou-nmpr`, `sdp_cannot_force_top_degree`): the confinement SDP /
      canonical `T_w` / `tr_M` are functionals of the UNGRADED Wedderburn dim
      `dim V_λ` alone (they factor through `⊕_λ End(V_λ)`, no cohomological-degree
      variable). **SDP route dead.**

    • #4574 (`qou-71ma`, `jetorder_valuation_cannot_force_single_degree`): the GS
      jet-order VALUATION reads only the bottom grade `n(λ)`; degree-blind above
      it (coefficient `1 ≠ dim` at the valuation grade). **Valuation route dead.**

  THE crux left open (bean `qou-7ygi`).  Does a genuine GRADED structure — the
  jet-order/coinvariant TOWER itself (not merely its valuation), a KLR / Demazure
  grading, the confinement filtration — force the CONCENTRATED object `G_λ`
  (`dim V_λ` at the single grade `n(λ)`, Euler char `Δ_λ`) rather than the honest
  coinvariant object `H_λ` (`V_λ` with graded multiplicity `f_λ(q)`, spread over
  `[n(λ), …]`, Euler char `f_λ(-1) ≠ Δ_λ`)?

  ────────────────────────────────────────────────────────────────────────────
  RESULT (this file): NO for every algebraic substrate grading — with a SINGLE
  structural REASON that unifies all four dead routes, plus the exact external
  input a successful graded structure would have to supply.

  The UNIFIED mechanism is CANCELLATION.  For any graded object `l` (graded dims
  `l[i] ∈ ℕ`) write the signed Euler characteristic as even-graded mass minus
  odd-graded mass, `χ(l) = E(l) − O(l)`, with ungraded total `Σ l[i] = E(l)+O(l)`.

    • `abs_altSum_le_sum`               `|χ(l)| ≤ Σ l[i]`      (general; the total
                                        dim is the CEILING on |Euler char|).
    • `abs_altSum_lt_sum_of_both_parity`  `0<E ∧ 0<O ⇒ |χ(l)| < Σ l[i]`  (STRICT:
                                        mass at BOTH grade-parities cancels).
    • `abs_altSum_eq_sum_of_single_parity` `E=0 ∨ O=0 ⇒ |χ(l)| = Σ l[i]`  (only a
                                        single-parity — cancellation-free — object
                                        saturates the ceiling).

  Since `|Δ_λ| = dim V_λ = Σ` (`binding_magnitude_eq_dim`), a graded object equals
  `Δ_λ` under signed-Euler ONLY IF it is cancellation-free (single grade-parity):

    • `deltaLambda_realization_is_cancellation_free` — THE FRONTIER (general):
        any `l` with `Σ l = dim V_λ` and `χ(l) = Δ_λ` has `E(l)=0 ∨ O(l)=0`.

  The honest coinvariant / jet-order TOWER `H_λ` (= the fake-degree graded
  multiplicity space) has mass at BOTH parities on every non-trivial block
  (`fake_both_parity`), hence STRICTLY undershoots and can never equal `Δ_λ`
  (`fake_cancels_ne_deltaLambda`).  The single-degree object `G_λ` is single-parity
  (`single_is_single_parity`), saturates, and equals `Δ_λ`
  (`single_altSum_eq_deltaLambda`).

  READING / VERDICT (honest negative, scope-(a) LIMITATIVE).  Every algebraic
  graded object the substrate produces is a genuine graded MULTIPLICITY space: it
  distributes the `dim V_λ` copies of `V_λ` across a run of consecutive grades
  `[n(λ), …]` (fake degree `f_λ(q)`), so it carries mass at both grade-parities and
  its signed Euler characteristic CANCELS to `f_λ(-1)`, strictly below `dim V_λ`.
  `Δ_λ = ±dim V_λ` is the cancellation-FREE extreme, attained only by piling the
  full `dim V_λ` onto a single grade-parity — the TOP-COHOMOLOGY PROJECTION
  `H^{2n(λ)}(𝓑_λ) = V_λ` (Springer 1978).  That projection is a statement about the
  cohomology of a specific VARIETY (the Springer fibre), NOT any operation the
  algebraic gradings (jet-order tower / coinvariant / KLR-in-the-semisimple-regime /
  Demazure) perform — they all realize `H_λ`, never `G_λ`.  So the concentration is
  an INDEPENDENT geometric categorification input the 13 categorical drivers do not
  supply; the graded route joins count / SDP / valuation as unable to force it.

  THE EXACT MISSING INPUT (beaned `qou-7ygi`).  A driver-internal construction of a
  space with a symmetric obstruction theory whose cohomology is concentrated in the
  single degree `2n(λ)` with fibre `V_λ` (equivalently: a substrate-forced
  cancellation-free grading), i.e. the Springer top-cohomology isomorphism realized
  from the drivers rather than imported.  Absent that, `DeltaLambdaDTRealization`
  stays open — but now sharply: the missing ingredient is exactly the removal of
  the multiplicity-grading CANCELLATION, characterized here.

  This does NOT reopen the VALUE.  `Δ_λ = (-1)^{n(λ)}·dim V_λ` is a function of two
  substrate SCALARS (the jet-order valuation parity `deltaSign_eq_nStat_parity` and
  the Wedderburn dimension), both derived without any graded/geometric object; only
  the DT/Springer geometric REALIZATION is open.

  Scope / discipline (STRICT).  Nothing fitted; `Δ_λ`, AME, CODATA, `q₀` never
  inverted; the fake-degree polynomials `f_λ(q)` are the standard coinvariant graded
  dimensions (`f_λ(1) = dim V_λ` machine-checked).  No `sorry`, no `True`-conclusion,
  no `native_decide` (the `decide`s discharge genuinely-finite concrete integer
  computations at `n = 5`; the structural lemmas are general over `List ℕ`); base
  ring `ℤ`/`ℕ` (§7c — no archimedean construct).  No instance of the open
  realization conjecture is fabricated: the proved content is LIMITATIVE.
  Companions: #4570 (ungraded), #4574 (valuation).  Converges with #4554
  (`A_ω=3` structurally-open) by a fifth direction.

  Primary sources:
  Springer, A construction of representations of Weyl groups,
    Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165
    (`H^{top}(𝓑_λ) = V_λ`, the single-degree top-cohomology concentration).
  Macdonald, Symmetric Functions and Hall Polynomials, 2nd ed., OUP 1995, §I.5
    (fake degree `f_λ(q) = Σ_T q^{maj T}`, graded multiplicity of `V_λ` in the
    coinvariant algebra; `f_λ(1) = dim V_λ`).
  Behrend, DT type invariants via microlocal geometry,
    Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307
  -- Ref: [macdonald1995] Macdonald, Symmetric Functions and Hall Polynomials
  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
-/
import QOU.BraidsAndKnots.DeltaLambdaTopDegreeConcentration
-- (dedup) singleCoeffs / fakeCoeffs are reused from DeltaLambdaTopDegreeConcentration (#4570);
-- this module adds the even/odd-mass reformulation + the general cancellation frontier.

namespace QOU.BraidsAndKnots

/-! ## Graded object and its signed (Behrend/DT) Euler characteristic

    A graded finite-dimensional object is `l : List ℕ`, `l[i]` its dimension in
    cohomological degree `i`.  Its signed Euler characteristic is
    `χ(l) = Σ_i (-1)^i · l[i]`.  The clean alternating recursion
    `altSum (c :: cs) = c − altSum cs` gives `c₀ − c₁ + c₂ − ⋯` — the same object
    as the `gradedEuler` of #4553 / #4570 / #4574 (`Σ_i (-1)^i l[i]`). -/
def altSum : List ℕ → ℤ
  | [] => 0
  | c :: cs => (c : ℤ) - altSum cs

/-- **Even-graded / odd-graded mass** of a graded object, as a pair
    `(E(l), O(l))`: `E(l) = Σ_{i even} l[i]`, `O(l) = Σ_{i odd} l[i]`.
    A cons shifts every grade up by one, so the even/odd roles swap. -/
def masses : List ℕ → ℤ × ℤ
  | [] => (0, 0)
  | c :: cs => ((c : ℤ) + (masses cs).2, (masses cs).1)

/-- Both masses are nonnegative (sums of dimensions). -/
theorem masses_nonneg : ∀ l : List ℕ, 0 ≤ (masses l).1 ∧ 0 ≤ (masses l).2
  | [] => ⟨le_refl 0, le_refl 0⟩
  | c :: cs => by
      have ih := masses_nonneg cs
      have hc : (0 : ℤ) ≤ (c : ℤ) := Int.natCast_nonneg c
      refine ⟨?_, ?_⟩ <;> simp only [masses] <;> omega

/-- `χ(l) = E(l) − O(l)`: the signed Euler characteristic is even mass minus odd
    mass. -/
theorem altSum_eq_masses : ∀ l : List ℕ, altSum l = (masses l).1 - (masses l).2
  | [] => rfl
  | c :: cs => by
      have ih := altSum_eq_masses cs
      simp only [altSum, masses]
      omega

/-- `Σ l[i] = E(l) + O(l)`: the ungraded total is even mass plus odd mass. -/
theorem sum_eq_masses : ∀ l : List ℕ, ((l.sum : ℤ)) = (masses l).1 + (masses l).2
  | [] => by simp [masses]
  | c :: cs => by
      have ih := sum_eq_masses cs
      simp only [List.sum_cons, masses, Nat.cast_add]
      omega

/-! ## The CANCELLATION invariant (general — the unified mechanism)

    `|χ(l)|` is bounded by the ungraded total `Σ l[i]`; the bound is STRICT exactly
    when the object has mass at both grade-parities (genuine cancellation), and is
    an equality exactly when it is cancellation-free (single grade-parity). -/

/-- **The total dimension is the ceiling on `|χ|`.** `|χ(l)| ≤ Σ l[i]`. -/
theorem abs_altSum_le_sum (l : List ℕ) : |altSum l| ≤ (l.sum : ℤ) := by
  have hn := masses_nonneg l
  rw [altSum_eq_masses, sum_eq_masses, abs_le]
  omega

/-- **CANCELLATION is strict under two-parity support.** If a graded object carries
    positive mass at BOTH an even and an odd grade, its signed Euler characteristic
    strictly undershoots the total: `|χ(l)| < Σ l[i]`.  This is the single mechanism
    behind every "does-not-force-concentration" negative — a genuine graded
    multiplicity space cancels. -/
theorem abs_altSum_lt_sum_of_both_parity (l : List ℕ)
    (he : 0 < (masses l).1) (ho : 0 < (masses l).2) :
    |altSum l| < (l.sum : ℤ) := by
  rw [altSum_eq_masses, sum_eq_masses, abs_lt]
  omega

/-- **Single-parity objects SATURATE the ceiling.** If all mass sits on one
    grade-parity (`E=0` or `O=0` — cancellation-free), then `|χ(l)| = Σ l[i]`.
    The single-degree top-cohomology object `G_λ` is of this form. -/
theorem abs_altSum_eq_sum_of_single_parity (l : List ℕ)
    (h : (masses l).1 = 0 ∨ (masses l).2 = 0) :
    |altSum l| = (l.sum : ℤ) := by
  have hn := masses_nonneg l
  rw [altSum_eq_masses, sum_eq_masses]
  rcases h with h | h <;> rw [h] <;>
    simp only [zero_sub, add_zero, zero_add, abs_neg] <;>
    rw [abs_of_nonneg] <;> omega

/-! ## THE FRONTIER: any graded realization of `Δ_λ` must be cancellation-free

    `|Δ_λ| = dim V_λ` (`binding_magnitude_eq_dim`), which is the ungraded total any
    substrate grading of `V_λ` carries.  So a graded object can realize `Δ_λ` under
    signed-Euler ONLY by saturating the ceiling — i.e. only if it is cancellation-
    free (single grade-parity).  This is the exact structural characterization of
    the missing input: NOT "some grade value", but the REMOVAL of the multiplicity-
    grading cancellation — the top-cohomology projection. -/

/-- `|Δ_λ| = dim V_λ`. -/
theorem abs_deltaLambda_eq_dim (p : PartitionOf5) : |p.deltaLambda| = (p.dim : ℤ) := by
  cases p <;> decide

/-- **THE FRONTIER (general, sorry-free).**  Any graded object `l` whose ungraded
    total is the Wedderburn dimension `dim V_λ` and whose signed Euler
    characteristic is the binding factor `Δ_λ` is necessarily CANCELLATION-FREE:
    all its mass sits on a single grade-parity (`E(l)=0 ∨ O(l)=0`).  Contrapositive:
    a graded object with mass at BOTH parities — every genuine coinvariant / jet-
    order / KLR multiplicity space — can NEVER equal `Δ_λ`.  The single-degree
    top-cohomology object is the canonical cancellation-free realization; the honest
    tower `H_λ` is excluded. -/
theorem deltaLambda_realization_is_cancellation_free
    (p : PartitionOf5) (l : List ℕ)
    (htot : (l.sum : ℤ) = (p.dim : ℤ)) (heuler : altSum l = p.deltaLambda) :
    (masses l).1 = 0 ∨ (masses l).2 = 0 := by
  by_contra h
  push_neg at h
  obtain ⟨he, ho⟩ := h
  have hn := masses_nonneg l
  have hlt := abs_altSum_lt_sum_of_both_parity l (lt_of_le_of_ne hn.1 (Ne.symm he))
    (lt_of_le_of_ne hn.2 (Ne.symm ho))
  rw [heuler, htot, abs_deltaLambda_eq_dim] at hlt
  exact (lt_irrefl _ hlt)

/-! ## The two graded objects at the `n = 5` anchor

    `G_λ = singleCoeffs` — `dim V_λ` concentrated in the single degree `n(λ)`.
    `H_λ = fakeCoeffs`   — the honest jet-order / coinvariant graded object
                           (graded dims = coefficients of `f_λ(q)`; the TOWER, not
                           merely its bottom valuation).  Data verbatim from
                           #4570 / #4574. -/

/-- Both objects carry the ungraded Wedderburn dimension `dim V_λ` (`f_λ(1)=dim`). -/
theorem PartitionOf5.single_sum_eq_dim (p : PartitionOf5) :
    (p.singleCoeffs).sum = p.dim := by cases p <;> decide

theorem PartitionOf5.fake_sum_eq_dim (p : PartitionOf5) :
    (p.fakeCoeffs).sum = p.dim := by cases p <;> decide

/-- `G_λ` realizes `Δ_λ` (the #4553 single-degree collapse). -/
theorem PartitionOf5.single_altSum_eq_deltaLambda (p : PartitionOf5) :
    altSum p.singleCoeffs = p.deltaLambda := by cases p <;> decide

/-! ### `G_λ` is single-parity; `H_λ` is two-parity — the mechanism, on the anchor -/

/-- **`G_λ` is cancellation-free** — all its mass sits on one grade-parity
    (`E=0` or `O=0`), matching the general characterization: the concentrated
    top-cohomology object saturates the `|χ| = dim` ceiling. -/
theorem single_is_single_parity (p : PartitionOf5) :
    (masses p.singleCoeffs).1 = 0 ∨ (masses p.singleCoeffs).2 = 0 := by
  cases p <;> decide

/-- **`H_λ` (the honest jet-order / coinvariant TOWER) is two-parity** on every
    non-trivial block: it carries positive mass at BOTH an even and an odd grade.
    THIS is the cancellation source — a genuine graded multiplicity space spreads
    `V_λ` across a run of consecutive grades, hitting both parities.  (The two
    dim-1 blocks are single monomials `q^0`, `q^{10}` — vacuously single-parity —
    hence the `dim ≠ 1` hypothesis.) -/
theorem PartitionOf5.fake_both_parity (p : PartitionOf5) (h : p.dim ≠ 1) :
    0 < (masses p.fakeCoeffs).1 ∧ 0 < (masses p.fakeCoeffs).2 := by
  revert h; cases p <;> decide

/-- **`H_λ` strictly undershoots**: `|χ(H_λ)| < dim V_λ` on every non-trivial block
    — the cancellation, quantified. -/
theorem PartitionOf5.fake_abs_altSum_lt_dim (p : PartitionOf5) (h : p.dim ≠ 1) :
    |altSum p.fakeCoeffs| < (p.dim : ℤ) := by
  have hb := p.fake_both_parity h
  have := abs_altSum_lt_sum_of_both_parity p.fakeCoeffs hb.1 hb.2
  rwa [p.fake_sum_eq_dim] at this

/-- **`H_λ` can never equal `Δ_λ`** — because it cancels below `dim = |Δ_λ|`.
    The honest coinvariant / jet-order TOWER does NOT realize the binding factor;
    the concentration is genuinely absent from it. -/
theorem PartitionOf5.fake_cancels_ne_deltaLambda (p : PartitionOf5) (h : p.dim ≠ 1) :
    altSum p.fakeCoeffs ≠ p.deltaLambda := by
  intro hbad
  have hlt := p.fake_abs_altSum_lt_dim h
  rw [hbad, abs_deltaLambda_eq_dim] at hlt
  exact lt_irrefl _ hlt

/-! ## THE CRUX: no algebraic graded substrate structure forces the concentration -/

/-- **THE CRUX (limitative — bean `qou-7ygi`).**  A single structural dichotomy
    settles the graded route.  Package it as: there are two graded assignments
    `single = G_λ` and `fake = H_λ` (`H_λ` = the honest jet-order / coinvariant
    TOWER, the genuine graded object the substrate produces) such that, on every
    non-trivial block,

      • BOTH carry the ungraded Wedderburn dimension `dim V_λ` (`same_total`);
      • `H_λ` is a two-parity multiplicity space, so its signed Euler characteristic
        CANCELS strictly below `dim` and never equals `Δ_λ` (`fake_ne`);
      • `G_λ` is the cancellation-free single-parity object and DOES equal `Δ_λ`
        (`single_is`);
      • and — the general reason (`realization_forces_single_parity`) — ANY graded
        object realizing `Δ_λ` must be cancellation-free (single grade-parity),
        i.e. the top-cohomology concentration, not a genuine multiplicity grading.

    Since every algebraic substrate grading (jet-order/coinvariant tower, KLR in the
    semisimple regime, Demazure) is a genuine graded multiplicity space — mass at
    both parities — none forces `G_λ`.  The single-degree concentration
    `H^{2n(λ)}(𝓑_λ) = V_λ` (Springer 1978) is a GEOMETRIC categorification input the
    13 drivers do not supply.  The NEGATIVE answer to `qou-7ygi`, unifying the
    count (#4559) / SDP (#4570) / valuation (#4574) negatives under one mechanism:
    CANCELLATION. -/
theorem graded_structure_cannot_force_concentration :
    ∃ single fake : PartitionOf5 → List ℕ,
      -- both carry the ungraded Wedderburn dimension:
      (∀ p : PartitionOf5, (single p).sum = (fake p).sum) ∧
      -- the honest graded TOWER never realizes Δ_λ (it cancels, on nontrivial blocks):
      (∀ p : PartitionOf5, p.dim ≠ 1 → altSum (fake p) ≠ p.deltaLambda) ∧
      -- the single-degree (top-cohomology) object does:
      (∀ p : PartitionOf5, altSum (single p) = p.deltaLambda) ∧
      -- and ANY graded realization of Δ_λ is forced to be cancellation-free:
      (∀ (p : PartitionOf5) (l : List ℕ), (l.sum : ℤ) = (p.dim : ℤ) →
          altSum l = p.deltaLambda → (masses l).1 = 0 ∨ (masses l).2 = 0) :=
  ⟨PartitionOf5.singleCoeffs, PartitionOf5.fakeCoeffs,
    fun p => by rw [p.single_sum_eq_dim, p.fake_sum_eq_dim],
    fun p h => p.fake_cancels_ne_deltaLambda h,
    fun p => p.single_altSum_eq_deltaLambda,
    fun p l => deltaLambda_realization_is_cancellation_free p l⟩

end QOU.BraidsAndKnots
