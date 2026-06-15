#!/usr/bin/env python3
"""Live SnapPy verification of the mass-pipeline hyperbolic-volume constants
+ a numerical record of the canonical-knot-id volume fork (thread 4).

Earlier sessions could not run SnapPy in-sandbox (vol-usage audit
2026-06-02 §"The Vol(β_K) data gap"); every census number in the corpus
was a literature / witness value. This sandbox has SnapPy 3.3.2, so this
script re-derives every consumed volume live and pins the discrepancies.

Three sections:

  S1  `substrate/knot_volumes.py` 50-dps constants vs live census
      volumes at SnapPy high precision (ManifoldHP, ~63 digits).

  S2  `per-atom-hyperbolic-volume.witness.json` (production atlas:
      p/n=𝓑₃, D=6_2, T=8_11, ³He=L6a4, ⁴He=4·8G) vs live census volumes
      of the NAMED knots.

  S3  `conj:canonical-knot-id-sdp` §"Historical evidence" table
      (mass-theory/conj-canonical-knot-id-sdp.md, volume-matching rows):
      the three claimed volumes (3.16396, 3.42721, 5.33349) vs the live
      census volumes of the knots they are attached to (6_2, 8_11,
      L6a4). All three rows disagree with their named knots while being
      internally consistent with a single 𝔈₀ ≈ 4.15 MeV — the signature
      of an earlier knot assignment surviving a later reassignment.
      The orphan numbers are census-identified by volume scan
      (3.16396 = Vol(6_1) leaked as far as MostowRigidity.lean:264).

DIAGNOSTIC ONLY — no production path is changed, no content block is
edited. Resolving the fork (which side of the assignment is canonical)
is owner-gated thread-4 / `conj:canonical-knot-id-sdp` scope per
docs/audits/2026-06-06-thread2-deuteron-perknot-gating.md.

Ref: docs/audits/2026-06-06-thread2-deuteron-perknot-gating.md
Ref: docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md
Ref: docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md
Ref: content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md
"""
from __future__ import annotations

# Path bridge (audits cluster — subdirectory refactor Phase 2).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from knot_volumes import (  # noqa: E402
    VOL_4_1_MPF,
    VOL_BORROMEAN_MPF,
    VOL_5_2_MPF,
    VOL_6_2_MPF,
    VOL_8_11_MPF,
    VOL_7_SQ_1_MPF,
)
from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent

# S1 — substrate constants → (census name, tolerance). All constants
# are Clausen-form or SnapPy-HP derived and verify to ≤ 1e-20.
# (VOL_5_2 was the one literature-sourced constant — ~12 effective dps,
# AHW-1991 digits 13–15 transcribed wrong — until the 2026-06-12
# in-sandbox ManifoldHP upgrade landed in this same PR.)
S1_ROWS = [
    ("VOL_4_1", VOL_4_1_MPF, "4_1", "1e-12"),
    ("VOL_BORROMEAN", VOL_BORROMEAN_MPF, "L6a4", "1e-12"),
    ("VOL_5_2", VOL_5_2_MPF, "5_2", "1e-12"),
    ("VOL_6_2", VOL_6_2_MPF, "6_2", "1e-12"),
    ("VOL_8_11", VOL_8_11_MPF, "8_11", "1e-12"),
    ("VOL_7_SQ_1", VOL_7_SQ_1_MPF, "7^2_1", "1e-12"),
]

# S2 — production per-atom witness → census names ("formula" handled inline).
S2_ROWS = [
    ("Vol_p", "L6a4"),
    ("Vol_n", "L6a4"),
    ("Vol_D", "6_2"),
    ("Vol_T", "8_11"),
    ("Vol_3He", "L6a4"),
]

# S3 — conj:canonical-knot-id-sdp §"Historical evidence" volume-matching
# table rows exactly as printed in the .md (named knot, claimed volume).
S3_ROWS = [
    ("2H", "6_2", "3.16396"),
    ("3H", "8_11", "3.42721"),
    ("3He", "L6a4", "5.33349"),
]
S3_SOURCE = (
    "content/quantum-observable-universe/mass-theory/"
    "conj-canonical-knot-id-sdp.md §Historical evidence (volume matching)"
)

ORPHAN_MATCH_TOL = 5e-4  # census-identification window for orphan volumes
SCAN_PROGRESS_EVERY = 2000


