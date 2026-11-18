---
# qou-3f7a
title: 'Fix the two RED q0 gates: anchor flip + value drift ratchet'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T02:13:12Z
updated_at: 2026-11-18T08:30:27Z
parent: qou-cdx1
---

---

## A commit from this bean's own drain STRIPPED a q0 stamp (found 2026-09-04, session on qou-y98b)

`9c2058f0bd` (*\"drain(qou-3f7a): q0 drift NEW 10 -> 5\"*) removed **both**
`q0Anchor` and `q0Value` from `computations/chi-neutron-h3.witness.json`,
leaving it unstamped. It is now a NEW entry on the sibling
**q0-anchor refill ratchet** (`computations/audits/q0_anchor_ratchet.py`).

**Net effect of that commit on the anchor gate: +2.** It touched 10 files,
**added** `q0Anchor` to 3 witnesses and **stripped** it from 1. So this is one
file, not a systematic problem with the drain — recorded because the direction
is the interesting part: *a commit whose purpose is draining one q0 gate
refilled another.*

**Established, not inferred, that the stamp was correct and its removal is a
regression:** the producer is
[`computations/delta_lambda_empirical_tabulation.py`](computations/delta_lambda_empirical_tabulation.py),
and line 93 is `from q_parameter import Q_MP` — it *does* read the proton q0.
So `q0Anchor: proton` was right, and nothing was written in its place; the
witness is now simply undeclared rather than correctly re-declared
`independent`. Evidence:

    git show 82a76eb752:computations/chi-neutron-h3.witness.json
      -> {'q0Anchor': 'proton', 'q0Value': '1.10997858275138080759...'}
    (current)
      -> NO q0 KEYS
    git show 9c2058f0bd -- computations/chi-neutron-h3.witness.json
      -  \"q0Anchor\": \"proton\",
      -  \"q0Value\": \"1.1099785827513808075916690956107688798744991218736\"

**NOT fixed here, deliberately.** The remedy is to re-run that producer, which
writes sibling witnesses and sits inside this bean's tranche — someone else's
live work. My judgement (not a finding): whoever owns this tranche should
re-run it as part of the next pass rather than have a passing branch reach into
it. The no-op is safe: the ratchet keeps reporting it, and the number it costs
is 1.

Cross-reference: `qou-q0rf` (the refill is the arrival rate). This is a
mechanism that bean does not record — its data is *new witnesses arriving
unstamped*, whereas this is *an existing stamp being removed by a drain*.


---

## 🛑 RETRACTION of the section above — I named the wrong producer and the wrong story (2026-09-04, same session)

The section immediately above says `9c2058f0bd` **stripped** a q0 stamp from
`chi-neutron-h3.witness.json` and calls it a regression. **Three of its claims
are wrong.** Corrected here; PR #6591 carries the fix.

**1. The producer.** I named
[`computations/delta_lambda_empirical_tabulation.py`](computations/delta_lambda_empirical_tabulation.py)
and cited its line 93 `from q_parameter import Q_MP` as proof the `proton`
stamp was correct. That file is a **CONSUMER** — the witness appears in it as a
`chi_witness` INPUT (line 119). I found it with `grep -rl <witness filename>`,
which finds readers exactly as readily as writers, and took the first hit.

The real writer is **`per_irrep_pole_atom._write_chi_cache`**. What I should
have done first: read the witness's own provenance — it has **none**, no
`scriptFile`, no `witness` block, which is itself the diagnosis.

**2. It was not a strip; it was a re-run of a BARE producer.** `9c2058f0bd`'s
own commit message says so: *"chi-neutron-h3 is a sibling witness the per_irrep
producer writes; it is legitimate output of that run, not churn."* The
`q0Anchor: proton` it erased had been **hand-added downstream** by `a4d9906659`
(2026-08-10), not written by any producer. This is the **bare-producer** class
AGENTS.md names verbatim: *"Some producers never emit provenance… Re-running
one deletes the field this audit keys on. Fix the producer to emit provenance
first."*

**3. The erased stamp was WRONG anyway, so the re-run was an improvement.**
Measured: `chi_lambda_symbolic` returns `q_character_on_braid_word(shape,
crossings, Q)` with `Q` a **sympy Symbol**, and no field in the
`_write_chi_cache` payload references `Q0_FLOAT` / `q_parameter` / `q0`. The
cache is q0-INDEPENDENT. `proton` asserted a pin it does not have — the exact
failure `qou-q0rf` warns about. The re-run replaced a false assertion with
silence, which is better, though `independent` + reason is better still.

**Two more chi caches carry the same wrong `proton`**: `chi-proton-h3` and
`chi-helium-3-h9`. Fixed at the producer in #6591.

**Nothing here is `qou-3f7a`'s to repair.** The prior section asked this
tranche to re-run a producer; that was based on the misidentification. Drop it.


---

## MEASURED 2026-09-07, and DELIBERATELY NOT DRAINED — the producer belongs to a live sibling

Worked from litlfred/qou#6971. Fresh gate numbers, because the ones in this bean's
audit are from 2026-08-29:

    q0-anchor refill ratchet    baseline 1677    drained since 188    NEW 97
    q0-value drift ratchet      2781 q0-bearing fields
                                stale 207        baseline 329         NEW 5

Note the shape on the anchor gate: **188 drained and 97 refilled**. That is the
revolving door `qou-mnrd` names, not a monotone drain, and it is the reason a
bulk pass here is worth less than it looks.

The 5 drift NEW are all −0.0769 / −0.0798 ppb, i.e. the muon re-pin delta this
bean exists for. One of them, `hadron-knot-table.witness.json`, is named in
AGENTS.md as the last file on the retired pin.

### The named regression is still live, and the fix is NOT mine to make

This bean records that `9c2058f0bd` stripped `q0Anchor`/`q0Value` from
`computations/chi-neutron-h3.witness.json`. Confirmed still stripped today — the
witness has neither key. The prior agent's judgement ("whoever owns this tranche
should re-run it") is correct, and there is now a concrete reason:

**`origin/claude/anchor-followups-2026-08-08` is actively editing the very
producer.** Its diff to `delta_lambda_empirical_tabulation.py` (+12/−5, last
commit 35 h ago) replaces `q0_float = float(Q_MP)` with `q0_mp = mp.mpf(Q_MP)`
and lifts the breakdown strings before arithmetic — the same float64-laundering
class as `qou-1evu` on my own branch.

So re-running that producer from here would emit a witness from the OLD producer
version, which their change supersedes. That is worse than the no-op.

### The cross-branch finding neither bean carries

**When that sibling re-runs the producer for their own fix, the stripped q0 stamp
comes back for free** — the producer reads `Q_MP` at line 93, so `q0Anchor:
proton` was correct and nothing replaced it. One q0-anchor-ratchet entry closes
as a side effect of a float64 fix, and neither bean mentions the other. Posting
this to their PR.

### Why the bulk drain is not on #6971

83 `Q0_FLIP` + 165 drift sites is a sweep in a different theme from that PR
(hardcoded constants), and AGENTS.md forbids widening a PR on the agent's own
initiative. It stays this bean's, on its own branch. What #6971 does carry is the
establishment that **none** of the q0 gates' NEW findings intersect its diff —
checked file by file, empty intersection on all three gates.


---

## 2026-09-07 — the named regression is a FALSE POSITIVE, and this bean's own finding is backwards

I recorded the prior agent's reading on 2026-09-07 without checking it. Checked
now, it does not hold.

### The witness has NO producer, so "re-run the producer" was never the fix

This bean says `9c2058f0bd` stripped `q0Anchor`/`q0Value` from
`computations/chi-neutron-h3.witness.json`, that the stamp was correct, and that
the remedy is to re-run `delta_lambda_empirical_tabulation.py` because "line 93
is `from q_parameter import Q_MP` -- it *does* read the proton q0."

Two errors in that:

1. **That script READS this witness, it does not write it.** It appears in the
   script's `chi_witness` list (line 119). Its `Q_MP` import is for its own
   output. Grepped for a writer: every other reference in the tree is to the
   *numeric* `chi-neutron-h3-at-q0-50dps.witness.json`, a different file. This
   one has `producer: None`, `computation: None`, `scriptFile: None` and
   `auditOnly: docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md`.
   **Nothing produces it.**

2. **Its content is purely SYMBOLIC, so it has no anchor to stamp.** Measured:

       chi_q_symbolic: '(q**4 + 2*q**2 + 1)/(4*q)'
       chi_q_symbolic: '(q**22 + q**20 + ... - 1)/(4*q**11)'
       q0-literal occurrences in the whole file: 0
       n_partitions 3/3, partial False

   A chi^lambda in the formal variable q is anchor-independent by construction.

**So the stamp asserted a dependence the object does not have, and removing it
was CORRECT.** The drain commit was right; the regression is the ratchet
reporting it, and the entry should be exempted rather than restored.

### Sizing the rest of the ratchet's backlog -- and my own detector was wrong twice

The interesting question is how much of the 110 NEW is the same false positive.
Three passes, each one making my false-positive claim SMALLER:

    pass 1  "no q0 literal in the payload"        -> 64 of 110  (58%)
    pass 2  + producer's own source reads q0      -> 16 candidates
    pass 3  + one-hop import cone, infra excluded ->  7 candidates  (6.4%)

Pass 1 was wrong because a producer can compute at q0 and report only derived
numbers -- `c5_sign_is_robust_convergence_claim_is_not_probe` reads `q_at()` and
echoes no literal. Pass 2 was wrong because it ignored the import cone. Pass 3's
first run was ALSO wrong: 14 of 15 "reached q0" through `_path_bridge`, which is
a `sys.path` bootstrap and supplies nothing -- verified directly against its
source. Excluding infra modules and stripping comments/docstrings before matching
gave the 7.

**Corrected totals for the 110 NEW:**

    A  carries a q0 literal                      46   genuine
    B  no literal, producer reads q0 directly    16   genuine
    C  reaches q0 via a real one-hop import       8   genuine
    C' no q0 reachable at one hop                 7   candidate anchor-free
    D  no producer resolvable                    32   undetermined

So **>= 70 of 110 are genuine** and at most 7 are false positives -- an upper
bound, since the cone check is one hop deep. **This drain is real work, not a
detector artifact.** That is the opposite of what pass 1 suggested and worth
knowing before anyone budgets it.

### The sibling blocker has weakened but the coordination note stands

`origin/claude/anchor-followups-2026-08-08` is now **2 days idle with no PR**,
and its `float(Q_MP)` -> `mp.mpf(Q_MP)` fix is still NOT on main (line 403 still
casts). It is not a live claim by the stalled-claim rule, but porting their
unmerged work is a separate decision from this bean's drain, and I have not taken
it.


--------

## 2026-09-07 — the chi-neutron-h3 finding above is WRONG, and 45 % of the refill has no producer to fix

Worked under PR #7061. Two corrections and one sizing, all measured.

### 1. CORRECTION: `q0Anchor: proton` on `chi-neutron-h3.witness.json` was NOT right

The section above states that the stamp's removal by `9c2058f0bd` "is a
regression", establishing it from the *consumer*: `delta_lambda_empirical_tabulation.py`
line 93 is `from q_parameter import Q_MP`, so it reads the proton q0.

**That is a consumer's property, not the file's.** Read the file itself and it
holds nothing but symbolic rational functions in `q`:

    [3]      (q**4 + 2*q**2 + 1)/(4*q)
    [2,1]    (q**22 + q**20 + q**18 + q**12 - q**10 - q**4 - q**2 - 1)/(4*q**11)
    [1,1,1]  (-q**4 - 2*q**2 - 1)/(4*q**3)

Its field is `chi_lambda_symbolic`; `partial: False`. The whole blob contains
**no** `1.10997`, **no** `q0`, **no** `mpf`, **no** `50dps`. It is symbolic in
`q` and does not evaluate at any pin.

So the correct token is **`independent`**, not `proton`, and `9c2058f0bd`
removed a **wrong** stamp. It was incomplete only in writing nothing in its
place. The direction of the earlier finding is inverted: this was not a
regression to revert, it was a half-finished correction to complete.

The reasoning error is the documented provenance/arity conflation — inferring a
file's anchor from a script that *reads* it. The consumer reads this cache and
separately evaluates at q0; both facts are true and only one is about the file.

### 2. CORRECTION: the stated remedy cannot work — that producer does not write it

"The remedy is to re-run that producer" — measured, it is not. Re-ran
`delta_lambda_empirical_tabulation.py` (exit 0, 2.1 s): it writes
`delta-lambda-empirical-tabulation.witness.json` and `chi-neutron-h3.witness.json`
still has NO q0 keys afterwards. That script only **reads** the chi caches
(`_load_chi_cache`, and a config table at lines 117-139 naming the files to
load).

Nothing in live `computations/` writes it. Every writer is under
`_deprecated/`. `hecke/hecke_character_symbolic.py` also only reads it
(`_load_chi_witness`). It is a committed symbolic-character cache with no live
producer.

### 3. SIZING: the ratchet's instruction is unfollowable for 45 % of its own queue

The ratchet prints "Each needs ONE of these **AT THE PRODUCER** (never hand-edit
the JSON)". Measured over its full NEW list:

