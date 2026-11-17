---
# qou-381n
title: 'SCREEN: 46 Lean files carry numeric literals citing a producer whose witness no longer matches its source — 1 confirmed (JetOrderIndependence), 45 unverified'
status: in-progress
pr: 8350
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T20:56:23Z
updated_at: 2026-10-04T15:24:21Z
parent: qou-5vkl
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

---

## 2026-09-14 (later still) — 🛑 ZERO of the 22 can be re-run interpretably in this container

The first verification flagged environment as an unexcluded confound. Measuring
it across the whole stage-2 queue changes the triage plan rather than refining
it.

```
stage-2 'needs a fresh producer run' candidates : 22
  environment MATCHES (re-run interpretable)    :  0
  environment DIFFERS (a move is confounded)    : 13
  no environment block (cannot tell)            :  9
```

**Not one.** Every re-run this container can perform produces a number whose
movement cannot be attributed to the producer.

This container: python 3.11.15, numpy 2.4.6, scipy 1.17.1, sympy 1.14.0,
mpmath **1.4.1**, pyhecke_native 0.9.0, clarabel 0.11.1,
`pyhecke_native_build` **`5df83fbc24b06f8a`**.

**The commonest difference is `mpmath 1.3.0 → 1.4.1`, 9 of the 13.** A minor
release of the arbitrary-precision library these producers compute in is not a
cosmetic difference — it is exactly where transcendental rounding can move.

**Four differ on `pyhecke_native_build`**, and the three witness values are all
distinct (`e3fab84c4c1df76a`, `47b406d9ba6e343f`, `30fd920c241a54fa`) — so the
compiled extension has been rebuilt at least three times across this corpus's
history and none of those binaries is the one here.

**One is from the future**: `s5_so3_su2_u1_fiber_action`'s witness was written
under python 3.13.12 / numpy 2.5.0 / scipy 1.18.0 — *newer* than this container
on three axes at once.

### A bug I made first, recorded because it manufactures false differences

`pyhecke_native_build` is **`sha256(<compiled .so>)[:16]`** — a content hash of
the compiled extension, not a module attribute. My first pass guessed at
`BUILD_ID` / `__build__`, got `None`, and reported the live value as **ABSENT**,
which turns a real 4-file difference into a confident-looking one against
nothing. Read it through the corpus's own
`qou_substrate.witness._pyhecke_native_build_hash`, which is what the committed
`--env` mode now does. The *conclusion* was unchanged (all three still differ
from `5df83fbc24b06f8a`), but it was right by luck for one pass.

### What this does to the first verification

It **settles** the caveat on `phi_k_weight_family_discriminator`: the only
environment difference is `pyhecke_native_build`, and it is real. So the 36 %
per-atom move and the `allPassed: true → false` flip are **confounded by a
different compiled binary**, not attributed to the producer. The witness-side
finding stands as *"this witness does not reproduce here"*; it does **not**
stand as *"the producer regressed"*. Whoever owns `qou-oots` needs the matching
binary, or a build-independent check, before reading anything into those
numbers.

`JetOrderIndependence` is **unaffected** — it is in the no-environment-block
bucket, and its defect was established from the producer's **source hash** and a
pure-SymPy rational computation, neither of which depends on a compiled
extension. That confirmation stands.

### Consequence — the triage as scoped is not runnable here

"Run each producer and compare" cannot yield a clean verdict in this container
for any of the 22. Three honest routes remain:

**A. Re-scope to source-level verification only.** Decide each hit by reading
the producer's *source* against the Lean's literals, as was done for
`JetOrderIndependence` (exact rationals, no floating point, no compiled
extension). *Costs*: manual, per file. *Risks*: only works where the quantity is
exactly computable — probably a minority. *Commits to*: nothing.

**B. Pin the environment.** Install `mpmath==1.3.0` and rebuild
`pyhecke_native` to match a target witness, then re-run. *Costs*: a build per
distinct target binary — at least three. *Risks*: disk (3.2 G free here) and the
rebuild may not reproduce the recorded hash at all. *Commits to*: maintaining a
matched environment.

