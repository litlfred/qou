#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q = q_0, not symbolic.
"""mu3_door_sign_C_vs_D_probe.py — does the mu_3 door's RECORDED SIGN survive
the convention-D resolution?

MEASUREMENT ONLY.  Nothing tuned; no production value changed.

THE RECORDED CONCLUSION UNDER TEST
----------------------------------
`computations/deltalambda/mu3_abs_choice_robustness_probe.py` records a
verdict that is a SIGN, not a magnitude:

    d2g = sum_lambda y_lambda * (chi_ab - chi_a - chi_b - + chi_empty)
    c3  = -E_0 * d2g
    door = "OPEN (submodular)"    if d2g < 0
           "CLOSED (supermodular)" if d2g > 0

where chi_S is the character of the A=3 atomic braid word with the
inter-nucleon crossings in S included, and the two interfaces are the two
generators g with g % 3 == 2.  The A=3 magnitude target r* = mu3/c3 ~ 1.585
(#4320 / #4364) is built on this c3.

d2g is a y_lambda-WEIGHTED sum over lambda |- 9.  Under convention D,
25 of the 30 weights are identically zero (only the 5 two-row partitions of 9
survive).  A sign is not protected by a reweighting, so this is exactly the
class of recorded conclusion that can flip.  This probe checks whether it does.

The three-way outcome is reported honestly:
  - same sign  -> the door verdict is convention-robust (a strengthening);
  - flipped    -> a recorded verdict is convention-dependent (a serious
                  finding: the door's status would be an artifact of z_C);
  - c3 moves   -> r* ~ 1.585 is a C-convention number and any probe targeting
                  it is targeting a convention-dependent value.

PIN: EXPERIMENTAL / proton, q_parameter.Q_50_DIGIT_STR.  y_lambda live from
the Wenzl-bridge closed form at each z; chi live from Hoefsmit at the proton
q_0.  No muon-built cache (the upstream probe's `_Y9` is not read).

Ref: computations/deltalambda/mu3_abs_choice_robustness_probe.py (the verdict)
Ref: computations/deltalambda/vassiliev_magnitude_a3_probe.py (r* ~ 1.585)
Ref: docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md
Ref: docs/audits/2026-08-07-mu3-door-status-consolidated.md
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    classical_dim, partitions_of, schur_principal,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from tr_m_wenzl_bridge_mpfr import (  # noqa: E402
    _build_seminormal_matrices_mpf, _chi_lambda_of_word_mpf,
)

# RAISE PRECISION AT MODULE SCOPE, before any mpf is built.
# `set_compute_dps()` was called only inside main() (below), while
# UPSTREAM_C3_ABS builds two mpf at module scope -- so both were constructed at
# mpmath's default 15 dps and carry 15-dps binary precision for the rest of the
# run. `mpf_import_time_dps_audit` proves this statically (literal arg), and
# these two were the ONLY "proven lossy" sites left on main and the only NEW
# file the audit's baseline had not seen. Bean qou-j6gb.
set_compute_dps()

T0 = time.time()
# The upstream probe's recorded c_3 values (|chi| variant).  This probe must
# reproduce them in convention C before its D numbers mean anything:
#   mu3_abs_choice_robustness_probe.py:53  EXPECT = {"T": -1.769, "3He": -1.405}
UPSTREAM_C3_ABS = {"T": mp.mpf("-1.769"), "3He": mp.mpf("-1.405")}


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def z_C(q):
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def z_D(q):
    return q ** 3 / (q ** 2 + 1)


def y_vector_at_z(n, q, z):
    Q = q ** 2
    X = q * z / (1 - Q + q * z)
    parts = [tuple(p) for p in partitions_of(n)]
    s = {p: schur_principal(list(p), X, Q) for p in parts}
    norm = sum(classical_dim(list(p)) * s[p] for p in parts)
    return {p: s[p] / norm for p in parts}


def main() -> int:
    set_compute_dps()
    q = Q_MP
    # E_0 is the UNIT-CELL scale m_e/(q_0(q_0-1)) ~ 4.186 MeV, exactly as the
    # upstream probe defines it (mu3_abs_choice_robustness_probe.py:48) -- NOT
    # Q_NEUTRON_MEV.  A wrong E_0 leaves the SIGN and every RATIO below correct
    # but makes c_3 incomparable to the recorded value, so the reproduction
    # gate would fail for a reason that has nothing to do with the convention.
    e0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    log(f"proton pin q_0 = {Q_50_DIGIT_STR}  (dps={mp.mp.dps})")
    log(f"E_0 = {mp.nstr(e0, 20)} MeV  (= m_e/(q_0(q_0-1)), unit-cell scale)")
    zc, zd = z_C(q), z_D(q)
    log(f"z_C = {mp.nstr(zc, 20)}   z_D = {mp.nstr(zd, 20)}")

    parts9 = [tuple(p) for p in partitions_of(9)]
    yC, yD = y_vector_at_z(9, q, zc), y_vector_at_z(9, q, zd)
    zero_tol = mp.mpf("1e-40")
    n_zero_D = sum(1 for l in parts9 if abs(yD[l]) < zero_tol)
    log(f"n=9: {len(parts9)} partitions; y_D vanishes on {n_zero_D} "
        f"(the >2-row blocks)")

    results = {}
    for name, (Z, N) in (("T", (1, 2)), ("3He", (2, 1))):
        full = atom_braid_word_3A(Z, N, include_inter=True)
        ga, gb = sorted({x[2] for x in full if x[2] % 3 == 2})
        log(f"{name}: interfaces at generators {ga}, {gb}")

        subwords = {
            "empty": [x for x in full if x[2] % 3 != 2],
            "a": [x for x in full if x[2] % 3 != 2 or x[2] == ga],
            "b": [x for x in full if x[2] % 3 != 2 or x[2] == gb],
            "ab": list(full),
        }
        chi = {k: {} for k in subwords}
        for lam in parts9:
            sig, dim = _build_seminormal_matrices_mpf(lam, q)
            for k, w in subwords.items():
                chi[k][lam] = (mp.mpf(0) if dim == 0
                               else _chi_lambda_of_word_mpf(sig, dim, w, q=q))
        log(f"  {name}: characters done for 4 sub-words x {len(parts9)} blocks")

        row = {"atom": name, "interfaces": [ga, gb],
               "n_partitions": len(parts9), "n_y_D_zero": n_zero_D}
        for tag, y in (("C", yC), ("D", yD)):
            for variant, tf in (("abs", abs), ("raw", lambda v: v)):
                d2 = sum(y[l] * (tf(chi["ab"][l]) - tf(chi["a"][l])
                                 - tf(chi["b"][l]) + tf(chi["empty"][l]))
                         for l in parts9)
                c3 = -e0 * d2
                door = ("OPEN (submodular)" if d2 < 0
                        else "CLOSED (supermodular)")
                row[f"{tag}_{variant}"] = {
                    "d2g": mp.nstr(d2, 20), "c3_MeV": mp.nstr(c3, 20),
                    "submodular": bool(d2 < 0), "door": door,
                }
                log(f"  {name} [{tag}/{variant:3s}]  d2g = {mp.nstr(d2, 12):>18s}"
                    f"   c3 = {mp.nstr(c3, 10):>14s} MeV   door {door}")
        # GATE: the C-convention c_3 must reproduce the upstream recorded value
        # before any D number here is meaningful.
        c3C_abs = mp.mpf(row["C_abs"]["c3_MeV"])
        row["upstream_recorded_c3_abs"] = mp.nstr(UPSTREAM_C3_ABS[name], 10)
        row["reproduces_upstream_c3"] = bool(
            abs(c3C_abs - UPSTREAM_C3_ABS[name]) < mp.mpf("0.01"))
        log(f"  {name}: C/abs c3 = {mp.nstr(c3C_abs, 10)} vs recorded "
            f"{mp.nstr(UPSTREAM_C3_ABS[name], 6)}  -> reproduces: "
            f"{row['reproduces_upstream_c3']}")
        for variant in ("abs", "raw"):
            sc = row[f"C_{variant}"]["submodular"]
            sd = row[f"D_{variant}"]["submodular"]
            row[f"sign_preserved_{variant}"] = bool(sc == sd)
            c3C = mp.mpf(row[f"C_{variant}"]["c3_MeV"])
            c3D = mp.mpf(row[f"D_{variant}"]["c3_MeV"])
            row[f"c3_D_over_C_{variant}"] = (
                mp.nstr(c3D / c3C, 12) if c3C != 0 else None)
            # r* = mu3/c3 with mu3 held fixed (mu3 is the AdditiveResidualSimplex
            # value, not a Hecke trace, so it is not reweighted here).
            row[f"r_star_scale_factor_{variant}"] = (
                mp.nstr(c3C / c3D, 12) if c3D != 0 else None)
            log(f"  {name} [{variant}] sign preserved: "
                f"{row[f'sign_preserved_{variant}']}   "
                f"c3 D/C = {row[f'c3_D_over_C_{variant}']}   "
                f"=> r* would scale by {row[f'r_star_scale_factor_{variant}']}")
        results[name] = row

    wb = WitnessBuilder("mu3-door-sign-c-vs-d", engine="mpmath")
    wb.add_parameter("q_0", Q_50_DIGIT_STR)
    wb.add_parameter("q_0_pin", "experimental/proton "
                                "(q_parameter.Q_50_DIGIT_STR)")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_parameter("uses_experimental_target_values_as_input", False)
    wb.add_parameter("E_0_MeV", mp.nstr(e0, 25))
    wb.add_parameter("E_0_definition",
                     "m_e/(q_0(q_0-1)) - unit-cell scale, per "
                     "mu3_abs_choice_robustness_probe.py:48")
    wb.add_parameter("z_C", mp.nstr(zc, 30))
    wb.add_parameter("z_D", mp.nstr(zd, 30))
    for name, row in results.items():
        wb.add_data(name, row)
        wb.add_assertion(
            f"{name}_reproduces_upstream_c3_in_convention_C",
            1 if row["reproduces_upstream_c3"] else 0, 1,
            source="the C-convention c_3 must match the recorded "
                   "mu3_abs_choice_robustness_probe EXPECT value before the "
                   "D-convention numbers here mean anything",
        )
        wb.add_assertion(
            f"{name}_door_sign_preserved_abs_variant",
            1 if row["sign_preserved_abs"] else 0, 1,
            source="whether the recorded mu_3 door verdict (submodular vs "
                   "supermodular, i.e. the SIGN of Delta^2 g) is the same "
                   "under convention D as under convention C",
        )
    wb.set_description(
        "Does the recorded mu_3 door verdict -- a SIGN (Delta^2 g < 0 => door "
        "OPEN/submodular) -- survive the convention-D resolution? Delta^2 g is "
        "a y_lambda-weighted sum over lambda |- 9, and convention D zeroes 25 "
        "of the 30 weights, so the sign is not protected. Also reports how far "
        "c_3 moves, hence how far the A=3 magnitude target r* ~ 1.585 moves. "
        "Proton pin. Measurement only."
    )
    wb.set_content_block("prop:h3-markov-wenzl-weights")
    log(f"witness -> {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
