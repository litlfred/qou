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
import os
import sys

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

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
        "parameters": {
            "dps": mp.mp.dps,
            "Zmax": ZMAX,
            "tolerance": mp.nstr(TOL, 2),
        },
        "result": {"all_ok": bool(all_ok), "per_q": per_q},
        "refs": [
            "docs/audits/2026-06-07-chebyshev-pairing-engine-proved.md",
            "folio/quantum-observable-universe/molecular-construction/palindromicity-orbital-type.md",
            "folio/quantum-observable-universe/molecular-construction/shell-closure-nf-term-count.md",
        ],
    }
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "substrate"))
    from witness_base import WitnessBuilder

    # ── Assertions (bean qou-srvu) ───────────────────────────────
    # This witness reported `allPassed: true` while asserting nothing,
    # so it read as a pass to every consumer of that field. Nothing is
    # invented here: the checks below were ALREADY computed (`ok`,
    # `identity_holds`, `sign_alternation_ok` above) and stored as data
    # — they were simply never asserted, so no consumer could see a
    # failure. The tolerance is the module's own TOL, declared at the
    # top of this file before any result is computed, so it is not a
    # threshold reverse-engineered from the observed residual.
    #
    # These are falsifiable and are not self-comparisons: `lhs` is
    # (σ⁻¹)^Z built by repeated matrix multiplication, `rhs` is the
    # closed form c_Z·σ + d_Z. A wrong c_Z / d_Z breaks the identity.
    n_identity_ok = sum(1 for r in per_q if r["identity_holds"])
    n_sign_checked = sum(1 for r in per_q if r["sign_alternation_ok"] is not None)
    n_sign_ok = sum(1 for r in per_q if r["sign_alternation_ok"] is True)
    overall_max_resid = max(
        (mp.mpf(r["max_residual"]) for r in per_q), default=mp.mpf(0)
    )

    builder = WitnessBuilder.wrap_legacy(
        "chebyshev-pairing-engine", witness,
        script_path=__file__, engine="mpmath",
    )
    builder.add_assertion(
        "identity_holds_all_q",
        computed=n_identity_ok,
        expected=len(per_q),
        tolerance=0,
        source=(
            "(σ⁻¹)^Z = c_Z·σ + d_Z in H₂(q), residual ≤ TOL at every "
            "sampled q; the identity is q-independent and algebraic"
        ),
    )
    builder.add_assertion(
        "sign_alternation_all_q_gt_1",
        computed=n_sign_ok,
        expected=n_sign_checked,
        tolerance=0,
        source="c_Z < 0 for even Z and > 0 for odd Z when q > 1",
    )
    # Strings keep the residual out of float64 (drained convention,
    # qou-t0rf); expected 0 because the identity is exact.
    builder.add_assertion(
        "max_residual_within_declared_TOL",
        computed=mp.nstr(overall_max_resid, 8),
        expected="0",
        tolerance=mp.nstr(TOL, 2),
        source="module constant TOL, declared before any result is computed",
    )
    out = builder.save()
    print(f"all_ok = {all_ok}")
    for r in per_q:
        print(f"  q={r['q']:>8}  max_resid={r['max_residual']}  "
              f"identity={r['identity_holds']}  sign_alt={r['sign_alternation_ok']}")
    print(f"witness -> {out}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
