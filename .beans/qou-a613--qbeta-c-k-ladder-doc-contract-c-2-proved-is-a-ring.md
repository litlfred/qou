---
# qou-a613
title: 'qbeta c_k ladder doc contract: mba sidecar names a canonical c_k compute that records no c_k (F1/F2 superseded by the red-team audit; F3a RETRACTED)'
status: done
type: task
created_at: 2026-08-16T16:47:05Z
updated_at: 2026-08-24T15:10:00Z
---

> **⚠ REWRITTEN 2026-08-16T21:05Z after `origin/main` moved.** The first version
> of this bean claimed three findings. **Two were already recorded — by a better
> audit, hours earlier — and the one I called NEW was wrong.** Original text is
> superseded, not hidden; the corrections are §Corrections below. One finding
> survives.

Verification of a sibling's defect report on PR #5124 (comment 5308056155,
`AGENTS.md:1062`). **No file was edited.**

## The prior art I missed

`docs/audits/2026-08-16-ck-ladder-red-team.md` — bean `qou-cds1`, landed on main
14:26Z, **two hours and twenty minutes before I filed this bean at 16:47Z**. I did
not read it because I never re-fetched `main` between starting the verification
and filing; it arrived in my checkout only at the 21:00Z check-in merge. It is a
merits red-team of the whole ladder and it contains both of my first two findings,
with line cites I did not have, plus consequences I did not reach.

Cheap habit that would have caught this: `git fetch origin main` **before**
filing, not only at check-in. A finding is only new relative to a checkout you
have actually refreshed.

## F1 (superseded) — `c_2 = -1` "PROVED Taylor-exact" is a `ring` tautology

Correct, but **not mine and not new**. Red-team row 1 states it with the line
cite I lacked:

> Lean is a `ring` tautology `1 − b²ℏ⁴ = 1 − (bℏ²)²`
> (`q-beta-c-2-eq-neg-one-structural.lean:50-53`). The load-bearing step — "the
> operator-valued N=2 correction factor *is* `(1 − b²ℏ_q⁴)`" — is in the
> **docstring, not the Lean** (`:2-12`).

It also goes a step further than I did: under D the *implied empirical*
c₂ = **−9.299** (registry §9g:713), so **even c₂ is a C-frame object**. I had
concluded the "PROVED" label overstates the Lean; the audit had already concluded
that *and* that the value itself does not survive the convention ruling.

> **⚠ The −9.299 itself is RETRACTED UPSTREAM (2026-08-21, PR #5348 /
> `qou-cds1`).** The cds1 state synthesis records the sensitivity-table
> `c₃ ≈ −974` and `c₂ ≈ −9.299` as **naive-z-swap artifacts** — the C-frame
> extractor fed `z_D`, which S1 proves invalid — and states they are *not*
> proposed D values and must not be wired or quoted. The paragraph above is
> accurate as a report of what the 2026-08-16 red-team audit said, and is
> **superseded as a statement about convention D**. Flagged rather than
> deleted so the reattribution still reads straight. Note the direction: this
> does not restore `c₂ = −1` under D — it removes a number that was standing
> in for the open question.

## F2 (superseded) — the ladder closes at k=3; c_4 is identically zero

Correct, **and known twice over before me**. Red-team row 3:

> c_4 reproduces as **identically 0** when c_3 is extracted exactly ⇒ the quoted
> −0.972 is "purely the truncation residual of a rounded c_3, zero independent
> content" (registry §3:112-124, **P4 entropy audit PR #3536**).

So this was recorded in the ck-dk registry and in PR #3536 well before today. My
derivation (`c_3 := (Q_codata/Q_prev − 1)/u³` ⟹ `Q_N3 ≡ Q_codata` ⟹ the
`EPS_RESIDUAL` guard is a tautology) is a correct independent rediscovery and
nothing more. I described it on the PR as "sharper than reported" — it was not
sharper than the record, only sharper than the sibling's one-line phrasing.

Still-true details not stated in the audit, kept because they are concrete and
mechanical: `structural_candidates` for k=4..7 is unreachable dead code, and the
producer prints `Q_N7 = …` while holding `Q_N3`.

## F3a — **RETRACTED. My "new" finding was wrong.**

I claimed `AGENTS.md:1062`'s *"N=4 → N=5 non-monotonicity as the experimental
signature"* cites a rung removed in #1416 under a "Superseded (do not restore)"
banner, and that two canonical docs therefore disagree. **They do not.**

