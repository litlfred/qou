#!/usr/bin/env python3
"""Total positivity of the Kashaev value <K>_N at every Galois conjugate (bean qou-pc7n).

A per-N Hermitian-square certificate (a sum of norms from Q(zeta_N) to Q(zeta_N)^+,
as proved for 4_1 in QOU/Core/KashaevHermitianCertificate.lean) forces <K>_N >= 0 at
EVERY primitive N-th root, not only at zeta = e^{2 pi i/N}. So if <K>_N < 0 at some
conjugate, no such certificate exists for that N, and a certificate has to be stated
at the Jones embedding (the coordinator's caveat 1).

Input: the exact Habiro coefficients c_k(K; q) in Z[q^{+-1}] of
weaving-habiro.result.json (k <= Kmax = 13), stored as Laurent polynomials in
w = q^{1/4}. Then, at q = e^{2 pi i a/N} with gcd(a, N) = 1,

    <K>_N(a) = sum_{k<N} c_k(q) * prod_{j=1}^{k} (2 - q^j - q^-j),

since {N+j}{N-j} = 2 - q^j - q^-j at any primitive N-th root. N <= Kmax + 1.

Arithmetic: mpmath at mp.dps = 60, no float. The exact values lie in Q(zeta_N)^+;
verdicts carry the imaginary-part residue and a margin. 4_1 is the control: its
value must be positive at every conjugate (proved in Lean).

Run: python3 -u computations/probes/weaving_kashaev_root_of_unity/galois_total_positivity_probe.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


def eval_c(poly: dict, q4) -> mp.mpc:
    """Evaluate a Laurent polynomial in w at w = q4 (a fourth root of q)."""
    lo, coeffs = poly["lo"], poly["coeffs"]
    return mp.fsum(mp.mpf(c) * q4 ** (lo + i) for i, c in enumerate(coeffs) if c)


def kashaev_at(cs: list, N: int, a: int) -> mp.mpc:
    theta = 2 * mp.pi * a / N
    q = mp.expjpi(2 * mp.mpf(a) / N)
    q4 = mp.expjpi(mp.mpf(a) / (2 * N))
    total, prod = mp.mpc(0), mp.mpf(1)
    for k in range(N):
        if k > 0:
            prod *= 2 - 2 * mp.cos(k * theta)
        total += eval_c(cs[k], q4) * prod
    # all c_k exponents in w are multiples of 4, so the q^{1/4} branch is irrelevant
    assert all((p["lo"] + i) % 4 == 0 for p in cs for i, c in enumerate(p["coeffs"]) if c)
    _ = q
    return total


def main() -> int:
    data = json.loads((HERE / "weaving-habiro.result.json").read_text())
    kmax = data["Kmax"]
    out = {"description": "Kashaev value at every Galois conjugate; bean qou-pc7n",
           "dps": mp.mp.dps, "Nmax": kmax + 1, "knots": {}}
    for name, rec in data["knots"].items():
        cs = rec["c"]
        rows = []
        for N in range(2, kmax + 2):
            vals = []
            for a in range(1, N // 2 + 1):
                if math.gcd(a, N) != 1:
                    continue
                v = kashaev_at(cs, N, a)
                vals.append({"a": a, "re": mp.nstr(v.real, 20), "im_abs": mp.nstr(abs(v.imag), 3)})
            neg = [r["a"] for r in vals if mp.mpf(r["re"]) < 0]
            rows.append({"N": N, "conjugates": vals, "negative_at_a": neg})
            print(f"{name:7s} N={N:2d} " + "  ".join(f"a={r['a']}:{mp.nstr(mp.mpf(r['re']), 8)}" for r in vals)
                  + (f"   NEGATIVE at a={neg}" if neg else ""), flush=True)
        out["knots"][name] = {"rows": rows,
                              "N_with_negative_conjugate": [r["N"] for r in rows if r["negative_at_a"]]}
    (HERE / "galois-total-positivity.result.json").write_text(json.dumps(out, indent=1))
    for name, rec in out["knots"].items():
        print(name, "N with a negative conjugate:", rec["N_with_negative_conjugate"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
