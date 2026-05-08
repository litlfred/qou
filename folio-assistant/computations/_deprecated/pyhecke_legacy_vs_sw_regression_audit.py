#!/usr/bin/env python3
"""
PR #518 regression audit: legacy H_3-per-generator vs proper H_{3A}
Schur-Weyl Markov-trace path in pyhecke.

Background:

  PR #518 ("Categorical mass: full Z≤10 census + ³He gap diagnosis")
  was authored using `pyhecke.trace.markov_trace_symbolic_eval` with
  the default path it had at the time the session started.  Late in
  the session, after #518 had merged, we discovered that the function
  had been redirected on 2026-05-02 (commit afb43af4f, "P2.2a:
  redirect markov_trace_symbolic_eval to proper H_{3A} SW path").

  The legacy H_3-per-generator product diverges by 5–7 orders of
  magnitude at A ≥ 2 according to the audit
  `docs/audits/2026-05-01-p2-2a-schur-weyl-low-a.witness.json`.
  The proper $H_{3A}$ Schur-Weyl sum is the mathematically correct
  evaluation.

  The pyhecke binding the PR #518 session actually executed was the
  legacy H_3 path (the `legacy_h3=False` Schur-Weyl path was already
  the default at that point in the codebase, but a code-path issue
  in our calling site caused the legacy formula to be used — see
  the audit below for the empirical discrepancy).

What this script does:

  1. Run both paths side-by-side at the 6 base atoms.
  2. Quantify the discrepancy (orders of magnitude, isospin
     symmetry breaking on the legacy path).
  3. Time the SW path at small atoms to expose the scaling
     issue (PR #518's "²⁰⁸Pb in 40ms" benchmark used the
     buggy fast path).

Findings:

  - Legacy: T ≠ ³He (breaks isospin symmetry — this is the bug)
  - SW:     T = ³He = 8.83e-04 (preserves isospin)
  - Legacy is fast (~ms); SW is slow (5s for 4He, 24s for 6Li,
    timeout at 8Be).

Implications for PR #518:

  - The −30% ³He M-term gap diagnosis is INVALID — at correct
    tr_M values T and ³He are identical, so the M-term contribution
    is identical.  Whatever causes the empirical B(³He) = 7.72 vs
    B(T) = 8.48 difference must come from a DIFFERENT term, not
    log|tr_M|.
  - The 50% mean miss in the categorical formula vs α-cluster
    needs re-evaluation with correct tr_M.
  - The "Rust → canonical bridge: NO BRIDGE NEEDED" verdict in
    PR #518 was based on the legacy fast path benchmarks.  With
    the correct SW path, scaling is exponential and the Rust
    pipeline (or a smarter algorithm) becomes relevant again.

What still holds from PR #518:

  - The Plan H census probe (independent of pyhecke values)
  - The Higgs scalar-correction probe (independent of pyhecke)
  - The fact that pyhecke supports arbitrary (Z, N)
  - The α-cluster phenomenology and the non-categorical baseline

This audit is the first commit of a follow-up PR that will
re-run the affected probes with the correct SW path and update
the conclusions.
"""
from __future__ import annotations

import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "../../tools/pyhecke/python"))
import pyhecke  # noqa: E402

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0  # noqa: E402

# ── Module-level constants ──────────────────────────────────────────
PRECISION = 20  # mpmath dps for both legacy and SW path comparisons
TIMEOUT_HINT_SEC = 60  # informational only — actual run-time guarded externally


def timed_trace(Z, N, *, legacy_h3, precision=PRECISION):
    """Run a single Markov-trace evaluation; return (tr_M_or_None, walltime, err_or_None).

    Note: actual hard timeout is enforced by the caller / shell wrapper —
    pyhecke calls do not honor a Python-level timeout.
    """
    t0 = time.time()
    try:
        tr = pyhecke.trace.markov_trace_symbolic_eval(
            Z, N, True, 1, 1, 1, float(Q0), precision=precision, legacy_h3=legacy_h3,
        )
        return float(tr), time.time() - t0, None
    except Exception as exc:
        return None, time.time() - t0, f"{type(exc).__name__}: {exc}"


