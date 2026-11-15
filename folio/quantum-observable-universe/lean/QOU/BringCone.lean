import Mathlib.Algebra.Quaternion
import Mathlib.Tactic.Ring

/-!
# Tetraplectic geometry of the Bring cone — the Reeb quaternionic twist

The affine cone of Bring's curve is a real 4-manifold; its 3-dimensional link
carries a 3-Sasakian (degenerate quaternionic-contact) structure whose Reeb
triad is modelled here on the quaternion algebra `Quaternion R`.

We take the three Reeb operators to be **right-multiplication** by the
imaginary units `i, j, k`.  Right-multiplication is used (rather than left) so
that the operators generate the correct `𝔰𝔲(2)` bracket with a `+2` structure
constant:

`[M_i, M_j] p = (p·i)·j − (p·j)·i = p·(ij) − p·(ji) = p·k − p·(−k) = 2·(p·k)`.

The three `reeb_twist_*` lemmas below discharge exactly this bracket
(`[M_i,M_j] = 2·M_k` and cyclic).  These are **pure quaternion-algebra
identities** — no ordering, radical, or other archimedean construct is used —
so per the §7c base-ring convention they are stated over a generic
`{R : Type*} [CommRing R]`, with `BringCone` naming the geometric object.  The
archimedean specialization `Quaternion ℝ` for the actual quaternionic-contact
geometry is left to the consumer; nothing here forces `Mathlib.Data.Real.Basic`
into the dependency cone.

Reference for the geometric interpretation (Reeb quaternionic twist on the
quaternionic-contact link): [leitner2026] `lem:bring-cone-reeb-quaternionic-twist`
(brings-surface §Spectral resolvents and gauge structures), with the SU(2)
reading and its scope limits in `rem:tetraplectic-su2-gauge-reading`.
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- The tetraplectic Bring cone, modelled on the quaternions over `R`. -/
abbrev BringCone (R : Type*) [CommRing R] := Quaternion R

/-- Reeb operator `M_i` — right-multiplication by the quaternionic unit `i`. -/
def reebM_i (p : BringCone R) : BringCone R := p * ⟨0, 1, 0, 0⟩
/-- Reeb operator `M_j` — right-multiplication by the quaternionic unit `j`. -/
def reebM_j (p : BringCone R) : BringCone R := p * ⟨0, 0, 1, 0⟩
/-- Reeb operator `M_k` — right-multiplication by the quaternionic unit `k`. -/
def reebM_k (p : BringCone R) : BringCone R := p * ⟨0, 0, 0, 1⟩

/-- Quaternionic twist `[M_i, M_j] = 2·M_k`. -/
theorem reeb_twist_ij (p : BringCone R) :
    reebM_j (reebM_i p) - reebM_i (reebM_j p) = (2 : R) • reebM_k p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_j, M_k] = 2·M_i`. -/
theorem reeb_twist_jk (p : BringCone R) :
    reebM_k (reebM_j p) - reebM_j (reebM_k p) = (2 : R) • reebM_i p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_k, M_i] = 2·M_j`. -/
theorem reeb_twist_ki (p : BringCone R) :
    reebM_i (reebM_k p) - reebM_k (reebM_i p) = (2 : R) • reebM_j p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-! ## The square of a Reeb operator is negation — a candidate for `ι`

Bean `qou-wqto`. `brings-surface/archimedean-chirality.md` states that chirality
sits in the ±-eigenspaces of **the Reeb involution `ξ ↦ −ξ`**, and
`QOU/StandardModel/ChiralityGradingConstruction.lean` (V10) proves that a
globally `ι`-odd grading exists **iff `ι` is fixed-point free**
(`free_of_reeb_odd_grading`). What the corpus does not state is any concrete
involution to put there — V10 parameterises over `reeb : State → State` and
nothing instantiates it.

The operators above supply one, as algebra. Right-multiplication by a
quaternionic unit has order four, and its **square is negation** — literally the
`ξ ↦ −ξ` of the content block:

    reebM_i (reebM_i p) = p * i * i = p * (-1) = -p

Negation is an involution, and its fixed points are exactly the solutions of
`2p = 0`: on a `BringCone R` where `2` is not a zero divisor that is the origin
alone, so **negation is fixed-point free on the punctured cone** — precisely
V10's hypothesis.

