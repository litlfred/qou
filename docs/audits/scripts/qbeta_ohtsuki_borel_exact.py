#!/usr/bin/env python3
"""
Sharp Borel singularity A of the 4₁ even-channel expansion — from EXACT rungs.

Track 1 of the owner-picked 1+2+3. #3628 estimated A ≈ 0.6177 from 5 noisy
numerically-extracted ratios (low-order fit, biased) and flagged "A ≈ Vol(4₁)/π
to 4.4%" as suggestive-only. The symbolic saddle recursion
(`qbeta_ohtsuki_symbolic_saddle.py`, same PR) now supplies κ_1..κ_M EXACTLY, so
the large-order analysis is noise-free and can be Richardson-accelerated
honestly.

Method. Gevrey-1 growth κ_n ~ C·Γ(n+β)/A^n gives ratios r_n = κ_{n+1}/κ_n =
(n+β)/A + O(A'/A stuff), hence FIRST DIFFERENCES Δr_n = r_{n+1} − r_n → 1/A
with O(1/n²)-type corrections — ideal for Richardson extrapolation on exact
data. β follows from β = r_n·A − n.

Candidates tested (all parameter-free): A = Vol/π, Vol/2π, 2Vol/π, 3Vol/4π,
𝔙-related multiples — plus the honest "none of the above" outcome.

DISCIPLINE: 4₁ topology; NOT wired Q_β c_k; no fit to QOU data (the Richardson
limit is an extrapolation of exact rationals, not a fit to experiment); no tier
change. Self-contained except for importing the sibling derivation module.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qbeta_ohtsuki_symbolic_saddle import derive_kappas  # noqa: E402

mp.mp.dps = 60


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
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e})") from e
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def richardson(seq):
    """Richardson table on a sequence assumed s_n = L + a/n + b/n² + …; returns
    the accelerated diagonal (last entry = best estimate)."""
    T = [list(seq)]
    k = len(seq)
    for lvl in range(1, k):
        prev = T[-1]
        nxt = []
        for i in range(len(prev) - 1):
            n = i + 1
            nxt.append(((n + lvl) * prev[i + 1] - n * prev[i]) / lvl)
        T.append(nxt)
    return [row[-1] for row in T]


def main():
    M = 12
    print(f"deriving exact rungs to κ_{M} (symbolic; may take a while) ...", flush=True)
    kappas = derive_kappas(M)
    for n in range(1, M + 1):
        print(f"  κ_{n} = {kappas[n]}", flush=True)

    kv = {n: mp.mpf(str(sp.N(kappas[n], 50))) for n in range(1, M + 1)}
    r = [kv[n + 1] / kv[n] for n in range(1, M)]          # r_1..r_{M-1}
    dr = [r[i + 1] - r[i] for i in range(len(r) - 1)]     # Δr_1..Δr_{M-2} → 1/A
    print("\n  ratios r_n:", [mp.nstr(x, 10) for x in r])
    print("  Δr_n (→1/A):", [mp.nstr(x, 10) for x in dr])

    diag = richardson(dr)
    invA = diag[-1]
    invA_prev = diag[-2] if len(diag) > 1 else invA
    A = 1 / invA
    stab = abs(1 / invA - 1 / invA_prev)
    conf = int(-mp.log10(stab)) if stab > 0 else 40
    print(f"\n  Richardson diagonal (1/A): {[mp.nstr(x, 12) for x in diag[-4:]]}")
    print(f"  A = {mp.nstr(A, 20)}   (stability {mp.nstr(stab, 3)}, ≈{conf} digits)")

    # β from the last exact ratio: β = r_n·A − n
    beta = r[-1] * A - (M - 1)
    print(f"  β = r_{M-1}·A − {M-1} = {mp.nstr(beta, 10)}")

    Vol = 2 * mp.clsin(2, mp.pi / 3)
    candidates = {
        "Vol/pi": Vol / mp.pi,
        "Vol/2pi": Vol / (2 * mp.pi),
        "2Vol/pi": 2 * Vol / mp.pi,
        "3Vol/4pi": 3 * Vol / (4 * mp.pi),
        "2Vol/3pi": 2 * Vol / (3 * mp.pi),
    }
    print("\n  candidate tests (A/candidate − 1):")
    best = None
    for name, val in candidates.items():
        rel = A / val - 1
        print(f"    {name:10s} = {mp.nstr(val, 12)}   rel dev = {mp.nstr(rel, 4)}")
        if best is None or abs(rel) < abs(best[1]):
            best = (name, rel)
    hit = abs(best[1]) < mp.mpf(10) ** (-max(4, conf - 2))
    print(f"\n  best candidate: {best[0]} (rel dev {mp.nstr(best[1], 4)}) "
          f"{'— MATCHES at attained precision' if hit else '— NOT a match at attained precision'}")

    verdict = (
        f"Borel singularity from EXACT rungs κ_1..κ_{M}: A = {mp.nstr(A, 12)} "
        f"(Richardson on exact Δr_n, ≈{conf} stable digits; β ≈ {mp.nstr(beta, 6)}). "
        + (f"A MATCHES {best[0]} = {mp.nstr(candidates[best[0]], 12)} at attained "
           f"precision (rel dev {mp.nstr(best[1], 3)}) — the resurgence action of the "
           "even channel is identified parameter-free."
           if hit else
           f"No tested parameter-free candidate matches at attained precision (best: "
           f"{best[0]}, rel dev {mp.nstr(best[1], 3)}); the #3628 'A ≈ Vol/π (4.4%)' "
           "suggestion is hereby SUPERSEDED as not exact — the true A awaits either "
           "more rungs (slow convergence) or the exact resurgence identification via "
           "the state integral.")
        + " Scope: 4₁ topology; NOT a Q_β c_k; no fit; no wiring; no tier change."
    )
    print("\nVERDICT:", verdict)

    assertions = [
        {"name": "richardson_stable_4plus_digits", "passed": bool(conf >= 4)},
        {"name": "A_positive_finite", "passed": bool(A > 0 and A < 10)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-borel-exact",
        "description": "Richardson-accelerated Borel singularity A of the 4₁ even "
                       "channel from the exact symbolic rungs κ_1..κ_12; candidate "
                       "tests vs Vol-multiples.",
        "audit_only": True,
        "tier": "symbolic-exact input, extrapolated A",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "sympy+mpmath",
        "engineVersion": f"sympy {sp.__version__}, mpmath {mp.__version__}",
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "M": M,
            "kappas_exact": {str(n): str(kappas[n]) for n in range(1, M + 1)},
            "A": mp.nstr(A, 20),
            "A_confident_digits": conf,
            "beta": mp.nstr(beta, 10),
            "candidate_devs": {k: mp.nstr(A / v - 1, 6) for k, v in candidates.items()},
            "best_candidate": best[0],
            "candidate_match": bool(hit),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: even-channel Borel singularity, exact input",
            "supersedes": "#3628 numerical A=0.6177 (5 noisy ratios)",
            "bridge_status": "open (Borel/Phi_b continuation)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-borel-exact.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
