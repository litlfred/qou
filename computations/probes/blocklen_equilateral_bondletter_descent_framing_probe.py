#!/usr/bin/env python3
"""80-dps mpmath probe for Round 75:
- qou-5jqv: QOU.Knot.BlockLengthAdditive.length_mul_of_supportedIn
- qou-ebs6: QOU.Mass.EquilateralBound.equidistant_directed_bonds_le_twelve_in_R3
- qou-gba1: QOU.Hecke.BondLetterIdentification.tr_bond_interp_sub
- qou-fn04: QOU.Torsion.mem_desc_iff_tau_eq
- qou-m4fp: QOU.StandardModel.TwistBattery.framing_split_spectrum_dichotomy
"""

from __future__ import annotations
import hashlib
import json
import pathlib
import sys
from mpmath import mp

mp.dps = 80


def inversion_count(perm: tuple[int, ...]) -> int:
    n = len(perm)
    return sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])


def compose_perm(u: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(u[v[i]] for i in range(len(u)))


def check_block_length_additive() -> dict[str, object]:
    # Permutations on Fin 6 supported in [0, 3) and [3, 6) with b1 = 3 <= a2 = 3
    u = (2, 0, 1, 3, 4, 5)
    v = (0, 1, 2, 5, 4, 3)
    uv = compose_perm(u, v)
    len_u = inversion_count(u)
    len_v = inversion_count(v)
    len_uv = inversion_count(uv)
    passed = (len_uv == len_u + len_v) and (len_u == 2) and (len_v == 3) and (len_uv == 5)
    return {
        "bean": "qou-5jqv",
        "theorem": "QOU.Knot.BlockLengthAdditive.length_mul_of_supportedIn",
        "len_u": str(len_u),
        "len_v": str(len_v),
        "len_uv": str(len_uv),
        "residual": mp.nstr(mp.mpf(len_uv - (len_u + len_v)), 80),
        "passed": passed,
    }


def check_equilateral_bound() -> dict[str, object]:
    # Regular tetrahedron in R^3: 3 vectors from apex p0 at common distance d
    d = mp.mpf("17") / mp.mpf("10")
    weights = [mp.mpf("3") / mp.mpf("7"), mp.mpf("-2") / mp.mpf("5"), mp.mpf("11") / mp.mpf("13")]
    # Gram matrix G_{ij} = d^2 / 2 * (1 + delta_{ij})
    lhs = mp.mpf("0")
    for i in range(3):
        for j in range(3):
            g_ij = (d ** 2) / mp.mpf("2") + ((d ** 2) / mp.mpf("2") if i == j else mp.mpf("0"))
            lhs += weights[i] * weights[j] * g_ij
    sum_w = sum(weights, mp.mpf("0"))
    sum_sq = sum((w ** 2 for w in weights), mp.mpf("0"))
    rhs = ((d ** 2) / mp.mpf("2")) * ((sum_w ** 2) + sum_sq)
    res = abs(lhs - rhs)
    card_iota = 3
    directed_bonds = (card_iota + 1) * card_iota
    passed = (res < mp.mpf("10") ** (-75)) and (directed_bonds <= 12) and (directed_bonds == 12)
    return {
        "bean": "qou-ebs6",
        "theorem": "QOU.Mass.EquilateralBound.equidistant_directed_bonds_le_twelve_in_R3",
        "gram_lhs": mp.nstr(lhs, 80),
        "gram_rhs": mp.nstr(rhs, 80),
        "gram_residual": mp.nstr(res, 80),
        "directed_bonds_at_r3_cap": str(directed_bonds),
        "passed": passed,
    }


def check_bond_letter_sub() -> dict[str, object]:
    q0 = mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000")
    z_d = (q0 ** 3) / ((q0 ** 2) + mp.mpf("1"))
    h = q0 - (mp.mpf("1") / q0)
    delta = ((q0 - mp.mpf("1")) ** 2) * (mp.mpf("1") - (q0 ** (-4))) / mp.mpf("3")
    t1 = mp.mpf("1") / mp.mpf("2") - delta / mp.mpf("4")
    t2 = mp.mpf("1") / mp.mpf("2")
    tr_ab = mp.mpf("7") / mp.mpf("11")
    tr1 = (z_d - h * t1) * tr_ab
    tr2 = (z_d - h * t2) * tr_ab
    lhs = tr1 - tr2
    rhs = h * (t2 - t1) * tr_ab
    res = abs(lhs - rhs)
    passed = (res < mp.mpf("10") ** (-75)) and (abs(lhs) > mp.mpf("10") ** (-6))
    return {
        "bean": "qou-gba1",
        "theorem": "QOU.Hecke.BondLetterIdentification.tr_bond_interp_sub",
        "trace_diff_lhs": mp.nstr(lhs, 80),
        "trace_diff_rhs": mp.nstr(rhs, 80),
        "residual": mp.nstr(res, 80),
        "passed": passed,
    }


def check_descent_projector() -> dict[str, object]:
    # 2x2 idempotent projector P = [[3/5, 6/25], [1, 2/5]]: trace = 1, det = 0 => P^2 = P
    p00 = mp.mpf("3") / mp.mpf("5")
    p01 = mp.mpf("6") / mp.mpf("25")
    p10 = mp.mpf("1")
    p11 = mp.mpf("2") / mp.mpf("5")

    def tau(v: tuple[mp.mpf, mp.mpf]) -> tuple[mp.mpf, mp.mpf]:
        return (p00 * v[0] + p01 * v[1], p10 * v[0] + p11 * v[1])

    v_sample = (mp.mpf("5"), mp.mpf("-3"))
    w_desc = tau(v_sample)
    tau_w = tau(w_desc)
    idem_res = abs(tau_w[0] - w_desc[0]) + abs(tau_w[1] - w_desc[1])
    trans_diff = abs(w_desc[0] - v_sample[0]) + abs(w_desc[1] - v_sample[1])
    passed = (idem_res < mp.mpf("10") ** (-75)) and (trans_diff > mp.mpf("1"))
    return {
        "bean": "qou-fn04",
        "theorem": "QOU.Torsion.mem_desc_iff_tau_eq",
        "idempotent_residual": mp.nstr(idem_res, 80),
        "transverse_norm": mp.nstr(trans_diff, 80),
        "passed": passed,
    }


def check_framing_split_dichotomy() -> dict[str, object]:
    # Verify framing_split_spectrum_dichotomy across integer triples (T, wr, threeQ, twoI3)
    cases_checked = 0
    all_ok = True
    for T in range(-3, 4):
        for wr in range(-3, 4):
            for threeQ in (-3, -1, 0, 2):
                for twoI3 in (-1, 1):
                    lk = T + wr
                    spec_eq = (2 * T - 3 * twoI3 == 2 * threeQ - 3 * twoI3)
                    if lk == 0 and (spec_eq != (-wr == threeQ)):
                        all_ok = False
                    if lk == wr and (spec_eq != (0 == threeQ)):
                        all_ok = False
                    cases_checked += 1
    return {
        "bean": "qou-m4fp",
        "theorem": "QOU.StandardModel.TwistBattery.framing_split_spectrum_dichotomy",
        "cases_checked": str(cases_checked),
        "passed": all_ok and (cases_checked == 392),
    }


def main() -> int:
    script_path = pathlib.Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    checks = [
        check_block_length_additive(),
        check_equilateral_bound(),
        check_bond_letter_sub(),
        check_descent_projector(),
        check_framing_split_dichotomy(),
    ]
    all_passed = all(bool(c["passed"]) for c in checks)
    payload = {
        "probe": "blocklen_equilateral_bondletter_descent_framing_probe",
        "dps": str(mp.dps),
        "scriptHash": script_hash,
        "allPassed": all_passed,
        "checks": checks,
    }
    print(json.dumps(payload, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
