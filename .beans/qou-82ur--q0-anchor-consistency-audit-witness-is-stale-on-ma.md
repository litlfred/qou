---
# qou-82ur
title: 'q0-anchor-consistency audit witness was stale: the movement is newly-scanned files, NOT reclassification (closed 2026-08-25)'
status: completed
type: task
priority: normal
created_at: 2026-08-16T12:56:54Z
updated_at: 2026-08-25T18:37:27Z
---

Surfaced by running scripts/precision-gates.sh on a clean checkout of main (PR #5229 branch, no relevant changes of my own — my new file is not even scanned; 'wenzl' appears 0 times in the diff). So this is PRE-EXISTING staleness on main, not branch drift.

Three committed audit witnesses regenerate differently from their committed copies:
  computations/audits/q0-anchor-consistency-audit.witness.json
  computations/q0-value-drift-audit.witness.json
  computations/witness-raw-float64-audit.witness.json

COUNTS moved, not just computedAt/commitSha/durationMs — so per the gate's own
rule this is genuine staleness, not the ignorable drift class:
  Q0_OK              653 -> 652
  Q0_ANCHOR_MISSING 1885 -> 1886
  Q0_INDEPENDENT       5 -> 6
  (total scanned 2543 -> 2544, i.e. one newly-scanned file plus one
   reclassification)

The two entries that moved are chi-tritium-h9.witness.json — which LOSES
"class": "proton-pin" and its ppb_vs_canonical: -11.537117889987831 — and
markov-identity-symbolic.witness.json, which is newly listed.

DELIBERATELY NOT FIXED on PR #5229. That PR is a science PR the owner is
reviewing (Wenzl level family); landing an unexplained q0-anchor
RECLASSIFICATION inside it would be noise at best and a hidden change at worst.
The chi-tritium-h9 line in particular touches the muon/proton pin bookkeeping
(-11.537 ppb is the mu-p substrate tension) and deserves its own look rather
than riding along in a diff about Hecke traces.

Next step: work out which upstream commit changed chi-tritium-h9's anchor
classification, confirm the new counts are correct, then commit the regenerated
witnesses as a chore(witness) commit naming the counts.


## Re-measured 2026-08-25 on `main` @ 5483aa95f — and the "confirm the counts" blocker is partly discharged

Reached independently while merge-verifying #5754, before finding this bean.
The staleness persists nine days on, and the corpus has moved underneath it, so
the 2026-08-16 figures above are themselves stale — do not chase them:

    2026-08-16 (this bean)  Q0_OK  653 -> 652    total scanned 2543 -> 2544
    2026-08-25 (today)      Q0_OK  963 -> 970    total scanned ~2758

### The next step asks to "confirm the new counts are correct". Here is that confirmation, for one dimension.

A sibling agent on PR #5770 reached `Q0_OK = 970` from an unrelated branch and
**reverted** the regenerated witnesses, on the reading that a bare container had
contaminated them (no `numpy`/`scipy`/`sympy`/`clarabel` installed, `mpmath
1.4.1` against the corpus's `1.3.0`).

That reading is right about the `environment` block and **wrong about the
counts**, which is the half that matters here. My container has a materially
different profile — `mpmath 1.3.0`, plus `numpy 2.4.6` / `scipy 1.17.1` /
`sympy 1.14.0` all present — and reproduces **970** exactly. Two containers
disagreeing on four packages and an mpmath minor version, same number.

Structurally they must, and this is the part worth keeping:

  * `witness_raw_float64_audit.py` imports `argparse`, `json`, `sys`,
    `pathlib`. Nothing else, no `subprocess`, no `importlib`.
  * `q0_anchor_consistency_audit.py` imports the same four, plus
    `witness_base.WitnessBuilder` and `qou_substrate.witness` to emit.

Neither imports a numerical library; neither invokes a producer. They **scan
committed JSON and count**. A count produced that way cannot vary with the
installed package set, so the counts are corpus facts and `963` is simply
stale.

### What this changes about the fix

The instinct to revert from a bare container is backwards for these files.
Reverting preserves a wrong count, and every future bare container will keep
re-deriving the same correct-but-unclaimable number. The right move is the one
already written above — regenerate and commit as `chore(witness)` naming the
counts — with one added constraint: do it from a container whose `environment`
block is faithful, so the counts land without the provenance lying beside them.

### Still open, and deliberately not claimed

I did not identify *which* 7 witnesses moved, and did not check whether
`STALE 229 -> 228` shares the explanation. Both look like the same staleness;
neither is measured. The `chi-tritium-h9` anchor-reclassification question in
the original finding is untouched and remains the substantive part of this
bean — the environment argument above says the counts are trustworthy, not
that the reclassification is understood.


## CLOSED 2026-08-25 — and the original premise was wrong

Regenerated and committed on `main` @ `4399ec0a3`. All three of this bean's
strands are now settled, and the headline one is settled by **refutation**.

### 1. There is no reclassification. There never was one, today.

The entry above frames this as an anchor RECLASSIFICATION and sets the next
step as *"work out which upstream commit changed chi-tritium-h9's anchor
classification"*. Diffed the committed `by_verdict` lists against a fresh run,
per witness:

    RECLASSIFIED        0
    NO LONGER PRESENT   0
    NEWLY SCANNED      19   ->  7 Q0_OK, 11 Q0_ANCHOR_MISSING, 1 Q0_AUDIT_EXEMPT

which is exactly the `+7 / +11 / +1` deltas. **Every count movement is the
corpus growing under a stale audit witness.** Not one existing witness changed
verdict.

The seven that made `Q0_OK 963 -> 970`:

    binding-channel-convention-exposure      mu3-door-budget
    binding-closed-form-c-vs-d               mu3-door-sign-c-vs-d
    binding-production-route-c-vs-d-deut     qbeta-d-frame-eigenphase-window
    binding-sum-c-vs-d-deut

### 2. `chi-tritium-h9` is stable — the named next step has no live subject

`Q0_ANCHOR_MISSING` in **both** the committed and the fresh classification, as
is `chi-tritium-h9-at-qinv-50dps`; the two `-at-q0-50dps` siblings are `Q0_OK`
in both. `markov-identity-symbolic` is `Q0_INDEPENDENT` in both. Whatever was
seen on 2026-08-16, none of these is moving now, so there is no upstream commit
to hunt. The file does carry no `q0Anchor`/`q0Value` — a separate, static
condition, not a reclassification.

### 3. Regenerated from an environment-matched container

The remaining actionable step. The sibling warning on #5768 was that a bare
container writes a lying `environment` block. Checked rather than assumed: this
container was missing `clarabel` (committed `0.11.1`, mine absent), so
`clarabel` was installed to `0.11.1` before the run that produced the committed
artifact. Post-install the block matches the previous one on every key —
`mpmath 1.3.0`, `numpy 2.4.6`, `scipy 1.17.1`, `sympy 1.14.0`,
`python 3.11.15`, `pyhecke_native 0.9.0`, `clarabel 0.11.1` — with one
exception, `pyhecke_native_build b843d058d29dcec6 -> c7ea7ebb0d76c4e2`. That is
a build hash of the *same* version of a locally-compiled extension; no second
container can reproduce it, and the recorded value is truthful.

Diff: 19 added witness entries plus `computedAt` / `commitSha` / `durationMs` /
the build hash. `allPassed` stays true; the audit's only assertion,
`no_q0_flip`, is 0 as before.

### Checked and NOT a finding

`Q0_ANCHOR_MISSING` is **1638 of 2758** (59 %) and the audit's sole assertion
passes, so it is informational, not a defect verdict. I had suspected the five
witnesses drained earlier that day had lost their q0 provenance to the drain;
they had not — `q0Anchor` is absent in **all** their revisions including
original creation (`f618127f3`), so the drain removed nothing. Recorded because
it is the more interesting-sounding hypothesis and it is false.


### Addendum — the refresh went stale inside 20 minutes, and that is the real lesson

Rebased to `main` @ `13fa0e0e3` before merge and re-ran. One witness had landed
in the interval (`qbeta-route76-strategy-matrix`, no `q0Anchor`), so:

    total              2758 -> 2759
    Q0_ANCHOR_MISSING  1638 -> 1639
    Q0_OK               970 (unchanged)

Caught only because I re-checked. My first check missed it: I used the pathspec
`'computations/**/*.witness.json'` with `--diff-filter=A`, which matched
nothing and reported "0 witnesses added" — a **glob artifact read as a fact**,
exactly the shape this bean is otherwise about. A plain `computations/`
pathspec found it immediately.

The substantive point: **this artifact is stale the moment any producer emits a
witness.** It was 9 days stale when the bean opened, and it went stale again in
under 20 minutes here. So "regenerate the audit witness" is a treadmill, not a
fix, and the count in a committed audit witness should never be quoted without
re-running — which is the same conclusion `qou-mnrd` reached from the other
side, and the same missing enforcement: nothing regenerates this on a push
because CI is `workflow_dispatch`-only.

Closing this bean anyway. Its three stated strands are answered; what remains
is not a q0-anchor question at all, it is the absent-enforcement item.
