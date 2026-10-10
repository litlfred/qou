/-
# The abstract tower inclusion — trivial-coset embedding at every rank

The general-rank leg of the tower program: the merged concrete `ι₃₄`
(H₃ ↪ H₄ on NF coordinates, extension by zero) is revealed as the
instance of a COMPLETELY GENERAL construction — for ANY Coxeter system
and ANY generator subset `J`, the parabolic subgroup carries an induced
descent structure, and extension-by-zero along the coset decomposition
embeds its length-rule module into the full one, intertwining BOTH the
generator actions and the `q = i` monodromy nilpotents:

* **`descentRight`** — the right-multiplication descent structure of a
  single generator on the full group (the abstract form of the
  transversals' `ti`/`tj`), with the length toggle from
  `length_mul_simple`. No hypotheses.
* **`descentParabolic`** — its restriction to the parabolic subtype
  `{w // w ∈ W_J}` for `l ∈ J`: the subgroup is closed under the step
  and inherits the length data. No hypotheses.
* **`iotaPar`** — extension by zero along the coset decomposition:
  `(W_J → R) → (W → R)` supported on the trivial coset.
* **`iotaPar_mulStep`** — the ACTION square: `ι ∘ (·σₗ) = (·σₗ) ∘ ι`
  for every `l ∈ J`, at every rank, over any commutative ring. The
  merged `iota34_mulσ₀` / `iota34_mulσ₁` are the `A₃ ⊂ A₄`-rung shadow
  of this statement.
* **`iotaPar_monodromyN`** — the NILPOTENT square over `ℂ`:
  `ι ∘ N_J = N ∘ ι`. The merged concrete `iota34_monodromyN` at the
  H₃ → H₄ rung is the table-level shadow; here it holds abstractly with
  NO faithfulness residue — membership logic only.

Together with the τ-assignment tower square (`HeckeTauAssignmentTower`),
this pins the general shape of the all-rungs functor: the inclusion,
its intertwining, and the nilpotent naturality are now rank-free; what
remains open is the general-rank ASSIGNMENT (a `TauAssignmentData` for
every rung with the compatibility square, whose H3/H4 instances are
proved) and the identification of the concrete NF enumerations with the
abstract coset decompositions.

HONESTY (STRICT): sorry-free, hypothesis-free (not even the Tits
residue — only subgroup membership logic and the length toggle).
Nothing wired; `1/(8π)` stays phase-4. Base ring: generic
`[CommRing R]`; `ℂ` enters only for the monodromy nilpotent (§7c).

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterParabolicCoset
import QOU.Machinery.HeckeMonodromyJordan

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

/-- The right-multiplication descent structure of a single generator on
the full group — the abstract form of the transversals' step maps. -/
noncomputable def descentRight (l : B) : DescentStructure W where
  t := fun w => w * σ l
  len := cs.length
  t_invol := fun w => by
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
  len_ne := fun w => by
    rcases cs.length_mul_simple w l with h | h <;> omega

variable (J : Set B)

/-- Right multiplication by a generator of `J` preserves the parabolic. -/
lemma mul_simple_mem_parabolic {l : B} (hl : l ∈ J) {w : W}
    (hw : w ∈ parabolic cs J) : w * σ l ∈ parabolic cs J :=
  (parabolic cs J).mul_mem hw (Subgroup.subset_closure ⟨l, hl, rfl⟩)

/-- Membership in the parabolic is invariant under the generator step. -/
lemma mul_simple_mem_parabolic_iff {l : B} (hl : l ∈ J) (w : W) :
    w * σ l ∈ parabolic cs J ↔ w ∈ parabolic cs J := by
  constructor
  · intro h
    have := mul_simple_mem_parabolic cs J hl h
    rwa [mul_assoc, cs.simple_mul_simple_self, mul_one] at this
  · exact mul_simple_mem_parabolic cs J hl

/-- The induced descent structure of `l ∈ J` on the parabolic subtype:
the subgroup is closed under the step and inherits the length data. -/
noncomputable def descentParabolic {l : B} (hl : l ∈ J) :
    DescentStructure {w : W // w ∈ parabolic cs J} where
  t := fun w => ⟨w.val * σ l, mul_simple_mem_parabolic cs J hl w.prop⟩
  len := fun w => ℓ w.val
  t_invol := fun w => by
    apply Subtype.ext
    show w.val * σ l * σ l = w.val
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
  len_ne := fun w => by
    show ℓ (w.val * σ l) ≠ ℓ w.val
    rcases cs.length_mul_simple w.val l with h | h <;> omega

/-- **The tower inclusion**: extension by zero along the coset
decomposition, supported on the trivial coset. -/
noncomputable def iotaPar {R : Type*} [CommRing R]
    (v : {w : W // w ∈ parabolic cs J} → R) : W → R :=
  fun w => if h : w ∈ parabolic cs J then v ⟨w, h⟩ else 0

variable {R : Type*} [CommRing R]

/-- **The ACTION square at every rank**: the inclusion intertwines the
generator step actions, for every `l ∈ J`, over any commutative ring —
the abstract form of the merged `iota34_mulσ₀` / `iota34_mulσ₁`. -/
theorem iotaPar_mulStep {l : B} (hl : l ∈ J) (h : R)
    (v : {w : W // w ∈ parabolic cs J} → R) :
    mulStep (descentRight cs l) h (iotaPar cs J v)
      = iotaPar cs J (mulStep (descentParabolic cs J hl) h v) := by
  funext w
  by_cases hw : w ∈ parabolic cs J
  · have hstep : w * σ l ∈ parabolic cs J :=
      mul_simple_mem_parabolic cs J hl hw
    simp only [mulStep, iotaPar, descentRight, descentParabolic,
      dif_pos hw, dif_pos hstep]
  · have hstep : ¬ (w * σ l ∈ parabolic cs J) := by
      rw [mul_simple_mem_parabolic_iff cs J hl]
      exact hw
    simp only [mulStep, iotaPar, descentRight, descentParabolic,
      dif_neg hw, dif_neg hstep, mul_zero, add_zero, ite_self]

/-- **The NILPOTENT square at every rank** (over `ℂ`, at the monodromy
point `q = i`): the inclusion intertwines the Jordan nilpotents,
`ι ∘ N_J = N ∘ ι` — the abstract form of the merged
`iota34_monodromyN`, with no faithfulness residue. -/
theorem iotaPar_monodromyN {l : B} (hl : l ∈ J)
    (v : {w : W // w ∈ parabolic cs J} → ℂ) :
    iotaPar cs J (monodromyN (descentParabolic cs J hl) v)
      = monodromyN (descentRight cs l) (iotaPar cs J v) := by
  unfold monodromyN
  rw [iotaPar_mulStep cs J hl]
  funext w
  by_cases hw : w ∈ parabolic cs J
  · simp only [iotaPar, Pi.sub_apply, Pi.smul_apply, smul_eq_mul,
      dif_pos hw]
  · simp only [iotaPar, Pi.sub_apply, Pi.smul_apply, smul_eq_mul,
      dif_neg hw, mul_zero, sub_zero]

end QOU.Machinery.CoxeterParabolic
