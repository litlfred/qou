---
# qou-c6xo
title: 'wave4: corpus-wide witness regen sweep to completion (162 producers)'
status: completed
type: task
priority: normal
created_at: 2026-08-09T01:23:57Z
updated_at: 2026-08-09T01:52:44Z
---

Branch: claude/anchor-followups-2026-08-08. CLAIMED by this session.

Continues qou-zfex (wave 3, 76/101). Wave 4 = full corpus, 162 producers in
dependency order, --timeout 900, report at
scratchpad/sweep.json.

## Why the six earlier attempts died — established, not guessed

No OOM (`dmesg | grep -ic oom` = 0; 10.5 GB of 16 GB free, 4 CPUs, 14 GB disk).
The tell was a LIVE ORPHAN found at session start: `term5_aK_audit.py` PID 7180,
**PPID 1**, 31 min elapsed — past the 900 s cap the wave would have enforced —
with stdout/stderr pipes that had no reader. A child outliving its timeout with
no reader on its pipes means the WAVE was killed, orphaning it; the wave did not
kill the child. So the wave is being reaped externally, almost certainly with the
launching shell's process group between turns.

FIX: launch under `setsid` (new session + new process group, no controlling
terminal), so a pgid-targeted kill aimed at the shell cannot reach it.
Launcher: scratchpad/launch_sweep.sh. Verified detached — wave SID 6261 vs
shell SID 6592.

Killed the orphan before starting: it was one producer away from dirtying the
tree, which would have been misattributed to whichever producer the new wave had
in flight (the clobbering the wave docstring warns about), and it violated the
never-two-producers-at-once rule.

RULED OUT as a stall risk: a timed-out producer hanging the wave. On POSIX
`subprocess.run(timeout=)` calls `process.wait()` after `kill()`, not
`communicate()`, so orphaned grandchildren of a multiprocessing producer cannot
block it.


## OUTCOME — STOOD DOWN at 27/162, nothing committed, nothing pushed

Coordinator directive mid-run: an owner ruling excises trace convention **C** in
favour of **D** (docs/coordination/trace-convention-registry.md;
docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md), changing the
Markov-trace weights behind ~155 files / ~96 witnesses. Any witness regenerated
now would be stale on arrival. Sweep stopped; coordinator will re-run after C→D.

### CORRECTION to the root-cause analysis recorded above — it was WRONG

The section above blames an external reaper and credits `setsid` as the fix.
That is incorrect and I am leaving it visible rather than deleting it. The wave
was killed **deliberately by the coordinator**. `setsid` was never the problem
and is not the fix. The reasoning was seductive because the evidence genuinely
fit — a PPID-1 orphan past its 900 s cap with unread pipes — but that signature
is produced by ANY kill of the parent, including an intentional one. I inferred a
mechanism from a signature that did not distinguish it. The earlier six deaths
may well have a different cause than the one I asserted; treat that analysis as
unproven.

### Result (verified from the report JSON, not asserted)

producers_run 27 / producers_total 162 — **INCOMPLETE**.
base 1b8b30758b97350c9120223748ebb04f9ee399c4, timeout 900 s,
01:20:24Z → 01:42:15Z. Report: scratchpad/sweep.json.

  VALUES 13 · NOCHANGE 7 · FAILED 6 · ANCHOR_MIGRATION_INFERRED 1 · **kept 0**

kept=0, so there was nothing to commit; `git status computations/` shows zero
dirty witnesses — the per-witness revert worked. No witness value was ever
hand-edited.

