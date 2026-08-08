/-
  Δ_λ as a Donaldson–Thomas / 3d-index graded Euler characteristic —
  the categorical home that unifies the two horns into ONE signed object.

  Context (epic `qou-r2nh`, bean `qou-f0ny`).  Two just-landed honest
  negatives bracket the per-partition binding factor `Δ_λ`:

    • Horn 1 (PR #4540, `StokesPhaseSignChirality`): the Δ_λ chirality SIGN
      is the Lusztig a-function / b-invariant parity `(-1)^{n(λ)}`
      (`PartitionOf5.deltaSign_eq_nStat_parity`, this repo), a real π-phase —
      NOT the resurgent ±i (π/2) Stokes phase.

    • Horn 2 (PR #4538, `StokesConstantQDimCategoricity`): the Δ_λ MAGNITUDE
      is NOT a KL-positive categorical q-dimension (the GGM descendant series
      has a negative coefficient); it is a signed, positivity-VIOLATING
      DT / 3d-index integer.

  Both horns share ONE invariant — KL-positivity — and both point at the SAME
  home: a *signed, a-graded, DT-index* object, not a positive-categorical one.

  This file makes that home precise and PROVES the unification (sorry-free,
  `decide`) at the `n = 5` anchor, building on the established per-partition
  data in `S5SO3FiberAction` (`nStat` = the a-function, `deltaSign`,
  `deltaLambda`, `deltaSign_eq_nStat_parity`, `binding_magnitude_eq_dim`):

    Δ_λ  =  (Behrend-signed) Donaldson–Thomas count of the Springer fibre 𝓑_λ.

  The Springer correspondence puts the Wedderburn irrep `V_λ` in the top
  cohomology of the Springer fibre `𝓑_λ`, whose COMPLEX dimension is exactly
  the a-function `n(λ)` (type A).  A DT / BPS invariant weights the point count
  by the Behrend function, contributing the sign `(-1)^{dim moduli}` on the
  smooth locus.  Hence

      DT(𝓑_λ)  =  (-1)^{dim_ℂ 𝓑_λ} · (count)  =  (-1)^{n(λ)} · dim V_λ  =  Δ_λ .

  So a SINGLE DT invariant supplies BOTH horns at once:
    – the Behrend `(-1)^{dim}` sign  ↦  horn-1 chirality `(-1)^{n(λ)}`;
    – the count `dim V_λ`            ↦  horn-2 magnitude;
  and the same odd complex dimension that makes the sign negative is exactly
  what pushes the count out of ℕ (horn-2's positivity violation).  Horn-1 and
  horn-2 are the SAME phenomenon: an odd a-function grade.

  Decategorified, `DT(𝓑_λ)` is the alternating (Euler-characteristic) sum of a
  graded object concentrated in degree `n(λ)` — a genuine finite alternating
  sum, computed below.

  Scope / discipline (STRICT).  This is the per-partition `Δ_λ` factor.  It is
  NOT a binding-energy closure: the many-body A=3 magnitude scalar
  `r* = μ₃/c₃ ≈ 1.585` is a distinct, still-open cluster-integral object,
  walled from every route (Hecke level / geometric `W_λ` / coordination edge /
  Milnor / Vassiliev; see `docs/coordination/option-e.md`).  Nothing here is
  fitted; nothing is wired to production; no anchor is inverted.  The internal
  derivation — that the QOU substrate *forces* the DT moduli `𝓑_λ` (dimension
  `n(λ)`, count `dim V_λ`) from the 13 categorical drivers, rather than the
  `(n(λ), dim V_λ)` data being read off — is carried as an OPEN, content-bearing
  primary conjecture with NO instance (§3b-tax).

  Primary sources:
  Behrend, Donaldson–Thomas type invariants via microlocal geometry,
    Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307
  Springer, A construction of representations of Weyl groups,
    Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165
  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
-/
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic.NormNum
import QOU.BraidsAndKnots.S5SO3FiberAction

namespace QOU.BraidsAndKnots

/-! ## The single-degree Springer/DT graded object `G_λ`

    `G_λ` is the decategorified Springer shadow: the Wedderburn irrep `V_λ`
    placed in the ONE cohomological degree `n(λ)` (the a-function = complex
    dimension of the Springer fibre `𝓑_λ`), zero elsewhere.  Its graded Euler
    characteristic is the DT / Behrend-signed count. -/

/-- Graded dimension of `G_λ`: `dim V_λ` concentrated in degree `n(λ)`. -/
def PartitionOf5.gradedDim (p : PartitionOf5) (k : ℕ) : ℕ :=
  if k = p.nStat then p.dim else 0

/-- The DT / 3d-index graded Euler characteristic
    `χ(G_λ) = Σ_{k=0}^{n(λ)} (-1)^k · dim (G_λ)_k` — a genuine finite
    alternating sum (the Behrend-weighted count of `𝓑_λ`). -/
def PartitionOf5.dtEuler (p : PartitionOf5) : ℤ :=
  ((List.range (p.nStat + 1)).map
    (fun k => (-1 : ℤ) ^ k * (p.gradedDim k : ℤ))).sum

/-! ## The unification: ONE object supplies both horns -/

/-- **The DT Euler characteristic is the sign × magnitude split**: the
    alternating sum collapses (single-degree concentration) to
    `(-1)^{n(λ)} · dim V_λ` — the Behrend sign `(-1)^{dim moduli}` times the
    count.  Sign and magnitude are the parity and value of ONE graded datum. -/
theorem dtEuler_eq_sign_times_dim (p : PartitionOf5) :
    p.dtEuler = (-1 : ℤ) ^ p.nStat * (p.dim : ℤ) := by
  cases p <;> decide

/-- **THE UNIFICATION (both horns from one object).**  The DT / 3d-index Euler
    characteristic of `G_λ` equals the corpus binding factor `Δ_λ`
    (`deltaLambda = deltaSign · dim`).  So the horn-1 sign
    (`deltaSign = (-1)^{n(λ)}`) and the horn-2 magnitude (`|Δ_λ| = dim`) are
    the sign and the size of a SINGLE Donaldson–Thomas invariant — not two
    independent ingredients. -/
theorem dtEuler_eq_deltaLambda (p : PartitionOf5) :
    p.dtEuler = p.deltaLambda := by
  cases p <;> decide

/-- **Horn-2 magnitude leg**: `(DT Euler)² = (dim V_λ)²`, i.e. the DT count's
    magnitude is the Wedderburn dimension.  (Equivalent to
    `binding_magnitude_eq_dim` via the unification.) -/
theorem dtEuler_magnitude_eq_dim (p : PartitionOf5) :
    p.dtEuler ^ 2 = (p.dim : ℤ) ^ 2 := by
  cases p <;> decide

/-- **Horn-1 sign leg**: the DT Euler characteristic is negative *iff* the
    a-function grade `n(λ)` is odd (all `dim V_λ > 0` at `n = 5`).  The Behrend
    `(-1)^{dim moduli}` sign is negative exactly on odd-dimensional moduli.
    (Oddness written as `n(λ) % 2 = 1` to keep the import surface within the
    `n = 5` anchor's cached olean set.) -/
theorem dtEuler_neg_iff_odd_grade (p : PartitionOf5) :
    p.dtEuler < 0 ↔ p.nStat % 2 = 1 := by
  cases p <;> decide

/-- **The two horns are ONE phenomenon (the crux).**  A partition with an ODD
    a-function grade simultaneously
      • carries the horn-1 minus sign (`dtEuler < 0`), and
      • escapes ℕ (`dtEuler < 0`), so it is NOT a KL-positive q-dimension
        (horn-2's positivity violation).
    Both are caused by the SAME odd grade — witnessed by `(4,1)`
    (`n(λ) = 1`, `Δ = -4`). -/
theorem horns_share_one_odd_grade :
    ∃ p : PartitionOf5,
      p.nStat % 2 = 1 ∧ p.dtEuler < 0 ∧ p.dtEuler = -(p.dim : ℤ) := by
  refine ⟨.fourOne, ?_, ?_, ?_⟩ <;> decide

/-- **Horn-2 consistency: `Δ_λ` is NOT a KL-positive q-dimension.**  Some block
    has a strictly negative DT Euler characteristic, so the sequence `(Δ_λ)_λ`
    leaves `ℕ` — it cannot be the `q = 1` value of any KL-positive (non-negative
    Laurent) quantum dimension.  A positivity-violating DT / 3d-index integer,
    exactly as horn 2 concluded. -/
theorem deltaLambda_not_kl_positive :
    ∃ p : PartitionOf5, p.deltaLambda < 0 := by
  refine ⟨.fourOne, ?_⟩; decide

/-- **Mixed sign from the grading (both horns, packaged).**  Both a positive
    and a negative DT Euler characteristic occur — the positive one from an
    even a-function grade, the negative one from an odd grade.  This is the
    `deltaSign_mixed` fact re-read as the two parities of one graded object. -/
theorem dtEuler_mixed_sign :
    (∃ p : PartitionOf5, 0 < p.dtEuler) ∧ (∃ p : PartitionOf5, p.dtEuler < 0) :=
  ⟨⟨.five, by decide⟩, ⟨.fourOne, by decide⟩⟩

/-! ## The open internal-derivation gap — content-bearing primary conjecture

    Everything above unifies the per-partition `Δ_λ` into ONE DT / 3d-index
    Euler characteristic using the a-function `n(λ)` as the grade and the
    Wedderburn dimension `dim V_λ` as the count.  Both inputs are corpus-derived
    from the substrate (the a-function is the Gröbner–Shirshov jet-order
    fake-degree valuation, `docs/coordination/option-e.md` 2026-07-18 front (i);
    the dimension is the `H_n(q) → Wedderburn` block dimension of the canonical
    derivation chain).

    What remains OPEN is the *internal* derivation: does the QOU substrate
    FORCE the DT moduli `𝓑_λ` — a space of complex dimension `n(λ)` whose
    Behrend-weighted count is `dim V_λ` — from the 13 categorical drivers, so
    that `Δ_λ` is its DT invariant rather than the `(n(λ), dim V_λ)` data being
    identified after the fact?  This mirrors bean `qou-ujmw` for `A_ω = 3`
    (the DT-count identification is established; the internal derivation from
    the drivers is the open leg).

    Carried as a PRIMARY conjecture (no upstream conjecture in its signature),
    content-bearing, with NO instance (the open state, §3b-tax).  It is NOT
    consumed by any theorem below — it does not launder anything.  Transparency
    note (anti-laundering): the *shape* is satisfiable by the toy assignment
    `moduliDim := nStat`, `virtualCount := dim`, which merely READS the answer;
    that is NOT the derivation the conjecture asserts.  The content the open
    problem demands is that `moduliDim` and `virtualCount` be *outputs of the
    substrate* (the 13 drivers), which no instance supplies — hence none is
    given. -/

/-- **Open primary conjecture (content-bearing, NO instance).**  The QOU
    substrate forces a Donaldson–Thomas / 3d-index moduli `𝓑_λ` whose
    Behrend-signed count is the per-partition binding factor `Δ_λ`. -/
class DeltaLambdaDTRealization where
  /-- The substrate-forced complex dimension of the DT moduli `𝓑_λ`
      (conjecturally the a-function `n(λ)`). -/
  moduliDim : PartitionOf5 → ℕ
  /-- The substrate-forced Behrend-weighted point count of `𝓑_λ`
      (conjecturally the Wedderburn dimension `dim V_λ`). -/
  virtualCount : PartitionOf5 → ℕ
  /-- **Content**: the DT invariant `(-1)^{dim moduli} · count` reproduces the
      per-partition binding factor `Δ_λ` for every block. -/
  dt_index_eq_deltaLambda :
    ∀ p : PartitionOf5,
      (-1 : ℤ) ^ (moduliDim p) * (virtualCount p : ℤ) = p.deltaLambda

end QOU.BraidsAndKnots
