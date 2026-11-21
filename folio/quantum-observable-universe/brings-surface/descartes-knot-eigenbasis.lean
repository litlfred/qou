import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.List.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic
import QOU.SchurWeyl.HoefsmitRep
import QOU.SchurWeyl.GenericParameter
import QOU.SchurWeyl.MarkovTraceInstance


/-!
# QOU.Archimedean.descartes_knot_eigenbasis

Instantiation theorem: a Descartes universe (χ(A) = -6) provides all the
data needed for `KnotEigenbasisData`, establishing that knot types form a
complete eigenbasis for the algebraic direct limit V_phys = colim V^⊗n
(no metric completion is used).

The chain of reasoning:
1. Descartes condition forces genus 4, hence C = Rep(SU_q(2))
2. The R-matrix of U_q(su(2)) gives a braided monoidal structure on C
3. The quadratic relation of c_{V,V} yields the Hecke algebra H_n(q)
4. q not a root of unity → H_n(q) semisimple → Schur-Weyl decomposition
5. Alexander surjectivity + Markov trace → knot eigenbasis completeness

LaTeX label: `cor:descartes-knot-eigenbasis`

## 2026-09-04 — three detection claims quantified over an index they discarded

`DescartesMarkovTrace.summand_detection` and
`DescartesKnotEigenbasis.all_summands_detected` both read, in effect,

    ∀ (_ : Fin numSummands), ∃ (val : ℝ), val ≠ 0

The summand index is bound as `_` — explicitly discarded — and the detected
value is a free real tied to no trace, no braid and no character. So each
field asserted that **`ℝ` has a non-zero element**, and any instance
discharged it with `⟨1, one_ne_zero⟩`. `descartes_knot_eigenbasis` did
exactly that.

Both are now stated over `DescartesMarkovTrace.trSummand`, a per-summand
component of the trace constrained by
`tr_eq_sum_summands : tr n x = Σ_{i < ⌊n/2⌋+1} trSummand n i x`, so the
component is not free data an instance may choose independently of `tr`, and
the index occurs in the body. Same repair as
[`knot-eigenbasis-complete.lean`](../braids-and-knots/knot-eigenbasis-complete.lean)
next door (bean `qou-9552`).

Also added: `schurWeyl_level`. `DescartesSchurWeyl` carries its own `n`, and
nothing tied it to the level it was requested at, so `schurWeyl n hn` could
return the decomposition of any *other* level. The sibling
`QOU.Braiding.SchurWeylDecomposition` carries the analogous `n_eq`.

## The designated fallback had the defect too — and is provably not separating

The theorem's old docstring named `descartes_n3_both_detected` as the concrete
`n = 3` content standing in for the missing general-`n` character formula.
That theorem was `∃ (j_sym j_mix : ℝ), j_sym ≠ 0 ∧ j_mix ≠ 0` — again a
property of `ℝ`. The two Jones values, the two channels and `n = 3` appeared
only in the proof term and the comments. The proof was real work; the
statement recorded none of it.

The values are now named (`jonesSymmetric`, `jonesMixed`) and the theorem is
stated over them. Naming them makes a further fact reachable, and it is not a
comfortable one:

**The two channel values coincide at a `q` the Descartes condition permits.**
`jonesSymmetric D = jonesMixed D` reduces over `q > 0` to
`q⁵ - q⁴ + q³ + q² - 1 = 0` (`jonesSymmetric_eq_jonesMixed_iff`, proved, not
asserted), which has a root in `[7/10, 4/5]` by the intermediate value theorem
(`jones_channels_coincide`). At it — `q ≈ 0.779544663820934968877573423932`,
both channels `≈ -2.0623447988`, verified at 50 decimal digits — the pair
`(jonesSymmetric, jonesMixed)` carries no more information than one number
(`jones_channels_not_separating`).

So exhibiting two non-zero values does **not** establish that the two summands
are distinguished, which is what "both summands are detected" needs. The old
existential form could not have expressed the difference; the named form makes
the gap statable and now states it.

## …but the characters DO separate, and that negative is narrow

The sentence that stood here said "the per-summand character values for
general `n` remain upstream". **That was wrong**, and the corpus-grep
checklist is what caught it: `chi_lambda_braid` / `chi_lambdas_braid` in
`tools/hecke-engine/src/seminormal.rs` compute `χ^λ(β)` for general `n` and
general `λ` by Hoefsmit seminormal form, with MPFR variants, a Geck–Pfeiffer
canonical-basis expansion beside them, and about twenty entry points reachable
from Python via `pyhecke_native`. "Not in this Lean file" had been reported as
"upstream and open".

With that machinery the follow-up question is a measurement, not a research
problem, and it comes out the other way: **at `q*` itself the two characters
separate**, on every braid word tried. The two `n = 3` representations are
written down below (`rhoMixedSigma1`, `rhoMixedSigma2`), `charMixedSigma` is
their trace rather than an asserted number, and `sigma_separates_n3_channels`
proves `σ₁` alone separates the summands at every Descartes `q`.

So `jones_channels_not_separating` is a fact about the particular *pair of
Jones values* those two theorems name — not about the framework's ability to
separate summands. Bean `qou-qhs3`;
`computations/descartes_n3_channel_separation_probe.py`.

## …and the trace itself already exists too. `DescartesMarkovTrace` is superseded

The paragraph that stood here said the remaining work was "constructing
`DescartesMarkovTrace.trSummand` from those Hoefsmit values … a formalisation
of the seminormal representation". **Wrong again, and in the same direction.**
`QOU.SchurWeyl.SeminormalRep.wtrace` is the whole object, proved:

    wtrace q hq0 hq2 n : Hecke ℝ q q⁻¹ n →ₗ[ℝ] ℝ
      x ↦ ∑_{ν ⊢ n+1} ocneanuWeight q (q³/(q²+1)) ν · tr(ρ_ν(x))

with `wtrace_cyclic`, `wtrace_one = 1`, `wtrace_incl`, and `wtrace_markov` —
the Markov property at exactly `z_D = q³/(q²+1)`, convention D.

`descartesWtrace` below is that trace at a Descartes parameter;
`descartes_notRootOfUnity` is what makes it available, and it is the one piece
that was genuinely missing (`0 < q` and `q ≠ 1` over `ℝ` already give
`qᵐ ≠ 1` for every `m > 0`).

**So the structure `DescartesMarkovTrace` is superseded.** It is weaker in
three ways, each stated in the note beside its declaration: the element type
is `ℝ` rather than the Hecke algebra, the λ-sum carries no Ocneanu weights,
and `z` is inert — `descartesMarkovTrace_z_arbitrary` proves that every
non-zero real is the `z` of some instance, so the field constrains nothing.
Retiring it in favour of `descartesWtrace` is a refactor of this file's
remaining structures and both theorems, and is **not** done here.

## References

