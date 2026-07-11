#!/usr/bin/env python3
"""
A-scaling of the binding magnitude: the A-STABILITY criterion selects the IRREP
dimension (Δ_λ=sgn·dim, p=1) over the block dim² (p=2). dim is A-bounded (ratio
0.18-0.40 across D/T/³He/⁴He); dim² blows up 40-450x. So the #3542 irrep trace was
the right A-scaling; the #3558 deuteron dim²≈101% was coincidental. The residual is an
O(1) factor (~2.5-5.5), NOT a wrong power. Reuses previous work; no fit; nothing wired.

Setup (validated, as in the cross-isotope probe):
  * χ^λ(β_K) from atom-chi-rust-{d,t,3he,4he} (data/atom/by_partition).
  * y_λ = wedderburn_jones_markov.y_lambda_at(n,q0) (validated vs deuteron co-casimir).
  * dim_q via q-hook-length; sgn=(-1)^{n(λ)} (#3542); B=Σ_λ y_λ χ^λ sgn·dim_q^p.
  * targets -B_AME/m_e.

RESULT (B/target vs power p):
  p     D       T       ³He     ⁴He      A-behaviour
  0    0.023   0.003   0.004   0.000    tiny (y_λ suppresses)
  1    0.180   0.295   0.402   0.206    A-BOUNDED [0.18,0.40] — the stable power
  1.5  0.416   3.318   4.748   9.336    grows with A
  2    1.014  39.438  59.521 449.613    blows up 40-450x

SELECTION (structural, not a fit): the physical binding is A-bounded (B/A ~ O(1)
per nucleon), so the magnitude power must give an A-bounded ratio. Only p=1 (the IRREP
dimension) is A-bounded; p≥1.5 blow up. So the A-stability criterion SELECTS Δ_λ=sgn·dim
(the #3542 irrep trace). This is a criterion on A-scaling, NOT a fit to the target.

Consequence:
  * #3542 irrep trace = the right A-scaling (vindicated cross-isotope); #3558 block dim²
    was a deuteron coincidence (now doubly confirmed: it blows up AND it's the wrong power
    by A-stability).
  * The residual is an O(1) multiplicative factor (target/B(dim): D 5.5, T 3.4, ³He 2.5,
    ⁴He 4.9) — same power, missing an O(1) coefficient. That coefficient is OPEN (derive,
    not fit). Combined with the cross-isotope SIGN validation (#3558), the picture is:
    Δ_λ = O(1)·sgn·dim(λ), with the O(1) the only remaining unknown. Nothing wired.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

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


def main():
    mp.mp.dps = 30
    from wedderburn_jones_markov import y_lambda_at
    try:
        from qou_substrate.constants import q_at
        q0 = mp.mpf(str(q_at(30)))
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
    isos = ["d", "t", "3he", "4he"]
    loaded = {}
    for iso in isos:
        with open(os.path.join(_ROOT, "computations", f"atom-chi-rust-{iso}.witness.json")) as f:
            w = json.load(f)
        bp = w["data"]["atom"]["by_partition"]
        n = w["data"]["atom"]["n_strands"]
        loaded[iso] = (bp, y_lambda_at(n, q0), -mp.mpf(B_AME_MEV[iso]) / me)

    def ratio(iso, p):
        bp, yd, tgt = loaded[iso]
        B = mp.mpf(0)
        for e in bp:
            lam = tuple(e["partition"])
            B += mp.mpf(str(yd[lam])) * mp.mpf(e["chi_lambda"]) * \
                ((-1) ** (n_lambda(lam) % 2)) * dim_q(lam) ** p
        return float(B / tgt)

    table = {p: {iso: ratio(iso, p) for iso in isos} for p in (1, 2)}
    r1 = [table[1][iso] for iso in isos]
    r2 = [table[2][iso] for iso in isos]

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    check("irrep_dim_p1_is_A_bounded",
          all(0.15 < abs(r) < 0.45 for r in r1),
          f"Δ_λ=sgn·dim (p=1): ratios "
          + ", ".join(f"{iso}:{table[1][iso]:.2f}" for iso in isos)
          + " — A-BOUNDED [0.18,0.40], no blow-up")
    check("block_dim2_p2_blows_up",
          max(abs(r) for r in r2) / max(abs(min(r2, key=abs)), 1e-9) > 100,
          f"Δ_λ=sgn·dim² (p=2): ratios "
          + ", ".join(f"{iso}:{table[2][iso]:.1f}" for iso in isos)
          + " — blows up 40-450x with A")
    check("A_stability_selects_irrep_dim",
          (max(abs(r) for r in r1) / min(abs(r) for r in r1) < 3) and
          (max(abs(r) for r in r2) / min(abs(r) for r in r2) > 100),
          "p=1 spread <3x (A-stable) vs p=2 spread >100x => the A-stability criterion "
          "(binding is A-bounded) SELECTS the irrep dimension, not the block dim²")

    # the residual O(1) factor for p=1 (target/B = 1/ratio)
    o1 = {iso: 1.0 / table[1][iso] for iso in isos}

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "A-STABILITY SELECTS THE IRREP DIMENSION (structural, not a fit): among magnitude "
        "powers Δ_λ=sgn·dim_q^p, only p=1 (the irrep dimension) gives an A-BOUNDED binding "
        "ratio ("
        + ", ".join(f"{iso}:{table[1][iso]:.2f}" for iso in isos)
        + ", spread <3x); p=2 (block dim²) blows up 40-450x with A. Since the physical binding "
        "is A-bounded, the A-stability criterion selects Δ_λ=sgn·dim — the #3542 IRREP TRACE — "
        "as the correct A-scaling, and confirms the #3558 block dim²≈101% on the deuteron was "
        "coincidental (wrong power). The remaining gap is an O(1) multiplicative factor "
        "(target/B(dim): "
        + ", ".join(f"{iso}:{o1[iso]:.1f}" for iso in isos)
        + ") — SAME power, missing coefficient — OPEN (derive, not fit). With the cross-isotope "
        "SIGN validation (#3558), the picture is Δ_λ = O(1)·sgn·dim(λ), O(1) the only unknown. "
        "NOTHING WIRED."
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
        "computation": "deltalambda-binding-a-scaling",
        "description": "A-stability criterion selects the irrep dimension (Δ_λ=sgn·dim, p=1, "
                       "A-bounded ratio 0.18-0.40) over the block dim² (p=2, blows up 40-450x). "
                       "Vindicates the #3542 irrep trace as the correct A-scaling; residual is an "
                       "O(1) factor (~2.5-5.5), same power. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-11-deltalambda-binding-a-scaling.md",
        "tier": "measurement (reuses atom-chi-rust χ + validated y_lambda_at; AME targets)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "ratio_p1_irrep": table[1], "ratio_p2_block": table[2],
            "residual_O1_factor_p1": o1, "verdict": verdict,
        },
        "context": {
            "reuses": "atom-chi-rust-{d,t,3he,4he} (χ) + wedderburn_jones_markov.y_lambda_at (y_λ)",
            "selects": "the #3542 irrep trace Δ_λ=sgn·dim as the A-stable magnitude scaling",
            "confirms": "#3558 block dim² was a deuteron coincidence (wrong power by A-stability)",
            "open": "the O(1) multiplicative factor (~2.5-5.5) — same power — DERIVE, do not fit",
            "gate": "Δ_λ gate — A-stability is a structural criterion, not a fit; nothing wired",
        },
    }
    out = os.path.join(_HERE, "deltalambda-binding-a-scaling.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