🛑 **This is a CANDIDATE, not a derivation, and the gap is named.** Proved below
is the *algebra*: that the square of each Reeb operator is negation, that
negation is involutive, and exactly when it is free. **Not** proved, and not
proved anywhere in the corpus: that the Bring cone is the physical state space,
or that the involution the Reeb field induces on physical states is this
negation. That identification is the CR-geometry step
`archimedean-chirality.md` asserts in one paragraph and nothing derives; the
whole V10/V11 tower remains conditional on it. Nothing here is wired and no
observable is predicted.
-/

/-- **`M_i² = −id`.**  Right-multiplication by `i` twice is negation, since
`i² = −1`. -/
theorem reebM_i_sq (p : BringCone R) : reebM_i (reebM_i p) = -p := by
  dsimp [reebM_i]
  ext <;> simp

/-- **`M_j² = −id`.** -/
theorem reebM_j_sq (p : BringCone R) : reebM_j (reebM_j p) = -p := by
  dsimp [reebM_j]
  ext <;> simp

/-- **`M_k² = −id`.** -/
theorem reebM_k_sq (p : BringCone R) : reebM_k (reebM_k p) = -p := by
  dsimp [reebM_k]
  ext <;> simp

/-- Each Reeb operator has **order four**, not two: its square is negation and
its fourth power is the identity. So `M_i` itself is not the involution — its
square is. -/
theorem reebM_i_quartic (p : BringCone R) :
    reebM_i (reebM_i (reebM_i (reebM_i p))) = p := by
  rw [reebM_i_sq, reebM_i_sq, neg_neg]

/-- **Negation on the cone is an involution** — the `ξ ↦ −ξ` of
`archimedean-chirality`, as a map on the cone. -/
theorem neg_involutive_cone (p : BringCone R) : -(-p) = p := neg_neg p

/-- **A fixed point of negation is exactly a solution of `p + p = 0`.**  Stated
as an iff so the next lemma's hypothesis is visibly the only thing needed. -/
theorem neg_fixed_iff_add_self_eq_zero (p : BringCone R) :
    -p = p ↔ p + p = 0 := neg_eq_iff_add_eq_zero

/-- **Negation is fixed-point free away from the origin**, whenever `2` is
cancellable on the cone — which is exactly V10's `free_of_reeb_odd_grading`
hypothesis, so a globally odd chirality grading exists on the punctured cone.

The hypothesis is an explicit cancellation property rather than a typeclass, so
the lemma stays over generic `[CommRing R]` per §7c. It holds in any `R` of
characteristic `≠ 2` without zero divisors, and in particular in `ℝ` for the
archimedean specialisation. -/
theorem neg_free_of_ne_zero {p : BringCone R}
    (h2 : ∀ x : BringCone R, x + x = 0 → x = 0) (hp : p ≠ 0) : -p ≠ p :=
  fun h => hp (h2 p ((neg_fixed_iff_add_self_eq_zero p).mp h))

/-! ## Negation cannot be `ι` on states; a Reeb operator can — via a chirality grading

Bean `qou-wqto`, owner request 2026-10-12 on PR #7712 ("1 2").

**Why the section above does not finish the job.** V10 needs `ι` to be fixed-point
free on **states**. A state is a ray: `p` and `c • p` for a unit `c` are the same
state. Negation is `(-1) • p` (`neg_eq_unit_smul`), so on rays it is the
identity, and it fixes **every** state. `neg_free_of_ne_zero` is a statement about
vectors and does not survive the passage to states.

**What does.** Combine the right Reeb operator `M_i` with the commuting **left**
multiplication by `i`. Then `Γ p := i · p · i` is a **grading**:
- `Γ² = id` (`chiralGamma_sq`);
- `Γ` acts as `−1` on `span(1, i)` and `+1` on `span(j, k)` (`chiralGamma_apply`);
- `M_i` commutes with `Γ` (`chiralGamma_comm_reebM_i`);
- **`M_j` anticommutes with `Γ`** (`chiralGamma_anticomm_reebM_j`), so it carries
  each `Γ`-eigenspace onto the other.

On rays `M_j` is an involution, because `M_j² = −id = (−1) •` is trivial
projectively. It is also fixed-point free on rays whenever `−1` is not a square in
`R` and `R`-scalars cancel on the cone (`reebM_j_ray_free`). That is V10's shape,
`ι` free and `chir` odd, on states, with `chir` = the eigenvalue of `Γ` and
`ι` = the Reeb operator `M_j` itself, not its square.

