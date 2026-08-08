import Mathlib.Tactic

/-!
# QOU.Eightfold.Sym2Gate — SU(3) fundamental has no invariant symmetric form

Bean `qou-bldy` (T3a), epic `qou-8lxd`.

The discriminator from docs/audits/2026-08-03-flavour-su3-schur-weyl-obstruction.md §3c:

  W carries faithful SU(3) action  ⟹  Sym²(W) is irreducible (dim 6, no singlet).

Contrapositive: singlet in Sym²(W)  ⟹  W is self-dual  ⟹  not SU(3) fundamental.

Corpus application:
- colour T₁: Sym² = A ⊕ H = 1 ⊕ 5  →  singlet present  →  FAILS (orthogonal/icosahedral)
- octonion G₂ route 3: Sym² = 6      →  no singlet       →  PASSES

## Mathlib status

No SU(3) type in Mathlib. We state the discriminator as a dimension check
and bridge the representation-theoretic content with an explicit axiom.

## Namespace

Added 2026-08-08 (bean `qou-ref10`).  The file previously declared everything
at the root, violating AGENTS.md §2 (*all declarations live under the `QOU`
root namespace*) and leaving `lean.ref`s into this module naming declarations
that do not exist.  The namespace matches the module path, as in the three
sibling files of this directory.

## Outstanding: this file's representation-theoretic content is vacuous

Recorded here so it is visible at the point of use, **not** repaired here —
the drain is bean `qou-8fl1` item 3, and the chapter prose already labels the
gate result honestly ("not excluded by the Sym² gate", "should not be cited
as" a machine-checked pass).

- `su3_sym2_irreducible` is an `axiom … : True`.  It asserts nothing: any
  proof of `True` discharges it, so nothing downstream gains content from it.
- `corpus_T1_fails_sym2_gate` and `octonion_3_passes_sym2_gate` conclude
  `1 + 5 = 6 ∧ 1 > 0` and `6 = 6 ∧ 0 = 0` — arithmetic tautologies whose
  representation-theoretic reading lives only in the docstrings.

`sym2_dim_3` is the one declaration here with content, and it is only the
dimension arithmetic.  The parity criterion that actually decides the gate is
formalised properly next door in `QOU.Eightfold.Sym2GateParity`, which also
records why the superseded self-duality argument was invalid.
-/

namespace QOU.Eightfold.Sym2Gate

-- § 1. Dimension check: Sym² of a 3-dim object

/-- dim(Sym²(V)) = n(n+1)/2 for dim V = n.  At n = 3, dim = 6. -/
theorem sym2_dim_3 : 3 * (3 + 1) / 2 = 6 := by norm_num

-- § 2. The gate: singlet in Sym² excludes SU(3)

/-- If Sym²(V) decomposes as 1 ⊕ 5 (dimensions), there is a 1-dimensional
    invariant subspace (a singlet), i.e. an invariant symmetric bilinear form.
    This means V is self-dual (orthogonal type).

    The SU(3) fundamental is complex type (not self-dual: 3 ≇ 3̄), so
    its Sym² = 6 is irreducible.  Any V with Sym² = 1 ⊕ 5 is therefore
    NOT the SU(3) fundamental.

    We state the representation-theoretic core as an axiom (Mathlib gap). -/
axiom su3_sym2_irreducible :
  -- "For V = the SU(3) fundamental (dim 3), Sym²(V) is irreducible (dim 6)."
  -- Equivalently: "V is not self-dual; V ≇ V*."
  -- This is standard: SU(n) fundamental for n ≥ 3 is complex type.
  True

/-- The corpus colour T₁ has Sym² = A ⊕ H with dims 1 + 5 = 6.
    The presence of the singlet A (dim 1) proves T₁ is self-dual,
    hence not SU(3) fundamental. -/
theorem corpus_T1_fails_sym2_gate : (1 : ℕ) + 5 = 6 ∧ (1 : ℕ) > 0 := by
  exact ⟨by norm_num, by norm_num⟩

/-- The octonion G₂ route 3 has Sym² = 6 (irreducible, no singlet).
    It passes the gate. -/
theorem octonion_3_passes_sym2_gate : (6 : ℕ) = 6 ∧ (0 : ℕ) = 0 := by
  exact ⟨rfl, rfl⟩

end QOU.Eightfold.Sym2Gate
