#!/usr/bin/env python3
"""
Cell structure of the canonical decomposition, and the Pachner-distance candidate.

Bean `qou-eptr`, issue #6941. The proposal behind that issue offers, as the
carrier of the binding gap's irreducibly many-body piece, a quantity built from
the canonical (Epstein-Penner) ideal decomposition — with the natural candidate
observable being the Pachner distance between the decomposition the framework
DERIVES from the braid word and the canonical one.

This probe evaluates that candidate on the only knot where the corpus can
currently produce both, and checks the cell type of the canonical decomposition
on the two manifolds the live nuclide dictionary actually uses.

TWO RESULTS, both negative for the candidate as posed.

1. The candidate observable VANISHES where it can be computed. The
   Floyd-Hatcher layered triangulation of `S^3 \\ 4_1`, derived from the braid
   word `(s1 s2^-1)^2` with no SnapPy input (`nz_gluing_from_braid_monodromy_probe`,
   2026-09-06), has two tetrahedra with both shapes at the sixth root of unity —
   which is the regular ideal tetrahedron. The canonical decomposition of the
   figure-eight is also two regular ideal tetrahedra. They coincide, so the
   Pachner distance is 0 and the observable carries no information on the one
   case the framework can derive.

2. The canonical decomposition of the framework's PRINCIPAL manifold is not a
   triangulation at all. 13 of the 19 atoms in the live dictionary are assigned
   the Borromean complement `L6a4`, whose canonical decomposition is two regular
   ideal OCTAHEDRA. This probe checks the consistency of that classical fact
   against the corpus's own volume registry, and checks that the volume is NOT
   an integer multiple of the regular ideal tetrahedron's, so the decomposition
   cannot be re-read as a tetrahedral one. The dialog's framing — a groupoid
   whose objects are ideal TRIANGULATIONS, with the canonical decomposition as a
   distinguished object of it — therefore does not even contain the object it
   distinguishes, on the manifold that matters most here.

SCOPE, stated so neither result is over-read. A volume identity is CONSISTENT
with a cell structure, it does not prove one; the octahedral decomposition of
the Borromean complement and the two-tetrahedron decomposition of the
figure-eight are classical results, cited below, and what this probe contributes
is the arithmetic check that the corpus's own registry agrees with them and the
non-integrality that rules out a tetrahedral re-reading. Result 1 is a statement
about `4_1` only; it says the candidate is uninformative there, not that a
Pachner distance is uninformative on some manifold where the two decompositions
differ. No such manifold is currently derivable in this corpus, which is itself
the point.

Precision: all volumes are mpmath at the corpus compute precision, from the
canonical registry and from closed forms (`Cl_2(pi/3)`, Catalan). Ratios are
exact quotients of mpf. No float64, no fit, no `q`, no anchor.

-- Ref: [thurston1979] http://library.msri.org/books/gt3m/
--      (the two-tetrahedron decomposition of the figure-eight complement, and
--       the two-octahedron decomposition of the Borromean rings complement)
-- Ref: [epstein1988] https://doi.org/10.4310/jdg/1214441650
-- Ref: [manuscript] docs/audits/2026-09-06-nz-gluing-data-from-braid-monodromy.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

import knot_volumes as kv  # noqa: E402
import sw_hyperbolicity_gate as gate  # noqa: E402
from _precision import COMPUTE_DPS  # noqa: E402


def derived_layered_fig8() -> tuple[int, mp.mpf]:
    """(tetrahedron count, volume) of the LAYERED triangulation of S^3 \\ 4_1,
    read from the witness of the braid-word derivation — not from SnapPy and not
    from memory. The tetrahedron count is the number of edge rows, one per
    letter of the LR word."""
    w = _HERE / "nz-gluing-from-braid-monodromy.witness.json"
    if not w.exists():
        raise FileNotFoundError(f"missing derived NZ witness: {w}")
    d = json.loads(w.read_text())["data"]
    n_tet = len(d["edge_rows_rect"])
    vol = mp.mpf(str(d["volume_50dps"]))
    return n_tet, vol


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 8))

    # Closed forms for the two regular ideal cells.
    v_tet = mp.clsin(2, mp.pi / 3)          # Cl_2(pi/3) = 3*Lambda(pi/3)
    v_oct = 4 * kv.CATALAN_G_MPF            # 4*Catalan = 8*Lambda(pi/4)

    vol_fig8 = gate.vol_component("4_1")
    vol_borro = gate.vol_component("L6a4")

    n_tet_layered, vol_layered = derived_layered_fig8()

    # The derived volume is SERIALIZED at 45 significant digits by its producer
    # (`mp.nstr(vol, 45)`), so a comparison against the registry's full-precision
    # value cannot be held to the corpus compute tolerance of 1e-62: the two
    # agree to every digit the witness actually records, and the residual
    # 4.94e-45 IS that truncation. The tolerance below is set to the recorded
    # precision with five digits of margin, and it is a statement about the
    # serialization, not a widened baseline -- widening a baseline to turn a red
    # gate green is forbidden (AGENTS.md), and this is the different case where
    # the input's own precision, not the quantity, bounds the comparison.
    tol_recorded = mp.mpf(10) ** (-40)

    # Canonical cell counts implied by the registry volumes.
    fig8_over_tet = vol_fig8 / v_tet
    borro_over_oct = vol_borro / v_oct
    borro_over_tet = vol_borro / v_tet
    oct_over_tet = v_oct / v_tet

    def dist_to_int(x: mp.mpf) -> mp.mpf:
        return abs(x - mp.nint(x))

    # The candidate observable, evaluated where both decompositions exist.
    n_tet_canonical_fig8 = int(mp.nint(fig8_over_tet))
    pachner_candidate = abs(n_tet_canonical_fig8 - n_tet_layered)

    checks = [
        ("fig8_canonical_is_two_regular_ideal_tetrahedra",
         dist_to_int(fig8_over_tet) < tol and n_tet_canonical_fig8 == 2,
         "Vol(4_1)/Vol(regular ideal tetrahedron) = 2 exactly"),
        ("borromean_canonical_is_two_regular_ideal_octahedra",
         dist_to_int(borro_over_oct) < tol and int(mp.nint(borro_over_oct)) == 2,
         "Vol(L6a4)/Vol(regular ideal octahedron) = 2 exactly"),
        ("borromean_canonical_is_not_a_tetrahedral_decomposition",
         dist_to_int(borro_over_tet) > mp.mpf("0.01"),
         "Vol(L6a4)/Vol(tetrahedron) is not an integer, so the canonical "
         "decomposition of the corpus's principal manifold is not a "
         "triangulation into regular ideal tetrahedra"),
        ("octahedron_is_not_an_integer_multiple_of_tetrahedron",
         dist_to_int(oct_over_tet) > mp.mpf("0.01"),
         "an ideal octahedron is not an integer number of regular ideal "
         "tetrahedra, reinforcing the previous check"),
        ("derived_layered_fig8_has_two_tetrahedra",
         n_tet_layered == 2,
         "the braid-word-derived layered triangulation of S^3\\4_1 has two "
         "tetrahedra (one per letter of the LR word RL)"),
        ("derived_layered_volume_matches_canonical",
         abs(vol_layered - vol_fig8) < tol_recorded,
         "the derived layered triangulation carries the full hyperbolic volume "
         "to the 45 significant digits its producer serializes (residual "
         "4.94e-45 = that truncation), so it is a decomposition of the same "
         "complete structure"),
        ("pachner_distance_candidate_vanishes_on_fig8",
         pachner_candidate == 0,
         "layered and canonical cell counts agree, so the candidate observable "
         "is 0 on the one knot the framework can derive both for"),
    ]

    print(f"Vol(regular ideal tetrahedron) = Cl_2(pi/3) = {mp.nstr(v_tet, 20)}")
    print(f"Vol(regular ideal octahedron)  = 4*Catalan  = {mp.nstr(v_oct, 20)}")
    print()
    print(f"Vol(4_1)   registry            = {mp.nstr(vol_fig8, 20)}")
    print(f"Vol(4_1)   derived (braid word)= {mp.nstr(vol_layered, 20)}")
    print(f"Vol(L6a4)  registry            = {mp.nstr(vol_borro, 20)}")
    print()
    print(f"Vol(4_1)  / V_tet = {mp.nstr(fig8_over_tet, 16)}")
    print(f"Vol(L6a4) / V_oct = {mp.nstr(borro_over_oct, 16)}")
    print(f"Vol(L6a4) / V_tet = {mp.nstr(borro_over_tet, 16)}   <- not an integer")
    print(f"V_oct     / V_tet = {mp.nstr(oct_over_tet, 16)}   <- not an integer")
    print()
    print(f"layered tetrahedra (derived)   = {n_tet_layered}")
    print(f"canonical tetrahedra (4_1)     = {n_tet_canonical_fig8}")
    print(f"PACHNER DISTANCE CANDIDATE     = {pachner_candidate}")
    print()

    ok = 0
    for name, cond, desc in checks:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}: {desc}")
        ok += 1 if cond else 0
    print(f"\n{ok}/{len(checks)} assertions")

    try:
        from qou_substrate.witness import WitnessBuilder
    except Exception as e:  # noqa: BLE001
        print(f"(witness not emitted: {e!r})")
        return 0 if ok == len(checks) else 1

    wb = WitnessBuilder("canonical-cell-structure", engine="mpmath",
                        _script_path=__file__)
    for name, cond, desc in checks:
        wb.add_assertion(name, computed="1" if cond else "0", expected="1",
                         tolerance="0.5", source=desc)
    wb.add_data("vol_regular_ideal_tetrahedron", mp.nstr(v_tet, 30))
    wb.add_data("vol_regular_ideal_octahedron", mp.nstr(v_oct, 30))
    wb.add_data("vol_fig8_registry", mp.nstr(vol_fig8, 30))
    wb.add_data("vol_fig8_derived_from_braid_word", mp.nstr(vol_layered, 30))
    wb.add_data("vol_borromean_registry", mp.nstr(vol_borro, 30))
    wb.add_data("ratio_fig8_over_tetrahedron", mp.nstr(fig8_over_tet, 20))
    wb.add_data("ratio_borromean_over_octahedron", mp.nstr(borro_over_oct, 20))
    wb.add_data("ratio_borromean_over_tetrahedron", mp.nstr(borro_over_tet, 20))
    wb.add_data("n_tetrahedra_layered_derived", n_tet_layered)
    wb.add_data("n_tetrahedra_canonical_fig8", n_tet_canonical_fig8)
    wb.add_data("pachner_distance_candidate_fig8", pachner_candidate)
    wb.add_data("derived_vs_registry_volume_residual",
                mp.nstr(abs(vol_layered - vol_fig8), 6))
    wb.add_data("derived_volume_recorded_significant_digits", 45)
    wb.add_data("scope",
                "A volume identity is consistent with a cell structure, it does "
                "not prove one; the octahedral and two-tetrahedron "
                "decompositions are classical and are cited. What is measured "
                "here is that the corpus registry agrees with them, that the "
                "Borromean volume admits no tetrahedral re-reading, and that "
                "the Pachner-distance candidate is 0 on 4_1. It is NOT a claim "
                "that a Pachner distance is uninformative on a manifold where "
                "the two decompositions differ; no such manifold is currently "
                "derivable in this corpus.")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "pure geometry: no q, no Markov parameter, no anchor"})
    print("witness written")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
