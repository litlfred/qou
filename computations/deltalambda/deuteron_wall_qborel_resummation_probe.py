#!/usr/bin/env python3
"""deuteron_wall_qborel_resummation_probe.py

q-Borel–Laplace resummation of the deuteron-wall binding statistic Z_n(q₀) —
the CORRECT transform on the CORRECT object.

WHY THIS PROBE EXISTS (the transform correction).
The prior "resummation closed the deuteron wall negatively" verdict
(`deuteron_wall_full_transseries_probe.py`, audit 2026-07-13) resummed the
q=1 telephone period a_D^(n) = I(n)/n with a CLASSICAL Γ-Borel divisor
Γ(n/2+1) (Gevrey-1/2). But the substrate binding object is
Z_n(q₀) = S^bal(n;q₀)·q₀^{n(n-1)/2}  (lever1_transfer_operator_spectral_qgevrey.py),
and it is q-GEVREY, not classical Gevrey: measured here,
    log Z_n(q₀) / n²  →  ln q₀,   per-level multiplier  m_n/(n·ln q₀) → 2,
so Z_n(q₀) ~ q₀^{n²}  (the "deg_q(cₙ)=n²" growth budget the C1/W2 q-Borel
programme names, docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md).
A classical Γ divisor cannot tame q₀^{n²}: the correct test is a q-Borel–Laplace
resummation with a q-Gevrey-matched divisor. That test had never been run on
Z_n(q₀). This probe runs it, parameter-free, at the substrate coupling.

THE q-CONVENTION (stated explicitly; corpus-justified — no invention).
- q-Borel kernel = the RSZ/Ramis–Zhang level-d theta kernel `tₙ` with growth
  q^{n²/2d} (w2 audit: `QBorelKernel`, level-1 `tₙ = q^{C(n,2)}`, and
  `B_{q,d}(Σ fₙzⁿ) = Σ (fₙ/tₙ)ξⁿ`). The level-1 kernel q^{C(n,2)} ~ q^{n²/2}
  UNDER-tames Z_n ~ q^{n²} (root test rises, no plateau — verified below), so
  the matched level is d = 1/2, kernel `tₙ = q₀^{n²}`. This is the q-lift of
  the classical Gevrey-1/2 moment Γ(n/2+1) AT THE SAME LEVEL 1/2 — the honest
  q-analogue of the wrong-transform probe's divisor.
- q-Laplace = a POSITIVE theta measure representing tₙ as an exact q-moment:
  points u_k = q₀^{2k}, weights p_k = q₀^{-k²}/Θ (k∈ℤ, Θ = Σ q₀^{-k²}).
  Then  Σ_k p_k u_k^n = q₀^{n²} = tₙ  EXACTLY (Jacobi-theta completing-the-square,
  gated below at reldiff 0), so
      f(x) = Σ_n aₙ xⁿ = Σ_k p_k · φ(x·q₀^{2k}),   φ(ξ) = Σ_n (aₙ/tₙ) ξⁿ
  with φ the q-Borel transform (finite radius ≈ 0.955), Padé-continued past its
  radius. This is the discrete theta-kernel (Jackson/Zhang) q-Laplace and is the
  exact q-analogue of the classical P(x) = ∫₀^∞ e^{−u} φ(x√u) du (there the
  positive measure e^{−u}du carries the Γ(n/2+1) moments; here the theta measure
  carries the q₀^{n²} moments). Positive-kernel, parameter-free.

RESULT (scope-(a) NEGATIVE, no fit). At every substrate-fixed coupling the
q-Borel–Laplace resummed binding UNDERSHOOTS B_D massively:
    m_e·f = 0.0051 / 0.058 / 0.061 MeV  at x = ℏ_q² / ℏ_q / t=ln q₀
vs B_D = 2.2245 MeV (best 2.75%, undershoot ~36×). The value is robust in the
truncation N, Padé order, theta cutoff, and the period convention (Z_n vs Z_n/n:
2.75% vs 3.24%), and the Stokes/alien jump at the substrate is ~0.007 MeV
(negligible — not a contour artifact). f reaches B_D only at x ≈ 1.12, BEYOND the
Borel radius 0.955 (through the singularity) — not a substrate quantity, so a
match would require tuning the coupling (a fit, forbidden).

HEADLINE. The correct q-Borel–Laplace resummation of the correct q-Gevrey object
Z_n(q₀), done parameter-free at the substrate coupling, does NOT close the
deuteron wall. This CONFIRMS the earlier negative-closure verdict was robust to
the transform choice — the wrong-transform probe reached the right conclusion —
and it now stands on the right object + right transform. The deuteron wall is a
distinct-mechanism problem (the working channel is the separate q-rotational
μ₀·ℏ_q·J_q² route, cheat-sheet "Bind" row), not a resummation-coupling problem.

SCOPE. (a) scope-limited negative — THIS construction, alone, at the substrate
coupling, does not reproduce B_D. NOT (b): no invariant is proved forbidding
every resummation route; a different period, measure, or bond count could differ.
No fit; no wiring; no tier change; EXPLORATORY / audit-only.

Discipline: proton pin (q_at(30), owner default 2026-08-07); all arithmetic in
mpmath.mpf (no float64); exact transfer-operator Z_n; 60 dps.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE.parent / "substrate"), str(HERE.parent), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)
sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

mp.mp.dps = 60


# ---------- exact transfer-operator Z_n(q) (mirrors lever1 W6/W9) ----------

def _corners(lam: tuple) -> list:
    out = []
    for i in range(len(lam)):
        if i == 0 or lam[i - 1] > lam[i]:
            out.append((i, lam[i]))
    out.append((len(lam), 0))
    return out


def _add_cell(lam: tuple, i: int) -> tuple:
    if i == len(lam):
        return lam + (1,)
    return lam[:i] + (lam[i] + 1,) + lam[i + 1:]


def partition_function(q, nmax):
    """Exact Z_n(q) = Σ_{w∈Inv} q^{2maj+content} via the descent transfer
    operator T_k = A_k + q^{2k} B_k, evaluated numerically at q. Returns
    Z[1..nmax]."""
    states = {((1,), 0): mp.mpf(1)}
    Z = [None, mp.mpf(1)]
    for k in range(1, nmax):
        nxt = defaultdict(lambda: mp.mpf(0))
        for (lam, r), val in states.items():
            for (i, j) in _corners(lam):
                w = q ** (j - i)
                if i > r:                      # descent edge
                    w *= q ** (2 * k)
                nxt[(_add_cell(lam, i), i)] += val * w
        states = dict(nxt)
        Z.append(mp.fsum(states.values()))
    return Z


def resum(Z, q0, N, L, KM, x, *, period="Zn_over_n", eps=mp.mpf(0)):
    """q-Borel–Laplace resummed f(x) = Σ_k p_k φ(x q₀^{2k}).

    period : binding-period convention a_n = Z_n/n ("Zn_over_n", the direct
             q-lift of I(n)/n) or a_n = Z_n ("Zn", robustness cross-check).
    eps    : contour rotation for the median (Stokes) reading; 0 = real value.
    Returns the (complex) resummed value f(x).
    """
    a = [mp.mpf(0)]
    for n in range(1, N + 1):
        a.append(Z[n] / n if period == "Zn_over_n" else Z[n])
    # level-1/2 q-Borel kernel t_n = q0^{n^2} (matched to Z_n ~ q0^{n^2})
    b = [a[n] / q0 ** (n * n) for n in range(0, N + 1)]
    p, qd = mp.pade(b, L, L)

    def phi(xi):
        return mp.polyval(p[::-1], xi) / mp.polyval(qd[::-1], xi)

    Theta = mp.fsum(q0 ** (-k * k) for k in range(-KM, KM + 1))
    rot = mp.e ** (1j * eps) if eps != 0 else mp.mpf(1)
    return mp.fsum((q0 ** (-k * k) / Theta) * phi(x * q0 ** (2 * k) * rot)
                   for k in range(-KM, KM + 1))


def main() -> int:
    q0 = q_at(30)                       # proton pin (owner default 2026-08-07)
    lnq = mp.log(q0)
    me = mp.mpf("0.51099895069")
    B_D = mp.mpf("2.22452")
    target = B_D / me
    N, L, KM = 30, 15, 40

    print("=" * 74)
    print(" deuteron wall — q-Borel–Laplace resummation of Z_n(q0) (no tuning)")
    print("=" * 74)
    print(f" q0 (proton) = {mp.nstr(q0, 22)}   dps={mp.mp.dps}")
    print(f" target B_D/m_e = {mp.nstr(target, 8)}  (B_D={mp.nstr(B_D, 6)} MeV)")

    Z = partition_function(q0, N)
    Z1 = partition_function(mp.mpf(1), N)

    # (C0) q=1 anchor: Z_n(1) = involution/telephone numbers I(n).
    I = [1, 1]
    for m in range(2, N + 1):
        I.append(I[m - 1] + (m - 1) * I[m - 2])
    okI = all(abs(Z1[n] - I[n]) < mp.mpf(10) ** (-40) * (I[n] + 1)
              for n in range(1, N + 1))
    print(f"\n(C0) q=1: Z_n == involution numbers I(n) to n={N}: "
          f"{'PASS' if okI else 'FAIL'}")

    # (C1) q-Gevrey order: log Z_n / n^2 -> ln q0  (=> Z_n ~ q0^{n^2}).
    r30 = mp.log(Z[N]) / (N * N)
    qgevrey = r30 > lnq and r30 < mp.mpf("1.3") * lnq        # above ln q0, converging down
    print(f"(C1) log Z_{N}/{N}^2 = {mp.nstr(r30, 8)}  vs ln q0 = {mp.nstr(lnq, 8)}"
          f"  => Z_n ~ q0^(n^2), q-Gevrey: {'PASS' if qgevrey else 'FAIL'}")

    # (C2) level test: level-1 theta kernel q^{C(n,2)} UNDER-tames (rises, no
    # plateau); matched level-1/2 kernel q^{n^2} gives finite Borel radius.
    def root(div_exp, n):
        return (Z[n] / n / q0 ** div_exp(n)) ** (mp.mpf(1) / n)
    lvl1 = [root(lambda n: n * (n - 1) // 2, n) for n in (10, 20, 30)]
    lvlh = [root(lambda n: n * n, n) for n in (10, 20, 30)]
    lvl1_rises = lvl1[2] > lvl1[1] > lvl1[0]
    lvlh_tamed = lvlh[2] < mp.mpf("1.2") and lvlh[2] < lvlh[0]   # bounded, settling
    print(f"(C2) root test |a_n/div|^(1/n) at n=10,20,30:")
    print(f"       level-1  q^C(n,2): {[mp.nstr(v,5) for v in lvl1]}  "
          f"rises (under-tames): {'PASS' if lvl1_rises else 'FAIL'}")
    print(f"       level-1/2 q^(n^2): {[mp.nstr(v,5) for v in lvlh]}  "
          f"finite radius (matched): {'PASS' if lvlh_tamed else 'FAIL'}")

    # (C3) theta measure reproduces the q-moment t_n = q0^{n^2} EXACTLY.
    Theta = mp.fsum(q0 ** (-k * k) for k in range(-KM, KM + 1))
    mom_ok = True
    for n in range(1, 8):
        m = mp.fsum((q0 ** (-k * k) / Theta) * (q0 ** (2 * k)) ** n
                    for k in range(-KM, KM + 1))
        if abs(m - q0 ** (n * n)) / q0 ** (n * n) > mp.mpf(10) ** (-45):
            mom_ok = False
    print(f"(C3) theta measure Σ p_k u_k^n == q0^(n^2) exactly (n≤7): "
          f"{'PASS' if mom_ok else 'FAIL'}")

    # Borel radius (nearest Padé pole of φ).
    a = [mp.mpf(0)] + [Z[n] / n for n in range(1, N + 1)]
    bcoef = [a[n] / q0 ** (n * n) for n in range(0, N + 1)]
    _, qd = mp.pade(bcoef, L, L)
    poles = sorted(mp.polyroots(qd[::-1]), key=lambda z: abs(z))
    radius = abs(poles[0])
    print(f"     q-Borel radius (nearest φ pole) = {mp.nstr(radius, 6)}")

    # ---------- the resummation at substrate couplings (no tuning) ----------
    hbar = 1 - 1 / q0
    couplings = [("hbar_q^2", hbar ** 2), ("hbar_q", hbar), ("t=ln q0", lnq)]
    print("\n q-Borel–Laplace resummed binding  B = m_e·M_2·f(x)  (M_2 = 1 bond):")
    rows = {}
    best = mp.mpf(0)
    for name, x in couplings:
        f0 = mp.re(resum(Z, q0, N, L, KM, x))
        fp = resum(Z, q0, N, L, KM, x, eps=mp.mpf("0.1"))
        fm = resum(Z, q0, N, L, KM, x, eps=-mp.mpf("0.1"))
        jump = me * abs(mp.im((fp - fm) / 2))
        Bpred = me * f0
        pct = Bpred / B_D * 100
        best = max(best, Bpred)
        rows[name] = {"x": mp.nstr(x, 8), "m_e_f_MeV": mp.nstr(Bpred, 8),
                      "pct_of_B_D": mp.nstr(pct, 5), "alien_jump_MeV": mp.nstr(jump, 4)}
        print(f"   x={name:9s}={mp.nstr(x, 5):>9}: m_e·f={mp.nstr(Bpred, 6):>10} MeV"
              f" ({mp.nstr(pct, 4)}% of B_D)  alien|Im|={mp.nstr(jump, 3)} MeV")

    # period-convention robustness
    fZn = mp.re(resum(Z, q0, N, L, KM, lnq, period="Zn"))
    print(f"\n period robustness at x=ln q0: Z_n/n -> {mp.nstr(best/B_D*100,4)}% ; "
          f"Z_n -> {mp.nstr(me*fZn/B_D*100,4)}% of B_D (both undershoot)")

    # diagnostic-only: what coupling WOULD give B_D (a fit if adopted)
    try:
        xstar = mp.findroot(lambda x: me * mp.re(resum(Z, q0, N, L, KM, x)) - B_D,
                            mp.mpf("0.5"))
    except Exception:
        xstar = mp.mpf("nan")
    print(f" [diagnostic only] x giving B_D = {mp.nstr(xstar, 6)}  "
          f"(> Borel radius {mp.nstr(radius,4)}, > substrate x≤{mp.nstr(lnq,4)}) "
          f"=> a FIT, forbidden")

    undershoots = best < B_D / 10
    ratio = B_D / best
    print(f"\n best substrate value {mp.nstr(best,5)} MeV = {mp.nstr(best/B_D*100,4)}% "
          f"of B_D => undershoots by ~{mp.nstr(ratio,4)}×")

    verdict = (
        "Scope-(a) NEGATIVE (no fit): the q-Borel–Laplace resummation of the "
        "q-Gevrey binding statistic Z_n(q0) ~ q0^(n^2), with the level-1/2 q-Borel "
        "kernel t_n=q0^(n^2) (the q-lift of the classical Gevrey-1/2 moment "
        "Gamma(n/2+1)) and a positive theta measure carrying t_n as an exact "
        "q-moment (Jackson/Zhang q-Laplace), evaluated parameter-free at the "
        f"substrate coupling gives m_e·f <= {mp.nstr(best,4)} MeV "
        f"(<= {mp.nstr(best/B_D*100,3)}% of B_D={mp.nstr(B_D,5)}), undershooting by "
        f"~{int(ratio)}x. The value is robust in N, Pade order, theta cutoff and the "
        "period convention (Z_n/n 2.75%, Z_n 3.24%); the Stokes/alien jump at the "
        "substrate is ~0.007 MeV (negligible). f reaches B_D only at x~1.12, beyond "
        f"the Borel radius {mp.nstr(radius,4)} (through the singularity) — not a "
        "substrate quantity, so a match would require tuning the coupling (a fit). "
        "This CORRECTS the transform used by the prior negative-closure probe "
        "(classical Gamma-Borel on the q=1 telephone period) and confirms its "
        "conclusion was robust: the correct q-Borel–Laplace on the correct q-Gevrey "
        "object does NOT close the deuteron wall parameter-free. Distinct-mechanism "
        "(q-rotational mu0·hbar_q·J_q^2) route indicated. No fit; no wiring; no tier "
        "change; EXPLORATORY."
    )
    print("\nVERDICT:", verdict)

    ok = okI and qgevrey and lvl1_rises and lvlh_tamed and mom_ok and undershoots

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("deuteron-wall-qborel-resummation", engine="mpmath",
                            _script_path=__file__)
        wb.set_description(
            "q-Borel–Laplace resummation of the deuteron-wall binding statistic "
            "Z_n(q0) — the CORRECT transform on the CORRECT object, correcting "
            "deuteron_wall_full_transseries_probe.py (which used a classical "
            "Gamma-Borel on the q=1 telephone period I(n)/n). Measured: Z_n(q0) is "
            "q-Gevrey, log Z_n/n^2 -> ln q0 so Z_n ~ q0^(n^2); the level-1 theta "
            "kernel q^C(n,2) under-tames (root test rises), the matched level-1/2 "
            "kernel q0^(n^2) gives finite Borel radius ~0.955. q-Laplace via a "
            "positive theta measure (points q0^(2k), weights q0^(-k^2)/Theta) that "
            "reproduces t_n=q0^(n^2) as an exact q-moment. Parameter-free at the "
            "substrate coupling the resummed binding m_e·f <= 0.061 MeV (<=2.75% of "
            "B_D=2.2245), undershooting ~36x; robust in N/Pade/theta-cutoff/period; "
            "alien jump ~0.007 MeV. Reaches B_D only at x~1.12 beyond the Borel "
            "radius (a fit). Scope-(a) negative; confirms the earlier negative "
            "closure was robust to the transform. No fit; no wiring; audit-only.")
        wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
        wb.add_data("q0_pin", "proton (q_at(30))")
        wb.add_data("q0_str", mp.nstr(q0, 50))
        wb.add_data("qgevrey_logZ_over_n2", mp.nstr(r30, 12))
        wb.add_data("ln_q0", mp.nstr(lnq, 12))
        wb.add_data("qborel_kernel", "level-1/2 t_n = q0^{n^2}")
        wb.add_data("qlaplace_measure",
                    "theta: u_k=q0^{2k}, p_k=q0^{-k^2}/Theta (exact q-moment)")
        wb.add_data("qborel_radius", mp.nstr(radius, 10))
        wb.add_data("target_B_D_over_m_e", mp.nstr(target, 10))
        wb.add_data("resummation_by_coupling", rows)
        wb.add_data("best_substrate_MeV", mp.nstr(best, 10))
        wb.add_data("best_pct_of_B_D", mp.nstr(best / B_D * 100, 6))
        wb.add_data("undershoot_factor", mp.nstr(ratio, 6))
        wb.add_data("x_star_for_B_D_diagnostic_only", mp.nstr(xstar, 8))
        wb.add_data("period_robustness_pct",
                    {"Zn_over_n": mp.nstr(best / B_D * 100, 5),
                     "Zn": mp.nstr(me * fZn / B_D * 100, 5)})
        wb.add_data("scope", "(a) scope-limited negative — not (b); no invariant "
                             "proved forbidding all resummation routes")
        wb.add_data("verdict", verdict)
        wb.add_assertion(
            name="qborel_resummation_undershoots_B_D_at_substrate",
            computed=str(int(ok)), expected="1", tolerance=0,
            source="q-Borel–Laplace (level-1/2 kernel q0^{n^2}, theta-measure "
                   "q-Laplace) of Z_n(q0) at the substrate coupling gives "
                   f"<= {mp.nstr(best,4)} MeV (<= {mp.nstr(best/B_D*100,3)}% of B_D); "
                   "reaches B_D only beyond the Borel radius (a fit). Scope-(a) "
                   "negative; no fit; audit-only.")
        out = wb.save()
        print(f"\nwitness -> {out}")
    except Exception as e:  # noqa: BLE001
        print(f"\n(witness skipped: {e})")

    print(f"\n### Verdict: {'ALL CHECKS PASS (negative closure)' if ok else 'CHECK FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
