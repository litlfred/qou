---
# qou-7sin
title: '13a sweep: 103 completed beans assert their own subject is still open (candidates, NOT a violation count)'
status: todo
type: task
created_at: 2026-09-07T18:13:32Z
updated_at: 2026-09-07T18:13:32Z
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
