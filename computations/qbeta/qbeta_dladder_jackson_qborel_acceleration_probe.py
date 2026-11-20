#!/usr/bin/env python3
"""qbeta_dladder_jackson_qborel_acceleration_probe.py

The acceleration arm of the D-ladder Jackson q-Borel / Écalle program
(audit `docs/audits/2026-07-17-dladder-qborel-acceleration.md` §3; PR #3818).
Runs AFTER the exact 2-adic transport probe (permissive invariant — the
grading obstructs nothing) and alongside the ORD-63 "more terms" sibling arm
(`qbeta_dladder_extension_singularity_probe.py`, running elsewhere): every
arm below takes an arbitrary-length exact coefficient list, so extended
`d_k` plug in unchanged.

Four arms (all scope-(a): measurement, NOT identification):

  ARM 1 — fixed-base class mismatch (structural). Within the two-parameter
    family `f_k = ([k]_Q!)^s`, the transform's log-growth is exact:
        log [k]_Q! = (log Q)·k²/2 + O(k)          (Q > 1)
        log [k]_Q! = k·log(1/(1−Q)) + O(1)-sum    (0 < Q < 1, geometric)
        log (k!)^s = s·k·log k + O(k)             (Q = 1, Leroy)
    The D-ladder grows like exp(B·k + C·k·log k) with small drifting C
    (q-Gevrey, KC22) — strictly between geometric (k) and q-factorial (k²).
    So a FIXED base Q > 1 over-accelerates (entire transform, no singularity
    to locate), a fixed base Q < 1 does not accelerate at all (divergence
    class unchanged), and only the Q → 1 Leroy boundary can match. The arm
    verifies each numerically. Honest scope: the transform-side growth is
    exact; the ladder-side divergence class is the triple-confirmed
    empirical finding — so this is a scope-(a) class-mismatch, conditional
    on the established divergence class, not a (b) exclusion.

  ARM 2 — Borel–Leroy estimator gate (the honest singularity locator).
    Fine s-scan with a PRE-REGISTERED consistency gate: a singularity is
    "resolved" only if the dlog-Padé radius, its (L,M)-spread, and the
    root-test radius agree within GATE_TOL = 15%. At k = 21 the prior probe
    found 0.156 vs 0.32 (inconsistent); this arm re-measures with the gate
    formalized and the merged conformal-mapped core (#3713) at the boundary.

  ARM 3 — parity-split acceleration. Per the 2-adic ℤ/2 grading, split
    D = D_odd + D_even (index parity; the sinh/cosh arithmetic shadow) and
    run the same gate on each sub-series in v = ũ² — the grading-motivated
    decomposition the scalar family cannot see (it is index-diagonal, so the
    split is exact and commutes with every f_k).

  ARM 4 — q-Laplace / Borel–Leroy back-transform meridian self-check.
    With the Γ(1+sk) Leroy normalization, D(ũ₀) = ∫₀^∞ e^(−t)·B(ũ₀·t^s) dt
    must reproduce the direct partial sum at the substrate meridian (where
    the series is effectively convergent — ũ₀ ≈ 0.0095 is far below the
    Borel scale). Machinery self-check (kill criterion 3 of the audit),
    plus the A2 cross-check: the resummed D is smooth through q* (the S = 0
    point), consistent with KC21's smooth-zero reading.

No `c_k` wired; no fit to QOU observables; no tier change; KC22's closed
(q-)holonomic classes are not re-run. Exact `d_k` from the ORD-43 build
(k ≤ 21) by default; pass ORD as argv[1] to consume extended ladders.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "probes"))

import json  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import fmt  # noqa: E402


def _serialise(obj):
    """Render the mpf working state to witness JSON at the LAST moment."""
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj



import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 43
core.ORD = ORD
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
dlad.ORD = ORD

import qbeta_borel_conformal_pade_probe as conf  # noqa: E402  (merged #3713 core)

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This held the RETIRED
# self-certified pin A -- retired 2026-08-22 for the CODATA-2022 derivation.
# MIGRATED TO PROTON on the owner ruling of 2026-08-30 (proton is the default;
# neither the E1 explicit-comparison nor the E2 ideal-CAL exception applies).
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 60
GATE_TOL = mp.mpf("0.15")          # pre-registered estimator-consistency gate
R3 = sp.sqrt(3)
QSTAR = mp.mpf("1.109978593031523288402328")   # anchor A2 (S=0 witness)


def d_exact():
    dk, KMAX, _vt, _ok = dlad.build_d_ladder()
    a, b = {}, {}
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        b[k] = sp.Rational(e.coeff(R3, 1))
        a[k] = sp.Rational(e - b[k] * R3)
    s3 = mp.sqrt(3)
    d = [mp.mpf(0)]
    for k in range(1, KMAX + 1):
        d.append(mp.mpf(a[k].p) / a[k].q + (mp.mpf(b[k].p) / b[k].q) * s3)
    return d, KMAX


def qfact_f(k, Q):
    f = mp.mpf(1)
    for j in range(1, k + 1):
        f *= (Q**j - 1) / (Q - 1)
    return f


def slope_tail(bser, kmax, klo=8):
    ks = list(range(klo, kmax + 1))
    rt = [abs(bser[k]) ** (mp.mpf(1) / k) for k in ks]
    mk = mp.fsum(ks) / len(ks)
    mr = mp.fsum(rt) / len(rt)
    num = mp.fsum((ks[i] - mk) * (rt[i] - mr) for i in range(len(ks)))
    den = mp.fsum((ks[i] - mk) ** 2 for i in range(len(ks)))
    return num / den, rt[-1]


def dlog_pade_radius(bser, kmax):
    """Nearest-singularity estimates of Σ b_k ζ^k over diagonal-ish (L,M):
    returns (median |ζ*|, relative spread, n_windows)."""
    F = [mp.mpf(1)] + list(bser[1:])
    n = len(F)
    fp = [F[k] * k for k in range(n)]
    g = [mp.mpf(0)] * n
    for k in range(n):
        ssum = fp[k]
        for j in range(1, k + 1):
            ssum -= F[j] * g[k - j]
        g[k] = ssum / F[0]
    mags = []
    for M in range(3, kmax // 2 + 1):
        L = min(M, kmax - M - 1)
        if L < 2:
            continue
        try:
            p, q = mp.pade(g[:L + M + 1], L, M)
            roots = mp.polyroots(list(reversed(q)), maxsteps=200, extraprec=200)
        except Exception:
            continue
        roots = [r for r in roots if abs(r) > 1e-6]
        if roots:
            mags.append(abs(min(roots, key=abs)))
    if not mags:
        return None, None, 0
    mags.sort()
    med = mags[len(mags) // 2]
    keep = [m for m in mags if abs(m - med) < 0.5 * med] or mags
    mean = mp.fsum(keep) / len(keep)
    spread = (max(keep) - min(keep)) / mean if len(keep) > 1 else mp.mpf(0)
    return mean, spread, len(keep)


def gate(rho_pade, spread, rho_root):
    """Pre-registered estimator-consistency gate."""
    if rho_pade is None or rho_root is None or rho_root <= 0:
        return False, None
    rel = abs(rho_pade - rho_root) / max(rho_pade, rho_root)
    return bool(rel <= GATE_TOL and (spread is not None and spread <= GATE_TOL)), rel


def leroy(d, kmax, s, gamma=False):
    """b_k = d_k/(k!)^s (root-test convention) or d_k/Γ(1+sk) (gamma=True,
    the back-transform-exact normalization)."""
    if gamma:
        return [mp.mpf(0)] + [d[k] / mp.gamma(1 + s * k) for k in range(1, kmax + 1)]
    return [mp.mpf(0)] + [d[k] / (mp.factorial(k) ** s) for k in range(1, kmax + 1)]


def u_of_q(qv):
    qv = mp.mpf(qv)
    return qv * (mp.sqrt(qv**4 + qv**2 + 1) / (qv**2 + 1)) * ((qv - 1) / qv) ** 2


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" D-ladder Jackson q-Borel acceleration — (Q,s) family, gate, meridian (ORD {ORD})")
    print("=" * 78)
    d, KMAX = d_exact()
    print(f"  exact d_k, k=1..{KMAX} (constant sign: Pringsheim ⇒ real-positive singularity)")

    wb = WitnessBuilder("qbeta-dladder-jackson-qborel-acceleration", engine="mpmath")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # ---------------- ARM 1: fixed-base class mismatch --------------------
    print("\n  [ARM 1] fixed-base Jackson q-Borel — class mismatch (structural):")
    arm1 = {}
    q0sub = Q_MP
    for tag, Q, s in [("substrate q0", q0sub, mp.mpf(1)),
                      ("Q=2", mp.mpf(2), mp.mpf(1)),
                      ("Q=3", mp.mpf(3), mp.mpf("0.5")),
                      ("Q=1/2", mp.mpf("0.5"), mp.mpf(1)),
                      ("Q=1/3", mp.mpf(1) / 3, mp.mpf(1))]:
        bser = [mp.mpf(0)] + [d[k] / (qfact_f(k, Q) ** s) for k in range(1, KMAX + 1)]
        sl, tail = slope_tail(bser, KMAX)
        # Q>1: log[k]_Q! = (log Q)k²/2 + O(k) exactly ⇒ transform entire; the
        # finite-k signature is a strictly NEGATIVE root-test slope (falling).
        # Q<1: [k]_Q! ~ C·A^k geometric (A = (1−Q)⁻¹-ish); dividing by A^k
        # rescales |b_k|^{1/k} (and hence its slope) by 1/A but keeps it
        # STRICTLY POSITIVE — the radius→0 divergence class is unchanged.
        regime = ("over-accel (entire; slope<0)" if Q > 1 and sl < 0 else
                  ("no accel (geometric rescale; still divergent)" if Q < 1 and sl > 0
                   else "?"))
        # `root_slope` is the sign test the `over` / `noacc` verdicts below are
        # decided on, and `tail` is inverted to a radius in arm 2. mpf here,
        # `fmt` at emission.
        arm1[tag] = {"Q": mp.nstr(Q, 8), "s": s, "root_slope": sl,
                     "tail": tail, "regime": regime}
        print(f"    {tag:12s} (s={float(s)}): slope={float(sl):+.4f} tail|b_k|^(1/k)={float(tail):.4f} → {regime}")
    sl0, tail0 = slope_tail([mp.mpf(0)] + d[1:], KMAX)
    over = all(arm1[t]["root_slope"] < 0 for t in ("substrate q0", "Q=2", "Q=3"))
    noacc = all(arm1[t]["root_slope"] > 1e-3 for t in ("Q=1/2", "Q=1/3"))
    print(f"    raw slope {float(sl0):+.4f}; Q>1 all falling (entire): {over}; "
          f"Q<1 all still divergent (class unchanged): {noacc}")
    print("    ⇒ within f_k=([k]_Q!)^s only the Q→1 (Leroy) boundary can match the")
    print("      exp(Bk+Ck·log k) class — the fixed-base Jackson transform cannot")
    print("      resolve the D-ladder singularity (scope-(a), conditional on the")
    print("      triple-confirmed divergence class; transform-side growth exact).")
    wb.add_data("arm1_fixed_base_scan", _serialise(arm1))
    wb.add_data("arm1_raw_slope", fmt(sl0))

    # ---------------- ARM 2: Leroy estimator gate -------------------------
    print(f"\n  [ARM 2] Borel–Leroy s-scan with estimator gate (tol {float(GATE_TOL):.0%}):")
    arm2 = []
    s_star = None
    best = None
    s = mp.mpf(0)
    while s <= mp.mpf("0.40") + 1e-9:
        bser = leroy(d, KMAX, s)
        sl, tail = slope_tail(bser, KMAX)
        if s_star is None and sl <= 1e-3:
            s_star = s
        rho_p, spread, nw = dlog_pade_radius(bser, KMAX)
        rho_r = 1 / tail if tail > 0 else None
        ok, rel = gate(rho_p, spread, rho_r)
        # Rows carry mpf; `_serialise` renders them at `add_data`. `float()`
        # here floored the scan's own outputs -- `gate_rel_gap` is the
        # estimator gap the gate is decided on, and `slope` is compared to
        # 1e-3 to locate s*.
        row = {"s": s, "slope": sl,
               "rho_root": rho_r if rho_r else None,
               "rho_pade": rho_p if rho_p else None,
               "pade_spread": spread if spread is not None else None,
               "gate_rel_gap": rel if rel is not None else None,
               "gate_pass": ok}
        arm2.append(row)
        if ok and (best is None or rel < best[1]):
            best = (s, rel)
        s += mp.mpf("0.02")
    for row in arm2:
        def _r(v, n):   # display only
            return round(float(v), n) if v is not None else None
        print(f"    s={float(row['s']):.2f}: slope={float(row['slope']):+.4f} "
              f"ρ_root={_r(row['rho_root'], 4)} ρ_padé={_r(row['rho_pade'], 4)} "
              f"spread={_r(row['pade_spread'], 3)} gap={_r(row['gate_rel_gap'], 3)} "
              f"gate={'PASS' if row['gate_pass'] else 'fail'}")
    gate_any = best is not None
    print(f"    s* (slope→0 crossing) ≈ {float(s_star) if s_star is not None else None}")
    print(f"    estimator gate passes anywhere: {gate_any}"
          + (f" (best s={float(best[0])}, gap {float(best[1]):.3f})" if best else ""))

    # conformal-mapped core at the s* boundary (merged #3713 machinery)
    conf_res = {}
    if s_star is not None:
        bser = leroy(d, KMAX, s_star)
        shifted = [bser[k + 1] for k in range(0, KMAX)]   # strip leading zero
        rho_p, _sp_, _nw = dlog_pade_radius(bser, KMAX)
        A0 = rho_p if rho_p else mp.mpf("0.2")
        for (L, M) in [(4, 4), (5, 5), (6, 6)]:
            r = conf.conformal_iterate(shifted, L, M, A0, mp.mpf("0.9"), use_dlog=False)
            conf_res[f"[{L}/{M}]"] = {kk: (mp.nstr(vv, 8) if isinstance(vv, mp.mpf) else
                                           (str(vv) if not isinstance(vv, (bool, int)) else vv))
                                      for kk, vv in r.items() if kk in
                                      ("converged", "A", "phase", "iters", "why")}
        conv_As = [mp.mpf(v["A"]) for v in conf_res.values()
                   if v.get("converged") and "A" in v]
        conf_spread = ((max(conv_As) - min(conv_As)) / (mp.fsum(conv_As) / len(conv_As))
                       if len(conv_As) >= 2 else None)
        print(f"    conformal-mapped core at s*={float(s_star):.2f}: "
              + "; ".join(f"{k}: A={v.get('A')} conv={v.get('converged')}" for k, v in conf_res.items()))
        conf_vs_root = None
        if conf_spread is not None:
            print(f"      window spread of converged A: {float(conf_spread):.3f}")
            A_conf = mp.fsum(conv_As) / len(conv_As)
            row_star = min(arm2, key=lambda r: abs(r["s"] - s_star))
            if row_star["rho_root"]:
                # `row_star` values are mpf now, so no re-lift through float.
                conf_vs_root = (abs(A_conf - row_star["rho_root"])
                                / max(A_conf, row_star["rho_root"]))
                print(f"      OBSERVATION (not a gate): conformal A≈{mp.nstr(A_conf, 5)} sits "
                      f"within {float(conf_vs_root):.1%} of the root-test radius "
                      f"{float(row_star['rho_root']):.4f} while raw dlog-Padé stays low "
                      f"({float(row_star['rho_pade']):.4f}) — suggestive that the raw Padé is the "
                      f"branch-cut-biased outlier; recorded for the extension arm, "
                      f"NOT promoted to a post-hoc gate.")
    wb.add_data("arm2_leroy_gate_scan", _serialise(arm2))
    wb.add_data("arm2_s_star", fmt(s_star) if s_star is not None else None)
    wb.add_data("arm2_gate_pass_anywhere", bool(gate_any))
    wb.add_data("arm2_conformal_at_s_star", conf_res)
    wb.add_data("arm2_conformal_window_spread",
                _serialise(conf_spread) if s_star is not None else None)
    wb.add_data("arm2_conformal_vs_root_gap_OBSERVATION_ONLY",
                _serialise(conf_vs_root) if s_star is not None else None)

    # ---------------- ARM 3: parity-split acceleration --------------------
    print("\n  [ARM 3] parity-split (2-adic grading decomposition), gate per branch:")
    arm3 = {}
    for tag, ks in [("odd", range(1, KMAX + 1, 2)), ("even", range(2, KMAX + 1, 2))]:
        sub = [mp.mpf(0)] + [d[k] for k in ks]          # series in v = ũ² (shifted)
        km = len(sub) - 1
        rows = []
        for sv in [mp.mpf(x) / 100 for x in range(0, 41, 5)]:
            bser = [mp.mpf(0)] + [sub[j] / (mp.factorial(j) ** sv) for j in range(1, km + 1)]
            sl, tail = slope_tail(bser, km, klo=4)
            rho_p, spread, _ = dlog_pade_radius(bser, km)
            rho_r = 1 / tail if tail > 0 else None
            ok, rel = gate(rho_p, spread, rho_r)
            rows.append({"s": sv, "slope": sl, "gate_pass": ok,
                         "rho_root": rho_r if rho_r else None,
                         "rho_pade": rho_p if rho_p else None,
                         "gate_rel_gap": rel if rel is not None else None})
        npass = sum(1 for r in rows if r["gate_pass"])
        arm3[tag] = {"n_terms": km, "rows": rows, "n_gate_pass": npass}
        print(f"    {tag:4s} branch ({km} terms): gate passes at {npass}/{len(rows)} scanned s")
    wb.add_data("arm3_parity_split", _serialise(arm3))

    # ---------------- ARM 4: back-transform meridian self-check -----------
    print("\n  [ARM 4] Borel–Leroy back-transform self-check at the meridian + A2:")
    s_bt = s_star if s_star is not None else mp.mpf("0.2")
    arm4 = {}
    for tag, qv in [("proton-q0", Q_MP), ("q_star(A2)", QSTAR)]:
        u0 = u_of_q(qv)
        direct = mp.fsum(d[k] * u0**k for k in range(1, KMAX + 1))
        bg = leroy(d, KMAX, s_bt, gamma=True)

        def Bfun(z):
            return mp.fsum(bg[k] * z**k for k in range(1, KMAX + 1))

        back = mp.quad(lambda t: mp.e**(-t) * Bfun(u0 * t**s_bt), [0, 5, 20, 60])
        rel = abs(back - direct) / abs(direct)
        arm4[tag] = {"u": mp.nstr(u0, 12), "direct_partial": mp.nstr(direct, 20),
                     "back_transform": mp.nstr(back, 20), "rel_diff": mp.nstr(rel, 4)}
        print(f"    {tag:10s}: ũ={mp.nstr(u0, 8)}  direct={mp.nstr(direct, 12)}  "
              f"back={mp.nstr(back, 12)}  rel diff={mp.nstr(rel, 3)}")
    self_check = all(mp.mpf(arm4[t]["rel_diff"]) < mp.mpf("1e-15") for t in arm4)
    dstar = mp.mpf(arm4["q_star(A2)"]["direct_partial"])
    # key follows the tag renamed at the ARM-4 loop above: that row is now
    # computed at the PROTON pin, so calling it "muon-q0" would be the very
    # label-vs-value defect this bean drains.
    dq0 = mp.mpf(arm4["proton-q0"]["direct_partial"])
    print(f"    self-check (back == direct to <1e-15): {self_check}")
    print(f"    A2: D smooth through q* — D(ũ(q*))={mp.nstr(dstar, 8)} ≈ D(ũ(q₀))={mp.nstr(dq0, 8)}")
    print("      (the S=0 zero at q* is NOT a zero of D: the sign structure lives in the")
    print("       h·D → S bridge — measured bridge datum, ord17 witness — consistent with")
    print("       KC21's smooth-zero, ladder-inversion-amplified reading)")
    wb.add_data("arm4_back_transform", _serialise({"s_used": s_bt, **arm4}))
    wb.add_data("arm4_A2_note",
                "D(ũ) smooth and nonzero through q*; the S=0 structural zero lives in "
                "the h·D→S bridge (ord17 measured ratio), not in the accelerated D — "
                "consistent with KC21 smooth-zero reading. No singularity within "
                "|ũ| ≲ ρ_Borel ≫ ũ(q*) ≈ 0.00945.")

    # ---------------- verdict --------------------------------------------
    resolved = bool(gate_any)
    verdict = (
        f"Acceleration family scan at k≤{KMAX}: (ARM1) fixed-base Jackson q-Borel "
        f"mismatches the D-ladder's exp(Bk+Ck·log k) class — Q>1 over-accelerates "
        f"(entire transform: all tails → {min(arm1[t]['tail'] for t in ('substrate q0','Q=2','Q=3')):.2g}), "
        f"Q<1 does not accelerate (class unchanged); only the Q→1 Leroy boundary "
        f"matches (scope-(a), conditional on the triple-confirmed divergence class; "
        f"transform growth exact). (ARM2) the Leroy estimator gate "
        f"{'PASSES' if gate_any else 'FAILS at every scanned s'} at k={KMAX} "
        f"(pre-registered {float(GATE_TOL):.0%} consistency)"
        + (f" — best s={best[0]}, gap {float(best[1]):.3f}" if best else
           " — the k=21 dlog-Padé/root-test inconsistency persists under the gate; "
           "singularity NOT resolved; blocked on the ORD-63 extension terms") +
        f". (ARM3) parity-split branches: gate "
        f"odd {arm3['odd']['n_gate_pass']}/{len(arm3['odd']['rows'])}, "
        f"even {arm3['even']['n_gate_pass']}/{len(arm3['even']['rows'])} — "
        f"{'some structure' if (arm3['odd']['n_gate_pass'] or arm3['even']['n_gate_pass']) else 'unresolved too'}. "
        f"(ARM4) back-transform reproduces the meridian partial sums to <1e-15 "
        f"(machinery validated); D smooth through q* (A2), the S=0 zero lives in the "
        f"h·D→S bridge. NO instanton action identified; no candidate value produced; "
        f"no c_k wired; no fit; no tier change."
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic() - t0:.1f}s)")

    wb.set_description(
        "Jackson q-Borel / Écalle acceleration of the exact bar-odd D-ladder "
        "(PR #3818; audit 2026-07-17-dladder-qborel-acceleration.md). Four arms: "
        "(1) fixed-base class mismatch — only the Q→1 Leroy boundary can match the "
        "q-Gevrey exp(Bk+Ck log k) class (Q>1 entire / Q<1 no-op; transform growth "
        "exact, ladder class empirical ⇒ scope-(a)); (2) Borel–Leroy s-scan under a "
        "pre-registered 15% estimator-consistency gate incl. the merged conformal-"
        "mapped core; (3) parity-split (2-adic grading) acceleration per branch; "
        "(4) Γ(1+sk) back-transform meridian self-check (<1e-15) + A2 q* smoothness "
        "cross-check. Measurement only: no instanton action identified, no candidate "
        "value, no c_k wired, no fit, no tier change."
    )
    wb.add_data("gate_tolerance", fmt(GATE_TOL))
    wb.add_data("singularity_resolved_at_this_k", resolved)
    wb.add_data("KMAX", KMAX)
    wb.add_data("verdict", verdict)
    wb.add_assertion("arm1_fixed_base_mismatch",
                     computed=str(int(over and noacc)), expected="1", tolerance="0.5",
                     source="Q>1 over-accelerates to an entire transform; Q<1 leaves the "
                            "divergence class unchanged; Leroy boundary is the only match")
    wb.add_assertion("arm4_back_transform_self_check",
                     computed=str(int(self_check)), expected="1", tolerance="0.5",
                     source="Borel–Leroy Γ(1+sk) back-transform equals the direct partial "
                            "sum at the meridian to <1e-15 at both anchors")
    # Was `computed=1.0, expected=1.0` named `no_identification_claimed` (bean
    # `qou-26f2`): a literal on both sides, so the probe asserted "nothing was
    # identified" without consulting `gate_any`, which it had already computed
    # and which is the only thing that decides it. Had the gate passed — an
    # identification — this would still have read PASS. Three checks replace
    # it, each of which flips the moment an identification is actually made.

    # (1) The ARM2 estimator gate, across the whole s-scan.
    n_arm2_pass = sum(1 for r in arm2 if r["gate_pass"])
    wb.add_assertion("arm2_estimator_gate_passes",
                     computed=n_arm2_pass, expected=0, tolerance=0,
                     source=f"{n_arm2_pass} of {len(arm2)} scanned Borel–Leroy "
                            f"s values clear the pre-registered "
                            f"{float(GATE_TOL):.0%} dlog-Padé / root-test "
                            f"consistency gate at k={KMAX}; "
                            f"gate_pass_anywhere={gate_any}. A pass here IS "
                            "the singularity resolution this probe declines "
                            "to claim")

    # (2) …and the ARM3 parity-split branches, scanned separately, which could
    # resolve one 2-adic grading without the other.
    n_parity_pass = arm3["odd"]["n_gate_pass"] + arm3["even"]["n_gate_pass"]
    n_parity_rows = len(arm3["odd"]["rows"]) + len(arm3["even"]["rows"])
    wb.add_assertion("parity_split_gate_passes",
                     computed=n_parity_pass, expected=0, tolerance=0,
                     source=f"odd {arm3['odd']['n_gate_pass']}/"
                            f"{len(arm3['odd']['rows'])}, even "
                            f"{arm3['even']['n_gate_pass']}/"
                            f"{len(arm3['even']['rows'])} = {n_parity_pass} of "
                            f"{n_parity_rows} graded scans clear the gate; "
                            "both branches unresolved is what makes the "
                            "negative uniform")

    # (3) The scan really reached the order the pre-registration names. Every
    # arm's verdict is stated "at k=21"; a shorter ladder would make the
    # negative cheap rather than informative.
    wb.add_assertion("dladder_order_reaches_preregistered_k",
                     computed=KMAX, expected=21, tolerance=0,
                     source=f"build_d_ladder() supplied {KMAX} exact D-ladder "
                            "terms; the docstring and every arm's verdict are "
                            "stated at k=21, and the probe reports itself "
                            "blocked on the ORD-63 extension beyond it")
    out = wb.save()
    print(f"  Witness: {out}")
    return 0 if self_check and (over and noacc) else 1


if __name__ == "__main__":
    sys.exit(main())
