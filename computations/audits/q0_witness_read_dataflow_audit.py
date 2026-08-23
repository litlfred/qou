#!/usr/bin/env python3
"""q0_witness_read_dataflow_audit.py — which producers inherit a q₀ by READING a
pinned witness, rather than by importing a q₀ accessor?

WHY THIS EXISTS
    Every q₀ classifier in this repo answers the question through the **import
    graph**: `q0_producer_pin_classifier.classify()` walks a producer's AST for
    imports and names, and the transitive variants walk its import cone. That
    is the right shape for a producer that calls `q_at()`.

    It is the wrong shape for this:

        UPSTREAM = "sublemma-2-1-A-operator-extract.witness.json"
        data = json.load(open(_pb.witness_path(UPSTREAM)))
        q0 = data["q_0"]

    Nothing is imported. No literal appears. The dependency travels through the
    **filesystem**, and no amount of depth on an import cone will ever reach it.
    A producer that reads a number out of a pinned witness is exactly as
    q₀-dependent as one that calls the accessor.

HOW THIS WAS MEASURED, AND WHY THAT MATTERS
    A 13-agent read-only adjudication (2026-08-19/23) checked an import-cone
    classifier's verdicts against agents actually reading the producers. Of 352
    producers it called `independent`, **130 were wrong** — and **49 of those
    130 were this route**, the second-largest class and the only one that is
    *structurally* invisible rather than merely missed.

    So this is not a hypothetical gap. It is a measured 14 % of one classifier's
    output, and it needs a detector of a different kind.

WHAT COUNTS AS A HIT
    A producer that, in live code (outside `if __name__ == "__main__"`, not in a
    docstring), names a `*.witness.json` which — on disk today — either declares
    a `q0Anchor` of `muon` / `proton` / `comparison`, or carries one of the pin
    prefixes anywhere in its payload.

    Naming a witness it WRITES is not a hit; producers are matched against their
    own output filename and that is excluded.

WHAT THIS DOES NOT ESTABLISH
    That the producer *uses* the q₀-bearing part of what it read. A witness
    carries many fields, and reading one is not reading its pin. This is a
    **candidate** detector in the same sense as its import-cone sibling: it says
    a q₀ is reachable through the filesystem, not that a number moved. The
    adjudication above is the standard for deciding that, and it is an agent
    read, not a scan.

    Chains are followed ONE hop. A producer reading a witness whose own producer
    reads a pinned witness is not resolved here.

MEASURED RECALL — 80 %, AND THE MISSES ARE A TAXONOMY
    Scored against the same adjudication that motivated it, on the 55 producers
    agents independently classified as this route:

        caught                  44 / 55   (80 %)
        missed                  11
        fires on adjudicated-independent   9 / 246  (3.7 %)

    The 11 misses are not noise; each names a route this shape cannot reach:

      * **The pin is one hop further.** `alpha_em_b2_cm_weierstrass_scale_probe`
        reads `alpha-em-b2-invariant-c.witness.json`, which carries no pin of its
        own — its *producer* calls `q_at()`. Chains are followed one hop, by
        construction, and this is the cost.
      * **The filename never appears as a string.** `qbeta_dladder_coupled_
        qsqrt3_recurrence_probe` gets its data from `dlad.build_d_ladder()` — a
        function call into another module that does the reading. Invisible to a
        filename scan *and* to an import-cone pin check, since the imported
        module's pin arrives through ITS filesystem read.

    The 9 that fire on adjudicated-independent producers are the documented
    caveat working as intended: reading a pinned witness is not using its pin.
    Treat every hit as a candidate.

    Recall is quoted against 55 adjudicated cases, not against the truth. A
    route nobody has adjudicated cannot appear in either column.

READ-ONLY
    Emits a report and, with `--emit`, a JSON list. Writes no witness, edits no
    manifest, runs no producer.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent

sys.path.insert(0, str(HERE))
from q0_producer_pin_classifier import strip_main_block  # noqa: E402

# 11 digits after the point — the corpus carries two muon values agreeing to 11
# and diverging at the 12th (see q0_muon_population_partition.py). A 12-digit
# prefix silently drops every artifact still on the superseded value.
MUON_PREFIX = "1.10997859555"
PROTON_PREFIX = "1.109978582751"
PINNED_ANCHORS = {"muon", "proton", "comparison"}

SKIP_DIRS = {".git", "__pycache__", "node_modules", "target", "_deprecated"}


def witness_index() -> dict[str, list[Path]]:
    idx: dict[str, list[Path]] = defaultdict(list)
    for p in COMPUTE_DIR.rglob("*.witness.json"):
        if SKIP_DIRS & set(p.parts):
            continue
        idx[p.name].append(p)
    return idx


def witness_pin(path: Path) -> tuple[str, str]:
    """(pin, how) for a witness on disk. pin is '' when it carries none."""
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "", ""
    try:
        body = json.loads(raw)
    except json.JSONDecodeError:
        return "", ""
    if isinstance(body, dict):
        anchor = body.get("q0Anchor")
        if anchor in PINNED_ANCHORS:
            return str(anchor), "q0Anchor"
    has_mu = MUON_PREFIX in raw
    has_pr = PROTON_PREFIX in raw
    if has_mu and has_pr:
        return "comparison", "payload (both prefixes)"
    if has_mu:
        return "muon", "payload"
    if has_pr:
        return "proton", "payload"
    return "", ""


def witness_names_read(py: Path) -> set[str]:
    """Every `*.witness.json` named in live code."""
    try:
        tree = ast.parse(py.read_text(encoding="utf-8", errors="replace"))
    except (SyntaxError, OSError, ValueError):
        return set()
    names: set[str] = set()
    for node in ast.walk(ast.Module(body=strip_main_block(tree), type_ignores=[])):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            s = node.value
            if s.endswith(".witness.json"):
                names.add(s.rsplit("/", 1)[-1])
    return names


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--emit", type=str, default=None)
    ap.add_argument("--show", type=int, default=15)
    args = ap.parse_args(argv)

    widx = witness_index()
    pin_cache: dict[Path, tuple[str, str]] = {}

    hits = []
    scanned = 0
    for py in sorted(COMPUTE_DIR.rglob("*.py")):
        if SKIP_DIRS & set(py.parts):
            continue
        scanned += 1
        own_stem = py.stem.replace("_", "-")
        for name in sorted(witness_names_read(py)):
            # a producer naming its OWN output is writing, not reading
            if name.replace(".witness.json", "") == own_stem:
                continue
            for wp in widx.get(name, []):
                if wp not in pin_cache:
                    pin_cache[wp] = witness_pin(wp)
                pin, how = pin_cache[wp]
                if pin:
                    hits.append({
                        "producer": str(py.relative_to(REPO)),
                        "reads": str(wp.relative_to(REPO)),
                        "pin": pin,
                        "evidence": how,
                    })
                break

    by_producer: dict[str, set[str]] = defaultdict(set)
    for h in hits:
        by_producer[h["producer"]].add(h["pin"])

    straddles = {p: v for p, v in by_producer.items()
                 if len(v - {"comparison"}) > 1 or "comparison" in v}

    print("=" * 72)
    print("q₀ inherited by READING a pinned witness (filesystem, not imports)")
    print("=" * 72)
    print(f"  python files scanned            : {scanned}")
    print(f"  producers reading a pinned one  : {len(by_producer)}")
    print(f"  distinct (producer, witness)    : {len(hits)}")
    print(f"  pins seen                       : "
          f"{dict(Counter(h['pin'] for h in hits))}")
    print(f"\n  🛑 producers reading MORE THAN ONE pin      : {len(straddles)}")
    print("     (a layer straddle candidate — AGENTS.md §q₀-anchor: 'never")
    print("      straddle the two layers inside one quantity'. Candidate, not")
    print("      verdict: reading two pinned witnesses is not yet combining")
    print("      them inside one number.)")
    for p, v in sorted(straddles.items())[:args.show]:
        print(f"       {p}  →  {sorted(v)}")
    if len(straddles) > args.show:
        print(f"       … and {len(straddles) - args.show} more")

    if args.emit:
        Path(args.emit).write_text(json.dumps({
            "schema": "q0-witness-read-dataflow/v1",
            "note": "CANDIDATES. Reachability through the filesystem, not proof "
                    "that a q0 moved. One hop only.",
            "hits": hits,
            "straddle_candidates": {p: sorted(v) for p, v in straddles.items()},
        }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"\n  written: {args.emit}")

    print("\n" + "=" * 72)
    print("Complements the import-cone classifiers; does not replace them.")
    print("Neither shape sees the other's route.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
