---
# qou-lz8f
title: A producer that cannot serialize an mpf DESTROYS its witness on every run — 38 candidates, and qou-geqa's crash class refills
status: in-progress
type: task
priority: high
created_at: 2026-09-13T17:29:26Z
updated_at: 2026-11-16T20:10:00Z
parent: qou-9nnz
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


## VERIFIED 2026-09-13 — all 37 run; 4 more are broken, 29 are clean

Ran every candidate with a 75 s timeout and `git checkout -- computations/`
after **each** run. The harness refuses to start on a dirty tree, and its
guard fired for real once (a leftover from a run whose restore could not
complete). Final tree: CLEAN.

    29  clean
     4  CONFIRMED-BROKEN      <- destroying their own witness on every run
     3  TIMEOUT (undecided)
     1  exit 77 (by design)

**The 4 confirmed:**

    computations/binding_bring_enhancement_compare.py
    computations/deltalambda/deltalambda_extensivity_gap_synthesis_probe.py
    computations/probes/he3_brane_tower_structural_gap.py
    computations/sweeps/low_isotope_binding_sweep.py     <- FIXED, 029254b6492

Plus `binding_ladder_catalog` already fixed, so **5 broken out of 38
candidates — a 13 % hit rate** for the static filter. Stated as the filter's
precision, not as a success rate.

**Two entries I first recorded as `other-crash` were MY CONTAINER, not their
code.** `option_e_canonical_reeb_v5` and `option_e_deuteron_delta_lambda_probe_v2`
died on `OSError: [Errno 28] No space left on device`; the session was at
**1.2 MB free**. Both re-run **clean** after cleanup. Recorded because
"crashed under measurement" and "is broken" are different claims and only one
of them was true.

*(The disk itself: 5.52 GiB of git `tmp_pack_*` garbage from a single
interrupted fetch on Sep 5, which `git count-objects` labels garbage outright.
Removing it took 1.2 MB -> 5.7 GB. Unrelated to this bean but it is what the
two false crashes were.)*

**3 undecided, and a timeout is not a verdict:** `canonical_tower`,
`mass_at_3A_proper`, `q_beta_complex_q_test1_phaseA` all exceeded 75 s. Re-run
with a real budget before calling them either way.

**`hyperbolic_volume_literal_audit` exits 77 by design** — an audit reporting
findings through its exit code. Not a defect; AGENTS.md's "a non-zero exit is
not a defect" case.

## What the low_isotope_binding_sweep fix showed, which generalises

Its `M_E_MEV = float(_M_E_MEV_MP)` carried the comment *"coerced to float for
json-serialisable arithmetic in this script"*. **The workaround for
mpf-unserialisability was to put the COMPUTE on float64** — and it is what
left the producer defenceless when a second mpf arrived without the same
coercion.

So this bean's class has a companion: not only "producers that crash on mpf",
but **"producers that were downcast to avoid crashing on mpf"**. The second
group does not crash, is invisible to this audit, and is quietly computing at
f64. Measured on the one case: the coercion moved `M_E_MEV` by **exactly 0.0**,
so it was buying nothing even on its own terms.

That is an argument for the shared-serializer fix at the top of this bean —
a `json.dump(..., default=fmt)` helper would remove the incentive for both
groups. Still an owner call.


## 2026-09-13, later — all 4 fixed; the class is closed at 5 of 38

    binding_ladder_catalog                     114 -> 0    a12aee299b0
    sweeps/low_isotope_binding_sweep           102 -> 21   029254b6492
    probes/he3_brane_tower_structural_gap        5 -> 0    5e2726c3c39
    binding_bring_enhancement_compare           39 -> 27   5e2726c3c39
    deltalambda/..._extensivity_gap_synthesis  SOURCE ONLY 5e2726c3c39

Every move in the four regenerated witnesses is the AME registry value
against the old hand-typed literal (8.99e-8 to 4.10e-7), reaching them for
the first time because their producers had been crashing. No verdict moves.

## Two mechanics worth carrying forward

**`isinstance(o, mp.mpf)` is not portable across these producers.**
`deltalambda_extensivity_gap_synthesis_probe` does `from mpmath import mp,
mpf, fabs`, where `mp` is mpmath's CONTEXT object, not the module. The test
there has to be the directly-imported `mpf`. Two of the four import the
module and one does not, so a copy-pasted `_ser` would have been silently
wrong in exactly one place.

**A producer can have more than one dump site, and the fatal one may not be
the write.** `he3_brane_tower_structural_gap` also does
`print("structural diagnosis:", json.dumps(structural, ...))`, holding the
same mpf, which dies BEFORE the witness write is reached.

## The one I did NOT regenerate, and why

`deltalambda_extensivity_gap_synthesis`'s regenerated witness moves
`B_base_MeV` for tritium **1.2648 -> 0.3209 (4x)**, `mu_ext_target`
6.71 -> 26.43, `err_pct` -85.1 -> -96.2.

**Not the fix.** The producer diff is one import, one `_ser` and one call
site; zero arithmetic. Its own line 138 already does `float(B_base)`, so
`_ser` touches only `B_AME_MeV` there -- 2 fields.

