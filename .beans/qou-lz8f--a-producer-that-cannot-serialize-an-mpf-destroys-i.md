---
# qou-lz8f
title: A producer that cannot serialize an mpf DESTROYS its witness on every run — 38 candidates, and qou-geqa's crash class refills
status: todo
type: task
priority: high
created_at: 2026-09-13T17:29:26Z
updated_at: 2026-09-13T17:30:03Z
---

## The defect, measured

`computations/binding_ladder_catalog.py` on `main`:

    $ python3 binding_ladder_catalog.py
    TypeError: Object of type mpf is not JSON serializable
    exit 1
    witness: 7352 bytes -> 491 bytes

It dies at `"B_AME_MeV"` on the first isotope. **The failure is destructive,
not merely unsuccessful**, and that is the property that makes this class
worth its own bean: the corpus witness idiom is

    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2)

and `open(..., "w")` **truncates the file before `json.dump` can raise**. So
every run of a producer in this state deletes 93 % of its own recorded output.

FIXED for this producer (PR #7318, commit `a12aee299b0`): carry `mpf` end to
end, serialize via `_precision.fmt` — which the file had imported and never
used. 114 raw-float64 fields drained to 0 as a side effect.

## Nobody wrote this bug — it arrives from upstream

Two *correct* precision fixes made the values `mpf` and neither re-ran the
consumer:

| commit | change | effect here |
|---|---|---|
| `70ae502091a` (`qou-psjm`, 2026-09-05) | 372 AME/CODATA literals -> registry, 178 files | **fatal** — line 152 `"B_AME_MeV": B_AME` had no cast |
| `2b74577a65d` (`qou-ckbv`, 2026-08-30) | volume registry -> `mpf` | absorbed by line 154's `float(leading)` |

## Why this is NOT covered by qou-geqa, and what that says

`qou-geqa` ("24 producers on main cannot complete") ran a
`PYTHONPATH`-equipped runner, corrected 14 crashes down to 2 real defects, and
recorded **"count closes at 0 outstanding"** on **2026-08-24**.
`binding_ladder_catalog` is not named in it — correctly, because it did not
break until **2026-09-05**.

**So the class REFILLS.** A crash census is a photograph, and every
mpf-lifting pass that does not re-run its consumers takes a new one out of
date. Same shape as `qou-ldwx` ("main's inherited ratchet red is a RECURRING
source, not one file"). A closed count here means *drained on that date*, never
*fixed*.

## The detector, and the false-alarm flood it started as

[`computations/audits/mpf_json_encoder_audit.py`](computations/audits/mpf_json_encoder_audit.py),
commit `26b8dea2e51`.

**Static by necessity — this is the load-bearing constraint.** You cannot
screen for the bug by running the candidates, because running them is what
does the damage.

**First attempt was useless and the module docstring records it.** Keying "can
hold an mpf" on `import mpmath` flagged essentially every producer in the tree.
That is a false-alarm flood, and it ends a search as effectively as a false
all-clear — it is the over-matching twin of the detector-blindness taxonomy's
row 40.

The fix was to target the regression **vector** rather than the capability:

    196   python files touched by 70ae502091a + 2b74577a65d
     38   of those, serializing via json.dump* with NO default=

38 is tractable, and it contains `binding_ladder_catalog` — the case
independently proved broken, which is the only calibration the filter has.

`default=str` is the corpus's existing escape hatch and is why sibling
producers with identical imports survive; `adjacent_vs_full_probe` is the
worked example (`json.dumps(witness, indent=2, default=str)`).

## What is NOT established

**A candidate is not a proof.** The `mpf` must actually reach the dumped
object, which depends on control flow the audit does not follow. Of the 38,
exactly **1 is confirmed** (this one). The other 37 are unverified.

The audit is also scoped to the two named commits. A producer broken by some
*third* mpf-lifting pass is outside its filter and this bean does not claim
otherwise.

## Next

Verify the 37, one at a time, using the protocol in the docstring:

    cp <witness> /tmp/backup.json       # or rely on git being clean
    python3 <producer>                  # observe
    git checkout -- computations/       # restore EVERYTHING, not one file --
                                        # producers write sibling witnesses

Budget the run: some are long-compute, and a timeout is not a verdict.
Classify honestly as CONFIRMED / clean / undecided-on-timeout.

Consider also whether the real fix is upstream of all 38: a shared
`json.dump(..., default=fmt)` helper, so an mpf lift can never again reach a
producer that cannot write it. That is a design change and an owner call, not
an idle-pass action.
