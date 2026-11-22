import QOU.Archimedean.BorromeanVolumeCatalan

/-!
# `conj:poincare-lefschetz-borromean` — a cited-hypothesis class, not a `Prop` stub

Sibling for content block
[`conj:poincare-lefschetz-borromean`](poincare-lefschetz-borromean.md).

## What this file used to be, and why that was wrong

It read, in its entirety:

```lean
class PoincareLefschetzBorromean where
  holds : Prop
```

`⟨True⟩` inhabits that, so a downstream `[PoincareLefschetzBorromean]`-conditional
theorem proved nothing modulo the conjecture, and the carrier recorded only that
*someone intends a proposition to go here*. It is the `holds : Prop` variant of
`proof-claims-unencoded` (AGENTS.md §3b-tax; bean `qou-hprp`), and it passes every
detector that looks for a `sorry`, an `axiom`, or a `: True` conclusion, because it
contains none of them.

## Why a *hypothesis* class rather than a conjecture carrier

Most of what the block states is **classical**, not conjectural:

* Poincaré–Lefschetz duality `H^k(M, ∂M) ≅ H_{3-k}(M)` is a theorem of algebraic
  topology, not a claim of this framework;
* `H₁(S³ ∖ 𝓑₃) ≅ ℤ³` for a 3-component link complement is standard.

Encoding either as a "conjecture" would misreport settled mathematics as open. So
they enter as **named, cited hypotheses** — the `IsWeilZeta` pattern
(`QOU/AlgebraicSubstrate/WeilZeta.lean`), where the classical inputs an argument
consumes are recorded as class fields with their references, and the corpus proves
only its own step.

The framework's actual claim is the third field: that the top-degree
Poincaré–Lefschetz pairing — volume form against fundamental class — evaluates to
`Vol(𝓑₃)`.

## What is NOT formalised here, stated rather than implied