It is **9 days of import-cone drift**: last written 2026-09-04 by
`831980f1ce6` ("the nine y_lambda consumers re-run"), broken by
`70ae502091a` the next day, and the y_lambda chain has moved since --
`qou-za3q`'s Wenzl ruling landed on main this morning. Propagating a 4x move
in a published Delta_lambda magnitude belongs to that arc, not to an idle
pass. Source fix landed; witness left as recorded.

**Whoever picks that up: check it against the Wenzl ruling first**, since
AGENTS.md now records that re-weighting with the real Wenzl bridge FLIPS the
sign of P_total at A=3 and A=4.

## Separate defect found in that file, NOT fixed (Delta_lambda arc)

Its numerology-guard **print is hardcoded** --

    "4He doubly-magic needs the largest, 9.31; 3He the smallest, 3.29"

-- against the table the same run computes, **8.19 / 26.43 / 19.19 / 28.80**.
Not a rounding difference; the prose asserts a *non-monotone ordering claim*
("3He the smallest") that its own numbers no longer support. Same class as
the convention-C `c_k` analysis script whose hardcoded prose disagreed with
its computed table by six orders of magnitude.

## Final population accounting

    38  candidates from the regression vector
     5  CONFIRMED broken (13 % filter precision) -- ALL FIXED
    29  clean
     3  undecided on a 75 s timeout: canonical_tower, mass_at_3A_proper,
        q_beta_complex_q_test1_phaseA -- a timeout is not a verdict
     1  exit 77 by design (hyperbolic_volume_literal_audit reports findings
        through its exit code)

**The audit is scoped to two commits and this bean does not claim more.** A
producer broken by some third mpf-lifting pass is outside the filter. The
standing recommendation is unchanged and still an owner call: a shared
`json.dump(..., default=fmt)` helper would close the class rather than its
current members, and would also remove the incentive for the *companion*
class -- producers DOWNCAST to avoid the crash, which do not fail, are
invisible here, and quietly compute at f64.


## 2026-09-14 — a SIXTH broken producer, and it is a DIFFERENT class

`brane_tower_isospin_diagnosis` exits 1 in 3.2 s with
`TypeError: unhashable type: 'dict'` at
`phi_vals = [float(Phi_q(v)) for v in vols]`.

**This bean's audit cannot see it, correctly.** The five here die at
`json.dump`; this one dies **before writing** — 0 files touched, so it is
**non-destructive**. `mpf_json_encoder_audit` keys on serialization and this
is a *call-signature* failure, so the miss is a scope boundary, not a blind
spot.

**Same half-done shape as everything else in this arc, though.**
`atom_per_generator_volumes` used to return a bare scalar per generator and
now returns a dict (`std`/`sym`/`alt`/`full`, values as decimal strings).
`abs_mpf` in that same file was adapted —

    x = v["full"] if isinstance(v, dict) else v

— and the line that uses it, `abs_vols = [...]`, is *immediately above* the
line that passes the raw dict to `Phi_q`. **One line adapted, its neighbour
not.** Fixed in `ce2eef20bf1` by factoring the unwrap into `scalar_mpf()` so
the two callers cannot drift apart again; `full` is not a choice I made, it
is the one `abs_mpf` already made.

**Its witness is NOT regenerated** — a re-run moves `phi_q_per_gen` by up to
**rel 23.92** and `sum_phi_q` by 14.47 across 90 fields, because the witness
predates the API change entirely. Those numbers are the *subject* of the
document (the −737 MeV Φ_q pathology), so restating them belongs to the
Φ_q / Li_2^q migration arc.

## The class the audit CAN see is unchanged: still 5, still all fixed

Nothing new found in that class. What this adds is the boundary: **"a
producer broken by an upstream change" is strictly larger than "a producer
that cannot serialize an mpf"**, and the second is the only part with a
detector. The general population is producers that have not been run since
something upstream of them changed shape — signature, return type, or
value — and the only screen that finds those is running them.

Which this session has been doing one at a time, as screen step (d) of the
drain: baseline the unmodified producer BEFORE editing. That step has now
produced four separate findings it was not looking for (`adjacent-vs-full`'s
270-field drift, `deltalambda_extensivity`'s 4×, this one's 24×, and this
crash). **It is the highest-yield step in the screen and it costs one run.**

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-9nnz`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.


## Round 48 Execution Update (2026-11-16, PR #8161)

- **PR:** https://github.com/litlfred/qou/pull/8161 (`38bc15fe7214bb6951d6acb18fa8c8d7d32d5225`)
- **Action taken:**
  - Updated `computations/audits/mpf_json_encoder_audit.py` so `_analyse_source` recognises sanitizer-wrapped payloads (`json.dumps(_ser(witness), ...)` / `json.dump(_ser(wit), ...)`, the repair idiom across the 5 confirmed producers in `qou-lz8f`), excludes `.claude`/`.lake` worktrees, and supports `--self-test` / `--selftest`.
- **Status:** Kept `in-progress` pending PR #8161 merge and owner review.
