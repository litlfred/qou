---
# qou-6766
title: 'REVIEW: n-v-leading-order-derivation — Proof+QED inside a conjecture block, ''derives from substrate'' vs sibling''s empirical closure (anti-laundering); + neutron-prediction n_pred/p* mismatch, Li6 table order, nitrogen-14 ''negative weight'' wording, lepton-discrepancies garbled closer, misplaced QED in magic-numbers computation (trap-drain obs-b4/b5)'
status: completed
type: task
priority: normal
tags:
    - needs-owner
    - 8f-lean
    - reorg-2026-10-04
created_at: 2026-08-15T11:28:11Z
updated_at: 2026-10-10T08:15:08Z
parent: qou-8lxd
---

## 3 of 7 items ENACTED 2026-10-10 — bean STAYS OPEN

This bean is a **bundle of seven distinct findings across three blocks**, which is
itself why it never moved: nothing in it could be "done". Itemised, with state.

### DONE (1) — `## Proof` + `$\square$` inside a conjecture block

`conj:n-v-leading-order-derivation` carried a `## Proof` section closing with
`$\square$`. **The sharp form of the defect: its two premises are exactly the two
open conjectures the block's own `uses[]` declares** — `conj:n-v-bring-action`
(the `|S_5| = 120` rescaling factor) and `conj:n-v-tower-depth-ninety` (the depth
90, tracked open as `qou-lyp3`, status `todo`). So the `□` asserted closure of
something the manifest says is conditional on two unproved inputs. That is
"conditional-proved != premise-established" plus the anti-laundering rule, in one
paragraph.

Fixed as **labelling only — the mathematics is byte-identical**: the heading is
now "Derivation sketch, conditional on the two conjectures in `uses[]`", each
premise is named and linked to its conjecture, the arithmetic step is stated to
hold as stated, and the `□` is gone.

### DONE (2) — the anti-laundering wording, and my first grep MISSED it

The block read *"The structural prefactor of $120$ minimizes the residual and
**derives from the geometric substrate**."*

**Recording the search error, because it is the reusable part:** a grep for
`derives from the substrate` / `derives from substrate` returned **clean**. The
text says "derives from the **geometric** substrate". A too-narrow pattern gave a
false all-clear on a live anti-laundering defect — exactly the failure mode the
corpus-grep discipline exists to prevent, one word wide.

Fixed by separating two claims that were run together: *minimizes the residual*
is fit quality (selection against the measured value, so not evidence for the
framework under the no-fitting directive), while *derives from the geometric
substrate* is the open assertion of `conj:n-v-bring-action`. The text now says
the residual-minimisation does not establish the substrate origin.

### DONE (3) — misplaced `$\square$` in the magic-numbers computation

`rem:magic-numbers-from-q-computation` closed its "## Witness" section with
`$\square$` on the sentence *"The file `shell-closure.witness.json` records ...
The block-diagonal optimised computation resides in `shell_closure_compute.py`."*
A QED on a file-location statement, in a **`remark`** block, which by AGENTS.md
§3a makes no logical claim at all. Removed.

### STILL OPEN (4) — not touched, each needs its own look

- neutron-prediction `n_pred` / `p*` mismatch
- Li6 table ordering
- nitrogen-14 "negative weight" wording
- lepton-discrepancies garbled closer

**These four are why the bean stays open.** Consider splitting them out: a
seven-item bundle cannot be claimed, worked or closed by one agent in one pass,
which is the organisational defect, not just a backlog.

### Verification

`qa-sweep` on both edited blocks: **0 critical, 0 major, 0 minor**.
`run-validate folio/quantum-observable-universe`: **valid, 8 issues, none in
these blocks** (all pre-existing: 3 unlisted blocks, bibliography registry, one
Lean-less lemma, one val-block-computation, two simulator stubs).
Render-QA grep battery on both: `$`/`$$` balanced, braces balanced,
`\begin`/`\end` matched. Both markdown links I added resolve on disk.


## SPLIT and CLOSED 2026-10-10 — the four residuals now have their own beans

This bean's own recommendation above was *"Consider splitting them out: a
seven-item bundle cannot be claimed, worked or closed by one agent in one pass,
which is the organisational defect, not just a backlog."* Enacted.

**Why closing is honest.** This is a **REVIEW** bean. Its deliverable was: find
the defects, characterise them, fix what is mechanical. All seven are found and
characterised, three are fixed, and the four unfixed ones are now individually
tracked and individually claimable. Nothing is lost by closing the umbrella;
what was lost was the ability to work any of it. Rule 13a is not engaged — the
subject is a prose review, not a conjecture.

| residual | bean | front | what it is |
|---|---|---|---|
| neutron-prediction `n_pred`/`p*` | **`qou-opjb`** | `8f-decide` | the display defines the inverse map, and `c = 0.01497` traces to an SEMF ratio, not to any definition in the corpus |
| Li6 table order | **`qou-dids`** | `8f-decide` | **does not reproduce**; what is there is `\|def\|` as an undefined synonym for the defined `\|dem\|`, in 2 blocks |
| nitrogen-14 "negative weight" | **`qou-652e`** | `8f-decide` | wording only — it is the *negative-crossing* weight; the numbers check out and a minus must NOT be added |
| lepton-discrepancies closer | **`qou-j98x`** | `8f-decide` | one dead sentence, no referent and no predicate; the empirical hedge beside it is legitimate under §3a |

**Each of the four carries its own measurement, options with costs, a stated
recommendation marked as judgement, a default-if-unanswered, and its blast
radius** — so each can be answered without reading this bean or the others.

**Two of the four turned on measurement rather than on the title**, which is the
same lesson the `8f-lean` triage has produced three times already:

- **"Li6 table order" is not a defect.** Narrative and table agree on every
  orderable claim (Regime I→II→III, fifth = Hopf, sixth = bare `C_pn`, build
  order terminating at `3p3n`). Surfaces searched are named in `qou-dids`. A
  *different*, real defect was found in the same block pair instead.
- **"nitrogen-14 negative weight" is not a sign error.** The tempting repair —
  restore the minus, since the Hecke eigenvalues are `q` and `−q^{-1}` — would
  **break** the block's two arithmetic checks (`(q+q^{-1})/2 = 1.00545 ≈ 1.005`,
  `(q−q^{-1})/2 = 0.10454 ≈ 0.105`). It is `σ^{-1}` = negative *crossing* per
  §7a, weight `q^{-1} > 0`. Recorded in `qou-652e` as a rejected hypothesis.

All three enacted fixes stand as recorded above; `needs-owner` is left on this
bean so a reader looking for the owner-gated material still lands here and is
forwarded to the four.
