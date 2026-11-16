---
# qou-5p7n
title: 'EPIC: §3b disclosure backlog — 125 of 147 self-assuming projections lack the disclosure sentence'
status: in-progress
type: epic
priority: normal
tags:
    - epic
    - vacuity
    - issue-2472
created_at: 2026-08-10T01:47:52Z
updated_at: 2026-11-16T21:22:30Z
parent: b9cj
---

The scanner's §3b placeholder exemption is justified by a stated premise: that these docstrings *"honestly state the content is carried by the context-class axioms with derivation pending"*. PR #4882 codified the honest-placeholder criterion and measured that premise against the 52 §3b-exempt declarations — it failed for 28 of them (54%).

Re-measuring across **all 147** `proof-no-self-assuming-projection` hits (exempt + non-exempt, not just the §3b subset):

| class | count |
|---|---:|
| discloses — premise holds | 22 |
| **asserts `**Theorem/Proposition**`, no disclosure** | **3** |
| **literature-cited, no disclosure** | **24** |
| **bare, no disclosure** | **98** |

So **125 of 147 (85%)** carry no disclosure. Split into four child beans by class and by whether the scanner currently exempts them.

The criterion, the worked examples, and the reason bulk axiom-conversion is unsound: `docs/audits/2026-08-09-honest-placeholder-criterion.md`.

Scope note: this is *disclosure* work — making the prose match what the Lean does. It does not by itself repair any vacuity. A declaration that discloses honestly and remains an unproved projection is fine per §3b; one that does not disclose is a dishonest dodge regardless of the mathematics.



## Reorganisation 2026-10-04

Now the epic for P2.HYG under UMBRELLA: open conjectures (formal mathematics only).

### Round 51 Update (PR #8206)
- [x] Devacuified `qou-zzhw`, `qou-1vu3`, `qou-w61k`, `qou-sz98`, `qou-00c5` in PR #8206 (`aecfe3f528c442bfb5e105f53d801fa139604119`).