🛑 **Still a candidate, and the gaps are named.**
1. `L_i`, left multiplication, is introduced here as the second complex structure.
   Nothing in the corpus attaches it to the Reeb field.
2. `BringCone` is the quaternionic (Hopf) model, not Bring's own cone (bean
   `qou-rydq`, `QOU/Brings/BringConeLinkEulerNumber.lean`).
3. No map from V10's eight `Gen1Quark` labels into these rays exists.

For comparison, the literature: Krasnov's one generation `S₊ = 𝕆 ⊗ 𝕆̃`
(`library/arxiv-2104.01786v1`) carries two commuting complex structures, and they
carry two **different** chiralities:
- **Lorentz handedness** is the `±i` split of `J̃` on the split octonions `𝕆̃`
  (§3.4: `y⁺`, `y⁻` are spinors of opposite chirality, `y⁻ = (y⁺)*`).
- **The weak `L`/`R` split**, `SU(2)_L` vs `SU(2)_R` doublets, which is what
  `u_L` vs `u_R` means for `qou-wqto`, is the `±i` split of `J = E⁴` on the
  ordinary octonions `𝕆` (§6.1: the `(1,0)` part `L ⊕ Q` is `(2,1)` and the
  `(0,1)` part `L̄ ⊕ Q̄` is `(1,2)`). The map between them is complex conjugation
  relative to `J`, which is antilinear.
So in that model `u_L` vs `u_R` lives on `𝕆`, the same octonions that carry colour
(`QOU/MathlibExt/OctonionComplexStructure.lean`, `Le_sq_eq_neg_id`), and it is
cut out by a complex structure plus conjugation, not by a real grading. The `ℍ`
construction here is the quaternionic analogue of that shape, not that theorem.
Nothing is wired.
-/

/-- Left multiplication by `i` — the second complex structure, commuting with every
right multiplication (associativity). -/
def leftI (p : BringCone R) : BringCone R := ⟨0, 1, 0, 0⟩ * p

/-- The chirality grading `Γ = L_i ∘ M_i`, i.e. `p ↦ i · p · i`. -/
def chiralGamma (p : BringCone R) : BringCone R := leftI (reebM_i p)

/-- **`Γ` explicitly:** `−1` on the `1, i` components, `+1` on the `j, k` components. -/
theorem chiralGamma_apply (a b c d : R) :
    chiralGamma (⟨a, b, c, d⟩ : BringCone R) = ⟨-a, -b, c, d⟩ := by
  dsimp [chiralGamma, leftI, reebM_i]
  ext <;> simp

/-- **`Γ² = id`** — a grading, not a complex structure. -/
theorem chiralGamma_sq (p : BringCone R) : chiralGamma (chiralGamma p) = p := by
  dsimp [chiralGamma, leftI, reebM_i]
  ext <;> simp

/-- `M_i` commutes with the grading. -/
theorem chiralGamma_comm_reebM_i (p : BringCone R) :
    chiralGamma (reebM_i p) = reebM_i (chiralGamma p) := by
  dsimp [chiralGamma, leftI, reebM_i]
  ext <;> simp

/-- **`M_j` anticommutes with the grading**: it exchanges the two chiralities. -/
theorem chiralGamma_anticomm_reebM_j (p : BringCone R) :
    chiralGamma (reebM_j p) = -reebM_j (chiralGamma p) := by
  dsimp [chiralGamma, leftI, reebM_i, reebM_j]
  ext <;> simp

/-- `M_j` sends a `Γ = −1` vector to a `Γ = +1` vector. -/
theorem reebM_j_flips_eigen {p : BringCone R} (hp : chiralGamma p = -p) :
    chiralGamma (reebM_j p) = reebM_j p := by
  rw [chiralGamma_anticomm_reebM_j, hp]
  dsimp [reebM_j]
  ext <;> simp

/-- **Negation is a scalar**, `−p = (−1) • p`, so on rays (states) it is trivial
and fixes every state. This retires `reebM_x² = −id` as the candidate `ι` on
states. -/
theorem neg_eq_unit_smul (p : BringCone R) : -p = (-1 : R) • p := by
  ext <;> simp

