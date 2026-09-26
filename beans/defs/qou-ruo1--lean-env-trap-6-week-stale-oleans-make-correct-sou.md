---
# qou-ruo1
title: 'Lean env trap: 6-week-stale oleans make correct source look broken'
status: completed
type: task
priority: normal
created_at: 2026-08-30T07:52:01Z
updated_at: 2026-08-30T08:01:35Z
---

Hit TWICE on 2026-08-30 in one session, both times presenting as a code defect.

1. QOU/AppendixSurreals/QCollatz.olean dated 2026-07-02 against a 2026-08-23 source. Symptom: "Function expected at QCollatz, but this term has type Type" in collatz_block_descent.lean — the olean predated the QCollatz CLASS being added. Looks like a namespace bug.
2. QOU/AlgebraicSubstrate/qou_obstruction_reduction.olean dated 2026-07-19 against a 2026-08-29 source. Symptom: "Invalid field trace_pairing: environment does not contain ..." in obstruction_residual_gap.lean. The field IS at line 79 of the source. Looks like a missing-field bug.

Both were verified NOT to be main-side changes (git diff merge-base..origin/main on the file = empty) and NOT source defects.

DIAGNOSTIC that separates env from code, cheap, do this FIRST:
    ls -l --time-style=+%F_%T <src>.lean <root>/<Mod>.olean
If the olean predates the source, it is the environment.

FIX (do NOT run 'lake build' — it evicts the restored cache):
    lean <src>.lean -o $ROOT/<Mod>.olean
rebuilding IN PLACE into the same LEAN_PATH root. LEAN_PATH does not fall through between roots: Lean resolves a module from the FIRST root owning the namespace and never falls back, so a fresh olean in a second root is invisible.

Also observed: the SessionStart lean-build-bg hook had 'lake update' + 'cache get' running (PIDs 1564/12894), with 267 denied CONNECTs to lakecache.blob.core.windows.net. That is the documented 403 situation; it cannot succeed and is not what caused either staleness. Mathlib olean count stayed at 6990 throughout, so nothing was evicted this session.

Worth considering: a preflight that compares every QOU olean mtime against its source and reports the stale set, so this is found in one command instead of one confusing error at a time.

RESOLVED. Both stale oleans rebuilt in place; all 9 Lean files this branch touches verify at exit 0, axiom-clean.

Tooling landed as scripts/lean-olean-staleness-check.py — but NOT the timestamp preflight this bean originally proposed. That idea was tried and MEASURED TO FAIL, twice, and the failures are worth recording because both look reasonable on paper:

  1. olean mtime vs source mtime -> reported 945 stale (the whole tree). A
     container clone stamps every source with the checkout time while oleans
     come from a lake-cache restore built weeks earlier.
  2. olean mtime vs the source's last COMMIT time (git log -1 --format=%ct),
     chosen specifically because commit time survives a checkout -> reported
     945, THE IDENTICAL NUMBER. That coincidence is what exposed it: agent
     clones here are SHALLOW (190 commits), so git log returns a date inside
     the fetched window for essentially every file. AdelicSubstrate.lean
     reports 'committed 2026-08-29' though its source predates that by months.

A tool that flags the entire tree is the same as a tool that flags nothing.
Neither number was ever a measurement of the corpus; both measured the harness.

The shipped script therefore asks LEAN, which is the only sound discriminator
here: it lean-verifies the files a branch changes, and on failure rebuilds each
in-repo dependency olean IN PLACE and retries, reporting REPAIRED (stale olean)
vs FAIL (real source defect). ~5s/file, which is affordable because the useful
scope is a changeset, never the tree. Self-tested by re-injecting the genuine
2026-07-02 QCollatz.olean: reports REPAIRED and exits 0.
