---
# szkf
title: Remap 64 stale Mathlib imports (post-f897ebcf module renames/splits)
status: completed
type: milestone
created_at: 2026-06-30T23:32:53Z
updated_at: 2026-07-05T05:05:00Z
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

> **Resolved 2026-07-05 (swarm 1).** Mathlib import remaps applied + Lean-verified (0 stale imports remain). Merged in PR #3337.

## Wave-3 reevaluation (2026-07-17) — import layer resolved, DEEP defects persist on main

PR #3202 (wave 2, closed as obsolete) drained 45 files on a pre-churn base. Reevaluation
against current main (0b4ed888d4):

- **Import layer: superseded** — PR #3337 remapped imports corpus-wide (confirmed 0 stale).
- **2 files deleted on main**: observations/algebraic-gns-embedding, mass-theory/skein-generation.
- **Deep defects NOT absorbed** — all 40 survivors diverged from both the old broken state and
  the wave-2 fixes (churn, not fixes). Spot-checks confirm still-broken on main HEAD:
  - bar-involution-invariance L99-106: Lean 3 `constant` declarations (parse error)
  - nuclear-spin-parity L61: beta_decay_preserves_spin_parity FALSE at n=0 (needs 1 ≤ n)
  - c-equals-bar-iff-all-1dim L50: `(-q) - h = q` ⟺ 4q = 0 falsity
  - computational-horizon L224: theorem over defaulted data field (unprovable)
- These siblings have no QA sidecar → red on main invisibly (the known verifier blind spot).

**Wave-3 plan (session 2026-07-17, branch claude/stale-mathlib-imports-9xzeul restarted from
main):** bulk lean-direct verify of all 40 at main HEAD → for each FAIL, 3-way port of the
wave-2 fix (base=3535f809, ours=main, theirs=49057c2b old tip) or hand-port → fresh PR.
Plus infra: ckj6 verifier hardening + lake-cache reseed. Wave-2 fix reference blobs live at
commit 49057c2b (closed PR #3202 head).
