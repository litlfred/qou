#!/usr/bin/env python3
"""⁴He with every nucleon pair bonded, by formation route (issue #8960).

Pre-registration: `preregistration.md` (this directory), commit d19e01e54, pushed
before any number was computed. Owner ask 2026-11-21: "Not all γγ production
should be on same strands. Look at how He formed."

The production atom word can only bond neighbouring nucleons
(`QOU/Mass/StrandLayoutForcesChain.lean`). Here a bond between nucleons i < j is
the production pair-type letter b on generator 3j−1, conjugated by the braid T
that carries nucleon i's last strand (3i+2) to position 3j−1:

    over : T = σ_{3i+2} ⋯ σ_{3j−2}        under: T = σ⁻¹_{3i+2} ⋯ σ⁻¹_{3j−2}
    bond = T · b · T⁻¹

Everything else is the production word, unmodified. Every pre-registered row is
reported; no row is chosen. AME 2020 appears only in a comparison column.

Usage:
    python3 -u computations/probes/he4_all_pairs_formation/he4_all_pairs_formation_probe.py \
        2>&1 | tee /tmp/he4_all_pairs_formation.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

import _path_bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
from tr_m_atom_via_transfer import _trM, tr_m_atom_zn  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0, Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import mass_binding_dashboard as mbd  # noqa: E402
from codata_constants import (  # noqa: E402  (comparison only)
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
)

DPS = 50
T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def bond_letters(Z: int, N: int) -> dict:
    """Production pair-type letters (c, d), read off the production word.

    The bond letters are the ones `atom_braid_word_3A(include_inter=True)`
    inserts at generators 3k+2; their pair type is fixed by the nucleon order
    (Z protons, then N neutrons). Reading them from the word, rather than
    retyping h and δ, keeps them identical to production by construction.
    """
    free = atom_braid_word_3A(Z, N, include_inter=False)
    atom = atom_braid_word_3A(Z, N, include_inter=True)
    kinds = ["p"] * Z + ["n"] * N
    out: dict = {}
    fi = 0
    for c, d, g in atom:
        if fi < len(free) and (c, d, g) == free[fi]:
            fi += 1
            continue
        k = (g - 2) // 3
        out["".join(sorted(kinds[k] + kinds[k + 1], reverse=True))] = (c, d)
    return out


def sigma_inv_letter(Z: int, N: int):
    """(c, d) for σ⁻¹ = σ − h, read off the production nn letter when present,
    else computed from q at working precision."""
    q = mp.mpf(Q_50_DIGIT_STR)
    return (mp.mpf(1), -(q - 1 / q))


def transported_bond(i: int, j: int, b, variant: str, sinv) -> list:
    """T · b · T⁻¹ joining nucleon i's last strand to nucleon j's first."""
    one, zero = mp.mpf(1), mp.mpf(0)
    gens = list(range(3 * i + 2, 3 * j - 1))  # 3i+2 .. 3j-2
    up = (one, zero) if variant == "over" else sinv
    down = sinv if variant == "over" else (one, zero)
    T = [(up[0], up[1], g) for g in gens]
    Tinv = [(down[0], down[1], g) for g in reversed(gens)]
    return T + [(b[0], b[1], 3 * j - 1)] + Tinv


def pair_type(kinds, i, j) -> str:
    return "".join(sorted(kinds[i] + kinds[j], reverse=True))


def build_atom(Z: int, N: int, bonds, variant: str) -> list:
    kinds = ["p"] * Z + ["n"] * N
    letters = bond_letters(Z, N)
    sinv = sigma_inv_letter(Z, N)
    w = list(atom_braid_word_3A(Z, N, include_inter=False))
    for i, j in bonds:
        w += transported_bond(i, j, letters[pair_type(kinds, i, j)], variant, sinv)
    return w


ROUTES_HE4 = {
    "D+D pairing a": [(0, 2), (1, 3), (0, 1), (2, 3), (1, 2), (0, 3)],
    "D+D pairing b": [(1, 2), (0, 3), (0, 1), (2, 3), (0, 2), (1, 3)],
    "3H+p": [(1, 2), (2, 3), (1, 3), (0, 1), (0, 2), (0, 3)],
    "3He+n": [(0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3)],
}
# D+D stage 1 is the two deuterons; the pre-registration lists them as
# (0,2),(1,3) and (0,3),(1,2). Within a stage, span ascending then left index:
# pairing b's deuterons (1,2) [span 1] then (0,3) [span 3].
ROUTES_A3 = {"all pairs": [(0, 1), (1, 2), (0, 2)]}
CHAIN_APPENDED = {
    (2, 2): [(0, 1), (1, 2), (2, 3)],
    (1, 2): [(0, 1), (1, 2)],
    (2, 1): [(0, 1), (1, 2)],
}
AME = {(1, 2): AME_B_TRITIUM_MEV_VALIDATION, (2, 1): AME_B_HE3_MEV_VALIDATION,
       (2, 2): AME_B_HE4_MEV_VALIDATION}
NAME = {(1, 2): "3H", (2, 1): "3He", (2, 2): "4He"}


def main() -> int:
    mp.mp.dps = DPS + 10
    _me, _q0, E0 = mbd._constants()
    E0 = mp.mpf(str(E0))
    log(f"E0 (tower-summed) = {mp.nstr(E0, 15)} MeV")
    rows = []
    checks = {}
    for (Z, N) in [(1, 2), (2, 1), (2, 2)]:
        n = 3 * (Z + N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
        tr_atom_prod, tr_free_prod = tr_m_atom_zn(Z, N)[:2]
        free = atom_braid_word_3A(Z, N, include_inter=False)
        tr_free = _trM(chi_all_lambda_any(free, n, dps=DPS), y)
        prod = atom_braid_word_3A(Z, N, include_inter=True)
        tr_prod = _trM(chi_all_lambda_any(prod, n, dps=DPS), y)
        checks[NAME[(Z, N)]] = {
            "free_vs_tr_m_atom_zn": mp.nstr(abs(tr_free - tr_free_prod), 5),
            "production_atom_vs_tr_m_atom_zn": mp.nstr(abs(tr_prod - tr_atom_prod), 5),
        }
        log(f"{NAME[(Z, N)]}: control |Δ| free {checks[NAME[(Z, N)]]['free_vs_tr_m_atom_zn']}, "
            f"atom {checks[NAME[(Z, N)]]['production_atom_vs_tr_m_atom_zn']}")

        def record(label, variant, bonds, tr_atom):
            B_log = E0 * mp.log(tr_free / tr_atom)
            B_diff = E0 * (tr_free - tr_atom)
            ame = mp.mpf(str(AME[(Z, N)]))
            row = {"atom": NAME[(Z, N)], "route": label, "variant": variant,
                   "bonds": bonds, "n_bonds": len(bonds),
                   "tr_free": mp.nstr(tr_free, 40), "tr_atom": mp.nstr(tr_atom, 40),
                   "B_log_MeV": mp.nstr(B_log, 30), "B_diff_MeV": mp.nstr(B_diff, 30),
                   "AME_over_B_log_comparison": mp.nstr(ame / B_log, 10) if B_log else None}
            rows.append(row)
            log(f"  {NAME[(Z, N)]:4s} {label:16s} {variant:6s} bonds={len(bonds)} "
                f"tr_atom={mp.nstr(tr_atom, 12)} B_log={mp.nstr(B_log, 8)} "
                f"B_diff={mp.nstr(B_diff, 8)} AME/B_log={mp.nstr(ame / B_log, 5)}")

        record("production (interleaved chain)", "-", [], tr_prod)
        w = build_atom(Z, N, CHAIN_APPENDED[(Z, N)], "over")
        record("chain appended", "-", CHAIN_APPENDED[(Z, N)],
               _trM(chi_all_lambda_any(w, n, dps=DPS), y))
        routes = ROUTES_HE4 if (Z, N) == (2, 2) else ROUTES_A3
        for label, bonds in routes.items():
            for variant in ("over", "under"):
                t = time.time()
                w = build_atom(Z, N, bonds, variant)
                tr_atom = _trM(chi_all_lambda_any(w, n, dps=DPS), y)
                record(label, variant, bonds, tr_atom)
                log(f"    ({len(w)} letters, {time.time() - t:.1f}s)")

    wb = WitnessBuilder("he4-all-pairs-formation", engine="mpmath (chi_general_word)",
                        output_dir=HERE)
    wb.set_description(
        "PROBE, adopts nothing (issue #8960). Light nuclei with every nucleon pair "
        "bonded: non-neighbouring pairs use the production pair letter conjugated by "
        "a strand-transport braid (over/under), bond order fixed by formation route "
        "(D+D two pairings, 3H+p, 3He+n). Pre-registered in preregistration.md. "
        "B_log is the posited log form B_sym uses; B_diff is E0 x trace difference. "
        "AME is comparison only; no route, pairing or variant is selected.")
    wb.add_data("E0_MeV", mp.nstr(E0, 40))
    wb.add_data("controls", checks)
    wb.add_data("rows", rows)
    worst = max(mp.mpf(c["production_atom_vs_tr_m_atom_zn"]) for c in checks.values())
    wb.add_assertion("production_word_reproduces_tr_m_atom_zn",
                     computed=worst, expected=0, tolerance=mp.mpf("1e-40"),
                     source="control 1 of the pre-registration")
    wb.save({"q0Anchor": "proton"})
    log("witness written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
