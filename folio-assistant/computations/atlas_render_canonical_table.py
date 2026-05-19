"""Auto-render the Layer-1 canonical |tr_M(q_0)| table inside
`recursive-atom-knot-atlas.md` from the
`canonical-mass-table-extended.witness.json` witness.

Replaces hand-edited tabular content so atoms beyond ⁴He (⁵Li, ⁶Li,
...) appear automatically on each rebuild of the canonical witness.

The renderer locates the section bounded by the
`<!-- AUTO:canonical-tr-m-table BEGIN -->` and
`<!-- AUTO:canonical-tr-m-table END -->` markers in the atlas .md
and replaces its body with the freshly-rendered table.

If markers are absent the script reports the expected location and
exits without modifying the file (safe for first-run inspection).

## CLI

    python3 atlas_render_canonical_table.py            # render in place
    python3 atlas_render_canonical_table.py --dry-run  # preview only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ATLAS_MD = (
    HERE.parent.parent
    / "content"
    / "quantum-observable-universe"
    / "braids-and-knots"
    / "recursive-atom-knot-atlas.md"
)
WITNESS = HERE / "canonical-mass-table-extended.witness.json"

BEGIN_MARKER = "<!-- AUTO:canonical-tr-m-table BEGIN -->"
END_MARKER = "<!-- AUTO:canonical-tr-m-table END -->"

ATOM_LABEL_BY_ZN = {
    (1, 0): r"$\mathfrak{p}$",
    (0, 1): r"$\mathfrak{n}$",
    (1, 1): "D",
    (1, 2): "T",
    (2, 1): r"${}^3$He",
    (2, 2): r"${}^4$He",
    (3, 2): r"${}^5$Li",
    (3, 3): r"${}^6$Li",
    (3, 4): r"${}^7$Li",
    (4, 3): r"${}^7$Be",
    (4, 4): r"${}^8$Be",
}


def render_table(witness_data: dict) -> str:
    """Render the markdown table from the witness rows."""
    lines = [
        "",
        "| Atom | $A$ | $n$ | $\\|\\mathrm{tr}_M(\\beta_{\\text{atom}}, q_0)\\|$ | Wall (s) |",
        "|---|---|---|---|---|",
    ]
    for row in witness_data.get("rows", []):
        Z = row["Z"]; N = row["N"]; A = row["A"]; n = row["n_strands"]
        label = ATOM_LABEL_BY_ZN.get((Z, N), f"(Z={Z}, N={N})")
        tr_m = row.get("tr_M_q0_canonical_50dps", "—")
        # Display only the first 16 significant digits
        if tr_m and tr_m != "—":
            tr_m_short = tr_m[:18] if len(tr_m) > 18 else tr_m
            tr_m_md = f"${tr_m_short}$"
        else:
            tr_m_md = "—"
        # Look up wall from any "rust_duration_ms" / row.get... (absent in
        # current schema; use a placeholder, can be added if we record it)
        wall = "—"  # the per-row wall isn't currently in the witness
        lines.append(f"| {label} | {A} | {n} | {tr_m_md} | {wall} |")
    lines.append("")
    method = witness_data.get("parameters", {}).get("method", "?")
    paper_floor = witness_data.get("parameters", {}).get(
        "paper_hard_floor_ppb", 780
    )
    lines.append(
        f"_Computed via [`canonical_mass_table_extended.py`]"
        f"(https://github.com/litlfred/qou/blob/main/folio-assistant/"
        f"computations/canonical_mass_table_extended.py) "
        f"(method=`{method}`). Witness: "
        f"[`canonical-mass-table-extended.witness.json`]"
        f"(https://github.com/litlfred/qou/blob/main/folio-assistant/"
        f"computations/canonical-mass-table-extended.witness.json). "
        f"Paper hard floor (CAL-2 propagation): ~{int(paper_floor)} ppb._"
    )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the rendered section without writing.")
    args = parser.parse_args()

    if not WITNESS.exists():
        print(f"  ERROR: witness not found at {WITNESS}")
        return 2
    if not ATLAS_MD.exists():
        print(f"  ERROR: atlas .md not found at {ATLAS_MD}")
        return 2

    witness = json.loads(WITNESS.read_text())
    # parameters lives at TOP level (WitnessBuilder convention); rows
    # live under `data`. Merge so render_table sees both — otherwise
    # `parameters.method` would render as "?" (Copilot review #708).
    merged = dict(witness)
    if "data" in witness and isinstance(witness["data"], dict):
        for k, v in witness["data"].items():
            merged[k] = v
    rendered = render_table(merged)

    md = ATLAS_MD.read_text()
    if BEGIN_MARKER not in md or END_MARKER not in md:
        print(f"  Markers not yet present in atlas .md.")
        print(f"  Add this block at the desired location:")
        print()
        print(f"  {BEGIN_MARKER}")
        print(rendered)
        print(f"  {END_MARKER}")
        print()
        if args.dry_run:
            return 0
        print(f"  --dry-run: no write; insert the markers manually first.")
        return 1

    start = md.find(BEGIN_MARKER) + len(BEGIN_MARKER)
    end = md.find(END_MARKER)
    new_md = md[:start] + "\n" + rendered + "\n" + md[end:]

    if args.dry_run:
        print("=" * 80)
        print("DRY RUN — rendered table:")
        print("=" * 80)
        print(rendered)
        print("=" * 80)
        return 0

    ATLAS_MD.write_text(new_md)
    print(f"  Updated: {ATLAS_MD}")
    print(f"  Rendered {len(merged.get('rows', []))} atom rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