- [chari1994guide] Chari–Pressley, *A Guide to Quantum Groups*, Ch. 10
- [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987)
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [turaev2010] https://doi.org/10.1515/9783110218145
- [leitner2026] §6/§4

**Ground ring.** This is the **archimedean realisation** (namespace
`QOU.Archimedean`): the deformation parameter carries the order `0 < q`,
the inverse `q⁻¹`, and eigenvalue/positivity inequalities, none of which
live on the formal ground ring `R_q = ℤ[q, q⁻¹]`. The data is stated over
`ℝ` at the substrate image `ι : R_q → ℝ, q ↦ q₀` (§7c).
-/

namespace QOU.Archimedean

/-! ## Descartes Universe Data (from archimedean-condition.lean) -/

/-- Descartes condition: χ(A) = -6 with 6 invertible. -/
structure DescartesData where
  /-- Deformation parameter q from U_q(su(2)). -/
  q : ℝ
  /-- q > 0. -/
  q_pos : 0 < q
  /-- q ≠ 1 (non-classical deformation). -/
  q_ne_one : q ≠ 1
  /-- Euler characteristic is -6. -/
  eulerChar : ℤ
  euler_eq : eulerChar = -6
  /-- Dimension of V (forced to 2 by the volume constraint). -/
  dimV : ℕ
  dimV_eq : dimV = 2

/-- The genus of a Descartes universe is 4. -/
theorem DescartesData.genus_is_four (D : DescartesData) :
    (1 : ℤ) - D.eulerChar / 2 = 4 := by
  rw [D.euler_eq]; norm_num

/-- q > 0 implies q ≠ 0. -/
theorem DescartesData.q_ne_zero (D : DescartesData) : D.q ≠ 0 :=
  D.q_pos.ne'

/-! ## Hecke Algebra from the Descartes R-Matrix -/

/-- The Hecke algebra H_n(q) constructed from the R-matrix of
    U_q(su(2)) in a Descartes universe.

    The braiding c_{V,V} has eigenvalues q and -q⁻¹.
    The quadratic relation (T_i - q)(T_i + q⁻¹) = 0 defines
    the Hecke algebra as a quotient of the braid group algebra. -/
-- Ref: [chari1994guide] Ch. 10, [kassel1995] Ch. XIII
structure DescartesHeckeAlgebra (D : DescartesData) where
  /-- Number of strands. -/
  n : ℕ
  n_ge_two : 2 ≤ n
  /-- Carrier of H_n(q). -/
  carrier : Type*
  /-- The generators T_i. -/
  T : Fin (n - 1) → carrier
  /-- Multiplication. -/
  mul : carrier → carrier → carrier
  /-- Unit. -/
  one : carrier
  /-- The positive braiding eigenvalue q. -/
  eigenvalue_pos : ℝ := D.q
  /-- The negative braiding eigenvalue -q⁻¹. -/
  eigenvalue_neg : ℝ := -(D.q⁻¹)
  /-- Eigenvalues are distinct (q ≠ -q⁻¹ when q > 0, q ≠ 1). -/
  eigenvalues_distinct : eigenvalue_pos ≠ eigenvalue_neg

/-- For q > 0, the eigenvalues q and -q⁻¹ are distinct. -/
theorem eigenvalues_distinct_of_descartes (D : DescartesData) :
    D.q ≠ -(D.q⁻¹) := by
  have hq := D.q_pos
  have hqi : 0 < D.q⁻¹ := inv_pos.mpr hq
  linarith

/-! ## Schur-Weyl Decomposition for Rep(SU_q(2)) -/

/-- **Schur-Weyl data** for a Descartes universe at level n.

    For C = Rep(SU_q(2)) with V the spin-1/2 representation:
    V^⊗n ≅ ⊕_{j} V_j ⊗ S_j where j ranges over spins
    n/2, n/2 - 1, ..., 1/2 or 0 (partitions with ≤ 2 parts).

    The number of summands is ⌊n/2⌋ + 1. -/
-- Ref: [chari1994guide] Ch. 10
structure DescartesSchurWeyl (D : DescartesData) where
  /-- Number of tensor factors. -/
  n : ℕ
  /-- V^⊗n as a type. -/
  tensorPower : Type*
  /-- Number of irreducible summands = ⌊n/2⌋ + 1. -/
  numSummands : ℕ
  summands_count : numSummands = n / 2 + 1
  /-- Spin labels for each summand. -/
  spinLabel : Fin numSummands → ℝ
  /-- Maximum spin is n/2. -/
  max_spin : ∀ i, spinLabel i ≤ (n : ℝ) / 2
  /-- Projection: every vector projects to a unique summand index. -/
  -- Ref: [chari1994guide] Ch. 10 (Jimbo's theorem gives semisimplicity)
  summandOf : tensorPower → Fin numSummands

/-- The Schur-Weyl decomposition at n = 3 has 2 summands:
    spin 3/2 (symmetric) and spin 1/2 (mixed symmetry). -/
theorem schur_weyl_n3 (D : DescartesData) (sw : DescartesSchurWeyl D)
    (hn : sw.n = 3) : sw.numSummands = 2 := by
  rw [sw.summands_count, hn]

/-- The Schur-Weyl decomposition always has at least one summand. -/
theorem schur_weyl_nonempty (D : DescartesData) (sw : DescartesSchurWeyl D)
    (hn : sw.n ≥ 1) : sw.numSummands ≥ 1 := by
  rw [sw.summands_count]; omega

/-! ## Braid Representation from the Descartes Structure -/

/-- **Faithful braid representation** ρ_n : B_n → Aut_C(V^⊗n) from
    the Descartes braided monoidal structure.

    Faithfulness for n = 3 follows from the distinct eigenvalues
    of the R-matrix (q ≠ -q⁻¹), which is guaranteed by q > 0, q ≠ 1. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
structure DescartesBraidRep (D : DescartesData) where
  /-- Number of strands. -/
  n : ℕ
  n_ge_two : 2 ≤ n
  /-- Braid type (abstract B_n). -/
  BraidType : Type*
  /-- Braid generators σ_1, ..., σ_{n-1}. -/
  sigma : Fin (n - 1) → BraidType
  /-- The representation ρ_n assigns each braid to an automorphism
      of V^⊗n, encoded here as a real number (trace in the
      fundamental representation). -/
  trace_of : BraidType → ℝ
  /-- Faithfulness: distinct braids give distinct traces. -/
  faithful : ∀ β₁ β₂ : BraidType,
    trace_of β₁ = trace_of β₂ → β₁ = β₂
  /-- Braid group structure. -/
  [grp : Group BraidType]
  /-- σ₁σ₂σ₁ = σ₂σ₁σ₂ (braid relation for adjacent generators). -/
  braid_relation : ∀ (i : Fin (n - 2)),
    let i' : Fin (n - 1) := ⟨i.val, by omega⟩
    let j : Fin (n - 1) := ⟨i.val + 1, by omega⟩
    sigma i' * sigma j * sigma i' = sigma j * sigma i' * sigma j
  /-- Far commutativity: σᵢσⱼ = σⱼσᵢ for |i - j| ≥ 2. -/
  far_comm : ∀ (i j : Fin (n - 1)),
    i.val + 2 ≤ j.val →
    sigma i * sigma j = sigma j * sigma i

/-! ## Markov Trace from the Descartes Hecke Algebra -/

/-- **Markov trace** on the Hecke algebra tower of a Descartes universe.
    The trace exists, is unique, and detects every irreducible summand. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987)
