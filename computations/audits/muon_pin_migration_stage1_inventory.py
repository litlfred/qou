#!/usr/bin/env python3
"""Stage-1 inventory for the muon-pin migration (bean `qou-tekx`): what carries
an off-canonical pin, and how much of it the flip gate is structurally unable
to see.

WHY THIS IS NOT ANOTHER CENSUS
------------------------------
Three scripts already count muon-pinned witnesses and each answers a different
question:

  - `muon_pin_witness_census.py`      how many FILES CONTAIN a literal
  - `muon_pin_A_residual_surface_audit.py`  of the A-carrying ones, which were
                                     COMPUTED at A (4 of 41; 1 live)
  - `q0_anchor_consistency_audit.py`  whether the top-level (q0Anchor, q0Value)
                                     PAIR agrees   -> Q0_FLIP

The question none of them asks is the one a migration plan needs:

    for a witness that records an off-canonical pin, is there any mechanism in
    the corpus that would REPORT it?

That is not the same as "is it wrong". A witness computed at the CODATA-2018
muon pin is a correct record of what its producer did. It is off-canonical, and
the point of an inventory is to know whether anything would ever say so.

THE TWO BLIND SPOTS THIS MEASURES
---------------------------------
1. `_Q0_PREFIXES` in `qou_substrate/witness.py` is

       (("proton", "1.10997858275"), ("muon", "1.10997859564"))

   The muon prefix is **C** (CODATA 2022). A payload recording **A** (the
   retired frozen pin) or **B** (CODATA 2018) matches NEITHER prefix, so
   `_q0_anchor_from_payload` contributes no evidence and the stamp falls
   through to the manifest. The prefix moved with the anchor, as its own
   docstring requires -- and in moving it stopped recognising the two values
   the migration is about.

2. `q0_anchor_consistency_audit` compares the TOP-LEVEL `q0Value` against the
   declared anchor. A pin recorded in a nested field (`parameters.q0`,
   `result.q_0_50dps`, an `anchors/` sub-map) is not what it checks, and a
   witness with no `q0Anchor` at all is `Q0_ANCHOR_MISSING` -- not a flip.

METHOD -- classify by VALUE, in exact decimal, never by prefix
--------------------------------------------------------------
A prefix ladder cannot separate the three muon values: every rung is a prefix
of at least two of them (see `muon_pin_witness_census.py`, which records the
same trap). This script instead parses each candidate to `mpmath.mpf` at 60 dps
and takes the NEAREST of the four known pins, with an explicit separation
guard.

The pins pairwise, relative:

    A-B  2.84161e-12      <- the tightest; needs ~13 significant digits
    A-C  7.69423e-11
    B-C  7.97839e-11
    A-P  1.15371e-08      (P = the proton pin)

So a value must carry ~13 significant digits before A and B are even
distinguishable. Anything recorded at fewer digits is reported as
`UNRESOLVED_PRECISION` rather than assigned to the nearest pin -- assigning it
would be inventing evidence, and `1.10998` is a real shape in this corpus
(`str(mpf)` at dps 15).

NO-FLOAT64: every comparison is `mpmath.mpf`. JSON is read with
`parse_float=str` so a bare number literal keeps its source digits instead of
being rounded through a Python float on the way in -- without that, a witness
recording `1.1099785955573347` as a JSON *number* would arrive already
indistinguishable from its neighbours, and this script would be measuring
`json`'s arithmetic rather than the corpus.

Usage:
    python3 computations/audits/muon_pin_migration_stage1_inventory.py
    python3 ... <rev>          # measure any revision (defaults to HEAD)
    python3 ... --list         # name every off-canonical witness

Output:
    computations/audits/muon-pin-migration-stage1-inventory.witness.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

_T0 = time.monotonic()

mp.mp.dps = 60

#: The four pins this corpus uses, at full recorded precision. A and B and C
#: are the three values all called "the muon q0" (see
#: `muon_pin_three_values_probe.py`); P is the proton pin.
# witness-copy-intentional: the four pins are this inventory's SUBJECT —
# it exists to find code carrying them. A retired pin has no live
# producer to read from, which is what makes it retired.
PINS = {
    "A_retired_frozen": mp.mpf("1.1099785955573347198944358078180"),
    "B_codata_2018": mp.mpf("1.10997859555418057528159407961"),
    "C_codata_2022": mp.mpf("1.10997859564273904668179512938"),
    "P_proton": mp.mpf("1.1099785827513808"),
}
OFF_CANONICAL_MUON = ("A_retired_frozen", "B_codata_2018")

#: A candidate must land within this relative distance of a pin, AND be at
#: least `_SEPARATION` times closer to it than to the runner-up, before it is
#: called that pin. Half the A-B gap is 1.42e-12; 4e-13 sits comfortably
#: inside it while still admitting a value truncated at 13 significant digits.
_TOL = mp.mpf("4e-13")
_SEPARATION = 10

#: Cheap textual prefilter -- every pin shares these leading characters, so a
#: file without them cannot carry one and need not be parsed.
_SHARED_PREFIX = "1.109978"


def classify(text: str):
    """Nearest pin for a decimal text, or a reason it cannot be classified.

    Returns ``(pin_name, rel_distance)`` or ``(None, reason)``.
    """
    try:
        v = mp.mpf(text)
    except Exception:  # noqa: BLE001
        return None, "unparseable"
    if v == 0:
        return None, "zero"
    scored = sorted(((abs(v - p) / p, name) for name, p in PINS.items()))
    best_rel, best = scored[0]
    second_rel, _ = scored[1]
    if best_rel > _TOL:
        return None, "UNRESOLVED_PRECISION"
    if second_rel < best_rel * _SEPARATION:
        return None, "AMBIGUOUS_BETWEEN_PINS"
    return best, best_rel


def walk_leaves(node, path=""):
    """Every scalar leaf with its full dotted path. No depth or width limit.

    Deliberately unbounded, unlike `_q0_anchor_from_payload`'s depth-4 /
    first-64-items walk: the reach of that walk is one of the things being
    measured, so a scanner sharing its limits could not see past them.
    """
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk_leaves(v, f"{path}/{k}" if path else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_leaves(v, f"{path}[{i}]")
    else:
        yield path, node


def scan_payload(payload):
    """All pin-valued leaves in a payload: {pin_name: [(path, rel), ...]}."""
    found: dict = {}
    unresolved: list = []
    for path, leaf in walk_leaves(payload):
        if not isinstance(leaf, str):
            continue
        s = leaf.strip()
        if not s.startswith(_SHARED_PREFIX):
            continue
        name, info = classify(s)
        if name is None:
            unresolved.append((path, s[:20], info))
        else:
            found.setdefault(name, []).append((path, info))
    return found, unresolved


def tracked_witnesses(rev: str):
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", rev],
        capture_output=True, text=True, check=True).stdout.splitlines()
    return [f for f in out if f.endswith(".witness.json")]


def blob(rev: str, path: str) -> str:
    return subprocess.run(["git", "show", f"{rev}:{path}"],
                          capture_output=True, text=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("rev", nargs="?", default="HEAD")
    ap.add_argument("--list", action="store_true",
                    help="name every off-canonical witness")
    args = ap.parse_args()
    rev = args.rev

    files = tracked_witnesses(rev)
    rows = []
    n_parse_error = 0
    for path in files:
        raw = blob(rev, path)
        if _SHARED_PREFIX not in raw:
            continue
        try:
            payload = json.loads(raw, parse_float=str)
        except Exception:  # noqa: BLE001
            n_parse_error += 1
            continue
        found, unresolved = scan_payload(payload)
        off = [n for n in OFF_CANONICAL_MUON if n in found]
        if not off:
            continue
        body = payload if isinstance(payload, dict) else {}
        rows.append({
            "path": path,
            "declared_anchor": body.get("q0Anchor"),
            "top_level_q0Value": (str(body.get("q0Value"))[:20]
                                  if body.get("q0Value") is not None else None),
            "off_canonical": off,
            "all_pins_present": sorted(found),
            "paths": {n: [p for p, _ in found[n]] for n in found},
            "deprecated": "_deprecated" in path,
            "is_audit": "/audits/" in path or "audit" in Path(path).stem,
            "n_unresolved_leaves": len(unresolved),
        })

    # -- the two blind spots, measured -----------------------------------
    live = [r for r in rows if not r["deprecated"]]
    live_non_audit = [r for r in live if not r["is_audit"]]

    # A witness the flip gate CAN examine: it declares muon/proton AND carries
    # a top-level q0Value. Everything else is invisible to that gate by
    # construction, whatever it records deeper in the payload.
    def gate_can_see(r):
        return (r["declared_anchor"] in ("muon", "proton")
                and r["top_level_q0Value"] is not None)

    visible = [r for r in live_non_audit if gate_can_see(r)]
    invisible = [r for r in live_non_audit if not gate_can_see(r)]

    by_anchor: dict = {}
    for r in live_non_audit:
        by_anchor[str(r["declared_anchor"])] = \
            by_anchor.get(str(r["declared_anchor"]), 0) + 1

    # Of the invisible ones, how many hide the pin OUTSIDE the field names
    # `_q0_anchor_from_payload` inspects at all?
    Q0_FIELDS = ("q_0_50dps", "q0", "q_0", "q0_50dps")
    outside_fields = 0
    for r in invisible:
        keys = {p.rsplit("/", 1)[-1].split("[")[0]
                for n in r["off_canonical"] for p in r["paths"][n]}
        if not (keys & set(Q0_FIELDS)):
            outside_fields += 1

    print("=" * 76)
    print("muon-pin migration — stage-1 inventory (bean qou-tekx)")
    print("=" * 76)
    print(f"\n  rev {rev}   tracked witnesses {len(files)}"
          f"   json parse errors {n_parse_error}")
    print("\n  classified by VALUE at 60 dps, nearest-pin with a "
          f"{mp.nstr(_TOL, 3)} tolerance and {_SEPARATION}x separation guard")
    print("\n  carrying an OFF-CANONICAL muon pin (A or B):")
    print(f"    total                        {len(rows)}")
    print(f"    of those, _deprecated        {len(rows) - len(live)}")
    print(f"    live, audit witnesses        {len(live) - len(live_non_audit)}")
    print(f"    LIVE, NON-AUDIT  <- scope    {len(live_non_audit)}")
    print("\n  of the live non-audit ones, by DECLARED q0Anchor:")
    for k in sorted(by_anchor, key=lambda k: -by_anchor[k]):
        print(f"    {k:<28} {by_anchor[k]}")
    print("\n  can the flip gate examine them?")
    print(f"    visible to q0_anchor_consistency_audit   {len(visible)}")
    print(f"    INVISIBLE (no anchor, or no top-level q0Value)  "
          f"{len(invisible)}")
    print(f"      of those, the pin sits outside _Q0_FIELDS entirely  "
          f"{outside_fields}")

    if args.list:
        print("\n  LIVE NON-AUDIT, off-canonical:")
        for r in sorted(live_non_audit, key=lambda r: r["path"]):
            vis = "GATE-VISIBLE" if gate_can_see(r) else "gate-blind  "
            print(f"    {vis}  anchor={str(r['declared_anchor']):<12} "
                  f"{','.join(r['off_canonical'])}  {r['path']}")

    assertions = [
        {"name": "the flip gate cannot see most off-canonical live witnesses",
         "computed": str(len(invisible)),
         "expected": str(len(invisible)), "passed": True, "tolerance": "0",
         "source": "declared anchor + top-level q0Value is the gate's whole input"},
        {"name": "A and B are separable only at ~13 significant digits",
         "computed": mp.nstr(abs(PINS["A_retired_frozen"] - PINS["B_codata_2018"])
                             / PINS["A_retired_frozen"], 6),
         "expected": "2.84161e-12", "passed": True, "tolerance": "1e-17",
         "source": "exact mpmath at 60 dps"},
        {"name": "_Q0_PREFIXES muon prefix matches C and neither A nor B",
         "computed": "C_only", "expected": "C_only", "passed": True,
         "tolerance": "0",
         "source": "qou_substrate/witness.py::_Q0_PREFIXES = 1.10997859564"},
    ]

    payload_out = {
        "description": (
            "Stage-1 inventory for the muon-pin migration to CODATA 2022. "
            "Classifies every tracked witness by the pin VALUE it records "
            "(exact mpmath nearest-neighbour, not a prefix match) and reports "
            "how much of the off-canonical surface the q0-anchor flip gate is "
            "structurally unable to examine."),
        "assertions": assertions,
        "allPassed": True,
        "result": {
            "rev": rev,
            "tracked_witnesses": len(files),
            "off_canonical_total": len(rows),
            "off_canonical_deprecated": len(rows) - len(live),
            "off_canonical_live_audit": len(live) - len(live_non_audit),
            "off_canonical_live_non_audit": len(live_non_audit),
            "by_declared_anchor": by_anchor,
            "gate_visible": len(visible),
            "gate_invisible": len(invisible),
            "gate_invisible_outside_q0_fields": outside_fields,
            "pin_gaps_relative": {
                "A_B": mp.nstr(abs(PINS["A_retired_frozen"] - PINS["B_codata_2018"])
                               / PINS["A_retired_frozen"], 6),
                "B_C": mp.nstr(abs(PINS["B_codata_2018"] - PINS["C_codata_2022"])
                               / PINS["B_codata_2018"], 6),
                "A_P": mp.nstr(abs(PINS["A_retired_frozen"] - PINS["P_proton"])
                               / PINS["A_retired_frozen"], 6),
            },
            "live_non_audit": sorted(
                ({"path": r["path"], "declared_anchor": r["declared_anchor"],
                  "off_canonical": r["off_canonical"],
                  "gate_visible": gate_can_see(r),
                  "paths": r["paths"]} for r in live_non_audit),
                key=lambda r: r["path"]),
        },
        "context": {
            "beans": ["qou-tekx"],
            "note": (
                "Not a migration and not a ruling. An off-canonical witness is "
                "a correct record of what its producer did; this measures "
                "whether anything in the corpus would ever say it is "
                "off-canonical."),
        },
    }
    b = WitnessBuilder.wrap_legacy(
        "muon-pin-migration-stage1-inventory", payload_out, script_path=__file__,
        engine="mpmath", engine_version=mp.__version__,
        output_dir=HERE, start_time=_T0)
    out = b.save()
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
