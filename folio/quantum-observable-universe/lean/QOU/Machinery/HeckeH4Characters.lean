/-
# HeckeH4Characters — the two 1-dim Wedderburn blocks (characters χ±) of H₄(q)

Wedderburn tranche W1 (bean `qou-308a`; design provenance: the H₄ Wedderburn
design doc §3 "The coordinate map and its lemmas" + §6 W1 row, session
scratchpad `h4_wedderburn_iso/design.md`; `linear_combination` payloads:
`h4_wedderburn_iso/cofactors.json` SET D, goal keys `chi_mulsigma0/1/2`).
Rank-4 counterpart of `HeckeH3Characters`, built on the **subscript** 24-word
NF basis of `HeckeH4StabilizationRung` via the `mulNF₄` / `H4A` algebra of
`HeckeH4AlgebraLaws` (W0).

At each root $\ell$ of the Hecke quadratic $x^2 = h\,x + 1$ (at
$h = q - q^{-1}$ over a field: $q$ and $-q^{-1}$), sending **all three**
generators $\sigma_0, \sigma_1, \sigma_2 \mapsto \ell$ extends to an algebra
homomorphism $H_4(q) \to R$.  On the subscript NF basis (word lengths
`[0,1,1,2,2,3,1,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,6]`) the character is

$$ \chi_\ell(v) = v_0 + \ell\,(v_1 + v_2 + v_6)
   + \ell^2 (v_3 + v_4 + v_7 + v_8 + v_9)
   + \ell^3 (v_5 + v_{10} + v_{11} + v_{12} + v_{13} + v_{14})
   + \ell^4 (v_{15} + v_{16} + v_{17} + v_{18} + v_{19})
   + \ell^5 (v_{20} + v_{21} + v_{22}) + \ell^6 v_{23} . $$

These are the two **one-dimensional Wedderburn blocks** of
$H_4(q) \cong K \times K \times M_2(K) \times M_3(K) \times M_3(K)$ — the
partitions $(4)$ (at $\ell_+ = q$, χ⁺) and $(1,1,1,1)$ (at
$\ell_- = -q^{-1}$, χ⁻).  Everything here is sorry-free: the generic-root
functional, its three per-generator intertwiners, multiplicativity on the
full NF product, the `H4A.character` AlgHom, and the two concrete
characters `characterPlus` / `characterMinus` at the field-level roots.

Proved here (sorry-free):

* `chiNF₄` — the character functional at a generic root `l` (`[CommRing R]`);
* `chiNF₄_mulσ₀ / _mulσ₁ / _mulσ₂` — the three per-generator intertwiners
  `χ_ℓ(u·σₖ) = ℓ·χ_ℓ(u)` (SET-D `linear_combination` cofactors);
* `chiNF₄_mulNF₄` — multiplicativity `χ_ℓ(u·v) = χ_ℓ(u)·χ_ℓ(v)` on the full
  24-dim NF product, by right-basis expansion + the intertwiners;
* `H4A.character` — the induced algebra homomorphism `H4A R h →ₐ[R] R` at
  any root of the quadratic (generic `[CommRing R]`);
* `characterPlus` / `characterMinus` — the two concrete 1-dim blocks χ± at
  `l = q` / `l = -q⁻¹` over a `[Field K]` (the only section needing `q⁻¹`,
  per §7c; root facts `root_q` / `root_negInv` re-stated from the H3 file
  in the `H4` namespace).

Deliberately NOT imported: `MarkovTraceH4` (its `trM_cyclic` rests on a
cited `sorry`; this file builds only on `HeckeH4AlgebraLaws` →
`HeckeH4StabilizationRung`, keeping the Wedderburn chain sorry-free by
construction).

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): every statement below
is discharged by computation — no axiom, no conditional class, no
`native_decide`.  The assembled rank-4 Wedderburn isomorphism (W3/W4) and
the three matrix blocks (W2a–c) are separate tranches, still open.
Nothing wired; `1/(8π)` stays phase-4.

Base ring (§7c): generic `[CommRing R]` throughout; `[Field K]` only in the
final section, where the concrete roots `q`, `-q⁻¹` need `q⁻¹`.  No `ℝ`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeH4AlgebraLaws
import Mathlib.Tactic

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-! ## The character functional `chiNF₄` at a generic root -/

/-- The **character functional** at `l` on the subscript 24-word NF
    coordinates: each basis word contributes `l ^ length` (lengths
    `[0,1,1,2,2,3,1,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,6]`). -/
def chiNF₄ (l : R) (v : Fin 24 → R) : R :=
  v 0 + l * (v 1 + v 2 + v 6) + l ^ 2 * (v 3 + v 4 + v 7 + v 8 + v 9)
    + l ^ 3 * (v 5 + v 10 + v 11 + v 12 + v 13 + v 14)
    + l ^ 4 * (v 15 + v 16 + v 17 + v 18 + v 19)
    + l ^ 5 * (v 20 + v 21 + v 22) + l ^ 6 * v 23

