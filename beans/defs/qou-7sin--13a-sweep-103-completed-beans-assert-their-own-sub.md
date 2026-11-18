---
# qou-7sin
title: '13a sweep: 103 completed beans assert their own subject is still open (candidates, NOT a violation count)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:13:32Z
updated_at: 2026-10-10T14:48:42Z
parent: qou-5vkl
---


## Measured 2026-09-07 on `main` `1a97d5017` — and the headline number is a CANDIDATE SET, not a finding

AGENTS.md **§13a** landed 2026-09-06 (`c1b63ac76d`, owner, verbatim *"Don't
close beans with open conjectures!!!"*). It is retroactive in force but nobody
has swept the existing tracker against it. This bean is that measurement, and
its main job is to stop the number being quoted as a violation count.

### Two scans, and the gap between them is the point

| scan | matches | what it means |
|---|---|---|
| any of `conjectur` / `not established` / `not proved` / `remains open` … | **372** of 2627 completed | **high recall, near-useless** |
| only phrases asserting the subject is open (`remains open`, `stays open`, `is still open`, `remains unproved`, `remains conjectural`, `the CHOICE is open`) | **103** of 2627 completed | the workable candidate set |

**Do not quote the 372.** `conjectur` matches any bean that *mentions* a
conjecture, and **"Not established"** is a standard section heading in these
bodies — it appears in beans whose closure is entirely legitimate, because
writing down what you did *not* establish is exactly what this corpus asks for.
A detector keyed on it flags good practice.

Tracker composition for reference: completed 2627, todo 1774, in-progress 489,
scrapped 150, done 43, open 3, draft 1.

### The 103 are candidates. Hand-read n = 8, and roughly half survived

| bean | verdict | why |
|---|---|---|
| `qou-yvly` | **likely violation** | titled *"GAP: per-element JM eigenvalue … (Ram Thm 4.1)"*; body says *"Ram Thm 4.1 remains open"*. The named subject is open. |
| `qou-dr8m` | **likely violation** | titled *"MFW lower bound for braid index …"*; body says *"MFW itself remains UNPROVED here"*. |
| `qou-g8i1` | **likely violation** | titled *"Prove the (z+d) bond rule"*; body says the entire mathematical content now sits in one equation *"which is what remains open"*. |
| `qou-3kos` | **likely** | *"A_ω = 3 remains open pending hibinv + hratio"* — and §13a's own text names the `A_ω → S` identification (`qou-q3np`) as its example. |
| `qou-b3nk` | ambiguous | subject was registry registration (mechanical); the open residue is the decay channel's fibre, adjacent. |
| `qou-8p1a` | ambiguous | its own task was the enumeration; the open thing (Bring → Klein degeneration) is adjacent. |
| `qou-y2o7` | **not a violation** | *"stays open"* refers to a **different** bean's A/B/C cost decision. |
| `qou-cp1w` | **not a violation** | subject was a `wb.write()` API defect — mechanical, which §13a explicitly permits closing. |

So ~4 of 8 look genuine. **n = 8 is far too small to state a rate**, and the
honest reading is "the true count is plausibly several tens, not 103 and not 0".
Anyone continuing this should hand-read a larger sample before quoting any
percentage — this corpus has repeatedly had an over-flagging estimate quoted as
a measurement, in both directions.

### The discriminator, for whoever drains it

The signal is **not** whether the body says something is open. It is whether the
**thing named in the title** is what is open. Three of the four negatives above
fail on exactly that: the open item is a sibling bean's scope, an adjacent
question, or a residue of a subject that was itself mechanical. A scan cannot
make that call — §13a is an agent judgement by construction.

### What is deliberately NOT done here

**No bean was reopened.** Reopening 103 beans is a large sweep that changes the
tracker's shape and starves nothing but also decides nothing; and reopening on a
keyword match would re-run the exact error §13a exists to prevent, one level up.
The direction is at least conservative — §13a's default is *stay open* — but it
is still a sweep, and it wants scoping.

### Open question for the author

Whether to drain this at all, and how. Options, with what each costs:

* **(a) Do nothing.** The 103 keep their `completed` status. Cost: §13a is
  retroactively unenforced, and a future corpus-grep on any of the ~4-in-8
  genuine ones reads "answered" when the mathematics is open — which is the
  precise failure §13a names. **This is the default if nothing is said.**
* **(b) Hand-adjudicate the 103.** Cost: a real tranche, ~103 bean bodies read
  by an agent applying the title-vs-body discriminator. Reversible per bean.
  Buys an accurate tracker.
* **(c) Reopen all 103 mechanically.** Cheap and **not recommended** — it would
  reopen the ~50 % that are legitimately closed, and the noise lands in the
  §4 idle-backlog policy that reads open beans for signal.

**My judgement, not a finding: (b), and scoped to the `likely` tier first** —
a bean whose *title* is "Prove X" or "GAP: X" while its body says X is open is
mechanically identifiable and is where the whole risk sits. (a) is a defensible
place to stop; (c) is not.
## 2026-09-08 — ADJUDICATED. The drainable core is **18**, and it needs no judgement at all

The n=8 hand-read above proposed a title-vs-body discriminator. Reading the
candidates turned up a **better** one, and the number it gives is smaller and
far harder to argue with.

**The discriminator: does the bean's own body say THIS BEAN is open?** Not
"something is open" — *this bean*. That is a self-contradiction against its own
`status: completed` field, decidable by reading one sentence, and it requires
judging no mathematics whatsoever.

| bucket | count |
|---|---|
| candidates (strong open-language, `completed`) | 103 |
| sentences asserting **this bean** is open | 20 |
| — genuine self-contradictions | **18** |
| — false positives on reading | 2 |
| rejected by the negation / delegation guard | 4 |

**The two false positives, and why a machine cannot drop them.** `qou-2yrn`'s
*"it does not close the conjecture, which remains open"* is a correct scope
note — that bean's subject was a status question ("is `res≠0 ⇒ P≠NP` a theorem
or an assumption in the corpus?"), which it answered. `qou-b5yi` quotes **its
own closing line** about a *different* bean (`qou-0hdx`, since scrapped).

**Four more were caught by guards that the first pass did not have**, and one
was my own error of exactly the kind this bean is about: `qou-1ucq` matched on
*"remains open on this bean"* when the sentence reads **"Nothing remains open
on this bean."** — the negation ran in an `elif` and was shadowed by the match
it was meant to veto. `j7j2` and `qou-looi` say *"stays open (bean qou-b2ie)"*,
i.e. the open item is **delegated to another bean**, which is correct practice.
`qou-qb8f` says *"stays open (NOT this bean's to close)"* — it anticipated the
misreading in its own text.

### The sharpest case

`qou-8dlq` was updated **2026-09-07**, the day *after* §13a landed, and its body
cites the rule verbatim — *"Bean stays OPEN per owner rule (AGENTS.md 13a): its
subject is the bridge's tier, which is an open conjecture."* — above a
`status: completed`. **The rule was applied in the prose and not in the field.**

Two others name the status they should carry and do not have it: `qou-j6gb`
(*"Bean stays open with status in-progress until the `literal` count reaches
0"*) and `qou-qexu` (*"the reason this bean is in-progress, not completed"*).

### What was done

All 18 set `completed` → `in-progress`, each with a note recording that only the
status field moved. **No finding was revisited and no mathematics was judged** —
the body already said what the status should be.

### What was NOT done, and remains the author's call

The other **79** candidates are the genuine judgement tier: a bean whose body
says something *adjacent* is open (a sibling's scope, a downstream question, a
residue of a mechanical subject). §13a is an agent judgement there by
construction, and n=8 gave roughly half genuine — too thin to act on. Draining
that tier is a real tranche and is still unclaimed.

## 2026-10-10: one confirmed false positive, `qou-8p1g`

`qou-8p1g` was reopened on 2026-09-08 because its body says "NOT closing … the open
question is unchanged". The very next section of the same body is headed "the open
question is CLOSED" and answers it with a scope-(b) exclusion, backed by a 23/23
witness. Re-closed, with the evidence appended there. The discriminator should read the
**last** word a bean has on its own openness, not any paragraph that asserts it, because
these beans are append-only ledgers and supersession is always by a later section.

- **Round 96 (`litlfred/qou#8428`)**: Advanced in `feat/round96-milnororder-signrep-mirrorsplit-multibond-moebius-43c1` (Commit 1 `22d991a251c6bf1bcf86f7ea08f935c2c280b7b3`, Commit 2 `391eb320415cc99c2e005cd0ffab67710cb6bc1d`, probe sha256 `94f6f6be6af6f9daa73f3911e2df79962cba2a56eed95434d4d929e3d5348851`).
