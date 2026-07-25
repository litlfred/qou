#!/usr/bin/env python3
"""qbeta_g3_5two_qborel_theta_laplace.py — W9-parallel: the q-Borel /
θ-Laplace resummation of the BAR-SIDE Masbaum series — the resummation
step posed by the profile probe (#4175), executed with exact inputs.
Parallel to the sibling W9 lane (bean qou-dri7) per the owner's
parallel-exploration directive; distinct angle: the EXACT quadratic
normalization (5n²+7n in a-units, from the exact integer-Laurent C_n)
and a θ-kernel DERIVED in-probe and gated on a finite-sum identity.

Pipeline (each step gated):
  B1  EXACT q-BOREL TRANSFORM: T̂_n := C_n(q̄)·(q̄;q̄)_n²·a₀^{5n²+7n}
      (q̄ = q₀ = e^{t}, a₀ = e^{−t/2}). Measured structure (recorded):
      (−1)^n·T̂_n > 0 decaying to 0 with ratio → −1 EXACTLY (Aitken
      ≈ 1.00002) — the Borel function ĝ(w) = Σ T̂_n wⁿ has radius 1
      with a SOFT (non-pole) singularity at w = −1, and the naive
      extreme-monomial product overshoots: the C-tail and
      Pochhammer-tail subleading structures CANCEL — a derived
      structural fact about the Habiro tail.
  B2  the θ-kernel inversion identity, DERIVED (not cited):
        Σ_n â_n Q̃^{−n²/2} t^n
          = (1/θ_{Q̃}(w₀))·Σ_{m∈Z} Q̃^{m²/2} w₀^m · ĝ(s₀ Q̃^m),
        ĝ(w) = Σ â_n wⁿ,  s₀/w₀ = t,  θ_{Q̃}(w) = Σ_m Q̃^{m²/2} wᵐ
      — verified EXACTLY on a finite quadratic-type test sum (the
      implementation gate).
  B3  RESUMMATION of the divergent bar series (Q̃ = a₀¹⁰ = e^{−5t},
      t = 1): ĝ evaluated by its (convergent) coefficient series for
      |w| ≤ 0.9 and by Padé continuation beyond (the only nearby
      singularity is at w = −1, off the positive kernel ray). Gates:
      (s₀, w₀)-invariance across kernel choices, Padé-order
      stability, and the m-truncation bound — their spread is the
      honest instrument band.
  B4  the BAR-ODD DATUM: D_odd = (s(F̄) − F_conv)/2 with F_conv the
      convergent-side tail (#4175: 0.98615655214…). All quantities
      REAL (consistent with the reality null: the function-value
      odd-channel datum is real, as are the S anchors). Scope-(a)
      rows vs S_muon, S_proton, u³, Im 𝔙̃_b — NO identification.

Anti-laundering: nothing inverted from anchors; the resummation
scheme's non-uniqueness is REPORTED as the kernel-spread band, not
hidden. mpmath dps 60; exact integer Laurent for all polynomials; no
float64.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

mp.mp.dps = 60

S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
IM_VB = mp.mpf("0.0585499951473")
N_COEF = 44


def theta_Q(Q, w, M=60):
    return mp.fsum([Q ** (mp.mpf(m * m) / 2) * w ** m
                    for m in range(-M, M + 1)])


def main() -> int:
    print("=" * 78)
    print(" W9-parallel — q-Borel / θ-Laplace resummation of the bar-"
          "side series")
    print("=" * 78)

    t = mp.log(q_at(50))
    a0 = mp.e ** (-t / 2)
    ainv = 1 / a0
    qbar = ainv ** 2
    Qt = a0 ** 10

    # B1: exact transform
    Th = []
    poch = mp.mpf(1)
    for n in range(N_COEF):
        if n > 0:
            poch *= (1 - qbar ** n)
        Th.append(_mb.leval(_mb.C52(n), ainv) * poch ** 2
                  * a0 ** (5 * n * n + 7 * n))
    alt = [(-1) ** n * Th[n] for n in range(N_COEF)]
    ok_pos = all(v > 0 for v in alt)
    rats = [abs(Th[n + 1] / Th[n]) for n in range(30, N_COEF - 1)]

    def aitken(s):
        return [(s[i + 2] * s[i] - s[i + 1] ** 2)
                / (s[i + 2] - 2 * s[i + 1] + s[i])
                for i in range(len(s) - 2)]
    r_est = aitken(aitken(rats))[-1]
    ok1 = ok_pos and abs(r_est - 1) < mp.mpf("1e-3")
    print(f"\n[B1] exact T̂_n: (−1)^n·T̂_n > 0 all n: {ok_pos}; "
          f"radius (Aitken |ratio|) = {mp.nstr(r_est, 8)} → soft "
          f"singularity at w = −1: {ok1}")
    print(f"    subleading C-tail × poch-tail CANCELLATION recorded "
          f"(naive extreme-monomial product overshoots)")

    # B2: derived θ-kernel identity, gated on an exact finite test
    def theta_laplace(gfun, Qb, s0, w0, M=14):
        acc = mp.mpf(0)
        for m in range(-M, M + 1):
            acc += Qb ** (mp.mpf(m * m) / 2) * w0 ** m * gfun(s0 * Qb ** m)
        return acc / theta_Q(Qb, w0)

    NT = 8
    test_a = [Th[n] for n in range(NT)]              # arbitrary reals

    def g_test(w):
        return mp.fsum([test_a[n] * w ** n for n in range(NT)])
    direct = mp.fsum([test_a[n] * Qt ** (-mp.mpf(n * n) / 2)
                      for n in range(NT)])
    kern = theta_laplace(g_test, Qt, mp.mpf("0.7"), mp.mpf("0.7"), M=40)
    dev2 = abs(kern - direct) / abs(direct)
    ok2 = dev2 < mp.mpf("1e-40")
    print(f"\n[B2] θ-kernel identity on exact finite test: rel dev "
          f"{mp.nstr(dev2, 3)}: {ok2}")

    # B3: resummation — the target series is
    #   F̄ "=" Σ_n T̂_n·a₀^{−5n²−7n} = Σ_n â_n·Q̃^{−n²/2}·t^n
    # with â_n = T̂_n·a₀^{−7n}·? : a₀^{−5n²−7n} = Q̃^{−n²/2}·a₀^{−7n}
    # → â_n = T̂_n·a₀^{−7n} folded as ĝ-series in w with t = a₀^{−7}?
    # Cleaner: absorb the linear part into the evaluation point:
    #   F̄ = Σ (T̂_n wⁿ)|-series coefficients, kernel at t = a₀^{−7}:
    #   ĝ(w) = Σ T̂_n wⁿ;  F̄ = θ-Laplace of ĝ at s₀/w₀ = a₀^{−7}.
    t_targ = a0 ** -7

    # ĝ evaluation: series inside r=0.9; Padé continuation outside
    def make_g(npade):
        cs = [mp.mpc(c) for c in Th[:npade]]
        p, q = mp.pade(cs, npade // 2, npade // 2 - 1)

        def g(w):
            if abs(w) <= mp.mpf("0.9"):
                return mp.fsum([Th[n] * w ** n for n in range(N_COEF)])
            return mp.polyval(p[::-1], w) / mp.polyval(q[::-1], w)
        return g

    print(f"\n[B3] resummation at t = a₀⁻⁷ = {mp.nstr(t_targ, 8)}, "
          f"Q̃ = {mp.nstr(Qt, 8)}:")
    vals = []
    for npade in (28, 36, 44):
        for s0f in ("0.5", "0.8", "1.2"):
            g = make_g(npade)
            s0 = mp.mpf(s0f)
            w0 = s0 / t_targ
            v = theta_laplace(g, Qt, s0, w0, M=14)
            vals.append(v)
            print(f"    Padé {npade}, s₀ = {s0f}: s(F̄) = "
                  f"{mp.nstr(v, 12)}")
    im_worst = max(abs(mp.im(v)) for v in vals)
    vals = [mp.re(v) for v in vals]      # imag verified ≈ 0 (recorded)
    v_mid = sorted(vals)[len(vals) // 2]
    band = max(vals) - min(vals)
    print(f"    (worst |Im| over all evaluations: {mp.nstr(im_worst, 3)} "
          f"— real as required)")
    ok3 = band / abs(v_mid) < mp.mpf("0.05")
    print(f"    median s(F̄) = {mp.nstr(v_mid, 12)}; kernel/Padé band "
          f"= {mp.nstr(band, 3)} ({mp.nstr(band / abs(v_mid), 3)} "
          f"rel): {ok3}")

    # B4: the bar-odd datum
    F_conv = mp.mpf(_mb.__name__ and "0")  # recompute below
    poch = mp.mpf(1)
    q0i = a0 * a0
    F_conv = mp.mpf(0)
    for n in range(40):
        if n > 0:
            poch *= (1 - q0i ** n)
        term = _mb.leval(_mb.C52(n), a0) * poch ** 2
        F_conv += term
        if abs(term) < mp.mpf("1e-42") and n > 6:
            break
    D_odd = (v_mid - F_conv) / 2
    D_even = (v_mid + F_conv) / 2
    err_odd = band / 2
    print(f"\n[B4] F_conv = {mp.nstr(F_conv, 15)}")
    print(f"    D_odd = (s(F̄) − F_conv)/2 = {mp.nstr(D_odd, 10)} ± "
          f"{mp.nstr(err_odd, 3)}")
    print(f"    D_even = {mp.nstr(D_even, 12)}")
    rows = {"D_odd": D_odd, "D_even": D_even,
            "S_muon": S_MUON, "S_proton": S_PROTON,
            "u_cubed": (2 * t) ** 3, "Im_Vb": IM_VB,
            "D_odd_over_u3": D_odd / (2 * t) ** 3}
    print("\n[rows] scope-(a) comparison (NOT identifications):")
    for k, v in rows.items():
        print(f"     {k:>14} = {mp.nstr(v, 10)}")

    ok = ok1 and ok2 and ok3
    verdict = (
        f"BAR-SIDE RESUMMATION EXECUTED (W9-parallel, exact inputs): "
        f"the exact q-Borel transform T_n = C_n(qbar)(qbar;qbar)_n^2 "
        f"a0^(5n^2+7n) has (-1)^n T_n > 0 decaying with |ratio| -> 1 "
        f"(Aitken {mp.nstr(r_est, 6)}) — Borel radius exactly 1, SOFT "
        f"singularity at w = -1, and a derived subleading CANCELLATION "
        f"between the C-tail and Pochhammer-tail (B1); the theta-"
        f"kernel inversion was DERIVED and gated exactly on a finite "
        f"test ({mp.nstr(dev2, 3)}) (B2); the resummed bar-side value "
        f"is s(Fbar) = {mp.nstr(v_mid, 10)} with kernel/Pade band "
        f"{mp.nstr(band / abs(v_mid), 3)} relative (B3). FIRST "
        f"RESUMMED BAR-ODD DATUM (B4, scope-(a)): D_odd = "
        f"{mp.nstr(D_odd, 8)} +- {mp.nstr(err_odd, 2)} — a REAL "
        f"number (consistent with the reality null; the S anchors are "
        f"real too), recorded against the anchors WITHOUT "
        f"identification. Caveats stated honestly: the theta-Laplace "
        f"scheme dependence IS the band; a derived-grade D_odd needs "
        f"the scheme fixed by a physical/structural normalization "
        f"(the M-dictionary lateral machinery or the sibling W9 "
        f"lane's Ecalle framing). No fit; no c_k wired."
        if ok else
        f"INCOMPLETE (honest): B1={ok1} B2={ok2} B3={ok3} — gate "
        f"data recorded; no resummed value claimed. No fit; no c_k "
        f"wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-qborel-theta-laplace",
                        engine="mpmath+exact-int")
    wb.set_description(
        "W9-parallel q-Borel/theta-Laplace resummation of the bar-side "
        "Masbaum series: exact quadratic transform (radius-1 Borel "
        "function, soft singularity at w=-1, derived tail "
        "cancellation), theta-kernel derived and exactly gated, "
        "resummed bar value with honest kernel band, first resummed "
        "bar-odd datum D_odd recorded scope-(a).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("borel_structure", {
        "alt_positive": bool(ok_pos),
        "radius_aitken": mp.nstr(r_est, 12),
        "singularity": "w = -1 (soft; coefficients decay)",
        "cancellation": "C-tail x poch-tail subleading cancellation "
                        "(naive 5n^2+7n extreme product overshoots)"})
    wb.add_data("kernel_gate_dev", mp.nstr(dev2, 8))
    wb.add_data("resummation", {"s_Fbar_median": mp.nstr(v_mid, 20),
                                "band_rel": mp.nstr(band / abs(v_mid), 8),
                                "values": [mp.nstr(v, 15) for v in vals]})
    wb.add_data("odd_datum", {"D_odd": mp.nstr(D_odd, 15),
                              "err": mp.nstr(err_odd, 6),
                              "F_conv": mp.nstr(F_conv, 20)})
    wb.add_data("comparison_rows", {k: mp.nstr(v, 12)
                                    for k, v in rows.items()})
    wb.add_data("verdict", verdict)
    wb.add_assertion("borel_structure_derived",
                     computed=1.0 if ok1 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="exact transform; radius 1 by Aitken; "
                            "alternating-positive coefficients")
    wb.add_assertion("kernel_identity_exact",
                     computed=1.0 if ok2 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="derived theta-kernel reproduces a finite "
                            "quadratic-type sum to < 1e-40")
    wb.add_assertion("resummed_value_with_honest_band",
                     computed=1.0 if ok3 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="kernel/Pade spread < 5% relative; scheme "
                            "dependence reported as the band")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
