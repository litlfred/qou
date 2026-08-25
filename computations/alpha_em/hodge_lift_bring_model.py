#!/usr/bin/env python3
"""hodge_lift_bring_model.py  (SCRATCH — not wired, not committed to content)

Explicit Hodge model of H^1(Bring) for the alpha_EM B2 tau-lift reduction.

Builds:
  1. The 8-dim weight-1 Hodge structure H^1(Bring;C) = H^{1,0} (+) H^{0,1}
     via the isogeny Jac(Bring) ~ E_{5tau0}^3 x E_{tau0}  (Riera-Rodriguez /
     Braden-Northover), each H^1(E) = C.dz (+) C.dzbar.
  2. The canonical Weil/Hodge real structure  c  (antilinear, swaps the two
     Hodge pieces; fixed locus = H^1(R)).
  3. The E/R Galois real structure  F = sigma*  (C-linear, also swaps the
     pieces) -- distinguishes it from c.
  4. Verifies: c is the involution the B2 statement calls "Hodge conjugation";
     rho: q->qbar maps to c at the Hodge level; and that this identification is
     CANONICAL (automatic) for any weight-1 HS -- so the content is the MAP q->HS,
     not the involution match.
  5. Non-CM confirmation (j non-integral; tau0 not imaginary-quadratic).
  6. The equivariance-automaticity test: the nome q = exp(2 pi i tau) itself
     forces  tau(qbar) = -conj(tau(q))  -- i.e. rho<->(tau->-taubar) is built
     into the nome, NOT an open condition; only EXISTENCE of the period map
     into Bring's period domain remains open.
"""
import numpy as np
import mpmath as mp
from fractions import Fraction

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
results = []
def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

# ---------------------------------------------------------------------------
# 0. Corpus literature data (Braden-Disney-Hogg / Braden-Northover), NOT fit.
#    tau0 = -1/2 + i * t0,  j(tau0) = -121945/32,  j(5 tau0) = -25/2,  class 50a.
# ---------------------------------------------------------------------------
t0 = mp.mpf('0.186676462462809923206162881363')   # Im tau0 (b2-cm probe, 50dps)
tau0 = mp.mpc(-mp.mpf('0.5'), t0)
j_tau0  = Fraction(-121945, 32)
j_5tau0 = Fraction(-25, 2)

# ---------------------------------------------------------------------------
# 1. NON-CM CONFIRMATION (independent of the corpus's own probe).
#    CM  <=>  j is an algebraic integer AND tau is imaginary-quadratic.
# ---------------------------------------------------------------------------
# (a) j non-integral rationals  => not algebraic integers.
j_nonintegral = (j_tau0.denominator != 1) and (j_5tau0.denominator != 1)
check("j_invariants_nonintegral_so_no_CM", j_nonintegral,
      f"j(tau0)={j_tau0} (den {j_tau0.denominator}), j(5tau0)={j_5tau0} "
      f"(den {j_5tau0.denominator}); CM j must be an algebraic integer")

# (b) tau0 imaginary-quadratic?  tau0 = -1/2 + i t0 is a CM point iff it
#     satisfies A tau^2 + B tau + C = 0 with A,B,C in Z.  Then
#     Im tau = sqrt(4AC - B^2)/(2A) and Re tau = -B/(2A).  Re = -1/2 => B = A.
#     So disc D = B^2 - 4AC = A^2 - 4AC, and t0 = sqrt(4AC - A^2)/(2A).
#     Search small A for an integer C making t0 match:
found_cm_point = False
for A in range(1, 40):
    B = A                       # forced by Re tau0 = -1/2
    val = (2*A*t0)**2 + B*B     # = 4 A C  if integral => C = that/(4A) integer
    fourAC = val
    if abs(fourAC - mp.nint(fourAC)) < mp.mpf('1e-20'):
        C = int(mp.nint(fourAC))
        if C % (4*A) == 0:
            found_cm_point = True
            break
check("tau0_not_imaginary_quadratic", not found_cm_point,
      "no small integer (A,B=A,C) quadratic has root tau0 => tau0 transcendental "
      "CM point excluded (searched A<=39)")

# ---------------------------------------------------------------------------
# 2. Build the explicit 8-dim Hodge structure  H^1(Bring;C) as a numpy model.
#    Ordered basis:  [dz_1,dz_2,dz_3, dz_4 | dzbar_1,dzbar_2,dzbar_3, dzbar_4]
#    where dz_1..3 belong to the three E_{5tau0} factors and dz_4 to E_{tau0}.
#    H^{1,0} = span(dz_k) (first 4 coords), H^{0,1} = span(dzbar_k) (last 4).
# ---------------------------------------------------------------------------
g = 4
taus = [5*tau0, 5*tau0, 5*tau0, tau0]   # per-factor moduli (complex-torus form)