What #1416 removed is a **performance claim** — `docs/precision-goals.md:320-323`
supersedes *"Q_β N=5 categorical meets Subgoal-1 (5.7 ppb)"*, i.e. the assertion
that the fitted N=5 ladder **met a target**. It did not retire the observation
that the residual moves non-monotonically across those rungs.

The banner cites the non-monotonicity as a **fit tell** — evidence that the higher
`c_k` are near-matches rather than Taylor coefficients. That is the *anti*-fit
argument, pointing the same direction as #1416, not against it. The red-team audit
uses it in exactly that sense (§(a-4)):

> A convergent series with *exact* coefficients truncates monotonically. The
> residual going +0.055 → +0.63 ppb from N=4 to N=5 is the ladder telling you its
> c_4, c_5 are near-matches, not Taylor coefficients. The canonical framing
> **states this explicitly** (Rule 3) and refuses to call the higher rungs proved.
> That is the discipline working.

So the banner sentence is **correct as written** and must not be "fixed".

**How I got it wrong — this is the campaign's own failure mode, in my reasoning.**
I keyed on the shape *"cites something that was removed"* and fired on a citation
whose content is the **opposite** of the removed claim. I compared two strings
("N=5 … removed"; "N=4→N=5 … signature") without checking what the second was
citing it **for**. That is detector-blindness of exactly the kind
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues — *a detector
is blind to the shape it keys on* — arriving inside the agent auditing for it,
which is the same shape as the `qou-76a6` retraction on this branch.

Had I acted on it unilaterally I would have deleted a correct anti-fit warning
from a STRICT banner. The restraint (flag, do not edit) is what stopped a real
regression, not a formality.

## F3b — SURVIVES: the mba sidecar's Python API and witness contract are both wrong

Independent of the #1416 question, verified directly, and **not found in the
red-team audit or the ck-dk registry** as a defect.

`content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-sidecar-ck-truncation-ladder.md`
states:

> **Python API entry point.** *Canonical compute is the script
> `computations/q_beta_predicted.py`, which records each $c_k$ with its tier in
> the witness JSON.*
>
> **Witness contract.** *Canonical witness: `q-beta-predicted.witness.json`.
> **Must** record each $c_k$ alongside its tier.*

Checked:

- `q_beta_predicted.py` has **no `c_k` logic at all** — it computes the base
  `Q_β = m_e·|q₀²−2q₀−1|·(q₀+1)/(2q₀³)` plus the typed-crossings legacy
  cross-check and the observable/virtual split.
- `q-beta-predicted.witness.json` contains **no `c_k` key and no `tier` key**
  anywhere (data keys: `energy_scale_E_0`, `q_beta_prediction`,
  `q_beta_typed_crossings_legacy`, `observable_virtual_split`). The contract is
  unsatisfied for `c_2` as well, not just `c_3+`.
- The actual `c_k` producer is `computations/qbeta/qbeta_ck_cache.py`, which the
  sidecar never names.

The canonical registry already records the underlying fact —
`ck-dk-canonical-registry.md:211`: *"**Q_β: c_2 only** (`Q_N2`-level).
`q_beta_predicted.py` wires **no** c_3+"* — so the sidecar is contradicted by the
registry it is supposed to bridge to.

This matters because the sidecar sits under the STRICT
Mass-and-Binding-Algorithms appendix-sync banner, whose stated job is keeping
propositions ↔ Python API in sync, and whose enforcement is "reviewers diff the
appendix against the compute". A reviewer following that pointer lands on a script
that implements none of the algorithm above it.

## Corrections

- **F3a retracted in full** (above) — the one I published as NEW, and it was the
  one that was wrong.
- **F1 and F2 reattributed** to `docs/audits/2026-08-16-ck-ladder-red-team.md`
  (`qou-cds1`), the ck-dk registry §3, and PR #3536.
- **"Sharper than reported" withdrawn** — sharper than the sibling's phrasing,
  not than the record.
- PR comment `5308539544` carries the uncorrected version; a correction comment
  follows it.

## Why still unclaimed / nothing edited

F3b is a real doc-contract defect but the repair is a judgement call about what
the sidecar *should* point at (repoint to `qbeta_ck_cache.py` and relax the
contract to what it actually records, vs. make `q_beta_predicted.py` record the
tiers), and it sits under a STRICT sync banner on a channel with a six-entry
flip-flop history. Left `todo` and unclaimed: the verification is done, the
decision is the owner's, and claiming would block a sibling for nothing.

