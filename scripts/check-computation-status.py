#!/usr/bin/env python3
"""Does a block's `computation.status` agree with the witness it cites?

`ComputationStatus` (folio-assistant/schemas/types.ts) is explicit:

    "verified"  script ran, witness matches expected values within tolerance
    "failed"    script ran, witness does NOT match expected values

and `ComputationAssertion` says "The CI pipeline checks
|computed - expected| <= tolerance".  So a witness whose own top-level
`allPassed` is `false` belongs to a block marked `failed`, not `verified`.

**Nothing checked this.**  The schema declares the field; no constraint, no
sweep and no CI step ever compared it to the witness.  Measured 2026-08-23:
8 of 166 blocks marked `verified` cited a witness with `allPassed: false`,
including one whose witness contradicts a number the block states by a factor
of three.

Only the witness's TOP-LEVEL `allPassed` is used. Nested booleans (a
comparison table's per-row `match`, say) are legitimately false and are not
evidence of anything.

  check-computation-status.py                 # report
  check-computation-status.py --strict        # exit 1 on any disagreement
  check-computation-status.py --files A.ts B.ts   # only these manifests
"""

import argparse
import json
import pathlib
import re
import sys

CONTENT = pathlib.Path(__file__).resolve().parent.parent / "content"
REPO = CONTENT.parent

LABEL = re.compile(r'label:\s*"([^"]+)"')
STATUS = re.compile(r'status:\s*"([^"]+)"')
# `witness: "x"` or `witness:\n  "x"` or `witness: ["x", "y"]`
WITNESS = re.compile(r'witness:\s*(\[[^\]]*\]|"[^"]+"|\n\s*"[^"]+")', re.S)


def witness_paths(raw: str):
    return re.findall(r'"([^"]+\.json)"', raw)


def scan(only=None):
    out = []
    for ts in sorted(CONTENT.rglob("*.ts")):
        if only is not None and str(ts.relative_to(REPO)) not in only:
            continue
        text = ts.read_text()
        if "computation:" not in text:
            continue
        lab, st, wit = LABEL.search(text), STATUS.search(text), WITNESS.search(text)
        if not (lab and st and wit):
            continue
        for w in witness_paths(wit.group(1)):
            out.append((lab.group(1), st.group(1), w, ts))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="exit 1 on any disagreement")
    ap.add_argument("--files", nargs="*", metavar="PATH",
                    help="restrict to these manifests (repo-relative)")
    args = ap.parse_args()

    only = None
    if args.files is not None:
        only = {str(pathlib.Path(f)) for f in args.files}

    # A block may cite SEVERAL witnesses, so the verdict has to be aggregated
    # per block: `failed` is right if ANY cited witness did not all-pass.
    # Judging each (block, witness) pair on its own reported a block correctly
    # marked `failed` as wrong, because its *other* witness was green.
    per_block, missing, checked = {}, [], 0
    for lab, st, w, ts in scan(only):
        p = REPO / w
        if not p.exists():
            missing.append((lab, w, ts))
            continue
        try:
            d = json.loads(p.read_text())
        except Exception:
            missing.append((lab, w, ts))
            continue
        ap_ = d.get("allPassed")
        if ap_ is None:
            continue                      # no top-level verdict; nothing to compare
        checked += 1
        fails = [a.get("name") or a.get("description") or "?"
                 for a in d.get("assertions", [])
                 if isinstance(a, dict) and a.get("passed") is False]
        e = per_block.setdefault(lab, {"st": st, "ts": ts, "any_false": False,
                                       "fails": [], "wit": []})
        e["wit"].append(w)
        if ap_ is False:
            e["any_false"] = True
            e["fails"].extend(fails)

    bad = []
    for lab, e in per_block.items():
        w = ", ".join(e["wit"])
        if e["st"] == "verified" and e["any_false"]:
            bad.append((lab, e["st"], w, e["fails"], e["ts"],
                        "verified but a cited witness has allPassed=false"))
        elif e["st"] == "failed" and not e["any_false"]:
            bad.append((lab, e["st"], w, [], e["ts"],
                        "failed but every cited witness all-passed"))

    print(f"{checked} block/witness pairs carry a top-level `allPassed`.\n")
    for lab, st, w, fails, ts, why in bad:
        print(f"  ✗ {lab}   [{why}]")
        print(f"      witness : {w}")
        if fails:
            print(f"      failing : {', '.join(fails[:6])}"
                  + (f"  (+{len(fails)-6} more)" if len(fails) > 6 else ""))
        print(f"      manifest: {ts.relative_to(REPO)}")
        print()
    if missing:
        print(f"  ({len(missing)} cited witness file(s) missing or unparseable)")
    print(f"{len(bad)} disagreement(s).")
    return 1 if (args.strict and bad) else 0


if __name__ == "__main__":
    sys.exit(main())