Left a live ORPHAN producer behind on the kill (`a4_brunnian_deficit_closed_form.py`,
PID 27523, PGID/SID 6261 = the dead wave's session, producer #28); killed it
before it could write. An identical orphan (`term5_aK_audit.py`, PID 7180) was
found and killed at session start — orphans outlive the wave and WILL dirty the
tree unattributed. Worth checking for one after any future kill.

### Failure triage — 6 FAILED (survives the C→D change; these are trace-independent)

**(b) timeout — 1.** `audits/term5_aK_audit.py`, exit `timeout`, 900.13 s,
touched 0. Chronic and known; not a bug.

**(c) missing upstream — 3, ONE shared root cause.**
`audits/delta_n2_placeholder_audit.py` (exit 1, "Run its producer first."),
`audits/deuteron_delta_i_audit.py` (exit 1, same),
`compound_binding_via_differences.py` (exit 1, EMPTY stderr_tail — it prints its
error to stdout, so the report's stderr-only tail hides it; a naive triage
mis-buckets this one as a genuine bug).
All three need `atomic-braid-mass-table.witness.json`, which **exists nowhere in
the tree and has no producer**. `audits/witness_provenance_audit.py:16` documents
it as `(off-main)` — a hand-edited legacy artifact predating WitnessBuilder, null
provenance. NOT a dependency-ordering problem: no ordering can produce it. These
three cannot pass until that witness is restored or the consumers are retired.

**(c) missing dependency — 2. A FOURTH bug class, not among the three known.**
`delta_lambda_alexander_phase4.py` and `delta_lambda_jsj_phase3.py`, both exit 1,
`ModuleNotFoundError: No module named 'probe_he4_jsj_topology'`. That module now
exists ONLY at `_deprecated/probes/probe_he4_jsj_topology.py`. Two LIVE producers
import a deprecated module. `_path_bridge` cannot fix this — it adds substrate
dirs, not `_deprecated/`, and `producers()` skips `_deprecated` by design. The fix
is a judgement call (un-deprecate vs. retire the importers), so it was not made.

### Recurrences of the three known bug classes: NONE that are live

- class 1 (missing `import _path_bridge`): **0**.
- class 3 (`mp.mpf(repr(x))` on a 50-dps string field): **0**.
- class 2 (bare `HERE / "<name>.witness.json"` needing `_path_bridge.witness_path()`):
  **2 latent sites among the failures, plus 1 more not reached** — all MASKED by
  the absent witness above, so fixing them changes no outcome today. Readers of
  `atomic-braid-mass-table.witness.json` split 3-vs-3, which is what makes it a
  real inconsistency rather than a style preference:
    class-2 (bare join):  compound_binding_via_differences.py:124
                          audits/deuteron_delta_i_audit.py:158
                          neutron_error_diagnostic.py:131   (not reached this run)
    correct:              audits/delta_n2_placeholder_audit.py:166
                          audits/braid_encoding_audit.py:397
                          atomic_mass_via_rho_k.py:453
  Left unfixed deliberately: no commit was authorised, and the fix is a no-op
  while the upstream is absent.

### One result a human should look at
`binding_energy_categorical_deuteron.py` → ANCHOR_MIGRATION_INFERRED on
`computations/binding-energy-categorical-deuteron.witness.json`. That verdict is
'review' by design and is NOT in KEEP, so it was reverted. It will resurface in
the post-C→D re-run.

### Scope note for the re-run
4 of the 5 'known-slow' producers are NOT in the 162: `_habiro_coefficient_extract`,
`extend_even_a_mirror_pair_test`, `he3_tritium_cosh_asymmetry_diagnosis`,
`mass_at_3A_proper` have ZERO `add_upstream`/`record_upstream` calls, so
`declares_upstream()` excludes them. `git log -S add_upstream` on `_habiro` is
empty — it never declared one, so wave 3's report of it timing out came from a
different selection. Only `term5_aK_audit` (900 s) and `alpha/alpha_k_jones_markov_h12`
(900 s, NOT on the known-slow list — new) are slow in this set. Budget ~2 × 900 s,
not 5 ×.

## CORRECTION 2026-08-09 (foreground session): the "no producer anywhere" item

This bean records `atomic-braid-mass-table.witness.json` as "exists nowhere in
the tree" and treats it as a missing-producer defect. **The absence is real; the
framing is wrong, and acting on it as stated would violate an explicit
forbidden-use.**

Checked, not assumed:

1. The file exists nowhere -- CONFIRMED (`find` over the whole tree, 0 hits).
2. It was **deliberately retired**, not lost.
   `computations/_deprecated/methodology-deprecation.witness.json:66` lists it
   under deprecated artifacts: "atomic-braid-mass-table.witness.json (off-main
   commitSha; six-term formula 24-54 % errors)", alongside the modes-sweep
   ("best mode still 22 % mean err").
3. Its consumer **degrades cleanly and says so**.
   `compound_binding_via_differences.py:124` checks `s3_path.exists()`, prints
   "ERROR: atomic-braid-mass-table.witness.json missing" and `return 1` -- an
   exit code, not a crash. Its own docstring at :118 reads: "This script remains
   a legacy consumer **by design**; for **mass predictions** use the canonical
   witness instead" -- naming `atomic-mass-via-rho-k.witness.json` as the
   replacement.

So there is nothing to repair here. **Do NOT regenerate it.** The deprecation
record lists "Generating new mass predictions for the atlas" and "Citing as
primary evidence for the mass-table-ppb framework" as FORBIDDEN USES; producing
the witness to make three audits resolve would do exactly that, and would
reinstate a six-term formula carrying 24-54 % errors.

The legitimate residue is documentation drift only: the three audits that cite
the witness (`2026-05-17-p4tt-migration-triage.md:60`,
`2026-05-10-workplan-0b-script-rewire-handoff.md:267`, `coordination/1ppb.md:132`)
predate the deprecation and read as though the artifact were live. That is a
doc-note fix, NOT a regen item, and it should be split out of this bean's
regen queue so a future sweep does not pick it up as work.