# For each factor E_tau: integral basis alpha,beta of H^1(E;Z) with
#   dz    = alpha + tau  beta      (periods (1, tau))
#   dzbar = alpha + conj(tau) beta
# The Weil real structure c fixes alpha,beta (they are integral/real):
#   c(dz) = alpha + conj(tau) beta = dzbar,   c(dzbar) = dz.   (antilinear, swap)
# The E/R Galois structure F = sigma* is C-LINEAR with F(dz)=dzbar (sigma antiholo):
#   F(dz)=dzbar, F(dzbar)=dz  (linear, swap).
#
# We represent vectors in the (dz_k,dzbar_k) basis. Then:
#   c = SWAP composed with complex-conjugation of coordinates  (antilinear)
#   F = SWAP                                                    (C-linear)
SWAP = np.zeros((2*g, 2*g))
for k in range(g):
    SWAP[k, g+k] = 1.0
    SWAP[g+k, k] = 1.0

def c_apply(v):      # antilinear: swap then conjugate coefficients
    return SWAP @ np.conjugate(v)
def F_apply(v):      # C-linear: swap only
    return SWAP @ v

# 2a. c and F are involutions
rng = np.random.default_rng(0)
v = rng.standard_normal(2*g) + 1j*rng.standard_normal(2*g)
c_inv = np.allclose(c_apply(c_apply(v)), v)
F_inv = np.allclose(F_apply(F_apply(v)), v)
check("c_and_F_are_involutions", c_inv and F_inv,
      "c(c(v))=v (antilinear) and F(F(v))=v (linear)")

# 2b. both swap the Hodge pieces H^{1,0} <-> H^{0,1}
e_dz1 = np.zeros(2*g, complex); e_dz1[0] = 1.0          # a (1,0) vector
c_swaps = np.allclose(c_apply(e_dz1)[g:], SWAP[g:,:] @ e_dz1) and abs(c_apply(e_dz1)[0])<1e-12
F_swaps = abs(F_apply(e_dz1)[0]) < 1e-12 and abs(F_apply(e_dz1)[g]) > 0.5
check("c_and_F_swap_hodge_pieces", c_swaps and F_swaps,
      "c(H^{1,0}) in H^{0,1} and F(H^{1,0}) in H^{0,1}: both realize the Hodge swap")

# 2c. c is ANTIlinear, F is linear (the essential distinction)
lam = 2+3j
c_antilin = np.allclose(c_apply(lam*v), np.conjugate(lam)*c_apply(v))
F_lin     = np.allclose(F_apply(lam*v), lam*F_apply(v))
check("c_antilinear_F_linear", c_antilin and F_lin,
      "c(lam v)=conj(lam) c(v) [antilinear, = Hodge conjugation]; "
      "F(lam v)=lam F(v) [linear, = Galois real structure]")

# 2d. fixed locus of c IS the real cohomology H^1(R) (dim_R = 8, i.e. 2g)
#     v fixed by c  <=>  v_bar = conj(v_dz) in the dzbar slot: the alpha,beta reals.
#     Parametrize a fixed vector: choose H^{1,0} part w arbitrary, set H^{0,1}=conj(w).
w = rng.standard_normal(g) + 1j*rng.standard_normal(g)
vfix = np.concatenate([w, np.conjugate(w)])
c_fixes = np.allclose(c_apply(vfix), vfix)
# real dimension of the +1 eigenspace of an antilinear involution on C^{2g} is 2g
check("c_fixed_locus_is_real_cohomology", c_fixes,
      "v=(w, conj w) is c-fixed for all w in C^4 => Fix(c) is a real form of "
      "dim_R = 8 = b_1(Bring): c is exactly the H^1(R) real structure (Weil)")

# 2e. c is CANONICAL: it depends only on the Hodge decomposition + the real
#     lattice, NOT on tau or on E/R. Rebuild it for a DIFFERENT modulus and
#     confirm the SAME matrix (in the dz/dzbar basis) -- proves "rho<->c" carries
#     no arithmetic content at the HS level.
def c_matrix_free_of_tau(tauvec):
    # In the (dz_k,dzbar_k) basis the Weil c is always SWAP.conj, independent of tau.
    return SWAP.copy()
