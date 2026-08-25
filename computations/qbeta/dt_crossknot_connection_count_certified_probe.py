#!/usr/bin/env python3
"""dt_crossknot_connection_count_certified_probe.py — D3 follow-up: the
#boundary-parabolic-connections count, certified locally (qou-btvl / qou-52sn).

The driver-14 constructibility audit's R1 reading (DT integer =
#boundary-parabolic connections = full A-polynomial L-degree; 4₁: 3, 5₂: 4)
rested on LITERATURE-RECALLED counts — the ptolemy database at
ptolemy.unhyperbolic.org is firewalled in this sandbox (403 through the
proxy). Egress workaround (owner hint 2026-08-15, "github.com clone"):
SnapPy's own source tree — and, it turns out, the INSTALLED WHEEL — ships
certified Magma primary-decomposition outputs for exactly these ptolemy
varieties in `snappy/ptolemy/testing_files/` (`4_1__sl2_c{0,1}`,
`5_2__sl2_c{0,1}`). This probe processes them with snappy's own parser
(`processMagmaFile.solutions_from_magma`) and counts:

  [1] 4₁: obstruction class c0 → 0 solutions; c1 → ONE Galois orbit of
      degree 2 (the ℚ(√−3) geometric/conjugate pair) ⇒ 2 irreducible
      boundary-parabolic PSL(2,ℂ) points.
  [2] 5₂: c0 → 0; c1 → ONE Galois orbit of degree 3 (the cubic trace
      field) ⇒ 3 irreducible points.
  [3] Adding the one abelian boundary-parabolic connection each (the
      (L−1) factor of the full A-polynomial — reducible reps are excluded
      from the ptolemy variety by nondegeneracy; this convention is the
      audit's, not new derivation) gives TOTALS 3 and 4 — exactly the R1
      counts and the full L-degrees `a41FullLDegree = 3` (Lean-pinned) and
      4. The literature recall is now a local computation.

Provenance: the .magma_out files are Magma outputs distributed with SnapPy
(GPL) as regression fixtures; they are read from the installed package at
runtime and NOT copied into this repository. The trace-field degrees (2, 3)
double as an internal consistency check against the known 4₁/5₂ trace
fields. 6₁ has no bundled data — the third-knot test for
dtMax = recursionOrder + 1 remains open (needs the ptolemy DB or magma).

Scope-(a); nothing wired; no fit. Beans qou-btvl / qou-52sn / qou-rtec.
"""
from __future__ import annotations

import bz2
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

EXPECT = {
    "4_1": {"c1_degrees": [2], "irreducible": 2, "abelian": 1, "total": 3},
    "5_2": {"c1_degrees": [3], "irreducible": 3, "abelian": 1, "total": 4},
}


def field_degree(nf) -> int:
    if nf is None:
        return 1
    try:
        return int(nf.poldegree())
    except Exception:
        return int(nf.degree())


def main() -> int:
    import snappy.ptolemy as ptolemy_mod
    from snappy.ptolemy import processMagmaFile

    data_dir = Path(ptolemy_mod.__file__).parent / "testing_files"

    print("=" * 78)
    print(" D3 follow-up — #boundary-parabolic connections, locally certified")
    print("=" * 78)
    print(f"  data: {data_dir} (shipped in the snappy wheel)")

    wb = WitnessBuilder("dt-crossknot-connection-count-certified",
                       engine="snappy-ptolemy-magma-fixtures")
    wb.set_description(
        "R1 #boundary-parabolic-connections counts for 4_1 and 5_2, "
        "computed locally from the certified Magma primary-decomposition "
        "outputs shipped in the snappy wheel (ptolemy testing_files; the "
        "ptolemy.unhyperbolic.org DB is firewalled - egress workaround "
        "per owner hint: the data rides the package itself). 4_1: one "
        "degree-2 Galois orbit (Q(sqrt(-3)) pair) -> 2 irreducible; 5_2: "
        "one degree-3 orbit (cubic trace field) -> 3 irreducible; plus "
        "one abelian connection each (the (L-1) factor, audit convention) "
        "-> totals 3 and 4 = the R1 counts / full L-degrees, previously "
        "literature-recalled. 6_1 not bundled; third-knot test stays "
        "open. Scope-(a); nothing wired. Beans qou-btvl/qou-52sn."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    results = {}
    all_ok = True
    for knot, exp in EXPECT.items():
        per_class = {}
        irreducible = 0
        for cls in ("c0", "c1"):
            p = data_dir / f"{knot}__sl2_{cls}.magma_out.bz2"
            sols = processMagmaFile.solutions_from_magma(
                bz2.open(p, "rt").read(), numerical=False)
            degs, polys = [], []
            for s in sols.flatten():
                nf = s.number_field()
                degs.append(field_degree(nf))
                polys.append(str(nf) if nf is not None else "rational")
            per_class[cls] = {"galois_orbits": len(degs), "degrees": degs,
                              "number_fields": polys, "points": sum(degs)}
            irreducible += sum(degs)
            print(f"\n  {knot} {cls}: orbits {len(degs)}, degrees {degs}"
                  + (f", fields {polys}" if polys else ""))
        total = irreducible + exp["abelian"]
        ok = (per_class["c1"]["degrees"] == exp["c1_degrees"]
              and irreducible == exp["irreducible"] and total == exp["total"])
        all_ok = all_ok and ok
        results[knot] = {**per_class,
                         "irreducible_points": irreducible,
                         "abelian_connections": exp["abelian"],
                         "total_connections": total,
                         "matches_r1": ok}
        print(f"  {knot}: irreducible {irreducible} + abelian "
              f"{exp['abelian']} = TOTAL {total}  (R1 expects "
              f"{exp['total']}: {'MATCH' if ok else 'MISMATCH'})")

    wb.add_data("knots", results)
    wb.add_data("provenance", {
        "source": "snappy wheel ptolemy/testing_files (Magma regression "
                  "fixtures, GPL; read at runtime, not vendored)",
        "abelian_convention": "the (L-1) factor of the full A-polynomial; "
                              "reducible reps excluded from the ptolemy "
                              "variety by nondegeneracy (audit convention)",
        "six_one": "no bundled data; dtMax=recursionOrder+1 third-knot "
                   "test remains open",
    })
    wb.add_assertion("fourone_connection_count",
                     computed=str(results["4_1"]["total_connections"]),
                     expected="3", tolerance="exact",
                     source="certified magma fixtures vs R1 / a41FullLDegree")
    wb.add_assertion("fivetwo_connection_count",
                     computed=str(results["5_2"]["total_connections"]),
                     expected="4", tolerance="exact",
                     source="certified magma fixtures vs R1 (was literature "
                            "recall)")
    wb.add_assertion("trace_field_degrees",
                     computed=str([results["4_1"]["c1"]["degrees"],
                                   results["5_2"]["c1"]["degrees"]]),
                     expected="[[2], [3]]", tolerance="exact",
                     source="Galois-orbit degrees vs known 4_1/5_2 trace "
                            "fields (internal consistency)")
    wb.save()

    print(f"\n  RESULT: {'CERTIFIED — R1 counts now locally computed' if all_ok else 'MISMATCH'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
