#!/usr/bin/env python3
"""
Cross-isotope check (the decisive test of the block-trace magnitude): REFUTES
Δ_λ=sgn·dim_q² as the binding magnitude — it matches the deuteron (~101%) by
COINCIDENCE and blows up 40-450x for T/³He/⁴He. But the DERIVED SIGN is validated
cross-isotope (right sign for all four). Reuses previous work; no fit; nothing wired.

Setup (all pieces precomputed / validated):
  * χ^λ(β_K) per partition from computations/atom-chi-rust-{d,t,3he,4he}.witness.json
    (data/atom/by_partition; consistent Rust kernel across isotopes).
  * y_λ from wedderburn_jones_markov.y_lambda_at(n, q0) — VALIDATED to 8 digits against
    the deuteron co-casimir y_lambda_at_q0.
  * dim_q via the q-hook-length formula; sgn = (-1)^{n(λ)} (derived, #3542).
  * targets -B_AME/m_e: D 2.22452, T 8.48180, ³He 7.71804, ⁴He 28.29567 MeV.
  * B(Δ) = Σ_λ y_λ χ^λ Δ_λ.

RESULT (B(Δ)/target):
  isotope  n  dim_q²(block)  dim²(block)
  D        6  1.01           0.91
  T        9  39.4           22.5
  ³He      9  59.5           33.4
  ⁴He     12  449.6          107.7

=> the block-trace magnitude (dim_q² OR dim²) is REFUTED: it reproduces the deuteron
only by coincidence and grows ~unboundedly with A. The #3558 "block trace is the
direction / dim_q² selected by convention" lead is OVERTURNED by this cross-check —
exactly the single-isotope caveat flagged there.

WHAT SURVIVES (cross-isotope positive): all four ratios are POSITIVE (B same sign as
target<0), so the DERIVED sign sgn(w_0^{S_{λ'}})=(-1)^{n(λ)} (#3542) gives the RIGHT
sign for D/T/³He/⁴He — where the counit (rho-k-counit-isotope-systematics) had the WRONG
sign for all four. So the jet-order sign holds up cross-isotope; only the magnitude fails.

Honest status: the binding magnitude is NOT the block dimension. Back to open on the
magnitude; the SIGN is now cross-isotope-validated. Nothing wired.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
from math import factorial

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (os.path.join(_ROOT, "computations"),
           os.path.join(_ROOT, "computations", "substrate"),
           os.path.join(_ROOT, "tools", "qou-substrate", "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

B_AME_MEV = {"d": "2.22452", "t": "8.48180", "3he": "7.71804", "4he": "28.29567"}
M_E_MEV = "0.51099895000"


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


def main():
    set_compute_dps()
    from wedderburn_jones_markov import y_lambda_at
    try:
        from qou_substrate.constants import q_at
        q0 = mp.mpf(str(q_at(40)))
    except Exception:                                # noqa: BLE001 (substrate optional in sandbox)
        q0 = mp.mpf("1.1099785827513808076")

    def qint(k):
        return (q0 ** k - q0 ** (-k)) / (q0 - 1 / q0)

    def dim_q(lam):
        num = mp.mpf(1)
        for k in range(1, sum(lam) + 1):
            num *= qint(k)
        den = mp.mpf(1)
        for h in _hooks(lam):
            den *= qint(h)
        return num / den

    me = mp.mpf(M_E_MEV)
    rows = []
    for iso in ["d", "t", "3he", "4he"]:
        with open(os.path.join(_ROOT, "computations", f"atom-chi-rust-{iso}.witness.json")) as f:
            w = json.load(f)
        bp = w["data"]["atom"]["by_partition"]
        n = w["data"]["atom"]["n_strands"]
        yd = y_lambda_at(n, q0)
        tgt = -mp.mpf(B_AME_MEV[iso]) / me
        Bq = Bc = mp.mpf(0)
        for e in bp:
            lam = tuple(e["partition"])
            chi = mp.mpf(e["chi_lambda"])
            y = mp.mpf(str(yd[lam]))
            sgn = (-1) ** (n_lambda(lam) % 2)
            Bq += y * chi * sgn * dim_q(lam) ** 2
            Bc += y * chi * sgn * dim_ordinary(lam) ** 2
        rows.append({"iso": iso, "n": n, "npart": len(bp),
                     "ratio_dimq2": float(Bq / tgt), "ratio_dim2": float(Bc / tgt),
                     "right_sign": bool(float(Bq / tgt) > 0)})
        print(f"  {iso:5} n={n:>2} #λ={len(bp):>3}  B(dim_q²)/tgt={float(Bq/tgt):>10.4f}  "
              f"B(dim²)/tgt={float(Bc/tgt):>9.4f}  sign={'OK' if Bq/tgt>0 else 'WRONG'}")

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    deut = next(r for r in rows if r["iso"] == "d")
    heavier = [r for r in rows if r["iso"] != "d"]
    check("deuteron_dimq2_near_100", abs(deut["ratio_dimq2"] - 1) < 0.05,
          f"D: dim_q² -> {deut['ratio_dimq2']:.3f} (~101%, the earlier #3558 match)")
    check("block_magnitude_blows_up_for_heavier",
          all(r["ratio_dimq2"] > 5 for r in heavier),
          "T/³He/⁴He: dim_q² -> "
          + ", ".join(f"{r['iso']}:{r['ratio_dimq2']:.1f}" for r in heavier)
          + " (40-450x overshoot) => block-trace magnitude REFUTED; deuteron match coincidental")
    check("derived_sign_right_all_isotopes",
          all(r["right_sign"] for r in rows),
          "all four B same sign as target<0 => derived sign (-1)^{n(λ)} is RIGHT cross-isotope "
          "(counit systematics had WRONG sign for all four)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "REFUTED (block-trace magnitude), SIGN VALIDATED (cross-isotope): Δ_λ=sgn·dim_q² "
        f"reproduces the deuteron (~{deut['ratio_dimq2']:.2f}) only by COINCIDENCE — it blows "
        "up 40-450x for T/³He/⁴He ("
        + ", ".join(f"{r['iso']}:{r['ratio_dimq2']:.0f}x" for r in heavier)
        + "), growing ~unboundedly with A. So the block-trace magnitude (dim_q² or dim²) is NOT "
        "the binding magnitude; the #3558 'block is the direction / convention selects dim_q²' "
        "lead is OVERTURNED by this cross-check (the single-isotope caveat was right). WHAT "
        "SURVIVES: the DERIVED sign (-1)^{n(λ)} (#3542) gives the RIGHT sign for ALL FOUR "
        "isotopes (all ratios >0), where the counit had the wrong sign for all four — so the "
        "jet-order sign holds up cross-isotope; only the magnitude fails. The binding magnitude "
        "returns to OPEN; nothing wired."
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
        "computation": "deltalambda-binding-cross-isotope",
        "description": "Cross-isotope check REFUTES the block-trace magnitude Δ_λ=sgn·dim_q²: it "
                       "matches the deuteron (~101%) by coincidence and blows up 40-450x for "
                       "T/³He/⁴He. The DERIVED sign is validated cross-isotope (right sign all four). "
                       "Binding magnitude returns to open; nothing wired.",
        "auditOnly": "docs/audits/2026-07-11-deltalambda-binding-block-trace.md",
        "tier": "measurement (reuses atom-chi-rust χ + validated y_lambda_at; AME targets)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {"per_isotope": rows, "verdict": verdict},
        "context": {
            "reuses": "atom-chi-rust-{d,t,3he,4he}.witness.json (χ); wedderburn_jones_markov.y_lambda_at (validated y_λ)",
            "overturns": "the #3558 block-trace lead (dim_q² was a deuteron coincidence)",
            "survives": "the derived sign (-1)^{n(λ)} — right sign for all four isotopes (#3542)",
            "counit_predecessor": "rho-k-counit-isotope-systematics.witness.json (ratio grows with A)",
            "open": "the binding magnitude (block trace refuted) — DERIVE, do not fit; nothing wired",
        },
    }
    out = os.path.join(_HERE, "deltalambda-binding-cross-isotope.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
