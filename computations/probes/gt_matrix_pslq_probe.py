#!/usr/bin/env python3
"""PSLQ uniqueness probe for the Gamow--Teller axial coupling g_A.

Hypothesis: g_A = [5]_q/[4]_q · (1 + δ_GT), with δ_GT (~+3.8e-3)
admitting a clean q-arithmetic closed form parallel to
δ_CS = ℏ_q^4·[5]_q from the 1/α_EM closure.

Honest caveat: PDG g_A = 1.27510(13) is bounded to ~1e-4 relative.
PSLQ at tol ≥ 1e-4 will manufacture spurious noise relations.
A relation is a *candidate closed form* only when residual ≤ 1e-50.
Since g_A is bounded to 1e-4 EXPERIMENTALLY, no run at tol ≤ 1e-50
can succeed against the input.  Real signal lives in `ansatz_tests`:
which small-rational `a` (in g_A = R_45·(1 + a·X)) is consistent
with current CODATA, i.e. predicts the next decimal of g_A.

Output: gt-matrix-pslq-probe.witness.json
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
from q_parameter import q_at
# Centralized PDG inputs (Gemini review on PR #515): pull g_A + uncertainty
# from experimental_constants rather than hardcoding here.
from experimental_constants import G_A_PDG, G_A_PDG_ERR

DPS = 1000
# Format with up to 5 decimal places to match the original 5-figure literal,
# strip trailing zeros to keep the witness JSON readable.
PDG_G_A_STR = (f"{G_A_PDG:.6f}").rstrip("0").rstrip(".")
PDG_G_A_ERR = mp.mpf(str(G_A_PDG_ERR))


def main() -> None:
    mp.mp.dps = DPS
    q = q_at(DPS)
    qi = 1 / q
    ha = q - qi
    hbar = (q - 1) / q

    def qn(n):
        return (q ** n - q ** (-n)) / ha

    g_A = mp.mpf(PDG_G_A_STR)
    R45 = qn(5) / qn(4)
    delta = g_A / R45 - 1
    log_g_A = mp.log(g_A)
    log_R45 = mp.log(R45)

    print(f"DPS={DPS}  q_0={mp.nstr(q,20)}  hbar_q={mp.nstr(hbar,20)}")
    print(f"R_45=[5]/[4]={mp.nstr(R45,30)}")
    print(f"g_A={mp.nstr(g_A,20)}  delta_GT={mp.nstr(delta,15)}")
    print(f"|delta_GT*R45|/PDG_err={mp.nstr(abs(delta)*R45/PDG_G_A_ERR,6)}\n")

    # Borromean Markov-rep word (σ1 σ2^-1)^3 in H_3(q), standard rep
    s1 = mp.matrix([[q, 0], [1, -qi]])
    s2 = mp.matrix([[-qi, ha], [0, q]])
    s2i = s2 - ha * mp.eye(2)
    w6 = (s1 * s2i) ** 3
    tr_borr_std = w6[0, 0] + w6[1, 1]
    tr_borr_triv = (q ** 3) * ((-qi) ** 3)
    tr_borr_sign = ((-qi) ** 3) * (q ** 3)

    # Plancherel weights for λ ⊢ 3
    n_fact = qn(3) * qn(2) * qn(1)
    w_3, w_21, w_111 = 1 / n_fact, qn(2) ** 2 / n_fact, 1 / n_fact

    delta_CS = hbar ** 4 * qn(5)

    # Primary basis (log-form): targets log(g_A) = ?·log(R45)+...
    primary = [("log(g_A)", log_g_A), ("log(R_45)", log_R45),
               ("1", mp.mpf(1)), ("log(q)", mp.log(q)),
               ("log(hbar_q)", mp.log(hbar))]
    for k in (2, 3, 4, 5):
        primary.append((f"log([{k}]_q)", mp.log(qn(k))))

    # Secondary basis (linear in delta): targets delta_GT directly
    secondary = [("delta_GT", delta), ("1", mp.mpf(1))]
    for k in range(1, 11):
        secondary.append((f"q^{k}", q ** k))
        secondary.append((f"q^-{k}", q ** (-k)))
    for k in range(1, 8):
        secondary.append((f"hbar_q^{k}", hbar ** k))
    for k in range(1, 11):
        secondary.append((f"[{k}]_q", qn(k)))
    for lab, v in [("hbar_q^4*[5]_q", delta_CS),
                   ("hbar_q^4*[3]_q", hbar ** 4 * qn(3)),
                   ("hbar_q^2*[3]_q", hbar ** 2 * qn(3)),
                   ("hbar_q^2*[5]_q", hbar ** 2 * qn(5)),
                   ("tr_std_borr", tr_borr_std),
                   ("tr_triv_borr", tr_borr_triv),
                   ("w_(3)", w_3), ("w_(2,1)", w_21), ("w_(1,1,1)", w_111)]:
        secondary.append((lab, v))

    print(f"primary basis: {len(primary)}  secondary basis: {len(secondary)}\n")

    pslq_runs = []
    for tag, basis in [("primary_log", primary), ("secondary_linear", secondary)]:
        labels = [l for l, _ in basis]
        values = [v for _, v in basis]
        for tol_dps in (4, 12, 30, 50, 100):
            tol = mp.mpf(10) ** (-tol_dps)
            print(f"PSLQ [{tag}] tol=1e-{tol_dps}", end=" ... ")
            t0 = time.time()
            try:
                rel = mp.pslq(values, tol=tol, maxcoeff=10 ** 25)
                dt = time.time() - t0
                if rel is None:
                    print(f"none ({dt:.1f}s)")
                    pslq_runs.append({"basis": tag, "tol_dps": tol_dps,
                                      "relation": None, "walltime_s": dt})
                    continue
                terms = [(int(c), lab) for c, lab in zip(rel, labels) if c != 0]
                check = sum(c * v for c, v in zip(rel, values))
                target_only = (len(terms) == 1 and
                               terms[0][1] in ("log(g_A)", "delta_GT"))
                kind = ("trivial" if target_only else
                        "noise" if tol_dps <= 12 else
                        "candidate" if tol_dps >= 50 else "intermediate")
                max_c = max(abs(c) for c, _ in terms)
                print(f"{kind} maxc={max_c} resid={mp.nstr(abs(check),3)}")
                pslq_runs.append({"basis": tag, "tol_dps": tol_dps, "kind": kind,
                                  "relation_terms": terms,
                                  "max_abs_coeff": int(max_c),
                                  "verify_residual": str(abs(check)),
                                  "walltime_s": dt})
            except Exception as e:  # pylint: disable=broad-except
                print(f"EXC {e}")
                pslq_runs.append({"basis": tag, "tol_dps": tol_dps,
                                  "exception": str(e)})

    # Targeted ansätze: a = delta / X for X ∈ {q-arithmetic candidates}
    ansatz_tests = []
    for name, X in [("hbar_q^4*[3]_q", hbar ** 4 * qn(3)),
                    ("hbar_q^4*[5]_q (=delta_CS)", delta_CS),
                    ("hbar_q^2*[3]_q", hbar ** 2 * qn(3)),
                    ("hbar_q^2*[5]_q", hbar ** 2 * qn(5)),
                    ("hbar_q^2", hbar ** 2),
                    ("hbar_q^3", hbar ** 3),
                    ("hbar_q",   hbar)]:
        a = delta / X
        af = float(a)
        best = (0, 1, 0.0, float("inf"))
        for num in range(-50, 51):
            for den in range(1, 51):
                err = abs(af - num / den)
                if err < best[3]:
                    best = (num, den, num / den, err)
        ansatz_tests.append({"ansatz": f"a · {name}", "a_value": str(a),
                             "a_float": af, "nearest_rational": {
                                 "num": best[0], "den": best[1],
                                 "value": best[2], "abs_err": best[3]}})
        print(f"a·{name}: a={mp.nstr(a,12)} ~ {best[0]}/{best[1]} "
              f"(|Δ|={best[3]:.2e})")

    # CODATA-consistent: a's nearest rational fits within g_A's relative
    # precision (1e-4) AFTER amplification by X.  Equivalently:
    # |Δa·X| < PDG g_A relative err.  Keep small denom (≤30) to avoid
    # rational-density false positives.
    candidates = []
    for a in ansatz_tests:
        nr = a["nearest_rational"]
        # Recover X from a_value / a_float ratio; simpler to recompute:
        # δ_pred = (a_rational) · X; residual after clipping to rational:
        delta_pred_err = nr["abs_err"] * abs(float(delta) / a["a_float"])
        a["delta_pred_err_after_clip"] = delta_pred_err
        if (delta_pred_err < 1e-4 and abs(nr["num"]) <= 30
                and nr["den"] <= 30):
            candidates.append(a)

    out = {
        "computation": "gt-matrix-pslq-probe",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "description": (
            "PSLQ probe of g_A = [5]_q/[4]_q · (1 + δ_GT) at q=q_0. "
            "Tests whether δ_GT admits a clean q-arithmetic closed "
            "form parallel to δ_CS = ℏ_q^4·[5]_q from 1/α_EM."),
        "precision_dps": DPS,
        "inputs": {"g_A_PDG": PDG_G_A_STR, "g_A_PDG_err": str(PDG_G_A_ERR),
                   "q_0_30dp": mp.nstr(q, 30),
                   "hbar_q_30dp": mp.nstr(hbar, 30)},
        "leading_order": {
            "ansatz": "g_A = [5]_q / [4]_q",
            "R_45_30dp": mp.nstr(R45, 30),
            "delta_GT": str(delta),
            "delta_GT_R45_over_PDG_err": str(abs(delta) * R45 / PDG_G_A_ERR),
            "agreement": "0.4% (~30σ above PDG bound — falsifiable)"},
        "borromean_skein": {
            "word": "(σ_1 σ_2^{-1})^3 in H_3(q)",
            "tr_standard": str(tr_borr_std),
            "tr_trivial": str(tr_borr_triv),
            "tr_sign": str(tr_borr_sign)},
        "plancherel_weights": {"w_(3)": str(w_3), "w_(2,1)": str(w_21),
                               "w_(1,1,1)": str(w_111)},
        "ansatz_tests": ansatz_tests,
        "pslq_runs": pslq_runs,
        "candidate_closures": candidates,
        "honest_assessment": (
            "PDG g_A is bounded to ~1e-4.  PSLQ at tol ≥ 1e-4 returns "
            "spurious 'noise' relations.  No tol ≤ 1e-50 PSLQ run "
            "can succeed against an input known only to 1e-4 — it "
            "would require a future measurement at 1e-50 precision. "
            "Real signal lives in ansatz_tests: a small-rational `a` "
            "in g_A = R_45·(1 + a·X) consistent with CODATA gives a "
            "falsifiable prediction for g_A's next decimal.")}

    out_path = Path(__file__).parent / "gt-matrix-pslq-probe.witness.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"\nWitness: {out_path}\nCandidate clean closures: {len(candidates)}")
    for c in candidates:
        nr = c["nearest_rational"]
        print(f"  {c['ansatz']}: a≈{nr['num']}/{nr['den']} (|Δ|={nr['abs_err']:.2e})")


if __name__ == "__main__":
    sys.exit(main())
