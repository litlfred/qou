---
# qou-zk51
title: q0 gates are blind to witnesses that consume the anchor but record only derived numbers
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T08:24:15Z
updated_at: 2026-10-04T15:13:35Z
parent: qou-5vkl
---


## The gap, measured

The 2026-08-22 muon-anchor re-pin (`fca08de7d2`, owner ruling: A → CODATA
2022) is drained under `qou-3f7a` through two gates. **Both key on a q₀
literal or stamp being PRESENT in the witness:**

- the **anchor-flip** gate reads the `q0Anchor` / `q0Value` pair;
- the **value-drift** gate reads q₀ literals appearing anywhere in the file.

Neither can see a witness that carries **no q₀ field at all** and records only
quantities **derived** from the anchor. That drain audit's summary — *"a pure
re-stamp for group M"* — is correct for the population it scopes and simply
does not describe this one.

The **route** is already detected: `q0_witness_read_dataflow_audit.py` finds
producers inheriting q₀ by *reading* a pinned witness (filesystem, not
imports). What it reports is **straddles**. Nobody had asked the *staleness*
question about the single-pin muon readers it counts.

New detector: [`computations/audits/muon_anchor_reader_invisible_staleness_audit.py`](computations/audits/muon_anchor_reader_invisible_staleness_audit.py)
(6/6), witness `muon-anchor-reader-invisible-staleness.witness.json`.

    producers NAMING the anchor (upper bound)     86
    paired to a witness by scriptFile provenance  65
      ... the same pairing BY FILENAME STEM       31
    witness carries a q0 literal or stamp         51
    carries neither, computed at/after the re-pin 10
    AT RISK: carries neither, predates the re-pin  5

## Why 0.0769 ppb is not a small number downstream

A witness reporting a **ppb-level residual** reports `(v − target)/target`, a
near-cancellation: a relative perturbation of `v` is divided by the residual's
own relative size. Measured on the one confirmed member:

| | |
|---|---|
| q₀, A → C | rel **+0.0769423 ppb** |
| `qbeta-ladder-convention-fee` muon row | 7.336484242 → 7.133936641 ppb, **−2.7608 %** |
| amplification | **3.588e8×** |

Reproduced by evaluating the published ladder at A and at C — to every digit
the witness carries. Its producer reads `derived_50_digit.q` straight out of
the anchor file; its committed witness on `main` had **no `q0Anchor`, no
`q0Value`, and no q₀ literal anywhere**, so neither gate could ever have
flagged it. It was found only because an **unrelated docstring edit** drifted
its `scriptHash`.

## Re-running the at-risk five: TWO causes, not one

2026-09-04 at HEAD, each baselined from `git show origin/main:<w>` (never from
the working tree), volatile keys masked, tree restored by name. **All five
moved.**

**Anchor-class** — the re-pin; own assertions still pass:

- `lambda-scale-derivation-probes-123` — up to **~210 ppb** on
  `delta_lambda_pn` and the strange-baryon λ's (≈2700× the anchor's own shift)
- `qbeta-c3-per-block-categorical-probe` — ~0.60 ppb on χ at q₀ (≈7.8×)
- `fvk-selection` — ~0.079 ppb on `I_F_lower_bound` (≈1×)

**Convention-class** — *not* the anchor; convention C → D reaching the import
cone — and **both record a green a fresh run does not reproduce**:

- `qbeta-symbolic-tbeta-min-l2` — `allPassed` true → **FALSE**; `A_q_symbolic`
  `sqrt(q)`-form → `q**3/(q**2+1)`
- `qbeta-markov-trace-norm-probe` — `allPassed` true → **FALSE**; L2 residue
  `6.85e-14` → `3.48e-9`

Reading all five as anchor drift would misattribute the larger half.

## What is NOT claimed

