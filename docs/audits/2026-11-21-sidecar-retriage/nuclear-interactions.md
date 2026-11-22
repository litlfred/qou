# Sidecar re-triage: nuclear-interactions (2026-11-21)

Part of umbrella issue #8766. After this pass every block is fresh on both
criteria: 15 statement blocks and 18 proof blocks.

## Re-stamps (12)

The diff was wording only. The earlier verdict is kept and cites the diff.
One of these re-stamps carries a partial fix: `q-beta-spectral-bridge-proof`
dropped its false "deferred via `sorry`" sentence, which was one point of the
earlier finding.

## Full reviews (9)

The `inductive-gb-reduction-proof` entry was written twice. The second entry
corrects which table row conflicts with the bound.

| block | criterion | verdict |
|---|---|---|
| parity-regime-selection-proof | proof | fail major: the a−b sign is now stated but not derived; the regime formulas are still not derived |
| groebner-shirshov-energy-proof | proof | pass, re-affirmed: Bokut–Shiao rules preserve length and coefficient |
| nuclear-operator-regimes | stmt vs Lean | fail major: the braid closures are now correct (T(2,4) and unknot) and T(2,n_s) is gone; the Lean is still an rfl table; a leftover "Hopf link" sentence remains |
| inductive-gb-reduction-proof | proof | fail major: the squares are now correct; the bound is admitted open |
| nuclear-groebner-reduction | stmt vs Lean | fail major: the md now has the correct GS basis; the ref is still an unasserted `def … : Prop`; Z[q^±] vs real q |
| nuclear-groebner-reduction-proof | proof | fail → warn major: the composition example checks; scoped to real q; understates the uniqueness claim |
| confinement-phase-stratification-proof | proof | fail major: relocated without change; claims (2) and (3) are still defective |
| shell-closure-stability-proof | proof | fail major: the banner admits the sign gap, but step 1(c) still contradicts it |
| groebner-shirshov-energy | stmt vs Lean | fail major: there is a new genuine short-model β theorem, but the ref is still a def, and old "energy rises" lemmas contradict item 3 |

## Ruling check (docs/coordination/owner-rulings.md)

- **T(2,n_s) shell rule (withdrawn).** No live T(2,n_s) remains in this chapter's `.md` files. `nuclear-operator-regimes` dropped it in this diff.
- **Electron = σ₀σ₁σ₀ ∈ B₃ with Hopf closure.** Blocks outside this pass's review scope still treat the trefoil as the electron: `two-photon-pair-production`, `intro-pair-production-anyon`, `confinement-operator-selection-interpretation`, `hydrogen-derived-nf`, `li6-derived-nf`, `helium4-derived-nf` and `box-braid-irreducibility-interpretation`. These are routed to the SM thread as findings.
- **Photon form.** No conflict found in the reviewed blocks. The `L_+ = σ₀σ₁` in `nuclear-operator-regimes` is a nuclear operator, not the photon.