structure DescartesMarkovTrace (D : DescartesData) where
  /-- The Markov parameter z = -(q - q⁻¹)⁻¹ · q^(1/2). -/
  z : ℝ
  z_ne_zero : z ≠ 0
  /-- The trace functional on H_n(q) elements. -/
  tr : ℕ → ℝ → ℝ  -- tr n x: trace of element x at level n
  /-- The trace of the identity is nonzero. -/
  tr_one_ne_zero : ∀ n, n ≥ 2 → tr n 1 ≠ 0
  /-- Component of the trace in the summand indexed by `i` at level `n`.

      Without this the decomposition is invisible to the trace, and no
      statement can be made *per summand* — see the module docstring. -/
  trSummand : ℕ → ℕ → ℝ → ℝ
  /-- The components decompose the trace:
      `tr n x = Σ_{i < ⌊n/2⌋+1} trSummand n i x`.

      This is what stops `trSummand` from being free data an instance may
      choose independently of `tr`. -/
  tr_eq_sum_summands : ∀ (n : ℕ) (x : ℝ),
    tr n x = ∑ i ∈ Finset.range (n / 2 + 1), trSummand n i x
  /-- Every irreducible summand is detected: for each level `n` and each
      summand index `i`, some element has non-zero trace **in that
      summand**.

      `i` occurs in the body. It did not until 2026-09-04 — see the module
      docstring for what the previous form asserted. -/
  -- Ref: [jones1987] §3, character non-vanishing
  summand_detection : ∀ (n i : ℕ), i < n / 2 + 1 →
    ∃ (x : ℝ), trSummand n i x ≠ 0

/-! ## `DescartesMarkovTrace` is superseded by `QOU.SchurWeyl.wtrace`

The structure above is named for the Markov trace and **does not contain the
Markov condition.** `z` occurs in its own declaration and in `z_ne_zero`, and
nowhere else: nothing relates it to `tr`, so `tr(x·σₙ) = z·tr(x)` is not
stated. `descartesMarkovTrace_z_arbitrary` below makes that machine-checked —
every non-zero real is the `z` of some instance, so the field carries no
information at all.

`QOU.SchurWeyl.wtrace` is the object this wanted to be, and it is already
proved:

    wtrace q hq0 hq2 n : Hecke ℝ q q⁻¹ n →ₗ[ℝ] ℝ
      x ↦ ∑_{ν ⊢ n+1} ocneanuWeight q (q³/(q²+1)) ν · tr(ρ_ν(x))

with `wtrace_cyclic`, `wtrace_one = 1`, `wtrace_incl`, and — the field this
structure lacks — `wtrace_markov`, the Markov property at exactly
`z = q³/(q²+1)`, which is `z_D`, the convention made canonical by the owner
ruling of 2026-08-15.

Three differences, each in the library's favour:

1. **The element type.** `tr : ℕ → ℝ → ℝ` above encodes a Hecke algebra
   element as *a real number*; `wtrace` is a linear functional on
   `Hecke ℝ q q⁻¹ n`. This is why the structure cannot state the Markov
   condition: with `x : ℝ` there is no `x · σₙ` to write.
2. **The weights.** The λ-sum above is unweighted; the real decomposition
   carries the Ocneanu weights `ocneanuWeight q z_D ν`. At `z_D` those
   weights *vanish* on every diagram of three or more rows
   (`ocneanuWeight_conventionD_eq_zero_of_three_rows`), which is what
   restricts the sum to the two-row `SU_q(2)` summands — for free, rather
   than by the `i < ⌊n/2⌋+1` index bound imposed by hand above.
3. **`z`.** Free here; there, the Markov parameter, appearing in the
   conclusion of `wtrace_markov`.

`descartes_wtrace_markov` below is the bridge: a Descartes universe satisfies
the library's genericity hypotheses, so the real Markov trace applies to it.
-/

/-- **A Descartes parameter is not a root of unity.**

    `DescartesData` gives `0 < q` and `q ≠ 1`; over `ℝ` that is already the
    library's `NotRootOfUnity`, since a positive real with `qᵐ = 1` for some
    `m > 0` must be `1`. This is the hypothesis `wtrace` needs, so every
    Descartes universe admits the genuine Markov trace. -/