**C. Record the environment gap as the finding and stop.** The screen's real
message becomes *"46 Lean provenance claims cite producers, and 22 of them
cannot be checked in a stock container"* — which is itself worth knowing, and
is arguably the more useful result.

**D. Do nothing.** 20 stay unverified.

**Recommendation, my judgement: C plus A on the exactly-computable subset.**
B is the only route to a clean numeric verdict and it is expensive, uncertain,
and buys verification of a class that has so far produced one real defect in two
checks. C is honest and cheap; A extends it wherever the arithmetic is exact.

Tally unchanged at **2 of 22 decided** — and now with a reason the other 20 are
not merely unchecked but **uncheckable here**.

---

## 2026-09-14 (later still) — the ranking was inflated by arXiv IDs, and my first fix for it did not work

### Option A: only 3 of the 22 are exactly computable — and that is why the one confirmed defect was confirmable

The `--env` split says 0 of 22 have a matching environment. But **an environment
difference only matters if the producer uses the differing package**, and the
differences are `mpmath` (9), `pyhecke_native_build` (4) and one
python/numpy/scipy case — **`sympy` matched everywhere it was recorded**. So a
producer computing only in sympy exact arithmetic is interpretable here whatever
its witness's environment block says about packages it never calls.

Classified by import cone (producer + local one-hop):

```
EXACT   (no mpmath/numpy/scipy/native)  ->  re-runnable here :  3
INEXACT (uses at least one)             ->  confounded       : 19
```

`jet_order_pivots` is one of the 3. **That is why its defect was confirmable at
all** — sympy Rationals end to end, no compiled extension, no float. A useful
internal consistency check on the method, not a coincidence.

Of the 19, **17 fail on `mpmath` alone**, which this container has at 1.4.1
against the witnesses' 1.3.0.

### 🛑 Then the two other "exact" candidates turned out to be citation artifacts

Their shared literals were `1208.1663` and `1906.12122` — **arXiv identifiers**,
matching on both sides because the Lean docstring and the witness `description`
cite the same paper:

```
M004AngleStructure.lean:76   -- Ref: [garoufalidis2012] arXiv:1208.1663 §2.2-2.3
witness description          1208.1663 eq (2.7) in pi-units ...

T3WritheVsDeltaLambdaSign:23 Hammer-Koenig-van Kolck arXiv:1906.12122 p.12
witness description          1906.12122 p.12: Pauli principle => isospin sign ...
```

**Shared bibliography is the single likeliest thing a Lean docstring and a
witness description have in common**, so without a filter the ranking is
inflated by citations. Section and equation numbers (`§2.2-2.3`, `Sec 2.2`,
`eq (2.7)`) are the same class. This is an **over-matching** blind spot — it
fails to a false hit rather than a false all-clear, which is the rarer and
easier-to-catch direction.

### 🛑 And my first fix for it silently did nothing

The filter shipped with `(?:arXiv|arxiv)\s*:\s*\d` in an alternation applied to
the text **immediately before** the matched number. The digit in that pattern
*is* the matched number, so it is never in the prefix — **that branch could
never fire**. The anchored section branch worked (which is why `2.2` dropped and
`1208.1663` did not), and **the corpus-wide counts did not move at all**, so
nothing revealed it but re-reading the ranked list by hand.

Fixed by anchoring every alternative with `$`. Both arXiv IDs are now gone.
**Five predicate unit cases are pinned in `--selftest`** so the branch cannot
silently die again — the counts were not a detector for it, and would not be.

### What the corrected ranking says

The split is **still 22 / 24** — removing literals changes counts, not buckets,
unless a file drops to zero. But the top changes:

