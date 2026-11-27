#!/usr/bin/env python3
"""
coulomb_shape_factor_qbessel_probe.py — bean qou-usft, shape half (thread "Derive the
Coulomb shape factor from q-Bessel", 2026-11-27).

Goal: a SCALE-FREE Coulomb shape factor f, defined by  E_C = f · Q² / r_rms  (Q = 1, α ħc = 1),
for a charge density that the corpus already carries, instead of the classical uniform-ball
3/5.  No radius is produced or claimed: E_q(2) has a q^ℤ dilation symmetry, so only the
dimensionless product E_C · r_rms is meaningful.

PRE-REGISTRATION (committed before the first run at q₀; nothing below was tuned)
---------------------------------------------------------------------------------
Arena (corpus): the non-compact SU_q(2) → E_q(2) contraction with Hahn–Exton q-Bessel
functions at real q₀ > 1 (KeystoneQBesselRadialTarget.lean; audit
2026-06-22-keystone-modular-category-identification.md).  Written with p := 1/q₀ < 1.

State (forced, no selection):
  * Koelink–Swarttouw q-Hankel orthogonality on the FULL Jackson lattice p^ℤ,
        Σ_{k∈ℤ} p^{2k} J_ν(p^{k+n}; p²) J_ν(p^{k+m}; p²) = p^{-2n} δ_{nm},
    so each J_ν(p^n x; p²) is a normalisable radial state with measure x d_p x — no box,
    no boundary condition, no extra length.  All n give the SAME density up to the
    dilation x ↦ p^{-n} x, so f does not depend on n.  (Classically, q = 1, no such
    normalisable state exists; this is a genuinely q-deformed object.)
  * Coulomb is a 3-D quantity and the ground channel is l = 0.  The 3-D radial
    density of an s-wave is r·|J_{1/2}(r)|² dr = (2-D radial measure)·|J_{1/2}|², so
    ν = l + 1/2 = 1/2.
  * Lattice step p = 1/q₀ with functions J_ν(·; p²): Koelink's E_q(2) convention, the
    same q² base as the Haar moments [k+1]_{q²} (OqSU2HaarState.haarMoment).
  * Density: shell charge P_k ∝ p^{2k} J_{1/2}(p^k; p²)² on the sphere of radius p^k,
    k ∈ ℤ, normalised to Σ P_k = 1.
  * Coulomb energy of concentric shells (exact 3-D electrostatics, no derivative
    convention):  E = ½ Σ_{i,j} P_i P_j / max(r_i, r_j),  r_rms² = Σ P_k r_k².
PRIMARY:  f := E · r_rms  for (ν = 1/2, step p = 1/q₀).

ALTERNATES (reported so the size of each convention is visible; NEVER selected):
  (a) ν = 0      — the intrinsic weight-0 E_q(2) channel (2-D), used as if 3-D.
  (b) step p = 1/q₀², functions J_ν(·; p²)  — the other reading of "base q₀".
  (c) q-uniform ball (constant density, measure r² d_p r on p^{ℕ}) — the q-Neumann
      ground state; its classical limit is the shipped 3/5 ball.
Classical references (closed forms, comparison only): uniform 0.464758, Gaussian
0.488602, exponential 0.454663; the value that would close the ³He CDE with zero strong
CSB, 0.5214134, from the measured r_rms(³He) (bean qou-usft STEP 3).  These are used ONLY
in the printed comparison, never as inputs.  Empirical values do not enter f.

Not wired to the scorecard or to coulomb_energy.py.  Scope (a): a statement about this
construction alone.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
try:
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
except Exception:  # pragma: no cover — standalone run
    Q_50_DIGIT_STR = None
try:
    from witness_base import WitnessBuilder  # noqa: E402
except Exception:  # pragma: no cover
    WitnessBuilder = None

# Comparison values only (bean qou-usft RESULT 3 / STEP 3). Never inputs.
CLASSICAL = {
    "uniform_ball": mp.mpf(3) / 5 * mp.sqrt(mp.mpf(3) / 5),
    "gaussian": mp.sqrt(3) / (2 * mp.sqrt(mp.pi)),
    "exponential": mp.sqrt(3) * mp.mpf(5) / 16,
}
REQUIRED_3HE = mp.mpf("0.5214134")


def hahn_exton(nu, x, Q):
    """J_ν(x; Q) = x^ν (Q^{ν+1};Q)_∞/(Q;Q)_∞ Σ_k (−1)^k Q^{k(k+1)/2} x^{2k} /((Q^{ν+1};Q)_k (Q;Q)_k).
    Same coefficient recurrence as MathlibExt/QBesselContiguityRecurrence (★) after x² ↦ Q x²."""
    a = Q ** (nu + 1)
    s = mp.mpf(0)
    t = mp.mpf(1)
    tiny = mp.mpf(10) ** (-(mp.mp.dps - 10))
    k = 0
    while True:
        s += t
        k += 1
        t *= -(Q ** k) * x * x / ((1 - a * Q ** (k - 1)) * (1 - Q ** k))
        if k > 20 and abs(t) < tiny * max(abs(s), tiny) and abs(t * x * x) < abs(t):
            s += t
            break
    return x ** nu * mp.qp(a, Q) / mp.qp(Q, Q) * s


def shell_f(radii, weights):
    """f = E · r_rms for unit charge on concentric shells. E = Σ_j (P_j/r_j)(P_j/2 + C_j)."""
    pairs = sorted(zip(radii, weights))
    tot = mp.fsum(w for _, w in pairs)
    pairs = [(r, w / tot) for r, w in pairs]
    E = mp.mpf(0)
    inner = mp.mpf(0)
    for r, w in pairs:
        E += w / r * (w / 2 + inner)
        inner += w
    rms = mp.sqrt(mp.fsum(w * r * r for r, w in pairs))
    return E * rms, E, rms


def qbessel_shells(nu, p, kmin, kmax):
    Q = p * p
    rs, ws = [], []
    for k in range(kmin, kmax + 1):
        r = p ** k
        rs.append(r)
        ws.append(r * r * hahn_exton(nu, r, Q) ** 2)
    return rs, ws


def f_qbessel(nu, p, tail=mp.mpf(10) ** -30):
    """Outer edge: J decays super-exponentially on p^{-k}; inner edge: weight ~ p^{(2+2ν)k}."""
    kmin = -1
    while True:  # extend outward until the shell weight is negligible
        r = p ** kmin
        if kmin < -5 and r * r * hahn_exton(nu, r, p * p) ** 2 < tail ** 2:
            break
        kmin -= 1
    kmax = int(mp.ceil(2 * mp.log(tail) / ((2 + 2 * nu) * mp.log(p)))) + 5
    rs, ws = qbessel_shells(nu, p, kmin, kmax)
    return shell_f(rs, ws) + ((kmin, kmax),)


def f_quniform_ball(p, tail=mp.mpf(10) ** -30):
    kmax = int(mp.ceil(2 * mp.log(tail) / (3 * mp.log(p)))) + 5
    rs = [p ** k for k in range(0, kmax + 1)]
    ws = [r ** 3 for r in rs]  # r² d_p r, Jackson weight ∝ r at r
    return shell_f(rs, ws)


def main() -> int:
    mp.mp.dps = 120
    if Q_50_DIGIT_STR is None:
        raise SystemExit("q_parameter unavailable")
    q0 = mp.mpf(Q_50_DIGIT_STR)
    p1, p2 = 1 / q0, 1 / q0 ** 2
    half = mp.mpf(1) / 2
    rows = {}
    for tag, nu, p in (("primary_nu_half_p_1_over_q0", half, p1),
                       ("alt_a_nu_0_p_1_over_q0", mp.mpf(0), p1),
                       ("alt_b_nu_half_p_1_over_q0sq", half, p2)):
        f, E, rms, rng = f_qbessel(nu, p)
        rows[tag] = {"nu": nu, "p": p, "f": f, "E": E, "r_rms": rms, "k_range": list(rng)}
    f_u, _, _ = f_quniform_ball(p1)
    rows["alt_c_q_uniform_ball_p_1_over_q0"] = {"f": f_u}

    print(f"q0 = {mp.nstr(q0, 20)}")
    for tag, r in rows.items():
        print(f"{tag:40s} f = {mp.nstr(r['f'], 12)}")
    print("comparison only:")
    for k, v in CLASSICAL.items():
        print(f"   classical {k:14s} f = {mp.nstr(v, 9)}")
    print(f"   required (3He, zero CSB)   f = {REQUIRED_3HE}")
    fp = rows["primary_nu_half_p_1_over_q0"]["f"]
    print(f"primary / uniform  = {mp.nstr(fp / CLASSICAL['uniform_ball'], 8)}")
    print(f"primary / gaussian = {mp.nstr(fp / CLASSICAL['gaussian'], 8)}")
    print(f"primary / required = {mp.nstr(fp / REQUIRED_3HE, 8)}")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("coulomb-shape-factor-qbessel-probe", engine="mpmath")
        wb.set_description(
            "Bean qou-usft shape half: scale-free Coulomb shape factor f = E_C·r_rms/Q² for the "
            "q-Hankel (Hahn–Exton, E_q(2)) l = 0 state J_{1/2}(p^k; p²), p = 1/q0, on the full "
            "Jackson lattice p^Z with measure x d_p x — normalisable without a box, unique up to "
            "q^Z dilation, so f is well defined while no radius is. Concentric-shell 3-D "
            "electrostatics. Alternates (ν = 0, p = 1/q0², q-uniform ball) reported, never "
            "selected. Classical shapes and the 3He required f are comparison only. Scope (a).")
        wb.add_data("rows", rows)
        wb.add_data("classical_comparison", CLASSICAL)
        wb.add_data("required_f_3He_comparison_only", REQUIRED_3HE)
        wb.add_assertion(name="primary_f_positive_finite", computed=str(int(0 < fp < 10)),
                         expected="1", tolerance=0, source="sanity only")
        print(f"witness: {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
