---
# qou-a613
title: 'qbeta c_k ladder doc contract: mba sidecar names a canonical c_k compute that records no c_k (F1/F2 superseded by the red-team audit; F3a RETRACTED)'
status: todo
type: task
created_at: 2026-08-16T16:47:05Z
updated_at: 2026-08-24T03:50:00Z
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