| Lean file | shared, corrected |
|---|---|
| `JetOrderIndependence` | `1/16 1/2 1/4 1/8 55/16` — **5/5, confirmed** |
| `DepthStratifiedWeightRequirements` | `0.991 1.111 1.517 6/9` — 4/4, Lean-side clean |
| `ModularDoubleReciprocity` | `0.0 0.00187 0.10434 378.3` — 4/7 |
| `M004AngleStructure` | `1/2 1/3` — was 4/4, now **2/3** |
| `T3WritheVsDeltaLambdaSign` | `4/5` — was 2/2, now **1/2** |

**So after removing citations, the only candidate with both a strong literal
signal and an exactly re-runnable producer is the one already confirmed.** The
other two exact ones now share only generic small rationals (`1/2`, `1/3`,
`4/5`) — what chance produces. That is a negative, and it is the useful kind: in
this container the screen's actionable surface is essentially exhausted at one.

Both are still worth running, being cheap and interpretable, and that is the
next step rather than a conclusion.

Tally: **2 of 22 decided**, 3 exactly checkable here, 19 environment-blocked.

---

## 2026-09-14 (final for this session) — the exactly-checkable set is CLOSED at 3: 1 defect, 1 clean, 1 unrunnable

Ran the two remaining exact producers. Option A is now complete, and it ends
smaller than it started.

### `t3_writhe_vs_delta_lambda_sign` — CLEAN, true negative

Exit 0, and the witness reproduces **byte-identically on substance**. The only
diff is three *added* provenance fields the old witness predates:

```
+  "scriptFile": "t3_writhe_vs_delta_lambda_sign.py",
+  "q0Anchor": "independent",
+  "q0AnchorReason": "producer declared q0-independent at the stamp site ..."
```

**No numeric field moved.** Witness reverted (the additions are not mine to
land).

### `borromean_angle_structure_lp_probe` — UNRUNNABLE here, and the guard is working

Exit 2, with its reason on **stdout**:

> `WALL: SnapPy is not importable — gluing data cannot be obtained from the
> source; refusing to hand-guess it (anti-guessing rule).`

That is a refusal, not a crash — the class AGENTS.md documents as *"exit non-zero
BY DESIGN ... guards working correctly, and both explain themselves on stdout."*

**And it exposes a gap in my own `--env` scan**: `snappy` was not in `_ENV_KEYS`,
so a producer gated on an optional dependency read as *exact and re-runnable*
while being unrunnable. Added (measured: `ModuleNotFoundError` here). Absence is
the signal; witnesses predating the key simply will not carry it.

### 🛑 Two more false-positive classes, and neither is fixable by regex

Both remaining candidates' shared literals turned out not to be data:

- **A mathematical constant of the construction.** `M004AngleStructure`'s `1/3`
  is *the regular ideal tetrahedron angle in π-units* — `theorem GA_regular :
  GA (1/3) (1/3) (1/3) (1/3) (1/3) (1/3)`. It appears on both sides because both
  discuss the same mathematics, not because one copied a number from the other.
- **An index range written with a slash.** `T3WritheVsDeltaLambdaSign`'s `4/5`
  is *"the height-4/5 columns"* — a pair of column indices, not a ratio.

Together with the arXiv-identifier class this is **three** ways a shared token
means nothing. The first was fixable by regex; these two need semantics and are
recorded as a known limit rather than chased. Practical consequence: **a low
shared count is close to worthless as evidence** — only `JetOrderIndependence`'s
5/5, where the shared set is a matrix's own entries, was ever a real signal.

### Where this leaves the screen

| bucket | count | resolution |
|---|---:|---|
| exactly checkable here | 3 | **1 defect, 1 clean, 1 unrunnable — CLOSED** |
| environment-blocked (mpmath / native) | 19 | needs a pinned environment |
| pointer, not a claim | 24 | no shared number |

**The exactly-checkable set is exhausted and produced exactly one real defect**,
the one that motivated the screen. That is the honest yield: 1 in 46 candidates,
1 in 3 checkable.

