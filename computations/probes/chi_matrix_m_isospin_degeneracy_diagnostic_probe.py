#!/usr/bin/env python3
"""
chi_matrix_m_isospin_degeneracy_diagnostic_probe.py — Bean `qou-sgv5` (parent `qou-wp3h`)

Executes the 4 diagnostic steps of `qou-sgv5` ("chi-matrix-m family does not
distinguish proton from neutron: tr_M identical, so Delta(n-p)=0"):

1. Inspect `_word_for_braid_word_3a(Z, N)` for (1,0) vs (0,1) (proton vs neutron)
   and (1,2) vs (2,1) (tritium vs helium-3) and diff them: proves that
   `_word_for_braid_word_3a` returns BYTE-IDENTICAL `(sign, gen_1based)` words
   for every isobar pair with the same `A = Z + N` (`diff_count == 0`).
2. Trace where the proton/neutron and tritium/helium-3 equality is introduced:
   `atom_braid_word_3A(Z, N)` returns `(c, d, gen_0based)` triples representing
   `c * sigma_g + d * 1`, where `c == +1.0` for EVERY crossing of EVERY nucleus,
   while the `sigma` (`d = 0`), `sigma_inv` (`d = -h`), `averaged` (`d = -h/2`),
   and `averaged_weighted` (`d = -h*(1/2 - delta/4)`) distinction lives entirely
   in `d`. Because `_word_for_braid_word_3a` reads `1 if c >= 0 else -1` off the
   constant `c == +1` field and discards `d`, every word collapses to an
   all-positive braid word whose generator sequence depends on `A = Z + N` alone.
   Even if `d` is decoded via `classify_crossing -> sign_for_ctype`,
   `sign_for_ctype` maps both `averaged` and `averaged_weighted` to `0` (not a
   braid generator in `B_n`, and dropping the `delta/4` colour-weighted shift).
3. Verify at 50 dps (`mpmath`, no `float64`) that the `matrix-m` / path-sum
   sign-only evaluation gives `tr_M(p) == tr_M(n)` and `tr_M(T) == tr_M(3He)`
   to all 50 digits (`Delta == 0` identically by construction), and verify that
   all `chi*matrix-m*.witness.json` witnesses carry explicit
   `isospinDegeneracyNote` and `pn_split_carried: False` metadata so no reader
   mistakes `Delta = 0` for a physics claim.
4. Cross-check against the exact-triple Hoefsmit (`chi_at_q0_via_hoefsmit_mpfr.py`)
   and closed-form Wenzl bridge (`closed_form_tau_M.py`) routes that consume the
   full `(c, d, gen)` triples and carry the non-zero isospin splits
   `Delta tr_M(n - p) != 0` and `Delta tr_M(3He - T) != 0`, agreeing to < 1e-49.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
if str(COMP) not in sys.path:
    sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(50)

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from canonical_braid_crossings import (  # noqa: E402
    atom_canonical_crossings,
    sign_for_ctype,
)
from derived_chi_catalogue_matrix_m import (  # noqa: E402
    ISOSPIN_DEGENERACY_NOTE,
    _word_for_braid_word_3a,
)
from chi_path_sum_seminormal import chi_all_partitions_path_sum  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
from closed_form_tau_M import closed_form_tau_M  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


MATRIX_M_WITNESS_FILES = (
    "chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json",
    "chi-deuteron-h6-at-q0-90dps-matrix-m.witness.json",
    "chi-tritium-h9-at-q0-50dps-matrix-m.witness.json",
    "chi-helium-3-h9-at-q0-50dps-matrix-m.witness.json",
    "chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json",
    "chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json",
    "chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json",
    "chi-at-q0-matrix-m-deuteron.witness.json",
    "chi-at-q0-matrix-m-tritium.witness.json",
    "chi-at-q0-matrix-m-helium-3.witness.json",
    "chi-at-q0-matrix-m-helium-4.witness.json",
)


def _tr_m_from_sign_word(n: int, word: list[tuple[int, int]], q: mp.mpf) -> mp.mpf:
    y_table = _load_y_lambda(n, None)
    chis = chi_all_partitions_path_sum(n, word, q)
    total = mp.mpf(0)
    for shape, chi_val in chis.items():
        total += mp.mpf(str(y_table[shape])) * chi_val
    return total


def main() -> int:
    set_compute_dps(50)
    q0 = mp.mpf(Q_50_DIGIT_STR)

    wb = WitnessBuilder(
        "chi-matrix-m-isospin-degeneracy-diagnostic-probe",
        engine="python+mpmath",
    )
    wb.set_description(
        "Bean qou-sgv5 4-step diagnostic probe: proves why the chi-*-matrix-m "
        "sign-only wire family gives tr_M(p) == tr_M(n) and tr_M(T) == tr_M(3He) "
        "identically by construction (_word_for_braid_word_3a reads sign from the "
        "constant c=+1 field and discards d), verifies that all 11 matrix-m "
        "witnesses carry isospinDegeneracyNote and pn_split_carried=False, and "
        "cross-checks against the exact-triple Hoefsmit / closed-form Wenzl "
        "bridge routes where Delta tr_M(n-p) != 0 and Delta tr_M(3He-T) != 0."
    )

    # ------------------------------------------------------------------
    # Step 1: Inspect and diff _word_for_braid_word_3a(Z, N) on isobar pairs
    # ------------------------------------------------------------------
    n_p, word_p = _word_for_braid_word_3a(1, 0)
    n_n, word_n = _word_for_braid_word_3a(0, 1)
    diff_pn = [
        i for i, (wp, wn) in enumerate(zip(word_p, word_n)) if wp != wn
    ]

    n_t, word_t = _word_for_braid_word_3a(1, 2)
    n_he3, word_he3 = _word_for_braid_word_3a(2, 1)
    diff_t_he3 = [
        i for i, (wt, whe) in enumerate(zip(word_t, word_he3)) if wt != whe
    ]

    wb.add_assertion(
        "step1_proton_neutron_sign_word_identical",
        computed=(n_p == n_n == 3 and len(word_p) == 11 and word_p == word_n and len(diff_pn) == 0),
        expected=True,
        source=f"len={len(word_p)}, diff_count={len(diff_pn)}",
    )
    wb.add_assertion(
        "step1_tritium_helium3_sign_word_identical",
        computed=(n_t == n_he3 == 9 and len(word_t) == 35 and word_t == word_he3 and len(diff_t_he3) == 0),
        expected=True,
        source=f"len={len(word_t)}, diff_count={len(diff_t_he3)}",
    )

    # ------------------------------------------------------------------
    # Step 2: Trace where equality is introduced in (c, d, gen) -> (sign, gen)
    # ------------------------------------------------------------------
    sample_nuclei = [
        ("proton", 1, 0),
        ("neutron", 0, 1),
        ("deuteron", 1, 1),
        ("tritium", 1, 2),
        ("helium-3", 2, 1),
        ("helium-4", 2, 2),
        ("lithium-6", 3, 3),
    ]
    c_all_plus_one = True
    ctype_profiles: dict[str, dict[str, int]] = {}
    for name, Z, N in sample_nuclei:
        triples = atom_braid_word_3A(Z, N)
        c_set = {int(round(float(c))) for (c, _d, _g) in triples}
        if c_set != {1}:
            c_all_plus_one = False
        crossings = atom_canonical_crossings(Z, N)
        counts = collections.Counter(ct for _g, ct in crossings)
        ctype_profiles[name] = dict(sorted(counts.items()))

    cr_p = atom_canonical_crossings(1, 0)
    cr_n = atom_canonical_crossings(0, 1)
    diff_cr_pn = [i for i, (a, b) in enumerate(zip(cr_p, cr_n)) if a != b]

    cr_t = atom_canonical_crossings(1, 2)
    cr_he3 = atom_canonical_crossings(2, 1)
    diff_cr_t_he3 = [i for i, (a, b) in enumerate(zip(cr_t, cr_he3)) if a != b]

    wb.add_assertion(
        "step2_c_field_identically_plus_one_across_nuclei",
        computed=c_all_plus_one,
        expected=True,
        source=f"c_all_plus_one={c_all_plus_one} across {len(sample_nuclei)} sample nuclei",
    )
    wb.add_assertion(
        "step2_d_decoded_ctypes_distinguish_proton_neutron_and_isobars",
        computed=(
            ctype_profiles["proton"] == {"averaged": 2, "sigma": 6, "sigma_inv": 3}
            and ctype_profiles["neutron"] == {"averaged": 2, "sigma": 5, "sigma_inv": 4}
            and len(diff_cr_pn) == 2
            and len(diff_cr_t_he3) == 4
            and sign_for_ctype("averaged") == 0
            and sign_for_ctype("averaged_weighted") == 0
        ),
        expected=True,
        source=(
            f"p={ctype_profiles['proton']}, n={ctype_profiles['neutron']}, "
            f"diff_pn={len(diff_cr_pn)}, diff_t_he3={len(diff_cr_t_he3)}"
        ),
    )

    # ------------------------------------------------------------------
    # Step 3: 50-dps verification of matrix-m tr_M degeneracy (borromean & grouped)
    #         + check all 11 chi*matrix-m*.witness.json carry warning notes
    # ------------------------------------------------------------------
    trm_sign_p = _tr_m_from_sign_word(n_p, word_p, q0)
    trm_sign_n = _tr_m_from_sign_word(n_n, word_n, q0)
    delta_sign_pn = trm_sign_n - trm_sign_p

    trm_sign_t_bor = _tr_m_from_sign_word(n_t, word_t, q0)
    trm_sign_he3_bor = _tr_m_from_sign_word(n_he3, word_he3, q0)
    delta_sign_t_he3_bor = trm_sign_he3_bor - trm_sign_t_bor

    triples_t_grp = atom_braid_word_3A(1, 2, intra_order="grouped")
    triples_he3_grp = atom_braid_word_3A(2, 1, intra_order="grouped")
    word_t_grp = [(1 if c >= 0 else -1, g + 1) for (c, _d, g) in triples_t_grp]
    word_he3_grp = [(1 if c >= 0 else -1, g + 1) for (c, _d, g) in triples_he3_grp]
    trm_sign_t_grp = _tr_m_from_sign_word(9, word_t_grp, q0)
    trm_sign_he3_grp = _tr_m_from_sign_word(9, word_he3_grp, q0)
    delta_sign_t_he3_grp = trm_sign_he3_grp - trm_sign_t_grp

    w_t_cache = json.loads((COMP / "chi-tritium-h9-at-q0-50dps-matrix-m.witness.json").read_text())
    w_he3_cache = json.loads((COMP / "chi-helium-3-h9-at-q0-50dps-matrix-m.witness.json").read_text())
    cache_t_val = mp.mpf(w_t_cache["tr_M_at_q0"])
    cache_he3_val = mp.mpf(w_he3_cache["tr_M_at_q0"])

    witness_note_status: dict[str, bool] = {}
    for wname in MATRIX_M_WITNESS_FILES:
        wbody = json.loads((COMP / wname).read_text())
        has_note = (
            wbody.get("pn_split_carried") is False
            and isinstance(wbody.get("pn_split_note"), str)
            and len(wbody.get("pn_split_note", "")) > 20
            and wbody.get("isospinDegeneracyNote") == ISOSPIN_DEGENERACY_NOTE
        )
        witness_note_status[wname] = has_note

    wb.add_assertion(
        "step3_matrix_m_trm_isobar_degeneracy_exact_50dps",
        computed=(
            delta_sign_pn == 0
            and delta_sign_t_he3_bor == 0
            and delta_sign_t_he3_grp == 0
            and cache_t_val == cache_he3_val
            and abs(trm_sign_t_bor - cache_t_val) < mp.mpf("1e-48")
        ),
        expected=True,
        source=(
            f"tr_M_sign(p)=tr_M_sign(n)={mp.nstr(trm_sign_p, 25)}, "
            f"tr_M_sign_bor(T)=tr_M_sign_bor(3He)={mp.nstr(trm_sign_t_bor, 25)}, "
            f"tr_M_sign_grp(T)=tr_M_sign_grp(3He)={mp.nstr(trm_sign_t_grp, 25)}"
        ),
    )
    wb.add_assertion(
        "step3_all_11_matrix_m_witnesses_carry_isospin_degeneracy_note",
        computed=all(witness_note_status.values()) and len(witness_note_status) == 11,
        expected=True,
        source=f"stamped={sum(witness_note_status.values())}/{len(witness_note_status)}",
    )

    # ------------------------------------------------------------------
    # Step 4: Cross-check against exact-triple Hoefsmit & closed-form Wenzl bridge
    # ------------------------------------------------------------------
    hoef_p = json.loads((COMP / "chi-proton-h3-at-q0-50dps.witness.json").read_text())
    hoef_n = json.loads((COMP / "chi-neutron-h3-at-q0-50dps.witness.json").read_text())
    hoef_t = json.loads((COMP / "chi-tritium-h9-at-q0-50dps.witness.json").read_text())
    hoef_he3 = json.loads((COMP / "chi-helium-3-h9-at-q0-50dps.witness.json").read_text())

    tau_p = mp.mpf(hoef_p["tr_M_at_q0"])
    tau_n = mp.mpf(hoef_n["tr_M_at_q0"])
    tau_t = mp.mpf(hoef_t["tr_M_at_q0"])
    tau_he3 = mp.mpf(hoef_he3["tr_M_at_q0"])

    delta_exact_pn = tau_n - tau_p
    delta_exact_t_he3 = tau_he3 - tau_t

    cf_t = closed_form_tau_M(1, 2, q0, tau_p, tau_n, pn_convention="bring_color_weighted")
    cf_he3 = closed_form_tau_M(2, 1, q0, tau_p, tau_n, pn_convention="bring_color_weighted")
    err_cf_t = abs(cf_t - tau_t)
    err_cf_he3 = abs(cf_he3 - tau_he3)

    wb.add_assertion(
        "step4_exact_triple_route_breaks_degeneracy_and_matches_closed_form",
        computed=(
            abs(delta_exact_pn) > mp.mpf("0.15")
            and abs(delta_exact_t_he3) > mp.mpf("0.029")
            and err_cf_t < mp.mpf("1e-49")
            and err_cf_he3 < mp.mpf("1e-49")
        ),
        expected=True,
        source=(
            f"Delta(n-p)={mp.nstr(delta_exact_pn, 25)}, "
            f"Delta(3He-T)={mp.nstr(delta_exact_t_he3, 25)}, "
            f"err_cf_T={mp.nstr(err_cf_t, 5)}, err_cf_3He={mp.nstr(err_cf_he3, 5)}"
        ),
    )

    wb.add_data("q_0_50dps", Q_50_DIGIT_STR)
    wb.add_data("isospinDegeneracyNote", ISOSPIN_DEGENERACY_NOTE)
    wb.add_data("step1_word_diff", {
        "proton_sign_word": [list(x) for x in word_p],
        "neutron_sign_word": [list(x) for x in word_n],
        "proton_neutron_diff_indices": diff_pn,
        "tritium_helium3_diff_indices": diff_t_he3,
    })
    wb.add_data("step2_crossing_profiles", {
        "c_all_plus_one": c_all_plus_one,
        "ctype_profiles": ctype_profiles,
        "proton_neutron_ctype_diff_indices": diff_cr_pn,
        "tritium_helium3_ctype_diff_indices": diff_cr_t_he3,
    })
    wb.add_data("step3_matrix_m_sign_only_traces", {
        "tr_M_sign_proton_50dps": mp.nstr(trm_sign_p, 50),
        "tr_M_sign_neutron_50dps": mp.nstr(trm_sign_n, 50),
        "delta_sign_neutron_minus_proton": mp.nstr(delta_sign_pn, 50),
        "tr_M_sign_tritium_borromean_50dps": mp.nstr(trm_sign_t_bor, 50),
        "tr_M_sign_helium3_borromean_50dps": mp.nstr(trm_sign_he3_bor, 50),
        "delta_sign_helium3_minus_tritium_borromean": mp.nstr(delta_sign_t_he3_bor, 50),
        "tr_M_sign_tritium_grouped_50dps": mp.nstr(trm_sign_t_grp, 50),
        "tr_M_sign_helium3_grouped_50dps": mp.nstr(trm_sign_he3_grp, 50),
        "witness_note_status": witness_note_status,
    })
    wb.add_data("step4_exact_triple_cross_check", {
        "tr_M_exact_proton_50dps": mp.nstr(tau_p, 50),
        "tr_M_exact_neutron_50dps": mp.nstr(tau_n, 50),
        "delta_exact_neutron_minus_proton_50dps": mp.nstr(delta_exact_pn, 50),
        "tr_M_exact_tritium_50dps": mp.nstr(tau_t, 50),
        "tr_M_exact_helium3_50dps": mp.nstr(tau_he3, 50),
        "delta_exact_helium3_minus_tritium_50dps": mp.nstr(delta_exact_t_he3, 50),
        "closed_form_tau_M_tritium_abs_err": mp.nstr(err_cf_t, 10),
        "closed_form_tau_M_helium3_abs_err": mp.nstr(err_cf_he3, 10),
    })

    out_path = wb.save()
    print(f"Saved witness to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
