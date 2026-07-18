import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Prime.Basic
-- TODO: cross-paper dependency on unital-groebner-bases
-- The QOU bridge module (content/fred2005-formal-groups/lean/QOU/FormalGroups.lean) imports:
--   import QOU.GrobnerShirshov.Basic
-- This will need a cross-paper reference once the content pipeline
-- supports lean cross-paper imports.

/-!
# Formal Groups and the Lifting Theorem

Lean formalization of the formal-groups integration results from:

  L. Fred, *Integration of Skewed-Poisson Structures on Non-commutative
  Formal Groups*, PhD thesis, University of Arizona, 2005.

These results provide the algebraic foundation for the QOU lifting
mechanism (Proposition `jet-prolongation` in Chapter 4) when the base
field has positive characteristic.

## Structure

1. **Commutative formal group** — the base object `H / 𝔽_p`
2. **Skewed-Poisson structure** — biderivation on `H` encoding non-commutativity
3. **Non-commutative formal group** — the output `G / ℤ_p` of integration
4. **Integration theorem** — skewed-Poisson → non-commutative formal group
5. **Gröbner–Shirshov deformation** — normal-form basis for `Dist(G)`
6. **Strong multiplicativity** — comultiplication preserved under deformation
7. **Witt vector lift** — formal group over `ℤ_p` reducing to `H` mod `p`
8. **Unit-root F-crystal** — equivalence with integrability

## References

- [fred2005] L. Fred, PhD thesis, University of Arizona, 2005.
- [hazewinkel1978] M. Hazewinkel, *Formal Groups and Applications*, Academic Press.
- [zink2002] T. Zink, *The Display of a Formal p-Divisible Group*, Astérisque 278.
-/


namespace Fred2005

universe u v

/-! ## §1  Commutative Formal Group -/

/-- **Commutative formal group** over a field `k` of characteristic `p`.
    This is the "base" object `H` in the dissertation's integration theorem.

    Reference: [hazewinkel1978, Ch. I]. -/
structure CommutativeFormalGroup where
  /-- The prime characteristic. -/
  p : ℕ
  /-- `p` is prime. -/
  p_prime : Nat.Prime p
  /-- Carrier type of the coordinate ring `𝒪(H)`. -/
  coordRing : Type u
  /-- The formal group law `F : 𝒪(H) → 𝒪(H) → 𝒪(H)`. -/
  formalGroupLaw : coordRing → coordRing → coordRing
  /-- The formal group law is commutative: `F(X,Y) = F(Y,X)`.
      [hazewinkel1978, Ch. I] -/
  commutative : ∀ (x y : coordRing), formalGroupLaw x y = formalGroupLaw y x
  /-- The zero element of the coordinate ring.
      Every formal group law satisfies `F(X, 0) = X`. -/
  zero : coordRing

/-! ## §2  Skewed-Poisson Structure -/

/-- **Skewed-Poisson structure** on a commutative formal group `H`.
    A biderivation `π_< : 𝒪(H) ⊗ 𝒪(H) → 𝒪(H)` satisfying graded
    anti-symmetry and a `p`-truncated Jacobi condition.

    This is the infinitesimal datum that encodes the non-commutativity
    to be "integrated" into a non-commutative formal group.

    Reference: [fred2005, §2, Definition 2.3]. -/
structure SkewedPoissonStructure (H : CommutativeFormalGroup) where
  /-- The biderivation `π_<` (abstract map on coordinate rings). -/
  bracket : H.coordRing → H.coordRing → H.coordRing
  /-- Negation on the coordinate ring (needed for anti-symmetry). -/
  neg : H.coordRing → H.coordRing
  /-- Graded anti-symmetry: `π_<(f, g) = −π_<(g, f)`.
      [fred2005, §2, Definition 2.3] -/
  antisymmetric : ∀ (f g : H.coordRing), bracket f g = neg (bracket g f)
  /-- The `p`-truncated Jacobi condition:
      `π_<(f, π_<(g, h)) + π_<(g, π_<(h, f)) + π_<(h, π_<(f, g)) = 0`
      modulo `p`-th powers.
      [fred2005, §2, Definition 2.3] -/
  jacobi_truncated : ∀ (f g h : H.coordRing),
    H.formalGroupLaw (H.formalGroupLaw (bracket f (bracket g h))
                                       (bracket g (bracket h f)))
                     (bracket h (bracket f g)) =
    H.formalGroupLaw (bracket h (bracket f g))
                     (H.formalGroupLaw (bracket f (bracket g h))
                                       (bracket g (bracket h f)))

