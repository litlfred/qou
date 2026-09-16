#!/usr/bin/env python3
"""relative_reeb_datum_trace_angle_probe.py — the candidate relative Reeb datum measured on committed data.
Beans `qou-jfx8` (RelativeReebDatum) and `qou-1x56` (the ⋈_{⟨knot_con, phase_space⟩} roast); milestone `qou-cgsn`.
Companion to `QOU/MassTheory/RelativeReebDatum.lean` (the class; clause `trM_lightCone_mem`) and
`QOU/MassTheory/InterfaceLetterCrossingMixture.lean` (`interfaceLetter_eq_mix`, `trace_interfaceLetter`).

WHAT IS MEASURED (committed inputs only: y-lambda-at-q0, chi-{proton,neutron}-h3, atom-chi-rust-{d,t,3he,4he})
  (E)  the inverse-crossing weight e = −d/h of every production letter template: interfaces pp (d = 0),
       pn (d = −h(1 − δ/2)/2, `pyhecke.constants.pn_interface_offset`, bring_color_weighted), nn (d = −h); intra-nucleon
       quark pairs uu / ud / dd (d = 0, −h/2, −h; `pyhecke.atom.nucleon_gen_chains`). Each letter is (1 − e)σ + eσ⁻¹,
       and its bond factor is (1 − e) z_D + e (z_D − h) = z_D + d — checked as an identity at q₀.
  (θ)  the TRACE-LEVEL candidate angle θ(X) = arccos(tr_M(light cone)) with tr_M(light cone) := tr_M(atom)/tr_M(free)
       = ∏_bonds (z_D + d) (the corpus's bond law), for D, T, ³He, ⁴He — the clause `trM_lightCone_mem` of the class
       requires that trace in [−1, 1]; here it lies in (0, 1).
  (r)  the BLOCK-LEVEL candidate ratio r_λ = χ_λ(atom)/χ_λ(free) on the two-row (y > 0) support: how many blocks per
       nucleus have |r_λ| ≤ 1 (an arccos would be defined) and how many have r_λ < 0 (the bound word flips the sign).
  (n)  the normalised-character candidate χ_λ(atom)/f^λ on the two-row support: how many lie in [−1, 1].

WHAT IS NOT CLAIMED: that any of these IS the relative Reeb angle. The class leaves `lightCone` as data; this probe
records which candidate definitions are well-defined on the production words and which are not. No fit, no
selection, no q₀ arithmetic beyond the committed strings; mpmath 60 dps.
-- Ref: [manuscript] prop:figure-eight-reeb-rotation; def:ew-interface-knot; bean qou-jfx8
"""
from __future__ import annotations
import json
import sys
from math import factorial  # float64-ok: exact ints only (hook-length count f^λ); //, %, == only, never a float
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
C = REPO / "computations"
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Yw = json.loads((C / "y-lambda-at-q0.witness.json").read_text(encoding="utf-8"))
assert Yw["q0Anchor"] == "proton"


def hook_dim(lam):
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j - 1) + (conj[j] - i - 1) + 1
    assert factorial(n) % prod == 0
    return factorial(n) // prod