def hp_volume(name: str):
    """Census volume at SnapPy high precision (~63 digits) as mpf.

    Returns (vol_mpf, solution_type_str)."""
    import snappy

    m = snappy.ManifoldHP(name)
    return mp.mpf(str(m.volume())), m.solution_type()


def identify_orphans(orphans: list[mp.mpf]) -> dict[str, list[str]]:
    """Scan SnapPy censuses for manifolds whose volume matches each orphan.

    OrientableCuspedCensus is volume-ordered → early stop past the max
    orphan. LinkExteriors (Rolfsen) is name-ordered → full pass.
    """
    import snappy

    if not orphans:
        return {}
    # Pair each float target with its dict key explicitly — zip-ing a
    # parallel list against dict keys silently misaligns when orphans
    # contain duplicate values (dict keys dedupe). Gemini review #2192.
    targets = [(float(v), str(v)) for v in orphans]
    hi = max(t for t, _ in targets) + 10 * ORPHAN_MATCH_TOL
    out: dict[str, list[str]] = {key: [] for _, key in targets}
    t0 = time.monotonic()

    n = 0
    for m in snappy.OrientableCuspedCensus:
        n += 1
        v = float(m.volume())
        if v > hi:
            break
        for t, key in targets:
            if abs(v - t) < ORPHAN_MATCH_TOL:
                ids = m.identify()
                tail = f" = {ids[0]}" if ids else ""
                out[key].append(f"{m.name()}({v:.6f}){tail}")
        if n % SCAN_PROGRESS_EVERY == 0:
            print(f"  [scan] cusped census {n} entries, vol={v:.4f}, "
                  f"elapsed {time.monotonic() - t0:.0f}s", flush=True)
    print(f"  [scan] cusped census done after {n} entries "
          f"({time.monotonic() - t0:.0f}s)", flush=True)

    n = 0
    for m in snappy.LinkExteriors:
        n += 1
        try:
            v = float(m.volume())
        except Exception:  # noqa: BLE001 — non-hyperbolic entries
            continue
        for t, key in targets:
            if abs(v - t) < ORPHAN_MATCH_TOL:
                out[key].append(f"{m.name()}({v:.6f})")
        if n % SCAN_PROGRESS_EVERY == 0:
            print(f"  [scan] LinkExteriors {n} entries, "
                  f"elapsed {time.monotonic() - t0:.0f}s", flush=True)
    print(f"  [scan] LinkExteriors done after {n} entries "
          f"({time.monotonic() - t0:.0f}s)", flush=True)
    return out


