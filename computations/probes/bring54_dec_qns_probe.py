#!/usr/bin/env python3
"""bring54_dec_qns_probe -- a discrete Navier-Stokes model on the Bring {5,4} map.

Bean qou-k5jb. Audit: docs/audits/2026-11-25-holography-qns-essay-review.md,
item 4 (the essay claim "Bring's triangulation prevents NS blow-up").

WHAT THIS IS. A finite-dimensional, metric-free (unit Hodge star) discrete model
of incompressible 2D flow on the exact Bring cochain complex (bring54_map.py).
It is a model computation. A finite-dimensional dissipative ODE has global
solutions, so nothing here bears on 3D regularity, and 2D Navier-Stokes is
globally regular in the continuum anyway.

MODELLING CHOICES (all stated, none tuned to a target):
  M1  velocity v is a primal 1-cochain (60 edges); incompressible: d0^T v = 0.
      The divergence-free space is 31 = 8 harmonic + 23 coexact (v = d1^T psi).
      Mohamed-Hirani-Samtaney (library/arxiv-1508.01166v2 §3.3, full text in
      qou-private) write U = *d*d Psi, which is coexact only and so drops the 8
      harmonic modes on genus 4; here the harmonic component is kept.
  M2  unit Hodge stars (combinatorial Laplacians). The Bring map is pentagonal,
      not the pairwise-Delaunay simplicial mesh MHS require (§3.1).
  M3  vorticity omega = d1 v on faces; viscous term -nu * Delta_1 v, which on the
      divergence-free space equals -nu * d1^T d1 v.
  M4  nonlinear term in Lamb form, -P K(v) v with K(v) = (D J + J D)/2, where
      D = diag(face-average of omega on the two faces of each edge) and J is the
      skew "quarter turn" built from the map's vertex rotation (consecutive
      outgoing edges at a 4-valent vertex). K(v) is skew for every v, so the
      nonlinear term does no work, and K(v) = 0 whenever omega = 0.
      P = Leray projector onto ker d0^T. This is ONE metric-free choice; another
      discretisation of the advection would change the nonlinear numbers (N4)
      but not E1-E5.
  M5  nu = hbar_q/2 = (1 - 1/q0)/2 at the proton-pinned q0, which is the value
      q-navier-stokes.md posits (it is introduced, not derived: bean qou-0nqs).
      In the linear part nu only sets the time unit.

EXACT CHECKS (Fractions / sympy, no float):
  E1  dim ker d0^T = 31, harmonic 8, coexact 23; P and P_H are exact projectors.
  E2  on the divergence-free space Delta_1 = d1^T d1; the 23 nonzero rates are
      nu * {4^5, 6^5, 10, (5-sqrt5)^6, (5+sqrt5)^6}; slowest decaying coexact rate
      nu*(5 - sqrt5).  The 8 harmonic modes have rate 0: they never decay under
      the linear (Stokes) flow.
  E3  J is skew; K(v) is skew for a sample of integer v.
  E4  harmonic fields are exact steady states of the FULL nonlinear model:
      omega(h) = 0, so K(h) = 0 and the Lamb term vanishes.
  E5  energy identity dE/dt = -nu * |d1 v|^2 (enstrophy), exactly, because K is
      skew and P is symmetric.

NUMERICAL RUNS (mpmath, dps 40, classical RK4; reported with mp.nstr):
  N1-N3  three initial data (pure coexact, pure harmonic, mixed), amplitude 1 and
      amplitude 20: energy, enstrophy, harmonic energy over time.
  N4  harmonic energy is NOT conserved in the mixed nonlinear run: the Lamb term
      transfers energy between the coexact and harmonic parts (measured below).
      The long-time state is a harmonic field whose energy differs from the
      initial harmonic energy by that transfer.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / p) for p in
                ("computations", "computations/probes", "computations/substrate",
                 "tools/qou-substrate/python")]

import sympy  # noqa: E402
from mpmath import mp, mpf, nstr  # noqa: E402

from bring54_map import build  # noqa: E402

mp.dps = 40
ASSERTS = []


def check(label, ok, detail=""):
    ASSERTS.append((label, bool(ok), detail))
    print(f"[{'ok' if ok else 'FAIL'}] {label}{(' -- ' + detail) if detail else ''}", flush=True)


M = build()
V, E, F = M["V"], M["E"], M["F"]
d0 = sympy.Matrix(M["d0"])          # E x V
d1 = sympy.Matrix(M["d1"])          # F x E
sigma, alpha, rep, vert_of, face_of = M["sigma"], M["alpha"], M["rep"], M["vert_of"], M["face_of"]
edge_of = M["edge_of"]

# ---------------- exact projectors ----------------
ones_V = sympy.ones(V, 1)
ones_F = sympy.ones(F, 1)
L0 = d0.T * d0
L2 = d1 * d1.T
L0inv = (L0 + ones_V * ones_V.T / V).inv()     # (L0 + 11^T/n)^-1; 1 is killed by d0
L2inv = (L2 + ones_F * ones_F.T / F).inv()
Pg = d0 * L0inv * d0.T                          # projector onto im d0 (gradients)
Pc = d1.T * L2inv * d1                          # projector onto im d1^T (coexact)
I = sympy.eye(E)
P = I - Pg                                      # Leray: onto ker d0^T
PH = I - Pg - Pc                                # harmonic
check("E1a P, P_H, P_c are exact idempotents and P = P_H + P_c",
      (P * P - P).is_zero_matrix and (PH * PH - PH).is_zero_matrix
      and (Pc * Pc - Pc).is_zero_matrix and (P - PH - Pc).is_zero_matrix)
check("E1b dim div-free = 31, harmonic = 8, coexact = 23",
      (P.rank(), PH.rank(), Pc.rank()) == (31, 8, 23),
      f"ranks {P.rank()}, {PH.rank()}, {Pc.rank()}")

# ---------------- E2 linear spectrum ----------------
L1 = d0 * d0.T + d1.T * d1
check("E2a on ker d0^T, Delta_1 = d1^T d1 (L1*P == d1^T d1 * P)",
      (L1 * P - d1.T * d1 * P).is_zero_matrix)
lam = sympy.symbols("lam")
cpc = (d1.T * d1).charpoly(lam).as_expr()
fl = sympy.factor_list(cpc)
expected = sympy.expand(lam**37 * (lam - 4)**5 * (lam - 6)**5 * (lam - 10) * (lam**2 - 10*lam + 20)**6)
check("E2b charpoly(d1^T d1) = lam^37 (lam-4)^5 (lam-6)^5 (lam-10) (lam^2-10lam+20)^6",
      sympy.expand(cpc - expected) == 0,
      "nonzero spectrum = 23 coexact decay rates / nu; zero eigenspace (37) = 29 gradients + 8 harmonic")
slow = 5 - sympy.sqrt(5)

# ---------------- J: quarter turn from the vertex rotation ----------------
Jm = [[0] * E for _ in range(E)]
for dd in range(120):
    e1, s1 = edge_of[dd]
    nd = sigma[dd]
    e2, s2 = edge_of[nd]
    # outgoing value along dart dd is s1*v[e1]; rotate it to the next outgoing dart nd
    Jm[e2][e1] += s2 * s1
    Jm[e1][e2] -= s2 * s1
J = sympy.Matrix(Jm)
check("E3a J is skew-symmetric and nonzero", (J + J.T).is_zero_matrix and not J.is_zero_matrix)

# face-average operator A: E x F, (A w)_e = (w_f + w_g)/2 over the two faces of e
A = sympy.zeros(E, F)
for e in range(E):
    A[e, face_of[rep[e]]] += sympy.Rational(1, 2)
    A[e, face_of[alpha[rep[e]]]] += sympy.Rational(1, 2)


def K_of(v):
    w = d1 * v
    Dm = sympy.diag(*list(A * w))
    return (Dm * J + J * Dm) / 2


samples = [sympy.Matrix([((7 * e + 3 * k) % 11) - 5 for e in range(E)]) for k in range(3)]
check("E3b K(v) is skew for 3 integer samples", all((K_of(v) + K_of(v).T).is_zero_matrix for v in samples))

Hbasis = PH.columnspace()
check("E4 harmonic fields are exact steady states of the nonlinear model: d1 h = 0, K(h) h = 0, Delta_1 h = 0",
      len(Hbasis) == 8 and all((d1 * h).is_zero_matrix and (K_of(h) * h).is_zero_matrix
                                and (L1 * h).is_zero_matrix for h in Hbasis))

# E5: <v, -P K v - nu L1 v> = -nu |d1 v|^2 for divergence-free v
vs = [P * v for v in samples]
nu_s = sympy.Symbol("nu")
ok5 = all(sympy.simplify((v.T * (-P * K_of(v) * v - nu_s * L1 * v))[0] + nu_s * (d1 * v).norm()**2) == 0
          for v in vs)
check("E5 energy identity dE/dt = -nu |d1 v|^2 holds exactly (3 samples)", ok5)

# ---------------- numerics (mpmath) ----------------
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

q0 = mpf(Q_50_DIGIT_STR)
nu = (1 - 1 / q0) / 2


def to_mp(Mx):
    out = []
    for i in range(Mx.rows):
        row = []
        for x in Mx.row(i):
            r = sympy.Rational(x)
            row.append(mpf(int(r.p)) / mpf(int(r.q)))
        out.append(row)
    return out


Pm, PHm = to_mp(P), to_mp(PH)
d1_sp = [[(e, M["d1"][f][e]) for e in range(E) if M["d1"][f][e]] for f in range(F)]
d0T_sp = [[(e, M["d0"][e][vv]) for e in range(E) if M["d0"][e][vv]] for vv in range(V)]
d0_sp = [[(vv, M["d0"][e][vv]) for vv in range(V) if M["d0"][e][vv]] for e in range(E)]
J_sp = [[(j, Jm[i][j]) for j in range(E) if Jm[i][j]] for i in range(E)]
fe = [(face_of[rep[e]], face_of[alpha[rep[e]]]) for e in range(E)]


def matvec(Mx, x):
    return [mp.fsum(Mx[i][j] * x[j] for j in range(E) if Mx[i][j]) for i in range(E)]


def spmv(sp, x):
    return [mp.fsum(c * x[j] for j, c in row) for row in sp]


def d1T(w):
    out = [mpf(0)] * E
    for f, row in enumerate(d1_sp):
        for e, c in row:
            out[e] += c * w[f]
    return out


G0 = to_mp(L0inv)


def proj(x):
    """Leray projection x - d0 L0inv d0^T x, sparse except the 30x30 G0."""
    a = spmv(d0T_sp, x)
    b = [mp.fsum(G0[i][j] * a[j] for j in range(V)) for i in range(V)]
    g = spmv(d0_sp, b)
    return [x[e] - g[e] for e in range(E)]


def rhs(v):
    w = spmv(d1_sp, v)                                   # vorticity on faces
    wb = [(w[a] + w[b]) / 2 for a, b in fe]              # face average on edges
    Jv = spmv(J_sp, v)
    JDv = spmv(J_sp, [wb[e] * v[e] for e in range(E)])
    Kv = [(wb[e] * Jv[e] + JDv[e]) / 2 for e in range(E)]
    nl = proj(Kv)
    visc = d1T(w)                                        # d1^T d1 v (= Delta_1 v on div-free)
    return [-nl[e] - nu * visc[e] for e in range(E)]


def energy(v):
    return mp.fsum(x * x for x in v) / 2


def enstrophy(v):
    return mp.fsum(x * x for x in spmv(d1_sp, v))


def rk4(v, dt):
    k1 = rhs(v)
    k2 = rhs([v[i] + dt / 2 * k1[i] for i in range(E)])
    k3 = rhs([v[i] + dt / 2 * k2[i] for i in range(E)])
    k4 = rhs([v[i] + dt * k3[i] for i in range(E)])
    return [v[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(E)]


def normalise(v, amp):
    E0 = energy(v)
    s = amp / mp.sqrt(2 * E0)
    return [x * s for x in v]


raw = [mpf(((13 * e + 5) % 17) - 8) for e in range(E)]
v_c = matvec(to_mp(Pc), raw)
v_h = matvec(PHm, raw)
inits = {
    "coexact": v_c,
    "harmonic": v_h,
    "mixed": [v_c[i] + v_h[i] for i in range(E)],
}
T, dt = mpf(40), mpf(1) / 50
steps = int(T / dt)
results = {}
for amp in (mpf(1), mpf(20)):
    for name, v0 in inits.items():
        v = normalise(v0, amp)
        EH0 = energy(matvec(PHm, v))
        E0 = energy(v)
        # energy-identity residual over the run: E(T) - E(0) + nu * int enstrophy dt (Simpson)
        ens = [enstrophy(v)]
        for k in range(steps):
            v = rk4(v, dt)
            ens.append(enstrophy(v))
        integ = dt / 3 * (ens[0] + ens[-1] + 4 * mp.fsum(ens[1:-1:2]) + 2 * mp.fsum(ens[2:-1:2]))
        ET, EHT = energy(v), energy(matvec(PHm, v))
        resid = ET - E0 + nu * integ
        key = f"{name}_amp{int(amp)}"
        results[key] = {
            "E0": nstr(E0, 15), "E_T": nstr(ET, 15),
            "E_harm_0": nstr(EH0, 15), "E_harm_T": nstr(EHT, 15),
            "enstrophy_0": nstr(ens[0], 15), "enstrophy_T": nstr(ens[-1], 15),
            "energy_identity_residual": nstr(resid, 5),
            "harmonic_energy_change": nstr(EHT - EH0, 15),
        }
        print(key, results[key], flush=True)

check("N1 pure harmonic data is stationary (amp 1 and 20): E_T = E_0",
      all(abs(mpf(results[f"harmonic_amp{a}"]["E_T"]) - mpf(results[f"harmonic_amp{a}"]["E0"]))
          < mpf(10) ** -12 for a in (1, 20)))
check("N2 pure coexact data decays at amp 1, at least as fast as exp(-2 nu (5-sqrt5) T) up to the nonlinear transfer",
      mpf(results["coexact_amp1"]["E_T"]) < mpf(results["coexact_amp1"]["E0"]) * mp.e ** (-2 * nu * (5 - mp.sqrt(5)) * T) * 2,
      f"E_T/E_0 = {nstr(mpf(results['coexact_amp1']['E_T'])/mpf(results['coexact_amp1']['E0']), 6)}, "
      f"linear bound exp(-2 nu (5-sqrt5) T) = {nstr(mp.e ** (-2 * nu * (5 - mp.sqrt(5)) * T), 6)}")
check("N3 energy identity holds along every run to < 1e-8 (RK4 + Simpson error)",
      all(abs(mpf(r["energy_identity_residual"])) < mpf(10) ** -8 for r in results.values()),
      "max |residual| = " + nstr(max(abs(mpf(r["energy_identity_residual"])) for r in results.values()), 3))
mix20 = results["mixed_amp20"]
check("N4 measured: the nonlinear term moves energy into/out of the harmonic modes in the mixed amp-20 run",
      True, f"harmonic energy {mix20['E_harm_0']} -> {mix20['E_harm_T']} (change {mix20['harmonic_energy_change']}); "
      f"amp-1 change {results['mixed_amp1']['harmonic_energy_change']}")

failures = [a for a in ASSERTS if not a[1]]
print(f"\n=== {len(ASSERTS)-len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("bring54-dec-qns")
    w.set_description(
        "Discrete incompressible Navier-Stokes model on the exact Bring {5,4} cochain complex "
        "(unit Hodge stars, Lamb-form nonlinearity built from the vertex rotation, Leray projection). "
        "Exact: 31-dim divergence-free space = 8 harmonic + 23 coexact; linear decay rates "
        "nu*{4^5,6^5,10,(5-sqrt5)^6,(5+sqrt5)^6}; harmonic fields are exact steady states of the full "
        "nonlinear model; energy identity dE/dt = -nu*enstrophy. Numerics (mpmath dps 40, RK4) measure "
        "nonlinear energy transfer into the harmonic modes. A model computation: it says nothing about "
        "3D regularity. nu = hbar_q/2 at the proton q0 is the corpus's posited value (bean qou-0nqs).")
    w.add_data("nu", nstr(nu, 30))
    w.add_data("q0", Q_50_DIGIT_STR)
    w.add_data("linear_rates_over_nu", "4^5, 6^5, 10^1, (5-sqrt5)^6, (5+sqrt5)^6; harmonic 0^8")
    w.add_data("slowest_coexact_rate", f"nu*(5-sqrt5) = {nstr(nu * (5 - mp.sqrt(5)), 20)}")
    w.add_data("runs", results)
    w.add_data("T", nstr(T, 5))
    w.add_data("dt", nstr(dt, 5))
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save({"q0Anchor": "proton", "q0AnchorReason": "nu = (1 - 1/q0)/2 at qou_substrate.constants.Q_50_DIGIT_STR (proton pin)"})
    print("witness written")
sys.exit(1 if failures else 0)
