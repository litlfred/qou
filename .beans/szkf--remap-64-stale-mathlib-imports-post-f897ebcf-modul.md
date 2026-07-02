---
# szkf
title: Remap 64 stale Mathlib imports (post-f897ebcf module renames/splits)
status: todo
type: milestone
created_at: 2026-06-30T23:32:53Z
updated_at: 2026-06-30T23:32:53Z
---


## Outcome (this session)

Import remap applied to all 63 siblings (targets validated vs pinned Mathlib.lean).
On verify: **15 pass + 3 neutral-skip = 18 import-only-green** (landed in PR #3191);
**45 surfaced pre-existing breakage** the dead import had masked (parse / unknown-tactic
/ noncomputable / proof-goals) — reverted to main, tracked here as a deep-drain backlog
(fixing only the import does NOT drain them). 1 LIBRARY file (qx79) deferred separately.

### 45 deep-broken siblings to drain (full wave-8-style per-file repair):
```
NONCOMPUT(mech) | braids-and-knots/chi-sym-alt-closed-form.lean
OTHER | braids-and-knots/chi-std-pernucleon-closed-form.lean
OTHER | content/unital-groebner-bases/unital-groebner-bases-chapter/remainder-modules.lean
OTHER | lifting-and-descent/brane-boundary-structure.lean
OTHER | mass-endomorphism/topological-mass-conjecture.lean
OTHER | mass-theory/habiro-expansion-atomic.lean
OTHER | models-of-qous/instanton.lean
OTHER | models-of-qous/irreducible-connection.lean
OTHER | models-of-qous/main-commutative-diagram-proof.lean
OTHER | models-of-qous/q-yang-mills-levi.lean
OTHER | models-of-qous/self-dual-curvature.lean
OTHER | observations/algebraic-gns-embedding.lean
OTHER | predicted-spectra/alpha-em-categorical-trace-ratio.lean
OTHER | predicted-spectra/nuclear-spin-parity.lean
OTHER | quantum-observable-universes/c-quantum-observable-universe.lean
OTHER | quantum-observable-universes/categorical-instanton.lean
OTHER | quantum-observable-universes/categorical-irreducible-proof.lean
OTHER | quantum-observable-universes/categorical-self-duality-proof.lean
OTHER | quantum-observable-universes/fermion-boson-decomposition.lean
OTHER | quantum-observable-universes/q-hodge-star.lean
OTHER | quantum-observable-universes/quantum-gauge-group.lean
OTHER | quantum-observable-universes/quantum-observable-universe.lean
OTHER | quantum-observable-universes/rigid-dualizing-complex.lean
OTHER | quantum-observable-universes/spin-labels.lean
OTHER | quantum-universes/categorical-connection.lean
OTHER | quantum-universes/higher-forms.lean
OTHER | quantum-universes/quantum-universe.lean
PARSE(mech) | braids-and-knots/skein-resolution-obstruction.lean
PARSE(mech) | information-theory/computational-horizon.lean
PARSE(mech) | lifting-and-descent/quantum-dilogarithm.lean
PARSE(mech) | mass-theory/skein-generation.lean
PARSE(mech) | particle-interactions/confinement-grading-correspondence-conditional.lean
PARSE(mech) | quantum-observable-universes/q-codifferential-formula-prop.lean
PROOF(LSP) | braids-and-knots/frobenius-lepton-meson-bridge.lean
PROOF(LSP) | lifting-and-descent/descent-lemma.lean
PROOF(LSP) | mass-endomorphism/atomic-mass-gb-nf.lean
PROOF(LSP) | mass-endomorphism/categorical-mass-markov.lean
PROOF(LSP) | mass-theory/full-pole-structure-mass-trace.lean
PROOF(LSP) | observations/trace-ratio-observable.lean
PROOF(LSP) | particle-interactions/c-equals-bar-iff-all-1dim.lean
TACTIC(mech) | mass-theory/he4-channel-active-set.lean
TACTIC(mech) | mass-theory/hecke-markov-transition.lean
TACTIC(mech) | particle-interactions/bar-involution-invariance.lean
TACTIC(mech) | particle-interactions/hyperelliptic-z5-classification.lean
TACTIC(mech) | particle-interactions/periodic-table-demand-conjecture.lean
```

Classes: PARSE/TACTIC/NONCOMPUT = mechanical (no LSP); PROOF = needs LSP goal inspection
(blocked in the web sandbox — lean-lsp MCP can't resolve the toolchain). Remap map:
/tmp/remap.sed in-session; reproduce via the codeload mathlib source at f897ebcf.

## Wave-2 progress (2026-07-02, PR #3202, branch claude/stale-mathlib-imports-9xzeul)

Remap checkpoint cherry-picked from claude/stale-import-deep-drain-2026-07-01.
**12/12 mechanical drained** (lean-direct exit 0 each): periodic-table-demand-conjecture,
he4-channel-active-set, hyperelliptic-z5-classification, chi-sym-alt-closed-form,
computational-horizon, skein-generation, quantum-dilogarithm, q-codifferential-formula-prop,
bar-involution-invariance, hecke-markov-transition, confinement-grading-correspondence-conditional
(+ skein-resolution-obstruction in flight).

**Root-cause classes discovered** (recur across files — check these FIRST on any remaining file):
1. Lean 3 `constant` keyword (never valid Lean 4) → `axiom` (bar-involution: 6, confinement-grading: 5)
2. Archimedean-sweep orphan rot: doc comments left live above commented-out fields/theorem
   headers; half-commented theorem bodies (computational-horizon, skein-generation, quantum-dilogarithm)
3. Unnamed `noncomputable section` opened after a `/- Ground ring -/` comment, never closed
   before `end <Namespace>` (5 files)
4. Doc comment attached to `noncomputable section` (illegal) → demote to `/- -/` (5 files)
5. Missing Mathlib.Tactic.* imports (norm_num/ring/linarith/field_simp/interval_cases/push_neg
   used with only Data.* imports)
6. Defaulted data fields (`mass_formula : R_q := ...`) are unconstrained → theorems about them
   unprovable → convert to defs / add proof field (skein-generation, computational-horizon NPWitness)
7. Division/Inv/LT over R_q = LaurentPolynomial ℤ (no instances) → generalize over [Field K] per §7c

**OTHER-class finding**: sampled files fail ONLY on missing QOU/Basic.olean — the lake-cache
branch was seeded while QOU.Basic itself had stale imports, so downstream library oleans are
absent. QOU.Basic + QOU.Glossary oleans now build clean via
`scripts/verify-lean-direct.sh <src> <out.olean>`; bulk re-verify of the 26 OTHER in progress.
→ RESEED lake-cache/qou-v4-24-0 after this lands so the QOU package oleans are preserved.
