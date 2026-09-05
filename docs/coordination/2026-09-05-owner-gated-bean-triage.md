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

## Pass 2 — the remaining 9, and a pattern

### 🛑 Four more are FALSE POSITIVES — the ask was already answered, inside the bean

This is the pass-2 headline, and it is the same shape as the 18 historical-only
hits: **a bean says it needs the owner, then resolves the question further down and
never updates the line at the top.** A keyword scan reads the stale sentence.

| bean | the stated ask | why it is not pending |
|---|---|---|
| `qou-zzwm` | *"either the dashboard records the frame it inherited, or the ladder is re-derived under D"* | **the first branch was taken.** Verified live: `per-observable-100x-status.witness.json` now carries `convention_frame_qbeta`, `reproducible_under_canonical_convention`, and explicit text naming the C frame and the 2026-08-15 ruling. The figures are no longer published bare. Live remainder is `qou-cds1`, already its own bean. |
| `qou-zdz5` | Λ vs Cl₂ wrong forms, 54 sites | the bean's own text: *"a name is not revising a finding, so no ruling was needed. **Had** any site carried a wrong value feeding a conclusion, that **would have been** the owner's call."* Conditional, and the condition was **not met**. |
| `qou-52i4` | the `would_shrink()` guard blocking a cache reseed | *"the 4459-vs-7268 obstacle predicted above is **not actually enforced**"* — the guard is skipped because the incumbent branch records no counts. Moot. |
| `qou-e9pp` | a producer requesting the muon anchor that `q_parameter` refuses | **answered by the owner ruling of 2026-08-30**: proton unless (E1) an explicit proton-vs-muon comparison or (E2) the ideal CAL-1/2/3 layer. This producer is neither. |

**So of 33 "pending", 4 were already decided.** Combined with the 18
historical-only, **22 of the original 81 were noise from the same root cause** —
a stale sentence outliving the work that answered it.

### Class A additions — default proposed, veto to change

| bean | the ask | **DEFAULT** |
|---|---|---|
| `qou-58zw` | 11 witnesses: regenerate (destroys recorded analysis, **including a retraction**) vs restore producing code from history | **restore the producing code; do not regenerate.** The conservative choice preserves evidence; a regenerated witness cannot be un-regenerated |
| `qou-9xla` | 178 actionable sites; the bean says *"should probably be sequenced, not swept"* | **no-op now** — do not start; a sweep of that size needs its own sequencing plan first |
| `qou-qflp` | 74 witnesses at a value that is neither canonical pin | **no new bulk action; fold into `qou-3f7a`**, which already scopes exactly this drain. AGENTS.md warns specifically against bulk re-pinning |
| `qou-r765` | a two-line signature change to classes predating the work | **do not change the signature.** It is one rung; wait for a rung that needs it |

### Class B additions — physics or claim change, NO DEFAULT

| bean | why it is not defaultable |
|---|---|
| `dgpc` | bundles a **`status: "verified"` downgrade** on two blocks with an AME re-point. Downgrading a verified block is a claim change |
| `qou-octr` | *"adding the missing hypotheses to each context class — a claim change"*. Its own words |

---

## Where the 33 landed

| class | count | meaning |
|---|---:|---|
| **A — default proposed** | **10** | veto any you want changed; silence applies them |
| **B — NO DEFAULT** | **19** | physics / convention / claim change; options in pass 3 |
| **C — not actually pending** | **6** | 2 from pass 1, 4 from pass 2; default is to close or reclassify |

**Class A, the full veto list:** `9h6x` `qou-agvb` `qou-jvav` `qou-pwut`
`qou-7yj0` `qou-52i4` `qou-58zw` `qou-9xla` `qou-qflp` `qou-r765`

**Class C, proposed closed:** `qou-gwe9` `qou-324i` `qou-zzwm` `qou-zdz5`
`qou-52i4`(guard half) `qou-e9pp`

---

## The finding that outlives this triage

**22 of 81 apparent owner-asks were stale sentences, not open questions** — 18
citing a past ruling, 4 answered inside their own bean. The queue was ~27 %
noise, and every one of those would have cost a round-trip to a physically-
disabled author.

The cheap fix is a convention, not a tool: **when a bean answers its own owner-ask,
edit the asking sentence** rather than appending the answer below it. A grep sees
the first sentence.

## Status

- **Pass 1** — 33 pending identified and split from 18 historical.
- **Pass 2** — remaining 9 classified; 4 more false positives found; A/B/C totals above.
- **Pass 3** — options for the 19 Class B. Two are already before the owner:
  `qou-goc9` is the same question as today's Q4, and `qou-cds1` is
  authorisation-to-spend.