/-- **`M_j` has no eigen-ray**: if `p * j = c • p` with `p ≠ 0`, then `c² + 1 = 0`.
So whenever `−1` is not a square in `R` and scalars cancel on the cone, `M_j`
fixes no state, and it is a fixed-point-free involution on rays (its square is
the scalar `−1`). -/
theorem reebM_j_ray_free {p : BringCone R} {c : R}
    (hcancel : ∀ (a : R) (x : BringCone R), a • x = 0 → x ≠ 0 → a = 0)
    (hp : p ≠ 0) (h : reebM_j p = c • p) : c * c + 1 = 0 := by
  have h2 : reebM_j (reebM_j p) = (c * c) • p := by
    rw [h]
    have : reebM_j (c • p) = c • reebM_j p := by
      dsimp [reebM_j]; ext <;> simp
    rw [this, h, smul_smul]
  rw [reebM_j_sq] at h2
  apply hcancel _ p _ hp
  rw [add_smul, one_smul, ← h2, neg_add_cancel]

/-! ## The second complex structure is forced into the commutant of the Reeb triad

Bean `qou-wqto`, issue #7774. The grading `Γ = L_i ∘ M_i` above uses a **left**
multiplication, and gap 1 of the previous section was that nothing attaches it to
the Reeb field. This section attaches it, in the strongest form available on this
model.

- Left multiplications commute with every Reeb operator (`leftMul_comm_reebM_*`,
  which is associativity).
- **Conversely**, an `R`-linear map that commutes with all three Reeb operators is
  left multiplication by `f 1` (`commutes_reeb_triad_iff_leftMul`).

So the operators commuting with the Reeb triad are **exactly** the left
multiplications. Any second complex structure that commutes with the Reeb field,
which is what "commuting complex structures" means in the `Γ = J·J′` construction,
has to be `L_u` for some `u`. The freedom left over is the choice of `u`, not the
kind of map.

🛑 Still a candidate. `BringCone` is the Hopf model, not Bring's own cone
(`qou-rydq`), and no map from V10's `Gen1Quark` labels into these rays exists.
-/

/-- Left multiplication by `u`. -/
def leftMul (u p : BringCone R) : BringCone R := u * p

theorem leftMul_comm_reebM_i (u p : BringCone R) :
    leftMul u (reebM_i p) = reebM_i (leftMul u p) := by
  simp [leftMul, reebM_i, mul_assoc]

theorem leftMul_comm_reebM_j (u p : BringCone R) :
    leftMul u (reebM_j p) = reebM_j (leftMul u p) := by
  simp [leftMul, reebM_j, mul_assoc]

theorem leftMul_comm_reebM_k (u p : BringCone R) :
    leftMul u (reebM_k p) = reebM_k (leftMul u p) := by
  simp [leftMul, reebM_k, mul_assoc]

/-- `leftI` is the left multiplication by `i`. -/
theorem leftI_eq_leftMul (p : BringCone R) : leftI p = leftMul ⟨0, 1, 0, 0⟩ p := rfl

