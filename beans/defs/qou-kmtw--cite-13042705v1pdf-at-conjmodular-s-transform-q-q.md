---
# qou-kmtw
title: Cite 1304.2705v1.pdf at conj:modular-s-transform-q-q-tilde
status: todo
type: task
priority: normal
created_at: 2026-08-08T16:13:08Z
updated_at: 2026-08-21T17:04:58Z
---

conj:modular-s-transform-q-q-tilde asserts modular continuation and a q<->q~ duality with no explicit factorisation anchor in its cites[] (kashaev1997, neumann-zagier1985, kashaev-tirkkonen2014). Cor. 1.7 is a proved instance.

**From the source**
- Cor. 1.7(a), eq. (14)-(15) — The Andersen-Kashaev state integral of the figure-eight knot factorises as I_{4_1}(b) = -(i/2)(q/q~)^{1/24}( b·G(q)g(q~) - b^{-1}·G(q~)g(q) ), an explicit bilinear pairing of two q-hypergeometric series evaluated at q and at the modular partner q~.
  Use here: A proved, explicit instance of the q <-> q~ pairing that conj:modular-s-transform-q-q-tilde asserts abstractly (its Open R&D item 1 asks precisely for framework quantities with well-defined modular continuation). It is also the source of the two 4_1 q-series whose Stokes matrix supplies the certified S^+(0)_{01} = 3 datum feeding A_omega(4_1).
- Lemma 1.5(a), eq. (10) — F_{A,B}(q^{-1}, x) = F~_{A,B}(q, x) — inverting q exchanges the series with its modular partner.
  Use here: Directly relevant to the folio's bar-vs-S-transform bookkeeping: the D14 block argues that only q_0^{-1} ~ 0.901 lands in the upper half-plane, so the modular sector is intrinsically bar-symmetric. This lemma is the literature statement of that bar/modular exchange at the level of the q-series themselves.

Source: `library/arxiv-1304.2705v1/1304.2705v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1304.2705v1/  ->  [garoufalidis2013]
  FROM STATE INTEGRALS TO q-SERIES

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis2013] as the citation key when you do it.
