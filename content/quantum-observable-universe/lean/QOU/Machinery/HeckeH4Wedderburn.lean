import QOU.Machinery.HeckeH4WedderburnInv

/-!
# QOU.Machinery.HeckeH4Wedderburn — the full rank-4 Wedderburn isomorphism

Wedderburn tranche **W4** (bean `qou-308a`; design provenance: the H₄
Wedderburn design doc §4, session scratchpad `h4_wedderburn_iso/design.md`):
the assembled explicit isomorphism

$$ H_4(q) \;\cong\; K \times K \times M_2(K) \times M_3(K) \times M_3(K) $$

from the two characters (`HeckeH4Characters`), the three block
representations (`HeckeH4BlockMap22/31/211`), and the Lean-verified inverse
coordinate map (`HeckeH4WedderburnCoord` → `HeckeH4WedderburnMul*` →
`HeckeH4WedderburnInv`), mirroring the merged rank-3 pattern
`HeckeH3Wedderburn.wedderburn₃`.

The inverse was computed symbolically (sympy, 24×24 inversion over
$\mathbb{Q}(q)$) and is **verified by Lean** — nothing is trusted from the
computation; the determinant of the coordinate map is

$$ \det A = -\frac{(q^2+1)^{24}\,(q^4+1)^{10}\,(q^2-q+1)^3\,(q^2+q+1)^3}
{q^{50}}, $$

so the degeneracy locus is exactly the Wenzl genericity condition at rank 4:
the hypotheses are `q ≠ 0`, `q ^ 2 + 1 ≠ 0` ($[2]$-type),
`q ^ 4 + q ^ 2 + 1 = (q^2+q+1)(q^2-q+1) ≠ 0` ($[3]$-type) and the **new**
$[4]$-type condition `q ^ 4 + 1 ≠ 0` absent at rank 3.  Over $\mathbb{R}$
all four hold for every `q ≠ 0` — the denominators are strictly positive —
so only `q ≠ 0` remains.

**Semisimplicity note:** the Prop-level corollary
`IsSemisimpleRing (H4A K (q - q⁻¹))` is derived in `HeckeH4Semisimple` by
transfer along this isomorphism, with the matrix factors supplied by
`QOU.MathlibExt.MatrixSemisimple`.  The explicit isomorphism below is the
stronger statement.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): every declaration below
is discharged by computation — no axiom, no `sorry`, no conditional class,
no `native_decide`.

Base ring (§7c): generic `[Field K]`; no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Machinery.H4

variable {K : Type*} [Field K]

/-- **The assembled Wedderburn homomorphism (sorry-free)**
    $(\chi_+, \chi_-, \rho_{22}, \rho_{31}, \rho_{211}) :
    H_4(q) \to K \times K \times M_2(K) \times M_3(K) \times M_3(K)$,
    assembled by `AlgHom.prod` from the five committed block algebra
    homomorphisms. -/
noncomputable def wedderburnHom₄ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    H4A K (q - q⁻¹) →ₐ[K] K × K × Matrix (Fin 2) (Fin 2) K
      × Matrix (Fin 3) (Fin 3) K × Matrix (Fin 3) (Fin 3) K :=
  (H4A.characterPlus q hq).prod <|
    (H4A.characterMinus q hq).prod <|
      (H4A.blockRep22 q hq h2).prod <|
        (H4A.blockRep31 q hq h2 h3).prod (H4A.blockRep211 q hq h2 h3)

@[simp] lemma wedderburnHom₄_apply (q : K) (hq : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (x : H4A K (q - q⁻¹)) :
    wedderburnHom₄ q hq h2 h3 x
      = (chiNF₄ q x.v, chiNF₄ (-q⁻¹) x.v, blockOf22 q x.v,
         blockOf31 q x.v, blockOf211 q x.v) := rfl

/-- **The rank-4 Wedderburn isomorphism (sorry-free):**
    $H_4(q) \cong K \times K \times M_2(K) \times M_3(K) \times M_3(K)$
    whenever `q ≠ 0`, `q ^ 2 + 1 ≠ 0`, `q ^ 4 + q ^ 2 + 1 ≠ 0` and
    `q ^ 4 + 1 ≠ 0` — exactly the Wenzl genericity locus at rank 4, read
    off the determinant of the coordinate map.  Injectivity is the
    coordinate left inverse `wedderburnInvV₄_left`; surjectivity is the
    explicit inverse with the five right-inverse component lemmas. -/
noncomputable def wedderburn₄ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    H4A K (q - q⁻¹) ≃ₐ[K] K × K × Matrix (Fin 2) (Fin 2) K
      × Matrix (Fin 3) (Fin 3) K × Matrix (Fin 3) (Fin 3) K :=
  AlgEquiv.ofBijective (wedderburnHom₄ q hq h2 h3) <| by
    constructor
    · -- injective via the coordinate left inverse
      intro x y hxy
      simp only [wedderburnHom₄_apply] at hxy
      apply H4A.ext
      have h1 : chiNF₄ q x.v = chiNF₄ q y.v := congrArg (fun p => p.1) hxy
      have hm : chiNF₄ (-q⁻¹) x.v = chiNF₄ (-q⁻¹) y.v :=
        congrArg (fun p => p.2.1) hxy
      have hb22 : blockOf22 q x.v = blockOf22 q y.v :=
        congrArg (fun p => p.2.2.1) hxy
      have hb31 : blockOf31 q x.v = blockOf31 q y.v :=
        congrArg (fun p => p.2.2.2.1) hxy
      have hb211 : blockOf211 q x.v = blockOf211 q y.v :=
        congrArg (fun p => p.2.2.2.2) hxy
      calc x.v
          = wedderburnInvV₄ q (chiNF₄ q x.v) (chiNF₄ (-q⁻¹) x.v)
              (blockOf22 q x.v) (blockOf31 q x.v) (blockOf211 q x.v) :=
            (wedderburnInvV₄_left q hq h2 h3 h4 x.v).symm
        _ = wedderburnInvV₄ q (chiNF₄ q y.v) (chiNF₄ (-q⁻¹) y.v)
              (blockOf22 q y.v) (blockOf31 q y.v) (blockOf211 q y.v) := by
            rw [h1, hm, hb22, hb31, hb211]
        _ = y.v := wedderburnInvV₄_left q hq h2 h3 h4 y.v
    · -- surjective via the explicit inverse
      rintro ⟨s, t, M2, M31, M211⟩
      refine ⟨⟨wedderburnInvV₄ q s t M2 M31 M211⟩, ?_⟩
      simp only [wedderburnHom₄_apply]
      refine Prod.ext ?_ (Prod.ext ?_ (Prod.ext ?_ (Prod.ext ?_ ?_)))
      · exact chiNF₄_wedderburnInvV₄_plus q hq h2 h3 h4 s t M2 M31 M211
      · exact chiNF₄_wedderburnInvV₄_minus q hq h2 h3 h4 s t M2 M31 M211
      · exact blockOf22_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211
      · exact blockOf31_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211
      · exact blockOf211_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211

end QOU.Machinery.H4
