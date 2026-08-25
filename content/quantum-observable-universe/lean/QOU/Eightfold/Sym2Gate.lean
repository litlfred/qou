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

No SU(3) type in Mathlib. We state the discriminator as a **dimension shadow**
— the Sym² dimension and the singlet count that decides the gate. The
representation-theoretic core (the SU(3) fundamental is complex type,
`𝟑 ≇ 𝟑̄`, so `Sym²(𝟑) = 𝟔` is irreducible with no singlet) is a genuine
Mathlib gap, tracked in bean `qou-8fl1` (T2). It is **not** stubbed here with a
vacuous `axiom … : True`: an earlier `su3_sym2_irreducible : True` was removed
2026-08-23 (it asserted nothing and nothing consumed it). The affirmative
gate-decision content is carried by the parity criterion proved next door in
`QOU.Eightfold.Sym2GateParity`.

## Namespace

Added 2026-08-08 (bean `qou-ref10`).  The file previously declared everything
at the root, violating AGENTS.md §2 (*all declarations live under the `QOU`
root namespace*) and leaving `lean.ref`s into this module naming declarations
that do not exist.  The namespace matches the module path, as in the three
sibling files of this directory.

## What is (and is not) proved here

`sym2_dim_3`, `corpus_T1_fails_sym2_gate` and `octonion_3_passes_sym2_gate` are
**dimension shadows**: the Sym²(3-dim object) dimension is `6`, and the gate is
decided by the singlet count (fail iff a singlet is present, i.e. count `≥ 1`).
T₁ carries singlet count `1` (fails); the octonion route carries singlet count
`0` (passes). What these do **not** prove is the SU(3) irreducibility that makes
the octonion route's singlet count `0` — that is the Mathlib gap above
(`qou-8fl1` T2). The parity criterion that actually decides the gate is
formalised in `QOU.Eightfold.Sym2GateParity`, which also records why the
superseded self-duality argument was invalid.
-/

namespace QOU.Eightfold.Sym2Gate

-- § 1. Dimension check: Sym² of a 3-dim object

/-- dim(Sym²(V)) = n(n+1)/2 for dim V = n.  At n = 3, dim = 6. -/
theorem sym2_dim_3 : 3 * (3 + 1) / 2 = 6 := by norm_num

-- § 2. The gate: singlet in Sym² excludes SU(3).
--
-- The representation-theoretic core — "the SU(3) fundamental is complex type
-- (3 ≇ 3̄), so Sym²(𝟑) = 𝟔 is irreducible with no singlet" — is a Mathlib gap
-- (no SU(3) type). It was previously stubbed as `axiom su3_sym2_irreducible :
-- True`, which asserted nothing; removed 2026-08-23 (bean qou-8fl1 T2). The two
-- gate applications below are honest dimension shadows: the Sym² dimension is 6,
-- and the gate is decided by the singlet count (fail iff ≥ 1).

/-- The corpus colour T₁ has Sym² = A ⊕ H with dims 1 + 5 = 6.  The singlet A
    has dimension 1, so its singlet count `1 ≥ 1`: T₁ **fails** the gate (self-
    dual / orthogonal type, not the SU(3) fundamental).  Dimension shadow. -/
theorem corpus_T1_fails_sym2_gate : (1 : ℕ) + 5 = 6 ∧ (1 : ℕ) ≥ 1 := by
  exact ⟨by norm_num, by norm_num⟩

/-- The octonion G₂ route 3 has Sym²(𝟑) = 6 with **no** singlet, so its singlet
    count `0 < 1`: it **passes** the gate.  Dimension shadow, parallel to
    `corpus_T1_fails_sym2_gate` — the Sym² dimension `3·4/2 = 6` is real
    (`sym2_dim_3`); the singlet count `0` is the SU(3)-irreducibility input that
    remains the Mathlib gap (bean `qou-8fl1` T2). -/
theorem octonion_3_passes_sym2_gate : 3 * (3 + 1) / 2 = 6 ∧ (0 : ℕ) < 1 := by
  exact ⟨by norm_num, by norm_num⟩

end QOU.Eightfold.Sym2Gate
