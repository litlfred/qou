#!/usr/bin/env python3
# polynomial_q_not_applicable: evaluates a closed form at q0; not a q-series compute.
"""Regenerate the Z=1-20 atomic mass table under the PUBLISHED third coefficient.

WHY THIS EXISTS. `tbl:mass-table-z1-20-table-data` quoted twenty predicted masses
that `thm:wedderburn-mass-formula` could not produce. Measured in
`computations/audits/wedderburn_beta3_vs_hA2_discrimination.py` (PR #5773): the
producer's `beta3 = 0.0499` reproduces 20/20 of the published values and the
published `h_A^2` reproduces 0/20. Measured independently in
`computations/wedderburn_beta3_provenance_probe.py` (PR #5763): `h_A^2` has an
exact construction and `0.0499` is reached by none of sixteen pre-declared
candidates. So the coefficient in the formula is the derivable one and the table
was computed with something else. This regenerates the table under the formula.

Authorised by the owner ("go", 2026-08-25) after both measurements landed.

THE COEFFICIENTS ARE LOCKED TOGETHER -- this is why only recomputing `beta3`
would have been incoherent, and it is fresh evidence against `0.0499`:

    [3]_q - 3 = (q^2 + 1 + q^-2) - 3 = q^2 - 2 + q^-2 = (q - q^-1)^2 = h_A^2

so  beta2 = -2[3]_q = -6 - 2*h_A^2  identically, for whatever q is in force.
The recovered witness records `beta2 = -6.087415`, which is `-6 - 2*h_A^2` at
its own `q0` to every digit it carries. Had `0.0499` been the `h_A^2` that
producer believed in, its `beta2` would have had to be `-6.0998`. **The witness
therefore disagrees with its own third coefficient**, in its own arithmetic, and
its second coefficient sides with the published formula.

WHAT IS AND IS NOT RECOMPUTED. The three Wedderburn invariants Phi_1, Phi_2,
Phi_3 are carried in verbatim from the recovered witness -- this script does NOT
re-derive them, and is not a from-scratch computation of the table. It evaluates
the published closed form on those recorded invariants. The base masses are also
carried as recorded, deliberately: see the CAVEAT below.

RE-DERIVING THEM HAS BEEN ATTEMPTED, AND THE GAP IS MEASURED (added 2026-08-29,
bean qou-1jw9). Do not start this from scratch.
`computations/wedderburn_Mi_constructor_test.py` reconstructs the M_i and hence
Phi_1/Phi_2/Phi_3 literally from the three blocks that define them
(def:atomic-braid + tbl:atomic-braid-table1-data + thm:wedderburn-mass-formula's
"chaining the crossing matrices of all strands j > i"). It misses deuterium --
the ONE point the theorem claims exactness, n = A+Z = 3 being the only n where
the three extremal Wedderburn blocks exhaust the partitions -- by 208.5 % under
the literal reading, and by 54 % to 2653 % across all four readings of that
prose.

CORRECTED 2026-08-29: that probe's reading is WRONG, and so was the conclusion I
drew from it. "chaining the crossing matrices of all strands j > i" means an
ALL-PAIRS braid -- for strand i, cross with every strand j > i -- not a suffix
product of adjacent crossings. Under the correct reading Phi_2 and Phi_3 ARE
re-derived, 19 of 19 non-hydrogen rows:

    Phi_3 = (-2Z - N(N-1)) * ln q
    Phi_2 = Z*N * ln(1 + h^2/4)

both convention-free (neither uses the Markov parameter z). See
computations/phi_allpairs_reconstruction.py. Phi_1 is the only invariant that uses z and
is still carried. So the remaining gap is Phi_1 alone, not all three.

q0 CONVENTION. Coefficients are evaluated at the PROTON pin
(`qou_substrate.constants.Q`), per the owner directive of 2026-08-07 that all
production compute defaults to the experimental anchor. The recovered witness
stored `q0 = 1.10998`, a five-decimal rounding that both documented pins share,
so it does not identify an anchor; the rounding carried a 2.4e-5 relative defect
in `h_A^2` which evaluating at the unrounded pin removes.

CAVEAT, NOT FIXED HERE. The recorded `m_p = 938.230457` and `m_n = 939.532005`
are 44 and 36 ppm below CODATA. That is a separate defect from the coefficient,
it was not part of what was authorised, and correcting it would move every row
again -- so it is left as recorded and reported in the witness rather than
silently repaired. `codata_base_mass_delta` records what it would be worth.

NO FITTING. Nothing here is tuned to the observed masses. Every coefficient is
computed from `q0`, `m_e` and Catalan's constant by the formula's own
definitions, and the AME2020 column is used only to report error, never to
choose anything.
"""