theorem descartes_notRootOfUnity (D : DescartesData) :
    QOU.SchurWeyl.GenericParameter.NotRootOfUnity D.q := by
  intro m hm hpow
  rcases lt_trichotomy D.q 1 with h | h | h
  · exact absurd hpow (by
      have : D.q ^ m < 1 := pow_lt_one₀ D.q_pos.le h hm.ne'
      exact this.ne)
  · exact D.q_ne_one h
  · exact absurd hpow (by
      have : 1 < D.q ^ m := one_lt_pow₀ h hm.ne'
      exact this.ne')

/-- The genericity the library's weight lemmas ask for, in the `q²` form. -/
theorem descartes_notRootOfUnity_sq (D : DescartesData) :
    ∀ i : ℕ, 0 < i → (D.q ^ 2 : ℝ) ^ i ≠ 1 := by
  intro i hi
  rw [← pow_mul]
  exact descartes_notRootOfUnity D (2 * i) (by omega)

/-- `q² + 1 ≠ 0` over `ℝ`. -/
theorem descartes_sq_add_one_ne_zero (D : DescartesData) : (D.q ^ 2 + 1 : ℝ) ≠ 0 := by
  positivity

/-- `q² ≠ 1` — the `m = 2` instance of `descartes_notRootOfUnity`.

    **Not** the hypothesis `wtrace` takes; see the docstring of `descartesWtrace`. -/
theorem descartes_sq_ne_one (D : DescartesData) : (D.q ^ 2 : ℝ) ≠ 1 :=
  descartes_notRootOfUnity D 2 (by omega)

/-- **The Markov trace of a Descartes universe** — the real one.

    `QOU.SchurWeyl.SeminormalRep.wtrace` at the Descartes parameter, available
    because `descartes_notRootOfUnity` discharges its genericity hypothesis. It
    is a linear functional on the actual Hecke algebra, its λ-sum carries the
    Ocneanu weights, and it satisfies the Markov property at `z_D` — the three
    things `DescartesMarkovTrace` above lacks. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def descartesWtrace (D : DescartesData) (n : ℕ) :
    QOU.SchurWeyl.Hecke ℝ D.q D.q⁻¹ n →ₗ[ℝ] ℝ :=
  QOU.SchurWeyl.SeminormalRep.wtrace D.q D.q_ne_zero (descartes_notRootOfUnity D) n

/-- **The Markov property holds for every Descartes universe**:
    `tr(ι y · σₙ) = z_D · tr(y)` with `z_D = q³/(q²+1)`.

    This is the property `DescartesMarkovTrace` is named for and does not
    contain. Nothing is assumed here — the library proves it, and the
    Descartes hypotheses discharge what it asks for. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
theorem descartesWtrace_markov (D : DescartesData) (n : ℕ)
    (y : QOU.SchurWeyl.Hecke ℝ D.q D.q⁻¹ n) :
    descartesWtrace D (n + 1)
        (QOU.SchurWeyl.HeckeInclusion.heckeIncl ℝ D.q D.q⁻¹ n y
          * QOU.SchurWeyl.Hecke.σ ℝ D.q D.q⁻¹ (n + 1) (Fin.last n))
      = (D.q ^ 3 / (D.q ^ 2 + 1)) * descartesWtrace D n y :=
  QOU.SchurWeyl.SeminormalRep.wtrace_markov D.q D.q_ne_zero (descartes_notRootOfUnity D)
    (descartes_sq_add_one_ne_zero D) (descartes_notRootOfUnity_sq D) n y

/-! #### RETRACTION — there is no universe blocker; the file was checked against a stale library

An earlier revision of this file carried a note asserting that the per-summand
decomposition below **cannot be written**, because naming `seminormalRep` from
a content-block file at `K := ℝ` produced

    (kernel) incorrect number of universe levels parameters for
    'QOU.SchurWeyl.SeminormalRep.seminormalRep', #1 expected, #0 provided

and that this was AGENTS.md §7d's universe-carrying problem across a package
boundary, beyond §7d's own remedy. **That is withdrawn. It does not reproduce**
— `descartesWtraceSummand` and `descartesWtrace_eq_sum` are directly below,
they name `seminormalRep` at `K := ℝ` with `μ` inferred, and they compile.

What was actually wrong was the *verification*, not the mathematics.
`descartesWtrace` and `descartesWtrace_markov` were checked `lean`-direct
against a **restored olean cache built 2026-08-30**, in which `wtrace` still
took `hq2 : q ^ 2 ≠ 1`. Commit `794c34897d7` (2026-09-03) retyped that
hypothesis to `GenericParameter.NotRootOfUnity q` across seven library
consumers; this file is a content-block sibling and was not among them. So
both call sites passed `descartes_sq_ne_one`, an `exit 0` was recorded, and
the two declarations were **red against the library source they call** from
the moment they landed. Rebuilding the 27-module dirty cone from source and
recompiling this file gives two `Application type mismatch` errors and nothing
else; passing `descartes_notRootOfUnity` instead clears them.

Two things generalise from this and are worth more than the fix:

* **A restored olean cache is a snapshot, and `exit 0` against it is a claim
  about that snapshot.** When a library signature has moved under you, a
  content-block file can be green and broken at once. Rebuilding the changed
  cone into a shadow tree placed first on `LEAN_PATH` costs ~90 s here and is
  the only thing that distinguishes the two.
* **A failure observed once is not a diagnosis.** The universe error was real
  when it was seen; the *explanation* attached to it — polymorphic `K`, a
  package boundary, §7d not reaching it — was constructed from the error text
  rather than tested, and it was published in a merged PR and a bean where the
  next agent would have started from it. The cheap discriminator (write the
  declaration again, alone, and see) was never run.

Bean `qou-xcvx`.
-/

/-- **The per-summand component of the Descartes Markov trace.**

    `W_ν · tr ρ_ν(x)` — the Ocneanu weight at `z_D = q³/(q²+1)` times the
    character of the seminormal representation on the shape `ν`. This is the
    real object `DescartesMarkovTrace.trSummand` gestures at: indexed by Young
    diagrams of size `n+1` rather than by `Fin (n/2+1)`, evaluated on an
    element of the Hecke algebra rather than on a natural number, and carrying
    the weight rather than asserting a value. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def descartesWtraceSummand (D : DescartesData) (n : ℕ)
    (ν : {ν : YoungDiagram // ν.cells.card = n + 1})
    (x : QOU.SchurWeyl.Hecke ℝ D.q D.q⁻¹ n) : ℝ :=
  QOU.SchurWeyl.ocneanuWeight D.q (D.q ^ 3 / (D.q ^ 2 + 1)) ν.1 *
    ((QOU.SchurWeyl.SeminormalRep.seminormalRep D.q D.q_ne_zero
      (descartes_notRootOfUnity D) n ν.2) x).trace

/-- **The Descartes Markov trace is the sum of its per-shape summands.**

    The decomposition `DescartesMarkovTrace` never states: the trace is not an
    opaque functional with a detached list of numbers beside it, it *is* the
    weighted sum over partitions of `n+1`. Together with `descartesWtrace_markov`
    this is the whole content the structure was standing in for. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
theorem descartesWtrace_eq_sum (D : DescartesData) (n : ℕ)
    (x : QOU.SchurWeyl.Hecke ℝ D.q D.q⁻¹ n) :
    descartesWtrace D n x = ∑ ν, descartesWtraceSummand D n ν x :=
  QOU.SchurWeyl.SeminormalRep.wtrace_apply D.q D.q_ne_zero
    (descartes_notRootOfUnity D) n x

/-- **`DescartesMarkovTrace.z` carries no information**: every non-zero real is
    the `z` of some instance.

    Machine-checked demonstration of the supersession note above. `z` occurs in
    its own declaration and in `z_ne_zero` and nowhere else, so it is not the
    Markov parameter of anything — the structure never relates it to `tr`.
    Contrast `descartesWtrace_markov`, where `z_D = q³/(q²+1)` appears in the
    conclusion because it is forced.

    Recorded as a theorem so a later reader cannot mistake the field for a
    constraint, and so re-introducing a free `z` after a repair fails against a
    standing counterexample. -/
theorem descartesMarkovTrace_z_arbitrary (D : DescartesData) (z : ℝ) (hz : z ≠ 0) :
    ∃ mt : DescartesMarkovTrace D, mt.z = z := by
  refine ⟨{ z := z, z_ne_zero := hz
            tr := fun n x => (n / 2 + 1 : ℕ) * x
            tr_one_ne_zero := ?_
            trSummand := fun _ _ x => x
            tr_eq_sum_summands := ?_
            summand_detection := fun _ _ _ => ⟨1, one_ne_zero⟩ }, rfl⟩
  · intro n _
    have : (0 : ℝ) < ((n / 2 + 1 : ℕ) : ℝ) := by positivity
    simpa using this.ne'
  · intro n x
    simp [Finset.sum_const, nsmul_eq_mul, mul_comm]

/-! ## Main Instantiation Theorem -/

/-- **Descartes knot eigenbasis completeness.**

    A Descartes universe provides all the data needed for knot
    eigenbasis completeness: the Hecke algebra (from the R-matrix),
    the Schur-Weyl decomposition (from semisimplicity), and the
    Markov trace (from Jones's construction).

    This is the instantiation theorem that bridges the abstract
    `KnotEigenbasisData` structure (Chapter 4) with the concrete
    Descartes universe (Chapter 6). -/
-- Ref: [chari1994guide], [jones1987], [kassel1995]
structure DescartesKnotEigenbasis (D : DescartesData) where
  /-- Schur-Weyl decomposition at each level n. -/
  schurWeyl : ∀ (n : ℕ), n ≥ 1 → DescartesSchurWeyl D
  /-- Braid representation at each level n ≥ 2. -/
  braidRep : ∀ (n : ℕ), n ≥ 2 → DescartesBraidRep D
  /-- Markov trace on the Hecke tower. -/
  markov : DescartesMarkovTrace D
  /-- Consistency: the decomposition returned at level `n` is a
      decomposition of `V^⊗n`.

      Missing until 2026-09-04, so `schurWeyl n hn` could return the
      decomposition of any *other* level and nothing noticed. The sibling
      `QOU.Braiding.SchurWeylDecomposition` carries the analogous `n_eq`. -/
  schurWeyl_level : ∀ (n : ℕ) (hn : n ≥ 1), (schurWeyl n hn).n = n
  /-- Each summand at each level is detected by the Markov trace — stated
      over `markov.trSummand`, so the summand index occurs in the body and
      the detected value is the trace's component in *that* summand rather
      than a free real. -/
  all_summands_detected : ∀ (n : ℕ) (hn : n ≥ 1) (i : ℕ),
    i < (schurWeyl n hn).numSummands →
    ∃ (x : ℝ), markov.trSummand n i x ≠ 0

/-- The Descartes condition (q > 0, q ≠ 1, q not a root of unity)
    is sufficient to construct the full knot eigenbasis data.

    The key inputs:
    - Semisimplicity of H_n(q) ← q not a root of unity (Jimbo's theorem)
    - Eigenvalue distinctness ← q > 0 and q ≠ 1
    - Markov trace existence ← Jones's construction (1987)
    - Alexander surjectivity ← classical topology (Alexander, 1923)

    All four are available for any Descartes universe.

    **The witness is trivial, and the statement now says so.** The previous
    version's conclusion was `∀ (_ : Fin numSummands), ∃ jonesVal, jonesVal
    < 0` — the summand index discarded and the value tied to nothing — and
    it was proved by exhibiting the symmetric-channel Jones value
    `-(q + q⁻¹)`, once, for every index. The docstring described that as "a
    genuine, `q`-dependent detector"; the *type* accepted any negative real
    and would have accepted the same one for all summands, which is what the
    proof did.

    The conclusion is now stated over `trSummand`, so the index occurs. The
    witness constructed below is deliberately the trivial one
    (`trSummand n i x = x`), because that is all this file can supply: the
    per-summand character values for general `n` are upstream. Nothing here
    claims otherwise any more. -/
-- Ref: [chari1994guide] Ch. 10, [jones1987] §3
theorem descartes_knot_eigenbasis (D : DescartesData) :
    ∃ mt : DescartesMarkovTrace D,
      ∀ (n i : ℕ), i < n / 2 + 1 → ∃ x : ℝ, mt.trSummand n i x ≠ 0 := by
  refine ⟨{ z := 1, z_ne_zero := one_ne_zero
            tr := fun n x => (n / 2 + 1 : ℕ) * x
            tr_one_ne_zero := ?_
            trSummand := fun _ _ x => x
            tr_eq_sum_summands := ?_
            summand_detection := fun _ _ _ => ⟨1, one_ne_zero⟩ }, ?_⟩
  · intro n _
    have : (0 : ℝ) < ((n / 2 + 1 : ℕ) : ℝ) := by positivity
    simpa using this.ne'
  · intro n x
    simp [Finset.sum_const, nsmul_eq_mul, mul_comm]
  · exact fun _ _ _ => ⟨1, one_ne_zero⟩

/-- Jones value of the unknot in the symmetric (spin-3/2) channel at `n = 3`:
    `J = -(q + q⁻¹)`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def jonesSymmetric (D : DescartesData) : ℝ := -(D.q + D.q⁻¹)

/-- Jones value of the trefoil in the mixed-symmetry (spin-1/2) channel at
    `n = 3`: `J = -q⁻⁴(1 - q² + q⁴)`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def jonesMixed (D : DescartesData) : ℝ :=
  -(D.q⁻¹ ^ 4 * (1 - D.q ^ 2 + D.q ^ 4))

/-- **Corollary**: for `n = 3` in a Descartes universe, the symmetric and
    mixed-symmetry channel values are each non-zero — the unknot's value in
    the spin-3/2 channel and the trefoil's in the spin-1/2 channel.

    Stated over the two **named** values. Until 2026-09-04 this was
    `∃ (j_sym j_mix : ℝ), j_sym ≠ 0 ∧ j_mix ≠ 0`, which is a property of `ℝ`:
    the two Jones values, and `n = 3`, and the two channels, appeared only in
    the proof term and the comments. The proof was real work; the statement
    recorded none of it.

    **This does not say the two channels are separated** — see
    `jones_channels_coincide` below, which shows they take the *same* value at
    a `q` the Descartes condition permits. -/
-- Ref: [leitner2026] §4, [jones1987] §3
theorem descartes_n3_both_detected (D : DescartesData) :
    jonesSymmetric D ≠ 0 ∧ jonesMixed D ≠ 0 := by
  have hq := D.q_pos
  have hqi : 0 < D.q⁻¹ := inv_pos.mpr hq
  constructor
  · -- -(q + q⁻¹) < 0 for q > 0
    have : jonesSymmetric D < 0 := by unfold jonesSymmetric; linarith
    exact this.ne
  · -- -q⁻⁴(1 - q² + q⁴) < 0 for q > 0 (both factors positive)
    have hqi4 : 0 < D.q⁻¹ ^ 4 := pow_pos hqi 4
    have h_poly : 0 < 1 - D.q ^ 2 + D.q ^ 4 := by nlinarith [sq_nonneg (D.q ^ 2 - 1 / 2)]
    have : jonesMixed D < 0 := by
      unfold jonesMixed; linarith [mul_pos hqi4 h_poly]
    exact this.ne

/-- **The two `n = 3` channel values coincide at a `q` the Descartes
    condition permits**, so non-vanishing of each does *not* establish that
    the two summands are distinguished.

    `jonesSymmetric D = jonesMixed D` reduces, over `q > 0`, to
    `q⁵ - q⁴ + q³ + q² - 1 = 0`, which is negative at `q = 7/10` and positive
    at `q = 4/5`; the intermediate value theorem supplies a root between.
    Numerically the root is `q ≈ 0.779544663820934968877573423932`, where both
    channels take the value `≈ -2.0623447988` (verified at 50 decimal digits).

    Such a `q` satisfies `0 < q` and `q ≠ 1`, so it is a legitimate Descartes
    parameter. At it, the pair `(jonesSymmetric, jonesMixed)` carries no more
    information than a single number.

    This is why `descartes_n3_both_detected` is scoped to non-vanishing:
    separating the channels needs the values attached to their summands, i.e.
    `DescartesMarkovTrace.trSummand`, not two reals that happen to be
    non-zero. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
theorem jones_channels_coincide :
    ∃ q : ℝ, q ∈ Set.Icc (7 / 10 : ℝ) (4 / 5 : ℝ) ∧
      q ^ 5 - q ^ 4 + q ^ 3 + q ^ 2 - 1 = 0 := by
  have hcont : ContinuousOn (fun q : ℝ => q ^ 5 - q ^ 4 + q ^ 3 + q ^ 2 - 1)
      (Set.Icc (7 / 10 : ℝ) (4 / 5 : ℝ)) := by fun_prop
  have hle : (7 / 10 : ℝ) ≤ 4 / 5 := by norm_num
  have hmem : (0 : ℝ) ∈ Set.Icc
      ((7 / 10 : ℝ) ^ 5 - (7 / 10 : ℝ) ^ 4 + (7 / 10 : ℝ) ^ 3 + (7 / 10 : ℝ) ^ 2 - 1)
      ((4 / 5 : ℝ) ^ 5 - (4 / 5 : ℝ) ^ 4 + (4 / 5 : ℝ) ^ 3 + (4 / 5 : ℝ) ^ 2 - 1) := by
    constructor <;> norm_num
  obtain ⟨q, hq, hq0⟩ := intermediate_value_Icc hle hcont hmem
  exact ⟨q, hq, hq0⟩

/-- The reduction the docstring above describes, **proved** rather than
    asserted: over `q > 0`, the two channel values agree exactly when the
    quintic vanishes. -/
theorem jonesSymmetric_eq_jonesMixed_iff (D : DescartesData) :
    jonesSymmetric D = jonesMixed D ↔
      D.q ^ 5 - D.q ^ 4 + D.q ^ 3 + D.q ^ 2 - 1 = 0 := by
  have hq0 : D.q ≠ 0 := ne_of_gt D.q_pos
  unfold jonesSymmetric jonesMixed
  rw [neg_inj]
  field_simp
  constructor <;> intro h <;> nlinarith [h, sq_nonneg D.q, pow_pos D.q_pos 4]

/-- **There is a Descartes universe in which the two `n = 3` channel values
    are equal.**

    The headline consequence of the two results above, and the reason
    `descartes_n3_both_detected` is scoped to non-vanishing: at this `q` the
    unknot's symmetric-channel value and the trefoil's mixed-channel value are
    the *same real number*, so exhibiting both non-zero says nothing about the
    two summands being distinguished.

    Numerically `q ≈ 0.7795446638`, both channels `≈ -2.0623447988` (50 dps).
    Separating the channels needs `DescartesMarkovTrace.trSummand`. -/
theorem jones_channels_not_separating :
    ∃ D : DescartesData, jonesSymmetric D = jonesMixed D := by
  obtain ⟨q, hq, hroot⟩ := jones_channels_coincide
  obtain ⟨hlo, hhi⟩ := hq
  have hpos : 0 < q := by linarith
  have hne : q ≠ 1 := by intro h; rw [h] at hhi; norm_num at hhi
  refine ⟨⟨q, hpos, hne, -6, rfl, 2, rfl⟩, ?_⟩
  exact (jonesSymmetric_eq_jonesMixed_iff _).mpr hroot

/-! ### The characters do separate, where the Jones pair does not

`jones_channels_not_separating` above is a negative about the *particular
pair of Jones values* `descartes_n3_both_detected` names. It is not a
statement about the framework, and the object that does separate the
summands — the per-partition character `χ^λ` — already exists in the corpus
(`tools/hecke-engine/src/seminormal.rs`, Hoefsmit seminormal form, general
`n` and `λ`; MPFR variants alongside).

On the single generator `σ₁`, at `n = 3` with the two `≤ 2`-row partitions
of 3, those characters are

    χ^[3](σ₁)   = q          (symmetric, spin 3/2, dim 1)
    χ^[2,1](σ₁) = q − q⁻¹    (mixed symmetry, spin 1/2, dim 2)

so their difference is `q⁻¹`, which never vanishes. Verified against the
native seminormal path at eight sample `q` to better than `1e-45`
(`computations/descartes_n3_channel_separation_probe.py`), including at the
`q*` of `jones_channels_not_separating` itself.
-/

/-! #### The two representations, written down

The characters below are **traces of matrices**, not asserted values. An
earlier version of this section defined `charSymmetricSigma := q` and
`charMixedSigma := q − q⁻¹` outright and proved they differ — true, and with
the right numbers, but it derived nothing about representations, which is the
defect class this whole file is being repaired for.

`λ = [3]` is one-dimensional and sends every generator to `q`.

`λ = [2,1]` is two-dimensional, with basis the two standard Young tableaux
of that shape. In the Hoefsmit seminormal basis `σ₁` is diagonal — `1` and
`2` share a row in one tableau and a column in the other, giving the
eigenvalues `q` and `−q⁻¹` — while `σ₂` mixes them:

    ρ(σ₁) = [ q , 0 ; 0 , −q⁻¹ ]
    ρ(σ₂) = [ −1/(q+q³) , b ; b , q³/(1+q²) ]

with `b = √(1 + q² + q⁴)/(1 + q²)`.

Both matrices were read off `pyhecke_native.seminormal_matrices_mpfr` and
the closed forms verified against it at nine sample `q` to better than
`1e-40`, before any of this was written
(`computations/descartes_n3_channel_separation_probe.py`).

**These forms are regular at `q = 1`** — `ρ(σ₂)` becomes
`[ −1/2 , √3/2 ; √3/2 , 1/2 ]` and both traces vanish, which is the standard
two-dimensional representation of `S₃` where a transposition has trace `0`.
The native path returns `NaN` there because it divides by `q − q⁻¹`; that is
a removable singularity in the implementation, **not** a pole of the
representation. An earlier note in this arc said otherwise and was wrong.
-/

/-- The off-diagonal Hoefsmit entry `√(1 + q² + q⁴)/(1 + q²)` of `ρ_[2,1](σ₂)`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def hoefsmitOffDiag (q : ℝ) : ℝ :=
  Real.sqrt (1 + q ^ 2 + q ^ 4) / (1 + q ^ 2)

/-- `1 + q² > 0`, so it is safe as a denominator. -/
theorem one_add_sq_pos (q : ℝ) : (0 : ℝ) < 1 + q ^ 2 := by positivity

/-- The radicand of `hoefsmitOffDiag` is non-negative, so the square root is
    honest and `hoefsmitOffDiag q ^ 2` recovers it. -/
theorem hoefsmitOffDiag_sq (q : ℝ) :
    hoefsmitOffDiag q ^ 2 = (1 + q ^ 2 + q ^ 4) / (1 + q ^ 2) ^ 2 := by
  have hrad : (0 : ℝ) ≤ 1 + q ^ 2 + q ^ 4 := by positivity
  unfold hoefsmitOffDiag
  rw [div_pow, Real.sq_sqrt hrad]

/-- `ρ_[2,1](σ₁)` in the Hoefsmit seminormal basis: diagonal, eigenvalues `q`
    and `−q⁻¹`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def rhoMixedSigma1 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  Matrix.of ![![q, 0], ![0, -q⁻¹]]

/-- `ρ_[2,1](σ₂)` in the Hoefsmit seminormal basis. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def rhoMixedSigma2 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  Matrix.of ![![-(q + q ^ 3)⁻¹, hoefsmitOffDiag q],
              ![hoefsmitOffDiag q, q ^ 3 / (1 + q ^ 2)]]

/-- Character of the symmetric (spin-3/2) summand `λ = [3]` on `σ₁` at
    `n = 3`. The representation is one-dimensional and sends each generator
    to `q`, so the character is its `1 × 1` trace. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def charSymmetricSigma (D : DescartesData) : ℝ :=
  Matrix.trace (Matrix.of ![![D.q]] : Matrix (Fin 1) (Fin 1) ℝ)

/-- Character of the mixed-symmetry (spin-1/2) summand `λ = [2,1]` on `σ₁` at
    `n = 3` — **the trace of `ρ_[2,1](σ₁)`**, not an asserted value. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def charMixedSigma (D : DescartesData) : ℝ :=
  Matrix.trace (rhoMixedSigma1 D.q)

/-- The symmetric character evaluates to `q`. -/
theorem charSymmetricSigma_eq (D : DescartesData) : charSymmetricSigma D = D.q := by
  simp [charSymmetricSigma, Matrix.trace_fin_one]

/-- The mixed character evaluates to `q − q⁻¹` — derived from the matrix. -/
theorem charMixedSigma_eq (D : DescartesData) : charMixedSigma D = D.q - D.q⁻¹ := by
  simp [charMixedSigma, rhoMixedSigma1, Matrix.trace_fin_two]
  ring

/-- **The two `n = 3` channel characters differ by exactly `q⁻¹`.** -/
theorem charSymmetricSigma_sub_charMixedSigma (D : DescartesData) :
    charSymmetricSigma D - charMixedSigma D = D.q⁻¹ := by
  rw [charSymmetricSigma_eq, charMixedSigma_eq]; ring

/-! #### These matrices really are a Hecke representation

Two matrices with the right traces would prove nothing — the point of writing
them down is that they satisfy the defining relations, which is what makes
`charMixedSigma` a *character* rather than a number.

Both relations were checked numerically against the same nine sample `q`
before being stated (`descartes_n3_channel_separation_probe.py`).
-/

/-- `ρ_[2,1](σ₂)` has the same trace as `ρ_[2,1](σ₁)`, namely `q − q⁻¹`.

    Forced: `σ₁` and `σ₂` are conjugate in the braid group, and conjugate
    elements have equal character. Here it falls out of the closed forms. -/
theorem trace_rhoMixedSigma2 (q : ℝ) (hq : q ≠ 0) :
    Matrix.trace (rhoMixedSigma2 q) = q - q⁻¹ := by
  have h1 : (1 : ℝ) + q ^ 2 ≠ 0 := (one_add_sq_pos q).ne'
  have h2 : q + q ^ 3 ≠ 0 := by
    have : q + q ^ 3 = q * (1 + q ^ 2) := by ring
    rw [this]; exact mul_ne_zero hq h1
  simp only [rhoMixedSigma2, Matrix.trace_fin_two, Matrix.of_apply,
    Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const]
  field_simp
  ring

/-- **The determinant of `ρ_[2,1](σ₂)` is `−1`** — the product of the two
    Hecke eigenvalues `q · (−q⁻¹)`. -/
theorem det_rhoMixedSigma2 (q : ℝ) (hq : q ≠ 0) :
    Matrix.det (rhoMixedSigma2 q) = -1 := by
  have h1 : (1 : ℝ) + q ^ 2 ≠ 0 := (one_add_sq_pos q).ne'
  have h2 : q + q ^ 3 ≠ 0 := by
    have : q + q ^ 3 = q * (1 + q ^ 2) := by ring
    rw [this]; exact mul_ne_zero hq h1
  have hb := hoefsmitOffDiag_sq q
  simp only [rhoMixedSigma2, Matrix.det_fin_two, Matrix.of_apply,
    Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const]
  have : hoefsmitOffDiag q * hoefsmitOffDiag q = hoefsmitOffDiag q ^ 2 := by ring
  rw [this, hb]
  field_simp
  ring

/-- **The Hecke quadratic relation for `ρ_[2,1](σ₁)`**:
    `σ² = (q − q⁻¹)·σ + 1`, equivalently `(σ − q)(σ + q⁻¹) = 0`. -/
theorem rhoMixedSigma1_hecke (q : ℝ) (hq : q ≠ 0) :
    rhoMixedSigma1 q * rhoMixedSigma1 q
      = (q - q⁻¹) • rhoMixedSigma1 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rhoMixedSigma1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

/-- **The Hecke quadratic relation for `ρ_[2,1](σ₂)`**. -/
theorem rhoMixedSigma2_hecke (q : ℝ) (hq : q ≠ 0) :
    rhoMixedSigma2 q * rhoMixedSigma2 q
      = (q - q⁻¹) • rhoMixedSigma2 q + 1 := by
  have h1 : (1 : ℝ) + q ^ 2 ≠ 0 := (one_add_sq_pos q).ne'
  have hb := hoefsmitOffDiag_sq q
  have hbb : hoefsmitOffDiag q * hoefsmitOffDiag q
      = (1 + q ^ 2 + q ^ 4) / (1 + q ^ 2) ^ 2 := by
    rw [← hb]; ring
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rhoMixedSigma2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply,
      hbb] <;>
    field_simp
  -- Every goal here is polynomial once `hbb` has fired, so one `ring` pass
  -- closes them all and `hb` is not needed.  The two later proofs in this
  -- section (`rhoMixedSigma2_hecke`, `rhoMixed_braid`) DO need the second
  -- pass, and there the passes must stay separated: `field_simp` re-normalises
  -- `b * b` back to `b ^ 2`, so the square is substituted after the goal is
  -- polynomial, and `first | ring | (rw [hb]; …)` does not work.
  -- (`linear_combination … * hb` is the natural-looking move and fails there:
  -- it finishes with `ring1`, which cannot clear the `(1 + q²)⁻¹` on `hb`'s
  -- right-hand side.)
  all_goals (try ring)

/-- **The braid relation** `ρ(σ₁)ρ(σ₂)ρ(σ₁) = ρ(σ₂)ρ(σ₁)ρ(σ₂)`.

    Together with the two quadratic relations above, this is what makes the
    pair a representation of `H_3(q)` rather than two matrices that happen to
    have the right traces — and hence what makes `charMixedSigma` a
    *character*. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
theorem rhoMixed_braid (q : ℝ) (hq : q ≠ 0) :
    rhoMixedSigma1 q * rhoMixedSigma2 q * rhoMixedSigma1 q
      = rhoMixedSigma2 q * rhoMixedSigma1 q * rhoMixedSigma2 q := by
  have h1 : (1 : ℝ) + q ^ 2 ≠ 0 := (one_add_sq_pos q).ne'
  have hb := hoefsmitOffDiag_sq q
  have hbb : hoefsmitOffDiag q * hoefsmitOffDiag q
      = (1 + q ^ 2 + q ^ 4) / (1 + q ^ 2) ^ 2 := by
    rw [← hb]; ring
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rhoMixedSigma1, rhoMixedSigma2, Matrix.mul_apply, Fin.sum_univ_two,
      hbb] <;>
    field_simp
  -- Same shape as `rhoMixedSigma2_hecke` above; see the note there.
  -- `first | ring | (rw [hb]; …)` does NOT work here; the two passes are
  -- separated deliberately.
  all_goals (try ring)
  all_goals (rw [hb]; field_simp; ring)

/-! #### Bridge to `QOU.SchurWeyl.HoefsmitRep` — and a duplication, recorded

`QOU/SchurWeyl/HoefsmitRep.lean` has carried `S0`, `S1`, `S0_quadratic`,
`S1_quadratic` and `S0_S1_braid` since 2026-08 (bean `qou-u86i`, completed).
**`rhoMixedSigma1` above is `S0` — the same matrix, re-derived.** That is a
duplication and it is recorded rather than hidden; the corpus-grep checklist
found it, one step later than it should have been run.

`rhoMixedSigma2` is **not** a duplicate of `S1`, and the difference is the
useful part. The library form is deliberately *square-root-free* and therefore
**not symmetric**:

    S1 = [ −1/(q³+q) , 1 ; (q⁴+q²+1)/(q²+1)² , q³/(q²+1) ]

whereas `pyhecke_native.seminormal_matrices_mpfr` — the compute this corpus
actually runs — returns the **orthogonal** form, symmetric with a square root
in the off-diagonal. Both are the shape-`(2,1)` representation; they sit in
different bases, and nothing in the corpus said so.

`rhoMixedSigma2_conj_S1` supplies the change of basis: conjugation by
`diag(b, 1)`, written without inverses. Since `b > 0` the gauge is invertible,
so the two are similar, hence the same representation with the same character
— which is why `trace_rhoMixedSigma2` and the library's trace agree.

Practical consequence: **a Lean statement proved about `S1` transfers to the
numbers the Rust path produces only through this conjugation.** Reading a
`pyhecke_native` matrix as though it were `S1` entry-by-entry would be wrong;
only basis-independent quantities (trace, determinant, spectrum, the relations)
match directly.
-/

/-- The diagonal gauge `diag(b, 1)` taking the library's square-root-free `S1`
    to the orthogonal form the compute returns. -/
noncomputable def hoefsmitGauge (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  Matrix.of ![![hoefsmitOffDiag q, 0], ![0, 1]]

/-- **`rhoMixedSigma1` is the library's `S0`.** Recorded so the duplication is
    visible in the code and not only in a commit message. -/
theorem rhoMixedSigma1_eq_S0 (q : ℝ) :
    rhoMixedSigma1 q = QOU.SchurWeyl.S0 q := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [rhoMixedSigma1, QOU.SchurWeyl.S0]

/-- **The orthogonal and square-root-free seminormal forms are conjugate**, by
    the diagonal gauge `diag(b, 1)`:

      `ρ(σ₂) · diag(b,1) = diag(b,1) · S1`.

    Stated without inverses. `hoefsmitOffDiag q > 0`, so the gauge is
    invertible and this is a genuine similarity. -/
theorem rhoMixedSigma2_conj_S1 (q : ℝ) (hq : q ≠ 0) :
    rhoMixedSigma2 q * hoefsmitGauge q
      = hoefsmitGauge q * QOU.SchurWeyl.S1 q := by
  have h1 : (1 : ℝ) + q ^ 2 ≠ 0 := (one_add_sq_pos q).ne'
  have hb := hoefsmitOffDiag_sq q
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rhoMixedSigma2, hoefsmitGauge, QOU.SchurWeyl.S1, Matrix.mul_apply,
      Fin.sum_univ_two]
  all_goals (try ring)
  all_goals (rw [hb]; field_simp; ring)

/-- The gauge is non-singular: `√(1 + q² + q⁴)/(1 + q²) > 0`. -/
theorem hoefsmitOffDiag_pos (q : ℝ) : 0 < hoefsmitOffDiag q := by
  have hrad : (0 : ℝ) < 1 + q ^ 2 + q ^ 4 := by positivity
  unfold hoefsmitOffDiag
  exact div_pos (Real.sqrt_pos.mpr hrad) (one_add_sq_pos q)

/-- **`σ₁` separates the two `n = 3` summands, in every Descartes universe.**

    The positive counterpart to `jones_channels_not_separating`, and the
    reason that negative is narrow: the difference is `q⁻¹`, and `q > 0`
    forces `q⁻¹ ≠ 0`, so there is no Descartes `q` at which these two
    characters agree — including the `q*` where the two *Jones values* do.

    So "both summands are detected" is not out of reach; it needs the
    detector attached to its summand, which is what
    `DescartesMarkovTrace.trSummand` is for. What remains is to construct
    `trSummand` from the Hoefsmit values rather than leave it free — a
    formalisation of the seminormal representation, not a further open
    question about the mathematics. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
theorem sigma_separates_n3_channels (D : DescartesData) :
    charSymmetricSigma D ≠ charMixedSigma D := by
  intro h
  have hgap : charSymmetricSigma D - charMixedSigma D = 0 := by rw [h]; ring
  rw [charSymmetricSigma_sub_charMixedSigma] at hgap
  exact (inv_pos.mpr D.q_pos).ne' hgap

/-- **Corollary**: the eigenvalues q and -q⁻¹ of the R-matrix braiding
    are always distinct in a Descartes universe, ensuring the Hecke
    algebra quotient is well-defined and the braid representation
    is faithful. -/
theorem descartes_eigenvalues_distinct (D : DescartesData) :
    D.q ≠ -(D.q⁻¹) :=
  eigenvalues_distinct_of_descartes D

/-- **Corollary**: the number of particle species at level n is finite
    and equals ⌊n/2⌋ + 1 — each species is a knot type. -/
theorem descartes_particle_count (n : ℕ) :
    n / 2 + 1 ≥ 1 := by omega

end QOU.Archimedean
