# Owner-gated bean triage — the veto ledger

**Started:** 2026-09-05 · **Bean:** `qou-fs4r` · **Mode:** owner chose *"triage +
propose a default for each; I veto rather than choose"* (Q2 option 3, 2026-09-05).

**How to use this:** read the **DEFAULT** column. Anything you do not veto, I
apply. Reply with the bean IDs you want changed — e.g. *"veto qou-zdz5, qou-agvb"*.

**One adjustment I made to the option you chose, and why.** Where a default would
land a **physics or convention claim**, I do **not** propose one. Those are marked
**NO DEFAULT** and get their options laid out instead. Silence-as-assent is
efficient for mechanics and is exactly how a wrong physics ruling gets laundered
into the corpus — which is the risk you accepted the rest of this trade for, not
one to spend on the claims themselves.

---

## The count was wrong three times. Here is the method.

I quoted **51**, then **67**, then **81**. All three were keyword scans over bean
prose with different patterns, and none is authoritative on its own.

Split properly, the **81** in-progress beans matching any owner-phrase are:

| | count | meaning |
|---|---:|---|
| **PENDING** | **33** | a live ask — "needs an owner decision", "still needs the owner's call", "author's call" |
| HISTORICAL ONLY | 18 | a *past* ruling being cited — "by owner decision", "per owner instruction", "Owner ruling 2026-08-15" |
| (pending, also citing history) | 3 | counted in PENDING |

The remaining 30 of the 81 matched only the looser patterns of the earlier scans.

**So the real backlog is 33, and 18 of the apparent backlog was you being quoted
back to yourself.** That is the single most useful thing this triage produced and
it cost one grep — the earlier counts conflated a pending ask with a citation of a
settled one.

---

## Pass 1 — classification

`A` mechanical (default proposed) · `B` physics/convention (**NO DEFAULT**) ·
`C` stale or already answered (default: close)

### Class A — mechanical, default proposed, veto to change

| bean | the ask | **DEFAULT** |
|---|---|---|
| `9h6x` | lake-cache archive truncated; left open "for the author to close" | **close it** — infra task, nothing downstream reads it |
| `qou-agvb` | witness provenance spelled three ways (`scriptFile`/`computation`/`producer`); a canonical spelling is proposed | **adopt the proposed spelling**, migrate readers; reversible, no number moves |
| `qou-jvav` | a resolver crash is fixed; whether to add an appendix section is separate | **do not add the appendix**; keep the crash fix |
| `qou-pwut` | 87 root-level QA writers bypass `qa-agent-entry.ts` | **no-op** — leave them; a refactor of that size needs its own justification |
| `qou-7yj0` | ten trivially-inhabited `BorromeanQuark` classes | **follow the bean's own standing recommendation: touch neither file** |
| `qou-52i4` (part) | seed the lake-cache orphan branch | **seed it** — pure infra (the `would_shrink()` half is separate, below) |

### Class B — physics or convention. NO DEFAULT. Options in pass 2.

`gm4q` · `qou-1jw9` · `qou-2tuv` · `qou-48is` · `qou-8na1` · `qou-aemx` ·
`qou-c66b` · `qou-cds1` · `qou-d7h1` · `qou-goc9` · `qou-hey2` · `qou-im4m` ·
`qou-imkb` · `qou-r4ya` · `qou-t7mt` · `qou-w1g8` · `t7qv`

**Two of these are already in front of you from another route:**

- **`qou-goc9`** — *"which nucleon NF is canonical for the Q_beta counit chain?"*
  This is **the same question as Q4** in today's analysis (chain `A−1` vs complete
  graph `C(A,2)`). Answer it once, both close.
- **`qou-cds1`** — the `c_k` ladder re-derivation under convention D. It is not a
  judgement so much as **authorisation to spend**: the bean says it needs your go,
  and it is a large compute.

### Class C — provisionally stale; default is to close

| bean | why | **DEFAULT** |
|---|---|---|
| `qou-gwe9` | its subject — "Copilot review does not arrive" — was **corrected on `main` 2026-08-30**: reviews do arrive and are quota-rationed | **close**, superseded by the correction |
| `qou-324i` | its own text says *"Measurement settles it"*, not an owner call | **reclassify as agent-actionable**, remove from this queue |

### Not yet classified (pass 2)

`dgpc` · `qou-58zw` · `qou-9xla` · `qou-e9pp` · `qou-octr` · `qou-qflp` ·
`qou-r765` · `qou-zdz5` · `qou-zzwm` · `qou-52i4` (the `would_shrink()` half)

**`qou-zzwm` is flagged now rather than left to pass 2**: it reports that the
C→D excision left **published accuracy figures** behind. If that is right it is a
correctness defect in reader-facing numbers, not a preference — it should not sit
in a veto queue at all. Verifying it is the first item of pass 2.

---

## Status

- **Pass 1** — 33 pending identified and split; 6 Class A defaults proposed, 17
  Class B held back, 2 Class C proposed for closure, 10 unclassified.
- **Pass 2** — options for each Class B; verify `qou-zzwm`; classify the
  remaining 10.
