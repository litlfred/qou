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

## Contradicted vs UNFALSIFIABLE — two different defects

The check above catches a block whose witness CONTRADICTS it. It says nothing
about a block whose witness cannot contradict anything, and that is the larger
class. Three shapes, all reported separately below because the fix differs:

  * **vacuous**  — `allPassed: true` over an EMPTY assertions array. `all([])`
    is `True`, so the witness reports that everything passed having tested
    nothing. A block citing it as "verified" is making an unbacked claim, and
    no amount of re-running changes that.
  * **absent**   — the cited witness file is missing or unparseable. Until
    2026-08-23 this was a parenthetical at the bottom of the report rather
    than a finding.
  * **no verdict** — the witness carries no top-level `allPassed` at all. Often
    legitimate (a data-only witness), so it is counted, not failed.

Measured 2026-08-22 (bean qou-vfy1) across the 221 blocks marked `verified`:
157 backed by real assertions, **43 vacuous**, 8 contradicted, 5 absent, 8
citing no witness at all. The 8 contradicted were drained under qou-bm4i; the
vacuous 43 are what this extension exists to surface.

Note on the fix: making `WitnessBuilder` emit `allPassed: null` for an empty
assertion list was investigated under qou-vfy1 and WITHDRAWN — about a dozen
producers hand-roll `return 0 if wit["allPassed"] else 1`, and `None` is falsy,
so that turns a silent false positive into a loud false negative. This checker
therefore reads `len(assertions)` directly and requires no schema change and no
producer change.

  check-computation-status.py                 # report
  check-computation-status.py --strict        # exit 1 on any CONTRADICTION
  check-computation-status.py --strict-unbacked   # also exit 1 on vacuous/absent
  check-computation-status.py --files A.ts B.ts   # only these manifests

`--strict` deliberately keeps its original meaning so existing callers do not
change behaviour under them; the new classes are opt-in.
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
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any CONTRADICTION (status vs allPassed)")
    ap.add_argument("--strict-unbacked", action="store_true",
                    help="also exit 1 on `verified` claims backed by a vacuous "
                         "or absent witness")
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
    per_block, missing, checked, no_verdict = {}, [], 0, 0
    for lab, st, w, ts in scan(only):
        e = per_block.setdefault(lab, {"st": st, "ts": ts, "any_false": False,
                                       "fails": [], "wit": [],
                                       "absent": [], "vacuous": [],
                                       "any_backed": False})
        e["wit"].append(w)
        p = REPO / w
        if not p.exists():
            missing.append((lab, w, ts))
            e["absent"].append(w)
            continue
        try:
            d = json.loads(p.read_text())
        except Exception:
            missing.append((lab, w, ts))
            e["absent"].append(w)
            continue
        ap_ = d.get("allPassed")
        if ap_ is None:
            no_verdict += 1               # no top-level verdict; often legitimate
            continue
        checked += 1
        # `all([])` is True, so a witness with NO assertions reports that
        # everything passed having tested nothing. Count the assertions rather
        # than trusting the flag — this is the whole point of the extension.
        asserts = d.get("assertions")
        n_assert = len(asserts) if isinstance(asserts, (list, dict)) else 0
        if ap_ is True and n_assert == 0:
            e["vacuous"].append(w)
        elif ap_ is True:
            e["any_backed"] = True
        fails = []
        if isinstance(asserts, list):
            fails = [a.get("name") or a.get("description") or "?"
                     for a in asserts
                     if isinstance(a, dict) and a.get("passed") is False]
        elif isinstance(asserts, dict):
            fails = [k for k, v in asserts.items() if v is False]
        if ap_ is False:
            e["any_false"] = True
            e["fails"].extend(fails)

    bad, unbacked = [], []
    for lab, e in per_block.items():
        w = ", ".join(e["wit"])
        if e["st"] == "verified" and e["any_false"]:
            bad.append((lab, e["st"], w, e["fails"], e["ts"],
                        "verified but a cited witness has allPassed=false"))
        elif e["st"] == "failed" and not e["any_false"]:
            bad.append((lab, e["st"], w, [], e["ts"],
                        "failed but every cited witness all-passed"))
        # UNFALSIFIABLE: only a `verified` claim is a claim. A block marked
        # experimental / not_run / pending citing a data-only witness is fine.
        # And a block is only unbacked if NO cited witness backs it — several
        # legitimately pair a data-only witness with an asserting one.
        if e["st"] == "verified" and not e["any_backed"] and not e["any_false"]:
            if e["vacuous"]:
                unbacked.append((lab, "vacuous", ", ".join(e["vacuous"]), e["ts"],
                                 "verified, but the cited witness has ZERO "
                                 "assertions (allPassed=true over all([]))"))
            elif e["absent"]:
                unbacked.append((lab, "absent", ", ".join(e["absent"]), e["ts"],
                                 "verified, but the cited witness is missing "
                                 "or unparseable"))

    print(f"{checked} block/witness pairs carry a top-level `allPassed`.\n")
    for lab, st, w, fails, ts, why in bad:
        print(f"  ✗ {lab}   [{why}]")
        print(f"      witness : {w}")
        if fails:
            print(f"      failing : {', '.join(fails[:6])}"
                  + (f"  (+{len(fails)-6} more)" if len(fails) > 6 else ""))
        print(f"      manifest: {ts.relative_to(REPO)}")
        print()
    print(f"{len(bad)} disagreement(s).\n")

    if unbacked:
        print(f"{len(unbacked)} `verified` claim(s) with nothing behind them "
              f"— UNFALSIFIABLE, not contradicted:\n")
        for lab, kind, w, ts, why in sorted(unbacked, key=lambda r: (r[1], r[0])):
            # one block cites 119 witnesses; printing them all buries the report
            names = [pathlib.Path(x).name for x in w.split(", ")]
            shown = ", ".join(names[:3])
            if len(names) > 3:
                shown += f"  (+{len(names) - 3} more)"
            print(f"  ? {lab}   [{kind}]")
            print(f"      {why}")
            print(f"      witness : {shown}")
            print(f"      manifest: {ts.relative_to(REPO)}")
            print()
    by_kind = {}
    for _, kind, *_ in unbacked:
        by_kind[kind] = by_kind.get(kind, 0) + 1
    print(f"  unbacked by kind: " + (", ".join(f"{k}={v}" for k, v in sorted(by_kind.items()))
                                      if by_kind else "none"))
    if no_verdict:
        print(f"  {no_verdict} cited witness(es) carry no top-level `allPassed` "
              f"(often legitimate: a data-only witness).")
    if missing:
        print(f"  {len(missing)} cited witness file(s) missing or unparseable.")
    fail = bool(args.strict and bad) or bool(args.strict_unbacked and (bad or unbacked))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
