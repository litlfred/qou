/-
  Does the confinement SDP / canonical `T_w` FORCE the top-degree (single-degree)
  cohomology projection that makes `Δ_λ = (-1)^{n(λ)}·dim V_λ`?
  — the precise open sub-question left by PR #4559 (`qou-ylot`), epic `qou-r2nh`,
  bean `qou-nmpr`.

  Context.  Two just-landed sorry-free results bracket the per-partition binding
  factor `Δ_λ = deltaSign · dim V_λ`:

    • PR #4553 (`DeltaLambdaDTIndex`): `Δ_λ` is the graded Euler characteristic of
      the SINGLE-DEGREE Springer object `G_λ = V_λ` concentrated in degree
      `n(λ)` — `dtEuler G_λ = (-1)^{n(λ)}·dim V_λ = Δ_λ`.

    • PR #4559 (`DeltaLambdaDTModuliUnderdetermined`): matching `Δ_λ` as a
      Behrend-signed DT count UNDER-DETERMINES the moduli dimension (pins only
      parity + count `dim V_λ`); the Springer dimension `n(λ)` must enter from an
      INDEPENDENT substrate map, and the residual obstruction it isolated is
      exactly the SINGLE-DEGREE CONCENTRATION: the substrate's natural coinvariant
      grading spreads `V_λ` across the fake-degree polynomial `f_λ(q)`, whose
      SIGNED evaluation `f_λ(-1)` is generically NOT `Δ_λ`.  Only selecting the
      top / lowest-fake-degree Springer piece `H^{top}(𝓑_λ) = V_λ` gives the clean
      `(-1)^{n(λ)}·dim`.

  THE CRUX (bean `qou-nmpr`).  Does the confinement SDP / canonical `T_w`
  selection force that top-degree projection?

  Answer proved here (NEGATIVE, sharply bounded).  The confinement SDP / canonical
  `T_w` reads only the UNGRADED Wedderburn datum:

    • its variables are the Hecke coefficients `c_w` (GB-NF basis of `H_n(q)`);
    • its constraints are the block-PSD conditions `ρ_λ(T(c)) ⪰ 0` on the
      *ungraded* seminormal (Hoefsmit) representations `ρ_λ` at `q = q₀`;
    • its anchor is the Markov trace `tr_M = Σ_λ w_λ(q)·χ_λ` — a weighted sum of
      *ungraded* Wedderburn characters `χ_λ`.

  Every one of these factors through the ungraded semisimple algebra
  `⊕_λ End(V_λ)`.  In particular each block contributes only through
  `dim V_λ` (and the ungraded block matrices) — there is NO cohomological degree
  variable anywhere in the SDP / `T_w` / `tr_M` data.  The fake-degree /
  coinvariant grading `V_λ = ⊕_i (V_λ)_i` (graded dimension `f_λ(q)`) is FINER
  structure invisible to that data.

  We formalize the obstruction sorry-free at the `n = 5` anchor.  Encode, for each
  block, the fake-degree graded object `H_λ` (graded dims = coefficients of
  `f_λ(q)`) alongside the single-degree Springer object `G_λ` (`dim V_λ` in degree
  `n(λ)`).  Then:

    1. `fakeTotalDim_eq_dim` / `singleTotalDim_eq_dim` — BOTH objects carry the
       SAME ungraded dimension `dim V_λ` (`= f_λ(1)`).  This is *all* the
       confinement SDP / canonical `T_w` / Markov trace can read.
    2. `single_gradedEuler_eq_deltaLambda` — the single-degree object's signed
       Euler characteristic is the corpus `Δ_λ`.
    3. `fake_gradedEuler_ne_deltaLambda` — the FULL fake-degree object's signed
       Euler characteristic `f_λ(-1)` differs from `Δ_λ` on every non-trivial
       block (dim > 1): the single-degree concentration is LOAD-BEARING (extends
       PR #4559's `λ=(2,1)` `n=3` example to the whole `n=5` anchor).
    4. `sdp_cannot_force_top_degree` — THE CRUX.  Two graded objects with the
       SAME ungraded Wedderburn dimension `dim V_λ` but DIFFERENT signed Euler
       characteristics.  Since the confinement SDP / canonical `T_w` / `tr_M` are
       functionals of the ungraded dimension alone, they cannot distinguish — and
       therefore cannot FORCE — the single-degree (top-cohomology) object.  The
       top-degree projection is a genuinely INDEPENDENT input (a Springer /
       coinvariant graded structure), NOT supplied by the confinement SDP.

  Scope / discipline (STRICT).  This is a LIMITATIVE (scope-(a)) negative with a
  structural backbone: the isolated invariant is that the SDP / `T_w` / `tr_M`
  factor through the ungraded Wedderburn algebra `⊕_λ End(V_λ)`, and the grading
  is not a function of that algebra (witnessed by `G_λ` vs `H_λ`).  It does NOT
  claim top-degree is excluded from every closure — an INDEPENDENT graded
  substrate map (the a-function = Gröbner–Shirshov jet-order valuation, per
  `docs/coordination/option-e.md`) could still supply it; that map is the precise
  next obstruction.  It DOES answer the bean's exact question: the confinement SDP
  / canonical `T_w`, as constructed, does not force the projection.  Nothing here
  is fitted; `Δ_λ`, AME, CODATA, `q₀` are never inverted; no instance of the open
  conjecture `DeltaLambdaDTRealization` is fabricated.  Base ring is `ℤ`
  throughout (signed Euler characteristics; §7c — no archimedean construct).  This
  converges, from the grading direction, with the `A_ω = 3` "structurally-open"
  verdict (PR #4554) and with the moduli under-determination (PR #4559).

  Primary sources:
  Springer, A construction of representations of Weyl groups,
    Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165
  Behrend, Donaldson–Thomas type invariants via microlocal geometry,
    Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307
  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
-/
import QOU.BraidsAndKnots.S5SO3FiberAction

namespace QOU.BraidsAndKnots

/-! ## Graded Euler characteristic of a coefficient vector

    A graded finite-dimensional object is encoded by its coefficient list
    `l : List ℕ`, where `l[i]` is the dimension in cohomological degree `i`
    (degree `0` first).  Its signed (DT / Behrend) Euler characteristic is
    `Σ_i (-1)^i · l[i]`.  This is exactly the decategorified `∑ (-1)^i dim H^i`.
    Defined by structural recursion on the list (degree accumulator `d`) so it
    reduces cleanly under `decide` at the `n = 5` anchor. -/
def gradedEulerAux : ℕ → List ℕ → ℤ
  | _, [] => 0
  | d, c :: cs => (-1 : ℤ) ^ d * (c : ℤ) + gradedEulerAux (d + 1) cs

def gradedEuler (l : List ℕ) : ℤ := gradedEulerAux 0 l

/-! ## The two graded objects at the `n = 5` anchor -/

/-- **The single-degree Springer object `G_λ`.**  `dim V_λ` concentrated in the
    ONE degree `n(λ)` (a-function `= dim_ℂ 𝓑_λ`), zero elsewhere: the
    coefficient list is `n(λ)` zeros followed by `dim V_λ`.  This is the graded
    object whose Euler characteristic is `Δ_λ` (PR #4553, `DeltaLambdaDTIndex`). -/
def PartitionOf5.singleCoeffs (p : PartitionOf5) : List ℕ :=
  List.replicate p.nStat 0 ++ [p.dim]

/-- **The full fake-degree object `H_λ`.**  Graded dimensions `= coefficients of
    the fake-degree polynomial `f_λ(q) = q^{n(λ)}·[5]_q! / ∏_{cell} [h]_q` (the
    graded dimension of the `λ`-isotypic component of the `S_5`-coinvariant
    algebra = graded `H^*(𝓑_λ)`).  Position `i` is the coefficient of `q^i`.
    Hard-coded table (n=5) whose shape matches that polynomial; separately
    verified `f_λ(1) = dim V_λ` by `fakeTotalDim_eq_dim`, below. -/
def PartitionOf5.fakeCoeffs : PartitionOf5 → List ℕ
  | .five         => [1]                              -- f = 1                    (q^0)
  | .fourOne      => [0, 1, 1, 1, 1]                  -- f = q[4]_q               (q^1..q^4)
  | .threeTwo     => [0, 0, 1, 1, 1, 1, 1]            -- f = q²[5]_q              (q^2..q^6)
  | .threeOneOne  => [0, 0, 0, 1, 1, 2, 1, 1]         -- f = q³[3]_q(1+q²)        (q^3..q^7)
  | .twoTwoOne    => [0, 0, 0, 0, 1, 1, 1, 1, 1]      -- f = q⁴[5]_q              (q^4..q^8)
  | .twoOneOneOne => [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]   -- f = q⁶[4]_q              (q^6..q^9)
  | .onesFive     => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] -- f = q^{10}              (q^10)

/-! ## Both objects carry the SAME ungraded Wedderburn dimension -/

/-- The single-degree object totals to `dim V_λ`. -/
theorem PartitionOf5.singleTotalDim_eq_dim (p : PartitionOf5) :
    (p.singleCoeffs).sum = p.dim := by
  cases p <;> decide

/-- The full fake-degree object ALSO totals to `dim V_λ` — this is `f_λ(1) =
    dim V_λ` (the number of standard Young tableaux).  Hence the ungraded datum
    `dim V_λ` — everything the confinement SDP / `T_w` / `tr_M` read — is SHARED
    between `G_λ` and `H_λ`. -/
theorem PartitionOf5.fakeTotalDim_eq_dim (p : PartitionOf5) :
    (p.fakeCoeffs).sum = p.dim := by
  cases p <;> decide

/-- The two objects carry the same ungraded dimension, block by block. -/
theorem PartitionOf5.same_ungraded_dim (p : PartitionOf5) :
    (p.singleCoeffs).sum = (p.fakeCoeffs).sum := by
  rw [p.singleTotalDim_eq_dim, p.fakeTotalDim_eq_dim]

/-! ## Their signed Euler characteristics DIFFER -/

/-- **The single-degree object realizes `Δ_λ`.**  Its Euler characteristic is
    `(-1)^{n(λ)}·dim V_λ = Δ_λ` (the collapse of PR #4553's `dtEuler`). -/
theorem PartitionOf5.single_gradedEuler_eq_deltaLambda (p : PartitionOf5) :
    gradedEuler p.singleCoeffs = p.deltaLambda := by
  cases p <;> decide

/-- **The full fake-degree object does NOT realize `Δ_λ`** on any non-trivial
    block: `f_λ(-1) ≠ Δ_λ` whenever `dim V_λ > 1`.  So the single-degree
    concentration (top-cohomology selection) is LOAD-BEARING — dropping it and
    keeping the full coinvariant grading breaks the identity at every block that
    is not already a single degree.  (Extends PR #4559's `λ=(2,1)`, `n=3`,
    `f(-1)=0≠-2` observation to the entire `n=5` anchor.  The two dim-1 blocks
    `(5)`, `(1⁵)` are trivially single-degree monomials, so they agree — hence the
    `dim ≠ 1` hypothesis.) -/
theorem PartitionOf5.fake_gradedEuler_ne_deltaLambda (p : PartitionOf5)
    (h : p.dim ≠ 1) : gradedEuler p.fakeCoeffs ≠ p.deltaLambda := by
  revert h; cases p <;> decide

/-! ## THE CRUX: the confinement SDP / canonical `T_w` cannot force top-degree -/

/-- **THE CRUX (limitative).**  There exist two graded assignments — the
    single-degree Springer object `G_λ = singleCoeffs` and the full fake-degree
    coinvariant object `H_λ = fakeCoeffs` — such that:

      • they carry the SAME ungraded Wedderburn dimension `dim V_λ` at every
        block (`same`), i.e. they are INDISTINGUISHABLE to any functional of the
        ungraded block data — which is *exactly* what the confinement SDP
        (`ρ_λ(T(c)) ⪰ 0`), the canonical `T_w` selection, and the Markov trace
        `tr_M = Σ_λ w_λ χ_λ` are (they factor through `⊕_λ End(V_λ)`);

      • yet their signed (DT/Behrend) Euler characteristics DIFFER on every
        non-trivial block (`differ`), with only the single-degree object equal to
        `Δ_λ` (`single_is_delta`).

    Consequently the ungraded datum does NOT pin the graded Euler characteristic,
    so NO functional of it — in particular the confinement SDP / canonical `T_w`
    — can FORCE the top-degree (single-degree) concentration.  The top-cohomology
    projection `H^{top}(𝓑_λ) = V_λ` is a genuinely INDEPENDENT input.  This is the
    precise NEGATIVE answer to bean `qou-nmpr`: the confinement SDP / canonical
    `T_w`, as constructed, does not reach top degree. -/
theorem sdp_cannot_force_top_degree :
    ∃ single fake : PartitionOf5 → List ℕ,
      -- same ungraded Wedderburn dimension (all the SDP / T_w / tr_M can read):
      (∀ p : PartitionOf5, (single p).sum = (fake p).sum) ∧
      -- but different signed Euler characteristics on every non-trivial block:
      (∀ p : PartitionOf5, p.dim ≠ 1 →
          gradedEuler (single p) ≠ gradedEuler (fake p)) ∧
      -- and only the single-degree (top-cohomology) object equals Δ_λ:
      (∀ p : PartitionOf5, gradedEuler (single p) = p.deltaLambda) :=
  ⟨PartitionOf5.singleCoeffs, PartitionOf5.fakeCoeffs,
    fun p => p.same_ungraded_dim,
    fun p h => by
      have hs := p.single_gradedEuler_eq_deltaLambda
      have hf := p.fake_gradedEuler_ne_deltaLambda h
      rw [hs]; exact fun hbad => hf hbad.symm,
    fun p => p.single_gradedEuler_eq_deltaLambda⟩

end QOU.BraidsAndKnots
