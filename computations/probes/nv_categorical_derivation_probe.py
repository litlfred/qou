#!/usr/bin/env python3
"""W-2 (real): probe N_v categorical-derivation candidates.

N_v = 3 · v_weak / m_e ≈ 1,445,519 is q-independent (function of CODATA
G_F and m_e only).  The structural-derivation question is whether
N_v admits a clean closed form like `factor · q_0^L` where:
  - `factor` is a small categorical constant (group order, partition
    sum, etc.)
  - `L` is a structural Hecke-tower depth or Coxeter-length quantity

Existing candidate from `docs/audits/n-v-derivation-candidates.md`:
  N_v ≈ 120 · q_0^90  (5! · q_0^90), match to −0.58%.
  Suggested categorical meaning:
    120 = |S_5| (automorphism group of Bring's surface)
    L = 90      (Hecke-tower depth at EW scale)

This probe deepens the search:
  - Compute the exact required L = log_{q_0}(N_v / factor) for several
    factor candidates;
  - Test whether L − 90 has a clean closed form in q-rationals;
  - Test alternative `factor` candidates (group orders, partition counts,
    factorials).

Output: nv-categorical-derivation-probe.witness.json.

References:
  - docs/audits/n-v-derivation-candidates.md (Strategy 2 best fit)
  - docs/audits/2026-05-02-nv-frob-filter-conjectures.md (alt candidates)
  - hadron-half-life-verification.md (N_v role in decay rate closure)
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
from datetime import datetime, timezone
from pathlib import Path

import mpmath
mpmath.mp.dps = 100

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR, Q_MP
from experimental_constants import M_E_MEV, G_F_MEV

G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))
v_weak = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
N_v_TARGET = 3 * v_weak / m_e  # = 1,445,519.45...

q = Q_MP


def qint(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** -n) / (q - 1 / q)


def main() -> int:
    h = q - 1 / q
    print("N_v categorical-derivation probe")
    print(f"  N_v target = {mpmath.nstr(N_v_TARGET, 18)}")
    print(f"  q_0        = {mpmath.nstr(q, 25)}")
    print(f"  h := q − q⁻¹ = {mpmath.nstr(h, 12)}, h² = {mpmath.nstr(h**2, 12)}")
    print()

    # Pass 1: for each candidate `factor`, compute exact L
    print("Pass 1 — Required exponent L per candidate factor:")
    print(f"  {'factor':<30}  {'value':>10}  {'L = log_q(N_v/factor)':>22}  {'L − ⌊L⌋':>12}")
    print("  " + "-" * 80)
    factor_candidates = [
        ("3! = |S_3|",        6),
        ("4! = |S_4|",        24),
        ("5! = |S_5|",        120),       # the doc's candidate
        ("6! = |S_6|",        720),
        ("|A_5| = 60",        60),
        ("|PSL(2,7)| = 168",  168),
        ("Mathieu M_11 = 7920", 7920),
        ("[5]_q! ≈ 192.0",   qint(1)*qint(2)*qint(3)*qint(4)*qint(5)),
        ("|S_4|·5 = 120",    120),       # alias
        ("|GL(2,F_3)|=48",   48),
        ("|S_5|·[2]_q = 241.4", 120 * qint(2)),
    ]
    rows_pass1 = []
    for name, factor in factor_candidates:
        L_exact = mpmath.log(N_v_TARGET / factor) / mpmath.log(q)
        L_floor = int(mpmath.floor(L_exact))
        frac = L_exact - L_floor
        rows_pass1.append({
            "factor_name": name,
            "factor_value": (factor if isinstance(factor, int)
                             else mpmath.nstr(factor, 14)),
            "L_exact": mpmath.nstr(L_exact, 14),
            "L_floor": L_floor,
            "L_frac": mpmath.nstr(frac, 12),
        })
        fac_disp = factor if isinstance(factor, int) else mpmath.nstr(factor, 10)
        print(f"  {name:<30}  {fac_disp:>10}  {mpmath.nstr(L_exact, 16):>22}  "
              f"{mpmath.nstr(frac, 8):>12}")

    # Pass 2: focus on factor=120 (the existing best candidate); refine L
    print()
    print("Pass 2 — refine L for factor = 120 (= |S_5|):")
    L_target = mpmath.log(N_v_TARGET / 120) / mpmath.log(q)
    delta_target = L_target - 90
    print(f"  L_exact = {mpmath.nstr(L_target, 16)}")
    print(f"  δ = L − 90 = {mpmath.nstr(delta_target, 14)}  (= {float(delta_target)*100:.4f}% above 90)")
    print()
    # Candidate forms for δ — must be small (~0.056) and ideally q-symmetric
    delta_candidates = [
        ("0 (bare 120·q^90)",            mpmath.mpf(0)),
        ("h² = (q-q⁻¹)²",                h**2),
        ("h²/2",                         h**2 / 2),
        ("h³ — q-asymmetric",            h**3),
        ("h³ · 6 — q-asymmetric",        h**3 * 6),
        ("(q − 1)/2 — q-asymmetric",     (q - 1) / 2),
        ("ln(q_0)/2 — q-asymmetric",     mpmath.log(q) / 2),
        ("h²·([2]_q-2)",                 h**2 * (qint(2) - 2)),
        ("1/(2[5]_q²)",                  1 / (2 * qint(5)**2)),
        ("h⁴ · ln(q_0)",                 h**4 * mpmath.log(q)),
        ("h²·(1+h²/16)",                 h**2 * (1 + h**2/16)),
        ("h²·[2]_q/4",                   h**2 * qint(2) / 4),
    ]
    print(f"  {'δ candidate':<30}  {'δ value':>14}  {'120·q^(90+δ)':>18}  {'rel_err':>14}")
    print("  " + "-" * 85)
    rows_pass2 = []
    best = None
    for name, delta in delta_candidates:
        val = 120 * q ** (90 + delta)
        err = float((val - N_v_TARGET) / N_v_TARGET)
        rows_pass2.append({
            "delta_name": name,
            "delta_value": mpmath.nstr(delta, 10),
            "value": mpmath.nstr(val, 14),
            "rel_err": err,
        })
        print(f"  {name:<30}  {mpmath.nstr(delta, 10):>14}  "
              f"{mpmath.nstr(val, 14):>18}  {err:>+14.4e}")
        if best is None or abs(err) < abs(best["rel_err"]):
            best = rows_pass2[-1]
    print()
    print(f"Best: 120·q^(90 + {best['delta_name']}) -> {best['value']}")
    print(f"  rel_err {best['rel_err']:+.4e}")
    print()
    print("HONEST ASSESSMENT:")
    print("  - The existing 120·q^90 = 5! · q^90 candidate is suggestive (5! =")
    print("    |S_5| = automorphism group of Bring's surface; q^90 = unexplained")
    print("    Hecke-tower depth).  Match: -0.58%.")
    print("  - Adding a small categorical correction h² closes 4×: -0.13%.")
    print("    h² IS q-symmetric (good), but 'why h²?' is unexplained.")
    print("  - L = 90 itself is unexplained.  Candidates: 90 = 2·3²·5 = 5·18 =")
    print("    6·15.  No paper-side derivation in n-v-derivation-candidates.md.")
    print("  - Without categorical justification of (factor, L, δ), the closure")
    print("    is suggestive numerology, not derivation.  N_v derivation remains")
    print("    open per the audit doc.")

    out = {
        # Provenance the producer emits ITSELF (bean `1j39`). These three keys
        # were previously added DOWNSTREAM, so re-running this script silently
        # STRIPPED them from the witness — including the `scriptFile` that every
        # provenance-keyed audit uses to attribute this witness at all.
        # NOTE: the audit doc moved to `_deprecated/`; the committed witness
        # still pointed at the pre-move path, so this pointer was DANGLING.
        # Nothing checks `auditOnly` resolves. Corrected here.
        "scriptFile": Path(__file__).name,
        "engine": "python",
        "auditOnly": "fsh-guts/deprecated/docs/audits/2026-05-05-nv-categorical-impasse.md",
        "computation": "nv-categorical-derivation-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Probe for closed-form N_v ≈ factor · q_0^(90 + δ) with "
            "factor a small categorical constant and δ a clean q-rational "
            "correction.  Best fit is 120·q^(90 + h²) at -0.13% (5× better "
            "than the bare 120·q^90 at -0.58% from "
            "docs/audits/n-v-derivation-candidates.md).  Neither factor=120 "
            "nor L=90 nor δ=h² have categorical derivations; the closure is "
            "suggestive numerology pending paper-side work."
        ),
        "N_v_target": mpmath.nstr(N_v_TARGET, 25),
        "q_0": mpmath.nstr(q, 50),
        "pass1_factor_search": rows_pass1,
        "pass2_delta_refinement": rows_pass2,
        "pass2_best": best,
        "verdict": "suggestive numerology; not yet derivation",
        "open_questions": [
            "Categorical justification for factor = 120 = |S_5|",
            "Categorical justification for L = 90 (Hecke-tower depth)",
            "Categorical justification for δ = h² correction",
            "Multi-q test impossible (N_v is q-independent)",
        ],
    }
    out_path = Path(__file__).parent / "nv-categorical-derivation-probe.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=None)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print()
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
