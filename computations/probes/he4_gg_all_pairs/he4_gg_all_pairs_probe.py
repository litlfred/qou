#!/usr/bin/env python3
"""he4_gg_all_pairs_probe.py: light nuclei with the gamma-gamma bond G^3 on every
pair (issue #8960, step 3). Pre-registered in preregistration.md.

Reuses the word builders of ../he4_all_pairs_formation (same blocks, same
transports, same route lists) with the single-crossing bond letter replaced by
G^3 = (sigma_{3j-1} sigma_{3j}^-1)^3. Nothing tuned; AME is comparison only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(HERE.parent / "he4_all_pairs_formation"))

import _path_bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_general_word import chi_all_lambda_any, chi_all_lambda_general  # noqa: E402
from tr_m_atom_via_transfer import _trM, tr_m_atom_zn  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0, Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import mass_binding_dashboard as mbd  # noqa: E402
from codata_constants import (  # noqa: E402  (comparison only)
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
)
from he4_all_pairs_formation_probe import ROUTES_HE4, ROUTES_A3  # noqa: E402

DPS = 50
T0 = time.time()
MU_PN_G3 = mp.mpf("1.00061119140688077961351843904")  # gamma-gamma-bond-is-pair-independent


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def G3(j, h):
    one, zero = mp.mpf(1), mp.mpf(0)
    i = 3 * j - 1
    return [(one, zero, i), (one, -h, i + 1)] * 3


def transported_G3(i, j, variant, h):
    one, zero = mp.mpf(1), mp.mpf(0)
    gens = list(range(3 * i + 2, 3 * j - 1))
    up, down = ((one, zero), (one, -h)) if variant == "over" else ((one, -h), (one, zero))
    return ([(up[0], up[1], g) for g in gens] + G3(j, h)
            + [(down[0], down[1], g) for g in reversed(gens)])


def build(Z, N, bonds, variant, h, appended=False):
    A = Z + N
    free = list(atom_braid_word_3A(Z, N, include_inter=False))
    if appended:
        w = free[:]
        for i, j in bonds:
            w += transported_G3(i, j, variant, h)
        return w
    per = len(free) // A
    blocks = [free[k * per:(k + 1) * per] for k in range(A)]
    after = {k: [] for k in range(A)}
    J = 0
    for i, j in bonds:
        J = max(J, j)
        after[J] += transported_G3(i, j, variant, h)
    w = []
    for k in range(A):
        w += blocks[k] + after[k]
    return w


CHAIN = {(1, 1): [(0, 1)], (1, 2): [(0, 1), (1, 2)], (2, 1): [(0, 1), (1, 2)],
         (2, 2): [(0, 1), (1, 2), (2, 3)]}
AME = {(1, 1): AME_B_DEUTERON_MEV_VALIDATION, (1, 2): AME_B_TRITIUM_MEV_VALIDATION,
       (2, 1): AME_B_HE3_MEV_VALIDATION, (2, 2): AME_B_HE4_MEV_VALIDATION}
NAME = {(1, 1): "2H", (1, 2): "3H", (2, 1): "3He", (2, 2): "4He"}


def main():
    mp.mp.dps = DPS + 10
    h = mp.mpf(Q_50_DIGIT_STR) - 1 / mp.mpf(Q_50_DIGIT_STR)
    _me, _q0, E0 = mbd._constants()
    E0 = mp.mpf(str(E0))
    log(f"E0 = {mp.nstr(E0, 15)} MeV")
    rows, checks = [], {}
    for (Z, N) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        n = 3 * (Z + N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}

        def tr(word):
            chi = chi_all_lambda_general(word, n, dps=DPS) if n >= 12 else chi_all_lambda_any(word, n, dps=DPS)
            return _trM(chi, y)

        tr_free = tr(list(atom_braid_word_3A(Z, N, include_inter=False)))
        tr_free_prod = tr_m_atom_zn(Z, N)[1]
        checks[NAME[(Z, N)]] = {"free_vs_tr_m_atom_zn": mp.nstr(abs(tr_free - tr_free_prod), 5)}
        ame = mp.mpf(str(AME[(Z, N)]))

        def record(label, variant, bonds, tr_atom, nlet):
            B_log = E0 * mp.log(tr_free / tr_atom)
            B_diff = E0 * (tr_free - tr_atom)
            rows.append({"atom": NAME[(Z, N)], "route": label, "variant": variant, "bonds": bonds,
                         "letters": nlet, "tr_free": mp.nstr(tr_free, 40),
                         "tr_atom": mp.nstr(tr_atom, 40), "ratio_atom_over_free": mp.nstr(tr_atom / tr_free, 30),
                         "B_log_MeV": mp.nstr(B_log, 30), "B_diff_MeV": mp.nstr(B_diff, 30),
                         "AME_over_B_log_comparison": mp.nstr(ame / B_log, 10)})
            log(f"  {NAME[(Z, N)]:4s} {label:16s} {variant:6s} ratio={mp.nstr(tr_atom / tr_free, 15)} "
                f"B_log={mp.nstr(B_log * 1000, 8)} keV B_diff={mp.nstr(B_diff * 1000, 8)} keV ({nlet} letters)")

        w = build(Z, N, CHAIN[(Z, N)], "over", h)
        t_chain = tr(w)
        record("gg chain", "-", CHAIN[(Z, N)], t_chain, len(w))
        if (Z, N) == (1, 1):
            checks["2H"]["mu_pn_vs_pair_witness"] = mp.nstr(abs(t_chain / tr_free - MU_PN_G3), 5)
            log(f"  control mu_pn: |gap| = {checks['2H']['mu_pn_vs_pair_witness']}")
            continue
        if Z + N == 3:
            for variant in ("over", "under"):
                b = ROUTES_A3["all pairs"]
                gap = abs(tr(build(Z, N, b, variant, h, appended=True)) - tr(build(Z, N, b, variant, h)))
                checks[NAME[(Z, N)]][f"arrangement_{variant}"] = mp.nstr(gap, 5)
                log(f"  arrangement {variant}: {mp.nstr(gap, 5)}")
        routes = ROUTES_HE4 if (Z, N) == (2, 2) else ROUTES_A3
        for label, bonds in routes.items():
            for variant in ("over", "under"):
                w = build(Z, N, bonds, variant, h)
                record(label, variant, bonds, tr(w), len(w))

    wb = WitnessBuilder("he4-gg-all-pairs", engine="mpmath (chi_general_word)", output_dir=HERE)
    wb.set_description(
        "PROBE, adopts nothing (issue #8960 step 3, preregistration.md). Light nuclei with the "
        "gamma-gamma bond G^3 = (s_{3j-1} s_{3j}^-1)^3 on the chain and on every pair; "
        "non-neighbours transported over/under. Four 4He formation routes, all rows reported. "
        "AME comparison only.")
    wb.add_data("E0_MeV", mp.nstr(E0, 40))
    wb.add_data("controls", checks)
    wb.add_data("rows", rows)
    wb.add_assertion("deuteron_chain_reproduces_mu_pn_G3",
                     computed=mp.mpf(checks["2H"]["mu_pn_vs_pair_witness"]), expected=0,
                     tolerance=mp.mpf("1e-28"),
                     source="control 1; the reference is stored to 30 significant digits, so 1e-28 (pre-registration said 1e-40, which the stored value cannot support)")
    wb.save({"q0Anchor": "proton"})
    log("witness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
