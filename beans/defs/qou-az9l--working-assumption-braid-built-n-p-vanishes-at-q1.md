---
# qou-az9l
title: 'Working assumption: braid-built n-p vanishes at q=1 (isospin breaking is O(h)); prove and formalise in general'
status: in-progress
type: task
priority: normal
created_at: 2026-11-22T09:23:07Z
updated_at: 2026-11-22T09:23:50Z
---

Owner 2026-11-22 (thread, PR #8804): siblings work under this working assumption and track this bean for proving and formalising it.

STATEMENT. Every n - p term built from the braid algebra (words in sigma_i^{+-1}, the gamma-gamma vertex V = sigma_0 sigma_1^-1, hol = V^3, the jet derivative D = (hol-1)/q + (1-q^-1)T3, all powers, any number of strands) vanishes at q = 1. So m_p = m_n in the classical limit and the size of m_n - m_p comes from O(h) terms, h = q - q^-1.

SCOPE (read before using). Electromagnetic terms built with alpha_EM (alpha = q^-1/([9][10]), alpha*QPair*hol) are NOT braid-built and do NOT vanish at q = 1 (PR #8804 s40: exactly -m_e/720). The assumption covers the braid part only.

PROVED (sorry-free, lean-direct, standard axioms):
- QOU/MassTheory/FlipSymmetryAtOne.lean: mirror-block traces of (hol - 1)^k agree for hol any product of strand permutations, all n, k.
- QOU/MassTheory/FlipSymmetryAtOneBridge.lean: at q = 1, h = 0 the Hecke generator (both letters) is the strand swap and D = hol - 1; blockTr_jetD_pow_word_at_one for every braid word.
- Numerics: H3 jet tower k=0..8 (s37), H6 two nucleons (s38), operator charge Q = log V/2pi i (s38).

OPEN (what remains to prove/formalise):
1. Generator and inverse letter are inverse for general q (h = q - qinv, q*qinv = 1) in Lean; that gen matches the corpus Rc.
2. The statement for the K-weighted / Markov-trace (convention D) sector maps, not only plain block traces.
3. Statement for operator-valued charges (log V) - functional calculus of a flip-equivariant matrix stays flip-equivariant.
4. Caution: on the section-35 muon map (pole hbar_q^-2) O(h) terms become 1/h divergent; the assumption does not say those maps are finite.
5. p <-> n orientation is an underived label (X V X = P V^-1 P); the assumption is symmetric under it.

Refs: PR #8804 LITERATURE-COMPARISON.md s37-s41.


Prior art: QOU/MassTheory/QOneFlipSymmetry.lean (s34) proves the n = 3 weight-space version (flip_A_i_one, trace_word_flip) and the charge condition q_u^2 = q_d^2 (self/pair_charge_equal_iff). FlipSymmetryAtOne(Bridge) generalise it to all n on C2^n.
