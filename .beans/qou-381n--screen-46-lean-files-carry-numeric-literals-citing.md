---
# qou-381n
title: 'SCREEN: 46 Lean files carry numeric literals citing a producer whose witness no longer matches its source — 1 confirmed (JetOrderIndependence), 45 unverified'
status: todo
type: task
created_at: 2026-09-14T20:56:23Z
updated_at: 2026-09-14T21:13:06Z
---


## The claim

A Lean file that documents its constants as coming from a `computations/` script
is making a **provenance claim**, and nothing in this corpus checks it. When the
producer changes, the Lean keeps the old numbers and keeps the old sentence, and
everything still looks right: the theorems typecheck, the file compiles,
`#print axioms` is clean. Only the claim is false.

Measured on main `6229029329`:

```
corpus Lean files (excluding .lake)  : 3856
  ... carrying a numeric literal     : 2086
live producers under computations/   : 4434
witnesses carrying a scriptHash      : 3121

CANDIDATES (distinct lean/producer pairs) :  46      = 2.2% of 2086
  ... confirmed defects                   :   1
  ... unverified                          :  45
```

## The one confirmed instance, and how it hid

`QOU/Archimedean/JetOrderIndependence.lean` documents

```
jetJacobianBase = !![1/4, -1, 55/16; 1/2, 0, -1/16; 1, 0, 0]
```

as *"witnessed from the framework's own canonical Markov traces
(`computations/jet_order_pivots.py`)"*. Running that producer today gives
`!![1/4, 0, 11/4; 1/2, 1, 1/4; 1, 0, 0]` — elimination determinant **`−11/4`,
not the `1/16` the Lean carries**, LU pivots `(1/4, 1, −11)` rather than
`(1/4, 2, 1/8)`. Two of three rows moved; `Borromean` and the whole `h^0` column
did not. Producer drift, not import-cone: `scriptHash` `1eadd3f17d76` against
the witness's `380671554d5b`, witness dated 2026-06-08.

**Nothing is wrong, and that is the point.** `−11/4 ≠ 0` exactly as `1/16 ≠ 0`,
so jet-order independence still holds and every theorem in the file is still
true. The exposure is provenance alone.

**That file had been verified three separate times** — 2026-08-22, 2026-09-08,
2026-09-14 (`qou-1n7g`) — and none of the three caught it, including mine.
All three checked the **shape** of the discharge (is there a fabricated
instance?) and none re-ran the producer. Detail in `qou-xc8t`.

## Why nothing else covers this

The three nearest audits are each scoped away from it:

| audit | scope |
|---|---|
| `assertion_on_literal_audit.py` | Python witness assertions, not Lean |
| `hardcoded_literal_audit.py` | `rglob("*.py")`, and about CODATA constants |
| `lean_ref_resolution_audit.py` | `rglob("*.ts")`, resolution not values |

**Every literal audit in this corpus is Python-scoped** — the same shape as
`convention-c-producer-audit.py` walking only `*.py` while the Lean Markov-
parameter surface went uncounted for weeks. Candidate row for the
detector-blindness taxonomy, and it is a *scope* row, not a spelling one.

## The screen

[`computations/audits/lean_literal_producer_drift_screen.py`](computations/audits/lean_literal_producer_drift_screen.py).
Reports a Lean file when BOTH (1) it carries a rational or decimal literal and
(2) it names a `computations/` producer whose committed witness records a
`scriptHash` that no longer matches that producer's source. Read-only; writes
no witness and no file. `--selftest` PASSES by pinning the one confirmed
positive and **fails** if the screen stops reporting it — a calibration an audit
asserts about itself cannot discover its own blind spot.

**It is a screen, not a verdict, and condition 2 is weak.** AGENTS.md records
~700 self-stale witnesses corpus-wide of which essentially none is safe to
refresh, so a self-stale citation is the normal state. What the screen buys is
the *intersection*: a provenance claim, over numbers, whose source has moved.