@[simp] theorem chiNF₄_unitNF₄ (l : R) :
    chiNF₄ l (unitNF₄ (R := R)) = 1 := by
  simp [chiNF₄, unitNF₄]

/-! ## Per-generator intertwiners (SET D)

Each lemma: `χ_ℓ(u·σₖ) = ℓ·χ_ℓ(u)` given the root property
`hl : l * l = h * l + 1`.  The `linear_combination` payload is the exact
SET-D cofactor from `h4_wedderburn_iso/cofactors.json` (goal keys
`chi_mulsigma0/1/2`) — the direct rank-4 generalization of H3's
`(-(u 1) - l * u 3 - l ^ 2 * u 5) * hl`. -/

/-- The character intertwines the right `σ₀`-action with multiplication
    by the root: `χ_ℓ(u·σ₀) = ℓ·χ_ℓ(u)` (sorry-free, given the root
    property). -/
theorem chiNF₄_mulσ₀ (h l : R) (hl : l * l = h * l + 1) (u : Fin 24 → R) :
    chiNF₄ l (mulσ₀ h u) = l * chiNF₄ l u := by
  simp [chiNF₄, mulσ₀]
  linear_combination (-(l ^ 5 * u 23) - l ^ 4 * u 21 - l ^ 4 * u 22
    - l ^ 3 * u 15 - l ^ 3 * u 18 - l ^ 3 * u 19 - l ^ 2 * u 11
    - l ^ 2 * u 14 - l ^ 2 * u 5 - l * u 3 - l * u 8 - u 1) * hl

/-- The character intertwines the right `σ₁`-action with multiplication
    by the root: `χ_ℓ(u·σ₁) = ℓ·χ_ℓ(u)` (sorry-free). -/
theorem chiNF₄_mulσ₁ (h l : R) (hl : l * l = h * l + 1) (u : Fin 24 → R) :
    chiNF₄ l (mulσ₁ h u) = l * chiNF₄ l u := by
  simp [chiNF₄, mulσ₁]
  linear_combination (-(l ^ 5 * u 23) - l ^ 4 * u 20 - l ^ 4 * u 22
    - l ^ 3 * u 16 - l ^ 3 * u 17 - l ^ 3 * u 19 - l ^ 2 * u 12
    - l ^ 2 * u 13 - l ^ 2 * u 5 - l * u 4 - l * u 9 - u 2) * hl

/-- The character intertwines the right `σ₂`-action with multiplication
    by the root: `χ_ℓ(u·σ₂) = ℓ·χ_ℓ(u)` (sorry-free). -/
theorem chiNF₄_mulσ₂ (h l : R) (hl : l * l = h * l + 1) (u : Fin 24 → R) :
    chiNF₄ l (mulσ₂ h u) = l * chiNF₄ l u := by
  simp [chiNF₄, mulσ₂]
  linear_combination (-(l ^ 5 * u 23) - l ^ 4 * u 20 - l ^ 4 * u 21
    - l ^ 3 * u 15 - l ^ 3 * u 16 - l ^ 3 * u 18 - l ^ 2 * u 10
    - l ^ 2 * u 11 - l ^ 2 * u 12 - l * u 7 - l * u 8 - u 6) * hl

/-! ## Multiplicativity on the full NF product -/

set_option maxHeartbeats 1600000 in
/-- **Multiplicativity of the character on the full NF product
    (sorry-free).**  Expand `mulNF₄` by right-linearity into the 24
    basis-word composites, then reduce each composite with the three
    intertwining lemmas (word length many root factors each). -/