1. **The two convention-class producers are not asserted broken.** A C-frame
   assertion failing under D is what AGENTS.md and
   `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` predict — the ladder must be
   **re-derived** under D and a z-substitution is not a valid move. The finding
   is a **stale green**, and its remedy is the `qou-cds1` re-derivation.
   **Refreshing these two would commit a red.**
2. **`fvk-selection` is not asserted mis-stamped by intent.** It stamps
   `q0Anchor: independent` with reason *"no q0-dependent field in this
   witness"*, and its numbers move ~1:1 with the anchor. Both cannot be right;
   which is wrong is not settled here.
3. **Nothing refreshed, nothing wired.** Scope-(a); all five restored.

## Two measurement traps this had to survive

- **Stem pairing fails silently, on this very class.**
  `qbeta_ladder_convention_fee_probe.py` emits
  `qbeta-ladder-convention-fee.witness.json` — no `-probe` suffix — so a
  filename-stem match cannot see the one confirmed member of the class being
  measured. 31 vs 65 paired; the "a gate can see it" bucket 21 vs 51. **Pair on
  `scriptFile` provenance, never on the name.**
- **The audit counted itself.** A scanner *names* the anchor filename in order
  to look for it, so a filename scan cannot separate *"consumes the value"*
  from *"greps for the name"* — the reader total read 87 before self was
  excluded, and the other q₀ audits are still in it. Read that figure as an
  **upper bound**. The at-risk bucket is unaffected: every member was confirmed
  to consume the value by re-running it.

## Still open

- Whether `fvk-selection`'s `independent` declaration or its q₀ sensitivity is
  the wrong one.
- Whether the three anchor-class witnesses should be refreshed now or wait for
  the `qou-3f7a` tranche — **not** taken here, because that tranche is another
  session's live work.
- Whether the gate should be extended to key on *producer dataflow* rather than
  on a literal's presence. That is the general fix and it is larger than this
  bean.

Found while closing a loose end in PR #6606 (`qou-99qc`), where I had written
*"it is upstream; I do not assert which upstream."* It was measurable.

---

## `fvk-selection` RESOLVED (same PR) — the declaration was false, and the obvious fix traded one red for another

The "still open" item above — *"whether `fvk-selection`'s `independent`
declaration or its q₀ sensitivity is the wrong one"* — is settled, and it took
one read: **the contradiction is inside a single file.**

    line  92   Q0_MUON_STR   = json.loads(_MUON_WITNESS.read_text())["q0Value"]
    line  93   Q0_PROTON_STR = "1.1099785827513808..."
    line 634   for name, qs in (("muon", Q0_MUON_STR), ("proton", Q0_PROTON_STR)):
    line 636       q0 = mpf(qs);  r = q0 ** mpf("0.25")      # -> moments -> Jacobi
    line 764   # ... no q0 in this producer's cone; stamp provenance only.
    line 769   _WB.stamp_staleness_metadata(..., q0_anchor=False)

`q0 ** 0.25` feeds the balanced moments, the qd-Jacobi recurrence and every
`I_F_lower_bound` / `lambda_min_N` the witness reports. The producer consumes
q₀ at two pins; the comment and the declaration are both **false**.

**Why a false `independent` is worse than an absent stamp.**
`q0_anchor_is_declared` treats it as **settled**, so no q₀ gate ever revisits
it — while the anchor-flip gate (reads `q0Anchor`/`q0Value`) and the
value-drift gate (reads q₀ literals) are *both* structurally blind to a witness
recording only derived numbers. The declaration closed the one door that was
left.

Corrected to **`comparison`** — the E1 exception in AGENTS.md §"q₀ anchor
convention", since evaluating at both pins is the producer's purpose.

### The fix I nearly shipped was half a fix

Stamping `comparison` alone is **not** an improvement. Measured on the live
gate:

| counter | main | stamp only | stamp + `q0Values` |
|---|---|---|---|
| `Q0_COMPARISON` | 5 | 5 | **6** |
| `Q0_COMPARISON_NO_VALUES` | 0 | **1** | **0** |
| `Q0_ANCHOR_MISSING` | 1603 | 1602 | **1602** |

