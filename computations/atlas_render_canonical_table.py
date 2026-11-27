"""Auto-render the Layer-1 canonical |tr_M(q_0)| table inside
`recursive-atom-knot-atlas-registry.md` from the
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

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ATLAS_MD = (
    HERE.parent
    / "folio"
    / "quantum-observable-universe"
    / "appendix-knot-periodic-table"
    / "recursive-atom-knot-atlas-registry.md"
)
WITNESS = _pb.witness_path("canonical-mass-table-extended.witness.json", HERE)

BEGIN_MARKER = "<!-- AUTO:canonical-tr-m-table BEGIN -->"
END_MARKER = "<!-- AUTO:canonical-tr-m-table END -->"

AME2020_DATA = {}
try:
    with open(HERE / "data" / "ame2020.json") as _f:
        _d = json.load(_f)["entries"]
        for _row in _d:
            AME2020_DATA[(_row["Z"], _row["N"])] = _row
except Exception as e:
    print(f"Warning: could not load ame2020.json: {e}")

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


def _fmt_number(v, fmt: str = "{:.4f}") -> str:
    """Format numeric value or return '—'. Strings are coerced to float."""
    if v is None or v == "":
        return "—"
    try:
        return fmt.format(float(v))
    except (TypeError, ValueError):
        return "—"


def _truncate_dps(v, max_digits: int = 16) -> str:
    """Format mpmath-string values to a fixed display length."""
    if v is None or v == "":
        return "—"
    s = str(v)
    return s[:max_digits + 2] if len(s) > max_digits + 2 else s


def render_table(witness_data: dict) -> str:
    """Render the markdown table from the witness rows.

    The atlas is the central display for the mass/β/Q/binding
    pipeline. Per repo-owner directive 2026-05-19, every row carries
    a unified `prediction_type` + `prediction_MeV_50dps` triple:

      - p, n  → prediction = nucleon mass (Borromean tower);
                CODATA reference; err in ppm.
      - D and up → prediction = binding energy (mass-table-ppb);
                AME reference; err in %.
    """
    lines = [
        "",
        "| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_{\\text{AME}}$ (MeV) | Binding Error | $M_{\\text{atom}}$ (MeV) | $M_{\\text{atom}}$ Error |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in witness_data.get("rows", []):
        Z = row["Z"]; N = row["N"]; A = row["A"]
        label = ATOM_LABEL_BY_ZN.get((Z, N), f"(Z={Z}, N={N})")
        ptype = row.get("prediction_type") or "binding_energy"
        
        # Default initialization for columns
        b_pred = "—"
        b_ref = "—"
        b_err = "—"
        m_pred = "—"
        m_err = "—"
        
        # Look up AME2020 experimental uncertainties
        exp_m_ppb_str = ""
        exp_b_pct_str = ""
        if (Z, N) in AME2020_DATA:
            ame = AME2020_DATA[(Z, N)]
            m_unc = ame.get("atomic_mass_unc_micro_u")
            m_val = ame.get("atomic_mass_micro_u")
            if m_unc is not None and m_val is not None and m_val != 0:
                exp_m_ppb_str = f" $\\pm$ {(m_unc / m_val) * 1e9:.2f}"
            
            b_unc_per_a = ame.get("binding_energy_per_A_unc_keV")
            b_total_ref = ame.get("binding_energy_total_keV")
            if b_unc_per_a is not None and b_total_ref is not None and b_total_ref != 0:
                b_unc_total = b_unc_per_a * A
                exp_b_pct_str = f" $\\pm$ {(b_unc_total / b_total_ref) * 100:.4f}"
        
        if ptype == "mass":
            # For p and n, the prediction IS the mass. Binding is 0.
            m_pred = _fmt_number(row.get("prediction_MeV_50dps"))
            err_ppm = row.get("err_ppm")
            if err_ppm is not None:
                # `float()` because err_ppm is a decimal STRING now — the
                # precision port (bean qou-3wqg) took the whole chain
                # mass_table_ppb -> canonical_mass_table_extended to mpmath, so
                # these serialize via `_precision.fmt`. Every other read here
                # goes through `_fmt_number`, which already coerces strings
                # ("Strings are coerced to float"); this is the one site doing
                # arithmetic BEFORE formatting, hence the one that needed it.
                m_err = f"{_fmt_number(float(err_ppm) * 1000.0, '{:+.2f}')}{exp_m_ppb_str} ppb"
        else:
            # For D and up, the prediction is binding energy.
            b_pred = _fmt_number(row.get("prediction_MeV_50dps"))
            b_ref = _fmt_number(row.get("B_AME_MeV"))
            err_pct = row.get("err_pct")
            if err_pct is not None:
                b_err = f"{_fmt_number(err_pct, '{:+.2f}')}{exp_b_pct_str} %"
                
            # And we have a composite mass derived from binding
            cm = row.get("composite_mass", {}) or {}
            m_pred_val = cm.get("M_pred_MeV")
            if m_pred_val is not None:
                m_pred = _fmt_number(m_pred_val, "{:.4f}")
            cm_ppm_val = cm.get("err_ppm")
            if cm_ppm_val is not None:
                m_err = f"{_fmt_number(cm_ppm_val * 1000.0, '{:+.2f}')}{exp_m_ppb_str} ppb"
                
        lines.append(
            f"| {label} | {A} | {N} "
            f"| {b_pred} | {b_ref} | {b_err} | {m_pred} | {m_err} |"
        )
    lines.append("")
    method = witness_data.get("parameters", {}).get("method", "?")
    paper_floor = witness_data.get("parameters", {}).get(
        "paper_hard_floor_ppb", 780
    )
    lines.append(
        # Reader-facing caption: no script, witness or function names
        # (voice-leak drain, qou-d4kh item 4a); provenance is in the block's
        # .ts authorNotes.
        f"_Computed by the extended canonical mass-table computation "
        f"(method: {method}); nucleon masses (m_p, m_n) from the canonical "
        f"nucleon-mass routine. "
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
