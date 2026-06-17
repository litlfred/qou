#!/usr/bin/env python3
"""Keystone Wu-manifold step: the proposed 'spatial-SO(3) Reeb on SU(3)/SO(3)' is
OBSTRUCTED — a derivation-attempt correction to the keystone scope doc.

Attempting to DERIVE the keystone's last open piece (does the SU(3)/SO(3) Wu-manifold
Sasakian's equivariant index reproduce the Ocneanu weights W_lambda?) surfaces a flaw
in the scope-doc's resolution direction
(`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`), which said the
colour Reeb should be "the spatial SO(3)_colour circle" on the SU(3)/SO(3) arena.

Rigorous obstruction (homogeneous-space structure, no compute needed):
  * SU(3)/SO(3) = G/H with G = SU(3) (acting by left translation), H = SO(3) the
    ISOTROPY (modded out).  dim = 8 - 3 = 5 (odd; Sasakian-dim-compatible).
  * A Reeb vector field is NOWHERE-ZERO.
  * The isotropy H = SO(3) FIXES the basepoint o = eH; any 1-parameter subgroup of H
    acts by left translation fixing o, so its Killing field VANISHES at o.
  * Hence an SO(2) subset SO(3)(=isotropy) Killing field is zero at o -> it CANNOT be
    a Reeb field.

=> The "spatial-SO(3)_colour Reeb on SU(3)/SO(3)" framing conflates the ISOTROPY
SO(3) (which is quotiented out and fixes the basepoint) with an ACTING symmetry.
The Reeb must be a U(1) subset SU(3) that is NOT in the isotropy SO(3).  The open
derivation must first re-derive WHICH U(1) subset SU(3) is the Reeb and how the
icosahedral A_5 subset SO(3) relates to it (regular vs irregular Sasakian), THEN
compute the equivariant index.  This is genuine differential geometry, multi-session.
"""
import sys

DIM_SU3, DIM_SO3 = 8, 3
dim_quot = DIM_SU3 - DIM_SO3

print("=" * 70)
print("Wu-manifold SU(3)/SO(3): can the colour Reeb be the spatial SO(3)?")
print("=" * 70)
print(f"  dim SU(3)/SO(3) = {DIM_SU3} - {DIM_SO3} = {dim_quot}  (odd: {dim_quot % 2 == 1})")
print("  G = SU(3) acts (left); H = SO(3) is the ISOTROPY (fixes basepoint o=eH).")
print("  Reeb is nowhere-zero; an isotropy-subgroup Killing field vanishes at o.")
print("  => SO(2) ⊂ SO(3)(isotropy) CANNOT be a Reeb on SU(3)/SO(3).")
print()
print("VERDICT: scope-doc 'spatial-SO(3) Reeb on SU(3)/SO(3)' is OBSTRUCTED")
print("(isotropy ≠ acting symmetry). Reeb must be a U(1) ⊂ SU(3) NOT in the")
print("isotropy SO(3); re-derive which U(1) + how A_5 ⊂ SO(3) relates, then the")
print("equivariant index. Multi-session differential geometry; NOT derivable here.")

# Structural assertions (homogeneous-space facts).
assert dim_quot == 5 and dim_quot % 2 == 1
# The obstruction is a theorem (isotropy fixes basepoint => its Killing fields
# vanish there); encoded as the logical premise the derivation must respect.
isotropy_reeb_impossible = True   # SO(2) ⊂ isotropy vanishes at o, Reeb is nowhere-zero
assert isotropy_reeb_impossible
print("\nWU-MANIFOLD REEB-OBSTRUCTION (scope-doc correction) RECORDED.")

# ============================================================================
# STRONGER obstruction (spacetime-fixed under the 123->345 S3->S5 embedding):
# the icosahedral SO(3) here is the SPACETIME rotation of the 3 colour sheets
# (spin-from-so3-fiber.md), embedded in colour SU(3) via the irreducible T1
# (vector) rep.  A Reeb that FIXES spacetime must COMMUTE with this SO(3).  But
# by Schur, the commutant of an irreducible rep is scalars -> the centralizer of
# SO(3)(T1) in SU(3) is FINITE (Z/3), so NO continuous U(1) ⊂ SU(3) commutes with
# the spacetime SO(3).  => a spacetime-fixing Reeb does NOT exist in SU(3) at all.
# ============================================================================
import numpy as np
import numpy.linalg as la

Lx = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]], float)
Ly = np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]], float)
Lz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]], float)
I3 = np.eye(3)


def comm_map(L):
    return np.kron(L.T, I3) - np.kron(I3, L)   # vec([M,L])


A = np.vstack([comm_map(Lx), comm_map(Ly), comm_map(Lz)])
null_dim = int(np.sum(la.svd(A, compute_uv=False) < 1e-9))
print()
print("=" * 70)
print("Spacetime-fixed constraint (123->345): is there a U(1)⊂SU(3) fixing SO(3)?")
print("=" * 70)
print(f"  dim commutant of so(3)-on-C^3 (T1, irreducible) in M(3,C) = {null_dim} (scalars)")
print("  => centralizer of spacetime SO(3) in SU(3) is FINITE (Z/3); NO continuous")
print("     U(1) commutes with it.  A spacetime-FIXING Reeb cannot live in SU(3).")
print("  => SU(3)/SO(3) is the WRONG arena once spacetime-fixed is imposed: the")
print("     spacetime SO(3) (irreducible in colour SU(3)) leaves no room for a")
print("     spacetime-fixing Reeb.  Spacetime (2I-spin divisor ℙ(C^2)) and colour")
print("     (SU(3) strands) must be INDEPENDENT factors, not a quotient -- the Reeb")
print("     is a colour U(1) acting TRIVIALLY on the spacetime C^2 (automatic when")
print("     they are separate). Reinforces the two-distinct-spaces theme (#2364/#2370).")

assert null_dim == 1, "commutant of irreducible SO(3) on C^3 must be scalars (Schur)"
print("\nSPACETIME-FIXED CENTRALIZER OBSTRUCTION VERIFIED (no U(1)⊂SU(3) fixes SO(3)).")
sys.exit(0)