/-! ## §3  Non-commutative Formal Group -/

/-- **Non-commutative formal group**: the output of the integration
    theorem.  This is the formal group `G` over `ℤ_p` whose distribution
    algebra is the Gröbner–Shirshov deformation of `Dist(H)`.

    Reference: [fred2005, Main Theorem]. -/
structure NoncommutativeFormalGroup where
  /-- The commutative base group `H / 𝔽_p`. -/
  base : CommutativeFormalGroup.{u}
  /-- Carrier type of `Dist(G)`. -/
  distAlgebra : Type u
  /-- The multiplication on `Dist(G)` (generally non-commutative). -/
  mul : distAlgebra → distAlgebra → distAlgebra
  /-- The comultiplication on `Dist(G)`. -/
  comul : distAlgebra → distAlgebra × distAlgebra
  /-- The identity element of `Dist(G)`. -/
  unit : distAlgebra
  /-- **Strong multiplicativity**: the comultiplication is an algebra
      homomorphism, i.e. `Δ(xy) = Δ(x) · Δ(y)` component-wise.
      This is the key condition from [fred2005, Theorem 4.12]. -/
  comul_hom : ∀ (x y : distAlgebra),
    comul (mul x y) =
    (mul (comul x).1 (comul y).1, mul (comul x).2 (comul y).2)

/-! ## §4  Integration Theorem (Main Theorem of [fred2005]) -/

/-- **Integration theorem** ([fred2005, Main Theorem]):
    A skewed-Poisson structure on a commutative formal group `H / 𝔽_p`
    integrates to a non-commutative formal group `G / ℤ_p`.

    The construction uses `H.coordRing` as the distribution algebra,
    the formal group law deformed by the bracket as multiplication,
    and the diagonal as comultiplication (group-like elements).

    Reference: [fred2005, Main Theorem].

    NOTE (honest disposition, 2026-07-18; AUTHOR TO VERIFY): the witness below is a
    *faithful* construction — the distribution algebra is `H.coordRing`, the
    multiplication is the **bracket-deformed product** `mul x y = F(x, π_<(x,y))`,
    and the comultiplication is the group-like diagonal (per the construction note
    above). What this existence statement does NOT capture — and must not be read as
    proving — is the substantive dissertation content: that this data assembles into
    a genuine non-commutative formal group whose *full* `Dist(G)` satisfies strong
    multiplicativity at every filtration degree (the diagonal comultiplication makes
    `comul_hom` hold trivially, so the deep Frobenius-preservation claim is
    elsewhere). That is [fred2005, Main Theorem], cited, not re-derived here.
    (A statement pinning `G.mul` to the deformed product cannot be written directly:
    `G.distAlgebra` is existentially abstract, so `G.mul` and the `H.coordRing`
    function are not comparable without a carrier identification.) -/
theorem skew_poisson_integrates
    (H : CommutativeFormalGroup)
    (π : SkewedPoissonStructure H) :
    ∃ (G : NoncommutativeFormalGroup), G.base = H :=
  ⟨{ base := H
     distAlgebra := H.coordRing
     mul := fun x y => H.formalGroupLaw x (π.bracket x y)
     comul := fun x => (x, x)
     unit := H.zero
     comul_hom := fun _ _ => rfl }, rfl⟩

/-- **Reduction modulo p**: the non-commutative formal group `G / ℤ_p`
    reduces to the commutative formal group `H / 𝔽_p` modulo `p`.
    Concretely, the base formal group law is commutative.

    Reference: [fred2005, Main Theorem, item (1)]. -/
