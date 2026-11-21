/-
  Δ_λ = DT/3d-index Euler characteristic — the general-n unification.

  Context (epic `qou-r2nh`, bean `qou-bvpp`).  The sibling file
  `DeltaLambdaDTIndex.lean` (PR #4553) proves, at the `n = 5` anchor
  (`PartitionOf5`, by `decide`), that the single-degree Donaldson–Thomas /
  3d-index graded Euler characteristic of the Springer shadow `G_λ` equals the
  corpus per-partition binding factor `Δ_λ`:

      dtEuler(λ)  =  (-1)^{n(λ)} · dim V_λ  =  deltaSign(λ) · dim V_λ  =  Δ_λ .

  This file LIFTS that identity off the finite `PartitionOf5` enum to ALL `n`.
  The lift factors cleanly:

    • The `decide`-at-`n=5` core is a *single-degree graded Euler-characteristic
      collapse*: a graded object concentrated in one cohomological degree `N`
      with graded dimension `d` has alternating Euler characteristic
      `Σ_{k=0}^{N} (-1)^k (G)_k = (-1)^N · d`.  This is TRUE FOR ALL `N, d`
      (`dtEulerG_collapse`) — a genuine finite alternating sum, proved by a
      `List.range` induction, NOT a per-partition case split.  So the DT/3d-index
      unification `dtEuler = deltaLambda` holds for EVERY partition, with the
      Behrend sign `(-1)^{n(λ)}` (the a-function parity) and the count `dim V_λ`
      as free data (`dtEulerG_eq_deltaLambdaG`).

    • The `n = 5` anchor is then the specialisation of this general identity to
      the corpus data `(n(λ), dim V_λ)` for the seven `λ ⊢ 5`
      (`PartitionOf5.dtEulerG_eq_deltaLambda`), using the *general* a-function
      statistic `nStatList : List ℕ → ℕ` (the same fold that defines
      `PartitionOf5.nStat`, here read on the general partition `parts`), the
      corpus `deltaLambda = deltaSign · dim`, and the n≤5 chirality-parity fact
      `deltaSign_eq_nStat_parity`.  The general theorem SUBSUMES the anchor.

  What remains n≤5-only (the precise open/formalization leg, bean `qou-bvpp`):
  matching the a-function parity `(-1)^{n(λ)}` to the *geometric* chirality
  FORMULA `sgn(w₀^{S_{λ'}}) = (-1)^{Σ_i C(λ'_i,2)}` at general `n` needs the
  standard (textbook, NOT open-math) combinatorial identity
  `n(λ) = Σ_i C(λ'_i, 2)` (`nStatList parts = sumChoose2 (conjugate parts)`),
  proved here only via the corpus `nStat_eq_sumChoose2_conj` at `n ≤ 5`.  Its
  general-`n` Lean proof (a double-counting induction over the Young diagram)
  is the remaining formalization gap — see the `sorry`-free reduction lemma
  `parity_eq_w0_sign_of_nStat_eq_sumChoose2` below, which closes the geometric
  leg *conditionally* on that one identity.

  Discipline.  Everything here is combinatorial / sign-level, so the base ring
  is `ℤ` (signs) and `ℕ` (dimensions/statistics) — no archimedean `ℝ`, per §7c.
  Nothing is fitted, nothing is wired to production; this is the per-partition
  `Δ_λ` factor, not a binding-energy closure (the many-body magnitude scalar
  `r* ≈ 1.585` stays open, walled — see `docs/coordination/option-e.md`).

  Primary sources (as in the anchor file):
  Behrend, DT type invariants via microlocal geometry,
    Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307
  Springer, A construction of representations of Weyl groups,
    Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165
  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
-/
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.BraidsAndKnots.S5SO3FiberAction
import QOU.BraidsAndKnots.DeltaLambdaDTIndex

namespace QOU.BraidsAndKnots

/-! ## General single-degree graded object and its DT/3d-index Euler characteristic

    A graded object concentrated in ONE cohomological degree `N` with graded
    dimension `d` (the decategorified Springer shadow `G_λ`: `V_λ` in degree
    `n(λ)`, zero elsewhere).  Definitions mirror `DeltaLambdaDTIndex.lean` but on
    free parameters `(N, d) : ℕ × ℕ`, so they hold for every partition, not just
    `λ ⊢ 5`. -/

/-- Graded dimension of the single-degree object: `d` in degree `N`, else `0`. -/
def gradedDimG (N d k : ℕ) : ℕ := if k = N then d else 0

/-- The DT / 3d-index graded Euler characteristic
    `χ = Σ_{k=0}^{N} (-1)^k · dim (G)_k` — a genuine finite alternating sum. -/
def dtEulerG (N d : ℕ) : ℤ :=
  ((List.range (N + 1)).map (fun k => (-1 : ℤ) ^ k * (gradedDimG N d k : ℤ))).sum

/-- **The general-`n` DT collapse (the real content, all `N, d`).**  The
    alternating Euler characteristic of a single-degree object collapses to the
    Behrend sign `(-1)^N` times the count `d`.  This is the `n`-free lift of the
    seven `decide`d instances in `DeltaLambdaDTIndex.lean`: proved once, by a
    `List.range` induction, for every grade `N` and dimension `d`. -/
theorem dtEulerG_collapse (N d : ℕ) : dtEulerG N d = (-1 : ℤ) ^ N * (d : ℤ) := by
  unfold dtEulerG
  rw [List.range_succ, List.map_append, List.sum_append]
  have h0 : ((List.range N).map
      (fun k => (-1 : ℤ) ^ k * (gradedDimG N d k : ℤ))).sum = 0 := by
    apply List.sum_eq_zero
    intro x hx
    rw [List.mem_map] at hx
    obtain ⟨k, hk, rfl⟩ := hx
    rw [List.mem_range] at hk
    have hkN : k ≠ N := Nat.ne_of_lt hk
    simp [gradedDimG, hkN]
  rw [h0, zero_add]
  simp [gradedDimG]

/-! ## The general-`n` unification: `dtEuler = Δ_λ` for every partition

    `Δ_λ = deltaSign · dim` with the chirality `deltaSign` the a-function parity
    `(-1)^{n(λ)}` — the corpus-proven characterisation (`deltaSign_eq_nStat_parity`
    at `n ≤ 5`; taken as the *general* chirality here).  The DT Euler
    characteristic reproduces exactly this signed dimension, for all `(N, d)`. -/

/-- General chirality sign = a-function parity `(-1)^{n(λ)}` (the corpus
    `deltaSign` at `n ≤ 5`, lifted to all `n`). -/
def deltaSignParity (N : ℕ) : ℤ := (-1 : ℤ) ^ N

/-- General per-partition binding factor `Δ_λ = deltaSign · dim`. -/
def deltaLambdaG (N d : ℕ) : ℤ := deltaSignParity N * (d : ℤ)

/-- **THE GENERAL-`n` UNIFICATION.**  For EVERY partition (any a-function grade
    `N = n(λ)`, any Wedderburn dimension `d = dim V_λ`), the DT / 3d-index Euler
    characteristic equals the binding factor `Δ_λ`.  The horn-1 sign
    (`deltaSignParity N = (-1)^{n(λ)}`) and the horn-2 magnitude (`d = dim V_λ`)
    are the parity and value of ONE graded datum — for all `n`, not just `n = 5`. -/
theorem dtEulerG_eq_deltaLambdaG (N d : ℕ) : dtEulerG N d = deltaLambdaG N d := by
  rw [dtEulerG_collapse]; rfl

/-- **Magnitude leg, general `n`**: `(DT Euler)² = d²`. -/
theorem dtEulerG_magnitude (N d : ℕ) : dtEulerG N d ^ 2 = (d : ℤ) ^ 2 := by
  rw [dtEulerG_collapse]
  rcases Nat.even_or_odd N with h | h
  · rw [h.neg_one_pow]; ring
  · rw [h.neg_one_pow]; ring

/-- **Sign leg, general `n`**: the DT Euler characteristic is negative iff the
    a-function grade is odd and the dimension is positive (Behrend `(-1)^{dim}`
    is negative exactly on odd-dimensional moduli). -/
theorem dtEulerG_neg_iff (N d : ℕ) :
    dtEulerG N d < 0 ↔ (N % 2 = 1 ∧ 0 < d) := by
  rw [dtEulerG_collapse]
  have hdnn : (0 : ℤ) ≤ (d : ℤ) := Int.natCast_nonneg d
  rcases Nat.even_or_odd N with hN | hN
  · rw [hN.neg_one_pow, one_mul]
    have hNm : N % 2 = 0 := Nat.even_iff.mp hN
    omega
  · rw [hN.neg_one_pow, neg_one_mul]
    have hNm : N % 2 = 1 := Nat.odd_iff.mp hN
    omega

/-! ## The `n = 5` anchor as a specialisation (the general theorem subsumes it)

    `PartitionOf5.nStat` is `nStatList p.parts` for the *same* fold — so the
    general `dtEulerG` at the corpus data `(n(λ), dim V_λ)` reproduces the corpus
    `Δ_λ = deltaSign · dim` for every one of the seven `λ ⊢ 5`, discharging the
    original `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda` from the general identity. -/

/-- The general a-function statistic on a partition's parts — the identical fold
    that defines `PartitionOf5.nStat`, read on a general `List ℕ`. -/
def nStatList (parts : List ℕ) : ℕ :=
  (parts.foldl (fun (acc : ℕ × ℕ) part => (acc.1 + 1, acc.2 + acc.1 * part)) (0, 0)).2

/-- `PartitionOf5.nStat` is the general `nStatList` on the block's parts. -/
theorem PartitionOf5.nStat_eq_nStatList (p : PartitionOf5) :
    p.nStat = nStatList p.parts := rfl

/-- **Anchor subsumption**: the general DT Euler characteristic, evaluated at the
    corpus `n = 5` data `(nStatList p.parts, p.dim)`, equals the corpus binding
    factor `p.deltaLambda`.  Uses the *general* collapse plus the corpus chirality
    parity `deltaSign_eq_nStat_parity`; no per-partition `decide`. -/
theorem PartitionOf5.dtEulerG_eq_deltaLambda (p : PartitionOf5) :
    dtEulerG (nStatList p.parts) p.dim = p.deltaLambda := by
  rw [dtEulerG_collapse, ← PartitionOf5.nStat_eq_nStatList,
      PartitionOf5.deltaLambda, PartitionOf5.deltaSign_eq_nStat_parity]

/-! ## The geometric-chirality leg — reduced to ONE standard identity

    The corpus defines the chirality geometrically as the conjugate Young
    subgroup's longest-element sign `deltaSign = sgn(w₀^{S_{λ'}}) =
    (-1)^{Σ_i C(λ'_i,2)}` (`deltaSign_eq_w0_conj_sign`, `n ≤ 5`).  Matching THAT
    formula to the a-function parity `(-1)^{n(λ)}` at general `n` needs exactly

        n(λ)  =  Σ_i C(λ'_i, 2)          (†)

    — `nStatList parts = sumChoose2 (conjugate parts)` — the standard (textbook,
    NOT open-math) double-counting identity, proved in the corpus only via
    `PartitionOf5.nStat_eq_sumChoose2_conj` at `n ≤ 5`.  The lemma below closes
    the geometric leg for ANY partition *conditionally on (†)*, so the ONLY
    residual is the general-`n` proof of (†) itself (bean `qou-bvpp`). -/

/-- **Geometric-chirality leg, conditional on (†).**  If the a-function statistic
    equals the conjugate-partition binomial sum (`nStatList parts = sumChoose2
    conj`, i.e. (†) above), then the a-function-parity chirality equals the
    geometric longest-element-sign formula `(-1)^{Σ_i C(λ'_i,2)}` for that
    partition.  The hypothesis `(†)` is the single remaining general-`n` gap. -/
theorem parity_eq_w0_sign_of_nStat_eq_sumChoose2
    (parts conj : List ℕ) (hconj : nStatList parts = sumChoose2 conj) :
    deltaSignParity (nStatList parts) = (-1 : ℤ) ^ (sumChoose2 conj) := by
  unfold deltaSignParity
  rw [hconj]

/-- **(†) holds at the `n = 5` anchor** (via the corpus identity), so the
    geometric leg is fully closed there: the a-function-parity chirality equals
    the conjugate Young-subgroup longest-element sign for every `λ ⊢ 5`.  This is
    the general lemma above discharged at the anchor — a witness that the
    conditional reduction is non-vacuous. -/
theorem parity_eq_w0_sign (p : PartitionOf5) :
    deltaSignParity (nStatList p.parts) = (-1 : ℤ) ^ (sumChoose2 p.conjParts) :=
  parity_eq_w0_sign_of_nStat_eq_sumChoose2 p.parts p.conjParts
    (by rw [← PartitionOf5.nStat_eq_nStatList]; exact p.nStat_eq_sumChoose2_conj)

/-! ## Bridge to the merged `n = 5` anchor (`DeltaLambdaDTIndex.lean`)

    The corpus `PartitionOf5.dtEuler` (proved `= p.deltaLambda` at `n = 5` by
    `decide` in `DeltaLambdaDTIndex.lean`, PR #4553, now on main) is *definitionally*
    the general `dtEulerG` evaluated at the block's `(n(λ), dim V_λ)` data — its
    `gradedDim`/`dtEuler` are the `PartitionOf5`-specialisation of the free
    `gradedDimG`/`dtEulerG` here.  So the merged `decide`d anchor is re-derived from
    the *general* collapse, confirming this file genuinely generalises it. -/

/-- The merged anchor's `PartitionOf5.dtEuler` is the general `dtEulerG` at
    `(nStat, dim)` — definitional. -/
theorem PartitionOf5.dtEuler_eq_dtEulerG (p : PartitionOf5) :
    p.dtEuler = dtEulerG p.nStat p.dim := rfl

/-- **The merged `n = 5` anchor `dtEuler = Δ_λ`, re-derived from the general
    collapse** (not `decide`).  Same statement as
    `DeltaLambdaDTIndex.PartitionOf5.dtEuler_eq_deltaLambda`, obtained here as a
    corollary of the all-`n` `dtEulerG_collapse` + the chirality parity — evidence
    that the general identity subsumes the anchor. -/
theorem dtEuler_eq_deltaLambda_via_collapse (p : PartitionOf5) :
    p.dtEuler = p.deltaLambda := by
  rw [PartitionOf5.dtEuler_eq_dtEulerG, PartitionOf5.nStat_eq_nStatList]
  exact p.dtEulerG_eq_deltaLambda

end QOU.BraidsAndKnots