`q0_anchor_consistency_audit` counts a comparison stamped without a `q0Values`
mapping as **`Q0_COMPARISON_NO_VALUES` — "the claim is unchecked"**. So the
stamp on its own trades `ANCHOR_MISSING` for a new red. With
`q0Values = {"muon": …, "proton": …}` the audit **verifies each leg against its
canonical pin** — which is the point: as its own source says, *"`independent`
is an assertion about an import cone; `comparison` names pins, and each named
pin either matches its canonical value or does not."* It is the one label the
audit can check rather than take on trust.

Nothing else in the 13 counters moves.

### A prediction of mine that was wrong, recorded

I expected the sharper finding to be that `fvk` reads **`q0Value`** (the
witness's own provenance self-stamp) rather than `derived_50_digit.q` (what
`_q0_value_for_anchor` reads), and that AGENTS.md's drain table shows those two
disagreeing — `derived_50_digit.q` at C, `q0Value` stale at **A**. **Measured:
they are identical today**, both at C. `48c84692679` (2026-08-29, *"repair two
anchor/value pairs the merge split across sides"*) fixed it. So AGENTS.md's
table describing `q0Value` as stale is itself out of date, and the story here is
the plain one: `q0Value` moved A → C and `fvk`'s numbers moved with it.

### Effect on this bean's own numbers

    AT RISK  5 -> 4        visible to a q0 gate  51 -> 52

The remaining four are left alone deliberately: two are the `qou-cds1` stale
greens (refreshing commits a red), and the anchor-class two sit in the
`qou-3f7a` tranche, which is another session's live work.

---

## The convention-class diagnosis is an IDENTITY, not an inference (2026-09-04)

Prompted by #6605's careful note that they had recorded my "a fresh run returns
`false`" half *as reported, not as measured*. It does not need to be taken on
report — **the two witnesses on disk settle it between them**, with no re-run.

The changed slot `A_q_symbolic[3]` / `A_vector_symbolic[3]` is literally `z²`:

| | committed on `main` | fresh run at HEAD |
|---|---|---|
| value | `q/(q**2 + 2*q + 1)` | `q**6/(q**4 + 2*q**2 + 1)` |
| identity | `= z_C²`  (`z_C = √q/(q+1)`, `(q+1)² = q²+2q+1`) | `= z_D²`  (`z_D = q³/(q²+1)`, `(q²+1)² = q⁴+2q²+1`) |

Verified symbolically: `simplify(q/(q**2+2*q+1) − z_C**2) == 0` and
`simplify(q**6/(q**4+2*q**2+1) − z_D**2) == 0`, both `True`.

So this is not *"a symbolic form changed in a way consistent with C→D"* — the
slot **is** the Markov parameter squared, and `main` holds `z_C²`. This is the
value-level convention test AGENTS.md recommends over any source grep ("test the
ANSWER, not the source"): a value cannot be stale, mislabelled, re-spelled or
inherited from a stale record and still equal `z_C²` exactly.

**One caution for whoever refreshes these.** In
`qbeta-markov-trace-norm-probe`, `assertions[3]` changes **shape**, not just
value: `computed` and `expected` both go from the number `0.0899095006045937`
to the boolean `True`. That assertion is becoming a different *kind* of check,
so a refresh is not a numeric update there. The signal I would actually track
is `constraint_residues_at_q0/L2`, `6.845644678724866e-14 → 3.478181380183418e-09`
— five orders, and the thing the re-derivation has to recover.

---

## 🛑 RETRACTION of my own "AGENTS.md's table is out of date" (2026-09-04, same session)

The section *"A prediction of mine that was wrong, recorded"* above closes with:

> "**Measured: they are identical today**, both at C. `48c84692679` (2026-08-29
> …) fixed it. So AGENTS.md's table describing `q0Value` as stale is itself out
> of date."

**The measurement is right. Both claims I built on it are wrong**, and it is the
second one that matters.

**1. Wrong document.** That table is **not in AGENTS.md** and never has been:

    grep -c "provenance self-stamp" AGENTS.md            -> 0
    git log -S "provenance self-stamp" -- AGENTS.md      -> no commits

It lives in [`docs/audits/2026-08-29-q0-muon-anchor-repin-drain.md`](docs/audits/2026-08-29-q0-muon-anchor-repin-drain.md),
the audit AGENTS.md *points to*. I conflated a cited document with the citing
one — the same class as citing a bean as though it were the corpus.

**2. Not out of date either.** The repair and the audit doc are **the same
commit**:

    48c84692679                                   2026-08-29 08:12:58 +0200
    docs/audits/2026-08-29-...-repin-drain.md     2026-08-29 08:12:58 +0200
      (first == last commit; the file has been touched once)

So the doc's table is not a stale record of a fixed state — it is the
**before-state stated as the rationale for the fix in the very commit that
applied it**, which its own next paragraph makes explicit: *"fixing this file
is not the forbidden re-pin … Bringing `q0Value` from A to C changes only the
self-stamp."* Reading a correctly-dated before/after table as a stale claim is
the inverse of the staleness error, and I made it while writing up a staleness
audit.

**What this does NOT touch.** The underlying measurement stands and nothing
downstream of it moves: `derived_50_digit.q` and `q0Value` are both at C today,
`fvk_selection_probe` reads `q0Value`, and its numbers moved because that field
went A → C. Every figure in commit 3 is unaffected.

**Contamination — three places, checked rather than assumed.** The claim reached
(a) this bean, corrected here; (b) the PR body of #6606, corrected there; and
(c) the commit message of `7296c96e59d`, which cannot be corrected in place and
is left standing with this retraction as its counterpart — rewriting a pushed
commit to tidy a message is worse than an additive correction. The coordination
comments on #6605 and #6595 do **not** carry it; I checked both rather than
assuming.

---

## The class is now GATED, not just reported (2026-09-04, after #6606 merged)

The deferred item *"whether the gate should be extended to key on producer
dataflow rather than on a literal's presence"* is done, as a **ratchet on this
audit** rather than a change to either live q₀ gate — zero blast radius on the
`qou-3f7a` / `qou-cds1` drains, which is why it took this shape.

`--strict` gates against `computations/audits/q0-dataflow-unstamped-baseline.json`.
**Drains only**: `--write-baseline` REFUSES to add an entry and says why.

### The design flaw caught before building, not after

Gating on the **AT-RISK** set — the obvious move — **catches nothing new.**
At-risk means *"predates the 2026-08-22 re-pin"*, so a witness written today
has a later `computedAt`, lands in `newer`, and sails through — while being
**exactly as invisible at the next anchor change**. The date answers *which are
stale now*; a gate must answer *which could go stale unseen*.

So the ratchet keys on the **structural**, date-independent property:

> an anchor-reader witness carrying **neither a q₀ stamp nor a q₀ literal** —
> one that no q₀ gate can see.

That disjunction is right because it is exactly *visible to at least one
existing gate*: anchor-flip reads `q0Anchor`/`q0Value`, value-drift reads q₀
literals. **Baseline at introduction: 13** (3 at-risk + 10 `newer`).

### Verified to actually fire

A gate that cannot fail is documentation — this repo lost weeks to
`precision-gates.sh` being prose nobody invoked (`qou-mnrd`, `qou-82ur`):

| case | expected | got |
|---|---|---|
| clean baseline, `--strict` | rc 0 | **rc 0**, `NEW 0` |
| one baseline entry removed (simulates a new unstamped witness) | rc 1 | **rc 1**, names it, points at the producer |
| `--write-baseline` against a grown set | rc 1 | **rc 1**, *"REFUSING to grow"* |

### Two things the gates told me about my OWN work

1. **This audit's witness must not be committed from a feature branch.**
   `precision-gates.sh` lists it under *"TREE-MEASURING AUDIT WITNESSES MOVED —
   DO NOT COMMIT THESE"* (`qou-v0t8`): it counts things about the tree, so it
   moves whenever main moves, and committing it either walks a drain-only
   ratchet backwards or acquires a recurring conflict. Only the `.py` and the
   baseline are committed here. The baseline is a *different* kind of artifact —
   a drains-only gate input, like `raw-float64-baseline.json`, deliberately
   committed.
2. **A new RED (`float64-padding ratchet`) is NOT mine.** It appeared between
   two gate runs, but attribution was settled by running the padding audit
   directly: every hit is on `qbeta-markov-trace-norm-probe.witness.json` —
   one of the two convention-class witnesses belonging to `qou-cds1` — and
   **zero** on any file of mine. The RED line differed only because main
   advanced ~130 commits between runs. **A comparison against a run on a
   different base is not attribution.**

### A self-inflicted loss worth recording

Mid-way I ran `git status --porcelain | grep '^ M' | awk '{print $2}' | xargs
git checkout --` to revert gate collateral. After a `git stash pop` my own
`.py` and bean edits were *unstaged*, so the blanket revert **destroyed them**
— no stash left to recover from; both had to be re-applied by hand. This is the
exact "revert **by name**, never blanket" rule in AGENTS.md, which I had
already invoked correctly twice in the same session before breaking it. The
failure mode is specifically **blanket-reverting after a stash pop**, when your
own work is unstaged and indistinguishable by status from the collateral.

### A number that moved between measurement and now

Reader count on `main` is **85** (was 86), paired **64** (was 65), AT RISK **3**
(was 4) — a sibling drained one in the interval. Re-measure rather than quoting
these; the audit prints them every run.

---

## First drain: `qbeta-ladder-convention-fee` stamped (2026-09-04, after #6635)

The ratchet's whole point is that it drains, so: **13 → 12**.

The confirmed member of this class is now stamped. Its producer reads **both**
pins — the proton pin via `Q_50_DIGIT_STR`, and the muon pin straight out of
`q-pinning-50-digit.witness.json` — so the honest declaration is `comparison`
(the E1 exception), with a `q0Values` mapping so the audit can **verify each
leg against its canonical pin** rather than take the claim on trust.

### Why this one and not the other twelve

Stamping requires **re-running** the producer, which regenerates its witness —
so a drain is only clean when the re-run moves *nothing but the stamp*. That is
true here and only here, because #6606 already refreshed this witness's values
this morning:

- the **two convention-class** entries (`qbeta-symbolic-tbeta-min-l2`,
  `qbeta-markov-trace-norm-probe`) would commit a **red** — they are
  `qou-cds1`'s, pending the C→D re-derivation;
- the **anchor-class** entries would commit the 2026-08-22 anchor drift, which
  is `qou-3f7a`'s tranche.

Reaching into either would be taking a sibling's work, so the remaining twelve
stay baselined until their own tranches run.

### Measured, not asserted

| check | result |
|---|---|
| did any **value** move? | **no** — stamp only, every payload field byte-identical to `main` after masking |
| `Q0_COMPARISON` | 29 → **30** |
| `Q0_ANCHOR_MISSING` | 1555 → **1554** |
| `Q0_COMPARISON_NO_VALUES` | **0 → 0** — the fvk trap avoided |
| `Q0_FLIP` | 1, unchanged (the pre-existing `hadron-knot-table` one) |
| ratchet | `drained 1`, then `--strict` clean at 12/12 |

The counters were measured as a **delta** — restoring `main`'s unstamped copy
of that one witness by name, running the gate, restoring the stamped copy,
running it again. The absolute numbers had moved a long way from the figures in
this bean's earlier sections (COMPARISON 6, ANCHOR_MISSING 1602) because main
advanced ~150 commits in between, so **quoting them would have looked like my
change did far more than it did.** Measure the delta; never diff an absolute
against a figure recorded on a different base.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
