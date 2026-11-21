---
# qou-cjkt
title: Cite 9504015v2.pdf at folio/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneRTSurgeryCon…
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:47Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

KeystoneRTSurgeryConstruction.lean carries the RT/WRT = Chern-Simons identification as a named, cited-but-unformalised hypothesis whose '-- Ref:' list currently names only Reshetikhin-Turaev 1991 / Turaev 1994 and beasleywitten2005. Adding this paper documents the perturbative form of that identification and its explicit verification on the Seifert class the file's manifold belongs to, so a reader can see how far the cited literature actually goes. It documents the hypothesis; it does not discharge it, and the file's honest-scope banner should stay unchanged.

**From the source**
- Proposition 1.1, p. 5 (proved in Section 3; verified for lens spaces and Seifert manifolds in Section 4) — Ohtsuki's invariants lambda_n(M) and the loop corrections S_n(M) to the trivial-connection contribution determine each other through sum_n lambda_n(M) x^n = exp[ sum_{n>=1} (S_n(M) - S_n(S^3)) (i pi/K)^n ] evaluated at x = exp(2 pi i/K) - 1, with S_1(M) = 6 lambda_CW.
  Use here: Gives the keystone's Chern-Simons framing its literature warrant at exactly the manifold class it needs: the identification is verified in Section 4 for Seifert manifolds, the class containing S^3/2I = Sigma(2,3,5). It says the perturbative expansion of a localized CS partition function on that manifold is the exponential of the connected loop corrections whose resummation is the Ohtsuki series — the step the Beasley-Witten route (#2524) takes for granted.
- Equation (1.6), p. 3, with equation (4.28), Section 4 — The Kirby-Melvin surgery formula for Z'(M;k) as a sum over odd colours of the framing-independent coloured Jones polynomial weighted by prod_j sin(pi alpha_j/K); and, for the Seifert surgery link of N unknots linked to a single unknot, the explicit sine-product coloured Jones J_{beta,alpha_1..alpha_N}(L;k) = prod_j sin(pi beta alpha_j/K) / [sin^{N-1}(pi beta/K) sin(pi/K)] up to normalisation.
  Use here: The per-colour weight sin(pi alpha/K) is the S-matrix vacuum row d_alpha/D that KeystoneRTSurgeryConstruction.lean proves the RT surgery sum weights each label by — so (1.6) is an explicit analytic instance of the assembly that file formalises abstractly. Equation (4.28) then gives the coloured Seifert link invariant in closed sine-product form, which is the machinery the colored-Sigma(2,3,5) step needs to lift the bare closed-manifold number to a lambda-indexed family. Useful as a cited construction to build against; it is not a substitute for the carried (RT) hypothesis.

Source: `library/arxiv-q-alg-9504015v2/9504015v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-q-alg-9504015v2/  ->  [rozansky1995]
  Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [rozansky1995] as the citation key when you do it.

## 2026-11-21 — expo-cite-xcheck drain

`Ref: [rozansky1995]` added to KeystoneRTSurgeryConstruction.lean (Prop 1.1 is on p.6 of the held copy, not p.5); honest-scope banner unchanged. Completes on merge. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.

## 2026-11-21: merged

Completed: PR #8852 merged (merge 4d8767a1c).