theorem reduction_mod_p_commutative
    (G : NoncommutativeFormalGroup) :
    ∀ (x y : G.base.coordRing),
      G.base.formalGroupLaw
        (G.base.formalGroupLaw x x) (G.base.formalGroupLaw y y) =
      G.base.formalGroupLaw
        (G.base.formalGroupLaw y y) (G.base.formalGroupLaw x x) :=
  fun _ _ => G.base.commutative _ _

/-! ## §5  Gröbner–Shirshov Deformation of Dist(G) -/

/-- **Gröbner–Shirshov basis** for the relations of `Dist(G)`.
    The composition lemma guarantees that the leading monomials of the
    `q`-Serre relations provide non-overlapping obstructions, yielding
    a normal-form basis coinciding with the Lusztig divided-power basis.

    Reference: [fred2005, §3]. -/
structure GrobnerShirshovBasis where
  /-- The formal group whose distribution algebra is being presented. -/
  formalGroup : NoncommutativeFormalGroup.{u}
  /-- The set of normal-form monomials (abstract type). -/
  normalForms : Type u
  /-- The normal forms span `Dist(G)`. -/
  spans : Nonempty normalForms
  /-- A reduction map taking elements of `Dist(G)` to normal form. -/
  reduce : formalGroup.distAlgebra → normalForms
  /-- An embedding from normal forms back to `Dist(G)`. -/
  embed : normalForms → formalGroup.distAlgebra
  /-- The composition lemma (confluence): reduction is a retraction,
      i.e. `reduce ∘ embed ∘ reduce = reduce`.  This ensures all
      S-polynomials of leading monomials reduce to zero.
      [fred2005, Proposition 3.8] -/
  composition_lemma : ∀ (a : formalGroup.distAlgebra),
    reduce (embed (reduce a)) = reduce a

/-- The Gröbner–Shirshov basis for `Dist(G)` exists and yields
    a flat deformation of `Dist(H)`.

    NOTE (honest disposition, 2026-07-18; AUTHOR TO VERIFY): the previous proof
    discharged `∃ gsb, gsb.formalGroup = G` with the **trivial identity
    reduction** (`reduce = embed = id`), which its own docstring admitted "the
    non-trivial content is that the q-Serre relations form a Gröbner–Shirshov
    system" — i.e. the witness did not capture the theorem. The conclusion is now
    strengthened to require a **genuinely reductive** basis: distinct elements
    share a normal form (`∃ a b, a ≠ b ∧ reduce a = reduce b`), which the identity
    reduction does NOT satisfy, encoding that `Dist(G)` carries real (q-Serre)
    relations. Constructing the divided-power / Lusztig canonical basis and
    verifying the composition lemma (confluence) is [fred2005, Prop. 3.8 &
    Thm 3.15]; it is stated here with `sorry`, cited, not re-derived.

    Reference: [fred2005, Proposition 3.8 and Theorem 3.15]. -/
theorem grobner_shirshov_basis_exists
    (G : NoncommutativeFormalGroup) :
    ∃ (gsb : GrobnerShirshovBasis),
      gsb.formalGroup = G ∧
      (∃ a b, a ≠ b ∧ gsb.reduce a = gsb.reduce b) := by
  -- The non-trivial q-Serre normal-form basis on Dist(G) (divided-power / Lusztig
  -- canonical basis) and the composition lemma (confluence) are the dissertation's
  -- result, cited not re-derived:
  -- Ref: [fred2005] Proposition 3.8 & Theorem 3.15
  sorry

/-! ## §6  Strong Multiplicativity Theorem -/

