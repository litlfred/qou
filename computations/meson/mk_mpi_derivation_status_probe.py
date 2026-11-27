#!/usr/bin/env python3
"""m_K/m_pi L2 row: component recomputation, selection look-elsewhere, EM-form ambiguity.

Audit: docs/audits/2026-11-20-mk-mpi-derivation-status.md
Lean:  QOU.BraidKnot.MesonFusionIndexSelection (qCG_unnormalised_general,
       meson_qCG_3x4_is_family_instance, scanPair_four_not_dictionary_index,
       sqrt_jet_agrees_to_order_two).

What this probe does, all in mpmath at the package compute precision (70 dps)
at the PROTON-pinned q0 (AGENTS.md 2026-08-07 directive; this stem is not in
q0_anchor_manifest.json, so q_parameter serves the proton pin):

1. Recomputes the dashboard row of per_observable_100x_status.py exactly
   (same formula, same alpha_em call) and asserts it reproduces the committed
   witness string `pred_MeV = 3.53711862102`, `err_ppb = 51.48`.
2. Splits the row into its components: strong core sqrt([3]_q[4]_q) alone and
   its residual; EM term; total.
3. Look-elsewhere on the scan family {[a]_q[b]_q : 1 <= a <= b <= 12}: where
   does (3,4) rank, how far is the runner-up. This quantifies what the pair
   selection bought; it does NOT derive anything.
4. EM-form ambiguity: three resummations that share the order-2 jet
   1 + h - h^2/2 (which is all the 2026-05-28 term-by-term hunt matched to
   data) -- 1 + log(1+h), sqrt(1+2h), and the [1/1] Pade 1 + h/(1 + h/2) --
   and the m_K/m_pi error under each.

Nothing here is fitted; no number below is tuned. The scan is reported, not
used to choose.
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    M_K_PM_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION)
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402


def qint(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def ppb(pred, ref):
    return (pred / ref - 1) * mp.mpf(10) ** 9


def main():
    set_compute_dps()
    q0 = Q_MP
    h = 1 - 1 / q0
    pdg = mp.mpf(M_K_PM_MEV_VALIDATION) / mp.mpf(M_PI_PM_MEV_VALIDATION)
    a_inv = alpha_em_inv_derived(q0)
    alpha_over_pi = (1 / a_inv) / mp.pi

    core_sq = qint(3, q0) * qint(4, q0)
    em_factor = 1 + mp.log(1 + h)
    em_term = alpha_over_pi * em_factor
    total = mp.sqrt(core_sq + em_term)
    core = mp.sqrt(core_sq)

    err_total = ppb(total, pdg)
    err_core = ppb(core, pdg)
    target = mp.mpf("263.6")

    # --- look-elsewhere on the scan family --------------------------------
    target_sq = pdg ** 2
    fam = []
    for a in range(1, 13):
        for b in range(a, 13):
            v = qint(a, q0) * qint(b, q0)
            fam.append(((a, b), v, abs(v / target_sq - 1)))
    fam.sort(key=lambda t: t[2])
    rank_34 = 1 + [p for p, _, _ in fam].index((3, 4))
    runner = fam[1] if fam[0][0] == (3, 4) else fam[0]
    # local density: nearest family values strictly below / above the target
    below = max((v for _, v, _ in fam if v < target_sq * (1 - mp.mpf("1e-3"))))
    above = min((v for _, v, _ in fam if v > target_sq * (1 + mp.mpf("1e-3"))))
    local_gap_rel = (above - below) / target_sq
    # chance that a target placed uniformly (in log) in the local gap falls within
    # +/- the (3,4) deviation of SOME member: ~ 2*dev / gap  (look-elsewhere, 1 trial)
    chance = 2 * fam[0][2] / local_gap_rel

    # dictionary-indexed readings (lepton-meson-torus-knot-dictionary):
    # pion quarks (3,3), kaon quarks (3,5); totals 6 and 8.
    dict_readings = {
        "[3][5]/([3][3]) = [5]/[3]": qint(5, q0) / qint(3, q0),
        "[8]/[6] (total crossings)": qint(8, q0) / qint(6, q0),
        "[3][5] (kaon quark product)": qint(3, q0) * qint(5, q0),
        "([3]+[5])/(2[3]) (GMOR, m(n)=[n])": (qint(3, q0) + qint(5, q0)) / (2 * qint(3, q0)),
    }
    dict_err_ppm = {k: (v / target_sq - 1) * 10 ** 6 for k, v in dict_readings.items()}

    # --- EM-form ambiguity -------------------------------------------------
    forms = {
        "1+log(1+h) (shipped)": 1 + mp.log(1 + h),
        "sqrt(1+2h)": mp.sqrt(1 + 2 * h),
        "Pade[1/1] 1+h/(1+h/2)": 1 + h / (1 + h / 2),
        "order-2 jet 1+h-h^2/2 (retired truncation)": 1 + h - h ** 2 / 2,
        "1 (LO, no substrate factor)": mp.mpf(1),
    }
    form_err = {k: ppb(mp.sqrt(core_sq + alpha_over_pi * v), pdg)
                for k, v in forms.items()}

    s = lambda x, n=12: mp.nstr(x, n)  # noqa: E731
    print(f"q0 (proton pin)       = {s(q0, 20)}")
    print(f"alpha_em^-1 (derived) = {s(a_inv, 15)}")
    print(f"PDG m_K/m_pi          = {s(pdg)}")
    print(f"core sqrt([3][4])     = {s(core)}   err {s(err_core, 8)} ppb  "
          f"miss {s(abs(err_core) / target, 5)}x")
    print(f"EM term (on ratio^2)  = {s(em_term, 10)}   factor {s(em_factor, 10)}")
    print(f"total                 = {s(total)}   err {s(err_total, 6)} ppb  "
          f"miss_factor {s(abs(err_total) / target, 4)}")
    print(f"scan family: (3,4) rank {rank_34}/{len(fam)}, "
          f"rel {s(fam[0][2] * 10**6, 6)} ppm; runner-up {runner[0]} "
          f"rel {s(runner[2] * 10**6, 6)} ppm")
    print(f"local gap (rel) {s(local_gap_rel, 6)}; chance-within-dev ~ {s(chance, 4)}")
    for k, v in dict_err_ppm.items():
        print(f"  dictionary reading {k:38s} {s(v, 6)} ppm on ratio^2")
    for k, v in form_err.items():
        print(f"  EM form {k:45s} err {s(v, 6)} ppb")

    wb = WitnessBuilder("mk-mpi-derivation-status", engine="mpmath")
    wb.set_description(
        "m_K/m_pi L2 row recomputed by component at the proton q0, 70 dps; "
        "look-elsewhere rank of the scan-selected pair (3,4) in "
        "{[a]_q[b]_q : 1<=a<=b<=12}; EM-form ambiguity among resummations "
        "sharing the order-2 jet 1+h-h^2/2. Diagnostic only: nothing fitted, "
        "nothing selected.")
    wb.set_audit_only("docs/audits/2026-11-20-mk-mpi-derivation-status.md")
    wb.add_data("q0", mp.nstr(q0, 40))
    wb.add_data("alpha_em_inv_derived", mp.nstr(a_inv, 30))
    wb.add_data("components", {
        "core_sqrt_3x4": mp.nstr(core, 30),
        "core_err_ppb": mp.nstr(err_core, 15),
        "core_miss_factor": mp.nstr(abs(err_core) / target, 10),
        "em_factor_1_plus_log_1_plus_hbar": mp.nstr(em_factor, 30),
        "em_term_on_ratio_sq": mp.nstr(em_term, 30),
        "total": mp.nstr(total, 30),
        "total_err_ppb": mp.nstr(err_total, 15),
        "total_miss_factor": mp.nstr(abs(err_total) / target, 10),
    })
    wb.add_data("scan_family_look_elsewhere", {
        "family": "[a]_q[b]_q, 1<=a<=b<=12 (78 members)",
        "rank_of_3_4": rank_34,
        "rel_dev_3_4_ppm_on_ratio_sq": mp.nstr(fam[rank_34 - 1][2] * 10 ** 6, 12),
        "runner_up": list(runner[0]),
        "runner_up_rel_dev_ppm": mp.nstr(runner[2] * 10 ** 6, 12),
        "local_gap_rel": mp.nstr(local_gap_rel, 10),
        "chance_within_dev_estimate": mp.nstr(chance, 6),
        "top5": [{"pair": list(p), "rel_dev_ppm": mp.nstr(d * 10 ** 6, 8)}
                 for p, _, d in fam[:5]],
    })
    wb.add_data("dictionary_index_readings_ppm_on_ratio_sq",
                {k: mp.nstr(v, 10) for k, v in dict_err_ppm.items()})
    wb.add_data("em_form_ambiguity_err_ppb",
                {k: mp.nstr(v, 12) for k, v in form_err.items()})

    wb.add_assertion(
        name="reproduces_dashboard_pred",
        computed=mp.nstr(total, 12), expected="3.53711862102", tolerance=0,
        unit="ratio", source="per-observable-100x-status.witness.json row m_K/m_pi pred_MeV")
    wb.add_assertion(
        name="reproduces_dashboard_err_ppb",
        computed=mp.nstr(err_total, 4), expected="51.48", tolerance=0,
        unit="ppb", source="per-observable-100x-status.witness.json row m_K/m_pi err_ppb")
    wb.add_assertion(
        name="core_alone_misses_target",
        computed=bool(abs(err_core) > target), expected=True, tolerance=0,
        unit="bool", source="red-team 2026-08-22 §2: strong core alone misses 385x")
    wb.add_assertion(
        name="all_order2_jet_forms_inside_target",
        computed=all(abs(v) < target for k, v in form_err.items()
                     if not k.startswith("1 (LO")),
        expected=True, tolerance=0, unit="bool",
        source="EM-form choice among order-2-jet resummations does not move the verdict")
    out = wb.save()
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
