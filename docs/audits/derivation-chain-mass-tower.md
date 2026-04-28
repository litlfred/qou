# Derivation chain to the mass-tower endomorphism — Lean audit

Per repo-owner direction: the mass-tower endomorphism is **not yet
fully determined / computable**. To make it computable we need to
trace the full chain of derivations (from foundational structures
to the endomorphism) step by step, marking each link's Lean status
honestly.

**Scope.** Only Lean files on `main` as of `0717c94b7` (HEAD of the
consolidated workplan branch). All paths relative to repo root.

## Chain

```
Hecke crossing energy
  → categorical (cyclic) action on hadron sheaves
    → Frobenius pairing (existence + uniqueness)
      → non-abelian Stokes (motivic-Galois descent)
        → Wedderburn block decomposition
          → Schur-Weyl (multiplicity / character)
            → finite Jones tower (transition operators)
              → mass-tower endomorphism
```

Each link below is annotated with: file, sorry count, axiom/class
count, and the next concrete proof gap.

---

### 1. Hecke crossing energy

**File:** `content/quantum-observable-universe/braids-and-knots/crossing-energy.lean`
**Status:** ✅ 0 sorrys, 0 axioms.
- `CrossingEnergy.decomposition` proved (`field_simp; ring`).
- Working over `R_q = ℤ[q, q⁻¹]` (Laurent polynomials), so positivity
  / archimedean predicates are deliberately commented out.
- **Gap to close:** none here; this link is solid.

### 2. Categorical action on hadron sheaves

**Files:**
- `content/quantum-observable-universe/quantum-observable-universes/categorical-action.lean` — ✅ 0 sorrys
- `categorical-action-exists.lean` — ⚠️ 1 sorry (existence assertion)
- `categorical-action-unique.lean` — ⚠️ 1 sorry (uniqueness assertion)

The two sorries depend on category-theoretic infrastructure not yet
in `QOU.Basic` (per the file headers). This is a **structural**
gap: the statements as written assert existence/uniqueness on any
monoidal category C, but the witness requires more structure on C.

- **Gap to close:** restate with hypothesis "C carries QOU
  Frobenius-Hopf data", then existence/uniqueness become trivial
  destructors. Out of scope for a single proof-closure session.

### 3. Frobenius pairing — existence + uniqueness

**Files:**
- `content/quantum-observable-universe/quantum-universes/frobenius-pairing.lean` — ✅ 0 sorrys
- `frobenius-pairing-exists.lean` — ⚠️ 1 sorry (`Nonempty (FrobeniusHopfData C)` for arbitrary C)
- `frobenius-pairing-unique.lean` — ⚠️ 1 sorry (`Subsingleton (FrobeniusHopfData C)` for arbitrary C)
- `frobenius-relation.lean` — ✅ 0 sorrys
- `frobenius-su2.lean` — ✅ 0 sorrys

**Substrate side:**
- `content/.../algebraic-substrate/frobenius-hopf-substrate.lean` — ✅ 0 sorrys

Same structural gap as link 2: the Nonempty/Subsingleton claims
are too strong for arbitrary C. They need restatement with a
"C is a QOU" hypothesis. Same disposition.

### 4. Non-abelian Stokes / motivic-Galois descent

**Files:**
- `content/quantum-observable-universe/lifting-and-descent/motivic-galois-character.lean`
  — axiomatic `class MotivicGaloisCharacter` (CLAUDE.md §3b: `sorry` on
  any field IS the conjecture).
- `motivic-perpetual-obstruction.lean` — class with conditional
  theorems downstream.
- `content/.../algebraic-substrate/motivic-substrate.lean` — class.

These are deliberate **axiomatic classes** documenting the obstruction.
The "concrete realization" is the open work flagged as **GAP 5b** in
`docs/audits/family-4-motivic-path.md`.

- **Gap to close:** write a concrete `instance` for the QOU substrate
  at q_0. Research-grade; needs derivation of the local Frobenius
  eigenvalues from the brane tower (not from cyclotomic guesswork).

### 5. Wedderburn block decomposition

**Files:**
- `content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.lean` — ✅ 0 sorrys
- `wedderburn-bratteli-recursion.lean` — ⚠️ 2 sorrys (recursion
  unfolding for higher Hecke levels)
- `content/.../appendix-atomic-mass-calculations/amc-wedderburn-method.{ts,md}` — narrative, no Lean

The **mass-formula** structural identities are fully proved. The
**recursion** at higher Hecke levels has 2 unproved induction steps.

- **Gap to close (tractable):** `wedderburn-bratteli-recursion`
  inductive step at H_4 / H_5. Needs Bratteli-diagram facts already
  on main but not threaded through the proof; could be closed in
  one focused session.

