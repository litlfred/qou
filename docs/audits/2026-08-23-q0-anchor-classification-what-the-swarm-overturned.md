# q₀ anchor classification: the swarm overturned my own method at 37 %

**Date:** 2026-08-23
**Bean:** `qou-qflp`
**Supersedes:** the 2026-08-19 draft of this doc, whose central number was wrong.

## Nothing here is the #5324 fix — main landed that independently

Before anything else: the diagnosis, the reference restore, and the guard that
PR #5324 carried are **all on `main` already**, landed by a sibling while this
branch was open:

| commit | what |
|---|---|
| `2e4745448` | restore the muon anchor — the repin sweep overwrote its own definition |
| `7ddaeab36` | the 262 Q0_FLIPs are ONE corrupted anchor definition (bean `qou-cezp`) |
| `31d1bdf6e` | a producer-declared **`comparison`** anchor — the one label the audit can verify |

So #5324's fix is redundant and this branch was rebuilt on `main` carrying only
what is additive. This is the sanctioned parallel-research overlap working as
intended — two agents reached the same diagnosis from different contexts, and
the convergence step is to drop the duplicate, not to defend it.

`31d1bdf6e` is a direct answer to a finding below: the witnesses that read
**both** pins deliberately now have a label of their own rather than needing an
exclusion list.

## The headline: a swarm measured my mechanical classifier, and it was wrong

I built a mechanical classifier for the ~1900 anchor-missing witnesses — AST
import-cone reachability at depth ≤ 3 over the repo's own
`q0_producer_pin_classifier.classify()`. It reported **722 of 889** producers
as reaching no q₀ at all, i.e. candidates for `q0Anchor: "independent"`.

Thirteen read-only agents then adjudicated the same producers by reading them.
Five completed before the run hit a weekly limit, covering **443**. Against
those:

| | swarm: independent | swarm: q0_dependent |
|---|---|---|
| **mine: independent** | 222 | **130** |
| **mine: q0_dependent** | 24 | 65 |

**130 of my 352 `independent` calls were wrong — 37 %.** That is the *dangerous*
direction, and I had said so in the swarm's own brief: a false `independent`
lets a later migration skip a q₀-dependent witness silently, leaving a stale pin
presented as pin-agnostic.

The routes the swarm found, on those 130:

| n | route | why my method could not see it |
|---|---|---|
| 72 | **d** — literal in the producer's own file | see the defect below; also my walker never classified the producer itself, only its imports |
| 49 | **b** — reads a q₀-bearing witness JSON by path | not an import; invisible to any import-cone method |
| 5 | f — indirect import | my cone should have caught these |
| 3+1 | a, e | — |

Route **b** is the structural lesson: **an import graph is the wrong shape for
this question.** A producer that opens `chi-proton-h3-at-q0-50dps.witness.json`
and reads a number out of it is exactly as q₀-dependent as one that calls
`q_at()`, and no amount of depth on the import cone will ever reach it.

The 24 the other way (mine dependent, swarm independent) are the safe direction
but still a 27 % over-flag on that side.

**Do not use the 722.** The honest reading is that ~55 % of the file-locally-
clean producers are genuinely independent, so the surviving candidate set is
roughly 490 of 889 — and that is an *extrapolation from a 443 sample*, not a
measurement of the whole.

## A real defect in shared infra: `classify()` never looked for a proton literal

Chasing route **d** found this, and it is live on `main` today.
[`q0_producer_pin_classifier.py:149`](../../computations/audits/q0_producer_pin_classifier.py)
tested `s.startswith("1.10997859555")` — **muon only**. There was no proton
branch at all. So:

```python
Q_P = mp.mpf("1.109978582751380808")     # computations/alpha_em_two_loop_structure_probe.py:63
```

classified as `none`, which that module's own docstring defines as *"no numeric
q₀ reached at all (purely symbolic producer)"*. It is not symbolic. It is
pinned, in the most literal way the language offers.

**Measured on the 2026-08-23 tree:** 137 producers carry a *live* proton literal
(non-comment, outside `__main__`, AST-confirmed). `classify()` called **53 of
them `none`.** Those 53 were invisible to the manifest-proposal path and stayed
`UNDETERMINED` — the same gap that let the 30.4 ppb `qbeta-ck-cache` mislabel
survive, one pin over.

Fixed here by a symmetric proton branch. Effect on the classifier's own reported
population of 112:

| | before | after |
|---|---|---|
| proton | 37 | **42** |
| muon | 28 | 25 |
| none | 25 | **20** |
| BOTH | 21 | 24 |
| *muon disagreements* | 7 | **5** |

Safe by construction: the extra evidence can only turn `none` into `proton`, or
`muon` into `BOTH`. It cannot manufacture an `ideal_muon` entry, which is the
only behaviourally live direction (`physical_proton` is inert — anything not
under `ideal_muon` already resolves to proton).

## The cheap question, corrected twice

Separate from what producers *do*: what do the witnesses already *say*?
[`q0_anchor_payload_recovery.py`](../../computations/audits/q0_anchor_payload_recovery.py)
scans the payloads for either pin.

| payload carries | count |
|---|---|
| no pin string at all | 1558 |
| **proton** | **147** |
| **muon** | **179** |
| **both** → `comparison` | **40** |

**326 of 1924 need no producer analysis and no re-run** — the q₀ is sitting in
their own payload, recorded under an ad-hoc key: `q_0_50dps` (89), `q0` (81),
`q_0` (44), `q_proton` (29), `q_muon` (21), `q` (15), and more. The field was
never missing; the **name** was never agreed. The 40 carrying both are
`31d1bdf6e`'s new `comparison` anchor, exactly.

Two corrections to my own figures on the way here, both worth recording because
they are opposite kinds of error:

1. **Population mismatch (over-count).** The first scan walked every
   `computations/**/*.witness.json` while quoting the population from the audit
   that skips `_deprecated` (370) and `AUDIT_SUFFIXES` (59). Two populations,
   one label.
2. **Prefix too long (under-count).** The scan then used the 12-digit muon
   prefix `1.109978595557`. The corpus carries **two** muon values agreeing to
   11 digits and diverging at the 12th — `…55733471989` (current) and
   `…55418057528` (superseded), as `q0_muon_population_partition.py` on main
   documents. The 12-digit prefix silently dropped every witness still on the
   superseded value: recoverable muon read **93** when it is **179**.

Both are the same failure in different directions — a threshold chosen without
checking what it separates. Which is, structurally, the same mistake as the
722: a method whose blind spot was never measured until something else measured
it.

## What is actually open

- **326** labellable by transcription (a witness mutation; needs the usual
  sign-off, but no recomputation and no numerical change).
- **40** are `comparison` — label, do not resolve to one pin.
- **1558** genuinely need the producer question, and the only method with a
  measured error rate on it is *reading them*, at ~55 % independent.
- The swarm covered 443 of 889; **446 were never adjudicated** (8 of 13 agents
  hit a weekly limit). Re-running them is the obvious next step now the limit
  has reset.
