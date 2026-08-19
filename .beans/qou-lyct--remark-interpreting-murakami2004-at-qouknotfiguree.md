---
# qou-lyct
title: Remark interpreting [murakami2004] at QOU.Knot.FigureEightComplexVolume
status: todo
type: task
created_at: 2026-08-08T23:35:13Z
updated_at: 2026-08-08T23:35:13Z
---

The ref() note carries an explicit 'not independently verified, a reader should confirm' caveat and records the v1 title/single author. The uploaded v3 is now in the corpus and the q_eval normalisation is confirmed verbatim; the caveat should be discharged and the entry aligned with the uploaded version (added author, revised title).

**From the source**
- Thm 2.2 + Cor. 2.4 — There is a neighbourhood U of 0 in C on which (u + 2 pi i) lim_N log J_N(E; exp((u + 2 pi i)/N))/N exists, defines a complex-analytic H(u) with H(0) = i Vol(S^3 minus E) and dH/du = v + pi i; Cor. 2.4 turns this into Vol and CS of the manifold obtained by generalised Dehn surgery at u.
  Use here: Supplies both the exact q_eval = exp((u + 2 pi i)/N) normalisation the corpus uses and the 'small |u| only' control region that FigureEightDeformedMeridianWinding.lean needs for its scope-(a) exclusion of the winding-lattice route to an anchor-free q_0.

Source: `library/arxiv-math-0401084v3/0401084v3.pdf` (`murakami2004`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