theorem chiNF₄_mulNF₄ (h l : R) (hl : l * l = h * l + 1)
    (u v : Fin 24 → R) :
    chiNF₄ l (mulNF₄ h u v) = chiNF₄ l u * chiNF₄ l v := by
  have e : chiNF₄ l (mulNF₄ h u v) =
      v 0 * chiNF₄ l u
      + v 1 * chiNF₄ l (mulσ₀ h u)
      + v 2 * chiNF₄ l (mulσ₁ h u)
      + v 3 * chiNF₄ l (mulσ₀ h (mulσ₁ h u))
      + v 4 * chiNF₄ l (mulσ₁ h (mulσ₀ h u))
      + v 5 * chiNF₄ l (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))
      + v 6 * chiNF₄ l (mulσ₂ h u)
      + v 7 * chiNF₄ l (mulσ₂ h (mulσ₁ h u))
      + v 8 * chiNF₄ l (mulσ₀ h (mulσ₂ h u))
      + v 9 * chiNF₄ l (mulσ₁ h (mulσ₂ h u))
      + v 10 * chiNF₄ l (mulσ₂ h (mulσ₁ h (mulσ₀ h u)))
      + v 11 * chiNF₄ l (mulσ₂ h (mulσ₀ h (mulσ₁ h u)))
      + v 12 * chiNF₄ l (mulσ₁ h (mulσ₂ h (mulσ₁ h u)))
      + v 13 * chiNF₄ l (mulσ₁ h (mulσ₀ h (mulσ₂ h u)))
      + v 14 * chiNF₄ l (mulσ₀ h (mulσ₁ h (mulσ₂ h u)))
      + v 15 * chiNF₄ l (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u))))
      + v 16 * chiNF₄ l (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u))))
      + v 17 * chiNF₄ l (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u))))
      + v 18 * chiNF₄ l (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h u))))
      + v 19 * chiNF₄ l (mulσ₀ h (mulσ₁ h (mulσ₀ h (mulσ₂ h u))))
      + v 20 * chiNF₄ l (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))))
      + v 21 * chiNF₄ l (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u)))))
      + v 22 * chiNF₄ l (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u)))))
      + v 23 * chiNF₄ l
          (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))))) := by
    simp only [chiNF₄, mulNF₄]
    ring
  rw [e]
  simp only [chiNF₄_mulσ₀ h l hl, chiNF₄_mulσ₁ h l hl, chiNF₄_mulσ₂ h l hl]
  simp only [chiNF₄]
  ring

/-! ## The character as an algebra homomorphism -/

namespace H4A

variable {h : R}

/-- **The 1-dim Wedderburn-block character of H₄(q) (sorry-free).**
    At a root `l` of the Hecke quadratic, `σ₀, σ₁, σ₂ ↦ l` extends to the
    algebra homomorphism `H₄(q) →ₐ R`.  The two roots give the two
    one-dimensional blocks — the partitions `(4)` and `(1,1,1,1)`. -/
def character (l : R) (hl : l * l = h * l + 1) : H4A R h →ₐ[R] R where
  toFun x := chiNF₄ l x.v
  map_one' := by simp
  map_mul' x y := chiNF₄_mulNF₄ h l hl x.v y.v
  map_zero' := by
    show chiNF₄ l (0 : Fin 24 → R) = 0
    simp [chiNF₄]
  map_add' x y := by
    show chiNF₄ l (x.v + y.v) = chiNF₄ l x.v + chiNF₄ l y.v
    simp only [chiNF₄, Pi.add_apply]
    ring
  commutes' c := by
    show chiNF₄ l ((c • (1 : H4A R h)).v) = algebraMap R R c
    rw [smul_v, one_v]
    simp [chiNF₄, unitNF₄]

@[simp] lemma character_apply (l : R) (hl : l * l = h * l + 1)
    (x : H4A R h) : character l hl x = chiNF₄ l x.v := rfl

end H4A

/-! ## The two concrete characters χ± at the field-level roots

The only section needing `q⁻¹` (§7c): over a field, the Hecke quadratic at
`h = q - q⁻¹` has the two roots `q` and `-q⁻¹`.  The root facts are
re-stated from `HeckeH3Wedderburn` in the `H4` namespace (per the design
§"Genericity hypotheses"). -/

section FieldRoots

variable {K : Type*} [Field K]

/-- `q` is a root of the Hecke quadratic at `h = q - q⁻¹` (sorry-free). -/
theorem root_q (q : K) (hq : q ≠ 0) : q * q = (q - q⁻¹) * q + 1 := by
  field_simp
  all_goals ring

/-- `-q⁻¹` is the other root (sorry-free). -/
theorem root_negInv (q : K) (hq : q ≠ 0) :
    (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by
  field_simp
  all_goals ring

/-- **χ⁺ — the trivial-type character of H₄(q) (sorry-free)**: the
    one-dimensional Wedderburn block of the partition `(4)`, at the root
    `l = q`. -/
noncomputable def H4A.characterPlus (q : K) (hq : q ≠ 0) :
    H4A K (q - q⁻¹) →ₐ[K] K :=
  H4A.character q (root_q q hq)

/-- **χ⁻ — the sign-type character of H₄(q) (sorry-free)**: the
    one-dimensional Wedderburn block of the partition `(1,1,1,1)`, at the
    root `l = -q⁻¹`. -/
noncomputable def H4A.characterMinus (q : K) (hq : q ≠ 0) :
    H4A K (q - q⁻¹) →ₐ[K] K :=
  H4A.character (-q⁻¹) (root_negInv q hq)

@[simp] lemma H4A.characterPlus_apply (q : K) (hq : q ≠ 0)
    (x : H4A K (q - q⁻¹)) : H4A.characterPlus q hq x = chiNF₄ q x.v := rfl

@[simp] lemma H4A.characterMinus_apply (q : K) (hq : q ≠ 0)
    (x : H4A K (q - q⁻¹)) :
    H4A.characterMinus q hq x = chiNF₄ (-q⁻¹) x.v := rfl

end FieldRoots

end QOU.Machinery.H4