Limits, stated so they are not rediscovered: association is by stem
(`<a-b-c>.witness.json` ↔ `<a_b_c>.py`), a producer with no witness is
invisible, `scriptHash` is a whole-file hash so comment-only edits drift it, and
**it cannot see import-cone drift** — a producer byte-stable while a module it
calls changed is not flagged (use `witness_import_cone_staleness_audit.py`).

**A defect found in the screen itself, recorded because it is the recurring
class.** The first draft did not exclude `.lake/` and reported *"11869 Lean
files scanned"* — **8013 of them Mathlib's own source**. The candidate count was
unaffected (no Mathlib file cites a `computations/*.py`) but every denominator
was inflated ~3×. Caught only by checking that the known positive appeared,
which required reading the head of the output rather than the tail.

## What I did NOT do

- **No hit was investigated beyond the one already known.** 45 are unverified.
- **Nothing is wired.** The screen exits 0 regardless; it is in no gate. Making
  it blocking needs a triage pass first, and most hits are probably benign.
- **No Lean literal was changed**, and none should be on the strength of a hit.
  Adopting a producer's current numbers assumes the producer is what is right;
  it may be what regressed. `qou-xc8t` enumerates that decision with options.

## Options

**A. Triage the 45** — read each hit's literals against a fresh producer run,
record a verdict per site in a committed ledger (the `lean-vacuity-review-ledger`
pattern). *Costs*: 45 producer runs, some expensive. *Risks*: none, it is
measurement. *Commits to*: keeping the ledger fresh as producers move.

**B. Wire it as an advisory line in `precision-gates.sh`** after A. *Costs*:
one line plus the scan's runtime (~90 s). *Risks*: a noisy advisory trains
readers to ignore advisories. *Commits to*: keeping the count near zero.

**C. Leave the screen committed and unwired** (the `qou-36i2` precedent — the
detector is on main, the wiring is gated). *Costs*: nothing. *Risks*: a detector
nobody invokes is documentation. *Commits to*: nothing.

**D. Do nothing further.** The 46 stay unmeasured and the next agent finds the
next one the way this one was found — by accident, three verifications in.

**Default is C**, which is where this bean leaves it.

**Recommendation, my judgement and not a finding: A, then decide B on what A
finds.** If most of the 45 are benign the class is not worth a gate and C is the
honest end state; if several are real then the provenance claim is systematically
unreliable and that is worth knowing before the next reader trusts one. A is
pure measurement and needs no permission — I stopped here for turn length, not
because it is gated.

## Blast radius

Confined to *what a reader believes about where a constant came from*. No
theorem, witness or content block changes on any hit. The reason it matters is
that these docstrings are exactly what a reviewer checks a Lean constant against
— the sentence is doing the work an audit would otherwise do, and on at least
one file it has been wrong for three months.

---

## 2026-09-14 (later) — stage 2 halves the queue, and the first verification is a SPLIT verdict

### Stage 2: 46 → 22, and the confirmed defect ranks first

Stage 1's signal is necessary and weak. The defect shape is sharper: **the Lean
literal matches the stale witness**, so the Lean is carrying that witness's data
and the producer has since moved. When none of a Lean file's literals appear
anywhere in the cited witness, the citation is a pointer (*"see this script"*),
not a provenance claim over numbers, and no producer run is needed.

```
stage-1 candidates                                      46
  NEEDS A FRESH RUN (Lean literal also in the witness)  22
  pointer, not a claim                                  24
```

**The filter calibrates.** Ranked by shared-literal count the one confirmed
defect is **first** — `JetOrderIndependence` at **5 of 5**, including `1/16` and
`55/16`, the two that moved. That ordering was not tuned for.

Top of the ranked queue:

| Lean file | producer | shared |
|---|---|---:|
| `JetOrderIndependence` | `jet_order_pivots` | **5/5** ← confirmed |
| `DepthStratifiedWeightRequirements` | `phi_k_weight_family_discriminator` | 4/4 |
| `M004AngleStructure` | `borromean_angle_structure_lp_probe` | 4/5 |
| `ModularDoubleReciprocity` | `qbeta_modular_double_reciprocity` | 4/7 |
| `MarginalRatioExtensivity` | `four_body_term_and_the_h12_collapse_probe` | 3/30 |

Folded into the screen as `--stage2`. The pointer bucket is a triage bucket, not
an all-clear: a Lean file could carry a number the producer emits in a form the
extractor does not match (different precision, a symbolic form).

### First verification — and the two halves disagree

Ran `phi_k_weight_family_discriminator.py` (rank 2) against
`DepthStratifiedWeightRequirements.lean`. **The two objects give opposite
answers, and conflating them would be the error.**

**The Lean docstring is CURRENT — a true negative.** Lines 118-119 record
`Σ_λ d_q²/[n]_q! = 0.991 / 1.111 / 1.517` at `n = 6 / 9 / 12`. The fresh run
prints `c_n by atom: D=0.99107952  T=1.1109231  3He=1.1109231  4He=1.5171332` —
`D` is `A=2, n=6`, `T`/`³He` are `A=3, n=9`, `⁴He` is `A=4, n=12`. **They
match.** These are the same figures AGENTS.md quotes in its `y_λ`
notation-collision rule, so that passage is current too. The screen flagged this
file and the check cleared it, which is the triage working rather than failing.

**But the WITNESS is a genuine positive, and it is not subtle.**
`computations/probes/phi-k-weight-family-discriminator.witness.json` moves
substantively on a fresh run — 113 lines changed:

| field | committed | fresh | move |
|---|---|---|---:|
| per-atom ratio `D` | 0.319160181993 | 0.260208414211 | −18.5 % |
| per-atom ratio `T` | 0.342478004989 | 0.410555725660 | +19.9 % |
| per-atom ratio `³He` | 0.355503230366 | 0.396317631720 | +11.5 % |
| per-atom ratio `⁴He` | 0.498568409744 | 0.318456126967 | **−36.1 %** |
| `max_over_min` (one block) | 1.50146673070 | 2.35943846094 | **+57.1 %** |
| `max_over_min` (other) | 1.56212597270 | 1.57779573310 | +1.0 % |
| **`allPassed`** | **`true`** | **`false`** | two assertions flip |

So the committed witness publishes `allPassed: true` for a configuration that
now **fails two of its eight assertions**, and per-atom numbers that have moved
by up to a third. That belongs to **`qou-oots`** — the open question of whether
`dim_q²` is the right numerator against the Molien `f^λ dim_q(λ)` — which is
exactly the territory these ratios decide.

**Environment is a live confound I have NOT excluded.** The diff also carries
`pyhecke_native_build: e3fab84c4c1df76a → 5df83fbc24b06f8a`, so this container's
native build differs from the one that wrote the witness. AGENTS.md's worked
case (`binding_canonical`) checked environment and found it inert; **I did not
do that check here**, so I cannot say whether the 36 % move is the producer or
the build. Anyone acting on this must run that discriminator first.

**The witness was reverted, not committed.** It is another arc's published
artifact, the fresh run FAILS two assertions, and adopting it would publish a
regression I do not own — three separate reasons, any one sufficient under the
2026-09-07 directive.

### What this changes for the triage

The first verified hit shows the screen's two failure modes are **independent**:
a Lean docstring can be current while its cited witness is badly stale. So the
triage should record **two verdicts per hit**, not one — *is the Lean's number
current?* and *is the witness's payload current?* — because the answer differed
on the very first case.

Running tally: **2 of 22 checked** — 1 Lean-side defect (`JetOrderIndependence`),
1 Lean-side clean with a witness-side finding (`phi_k_weight_family_discriminator`
→ `qou-oots`). 20 unverified.
