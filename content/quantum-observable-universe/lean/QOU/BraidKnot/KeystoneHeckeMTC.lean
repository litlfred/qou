import QOU.BraidKnot.BWVacuumRowIsHecke
import QOU.BraidKnot.KeystoneModularTwist
import QOU.BraidKnot.KeystoneVerlindeSMatrixBridge

/-!
# QOU.BraidKnot.KeystoneHeckeMTC — the Hecke/Temperley–Lieb side as a concrete MTC (the target of "BW = Hecke")

This file **assembles** the Hecke blocks into a single explicit `HeckeMTC` bundle carrying the two
pieces of modular data a modular tensor category must have — the vacuum `S`-matrix row `S₀` and the
diagonal ribbon twist / modular `T`-matrix `θ` — together with the quantum dimension `qDim = d_q`, the
global dimension `D` (`D² = Σ d_q²`), a distinguished vacuum object of quantum dimension `1`, and the
transpose (bar / charge-conjugation) involution `conj`. It then **proves** exactly the modular-data
relations that are genuinely provable from the existing corpus, reusing the already-established lemmas
rather than re-deriving them:

* `S0_ratio_eq_qDim` — the vacuum-row ratio recovers the quantum dimension, `S₀(λ)/S₀(vac) = d_q(λ)`,
  routed through the corpus-proved `QOU.BraidKnot.VerlindeVacuumRow.S0_ratio`
  ([`BWVacuumRowIsHecke.lean`](BWVacuumRowIsHecke.lean)). This is the `S₀ = d_q/D` modular datum.
* `S0_conj` — the vacuum row is transpose-invariant (chirality-blind), `S₀(λ′) = S₀(λ)`, derived from
  the `qDim_conj` field (the corpus-proved `QOU.BraidKnot.IdentityI.qDim_conj`,
  [`KeystoneC2QDimTranspose.lean`](KeystoneC2QDimTranspose.lean), `d_q(λ′) = d_q(λ)`).
* `theta_conj_mul` — the twist's chirality law in product form, `θ(λ′)·θ(λ) = 1`, derived from the
  `theta_conj` field (the corpus-proved `QOU.BraidKnot.Keystone.theta_conjugate`
  ([`KeystoneModularTwist.lean`](KeystoneModularTwist.lean)), `θ_{λ′} = θ_λ⁻¹`).
* `verlindeMeasure_conj` — the Verlinde measure `μ(λ) = S₀(λ)²` is transpose-invariant.

The concrete Hecke instance `heckeMTC` discharges `qDim_conj` from `IdentityI.qDim_conj` and
`theta_conj` from `Keystone.theta_conjugate` (not carried abstractly), and reuses
`KeystoneVerlindeSMatrixBridge`'s positivity (`sum_qDimSq_pos`) for `D ≠ 0`. A non-vacuity `example`
(a genuine `HeckeMTC ℝ` over the block set `{[]}`) confirms the structure is inhabited, so the
theorems above are **not** conditional-on-`False`.

## Honest scope — this does NOT close `bwse`

