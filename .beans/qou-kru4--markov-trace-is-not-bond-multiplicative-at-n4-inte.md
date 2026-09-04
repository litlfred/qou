---
# qou-kru4
title: 'Markov trace is NOT bond-multiplicative at n=4: interleaved s0 s1 s0 s2 s1 carries the exact cross term z(z^2 - h z - 1)'
status: completed
type: task
priority: normal
created_at: 2026-09-03T15:06:58Z
updated_at: 2026-09-04T02:32:22Z
---

Branch claude/two-nucleon-sign-closure-correction-2026-09-03 (continuing the tranche; will land as its own PR). Answers the general-n question qou-ls86 left OPEN on 2026-08-18 (its probe names s0 s1 s0 s2 s1 verbatim as the untested n=4 case).

RESULT (two independent routes agree as rational functions):
  (1) Ocneanu axioms only (tr 1 = 1, Markov, cyclicity, Hecke g^2 = h g + 1, braid):
      tr(s0 s1 s0 s2 s1) = z(z^2 + h z + h^2 z^2);  tr(s0^2 s1^2 s2) = z(h z + 1)^2;
      difference = z(z^2 - h z - 1).
  (2) spin-1/2 V^{⊗4} rep (16-dim), μ-weighted qtr/[2]^4: identical closed form; the n=3 identity reproduces as exactly 0 in the same rep (control).
  At convention D: difference = -q^3(q^2-q+1)(q^2+q+1)/(q^2+1)^3 < 0 for q > 0.
  The factor z^2 - h z - 1 is the corpus's 'convention-D Markov defect' (qou-19jc), = -(q^4+q^2+1)/q^2 * y_(2,1) (qou-xzrj) — interleaving is priced by the (2,1) two-row block weight.
  Sign: interleaved trace SMALLER => extra log-suppression => EXTRA BINDING (the direction R > 0 on the well-bound regime needs). Magnitude at the proton pin: ratio 0.4085, 0.895 nats per interleaving.

SO: the Markov trace is NOT bond-multiplicative at n=4. The multi-bond source qou-ls86 closed at n=3 (as the one place both the many-body collective term and a quadratic Coulomb term could live) is OPEN at n=4 for interleaved word classes, with an EXACT nonzero cross term.

SCOPE (a), positive existence, deliberately narrow: production atom_braid_word_3A is sequential (single inter-nucleon letter, no generator recurs after its neighbour), so the production bare-product trace is EXACT for the production word class and NO existing number moves. This is a candidate SOURCE, not a correction. Which word class (if any) a nucleus is = the carrier blocker (qou-5vhf). Not wired, not fitted.

Artifacts: computations/probes/markov_trace_n4_interleaved_cross_term_probe.py (exact sympy + mp@50dps, 10/10 + anchor), QOU/MathlibExt/MarkovTraceInterleavedCrossTerm.lean (abstract over the MarkovTrace structure + conv-D closed form + sign), audit doc pending.


## 2026-09-04 — CLOSED: the converse is proved (branch claude/monotone-word-trace-factorizes-2026-09-04)

`QOU/MathlibExt/MonotoneWordTraceFactorizes.lean` (sorry-free, lean-direct exit 0, axiom-clean on 8 decls): a MONOTONE word (ascending, letters s m ∈ H(m+1) stabilising H m) has tr = ∏ tr(letter) (`tr_stabWord_eq_prod_tr`); the production superposition letters a•1 + b•g stabilise with a + b z (`tr_affineWord`) and close under product at one level (`affine_mul_affine`), so a RUN of them is one affine letter; runs g^e stabilise with the Chebyshev-type `runCoeff` (1, z, hz+1, ...). `content_reorder_defect`: the interleaved word = (∏ over its own content) + z(z²−hz−1) — same letters, non-ascending order, cross term.

SO: the production trace's per-bond product is exact BECAUSE atom_braid_word_3A is monotone (chain-walk, one run per generator; ²H = 5 affine letters at g0..g4). Bond-additivity is a theorem about ORDERING, not a Markov-trace property. Same hypothesis gives Vol = 0 for every production closure (2026-08-25 audit). Hence: a derived hyperbolic carrier (qou-5vhf) and a derived collective cross term (this bean) need the SAME thing — a non-monotone word — and neither can come from atom_braid_word_3A as written. Audit: docs/audits/2026-09-04-monotone-word-trace-factorizes-derived-link-map.md. Nothing wired, nothing fitted.