**Recommendation, unchanged in direction but firmer: option C.** The screen's
durable value is the *statement* — 46 Lean provenance claims cite producers, 22
carry numbers from a moved producer, and only 3 can be checked without a pinned
environment — not a queue anyone should work down. Wiring it as a gate would be
wrong: with three false-positive classes and a 1-in-3 hit rate on the checkable
subset, it would train readers to ignore it.

Bean stays open on the environment-pinning decision (option B) and on the
`qou-oots` witness finding, neither of which is mine to take.

---

## 2026-09-14 — four candidate taxonomy rows, drafted but NOT added

This session's screen produced four distinct blind spots. The
detector-blindness taxonomy
([`2026-08-15-detector-blindness-taxonomy.md`](docs/audits/2026-08-15-detector-blindness-taxonomy.md))
is where they belong, but **it states no intake convention** — no "add a row
when", no format note — so adding rows is a judgement about what belongs in
someone else's document, which the 2026-09-07 directive does not exempt.
Drafted here so the addition is a copy-paste for whoever owns it.

**All four run the OVER-matching direction** — they fail to a false *hit*, not a
false all-clear. The table's own note says row 40 is the first of that kind, so
these would thicken a thin and useful part of it.

| draft | class |
|---|---|
| a | **scan SCOPE, for a whole LANGUAGE** — every literal audit in the corpus is `rglob("*.py")` (`assertion_on_literal_audit`, `hardcoded_literal_audit`) or `rglob("*.ts")` (`lean_ref_resolution_audit`); the `.lean` surface carrying witnessed constants is covered by none. Same shape as `convention-c-producer-audit.py` walking only `*.py` while the Lean Markov surface went uncounted. |
| b | **a CITATION IDENTIFIER that lexes as a decimal** — `arXiv:1208.1663`, `arXiv:1906.12122`. Matching on both sides of a Lean/witness comparison because both cite the same paper; shared *bibliography* is the likeliest thing those two texts have in common. Section and equation numbers (`§2.2-2.3`, `eq (2.7)`) are the same class. |
| c | **a MATHEMATICAL CONSTANT of the construction** — `M004AngleStructure`'s `1/3` is the regular ideal tetrahedron angle in π-units (`theorem GA_regular : GA (1/3) … (1/3)`). It appears on both sides because both discuss the same mathematics. Not fixable by regex; needs semantics. |
| d | **an INDEX RANGE written with a slash** — `T3WritheVsDeltaLambdaSign`'s `4/5` is *"the height-4/5 columns"*, a pair of column indices, not a ratio. Same non-fixability as (c). |

And one bug rather than a blind spot, worth the same shelf because it is the
reason (b) survived a fix: **an unanchored pattern applied to PREFIX text.**
`(?:arXiv|arxiv)\s*:\s*\d` in an alternation matched against the characters
*before* a number can never fire — the digit it wants *is* the number. The
anchored sibling branch worked, so the filter looked half-alive, and **the
corpus-wide counts did not move**, so nothing revealed it but re-reading the
ranked list by hand. Pinned now with five predicate unit cases in `--selftest`.

### A staleness I went looking for and did not find

Checked whether AGENTS.md's *"catalogues **forty-five** rows (re-counted
2026-09-14)"* had gone stale again — its own parenthesis records six prior
staleness events and says *"re-count the table; do not trust this sentence,
including this parenthesis."* A first loose count (`grep -cE '^\| *[0-9]+'`)
returned **47** and looked like a seventh. Counting the numbered first cells
exactly (`grep -oE '^\| *[0-9]+ *\|'`) gives **45**, contiguous 1-45, highest 45.

**AGENTS.md is correct; the discrepancy was my own regex.** Recorded because the
near-miss is the point: I was two minutes from "correcting" a current figure in
the document that exists to warn against exactly that.


## Round 57 Implementation (PR #8350)
- Implemented on branch `claude/round57-trd0-9nnz-fixes` (commit `35175f892e4827e826a23a3d007073dd800ff733`, https://github.com/litlfred/qou/pull/8350).
