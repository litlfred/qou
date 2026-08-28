#!/usr/bin/env python3
"""Exact closed form for the tetraplectic elementary-symmetric coefficients.

Bean ``qou-5843`` (c₃ Faddeev tetraplectic → combinatorics reduction). The single
sinh-lattice factor of the Faddeev modular-double residue product is

    P(x) = ∏_{n≥0} (1 + q^{2n+1} · x),      [x^k] P = e_k(q, q³, q⁵, …).

The scope doc
``docs/scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md``
states only the *lowest term* ``q^{k²}``. This script pins the **full closed form**
symbolically (exact, via sympy — no floating point):

    e_k(q, q³, q⁵, …)  =  q^{k²} / (q²; q²)_k ,   (q²; q²)_k = ∏_{j=1}^{k} (1 − q^{2j}).

Method: expand the *finite* product ∏_{n=0}^{N−1}(1 + q^{2n+1} x) exactly, extract
the coefficient of x^k (a polynomial in q), and check it agrees with the q-series
of q^{k²}/(q²;q²)_k up to the truncation order the finite product controls
(order < 2N). Because the infinite product's [x^k] stabilises once 2N exceeds the
compared order, this is an exact identity check, not a numerical fit.

Companion to the Lean recurrence backbone
``QOU/QBeta/TetraplecticProductRecurrence.lean`` (``tetraProd_funcEq``, the
q²-shift functional equation whose normalised power-series solution has exactly
these coefficients). Structural reduction only — this does NOT evaluate the c₃
carrier S = c₃ + Vol(4₁); that needs the transcendental argument map z(q₀), which
the deformation-gap audit proved is not a combinatorial object (beaned separately).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import sympy as sp

Q = sp.symbols("q")
X = sp.symbols("x")

K_MAX = 6          # check e_1 .. e_6
COMPARE_ORDER = 60  # compare q-series up to q^COMPARE_ORDER


def q_pochhammer_qsq(k: int) -> sp.Expr:
    """(q²; q²)_k = ∏_{j=1}^{k} (1 − q^{2j})."""
    out = sp.Integer(1)
    for j in range(1, k + 1):
        out *= (1 - Q ** (2 * j))
    return sp.expand(out)


def finite_ek(k: int, N: int) -> sp.Expr:
    """[x^k] of ∏_{n=0}^{N-1}(1 + q^{2n+1} x), via x-truncated multiplication.

    Track only x-degrees 0..k: `c[j]` is the coefficient of x^j. Each factor
    `(1 + q^{2n+1} x)` updates `c[j] += q^{2n+1}·c[j-1]` (descending j). O(N·k),
    no 2^N blow-up. Returns the exact polynomial `c[k]` in q.
    """
    c = [sp.Integer(1)] + [sp.Integer(0)] * k
    for n in range(N):
        a = Q ** (2 * n + 1)
        for j in range(k, 0, -1):
            c[j] = sp.expand(c[j] + a * c[j - 1])
    return c[k]


def min_q_degree(expr: sp.Expr) -> int | None:
    """Lowest power of q appearing in a polynomial in q (None if identically 0)."""
    e = sp.expand(expr)
    if e == 0:
        return None
    p = sp.Poly(e, Q)
    return min(int(m[0]) for m in p.monoms())


def main() -> None:
    results = []
    all_ok = True
    for k in range(1, K_MAX + 1):
        # 2N must exceed COMPARE_ORDER so the finite [x^k] equals the infinite one
        # up to order COMPARE_ORDER (the tail only affects order ≥ 2N−k terms).
        N = (COMPARE_ORDER + 2 * k) // 2 + 2
        lhs = finite_ek(k, N)                       # finite e_k (polynomial in q)
        poch = q_pochhammer_qsq(k)                  # (q²;q²)_k

        # Exact identity check: infinite e_k · (q²;q²)_k = q^{k²}. For the finite e_k
        # the residual `lhs·poch − q^{k²}` must vanish to all orders the finite
        # product controls, i.e. its lowest surviving q-power exceeds COMPARE_ORDER.
        resid = sp.expand(lhs * poch - Q ** (k * k))
        resid_min = min_q_degree(resid)
        match = (resid_min is None) or (resid_min > COMPARE_ORDER)
        all_ok = all_ok and match

        lowest = min_q_degree(lhs)
        results.append({
            "k": k,
            "N_truncation": N,
            "closed_form": f"q^{k*k} / (q^2;q^2)_{k}",
            "lowest_power": lowest,
            "lowest_power_expected": k * k,
            "lowest_power_ok": lowest == k * k,
            "residual_min_q_degree": resid_min,
            "controlled_to_order": COMPARE_ORDER,
            "match": bool(match),
        })
        tag = "OK" if match else "MISMATCH"
        rr = "∞" if resid_min is None else f"q^{resid_min}"
        print(f"e_{k}: closed form q^{k*k}/(q^2;q^2)_{k}  "
              f"lowest=q^{lowest} (exp q^{k*k})  residual≥{rr} (>q^{COMPARE_ORDER}?) {tag}")

    script_path = Path(__file__).resolve()

    def _git(args: list[str]) -> str:
        try:
            return subprocess.check_output(
                ["git", *args], cwd=script_path.parent, text=True).strip() or "unknown"
        except Exception:
            return "unknown"

    commit = _git(["log", "-1", "--format=%H", "--", str(script_path)])
    repo_head = _git(["rev-parse", "HEAD"])
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]

    witness = {
        "schema": "witness/v1",
        # I14 provenance triple (computations/audits/witness_provenance_audit.py)
        "engine": "python+sympy",
        "scriptFile": "qbeta_ek_qpochhammer_closed_form.py",
        "commitSha": repo_head,
        "description": (
            "Exact closed form e_k(q,q^3,q^5,...) = q^{k^2}/(q^2;q^2)_k for the "
            "tetraplectic single-lattice product coefficients (c3 Faddeev reduction, "
            "bean qou-5843). Symbolic (sympy), no floating point."
        ),
        "computation": {
            "script": "computations/qbeta/qbeta_ek_qpochhammer_closed_form.py",
            "scriptCommitSha": commit,
            "scriptHash": script_hash,
            "method": "finite-product coefficient vs q-series of q^{k^2}/(q^2;q^2)_k",
        },
        "parameters": {"k_max": K_MAX, "compare_order": COMPARE_ORDER},
        "results": results,
        "verdict": (
            "CONFIRMED: e_k = q^{k^2}/(q^2;q^2)_k exact for k=1..%d "
            "(q-series agree to order q^%d)." % (K_MAX, COMPARE_ORDER)
        ) if all_ok else "MISMATCH — closed form failed; investigate.",
        "all_ok": all_ok,
        "scope": (
            "Structural reduction coefficient only. Does NOT evaluate the c3 carrier "
            "S = c3 + Vol(4_1); the z(q0) argument map is transcendental (not "
            "combinatorial) and is beaned separately. No fit; nothing wired."
        ),
    }
    out = script_path.with_suffix(".witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nverdict: {witness['verdict']}")
    print(f"witness: {out}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