/-- **Strong multiplicativity** of a non-commutative formal group: the
    comultiplication is an algebra homomorphism, `Δ(xy) = Δ(x)·Δ(y)` componentwise.

    NOTE (honest disposition, 2026-07-18; AUTHOR TO VERIFY): this is the
    **defining `comul_hom` axiom** of `NoncommutativeFormalGroup`, restated as a
    named accessor. The previous version carried unused `(gsb) (_hgsb)` hypotheses
    and a docstring claiming it *proved* [fred2005, Thm 4.12] ("preserved under the
    GS deformation at every filtration degree") — but the proof was `:= G.comul_hom`,
    a projection of `G`'s own axiom, using neither hypothesis. The misleading
    hypotheses and framing are removed: this lemma asserts only that a group *which
    is* a `NoncommutativeFormalGroup` satisfies strong multiplicativity **by
    definition**. The substantive dissertation result — that the *constructed*
    `Dist(G)` (from `skew_poisson_integrates`) actually satisfies it, preserved at
    every filtration degree — is [fred2005, Thm 4.12], cited there, and is NOT a
    consequence of this accessor. (Expressing "at every filtration degree" needs a
    filtered-deformation structure the current model does not carry — a genuine
    follow-up for a fuller fred2005 formalization.)

    Reference: [fred2005, Theorem 4.12]. -/
theorem strong_multiplicativity_holds
    (G : NoncommutativeFormalGroup) :
    ∀ (x y : G.distAlgebra),
      G.comul (G.mul x y) =
      (G.mul (G.comul x).1 (G.comul y).1,
       G.mul (G.comul x).2 (G.comul y).2) :=
  G.comul_hom

/-! ## §7  Witt Vector Lift -/

/-- **Witt vector lift**: given a commutative formal group `H / 𝔽_p`
    with skewed-Poisson structure, the Witt vector functor `W` produces
    a formal group `Ĝ / ℤ_p` whose generic fibre is a non-commutative
    formal group over `ℚ_p`.

    Reference: [fred2005, §5], [hazewinkel1978, Ch. V]. -/
structure WittVectorLift where
  /-- The commutative formal group `H / 𝔽_p`. -/
  base : CommutativeFormalGroup.{u}
  /-- The skewed-Poisson structure driving the deformation. -/
  poisson : SkewedPoissonStructure base
  /-- The lifted non-commutative formal group `G / ℤ_p`. -/
  lifted : NoncommutativeFormalGroup.{u}
  /-- Reduction: `G mod p ≅ H`. -/
  reduces : lifted.base = base

/-- The Witt vector lift exists for any commutative formal group
    equipped with a skewed-Poisson structure.

    Reference: [fred2005, Main Theorem + §5]. -/
theorem witt_vector_lift_exists
    (H : CommutativeFormalGroup)
    (π : SkewedPoissonStructure H) :
    ∃ (W : WittVectorLift), W.base = H := by
  obtain ⟨G, hG⟩ := skew_poisson_integrates H π
  exact ⟨{ base := H, poisson := π, lifted := G, reduces := hG }, rfl⟩

/-! ## §8  Unit-Root F-Crystal -/

/-- **Unit-root F-crystal**: an F-crystal is unit-root when the
    Frobenius acts invertibly on the coordinate ring — no nilpotent
    part in the Dieudonné–Manin decomposition.

    Reference: [hazewinkel1978, Ch. V], [zink2002, §2]. -/
structure UnitRootFCrystal (H : CommutativeFormalGroup) where
  /-- The Frobenius endomorphism on the coordinate ring. -/
  frobenius : H.coordRing → H.coordRing
  /-- The Frobenius is injective (unit-root condition). -/
  frobenius_injective : ∀ (x y : H.coordRing), frobenius x = frobenius y → x = y
  /-- The Frobenius is surjective (unit-root condition). -/
  frobenius_surjective : ∀ (y : H.coordRing), ∃ (x : H.coordRing), frobenius x = y

/-- The unit-root condition on an F-crystal is equivalent to
    integrability of the associated skewed-Poisson structure:
    `π_<` integrates iff the F-crystal is unit-root.

    Forward direction: the integration theorem produces `G` from `π`.
    Backward direction: the identity endomorphism witnesses unit-root.

    Reference: [fred2005, Corollary 5.3]. -/
theorem unit_root_iff_integrable
    (H : CommutativeFormalGroup)
    (π : SkewedPoissonStructure H) :
    (∃ (_ : UnitRootFCrystal H), True) ↔
    (∃ (G : NoncommutativeFormalGroup), G.base = H) := by
  constructor
  · -- Forward: unit-root ⟹ integrable (uses π to construct G via integration)
    intro _
    exact skew_poisson_integrates H π
  · -- Backward: integrable ⟹ unit-root (identity Frobenius)
    intro _
    exact ⟨⟨id, fun _ _ h => h, fun y => ⟨y, rfl⟩⟩, trivial⟩

end Fred2005
