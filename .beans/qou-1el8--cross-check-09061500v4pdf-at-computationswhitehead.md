---
# qou-1el8
title: Cross-check 0906.1500v4.pdf at computations/whitehead_c_sigma_torsion.py
status: todo
type: task
priority: normal
created_at: 2026-08-08T16:13:01Z
updated_at: 2026-08-21T17:04:39Z
---

Recompute |tau_adjoint| for 4_1 and for the Whitehead link L5a1 by the Theorem-5 derivative formula on the Wirtinger presentation, and compare against the corpus values sqrt(3) and 2^{5/2}. This is the highest-value item in the slice: it adjudicates a refuted computation (bean qou-fl4t) with a method that is triangulation-independent by construction, and it either restores or kills the c_sigma = 2^{-3/4} derivation.

**From the source**
- Theorem 5, §6 (eq. (15)) — For a hyperbolic M with b torus boundary components satisfying (A_M), (A_phi), (A_rho), lim_{t->1} Delta^{phi (x) Ad.rho}_M(t) / prod_{l=1..b}(t^{a_l} - 1) = (-1)^b * T^lambda_M(rho), i.e. the derivative of the twisted Alexander invariant at t = 1 computes the non-abelian (adjoint) Reidemeister torsion for the multi-longitude lambda — for LINK exteriors, not only knot exteriors.
  Use here: A route to |tau_adjoint(L5a1)| that does not pass through an ideal triangulation, replacing the |det J| construction refuted in bean qou-fl4t. The multi-component (b > 1) generality is the part that matters: the earlier corpus work needed the Whitehead link (b = 2) and would need the Borromean rings (b = 3) next.
- §4 'Examples of computations', p.12 onward — Explicit computation of the polynomial torsion for the figure-eight knot exterior and for the Whitehead link exterior, via Fox free differential calculus on Wirtinger presentations.
  Use here: Both QOU anchors done in the source. The 4_1 case is the non-circular calibration (known |tau| = sqrt(3)); the Whitehead case is the disputed value. Running the corpus's number against the paper's own computation is a direct, cheap adjudication of the 4*sqrt(2) vs 2*sqrt(2) discrepancy that motivated the per-cusp 2^{(c-1)/2} factor.
- Theorem 14 + eq. (32), §8, p.23 — Duality with sign: Delta^{phi (x) Ad.rho}_{E_L}(t^{-1}) = (-1)^b * Delta^{phi (x) Ad.rho}_{E_L}(t) for a link exterior with b boundary components (sign term epsilon = (-1)^{b(b-1)/2} computed in Prop. 16).
  Use here: A proved bar-involution (t -> t^{-1}) parity law for the torsion polynomial, with the parity set by the component count b. QOU's bar-even/bar-odd bookkeeping is currently asserted per-object; this is an external, proved instance of exactly that symmetry on an object the corpus already computes, and it is a falsifiable constraint on any candidate torsion polynomial the corpus produces.

Source: `library/arxiv-0906.1500v4/0906.1500v4.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0906.1500v4/  ->  [dubois-yamaguchi2012]
  Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dubois-yamaguchi2012] as the citation key when you do it.
