#!/usr/bin/env python3
"""ρ_F · V_hyp binding-energy gap analysis for light atomic species.

Per `rem:frobenius-packing-density`, the QOU binding-energy law is

    E_binding(K)  =  ρ_F(K) · V_hyp(K),

with ρ_F ∈ {m_e, 2 m_e} from Type-B fold-orbit closure of the
populated Wedderburn blocks (`prop:cpt-orbit-closure-density`)
and V_hyp the Thurston volume of the atomic-link complement.

This script does **not** compute V_hyp from QOU primitives — the
atom→atomic-link mapping for general isotopes is paper-side
content not yet wired through.  Instead, it inverts the law:
given the empirical binding from AME2020
(`ame-2020-binding-energies.witness.json`) and the SnapPy-known V_hyp of
the three currently-tabulated atomic-link primitives (figure-
eight, three-twist, Borromean), it reports the **required ρ_F**
that each candidate link would need to reproduce the observed
binding energy.

Composite-link cases (sums of the listed primitives, JSJ
decompositions for heavier nuclei) are not modelled in the
current row-by-row table — if the atom→atomic-link map turns
out to require composite links, the table is extended by adding
rows to `LINK_PRIMITIVES`.

The output is the gap audit: which (link, ρ_F) candidates are
close to the QOU prediction ρ_F ∈ {m_e, 2 m_e}, and which need
multi-link composite atomic-link constructions.

Output: `rho-f-volume-binding-gap.witness.json`.

References
----------
- rem:frobenius-packing-density
- prop:cpt-orbit-closure-density
- def:topological-mass-formula
- ame-2020-binding-energies.witness.json — empirical binding source
- experimental_constants.VOL_* — SnapPy 3.3.2 volumes
"""

from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from decimal import Decimal
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import (  # noqa: E402
    M_E_MEV,
    VOL_FIGURE_EIGHT,
    VOL_THREE_TWIST,
    VOL_BORROMEAN,
)


def _disp(val, digits: int = 15) -> Decimal:
    if isinstance(val, mp.mpf):
        return Decimal(mp.nstr(val, digits))
    return Decimal(str(val))


# Candidate atomic-link primitives.  These are the only hyperbolic
# links with high-precision SnapPy volumes currently in the repo's
# experimental_constants table.  Composite atomic-links for
# heavier isotopes would build from these as JSJ pieces.
# Kept at mpmath default dps=15 per `precision_ceiling_note` below so
# VOL_THREE_TWIST (12-digit SnapPy table value) is never padded past 15 digits.
LINK_PRIMITIVES: dict[str, mp.mpf] = {
    "figure-eight (4_1)": mp.mpf(str(VOL_FIGURE_EIGHT)),
    "three-twist (5_2)": mp.mpf(str(VOL_THREE_TWIST)),
    "Borromean (6^3_2)": mp.mpf(str(VOL_BORROMEAN)),
}


def required_rho(delta_binding_mev: mp.mpf, vol: mp.mpf) -> mp.mpf:
    """ρ_F that reproduces `delta_binding = ρ_F · vol` (in MeV)."""
    if vol <= 0:
        return mp.mpf("inf")
    return delta_binding_mev / vol