| | count | share |
|---|---|---|
| NEW unstamped witnesses (the refill) | **110** | |
| producer-stamped (has `scriptHash`/`commitSha`) | 60 | 55 % |
| **NO stamp at all** — data cache or hand-maintained file | **50** | **45 %** |
| contain no q0 literal anywhere | 64 | 58 % |

For those 50 there is no producer to declare in the manifest and no `build()`
to enter, so the only available action is the one the ratchet forbids. That is
not a defect in the ratchet's advice for the 60; it is a category the advice
does not cover.

`Q0_AUDIT_EXEMPT` already exists and holds 90 entries, so there is precedent
for scoping such files out rather than stamping them.

### What is NOT done here, and why

Nothing was hand-edited and no exemption was added. Both are scope decisions
about what the ratchet is *for*, and they move a number other agents read.
Framed for the owner on PR #7061.

### Not to be confused with the sibling gate

`q0_anchor_consistency_audit.py` is a **different** gate and is live work on
PR #7048 (`qou-9ot5`) as of today. Independently re-measured here, agreeing
with theirs exactly: `Q0_FLIP 1` (`hadron-knot-table`, documented not-drainable
— >50 min for one bound atom of nineteen) and `Q0_ANCHOR_UNRECOGNISED 4` (all
four in their scope, two already fixed on their branch). **Nothing in that gate
was touched here**, per the one-owner rule for mechanical work.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

