import QOU.Machinery.HeckeH2AlgebraInstance
import Mathlib.RingTheory.SimpleModule.Basic

/-!
# QOU.Machinery.HeckeH2Wedderburn — explicit Wedderburn decomposition of H₂(q)

Wenzl-bridge **stage 2b** (bean `qou-101j`, epic `qou-otbb`): the first
*proved* semisimplicity content behind the cited criterion classes
(`QOU.Information.PNeqNpEquivalence.WenzlCriterion`,
`QOU.MathlibExt.WenzlSchurElement.SchurElementCriterion`), at rank
$n = 2$, on the concrete Hecke algebra `H2A` of
`HeckeH2AlgebraInstance`.

Given the two roots $\ell_\pm$ of the Hecke quadratic
$x^2 = h\,x + 1$ (over $\mathbb{R}$: $\ell_\pm = (h \pm \sqrt{h^2+4})/2$,
i.e. $q$ and $-q^{-1}$) with invertible difference, the two
**characters** $a + b\,\sigma \mapsto a + \ell_\pm b$ assemble into an
explicit algebra isomorphism

$$ H_2(q) \;\cong\; R \times R $$

— the rank-2 Wedderburn decomposition, whose two one-dimensional
blocks are the partitions $(2)$ and $(1,1)$.  Everything here is
**sorry-free** over a generic commutative ring per §7c; the
archimedean instantiation (real roots via `Real.sqrt`, unconditional
semisimplicity) lives in `HeckeH2WedderburnReal`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.Machinery.H3
namespace H2A

variable {R : Type*} [CommRing R] {h : R}

/-- The **character** of `H2A R h` at a root `l` of the Hecke quadratic
    `x² = h·x + 1`: the ring homomorphism `a + b·σ ↦ a + l·b`
    (sorry-free — multiplicativity is exactly the root property). -/
def character (l : R) (hl : l * l = h * l + 1) : H2A R h →+* R where
  toFun x := x.a + l * x.b
  map_one' := by simp
  map_mul' x y := by
    simp only [mul_a, mul_b]
    linear_combination (-(x.b * y.b)) * hl
  map_zero' := by simp
  map_add' x y := by simp; ring

@[simp] lemma character_apply (l : R) (hl : l * l = h * l + 1)
    (x : H2A R h) : character l hl x = x.a + l * x.b := rfl

/-- **The rank-2 Wedderburn decomposition (sorry-free).**  Given the two
    roots `lp`, `lm` of the Hecke quadratic with invertible difference
    (`d` its inverse), the paired characters give an `R`-algebra
    isomorphism `H₂(q) ≃ R × R`.  The two factors are the Wedderburn
    blocks of the partitions `(2)` and `(1,1)`. -/
def wedderburn (lp lm : R)
    (hp : lp * lp = h * lp + 1) (hm : lm * lm = h * lm + 1)
    (d : R) (hd : d * (lp - lm) = 1) :
    H2A R h ≃ₐ[R] R × R where
  toFun x := (character lp hp x, character lm hm x)
  invFun p := ⟨p.1 - lp * (d * (p.1 - p.2)), d * (p.1 - p.2)⟩
  left_inv x := by
    ext
    · show x.a + lp * x.b - lp * (d * ((x.a + lp * x.b) - (x.a + lm * x.b))) = x.a
      linear_combination (-lp * x.b) * hd
    · show d * ((x.a + lp * x.b) - (x.a + lm * x.b)) = x.b
      linear_combination x.b * hd
  right_inv p := by
    ext
    · show (p.1 - lp * (d * (p.1 - p.2))) + lp * (d * (p.1 - p.2)) = p.1
      ring
    · show (p.1 - lp * (d * (p.1 - p.2))) + lm * (d * (p.1 - p.2)) = p.2
      linear_combination (p.2 - p.1) * hd
  map_mul' x y := by
    ext
    · show character lp hp (x * y) = character lp hp x * character lp hp y
      exact map_mul _ x y
    · show character lm hm (x * y) = character lm hm x * character lm hm y
      exact map_mul _ x y
  map_add' x y := by
    ext
    · show character lp hp (x + y) = character lp hp x + character lp hp y
      exact map_add _ x y
    · show character lm hm (x + y) = character lm hm x + character lm hm y
      exact map_add _ x y
  commutes' r := by
    have hmap : (algebraMap R (H2A R h) r) = ⟨r, 0⟩ := by
      ext <;> simp [Algebra.algebraMap_eq_smul_one]
    ext <;> simp [hmap]

/-- **Semisimplicity of H₂(q) over a field, given generic roots
    (sorry-free).**  Transfer `IsSemisimpleRing (K × K)` along the
    Wedderburn isomorphism. -/
theorem isSemisimpleRing_of_roots {K : Type*} [Field K] {h : K}
    (lp lm : K) (hp : lp * lp = h * lp + 1) (hm : lm * lm = h * lm + 1)
    (hne : lp ≠ lm) : IsSemisimpleRing (H2A K h) :=
  ((wedderburn lp lm hp hm (lp - lm)⁻¹
      (inv_mul_cancel₀ (sub_ne_zero.mpr hne))).symm.toRingEquiv).isSemisimpleRing

end H2A
end QOU.Machinery.H3
