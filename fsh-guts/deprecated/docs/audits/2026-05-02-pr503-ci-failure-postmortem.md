> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

# PR #503 — CI failure postmortem (validate / witness-pipeline)

**Compiled** 2026-05-02 on `claude/refactor-computation-framework-Dmvva`.
**Run:** [25260536957/job/74066962534](https://github.com/litlfred/qou/actions/runs/25260536957/job/74066962534).
**Result:** `failure` on the `validate` job of the `Witness pipeline`
workflow ([`.github/workflows/witness-pipeline.yml`](../../.github/workflows/witness-pipeline.yml)).

## Failure cause

The **drift-check** step (witness-pipeline.yml lines 131–161) detected
substantive drift in
[`computations/derivation-chain-audit.witness.json`](../../computations/derivation-chain-audit.witness.json).
The drift survived the CI filter, which strips only timestamp /
commit / hash / engine fields:

```text
"(computedAt|durationMs|commitSha|scriptCommitSha|scriptHash|
  engineVersion|engine|engine_version)"
```

After filtering, the only surviving drift line was:

```diff
+        "ew-higgs-sdp-probe.witness.json",
```

i.e. the witness file [`ew-higgs-sdp-probe.witness.json`](../../computations/probes/ew-higgs-sdp-probe.witness.json)
that was *introduced* in commit `713e990e` (the EW/Higgs SDP probe).

## Why the drift exists

[`derivation_chain_validator.py`](../../computations/derivation_chain_validator.py)
walks every `*.witness.json` in `computations/` and
classifies each as one of:

| Class | Definition |
|-------|------------|
| `fully-trusted` | has a `derivation.json` companion that resolves to a leaf-value witness, and the leaf value matches the witness numeric |
| `derivation-backed` | has a `derivation.json` companion (no leaf-numeric check) |
| `computational-only` | no derivation chain exists — the witness is a raw script output |

The new `ew-higgs-sdp-probe.witness.json` has no derivation chain
(no companion `.derivation.json`), so the validator correctly classified
it as `computational-only` and added its filename to the
`computational-only witnesses (need a derivation chain)` list inside
the regenerated audit witness.

This is **expected behaviour**, not a bug — the audit witness
literally documents *what witnesses still need a derivation chain*,
and adding a new computational witness extends that list by one
entry.

## Fix

Two acceptable resolutions, both followed:

1. **Commit the regenerated audit witness.** This is the canonical
   pattern used for every prior `*-validator.py` cycle on this
   repo; the audit witness is *intended* to be regenerated and
   re-committed alongside any new witness file. The CI drift
   check is satisfied because, after the commit, there is no
   diff between the locally-regenerated audit and the committed
   one.
2. **Document the failure mode** so the next contributor (or
   subagent) does not waste a CI cycle on the same surprise.
   This file is that documentation.

## Lessons / process improvement

- **Pre-push checklist for witness-pipeline-touching commits.**
  Whenever a commit adds or modifies a `*.witness.json` or
  `*.derivation.json` under `computations/`, run
  the four validators **locally** before pushing:

  ```bash
  python3 computations/habiro/habiro_witness_validator.py
  python3 computations/markov/markov_substrate_realizer.py
  python3 computations/markov/markov_pipeline_cross_validator.py
  python3 computations/derivation_chain_validator.py
  ```

  Then `git status` — if any `*.witness.json` got touched, commit
  the regenerated copies along with the originating change.
  This is the same pattern as the deferred `regenerated-witness`
  step in commits like
  [`a8b02b6c`](https://github.com/litlfred/qou/commit/a8b02b6c)
  and
  [`c45b636d`](https://github.com/litlfred/qou/commit/c45b636d).

- **Suggested CI hardening (out of scope for this PR).** The drift
  filter at line 154 of
  [`witness-pipeline.yml`](../../.github/workflows/witness-pipeline.yml)
  could be extended with one more allowed-drift family:
  `"computational-only-list-additions"` — i.e., new entries
  in the list literal `"computational-only witnesses (need a
  derivation chain)"` are non-substantive when the new entry is
  the basename of a file freshly added in the same commit. This
  would auto-classify "I added a new witness, the audit notices,
  fix not needed" as benign drift. The current behavior — fail
  CI, force the contributor to re-run the validator and commit
  — is also defensible (it forces awareness) but creates a CI
  cycle every time.

## Detailed timeline

| time | event |
|------|-------|
| 18:46 UTC | Gemini posted two review comments on PR #503 (Step 19' typo, $H_4 = 14$ math error) |
| 18:50 UTC | Both comments addressed by commit `1b051970` (push, Gemini threads outdated) |
| 19:50 UTC | FROB-FILTER signature compute + Bring inventory commit `f2b46970` |
| 19:55 UTC | EW/Higgs SDP probe commit `713e990e` — adds `ew-higgs-sdp-probe.witness.json` |
| 19:57 UTC | `validate` CI job started |
| ~19:59 UTC | `validate` failed — drift in `derivation-chain-audit.witness.json` |
| 20:05 UTC | Local validator re-ran; only substantive drift confirmed: the new witness filename added to the `computational-only` list |
| **next push** | Audit witness regenerated and committed alongside this postmortem |

## Related cross-references

- The fixed PR commits: f2b46970 (FROB-FILTER + Bring), 713e990e
  (SDP probe), [next] (audit witness + this postmortem).
- The validator code:
  [`derivation_chain_validator.py`](../../computations/derivation_chain_validator.py)
  (witness classification logic).
- The drift check:
  [`witness-pipeline.yml`](../../.github/workflows/witness-pipeline.yml)
  lines 131–161.
- Prior similar landings (audit-witness-regeneration pattern):
  the BB-stratification cycle (commit `cffbf553`) and the
  six-knot-basis cycle (commit `a8b02b6c`) both followed the
  same "regenerate + commit" pattern.

**Audit closed:** the failure was a benign auto-detection of a
new computational witness; no math-framework bug, no compute
defect. Fix is mechanical and is part of the next push.