`qou-cds1` is ACTIVE with a sibling — not claimed here. F2 bears on it only as
already-recorded context, not as new input.

---

## F3b RE-VERIFIED 2026-08-23 — still live, unchanged in shape, and one element the original write-up missed

Every claim re-checked against the current tree. **All of it reproduces.**

| claim | state |
|---|---|
| sidecar `.md` says `q_beta_predicted.py` "records each $c_k$ with its tier" | **still there**, `:51-57` |
| sidecar `.md` witness contract "**Must** record each $c_k$ alongside its tier" | **still there**, `:59-63` |
| `q_beta_predicted.py` has no c_k logic | **confirmed** — 0 matches for `c_k` / `tier` / `c_3` |
| `q-beta-predicted.witness.json` has no `c_k`, no `tier` | **confirmed** — 0 matches; `data` keys are exactly the four originally listed |
| real producer is `qbeta/qbeta_ck_cache.py` | **confirmed**, and it *does* record tiers (`:118` `"tier": "derived"`, `:168` `"tier": "cal-anchored"`) |
| registry says "**Q_β: c_2 only** … wires **no** c_3+" | **still there**, now `:230` (was `:211`) |

The only commit to the sidecar since (`67f0ed0d4`, 2026-08-17) touched the tier
table, the pseudo-code and the correctness conditions — the two false paragraphs
were not in that diff.

### NEW — the machine-readable half carries the same error

The original F3b was written about the `.md` only. Its companion
`mba-sidecar-ck-truncation-ladder.ts` repeats the mispointing in the fields the
STRICT banner actually names:

```
:23   script:  "computations/q_beta_predicted.py"
:24   witness: "computations/q-beta-predicted.witness.json"
:12-13 authorNote … "must update both that ledger and the canonical witness
       `computations/q-beta-predicted.witness.json`"
```

with `status: "verified"`. The banner tells reviewers to keep
`computation.script`, `computation.witness` and the `.md` *Python API* section in
sync with the actual compute — **all three are wrong**, and one of them is a
`status: verified` machine field, not prose. That widens the finding: this is not
a stale sentence in a document, it is a stale pointer in the metadata a tool would
read.

### Repair options, and why this still is not mine to pick

- **A — repoint at the real producer** (docs + `.ts`, no compute change). But to
  be *accurate* the contract sentence must also weaken: the cache witness holds
  only **k=2 and k=3** (the greedy guard fires at k=4), and its tier vocabulary is
  `derived` / `cal-anchored`, which does **not** match the sidecar table's
  `structural` / `near-match` / `fitted`. So A is a repoint **plus** a vocabulary
  reconciliation, not a link swap.
- **B — make `q_beta_predicted.py` satisfy the contract.** Regenerates the
  canonical witness and imports cal-anchored (Q_codata-derived) values into the
  one script the registry says deliberately wires **no** c_3+, and which feeds the
  L2 dashboard headline. Cuts against `:230`.
- **C — minimal honesty edit.** Delete the two false clauses, cross-reference the
  cache. Smallest diff, but leaves `computation.script` / `computation.witness`
  in the `.ts` pointing at a script implementing none of the algorithm above it —
  precisely what the banner tells reviewers to diff.

Each option trades a different thing away, and B changes published numbers. **The
verification is now complete and the decision is still the owner's** — which is
what this bean concluded in August and remains the honest position. What is added
today is that the defect is **two files wide, not one**, and that option A is
larger than a link swap.

---

## F3b REPAIRED 2026-08-24 — option A, owner-chosen

Commit `b19342fcc8` on `claude/anchor-followups-2026-08-08`, two files:
`mba-sidecar-ck-truncation-ladder.md` and `.ts`. **No compute ran, no witness
was regenerated, no number changed.**

### Every line number in this bean re-verified before editing

