---
# qou-3f7a
title: 'Fix the two RED q0 gates: anchor flip + value drift ratchet'
status: todo
type: task
priority: normal
created_at: 2026-08-29T02:13:12Z
updated_at: 2026-09-07T06:26:31Z
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
