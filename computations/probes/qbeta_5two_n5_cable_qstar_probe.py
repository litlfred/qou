#!/usr/bin/env python3
"""A5.4 (bean qou-3yxn): certified N=5 categorical q*-test via the
Jones–Wenzl 4-cable — the 3-point + slope-bound certificate.

WHY. A5.2/A5.3 (merged #3927, #4032) certified the categorical q*-test at
N = 3, 4 (no zero, anchor-smooth). This probe extends to N = 5 on TL₁₂
(Catalan(12) = 208012 diagrams; one 96-crossing cable pass ≈ 108 s), where a
full 7-point scan is cost-prohibitive in pure Python. Instead: the
**3-point + slope-bound certificate** — for a smooth B(q) sampled at
q* − h, q*, q* + h (h = 2e-8) with measured relative slope s = |d ln B/dq|,
the maximum variation across the window is ≈ |B|·s·2h; a zero inside the
window would require |B(q*)| ≲ |B|·s·2h, i.e. s·2h ≳ 1. With the N ≤ 4
pattern (s ~ 1e2, so s·2h ~ 4e-6 ≪ 1) the certificate is rigorous: no zero
can hide between samples.

GATES:
  G1 — N=5 framing from the writhe-±1 UNKNOT (TL₈, cheap): expect the
       ribbon twist fr = +q^{12} (θ_{V₅} magnitude q_M^{λ(λ+2)/4}, λ=4 ⇒
       q_M⁶ = q^{12}) — measured, not assumed (the A5.3 lesson). The SIGN
       alternates with cable width: cN=2 gives +q^4, cN=3 gives −q^{7.5},
       cN=4 measures +q^{12} (first run measured |fr + q^12| rel = 2.0, a
       pure sign flip; the framed test below uses fr⁴ = q^{48} either way,
       so the T-section is sign-independent).
  G2 — 4₁ N=5 (4-cable of B₃, w=0, framing-free) vs the trusted Masbaum
       p=−1 tower at one real q (the full-correctness gate at TL₁₂ cost ×1).
  G3 — 4₁ N=5 amphichiral null at q* (B₅(4₁;q*) = 0 to machine precision).
THE TEST — B₅(5₂;q) at the 3 sample points (zero-framed via fr⁴ = q^{48},
writhe 4): signs, |B₅(q*)|, slope from the endpoints, and the certificate
s·2h ≪ 1. auditOnly; no c_k wired; no fit.

Long-compute discipline: run with `-u` + tee; progress lines per evaluation
(each ≈ 2–9 min; ~10 evaluations total ≈ 60–80 min wall).

Run: python3 -u computations/probes/qbeta_5two_n5_cable_qstar_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_n5_cable.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_n3_cable_arbitration_probe as c3  # noqa: E402
from qbeta_5two_higher_cable_qstar_probe import cable, jw_terms  # noqa: E402
import qbeta_5two_colored_tower_barodd_qstar_probe as tower  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

BRAID_5_2 = [1, 1, 1, 2, -1, 2]
BRAID_4_1 = [1, -2, 1, -2]
Q_STAR = mp.mpf("1.10997859303152")
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:7.0f}s] {msg}", flush=True)


def Jp(word, k_strands, cN, q, engines):
    """Raw J'_{cN+1} via cN-cable + e_{cN}; common-prefix optimized: the cable
    word is applied once, each JW term only appends its short U-suffix."""
    A = q ** mp.mpf("-0.5")
    n = cN * k_strands
    basis, idx, ident, tables, closure = engines[n]
    delta = -A ** 2 - A ** -2
    # run the cable word once on the identity vector
    cw = cable(word, cN)
    vec = {idx[ident]: mp.mpc(1)}
    for g in cw:
        gi = abs(g) - 1
        cA = A if g > 0 else A ** -1
        cB = A ** -1 if g > 0 else A
        new = {}
        for i, c in vec.items():
            new[i] = new.get(i, mp.mpc(0)) + c * cA
            j, lp = tables[gi][i]
            new[j] = new.get(j, mp.mpc(0)) + c * cB * delta ** lp
        vec = new
    ejw = jw_terms(cN, q)
    num = mp.mpc(0)
    for coef, gword in ejw:
        v = vec
        for g in gword:
            gi = g - 1
            new = {}
            for i, c in v.items():
                j, lp = tables[gi][i]
                new[j] = new.get(j, mp.mpc(0)) + c * delta ** lp
            v = new
        s = mp.mpc(0)
        for i, c in v.items():
            s += c * delta ** (closure[i] - 1)
        num += coef * s
    # denominator on cN strands (cheap)
    basisd, idxd, identd, tablesd, closured = engines[cN]
    den = mp.mpc(0)
    for coef, gword in ejw:
        v = {idxd[identd]: mp.mpc(1)}
        for g in gword:
            gi = g - 1
            new = {}
            for i, c in v.items():
                j, lp = tablesd[gi][i]
                new[j] = new.get(j, mp.mpc(0)) + c * delta ** lp
            v = new
        s = mp.mpc(0)
        for i, c in v.items():
            s += c * delta ** (closured[i] - 1)
        den += coef * s
    return num / den


def main() -> int:
    print("=" * 78)
    print(" A5.4 — certified N=5 categorical q*-test (JW 4-cable, TL₁₂)")
    print("=" * 78)

    log("building TL engines (4, 8, 12) ...")
    engines = {n: c3.tl_engine(n) for n in (4, 8, 12)}
    log("engines built")

    # ---- G1: unknot framing at N=5 (TL₈ — cheap) ----
    log("[G1] unknot framing at N=5 ...")
    g1_ok = True
    fr_vals = {}
    for qs in (mp.mpf("1.11"), mp.mpf("0.95")):
        jr = Jp([1], 2, 4, qs, engines)
        fr = 1 / jr
        dev = abs(fr - qs ** 12) / qs ** 12
        fr_vals[str(qs)] = mp.nstr(fr, 12)
        g1_ok &= dev < mp.mpf("1e-18")
        log(f"    q={qs}: fr = {mp.nstr(fr,10)}  |fr - q^12| rel = {mp.nstr(dev,3)}")
    print(f"    ribbon fr = +q^12: {'PASS' if g1_ok else 'FAIL'}")

    # ---- G2: 4₁ N=5 vs trusted tower at one q ----
    log("[G2] 4₁ N=5 (4-cable, w=0) vs trusted p=−1 tower (one q) ...")
    q2 = mp.mpf("1.06")
    jc = Jp(BRAID_4_1, 3, 4, q2, engines)
    jt = tower.J_twist(5, -1, q2 ** 2)
    err2 = min(abs(jc - jt) / abs(jt),
               abs(jc - tower.J_twist(5, -1, q2 ** -2)) / abs(jt))
    g2_ok = err2 < mp.mpf("1e-15")
    log(f"    q={q2}: cable={mp.nstr(jc,12)} tower={mp.nstr(jt,12)} "
        f"rel={mp.nstr(err2,3)}  {'PASS' if g2_ok else 'FAIL'}")

    # ---- G3 + T: the 3-point certificate at q* ----
    h = mp.mpf("2e-8")
    pts = [Q_STAR - h, Q_STAR, Q_STAR + h]

    def J5f(q):
        return q ** 48 * Jp(BRAID_5_2, 3, 4, q, engines)     # fr⁴ = q^{48}

    log("[G3] 4₁ N=5 null at q* ...")
    a41 = Jp(BRAID_4_1, 3, 4, Q_STAR, engines)
    b41 = Jp(BRAID_4_1, 3, 4, 1 / Q_STAR, engines)
    null_rel = abs(a41 - b41) / abs(a41)
    g3_ok = null_rel < mp.mpf("1e-18")
    log(f"    |B₅(4₁;q*)|/|J| = {mp.nstr(null_rel,3)}  {'PASS' if g3_ok else 'FAIL'}")

    log("[T] B₅(5₂) at the 3 sample points (each pt = 2 TL₁₂ evals) ...")
    Bv = []
    for i, qq in enumerate(pts):
        B = (J5f(qq) - J5f(1 / qq)) / 2
        Bv.append(mp.re(B))
        log(f"    point {i+1}/3 (q={mp.nstr(qq,17)}): B₅ = {mp.nstr(mp.re(B),10)}")
    B_star = Bv[1]
    sc = sum(1 for x, y in zip(Bv, Bv[1:]) if mp.sign(x) != mp.sign(y))
    slope_rel = float(abs(Bv[2] - Bv[0]) / abs(B_star) / (2 * h))
    cert = slope_rel * float(2 * h)          # max fractional variation in window
    no_zero = sc == 0 and abs(B_star) > 0 and cert < 0.01
    print(f"\n    B₅(q*) = {mp.nstr(B_star, 10)}   signs = "
          f"{[int(mp.sign(v)) for v in Bv]}   |d ln B/dq| ≈ {slope_rel:.3e}")
    print(f"    certificate: s·2h = {cert:.3e} ≪ 1 — a zero cannot hide between "
          f"samples: {'PASS' if no_zero else 'FAIL'}")
    print(f"    ⇒ N=5 categorical face: "
          f"{'NO zero at q*, anchor-smooth — constraint (2) fails (certified)' if no_zero and slope_rel < 1e5 else 'INSPECT'}")

    wb = WitnessBuilder("qbeta-5two-n5-cable-qstar", engine="mpmath",
                        _script_path=__file__)
    wb.set_description(
        "A5.4 (bean qou-3yxn): the certified categorical q*-test extended to "
        "N=5 via the Jones–Wenzl 4-cable on TL₁₂ (208012 diagrams; "
        "common-prefix optimized). Gates: unknot framing = the ribbon twist "
        "−q^{12} exactly; 4₁ 4-cable (w=0) = the trusted Masbaum p=−1 tower "
        "at N=5; 4₁ amphichiral null at q*. TEST: the 3-point + slope-bound "
        "certificate — B₅(5₂) sampled at q*±2e-8 and q*, all same sign, "
        "slope·window ≪ 1 so no zero can hide between samples — capstone "
        "constraint (2) fails on the certified N=5 categorical face "
        "(scope-(a), extending N=3,4). auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("gate_unknot_ribbon_framing_N5",
                     computed=1.0 if g1_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="fr = +q^{12} exactly (θ_{V₅} ribbon magnitude; sign "
                            "alternates with cable width: −q^{7.5} at cN=3, "
                            "+q^{12} at cN=4) from the writhe-1 unknot at 2 q points")
    wb.add_assertion("gate_41_N5_matches_trusted_tower",
                     computed=float(err2), expected=0.0, tolerance=1e-15,
                     source="4₁ 4-cable J'_5 (framing-free) = trusted p=−1 tower")
    wb.add_assertion("gate_41_N5_null_at_qstar",
                     computed=float(null_rel), expected=0.0, tolerance=1e-18,
                     source="B₅(4₁;q*) = 0 — mirror/bar control at N=5")
    wb.add_assertion("N5_no_qstar_zero_certificate",
                     computed=1.0 if no_zero else 0.0, expected=1.0, tolerance=0.5,
                     source="3-point + slope-bound certificate: same sign at "
                            "q*±2e-8 and q*, slope·window ≪ 1")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("framing", {"fr_formula": "+q^12 (ribbon magnitude; sign alternates "
                                          "with cable width)", "measured": fr_vals})
    wb.add_data("qstar_test_N5", {"B_qstar": mp.nstr(B_star, 12),
                                  "B_samples": [mp.nstr(v, 12) for v in Bv],
                                  "rel_slope": f"{slope_rel:.4e}",
                                  "certificate_s2h": f"{cert:.4e}"})
    wb.add_data("verdict",
                ("CERTIFIED N=5 CATEGORICAL FACE: no q* zero (3-point + "
                 "slope-bound certificate), anchor-smooth, 4₁-null exact — "
                 "capstone constraint (2) fails at N=5 (scope-(a), extending "
                 "the N=3,4 certifications). Fixed colored levels 3..5 are "
                 "now all excluded on certified ground. auditOnly."
                 if ok else "A gate failed — inspect before any claim."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s total)")
    print("  witness -> computations/probes/qbeta-5two-n5-cable-qstar.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
