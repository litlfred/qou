#!/usr/bin/env python3
"""Measure the (1−q)-adic valuations behind the level-map prune
(bean qou-vnuf) — is the proved 2n+3m floor tight, or does the
Masbaum coefficient contribute extra vanishing?

The Lean file `QOU/QBeta/LevelMapValuation.lean` proves that a
single-level bridge joining Masbaum level n to GGM block level m
forces its coefficient to carry (1−q)^{2n+3m}: the block's order-3m
pole at q = 1 must be paid for, and the Masbaum level term
T^Mas_n = C_n·(q;q)_n² already vanishes to order ≥ 2n. Over ℤ[X] that
is a degree bound.

A bound is only as useful as it is tight, so this probe MEASURES the
actual order of vanishing at q = 1 of the real 5₂ Masbaum level terms
and compares:

  * ν(T^Mas_n) — exact, by repeated synthetic division by (q−1) on the
    integer coefficient list (no floats, no tolerance);
  * the proved floor 2n;
  * the excess ν(T^Mas_n) − 2n, i.e. what C_n contributes on its own
    (ν(C_n), also measured directly).

Gates (all exact): the measured ν(T^Mas_n) ≥ 2n for every n — a
machine check of the Lean theorem on the real data; the additivity
ν(T^Mas_n) = ν(C_n) + 2n, which certifies the two measurements against
each other; and ν((q;q)_n) = n on the same code path.

An excess would mean the proved bound is not tight and the real prune
is stronger than the theorem states — reported either way, with the
implied level ceiling for coefficients of a given degree.

auditOnly; no c_k wired; no fit; no bridge claimed. Comparison to
observed only; no ontological claims.

Run: python3 -u computations/probes/qbeta_5two_masbaum_valuation_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_valuation.log
"""
from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

N_MAX = 12
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def dict_to_coeffs(d):
    """{exponent: int} → dense coefficient list from the lowest exponent
    (a monomial shift never changes the order of vanishing at q = 1)."""
    d = {e: int(c) for e, c in d.items() if c != 0}
    if not d:
        return []
    lo, hi = min(d), max(d)
    return [d.get(e, 0) for e in range(lo, hi + 1)]


def valuation_at_one(coeffs):
    """Exact order of vanishing at q = 1 of Σ coeffs[i]·q^i, by repeated
    synthetic division by (q − 1). Integer arithmetic throughout."""
    c = list(coeffs)
    v = 0
    while c and any(c):
        # evaluate at q = 1
        if sum(c) != 0:
            break
        # synthetic division by (q - 1), descending order
        desc = c[::-1]
        out, carry = [], 0
        for a in desc:
            carry = carry + a
            out.append(carry)
        # exact division ⟹ final remainder is 0
        assert out[-1] == 0, "synthetic division left a remainder"
        c = out[:-1][::-1]
        v += 1
    return v


def poly_mul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def qpoch_coeffs(n):
    """(q;q)_n as a dense integer coefficient list."""
    p = [1]
    for j in range(1, n + 1):
        f = [0] * (j + 1)
        f[0] = 1
        f[j] = -1
        p = poly_mul(p, f)
    return p