def main() -> int:
    base = Path(__file__).parent
    print("=" * 80)
    print("  PR #518 regression audit: legacy H_3 vs Schur-Weyl H_{3A}")
    print(f"  q_0 = {float(Q0):.10f}")
    print("=" * 80)

    atoms = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
             ("6Li", 3, 3), ("8Be", 4, 4)]

    rows = []
    print(f"\n  {'atom':<6} {'A':>3} {'n':>3}  {'path':<10}  {'tr_M':>14}  {'sec':>8}")
    print("  " + "-" * 60)
    for label, Z, N in atoms:
        A = Z + N
        n = 3 * A
        for legacy in (True, False):
            path = "legacy" if legacy else "SW(H_3A)"
            tr, dt, err = timed_trace(Z, N, legacy_h3=legacy)
            if err:
                print(f"  {label:<6} {A:>3} {n:>3}  {path:<10}  ERROR  {err[:30]}  {dt:>6.1f}")
                rows.append({
                    "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n,
                    "path": path, "error": err, "walltime_sec": dt,
                })
            else:
                a = abs(tr)
                print(f"  {label:<6} {A:>3} {n:>3}  {path:<10}  "
                      f"{tr:>+14.4e}  {dt:>8.2f}")
                rows.append({
                    "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n,
                    "path": path,
                    "tr_M_q0": tr,
                    "abs_tr_M": a,
                    "log_abs_tr_M": math.log(a) if a > 0 else None,
                    "walltime_sec": dt,
                })

    # Discrepancies / isospin check
    print("\n  Discrepancies (legacy / SW ratio) and isospin (T vs ³He):")
    by_atom: dict[str, dict[str, dict]] = {}
    for r in rows:
        if "error" in r:
            continue
        by_atom.setdefault(r["atom"], {})[r["path"]] = r
    for atom, paths in by_atom.items():
        if "legacy" in paths and "SW(H_3A)" in paths:
            sw_abs = paths["SW(H_3A)"]["abs_tr_M"]
            if sw_abs == 0:
                print(f"    {atom:<5}  SW trace is zero — ratio undefined")
                continue
            ratio = paths["legacy"]["abs_tr_M"] / sw_abs
            print(f"    {atom:<5}  legacy / SW = {ratio:>14.4e}  "
                  f"(orders: {math.log10(ratio):>+6.2f})")
    if "T" in by_atom and "3He" in by_atom:
        for path in ("legacy", "SW(H_3A)"):
            if path in by_atom["T"] and path in by_atom["3He"]:
                tT = by_atom["T"][path]["abs_tr_M"]
                t3 = by_atom["3He"][path]["abs_tr_M"]
                if tT == 0:
                    print(f"    Isospin on {path:<10}: |tr_T|=0 — ratio undefined")
                    continue
                ratio_t3_tT = t3 / tT
                print(f"    Isospin (T = ³He?) on {path:<10}: "
                      f"|tr_T|={tT:.4e}  |tr_3He|={t3:.4e}  "
                      f"ratio={ratio_t3_tT:.6f}  "
                      f"({'EQUAL' if abs(ratio_t3_tT - 1) < 1e-3 else 'DIFFERENT'})")

    witness = {
        "computation": "pyhecke-legacy-vs-sw-regression-audit",
        "description": (
            "Documents the discrepancy between pyhecke's legacy H_3-"
            "per-generator path and the proper H_{3A} Schur-Weyl path "
            "in markov_trace_symbolic_eval.  Establishes that PR #518's "
            "categorical mass results were based on the legacy (buggy) "
            "path — orders-of-magnitude wrong, isospin-violating.  Lists "
            "what still holds from PR #518 and what needs re-running."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commit_introducing_redirect": "afb43af4f (P2.2a, 2026-05-02)",
        "audit_witness_legacy_diverges": (
            "docs/audits/2026-05-01-p2-2a-schur-weyl-low-a.witness.json"
        ),
        "rows": rows,
        "pr_518_status": {
            "still_valid": [
                "Plan H census probe (independent of pyhecke values)",
                "Higgs scalar-correction probe (independent of pyhecke)",
                "pyhecke supports arbitrary (Z, N) — true on both paths",
                "α-cluster phenomenology and non-categorical baseline",
            ],
            "needs_rerun_with_sw_path": [
                "Markov-invariant unified mass formula on full census "
                "(the −50% miss vs α-cluster)",
                "³He gap diagnosis (the −30% gap was based on T ≠ ³He, "
                "but SW path has T = ³He — the diagnosis is invalid)",
                "Rust → canonical bridge analysis (the '²⁰⁸Pb in 40ms' "
                "benchmark used the legacy fast path; SW scales "
                "exponentially)",
            ],
        },
    }
    out = base / "pyhecke-legacy-vs-sw-regression-audit.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
