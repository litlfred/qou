---
# qou-zdz5
title: 'DRAIN: Vol(4_1) Lambda-Cl2 wrong forms — 54 sites / 35 files still live (computations/ + docs/ never swept)'
status: todo
type: task
created_at: 2026-08-15T15:22:10Z
updated_at: 2026-08-15T15:22:10Z
---


## Measurement (2026-08-15, fixed-string grep)

The 2026-08-10 drain (#4886 → #4901 → #4917) reported the Λ↔Cl₂ slip fixed
"corpus-wide, 14 sites across 12 files". It swept `content/` only. AGENTS.md
was updated to say both wrong forms "were live in the corpus until 2026-08-10",
i.e. an all-clear. That all-clear was false and has been corrected in this PR.

Remaining after PR #5119's 9 fixes:

| tree | sites | files |
|---|---|---|
| `content/` | 5 | 1 |
| `computations/` | 28 | 18 |
| `docs/` | 21 | 16 |
| **total** | **54** | **35** |

By extension: 25 `.py`, 17 `.md`, 12 `.json`, **0** `.lean`, **0** `.ts`.
The `.lean`/`.ts` surface IS clear — that part of the drain worked.

Per-file counts:

```
content/bib-qa-verifications.json:5
computations/qbeta/qbeta_bring_embedding_magnitude_probe.py:5
computations/qbeta/qbeta_c3_barodd_nz_deformation_probe.py:4
docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md:3
computations/q0_figure_eight_phase_derivation.py:3
docs/audits/scripts/qbeta_ohtsuki_figure_eight_ladder.py:2
docs/audits/2026-07-13-moire-resonance-framing-critical-assessment.md:2
docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md:2
computations/qbeta/qbeta_c3_barodd_tetraplectic_reduction_probe.py:2
computations/qbeta/qbeta-bring-embedding-magnitude.witness.json:2
docs/coordination/udeform-spin-part-derivation.md:1
docs/audits/scripts/qbeta_s_complex_volume_rigidity_probe.py:1
docs/audits/scripts/mu_p_carrier_order_window_probe.py:1
docs/audits/2026-08-09-canonical-chain-walk-gaps-marked.md:1
docs/audits/2026-08-02-geometric-q0-substrate-derivation-assessment.md:1
docs/audits/2026-08-02-aomega-internal-derivation-symmetry-constant-target.md:1
docs/audits/2026-08-01-bring-embedding-magnitude.md:1
docs/audits/2026-07-13-alien-calculus-surreal-integration-review.md:1
docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md:1
docs/audits/2026-07-07-c3-even-solved-s-complex-volume-rigidity.md:1
docs/audits/2026-06-17-qbeta-root-of-unity.md:1
docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md:1
computations/substrate/knot-volumes.witness.json:1
computations/qbeta/qbeta_magnitude_taylor_qstar_probe.py:1
computations/qbeta/qbeta_fmap_phi_b_root_of_unity_reference.py:1
computations/qbeta/qbeta_c4_qhermite_entry_gate_probe.py:1
computations/qbeta/qbeta-c3-barodd-nz-deformation-gap.witness.json:1
computations/probes/qbeta_ck_basis_constrained_pslq.py:1
computations/probes/qbeta-root-of-unity.witness.json:1
computations/probes/qbeta-ck-basis-constrained-pslq.witness.json:1
computations/probes/__pycache__/qbeta_ck_basis_constrained_pslq.cpython-311.pyc:1
computations/neutrino-mass-volume-exclusion.witness.json:1
computations/knot-volumes.py:1
computations/knot-particle-generation.py:1
computations/binding_wn_link_volume_probe.py:1
```

## Do not mass-rewrite — three classes, three dispositions

1. **`.py` comments (25)** — safe, mechanical. Most compute the RIGHT value
   under the WRONG name: `VOL41 = 2*mp.clsin(2, mp.pi/3)` is `2·Cl₂(π/3) =
   2.0299` ✓ annotated `# Vol(4₁) = 2Λ(π/3)` ✗. Check the arithmetic beside
   each before touching it — a bad name does not imply a bad number, and
   "correcting" a correct value would be the real regression.
2. **`.json` (12)** — witness payloads and `bib-qa-verifications.json`.
   Needs producer re-runs, not hand edits. At least one producer
   (`qbeta_ck_basis_constrained_pslq.py`) currently regenerates a FAILING
   witness for unrelated reasons — see `qou-u6cz`. Blocked behind that.
3. **`.md` (17)** — mostly `docs/audits/`, which are historical records of
   what was believed at the time. **Owner call** whether audit docs get
   rewritten or annotated; do not rewrite unilaterally.

## Why this recurred

The guard in AGENTS.md read as "already drained", so three sessions plus this
one took it at face value. The lesson is in the guard now: assume the file you
are editing still carries it.

Found in PR #5119.

## Tranche 2 (PR #5128) — the `.py` class is DONE

22 sites / 13 files drained. Remaining from the 54: the 12 `.json` and the
17 `.md`.

**One site was not a naming slip.** `docs/audits/scripts/qbeta_s_complex_volume_rigidity_probe.py`
had `lam_pi3 = mp.mpf("0.5074708")` labelled `Λ(π/3)`. Λ(π/3) = 0.338314;
0.5074708 is Λ(π/6) = Cl₂(π/3)/2. So `2 * lam_pi3` = 1.0149416 — ONE ideal
tetrahedron, exactly HALF of Vol(4₁) = 2.0298832. Part B's 4₁ row was
computed against it. Verdict unchanged (still "no clean near-integer
match"; the prune rests on Part A's proved anchor-invariance, not Part B),
so scope-(a): wrong value, sound conclusion. This is why the "check the
arithmetic beside the name" rule above is not optional.

**New sub-item — orphan witness, no producer.**
`computations/substrate/knot-volumes.witness.json` is committed and still
carries `3·Cl₂(π/3)`, but NOTHING writes to that path.
`computations/knot-volumes.py` (whose `source` string is fixed in #5128)
emits next to itself, to `computations/knot-volumes.witness.json`, which is
neither tracked nor gitignored. So the orphan cannot be regenerated in
place. Resolve the producer/output-path question first; the notation fix
follows for free. Needs SnapPy installed (`pip install snappy`) to run the
producer at all.

**Provisioning is part of this drain, not incidental.** Re-running any
producer in an under-provisioned container silently strips `environment`
fields from its witness (measured: `numpy` + `pyhecke_native` dropped on a
one-word label fix). Bootstrap fully before re-running, and diff the
witness for `-` version lines. Written up in `local/compute-author` §0.1.