**This file does NOT close `bwse` ("BW = Hecke").** It formalizes the *target* category — the
Hecke/Temperley–Lieb MTC — and proves the modular-data relations internal to it. The physics
identification, that the Beasley–Witten localization of `S³/2I` (the BW gauge datum) *is* this modular
tensor category — i.e. `bwS0 = d_q/D` for the actual path-integral output, **bean `bwhk`** — remains
**open** and owner-gated (the abstract gauge datum `bwS0` and the single open conjecture
`bwS0_eq_hecke` live in [`BWVacuumRowIsHecke.lean`](BWVacuumRowIsHecke.lean); narrow Subgoal-2 reversal
#2503/#2524, foreclosed on the SU(2)`_k` sub-route by `Su2SchurWeylForeclosure.lean`). Assembling this
`HeckeMTC` class is **not** a proof of that identification (AGENTS.md §"Axiomatization is NOT a Proof");
it is the concrete description of what the localization must be shown to produce.

**Base ring (§7c).** The bundle and every relation proved here are pure field algebra —
`{R : Type*} [Field R]`, no ordering, no `Real.sqrt`, no `q₀`. The single archimedean specialisation is
the concrete Hecke instance `heckeMTC : HeckeMTC ℝ`, where `D = √(Σ d_q²)` genuinely needs `ℝ` (exactly
as `heckeVerlindeData` does).

Refs:
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (`S`, `T` modular data).
- [beasleywitten2005] https://doi.org/10.4310/jdg/1143593746 — non-abelian CS localization.
-/

namespace QOU.BraidKnot.Keystone

open scoped BigOperators
open QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

/-- **The Hecke/Temperley–Lieb side as a concrete modular tensor category (the target of "BW = Hecke").**

Bundles both pieces of modular data on the Hecke partition blocks:

* the **vacuum `S`-matrix row** `S0 : Part → R` with the published modular-data identity
  `S₀(λ) = d_q(λ)/D` (`S0_eq`), and a distinguished vacuum object `vac` of quantum dimension `1`;
* the **ribbon twist / modular `T`-matrix** `theta : Part → R`, diagonal, with the chirality law
  `θ_{λ′} = θ_λ⁻¹` (`theta_conj`) and `θ_vac = 1`;

together with the quantum dimension `qDim = d_q` (transpose-invariant, `qDim_conj`), the global
dimension `D` (`D² = Σ d_q²`, `D_sq`; `D ≠ 0`, `D_ne`), and the transpose (bar) involution `conj`
closing the block set (`conj_mem`).

The fields `qDim_conj`, `theta_conj`, `S0_eq`, `D_sq` are the modular-data *inputs*; the file's theorems
*derive* the modular-data consequences from them. Constructing an instance whose `qDim` is the *Hecke*
`d_q` and whose `S0` is the *BW gauge datum* is the open physics content (`bwse` / bean `bwhk`), NOT
supplied by this class. -/
structure HeckeMTC (R : Type*) [Field R] where
  /-- Partition index for the Hecke block `λ ⊢ n`. -/
  Part : Type*
  /-- The finite set of Hecke partition blocks. -/
  parts : Finset Part
  /-- The transpose (bar / charge-conjugation) involution `λ ↦ λ′`. -/
  conj : Part → Part
  /-- The blocks are closed under transpose. -/
  conj_mem : ∀ p ∈ parts, conj p ∈ parts
  /-- The monoidal unit / vacuum object. -/
  vac : Part
  /-- The vacuum is one of the blocks. -/
  vac_mem : vac ∈ parts
  /-- The categorical quantum dimension `d_q(λ)` of the Hecke block. -/
  qDim : Part → R
  /-- The vacuum object has quantum dimension `1`. -/
  qDim_vac : qDim vac = 1
  /-- **Corpus-proved input** `d_q(λ′) = d_q(λ)` (`QOU.BraidKnot.IdentityI.qDim_conj`). -/
  qDim_conj : ∀ p ∈ parts, qDim (conj p) = qDim p
  /-- The ribbon twist / modular `T`-matrix eigenvalue `θ_λ` (diagonal modular datum). -/
  theta : Part → R
  /-- The twist is trivial on the vacuum: `θ_vac = 1`. -/
  theta_vac : theta vac = 1
  /-- **Corpus-proved input** — the twist's chirality law `θ_{λ′} = θ_λ⁻¹`
  (`QOU.BraidKnot.Keystone.theta_conjugate`). -/
  theta_conj : ∀ p ∈ parts, theta (conj p) = (theta p)⁻¹
  /-- The global quantum dimension `D` (total dimension of the modular category). -/
  D : R
  /-- `D ≠ 0`. -/
  D_ne : D ≠ 0
  /-- `D² = Σ_λ d_q(λ)²` — the defining global-dimension relation. -/
  D_sq : D ^ 2 = ∑ p ∈ parts, qDim p ^ 2
  /-- The **vacuum `S`-matrix row** `S₀(λ)`. -/
  S0 : Part → R
  /-- **Published modular-data identity** `S₀(λ) = d_q(λ)/D` (vacuum row of the `S`-matrix in any MTC). -/
  S0_eq : ∀ p ∈ parts, S0 p = qDim p / D

namespace HeckeMTC

variable {R : Type*} [Field R] (M : HeckeMTC R)

/-- **Reuse bridge** — the `HeckeMTC`'s vacuum-`S`-row data as a `VerlindeVacuumRow`
([`BWVacuumRowIsHecke.lean`](BWVacuumRowIsHecke.lean)): `d := qDim`, `D := D`, `vac := vac`. Lets the
corpus-proved `VerlindeVacuumRow.S0_ratio` / `S0_eq_smul` discharge the `S`-matrix relations without
re-deriving `S₀ = d_q/D`. -/
def toVerlindeVacuumRow : VerlindeVacuumRow M.Part R where
  d := M.qDim
  D := M.D
  vac := M.vac
  d_vac := M.qDim_vac
  D_ne := M.D_ne

/-- **The `S`-matrix vacuum-row modular datum (`S₀ = d_q/D`), via `VerlindeVacuumRow`.** The
vacuum-row ratio to the vacuum entry recovers the quantum dimension:
`S₀(λ) / S₀(vac) = d_q(λ)`. Proved by transporting the corpus-proved
`QOU.BraidKnot.VerlindeVacuumRow.S0_ratio` through the `S0_eq` identity `S₀ = d_q/D`. -/
theorem S0_ratio_eq_qDim (p : M.Part) (hp : p ∈ M.parts) :
    M.S0 p / M.S0 M.vac = M.qDim p := by
  have h := M.toVerlindeVacuumRow.S0_ratio p
  rw [M.S0_eq p hp, M.S0_eq M.vac M.vac_mem]
  simpa only [VerlindeVacuumRow.S0, toVerlindeVacuumRow] using h

/-- **The vacuum row as a `1/D`-rescaling of the quantum dimension**, `S₀(λ) = (1/D)·d_q(λ)`, via the
corpus-proved `VerlindeVacuumRow.S0_eq_smul` (no per-block freedom — the single normalisation `1/D`). -/
theorem S0_eq_smul (p : M.Part) (hp : p ∈ M.parts) :
    M.S0 p = (1 / M.D) * M.qDim p := by
  have h := M.toVerlindeVacuumRow.S0_eq_smul p
  rw [M.S0_eq p hp]
  simpa only [VerlindeVacuumRow.S0, toVerlindeVacuumRow] using h

/-- **The vacuum row is chirality-blind (transpose-invariant): `S₀(λ′) = S₀(λ)`.** Derived from the
`qDim_conj` field (the corpus-proved `d_q(λ′) = d_q(λ)`) via `S₀ = d_q/D` — the `S`-matrix's
`C₂`-analogue (invariant, complementing the twist's inverting `θ_{λ′} = θ_λ⁻¹`). -/
theorem S0_conj (p : M.Part) (hp : p ∈ M.parts) :
    M.S0 (M.conj p) = M.S0 p := by
  rw [M.S0_eq (M.conj p) (M.conj_mem p hp), M.S0_eq p hp, M.qDim_conj p hp]

/-- **The twist's chirality law in product form: `θ(λ′)·θ(λ) = 1`.** Derived from the `theta_conj`
field (`θ_{λ′} = θ_λ⁻¹`) and `θ(λ) ≠ 0`. The bar-involution pairs `V_λ` with its dual `V_{λ′}` so their
framing anomalies cancel — the modular `T`-matrix's charge-conjugation compatibility. -/
theorem theta_conj_mul (p : M.Part) (hp : p ∈ M.parts) (hθ : M.theta p ≠ 0) :
    M.theta (M.conj p) * M.theta p = 1 := by
  rw [M.theta_conj p hp]
  exact inv_mul_cancel₀ hθ

/-- **The Verlinde measure** `μ(λ) = S₀(λ)²` of the target MTC. -/
def verlindeMeasure (p : M.Part) : R := M.S0 p ^ 2

/-- **The Verlinde measure is transpose-invariant: `μ(λ′) = μ(λ)`.** Immediate from `S0_conj` — the
Plancherel weight is chirality-blind. -/
theorem verlindeMeasure_conj (p : M.Part) (hp : p ∈ M.parts) :
    M.verlindeMeasure (M.conj p) = M.verlindeMeasure p := by
  unfold verlindeMeasure
  rw [M.S0_conj p hp]

end HeckeMTC

/-! ## The concrete Hecke instance (reusing the corpus `qDim_conj` / `theta_conjugate` / positivity) -/

/-- **The Hecke q-dimensions + ribbon twist realize `HeckeMTC`** for `q > 1` on any conjugate-closed
set `P` of weakly-decreasing blocks containing the empty (vacuum) partition. `qDim := d_q`,
`theta := θ_λ = q^{c(λ)}`, `D := √(Σ d_q²)`, `S0 := d_q/D`, `vac := []`.

The two modular-data inputs are discharged from the **corpus proofs**, not carried abstractly:
`qDim_conj` from `QOU.BraidKnot.IdentityI.qDim_conj` and `theta_conj` from
`QOU.BraidKnot.Keystone.theta_conjugate`. `D ≠ 0` reuses `KeystoneVerlindeSMatrixBridge.sum_qDimSq_pos`
(positivity, `q > 1`). `S0_eq` is `rfl`.

The **only** thing this does *not* establish is the physics — that the BW localization of `S³/2I`
actually *is* this category (`bwse` / bean `bwhk`); that owner-gated identification is the open
residual. -/
noncomputable def heckeMTC
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hnil : [] ∈ P) :
    HeckeMTC ℝ where
  Part := List ℕ
  parts := P
  conj := Partition.conjugate
  conj_mem := hconj
  vac := []
  vac_mem := hnil
  qDim := qDim q
  qDim_vac := by simp
  qDim_conj := fun p hp => qDim_conj q p (hsorted p hp)
  theta := Keystone.theta q
  theta_vac := theta_nil q
  theta_conj := fun p hp => theta_conjugate q p (hsorted p hp)
  D := Real.sqrt (∑ m ∈ P, qDim q m ^ 2)
  D_ne := ne_of_gt (Real.sqrt_pos.mpr (sum_qDimSq_pos hq ⟨[], hnil⟩))
  D_sq := Real.sq_sqrt (le_of_lt (sum_qDimSq_pos hq ⟨[], hnil⟩))
  S0 := fun p => qDim q p / Real.sqrt (∑ m ∈ P, qDim q m ^ 2)
  S0_eq := fun _ _ => rfl

/-- `Partition.conjugate [] = []` — the empty diagram is self-conjugate (no columns). -/
theorem conjugate_nil : Partition.conjugate [] = [] := rfl

/-- **Non-vacuity — `HeckeMTC ℝ` is inhabited** (the rank-1 target MTC on the single vacuum block
`{[]}`, at `q = 3/2`), so `HeckeMTC` and every theorem in `namespace HeckeMTC` above are **not**
conditional-on-`False`. The genuinely open content is the *physical* instance where `S0` is the BW
localization gauge datum (`bwse` / bean `bwhk`), not the Hecke `d_q/D` assembled here. -/
noncomputable example : HeckeMTC ℝ :=
  heckeMTC (3 / 2) (by norm_num) {[]}
    (fun l hl => by rw [Finset.mem_singleton] at hl; subst hl; exact List.sorted_nil)
    (fun l hl => by
      rw [Finset.mem_singleton] at hl; subst hl
      rw [Finset.mem_singleton, conjugate_nil])
    (Finset.mem_singleton.mpr rfl)

end QOU.BraidKnot.Keystone
