#!/usr/bin/env python3
"""z-Habiro → Φ_q numerical wiring (entry point).

Wires the now-PROVEN Lean identification of the brane-tower limit (PR #2447,
`QOU.MassEndomorphism.ZHabiroCauchy`) into numerical compute at the substrate
q_0. This is the FIRST wiring step: it does NOT yet rewire any production mass
table — it establishes the canonical numerical bridge and the cross-checks that
a production wiring will rely on.

What it verifies (exact-ish, mpmath, no fit):

  1. **eulerCoeff** — the proven monomial coefficient
        b_m = q^{-m} / ∏_{j=1}^m (1 - q^{-j})            (`eulerCoeff`)
     evaluated at q_0, with the depth recurrence
        b_{m+1} = b_m · q^{-1} · (1 - q^{-(m+1)})^{-1}     (`eulerCoeff_succ`)
     cross-checked to machine precision (the q-difference recurrence whose
     unique solution is eulerCoeff — `eulerCoeff_unique`).

  2. **eulerTrunc = cyclotomic partial sum** — the Lean identity
     `eulerTrunc_eq_cyclotomic`: the genuine monomial truncation
        Φ̃_q^{(n)}(z) = Σ_{m≤n} b_m z^m
     equals a brane-tower cyclotomic partial sum Σ_{m≤n} c_m P_m,
     P_m(z) = ∏_{k=1}^m (1 - q^{-k} z). Verified by recovering the cyclotomic
     coefficients c_m via the triangular base change and confirming the two
     polynomials agree at sample points.

  3. **N=0 → Φ_q correction** — the convergent product
        Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}
     vs the N=0 single-tick value 1, reporting the multiplicative correction
     factor at a representative z = ℏ_q² (the brane-tower variable scale).

Output: zhabiro-phiq-wiring.witness.json
Lean refs: QOU.MassEndomorphism.ZHabiroCauchy.{eulerCoeff,eulerCoeff_succ,
eulerCoeff_unique,eulerTrunc_eq_cyclotomic,zHabiroLimit_coord_eq_eulerTrunc}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
mp.mp.dps = 60

# substrate q_0 (proton-pinned) — canonical accessor, with literal fallback.
try:
    sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
    from qou_substrate.constants import q_at  # type: ignore
    Q0 = mp.mpf(str(q_at()))
    Q0_SOURCE = "qou_substrate.constants.q_at (proton pin)"
except Exception:  # pragma: no cover - fallback for bare environments
    Q0 = mp.mpf("1.10997859555733")
    Q0_SOURCE = "literal fallback 1.10997859555733"

N_DEPTH = 12  # cyclotomic depth for the truncation cross-check


def euler_coeff(q: mp.mpf, m: int) -> mp.mpf:
    """b_m = q^{-m} / ∏_{j=1}^m (1 - q^{-j})  (Lean `eulerCoeff`)."""
    denom = mp.mpf(1)
    for j in range(1, m + 1):
        denom *= (1 - q ** (-j))
    return q ** (-m) / denom


def euler_coeff_recurrence(q: mp.mpf, n: int) -> list[mp.mpf]:
    """b_0 = 1; b_{m+1} = b_m · q^{-1} · (1 - q^{-(m+1)})^{-1} (Lean `eulerCoeff_succ`)."""
    b = [mp.mpf(1)]
    for m in range(n):
        b.append(b[-1] * q ** (-1) * (1 - q ** (-(m + 1))) ** (-1))
    return b


def cyclotomic_coeffs(q: mp.mpf, b: list[mp.mpf]) -> list[mp.mpf]:
    """Triangular base change: recover c_m with Σ b_m z^m = Σ c_m P_m,
    P_m = ∏_{k=1}^m (1 - q^{-k} z). Peel top monomial coefficient against the
    degree-m, unit-leading-coeff P_m (the Lean `cyclo_repr_exists` change)."""
    n = len(b) - 1
    # polynomial coefficient arrays (index = power of z), low->high
    rem = list(b)
    # P_m coefficients
    def P_coeffs(m: int) -> list[mp.mpf]:
        poly = [mp.mpf(1)]
        for k in range(1, m + 1):
            # multiply by (1 - q^{-k} z)
            nxt = [mp.mpf(0)] * (len(poly) + 1)
            for i, ci in enumerate(poly):
                nxt[i] += ci
                nxt[i + 1] += -(q ** (-k)) * ci
            poly = nxt
        return poly
    Ps = [P_coeffs(m) for m in range(n + 1)]
    c = [mp.mpf(0)] * (n + 1)
    for m in range(n, -1, -1):
        lead = Ps[m][m]  # leading coeff of P_m (a unit)
        c[m] = rem[m] / lead
        # subtract c[m] * P_m
        for i, pc in enumerate(Ps[m]):
            rem[i] -= c[m] * pc
    return c


def poly_eval(coeffs: list[mp.mpf], z: mp.mpf) -> mp.mpf:
    return sum(ci * z ** i for i, ci in enumerate(coeffs))


def P_eval(q: mp.mpf, m: int, z: mp.mpf) -> mp.mpf:
    out = mp.mpf(1)
    for k in range(1, m + 1):
        out *= (1 - q ** (-k) * z)
    return out


def main() -> int:
    q = Q0
    print("=" * 68)
    print("  z-Habiro → Φ_q numerical wiring (entry point)")
    print(f"  q_0 = {mp.nstr(q, 18)}  [{Q0_SOURCE}]   depth N = {N_DEPTH}")
    print("=" * 68)

    # (1) eulerCoeff vs its recurrence
    b_closed = [euler_coeff(q, m) for m in range(N_DEPTH + 1)]
    b_rec = euler_coeff_recurrence(q, N_DEPTH)
    rec_err = max(abs(b_closed[m] - b_rec[m]) for m in range(N_DEPTH + 1))
    print(f"\n  (1) eulerCoeff closed-form vs recurrence: max abs err = {mp.nstr(rec_err, 3)}")

    # (2) eulerTrunc (monomial) == cyclotomic partial sum, at sample points
    c = cyclotomic_coeffs(q, b_closed)
    # z must satisfy |z| < q for the cyclotomic/Euler pictures to make sense;
    # sample a few z in (0, 1) (well inside |z|<q).
    sample_z = [mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.5")]
    ident_err = mp.mpf(0)
    for z in sample_z:
        monomial = poly_eval(b_closed, z)
        cyclo = sum(c[m] * P_eval(q, m, z) for m in range(N_DEPTH + 1))
        ident_err = max(ident_err, abs(monomial - cyclo))
    print(f"  (2) eulerTrunc == Σ c_m P_m  (eulerTrunc_eq_cyclotomic): "
          f"max abs err over samples = {mp.nstr(ident_err, 3)}")

    # (3) N=0 -> Φ_q correction at z = ℏ_q² (brane-tower variable scale)
    hbar_q = 1 - q ** (-1)
    z_brane = hbar_q ** 2
    # convergent product Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}
    phi = mp.mpf(1)
    k = 1
    while True:
        factor = (1 - q ** (-k) * z_brane) ** (-1)
        phi *= factor
        if abs(factor - 1) < mp.mpf(10) ** (-50):
            break
        k += 1
        if k > 2000:
            break
    correction = phi - 1  # N=0 single-tick value is 1
    print(f"\n  (3) brane-tower variable z = ℏ_q² = {mp.nstr(z_brane, 8)}")
    print(f"      Φ_q(z) convergent = {mp.nstr(phi, 18)}  (converged at k={k})")
    print(f"      N=0 → Φ_q multiplicative correction = {mp.nstr(correction, 6)}"
          f"  ({mp.nstr(correction * 100, 4)} %)")

    ok = (rec_err < mp.mpf(10) ** (-45)) and (ident_err < mp.mpf(10) ** (-40))
    print("\n" + "=" * 68)
    print("  ✓ WIRING BRIDGE VERIFIED" if ok else "  ✗ cross-check FAILED")
    print("    eulerCoeff recurrence + eulerTrunc=cyclotomic identity hold at q_0")
    print("    (numerical realization of the merged Lean theorems, PR #2447).")
    print("=" * 68)

    witness = {
        "computation": "zhabiro-phiq-wiring",
        "kind": "exploratory-probe",
        "content_block": "conj:brane-tower-z-habiro",
        "engine": "mpmath",
        "dps": mp.mp.dps,
        "q0": mp.nstr(q, 30),
        "q0_source": Q0_SOURCE,
        "depth_N": N_DEPTH,
        "result": {
            "eulerCoeff_recurrence_max_abs_err": mp.nstr(rec_err, 6),
            "eulerTrunc_eq_cyclotomic_max_abs_err": mp.nstr(ident_err, 6),
            "brane_z_hbar_q_squared": mp.nstr(z_brane, 30),
            "phi_q_convergent": mp.nstr(phi, 30),
            "n0_to_phi_correction": mp.nstr(correction, 30),
            "n0_to_phi_correction_pct": mp.nstr(correction * 100, 12),
            "cross_check_ok": bool(ok),
        },
        "euler_coeffs_b_m": [mp.nstr(b_closed[m], 18) for m in range(N_DEPTH + 1)],
        "cyclotomic_coeffs_c_m": [mp.nstr(c[m], 18) for m in range(N_DEPTH + 1)],
        "_provenance": {
            "series_coeff_formula": "b_m = q^-m / prod_{j=1}^m (1 - q^-j)",
            "lean_refs": [
                "QOU.MassEndomorphism.ZHabiroCauchy.eulerCoeff",
                "QOU.MassEndomorphism.ZHabiroCauchy.eulerCoeff_succ",
                "QOU.MassEndomorphism.ZHabiroCauchy.eulerCoeff_unique",
                "QOU.MassEndomorphism.ZHabiroCauchy.eulerTrunc_eq_cyclotomic",
                "QOU.MassEndomorphism.ZHabiroCauchy.zHabiroLimit_coord_eq_eulerTrunc",
                "QOU.MassEndomorphism.PhiQConvergence.quantumDilog_functional_eq",
            ],
            "wiring_status": "entry-point: numerical bridge + cross-checks; "
                             "production mass-table rewire is the next step",
        },
    }
    out = HERE.parent / "zhabiro-phiq-wiring.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