The q0 ANCHOR axis (ruling R2, proton pin), not the convention axis (R1). Both
landed in the same 2026-08-15 ruling, which is why they share a milestone, but
they are independent surfaces with independent audits. Keep open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


## RETRACTION, same session — this bean was CORRECTLY parented and my verdict above was wrong (bean `qou-am5t`)

The 2026-10-10 verdict above says **REPARENT**, on the reasoning that this is the
q0/colour axis rather than the convention axis and therefore the wrong milestone.
**That reasoning is wrong, and `qou-cdx1`'s own title says so**:

> `MILESTONE: excise convention C, adopt proton pin + colour weighting (owner ruling 2026-08-15)`

Its body states the three rulings explicitly — **R1** convention D canonical / C
excised, **R2** proton pin canonical, **R3** `bring_color_weighted` canonical.
So the milestone is a THREE-RULING milestone, not a C-excision milestone, and a
q0-pin bean (R2) or a colour-weight bean (R3) sits under it by design.

My §9 paragraph calling the shared milestone an artefact of the two rulings
"landing in the same message" had it backwards: they share a milestone because
the milestone was scoped to cover all three, deliberately.

**This bean stays under `qou-cdx1`. It is not re-parented, and the REPARENT
verdict above is withdrawn.** Everything else in that verdict — that it is live
and worth doing — stands.

Third correction of this session, and the same class each time: a claim about a
bean made without reading that bean's own primary text closely enough. The first
was `qou-m7py` (called satisfied off one grepped line), the second was the
66-unscoped paper classifier.

## Round 86 Progress (PR #8398)
- Branch: `feat/round86-irrcubic-resolvent3-dimsum5-tau1-satdiff-43c1`
- Commit 1 (code + probe): `b5de63778dc1a1dd5f06089955f845fb94bba20f`
- Commit 2 (witness): `cda43c1b21fb03c917cb1d6c4ebc184aeff1e706` (`scriptSha256 = d48339de07d62c85bc2a014c14ff39ca61b8c6091d44dbc01d9abdb15245ae18`)
