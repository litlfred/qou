#!/usr/bin/env python3
"""Phase-2 driver: multi-prime CRT lift of the Borromean diagonal
recurrence to Z[q^{±1}], with exact symbolic verification (bean n920;
follow-up to PR #3443's existence certificate + degree scoping).

Pipeline:
  1. Run the Rust sampler (tools/borromean-recurrence-crt) at k distinct
     ~61-bit primes.  Each run emits, per matrix column c of the unique
     (r, W) = (6, 11) window, the minimal-degree rational function
     P_c(q)/Q_c(q) over F_p with the CANONICAL normalization (leading
     coefficient of Q_c = 1) — so the residues across primes describe
     the SAME rational number per polynomial coefficient.
  2. CRT each coefficient across the primes; Wang-rational-reconstruct
     against the combined modulus.  Adaptively add primes until every
     coefficient of every column lifts and the lift validates.
  3. Assemble the operator sum_i a_i(q, m) J_{B,n+i} = b(q, m) in sympy
     and run the CLAIM-BEARING step: exact symbolic annihilation against
     the verified Habiro tower (habiro_borromean_colored_jones), for
     n = 1..NVER, symbolic in q.  (The modular fits are heuristics; only
     this step certifies the operator.)
  4. q -> 1 specialization of the homogeneous part under m -> M^2 — the
     candidate diagonal Borromean A-polynomial.
  5. Witness JSON with full provenance; the operator serialized.

Audit-only; no wiring.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction
from math import isqrt
from pathlib import Path

R_ORD = 6
W_WIN = 11
NBLK = 2 * W_WIN + 1
NCOLS = (R_ORD + 2) * NBLK
BIN = Path(__file__).parent.parent / "tools/borromean-recurrence-crt/target/release/borromean-recurrence-crt"
MAX_PRIMES = 24
NVER = 14


def gen_primes(k: int) -> list[int]:
    from sympy import nextprime
    ps, x = [], (1 << 61) - 1
    ps.append(x)  # Mersenne
    while len(ps) < k:
        x = int(nextprime(x + 10**9))
        ps.append(x)
    return ps


def run_prime(p: int, degrees: list[int] | None, log) -> dict:
    cmd = [str(BIN), str(p)]
    if degrees is not None:
        cmd += ["--degrees", ",".join(map(str, degrees))]
    t = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"sampler failed at p={p}: {r.stderr[-500:]}")
    print(f"  [prime] p={p} done in {time.time()-t:.0f}s", flush=True)
    log.append({"prime": str(p), "seconds": round(time.time() - t, 1)})
    return json.loads(r.stdout)


def crt_pair(a1: int, m1: int, a2: int, m2: int) -> tuple[int, int]:
    from sympy import mod_inverse
    m = m1 * m2
    x = (a1 + m1 * ((a2 - a1) * mod_inverse(m1 % m2, m2) % m2)) % m
    return x, m


def ratrec(a: int, m: int) -> Fraction | None:
    a %= m
    if a == 0:
        return Fraction(0)
    bound = isqrt(m // 2)
    r0, r1, t0, t1 = m, a, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    if t1 == 0 or abs(t1) > bound:
        return None
    return Fraction(r1, t1)


def main() -> int:
    t0 = time.time()
    print("\n  Borromean recurrence phase 2 — multi-prime CRT lift (Rust sampler)\n")
    primes = gen_primes(MAX_PRIMES)
    runlog: list = []

    # prime 0 with bisection (or reuse a cached run passed as argv[1])
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        data0 = json.loads(Path(sys.argv[1]).read_text())
        print(f"  [prime] p={data0['prime']} loaded from cache {sys.argv[1]}")
        assert int(data0["prime"]) == primes[0]
    else:
        data0 = run_prime(primes[0], None, runlog)
    degrees = data0["degrees"]
    print(f"  degrees: min {min(degrees)} max {max(degrees)} "
          f"median {sorted(degrees)[len(degrees)//2]}")

    # residue store: per column, per P/Q, per coeff index -> (value, modulus)
    runs = [data0]

    def try_lift() -> dict | None:
        """CRT + Wang across current runs; None if any coefficient fails."""
        lifted = {}
        for c in range(NCOLS):
            Pf, Qf = [], []
            npc = len(runs[0]["columns"][c]["P"])
            nqc = len(runs[0]["columns"][c]["Q"])
            for kind, ncoef, out in (("P", npc, Pf), ("Q", nqc, Qf)):
                for i in range(ncoef):
                    a, m = 0, 1
                    for run in runs:
                        a, m = crt_pair(a, m, run["columns"][c][kind][i],
                                        int(run["prime"])) if m > 1 else (
                            run["columns"][c][kind][i], int(run["prime"]))
                    fr = ratrec(a, m)
                    if fr is None:
                        return None
                    out.append(fr)
            lifted[c] = (Pf, Qf)
        return lifted

    lifted = try_lift()
    k = 1
    while lifted is None and k < MAX_PRIMES:
        runs.append(run_prime(primes[k], degrees, runlog))
        k += 1
        lifted = try_lift()
        print(f"  [lift] after {k} primes: "
              f"{'SUCCESS' if lifted is not None else 'incomplete'}", flush=True)
    if lifted is None:
        print(f"  LIFT FAILED after {MAX_PRIMES} primes — record and stop")
        verdict = {"lifted": False, "primes_used": MAX_PRIMES}
        verified = False
    else:
        print(f"  [lift] all {NCOLS} columns lifted with {len(runs)} prime(s)"
              f"  ({time.time()-t0:.0f}s)")
        # ── assemble + exact symbolic verification ─────────────────────
        import sympy as sp
        sys.path.insert(0, str(Path(__file__).parent))
        from habiro_borromean_colored_jones import habiro_borromean, s as ssym

        qsym = sp.symbols("q")
        entry = {}
        for c, (Pf, Qf) in lifted.items():
            num = sum(sp.Rational(f) * qsym**i for i, f in enumerate(Pf))
            den = sum(sp.Rational(f) * qsym**i for i, f in enumerate(Qf))
            entry[c] = sp.cancel(num / den) if den != 0 else sp.Integer(0)

        def coeff(i, k_):
            return entry[i * NBLK + (k_ + W_WIN)]

        def rhs_coeff(k_):
            return entry[(R_ORD + 1) * NBLK + (k_ + W_WIN)]

        Jsym = {n: habiro_borromean(n) for n in range(1, NVER + R_ORD + 1)}
        verified = True
        for n in range(1, NVER + 1):
            msym = ssym ** (2 * n)
            lhs = sp.Integer(0)
            for i in range(R_ORD + 1):
                ai = sum(coeff(i, k_) * msym**k_
                         for k_ in range(-W_WIN, W_WIN + 1))
                lhs += ai * Jsym[n + i]
            rhs = sum(rhs_coeff(k_) * msym**k_
                      for k_ in range(-W_WIN, W_WIN + 1))
            diff = sp.cancel(sp.together((lhs - rhs).subs(qsym, ssym**2)))
            zero = diff.equals(0) or sp.simplify(diff) == 0
            print(f"  [verify] n={n}: exact symbolic annihilation? {zero}"
                  f"  ({time.time()-t0:.0f}s)", flush=True)
            if not zero:
                verified = False
                break

        verdict = {"lifted": True, "primes_used": len(runs),
                   "verified_exact_symbolic": bool(verified),
                   "verify_range": f"n=1..{NVER}"}
        if verified:
            M, L = sp.symbols("M L")
            Apoly, degen = sp.Integer(0), False
            for i in range(R_ORD + 1):
                ai1 = sp.Integer(0)
                for k_ in range(-W_WIN, W_WIN + 1):
                    e = coeff(i, k_)
                    lim = sp.limit(e, qsym, 1)
                    if lim.has(sp.zoo) or lim.has(sp.oo):
                        degen = True
                        break
                    ai1 += lim * M ** (2 * k_)
                if degen:
                    break
                Apoly += sp.cancel(ai1) * L**i
            verdict["q_to_1_diagonal_A_candidate"] = (
                "DEGENERATE (pole at q=1 under this normalization)"
                if degen else str(sp.factor(sp.cancel(sp.together(Apoly)))))
            if not degen:
                print(f"\n  [q->1] candidate diagonal A-polynomial:\n"
                      f"    {verdict['q_to_1_diagonal_A_candidate']}")
            op = {
                f"a_{i}": {str(k_): str(coeff(i, k_))
                           for k_ in range(-W_WIN, W_WIN + 1)
                           if coeff(i, k_) != 0}
                for i in range(R_ORD + 1)
            }
            op["b"] = {str(k_): str(rhs_coeff(k_))
                       for k_ in range(-W_WIN, W_WIN + 1)
                       if rhs_coeff(k_) != 0}
            Path(__file__).with_name(
                "borromean-diagonal-recurrence-operator.json").write_text(
                json.dumps(op, indent=1) + "\n")
            print("  operator → borromean-diagonal-recurrence-operator.json")

    script_path = Path(__file__)
    witness = {
        "engine": f"python {sys.version.split()[0]} + rust sampler "
                  "(tools/borromean-recurrence-crt), exact mod-p + CRT + "
                  "Wang; sympy for the symbolic verification",
        "scriptFile": f"computations/{script_path.name}",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            cwd=script_path.parent).stdout.strip(),
        "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Multi-prime CRT reconstruction of the unique (r,W)=(6,11) "
            "Borromean diagonal colored-Jones recurrence operator, with "
            "exact symbolic annihilation as the claim-bearing gate"
        ),
        "computation": "borromean-diagonal-recurrence-reconstruct",
        "audit_only": True,
        "parameters": {"r": R_ORD, "W": W_WIN,
                       "degree_stats": {"min": min(degrees),
                                        "max": max(degrees)}},
        "prime_runs": runlog,
        "verdict": verdict,
        "wall_seconds": round(time.time() - t0, 1),
    }
    out = script_path.with_name(
        "borromean-diagonal-recurrence-reconstruct.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness → {out.name}   wall {witness['wall_seconds']}s")
    return 0 if verdict.get("verified_exact_symbolic") else 1


if __name__ == "__main__":
    sys.exit(main())
