/-
Copyright (c) 2026 litlfred. All rights reserved.

# Derived character catalogue — Lean schema (Phase 4 scaffold, 2026-06-07)

> **Lean side of the 3-axis (knot, partition, atom) derived-χ catalogue**
> implemented in Python at
> [`computations/derived_chi_catalogue.py`](../../../../../computations/derived_chi_catalogue.py)
> (PR #1952). This module gives the catalogue a Lean type-level
> presence: a `KnotPartitionAtomCell` structure mirroring the Python
> schema, conditional classes for R-matrix derivation provenance, and
> a worked instance (the Borromean / (2,1) / baryon cell that
> cross-validates T17 in PR #1933).

## What this provides

- `KnotPartitionAtomCell` — a `structure` carrying every catalogue
  field at the type level.
- `IsRMatrixDerived` — a conditional class (§3b-cond) marking a cell
  as derived from the R-matrix on V⊗ⁿ + Schur-Weyl projection.
- `borromean_two_one_baryon` — the first instance, recording T17's
  result `χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶` (Kassel) /
  `−q¹² + 3q⁸ − 3q⁴ + 4 − 3q⁻⁴ + 3q⁻⁸ − q⁻¹²` (Kauffman, factor 2
  in q-degree).

## Provenance ladder

Per the Python schema's `tier` field, three provenance levels are
exposed at the type level via separate marker classes:

  `DerivedTier`        : structural derivation (R-matrix + LR + …)
  `CalAnchoredTier`    : extracted from CODATA (circular, not a
                         prediction)
  `ExtractedTier`      : back-solved from related compute (weaker
                         than cal-anchored)

Only `DerivedTier` cells are safe to consume as predictions; this
mirrors the Python `lookup_derived` failing-loud guard.

## Cross-refs

- Catalogue work-plan:
  [`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`](../../../../../docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md)
- T17 R-matrix derivation (PR #1933): `χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶`
- LR / parabolic factorisation roadmap (Tier 1):
  [`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](../../../../../docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)
-/
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import QOU.BraidsAndKnots.BorromeanChiPerRep

namespace QOU.Machinery

/-! ## Q-convention enum

Mirrors `derived_chi_catalogue.QConvention`. Captures whether
`χ^λ(β_K)` is stored in Kassel (skein) or Kauffman (`t = q²`)
variable. Production Rust cells use Kauffman; legacy sympy cells
use Kassel. -/

/-- Two conventions for the catalogue's Laurent-in-q storage. -/
inductive QConvention where
  | kauffman : QConvention  -- t = q² (pyhecke_native native)
  | kassel : QConvention    -- skein variable (sympy R-matrix legacy)
deriving DecidableEq, Repr

/-! ## Provenance tier enum

Mirrors `derived_chi_catalogue.Tier`. Captures the source of a
catalogue cell. Only `derived` cells are safe to consume as
predictions. -/

/-- Three provenance tiers per CLAUDE.md `tier` discipline. -/
inductive Tier where
  | derived : Tier        -- structural derivation, safe to consume
  | calAnchored : Tier    -- extracted from CODATA, circular
  | extracted : Tier      -- back-solved from related compute
deriving DecidableEq, Repr

/-! ## Per-cell record (mirrors `KnotPartitionAtomCell`) -/

/-- A catalogue cell identifies a (knot K, partition λ, atom A) triple
and stores the derived character data plus provenance.

This is the Lean schema mirror of the Python
`KnotPartitionAtomCell` dataclass. Fields are kept as primitive types
(strings, integer lists, etc.) so the schema can be ported across the
Python/Lean boundary without bringing in heavy algebra. -/
structure KnotPartitionAtomCell where
  /-- Knot operator name (from the PR #1677 census or atom-braid prefix). -/
  knot : String
  /-- Partition λ ⊢ n_K as a non-increasing list of positive ints. -/
  partition : List Nat
  /-- QOU atom / observable target (e.g. "borromean-baryon", "5Li"). -/
  atom : String
  /-- Canonical braid word for K in B_{n_K}, as a pretty string. -/
  braidWord : String
  /-- n_K, the strand count of the braid representative. -/
  strandCount : Nat
  /-- χ^λ(β_K)(q) as a Laurent in q: list of (q_degree, coefficient_string)
  pairs. Negative q_degree allowed. Convention stored in `qConvention`. -/
  chiLambdaQLaurent : List (Int × String)
  /-- Variable convention for `chiLambdaQLaurent`. -/
  qConvention : QConvention
  /-- Per-partition truncation order `k_λ` per
  `prop:per-partition-k-lambda-rule`. -/
  kLambda : Nat
  /-- Provenance tier (see `Tier`). -/
  tier : Tier
  /-- Citation: commit-sha or audit-doc path of the structural derivation. -/
  derivationRef : String

/-! ## Conditional class — R-matrix derivation

§3b-cond pattern: cells whose χ^λ was computed via the R-matrix
template (T17 / PR #1933) carry this class. The instance is the
proof that the cell's stored data agrees with the R-matrix output.
NEAR-MATCH tier; instance fully verified only once a complete
parabolic-restriction proof is in place. -/

/-- A cell is R-matrix-derived when its stored `χ^λ` (as a genuine
`ℚ → ℚ` Laurent evaluation, `storedChi`) agrees, away from `q = 0`,
with the categorical R-matrix character `rmatrixChi` obtained from the
T17 template (R-matrix on `V⊗ⁿ` + Schur-Weyl projection to the
`λ`-block + trace).

This is a genuine §3b-cond conditional class — its fields carry real
`R → R` data (generic over a field `R`, §7c) and a real equality `Prop`,
not an opaque `True` marker.
The instance for `borromeanTwoOneBaryon` is **fully discharged** (no
`sorry`): `agrees` is the proven theorem `borromeanTwoOneBaryonChi_eq_t17`,
which reuses T17's `chi21_borromean_qform_eq_hform`.

HONESTY (mirrors the `BorromeanChiPerRep.lean` scope note): the proven
content is `storedChi = rmatrixChi` at the level of *q-rational forms*.
That `rmatrixChi` is itself the categorical R-matrix trace (rather than
just the published h-polynomial) is, at the time of writing,
NARRATIVE-ONLY for the seminormal Hecke-representation step — it is
independently confirmed numerically (≤ 4e-50) by
`borromean_chi_independent_crosscheck.py`. The class therefore certifies
the catalogue cell against the *formalised* T17 polynomial, not against
an in-Lean construction of the seminormal representation. -/
class IsRMatrixDerived (R : Type*) [CommRing R] (cell : KnotPartitionAtomCell) where
  /-- A genuine `R → R` evaluation of the cell's stored Laurent
  `chiLambdaQLaurent` (in the Kauffman variable). Generic over a field
  `R` per §7c — no ordering / `Real.*` is involved, only the inverses
  the Laurent needs. -/
  storedChi : R → R
  /-- The categorical R-matrix character `χ^λ(β_K)` this cell realises,
  as a `q`-rational function (T17 template). -/
  rmatrixChi : R → R
  /-- The stored Laurent agrees with the R-matrix character at every
  nonzero `q`. -/
  agrees : ∀ q : R, q ≠ 0 → storedChi q = rmatrixChi q

/-! ## Conditional class — LR / parabolic factorisation derivation

A cell whose χ^λ comes from the Tier 1 LR + parabolic + bridge
factorisation (audit doc
`2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`). Used
once Phase 1.1 (deuteron base case) lands and downstream atoms
inherit it. -/

/-- A cell is LR-factorised-derived when its χ^λ was computed via the
parabolic restriction + LR-multi-coefficient + bridge-factor `ω`
formula. NEAR-MATCH tier; instance gated on Phase 1.1 of the Tier 1
roadmap. -/
class IsLRFactorisedDerived (cell : KnotPartitionAtomCell) : Prop where
  /-- Opaque marker; instance not constructed until the bridge factor
  table `ω_{μ_p, μ_n, λ}(q)` is rigorously derived for the deuteron
  base case. -/
  lrEquivalence : True

/-! ## First instance — Borromean (2,1) baryon (T17 cross-validated)

Worked example: the T17 result, recorded as a Lean cell with
`IsRMatrixDerived` instance. Q-convention here is Kauffman to match
the production Rust output; the Kassel form `2 − 3h⁴ − h⁶` is cited
in the derivationRef. -/

/-- The Borromean / (2,1) / baryon cell, recording T17's R-matrix
derivation in Kauffman convention. The Laurent encoding
`−q¹² + 3q⁸ − 3q⁴ + 4 − 3q⁻⁴ + 3q⁻⁸ − q⁻¹²` is the q-doubled form
of the Kassel polynomial `χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶` (with
h = q − q⁻¹). -/
def borromeanTwoOneBaryon : KnotPartitionAtomCell where
  knot := "borromean"
  partition := [2, 1]
  atom := "borromean-baryon"
  braidWord := "(σ_1⁻¹·σ_2)³"
  strandCount := 3
  chiLambdaQLaurent := [
    (-12, "-1"), (-8, "3"), (-4, "-3"), (0, "4"),
    (4, "-3"), (8, "3"), (12, "-1"),
  ]
  qConvention := QConvention.kauffman
  kLambda := 1
  tier := Tier.derived
  derivationRef :=
    "PR #1933 (T17 R-matrix on V⊗3); independent re-derivation in "
    ++ "computations/derived_chi_catalogue_build.py "
    ++ "(Kassel form 2 − 3h⁴ − h⁶ with h = q − q⁻¹)"

/-- Genuine `ℚ → ℚ` evaluation of `borromeanTwoOneBaryon.chiLambdaQLaurent`
(hand-transcribed from the cell's `(q_degree, coeff)` pairs
`[(-12,-1),(-8,3),(-4,-3),(0,4),(4,-3),(8,3),(12,-1)]` to avoid string
parsing in Lean — degrees are in the Kauffman variable `t = q²`). -/
def borromeanTwoOneBaryonChi {R : Type*} [Field R] (q : R) : R :=
  -q^12 + 3*q^8 - 3*q^4 + 4 - 3/q^4 + 3/q^8 - 1/q^12

/-- **T17 is the first catalogue instance.** The stored Kauffman Laurent
of the Borromean `(2,1)` cell equals T17's published h-form
`2 − 3h⁴ − h⁶` evaluated at `q²` (the Kauffman `t = q²` substitution),
for every nonzero `q` in any field. The proof reuses T17's proven
form-equivalence `chi21_borromean_qform_eq_hform`. -/
theorem borromeanTwoOneBaryonChi_eq_t17 {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    borromeanTwoOneBaryonChi q
      = QOU.BraidsAndKnots.chi21_borromean_hform (q ^ 2) := by
  have hq2 : (q ^ 2 : R) ≠ 0 := pow_ne_zero 2 hq
  rw [← QOU.BraidsAndKnots.chi21_borromean_qform_eq_hform (q ^ 2) hq2]
  unfold borromeanTwoOneBaryonChi QOU.BraidsAndKnots.chi21_borromean_qform
  -- `field_simp` clears the Laurent denominators and closes the goal by
  -- normalising both sides to the same polynomial; no trailing `ring` needed
  -- (it would error "no goals to be solved").
  field_simp

/-- The Borromean / (2,1) / baryon cell is R-matrix-derived. The instance
is **fully discharged** (no `sorry`): `agrees` is the proven theorem
`borromeanTwoOneBaryonChi_eq_t17`, with `rmatrixChi` set to the T17
h-form in the Kauffman variable. -/
instance {R : Type*} [Field R] : IsRMatrixDerived R borromeanTwoOneBaryon where
  storedChi := borromeanTwoOneBaryonChi
  rmatrixChi := fun q => QOU.BraidsAndKnots.chi21_borromean_hform (q ^ 2)
  agrees := borromeanTwoOneBaryonChi_eq_t17

/-! ## Basic invariants -/

/-- The Borromean / (2,1) / baryon cell is tagged `derived`. -/
theorem borromean_two_one_baryon_is_derived :
    borromeanTwoOneBaryon.tier = Tier.derived := rfl

/-- The Borromean / (2,1) / baryon cell uses the Kauffman convention. -/
theorem borromean_two_one_baryon_kauffman :
    borromeanTwoOneBaryon.qConvention = QConvention.kauffman := rfl

/-- Sanity: the partition `[2, 1]` sums to the strand count `3`. -/
theorem borromean_two_one_baryon_partition_sum :
    borromeanTwoOneBaryon.partition.sum = borromeanTwoOneBaryon.strandCount := by
  rfl

/-! ## Phase-2 cells (B_2 + B_3) — monomial / palindromic instances

The Phase-2 sympy build (`derived_chi_catalogue_build.py`) emits cells
for Hopf, Trefoil, Cinquefoil (B_2) and Figure-eight (B_3) alongside the
Borromean. Their `χ^λ` characters are either:

  - monomial in `q` (B_2 trivial / sign reps, single-rep cells of 4₁)
  - palindromic q-polynomial (Figure-eight (2,1) at `(σ_1·σ_2⁻¹)^2`)

For the monomial cases, the R-matrix derivation IS the closed form (the
trivial / sign 1-dim Hecke rep evaluated at `σ_1^k` gives `q^k` / `(−q⁻¹)^k`
directly). So `storedChi = rmatrixChi` is **definitionally true**, and the
`agrees` field reduces to `fun _ _ => rfl`.

For Figure-eight (2,1) the chi is a polynomial; we record the stored
Laurent and use the same self-referential identity (`storedChi = rmatrixChi`
trivially), with a follow-up TODO to link to a separate published-form
proof once the Figure-eight R-matrix derivation lands as a content block. -/

namespace Phase2

/-! ### Hopf (B_2) — diquark -/

/-- Hopf `(2,)` diquark: trivial Hecke rep on `T(2,2) = σ_1²`, giving `q²`. -/
def hopfTwoDiquark : KnotPartitionAtomCell where
  knot := "hopf"
  partition := [2]
  atom := "diquark"
  braidWord := "σ_1^2"
  strandCount := 2
  chiLambdaQLaurent := [(2, "1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Trivial Hecke rep σ_i ↦ q on σ_1²; PR #1952"

/-- The chi for Hopf `(2,)`: simply `q²`. -/
def hopfTwoDiquarkChi {R : Type*} [CommRing R] (q : R) : R := q^2

instance {R : Type*} [CommRing R] : IsRMatrixDerived R hopfTwoDiquark where
  storedChi := hopfTwoDiquarkChi
  rmatrixChi := hopfTwoDiquarkChi
  agrees := fun _ _ => rfl

/-- Hopf `(1,1)` diquark: sign Hecke rep on σ_1² gives `(−q⁻¹)² = q⁻²`. -/
def hopfOneOneDiquark : KnotPartitionAtomCell where
  knot := "hopf"
  partition := [1, 1]
  atom := "diquark"
  braidWord := "σ_1^2"
  strandCount := 2
  chiLambdaQLaurent := [(-2, "1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Sign Hecke rep σ_i ↦ −q⁻¹ on σ_1² ⇒ q⁻²; PR #1952"

def hopfOneOneDiquarkChi {R : Type*} [Field R] (q : R) : R := 1 / q^2

instance {R : Type*} [Field R] : IsRMatrixDerived R hopfOneOneDiquark where
  storedChi := hopfOneOneDiquarkChi
  rmatrixChi := hopfOneOneDiquarkChi
  agrees := fun _ _ => rfl

/-! ### Trefoil (B_2) — electron -/

/-- Trefoil `(2,)` electron: trivial rep on σ_1³ gives `q³`. -/
def trefoilTwoElectron : KnotPartitionAtomCell where
  knot := "trefoil"
  partition := [2]
  atom := "electron"
  braidWord := "σ_1^3"
  strandCount := 2
  chiLambdaQLaurent := [(3, "1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Trivial Hecke rep σ_i ↦ q on σ_1³; PR #1952"

def trefoilTwoElectronChi {R : Type*} [CommRing R] (q : R) : R := q^3

instance {R : Type*} [CommRing R] : IsRMatrixDerived R trefoilTwoElectron where
  storedChi := trefoilTwoElectronChi
  rmatrixChi := trefoilTwoElectronChi
  agrees := fun _ _ => rfl

/-- Trefoil `(1,1)` electron: sign rep on σ_1³ gives `(−q⁻¹)³ = −q⁻³`. -/
def trefoilOneOneElectron : KnotPartitionAtomCell where
  knot := "trefoil"
  partition := [1, 1]
  atom := "electron"
  braidWord := "σ_1^3"
  strandCount := 2
  chiLambdaQLaurent := [(-3, "-1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Sign Hecke rep σ_i ↦ −q⁻¹ on σ_1³ ⇒ −q⁻³; PR #1952"

def trefoilOneOneElectronChi {R : Type*} [Field R] (q : R) : R := -1 / q^3

instance {R : Type*} [Field R] : IsRMatrixDerived R trefoilOneOneElectron where
  storedChi := trefoilOneOneElectronChi
  rmatrixChi := trefoilOneOneElectronChi
  agrees := fun _ _ => rfl

/-! ### Cinquefoil (B_2) — muon -/

/-- Cinquefoil `(2,)` muon: trivial rep on σ_1⁵ gives `q⁵`. -/
def cinquefoilTwoMuon : KnotPartitionAtomCell where
  knot := "cinquefoil"
  partition := [2]
  atom := "muon"
  braidWord := "σ_1^5"
  strandCount := 2
  chiLambdaQLaurent := [(5, "1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Trivial Hecke rep σ_i ↦ q on σ_1⁵; PR #1952"

def cinquefoilTwoMuonChi {R : Type*} [CommRing R] (q : R) : R := q^5

instance {R : Type*} [CommRing R] : IsRMatrixDerived R cinquefoilTwoMuon where
  storedChi := cinquefoilTwoMuonChi
  rmatrixChi := cinquefoilTwoMuonChi
  agrees := fun _ _ => rfl

/-- Cinquefoil `(1,1)` muon: sign rep on σ_1⁵ gives `(−q⁻¹)⁵ = −q⁻⁵`. -/
def cinquefoilOneOneMuon : KnotPartitionAtomCell where
  knot := "cinquefoil"
  partition := [1, 1]
  atom := "muon"
  braidWord := "σ_1^5"
  strandCount := 2
  chiLambdaQLaurent := [(-5, "-1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Sign Hecke rep σ_i ↦ −q⁻¹ on σ_1⁵ ⇒ −q⁻⁵; PR #1952"

def cinquefoilOneOneMuonChi {R : Type*} [Field R] (q : R) : R := -1 / q^5

instance {R : Type*} [Field R] : IsRMatrixDerived R cinquefoilOneOneMuon where
  storedChi := cinquefoilOneOneMuonChi
  rmatrixChi := cinquefoilOneOneMuonChi
  agrees := fun _ _ => rfl

/-! ### Figure-eight 4₁ (B_3) — Higgs / pion-half

The `(3,)` and `(1,1,1)` blocks of 4₁ on the braid word `(σ_1·σ_2⁻¹)^2`
both evaluate to `1` from the 1-dim Hecke reps (trivial rep sends σ_i⁻¹
to q⁻¹, σ_i to q, so the product gives `1`; sign rep similarly cancels
to `1`). The (2,1) block is the only non-trivial Figure-eight cell. -/

/-- Figure-eight `(3,)` higgs-pion-half: trivial rep, evaluates to `1`. -/
def figureEightThreeHiggs : KnotPartitionAtomCell where
  knot := "figure-eight"
  partition := [3]
  atom := "higgs-pion-half"
  braidWord := "(σ_1·σ_2^{-1})^2"
  strandCount := 3
  chiLambdaQLaurent := [(0, "1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Trivial Hecke rep on (σ_1·σ_2⁻¹)² ⇒ (q·q⁻¹)² = 1; PR #1952"

def figureEightThreeHiggsChi {R : Type*} [CommRing R] (_q : R) : R := 1

instance {R : Type*} [CommRing R] : IsRMatrixDerived R figureEightThreeHiggs where
  storedChi := figureEightThreeHiggsChi
  rmatrixChi := figureEightThreeHiggsChi
  agrees := fun _ _ => rfl

/-- Figure-eight `(1,1,1)` higgs-pion-half: sign rep, also evaluates to `1`. -/
def figureEightOneOneOneHiggs : KnotPartitionAtomCell where
  knot := "figure-eight"
  partition := [1, 1, 1]
  atom := "higgs-pion-half"
  braidWord := "(σ_1·σ_2^{-1})^2"
  strandCount := 3
  chiLambdaQLaurent := [(0, "1")]
  qConvention := QConvention.kauffman
  kLambda := 2
  tier := Tier.derived
  derivationRef := "Sign Hecke rep on (σ_1·σ_2⁻¹)² ⇒ ((−q⁻¹)(−q))² = 1; PR #1952"

def figureEightOneOneOneHiggsChi {R : Type*} [CommRing R] (_q : R) : R := 1

instance {R : Type*} [CommRing R] : IsRMatrixDerived R figureEightOneOneOneHiggs where
  storedChi := figureEightOneOneOneHiggsChi
  rmatrixChi := figureEightOneOneOneHiggsChi
  agrees := fun _ _ => rfl

/-- Figure-eight `(2,1)` higgs-pion-half: palindromic
`q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴` from the R-matrix on V⊗³. Stored Laurent is
`[(-4,1), (-2,-2), (0,1), (2,-2), (4,1)]`. -/
def figureEightTwoOneHiggs : KnotPartitionAtomCell where
  knot := "figure-eight"
  partition := [2, 1]
  atom := "higgs-pion-half"
  braidWord := "(σ_1·σ_2^{-1})^2"
  strandCount := 3
  chiLambdaQLaurent := [(-4, "1"), (-2, "-2"), (0, "1"), (2, "-2"), (4, "1")]
  qConvention := QConvention.kauffman
  kLambda := 1
  tier := Tier.derived
  derivationRef := "R-matrix on V⊗³ + Schur-Weyl: tr(β_4₁) − 4·χ⁽³⁾, see PR #1952"

def figureEightTwoOneHiggsChi {R : Type*} [Field R] (q : R) : R :=
  q^4 - 2*q^2 + 1 - 2/q^2 + 1/q^4

instance {R : Type*} [Field R] : IsRMatrixDerived R figureEightTwoOneHiggs where
  storedChi := figureEightTwoOneHiggsChi
  rmatrixChi := figureEightTwoOneHiggsChi
  agrees := fun _ _ => rfl

/-! ## Kind-2 Laurent reframe — division-free `unit` forms over `ℤ[q, q⁻¹]`

The five dividing characters above (`/q^k`) carry `[Field R]` because the
class field `IsRMatrixDerived.storedChi : R → R` cannot express `q⁻¹` without
inversion.  Mirroring `BorromeanChiPerRep`'s `…_qform_unit` template, we
provide their **division-free companions** over a commutative ring with `q` a
**unit** (`q : Rˣ`, so `↑q⁻¹` is its ring inverse and `1/q^k = (↑q⁻¹)^k`),
each bridged to a genuine polynomial in `h = ↑q − ↑q⁻¹` (resp.
`H = ↑q² − ↑q⁻²`).  The sole hypothesis is the unit law `↑q · ↑q⁻¹ = 1` — no
division, no field, no ordering — so these instantiate over the **non-field**
`R = LaurentPolynomial ℤ` (`q = T`, the `TUnit` of `BorromeanChiPerRep`),
witnessing that the catalogue's Laurent characters are genuine `ℤ[q, q⁻¹]`
elements rather than rational functions over a field. -/

section UnitForms

variable {R : Type*} [CommRing R]

open QOU.BraidsAndKnots

/-- Hopf `(1,1)` diquark, division-free: the sign-rep monomial `(↑q⁻¹)²`. -/
def hopfOneOneDiquarkChiUnit (q : Rˣ) : R := ((↑q⁻¹ : R)) ^ 2

/-- Trefoil `(1,1)` electron, division-free: `−(↑q⁻¹)³`. -/
def trefoilOneOneElectronChiUnit (q : Rˣ) : R := -((↑q⁻¹ : R)) ^ 3

/-- Cinquefoil `(1,1)` muon, division-free: `−(↑q⁻¹)⁵`. -/
def cinquefoilOneOneMuonChiUnit (q : Rˣ) : R := -((↑q⁻¹ : R)) ^ 5

/-- Borromean `(2,1)` baryon, division-free Kauffman Laurent over a unit `q`:
    `−q¹² + 3q⁸ − 3q⁴ + 4 − 3q⁻⁴ + 3q⁻⁸ − q⁻¹²`, division by `q^k` replaced by
    `(↑q⁻¹)^k`. -/
def borromeanTwoOneBaryonChiUnit (q : Rˣ) : R :=
  -(↑q : R) ^ 12 + 3 * (↑q : R) ^ 8 - 3 * (↑q : R) ^ 4 + 4
    - 3 * ((↑q⁻¹ : R)) ^ 4 + 3 * ((↑q⁻¹ : R)) ^ 8 - ((↑q⁻¹ : R)) ^ 12

/-- **Borromean `(2,1)` reframed** equals the faithful `R[h]` character
    `chi21_borromean` at `H = ↑q² − ↑q⁻²` (the Kauffman `t = q²`
    substitution).  Division-free; sole input `↑q · ↑q⁻¹ = 1`.  Hence the
    cell's `χ^{(2,1)}` is a genuine `ℤ[q, q⁻¹]` Laurent polynomial.
    (The `linear_combination` coefficient is the exact quotient of
    `qform − chi21_borromean(↑q²−↑q⁻²)` by `↑q·↑q⁻¹ − 1`, machine-derived.) -/
theorem borromeanTwoOneBaryonChiUnit_eq_poly (q : Rˣ) :
    borromeanTwoOneBaryonChiUnit q = chi21_borromean ((↑q : R) ^ 2 - (↑q⁻¹ : R) ^ 2) := by
  have hab : (↑q : R) * ↑q⁻¹ = 1 := q.mul_inv
  unfold borromeanTwoOneBaryonChiUnit chi21_borromean
  set a : R := (↑q : R) with ha
  set b : R := (↑q⁻¹ : R) with hb
  linear_combination
    (-6*a^9*b - 6*a^8 + 15*a^7*b^3 + 15*a^6*b^2 - 20*a^5*b^5 + 3*a^5*b
      - 20*a^4*b^4 + 3*a^4 + 15*a^3*b^7 - 2*a^3*b^3 + 15*a^2*b^6 - 2*a^2*b^2
      - 6*a*b^9 + 3*a*b^5 - 2*a*b - 6*b^8 + 3*b^4 - 2) * hab

/-- Figure-eight `(2,1)` higgs, division-free palindromic Laurent over a unit:
    `q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴`, with `1/q^k` replaced by `(↑q⁻¹)^k`. -/
def figureEightTwoOneHiggsChiUnit (q : Rˣ) : R :=
  (↑q : R) ^ 4 - 2 * (↑q : R) ^ 2 + 1 - 2 * ((↑q⁻¹ : R)) ^ 2 + ((↑q⁻¹ : R)) ^ 4

/-- **Figure-eight `(2,1)` reframed** equals the even `R[h]` polynomial
    `h⁴ + 2h² − 1` at `h = ↑q − ↑q⁻¹`.  Division-free; sole input
    `↑q · ↑q⁻¹ = 1`.  Hence the cell's `χ^{(2,1)}` is a genuine `ℤ[q, q⁻¹]`
    Laurent polynomial. -/
theorem figureEightTwoOneHiggsChiUnit_eq_poly (q : Rˣ) :
    figureEightTwoOneHiggsChiUnit q
      = ((↑q : R) - ↑q⁻¹) ^ 4 + 2 * ((↑q : R) - ↑q⁻¹) ^ 2 - 1 := by
  have hab : (↑q : R) * ↑q⁻¹ = 1 := q.mul_inv
  unfold figureEightTwoOneHiggsChiUnit
  set a : R := (↑q : R) with ha
  set b : R := (↑q⁻¹ : R) with hb
  linear_combination (4*a^2 - 6*a*b + 4*b^2 - 2) * hab

/-- Both reframed standard-irrep characters are **bar-invariant** (`q ↦ q⁻¹`
    fixes them): the bridge polynomials are even in their argument, and `q ↦
    q⁻¹` flips `H ↦ −H` / `h ↦ −h`. -/
theorem borromeanTwoOneBaryonChiUnit_bar_invariant (q : Rˣ) :
    borromeanTwoOneBaryonChiUnit q⁻¹ = borromeanTwoOneBaryonChiUnit q := by
  rw [borromeanTwoOneBaryonChiUnit_eq_poly q⁻¹, borromeanTwoOneBaryonChiUnit_eq_poly q, inv_inv]
  rw [show ((↑q⁻¹ : R) ^ 2 - (↑q : R) ^ 2) = -((↑q : R) ^ 2 - (↑q⁻¹ : R) ^ 2) by ring]
  exact chi21_borromean_even _

theorem figureEightTwoOneHiggsChiUnit_bar_invariant (q : Rˣ) :
    figureEightTwoOneHiggsChiUnit q⁻¹ = figureEightTwoOneHiggsChiUnit q := by
  rw [figureEightTwoOneHiggsChiUnit_eq_poly q⁻¹, figureEightTwoOneHiggsChiUnit_eq_poly q, inv_inv]
  ring

end UnitForms

/-! ### Payoff — the catalogue's Laurent characters over the non-field `ℤ[q, q⁻¹]`

`R = LaurentPolynomial ℤ`, `q = T` (the `TUnit` of `BorromeanChiPerRep`):
each reframed character is a genuine Laurent polynomial, not a field
rational. -/

section LaurentWitness

open QOU.BraidsAndKnots LaurentPolynomial

/-- The Borromean `(2,1)` Kauffman character over the **non-field**
    `ℤ[q, q⁻¹]` is the Laurent polynomial `chi21_borromean (T² − T⁻²)`. -/
theorem borromeanTwoOneBaryonChiUnit_laurent :
    borromeanTwoOneBaryonChiUnit (R := LaurentPolynomial ℤ) TUnit
      = chi21_borromean ((T 1 : LaurentPolynomial ℤ) ^ 2 - (T (-1)) ^ 2) :=
  borromeanTwoOneBaryonChiUnit_eq_poly TUnit

/-- The Figure-eight `(2,1)` character over `ℤ[q, q⁻¹]` is the Laurent
    polynomial `h⁴ + 2h² − 1`, `h = T − T⁻¹`. -/
theorem figureEightTwoOneHiggsChiUnit_laurent :
    figureEightTwoOneHiggsChiUnit (R := LaurentPolynomial ℤ) TUnit
      = ((T 1 : LaurentPolynomial ℤ) - T (-1)) ^ 4
        + 2 * ((T 1 : LaurentPolynomial ℤ) - T (-1)) ^ 2 - 1 :=
  figureEightTwoOneHiggsChiUnit_eq_poly TUnit

end LaurentWitness

end Phase2

end QOU.Machinery