- **No manifold theory.** The block's own "What remains open" item 3 says closing
  this needs a Lean class for manifold-with-cusps Poincaré–Lefschetz, which Mathlib
  supports only partially. Nothing here builds one. The datum below records the
  *ranks* the block consumes, abstractly, and the duality field is stated at the
  level of ranks — which is the level at which the block uses it ("in particular
  `H²(∂𝓑₃) ≅ H₁ ≅ ℤ³`").
- **No proof that the pairing is `8G`.** `pairing_eq_vol` is a hypothesis. It is the
  conjecture.
- **No connection to the Bloch-group route.** The block's cross-reference to
  `conj:borromean-bloch-group-element` — that the regulator `r₂[𝓑₃]` and this
  pairing are the same number by two different dualities — is not stated here.
  Nothing in this file relates the two.
- **`borromeanHomologyModel` is a consistency witness, not the Borromean
  complement.** It is *constructed* to satisfy the three fields, exactly as
  `weilZetaExample` is constructed to satisfy `IsWeilZeta`. That the axioms are
  jointly satisfiable is all it shows; it is deliberately a `def` and its
  satisfaction is a `theorem`, **not an `instance`**, so typeclass resolution can
  never discharge a `[PoincareLefschetzBorromean D]` binder for someone else's `D`.

## References
- [lefschetz1926] Lefschetz, "Intersections and transformations of complexes and
  manifolds" — the duality.
- [neumann-zagier1985] Neumann–Zagier, "Volumes of hyperbolic three-manifolds" —
  the cusped-manifold setting.
- [adams1985hyperbolic] Adams — `Vol(𝓑₃) = 8G`, via `QOU.Archimedean.vol_B3`.
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots

open QOU.Archimedean

/-- The homological data of a cusped 3-manifold that the block consumes.

`rankH k` is the rank of `H_k(M)`, `rankHrel k` the rank of `H^k(M, ∂M)`, and
`plPairing` the value of the top-degree Poincaré–Lefschetz pairing of the volume
form against the fundamental class.

Ranks rather than groups: the block's use of the duality is the rank statement
("in particular `H²(∂𝓑₃) ≅ H₁ ≅ ℤ³`"), and recording groups would require the
manifold-with-cusps machinery the block itself lists as missing. -/
-- Ref: [leitner2026] conj:poincare-lefschetz-borromean
structure BorromeanHomology where
  /-- rank of `H_k(M)`. -/
  rankH : ℕ → ℕ
  /-- rank of `H^k(M, ∂M)`. -/
  rankHrel : ℕ → ℕ
  /-- the top-degree Poincaré–Lefschetz pairing `⟨vol, [M]⟩`. -/
  plPairing : ℝ

/-- **Poincaré–Lefschetz closure on the Borromean complement.**

Two classical hypotheses and one framework claim, over an abstract datum `D`.

* `duality` — Poincaré–Lefschetz: `rank H^k(M, ∂M) = rank H_{3-k}(M)` in degrees
  `k ≤ 3`. Classical; cited, not conjectured.
* `h1_rank` — `H₁(S³ ∖ 𝓑₃) ≅ ℤ³`, the three meridian classes. Standard for a
  3-component link complement; cited, not conjectured.
* `pairing_eq_vol` — **this is the conjecture**: the top pairing is the hyperbolic
  volume `Vol(𝓑₃) = 8G`.

`D` is a parameter, so a `[PoincareLefschetzBorromean D]` binder is a hypothesis
about the caller's datum rather than about one the instance chose. No instance is
supplied for any datum other than the consistency witness below. -/
-- Ref: [lefschetz1926] Lefschetz, "Intersections and transformations of complexes and manifolds"
-- Ref: [neumann-zagier1985] Neumann, Zagier, "Volumes of hyperbolic three-manifolds"
-- Ref: [leitner2026] conj:poincare-lefschetz-borromean
class PoincareLefschetzBorromean (D : BorromeanHomology) : Prop where
  /-- Poincaré–Lefschetz duality, at the level of ranks. -/
  duality : ∀ k, k ≤ 3 → D.rankHrel k = D.rankH (3 - k)
  /-- `H₁ ≅ ℤ³` — three meridian classes, one per Borromean component. -/
  h1_rank : D.rankH 1 = 3
  /-- The top Poincaré–Lefschetz pairing is the hyperbolic volume. -/
  pairing_eq_vol : D.plPairing = vol_B3

/-- The block's "in particular": `H²(M, ∂M)` has rank 3, matching `H₁`.

**Derived**, and this is the point of the re-encoding — it is none of the three
fields, and it needs two of them. The previous carrier could not state it, because
it stated nothing. -/
theorem rankHrel_two_eq_three (D : BorromeanHomology)
    [h : PoincareLefschetzBorromean D] :
    D.rankHrel 2 = 3 := by
  have hd := h.duality 2 (by norm_num)
  have : (3 : ℕ) - 2 = 1 := by norm_num
  rw [hd, this, h.h1_rank]

/-- The pairing is `8G`. -/
theorem plPairing_eq_eight_catalan (D : BorromeanHomology)
    [h : PoincareLefschetzBorromean D] :
    D.plPairing = 8 * catalan_G := by
  rw [h.pairing_eq_vol, vol_B3_eq_8_catalan]

/-- The pairing is strictly positive — a real consequence, not a restatement:
it follows from the conjectural field together with a *proved* fact about
Catalan's constant, and would fail for a datum whose pairing were `0`. -/
theorem plPairing_pos (D : BorromeanHomology)
    [h : PoincareLefschetzBorromean D] :
    0 < D.plPairing := by
  rw [h.pairing_eq_vol]
  exact vol_B3_pos_via_catalan

/-- Betti numbers of a 3-component link complement in `S³`:
`b₀ = 1`, `b₁ = 3`, `b₂ = 2`, `b_k = 0` above. -/
def bettiB3 : ℕ → ℕ
  | 0 => 1
  | 1 => 3
  | 2 => 2
  | _ => 0

/-- A datum satisfying all three fields, so the class is not an empty carrier.

Constructed to satisfy them — `rankHrel` is *defined* as the dual of `rankH`, and
`plPairing` is *defined* as `vol_B3`. It therefore shows consistency and nothing
more; it is not a model of the Borromean complement and asserts nothing about it. -/
noncomputable def borromeanHomologyModel : BorromeanHomology where
  rankH := bettiB3
  rankHrel := fun k => bettiB3 (3 - k)
  plPairing := vol_B3

/-- The three fields are jointly satisfiable.

A `theorem`, deliberately **not** an `instance`: as an instance it would be found
by resolution only for this datum, but making it one invites the next reader to add
`instance` to a datum that is *not* constructed to satisfy the fields. Cf. the
`trivialSkeinGenerationContext` note in `QOU/Torsion/skein_generation.lean`. -/
theorem borromeanHomologyModel_satisfies :
    PoincareLefschetzBorromean borromeanHomologyModel where
  duality := fun _ _ => rfl
  h1_rank := rfl
  pairing_eq_vol := rfl

/-- The fields **discriminate**: a datum with `b₁ = 2` is not a Poincaré–Lefschetz
Borromean datum.

Without this, "the class is satisfiable" is compatible with the class being
satisfied by everything, which is the failure mode the empty carrier had. -/
theorem not_poincareLefschetz_of_h1_rank_two
    (D : BorromeanHomology) (h2 : D.rankH 1 = 2) :
    ¬ PoincareLefschetzBorromean D := by
  intro h
  have := h.h1_rank
  rw [h2] at this
  exact absurd this (by norm_num)

end QOU.BraidsAndKnots
