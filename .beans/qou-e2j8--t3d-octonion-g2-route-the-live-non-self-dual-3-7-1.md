---
# qou-e2j8
title: 'T3d: octonion G2 route -- the live non-self-dual 3 (7 = 1+3+3bar)'
status: completed
type: task
priority: critical
created_at: 2026-08-04T00:07:00Z
updated_at: 2026-08-29T10:11:14Z
parent: qou-8lxd
---

SUPERSEDES the 'no such object' claim. docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md Investigation 2: colour SU(3) subset G2 = Aut(O), Gunaydin-Gursey 7 = 1 + 3 + 3bar. The 3/3bar ARE complex conjugates => non-self-dual => PASSES the Sym^2 gate. Discrete skeleton machine-checked (det3_cyclic_invariant, PSL(2,7) = GL(3,F_2) Fano symmetry). Missing: continuous G2 completion, coset S^6 = G2/SU(3) -- a MATHLIB GAP (no Octonion, no G2 Lie group), not a structural obstruction. Caveats: it is COLOUR not flavour SU(3) (but that is the sm-open-problems item anyway); PSL(2,7) is genus 3 Klein quartic vs QOU genus 4 Bring/S5.


---

## Parenthetical tightened 2026-08-29

This bean reads "it is COLOUR not flavour SU(3) (but that is the sm-open-problems
item anyway)", which is too casual and I inherited the misreading from it.

eightfold-open-problems item 4 makes flavour-versus-colour its OWN open item, and
the separation is PROVED unreachable by the two tools the corpus has:
gate_does_not_separate_two_triples (Sym^2) and
identification_invisible_to_selection_rule (Z/3). The 2026-08-26 discriminator
search then generalised that to a class: no_object_gate_separates.

So closing the Mathlib G_2 gap would NOT deliver the flavour N=3 the ledger row
asks for. There are two blockers, not one:

  1. Mathlib gap        no Octonion type, no G_2 Lie group   INFRASTRUCTURE
  2. flavour vs colour  item 4, open, gate provably blind    RESEARCH

The parenthetical elides 2.
