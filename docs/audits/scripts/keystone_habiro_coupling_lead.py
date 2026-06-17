#!/usr/bin/env python3
"""Habiro framing of the keystone coupling — a structural LEAD + exposition-easing,
NOT a derivation.  Verifies the arithmetic anchors only; flags the coupling as open.

After #2409 (the keystone full-Hecke trace is a Habiro-ring element at q0, three faces:
colour gl_∞ / Jones II_1, spacetime affine-E8/2I, arithmetic Habiro), the spacetime
Habiro element is canonically identified:

  spacetime Habiro element = WRT(S^3/2I) = WRT(Poincaré homology sphere)
                           = the Lawrence-Zagier quantum modular form (known).

So the keystone "coupling" is, in the Habiro ring, a relation between two NAMED elements:
  - WRT(S^3/2I)  [spacetime, Lawrence-Zagier, E8/2I McKay], and
  - the full-Hecke Markov trace at q0  [colour, principal specialization].

VERIFIED ANCHORS (arithmetic only):
  |2I| = 120;  h(E8) = h^vee(E8) = 30;  |2I| = 4*h(E8);  dim E8 = 248 = 8*31 = rank*(h+1);
  S^3/2I is the Poincaré homology sphere (|H_1|=1, pi_1 = 2I).

CRITICAL-DISTANCE FLAG: naming the two Habiro elements is an IDENTIFICATION, not a
derivation of the coupling or the masses.  Pushing to "the coupling IS [formula]"
without the physics would be an unfalsifiable correspondence-chain (2I→E8→Poincaré→
Lawrence-Zagier→Habiro→masses) — explicitly NOT done.  The coupling stays open.

WHAT IT *DOES* EASE (the honest payoff): the Q_β c_k ladder.  Near q=1 (the q0 regime)
a Habiro element has a canonical Ohtsuki (perturbative) expansion; its coefficients are
the Ohtsuki invariants.  The Q_β `c_k` ladder = m_e·Π(1+c_k u^k) is exactly such an
expansion (1ppq-qbeta.md already invokes Ohtsuki; CLAUDE.md names "the Q_β Habiro
element" as the permanent c_k fix).  Reframing c_k as Ohtsuki invariants of a Habiro
element dissolves the per-coefficient mystery + the 6-entry flip-flop framing: they are
not free near-matches to settle one-by-one, but the canonical Ohtsuki series of one
quantum invariant.  This is an EXPOSITION simplification, not a new physical claim.
"""
import sys

twoI_order = 120
E8_h = 30          # Coxeter number of E8
E8_dim, E8_rank = 248, 8

print("=" * 70)
print("Arithmetic anchors: 2I / E8 / Poincaré sphere (the spacetime Habiro element)")
print("=" * 70)
print(f"  |2I| = {twoI_order}; h(E8) = h^vee(E8) = {E8_h}; |2I|/h(E8) = {twoI_order // E8_h}")
print(f"  dim E8 = {E8_dim} = rank*(h+1) = {E8_rank*(E8_h+1)} : {E8_dim == E8_rank*(E8_h+1)}")
print("  S^3/2I = Poincaré homology sphere (|H_1|=1, pi_1=2I)")
print("  => spacetime Habiro element = WRT(S^3/2I) = Lawrence-Zagier quantum modular form")

print()
print("=" * 70)
print("The coupling = relation between TWO NAMED Habiro elements (IDENTIFICATION, open)")
print("=" * 70)
print("  spacetime: WRT(S^3/2I) = Lawrence-Zagier")
print("  colour   : full-Hecke Markov trace at q0 (principal specialization)")
print("  CRITICAL-DISTANCE: this NAMES the elements; it does NOT derive the coupling or")
print("  the masses.  No coupling formula is asserted (that would be unfalsifiable).")

print()
print("=" * 70)
print("WHAT IT EASES (honest payoff): the Q_β c_k ladder exposition")
print("=" * 70)
print("  Near q=1 (q0 regime) a Habiro element has a canonical OHTSUKI expansion; its")
print("  coefficients ARE the Ohtsuki invariants.  Q_β c_k = m_e·Π(1+c_k u^k) is such an")
print("  expansion (1ppq-qbeta.md invokes Ohtsuki; CLAUDE.md names the Q_β Habiro element")
print("  as the permanent c_k fix).  => c_k are Ohtsuki invariants of ONE Habiro element,")
print("  not free near-matches to settle one-by-one — dissolving the 6-entry flip-flop")
print("  framing.  EXPOSITION simplification, no new physical claim.")

assert twoI_order == 4 * E8_h and E8_dim == E8_rank * (E8_h + 1)
print("\nHABIRO-LEAD ARITHMETIC ANCHORS VERIFIED (identification + exposition payoff; coupling OPEN).")
sys.exit(0)
