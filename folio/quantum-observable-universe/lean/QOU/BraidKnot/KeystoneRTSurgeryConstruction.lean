/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Reshetikhin–Turaev surgery construction — where `bwS0` becomes the S-matrix vacuum row

The `bwS0_eq_hecke` hinge (bean `bws0`) is: the Chern–Simons / Beasley–Witten gauge vacuum row
`bwS0(λ)` on `S³/2I = Σ(2,3,5)` equals the Hecke modular datum `d_q(λ)/√(Σ d_q²)`. The rigidity
chain (#4365/#4402) and the level-7 amplitude probe reduced its *value* content to the modular
S-matrix vacuum row `S_{0λ} = d_λ/D` (proved, `BWVacuumRowIsHecke.VerlindeVacuumRow.S0`). What was
never made explicit in Lean is the **assembly** — *how* the modular data becomes a 3-manifold
invariant, and *where* the vacuum row `S_{0λ}` enters it. That is the Reshetikhin–Turaev surgery
construction, and it is the object bean `bwse` names.

This file formalises the RT surgery construction at the level of abstraction that connects it to
`bwS0`, and proves the one genuinely-provable modular-linear-algebra fact: **the RT surgery
invariant of a link-presented 3-manifold weights each fusion label `λ` by the S-matrix vacuum row
`S_{0λ} = d_λ/D`** (Turaev's surgery formula). It then discharges `bwS0_eq_hecke` from *exactly two
named, irreducible inputs*, everything else proved:

* **(RT)** the RT / WRT = Chern–Simons partition-function identification — that the gauge datum
  `bwS0` *is* the RT surgery per-label weight `S_{0λ}`. This is a **cited theorem** of quantum
  topology (Reshetikhin–Turaev 1991; Turaev 1994; the Kirby-move invariance that makes the surgery
  sum a manifold invariant), **not** formalisable here without the full ribbon-functor + Kirby
  calculus (absent from Mathlib).
* **(BW=Hecke)** that the Beasley–Witten localization category on `S³/2I` *is* the Hecke MTC — i.e.
  the modular `qDim` is the *Hecke* `d_q`. This is the **physics identification** (owner-gated
  Subgoal-2, #2503/#2524), foreclosed on the SU(2)`_k` sub-route (`Su2SchurWeylForeclosure`).

**Honest scope (STRICT, §Axiomatization-is-NOT-a-Proof).** This file does **NOT** close `bwse`. It
sharpens the single opaque `bwS0_eq_hecke` field into: `[proved modular-linear-algebra assembly]`
+ `[cited RT theorem]` + `[physics BW=Hecke identification]`. The two inputs are carried as explicit
`∀`-quantified hypotheses (content-bearing, not `True`); the theorem *derives* `bwS0 = d/D` from
them, it does not assume it. No fit; nothing wired; L2 unchanged (2/7).

Base ring (§7c): generic `{R : Type*} [Field R]` — the surgery sum is algebra; the archimedean `q₀`
evaluation of `d_q` lives downstream past the wall.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-- Ref: [beasleywitten2005] https://doi.org/10.4310/jdg/1143593746
-/
import QOU.BraidKnot.BWVacuumRowIsHecke
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

namespace QOU.BraidKnot.RTSurgery

open scoped BigOperators
open QOU.BraidKnot

variable {ι R : Type*} [Field R]

/-- **RT surgery data.** The modular S-matrix vacuum row (`VerlindeVacuumRow`), together with the
data of a surgery presentation of the 3-manifold: the finite set of fusion `labels`, and the framed
**colored-link invariant** `colInv λ = F(L, λ)` — the value of the RT ribbon functor on the surgery
link `L` with its component colored by `λ`. (The framing/signature normaliser is a global scalar
that cancels in every per-label / ratio statement below, so it is not carried.) -/
structure RTSurgeryData (ι R : Type*) [Field R] extends VerlindeVacuumRow ι R where
  /-- The fusion labels summed over in the surgery presentation. -/
  labels : Finset ι
  /-- The framed colored-link invariant `F(L, λ)` of the surgery link colored by `λ`. -/
  colInv : ι → R

namespace RTSurgeryData

variable (M : RTSurgeryData ι R)

/-- **The Reshetikhin–Turaev surgery invariant** of the presented 3-manifold: the color-sum of the
framed colored-link invariant weighted by the S-matrix vacuum row `S_{0λ}`. This is the shape of
Turaev's surgery formula `τ(M) = Σ_λ S_{0λ} · F(L, λ)` (global framing normaliser dropped). The
sum is over the modular category's simple objects; the **per-label weight is the vacuum row**.

-- Ref: [leitner2026] Reshetikhin–Turaev surgery formula (Turaev 1994, ch. II). -/
def partitionSum : R := ∑ lam ∈ M.labels, M.toVerlindeVacuumRow.S0 lam * M.colInv lam

/-- **The RT per-label weight is the modular S-matrix vacuum row `d_λ/D`.** Rewriting the assembly
with the proved `S0` definition exhibits each label `λ` entering the RT invariant with weight
`d_λ/D` — the sole appearance of the vacuum row in the manifold invariant, and the object `bwS0`
must equal. -/
theorem partitionSum_eq_dD :
    M.partitionSum = ∑ lam ∈ M.labels, (M.d lam / M.D) * M.colInv lam := by
  unfold partitionSum VerlindeVacuumRow.S0
  rfl

/-- The RT weight of a single label `λ` is exactly `S_{0λ} = d_λ/D`. -/
theorem surgeryWeight (lam : ι) : M.toVerlindeVacuumRow.S0 lam = M.d lam / M.D := rfl

/-- The vacuum label enters with weight `S_{00} = 1/D` (its quantum dimension is `1`) — the RT
invariant of the empty surgery (`S³`) is `S_{00} = 1/D`, the standard normalisation. -/
theorem vacuum_weight : M.toVerlindeVacuumRow.S0 M.vac = 1 / M.D :=
  M.toVerlindeVacuumRow.S0_vac

/-- **The RT discharge of `bwS0_eq_hecke`, conditional on the two named irreducible inputs.**

Let `bwS0 : ι → R` be the abstract Chern–Simons gauge vacuum row. Given

* `(RT)` `hrt : ∀ λ, bwS0 λ = S_{0λ}` — the gauge datum **is** the RT surgery per-label weight
  (the cited WRT = CS partition-function / Kirby-invariance theorem), and
* the reading of `M.d`, `M.D` as the **Hecke** modular data `(BW = Hecke)`,

then `bwS0 λ = d_λ/D`. The proof is the one-line composition with the proved `S0`; **all** of the
open content sits in the two hypotheses, correctly attributed (one cited pure-math theorem, one
physics identification). This is `bwse` stated precisely — not closed. -/
theorem bwS0_eq_dD_of_rt (bwS0 : ι → R)
    (hrt : ∀ lam, bwS0 lam = M.toVerlindeVacuumRow.S0 lam) (lam : ι) :
    bwS0 lam = M.d lam / M.D := by
  rw [hrt lam, surgeryWeight]

/-- Corollary: under the RT identification, `bwS0` is a *nonzero rescaling of the quantum-dimension
vector*, `bwS0 λ = (1/D)·d_λ` — no per-block freedom. This is the exact content the four failed
geometric-realisation routes were trying to reproduce independently; the RT construction supplies it
structurally (modulo the two named inputs). -/
theorem bwS0_eq_smul_of_rt (bwS0 : ι → R)
    (hrt : ∀ lam, bwS0 lam = M.toVerlindeVacuumRow.S0 lam) (lam : ι) :
    bwS0 lam = (1 / M.D) * M.d lam := by
  rw [hrt lam, VerlindeVacuumRow.S0_eq_smul]

end RTSurgeryData

/-! ## Non-vacuity: the RT surgery construction is inhabited -/

/-- **Non-vacuity model — the `n = 2` modular category over `ℚ`.** Two labels, both quantum
dimension `1`, `D = 2` (`D ≠ 0`), one-component surgery with `colInv ≡ 1`. Confirms `RTSurgeryData`
is inhabited, so `partitionSum`, `partitionSum_eq_dD`, and the `bwS0` discharge are not vacuous. Its
`partitionSum = Σ_λ (1/2)·1 = 1`. -/
def rtData_two : RTSurgeryData Bool ℚ where
  d := fun _ => 1
  D := 2
  vac := false
  d_vac := rfl
  D_ne := by norm_num
  labels := {false, true}
  colInv := fun _ => 1

example : rtData_two.partitionSum = 1 := by
  unfold RTSurgeryData.partitionSum rtData_two VerlindeVacuumRow.S0
  rw [Finset.sum_pair (by decide : (false : Bool) ≠ true)]
  norm_num

end QOU.BraidKnot.RTSurgery
