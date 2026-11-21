/-
  Δ_λ = DT-count of the Springer fibre `𝓑_λ`: the target constraint
  UNDER-DETERMINES the moduli — sharpening the open substrate-derivation crux
  (epic `qou-r2nh`, bean `qou-ylot`).

  Context.  The just-landed DT / 3d-index unification (`DeltaLambdaDTIndex.lean`,
  PR #4553) proved sorry-free that the per-partition binding factor `Δ_λ` is the
  Behrend-signed Donaldson–Thomas count of the Springer fibre `𝓑_λ`:

      Δ_λ  =  (-1)^{n(λ)} · dim V_λ  =  DT(𝓑_λ),

  with the a-function grade `n(λ)` the Behrend `(-1)^{dim moduli}` sign and the
  Wedderburn dimension `dim V_λ` the virtual count.  That file honestly flags the
  OPEN leg as a content-bearing primary conjecture `DeltaLambdaDTRealization`
  (no instance): does the QOU substrate *force* the DT moduli `𝓑_λ` — a space of
  complex dimension `n(λ)` whose Behrend-weighted count is `dim V_λ` — from the 13
  categorical drivers, so that `Δ_λ` is its DT invariant, rather than the
  `(n(λ), dim V_λ)` data being read off `Δ_λ` after the fact?

  This file attacks that crux from the substrate-derivation angle and lands a
  precise NEGATIVE bound on what the `Δ_λ = DT-count` *identification alone* can
  force — the exact sense in which the toy assignment merely READS the answer.
  We work with the realization predicate abstractly:

      `IsDTRealization md vc  :=  ∀ λ, (-1)^{md λ} · vc λ = Δ_λ`

  i.e. `(md, vc)` is a (moduli-dimension, virtual-count) assignment reproducing
  `Δ_λ` as a Behrend-signed DT count.  Two results:

  1. **The count is forced up to sign, the moduli DIMENSION is forced only mod 2.**
     Any realization with the substrate count `vc = dim V_λ` has its Behrend sign
     `(-1)^{md λ}` pinned to `(-1)^{n(λ)}` (`dt_moduliDim_sign_forced`) — but the
     *value* `md λ` is not pinned: `n(λ)` and `n(λ)+2` are BOTH valid realizations
     (`dt_moduliDim_underdetermined`).  So matching `Δ_λ` sees only the PARITY of
     the moduli dimension, never the Springer value `n(λ) = dim_ℂ 𝓑_λ` itself.

  This is the formalize-first crux answer: the `Δ_λ = DT-count` identity is a
  correct categorical HOME, but it constrains the moduli only to *parity + count*
  — it does NOT single out the Springer fibre `𝓑_λ` (dimension exactly `n(λ)`).
  The Springer *dimension* `n(λ)` must therefore enter from an INDEPENDENT
  substrate map — the a-function = Gröbner–Shirshov jet-order fake-degree
  valuation (`docs/coordination/option-e.md`, 2026-07-18) — not from the DT-count
  identification.  And the geometric moduli object itself (a variety with a
  Behrend function / symmetric obstruction theory) is not produced by the drivers
  at all; only its numerical shadow `(n(λ), dim V_λ)` is.  Hence the internal
  derivation remains OPEN, now precisely bounded (see the audit doc
  `docs/audits/2026-08-01-deltalambda-dt-substrate-derivation.md`).

  Discipline.  Nothing here is fitted; `Δ_λ`, AME, CODATA, `q₀` are never
  inverted; no instance of the open conjecture is fabricated.  This file proves a
  *limitative* fact (the target under-determines the moduli), which is the honest
  content — it does NOT close the open leg and does not launder it.  Base ring is
  ℤ throughout (the DT count is a signed integer; §7c — no archimedean construct).

  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
-/
import QOU.BraidsAndKnots.S5SO3FiberAction

namespace QOU.BraidsAndKnots

/-! ## The DT-realization predicate

    `(md, vc)` assigns to each block a moduli complex-dimension `md λ` and a
    Behrend-weighted virtual count `vc λ`; it *realizes* `Δ_λ` when the resulting
    Behrend-signed DT count `(-1)^{md λ}·vc λ` reproduces the corpus binding
    factor `deltaLambda` for every block.  The Springer/toy reading is
    `(md, vc) = (nStat, dim)`. -/
def IsDTRealization (md vc : PartitionOf5 → ℕ) : Prop :=
  ∀ p : PartitionOf5, (-1 : ℤ) ^ (md p) * (vc p : ℤ) = p.deltaLambda

/-- **The Springer/toy reading realizes `Δ_λ`.**  `md = n(λ)` (a-function =
    `dim_ℂ 𝓑_λ`), `vc = dim V_λ` (Wedderburn count) reproduces every `Δ_λ` — this
    is `deltaSign_eq_nStat_parity` repackaged as a DT realization. -/
theorem canonical_dt_realization :
    IsDTRealization PartitionOf5.nStat PartitionOf5.dim := by
  intro p; cases p <;> decide

/-- **The parity-shifted reading ALSO realizes `Δ_λ`.**  Bumping the moduli
    dimension by `2` leaves the Behrend sign `(-1)^{md}` unchanged, so
    `md = n(λ)+2` with the same count reproduces every `Δ_λ`.  This is the
    witness that the moduli dimension is not pinned by the `Δ_λ` target. -/
theorem shifted_dt_realization :
    IsDTRealization (fun p => PartitionOf5.nStat p + 2) PartitionOf5.dim := by
  intro p; cases p <;> decide

/-- **Count forced up to sign; sign forced.**  Any DT realization that uses the
    substrate count `vc = dim V_λ` has its Behrend sign `(-1)^{md λ}` pinned to
    `(-1)^{n(λ)}` — the target `Δ_λ` determines the parity of the moduli
    dimension exactly.  (The count itself is `dim V_λ` by the landed
    `binding_magnitude_eq_dim`; here we isolate the sign leg.) -/
theorem dt_moduliDim_sign_forced (md : PartitionOf5 → ℕ)
    (h : IsDTRealization md PartitionOf5.dim) (p : PartitionOf5) :
    (-1 : ℤ) ^ (md p) = (-1 : ℤ) ^ p.nStat := by
  have hd : (p.dim : ℤ) ≠ 0 := by
    have hp : 0 < p.dim := by cases p <;> decide
    exact_mod_cast hp.ne'
  have hb := h p
  rw [PartitionOf5.deltaLambda, PartitionOf5.deltaSign_eq_nStat_parity] at hb
  exact mul_right_cancel₀ hd hb

/-- **THE CRUX (limitative).**  The `Δ_λ = Behrend-signed DT-count` target
    UNDER-DETERMINES the moduli dimension: two DISTINCT moduli-dimension
    assignments — the Springer value `n(λ)` and `n(λ)+2` — both realize `Δ_λ`
    with the substrate count `dim V_λ`.  So matching `Δ_λ` constrains the moduli
    dimension only *mod 2* (its Behrend-sign parity), never the actual Springer
    value `n(λ) = dim_ℂ 𝓑_λ`.  The `Δ_λ = DT-count` identification therefore does
    NOT force the Springer fibre `𝓑_λ`; the dimension `n(λ)` must come from an
    independent substrate map (the a-function / GS jet-order valuation).  This is
    the precise sense in which the toy `moduliDim := nStat` merely READS the
    answer — the open internal derivation (`DeltaLambdaDTRealization`, bean
    `qou-ylot`) is not closed by the DT identity. -/
theorem dt_moduliDim_underdetermined :
    ∃ md₁ md₂ : PartitionOf5 → ℕ,
      IsDTRealization md₁ PartitionOf5.dim ∧
      IsDTRealization md₂ PartitionOf5.dim ∧
      (∀ p : PartitionOf5, md₁ p ≠ md₂ p) :=
  ⟨PartitionOf5.nStat, fun p => PartitionOf5.nStat p + 2,
    canonical_dt_realization, shifted_dt_realization,
    fun p => by show p.nStat ≠ p.nStat + 2; omega⟩


/-- **Arbitrary even-shift DT realization family (`qou-nmpr`).**
For every `k : ℕ`, shifting the Springer dimension by `2 * k` (`md p = p.nStat + 2 * k`)
preserves the Behrend sign `(-1)^{md p}` and therefore realizes `Δ_λ` on every `p : PartitionOf5`. -/
theorem even_shifted_dt_realization (k : ℕ) :
    IsDTRealization (fun p => PartitionOf5.nStat p + 2 * k) PartitionOf5.dim := by
  intro p
  have hpar : (-1 : ℤ) ^ (p.nStat + 2 * k) = (-1 : ℤ) ^ p.nStat := by
    rw [pow_add, pow_mul]
    norm_num
  rw [hpar]
  exact canonical_dt_realization p

end QOU.BraidsAndKnots
