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
0.488602, exponential density e^{-r} 0.541266 (5√3/16); the value that would close the ³He CDE with zero strong
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
    # ρ ∝ e^{-r/a}: E = 5/(32a), r_rms = √12·a  ⇒  f = 5√3/16 = 0.541266.  The bean's
    # RESULT 3 row "exponential 0.454663" does NOT reproduce under this definition.
    "exponential": mp.sqrt(3) * mp.mpf(5) / 16,
    "box_s_wave_sin2": None,  # filled numerically in main(): ρ ∝ sin²(πr)/r² on r < 1
}
REQUIRED_3HE_STR = "0.5214134"


def hahn_exton_on_lattice(nu, k, step):
    """J_ν(p^k; p²) with p = 1/step, evaluated EXACTLY on the lattice point.

    J_ν(x; Q) = x^ν (Q^{ν+1};Q)_∞/(Q;Q)_∞ Σ_j (−1)^j Q^{j(j+1)/2} x^{2j} /((Q^{ν+1};Q)_j (Q;Q)_j),
    the same coefficient recurrence as MathlibExt/QBesselContiguityRecurrence (★) after
    x² ↦ Q x².  For x = p^k, k < 0, the alternating series peaks near 10^{k² log10(1/p)}
    while the sum is tiny: J is small ON the lattice only (off it, it grows), so p, Q and x
    are all rebuilt from `step` (an exact decimal string) at the raised precision."""
    extra = int(mp.ceil(k * k * mp.log10(mp.mpf(step)))) + 20 if k < 0 else 20
    with mp.workdps(mp.mp.dps + extra):
        p = 1 / mp.mpf(step)
        return +_hahn_exton_raw(mp.mpf(nu), p ** k, p * p)


def _hahn_exton_raw(nu, x, Q):
    a = Q ** (nu + 1)
    s = mp.mpf(0)
    t = mp.mpf(1)
    Qk = mp.mpf(1)  # Q^k
    tiny = mp.mpf(10) ** (-(mp.mp.dps - 10))
    k = 0
    while True:
        s += t
        k += 1
        Qprev = Qk
        Qk *= Q
        t_next = -Qk * x * x / ((1 - a * Qprev) * (1 - Qk)) * t
        # stop once terms are past their peak (|ratio| < 1/2) and negligible
        if abs(t_next) <= abs(t) / 2 and abs(t_next) < tiny * max(abs(s), tiny):
            s += t_next
            break
        t = t_next
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


def qbessel_shells(nu, step, kmin, kmax):
    p = 1 / mp.mpf(step)
    rs, ws = [], []
    for k in range(kmin, kmax + 1):
        r = p ** k
        rs.append(r)
        ws.append(r * r * hahn_exton_on_lattice(nu, k, step) ** 2)
    return rs, ws


def f_qbessel(nu, step, tail=mp.mpf(10) ** -30):
    """Outer edge: J decays super-exponentially on p^{-k}; inner edge: weight ~ p^{(2+2ν)k}."""
    p = 1 / mp.mpf(step)
    kmin, small = -1, 0
    while small < 4:  # extend outward until 4 consecutive shell weights are negligible
        kmin -= 1
        r = p ** kmin
        small = small + 1 if r * r * hahn_exton_on_lattice(nu, kmin, step) ** 2 < tail ** 2 else 0
    kmax = int(mp.ceil(2 * mp.log(tail) / ((2 + 2 * nu) * mp.log(p)))) + 5
    rs, ws = qbessel_shells(nu, step, kmin, kmax)
    return shell_f(rs, ws) + ((kmin, kmax),)


def f_quniform_ball(p, tail=mp.mpf(10) ** -30):
    kmax = int(mp.ceil(2 * mp.log(tail) / (3 * mp.log(p)))) + 5
    rs = [p ** k for k in range(0, kmax + 1)]
    ws = [r ** 3 for r in rs]  # r² d_p r, Jackson weight ∝ r at r
    return shell_f(rs, ws)


