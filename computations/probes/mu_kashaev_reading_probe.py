#!/usr/bin/env python3
"""mu_kashaev_reading_probe -- the CAL-2 muon carrier read as the leading saddle
of the 4_1 Kashaev series, and the size of every DERIVED correction term.

Bean qou-6gf9 (lepton self-energy front, owner 2026-11-20).
Lean companion: folio/.../lean/QOU/BraidKnot/MuonKashaevReading.lean.
Audit: docs/audits/2026-11-20-lepton-self-energy-front.md.

QUESTION. The corpus calls m_mu/m_e = Vol(4_1)/hbar_q^2 "the Kashaev limit".
Taken literally it is the leading term of

    log J_N(4_1; e^{2 pi i/N}) = N Vol/(2 pi) + (3/2) log N - (1/4) log 3
                                 + sum_{n>=1} kappa_n / N^n            (*)

(Andersen-Hansen, quoted in [murakami-h2011] Thm 1.2; kappa_1..kappa_5 are the
corpus's exact identifications, 2026-07-12 audits). Matching the leading term
forces N_eff = 2 pi / hbar_q^2 (Lean: leading_match_forces_hbar_sq). The
corrections are then FIXED -- no coefficient is chosen here.

WHAT IS COMPUTED (mpmath, 70 dps, no float64):
  1. the datum at the proton pin (CODATA 2022 ratio);
  2. N_eff and every term of (*) at N_eff, as an absolute shift of the ratio and
     as ppb on m_mu -- NO adjustment;
  3. a check that (*) is the right expansion at this N: log J_N computed EXACTLY
     at the two integers bracketing N_eff, compared with the truncation;
  4. the effect on the muon q0 pin if CAL-2 were replaced by a truncation of (*)
     (CAL-2 itself is NOT changed);
  5. for completeness, the size of the same Ohtsuki rungs under a multiplicative
     (amplitude) reading -- flagged as NOT derived, already covered by the
     monomial order window (MuPCarrierOrderWindow.lean);
  6. LAST, and only as a diagnostic, the comparison with the -211 ppb residual.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    Q_50_DIGIT_STR, MASS_RATIO_MU_E_STR)

# CODATA 2022 sigma on m_mu/m_e, as a string (qou_substrate carries it as float)
RATIO_ERR_STR = "0.0000046"


def log_kashaev_4_1(N):
    """Exact log of Kashaev's <4_1>_N = sum_{k<N} prod_{j<=k} |1-e^{2 pi i j/N}|^2,
    streamed in log-sum-exp form (same object as qbeta_ohtsuki_higher_rungs)."""
    logP = mp.mpf(0)
    m = mp.mpf(0)
    s = mp.mpf(1)
    for k in range(1, N):
        logP += 2 * mp.log(2 * mp.sin(mp.pi * k / N))
        if logP > m:
            s = s * mp.exp(m - logP) + 1
            m = logP
        else:
            s += mp.exp(logP - m)
    return m + mp.log(s)


def main():
    set_compute_dps(70)
    pi = mp.pi
    s3 = mp.sqrt(3)
    q = mp.mpf(Q_50_DIGIT_STR)
    vol = 2 * mp.clsin(2, pi / 3)
    hq = 1 - 1 / q
    R = vol / hq ** 2
    r_exp = mp.mpf(MASS_RATIO_MU_E_STR)
    r_err = mp.mpf(RATIO_ERR_STR)
    resid_ppb = (R / r_exp - 1) * mp.mpf(10) ** 9
    sigma = (R - r_exp) / r_err
    delta_needed_abs = r_exp - R          # what the carrier would have to move

    # --- (*) at N_eff -----------------------------------------------------
    Neff = 2 * pi / hq ** 2
    kappa = {
        1: 11 * s3 * pi / 108,
        2: 2 * pi ** 2 / 27,
        3: 1081 * s3 * pi ** 3 / 21870,
        4: 98 * pi ** 4 / 729,
        5: mp.mpf(110011) * s3 * pi ** 5 / 688905,
    }
    c0 = -mp.log(3) / 4
    terms = {
        "leading_N_Vol_over_2pi": Neff * vol / (2 * pi),
        "one_loop_three_halves_logN": mp.mpf(3) / 2 * mp.log(Neff),
        "one_loop_const_minus_quarter_log3": c0,
    }
    for n, k in kappa.items():
        terms[f"kappa_{n}_over_N^{n}"] = k / Neff ** n
    lead_check = abs(terms["leading_N_Vol_over_2pi"] - R)

    rows = {}
    cumulative = mp.mpf(0)
    for name, v in terms.items():
        if name == "leading_N_Vol_over_2pi":
            continue
        cumulative += v
        rows[name] = {
            "absolute_shift_of_ratio": fmt(v),
            "ppb_on_m_mu": fmt(v / R * mp.mpf(10) ** 9),
            "cumulative_ppb_on_m_mu": fmt(cumulative / R * mp.mpf(10) ** 9),
            "over_needed_abs": fmt(v / abs(delta_needed_abs)),
        }
    trunc_total = R + cumulative

    # --- exact log J_N at the two integers bracketing N_eff ---------------
    Nlo = int(mp.floor(Neff))
    exact = {}
    for N in (Nlo, Nlo + 1):
        lj = log_kashaev_4_1(N)
        ser = (N * vol / (2 * pi) + mp.mpf(3) / 2 * mp.log(N) + c0
               + sum(k / mp.mpf(N) ** n for n, k in kappa.items()))
        exact[str(N)] = {"log_J_N_exact": fmt(lj),
                         "series_through_kappa5": fmt(ser),
                         "exact_minus_series": fmt(lj - ser),
                         "exact_minus_leading": fmt(lj - N * vol / (2 * pi))}
    worst_series_gap = max(abs(mp.mpf(e["exact_minus_series"]))
                           for e in exact.values())

    # --- effect on the muon q0 pin (CAL-2 NOT changed) --------------------
    def carrier(qq, with_corr):
        h = 1 - 1 / qq
        Ne = 2 * pi / h ** 2
        val = vol / h ** 2
        if with_corr:
            val += mp.mpf(3) / 2 * mp.log(Ne) + c0 + sum(
                k / Ne ** n for n, k in kappa.items())
        return val

    q_bare = mp.findroot(lambda x: carrier(x, False) - r_exp, q)
    q_corr = mp.findroot(lambda x: carrier(x, True) - r_exp, q)
    pin_shift_ppb = (q_corr / q_bare - 1) * mp.mpf(10) ** 9
    bare_vs_proton_ppb = (q_bare / q - 1) * mp.mpf(10) ** 9

    # --- multiplicative reading (NOT derived; comparison only) ------------
    mult = {}
    for n, k in kappa.items():
        kt = k / (2 * pi) ** n                       # coefficient of hbar_K^n
        mult[f"kappa_tilde_{n}"] = {
            "coefficient": fmt(kt),
            "relative_with_hbarK_eq_hbar_q_sq_ppb": fmt(kt * hq ** (2 * n)
                                                       * mp.mpf(10) ** 9),
        }

    # --- assertions -------------------------------------------------------
    b = WitnessBuilder("mu-kashaev-reading")
    b.set_description(
        "Bean qou-6gf9. Reads CAL-2 m_mu/m_e = Vol(4_1)/hbar_q^2 literally as "
        "the leading term of the Andersen-Hansen/Ohtsuki log-series of the "
        "4_1 Kashaev invariant [murakami-h2011]; leading-term matching forces "
        "N_eff = 2 pi/hbar_q^2 ~ 640.02. Every derived correction term is "
        "evaluated at the proton pin with NO adjustment. The one-loop term "
        "(3/2)log N - (1/4)log 3 = +9.42 moves m_mu UP by ~4.6e7 ppb; all five "
        "identified Ohtsuki rungs are positive and also move it UP. The "
        "measured residual needs the carrier DOWN by 211 ppb. Exact log J_N at "
        "N=640,641 matches the series to the kappa_6 scale, so the expansion "
        "is the right one at this N. Scope (b) for the class 'finite "
        "truncation of the 4_1 Kashaev log-series with non-negative rungs' "
        "(Lean kashaev_reading_excluded); CAL-2 unchanged.")
    b.add_parameter("q0_proton_50dps", Q_50_DIGIT_STR)
    b.add_parameter("m_mu_over_m_e_codata2022", MASS_RATIO_MU_E_STR)
    b.add_parameter("m_mu_over_m_e_sigma", RATIO_ERR_STR)
    b.add_parameter("dps", "70")
    b.add_data("datum", {
        "hbar_q": fmt(hq), "Vol_4_1": fmt(vol), "carrier_Vol_over_hbar_sq": fmt(R),
        "residual_ppb": fmt(resid_ppb), "residual_sigma_on_ratio": fmt(sigma),
        "needed_absolute_shift": fmt(delta_needed_abs),
    })
    b.add_data("kashaev_reading", {
        "N_eff_2pi_over_hbar_q_sq": fmt(Neff),
        "leading_term_minus_carrier": fmt(lead_check),
        "terms": rows,
        "truncation_through_kappa5_ratio": fmt(trunc_total),
        "truncation_through_kappa5_ppb_vs_codata": fmt(
            (trunc_total / r_exp - 1) * mp.mpf(10) ** 9),
    })
    b.add_data("exact_kashaev_at_bracketing_integers", exact)
    b.add_data("muon_pin_effect_if_cal2_were_the_truncation", {
        "q0_bare_muon_pin": fmt(q_bare),
        "q0_bare_minus_proton_ppb": fmt(bare_vs_proton_ppb),
        "q0_corrected_muon_pin": fmt(q_corr),
        "pin_shift_ppb": fmt(pin_shift_ppb),
        "note": "Reported only; CAL-2 is NOT changed (owner 2026-11-20).",
    })
    b.add_data("multiplicative_reading_not_derived", {
        "rows": mult,
        "note": "No corpus artifact derives an amplitude-multiplicative "
                "reading; shown so the reader can see it is excluded anyway "
                "(kappa_tilde_1*hbar_q^2 ~ +8.7e5 ppb, positive, i.e. the "
                "order-window k=2 case of MuPCarrierOrderWindow).",
    })
    b.add_assertion(
        "leading_term_equals_carrier", computed=fmt(lead_check),
        expected="0", tolerance="1e-60", unit="absolute",
        source="N_eff*Vol/(2pi) with N_eff = 2pi/hbar_q^2 is Vol/hbar_q^2 "
               "(Lean leading_term_eq).")
    b.add_assertion(
        "series_matches_exact_kashaev_at_N_eff", computed=fmt(worst_series_gap),
        expected="0", tolerance="1e-12", unit="absolute",
        source="|log J_N exact - series through kappa_5| at N = floor/ceil "
               "N_eff; the gap is the kappa_6/N^6 scale (~1e-14).")
    b.add_assertion(
        "one_loop_term_positive_and_gt_two_thirds",
        computed="1" if terms["one_loop_three_halves_logN"] + c0
        > mp.mpf(2) / 3 else "0", expected="1",
        source="Lean two_thirds_lt_one_loop_4_1.")
    b.add_assertion(
        "every_derived_term_has_wrong_sign",
        computed="1" if all(v > 0 for k, v in terms.items()
                            if k not in ("leading_N_Vol_over_2pi",
                                         "one_loop_const_minus_quarter_log3"))
        and cumulative > 0 and delta_needed_abs < 0 else "0",
        expected="1",
        source="All non-constant terms and their sum are positive; the needed "
               "shift is negative.")
    b.save(extra={"q0Anchor": "proton", "q0AnchorReason": (
        "evaluates at the proton pin per the 2026-08-07 directive; the muon "
        "pin is only re-solved as a reported comparison")})

    print(f"carrier R = {mp.nstr(R, 20)}  CODATA = {MASS_RATIO_MU_E_STR}")
    print(f"residual {mp.nstr(resid_ppb, 8)} ppb  ({mp.nstr(sigma, 5)} sigma); "
          f"needed abs shift {mp.nstr(delta_needed_abs, 8)}")
    print(f"N_eff = {mp.nstr(Neff, 15)}")
    for k, r in rows.items():
        print(f"  {k:<38} abs {r['absolute_shift_of_ratio'][:14]:>16}  "
              f"ppb {r['ppb_on_m_mu'][:14]:>16}  cum {r['cumulative_ppb_on_m_mu'][:14]}")
    for N, e in exact.items():
        print(f"  N={N}: exact-series {e['exact_minus_series'][:12]}  "
              f"exact-leading {e['exact_minus_leading'][:14]}")
    print(f"muon pin: bare-proton {mp.nstr(bare_vs_proton_ppb, 8)} ppb; "
          f"corrected-bare {mp.nstr(pin_shift_ppb, 10)} ppb")
    for k, r in mult.items():
        print(f"  mult {k}: coeff {r['coefficient'][:12]}  "
              f"ppb {r['relative_with_hbarK_eq_hbar_q_sq_ppb'][:12]}")


if __name__ == "__main__":
    main()
