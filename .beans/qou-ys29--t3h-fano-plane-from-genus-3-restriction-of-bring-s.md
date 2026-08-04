---
# qou-ys29
title: 'T3h: Fano plane from genus-3 restriction of Bring surface — derive octonions from geometry'
status: todo
type: task
priority: critical
created_at: 2026-08-04T10:18:37Z
updated_at: 2026-08-04T10:18:37Z
parent: qou-8lxd
---

CONJECTURED DERIVATION CHAIN (user insight, 2026-08-04):

SM fermions exhaust at genus 3 (unmapped-torus-knots.md: "Standard Model
fermions exhaust at genus 3"). The tau T(2,7) and charm are the genus-3
matter generators. The natural automorphism group of genus-3 curves is
PSL(2,7) = GL(3,F_2) = Aut(Fano plane) (168 elements; Klein quartic is
the Hurwitz surface at genus 3). The Fano plane encodes the octonion
multiplication table (7 imaginary units, 7 lines, each line = associative
triple). And Stab_{G_2}(e) = SU(3) is already proved (color-su3-from-g2).

So the chain is:
  Bring (genus 4, S_5) ⊃ genus-3 Seifert surfaces
  → PSL(2,7) = Aut(Klein quartic) = Aut(Fano)
  → Fano plane = octonion multiplication table
  → G_2 = Aut(O) ⊃ SU(3) = Stab(e)
  → color SU(3) DERIVED from Bring geometry

If this works, it replaces the current "import octonions ad hoc" with a
geometric derivation: the octonionic structure IS the genus-3 restriction
of the Bring surface's coordinate system.

SPECIFIC TESTS:
1. Does the genus-3 Seifert surface of T(2,7) embed in Bring's genus-4
   surface as a codimension-1 subsurface? (Topologically: genus 4 → genus 3
   by pinching one handle.)
2. Does the S_5 symmetry of Bring restrict on the genus-3 subsurface to a
   subgroup containing PSL(2,7)? Note: |PSL(2,7)| = 168, |S_5| = 120, so
   PSL(2,7) is NOT a subgroup of S_5. This is a potential obstruction.
   Alternative: the genus-3 surface may not inherit Bring's S_5 but carry
   its OWN PSL(2,7) symmetry.
3. Do the 7 genus-3 torus-knot generators (the 7 imaginary octonion units)
   map to the 7 points of the Fano plane under the Klein quartic's
   automorphisms?
4. Does the associator structure (the Fano lines = associative triples)
   reproduce the octonionic multiplication table?

ANTI-FITTING: The chain must be a DERIVATION, not a coincidence. The key
test: does the genus-3 restriction of Bring force PSL(2,7) structure, or
is PSL(2,7) merely compatible? If forced → derivation. If merely
compatible → numerology.

OBSTRUCTION NOTE: |PSL(2,7)| = 168 > |S_5| = 120, so PSL(2,7) cannot be
a subgroup of S_5. The genus-3 subsurface of Bring might carry LESS
symmetry than the Klein quartic. This must be checked before claiming
derivation. The connection may go through the McKay correspondence
(A_5 → E_8) at the lattice level, as already noted in
color-su3-from-g2.md line 49.

RELATED: T3d (octonion G_2 route), T3b (distinct-fibre groupoid),
fivefold-symmetry-table row 3 ("Borromean B_3 (color SU(3))").