def main() -> int:
    mp.mp.dps = 60
    with mp.workdps(30):
        P = lambda r: mp.sin(mp.pi * r) ** 2
        C = lambda r: mp.quad(P, [0, r])
        Qb = mp.quad(P, [0, 1])
        Eb = mp.quad(lambda r: P(r) / r * C(r), [0, 1]) / Qb ** 2
        CLASSICAL["box_s_wave_sin2"] = Eb * mp.sqrt(mp.quad(lambda r: P(r) * r * r, [0, 1]) / Qb)
    if Q_50_DIGIT_STR is None:
        raise SystemExit("q_parameter unavailable")
    q0 = mp.mpf(Q_50_DIGIT_STR)
    p1 = 1 / q0
    with mp.workdps(400):
        step1 = Q_50_DIGIT_STR
        step2 = mp.nstr(mp.mpf(Q_50_DIGIT_STR) ** 2, 300)  # q0² exactly from the 50-digit q0
    half = mp.mpf(1) / 2
    REQUIRED_3HE = mp.mpf(REQUIRED_3HE_STR)
    # Convention self-test (Koelink–Swarttouw q-Hankel orthogonality at q0, not tuned):
    # Σ_k p^{2k} J(p^k) J(p^{k+m}) = δ_{m0}.  Checks base, lattice step and measure.
    Jv = {k: hahn_exton_on_lattice(half, k, step1) for k in range(-60, 700)}
    ortho = {m: mp.fsum(p1 ** (2 * k) * Jv[k] * Jv[k + m] for k in range(-60, 690))
             for m in (0, 1, 2)}
    scan = {}
    for st in ("1.05", "1.2", "1.5", "2"):
        scan[st] = f_qbessel(half, st, tail=mp.mpf(10) ** -20)[0]
    rows = {}
    for tag, nu, step in (("primary_nu_half_p_1_over_q0", half, step1),
                          ("alt_a_nu_0_p_1_over_q0", mp.mpf(0), step1),
                          ("alt_b_nu_half_p_1_over_q0sq", half, step2)):
        f, E, rms, rng = f_qbessel(nu, step)
        rows[tag] = {"nu": nu, "p": 1 / mp.mpf(step), "f": f, "E": E, "r_rms": rms, "k_range": list(rng)}
    f_u, _, _ = f_quniform_ball(p1)
    rows["alt_c_q_uniform_ball_p_1_over_q0"] = {"f": f_u}

    print(f"q0 = {mp.nstr(q0, 20)}")
    for tag, r in rows.items():
        print(f"{tag:40s} f = {mp.nstr(r['f'], 12)}")
    print("comparison only:")
    for k, v in CLASSICAL.items():
        print(f"   classical {k:14s} f = {mp.nstr(v, 9)}")
    print(f"   required (3He, zero CSB)   f = {REQUIRED_3HE}")
    print("q-scan of the primary construction (context only, no limit claimed):")
    for st, fv in scan.items():
        print(f"   q = {st:6s} f = {mp.nstr(fv, 8)}")
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
        wb.add_data("required_f_3He_comparison_only", REQUIRED_3HE_STR)
        wb.add_data("qhankel_orthogonality_at_q0", ortho)
        wb.add_data("q_scan_primary_context_only", scan)
        wb.add_assertion(name="qhankel_norm_at_q0", computed=mp.nstr(ortho[0], 30), expected="1",
                         tolerance=1e-25, source="Koelink–Swarttouw q-Hankel orthogonality, m = 0")
        wb.add_assertion(name="qhankel_overlap_m1_at_q0", computed=mp.nstr(ortho[1], 5), expected="0",
                         tolerance=1e-25, source="Koelink–Swarttouw q-Hankel orthogonality, m = 1")
        wb.add_assertion(name="primary_f_positive_finite", computed=str(int(0 < fp < 10)),
                         expected="1", tolerance=0, source="sanity only")
        print(f"witness: {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
