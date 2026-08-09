# Tautology drain: 12 adjudicated genuine, 5 fixed — and a stale-olean trap

**Date:** 2026-08-09
**Branch:** `claude/issue-2472-analysis-qgqk7u`
**Scope:** `groebner-shirshov-energy.lean`, `SkewSYT.lean`, review ledger

## 1. All 12 `reflexive-tautology-ascribed-literal` candidates are genuine

Every one has the shape `theorem X : (n : T) = n := rfl` under a docstring or
name asserting real content. This is the exact shape banned by Strict Lean
Discipline §5, and the opposite outcome from the `proof-no-false-premise`
sweep (0-for-56, [narrowed separately](2026-08-09-false-premise-criterion-narrowed.md)) —
worth stating plainly, because it shows the vacuity criteria are not uniformly
noisy. This one is carrying real signal.

| decl | asserts | proves |
|---|---|---|
| `colour_sector_count` | 3 colour sectors | `3 = 3` |
| `exactly_two_one_dim_irreps` | H₂ has exactly two 1-dim irreps | `2 = 2` |
| `degree_zero_dim_one` | degree-0 subspace has dimension 1 | `1 = 1` |
| `kahler_differentials_no_sym_component` | `dim Ω¹(A)₀ = 0` | `0 = 0` |
| `meson_squaring_exponent` | exponent = number of quark constituents | `2 = 2` |
| `branch_31_to_3` / `_21` / `_111` | branching multiplicities 1, 1, 0 | `1 = 1`, `1 = 1`, `0 = 0` |
| `yangBaxter_energy_zero` / `farComm_energy_zero` | those steps cost no energy | `0 = 0` |
| `delta_max_numerical_scale`, `plancherel_via_recipe` | a bound / a Plancherel identity | `1 = 1` via `ctx.holds` |

The last two are doubly vacuous: a self-assuming projection whose conclusion is
*also* a tautology, so they assert nothing with or without an instance.

Several carry their real argument in a comment. `kahler_differentials_no_sym_component`
spells out the whole derivation — symmetric channel sees `σ_i → q`, restricted
multiplication kernel is trivial — and then concludes `(0 : ℕ) = 0 := rfl`.
The reasoning is present; none of it is in the Lean.

## 2. Five fixed, `lean`-direct verified

**`groebner-shirshov-energy.lean`** — the file had no per-step energy function
at all, only `heckeEnergyChange`. Added `stepEnergyChange`, which is the
per-step form of the `.hecke`-only filter its own `energy_path_independent`
axiom already writes inline. The two theorems now state
`stepEnergyChange q coeff step = 0` under their step hypothesis, so `h` is
load-bearing — Lean's `unusedVariables` linter had been flagging both, which is
independent corroboration of the audit. Added
`stepEnergyChange_hecke_ne_zero` proving the remaining constructor *does* move
energy, so the two results are demonstrably non-vacuous.

**`SkewSYT.lean`** — `branchingMult` already existed, but `skewSYTCount` is
`noncomputable` well-founded recursion, so `decide` cannot reduce it. What is
decidable is the skew shape itself, which is exactly what the comments claim
("one cell at (1,0)"):

- `skewCells_31_3 : skewCells p31 p3 = {⟨1,0⟩}` — proved
- `skewCells_31_21 : skewCells p31 p21 = {⟨0,2⟩}` — proved
- `branch_31_to_111 : branchingMult p31 p111 = 0` — proved via `dif_neg` on
  non-containment

**Not claimed:** `branchingMult p31 p3 = 1` and `branchingMult p31 p21 = 1`.
Those need the well-founded recursion unfolded (`dif_neg` on the size guard,
`skewCorners` computed, the `Finset.attach` sum reduced, base case at
`size ≤ size`). Tractable, not done — filed rather than asserted.

Verification: `lean`-direct exit 0 on both files; `#print axioms` on all six new
declarations shows `[propext, Classical.choice, Quot.sound]` only — no
`sorryAx`, and no dependence on either file's own `axiom` declarations.

Non-exempt scanner candidates 64 → 57; ledger 148 → 141.

## 3. Stale oleans fake "unknown identifier" errors — check before reporting

`SkewSYT.lean` first came back **red**: two `unknown identifier` errors for
`QOU.MathlibExt.sum_insertionSort_eq` and `sum_eq_finsetSum_getD`. Both lemmas
exist in `QOU/MathlibExt.lean`, and `SkewSYT.lean` imports `QOU.MathlibExt`.

The cause was the **restored olean cache**: `QOU/MathlibExt.olean` was dated
Jun 9, while the source had been modified Aug 9. `lean`-direct read the stale
olean, which predates both lemmas. Rebuilding just that one module into a
scratch lib and prepending it to `LEAN_PATH` took **3.7 s** and turned the file
green:

```bash
SCRATCH=/tmp/.../freshlib && mkdir -p $SCRATCH/QOU
env LEAN_PATH="$SCRATCH:$LP" lean -D autoImplicit=false \
  --root=content/quantum-observable-universe/lean \
  -o $SCRATCH/QOU/MathlibExt.olean \
  content/quantum-observable-universe/lean/QOU/MathlibExt.lean
env LEAN_PATH="$SCRATCH:$LP" lean -D autoImplicit=false <target>.lean
```

This is a live trap for the `lean`-direct recipe, which the environment-setup
skill presents as read-only against the restored cache. An `unknown identifier`
for a name you can grep in the tree is almost always a stale olean, not a
corpus defect. **Compare `stat` on the source against its olean before reporting
a compile failure** — reporting that one as broken would have been a fabricated
defect in a file that is in fact clean.
