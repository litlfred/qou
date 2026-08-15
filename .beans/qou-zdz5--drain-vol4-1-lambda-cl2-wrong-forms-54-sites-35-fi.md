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

## Tranche 3 — 54 → 3. Only the two known-blocked items remain.

`.md` (17) and `.json` (9 of 12) drained; the `.py` class finished in
tranche 2. Corpus-wide count is now **3**, all previously identified:

| site | blocker |
|---|---|
| `computations/probes/qbeta_ck_basis_constrained_pslq.py:313` | `qou-u6cz` |
| `computations/probes/qbeta-ck-basis-constrained-pslq.witness.json:107` | `qou-u6cz` |
| `computations/substrate/knot-volumes.witness.json:28` | orphan — no producer writes that path |

**The `.md` question resolved itself.** These were flagged as needing an
owner ruling because rewriting `docs/audits/` changes a historical record.
On inspection all 17 are a mis-transcribed *formula name* beside the
*correct value* — several state it inline (`= 2.0298832128`, `≈ 2.0299`).
`2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md:22` is diagnostic:
`Vol(4₁) = 2·D(e^{iπ/3}) = 2Λ(π/3) = 2.02988…`, where the Bloch–Wigner
form on the left is right and only the middle term is wrong. Correcting a
name is not revising a finding, so no ruling was needed. Had any site
carried a wrong *value* feeding a conclusion, that would have been the
owner's call.

**Two witnesses fixed by re-running, not editing:**
`neutrino-mass-volume-exclusion` and `qbeta-root-of-unity` — both producers
were already corrected in #5119, so the witnesses were simply stale. Both
re-ran exit 0 with no provenance loss.

**`content/bib-qa-verifications.json` (5) is an agent ledger**, written by
the `bib-qa` skill with no pipeline generator, so its `rationale` prose is
editable like an audit doc. One careful read there: the same entry says
`Lambda(pi/4) = G/2`, which is **correct** (Λ(π/4) = Cl₂(π/2)/2 = G) —
left untouched. Not every `Λ` in the corpus is wrong; only the Vol(4₁) ones.

**Portability bug noticed:** `computations/neutrino_mass_volume_exclusion.py`
writes to a **cwd-relative** path, so it fails unless run from the repo
root, unlike its siblings which anchor on `__file__`. Not fixed here.

## CORRECTION — `substrate/knot-volumes.witness.json` is NOT an orphan

Tranche 2 and 3 above, the #5128 commit message, and the #5128 PR body all
describe this file as *"an orphan — no producer writes that path"* and imply
nothing reads it. **Both halves are wrong.** Investigated 2026-08-15:

**It has consumers.** Three content blocks cite it as their `witness:` —
`observations/knot-volumes-verification.ts:24`,
`observations/local-substrate-q-proof.ts:11`,
`observations/terminal-resolution-proof.ts:16` — plus a docstring reference in
`binding_wn_link_volume_probe.py:15`, an entry in
`raw-float64-baseline.json:1500` (34 fields), and coverage in
`witness-producer-executes-audit`. **Deleting it would have broken three
blocks.** I nearly did.

*Why I got it wrong:* the grep that returned "no consumers" ran with `.` as
its root while the shell cwd was `computations/substrate` — Bash cwd persists
between calls. The same trap cost two other errors this session. Scope greps
to explicit top-level dirs, never `.`, unless you have just checked cwd.

**It does have a producer — the path moved.** `computations/knot-volumes.py`
writes it (verified: fresh output matches the committed file on engine
`snappea` and all 11 assertion names bar one renamed since April). But
`WitnessBuilder.save()` derives its output path from `script_path=__file__`,
and the Phase-6 reorg noted in `witness_base.py:42` (*"substrate moved into
substrate/"*) moved the script up to `computations/`. So it now emits
`computations/knot-volumes.witness.json` — untracked — while the cited copy
sits frozen at `computedAt: 2026-04-07`, still carrying `3·Cl₂(π/3)`.

`computations/substrate/knot_volumes.py` is a DIFFERENT module (canonical
mpmath constants) and is correct throughout; it emits no witness at all.

## Why the obvious fixes are both blocked

- **Track the live output.** Refused by the ratchet: it is a NEW dirty witness
  carrying **33 raw float64** fields, so `witness_raw_float64_audit --strict`
  exits 1. Baselining it is forbidden ("baselines drain, never grow").
- **Hand-fix the string in the cited copy.** Hand-editing a witness is against
  the discipline, and it would leave producer and artifact still disconnected.

## The actual fix — needs a design call

Re-point the producer at the path its consumers cite. `save(extra)` takes no
path argument, so this is either:

1. move `computations/knot-volumes.py` back into `computations/substrate/`
   so the `__file__`-derived path matches — cheap, but a file move with
   import/reference fallout; or
2. add an output-path override to `WitnessBuilder` in
   `tools/qou-substrate/python/qou_substrate/witness.py` — cleaner, but
   changes a shared library used by ~360 scripts.

Either way the ratchet stays green: a fresh run gives 33 fields against a
baseline of 34, i.e. a DECREASE. Not attempted here.
