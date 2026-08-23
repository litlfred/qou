#!/usr/bin/env python3
"""A5.5 (bean qou-69pr): certified N=6 categorical q*-test via the
Jones–Wenzl 5-cable on TL₁₅ — Rust engine (`tl-cable-mpfr`).

WHY. A5.2/A5.3/A5.4 (merged #3927, #4032; #4034) certified the categorical
q*-test at N = 3, 4, 5. TL₁₅ (Catalan(15) = 9 694 845 diagrams) is out of
pure-Python reach (~46× the TL₁₂ state space that already cost 6-7 min per
evaluation), so this rung runs on the Rust port of the same engine
(`tools/hecke-engine/src/tl_cable_mpfr.rs`, batch CLI `tl-cable-mpfr`, MPFR
192-bit — the full-precision sibling of main's `tl_cable` dense-f64 engine).
The port is gated here (G0) against the live Python engine at N=3 and the
committed N=4/N=5 witness values before any N=6 number is trusted.

GATES:
  G0 — Rust-vs-Python port cross-check: 5₂ raw J' at N=3 vs the live
       Python engine at 2 real q (1e-25); B₄(q*), B₅(q*) vs the committed
       witness values (1e-10, string-limited).
  G1 — N=6 framing from the writhe-±1 UNKNOT (TL₁₀, cheap): gate the
       MAGNITUDE |fr| = q^{17.5} (θ_{V₆} = q_M^{λ(λ+2)/4}, λ=5 ⇒
       q_M^{35/4} = q^{35/2}) and RECORD the sign — measured, not assumed
       (the A5.4 lesson: the sign alternates with cable width, +q⁴ at
       cN=2, −q^{7.5} at cN=3, +q^{12} at cN=4; alternation predicts
       −q^{17.5} at cN=5 but only the measurement decides).
  G2 — 4₁ N=6 (5-cable, w=0, framing-free) vs the trusted Masbaum p=−1
       tower at one real q.
  G3 — 4₁ N=6 amphichiral null at q*.
THE TEST — B₆(5₂;q) at the 3 sample points q*±2e-8 and q* (zero-framed
via fr⁴ = q^{70}, writhe 4, sign-independent): signs, |B₆(q*)|, slope,
and the 3-point + slope-bound certificate s·2h ≪ 1 (a zero inside the
window would need s·2h ≳ 1; the N ≤ 5 pattern gives s ~ 1e2 so
s·2h ~ 4e-6). auditOnly; no c_k wired; no fit.

Long-compute discipline: run with `-u` + tee; the Rust binary logs
per-job progress to stderr (forwarded).

Run: python3 -u computations/probes/qbeta_5two_n6_cable_qstar_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_n6_cable.log
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_n3_cable_arbitration_probe as c3  # noqa: E402
from qbeta_5two_n5_cable_qstar_probe import Jp  # noqa: E402
import qbeta_5two_colored_tower_barodd_qstar_probe as tower  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

BRAID_5_2 = [1, 1, 1, 2, -1, 2]
BRAID_4_1 = [1, -2, 1, -2]
Q_STAR = mp.mpf("1.10997859303152")
REPO = Path(__file__).resolve().parents[2]
BIN = REPO / "tools" / "hecke-engine" / "target" / "release" / "tl-cable-mpfr"
T0 = time.monotonic()

# committed reference values (string-limited to 12 digits)
REF_B4 = mp.mpf("-10.3376891441")   # qbeta-5two-higher-cable-qstar.witness.json
REF_B5 = mp.mpf("593.607693594")    # qbeta-5two-n5-cable-qstar.witness.json


def log(msg):
    print(f"  [{time.monotonic()-T0:7.0f}s] {msg}", flush=True)


def ensure_binary():
    if BIN.exists():
        return
    log("building tl-cable-mpfr (cargo build --release) ...")
    subprocess.run(
        ["cargo", "build", "--release", "--bin", "tl-cable-mpfr"],
        cwd=REPO / "tools" / "hecke-engine", check=True)


def run_batch(jobs, prec=192):
    """One tl-cable-mpfr subprocess per batch (engines cached inside)."""
    payload = json.dumps({"prec": prec, "jobs": jobs})
    proc = subprocess.Popen([str(BIN)], stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)
    out, err = proc.communicate(payload)
    for line in err.strip().splitlines():
        log(f"    {line}")
    if proc.returncode != 0:
        raise RuntimeError(f"tl-cable-mpfr failed rc={proc.returncode}: {err[-500:]}")
    return [mp.mpf(r["jp"].replace("e", "E"))
            for r in json.loads(out)["results"]]


def q_str(q):
    return mp.nstr(mp.mpf(q), 45)


def main() -> int:
    print("=" * 78)
    print(" A5.5 — certified N=6 categorical q*-test (JW 5-cable, TL₁₅, Rust)")
    print("=" * 78)
    ensure_binary()

    j52 = {"word": BRAID_5_2, "k": 3}
    j41 = {"word": BRAID_4_1, "k": 3}
    h = mp.mpf("2e-8")
    pts = [Q_STAR - h, Q_STAR, Q_STAR + h]

    # ---- one batch: everything (engines cached per (k, cn) in-process) ----
    jobs = []
    # G0a: N=3 port cross-check (2 jobs)
    jobs += [{**j52, "cn": 2, "q": q} for q in ("1.07", "1.11")]
    # G0b: N=4 + N=5 B(q*) vs committed witnesses (4 jobs)
    jobs += [{**j52, "cn": 3, "q": q_str(q)} for q in (Q_STAR, 1 / Q_STAR)]
    jobs += [{**j52, "cn": 4, "q": q_str(q)} for q in (Q_STAR, 1 / Q_STAR)]
    # G1: unknot framing at N=6 (2 jobs, TL₁₀)
    jobs += [{"word": [1], "k": 2, "cn": 5, "q": q} for q in ("1.11", "0.95")]
    # G2: 4₁ N=6 vs tower at one q (1 job, TL₁₅)
    jobs += [{**j41, "cn": 5, "q": "1.06"}]
    # G3: 4₁ N=6 null at q* (2 jobs, TL₁₅)
    jobs += [{**j41, "cn": 5, "q": q_str(q)} for q in (Q_STAR, 1 / Q_STAR)]
    # T: B₆(5₂) at 3 points (6 jobs, TL₁₅)
    for qq in pts:
        jobs += [{**j52, "cn": 5, "q": q_str(q)} for q in (qq, 1 / qq)]

    log(f"launching tl-cable-mpfr batch: {len(jobs)} jobs (TL₁₅ dim 9 694 845) ...")
    R = run_batch(jobs)

    # ---- G0a: N=3 vs live Python engine ----
    log("[G0a] N=3 Rust vs live Python engine ...")
    engines = {n: c3.tl_engine(n) for n in (2, 6)}
    g0a_ok = True
    for i, q in enumerate(("1.07", "1.11")):
        py = Jp(BRAID_5_2, 3, 2, mp.mpf(q), engines)
        rel = abs(R[i] - py) / abs(py)
        g0a_ok &= rel < mp.mpf("1e-25")
        log(f"    q={q}: rel = {mp.nstr(rel,3)}")
    print(f"    N=3 port cross-check at 1e-25: {'PASS' if g0a_ok else 'FAIL'}")

    # ---- G0b: B₄(q*), B₅(q*) vs committed witnesses ----
    B4 = (Q_STAR ** 30 * R[2] - Q_STAR ** -30 * R[3]) / 2
    B5 = (Q_STAR ** 48 * R[4] - Q_STAR ** -48 * R[5]) / 2
    rel4 = abs(B4 - REF_B4) / abs(REF_B4)
    rel5 = abs(B5 - REF_B5) / abs(REF_B5)
    g0b_ok = rel4 < mp.mpf("1e-10") and rel5 < mp.mpf("1e-10")
    log(f"[G0b] B₄(q*) rel = {mp.nstr(rel4,3)}, B₅(q*) rel = {mp.nstr(rel5,3)}")
    print(f"    N=4/N=5 vs committed witnesses at 1e-10: "
          f"{'PASS' if g0b_ok else 'FAIL'}")

    # ---- G0c: cross-engine gate vs the committed dense-f64 N=6 results ----
    f64_path = Path(__file__).parent / "qbeta-5two-n6-cable-qstar-rust.results.json"
    B6_f64 = mp.mpf(repr(json.load(open(f64_path))["B_qstar"]))

    # ---- G1: unknot framing at N=6 — magnitude gated, sign recorded ----
    log("[G1] unknot framing at N=6 ...")
    g1_ok = True
    fr_vals, fr_signs = {}, []
    for i, q in enumerate(("1.11", "0.95")):
        qs = mp.mpf(q)
        fr = 1 / R[6 + i]
        mag_dev = abs(abs(fr) - qs ** mp.mpf("17.5")) / qs ** mp.mpf("17.5")
        g1_ok &= mag_dev < mp.mpf("1e-18")
        fr_vals[q] = mp.nstr(fr, 12)
        fr_signs.append(int(mp.sign(fr)))
        log(f"    q={q}: fr = {mp.nstr(fr,10)}  ||fr| - q^17.5| rel = "
            f"{mp.nstr(mag_dev,3)}  sign = {int(mp.sign(fr))}")
    g1_ok &= fr_signs[0] == fr_signs[1]
    fr_sign = fr_signs[0]
    print(f"    ribbon |fr| = q^17.5 (measured sign {fr_sign:+d}): "
          f"{'PASS' if g1_ok else 'FAIL'}")

    # ---- G2: 4₁ N=6 vs trusted tower ----
    q2 = mp.mpf("1.06")
    jc = R[8]
    jt = tower.J_twist(6, -1, q2 ** 2)
    err2 = min(abs(jc - jt) / abs(jt),
               abs(jc - tower.J_twist(6, -1, q2 ** -2)) / abs(jt))
    g2_ok = err2 < mp.mpf("1e-15")
    log(f"[G2] q={q2}: cable={mp.nstr(jc,12)} tower={mp.nstr(jt,12)} "
        f"rel={mp.nstr(err2,3)}  {'PASS' if g2_ok else 'FAIL'}")

    # ---- G3: 4₁ N=6 null at q* ----
    null_rel = abs(R[9] - R[10]) / abs(R[9])
    g3_ok = null_rel < mp.mpf("1e-18")
    log(f"[G3] |B₆(4₁;q*)|/|J| = {mp.nstr(null_rel,3)}  "
        f"{'PASS' if g3_ok else 'FAIL'}")

    # ---- T: 3-point + slope-bound certificate ----
    log("[T] B₆(5₂) at the 3 sample points (fr⁴ = q^{70}, sign-independent) ...")
    Bv = []
    for i, qq in enumerate(pts):
        jp_q, jp_qi = R[11 + 2 * i], R[12 + 2 * i]
        B = (qq ** 70 * jp_q - qq ** -70 * jp_qi) / 2
        Bv.append(B)
        log(f"    point {i+1}/3 (q={mp.nstr(qq,17)}): B₆ = {mp.nstr(B,10)}")
    B_star = Bv[1]
    sc = sum(1 for x, y in zip(Bv, Bv[1:]) if mp.sign(x) != mp.sign(y))
    slope_rel = float(abs(Bv[2] - Bv[0]) / abs(B_star) / (2 * h))
    cert = slope_rel * float(2 * h)
    no_zero = sc == 0 and abs(B_star) > 0 and cert < 0.01
    print(f"\n    B₆(q*) = {mp.nstr(B_star, 10)}   signs = "
          f"{[int(mp.sign(v)) for v in Bv]}   |d ln B/dq| ≈ {slope_rel:.3e}")
    print(f"    certificate: s·2h = {cert:.3e} ≪ 1 — a zero cannot hide between "
          f"samples: {'PASS' if no_zero else 'FAIL'}")
    print(f"    ⇒ N=6 categorical face: "
          f"{'NO zero at q*, anchor-smooth — constraint (2) fails (certified)' if no_zero and slope_rel < 1e5 else 'INSPECT'}")

    wb = WitnessBuilder("qbeta-5two-n6-cable-qstar", engine="rust",
                        _script_path=__file__)
    wb.set_description(
        "A5.5 (bean qou-69pr): the certified categorical q*-test extended to "
        "N=6 via the Jones–Wenzl 5-cable on TL₁₅ (9 694 845 diagrams), "
        "computed by the Rust tl-cable-mpfr engine (hecke-engine::tl_cable_mpfr, MPFR "
        "192-bit) — the port is gated in-run against the live Python engine "
        "at N=3 (1e-25) and the committed N=4/N=5 witness values (1e-10). "
        "Gates: unknot framing magnitude = the ribbon twist q^{17.5} with "
        "the sign measured (not assumed); 4₁ 5-cable (w=0) = the trusted "
        "Masbaum p=−1 tower at N=6; 4₁ amphichiral null at q*. TEST: the "
        "3-point + slope-bound certificate — B₆(5₂) sampled at q*±2e-8 and "
        "q*, all same sign, slope·window ≪ 1 so no zero can hide between "
        "samples — capstone constraint (2) fails on the certified N=6 "
        "categorical face (scope-(a), extending N=3,4,5). auditOnly; no c_k "
        "wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("gate_rust_port_N3_vs_python",
                     computed=1.0 if g0a_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="5₂ raw J'_3: Rust tl-cable-mpfr = live Python TL engine "
                            "at 2 real q, 1e-25")
    wb.add_assertion("gate_rust_port_N4_N5_vs_witnesses",
                     computed=1.0 if g0b_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="B₄(q*), B₅(q*) = committed witness values at 1e-10 "
                            "(string-limited)")
    rel_f64 = abs(B_star - B6_f64) / abs(B6_f64)
    log(f"[G0c] B₆(q*) MPFR vs committed dense-f64: rel = {mp.nstr(rel_f64,3)}")
    wb.add_assertion("gate_cross_engine_B6_vs_dense_f64",
                     computed=float(rel_f64), expected=0.0, tolerance=1e-7,
                     source="B₆(q*) full-MPFR = main's independently-written "
                            "dense-f64 tl_cable engine within its f64 noise "
                            "floor (~1e-8; two-route convergence)")
    wb.add_assertion("gate_unknot_ribbon_framing_N6_magnitude",
                     computed=1.0 if g1_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="|fr| = q^{17.5} exactly (θ_{V₆} ribbon magnitude) "
                            "from the writhe-1 unknot at 2 q points; sign "
                            "measured and recorded, not assumed")
    wb.add_assertion("gate_41_N6_matches_trusted_tower",
                     computed=float(err2), expected=0.0, tolerance=1e-15,
                     source="4₁ 5-cable J'_6 (framing-free) = trusted p=−1 tower")
    wb.add_assertion("gate_41_N6_null_at_qstar",
                     computed=float(null_rel), expected=0.0, tolerance=1e-18,
                     source="B₆(4₁;q*) = 0 — mirror/bar control at N=6")
    wb.add_assertion("N6_no_qstar_zero_certificate",
                     computed=1.0 if no_zero else 0.0, expected=1.0, tolerance=0.5,
                     source="3-point + slope-bound certificate: same sign at "
                            "q*±2e-8 and q*, slope·window ≪ 1")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("engine", {"backend": "rust hecke-engine tl-cable",
                           "prec_bits": 192, "tl_dim": 9694845})
    wb.add_data("port_cross_check", {"B4_rel_vs_witness": mp.nstr(rel4, 3),
                                     "B5_rel_vs_witness": mp.nstr(rel5, 3)})
    wb.add_data("framing", {"fr_magnitude": "q^17.5 (theta_V6 ribbon)",
                            "fr_sign_measured": fr_sign,
                            "sign_by_cable_width": "+q^4 (cN=2), -q^7.5 (cN=3), "
                                                   "+q^12 (cN=4), measured here (cN=5)",
                            "measured": fr_vals})
    wb.add_data("qstar_test_N6", {"B_qstar": mp.nstr(B_star, 12),
                                  "B_samples": [mp.nstr(v, 12) for v in Bv],
                                  "rel_slope": f"{slope_rel:.4e}",
                                  "certificate_s2h": f"{cert:.4e}"})
    wb.add_data("verdict",
                ("CERTIFIED N=6 CATEGORICAL FACE: no q* zero (3-point + "
                 "slope-bound certificate), anchor-smooth, 4₁-null exact, "
                 "Rust port gated against Python at N=3,4,5 in-run — capstone "
                 "constraint (2) fails at N=6 (scope-(a), extending the "
                 "N=3,4,5 certifications). auditOnly."
                 if ok else "A gate failed — inspect before any claim."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s total)")
    print("  witness -> computations/probes/qbeta-5two-n6-cable-qstar.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
