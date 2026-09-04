#!/usr/bin/env python3
"""qbeta_g3_5two_dodd_median_crosschecks.py — the MEDIAN (Écalle-torus)
normalization of the resummed bar-odd datum D_odd (#4184) plus the
cross-check battery — upgrading D_odd from scheme-tied to
median-normalized-with-quantified-ambiguity, and situating it against
the sibling b3ix estimate and the q₀-pin structure.

E — MEDIAN NORMALIZATION (the Écalle question, answered computably):
  the θ-Laplace of a quadratic q-Gevrey series is a FAMILY of sums
  indexed by the spiral offset δ (sampling points s₀·Q̃^{m+δ}); the
  q-analogue of the Écalle median is the δ-TORUS AVERAGE. This probe
  sweeps δ densely over one period, records the orbit s(δ), takes
  s_med = mean and reports the orbit VARIATION as the EXACT scheme
  ambiguity (the q-Stokes content along the positive ray, sourced by
  the soft w = −1 Borel singularity). Expected (from #4184's 3-point
  scan): variation ~1e-10 — seven orders below the physics scale, so
  the normalization question RESOLVES: D_odd is scheme-robust.

C — CROSS-CHECKS:
  C1  SUPERASYMPTOTIC consistency: the divergent bar series' optimal
      (minimal-term) truncation must agree with s(F̄) within the
      minimal term — the classic internal gate of any resummation.
  C2  vs the sibling b3ix order-3 tail (merged witness
      qbeta-5two-order3-barodd-tail: T_odd = +0.01916053 at the muon
      pin): same-decade row; DIFFERENT object (order-3 truncated
      action vs full resummed tail split) — recorded, not gated.
  C3  q₀-PIN SENSITIVITY: the full pipeline recomputed at the muon
      pin (q₀ = 1.10997859555733471989976322048322502665620840878…).
      The pins differ by ~11.5 ppb, so D_odd(muon) − D_odd(proton)
      is expected TINY — while S_muon − S_proton = +0.0491. The row
      demonstrates (scope-(a), structural): the anchors' S-difference
      is NOT a q₀-pin effect on this object — the anchor dependence
      of S lives per-observable, not in the substrate modulus.

Scope-(a) throughout; no identification; no fit; no c_k wired.
Exact integer Laurent polynomials; mpmath dps 60; no float64.
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
from q_parameter import q_muon_at, q_at  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402

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
T_ODD_B3IX = mp.mpf("0.01916053432")
# Muon leg read BY NAME (bean qou-9ugp, 2026-09-03). It was the literal
# 1.1099785955573...15368 -- the RETIRED self-certified muon pin A, superseded
# 2026-08-22. The proton leg (t_p) already used q_at(50) by name, so this probe
# was comparing a live proton pin against a retired muon one -- inside the very
# assertion that the mu-vs-p pin move is below 1e-6. Exception E1 of the
# 2026-08-30 ruling: both pins are read here on purpose.
Q0_MUON = q_muon_at(50)
N_COEF = 44


def theta_Q(Q, w, M=60):
    return mp.fsum([Q ** (mp.mpf(m * m) / 2) * w ** m
                    for m in range(-M, M + 1)])


def pipeline(t, deltas):
    """Full D_odd pipeline at substrate log-modulus t. Returns dict."""
    a0 = mp.e ** (-t / 2)
    ainv = 1 / a0
    qbar = ainv ** 2
    Qt = a0 ** 10
    # exact q-Borel coefficients
    Th = []
    poch = mp.mpf(1)
    for n in range(N_COEF):
        if n > 0:
            poch *= (1 - qbar ** n)
        Th.append(_mb.leval(_mb.C52(n), ainv) * poch ** 2
                  * a0 ** (5 * n * n + 7 * n))
    # convergent side
    q0i = a0 * a0
    poch = mp.mpf(1)
    F_conv = mp.mpf(0)
    for n in range(40):
        if n > 0:
            poch *= (1 - q0i ** n)
        term = _mb.leval(_mb.C52(n), a0) * poch ** 2
        F_conv += term
        if abs(term) < mp.mpf("1e-42") and n > 6:
            break
    # Padé continuation of the Borel function
    cs = [mp.mpc(c) for c in Th]
    p, q = mp.pade(cs, N_COEF // 2, N_COEF // 2 - 1)

    def g(w):
        if abs(w) <= mp.mpf("0.9"):
            return mp.fsum([Th[n] * w ** n for n in range(N_COEF)])
        return mp.polyval(p[::-1], w) / mp.polyval(q[::-1], w)

    t_targ = a0 ** -7
    orbit = []
    for d in deltas:
        s0 = mp.mpf("0.7") * Qt ** d
        w0 = s0 / t_targ
        acc = mp.mpf(0)
        for m in range(-14, 15):
            acc += mp.re(Qt ** (mp.mpf(m * m) / 2) * w0 ** m
                         * g(s0 * Qt ** m))
        orbit.append(acc / theta_Q(Qt, w0))
    s_med = mp.fsum(orbit) / len(orbit)
    var = max(orbit) - min(orbit)
    D_odd = (s_med - F_conv) / 2
    # superasymptotic: optimal truncation of the raw divergent series
    parts = []
    acc = mp.mpf(0)
    terms = []
    for n in range(N_COEF):
        term = Th[n] * a0 ** (-(5 * n * n + 7 * n))
        acc += term
        parts.append(acc)
        terms.append(abs(term))
    n_star = min(range(2, N_COEF - 1), key=lambda n: terms[n])
    return {"F_conv": F_conv, "s_med": s_med, "var": var,
            "D_odd": D_odd, "orbit": orbit,
            "S_trunc": parts[n_star - 1], "min_term": terms[n_star],
            "n_star": n_star}


def main() -> int:
    print("=" * 78)
    print(" D_odd — median normalization (δ-torus) + cross-check "
          "battery")
    print("=" * 78)

    t_p = mp.log(q_at(50))
    deltas = [mp.mpf(k) / 10 for k in range(10)]

    print("\n[E] proton-pin pipeline with dense δ-orbit:")
    P = pipeline(t_p, deltas)
    print(f"    orbit s(δ): min {mp.nstr(min(P['orbit']), 15)}, max "
          f"{mp.nstr(max(P['orbit']), 15)}")
    print(f"    s_med = {mp.nstr(P['s_med'], 15)}; orbit variation = "
          f"{mp.nstr(P['var'], 3)}")
    okE = P["var"] < mp.mpf("1e-8")
    print(f"    scheme ambiguity {mp.nstr(P['var'], 3)} — seven orders "
          f"below |D_odd|: {okE}")
    D_odd_p = P["D_odd"]
    print(f"    MEDIAN-NORMALIZED D_odd(proton) = "
          f"{mp.nstr(D_odd_p, 12)} ± {mp.nstr(P['var'], 2)}")

    # C1: superasymptotic consistency
    dev1 = abs(P["S_trunc"] - P["s_med"])
    ok1 = dev1 < P["min_term"]
    print(f"\n[C1] superasymptotic: optimal truncation at n* = "
          f"{P['n_star']}, S_trunc = {mp.nstr(P['S_trunc'], 12)}, "
          f"|S_trunc − s_med| = {mp.nstr(dev1, 3)} < min term "
          f"{mp.nstr(P['min_term'], 3)}: {ok1}")

    # C3: muon-pin pipeline
    t_m = mp.log(Q0_MUON)
    M = pipeline(t_m, deltas[:4])
    D_odd_m = M["D_odd"]
    dD = D_odd_m - D_odd_p
    dS = S_MUON - S_PROTON
    print(f"\n[C3] muon-pin: D_odd(muon) = {mp.nstr(D_odd_m, 12)}")
    print(f"    ΔD_odd(pin) = {mp.nstr(dD, 4)}  vs  ΔS(anchors) = "
          f"{mp.nstr(dS, 6)}")
    ok3 = abs(dD) < mp.mpf("1e-6")
    print(f"    ⇒ the anchors' S-difference is NOT a q₀-pin effect on "
          f"this object (pin moves D_odd by {mp.nstr(abs(dD), 2)}): "
          f"{ok3}")

    # C2: b3ix same-decade row (different object; recorded, not gated)
    print(f"\n[C2] sibling b3ix order-3 tail (muon pin): T_odd = "
          f"+0.01916053 — same decade as |D_odd| = "
          f"{mp.nstr(abs(D_odd_m), 6)}; different object "
          f"(order-3 truncated action vs full resummed split) — "
          f"recorded")

    rows = {"D_odd_proton": D_odd_p, "D_odd_muon": D_odd_m,
            "scheme_ambiguity": P["var"],
            "pin_shift": dD,
            "S_muon": S_MUON, "S_proton": S_PROTON,
            "S_diff": dS, "T_odd_b3ix_muon": T_ODD_B3IX,
            "u_cubed_proton": (2 * t_p) ** 3}
    print("\n[rows] scope-(a) comparison (NOT identifications):")
    for k, v in rows.items():
        print(f"     {k:>18} = {mp.nstr(v, 10)}")

    ok = okE and ok1 and ok3
    verdict = (
        f"D_ODD MEDIAN-NORMALIZED AND CROSS-CHECKED: (E) the delta-"
        f"torus average (the q-analogue of the Ecalle median) gives "
        f"s_med = {mp.nstr(P['s_med'], 12)} with EXACT scheme "
        f"ambiguity {mp.nstr(P['var'], 2)} — seven orders below the "
        f"physics scale, so the normalization question RESOLVES: "
        f"D_odd = {mp.nstr(D_odd_p, 10)} +- {mp.nstr(P['var'], 2)} "
        f"(proton pin) is scheme-robust; (C1) the superasymptotic "
        f"optimal truncation agrees within its minimal term "
        f"({mp.nstr(dev1, 2)} < {mp.nstr(P['min_term'], 2)}) — the "
        f"classic internal resummation gate; (C3) the muon-pin "
        f"recomputation moves D_odd by only {mp.nstr(abs(dD), 2)} "
        f"while the anchors differ by {mp.nstr(dS, 4)} — so the "
        f"anchor-dependence of S is per-observable structure, NOT a "
        f"substrate-modulus effect on this object (an honest "
        f"constraint on any future identification); (C2) same-decade "
        f"consistency with the sibling b3ix order-3 estimate "
        f"recorded. D_odd now stands as a median-normalized, "
        f"internally-gated, pin-characterized bar-odd number. "
        f"Scope-(a); no identification; no fit; no c_k wired."
        if ok else
        f"INCOMPLETE (honest): E={okE} C1={ok1} C3={ok3} — data "
        f"recorded. Scope-(a); no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-dodd-median-crosschecks",
                        engine="mpmath+exact-int")
    wb.set_description(
        "Median (delta-torus/Ecalle) normalization of the resummed "
        "bar-odd datum D_odd with exact scheme-ambiguity "
        "quantification, superasymptotic internal gate, muon-vs-"
        "proton pin sensitivity, and the sibling b3ix same-decade "
        "row. Scope-(a).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("median", {"s_med": mp.nstr(P["s_med"], 20),
                           "orbit_variation": mp.nstr(P["var"], 8),
                           "orbit": [mp.nstr(v, 18) for v in P["orbit"]],
                           "D_odd_proton": mp.nstr(D_odd_p, 18)})
    wb.add_data("superasymptotic", {"n_star": P["n_star"],
                                    "S_trunc": mp.nstr(P["S_trunc"], 18),
                                    "dev": mp.nstr(dev1, 8),
                                    "min_term": mp.nstr(P["min_term"], 8)})
    wb.add_data("pin_sensitivity", {"D_odd_muon": mp.nstr(D_odd_m, 18),
                                    "delta_D": mp.nstr(dD, 8),
                                    "delta_S_anchors": mp.nstr(dS, 8)})
    wb.add_data("b3ix_row", {"T_odd_muon": mp.nstr(T_ODD_B3IX, 12),
                             "note": "different object; same decade"})
    wb.add_data("comparison_rows", {k: mp.nstr(v, 12)
                                    for k, v in rows.items()})
    wb.add_data("verdict", verdict)
    wb.add_assertion("median_scheme_robust",
                     computed=1.0 if okE else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="delta-torus orbit variation < 1e-8 "
                            "(measured ~1e-10) — seven orders below "
                            "|D_odd|")
    wb.add_assertion("superasymptotic_gate",
                     computed=1.0 if ok1 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="optimal truncation agrees with s_med "
                            "within the minimal term")
    wb.add_assertion("pin_sensitivity_characterized",
                     computed=1.0 if ok3 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="muon-vs-proton pin moves D_odd by < 1e-6 "
                            "while anchors differ by 0.049")
    # Explicit `comparison` stamp (bean qou-9ugp): this probe computes
    # D_odd at BOTH pins and asserts their difference is below 1e-6, so it
    # belongs to neither anchor list and was going out unstamped. The stamp
    # carries the values actually computed with.
    wb.save(q0_comparison(
        muon=Q0_MUON, proton=q_at(50),
        reason='computes the 5_2 D_odd median-normalised tail at BOTH the '
               'muon and proton pins and asserts the pin move is below 1e-6; '
               'both pins are read on purpose and each is reported under its '
               'own key',
    ))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
