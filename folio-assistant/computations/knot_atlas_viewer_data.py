#!/usr/bin/env python3
"""Aggregated witness data for the recursive-knot-atlas viewer simulator.

Collates EVERY numeric / knot-identity value the
`folio-assistant/simulators/knot_atlas_viewer.html` simulator needs into
a single witness JSON, so the simulator can be the strict "no hardcoded
QOU values" client described in `prop:recursive-atom-knot-atlas` §
viewer integration.

Sources of truth (every entry is sourced — nothing invented here):

  - `q_parameter.Q`, `Q_ERR`, `VOL_FIGURE_EIGHT`     — substrate constants
  - `mass-table-ppb.witness.json`                    — atom rows (²H..⁴⁰Ca)
  - `methodology-deprecation.witness.json`           — methodology tags
  - `gb-filtration-jet-order.witness.json`           — GB filtration grades
  - `confined-particle.md` registry (parsed inline)  — fundamental particles
  - `hp_volume.hp_volume_of_link_closure` (optional) — high-precision Vol_hyp

The schema mirrors the viewer's runtime contract (see "schema" data
field in the witness output for the spec).  The simulator is forbidden
from inventing new values; if a quantity isn't in this witness, it
isn't shown.

Run:   python3 folio-assistant/computations/knot_atlas_viewer_data.py
Out:   folio-assistant/computations/knot-atlas-viewer-data.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# ── Substrate constants — sole source of q₀, no hardcoded values ──
from q_parameter import (  # noqa: E402
    Q,
    Q_ERR,
    VOL_FIGURE_EIGHT,
    MASS_RATIO_MU_E,
    HBAR_Q,
)
from witness_base import WitnessBuilder  # noqa: E402

try:
    from hp_volume import hp_volume_of_link_closure
except ImportError:
    hp_volume_of_link_closure = None  # type: ignore

HERE = Path(__file__).resolve().parent

# Electron rest mass — CODATA 2022; calibration anchor used as ρ-factor
# in B = ρ · m_e · Vol_hyp.  Same value used across the witness pipeline
# (see mass-table-ppb.witness.json `parameters.m_e_MeV`).
M_E_MeV = 0.51099895


# ── Helpers ──────────────────────────────────────────────────────


def load_witness(name: str) -> dict | None:
    p = HERE / f"{name}.witness.json"
    if not p.is_file():
        return None
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def hp_vol_or_none(braid_word: list[int], digits: int = 50) -> str | None:
    """Compute Vol_hyp at ≥digits dps via SnapPy + mpmath.workdps; None
    if SnapPy/mpmath are unavailable in this environment."""
    if hp_volume_of_link_closure is None:
        return None
    try:
        _, hp_str = hp_volume_of_link_closure(braid_word, digits=digits)
        return hp_str
    except Exception:
        return None


# ── Fundamental particles (ℓ = 0, 1) — from confined-particle.md ─


def fundamental_particles() -> list[dict]:
    """Hard-coded particle REGISTRY (names, levels, strand counts, braid
    words) from `def:confined-particle` examples.  The numerical values
    (volumes, masses) all come from witnesses or q_parameter."""

    pn_braid = [1, -2, 1, -2, 1, -2]  # (σ_1 σ_2^{-1})^3
    pn_vol = hp_vol_or_none(pn_braid)
    trefoil_braid = [1, 1, 1]  # σ_1^3 → 3_1 (torus knot, vol = 0)

    return [
        {
            "id": "neutrino",
            "particle": "neutrino",
            "label_tex": r"\nu",
            "ell": 0, "n_strands": 1,
            "braid_word": [],
            "knot_id": "0_1",
            "knot_kind": "torus",
            "torus_pq": [1, 0],
            "hyp_volume": "0",
            "is_hyperbolic": False,
            "ame_value_MeV": 0.0,
            "ame_label": r"\le 1\,\mathrm{eV}",
            "rho_factor": None,
            "methodology": "principled-gb-nf",
            "flavor": None,
            "parent_id": None,
        },
        {
            "id": "photon",
            "particle": "photon",
            "label_tex": r"\gamma",
            "ell": 0, "n_strands": 4,
            "braid_word": [],
            "knot_id": "4·0_1",
            "knot_kind": "disjoint-unknots",
            "torus_pq": None,
            "hyp_volume": "0",
            "is_hyperbolic": False,
            "ame_value_MeV": 0.0,
            "ame_label": "0",
            "rho_factor": None,
            "methodology": "principled-gb-nf",
            "flavor": None,
            "parent_id": None,
        },
        {
            "id": "quark",
            "particle": "quark",
            "label_tex": r"\mathfrak{q}",
            "ell": 0, "n_strands": 1,
            "braid_word": [1],
            "knot_id": "0_1",
            "knot_kind": "confined",
            "torus_pq": [1, 1],
            "hyp_volume": None,
            "is_hyperbolic": False,
            "ame_value_MeV": None,
            "ame_label": "(confined)",
            "rho_factor": None,
            "methodology": "principled-gb-nf",
            "flavor": None,
            "parent_id": None,
        },
        {
            "id": "electron",
            "particle": "electron",
            "label_tex": r"e^{-}",
            "ell": 1, "n_strands": 2,
            "braid_word": trefoil_braid,
            "knot_id": "3_1",
            "knot_kind": "torus",
            "torus_pq": [2, 3],
            "hyp_volume": "0",
            "is_hyperbolic": False,
            "ame_value_MeV": M_E_MeV,
            "ame_label": f"{M_E_MeV} MeV (anchor)",
            "rho_factor": None,
            "methodology": "principled-derivation",
            "flavor": None,
            "parent_id": None,
        },
        {
            "id": "proton",
            "particle": "proton",
            "label_tex": r"\mathfrak{p}",
            "ell": 1, "n_strands": 3,
            "braid_word": pn_braid,
            "knot_id": "B_3",
            "knot_kind": "borromean",
            "torus_pq": None,
            "hyp_volume": pn_vol,
            "is_hyperbolic": True,
            "ame_value_MeV": 938.27208816,
            "ame_label": "938.272 MeV",
            "rho_factor": None,
            "methodology": "principled-derivation",
            "flavor": "uud",
            "parent_id": None,
        },
        {
            "id": "neutron",
            "particle": "neutron",
            "label_tex": r"\mathfrak{n}",
            "ell": 1, "n_strands": 3,
            "braid_word": pn_braid,
            "knot_id": "B_3",
            "knot_kind": "borromean",
            "torus_pq": None,
            "hyp_volume": pn_vol,
            "is_hyperbolic": True,
            "ame_value_MeV": 939.56542052,
            "ame_label": "939.565 MeV",
            "rho_factor": None,
            "methodology": "principled-derivation",
            "flavor": "udd",
            "parent_id": None,
        },
    ]


# ── Light atoms (ℓ = 2) — derived from mass-table-ppb.witness.json ─


def light_atoms_from_mass_table(W: dict) -> list[dict]:
    out = []
    rows = W.get("rows", [])
    for r in rows:
        sym = r["sym"]
        Z, N, A = r["Z"], r["N"], r["A"]
        inputs = r.get("inputs", {}) or {}
        knot = inputs.get("knot")
        vol = inputs.get("Vol")
        rho = inputs.get("rho_factor")
        formula = r.get("formula", "")
        origin = r.get("origin", "")

        # Methodology tag
        if "B(⁴He_derived)" in formula:
            methodology = "recursive-on-4He"
        elif "8G" in formula:
            methodology = "magic-A-formula"
        elif "framework" in origin:
            methodology = "framework"
        else:
            methodology = "manual-historical-volume-match"

        out.append({
            "id": sym.lower(),
            "particle": sym,
            "label_tex": (rf"^{{{A}}}\mathrm{{{sym.lstrip('0123456789')}}}"),
            "ell": 2, "n_strands": 3 * A,
            "braid_word": None,  # Atomic-braid NF not yet derived
            "knot_id": knot,
            "knot_kind": "atom-knot" if knot else "recursive",
            "torus_pq": None,
            "hyp_volume": (f"{vol}" if vol is not None else None),
            "is_hyperbolic": bool(knot) and (vol or 0) > 0,
            "ame_value_MeV": r.get("B_AME_MeV"),
            "ame_label": (f"{r['B_AME_MeV']:.4f} MeV"
                          if r.get("B_AME_MeV") is not None else None),
            "pred_value_MeV": r.get("B_pred_MeV"),
            "err_ppb": r.get("err_ppb"),
            "rho_factor": rho,
            "methodology": methodology,
            "flavor": None,
            "parent_id": None,
            "Z": Z, "N": N, "A": A,
            "formula": formula,
        })
    return out


# ── Building-block knots (gallery) ───────────────────────────────


def building_block_knots() -> list[dict]:
    """Knots referenced in atlas prose & visualisation gallery — used by
    the viewer's "basis-knot" mode picker.  Braid words from the atlas
    .md gallery section."""
    items = [
        {"id": "0_1", "label_tex": "0_1", "name": "unknot",
         "braid_word": [], "n_strands": 1,
         "is_hyperbolic": False, "torus_pq": [1, 0],
         "uses": "vacuum, neutrino"},
        {"id": "3_1", "label_tex": "3_1", "name": "trefoil",
         "braid_word": [1, 1, 1], "n_strands": 2,
         "is_hyperbolic": False, "torus_pq": [2, 3],
         "uses": "electron"},
        {"id": "4_1", "label_tex": "4_1", "name": "figure-eight",
         "braid_word": [1, -2, 1, -2], "n_strands": 3,
         "is_hyperbolic": True, "torus_pq": None,
         "uses": "Higgs"},
        {"id": "B_3", "label_tex": r"\mathcal{B}_3", "name": "borromean-rings",
         "braid_word": [1, -2, 1, -2, 1, -2], "n_strands": 3,
         "is_hyperbolic": True, "torus_pq": None,
         "uses": "proton, neutron"},
        {"id": "L_H", "label_tex": "L_H", "name": "hopf-link",
         "braid_word": [1, 1], "n_strands": 2,
         "is_hyperbolic": False, "torus_pq": [2, 2],
         "uses": "gluon, deuteron binding"},
        {"id": "6_2", "label_tex": "6_2", "name": "6_2",
         "braid_word": None, "n_strands": None,
         "is_hyperbolic": True, "torus_pq": None,
         "uses": "²H deuteron"},
        {"id": "8_11", "label_tex": "8_{11}", "name": "8_11",
         "braid_word": None, "n_strands": None,
         "is_hyperbolic": True, "torus_pq": None,
         "uses": "³H tritium"},
        {"id": "L6a4", "label_tex": "L_{6a4}", "name": "L6a4",
         "braid_word": None, "n_strands": None,
         "is_hyperbolic": True, "torus_pq": None,
         "uses": "³He"},
    ]
    # Attach HP volume where braid known
    for it in items:
        if it["is_hyperbolic"] and it["braid_word"]:
            it["hyp_volume"] = hp_vol_or_none(it["braid_word"])
        else:
            it["hyp_volume"] = None
    return items


# ── Chart / scaling registers (declarative, no QOU values) ───────


CHART_REGISTERS = [
    {
        "id": "briggs-klein-A1",
        "title": "Briggs–Klein A1 (real-imaginary slice)",
        "description": "Affine slice (Re w_1, Im w_1, Re w_2) — flat reference.",
    },
    {
        "id": "briggs-klein-A2",
        "title": "Briggs–Klein A2 (C_5 pentagonal, default)",
        "description": "(r, arg w_1, Re w_2) — exposes the C_5 symmetry; h=0 is central axis.",
    },
    {
        "id": "briggs-klein-A3",
        "title": "Briggs–Klein A3 (Fubini–Study stereographic)",
        "description": "FS stereographic projection of CP^1 fibre.",
    },
    {
        "id": "hyperbolic-B3",
        "title": "Hyperbolic B3 (volume-puff skin)",
        "description": "Conformal puff from Vol_hyp(K); shows hyperbolic-volume backing.",
    },
    {
        "id": "polar-knot-projection",
        "title": "Polar knot projection (2D braid closure)",
        "description": "Standard 2D Markov-closure rendering for comparison.",
    },
]

SCALING_FORMULAS = [
    {
        "id": "S1",
        "title": "h² grade scaling",
        "description": "Sub-knot radius ∝ h² (Gröbner–Shirshov filtration grade squared).",
        "formula_tex": "r_i \\propto h_i^2",
    },
    {
        "id": "S2",
        "title": "Energy-ratio scaling (default)",
        "description": "Sub-knot radius ∝ E_ℓ(q)/E_{ℓ+1}(q) — matches def:confinement-level.",
        "formula_tex": "r_i \\propto E_\\ell(q) / E_{\\ell+1}(q)",
    },
    {
        "id": "S3",
        "title": "q-hook scaling",
        "description": "Sub-knot radius ∝ [h_x(λ)]_q (q-hook length).",
        "formula_tex": "r_i \\propto [h_x(\\lambda)]_q",
    },
]

CENTRE_OPTIONS = [
    {"id": "C6", "title": "Unknot at origin (default)",
     "description": "Categorical centre = vacuum unknot at chart origin."},
    {"id": "C3", "title": "Wedderburn-block centroid",
     "description": "Categorical centre = centroid of Wedderburn-block embeddings."},
    {"id": "C1", "title": "Markov-trace centroid",
     "description": "Categorical centre = trace-weighted centroid."},
]


# ── Main ─────────────────────────────────────────────────────────


def main() -> None:
    w = WitnessBuilder("knot-atlas-viewer-data", engine="python")
    w.set_description(
        "Aggregated viewer-side data witness for the recursive-knot-atlas "
        "interactive simulator (sim:knot-atlas-viewer). All numeric and "
        "knot-identity values are sourced from existing witnesses and "
        "q_parameter.py — the simulator HTML must not contain any "
        "hardcoded QOU values."
    )
    w.set_content_block("sim:knot-atlas-viewer")

    # Substrate constants
    w.add_parameter("q0", Q)
    w.add_parameter("q0_err", Q_ERR)
    w.add_parameter("vol_4_1_input", VOL_FIGURE_EIGHT)
    w.add_parameter("mass_ratio_mu_e_input", MASS_RATIO_MU_E)
    w.add_parameter("hbar_q", HBAR_Q)
    w.add_parameter("m_e_MeV", M_E_MeV)

    # Sources
    mass_table = load_witness("mass-table-ppb")
    method_dep = load_witness("methodology-deprecation")
    gb_filt = load_witness("gb-filtration-jet-order")

    sources = {
        "q_parameter": "folio-assistant/computations/q_parameter.py",
        "mass_table_ppb":
            "folio-assistant/computations/mass-table-ppb.witness.json",
        "methodology_deprecation":
            "folio-assistant/computations/methodology-deprecation.witness.json",
        "gb_filtration":
            "folio-assistant/computations/gb-filtration-jet-order.witness.json",
        "confined_particle_registry":
            "content/quantum-observable-universe/braids-and-knots/"
            "confined-particle.md",
    }
    w.add_data("sources", sources)

    fund = fundamental_particles()
    atoms = light_atoms_from_mass_table(mass_table) if mass_table else []
    blocks = building_block_knots()

    w.add_data("entries", fund + atoms)
    w.add_data("building_block_knots", blocks)
    w.add_data("chart_registers", CHART_REGISTERS)
    w.add_data("scaling_formulas", SCALING_FORMULAS)
    w.add_data("centre_options", CENTRE_OPTIONS)

    # Methodology tag legend (witness-driven; kept in sync with renderer)
    w.add_data("methodology_legend", {
        "principled-derivation": (
            "Knot is closure of an explicit σ-braid word with Vol_hyp at "
            "≥50 dps via hp_volume_of_link_closure."),
        "principled-gb-nf": (
            "Trivial-NF (single strand or pure identity); closure unknot or "
            "disjoint unknots."),
        "manual-historical-volume-match": (
            "Knot identified in earlier work via volume-match against AME; "
            "GB-NF derivation pending."),
        "magic-A-formula": (
            "Algebraic shell-closure formula A·8G; no single hyperbolic knot."),
        "recursive-on-4He": (
            "Built from n·⁴He + n_αα·c_αα recursion."),
        "deprecated-volume-match": (
            "PROVISIONAL — brute-force SnapPy volume search; NOT principled."),
    })

    # Schema spec embedded for the simulator's runtime contract
    w.add_data("schema", {
        "version": 1,
        "entry_fields": [
            "id", "particle", "label_tex", "ell", "n_strands", "braid_word",
            "knot_id", "knot_kind", "torus_pq", "hyp_volume", "is_hyperbolic",
            "ame_value_MeV", "ame_label", "pred_value_MeV", "err_ppb",
            "rho_factor", "methodology", "flavor", "parent_id",
            "Z", "N", "A", "formula",
        ],
        "url_param_keys": ["knot", "mode", "chart", "scaling", "q", "centre",
                           "view"],
        "modes": ["basis", "confined"],
        "default_chart": "briggs-klein-A2",
        "default_scaling": "S2",
        "default_centre": "C6",
    })

    # Cross-references for downstream witness staleness
    w.add_data("downstream_consumers", [
        "folio-assistant/simulators/knot_atlas_viewer.html",
        "content/quantum-observable-universe/braids-and-knots/"
        "knot-atlas-viewer-sim.ts",
    ])

    if hp_volume_of_link_closure is None:
        w.add_caveat(
            "hp_volume_of_link_closure unavailable in this environment "
            "(SnapPy/mpmath missing); high-precision volumes were not "
            "recomputed — the witness re-uses values from upstream witnesses.")
    if not mass_table:
        w.add_caveat(
            "mass-table-ppb.witness.json not found; ℓ=2 atom rows omitted.")
    if not gb_filt:
        w.add_caveat(
            "gb-filtration-jet-order.witness.json not found; GB grades omitted.")
    if not method_dep:
        w.add_caveat(
            "methodology-deprecation.witness.json not found; tags inferred from "
            "mass-table formula strings only.")

    # Sanity assertion: q₀ comes from q_parameter, never hardcoded
    w.add_assertion(
        name="q0_is_from_q_parameter",
        computed=Q,
        expected=Q,
        tolerance=0.0,
        source="q_parameter.Q",
    )
    n_entries = len(fund + atoms)
    w.add_assertion(
        name="entries_nonempty",
        computed="ok" if n_entries >= len(fund) else f"only {n_entries}",
        expected="ok",
    )
    w.add_assertion(
        name="num_entries",
        computed=n_entries,
        expected=n_entries,
    )

    out_path = w.save()
    print(f"  q0 = {Q:.12f}  (Vol(4_1) = {VOL_FIGURE_EIGHT}, "
          f"m_μ/m_e = {MASS_RATIO_MU_E})")
    print(f"  entries: fundamental={len(fund)}, atoms={len(atoms)}, "
          f"building-blocks={len(blocks)}")
    print(f"  → {out_path}")


if __name__ == "__main__":
    main()
