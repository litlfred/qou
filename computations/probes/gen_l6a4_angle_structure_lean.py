#!/usr/bin/env python3
"""Emit QOU/Knot/L6a4AngleStructure.lean from the VERIFIED SnapPy data.

Generated rather than hand-typed so the 24-variable constraint system and the
orbit chains cannot drift from what the probe measured.
"""
import sys, snappy
from collections import deque
# Repo-root-relative (bean qou-c7g8). This line hardcoded
# "/home/user/qou/..." -- an absolute path into a DIFFERENT machine's
# checkout. It resolves to nothing in this repo (or any clone not at
# that exact path), so the insert silently did nothing and the import
# below survived only because `_path_bridge` happened to cover it.
from pathlib import Path as _P
_HERE = _P(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
from borromean_angle_structure_lp_probe import gluing, ga_equalities

M, N, r, edge_rows, _ = gluing(snappy, "L6a4")
A, b = ga_equalities(N, edge_rows)
n = 3 * N

GENS = [
 (1,0,2,5,4,3,11,10,9,8,7,6,14,13,12,19,18,20,16,15,17,22,21,23),
 (3,5,4,0,2,1,15,17,16,18,20,19,21,23,22,6,8,7,9,11,10,12,14,13),
 (6,8,7,15,17,16,14,13,12,0,2,1,11,10,9,22,21,23,3,5,4,19,18,20),
]
OA = [0,1,3,5,6,8,9,11,12,14,15,16,18,19,21,22]
OB = [2,4,7,10,13,17,20,23]

def bfs(root):
    """For each index in root's orbit, a chain of (gen, from) steps reaching it."""
    prev = {root: None}
    q = deque([root])
    while q:
        u = q.popleft()
        for gi, g in enumerate(GENS):
            # fixedness gives x (g i) = x i, so from u we reach g[u]
            v = g[u]
            if v not in prev:
                prev[v] = (gi, u)
                q.append(v)
    return prev

pa, pb = bfs(0), bfs(2)
assert set(pa) == set(OA) and set(pb) == set(OB), "orbit mismatch vs measurement"

def lean_perm(g):
    return "![" + ", ".join(str(x) for x in g) + "]"

def eqn(row, rhs):
    terms = []
    for j, c in enumerate(row):
        if c == 0: continue
        terms.append(f"x {j}" if c == 1 else f"{c} * x {j}")
    return " + ".join(terms) + f" = {rhs}"

L = []
w = L.append
w('''/-
  L6a4 (Borromean rings) angle structure: the symmetric point is UNIQUE, and it
  is the regular ideal octahedron.  Bean `qou-krvm`, the L6a4 half.

  COMPANION TO `M004AngleStructure` — AND ITS OPPOSITE.  Bean qou-krvm's
  hypothesis (ii) ("the symmetric point is UNIQUE") is FALSE for m004, whose
  fixed locus is a line.  For L6a4 it is TRUE, and this file proves it.  So the
  two anchors of PR #4513 are explained differently:

    m004  (muon)   |Sym| = 4    fixed locus a LINE   -> symmetry does NOT pin it;
                                the Casson-Rivin objective finishes the job
    L6a4 (proton)  |Sym| = 16   fixed locus a POINT  -> symmetry ALONE pins it,
                                so `SymmetricOptimum.symmetric_point_optimal`
                                applies directly and the measured vanishing
                                offset at the proton anchor is forced

  WHAT IS PROVED HERE (sorry-free)

  * `GA.gen0/1/2` — the three generators of the order-16 coordinate symmetry
    preserve the generalised-angle system.  (The full group is order 16; three
    generators suffice, verified minimal by exhaustive search.)
  * `fixed_orbitA` / `fixed_orbitB` — a fixed point is CONSTANT on each of the
    two orbits (sizes 16 and 8), by explicit chains of generator steps.
  * `unique_symmetric_point` — a fixed feasible point is exactly the regular
    ideal octahedron point: `1/4` on the size-16 orbit, `1/2` on the size-8
    orbit.  This is bean qou-krvm's hypothesis (ii), TRUE for this anchor.

  THE SYSTEM IS OVERDETERMINED AND CONSISTENT, which is what makes uniqueness
  immediate.  On an orbit-constant point the 16 constraints collapse to just
  three distinct equations:

      tet   (x8):  2a + b = 1
      edge  (x4):  8a     = 2      ->  a = 1/4
      edge  (x4):      4b = 2      ->  b = 1/2

  The two edge families pin `a` and `b` OUTRIGHT, and `2a + b = 1` is then a
  compatibility check that happens to hold (2/4 + 1/2 = 1).  Every tetrahedron
  carries exactly one size-8 coordinate and two size-16 coordinates — the
  (pi/4, pi/4, pi/2) shape of the regular ideal octahedron.

  PROVENANCE.  The 24-variable system, the generators and the orbits are NOT
  hand-typed: this file is GENERATED from SnapPy via the corpus's own
  `gluing` / `ga_equalities` helpers (`borromean_angle_structure_lp_probe`),
  the same system the LP was solved against.  The symmetry group was found by
  label-preserving graph automorphism with every candidate verified
  algebraically (rref of the augmented system), and recorded in
  `computations/probes/qbeta-krvm-ga-symmetry-fixed-locus.witness.json`.

  HONESTY BOUNDARY.  As in the m004 file: this is the SYMMETRY half.  Bean
  qou-krvm's hypothesis (iv) — that the hyperbolic volume functional is concave
  and invariant (Rivin) — is untouched; Mathlib has no ideal-tetrahedron volume
  theory.  Nothing here says the LP optimum is unique, only that the SYMMETRIC
  point is.

  Archimedean (R): ordering and division over R (§7c).

  -- Ref: [manuscript] computations/probes/qbeta_krvm_ga_symmetry_fixed_locus_probe.py
  -- Ref: [garoufalidis2012] arXiv:1208.1663 §2.2-2.3 (generalised angle structures)
-/

import Mathlib.Tactic

namespace QOU.Knot.L6a4AngleStructure

/-- The 24 tetrahedron angles of the L6a4 (Borromean rings) triangulation,
in pi-units: 8 ideal tetrahedra, 3 angles each.  Indexed by `Nat` rather than
`Fin 24` so the permutation generators reduce definitionally at literal indices;
coordinates past 23 are simply unconstrained and never referenced. -/
abbrev Pt := Nat -> Real
''')

# --- GA definition -----------------------------------------------------------
w("/-- **The L6a4 generalised angle structure.**  SnapPy's 8 per-tetrahedron")
w("sums and 8 edge equations, in pi-units. Generated from the measured system. -/")
w("structure GA (x : Pt) : Prop where")
for i, (row, rhs) in enumerate(zip(A, b)):
    nm = f"tet{i}" if i < N else f"edge{i - N}"
    w(f"  {nm} : {eqn(row, rhs)}")
w("")

# --- generators --------------------------------------------------------------
for gi, g in enumerate(GENS):
    w(f"/-- Symmetry generator {gi} of the order-16 coordinate group. -/")
    w(f"def sigma{gi} : Nat -> Nat")
    for src_i, dst in enumerate(g):
        w(f"  | {src_i} => {dst}")
    w("  | n => n")
    w("")

w("/-- A point is **fixed** when all three generators leave it unchanged. -/")
w("def Fixed (x : Pt) : Prop :=")
w("  (forall i, x (sigma0 i) = x i) @A@ (forall i, x (sigma1 i) = x i) @A@")
w("  (forall i, x (sigma2 i) = x i)")
w("")

# --- generator preserves GA --------------------------------------------------
for gi, g in enumerate(GENS):
    w(f"/-- **Generator {gi} preserves the angle structure.**  It permutes the")
    w("constraint rows among themselves; the proof is the resulting linear identity. -/")
    w(f"theorem GA.gen{gi} " + "{x : Pt} (h : GA x) : GA (fun i => x (sigma" + str(gi) + " i)) := by")
    w("  obtain ⟨" + ", ".join([f"t{i}" for i in range(N)] + [f"e{i}" for i in range(len(A) - N)]) + "⟩ := h")
    w("  constructor <;> simp only [sigma%d] <;> linarith" % gi)
    w("")

# --- orbit chains ------------------------------------------------------------
def chain_block(name, prev, root, orbit, val):
    w(f"/-- A fixed point is **constant on the size-{len(orbit)} orbit**"
      f" (representative `{root}`). -/")
    w(f"theorem fixed_{name} " + "{x : Pt} (hf : Fixed x) :")
    w("    " + " @A@ ".join(f"x {i} = x {root}" for i in orbit if i != root) + " := by")
    w("  obtain ⟨f0, f1, f2⟩ := hf")
    order = [i for i in orbit if i != root]
    order.sort(key=lambda i: len(_path(prev, i)))
    for i in order:
        gi, u = prev[i]
        w(f"  have h{i} : x {i} = x {u} := by")
        w(f"    have := f{gi} {u}; simpa [sigma{gi}] using this")
    w("  exact ⟨" + ", ".join("by linarith" for _ in order) + "⟩")
    w("")

def _path(prev, i):
    p = []
    while prev[i] is not None:
        gi, u = prev[i]; p.append(i); i = u
    return p

def _expand(prev, i, root):
    p = _path(prev, i)
    if len(p) == 1: return f"h{i}"
    return "by rw [" + ", ".join(f"h{k}" for k in p) + "]"

chain_block("orbitA", pa, 0, OA, "1/4")
chain_block("orbitB", pb, 2, OB, "1/2")

# --- uniqueness --------------------------------------------------------------
w('''/-- **The unique symmetric point (bean qou-krvm hypothesis (ii), TRUE here).**
A feasible point fixed by the symmetry group is exactly the regular ideal
octahedron: `1/4` on the size-16 orbit, `1/2` on the size-8 orbit.

Contrast `M004AngleStructure.fixed_iff_line`, where the same hypothesis is
FALSE and the fixed locus is one-dimensional. -/
theorem unique_symmetric_point {x : Pt} (h : GA x) (hf : Fixed x) :
    x 0 = 1/4 @A@ x 2 = 1/2 := by
  obtain ⟨t0, t1, t2, t3, t4, t5, t6, t7, e0, e1, e2, e3, e4, e5, e6, e7⟩ := h
  obtain ⟨''' + ", ".join(f"a{i}" for i in OA if i != 0) + '''⟩ := fixed_orbitA hf
  obtain ⟨''' + ", ".join(f"b{i}" for i in OB if i != 2) + '''⟩ := fixed_orbitB hf
  constructor <;> linarith

/-! ## Non-vacuity: the point exists

`unique_symmetric_point` says AT MOST one symmetric feasible point. On its own
that would also hold if there were NONE — the theorem would be vacuously true.
These two witnesses close that hole by exhibiting the point. -/

/-- The regular ideal octahedron point: `1/2` on the size-8 orbit, `1/4`
elsewhere. -/
noncomputable def regularOctahedron : Pt := fun n =>
  if n = 2 @O@ n = 4 @O@ n = 7 @O@ n = 10 @O@ n = 13 @O@ n = 17 @O@ n = 20 @O@ n = 23
  then 1/2 else 1/4

/-- It is feasible. -/
theorem GA_regularOctahedron : GA regularOctahedron := by
  constructor <;> norm_num [regularOctahedron]

/-- It is fixed by the whole symmetry group. -/
theorem Fixed_regularOctahedron : Fixed regularOctahedron := by
  refine ⟨?_, ?_, ?_⟩ <;> intro i <;>
    (rcases i with _|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|n <;>
      simp [sigma0, sigma1, sigma2, regularOctahedron])

/-- **The symmetric point exists and is unique.**  Combining the two: L6a4's
fixed locus is exactly one point, the regular ideal octahedron — bean
`qou-krvm` hypothesis (ii), TRUE for this anchor and FALSE for m004. -/
theorem symmetric_point_exists_unique :
    GA regularOctahedron ∧ Fixed regularOctahedron ∧
      ∀ x : Pt, GA x → Fixed x → x 0 = 1/4 ∧ x 2 = 1/2 :=
  ⟨GA_regularOctahedron, Fixed_regularOctahedron,
   fun _ h hf => unique_symmetric_point h hf⟩

end QOU.Knot.L6a4AngleStructure''')

src = "\n".join(L)
# Lean uses ∧ / ∀ / ∈ ; emit them after assembling to keep the generator ASCII.
src = (src.replace("@A@", "∧").replace("@O@", "∨").replace("forall ", "∀ ")
          .replace(" in (", " ∈ (").replace("Real", "ℝ"))
# Repo-root-relative (bean qou-c7g8): this was an absolute path into a
# DIFFERENT machine's checkout, so the generator wrote nowhere reachable
# here and died with FileNotFoundError before emitting the Lean file.
out = str(_HERE.parents[1] / "content" / "quantum-observable-universe"
          / "lean" / "QOU" / "Knot" / "L6a4AngleStructure.lean")
open(out, "w").write(src + "\n")
print("wrote", out, "-", len(src.splitlines()), "lines")
