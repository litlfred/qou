---
# qou-cg1b
title: qbeta-habiro-residual witness ships a 30x failed assertion — the 112th recorded-failure witness
status: todo
type: bug
created_at: 2026-08-21T16:38:18Z
updated_at: 2026-08-21T16:38:18Z
---

Found by `/prepare-merge-auto` on PR #5342 (2026-08-21). **Not that branch's
defect** — landed on `main` the same day by `ae571e445d`
("qbeta_habiro_residual -> PROTON (owner ruling)").

## The offender

`computations/probes/qbeta-habiro-residual.witness.json`

    Q_A_witness_matches_live_single_wrap
      computed  = 29.959
      expected  = 0.0
      tolerance = 1.0
      passed    = false

A committed witness asserting agreement, recording **~30× the tolerance**, and
shipping anyway. This is not a tolerance nudge: at 30× the assertion is not
"close but outside" — whatever it compares does not agree at all.

## Why it matters beyond one witness

It is the **112th** entry in the recorded-failure class of `qou-ad4t`, and it
arrived *after* `witness_failed_assertion_audit.py` was baselined at 111. That
timing is the whole point of the ratchet: the baseline records history, and a
new arrival is supposed to fire.

It did — and its first act was to block the merge of the PR that introduced it,
because a blocking gate red for a reason the branch did not cause would have
made `scripts/precision-gates.sh` exit 1 on `main` for every other agent. The
gate was therefore landed **advisory with an explicit flip-to-blocking-at-0
note** (owner decision, 2026-08-21). **Draining this witness is one of the two
things standing between that gate and blocking.**

## What NOT to do

- **Do not add it to `witness-failed-assertion-baseline.json`.** The ratchet
  drains and never grows (AGENTS.md). A baseline that absorbs each new arrival
  is not a ratchet, and this one would be absorbing the very first arrival it
  was built to catch.
- **Do not widen the tolerance to 30.** Same rule, and see `qou-4e5k` for what
  a tolerance sized to fit an unexplained residual does: it converts a detector
  into a rationalisation that passes forever.

## Ownership

Belongs to the live qbeta proton re-pin arc — cf. **#5386**, whose own summary
says *"its committed witness does not reproduce"*, i.e. that arc is already
looking at this object. Filed separately anyway because no bean named this
witness, and the prepare-merge agent's report treated it as owned when it was
only adjacent. The fix is a re-derivation on that arc's schedule, not an edit
from outside it.

## RECOVERY — the advisory-flip patch, carried here because `git push` is down

The companion change to `scripts/precision-gates.sh` is committed locally
(`1d3759873e`, rebased onto `origin/main`) and is **NOT on origin**. The git
proxy returns 502/503 to CONNECT on `github.com` — `/__agentproxy/status` reports
*"gateway answered 503 to CONNECT (policy denial or upstream failure)"* — across
six attempts in two windows. The GitHub API path still works, which is how this
file lands.

The script itself was deliberately **not** pushed through the API: 17.7 KB /
~450 lines of shell, re-transcribed by hand into a tool call, risks corrupting
the script that gates every precision check in the repo. That is strictly worse
than leaving it unpushed. The patch is 29 added lines replacing one, so carrying
it verbatim is equivalent for recovery with none of that risk.

Apply to `scripts/precision-gates.sh`. The only functional change is the gate
row's last field, `yes` -> `no`:

```diff
@@ -88,7 +88,34 @@ GATES=(
   # Counts shrink, never grow. Drain triage is bean qou-ad4t; the category to
   # identify first is the probe that records an EXPECTED negative, since every
   # such witness teaches readers that red is normal.
-  "witness failed-assertion ratchet|computations/witness_failed_assertion_audit.py|--strict|yes|yes"
+  #
+  # ADVISORY ON ARRIVAL, AND THIS IS THE FLIP-TO-BLOCKING NOTE.
+  # ----------------------------------------------------------
+  # FLIP TO BLOCKING WHEN THE NEW-OFFENDER COUNT REACHES 0 — i.e. when a plain
+  # run reports no witness outside the baseline. Same terms as the
+  # audits-tree entry above, and the same precedent this file set for its
+  # red-on-arrival provenance gate.
+  #
+  # It was authored BLOCKING and green at 111. Between authoring and merge,
+  # `main` gained a 112th (`computations/probes/qbeta-habiro-residual.witness.json`,
+  # `Q_A_witness_matches_live_single_wrap computed=29.959 expected=0.0
+  # tolerance=1.0`, landed by ae571e445d). Shipping it blocking would therefore
+  # have made THIS SCRIPT exit 1 on `main` for every other agent — over a
+  # witness that has nothing to do with the branch introducing the gate.
+  #
+  # That is the failure this gate exists to prevent, arriving one level up: a
+  # preflight that is red for reasons you did not cause is a preflight you
+  # learn to skip. Advisory keeps the signal and costs nobody a red run.
+  #
+  # The two shortcuts were BOTH refused, and neither should be taken later:
+  #   * do NOT add the offender to the baseline — the ratchet drains and never
+  #     grows (AGENTS.md), and a baseline that absorbs each new arrival is not
+  #     a ratchet;
+  #   * do NOT "fix" qbeta-habiro-residual to clear this — it is a 30x
+  #     residual, not a tolerance nudge, and it belongs to the live qbeta
+  #     proton re-pin arc (#5386). Editing it steps on a sibling mid-flight.
+  # Drain owners: bean qou-6ort (the dps defect) and the qbeta re-pin arc.
+  "witness failed-assertion ratchet|computations/witness_failed_assertion_audit.py|--strict|yes|no"
   # Blocking, and GREEN as of the commit that added it (0 candidates across
   # 273 numpy-importing files) — which is exactly when a gate is safe to make
   # blocking, because it can then only ever fire on a NEW regression.
```

Verified before the push failed: with this applied, `precision-gates.sh` reports
the failed-assertion ratchet under ADVISORY, and the only remaining blocking
reds are the two inherited `qbeta_ohtsuki_sixone_kappa_series.py:166` gates
(`qou-xbh4`) — which are red on `main` independently of any branch.
