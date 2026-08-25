---
# qou-qspu
title: Obtain and triage Kang-Lee-Lee-Oh 2002 — the q-deformed type-A GS basis qou-auq3 needs
status: todo
type: task
priority: high
created_at: 2026-08-09T18:28:16Z
updated_at: 2026-08-09T18:28:16Z
---

S.-J. Kang, I.-S. Lee, K.-H. Lee, H. Oh, "Hecke algebras, Specht modules and
Groebner-Shirshov bases", J. Algebra 252 (2002), 258-292.

WHY THIS IS THE ONE TO GET. `qou-auq3` wants a Groebner-Shirshov basis for
H_n(q) as the only route from n <= 4 to general n. The source the folio has been
attributing that to is Bokut & Shiao 2001 ([bokut2001], entry created
2026-08-09), but every document in the nine-PDF triage batch describes
Bokut-Shiao as a theorem about Coxeter GROUPS -- W = sgp<S | (ss')^m = 1>, q = 1
-- and none of them mentions H_n(q) in connection with it. Whether the
group-level GS basis lifts to the q-deformation is exactly the load-bearing
question, and it is currently assumed rather than checked.

Two independent bibliographies in the batch (library/arxiv-1808.05026v1/1808.05026v1.pdf intro and
library/fd58d8e1...pdf intro) say the same thing in the same words: "The cases
for Hecke algebras and Temperley-Lieb algebras of type A were calculated in
[Kang-Lee-Lee-Oh]." Both papers quote its Prop. 6.2 verbatim for the
Temperley-Lieb half. So this is the paper that treats the deformed, type-A case
the folio actually computes with.

WORK:
1. Obtain the paper (J. Algebra 252 (2002) 258-292); add it to library/ and
   reseed the source ledger.
2. Triage it under the paper-relevance-triage skill.
3. If its section 6 does state the GS basis for H_n(q) of type A, create the
   ref() entry and wire it into `qou-auq3` as the source for the completion,
   and into `def:hecke-normal-form` (see the confluence-defect bean).

HONESTY FLAG: this paper has NOT been read. Everything above is from two other
documents' bibliographies and introductions. Do not cite it as load-bearing
before reading it.
