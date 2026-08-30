#!/usr/bin/env python3
"""witness_filename_blindspot_audit.py — witnesses that no witness-keyed tool can see.

THE BLIND SPOT.  Every witness-consuming tool in this corpus globs `*.witness.json`
-- the raw-float64 ratchet, `witness_staleness_triage.py`, the q0-anchor
classifier and ratchet, and layers 2 and 3 of
`computations/audits/ylambda_threerow_frame_audit.py`.  A file that carries full
witness provenance (`scriptHash`, `commitSha`, `computedAt`, `q0Anchor`, ...) but
is named `foo-witness.json` or plain `foo.json` is invisible to all of them.

One character.  `-witness.json` against `.witness.json`.

MEASURED 2026-08-30 against `origin/main`: 7 tracked files under `computations/`
carry >= 3 provenance stamps and are NOT named `*.witness.json`.  FIVE of them are
the `y-lambda-*` family -- the subject of the audit that was blind to them.

BASELINE FROM GIT, NEVER FROM THE WORKING TREE.  This audit's first run reported
**8**, and the extra one was its own author's doing: running
`l1_ceiling_d_frame_remeasure.py` a few minutes earlier had ADDED provenance
stamps to `l1-ceiling-d-frame-remeasure.json`, which on `origin/main` carries
NONE.  That file is not an invisible witness at all; it is unstamped output that
becomes stamped the moment anyone re-runs its producer.  Measuring a corpus
property against a tree your own commands have mutated gives you a fact about
your session.  AGENTS.md records the same error costing two wrong figures in the
witness-staleness rate (39 % and 73 %, both retracted); this is a third.  Pass
`--worktree` to measure the tree deliberately.

THE PAYOFF QUESTION, and the answer is mostly reassuring.  Every one of the five
carries CONVENTION-D values where a fingerprint is detectable; there is no C-frame
contamination hiding here.  But one carries a declaration its own contents refute:

    y-lambda-wenzl-bridge-numeric-witness.json
        q0Anchor:       "independent"
        q0AnchorReason: "producer declared q0-independent at the stamp site
                         (q0_anchor=False): no q0-dependent field in this witness"
        /q0:            1.10997859555418051695830018898879867637876138498395

A `/q0` VALUE field, not a mention in a description -- checked by walking the JSON
and reporting the path, because "the token appears" and "the value is used" are
different claims and only one of them is a defect.

AND NOTE WHICH MUON VALUE.  That is `...55541805...`, the CODATA-2018 lepton-tower
derivation -- NOT the frozen canonical pin `1.1099785955573347...`.  AGENTS.md
records three distinct values all called "the muon q0", diverging at the 13th
significant digit; calling this one "the muon pin" would be the error that section
exists to prevent.

NOT FIXED HERE.  Re-stamping is a producer-side declaration, which per bean
`qou-x5mi` costs a full re-run and inherits every environment difference -- four
producers there did not reproduce their committed values under a changed mpmath.
Renaming is worse: any consumer reading the path breaks silently.  This audit
reports; the fix is a scoped change.

Exit 1 if any file is found, so the count cannot quietly grow.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
STAMPS = ("scriptHash", "scriptCommitSha", "commitSha", "computedAt", "q0Anchor", "engine")
MIN_STAMPS = 3

# The three values AGENTS.md records as all being called "the muon q0". They
# diverge at the 13th significant digit, so the prefix chosen decides which one
# is being counted -- quote the label, never a bare "muon".
MUON_VALUES = {
    "1.1099785955573347": "frozen canonical pin",
    "1.1099785955541805": "lepton tower, CODATA 2018",
    "1.1099785956427390": "lepton tower, CODATA 2022",
}
PROTON = "1.10997858275138"


def _walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from _walk(v, f"{path}/{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _walk(v, f"{path}[{i}]")
    else:
        yield path, o


REF = "origin/main"


def _tracked_json(ref):
    """Paths, plus a reader that returns the content AT `ref` (or the worktree)."""
    listing = (["git", "-C", str(ROOT), "ls-files", "computations"] if ref is None
               else ["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only",
                     ref, "computations"])
    out = subprocess.run(listing, capture_output=True, text=True).stdout.split()
    for f in out:
        if f.endswith(".json") and not f.endswith(".witness.json"):
            yield f


def _read(rel, ref):
    if ref is None:
        return (ROOT / rel).read_text()
    r = subprocess.run(["git", "-C", str(ROOT), "show", f"{ref}:{rel}"],
                       capture_output=True, text=True)
    if r.returncode:
        raise FileNotFoundError(rel)
    return r.stdout


def main() -> int:
    ref = None if "--worktree" in sys.argv else REF
    print("=" * 88)
    print(" Witnesses invisible to every *.witness.json-keyed tool")
    print(f" measured against: {ref or 'THE WORKING TREE (--worktree)'}")
    if ref is None:
        print(" WARNING: a producer you ran this session may have added stamps that")
        print("          are not in the committed tree. This is a fact about your")
        print("          session, not about the corpus.")
    print("=" * 88)
    found = []
    for rel in sorted(_tracked_json(ref)):
        try:
            d = json.loads(_read(rel, ref))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        stamps = [k for k in STAMPS if k in d]
        if len(stamps) < MIN_STAMPS:
            continue

        # Where does a pin VALUE actually sit? A description that merely mentions
        # one is not a q0-dependent field.
        pin_value_sites = []
        for path, val in _walk(d):
            sval = str(val)
            if len(sval) > 400:      # prose, not a number
                continue
            for prefix, label in MUON_VALUES.items():
                if sval.startswith(prefix):
                    pin_value_sites.append((path, f"muon ({label})"))
            if sval.startswith(PROTON):
                pin_value_sites.append((path, "proton"))

        declared = d.get("q0Anchor")
        contradiction = (declared == "independent" and pin_value_sites)
        found.append((rel, stamps, declared, pin_value_sites, contradiction))

    for rel, stamps, declared, sites, contra in found:
        flag = "   <-- DECLARATION CONTRADICTED BY ITS OWN FIELDS" if contra else ""
        print(f"\n  {rel}{flag}")
        print(f"      stamps: {','.join(stamps)}")
        print(f"      q0Anchor: {declared}")
        for path, kind in sites:
            print(f"      pin VALUE at {path}: {kind}")

    contradicted = [f for f, _, _, _, c in found if c]
    print("\n" + "=" * 88)
    print(f"  files carrying witness provenance but not named *.witness.json: {len(found)}")
    print(f"  of those, q0Anchor declaration contradicted by a pin value field: "
          f"{len(contradicted)}")
    for f in contradicted:
        print(f"      {f}")
    print()
    print("  Every one is invisible to the raw-float64 ratchet, witness staleness")
    print("  triage, the q0-anchor classifier and ratchet, and layers 2 and 3 of the")
    print("  y_lambda frame audit -- all of which glob *.witness.json.")
    print("=" * 88)
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
