# De-laundering the "context enrichment" sorry-discharge campaign

**Date:** 2026-08-08 · **Branch:** `claude/delaunder-context-enrichment-2026-08-08`

## Finding

On 2026-08-03 a batch of **16 commits** (`feat(lean): prove <thm> via context
enrichment`) discharged `sorry`s across the corpus by a uniform mechanism:

```lean
class FooContext where
  /-- The foo claim (conclusion). -/          -- ← the theorem's OWN conclusion
  foo_claim : <verbatim conclusion of theorem foo>

theorem foo [ctx : FooContext] … := ctx.foo_claim   -- ← projects the assumption
```

The `*Context` class field **is** the theorem's conclusion (the docstrings
literally read `The … claim (conclusion)`), and the proof merely projects it.
When **no discharging instance** of the class exists, the theorem is not
proved — it *assumes itself*. The only thing that changed is the `sorry`
token disappeared, so the result silently passes the sorry / vacuity audits
while remaining unproven.

This violates three standing rules:

- **AGENTS.md "Axiomatization is NOT a Proof"** — a conditional `class`
  wrapping the claim does not prove it.
- **§3b-cond point 5** — "a class that carries the block's own conclusion as
  a field, with a theorem that merely projects it, is a vacuous self-assuming
  projection."
- **"Conditional-proved ≠ premise-established."**

### Legit vs. laundered

The pattern is **legitimate when the class is discharged by a genuine
instance**. Exactly **one** of the 16 is: `burnside`, whose
`instance instBurnsideContext := burnside_proved` supplies a real,
sorry-free proof of `Σ_λ (dimIrrep λ)² = n!`. The other **15 have no
discharging instance** — laundered.

## Disposition

Restore each of the 15 to its **honest pre-laundering state**: the real
theorem statement with an honest `sorry` + `-- Ref:` (state-and-queued, the
disposition §3b sanctions), removing the self-assuming `*_claim` field. Most
carry a legit **inputs** `*Context` class (data hypotheses — α, masses,
Gram matrix, …); only the added conclusion field is removed. `burnside` is
untouched.

| # | theorem | file | disposition |
|---|---------|------|-------------|
| 1 | `burnside` | `BraidKnot/DeltaLambdaSignRule.lean` | **kept** — genuine `instBurnsideContext := burnside_proved` |
| 2 | `volume_perturbation` | `BraidKnot/volume_perturbation.lean` | revert → honest `sorry` |
| 3 | `whitehead_volume_conjecture` | `Knot/WhiteheadVolumeConjecture.lean` | manual → honest `sorry` + **pointer to genuine proof** `QOU.Knot.WhiteheadSaddle.whitehead_vc_innerSum_half` (downstream, sorry-free) |
| 4 | `markovTrace_branching` | `FeynmanPathIntegrals/markov_identification.lean` | revert → honest `sorry` |
| 5 | `finite_cascade_depth` | `FluidDynamics/q_turbulence_spectrum.lean` | revert → honest `sorry` |
| 6 | `q_ns_wellposedness` | `FluidDynamics/q_ns_wellposedness.lean` | revert → honest `sorry` |
| 7 | `neutron_proton_splitting` | `Torsion/neutron_proton_splitting.lean` | revert → honest `sorry` |
| 8 | `liouville_green_weber_limit` | `QBeta/ToroidalHarmonicsBasis.lean` | revert → honest `sorry` |
| 9 | `q_gl_obstruction_calc` | `q_gl_obstruction_calc.lean` | revert → honest `sorry` |
| 10 | `atomic_lp_stability` | `ParticleInteractions/atomic_lp_stability.lean` | revert → honest `sorry` |
| 11 | `lp_dual_stability` | `ParticleInteractions/lp_dual_stability.lean` | revert → honest `sorry` |
| 12 | `operator_selection_lp` | `ParticleInteractions/operator_selection_lp.lean` | manual → honest `sorry` |
| 13 | `four_term_pair_nucleon` | `ParticleInteractions/four_term_pair_nucleon.lean` | revert → honest `sorry` |
| 14 | `atomic_nf_witness` | `ParticleInteractions/atomic_nf_witness.lean` | manual → honest `sorry` |
| 15 | `confinement_frobenius_reciprocity` | `ParticleInteractions/confinement_frobenius_reciprocity.lean` | revert → honest `sorry` |
| 16 | `parity_regime_selection` | `ParticleInteractions/parity_regime_selection.lean` | revert → honest `sorry` |

12 reverted cleanly (auto-commit each); 3 (whitehead, operator_selection_lp,
atomic_nf_witness) conflicted with later §7c base-ring ports and were
de-laundered by hand.

## Verification

`lean --root` (v4.24.0, warm oleans), all `EXIT=0`:

- `WhiteheadVolumeConjecture.lean` — EXIT 0 (`sorry` @298, honest)
- `operator_selection_lp.lean` — EXIT 0 (`sorry` @98)
- `atomic_nf_witness.lean` — EXIT 0 (`sorry` @93)
- spot-checks across directories: `neutron_proton_splitting`,
  `q_ns_wellposedness`, `lp_dual_stability` — all EXIT 0.

Residual `exact ctx.*_claim` / `claim (conclusion)` in the corpus: **burnside
only** (legit).

## Follow-up (honest open state)

These 15 are now honestly **stated, not proved**. Genuine closure is a
per-theorem research task:

- **`whitehead_volume_conjecture`** — the genuine proof already exists
  downstream (`whitehead_vc_innerSum_half`, ⌊N/2⌋ inner sum). The remaining
  `sorry` is only the base-file abstract `kashaev`/(N−1)/2 form, blocked by
  the Mathlib-only import boundary. Bean qou-1gkf.
- **`q_ns_wellposedness`, LP-dual trio** (`operator_selection_lp`,
  `lp_dual_stability`, `atomic_lp_stability`) — depend on LP strong-duality /
  Navier–Stokes well-posedness infra not in Mathlib; likely long-horizon.
- The rest depend on the compact quantum dilogarithm `Φ_q` / GS-normal-form
  compute facts not yet formalised.

**None of these should be "closed" by re-assuming the conclusion.** A genuine
proof, or an honest `conjecture`-kind demotion, are the only acceptable
future dispositions.
