#!/usr/bin/env python3
"""Render per-Z sections of the recursive atom-knot atlas from the
per-Z canonical-isotope-witness shards.

Companion to `atlas_render_canonical_table.py`. That script renders
the Layer-1 |tr_M| highlights at the top of
`recursive-atom-knot-atlas.md`. This one renders the **full AME
2020 coverage** as per-element sections at the bottom of the same
file, between the AUTO:per-z-sections markers.

Source: every `canonical-isotope-witness-Z<NN>.witness.json`
emitted by `canonical_isotope_witness.py`.

Per repo-owner directives 2026-05-19:
  - "expand to make sure all isotopes"
  - "keep recursive knot atlas an integral part of mass / beta /
     Q / binding pipeline"
  - Atlas presentation: per-Z section + summary header (user pick).

CLI:
    python3 atlas_render_per_z.py            # render in place
    python3 atlas_render_per_z.py --dry-run  # preview only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AME2020_DATA = {}
try:
    with open(Path(__file__).resolve().parent / "data" / "ame2020.json") as _f:
        _d = json.load(_f)["entries"]
        for _row in _d:
            AME2020_DATA[(_row["Z"], _row["N"])] = _row
except Exception as e:
    print(f"Warning: could not load ame2020.json: {e}")

HERE = Path(__file__).resolve().parent
ATLAS_MD = (
    HERE.parent
    / "content"
    / "quantum-observable-universe"
    / "appendix-knot-periodic-table"
    / "recursive-atom-knot-atlas.md"
)

BEGIN_MARKER = "<!-- AUTO:per-z-sections BEGIN -->"
END_MARKER = "<!-- AUTO:per-z-sections END -->"

ELEMENT_NAMES = {
    0: "neutron",
    1: "Hydrogen", 2: "Helium", 3: "Lithium", 4: "Beryllium",
    5: "Boron", 6: "Carbon", 7: "Nitrogen", 8: "Oxygen",
    9: "Fluorine", 10: "Neon", 11: "Sodium", 12: "Magnesium",
    13: "Aluminium", 14: "Silicon", 15: "Phosphorus", 16: "Sulfur",
    17: "Chlorine", 18: "Argon", 19: "Potassium", 20: "Calcium",
    21: "Scandium", 22: "Titanium", 23: "Vanadium", 24: "Chromium",
    25: "Manganese", 26: "Iron", 27: "Cobalt", 28: "Nickel",
    29: "Copper", 30: "Zinc", 31: "Gallium", 32: "Germanium",
    33: "Arsenic", 34: "Selenium", 35: "Bromine", 36: "Krypton",
    37: "Rubidium", 38: "Strontium", 39: "Yttrium", 40: "Zirconium",
    41: "Niobium", 42: "Molybdenum", 43: "Technetium", 44: "Ruthenium",
    45: "Rhodium", 46: "Palladium", 47: "Silver", 48: "Cadmium",
    49: "Indium", 50: "Tin", 51: "Antimony", 52: "Tellurium",
    53: "Iodine", 54: "Xenon", 55: "Caesium", 56: "Barium",
    57: "Lanthanum", 58: "Cerium", 59: "Praseodymium", 60: "Neodymium",
    61: "Promethium", 62: "Samarium", 63: "Europium", 64: "Gadolinium",
    65: "Terbium", 66: "Dysprosium", 67: "Holmium", 68: "Erbium",
    69: "Thulium", 70: "Ytterbium", 71: "Lutetium", 72: "Hafnium",
    73: "Tantalum", 74: "Tungsten", 75: "Rhenium", 76: "Osmium",
    77: "Iridium", 78: "Platinum", 79: "Gold", 80: "Mercury",
    81: "Thallium", 82: "Lead", 83: "Bismuth", 84: "Polonium",
    85: "Astatine", 86: "Radon", 87: "Francium", 88: "Radium",
    89: "Actinium", 90: "Thorium", 91: "Protactinium", 92: "Uranium",
    93: "Neptunium", 94: "Plutonium", 95: "Americium", 96: "Curium",
    97: "Berkelium", 98: "Californium", 99: "Einsteinium", 100: "Fermium",
    101: "Mendelevium", 102: "Nobelium", 103: "Lawrencium",
    104: "Rutherfordium", 105: "Dubnium", 106: "Seaborgium",
    107: "Bohrium", 108: "Hassium", 109: "Meitnerium", 110: "Darmstadtium",
    111: "Roentgenium", 112: "Copernicium", 113: "Nihonium",
    114: "Flerovium", 115: "Moscovium", 116: "Livermorium",
    117: "Tennessine", 118: "Oganesson",
}


def _fmt(v, fmt: str = "{:.4f}") -> str:
    if v is None:
        return "—"
    try:
        return fmt.format(float(v))
    except (TypeError, ValueError):
        return "—"


_STATUS_BADGES = {
    "canonical-substrate": "🟢 substrate",
    "canonical-with-empirical-assignment": "🟡 +empirical-(K,ρ)",
    "canonical-recursive": "🟢 recursive",
    "heuristic": "🟠 heuristic",
    "pending": "⚪ pending",
}


def render_row(r: dict) -> str:
    """One markdown table row for an isotope."""
    A = r["A"]
    element = r.get("element", "?")
    if r["Z"] == 0 and r["N"] == 1:
        label = "$\\mathfrak{n}$"
    elif r["Z"] == 1 and r["N"] == 0:
        label = "$\\mathfrak{p}$"
    else:
        label = f"${{}}^{{{A}}}${element}"
    
    pred = _fmt(r.get("prediction_MeV_50dps"))
    
    
    # Always ppb for binding
    err_val = r.get("err_ppm")
    if err_val is not None:
        err = _fmt(err_val * 1000.0, "{:+.2f}")
        err_cell = f"{err}"
    else:
        err_cell = "—"
    
    cm = r.get("composite_mass", {}) or {}
    cm_pred = _fmt(cm.get("M_pred_MeV"), "{:.4f}")
    
    cm_ppm_val = cm.get("err_ppm")
    if cm_ppm_val is not None:
        cm_ppb = _fmt(cm_ppm_val * 1000.0, "{:+.2f}")
        cm_cell_err = f"{cm_ppb}"
    else:
        cm_cell_err = "—"
        
    cm_cell_pred = f"{cm_pred}" if cm_pred != "—" else "—"
    
    # Calculate experimental ppb
    cm_cell_err_exp = "—"
    if (r["Z"], r["N"]) in AME2020_DATA:
        ame = AME2020_DATA[(r["Z"], r["N"])]
        unc = ame.get("atomic_mass_unc_micro_u")
        val = ame.get("atomic_mass_micro_u")
        if unc is not None and val is not None and val != 0:
            exp_ppb = (unc / val) * 1e9
            cm_cell_err_exp = f"{exp_ppb:.2f}"
            
    return (
        f"| {label} | {r['A']} | {r['N']} | {pred} | {err_cell} "
        f"| {cm_cell_pred} | {cm_cell_err} | {cm_cell_err_exp} |"
    )


def render_z_section(shard: dict) -> list[str]:
    """One markdown subsection per element."""
    rows = shard.get("data", {}).get("rows", [])
    Z = shard.get("parameters", {}).get("Z", -1)
    el = shard.get("parameters", {}).get("element", "?")
    name = ELEMENT_NAMES.get(Z, el)
    n_total = shard.get("parameters", {}).get("rows_total", len(rows))
    n_pred = shard.get("parameters", {}).get("rows_with_prediction", 0)
    n_cm = shard.get("parameters", {}).get("rows_with_composite_mass", 0)
    coverage_note = (
        f"_{n_pred} of {n_total} isotopes with a framework "
        f"prediction; {n_cm} of {n_total} with $M_{{\\mathrm{{atom}}}}$ "
        f"$M = N \\cdot m_n + Z \\cdot m_p + Z \\cdot m_e - B$._"
    )
    lines = [
        "",
        f"### {name} (Z = {Z})",
        "",
        coverage_note,
        "",
        "| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(render_row(r))
    return lines


def render_all(shards: list[dict]) -> str:
    """Render the full per-Z section block."""
    lines: list[str] = [""]
    lines.append("## Per-element coverage (AME 2020 cross-reference)")
    lines.append("")
    lines.append(
        "_Auto-rendered from per-Z shards "
        "`canonical-isotope-witness-Z<NN>.witness.json` "
        "(emitted by [`canonical_isotope_witness.py`]"
        "(https://github.com/litlfred/qou/blob/main/folio-assistant/"
        "computations/canonical_isotope_witness.py)). Each row carries "
        "the framework prediction, the AME 2020 reference, and the residual. "
        "For free nucleons (p, n) the prediction is the mass "
        "conditional on `conj:borromean-baryon-mass-formula`. "
        "For D and up, the prediction is the binding energy; "
        "the AME 2020 reference is the total binding energy. "
        "$M_{\\mathrm{atom}}$ is the composite atomic mass "
        "$N \\cdot m_n + Z \\cdot m_p + Z \\cdot m_e - B$."
    )
    for shard in shards:
        lines.extend(render_z_section(shard))
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if not ATLAS_MD.exists():
        print(f"  ERROR: atlas .md not found at {ATLAS_MD}")
        return 2

    shards: list[dict] = []
    for p in sorted(HERE.glob("canonical-isotope-witness-Z*.witness.json")):
        try:
            shards.append(json.loads(p.read_text()))
        except json.JSONDecodeError:
            pass

    if not shards:
        print("  no per-Z shards found — run canonical_isotope_witness.py first")
        return 1

    rendered = render_all(shards)

    md = ATLAS_MD.read_text()
    if BEGIN_MARKER not in md or END_MARKER not in md:
        if args.dry_run:
            print("=" * 80)
            print(f"DRY RUN — markers not yet present in atlas .md.")
            print(f"Insert between these tags:")
            print(f"  {BEGIN_MARKER}")
            print(rendered[:500] + "...")
            print(f"  {END_MARKER}")
            return 0
        # Append the markers + rendered content at the end of the file.
        md = (
            md.rstrip()
            + "\n\n"
            + BEGIN_MARKER + "\n"
            + rendered + "\n"
            + END_MARKER + "\n"
        )
        ATLAS_MD.write_text(md)
        print(f"  Inserted per-Z section markers + content into {ATLAS_MD}")
        print(f"  Rendered {len(shards)} per-Z sections.")
        return 0

    start = md.find(BEGIN_MARKER) + len(BEGIN_MARKER)
    end = md.find(END_MARKER)
    new_md = md[:start] + "\n" + rendered + "\n" + md[end:]

    if args.dry_run:
        print("=" * 80)
        print(f"DRY RUN — would render {len(shards)} sections")
        print(rendered[:800] + "...")
        return 0

    ATLAS_MD.write_text(new_md)
    print(f"  Updated: {ATLAS_MD}")
    print(f"  Rendered {len(shards)} per-Z sections.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