from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
# `q_parameter` lives in the `substrate/` cluster subdirectory, not beside this
# file, so the line above does not reach it and the bare-name import below
# raises ModuleNotFoundError from a clean checkout. `_path_bridge` is the
# repo's idiom for that (it puts every cluster subdir on sys.path); importing
# it is what every other producer doing a bare-name cross-cluster import does.
# Added 2026-08-29, bean qou-1jw9 — verified pre-existing against pristine
# origin/main, which fails identically.
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.constants import Q as Q_PROTON  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from codata_constants import M_N_MEV_VALIDATION, M_P_MEV_VALIDATION
from codata_constants import M_C12_ATOMIC_MEV_VALIDATION, M_HE4_ATOMIC_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

mp.dps = 50

# --- inputs carried from the recovered producer witness -----------------------
# git show 1359fe23ac:folio-assistant/computations/atom-mass-complete-wedderburn.witness.json
SOURCE_COMMIT = "1359fe23ac"
SOURCE_PATH = "folio-assistant/computations/atom-mass-complete-wedderburn.witness.json"

M_E = "0.510999"        # recorded; CODATA 0.51099895
M_P = "938.230457"      # recorded; CODATA M_P_MEV_VALIDATION  (-44 ppm)
M_N = "939.532005"      # recorded; CODATA M_N_MEV_VALIDATION  (-36 ppm)
CODATA_M_P = "938.27208816"
CODATA_M_N = "939.56542052"

# atom, Z, N, Phi1, Phi2, Phi3, M_obs (AME2020 as recorded), published M_pred
ROWS = [
    ("H",  1,  1,  0, "-0.007015",  "-0.0",     "1.04342",    "938.78313",   "938.910"),
    ("He", 2,  2,  2, "-5.558902",  "0.04347",  "-0.626052",  _ame_nstr(M_HE4_ATOMIC_MEV_VALIDATION, 30),   "3734.624"),
    ("Li", 3,  3,  4, "-9.838642",  "0.130411", "-1.878156",  "6535.367",    "6534.188"),
    ("Be", 4,  4,  5, "-18.272718", "0.217351", "-2.921576",  "8394.7937",   "8378.704"),
    ("B",  5,  5,  6, "-22.803608", "0.326027", "-4.17368",   "10255.103",   "10237.301"),
    ("C",  6,  6,  6, "-24.310734", "0.391232", "-4.382364",  _ame_nstr(M_C12_ATOMIC_MEV_VALIDATION, 30),  "11168.874"),
    ("N",  7,  7,  7, "-27.961737", "0.53251",  "-5.843152",  "13043.7816",  "13029.983"),
    ("O",  8,  8,  8, "-31.574308", "0.695523", "-7.512624",  "14899.1693",  "14890.701"),
    ("F",  9,  9, 10, "-34.397752", "0.97808",  "-11.268936", "17696.901",   "17690.792"),
    ("Ne", 10, 10, 10, "-37.5487",  "1.086755", "-11.47762",  "18622.8354",  "18615.219"),
    ("Na", 11, 11, 12, "-39.146787", "1.434517", "-16.068668", "21414.8301", "21418.256"),
    ("Mg", 12, 12, 12, "-42.17203", "1.564928", "-16.277352", "22341.908",   "22342.658"),
    ("Al", 13, 13, 14, "-44.011395", "1.977895", "-21.703135", "25133.1432", "25143.149"),
    ("Si", 14, 14, 14, "-46.806126", "2.130041", "-21.911819", "26060.3443", "26067.918"),
    ("P",  15, 15, 16, "-47.062156", "2.608213", "-28.172339", "28851.873",  "28872.696"),
    ("S",  16, 16, 16, "-49.798916", "2.782094", "-28.381023", "29781.8",    "29797.187"),
    ("Cl", 17, 17, 18, "-50.698281", "3.325472", "-35.476279", "32573.283",  "32597.913"),
    ("Ar", 18, 18, 22, "-49.526301", "4.303551", "-51.962315", "37224.719",  "37273.796"),
    ("K",  19, 19, 20, "-53.364492", "4.129671", "-43.614955", "36294.464",  "36324.625"),
    ("Ca", 20, 20, 20, "-55.937487", "4.347022", "-43.823639", "37213.777",  "37248.739"),
]


def s(x, n=16):
    """Serialize an mpf as a decimal string. Never through float."""
    return mp.nstr(x, n, strip_zeros=False)