def main() -> int:
    set_compute_dps()
    w = WitnessBuilder("snappy-census-volume-verification", engine="snappea")
    w.set_description(
        "Live SnapPy (ManifoldHP) verification of every hyperbolic-volume "
        "constant the mass pipeline consumes: substrate/knot_volumes.py "
        "constants (S1), the per-atom-hyperbolic-volume production atlas "
        "(S2), and the conj:canonical-knot-id-sdp historical "
        "volume-matching table (S3 — documents the thread-4 fork: all "
        "three claimed volumes belong to OTHER census manifolds than the "
        "knots they name; orphan numbers census-identified by volume "
        "scan). Diagnostic only; fork resolution is owner-gated."
    )

    print("S1 — substrate/knot_volumes.py vs live census (ManifoldHP)")
    for const_name, const_val, census_name, tol_str in S1_ROWS:
        vol, sol = hp_volume(census_name)
        diff = abs(vol - const_val)
        print(f"  {const_name:16s} {census_name:6s} census={mp.nstr(vol, 20)} "
              f"|diff|={mp.nstr(diff, 3)}  [{sol}]")
        w.add_data(f"s1_{const_name}_census", mp.nstr(vol, 50))
        w.add_data(f"s1_{const_name}_absdiff", mp.nstr(diff, 5))
        w.add_data(f"s1_{const_name}_solution_type", str(sol))
        w.add_assertion(
            name=f"s1_{const_name}_matches_census",
            computed=bool(diff < mp.mpf(tol_str)),
            expected=True,
            tolerance=float(tol_str),
            source=f"substrate/knot_volumes.py {const_name} vs "
                   f"ManifoldHP('{census_name}')"
                   + (" — upgraded to SnapPy HP 50 dps 2026-06-12 "
                      "(former AHW-1991 literature anchor had a "
                      "digit-13-15 transcription error)"
                      if const_name == "VOL_5_2" else ""),
        )

    print("S2 — per-atom-hyperbolic-volume.witness.json vs named census")
    atlas = json.loads(
        (COMPUTATIONS / "per-atom-hyperbolic-volume.witness.json").read_text()
    )["data"]
    for key, census_name in S2_ROWS:
        claimed = mp.mpf(atlas[key])
        vol, _sol = hp_volume(census_name)
        diff = abs(vol - claimed)
        print(f"  {key:8s} {census_name:6s} witness={mp.nstr(claimed, 17)} "
              f"|diff|={mp.nstr(diff, 3)}")
        w.add_data(f"s2_{key}_census", mp.nstr(vol, 50))
        w.add_data(f"s2_{key}_absdiff", mp.nstr(diff, 5))
        w.add_assertion(
            name=f"s2_{key}_matches_named_census",
            computed=bool(diff < mp.mpf("1e-12")),
            expected=True,
            tolerance=1e-12,
            source=f"per-atom-hyperbolic-volume.witness.json {key} "
                   f"({atlas['knot_' + key.split('_', 1)[1]]}) vs "
                   f"ManifoldHP('{census_name}')",
        )
    # 4He is a formula entry (4·8G), not a census manifold.
    he4_claimed = mp.mpf(atlas["Vol_4He"])
    he4_formula = 4 * 8 * mp.catalan
    he4_diff = abs(he4_formula - he4_claimed)
    w.add_data("s2_Vol_4He_formula_4x8G", mp.nstr(he4_formula, 50))
    w.add_data("s2_Vol_4He_absdiff", mp.nstr(he4_diff, 5))
    w.add_assertion(
        name="s2_Vol_4He_matches_4x8G_formula",
        computed=bool(he4_diff < mp.mpf("1e-12")),
        expected=True,
        tolerance=1e-12,
        source="per-atom witness Vol_4He vs 4·8·Catalan (magic-A formula)",
    )

    print("S3 — conj:canonical-knot-id-sdp historical table (the fork)")
    orphan_vals = []
    for nucleus, census_name, claimed_str in S3_ROWS:
        claimed = mp.mpf(claimed_str)
        orphan_vals.append(claimed)
        vol, _sol = hp_volume(census_name)
        mismatch = abs(vol - claimed)
        print(f"  {nucleus:4s} named {census_name:6s}: table={claimed_str}  "
              f"census({census_name})={mp.nstr(vol, 12)}  "
              f"|mismatch|={mp.nstr(mismatch, 4)}")
        w.add_data(f"s3_{nucleus}_table_value", claimed_str)
        w.add_data(f"s3_{nucleus}_named_knot", census_name)
        w.add_data(f"s3_{nucleus}_census_of_named", mp.nstr(vol, 50))
        w.add_data(f"s3_{nucleus}_mismatch", mp.nstr(mismatch, 5))
        w.add_assertion(
            name=f"s3_fork_{nucleus}_mismatch_documented",
            computed=bool(mismatch > mp.mpf("0.1")),
            expected=True,
            tolerance=0.1,
            source=f"{S3_SOURCE} — documents that the table value is NOT "
                   f"Vol({census_name}); resolution is thread-4 owner scope",
        )

    # The 6_1 identification of the deuteron-row orphan is established
    # (thread-2 gating doc + MostowRigidity.lean:264) — assert it live.
    vol_6_1, _ = hp_volume("6_1")
    d_orphan_diff = abs(vol_6_1 - mp.mpf("3.16396"))
    w.add_data("s3_Vol_6_1_census", mp.nstr(vol_6_1, 50))
    w.add_assertion(
        name="s3_orphan_3p16396_is_Vol_6_1",
        computed=bool(d_orphan_diff < mp.mpf("5e-4")),
        expected=True,
        tolerance=5e-4,
        source="orphan 3.16396 (conj table ²H row + MostowRigidity.lean:264)"
               " equals census Vol(6_1)",
    )

    print("S3b — census-identifying the orphan volumes (scan)")
    matches = identify_orphans(orphan_vals)
    for key, hits in matches.items():
        short = "; ".join(hits) if hits else "none within ±5e-4"
        print(f"  orphan {key}: {short}")
        w.add_data(f"s3b_orphan_{key.replace('.', 'p')}_census_matches", short)

    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
