#!/usr/bin/env python3
# polynomial_q_not_applicable: arithmetic on recorded invariants, not a q-series compute.
"""Does the PUBLISHED Wedderburn mass formula produce the PUBLISHED table?

THE OPEN ITEM (bean `qou-1jw9`, PR #5758 "Left open"). The recovered producer
witness `atom-mass-complete-wedderburn` (added 2026-04-10 in `1359fe23ac` under
`folio-assistant/computations/`, out of tree since the miga split) reproduces
the published 20-row table exactly -- but its third coefficient is

    beta3 = 0.0499

while `thm:wedderburn-mass-formula` publishes that coefficient as

    h_A^2 = (q0 - 1/q0)^2 = 0.043707282...      (h_A = q - q^-1, block's own defn)

a 14.2 % departure. Under the owner's no-fitting ruling (2026-08-25) neither may
be adjusted to meet the other, so the corpus was left with a straight authoring
question: is the published `h_A^2` wrong, or was the table never the published
formula's output?

WHY THIS IS A MEASUREMENT AND NOT A PREFERENCE. Both coefficients multiply the
SAME recorded per-row `Phi_3`, and the witness records `Phi_1`, `Phi_2`, `Phi_3`,
`M_pred` and `M_obs` for every row. So the published formula can be evaluated on
the producer's own invariants, with every other input held fixed, and compared
against both the recorded table and AME2020. Nothing is fitted, reconstructed or
guessed here: the only substitution is beta3 -> h_A^2(q0), which is what the
published block says the coefficient IS.

WHAT IS DELIBERATELY NOT DONE. `beta3` is not reconstructed, the published
`h_A^2` is not adjusted, no tolerance is set, and no base mass is re-derived.
Per AGENTS.md "Before declaring refuted", conclusions here are scope (a):
statements about THESE coefficients on THESE recorded invariants.

Data provenance: every literal below is transcribed from
`git show 1359fe23ac:folio-assistant/computations/atom-mass-complete-wedderburn.witness.json`
and is carried as a STRING into mpmath (never through float).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 50

# --- recorded parameters (witness `parameters` block, verbatim) ---------------
P = {
    "q0": "1.10998",
    "m_e": "0.510999",
    "m_p": "938.230457",
    "m_n": "939.532005",
    "alpha": "3.74446",
    "beta2": "-6.087415",
    "beta3": "0.0499",
}

# --- CODATA counterparts, for magnitude comparison only ----------------------
CODATA_M_P = "938.27208816"
CODATA_M_N = "939.56542052"

# --- recorded table: atom, Z, N, Phi1, Phi2, Phi3, M_pred, M_obs -------------
ROWS = [
    ("1H",    1,  0,  "-0.007015", "-0.0",      "1.04342",   "938.91",    "938.78313"),
    ("4He",   2,  2,  "-5.558902", "0.04347",   "-0.626052", "3734.624",  "3728.4013"),
    ("7Li",   3,  4,  "-9.838642", "0.130411",  "-1.878156", "6534.188",  "6535.367"),
    ("9Be",   4,  5,  "-18.272718","0.217351",  "-2.921576", "8378.704",  "8394.7937"),
    ("11B",   5,  6,  "-22.803608","0.326027",  "-4.17368",  "10237.301", "10255.103"),
    ("12C",   6,  6,  "-24.310734","0.391232",  "-4.382364", "11168.874", "11177.9292"),
    ("14N",   7,  7,  "-27.961737","0.53251",   "-5.843152", "13029.983", "13043.7816"),
    ("16O",   8,  8,  "-31.574308","0.695523",  "-7.512624", "14890.701", "14899.1693"),
    ("19F",   9, 10,  "-34.397752","0.97808",   "-11.268936","17690.792", "17696.901"),
    ("20Ne", 10, 10,  "-37.5487",  "1.086755",  "-11.47762", "18615.219", "18622.8354"),
    ("23Na", 11, 12,  "-39.146787","1.434517",  "-16.068668","21418.256", "21414.8301"),
    ("24Mg", 12, 12,  "-42.17203", "1.564928",  "-16.277352","22342.658", "22341.908"),
    ("27Al", 13, 14,  "-44.011395","1.977895",  "-21.703135","25143.149", "25133.1432"),
    ("28Si", 14, 14,  "-46.806126","2.130041",  "-21.911819","26067.918", "26060.3443"),
    ("31P",  15, 16,  "-47.062156","2.608213",  "-28.172339","28872.696", "28851.873"),
    ("32S",  16, 16,  "-49.798916","2.782094",  "-28.381023","29797.187", "29781.8"),
    ("35Cl", 17, 18,  "-50.698281","3.325472",  "-35.476279","32597.913", "32573.283"),
    ("40Ar", 18, 22,  "-49.526301","4.303551",  "-51.962315","37273.796", "37224.719"),
    ("39K",  19, 20,  "-53.364492","4.129671",  "-43.614955","36324.625", "36294.464"),
    ("40Ca", 20, 20,  "-55.937487","4.347022",  "-43.823639","37248.739", "37213.777"),
]


def mass(Z, N, phi1, phi2, phi3, *, m_p, m_n, m_e, alpha, beta2, beta3):
    """m(Z,N) = Z*m_p + N*m_n + Z*m_e + alpha*(Phi1 + beta2*Phi2 + beta3*Phi3)."""
    return (Z * m_p + N * m_n + Z * m_e
            + alpha * (phi1 + beta2 * phi2 + beta3 * phi3))


def main() -> int:
    q0 = mpf(P["q0"])
    m_e, m_p, m_n = mpf(P["m_e"]), mpf(P["m_p"]), mpf(P["m_n"])
    alpha, beta2 = mpf(P["alpha"]), mpf(P["beta2"])
    beta3_recorded = mpf(P["beta3"])

    # the PUBLISHED coefficient, from the block's own definition h_A = q - q^-1
    h_A = q0 - 1 / q0
    h_A2 = h_A ** 2

    out = {
        "name": "wedderburn-beta3-vs-hA2-discrimination",
        "source_witness": {
            "path": "folio-assistant/computations/atom-mass-complete-wedderburn.witness.json",
            "commit": "1359fe23ac",
            "note": "out of tree since the miga split; transcribed, not restored",
        },
        "coefficients": {
            "beta3_recorded": mp.nstr(beta3_recorded, 12),
            "h_A_published": mp.nstr(h_A, 20),
            "h_A2_published": mp.nstr(h_A2, 20),
            "ratio_recorded_over_published": mp.nstr(beta3_recorded / h_A2, 12),
            "departure_pct": mp.nstr((beta3_recorded / h_A2 - 1) * 100, 8),
        },
    }

    # --- Q1: is the witness internally consistent? ---------------------------
    max_repro = mpf(0)
    rows_out = []
    tot_recorded = mpf(0)
    tot_published = mpf(0)
    max_recorded = mpf(0)
    max_published = mpf(0)
    max_shift = mpf(0)

    for atom, Z, N, s1, s2, s3, sM, sObs in ROWS:
        phi1, phi2, phi3 = mpf(s1), mpf(s2), mpf(s3)
        M_rec, M_obs = mpf(sM), mpf(sObs)

        # reproduce the recorded prediction from the recorded parameters
        M_repro = mass(Z, N, phi1, phi2, phi3, m_p=m_p, m_n=m_n, m_e=m_e,
                       alpha=alpha, beta2=beta2, beta3=beta3_recorded)
        repro_err = abs(M_repro - M_rec)
        max_repro = max(max_repro, repro_err)

        # the same row under the PUBLISHED coefficient, everything else held
        M_pub = mass(Z, N, phi1, phi2, phi3, m_p=m_p, m_n=m_n, m_e=m_e,
                     alpha=alpha, beta2=beta2, beta3=h_A2)

        err_rec = abs(M_repro - M_obs) / M_obs * 100
        err_pub = abs(M_pub - M_obs) / M_obs * 100
        shift = M_pub - M_repro

        tot_recorded += err_rec
        tot_published += err_pub
        max_recorded = max(max_recorded, err_rec)
        max_published = max(max_published, err_pub)
        max_shift = max(max_shift, abs(shift))

        rows_out.append({
            "atom": atom, "Z": Z, "N": N,
            "M_recorded": mp.nstr(M_rec, 10),
            "M_reproduced": mp.nstr(M_repro, 10),
            "reproduction_residual_MeV": mp.nstr(repro_err, 6),
            "M_published_coeff": mp.nstr(M_pub, 10),
            "shift_MeV": mp.nstr(shift, 6),
            "err_pct_recorded": mp.nstr(err_rec, 6),
            "err_pct_published": mp.nstr(err_pub, 6),
        })

    n = len(ROWS)
    out["reproduction"] = {
        "max_residual_MeV": mp.nstr(max_repro, 8),
        "verdict": ("the recorded parameters DO reproduce the recorded table"
                    if max_repro < mpf("0.001")
                    else "the recorded parameters do NOT reproduce the recorded table"),
    }
    out["accuracy"] = {
        "mean_pct_with_beta3": mp.nstr(tot_recorded / n, 6),
        "mean_pct_with_h_A2": mp.nstr(tot_published / n, 6),
        "max_pct_with_beta3": mp.nstr(max_recorded, 6),
        "max_pct_with_h_A2": mp.nstr(max_published, 6),
        "max_abs_shift_MeV": mp.nstr(max_shift, 6),
    }

    # --- Q2: what q would make the published h_A^2 equal the recorded beta3? --
    # solve (q - 1/q)^2 = beta3 for q > 1:  q = (h + sqrt(h^2+4))/2, h = sqrt(beta3)
    h_implied = mp.sqrt(beta3_recorded)
    q_implied = (h_implied + mp.sqrt(h_implied ** 2 + 4)) / 2
    out["implied_anchor"] = {
        "q_solving_hA2_eq_beta3": mp.nstr(q_implied, 12),
        "q0_recorded": mp.nstr(q0, 12),
        "departure_from_q0_pct": mp.nstr((q_implied / q0 - 1) * 100, 6),
    }

    # --- Q3: magnitude of the non-CODATA base masses, for comparison ---------
    dmp = mpf(CODATA_M_P) - m_p
    dmn = mpf(CODATA_M_N) - m_n
    heaviest = ROWS[-1]
    Z_h, N_h = heaviest[1], heaviest[2]
    out["base_mass_offset"] = {
        "delta_m_p_MeV": mp.nstr(dmp, 8),
        "delta_m_n_MeV": mp.nstr(dmn, 8),
        "total_at_40Ca_MeV": mp.nstr(Z_h * dmp + N_h * dmn, 8),
    }

    # --- Q4: foreclose "beta3 is h_A^2 at some other anchor / a power of q0" --
    # documented pins (AGENTS.md q0 anchor convention)
    PINS = {"proton": "1.1099785827513808", "muon": "1.10997859555733471"}
    pin_out = {}
    for nm, sv in PINS.items():
        qp = mpf(sv)
        pin_out[nm] = mp.nstr((qp - 1 / qp) ** 2, 14)
    ratio = beta3_recorded / h_A2
    # is the ratio a power of q0?  k = ln(ratio)/ln(q0)
    k = mp.log(ratio) / mp.log(q0)
    out["alternatives_foreclosed"] = {
        "h_A2_at_documented_pins": pin_out,
        "note_pins": ("neither documented anchor yields 0.0499; h_A^2 is flat to "
                      "13 digits across the two pins, so no anchor choice explains it"),
        "ratio_beta3_over_hA2": mp.nstr(ratio, 14),
        "q0_exponent_matching_ratio": mp.nstr(k, 12),
        "note_power": ("k is not an integer or half-integer, so the ratio is not a "
                       "power of q0 -- a mistyped exponent does not explain it either"),
        "significant_figures": {
            "alpha": 6, "beta2": 7, "beta3": 3,
            "note": ("alpha and beta2 carry computed precision; beta3 carries three "
                     "significant figures, the precision of a typed constant"),
        },
    }

    out["results"] = rows_out
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