def main() -> int:
    q0 = Q_MP
    m_e, m_p, m_n = mpf(M_E), mpf(M_P), mpf(M_N)

    # coefficients, all from q0 / m_e / Catalan by the formula's own definitions
    catalan = mp.catalan
    alpha = m_e * 8 * catalan
    h_A = q0 - 1 / q0
    h_A2 = h_A ** 2
    three_q = (q0 ** 3 - q0 ** -3) / (q0 - 1 / q0)
    beta2 = -2 * three_q

    lock_residual = abs(beta2 - (-6 - 2 * h_A2))

    wb = WitnessBuilder("wedderburn-mass-table-z1-20", engine="mpmath")
    wb.set_description(
        "Z=1-20 atomic masses from thm:wedderburn-mass-formula evaluated at the "
        "proton-pin q0 on the Wedderburn invariants recorded in the recovered "
        "atom-mass-complete-wedderburn witness. Replaces a published table that "
        "was computed with an unattributed third coefficient (beta3=0.0499)."
    )
    wb.set_content_block("tbl:mass-table-z1-20-table-data")
    wb.add_parameter("q0", s(q0, 20))
    wb.add_parameter("q0_anchor", "physical_proton")
    wb.add_parameter("m_e_MeV", M_E)
    wb.add_parameter("m_p_MeV", M_P)
    wb.add_parameter("m_n_MeV", M_N)
    wb.add_parameter("alpha", s(alpha, 20))
    wb.add_parameter("beta2", s(beta2, 20))
    wb.add_parameter("h_A_squared", s(h_A2, 20))
    wb.add_parameter("fitted_parameters", 0)
    wb.add_parameter("upstream_invariants_source", f"{SOURCE_PATH}@{SOURCE_COMMIT}")

    results, max_pct, tot_pct = [], mpf(0), mpf(0)
    max_shift = mpf(0)
    for el, Z, _z2, N, p1, p2, p3, obs, published in ROWS:
        phi1, phi2, phi3 = mpf(p1), mpf(p2), mpf(p3)
        m_obs, m_pub = mpf(obs), mpf(published)
        m_pred = (Z * m_p + N * m_n + Z * m_e
                  + alpha * (phi1 + beta2 * phi2 + h_A2 * phi3))
        delta = m_pred - m_obs
        pct = delta / m_obs * 100
        tot_pct += abs(pct)
        max_pct = max(max_pct, abs(pct))
        max_shift = max(max_shift, abs(m_pred - m_pub))
        results.append({
            "element": el, "Z": Z, "N": N, "A": Z + N,
            "M_pred_MeV": s(m_pred, 12),
            "M_obs_MeV": obs,
            "delta_MeV": s(delta, 8),
            "delta_pct": s(pct, 6),
            "M_published_superseded": published,
            "shift_from_published_MeV": s(m_pred - m_pub, 8),
        })

    n = len(ROWS)
    mean_pct = tot_pct / n
    wb.add_data("results", results)
    wb.add_data("summary", {
        "n_atoms": n,
        "mean_abs_pct": s(mean_pct, 8),
        "max_abs_pct": s(max_pct, 8),
        "max_shift_from_published_MeV": s(max_shift, 8),
    })
    wb.add_data("coefficient_lock", {
        "identity": "[3]_q - 3 == (q - 1/q)^2, hence beta2 == -6 - 2*h_A^2",
        "residual": s(lock_residual, 6),
        "superseded_beta3": "0.0499",
        "beta2_that_0.0499_would_force": s(-6 - 2 * mpf("0.0499"), 12),
        "beta2_recorded_by_producer": "-6.087415",
        "note": ("the producer's recorded beta2 agrees with the PUBLISHED h_A^2, "
                 "not with its own beta3 -- the superseded witness contradicts "
                 "its third coefficient in its own arithmetic"),
    })
    dmp = mpf(CODATA_M_P) - m_p
    dmn = mpf(CODATA_M_N) - m_n
    wb.add_data("codata_base_mass_delta", {
        "delta_m_p_MeV": s(dmp, 8),
        "delta_m_n_MeV": s(dmn, 8),
        "shift_at_Ca40_MeV": s(20 * dmp + 20 * dmn, 8),
        "note": "NOT applied; a separate defect from the coefficient, left as recorded",
    })

    wb.add_assertion(
        "coefficient_lock_holds",
        s(lock_residual, 6), "0.0", tolerance="1e-40",
        source="beta2 == -6 - 2*h_A^2, identically in q",
    )
    wb.add_assertion(
        "mean_abs_error_under_one_tenth_percent",
        s(mean_pct, 8), "0.0", tolerance="0.1", unit="percent",
        source="AME2020; reported only, never used to choose a coefficient",
    )
    wb.add_caveat(
        "Phi_1/Phi_2/Phi_3 are carried verbatim from the recovered witness at "
        f"{SOURCE_COMMIT}; this script evaluates the closed form on them and does "
        "not re-derive the invariants."
    )
    wb.add_caveat(
        "Base masses are the producer's recorded values, 44/36 ppm below CODATA. "
        "Not corrected here; see codata_base_mass_delta."
    )

    out = wb.save()
    print(f"mean |delta|/m = {s(mean_pct, 6)} %   max = {s(max_pct, 6)} %")
    print(f"max shift from the superseded table = {s(max_shift, 6)} MeV")
    print(f"coefficient-lock residual = {s(lock_residual, 6)}")
    print(f"witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