def load_y(n):
    return {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"]) for e in Yw["data"]["by_n"][str(n)]}


def load_atom(tag):
    w = json.loads((C / f"atom-chi-rust-{tag}.witness.json").read_text(encoding="utf-8"))
    atom = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["data"]["atom"]["by_partition"]}
    free = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["data"]["free"]["by_partition"]}
    return atom, free, {"computedAt": w["computedAt"], "commitSha": w["commitSha"][:12]}


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    q0 = mp.mpf(Yw["q0Value"])
    h = q0 - 1 / q0
    zD = q0 ** 3 / (q0 ** 2 + 1)
    delta = (q0 - 1) ** 2 * (1 - q0 ** -4) / 3
    d = {"pp": mp.mpf(0), "pn": -(h * (1 - delta / 2) / 2), "nn": -h, "uu": mp.mpf(0), "ud": -h / 2, "dd": -h}
    e = {k: -v / h for k, v in d.items()}
    bond = {k: zD + v for k, v in d.items()}
    mix = {k: (1 - e[k]) * zD + e[k] * (zD - h) for k in d}
    worst_mix = max(abs(bond[k] - mix[k]) for k in d)
    print("inverse-crossing weights e = −d/h:", {k: mp.nstr(v, 20) for k, v in e.items()})
    print("bond factors z_D + d:", {k: mp.nstr(v, 20) for k, v in bond.items()})
    check("every_production_letter_template_has_e_in_unit_interval", all(0 <= v <= 1 for v in e.values()), "e = −d/h for pp, pn, nn, uu, ud, dd")
    check("bond_factor_equals_mixture_of_crossing_traces_to_1e-50", worst_mix < mp.mpf("1e-50"), "(1−e) z_D + e (z_D − h) = z_D + d; Lean trace_interfaceLetter")
    check("e_pn_is_half_minus_delta_over_four", abs(e["pn"] - (mp.mpf(1) / 2 - delta / 4)) < mp.mpf("1e-50"), "pn_interface_offset, bring_color_weighted")

    chain_kinds = {"d": ["pn"], "t": ["pn", "nn"], "3he": ["pp", "pn"], "4he": ["pp", "pn", "nn"]}
    per = {}
    for tag, n in {"d": 6, "t": 9, "3he": 9, "4he": 12}.items():
        atom, free, meta = load_atom(tag)
        y = load_y(n)
        two_row = [l for l in y if y[l] > 0]
        tr_a = sum(y[l] * atom[l] for l in y)
        tr_f = sum(y[l] * free[l] for l in y)
        ratio = tr_a / tr_f
        bond_prod = mp.mpf(1)
        for k in chain_kinds[tag]:
            bond_prod *= bond[k]
        theta = mp.acos(ratio)
        r = {l: atom[l] / free[l] for l in two_row}
        nrm = {l: atom[l] / hook_dim(l) for l in two_row}
        per[tag] = {
            "chi_witness": meta, "bond_chain_kinds": chain_kinds[tag],
            "tr_light_cone_ratio": mp.nstr(ratio, 50), "bond_product": mp.nstr(bond_prod, 50), "abs_dev": mp.nstr(abs(ratio - bond_prod), 5),
            "theta_trace_rad": mp.nstr(theta, 40), "theta_trace_deg": mp.nstr(theta * 180 / mp.pi, 30),
            "two_row_blocks": [str(l) for l in two_row],
            "block_ratio_chi_atom_over_chi_free": {str(l): mp.nstr(r[l], 25) for l in two_row},
            "block_ratio_n_abs_le_1": sum(1 for l in two_row if abs(r[l]) <= 1),
            "block_ratio_n_negative": sum(1 for l in two_row if r[l] < 0),
            "normalised_chi_atom_over_dim": {str(l): mp.nstr(nrm[l], 25) for l in two_row},
            "normalised_n_in_unit_interval": sum(1 for l in two_row if abs(nrm[l]) <= 1),
        }
        print(f"{tag:>4}: tr(light cone) = {mp.nstr(ratio, 15)} = ∏(z+d) {mp.nstr(bond_prod, 15)}  θ_trace = {mp.nstr(theta * 180 / mp.pi, 10)}°"
              f"  block ratios |r|≤1: {per[tag]['block_ratio_n_abs_le_1']}/{len(two_row)}, r<0: {per[tag]['block_ratio_n_negative']};"
              f"  χ/dim in [−1,1]: {per[tag]['normalised_n_in_unit_interval']}/{len(two_row)}")
        for l in two_row:
            print(f"        {str(l):<8} r = {mp.nstr(r[l], 12):>16}   χ_atom/dim = {mp.nstr(nrm[l], 12):>16}")
    check("trace_of_light_cone_in_open_unit_interval_all_four", all(0 < mp.mpf(per[t]["tr_light_cone_ratio"]) < 1 for t in per),
          "clause trM_lightCone_mem holds on the production chains; θ_trace defined")
    check("trace_of_light_cone_equals_bond_product_to_1e-40", all(mp.mpf(per[t]["abs_dev"]) < mp.mpf("1e-40") for t in per), "bond law, re-measured")
    thetas = [mp.mpf(per[t]["theta_trace_rad"]) for t in ("d", "3he", "t", "4he")]
    check("theta_trace_increases_with_bond_count_D_lt_3He_lt_T_lt_4He", thetas[0] < thetas[1] < thetas[2] < thetas[3],
          "one, two, two, three bonds; the nn bond factor is the smallest so T > 3He")
    check("block_level_ratio_candidate_is_not_uniformly_definable", any(per[t]["block_ratio_n_abs_le_1"] < len(per[t]["two_row_blocks"]) for t in per),
          "some two-row block has |χ_atom/χ_free| > 1 on at least one nucleus — arccos of the block ratio is not a datum")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("relative-reeb-datum-trace-angle", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0_anchor_reason": "committed proton-pinned witnesses only; q0 enters through the committed string",
        "description": ("PROBE (beans qou-jfx8, qou-1x56): candidate relative-Reeb data on committed words. Every production letter "
                        "is (1−e)σ + eσ⁻¹ with e ∈ [0,1] (pp 0, pn ½−δ/4, nn 1; uu 0, ud ½, dd 1); the trace-level candidate "
                        "θ = arccos(tr(atom)/tr(free)) is defined for D/T/3He/4He because the bond product lies in (0,1); the "
                        "block-level ratio candidate is not uniformly definable. Nothing selected; the class leaves lightCone as data."),
        "weight_family": "markov_y_lambda_convention_D",
        "q0_from_y_witness": mp.nstr(q0, 50), "h": mp.nstr(h, 50), "z_D": mp.nstr(zD, 50), "delta_flavor_split": mp.nstr(delta, 50),
        "letter_offsets_d": {k: mp.nstr(v, 50) for k, v in d.items()},
        "inverse_crossing_weights_e": {k: mp.nstr(v, 50) for k, v in e.items()},
        "bond_factors_z_plus_d": {k: mp.nstr(v, 50) for k, v in bond.items()},
        "pn_convention": "bring_color_weighted",
        "per_nucleus": per,
        "K_2H_negative_nf_coefficient_note": "k_versus_selected_operator_probe.py: K(2H) = σ₀ + D_PN·1 has exactly one negative NF coefficient, D_PN = −e_pn·h (cited, not recomputed here)",
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
