# lean-verifier — v4.24.0 names, module moves and notation tokens

Read when a file fails on an **unknown identifier / unknown constant**, or on
`object file … does not exist` for a module you believe exists.

> **The discriminator, every time: grep the mathlib SOURCE tree.**
> `.lake/packages/mathlib/Mathlib/…` is present in full even when the olean
> cache is partial. A `.lean` that is absent from the source tree is a **rename
> or move** (fix the import); a `.lean` that is present with no olean is a
> **cache gap** (fix the cache). The two symptoms are byte-identical at the
> error line and lead to opposite actions.

Every fix below is mechanical and statement-preserving — no witness, no
proposition and no tactic block changes.

## Module moves

| written | actual in v4.24.0 | seen |
|---|---|---|
| `Mathlib.Data.Matrix.Notation` | `Mathlib.LinearAlgebra.Matrix.Notation` (`!![a,b;c,d]`) | 2026-08-29 |
| `Mathlib.Data.Matrix.Kronecker` | `Mathlib.LinearAlgebra.Matrix.Kronecker` (`⊗ₖ`, `open scoped Kronecker`, `mul_kronecker_mul`, `trace_kronecker`, `one_kronecker_one`) | 2026-08-31 |
| `Mathlib.Algebra.BigOperators.Ring` | **not a module** — a directory with no aggregator. `Finset.mul_sum` is in `…Ring.Finset` | 2026-08-31 |

So: `object file …` for a `Data.Matrix.*` import in v4.24.0 → check the source
tree. Several `Data.Matrix` modules moved to `LinearAlgebra.Matrix`. For
`BigOperators/Ring`, zero mathlib files import the bare path — that is the tell.

## Renames and deprecated aliases

| written | actual | note |
|---|---|---|
| `pow_le_pow_left` (from `Mathlib.Algebra.Order.Ring.Pow`, which also carries `one_add_mul_le_pow`) | `pow_le_pow_left₀` (`Algebra/Order/GroupWithZero/Unbundled/Basic.lean:449`) | 2026-09-04. **Prefer `gcongr`** — it discharged the goal from hypotheses already in context and does not move when a lemma is renamed |
| `Matrix.dotProduct` | root-namespace `dotProduct` (`Data/Matrix/Mul.lean:66`) | prints `Unknown constant` once per `fin_cases` branch, and the simp set silently loses the unfold |
| `Matrix.smul_mulVec_assoc` | deprecated alias (2025-08-14) of `Matrix.smul_mulVec`, identical statement | |
| `Finset.sum_powerset_card` | **does not exist**. Use `Finset.sum_powerset s f` (additive of `prod_powerset`, `Algebra/BigOperators/Group/Finset/Powerset.lean`): `∑ t∈powerset s = ∑ j∈range(#s+1), ∑ t∈powersetCard j s`, then `Finset.card_univ` | 2026-09-02 |

## Notation tokens and elaboration

- **`₊`/`₋` (U+208A/U+208B) are notation tokens** under a full
  `import Mathlib.Tactic` (PosPart etc.), so a binder named `ρ₊` fails to lex:
  `unexpected token '₊'; expected ','`. Rename the binder (`ρ₊`→`ρp`) — pure
  alpha-renaming. Fine in comments and docstrings, never in identifiers.
- **A `def` of a `Matrix _ _ ℂ` built with `*` must be `noncomputable`** —
  `Finset.sum` over ℂ hits `Complex.instNormedAddCommGroup`, which has no
  executable code. `!![…]` literals and `•`/`+` alone did not need it; `*` did.
- **`Complex.I ^ 2` is created by `ring_nf`, not by `simp`.** After `simp` the
  `I`s sit as `n₂ * I * (n₂ * I)`, so `Complex.I_mul_I` *and* `Complex.I_sq`
  both report "unused" and `ring` fails with `I ^ 2` in the goal. Working chain:
  `simp [...] <;> ring_nf <;> simp [Complex.I_sq] <;> ring`. **Do not obey the
  `unnecessarySeqFocus` linter here** — rewriting the tail as
  `(simp [Complex.I_sq]; ring)` fails `No goals to be solved`, because `simp`
  closes some branches outright. Keep `<;>`; the lint is cosmetic.
- `vecHead (vecTail …)` residue after `!![…]`/`![…]` simp: add
  `Matrix.vecHead, Matrix.vecTail` to the simp set.
- An `rw [esymm]`-style rewrite **under a binder** cannot fire. Do it after
  `intro`.

## File-shape rules Lean enforces

- **`/-!` module doc must come after the imports.** Lean rejects any `import`
  following a module doc. A docstring before the import block is a hard error.
- **`omit [inst] in` precedes the docstring**, not the other way round.

## Source files these were measured on

`QOU/MassTheory/MagnusPairingSignStructure.lean` (2026-08-29),
`QOU/MassTheory/MagnusOmega2LocalDecomposition.lean` (2026-08-31),
`QOU/MassTheory/QuantumTraceTower.lean` (2026-08-31),
`QOU/MassTheory/MagnusHookExteriorPower.lean` (2026-09-02),
`QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean` (2026-09-03),
`QOU/Hecke/BindingExtensivity.lean` (2026-09-04).
