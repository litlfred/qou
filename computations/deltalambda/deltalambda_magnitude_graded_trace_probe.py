#!/usr/bin/env python3
"""
MAGNITUDE (owner-authorised Track-A reversal for Δ_λ): the magnitude is not a
seventh weight-ansatz — it is the trace of the sign-grading, a CLASSICAL (q=1)
dimension, not the substrate q₀ quantum-dimension. Formalize-first; no fit; nothing
wired. This REDUCES the closure to one object (g_ρ); it does NOT derive g_ρ.

Prior (merged): the Δ_λ chirality SIGN is the principal (ρ) grading g_ρ evaluated at
ζ₄ (sgn(Δ_λ)=(-1)^{n(λ)}=q^{2n(λ)}|_{q=i}), NOT a knot / framing / JM / FS-twist
invariant (#3509/#3523/#3529). Since Δ_λ = sgn(w_0^{S_{λ'}})·dim(λ) and g_ρ acts on
V_λ by the scalar (-1)^{n(λ)}, we have

    Δ_λ = tr_{V_λ}(g_ρ) = (-1)^{n(λ)}·dim(λ).

So the MAGNITUDE |Δ_λ| = dim(λ) is not a separate ansatz to fit — it is the ordinary
dimension carried by the SAME object whose trace gives the sign. The six failed
ansätze (co-Casimir, Demazure, LP×2, crystal, Wenzl) were constructing Δ_λ as a direct
weight/dimension; the graded-trace form says the closure is "construct g_ρ, trace it".

Two exact structural facts (parameter-free):

  1. Δ_λ = tr(g_ρ) = (-1)^{n(λ)}·dim(λ) — magnitude = ordinary dimension = graded trace.

  2. The magnitude is the CLASSICAL (q=1) dimension, NOT the substrate q₀ quantum
     dimension: dim_q(λ; q₀) (q-hook-length [n]_q!/Π[h]_q at q₀≈1.11) differs from the
     integer dim(λ) by up to ~4.41% (e.g. [3,2]: 5.22 vs 5). So the magnitude anchor is
     q=1, the sign anchor is ζ₄ — NEITHER is the substrate q₀. Δ_λ is a two-anchor
     object (classical magnitude ⊗ ζ₄ sign).

REDUCED open problem (explicitly NOT claimed derived): construct the principal grading
g_ρ (the q^{2ρ}-type ρ-grading realizing (-1)^{n(λ)} at ζ₄, with classical q=1
dimension) as a canonical categorical morphism from the 13 drivers. Per
"Axiomatization is NOT a Proof", this reduction does NOT unlock the binding compute;
only a driver-level construction of g_ρ would. Nothing wired.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
from math import factorial

import mpmath as mp
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (_HERE, os.path.join(_ROOT, "tools", "qou-substrate", "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from t25_cinquefoil_deltalambda_sign_probe import (  # noqa: E402
    partitions, target_sign)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def n_lambda(lam):
    return sum(i * p for i, p in enumerate(lam))


def _hooks(lam):
    hs = []
    for r, rl in enumerate(lam):
        for c in range(rl):
            arm = rl - c - 1
            leg = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            hs.append(arm + leg + 1)
    return hs


def dim_ordinary(lam):
    prod = 1
    for h in _hooks(lam):
        prod *= h
    return factorial(sum(lam)) // prod


def dim_q(lam, q):
    def qint(k):
        return (q ** k - q ** (-k)) / (q - 1 / q)
    num = mp.mpf(1)
    for k in range(1, sum(lam) + 1):
        num *= qint(k)
    den = mp.mpf(1)
    for h in _hooks(lam):
        den *= qint(h)
    return num / den


def main():
    set_compute_dps()
    try:
        from qou_substrate.constants import q_at
        q0 = mp.mpf(str(q_at(30)))
        q0src = "qou_substrate.q_at(30)"
    except Exception:                                # noqa: BLE001 (substrate optional in sandbox)
        # matches the primary q_at (proton pin) for cross-environment consistency; the
        # magnitude≠q-dim result is q₀-insensitive (4.41% gap ≫ the 11.5 ppb μ–p diff).
        q0 = mp.mpf("1.1099785827513808076")
        q0src = "fallback (q_at proton pin, hardcoded high-precision)"

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # 1. Δ_λ = tr(g_ρ) = (-1)^{n(λ)}·dim(λ): magnitude = ordinary dim = graded trace.
    graded_trace_ok = all(
        target_sign(lam) * dim_ordinary(lam) ==
        int(sp.re(sp.I ** (2 * n_lambda(lam)))) * dim_ordinary(lam)
        for lam in partitions(5))
    check("delta_lambda_is_graded_trace", graded_trace_ok,
          "Δ_λ = sgn(w_0^{S_{λ'}})·dim(λ) = (q^{2n(λ)}|_{q=i})·dim(λ) = tr_{V_λ}(g_ρ) "
          "for all λ⊢6 => magnitude = ordinary dimension, NOT a separate weight ansatz")

    # 2. magnitude = CLASSICAL q=1 dim, NOT substrate q₀ quantum dimension.
    rows = []
    mag_ne_q0 = False
    max_gap = 0.0
    for lam in partitions(5):
        d = dim_ordinary(lam)
        dq = float(dim_q(lam, q0))
        gap = abs(dq - d) / d * 100 if d else 0.0
        max_gap = max(max_gap, gap)
        if gap > 1e-6:
            mag_ne_q0 = True
        rows.append({"lambda": list(lam), "dim_q1": d, "Delta_lambda": target_sign(lam) * d,
                     "dim_q_q0": dq, "gap_pct": gap})
    check("magnitude_is_classical_not_substrate_q0",
          mag_ne_q0 and max_gap > 1.0,
          f"|Δ_λ|=dim(λ) is the q=1 ordinary dim; the substrate q-dimension dim_q(q₀) "
          f"differs by up to {max_gap:.2f}% => magnitude anchor is q=1, not q₀")

    # 3. two-anchor: magnitude q=1, sign ζ₄, neither at q₀ (real, ≈1.11, not a root of unity).
    q0_not_root = abs(q0 - 1.0) > 1e-3 and q0 > 1.0    # real >1, not ζ₄
    check("two_anchor_neither_at_substrate_q0", q0_not_root,
          "magnitude anchor q=1 (classical dim) ⊗ sign anchor ζ₄ (grading); substrate "
          f"q₀={mp.nstr(q0, 7)} (real>1) is NEITHER => Δ_λ is a two-anchor object")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "MAGNITUDE REDUCED (structural; g_ρ NOT derived): Δ_λ = tr_{V_λ}(g_ρ) = "
        "(-1)^{n(λ)}·dim(λ), so the magnitude |Δ_λ|=dim(λ) is not a seventh weight-ansatz — "
        "it is the ordinary dimension carried by the SAME object whose trace gives the sign "
        "(the ρ-grading g_ρ). The magnitude is the CLASSICAL q=1 dimension, NOT the substrate "
        f"q₀ quantum dimension (dim_q(q₀) differs by up to {max_gap:.2f}%). So Δ_λ is a "
        "two-anchor object: magnitude at q=1, sign at ζ₄, NEITHER at the substrate q₀. This "
        "REDUCES the whole Δ_λ closure to constructing the single object g_ρ (the principal "
        "ρ-grading) and pruning the substrate q-dimension. It does NOT derive g_ρ from the 13 "
        "drivers — per 'Axiomatization is NOT a Proof' the binding compute stays blocked until "
        "a driver-level construction of g_ρ exists. NOTHING wired."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_HERE, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "deltalambda-magnitude-graded-trace",
        "description": "The Δ_λ magnitude is the trace of the sign-grading g_ρ (= ordinary "
                       "dimension), a classical q=1 dimension, NOT the substrate q₀ quantum "
                       "dimension. Reduces the closure to constructing g_ρ; does not derive it.",
        "auditOnly": "docs/audits/2026-07-11-deltalambda-magnitude-graded-trace.md",
        "tier": "symbolic-exact + mpmath (parameter-free; exact identities + q₀ q-dimension)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy+mpmath", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "q0_source": q0src, "q0": mp.nstr(q0, 20),
        "assertions": assertions, "allPassed": all_passed,
        "result": {"per_partition": rows, "max_q0_gap_pct": max_gap,
                   "delta_lambda_form": "tr_{V_λ}(g_ρ) = (q^{2n(λ)}|_{q=i})·dim(λ)",
                   "magnitude_anchor": "q=1 (classical dim)", "sign_anchor": "ζ₄ (grading)",
                   "verdict": verdict},
        "context": {
            "closes_sign": "computations/deltalambda/deltalambda-sign-pivotal-grading-capstone.witness.json (#3529)",
            "reduced_open_problem": "construct g_ρ (principal ρ-grading) from the 13 drivers — categorical, formalize-first, NOT done",
            "gate": "Track-A/Subgoal-2 (owner-reversed for this reduction); no fit; nothing wired",
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    # Payload carries a top-level `assertions` mapping → stamp preserves it.
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(_HERE, "deltalambda-magnitude-graded-trace.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
