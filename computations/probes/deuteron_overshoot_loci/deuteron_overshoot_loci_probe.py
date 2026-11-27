#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath evaluation at the proton q0; no symbolic-q output.
"""Deuteron +27.4 % overshoot of the log binding law: the two loci, measured.

Bean qou-of4i (owner ruling 2026-11-25, "3y sibling"). Derivation only.
NOTHING here selects a scale or a letter by its residual; every candidate
tabulated is one the corpus already defines, and the AME values enter only
as comparison points.

Law: B = E_0 * ln(tr_free / tr_atom)   (computations/binding_log_free_energy.py)

Locus (a), the scale. Two corpus forms of E_0 (computations/qbeta/qbeta_e0.py):
order-zero m_e/(q(q-1)) (what the live producer uses) and the tower-summed
E_0/(1 - hbar_q^2) (qbeta_e0.canonical(); binding arc ruling 2026-09-05).
Required scale r_A = B_AME(A) / ln(tr_free/tr_atom) per nucleus, and the
minimax floor t = (r2 - r1)/(r1 + r2) of QOU/Nuclear/UniversalScaleMinimax.lean
for every pair: no single universal E_0 reproduces both nuclei to better
than t.

Locus (b), the p-n letter. mu_pn for every interface candidate the corpus
defines (InterfaceScalar.lean; 2026-08-08 audit §1, §7; 2026-09-05 synthesis
§6), at both scales.

SCOPE: the traces come from atom_braid_word_3A's single-crossing interface
letters, which the 2026-11-15 gamma-gamma ruling marks as superseded
(docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md). These
numbers are a record of that word, not a current result.

No float64: mpmath end to end, 70 dps; float() appears only nowhere.
q0 pin: proton (qou_substrate.constants.Q_50_DIGIT_STR).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations", "computations/substrate", "computations/qbeta",
          "tools/qou-substrate/python", "tools/pyhecke/python"):
    sys.path.insert(0, str(ROOT / p))

from mpmath import mp, mpf, log, sqrt, nstr  # noqa: E402

mp.dps = 70

import qou_substrate.constants as C  # noqa: E402
import qbeta_e0  # noqa: E402
from binding_canonical import binding_canonical  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION as _BD, AME_B_TRITIUM_MEV_VALIDATION as _BT,
    AME_B_HE3_MEV_VALIDATION as _BH3, AME_B_HE4_MEV_VALIDATION as _BH4)

q = mpf(C.Q_50_DIGIT_STR)
me = mpf(str(C.M_E_MEV))
h = q - 1 / q
z = q ** 3 / (q ** 2 + 1)                    # convention D
delta = (q - 1) ** 2 * (1 - q ** -4) / 3     # flavor_split_leading
E0 = qbeta_e0.order_zero(q, me)
E0t = qbeta_e0.tower_summed(q, me)

NUC = [("2H", 1, 1, _BD), ("3H", 1, 2, _BT), ("3He", 2, 1, _BH3), ("4He", 2, 2, _BH4)]


def s(x, n=12):
    return nstr(x, n)


def main() -> int:
    out = {"q0": s(q, 30), "E0_order_zero": s(E0, 15), "E0_tower_summed": s(E0t, 15),
           "z_D": s(z, 20), "h": s(h, 20), "delta": s(delta, 20),
           "scope": "single-crossing interface letters (superseded by 2026-11-15 gg ruling)"}
    rows, r = [], {}
    for name, Z, N, Bame in NUC:
        res = binding_canonical(Z, N)
        assert res["status"] == "solved", res
        L = log(mpf(res["tr_M_free"]) / mpf(res["tr_M_atom"]))
        B = mpf(str(Bame))
        r[name] = B / L
        rows.append({"nucleus": name, "L": s(L, 20), "B_AME": s(B, 10),
                     "B_E0": s(E0 * L, 10), "err_E0_pct": s(100 * (E0 * L / B - 1), 8),
                     "B_E0t": s(E0t * L, 10), "err_E0t_pct": s(100 * (E0t * L / B - 1), 8),
                     "required_scale_MeV": s(r[name], 12),
                     "required_over_E0": s(r[name] / E0, 12)})
    out["nuclei"] = rows
    names = [n for n, *_ in NUC]
    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            r1, r2 = sorted((r[a], r[b]))
            pairs.append({"pair": f"{a}-{b}", "minimax_rel_err_pct": s(100 * (r2 - r1) / (r1 + r2), 8),
                          "best_scale_harmonic_MeV": s(2 * r1 * r2 / (r1 + r2), 10)})
    out["minimax_pairs"] = pairs

    cands = {
        "colour-weighted d=-h(1/2-delta/4) [live]": z - h * (mpf(1) / 2 - delta / 4),
        "colour-blind average d=-h/2": z - h / 2,
        "derived crossing weight w=1/(q^2+1)": z - h * q ** 2 / (q ** 2 + 1),
        "geometric mean sqrt(z(z-h))": sqrt(z * (z - h)),
        "bare sigma, d=0 (pp letter)": z,
        "bare sigma^-1, d=-h (nn letter)": z - h,
        "isospin T=1 projector mu+": (z + 1 / q) / (q + 1 / q),
        "isospin T=0 projector mu- (deuteron channel)": (q - z) / (q + 1 / q),
    }
    BD = mpf(str(_BD))
    out["deuteron_letter_candidates"] = [
        {"candidate": k, "mu_pn": s(mu, 15),
         "B_E0": s(-E0 * log(mu), 10), "err_E0_pct": s(100 * (-E0 * log(mu) / BD - 1), 8),
         "B_E0t": s(-E0t * log(mu), 10), "err_E0t_pct": s(100 * (-E0t * log(mu) / BD - 1), 8)}
        for k, mu in cands.items()]
    # Exact identities checked, not assumed:
    one_over_2q = q / (q ** 2 + 1)
    out["identities_D"] = {
        "crossing_weight_mu_minus_1/[2]_q": s(cands["derived crossing weight w=1/(q^2+1)"] - one_over_2q, 5),
        "geometric_mean_minus_1/[2]_q": s(cands["geometric mean sqrt(z(z-h))"] - one_over_2q, 5),
        "mu_minus_minus_1/[2]_q^2": s(cands["isospin T=0 projector mu- (deuteron channel)"] - one_over_2q ** 2, 5),
    }
    mu_req = mp.e ** (-BD / E0)
    out["diagnostic_not_a_target"] = {
        "mu_req_at_E0": s(mu_req, 15), "d_req_over_h": s((mu_req - z) / h, 12),
        "note": "what AME would need; choosing d or E0 to hit it is a fit and is not done"}

    # Assertions: identities exact; the minimax floor is what the Lean bound says.
    ok = all(abs(mpf(v)) < mpf(10) ** -60 for v in out["identities_D"].values())
    out["assertions"] = {"identities_exact_to_1e-60": ok}
    dest = Path(__file__).with_name("deuteron-overshoot-loci.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
