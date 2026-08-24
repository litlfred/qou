#!/usr/bin/env python3
# polynomial_q_not_applicable: validator, not a q-series compute.
"""Producers that INHERIT their q0 from another producer's witness -- and are
stamped from the manifest, which knows nothing about what they inherited.

THE SHAPE. A producer reads a q0 out of an upstream `*.witness.json` and
computes with it:

    src = json.load(open("binding-bar-even-odd-probe.witness.json"))
    q0  = mp.mpf(src["constants"]["q_0"])      # whatever pin THAT probe was at
    ...
    nu  = invert_ratio(rho, lambda x: gamma_q_gt1(x, q0))   # reaches the math

Its own witness is then stamped by `witness.py` from the producer's stem in
`q0_anchor_manifest.json`. Those two facts are independent: the manifest says
what the producer is SUPPOSED to be pinned at, the upstream witness carries
whatever it IS pinned at today. Re-pin the upstream and the producer silently
follows it while its stamp does not move.

WHY THE EXISTING GATES CANNOT SEE IT. Measured 2026-08-24 on
`parabolic_cylinder_channel_mixing_probe`, then stamped `muon` while computing
at proton. **That instance is FIXED in the same commit as this file** -- the
manifest now lists it `physical_proton` and its witness was regenerated, and
regenerating moved the stamp and nothing else, which is the signature of a
label correction rather than a value change. Cite the mechanism, re-measure the
instance. What every gate below reported while it was live:

  q0_anchor_consistency_audit   compares the stamp against itself     -> Q0_OK
  anchor_flip_straddle_audit    flips QOU_Q0_ANCHOR and diffs; a q
    (BLOCKING, fa2794159b)      read from a FILE does not move        -> clean
  q0_producer_pin_classifier    keys on accessors, module imports,
                                muon artifact names, 50-digit
                                literals -- an upstream subscript is
                                none of those                    -> ('none',[])
  tnjb_stale_stamp_migrate      scoped to producers the classifier
                                resolves PROTON; `none` is excluded  -> skipped
  q0_anchor_contradiction_triage  scoped to witnesses declaring
                                `proton`; this one declares muon  -> out of scope

Five mechanisms, none of which is wrong about its own question. The gap is
that none of them asks whether the stamp matches the NUMBERS IN THE SAME FILE.

THE CONTROL THAT SETTLES IT. Two other producers --
`defect_weighted_zero_point_probe` and `zero_point_channel_energy_probe` --
read the SAME upstream witness by the same expression and are listed
`physical_proton`. Three readers of one file, two labelled proton and one
labelled muon, is not a policy disagreement about which layer the quantity
belongs to; it is one row that disagrees with its own input.

NOT EVERY INHERITED PIN IS A DEFECT. Reading
`q-pinning-50-digit.witness.json` -- the anchor-DEFINING muon witness -- is an
explicit muon pin, stable by construction, and is exempt. Measured, that is
where 9 of the 10 literal-key readers point. The unstable case is inheriting
from an ORDINARY downstream probe, whose pin is whatever its own last
regeneration left behind.

🛑 THIS DETECTOR HAS A KNOWN BLIND SPOT, AND IT IS THE ONE THAT FOUND IT.
A first pass keyed on LITERAL subscript keys (`src["constants"]["q_0"]`) and
therefore MISSED `parabolic_cylinder_channel_mixing_probe`, which spells the
key as a module constant (`Q0_KEY = "q_0"; src["constants"][Q0_KEY]`). Module
level `str` constants are resolved below, but a key built at runtime, read from
argv, or reached through a helper function still escapes. Per
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`: closing one spelling
does not close the class. `--selftest` pins the known positive so a future
narrowing cannot silently report a clean tree.

Usage:
    python3 inherited_q0_pin_audit.py [--selftest] [--json OUT]
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMPUTE = REPO / "computations"
MANIFEST = COMPUTE / "q0_anchor_manifest.json"
SKIP = (".git", ".claude", "_deprecated", "node_modules", "__pycache__", "tests")

# The anchor-DEFINING witness. Reading it IS an explicit muon pin (AGENTS.md
# §"NEVER re-pin an anchor-DEFINING witness"), so it is exempt from this audit.
ANCHOR_DEFINING = ("q-pinning-50-digit.witness.json",)

MUON = "1.10997859555733471989976322048322502665620840878015368660798114614493"
PROTON = "1.1099785827513808075916690956107688798744991218736"
# 14 digits separates the two pins (they agree to 1.1099785 8/9) and is short
# enough to match a value serialized at reduced precision.
_PREFIX = 14

Q0_KEY = re.compile(r"^(q_?0|q|q_str|substrate_q|q_value|q0_value)$", re.I)
WITNESS_READ = re.compile(r"json\.load|read_text|record_upstream|load_witness")
KNOWN_POSITIVE = "parabolic_cylinder_channel_mixing_probe"


def pin_class(value) -> str | None:
    """'muon' / 'proton' / None -- by 14-digit prefix, never by arithmetic."""
    s = str(value).strip()
    if s.startswith(MUON[:_PREFIX]):
        return "muon"
    if s.startswith(PROTON[:_PREFIX]):
        return "proton"
    return None


def manifest_class() -> dict[str, str]:
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {stem: k for k, v in man.items() if isinstance(v, list) for stem in v}


def _str_consts(tree: ast.Module) -> dict[str, str]:
    """Module-level `NAME = "literal"`, so a key spelled as a constant resolves."""
    out = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                and isinstance(n.targets[0], ast.Name) \
                and isinstance(n.value, ast.Constant) \
                and isinstance(n.value.value, str):
            out[n.targets[0].id] = n.value.value
    return out


def _key_of(node: ast.Subscript, consts: dict[str, str]) -> str | None:
    s = node.slice
    if isinstance(s, ast.Constant) and isinstance(s.value, str):
        return s.value
    if isinstance(s, ast.Name):
        return consts.get(s.id)
    return None


def _witness_names(tree: ast.Module, src: str) -> dict[str, str]:
    """name -> the witness filename it was read from (best effort)."""
    out = {}
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Assign) and len(n.targets) == 1
                and isinstance(n.targets[0], ast.Name)):
            continue
        rhs = ast.unparse(n.value)
        if not WITNESS_READ.search(rhs):
            continue
        m = re.search(r"([A-Za-z0-9_.\-]+\.witness\.json)", rhs)
        if m:
            out[n.targets[0].id] = m.group(1)
            continue
        # The path is usually a module constant: WITNESS_IN = Path(...)
        for name in {x.id for x in ast.walk(n.value) if isinstance(x, ast.Name)}:
            hit = re.search(rf"{re.escape(name)}\s*=.*?([A-Za-z0-9_.\-]+\.witness\.json)",
                            src, re.S)
            if hit:
                out[n.targets[0].id] = hit.group(1)
                break
        else:
            out[n.targets[0].id] = "?"
    return out


def _find_upstream(fname: str) -> Path | None:
    for p in COMPUTE.rglob(fname):
        return p
    return None


def scan() -> list[dict]:
    mcls = manifest_class()
    rows = []
    for p in sorted(COMPUTE.rglob("*.py")):
        if any(x in p.parts for x in SKIP):
            continue
        try:
            src = p.read_text(encoding="utf-8")
            tree = ast.parse(src)
        except (OSError, SyntaxError):
            continue
        if ".witness.json" not in src:
            continue
        wnames = _witness_names(tree, src)
        if not wnames:
            continue
        consts = _str_consts(tree)
        for n in ast.walk(tree):
            if not isinstance(n, ast.Subscript):
                continue
            key = _key_of(n, consts)
            if not key or not Q0_KEY.match(key):
                continue
            base = n
            while isinstance(base, ast.Subscript):
                base = base.value
            if not (isinstance(base, ast.Name) and base.id in wnames):
                continue
            upstream = wnames[base.id]
            if upstream in ANCHOR_DEFINING:
                continue                      # explicit, stable muon pin
            rows.append({
                "producer": str(p.relative_to(REPO)),
                "stem": p.stem,
                "expr": ast.unparse(n)[:80],
                "upstream": upstream,
                "manifest": mcls.get(p.stem, "ABSENT"),
            })
            break                             # one row per producer
    # Annotate with what the upstream ACTUALLY holds today.
    for r in rows:
        up = _find_upstream(r["upstream"]) if r["upstream"] != "?" else None
        r["upstream_pin"] = None
        if up is not None:
            try:
                w = json.loads(up.read_text(encoding="utf-8"))
            except Exception:                                   # noqa: BLE001
                w = None
            if w is not None:
                r["upstream_pin"] = _pin_in(w, r["expr"])
        declared = {"ideal_muon": "muon", "physical_proton": "proton"}.get(r["manifest"])
        if r["upstream_pin"] and declared and r["upstream_pin"] != declared:
            r["verdict"] = "MISLABEL"
        elif r["upstream_pin"] and declared:
            r["verdict"] = "agrees"
        else:
            r["verdict"] = "undetermined"
    return rows


def _pin_in(obj, _expr) -> str | None:
    """First q0-classed value anywhere in the upstream witness body."""
    stack = [obj]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            stack += list(o.values())
        elif isinstance(o, list):
            stack += o
        else:
            c = pin_class(o)
            if c:
                return c
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json")
    args = ap.parse_args()

    rows = scan()
    if args.selftest:
        # The guard is on the DETECTOR'S REACH, not on a live defect. The
        # known positive was a MISLABEL when this was written and is now
        # `agrees` (manifest corrected + witness regenerated, same commit) --
        # so asserting MISLABEL would be a gate that goes red the moment the
        # bug it names is fixed. What must not regress is that this producer
        # is SEEN at all: it spells its key as a module constant
        # (`Q0_KEY = "q_0"; src["constants"][Q0_KEY]`), the exact spelling a
        # literal-key-only pass missed. If a future narrowing drops it, the
        # tree reads clean for the wrong reason.
        got = [r for r in rows if r["stem"] == KNOWN_POSITIVE]
        print(f"  key-resolution probe {KNOWN_POSITIVE}: "
              f"{got[0]['verdict'] if got else 'NOT DETECTED'}")
        if not got:
            print("  SELFTEST FAILED — the constant-spelled key is no longer resolved.")
            return 1
        print("  selftest OK")
        return 0

    print("=" * 72)
    print("inherited-q0-pin audit — producers whose q0 comes from another")
    print("producer's witness, stamped from a manifest that cannot know it")
    print("=" * 72)
    order = {"MISLABEL": 0, "undetermined": 1, "agrees": 2}
    for r in sorted(rows, key=lambda x: (order[x["verdict"]], x["producer"])):
        print(f"  {r['verdict']:13s} {r['producer']}")
        print(f"{'':17s}{r['expr']}")
        print(f"{'':17s}upstream={r['upstream']} holds={r['upstream_pin']} "
              f"manifest={r['manifest']}")
    tally = {}
    for r in rows:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    print("\n  " + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    print("=" * 72)
    if args.json:
        Path(args.json).write_text(json.dumps({"rows": rows, "tally": tally}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