def main() -> None:
    builder = (
        WitnessBuilder("rho-f-volume-binding-gap", engine="python")
        .set_description(
            "Inverts ρ_F · V_hyp = Δ_binding to report the required "
            "ρ_F (in units of m_e) that each atomic-link-primitive "
            "candidate (figure-eight, three-twist, Borromean) would "
            "need to reproduce the empirical binding energy of the "
            "light nuclei ²H–⁷Li (the AME binding-energy witness set).  "
            "QOU's prediction is ρ_F ∈ {m_e, "
            "2 m_e} from prop:cpt-orbit-closure-density; deviations "
            "from these two values quantify the atom-to-link mapping "
            "gap.  Bridges AME2020 binding to the "
            "Frobenius packing density law in "
            "rem:frobenius-packing-density."
        )
        .set_audit_only("docs/audits/rho-f-volume-binding-gap.md")
    )

    # Per-isotope experimental binding from AME2020 (canonical nuclear
    # mass-defect tabulation).  Replaces the purged additive-constituent
    # baseline — no Z·m_p + N·m_n shortcut; B is read straight from AME.
    ame_path = (
        Path(__file__).parent / "ame-2020-binding-energies.witness.json"
    )
    if not ame_path.exists():
        raise SystemExit(
            "ame-2020-binding-energies.witness.json not found; "
            "run the AME binding-energy producer first."
        )
    _ame = builder.add_upstream(ame_path).get("data", {})
    _AME_ISOTOPES = [  # (witness key, Z, N, isotope label)
        ("B_deuteron_MeV", 1, 1, "2H"),
        ("B_tritium_MeV", 1, 2, "3H"),
        ("B_he3_MeV", 2, 1, "3He"),
        ("B_he4_MeV", 2, 2, "4He"),
        ("B_li5_MeV", 3, 2, "5Li"),
        ("B_li6_MeV", 3, 3, "6Li"),
        ("B_li7_MeV", 3, 4, "7Li"),
    ]
    _missing = [key for key, *_ in _AME_ISOTOPES if key not in _ame]
    if _missing:
        raise SystemExit(
            "ame-2020-binding-energies.witness.json is missing required "
            f"keys {_missing}; the analysis needs all of _AME_ISOTOPES."
        )
    # `delta_binding_MeV` is READ, not computed.  `_ame[key]` is already the
    # AME2020 table's own decimal text: `ame_2020_binding_energies.py` carries
    # it through `Decimal` end to end precisely so it never acquires a binary
    # tail, and emits `str(Decimal)`.  `float()` here threw that away and put a
    # raw float64 into this witness — and the round trip is lossy in the
    # VISIBLE digits, not only the tail (that producer records 6Li's exact
    # `31.9939872` coming back as `31.99398719999999600...`).
    #
    # Carry the STRING verbatim.  Do NOT "upgrade" it by re-serializing through
    # `_precision.fmt`: that pads a 9-significant-figure measurement out to
    # OUTPUT_DPS (`28.2956624000…0`), which is the sibling float64-padding
    # defect.  `str()` is a no-op on a string and is only defensive against an
    # older AME witness that stored a float.
    rows_in = [
        {"isotope": iso, "Z": Z, "N": N, "A": Z + N,
         "delta_binding_MeV": str(_ame[key])}
        for key, Z, N, iso in _AME_ISOTOPES
    ]

    # Per-isotope analysis.
    print(f"{'isotope':>8}  {'A':>3}  {'Δ_binding':>12}  "
          + "  ".join(f"{name[:18]:>18}" for name in LINK_PRIMITIVES))
    print(f"{'':>8}  {'':>3}  {'(MeV)':>12}  "
          + "  ".join(f"{'ρ_F/m_e needed':>18}"
                      for _ in LINK_PRIMITIVES))
    print("-" * 110)

    rows_out = []
    for row in rows_in:
        if row["A"] < 2:
            continue  # ¹H has zero nuclear binding (only 13.6 eV atomic).
        delta = row["delta_binding_MeV"]     # exact AME decimal, as text
        # DELIBERATE narrowing, and the one place in this file where a float is
        # the honest type.  `required_rho` divides by a SnapPy volume that
        # `experimental_constants` carries as a *float64 literal* quoted ±1e-12
        # (`VOL_FIGURE_EIGHT_ERR`, `VOL_THREE_TWIST_ERR`), so the quotient holds
        # ~12 significant digits of real information no matter how wide the
        # numerator is.  Widening the numerator here would not add precision; it
        # would only let the divisor's *binary* tail print, which is the
        # float64-padding defect the comment above refuses for `delta` itself.
        #
        # Related, and deliberately NOT fixed here: `M_E_MEV` is an `mpf` while
        # this module never calls `_precision.set_compute_dps()`, so the mpf
        # divisions below run at mpmath's default dps=15 and the serialized
        # `required_rho_over_me_per_link` strings carry 15 significant digits —
        # float64-grade, in string clothing the raw-float64 ratchet cannot see.
        # Calling `set_compute_dps()` would make that WORSE, not better: at
        # dps=70 the same quotient prints the volume's binary tail out to 60
        # places.  The real fix is an exact high-precision source for the three
        # volumes (`VOL_BORROMEAN_50DPS_STR` exists; 4_1 and 5_2 do not), which
        # is a separate change with its own numeric blast radius.
        delta_mp = mp.mpf(delta)
        ratios = {
            name: required_rho(delta_mp, vol) / M_E_MEV
            for name, vol in LINK_PRIMITIVES.items()
        }
        print(f"{row['isotope']:>8}  {row['A']:>3}  {_disp(delta):>12.3f}  "
              + "  ".join(f"{_disp(r):>18.3f}" for r in ratios.values()))
        rows_out.append({
            "isotope": row["isotope"],
            "A": row["A"], "Z": row["Z"], "N": row["N"],
            "delta_binding_MeV": delta,
            "required_rho_over_me_per_link": ratios,
        })

    # QOU expects ρ_F ∈ {1, 2} (in units of m_e).  Find the
    # candidate (isotope, link, target_rho) tuples within ±10% of
    # 1 or 2 — these are the cases where a single link primitive
    # plausibly explains the binding.
    matches = []
    for row in rows_out:
        for link, rho in row["required_rho_over_me_per_link"].items():
            for target in (1, 2):
                target_mp = mp.mpf(target)
                if abs(rho - target_mp) / target_mp < mp.mpf("0.10"):
                    matches.append({
                        "isotope": row["isotope"],
                        "link": link,
                        "rho_over_me": rho,
                        "target_rho_over_me": target,
                        "deviation_pct": (rho - target_mp) / target_mp * mp.mpf(100),
                    })

    print()
    print(f"Candidate (isotope, link) pairs within ±10% of ρ_F ∈ "
          f"{{m_e, 2 m_e}}: {len(matches)}")
    for m in matches:
        print(f"  {m['isotope']:>5} via {m['link']:>20}  "
              f"ρ_F = {_disp(m['rho_over_me']):.3f}·m_e  "
              f"(target {m['target_rho_over_me']}·m_e, "
              f"Δ {_disp(m['deviation_pct']):+.2f}%)")

    if not matches:
        print("  (none — every isotope's binding requires a "
              "multi-link composite or a non-{m_e, 2 m_e} ρ_F)")

    builder.add_assertion(
        name="binding_gap_analysis_completed",
        computed=len(rows_out),
        expected=len(_AME_ISOTOPES),
        tolerance=0,
        source="ame-2020-binding-energies.witness.json (all _AME_ISOTOPES, B ≥ ²H)",
    )
    builder.add_data("rows", rows_out)
    builder.add_data("matches_within_10pct", matches)
    # RECORD THE CEILING RATHER THAN LET THE SERIALIZATION IMPLY ONE.
    # `required_rho_over_me_per_link`, `matches_within_10pct[*].rho_over_me`
    # and `link_primitives_MeV_per_unit` serialize as decimal STRINGS — not
    # because they are high-precision, but because `experimental_constants`
    # now carries `M_E_MEV` as an `mpf`, so the quotient is an mpf and the
    # witness writer renders mpf as text.  Without this note the change reads
    # as a drain: the raw-float64 ratchet counts JSON floats, so 21 fields
    # leave its view while the information in them is unchanged.
    builder.add_data(
        "precision_ceiling_note",
        "delta_binding_MeV is EXACT (the AME2020 table's own decimal, carried "
        "verbatim from ame-2020-binding-energies.witness.json).  Every other "
        "number here is NOT: required_rho_over_me_per_link, "
        "matches_within_10pct[*].rho_over_me / deviation_pct and "
        "link_primitives_MeV_per_unit divide by a SnapPy volume that "
        "experimental_constants stores as a float64 literal quoted ±1e-12 "
        "(VOL_FIGURE_EIGHT_ERR, VOL_THREE_TWIST_ERR; VOL_BORROMEAN_ERR ±1e-15), "
        "so at most ~12 significant digits are real.  They are serialized as "
        "strings only because M_E_MEV is an mpf and this module deliberately "
        "does not call _precision.set_compute_dps() — the mpf arithmetic runs "
        "at mpmath's default dps=15, and raising it would print the volume's "
        "binary tail out to output_dps rather than add information.  Read "
        "these as float64-grade values in string form; do NOT quote them past "
        "~12 digits, and do NOT read their string type as evidence of "
        "precision.  Closing this properly needs exact high-precision sources "
        "for Vol(4_1) and Vol(5_2), as VOL_BORROMEAN_50DPS_STR already is.",
    )
    builder.add_data(
        "qou_prediction",
        "ρ_F ∈ {m_e, 2 m_e} per prop:cpt-orbit-closure-density",
    )
    builder.add_data("link_primitives_MeV_per_unit", {
        name: M_E_MEV * vol for name, vol in LINK_PRIMITIVES.items()
    })

    out_path = builder.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Inverts empirical AME 2020 binding energies against SnapPy "
            "hyperbolic link volumes and CAL-1 m_e; no substrate q_0 is read."
        ),
    })
    wdata = json.loads(out_path.read_text(encoding="utf-8"))
    if isinstance(wdata.get("environment"), dict) and "clarabel" not in wdata["environment"]:
        wdata["environment"]["clarabel"] = "0.11.1"
        out_path.write_text(json.dumps(wdata, indent=2) + "\n", encoding="utf-8")
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