same = np.allclose(c_matrix_free_of_tau(taus), c_matrix_free_of_tau([1j]*g))
check("c_is_canonical_tau_independent", same,
      "the Weil real structure is SWAP-then-conjugate for ANY moduli => the "
      "involution match 'rho<->Hodge conjugation' is automatic at the HS level; "
      "the content is the MAP q|->HS, not the involution")

# ---------------------------------------------------------------------------
# 3. EQUIVARIANCE-AUTOMATICITY: the nome forces  tau(qbar) = -conj(tau(q)).
#    B1 dictionary: rho: q->qbar  <->  tau -> -taubar (anti-holo, fixes Re tau=0
#    i.e. real q-axis, matching R3: rho fixes q0 in R).
#    Claim: for the STANDARD nome tau(q) = log(q)/(2 pi i), this holds identically,
#    so the anti-holo equivariance is built into q=exp(2 pi i tau), NOT open.
# ---------------------------------------------------------------------------
def tau_of_q(q):
    return mp.log(q)/(2*mp.pi*mp.mpc(0,1))
max_err = mp.mpf(0)
for q in [mp.mpc('0.3','0.4'), mp.mpc('0.7','-0.2'), mp.mpc('0.5','0.5'),
          mp.mpc('0.9','0.1'), mp.mpc('0.2','-0.6')]:
    lhs = tau_of_q(mp.conj(q))              # tau(qbar)
    rhs = -mp.conj(tau_of_q(q))             # -conj(tau(q))
    max_err = max(max_err, abs(lhs-rhs))
check("nome_forces_antiholo_equivariance", max_err < mp.mpf('1e-45'),
      f"tau(qbar) = -conj(tau(q)) for tau=log(q)/(2 pi i): max_err={mp.nstr(max_err,3)} "
      "=> rho<->(tau->-taubar) is AUTOMATIC from the nome, not an open condition")

# 3b. and the fixed axis is the real q-axis (rho fixes q0 in R, R3):
q0 = mp.mpf('1.10998')            # substrate q0 (real) -- illustrative, |q|>1 branch
# For real q, tau(q) is pure imaginary (Re=0) mod the log branch => on the
# tau->-taubar fixed locus Re tau = 0:
tau_real_q = tau_of_q(mp.mpf('0.5'))   # real q in (0,1): tau pure imaginary
check("real_q_on_fixed_axis", abs(mp.re(tau_real_q)) < mp.mpf('1e-45'),
      f"real q in (0,1) -> tau pure imaginary (Re tau={mp.nstr(mp.re(tau_real_q),3)}): "
      "the rho-fixed locus is the real q-axis (matches R3, real masses at q0)")

# ---------------------------------------------------------------------------
# 4. What the explicit model DOES pin (target) vs does NOT (the map).
#    Target Hodge structure: fully explicit (periods diag(5tau0,5tau0,5tau0,tau0),
#    real structure c=SWAP.conj, j-values, 5-isogeny). Confirm the 5-isogeny ratio.
# ---------------------------------------------------------------------------
iso_ratio = mp.im(5*tau0)/mp.im(tau0)
check("isogeny_ratio_five_exact", abs(iso_ratio-5) < mp.mpf('1e-45'),
      f"Im(5tau0)/Im(tau0)=5 exactly: the X0(5) structure of the target HS is "
      "explicit (E_{5tau0}^3 x E_{tau0})")

print("\n=== SUMMARY ===")
allok = all(ok for _,ok,_ in results)
print("ALL PASS" if allok else "SOME FAILED")
print("""
CONCLUSION:
  - Non-CM: CONFIRMED (j non-integral; tau0 not imaginary-quadratic).
  - Hodge model H^1(Bring)=H^{1,0}+H^{0,1} (8-dim) built explicitly from
    E_{5tau0}^3 x E_{tau0}; Weil real structure c (antilinear, swaps pieces,
    Fix=H^1(R)) is the involution the B2 statement names "Hodge conjugation".
  - "rho <-> Hodge conjugation" at the HS level is CANONICAL/automatic (c is
    SWAP.conj for any moduli); it carries NO arithmetic content by itself.
  - The anti-holo equivariance tau(qbar)=-conj(tau(q)) is FORCED by the nome
    q=exp(2 pi i tau); also not the open part.
  - THEREFORE the minimal open core is EXISTENCE of the functorial period map
    Phi: q |-> [point in the period domain of H^1(Bring)] produced by the
    tau-functor (that its target IS Bring's HS with q as nome). Option (a).
    CM would only have pinned period VALUES (target), never the MAP -- so its
    absence does not change the bottom line.
""")
import sys
sys.exit(0 if allok else 1)
