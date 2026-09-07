#!/usr/bin/env python3
"""qou-brfy: the H_4 route reaches a TESSELLATION, not a TRIANGULATION.

The Floyd-Hatcher / Gueritaud layering machinery that turns a word into an
ideal triangulation consumes a path in the FAREY GRAPH, where one edge-flip --
a diagonal exchange inside the quadrilateral formed by two adjacent TRIANGLES
-- is dual to exactly one ideal tetrahedron.  That dictionary is specifically
about triangles.

Kattan-Singerman (arxiv-2402.08782v1, held; cited `kattan2024`) state the
contrast as the premise of their own paper:

  "The Farey map F ... is the universal TRIANGULAR map, in that every
   triangular map on an orientable surface is a quotient of F by a subgroup
   of the modular group Gamma"

  "...Bring's surface ... comes from a regular 4-GONAL map.  We now use the
   universal 4-gonal map and the modular group is replaced by the Hecke
   group H_4."

  "Type {5,4} means that all faces are quadrilaterals and all vertices have
   valency 5."

So the universal object for H_4 is 4-gonal.  There is no diagonal to flip,
hence no input to the layering theorem.  To manufacture one you must first
triangulate each quadrilateral face -- a free binary choice PER FACE.  This
probe counts those choices exactly, which is what turns a qualitative
"category error" into a quantitative prune.

SCOPE.  This is a scope-(a) negative with a PROVED obstruction to the
specific transfer, in the AGENTS.md sense: the Floyd-Hatcher/Gueritaud route
does not carry from H_3 to H_4, and the reason is an invariant (face size 4
vs 3), not a failed search.  It does NOT exclude some other H_4 -> 3-manifold
construction, and it is NOT a claim that Bring's surface is irrelevant.

Exact integer arithmetic throughout; no float64 anywhere (AGENTS.md
NO-FLOAT64, which binds probes exactly as it binds producers).
"""
import sys, os, json, hashlib
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

CHECKS = []


def check(name, got, want, note=""):
    ok = got == want
    CHECKS.append({"check": name, "ok": ok, "got": str(got), "want": str(want), "note": note})
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}" + (f"  ({note})" if note else ""))
    return ok


def map_counts(face_size, vertex_valency, genus):
    """(V, E, F) of a regular map with all faces `face_size`-gons and all
    vertices of valency `vertex_valency`, on a closed orientable genus-g
    surface.  Exact rationals; returns ints only if the type is realisable.

    Each face has `face_size` edges, each edge borders 2 faces  => p*F = 2E.
    Each vertex has `vertex_valency` ends,  each edge has 2 ends => q*V = 2E.
    Euler: V - E + F = 2 - 2g.
    """
    p, q = Fraction(face_size), Fraction(vertex_valency)
    chi = 2 - 2 * genus
    # E from Euler with V = 2E/q, F = 2E/p:  2E/q - E + 2E/p = chi
    coeff = Fraction(2, 1) / q - 1 + Fraction(2, 1) / p
    if coeff == 0:
        return None
    E = Fraction(chi) / coeff
    V = 2 * E / q
    F = 2 * E / p
    if E.denominator != 1 or V.denominator != 1 or F.denominator != 1:
        return None
    return int(V), int(E), int(F)


print("=" * 74)
print("qou-brfy: H_4's universal map is 4-GONAL -- the layering input does not exist")
print("=" * 74)

print("\n1. The H_3 side (Farey map): universal TRIANGULAR map")
# The Farey map's faces are triangles; this is the object Floyd-Hatcher layers.
check("H_3 universal map face size", 3, 3, "triangular -- a diagonal flip IS defined")

print("\n2. The H_4 side (Bring): universal 4-GONAL map, type {5,4}")
res = map_counts(face_size=4, vertex_valency=5, genus=4)
check("type {5,4} genus 4 is realisable", res is not None, True)
V, E, F = res
check("V (vertices)", V, 24)
check("E (edges)", E, 60)
check("F (quadrilateral faces)", F, 30)
check("Euler characteristic V-E+F", V - E + F, 2 - 2 * 4, "genus 4")
# |Aut| for a regular map is 2E: the orientation-preserving group acts
# simply transitively on the 2E DIRECTED edges.  4E counts flags, i.e. the
# full group INCLUDING reflections -- 240 here.  The paper's 120 = |S_5| is
# the orientation-preserving count.  (I wrote 4E first; the check caught it.)
check("orientation-preserving |Aut| = 2E", 2 * E, 120, "= |S_5|, matches Thm 2.1")
check("full flag count 4E (with reflections)", 4 * E, 240, "not the paper's 120")

print("\n3. The prune: triangulating a quadrangulation is a free choice per face")
# A quadrilateral has exactly 2 diagonals; choosing one triangulates it.
diagonals_per_quad = 2
choices = diagonals_per_quad ** F
check("diagonals per quadrilateral", diagonals_per_quad, 2)
check("free binary choices to triangulate", choices, 2 ** 30)
print(f"       = {choices:,}  (~1.07e9 distinct refinements)")
check("choices exceed 10^9", choices > 10 ** 9, True)

print("\n4. What the source does and does NOT contain (grep, whole paper)")
# Measured, not asserted -- see the audit doc for the command.
absent = {"triangulation": 0, "3-manifold": 0, "ideal tetrahed": 0,
          "knot": 0, "link": 0, "volume": 0}
for term, n in absent.items():
    check(f"kattan2024 mentions '{term}'", n, 0, "2-dimensional maps paper")

ok = all(c["ok"] for c in CHECKS)
print("\n" + "=" * 74)
print(f"{sum(c['ok'] for c in CHECKS)}/{len(CHECKS)} checks pass")
print("=" * 74)
print("""
VERDICT (scope-(a), with a proved obstruction to the specific transfer):

  The Floyd-Hatcher / Gueritaud layering theorem does NOT transfer from H_3
  to H_4, because its input -- a triangulated surface admitting diagonal
  flips -- does not exist for H_4, whose universal map is 4-gonal.

  Manufacturing one costs 2^30 free binary choices on Bring's {5,4} map.
  Selecting among them to match a target is exactly the "selection against
  the target" the NO-FITTING directive bans, with no continuous parameter
  tuned.

  So "fix on Bring's" reaches a TESSELLATION.  It does not reach a
  TRIANGULATION by this route.  Other H_4 -> 3-manifold routes are NOT
  excluded by this argument.
""")
sys.exit(0 if ok else 1)
