---
# qou-u59p
title: Apply 1104.0755v2.pdf at content/quantum-observable-universe/lean/QOU/Archimedean/AwZeroLocalizat…
status: todo
type: task
created_at: 2026-08-08T16:13:04Z
updated_at: 2026-08-08T16:13:04Z
---

Hypotheses verified to hold, not merely 'related': the paper's A_q is the corpus's A_w term-for-term, and its standing assumption 0 < |q| < 1 is satisfied. The identity supplies the exact theta-factorised form of A_q at infinity that the audit's recentring argument constructs approximately. SCOPE, stated honestly: it does not by itself yield zeta_n = w^{1-2n}(1 + O(w^n)) — the argument-principle/Rouche step against the theta zero lattice still has to be run — but it replaces the hand-built theta limit with a published exact identity, which is the part of the debt that is currently unbacked.

**From the source**
- Theorem, §1 p.4 (proved in §4) — For all x in C*, A_{q^2}(-q^3/x^2) = (1/(q,-1;q)_infinity) * { theta(x/q) Ai_q(-x) + theta(-x/q) Ai_q(x) }, where theta is the Jacobi theta function and Ai_q the q-Painleve q-Airy function.
  Use here: An exact closed-form theta factorisation of the Ramanujan function A_q, valid for all x in C*. The corpus's Rouche argument compares A_w against a theta LIMIT obtained by recentring; this identity is the exact statement that comparison approximates, so the zero asymptotics zeta_n = w^{1-2n}(1 + O(w^n)) can be read off the theta zero lattice with the error controlled by the Ai_q factors rather than by a hand-built limit. Hypotheses check out: 0 < |q| < 1 matches the corpus's 0 < w < 1 (set q^2 = w), and the series definitions coincide exactly.
- eq. (4) and Remark 1, §3.1 p.6 — A_q satisfies the q-difference equation (q x sigma_q^2 - sigma_q + 1) u(x) = 0, whose second solution is u(x) = theta(x) * 2phi_0(0,0;-;q,-x) with the 2phi_0 series DIVERGENT.
  Use here: Shows the theta function is intrinsic to the q-difference equation A_q solves — it is the multiplier attached to the divergent second solution, not an artefact of a chosen comparison. That is the structural reason the corpus's theta-limit step works, and it is the level-1 q-Borel kernel picture (t_n = q^{n(n-1)/2}) that QBorelKernel.lean already formalises, now instantiated on a function the corpus actually uses.
- Lemma 1, §2 p.5 — Jacobi's triple product identity: theta(x) = (q, -x, -q/x; q)_infinity.
  Use here: Exactly one of the three analytic steps AwZeroLocalization.lean names as not formalised ('Jacobi triple product, Rouche, the argument principle'). Having it stated with the paper's own normalisation removes the normalisation ambiguity when that step is eventually formalised or cited.

Source: `library/arxiv-1104.0755v2/1104.0755v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