### 6. Schur-Weyl mass decomposition

**Files:**
- `content/quantum-observable-universe/braids-and-knots/schur-weyl-mass-decomposition.lean` — ⚠️ 2 sorrys, 1 axiom/class
- `shell-schur-weyl-self-duality.lean` — separate proposition

The two sorries in `schur-weyl-mass-decomposition` and the supporting
class form the principal Lean gap **before** the mass-tower endomorphism
becomes computable. Closing them requires either:
- Use of existing Mathlib `RepresentationTheory.SchurWeyl` lemmas (if
  imported); or
- Hand derivation from `Wedderburn` + `MarkovTraceFamilyOneDim`.

- **Gap to close:** principal next target. A real proof here propagates
  to mass-tower endomorphism computability.

### 7. Finite Jones tower (transition operators)

**Files:**
- `content/.../braids-and-knots/hecke-mass-trace.lean` — ✅ 0 sorrys
- `hecke-mass-element.lean` — ✅ 0 sorrys
- `hecke-normal-form.lean` — ✅ 0 sorrys
- `hecke-markov-transition.lean` — ⚠️ 2 sorrys (Markov factorization +
  one structural premise)
- `hecke-convergence-bound.lean` — ✅ **closed in this PR** (0.001·4⁻⁸ < 2·10⁻⁸ via `norm_num`)
- `nucleon-hecke-element.lean` — ✅ 0 sorrys

Of the 2 sorries in `hecke-markov-transition`, one (`markov_chain_factorization_exists`) is **vacuous as stated** — the
hypotheses do not link `totalTrace` to the steps; the theorem
statement itself needs to be tightened before a proof is meaningful.

- **Gap to close:** restate `markov_chain_factorization_exists` with
  a real link from `totalTrace` to the steps (e.g., make `totalTrace`
  a definition rather than a free variable), then induct.

### 8. Mass-tower endomorphism

**File:** `content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.lean`
**Status:** 1 sorry, 1 axiomatic `class MassEvaluation`.

The sorry is in `proton_electron_ratio` and is **conditional on
`MassEvaluation`**. The `MassEvaluation` class axiomatizes
- `V₀, V₁, Ve : ℝ` (Wedderburn-traced volumes)
- positivity / ordering / `< 1` constraints
- `me_pos : 0 < mass q 1 ![Ve]`
- **`ratio_ge : mass q 2 ![V₀, V₁] / mass q 1 ![Ve] ≥ 1836`**

The instance is the heart of "not yet computable": providing it
requires evaluating the quantum dilogarithm `Φ_q` at the specific
witness volumes, which is a numerical / categorical computation
chain that has not yet been written down end-to-end.

- **Gap to close:** construct an explicit `MassEvaluation` instance
  with V₀, V₁, Ve from the canonical chain at q_0. Direct chain:
  Wedderburn block decomposition (link 5) → numerical witness for
  Schur-Weyl trace (link 6) → finite Jones-tower volumes (link 7)
  → instance.

This is the principal "not yet determined" gap the repo owner
flagged.

---

## Smallest tractable gap that propagates

Across the eight links, the gap whose closure has the most leverage
on **mass-tower endomorphism computability** is **link 6**
(`schur-weyl-mass-decomposition.lean`, 2 sorrys + 1 class).

Closing it would unblock concrete construction of `MassEvaluation`
in link 8 by providing a derivation of the Wedderburn-traced volumes
that doesn't go through the axiomatic `MassEvaluation` itself.

## What this PR closed (concrete)

| File | Before | After |
|------|--------|-------|
| `hecke-convergence-bound.lean` | 1 sorry | 0 sorrys (real `norm_num` proof of `0.001·4⁻⁸ < 2·10⁻⁸`) |
| `AlgOps.lean` | 7 sorrys | **1** sorry (5 closed in earlier commits + `mkDegLexOrder.right_compat` closed in this branch; `mkDegLexOrder.wf` deferred — needs Mathlib `Shortlex` API) |

## What this audit does NOT do

- Does **not** claim the chain links 2/3/4/5/6/7/8 are correct as
  stated — several sorries (2, 3) are blocked on **statement
  restatement**, not proof closure.
- Does **not** invent witness values for link 8. Constructing the
  `MassEvaluation` instance is research; the audit just maps which
  upstream pieces are needed.
- Does **not** address jet-order / GB-filtration / spectral
  bookkeeping yet — those are the `prop:joint-tower-sdp-confinement`
  / `prop:atom-knot-mass-derivation` files, audit deferred to a
  separate pass.
