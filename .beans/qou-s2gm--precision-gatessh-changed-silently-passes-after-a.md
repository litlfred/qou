---
# qou-s2gm
title: precision-gates.sh --changed silently passes after a commit; full run stamps sandbox lib versions into an audit witness
status: todo
type: bug
priority: normal
created_at: 2026-08-16T13:48:36Z
updated_at: 2026-08-22T20:18:26Z
---

Both found while running the mandatory precision preflight on PR #5241 after
editing `computations/wedderburn_jones_markov.py`.

## Defect 1 — `--changed` is working-tree-only, so it no-ops after a commit

`scripts/precision-gates.sh:124-138` computes its relevance set from

    git diff --name-only HEAD
    git diff --cached --name-only
    git ls-files --others --exclude-standard

All three see only the **working tree**. Once the change is committed the set
is empty and the script prints

    precision-gates: no witness or computations/ script touched — skipped.

and `exit 0`. I hit this directly: I had just committed an edit to
`computations/wedderburn_jones_markov.py` and `--changed` reported nothing
touched. A **false all-clear**, indistinguishable from a real pass.

Why this matters rather than being cosmetic. AGENTS.md says to run it "before
every commit", so pre-commit is the intended workflow — but the same document
tells every agent to "commit early, commit often" (Branch+PR rule 0/3), and
`--changed` exists precisely so agents can run it cheaply and habitually. An
agent that commits first and verifies second — a completely natural order, and
the one the microcommit rule encourages — gets a green that means nothing. This
is the same failure mode as bean `qou-mnrd` (three dirty witnesses reached main
because the gate did not actually run).

Fix: diff against the merge-base with origin/main, not the working tree, e.g.

    git diff --name-only "$(git merge-base HEAD origin/main)"...HEAD

unioned with the existing three working-tree sources. Cheap, and makes the
answer independent of whether the agent has committed yet.

## Defect 2 — a full run rewrites an audit witness with the RUNNER's library versions

A full `bash scripts/precision-gates.sh` regenerates three committed audit
witnesses. Two of them move only real counts. The third,
`computations/audits/q0-anchor-consistency-audit.witness.json`, also rewrites
an **environment stamp** to whatever the runner happens to have installed. In
this sandbox that diff was:

    - "scipy": "1.17.1",          (removed — not installed here)
    - "clarabel": "0.11.1"        (removed — not installed here)
    - "mpmath": "1.4.1"  ->  + "mpmath": "1.3.0"    (DOWNGRADE)
    - "sympy": "1.12"    ->  + "sympy": "1.14.0"

Committing that would degrade the recorded toolchain provenance — dropping two
libraries and back-dating mpmath — as a pure side effect of where the gate was
run. The script's own trailer says "If a COUNT moved, the committed witness was
stale: commit the regenerated one", which is correct guidance that here would
have caused the corruption, because the real count movement rides along with
the bogus env stamp.

Fix options: mask the env block from the diff the way `scriptCommitSha` is
masked in `_EPHEMERAL_META_FIELDS`; or have the trailer warn explicitly that
the anchor-consistency witness carries an env stamp and must be regenerated in
a full environment.

I reverted all three rather than commit any of them — see the upstream
staleness recorded below, which someone with a complete environment should
regenerate.

## Two pre-existing REDs recorded (NOT caused by PR #5241, NOT fixed here)

  - **raw-float64 ratchet RED**: `computations/rho-k-co-casimir-extended.witness.json`
    REGRESSED 3 -> 4 raw float64 fields. That file is not touched anywhere on
    the PR #5241 branch (`git log origin/main..HEAD --name-only` does not list
    it), so this is live on main. Per the ratchet's own rule the fix is AT THE
    PRODUCER — do not baseline it.
  - **Stale committed audit witnesses on main**, counts measured 2026-08-16:
      witness-raw-float64-audit: dirty 1551 -> 1550, total_fields
        533831 -> 533830, drained_files 30 -> 31  (someone drained a file and
        did not regenerate the audit)
      q0-value-drift-audit: proton-pin 801 -> 800; chi-tritium-h9.witness.json
        left the list
      q0-anchor-consistency-audit: Q0_OK 653 -> 652, Q0_INDEPENDENT 5 -> 6,
        Q0_ANCHOR_MISSING 1885 -> 1886
    Regenerate in an environment that has scipy + clarabel, or defect 2 will
    corrupt the third one again.


## Defect 1 FIXED (PR #5474, 2026-08-22) — and it was in TWO scripts

Fixed as proposed: union `git diff --name-only $(git merge-base HEAD
origin/main)...HEAD` into the file-collection.

* `scripts/precision-gates.sh` (commit a315e8af05)
* `scripts/check-sidecars.sh:28` (commit a1f111e438) — SAME DEFECT, found
  by running it on a branch with three commits and being told "no changed
  files". Not in the original bean.

check-sidecars is the worse of the two. AGENTS.md names it as the
pre-commit preflight AND as the Phase-4 merge-time verification gate
("Content blocks changed -> check-sidecars.sh clean"). At merge time the
changes are ALWAYS committed, so as the merge gate — the one standing in
for CI while auto-triggers are off — it was reading an empty set and
reporting success.

Fixing it immediately surfaced a P30 in the file the same PR was editing
(the CODATA scan wrote its witness with raw json.dump, no provenance),
which is the argument for the fix in one line.

## Defect 2 STILL OPEN

q0-anchor-consistency-audit.witness.json still gets its `environment`
block rewritten to the runner's installed versions on every full run.
Reverted by hand twice on #5474 (no count moved, so the trailer's own
rule says drift). This bean stays open for it. Fix is still one of:
mask `environment` the way scriptCommitSha is masked in
_EPHEMERAL_META_FIELDS, or have the trailer name this witness
explicitly as env-stamped.
