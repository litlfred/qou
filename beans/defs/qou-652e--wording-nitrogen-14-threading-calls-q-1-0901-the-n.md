---
# qou-652e
title: 'WORDING: nitrogen-14-threading calls q^{-1} = 0.901 ''the negative weight''; it is the NEGATIVE-CROSSING weight and is positive (numbers are correct, do not add a minus)'
status: completed
type: task
priority: normal
tags:
    - 8f-decide
    - reorg-2026-10-04
    - split-from-6766
created_at: 2026-10-10T08:14:01Z
updated_at: 2026-10-10T10:18:48Z
parent: qou-8lxd
---

Split out of `qou-6766` on 2026-10-10 (seven findings in one title). Residual
item (3) of four. **One-line wording fix; the mathematics does not move.**

## The sentence

`folio/quantum-observable-universe/observations/nitrogen-14-threading.md:13`
(block kind `example`):

> "The mixed crossing weight $(q + q^{-1})/2 \approx 1.005$ averages **the
> positive weight $q = q_0$ and the negative weight $q^{-1} = 0.901$**."

`q^{-1} = 0.901` is a **positive number**. Read as sign-of-the-number the
sentence is simply false; it is only correct read as sign-of-the-*crossing*.

## What it means, established from the corpus

AGENTS.md §7a (Hecke-Skein convention) fixes the dictionary: `σ_i` is the
**positive crossing** `L_+`, `σ_i^{-1}` the **negative crossing** `L_-`. And
`mass-endomorphism/chi-v3-closed-form-proof.md:17` gives the mixed weight's
provenance explicitly — `averaged = ½(σ + σ^{-1}) ↦ (q + q^{-1})/2` — so the
"average" is over the two *crossing types*, not over two signed numbers. The
block's own line 1 already says it correctly: same-species crossings carry
"weight $q$ or $q^{-1}$", mixed carry "$(q + q^{-1})/2$".

## The numbers are right — do NOT "fix" them

At the proton `q_0 = 1.10998`, `q_0^{-1} = 0.90091`:
`(q + q^{-1})/2 = 1.00545` ✓ matches "≈ 1.005";
`(q − q^{-1})/2 = 0.10454` ✓ matches "≈ 0.105".

**A hypothesis this bean considered and REJECTED**, recorded so the next reader
does not enact it: that a minus sign had been dropped, because the Hecke
generator's *eigenvalues* are `q` and `−q^{-1}` (§7a), which would make
`−q^{-1} = −0.901` genuinely negative. That is not what this block computes — it
weights crossings, it does not use the σ eigenvalues — and substituting `−q^{-1}`
would break both arithmetic checks above. The defect is in the adjective only.

## Drafted replacement (one clause, two words)

> "… averages the **positive-crossing** weight $q = q_0$ and the
> **negative-crossing** weight $q^{-1} = 0.901$."

## Options

1. **Enact the draft.** Cost: one clause in one block. Risk: none measurable —
   no number, no witness, no Lean, no label.
2. **Enact it and sweep the same phrasing** wherever else a weight is called
   "negative". Measured: the phrase occurs only here (`\mathrm{dem}`-style grep
   over `.md` for "negative weight" returns this one site).
3. **Nothing.**

**Recommendation (agent judgement):** (1). It is corpus-derived — §7a and the
block's own line 1 both fix the reading — but it is still prose in a chapter this
bean's author was not sent to, so it waits under the ask-first rule.

**Default if unanswered: (3).** The sentence keeps a false literal reading of a
correct computation.

**Blast radius:** `ex:nitrogen-14-threading` only.


## ENACTED 2026-10-10 — owner picked it; the draft went in verbatim

`nitrogen-14-threading.md:13` now reads *"averages the positive-crossing weight
$q = q_0$ and the negative-crossing weight $q^{-1} = 0.901$."*

**The numbers were not touched and must stay untouched.** Re-verified after the
edit: $(q+q^{-1})/2 = 1.00545$ against the block's "≈ 1.005", and
$(q-q^{-1})/2 = 0.10454$ against its "≈ 0.105". The rejected repair — restoring
a minus from the Hecke eigenvalues $q$, $-q^{-1}$ — would break both, and that
rejection is recorded in the body above so it is not re-attempted.

`qa-sweep` on the block after the edit: **0 critical, 0 major, 0 minor**.
