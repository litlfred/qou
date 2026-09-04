---
# qou-sorn
title: 'Non-monotone word class: only the cyclic triple carries a cross term; measured on 2H-4He it is intensive-suppressed (<=1 MeV, shrinking with A) against a 7-27 MeV extensive residual'
status: completed
type: task
priority: normal
created_at: 2026-09-04T03:11:25Z
updated_at: 2026-09-04T10:28:53Z
---

Branch claude/monotone-word-trace-factorizes-2026-09-04 (PR #6561, stacked on the monotone-factorizes tranche). Owner picked the formalize-first non-monotone probe.

FORMALIZE-FIRST RESULT (QOU/MathlibExt/RevisitClassCrossTerm.lean, sorry-free, 8 decls axiom-clean): a bond re-crossing after its neighbour (x g_m g_{m+1} g_m), skipping it (x g_m g_{m+2} g_m), or climbing two and returning (x g_m g_{m+1} g_{m+2} g_m) carries NO cross term. The ONLY source is the cyclic square (g_m g_{m+1})^2 — three adjacent strands cyclically braided, closure T(3,2) — with cross term exactly (z^2 - h z - 1)·tr x vs the Hopf chain. So the structural argument the option asked for is false and the class collapsed to one shape with an exactly known value.

CORRECTION of my own kru4 claim: the smallest failing instance is n=3 content (2,2), not n=4; the n=4 word is the 3-strand cyclic square stabilised once (interleaved_eq_stab_cyclicSquare).

PROBE (computations/probes/cyclic_triple_bond_cross_term_probe.py, 32/32, 50 dps, general-word Rust kernel validated byte-for-byte vs tr_m_atom_zn on 2H/3H/3He/4He; the production transfer kernel REFUSES non-monotone words): make each bond a cyclic triple (bond doubled, alternating with nucleon k's last two intra crossings; no free count). Closed form b(L1L2L3)·(z²−hz−1)·tr(prefix)·Πsuffix confirmed by kernel at every bond of 2H/3H/3He. Under the production law B = Q_β·(tr_free − tr_atom):
  2H: ΣΔB = +0.78 MeV vs residual 1.79 (43 %); 3H: +0.71 vs 7.79 (9 %); 3He: +1.00 vs 7.02 (14 %); 4He: +0.68 vs 27.4 (2.5 %).
Right sign, wrong size, and WRONG DIRECTION IN A: the term is a product of sub-unit letter traces so it shrinks with A while the residual grows — the intensive/extensive gap of qou-brng, at the word level. Under a log law it would read 2–4 nats/bond only because the cyclic trace is driven near zero (fragility, not mechanism; qou-y0mc open).

VERDICT scope-(a) negative for the cyclic-triple class. Recommendation (judgement): the collective term is not a functional of the single atom word's Markov trace. Not probed: the A≥3 cyclic coordination graph (needs a band-generator over/under choice) and the intra-nucleon cyclic square (changes the nucleon, not the bond). Audit: docs/audits/2026-09-04-cyclic-triple-word-class-prune-and-probe.md. Nothing wired or fitted.


## 2026-09-04 later — MeV column superseded by #6611 (qou-rp9i). The linear law this bean's numbers use is refuted; under the surviving log law the class is EXTENSIVE (p–p 3.77 / p–n 5.65 / n–n 14.09 MeV per bond) and over-shoots 3–8× with the retracted asymmetry sign. Still scope-(a) negative; the Lean prune and kernel agreement stand. See docs/audits/2026-09-04-cyclic-triple-under-log-law.md.
