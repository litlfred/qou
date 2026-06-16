#!/usr/bin/env python3
"""The canonical spin->colour coupling map and its Reeb-intertwining obstruction
(conj:s5-so3-fiber-action, dynamical part).

The static coupling is Schur-forced; the open question is the DYNAMICAL
intertwining of the spin Hopf Reeb (S^3 subset C^2_spin) with the colour
Sasakian Reeb (S^5 subset C^3_colour), A_5-equivariantly.

CLAIM tested here: the canonical A_5-equivariant coupling is the Hopf MOMENT MAP
    mu : C^2_spin -> R^3 subset C^3_colour,   mu(z) = ( z* sigma_x z, z* sigma_y z, z* sigma_z z ),
i.e. the Ad: SU(2) ->> SO(3) map at the vector level (also the Hopf fibration
S^3 -> S^2).  We verify:
  (1) mu is real-valued and QUADRATIC -> mu(-z)=mu(z): the central -1 of 2I acts
      TRIVIALLY on the image -> resolves the spin-parity obstruction (odd spinor
      -> even colour) that blocked a linear C^2 -> C^3 coupling.
  (2) mu is invariant under the spin PHASE z -> e^{i theta} z: so the spin Hopf
      Reeb is exactly the mu-fibre direction -> intertwined (vertical) on the
      spin side.
  (3) mu is 2I-equivariant: mu(g z) = Ad(g) mu(z) for g in SU(2), Ad(g) in SO(3).
  (4) OBSTRUCTION: the colour Sasakian Reeb (overall U(1) phase on C^3) does NOT
      preserve mu's image R^3: e^{i phi} * (real vector) leaves R^3 for generic
      phi.  So mu intertwines the SPIN Reeb but NOT the round-S^5 COLOUR Reeb;
      the two flows are transverse at the coupling locus.

Conclusion: the canonical coupling exists and resolves parity + the spin Reeb,
but the round colour Reeb is transverse to it.  A colour contact structure whose
Reeb is intertwinable must have its Reeb in the SPATIAL SO(3)_colour subset SU(3)
(where A_5 lives), i.e. an SU(3)/SO(3)-homogeneous Sasakian, NOT the round S^5.

deps: numpy.
"""
import sys
import numpy as np

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMA = [sx, sy, sz]
TOL = 1e-12


def mu(z):
    """Hopf moment map C^2 -> R^3 (returns a real 3-vector)."""
    return np.array([np.vdot(z, s @ z) for s in SIGMA])  # z* s z, real for Hermitian s


def Ad(g):
    """SO(3) image of g in SU(2): Ad(g)_jk = (1/2) tr(sigma_j g sigma_k g^dag)."""
    R = np.zeros((3, 3))
    for j in range(3):
        for k in range(3):
            R[j, k] = 0.5 * np.real(np.trace(SIGMA[j] @ g @ SIGMA[k] @ g.conj().T))
    return R


def su2_axis_angle(axis, angle):
    n = np.array(axis, dtype=float)
    n = n / np.linalg.norm(n)
    return (np.cos(angle / 2) * np.eye(2)
            - 1j * np.sin(angle / 2) * (n[0] * sx + n[1] * sy + n[2] * sz))


rng = np.random.default_rng(0)
z = rng.standard_normal(2) + 1j * rng.standard_normal(2)

print("=" * 70)
print("Canonical coupling mu(z) = z* sigma z  (Hopf moment map C^2 -> R^3)")
print("=" * 70)
m = mu(z)
real_ok = np.allclose(m.imag, 0, atol=TOL)
print(f"  mu(z) = {np.round(m.real, 6)}   (purely real: {real_ok})")

# (1) even -> central -1 of 2I trivial on image (parity resolved)
even_ok = np.allclose(mu(-z), mu(z), atol=TOL)
print(f"  (1) mu(-z) == mu(z): {even_ok}  -> 2I central -1 acts TRIVIALLY on image")
print(f"      => quadratic mu bridges odd spinor (central -1) to even colour (+1):")
print(f"         resolves the spin-parity obstruction to a C^2->C^3 coupling.")

# (2) spin phase invariance -> spin Reeb is the mu-fibre
theta = 0.7
phase_ok = np.allclose(mu(np.exp(1j * theta) * z), mu(z), atol=TOL)
print(f"  (2) mu(e^(i theta) z) == mu(z): {phase_ok}  -> spin Hopf Reeb = mu-fibre")
print(f"      (mu IS the Hopf fibration S^3->S^2; spin Reeb intertwined/vertical)")

# (3) 2I-equivariance: mu(g z) = Ad(g) mu(z), incl. an order-5 (icosahedral) g
g_rand = su2_axis_angle(rng.standard_normal(3), 1.3)
equiv_rand = np.allclose(mu(g_rand @ z), Ad(g_rand) @ mu(z), atol=1e-10)
g5 = su2_axis_angle([0, 0, 1], 2 * np.pi / 5)          # order-5 (binary: order 10)
equiv5 = np.allclose(mu(g5 @ z), Ad(g5) @ mu(z), atol=1e-10)
order5 = np.allclose((g5 @ g5 @ g5 @ g5 @ g5), -np.eye(2), atol=1e-10)  # g5^5 = -I in SU(2)
print(f"  (3) mu(g z) == Ad(g) mu(z): random g {equiv_rand}; order-5 g {equiv5}")
print(f"      (order-5 binary element: g5^5 = -I in SU(2): {order5}) -> A_5-equivariant")

# (4) OBSTRUCTION: colour phase does NOT preserve R^3
phi = 0.9
colour_phase_img = np.exp(1j * phi) * m.real            # colour Reeb acts by overall phase
leaves_R3 = not np.allclose(colour_phase_img.imag, 0, atol=TOL)
print(f"  (4) colour Reeb (phase e^(i phi)) on mu(z): leaves R^3 (nonzero imag): {leaves_R3}")
print(f"      => the round-S^5 colour Reeb is TRANSVERSE to mu's image R^3:")
print(f"         mu does NOT intertwine the colour Reeb (only the spin Reeb).")

print()
print("=" * 70)
print("VERDICT")
print("=" * 70)
print("  CONSTRUCTED: the canonical A_5-equivariant coupling mu = Hopf moment map.")
print("    - resolves the spin-parity obstruction (quadratic/even);")
print("    - realizes the static Schur-forced coupling geometrically;")
print("    - intertwines the SPIN Hopf Reeb (it IS the Hopf fibration).")
print("  OBSTRUCTION (verified): the round-S^5 COLOUR Reeb (U(1) phase) is")
print("    transverse to mu's image R^3, so it is NOT intertwined by mu.")
print("  RESOLUTION DIRECTION: the intertwinable colour contact structure must")
print("    carry its Reeb in the SPATIAL SO(3)_colour subset SU(3) (where the")
print("    icosahedral A_5 acts), i.e. an SU(3)/SO(3)-homogeneous Sasakian, NOT")
print("    the round S^5.  That is the next construction target (open).")

assert real_ok and even_ok and phase_ok and equiv_rand and equiv5 and order5
assert leaves_R3
print("\nCOUPLING-CONSTRUCTION + OBSTRUCTION ASSERTIONS VERIFIED.")
sys.exit(0)
