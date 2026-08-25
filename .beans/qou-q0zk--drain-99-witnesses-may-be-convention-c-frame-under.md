---
# qou-q0zk
title: 'DRAIN: 99 witnesses may be convention-C-frame under D producers (#4899 sweep tail)'
status: todo
type: task
priority: normal
created_at: 2026-08-19T20:13:39Z
updated_at: 2026-08-23T17:04:24Z
---

PR #4899 excised convention C from the producer layer ("178 sites -> 0") and
reported "witnesses regenerated across 68 producers". **Two witnesses it missed
were found independently, by two sessions, from different directions:**

* `qou-580o` — a `qbeta` witness, found auditing the c_3 ladder (PR #5265).
* `qou-h4ab` — `wedderburn-lp-ew-wiring`, found porting that producer off
  float64; `t_legacy_matrix_entries` moved 13-21%.

Two independent hand-finds of one class is the signal the class is not two
items long. New scanner: [`computations/convention_frame_staleness_audit.py`].

## Measured

    producers with a D-form bound to a Markov-named variable : 137
    their witnesses                                          : 138
    witness predates the 2026-08-10 migration                : 101
    ... and producer changed since (SUSPECT)                 :  99
    ... dropped, producer unchanged (same D code wrote it)   :   2

## Confirmed by the decisive test, 2 of 2 attempted

The test is: swap the producer's `z` back to the C form and check the
**committed** value reappears.

| witness | committed | conv D | conv C |
|---|---|---|---|
| `wedderburn-lp-ew-wiring` (proton) | 0.6003377241833765 | 0.68036969746 | **2.1e-16** |
| `wedderburn-lp-ew-wiring` (neutron) | 0.3727036271108378 | 0.44938418327 | **5.7e-16** |
| `fr-pullback-cosh-h` `best_variance_finite` | 1.537500801376956 | 1.488319082475366 | **1.537500801376956 exact** |

`fr-pullback-cosh-h` was found BY the scan and then confirmed, which is what
makes the scan worth trusting rather than a grep someone ran once. Its
producer + witness were restored after the test; nothing committed from it.

## What the 99 is NOT

A count of confirmed-stale witnesses. It is a **high-recall candidate list**,
same standing as the lean-vacuity candidates and the raw-float64 ratchet — the
verdict is an agent call, per candidate. Specifically:

* `q**3/(q**2+1)` is a shape, not a meaning. The scan requires it bound to a
  Markov-NAMED variable (`z`, `z_mark`, `z_D`, `z_electron`, ...). A producer
  computing the Markov parameter under another name is **missed** — so 99 is
  also not an upper bound.
* "witness predates the migration" does not prove its values are C-frame; the
  producer may not use `z` in anything serialized.
* `scriptHash` matching means the producer is unchanged, so that same D code
  wrote the witness. Those 2 are dropped, not counted.

## Do NOT bulk-regenerate

Re-running `fr_pullback_cosh_h_test.py` alone dirtied its witness with **40
raw float64 fields** and dropped `clarabel` from the environment block (main's
new `_check_environment_regression` caught it). A 99-file sweep in this
container would import that damage wholesale. Each item needs: decisive test
-> confirm -> regenerate in an environment that matches the recorded one ->
check the raw-float64 ratchet did not grow.

Related: `qou-1c4y` (the muon->proton witness migration) has the same
"large tracked sweep, needs scoped sign-off" shape.


## 2026-08-23 — re-measured after merging main, and RANKED

**73, down from 99.** Main drained 26 of the candidates during the four days
this branch was open — independent corroboration that the detector tracks a
real class rather than a grep artifact.

**Every one of the 73 is CONSUMED.** Ranked by in-corpus references
(`_deprecated/` consumers excluded, since those do not matter):

| refs | witness | reached by |
|---|---|---|
| content 2 | `alpha-k-jones-markov-h3` | `explicit-alpha-k-h3-proof.md`, `categorical-mass-markov-proof.ts`, `codata_reconciliation.py` |
| content 2 | `wedderburn-pair-volumes` | `knot-operator-lp-selection.ts` + `.qa.json` |
| content 2 | `probes/gauge-coupling-uniqueness-probe` | `gauge-coupling-uniqueness.ts` + proof `.qa.json` |
| content 1, code 22 | `free-neutron-decay` | `energy-scale-planck.qa.json`, `beta-decay-energy-scale.py` |
| content 1, code 7 | `binding-depth-stratified` | `depth-stratified-frobenius-reciprocity.ts`, `low_isotope_binding_model_comparison.py` |
| content 1, code 2 | `demazure-markov-trace` | `demazure-fiber-markov-trace.ts`, **`onepb_status_dashboard.py`** |
| content 1, code 2 | `qbeta/qbeta-c3even-exact-sseries` | `binding-qbeta-complex-volume.md` |

**0 of 73 are terminal probes.** So this is not a backwater: the class reaches
content blocks (the paper itself), the **L1 status dashboard**, and the CODATA
reconciliation.

### What this ranking does and does not establish

It says **which to check first**, not that any of them is stale. Consumption
is a priority signal, not evidence. The confirmed count is still **2 of 2
attempted** (`wedderburn-lp-ew-wiring`, `fr-pullback-cosh-h`) — every other
row needs its own decisive test (swap `z` to the C form, check the committed
value reappears) before being called anything.

Suggested order for a drainer: the three content-cited rows first, since a
stale frame there propagates into the paper rather than into another probe.


## CONFIRMED #3 — `wedderburn-pair-volumes`, and it is cited by a content block

The top-ranked content-cited candidate, tested decisively:

    committed (2026-06-12)   full = 0.6003376915089118
    convention C, proton pin        0.60033769150891203   rel 3.70e-16
    convention D (current code)     0.68036965422380191   rel 0.1333

C-frame, confirmed to machine zero. Cited by
`content/quantum-observable-universe/mass-theory/knot-operator-lp-selection.ts`
and its `.qa.json`.

**Confirmed count is now 3 of 3 attempted** — the detector has not produced a
false positive yet, though three is a small sample and the list is still
CANDIDATES, not findings.

Two things I had wrong going in, worth recording:

* I expected the residual 8th-digit gap from my earlier C value to be a muon
  pin, since 2026-06-12 predates the proton migration. It is not — the
  witness is already proton-pinned (module `q0 = 1.1099785827513808`), and
  C+proton reproduces it exactly. The gap was between two different C
  evaluations, not two pins.
* The frame was decidable by INSPECTION before running anything: 0.60 against
  D's 0.68 is a 13% gap. The run only settled the pin question.

### NOT regenerated, deliberately

Regenerating this one moves a **content-cited** number by 13%, which stales
the block's `.qa.json` sidecar and may contradict figures quoted in the `.md`.
That is the drain itself, not a ride-along fix, and it needs a scope decision
before it runs — same standing as `qou-1c4y`.


## 2026-08-24 — 63 now; CONFIRMED #4, and its mechanism is NOT the producer

Re-ran the detector on current `main`: **63**, down from 73 (2026-08-23) and 99
(2026-08-19). Main keeps draining; the trend is the third independent sign the
class is real rather than a grep artifact.

### Confirmed #4: `alpha-k-jones-markov-h3` — decidable by inspection, no swap needed

The other three confirmations needed the decisive test (swap `z` back to C,
check the committed value reappears). This one does not: the witness
**serialises `z` itself**.

    computations/alpha-k-jones-markov-h3.witness.json        z = 0.4993203341836944   <- C
    computations/alpha/alpha-k-jones-markov-h3.witness.json  z = 0.6126880371464652   <- D

Both files exist, same basename, different directories, identical key
structure. **Confirmed count 4 of 4 attempted.**

### The mechanism is different from #1-#3, and that matters

For the first three the producer emitted C. Here the producer emits **D** —
`computations/alpha/alpha_k_jones_markov_h3.py` is proton-pinned, current
`scriptHash`, and writes *next to itself* under `alpha/`. The C values live in
a 2026-05-30 orphan at the top level that **no producer writes any more**, and
that orphan is the copy consumers read.

This is a candidate answer to this bean's own open question — *"11/41 producers
re-run, not one witness moved C->D"*. A producer whose output path differs from
the consumed path cannot move the consumed witness however many times it is
re-run.

**But it explains 1 of 63, not the class.** Tested corpus-wide: exactly one
candidate has a live (non-`_deprecated`) same-basename twin. That makes this
the fourth consecutive time in this arc that a plausible shared mechanism
turned out to have single-file scope — the same pattern `qou-pvem` records for
the DEAD_TOL sub-class.

### REDISCOVERY, not a find — `qou-kcii` already owns this

`qou-kcii` measured **25 duplicated witness stems** in `computations/`, all 25
with differing payloads, and lists `alpha-k-jones-markov-h3  None vs proton`
explicitly. I ran the corpus-grep after finding this rather than before, which
is the wrong order and exactly the mistake `qou-nr8y` records one bean over.

What is **new** on top of `qou-kcii`, and worth carrying back to it:

1. For this stem the payload difference **is a convention frame** (C vs D), not
   just the anchor label `qou-kcii` records. For the h4 twin it is *both*: C
   **and** the muon pin (`q_0 = 1.10997859555418` vs proton
   `1.10997858275138`), with nonzero 3+-row weights `(1,1,1,1) = -8.4e-4`,
   `(2,1,1) = 2.4e-2` against D's ~1e-17.
2. **A confirmed live instance.** `qou-kcii` scopes its consumer finding
   carefully — *"this is the capability to pick wrong; I have NOT established
   that any of the six currently resolves one of the 25 ambiguous stems"*.
   `computations/codata_reconciliation.py` did, and it is a **seventh**
   mechanism its list does not cover: not `rglob`, a **hardcoded path**.

### What was actually fixed here, stated precisely

The `alpha_2 = z^2` row in `codata_reconciliation` is **convention-invariant** —
it compares a witness against *its own* `z` — so it passed on either copy and
the residual only moves `2.78e-17 -> 5.55e-17`, both machine zero. **No number
was wrong.** What was wrong is *provenance*: the row named a muon-pinned,
C-frame, no-longer-written file as its `predicted_source`, so an auditor
following that citation lands on the wrong frame. That is what the repoint
fixes, and it should not be described as a numerical correction.

The content block `explicit-alpha-k-h3-proof.md` quotes **no numerals** — its
claims are the symbolic `alpha_2 = z^2`, `alpha_3 = h z^2 + z`, which hold for
any `z` by the Markov axioms. Repointing its link costs nothing downstream.

### NOT changed, and this is the important half

`computations/h4_markov_weights_closed_form.py` reads the **top-level (C-frame,
muon)** h4 witness and looks like the identical defect. It is not. It hardcodes
`XCHECK_Z = "0.49932033403359827"` and `XCHECK_WEIGHTS` transcribed from that
witness, and evaluates its symbolic closed forms at *that* `(q_0, z)` to show
they reproduce the published record — then evaluates at the proton anchor
separately. It is a **reproduction cross-check**: it uses C deliberately.
Repointing it would have broken a working control.

That is precisely the hazard `qou-a6yh` names, and I walked up to it one file
after concluding the control-arm caution did not apply here. **My intersection
test was at the wrong layer**: I compared the 63 candidate *witnesses* against
the fingerprint detector's control arms (intersection empty, correctly) and
concluded there were none. The control arm here is a **consumer**, not a
witness. A drain that classifies witnesses and repoints consumers mechanically
will break controls that no witness-level test can see.

### Still not drained, deliberately

`wedderburn-pair-volumes` (confirmed #3) still moves a content-cited number by
13% and still needs the scope decision. Unchanged from 2026-08-23.