def main() -> int:
    print("=" * 78)
    print(" (1−q)-adic valuations behind the level-map prune")
    print("=" * 78)

    # ---- gate: ν((q;q)_n) = n on this code path ----
    g_poch = True
    for n in range(0, N_MAX + 1):
        if valuation_at_one(qpoch_coeffs(n)) != n:
            g_poch = False
    log(f"[gate] ν((q;q)_n) = n for n ≤ {N_MAX}: "
        f"{'PASS' if g_poch else 'FAIL'}")

    # ---- measure ν(C_n) and ν(T^Mas_n) ----
    log("measuring the Masbaum level valuations ...")
    rows = []
    g_floor = True
    g_additive = True
    for n in range(0, N_MAX + 1):
        # C_n(a) in the variable a; the Masbaum level term is built at
        # q = a², so express both on the same q-grid: C_n has only even
        # a-exponents (established u-even in B1.3/B1.4′).
        Cn = _mb.C52(n)
        Cn = {e: int(c) for e, c in Cn.items() if c != 0}
        odd = [e for e in Cn if e % 2]
        assert not odd, f"odd a-exponent in C_{n}: {odd[:4]}"
        Cq = {e // 2: c for e, c in Cn.items()}
        c_coeffs = dict_to_coeffs(Cq)
        nu_C = valuation_at_one(c_coeffs)
        # T^Mas_n = C_n · (q;q)_n²
        poch = qpoch_coeffs(n)
        T = poly_mul(c_coeffs, poly_mul(poch, poch))
        nu_T = valuation_at_one(T)
        floor_ok = nu_T >= 2 * n
        add_ok = nu_T == nu_C + 2 * n
        g_floor = g_floor and floor_ok
        g_additive = g_additive and add_ok
        rows.append({"n": n, "nu_C": nu_C, "nu_T": nu_T,
                     "floor_2n": 2 * n, "excess": nu_T - 2 * n,
                     "deg_T": max(len(T) - 1, 0)})
        log(f"    n={n:2d}: ν(C_n)={nu_C:3d}  ν(T^Mas_n)={nu_T:3d}  "
            f"floor 2n={2*n:3d}  excess={nu_T - 2*n:3d}")
    log(f"[gate] ν(T^Mas_n) ≥ 2n (the Lean theorem, on real data): "
        f"{'PASS' if g_floor else 'FAIL'}")
    log(f"[gate] ν(T^Mas_n) = ν(C_n) + 2n (cross-certification): "
        f"{'PASS' if g_additive else 'FAIL'}")

    excesses = [r["excess"] for r in rows]
    tight = all(e == 0 for e in excesses)
    log(f"[T] excess over the proved floor: min {min(excesses)}, "
        f"max {max(excesses)} ⇒ bound is "
        f"{'TIGHT' if tight else 'NOT tight (real prune is stronger)'}")

    wb = WitnessBuilder("qbeta-5two-masbaum-valuation",
                        engine="exact-integer",
                        _script_path=__file__)
    wb.set_description(
        "Measures the (1−q)-adic valuation at q = 1 of the real 5₂ "
        "Masbaum level terms T^Mas_n = C_n·(q;q)_n², to test whether "
        "the proved level-map coefficient floor (1−q)^{2n+3m} "
        "(QOU/QBeta/LevelMapValuation.lean, "
        "sub_one_pow_dvd_coeff_combined) is tight on the real data. "
        "Valuations computed exactly by repeated synthetic division by "
        "(q−1) over the integers — no floats, no tolerance. Gates: "
        "ν((q;q)_n) = n on the same code path; ν(T^Mas_n) ≥ 2n (the "
        "theorem, machine-checked); ν(T^Mas_n) = ν(C_n) + 2n "
        "(cross-certification of the two measurements). auditOnly; no "
        "c_k wired; no fit; no bridge claimed.")
    wb.set_content_block("prop:habiro-tail-star-identity")

    wb.add_assertion("qpoch_valuation_is_n",
                     computed=1.0 if g_poch else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="ν((q;q)_n) = n for every n in range — "
                            "validates the valuation routine")
    wb.add_assertion("masbaum_valuation_meets_proved_floor",
                     computed=1.0 if g_floor else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="ν(T^Mas_n) ≥ 2n — the Lean theorem checked "
                            "against the real Masbaum coefficients")
    wb.add_assertion("valuation_additivity",
                     computed=1.0 if g_additive else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="ν(T^Mas_n) = ν(C_n) + 2n — the two "
                            "measurements certify each other")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("levels", rows)
    wb.add_data("excess_over_floor",
                {"min": min(excesses), "max": max(excesses),
                 "tight": bool(tight)})
    wb.add_data("verdict",
                ((f"The proved floor ν ≥ 2n is TIGHT on the real data "
                  f"(ν(C_n) = 0 for every measured n ≤ {N_MAX}): the "
                  f"Masbaum coefficient contributes NO extra vanishing "
                  f"at q = 1, so (1−q)^{{2n+3m}} is exactly the forced "
                  f"content of a single-level bridge coefficient and "
                  f"the degree bound deg ≥ 2n+3m cannot be improved by "
                  f"this argument."
                  if tight else
                  f"The proved floor is NOT tight: ν(C_n) > 0 for some "
                  f"n (excess up to {max(excesses)}), so the real prune "
                  f"is STRONGER than the theorem states — the extra "
                  f"vanishing is a structural property of the Masbaum "
                  f"coefficients themselves and is worth promoting to a "
                  f"sharper Lean bound.")
                 + " auditOnly.") if ok else "A gate failed — inspect.")
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-masbaum-valuation.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
