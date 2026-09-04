---
# qou-3f7a
title: 'Fix the two RED q0 gates: anchor flip + value drift ratchet'
status: todo
type: task
priority: normal
created_at: 2026-08-29T02:13:12Z
updated_at: 2026-09-04T04:33:27Z
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
