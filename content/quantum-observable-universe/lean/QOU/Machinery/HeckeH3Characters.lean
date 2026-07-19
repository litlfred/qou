import QOU.Machinery.HeckeH2Wedderburn

/-!
# QOU.Machinery.HeckeH3Characters — the two 1-dim Wedderburn blocks of H₃(q)

Wenzl-bridge **stage 2c-1** (bean `qou-vndn`, epic `qou-otbb`): the
character route of `HeckeH2Wedderburn` generalised to the
six-dimensional `H3A` of `HeckeH3AlgebraInstance`.

At each root $\ell$ of the Hecke quadratic $x^2 = h\,x + 1$ (over
$\mathbb{R}$: $q$ and $-q^{-1}$), sending **both** generators
$\sigma_0, \sigma_1 \mapsto \ell$ extends to a ring homomorphism
$H_3(q) \to R$.  On the NF basis
$[\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-]$ (words of lengths
$0,1,1,2,2,3$) the character is

$$ \chi_\ell(v) = v_0 + \ell\,(v_1 + v_2) + \ell^2 (v_3 + v_4)
   + \ell^3 v_5 . $$

These are the two **one-dimensional Wedderburn blocks** of
$H_3(q) \cong R \times R \times M_2(R)$ — the partitions $(3)$ and
$(1,1,1)$.  Everything here is sorry-free over a generic
`[CommRing R]` per §7c, including the **stabilization** statement:
the H₃ characters restrict along the tower inclusion `iotaAlg` to the
H₂ characters of `HeckeH2Wedderburn`.

**What stays open at this rank** (bean `qou-vndn`): the
two-dimensional block — the Hoefsmit seminormal representation
$H_3(q) \to M_2(R)$ for the partition $(2,1)$ (it needs the
invertible content denominator $[2]_q = \ell_+ - \ell_-$) — and the
assembled six-dimensional Wedderburn isomorphism
$H_3(q) \cong R \times R \times M_2(R)$.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- The **character functional** at `l` on NF coordinates: each basis
    word contributes `l ^ length`. -/
def chiNF (l : R) (v : Fin 6 → R) : R :=
  v 0 + l * (v 1 + v 2) + l ^ 2 * (v 3 + v 4) + l ^ 3 * v 5

@[simp] theorem chiNF_unitNF (l : R) : chiNF l (unitNF (R := R)) = 1 := by
  simp [chiNF, unitNF]

/-- The character intertwines the right `σ₀`-action with multiplication
    by the root: `χ_ℓ(σ₀ · u) = ℓ · χ_ℓ(u)` (sorry-free, given the root
    property). -/
theorem chiNF_mulσ₀ (h l : R) (hl : l * l = h * l + 1) (u : Fin 6 → R) :
    chiNF l (mulσ₀ h u) = l * chiNF l u := by
  simp [chiNF, mulσ₀]
  linear_combination (-(u 1) - l * u 3 - l ^ 2 * u 5) * hl

/-- The character intertwines the right `σ₁`-action with multiplication
    by the root (sorry-free). -/
theorem chiNF_mulσ₁ (h l : R) (hl : l * l = h * l + 1) (u : Fin 6 → R) :
    chiNF l (mulσ₁ h u) = l * chiNF l u := by
  simp [chiNF, mulσ₁]
  linear_combination (-(u 2) - l * u 4 - l ^ 2 * u 5) * hl

/-- **Multiplicativity of the character on the full NF product
    (sorry-free).**  Expand `mulNF` by right-linearity, then reduce each
    basis-word action with the two intertwining lemmas. -/
theorem chiNF_mulNF (h l : R) (hl : l * l = h * l + 1)
    (u v : Fin 6 → R) :
    chiNF l (mulNF h u v) = chiNF l u * chiNF l v := by
  have e : chiNF l (mulNF h u v) =
      v 0 * chiNF l u
      + v 1 * chiNF l (mulσ₀ h u)
      + v 2 * chiNF l (mulσ₁ h u)
      + v 3 * chiNF l (mulσ₀ h (mulσ₁ h u))
      + v 4 * chiNF l (mulσ₁ h (mulσ₀ h u))
      + v 5 * chiNF l (mulσ₀ h (mulσ₁ h (mulσ₀ h u))) := by
    simp only [chiNF, mulNF]
    ring
  rw [e]
  simp only [chiNF_mulσ₀ h l hl, chiNF_mulσ₁ h l hl]
  simp only [chiNF]
  ring

/-- The character restricts along the `H₂ ↪ H₃` inclusion to the rank-2
    character: `χ_ℓ(ι(a·γ + b·σ₀)) = a + ℓ·b` (sorry-free). -/
@[simp] theorem chiNF_iota23 (l a b : R) :
    chiNF l (iota23 a b) = a + l * b := by
  simp [chiNF, iota23]

namespace H3A

variable {h : R}

/-- **The 1-dim Wedderburn-block character of H₃(q) (sorry-free).**
    At a root `l` of the Hecke quadratic, `σ₀, σ₁ ↦ l` extends to the
    ring homomorphism `H₃(q) → R`.  The two roots give the two
    one-dimensional blocks — the partitions `(3)` and `(1,1,1)`. -/
def character (l : R) (hl : l * l = h * l + 1) : H3A R h →+* R where
  toFun x := chiNF l x.v
  map_one' := by simp
  map_mul' x y := chiNF_mulNF h l hl x.v y.v
  map_zero' := by simp [chiNF]
  map_add' x y := by
    show chiNF l (x.v + y.v) = chiNF l x.v + chiNF l y.v
    simp only [chiNF, Pi.add_apply]
    ring

@[simp] lemma character_apply (l : R) (hl : l * l = h * l + 1)
    (x : H3A R h) : character l hl x = chiNF l x.v := rfl

/-- **Character stabilization along the tower (sorry-free)**: the H₃
    character restricts along `iotaAlg : H₂(q) →ₐ H₃(q)` to the H₂
    character of `HeckeH2Wedderburn` at the same root. -/
theorem character_iotaAlg (l : R) (hl : l * l = h * l + 1)
    (x : H2A R h) :
    character l hl (H2A.iotaAlg x) = H2A.character l hl x := by
  show chiNF l (iota23 x.a x.b) = x.a + l * x.b
  simp

end H3A

end QOU.Machinery.H3
