#!/usr/bin/env python3
"""Witness for the Hecke pairing engine (σ⁻¹)^Z = c_Z σ + d_Z in H₂(q).

Proves numerically (to 1e-40) the identity established in
docs/audits/2026-06-07-chebyshev-pairing-engine-proved.md:

    (σ⁻¹)^Z = c_Z·σ + d_Z   in H₂(q),  σ² = h·σ + 1,  h = q - q⁻¹,
    c_Z = (q^{-Z} - (-1)^Z q^Z)/[2]_q,
    d_Z = (q^{-(Z+1)} + (-1)^Z q^{Z+1})/[2]_q,   [2]_q = q + q⁻¹.

The identity is exact for ALL q (it is algebra, not a fit), so the
witness checks several q including the substrate q₀ ≈ 1.1097 and a
q < 1 value, and confirms the sign-alternation c_Z<0 (even) / >0 (odd)
for q>1. Uses the regular representation M_σ = [[0,1],[1,h]] of σ on
the basis {1, σ}.
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

import mpmath as mp

mp.mp.dps = 50

Q_SUBSTRATE = mp.mpf("1.1097")  # substrate q₀ (display value; identity is q-independent)
QS = [Q_SUBSTRATE, mp.mpf("1.5"), mp.mpf("2"), mp.mpf("0.7")]
ZMAX = 12
TOL = mp.mpf("1e-40")


def bracket2(q):
    return q + 1 / q


def c_Z(q, Z):
    return (q ** (-Z) - (-1) ** Z * q ** Z) / bracket2(q)


def d_Z(q, Z):
    return (q ** (-(Z + 1)) + (-1) ** Z * q ** (Z + 1)) / bracket2(q)


def M_sigma(q):
    h = q - 1 / q
    return mp.matrix([[0, 1], [1, h]])


def mat_max_abs(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def git_sha_of(path):
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", path],
            cwd=os.path.dirname(os.path.abspath(__file__)),
        ).decode().strip()
    except Exception:
        return None


def file_hash(path):
    import hashlib
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except Exception:
        return None


def main():
    I = mp.matrix([[1, 0], [0, 1]])
    all_ok = True
    per_q = []
    for q in QS:
        Ms = M_sigma(q)
        Minv = Ms ** (-1)
        max_resid = mp.mpf(0)
        sign_ok = True
        Mz = I.copy()  # (σ⁻¹)^0
        for Z in range(0, ZMAX + 1):
            lhs = Mz
            rhs = c_Z(q, Z) * Ms + d_Z(q, Z) * I
            resid = mat_max_abs(lhs - rhs)
            max_resid = max(max_resid, resid)
            if q > 1 and Z >= 1:
                cz = c_Z(q, Z)
                want_neg = (Z % 2 == 0)
                if (cz < 0) != want_neg:
                    sign_ok = False
            Mz = Mz * Minv  # advance to (σ⁻¹)^{Z+1}
        ok = (max_resid <= TOL) and (sign_ok if q > 1 else True)
        all_ok = all_ok and ok
        per_q.append({
            "q": mp.nstr(q, 8),
            "max_residual": mp.nstr(max_resid, 4),
            "identity_holds": bool(max_resid <= TOL),
            "sign_alternation_ok": bool(sign_ok) if q > 1 else None,
            "c_Z_sample": {str(Z): mp.nstr(c_Z(q, Z), 8) for Z in range(0, 7)},
        })

    script_path = os.path.abspath(__file__)
    witness = {
        "schema": "qou-witness/v1",
        "name": "chebyshev-pairing-engine",
        "description": (
            "Exact-identity witness for (σ⁻¹)^Z = c_Z σ + d_Z in H₂(q) with "
            "c_Z=(q^{-Z}-(-1)^Z q^Z)/[2]_q, d_Z=(q^{-(Z+1)}+(-1)^Z "
            "q^{Z+1})/[2]_q. Verified to 1e-40 across several q (q-independent "
            "algebraic identity) plus the sign-alternation c_Z<0 even / >0 odd "
            "for q>1. Underlies conj:palindromicity-orbital-type and "
            "conj:shell-closure-nf-term-count."
        ),
        "computation": {
            "engine": "python+mpmath",
            "dps": mp.mp.dps,
            "Zmax": ZMAX,
            "tolerance": mp.nstr(TOL, 2),
            "script": "computations/chebyshev_pairing_engine_witness.py",
        },
        "scriptCommitSha": git_sha_of(script_path),
        "scriptHash": file_hash(script_path),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "result": {"all_ok": bool(all_ok), "per_q": per_q},
        "refs": [
            "docs/audits/2026-06-07-chebyshev-pairing-engine-proved.md",
            "content/quantum-observable-universe/molecular-construction/palindromicity-orbital-type.md",
            "content/quantum-observable-universe/molecular-construction/shell-closure-nf-term-count.md",
        ],
    }
    out = os.path.join(
        os.path.dirname(script_path), "chebyshev-pairing-engine.witness.json"
    )
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"all_ok = {all_ok}")
    for r in per_q:
        print(f"  q={r['q']:>8}  max_resid={r['max_residual']}  "
              f"identity={r['identity_holds']}  sign_alt={r['sign_alternation_ok']}")
    print(f"witness -> {out}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
