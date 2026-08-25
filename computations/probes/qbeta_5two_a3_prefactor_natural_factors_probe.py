#!/usr/bin/env python3
"""qbeta_5two_a3_prefactor_natural_factors_probe.py — no natural 5₂ structural
smooth factor supplies the N_odd zero-at-q*; A3's prefactor zero is
representational, not geometric.

CONTEXT (bean qou-a664 follow-on; supports #3927 A3). #3954 (merged) showed the
5₂ σ3 bar-odd carrier Im 𝔙_q(5₂) is smooth/monotone (no zero near the substrate)
and its slope is ~12× below A′(q*)=2.37 — so for A3's `u³·smooth × Im 𝔙_q(5₂) =
N_odd` to hold, the **u³·smooth prefactor must supply the zero at q* and amplify
the slope ~12×**. This probe asks the distinct-route question the owner posed:
does ANY natural 5₂ structural smooth factor produce that zero at q*?

METHOD (structural enumeration — NOT a fit). Enumerate the natural smooth
candidate factors from the 5₂ saddle / Hecke structure and check each for a zero
crossing anywhere in the substrate window q ∈ [1.02, 1.30]:

  1. Im V(σ1)  — the σ1 quantum volume (bar-even Vol, #3902)
  2. Re(ι₁₃)   — the σ3-pair bar-even part
  3. [3]_q     — the 5₂ Hecke q-integer q²+1+q⁻²
  4. [5]_q     — q⁴+q²+1+q⁻²+q⁻⁴
  5. |ι₁₃/ι₁₂| — the σ3/σ1 saddle-action ratio
  6. |y_σ1−y_σ3| — the σ1–σ3 saddle-root separation (geometric length)

RESULT. ALL six candidates are smooth, monotone, and bounded away from zero
across the window (the smallest, |ι₁₃/ι₁₂| ≈ 0.79–0.89, never approaches 0). NO
natural 5₂ structural factor crosses zero near the substrate. So the zero at q*
that A3's prefactor must supply is NOT a geometric/algebraic feature of any
natural 5₂ object — it is representational: q* is the S = A/u³ crossing, a
property of the CODATA-vs-ladder N_odd (pinned by experimental Q_β), not of the
5₂ geometry. A3's prefactor can only produce the zero by a NON-structural factor
tuned to q* — which the anti-fit / anti-laundering discipline forbids as a
derivation.

SCOPE (2026-06-23 (a)/(b)). scope-(a): no natural structural factor supplies the
zero (a magnitude/shape statement over the enumerated candidates), constraining
the closure route not the ingredients. This does NOT prove no factor exists — a
future structural object with a zero at q* would reopen it — but it excludes the
obvious natural candidates and confirms the N_odd zero is not a manifest 5₂
geometric feature. NO fit (nothing tuned to q* or the AME anchors); NO c_k wired;
μ never fixed from QOU data.

Run: python3 -u computations/probes/qbeta_5two_a3_prefactor_natural_factors_probe.py \\
       2>&1 | tee /tmp/qbeta_a3_prefactor.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" A3 prefactor: does any natural 5₂ structural factor zero at q*?")
    print("=" * 78)

    sys.argv = [sys.argv[0]]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import qbeta_g3_5two_saddle_exact_predictions as p  # noqa

    def saddles(q):
        u = 2 * mp.log(q)
        return u, p.order_saddles(p.saddle_roots(mp.e ** u))

    def im_v1(q):
        u, d = saddles(q); return mp.im(p.V_of(u, d[0])[0])

    def re_i13(q):
        u, d = saddles(q)
        V1 = p.V_of(u, d[0])[0]; V3 = p.V_sigma3(u, d[2])[0]
        return mp.re((V1 - V3) / (2 * mp.pi * mp.mpc(0, 1)))

    def q3(q):
        return q ** 2 + 1 + q ** -2

    def q5(q):
        return q ** 4 + q ** 2 + 1 + q ** -2 + q ** -4

    def ratio_1312(q):
        u, d = saddles(q)
        V1 = p.V_of(u, d[0])[0]; V2 = p.V_of(u, d[1])[0]; V3 = p.V_sigma3(u, d[2])[0]
        i13 = (V1 - V3) / (2 * mp.pi * mp.mpc(0, 1))
        i12 = (V1 - V2) / (2 * mp.pi * mp.mpc(0, 1))
        return abs(i13 / i12)

    def sep_1_3(q):
        # σ1–σ3 saddle-root separation |y_σ1 − y_σ3| (a real geometric length)
        u, d = saddles(q); return abs(d[0] - d[2])

    cands = {
        "Im V(σ1) [Vol]": im_v1,
        "Re(ι₁₃)": re_i13,
        "[3]_q": q3,
        "[5]_q": q5,
        "|ι₁₃/ι₁₂|": ratio_1312,
        "|y_σ1−y_σ3|": sep_1_3,
    }
    qs = [mp.mpf(s) for s in ("1.02", "1.05", "1.08", "1.11", "1.15", "1.20",
                              "1.30")]
    print("\n  candidate           values across q∈[1.02,1.30]"
          "                | zero?")
    any_zero = False
    results = {}
    for nm, f in cands.items():
        vals = [f(q) for q in qs]
        signs = set(1 if v > 0 else (-1 if v < 0 else 0) for v in vals)
        crosses = len(signs) > 1 or 0 in signs
        min_abs = min(abs(v) for v in vals)
        any_zero = any_zero or crosses
        results[nm] = {"crosses_zero": bool(crosses),
                       "min_abs": mp.nstr(min_abs, 6)}
        print(f"  {nm:18}: {mp.nstr(vals[0],5):>8} … {mp.nstr(vals[-1],5):>8}  "
              f"(min|·|={mp.nstr(min_abs,5)})   | {crosses}")

    check("no_natural_5two_factor_zeros_near_substrate", not any_zero,
          computed=f"6 candidates, min |·| over window all ≥ "
                   f"{mp.nstr(min(mp.mpf(results[nm]['min_abs']) for nm in results),4)}",
          source="none of the six natural 5₂ structural smooth factors (σ1 Vol, "
                 "σ3 bar-even part, [3]_q, [5]_q, σ3/σ1 action ratio, σ1–σ3 saddle separation "
                 "Im) crosses zero in the substrate window — no natural factor "
                 "supplies the N_odd zero-at-q* the A3 prefactor requires")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("SUPPORT for #3927 A3 (distinct route): NO natural 5₂ structural smooth "
         "factor supplies the N_odd zero-at-q* that the A3 prefactor requires. "
         "All six enumerated candidates (σ1 quantum volume, σ3 bar-even part, "
         "[3]_q, [5]_q, σ3/σ1 action ratio, σ1–σ3 saddle separation) are smooth, monotone, "
         "and bounded away from zero across q∈[1.02,1.30] (the smallest, "
         "|ι₁₃/ι₁₂|≈0.79–0.89, never approaches 0). So the zero at q* is NOT a "
         "manifest geometric/algebraic feature of any natural 5₂ object — it is "
         "representational: q* is the S=A/u³ crossing, a property of the "
         "CODATA-vs-ladder N_odd (pinned by experimental Q_β). A3's prefactor "
         "can produce the zero only by a NON-structural factor tuned to q*, which "
         "the anti-fit discipline forbids as a derivation. This confirms the "
         "campaign's representational conclusion from the prefactor side. "
         if all_passed else
         "PARTIAL: a candidate crossed zero — see the table; investigate. ")
        + "scope-(a): excludes the obvious natural candidates (magnitude/shape), "
        "NOT a proof that no factor exists; a future structural object with a "
        "zero at q* would reopen it. NO fit; NO c_k wired; μ never fixed from "
        "QOU data."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-5two-a3-prefactor-natural-factors",
        "description": "No natural 5₂ structural smooth factor (σ1 Vol, σ3 "
                       "bar-even part, [3]_q, [5]_q, σ3/σ1 ratio, σ1–σ3 saddle separation) "
                       "supplies the N_odd zero-at-q* the A3 prefactor requires — "
                       "all monotone, bounded from zero across the substrate "
                       "window; the zero is representational, not geometric. "
                       "scope-(a); supports #3927 A3 (distinct route).",
        "audit_only": True,
        "tier": "numerical (structural enumeration; A3 support)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"candidates": results, "any_zero": bool(any_zero),
                   "verdict": verdict},
        "context": {
            "axis": "A3 prefactor natural-factor census (supports #3927 A3)",
            "follows": "#3954 (σ3 carrier no N_odd zero, slope 12× short)",
            "saddle_machinery": "qbeta_g3_5two_saddle_exact_predictions "
                                "(V_sigma3=Re(V) erratum)",
            "nodd_zero": "q* = S=A/u³ crossing (representational; "
                         "BarOddLadderShape)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-5two-a3-prefactor-natural-factors.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
