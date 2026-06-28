# Audit: Moving Observations (2026-06-28)

This audit log records empirical fits, software probes, Python scripts, and CI/infrastructure commentary removed from canonical derivation sections in `content/quantum-observable-universe/observations/`.

## From knot-volumes-verification.md

```markdown
**Reproducibility**: Run `python3 computations/knot-volumes.py` to regenerate
the witness file.  Requires `pip install snappy`.

The witness file `computations/knot-volumes.witness.json` is committed to the
repository for CI verification.  Lean declarations that depend on these
volumes use `axiom` with `-- Ref: [computation]` annotations pointing to
this witness.
```

## From epistemic-status-of-calibrations.md

```markdown
- Does **not** propose to replace CAL-1, CAL-2, or CAL-3 with empirical fits.
```

## From flavor-split-substrate.md

```markdown
**Empirical match (probe `probe_flavor_split_substrate.py`):**
```

## From flavor-split-substrate-interpretation.md

```markdown
See `probe_per_sheet_flavor_nonin.py` for the
explicit numerical confirmation.
```

```markdown
See the
`witness_dependency_drift.py` validator for the residual budget.
```

## From isospin-mirror-v9-empirical-near-match.md

```markdown
The Option-E v9 $^3$H/$^3$He isospin-mirror probe surfaces an empirical
near-match: a cross-isotope bar-symmetric character sum scaled by
$m_\pi\,\hbar_q$ reproduces the measured $B_T - B_{^3\mathrm{He}}$ to
about 6 %, and a further $(1+q)/2$ multiplier brings the prediction
to within 0.11 % of experiment.

The disposition is **fitted, not derived**: the $(1+q)/2$ factor was
computed as the exact ratio needed to hit the target and then
name-matched against a 9-candidate substrate menu, and it fails to
generalize to the absolute binding energies (154 % error when applied
to $B(\mathrm{D},\mathrm{T},{}^3\mathrm{He})$). Per the Δ_λ gate
(AGENTS.md) this is recorded as a near-match, not a closure of the
mirror difference.

**Primary content moved to audits.** See [`docs/audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md`](../../../docs/audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md)
for the full discipline assessment (v7/v8/v9 candidate sweep, exact
$(1+q)/2$ extraction, generalization-test refutation against absolute
binding energies, and verdict "numerology / post-hoc fit").

This block is retained in the paper as an interpretive cross-reference;
it makes no logical claim.
```
