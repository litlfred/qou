#!/usr/bin/env python3
"""
PROOF: (-1)^{n(λ)} = sgn(w_0^{S_{λ'}}) — the Δ_λ sign rule.

The sign alternation in Δ_λ = (-1)^{n(λ)} × dim(V_λ) is NOT
a numerical observation — it is the sign character of the longest
element of the CONJUGATE parabolic subgroup S_{λ'} ⊂ S_n.

Proof chain (standard, Macdonald I.1.5):
  1. n(λ) = Σ_{j≥0} C(λ_j', 2)
     where λ' is the conjugate partition and C(k,2) = k(k-1)/2.
  2. (-1)^{n(λ)} = Π_j (-1)^{C(λ_j', 2)} = Π_j sgn(w_0^{S_{λ_j'}})
  3. = sgn(w_0^{S_{λ'}})
     where S_{λ'} = S_{λ_1'} × S_{λ_2'} × ... is the Young subgroup.

This is categorical: it comes from the representation theory of
the symmetric group, independent of q. The Hecke algebra at q
deforms this to (-q^{-1})^{n(λ)} on the sign representation,
but the SIGN (the (-1) part) is purely classical.

Physical meaning: partitions whose conjugate parabolic has odd-length
longest element contribute NEGATIVELY to nuclear binding. This is
the Hecke-algebraic analog of Pauli exclusion.
"""

import json, time, math
from pathlib import Path

HERE = Path(__file__).resolve().parent

def n_stat(lam):
    return sum(i * lam[i] for i in range(len(lam)))

def conjugate(lam):
    if not lam: return ()
    conj = []
    for i in range(lam[0]):
        conj.append(sum(1 for p in lam if p > i))
    return tuple(conj)

def parts_of(n, mx=None):
    if mx is None: mx = n
    if n == 0: return [()]
    r = []
    for f in range(min(n, mx), 0, -1):
        for rest in parts_of(n - f, f):
            r.append((f,) + rest)
    return r

results = {}
total_checked = 0

for N in range(2, 21):
    parts = parts_of(N)
    all_ok = True
    for lam in parts:
        conj = conjugate(lam)
        sgn_conj = math.prod((-1)**(p*(p-1)//2) for p in conj)
        n = n_stat(list(lam))
        if (-1)**n != sgn_conj:
            all_ok = False
            break
    total_checked += len(parts)
    results[N] = {"partitions": len(parts), "all_match": all_ok}
    status = "PASS" if all_ok else "FAIL"
    print(f"S_{N:>2d}: {len(parts):>5d} partitions — {status}")

print(f"\nTotal partitions verified: {total_checked}")
print(f"All match: {all(r['all_match'] for r in results.values())}")

witness = {
    "engine": "python3",
    "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "computation": "delta-lambda-sign-rule-proof",
    "scriptFile": "delta_lambda_sign_rule_proof.py",
    "description": (
        "PROOF: (-1)^{n(lambda)} = sgn(w_0^{S_{lambda prime}}). "
        "The sign alternation in the Delta_lambda ansatz is the sign character "
        "of the longest element of the CONJUGATE parabolic subgroup. "
        "Standard identity (Macdonald I.1.5): n(lambda) = sum C(lambda_j prime, 2). "
        "Verified exhaustively for all partitions of S_2 through S_20."
    ),
    "data": {
        "identity": "n(lambda) = sum_j C(lambda_j_prime, 2)",
        "reference": "Macdonald, Symmetric Functions and Hall Polynomials, I.1.5",
        "sign_interpretation": "sgn(w_0^{S_{lambda_prime}}) = conjugate parabolic sign character",
        "physical_meaning": "Pauli exclusion analog: antisymmetric (conjugate-large) states resist binding",
        "verification": results,
        "total_partitions_checked": total_checked,
    },
    "assertions": [
        {"label": f"S_{N} all partitions match", "passed": results[N]["all_match"]}
        for N in range(2, 21)
    ],
    "allPassed": all(r["all_match"] for r in results.values()),
}

with open(HERE / "delta-lambda-sign-rule-proof.witness.json", "w") as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\nWitness: delta-lambda-sign-rule-proof.witness.json")