| bean's cite | state in this tree |
|---|---|
| `.md:51-57` Python API "records each $c_k$ with its tier" | **exact**, reproduced |
| `.md:59-63` witness contract "**Must** record each $c_k$ alongside its tier" | **exact**, reproduced |
| `.ts:23` `script: "computations/q_beta_predicted.py"` | **exact** |
| `.ts:24` `witness: "computations/q-beta-predicted.witness.json"` | **exact** |
| `.ts:12-13` authorNote naming the same witness | **exact** |
| `q_beta_predicted.py` has no c_k logic | **confirmed** — 0 hits; the file is the single-wrap closed form + typed-crossings legacy + observable/virtual split |
| `q-beta-predicted.witness.json` has no `c_k`, no `tier` | **confirmed** — `data` keys are exactly the four listed |
| `qbeta_ck_cache.py:118` `"tier": "derived"`, `:168` `"tier": "cal-anchored"` | **exact**, both |
| registry `:230` "**Q_β: c_2 only** … wires **no** c_3+" | **exact** |

**Nothing had been fixed by someone else in the interim; every claim still
reproduced.** The only number that had moved since the 2026-08-16 filing was
the registry line (`:211` → `:230`), which the 2026-08-23 re-verification had
already caught.

### What the repair actually did

Both files now point at `computations/qbeta/qbeta_ck_cache.py` and
`computations/qbeta/qbeta-ck-cache.witness.json` — `computation.script`,
`computation.witness`, the maintenance-contract authorNote, and the `.md`
*Python API* / *Witness contract* sections.

The contract was **relaxed to what that witness holds**, read off the file
rather than assumed:

- Per rung: `k`, `c_k`, `tier`, `q0_dependent`, `Q_pred_after_this_rung_MeV`,
  `err_ppb_after_this_rung`; above `k = 2` also `structural_candidates`,
  `closest_structural`, `closest_structural_err_pct`. Plus `data.q_0` and the
  top-level `q0Anchor` / `q0Value` stamp.
- **Bound to the rungs the extraction reaches, not to `N`.** The cache holds
  **exactly two rows** (k=2, k=3) — measured, matching the bean's prediction and
  `AGENTS.md`'s greedy-guard correction.
- The `tier` vocabulary is stated as the producer's own two-value
  production-semantics axis (`derived` / `cal-anchored`) and stated to be a
  **different axis** from the `.md`'s editorial tier column
  (`structural` / `near-match` / `fitted`). That is the vocabulary
  reconciliation option A required, done without rewriting a published tier.

### Registry consistency

`ck-dk-canonical-registry.md:230` is untouched and uncontradicted:
`q_beta_predicted.py` keeps its place as the **step-11** production script
(`alg:q-beta-truncation`, whose own `.ts` still points at it), and the repaired
sidecar says in as many words that no c_3-or-beyond rung reaches production.
Only the **c_k-ladder sidecar** moved.

### Validators run

| what | result |
|---|---|
| `scripts/check-computation-status.py --files <ts> --strict-unbacked` | **exit 0** — 1 block/witness pair, 0 disagreements, unbacked: none. The new witness path resolves and is backed by a real assertion (`c2_extraction_matches_lean_proved_value`, `allPassed: true`), so `status: "verified"` stays honest. |
| `content/pipeline/block-manifest-audit.ts --diff <ts> <md>` | **exit 0** — manifest loads and is listed |
| `scripts/run-validate.ts content/quantum-observable-universe` | **Valid — 4 issue(s)**, all in unrelated blocks; this block does not appear (baseline unchanged) |
| `scripts/check-sidecars.sh <md> <ts>` | **no flags** |

### Two things left deliberately, both reported rather than fixed

1. **`.qa.json` not refreshed.** `qa-sweep.ts` on this block alone recomputes
   `cone_size` 130 → 1 and `depth` 34 → 1 — an artifact of loading one block
   instead of the corpus `uses` graph, so landing it would replace real metrics
   with garbage. Reverted; a corpus-wide sweep is the way to refresh it.
2. **Pre-existing `voice-unicode-crash` critical at `.md:23`** (the `→` in the
   `N=4→N=5` table row). Recorded as `fail` in the committed sidecar since
   2026-08-09, outside this change's diff, and inside the very sentence F3a
   established must not be "fixed" on content grounds. Left alone.

### Adjacent inconsistency found, NOT fixed

`.md:14-15` (algorithm **Output**) still lists the tier vocabulary as
`proved` / `near-match` / `fitted`, while the tier table nine lines below says
**structural** — `67f0ed0d4` swept the table, the pseudo-code and the
correctness conditions but missed this line. That is F1's territory (the
"proved" label), which this bean records as superseded and which was
deliberately scoped by that commit; it is not F3b and not a pointer defect, so
it was left for whoever owns the F1 sweep.