/-- **The commutant of the Reeb triad is the left multiplications.** An `R`-linear
map commuting with `M_i`, `M_j`, `M_k` is left multiplication by `f 1`. -/
theorem commutes_reeb_triad_iff_leftMul (f : BringCone R →ₗ[R] BringCone R)
    (hi : ∀ p, f (reebM_i p) = reebM_i (f p))
    (hj : ∀ p, f (reebM_j p) = reebM_j (f p))
    (hk : ∀ p, f (reebM_k p) = reebM_k (f p)) (p : BringCone R) :
    f p = leftMul (f 1) p := by
  have hp : p = p.re • (1 : BringCone R) + p.imI • reebM_i 1
      + p.imJ • reebM_j 1 + p.imK • reebM_k 1 := by
    dsimp [reebM_i, reebM_j, reebM_k]
    ext <;> simp
  have e : f p = p.re • f 1 + p.imI • reebM_i (f 1)
      + p.imJ • reebM_j (f 1) + p.imK • reebM_k (f 1) := by
    conv_lhs => rw [hp]
    simp only [map_add, map_smul, hi, hj, hk]
  rw [e]
  dsimp [leftMul, reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-! ## Which unit `u`: what the structure forces, and what it leaves free

Bean `qou-wqto`. The previous section forces the second complex structure to be a
left multiplication `L_u`; it does not fix `u`. This section asks which structure
on the model cone could fix it, and proves the answer: **only the shape of `u`
is forced, not `u` itself.**

1. **Forced: `u` is a pure unit.** `L_u` is a complex structure iff `u * u = −1`
   (`leftMul_complex_iff`). For pure `u` that is `normSq u = 1`
   (`sq_eq_neg_one_iff_normSq_of_pure`), and over a domain of characteristic `≠ 2`
   in which `−1` is not a square (so in `ℝ`) every solution is pure
   (`re_eq_zero_of_sq_eq_neg_one`). Over `ℂ` the scalar `√−1` also solves it; that
   case is excluded by the hypothesis, not hidden.
2. **Not forced by the Reeb triad.** For every `u`, `Γ_u := L_u ∘ M_i` commutes
   with `M_i` and anticommutes with `M_j`, `M_k` (`chiralGammaU_comm_reebM_i`,
   `chiralGammaU_anticomm_reebM_j`, `chiralGammaU_anticomm_reebM_k`), and it is a
   grading for every complex-structure `u` (`chiralGammaU_sq`). No compatibility
   condition with the Reeb operators distinguishes one `u` from another.
3. **All choices are equivalent up to the commutant and one sign.** For square
   roots `u`, `v` of `−1`, left multiplication by `q = 1 − v·u` commutes with the
   Reeb triad and carries `Γ_u` to `Γ_v` (`intertwiner_mul`,
   `leftMul_intertwines_chiralGammaU`), and `L_{q̄} ∘ L_q = normSq q • id`
   (`leftMul_star_leftMul`) with `normSq q = 2·(1 + u·v)` for pure units
   (`normSq_intertwiner`), so `L_q` is invertible whenever `2·(1 + u·v)` is a
   unit. The antipodal pair `v = −u` is the global flip: `Γ_{−u} = −Γ_u`
   (`chiralGammaU_neg`), which exchanges the two chirality labels, matching V10's
   `reeb_odd_grading_unique_up_to_flip`.
4. **What does pick `u` is a base point, i.e. a choice.** Asking a given unit
   vector `p` (a radial direction) to be a `Γ_u = −1` eigenvector forces
   `u = p·i·p̄` (`chiralGammaU_eigen_iff`), the Hopf image of `p`, which is pure
   and has norm `normSq p ^ 2` (`re_hopf`, `normSq_hopf`). So `u` ranges over the
   Hopf base `S²`, and fixing it is fixing a point there. Nothing in the corpus
   selects such a point.

So on this model the residual freedom is exactly one point of the sphere of pure
unit quaternions, up to automorphisms commuting with the Reeb triad, plus the
global orientation sign `u ↦ −u`. That freedom is a gap for the owner, not a
choice made here.
-/

/-- The quaternionic unit `i` on the cone, named so that proofs can manipulate it. -/
def unitI : BringCone R := ⟨0, 1, 0, 0⟩

theorem unitI_mul_unitI : (unitI : BringCone R) * unitI = -1 := by
  ext <;> simp [unitI]

theorem unitI_mul_neg_unitI : (unitI : BringCone R) * -unitI = 1 := by
  ext <;> simp [unitI]

theorem reebM_i_eq_mul_unitI (p : BringCone R) : reebM_i p = p * unitI := rfl

/-- The chirality grading built from an arbitrary left unit: `Γ_u = L_u ∘ M_i`,
`p ↦ u · p · i`. -/
def chiralGammaU (u p : BringCone R) : BringCone R := leftMul u (reebM_i p)

/-- `Γ_i` is the grading `chiralGamma` of the earlier section. -/
theorem chiralGammaU_i (p : BringCone R) :
    chiralGammaU unitI p = chiralGamma p := rfl

/-- **`L_u` is a complex structure iff `u * u = −1`.** -/
theorem leftMul_complex_iff (u : BringCone R) :
    (∀ p, leftMul u (leftMul u p) = -p) ↔ u * u = -1 := by
  constructor
  · intro h
    have := h 1
    simpa [leftMul] using this
  · intro h p
    simp [leftMul, ← mul_assoc, h]

/-- For a pure `u`, `u * u = −1` iff `normSq u = 1`. -/
theorem sq_eq_neg_one_iff_normSq_of_pure (u : BringCone R) (hre : u.re = 0) :
    u * u = -1 ↔ Quaternion.normSq u = 1 := by
  have hsq : u * u = ⟨-(u.imI * u.imI + u.imJ * u.imJ + u.imK * u.imK), 0, 0, 0⟩ := by
    ext <;> simp [hre] <;> ring
  rw [hsq, Quaternion.normSq_def']
  constructor
  · intro h
    have := congrArg (fun x : BringCone R => x.re) h
    simp at this
    rw [hre]
    linear_combination -this
  · intro h
    rw [hre] at h
    ext <;> simp
    linear_combination -h

/-- **Every square root of `−1` is pure**, over a domain of characteristic `≠ 2` in
which `−1` is not a square. -/
theorem re_eq_zero_of_sq_eq_neg_one [IsDomain R] (h2 : (2 : R) ≠ 0)
    (hns : ∀ x : R, x * x ≠ -1) {u : BringCone R} (h : u * u = -1) : u.re = 0 := by
  by_contra ha
  have hI := congrArg (fun x : BringCone R => x.imI) h
  have hJ := congrArg (fun x : BringCone R => x.imJ) h
  have hK := congrArg (fun x : BringCone R => x.imK) h
  have hR := congrArg (fun x : BringCone R => x.re) h
  simp at hI hJ hK hR
  have h2a : (2 : R) * u.re ≠ 0 := mul_ne_zero h2 ha
  have hb : u.imI = 0 := by
    have : (2 * u.re) * u.imI = 0 := by linear_combination hI
    exact (mul_eq_zero.mp this).resolve_left h2a
  have hc : u.imJ = 0 := by
    have : (2 * u.re) * u.imJ = 0 := by linear_combination hJ
    exact (mul_eq_zero.mp this).resolve_left h2a
  have hd : u.imK = 0 := by
    have : (2 * u.re) * u.imK = 0 := by linear_combination hK
    exact (mul_eq_zero.mp this).resolve_left h2a
  apply hns u.re
  rw [hb, hc, hd] at hR
  linear_combination hR

/-- `Γ_u` is a grading for every complex-structure `u`. -/
theorem chiralGammaU_sq {u : BringCone R} (hu : u * u = -1) (p : BringCone R) :
    chiralGammaU u (chiralGammaU u p) = p := by
  simp only [chiralGammaU, leftMul, reebM_i_eq_mul_unitI]
  calc u * (u * (p * unitI) * unitI) = (u * u) * p * (unitI * unitI) := by
        simp only [mul_assoc]
    _ = p := by rw [hu, unitI_mul_unitI]; simp

/-- `M_i` commutes with `Γ_u`, for every `u`. -/
theorem chiralGammaU_comm_reebM_i (u p : BringCone R) :
    chiralGammaU u (reebM_i p) = reebM_i (chiralGammaU u p) := by
  simp [chiralGammaU, leftMul, reebM_i, mul_assoc]

/-- `M_j` anticommutes with `Γ_u`, for every `u`. -/
theorem chiralGammaU_anticomm_reebM_j (u p : BringCone R) :
    chiralGammaU u (reebM_j p) = -reebM_j (chiralGammaU u p) := by
  have h : (⟨0, 0, 1, 0⟩ : BringCone R) * ⟨0, 1, 0, 0⟩
      = -((⟨0, 1, 0, 0⟩ : BringCone R) * ⟨0, 0, 1, 0⟩) := by ext <;> simp
  simp only [chiralGammaU, leftMul, reebM_i, reebM_j, mul_assoc, h, mul_neg]

/-- `M_k` anticommutes with `Γ_u`, for every `u`. -/
theorem chiralGammaU_anticomm_reebM_k (u p : BringCone R) :
    chiralGammaU u (reebM_k p) = -reebM_k (chiralGammaU u p) := by
  have h : (⟨0, 0, 0, 1⟩ : BringCone R) * ⟨0, 1, 0, 0⟩
      = -((⟨0, 1, 0, 0⟩ : BringCone R) * ⟨0, 0, 0, 1⟩) := by ext <;> simp
  simp only [chiralGammaU, leftMul, reebM_i, reebM_k, mul_assoc, h, mul_neg]

/-- **The antipodal unit is the global flip**: `Γ_{−u} = −Γ_u`. -/
theorem chiralGammaU_neg (u p : BringCone R) :
    chiralGammaU (-u) p = -chiralGammaU u p := by
  simp [chiralGammaU, leftMul]

/-- For two square roots of `−1`, `q = 1 − v·u` satisfies `q·u = v·q`. -/
theorem intertwiner_mul {u v : BringCone R} (hu : u * u = -1) (hv : v * v = -1) :
    (1 - v * u) * u = v * (1 - v * u) := by
  rw [sub_mul, mul_sub, one_mul, mul_one, mul_assoc, hu, ← mul_assoc, hv]
  simp [add_comm]

/-- `L_q`, which commutes with the Reeb triad, carries `Γ_u` to `Γ_v`. -/
theorem leftMul_intertwines_chiralGammaU {u v : BringCone R}
    (hu : u * u = -1) (hv : v * v = -1) (p : BringCone R) :
    leftMul (1 - v * u) (chiralGammaU u p) = chiralGammaU v (leftMul (1 - v * u) p) := by
  simp only [chiralGammaU, leftMul, reebM_i]
  rw [← mul_assoc, ← mul_assoc, intertwiner_mul hu hv]
  simp only [mul_assoc]

/-- `L_{q̄} ∘ L_q = normSq q • id`: `L_q` is invertible when `normSq q` is a unit. -/
theorem leftMul_star_leftMul (q p : BringCone R) :
    leftMul (star q) (leftMul q p) = Quaternion.normSq q • p := by
  simp only [leftMul, ← mul_assoc, Quaternion.star_mul_self]
  ext <;> simp

/-- For pure units `u`, `v`, `normSq (1 − v·u) = 2·(1 + u·v)`. -/
theorem normSq_intertwiner {u v : BringCone R} (hu0 : u.re = 0) (hv0 : v.re = 0)
    (hu1 : Quaternion.normSq u = 1) (hv1 : Quaternion.normSq v = 1) :
    Quaternion.normSq (1 - v * u)
      = 2 * (1 + (u.imI * v.imI + u.imJ * v.imJ + u.imK * v.imK)) := by
  rw [Quaternion.normSq_def'] at hu1 hv1 ⊢
  simp [hu0, hv0] at hu1 hv1 ⊢
  linear_combination (v.imI ^ 2 + v.imJ ^ 2 + v.imK ^ 2) * hu1 + hv1

/-- **A radial direction is a chirality eigenvector only at its Hopf image.** For
a unit vector `p`, `Γ_u p = −p` iff `u = p·i·p̄`. -/
theorem chiralGammaU_eigen_iff {p : BringCone R} (hp : Quaternion.normSq p = 1)
    (u : BringCone R) :
    chiralGammaU u p = -p ↔ u = p * unitI * star p := by
  have hps : p * star p = 1 := by
    rw [Quaternion.self_mul_star, hp]; rfl
  have hsp : star p * p = 1 := by
    rw [Quaternion.star_mul_self, hp]; rfl
  simp only [chiralGammaU, leftMul, reebM_i_eq_mul_unitI]
  constructor
  · intro h
    have h1 : u * p = p * unitI := by
      calc u * p = u * p * (unitI * -unitI) := by rw [unitI_mul_neg_unitI, mul_one]
        _ = (u * (p * unitI)) * -unitI := by simp only [mul_assoc]
        _ = p * unitI := by
          rw [h, neg_mul_neg]
    calc u = u * (p * star p) := by rw [hps, mul_one]
      _ = (u * p) * star p := by rw [mul_assoc]
      _ = p * unitI * star p := by rw [h1]
  · intro h
    rw [h]
    calc p * unitI * star p * (p * unitI)
        = p * unitI * (star p * p) * unitI := by simp only [mul_assoc]
      _ = -p := by rw [hsp, mul_one, mul_assoc, unitI_mul_unitI]; simp

/-- The Hopf image `p·i·p̄` is pure. -/
theorem re_hopf (p : BringCone R) : (p * unitI * star p).re = 0 := by
  simp [unitI]; ring

/-- The Hopf image has norm `normSq p ^ 2`, so it is a pure unit when `p` is. -/
theorem normSq_hopf (p : BringCone R) :
    Quaternion.normSq (p * unitI * star p) = Quaternion.normSq p ^ 2 := by
  have hi : Quaternion.normSq (unitI : BringCone R) = 1 := by
    rw [Quaternion.normSq_def']; simp [unitI]
  simp only [map_mul, Quaternion.normSq_star, hi, mul_one, sq]

end QOU.Tetraplectic
