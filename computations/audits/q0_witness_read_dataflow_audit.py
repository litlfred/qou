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

MEASURED — AND EVERY HEADLINE NUMBER HERE WAS AN ARTIFACT FIRST
    Scored against a 13-agent read-only adjudication, on the 55 producers agents
    independently classified as this route:

        direct reads (filename in the producer)      44 / 55
        + transitive (read is in an imported module) 46 / 55   (84 %)
        fires on adjudicated-independent             14 / 246  (5.7 %)

    The corpus counts: **542** producers read a pinned witness directly (559
    proton / 268 muon / 12 comparison), **53** read more than one pin (layer-
    straddle candidates), and **239** more inherit one through an imported
    module — 115 of those via `wedderburn_jones_markov`, the accessor AGENTS.md
    §q₀-anchor names as the straddle trap.

    **Three of those numbers were wrong by an order of magnitude first**, each
    for the same reason, and the pattern is more useful than any of them:

      1. Counting `qou_substrate/witness.py` gave 400 spurious straddles. It
         knows both pins because it STAMPS the anchor field.
      2. Counting `_precision.py` gave 195 of 198 muon reaches. It has no q₀ at
         all — its DOCSTRING mentions `wedderburn_jones_markov`.
      3. Counting `q_parameter` in the transitive pass gave **1117** instead of
         239. It is the q₀ accessor, so its importers are the import-cone
         classifier's job, not this one.

    **A shared module's q₀ knowledge is infrastructure for its importers, not
    evidence about them.** Any count here is dominated by the exclusion list
    until that is applied, so quote no number from this file without it.

    **And the fix for (2) caused a blind spot.** Discounting string-constant
    evidence as prose also discounted `"q-pinning-50-digit.witness.json"` — a
    FILENAME, which is this route exactly. That is why the motivating case
    (`qbeta_dladder_coupled_qsqrt3_recurrence_probe`, whose imported module
    reads the pin witness at line 111) stayed missed through two revisions. A
    filter aimed at prose cannot be shaped like "is it a string".

THE LIMIT THAT NO SCAN REMOVES
    Of the 9 route-b cases still missed, several read witnesses that are
    entirely q₀-DERIVED while containing no q₀: `atom-chi-rust-*.witness.json`
    carry 50-dps χ values computed at a pin the file never records. Nothing
    recoverable from the artifact says which pin, because the pin is not in it.

    That is the whole reason `q0Anchor` exists as a declared field. A detector
    can find the read; only the producer can say what it was reading at.

READ-ONLY
    Emits a report and, with `--emit`, a JSON list. Writes no witness, edits no
    manifest, runs no producer.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent

sys.path.insert(0, str(HERE))
from q0_producer_pin_classifier import strip_main_block, classify  # noqa: E402

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


def local_import_index() -> dict[str, Path]:
    """module basename -> path, for the repo's flat-ish import namespace."""
    idx: dict[str, Path] = {}
    for root in (COMPUTE_DIR, REPO / "tools"):
        if not root.is_dir():
            continue
        for p in root.rglob("*.py"):
            if SKIP_DIRS & set(p.parts):
                continue
            idx.setdefault(p.stem, p)
    return idx


# `witness.py` STAMPS the q0Anchor field and so names pinned witnesses without
# evaluating anything; every producer imports WitnessBuilder. Counting it made
# an earlier version of this analysis report 400 spurious straddles.
INFRA_MODULES = {"witness", "_precision", "witness_base", "_path_bridge"}


def imported_modules(py: Path, idx: dict[str, Path]) -> list[Path]:
    try:
        tree = ast.parse(py.read_text(encoding="utf-8", errors="replace"))
    except (SyntaxError, OSError, ValueError):
        return []
    mods: set[str] = set()
    for node in ast.walk(ast.Module(body=strip_main_block(tree), type_ignores=[])):
        if isinstance(node, ast.Import):
            for a in node.names:
                mods.add(a.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            mods.add(node.module.split(".")[-1])
            mods.add(node.module.split(".")[0])
    return [idx[m] for m in sorted(mods)
            if m in idx and m not in INFRA_MODULES]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--emit", type=str, default=None)
    ap.add_argument("--show", type=int, default=15)
    ap.add_argument("--transitive", action="store_true",
                    help="also report producers whose IMPORTED MODULE does the "
                         "reading — the third route, invisible to a filename "
                         "scan and to an import-cone pin check alike")
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
    # SPLIT THE STRADDLES, because the raw count over-claims.
    # A producer that reads two differently-pinned witnesses ON PURPOSE is a
    # cross-anchor comparison, which the owner ruling of 2026-08-08 (bean
    # qou-pin2) protects explicitly: "explicit comparison probes are OK ... and
    # must not be fixed". Measured on this tree, 29 of 53 carry such a signal,
    # so quoting 53 as a defect count would be wrong by more than half.
    #
    # The signal is deliberately weak-but-cheap (a `compare` in prose, an
    # explicit muon accessor, a pins dict, both literals). It is a TRIAGE
    # ORDER, not a verdict: a `silent` producer may still be a legitimate
    # comparison whose author never said so, and a `deliberate` one may still
    # combine its two pins inside a single number, which is the thing actually
    # forbidden. Only a read settles either.
    _CMP = re.compile(
        r"\b(compare|comparison|cross[- _]?anchor|both pins|anchor.?dependence)\b",
        re.I)

    def _deliberate(rel: str) -> list[str]:
        f = REPO / rel
        try:
            src = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return []
        sig = []
        if "q_muon_at" in src or "Q_MUON" in src:
            sig.append("muon-accessor")
        if _CMP.search(src):
            sig.append("compare-word")
        if re.search(r"(ANCHORS|PINS)\s*=\s*\{", src):
            sig.append("pins-dict")
        if MUON_PREFIX in src and PROTON_PREFIX in src:
            sig.append("both-literals")
        return sig

    delib, silent = {}, []
    for p in sorted(straddles):
        sig = _deliberate(p)
        (delib.setdefault(p, sig) if sig else silent.append(p))
    print(f"     ├─ deliberate comparison (protected, qou-pin2) : {len(delib)}")
    print(f"     └─ SILENT — no comparison signal in source     : {len(silent)}")
    for p in silent[:args.show]:
        print(f"          {p}  →  {sorted(straddles[p])}")
    if len(silent) > args.show:
        print(f"          … and {len(silent) - args.show} more")

    transitive = []
    if args.transitive:
        midx = local_import_index()
        cone_owned: dict[Path, bool] = {}
        direct = set(by_producer)
        for py in sorted(COMPUTE_DIR.rglob("*.py")):
            if SKIP_DIRS & set(py.parts):
                continue
            rel = str(py.relative_to(REPO))
            if rel in direct:
                continue          # already caught directly; nothing new to say
            seen = {py}
            frontier = [py]
            found = None
            for _ in range(3):
                nxt = []
                for cur in frontier:
                    for mod in imported_modules(cur, midx):
                        if mod in seen:
                            continue
                        seen.add(mod)
                        nxt.append(mod)
                        # A module the IMPORT-CONE classifier already owns is
                        # not this route. `q_parameter` reads the pin witness,
                        # but any producer importing it is caught by
                        # q0_producer_pin_classifier — reporting it here is
                        # double-counting, and it dominated: without this gate
                        # the count reads 1117, almost all `via q_parameter`.
                        # Third artifact of exactly this shape in this analysis
                        # (see witness.py and _precision.py above); the pattern
                        # is that a shared module's q0 knowledge is INFRASTRUCTURE
                        # for its importers, not evidence about them.
                        if mod not in cone_owned:
                            # Own it only on IMPORT-SHAPED evidence. classify()
                            # also fires on the artifact NAME
                            # ("q-pinning-50-digit.witness.json"), which is
                            # precisely this route — skipping on it would hide
                            # the very case this pass exists for. Measured: with
                            # the naive `!= "none"` gate, the motivating miss
                            # (qbeta_dladder_coupled_qsqrt3_recurrence_probe,
                            # whose imported module reads the pin witness at
                            # line 111) stayed missed.
                            _pin, _ev = classify(mod)
                            cone_owned[mod] = _pin != "none" and any(
                                "import" in e or e.startswith(".")
                                for e in _ev)
                        if cone_owned[mod]:
                            continue
                        for name in witness_names_read(mod):
                            for wp in widx.get(name, []):
                                if wp not in pin_cache:
                                    pin_cache[wp] = witness_pin(wp)
                                pin, _how = pin_cache[wp]
                                if pin:
                                    found = (str(mod.relative_to(REPO)),
                                             str(wp.relative_to(REPO)), pin)
                                    break
                            if found:
                                break
                        if found:
                            break
                    if found:
                        break
                if found or not nxt:
                    break
                frontier = nxt
            if found:
                transitive.append({"producer": rel, "via_module": found[0],
                                   "reads": found[1], "pin": found[2]})

        print(f"\n  TRANSITIVE — the read happens in an IMPORTED module : "
              f"{len(transitive)}")
        print("     (the third route: no filename in the producer, and the")
        print("      imported module's pin arrives through ITS filesystem read,")
        print("      so an import-cone PIN check does not see it either.)")
        for t in transitive[:args.show]:
            print(f"       {t['producer']}")
            print(f"           via {t['via_module']}  →  {t['pin']}")
        if len(transitive) > args.show:
            print(f"       … and {len(transitive) - args.show} more")

    if args.emit:
        Path(args.emit).write_text(json.dumps({
            "schema": "q0-witness-read-dataflow/v1",
            "note": "CANDIDATES. Reachability through the filesystem, not proof "
                    "that a q0 moved. One hop only.",
            "hits": hits,
            "straddle_candidates": {p: sorted(v) for p, v in straddles.items()},
            "straddle_deliberate": delib,
            "straddle_silent": silent,
            "transitive": transitive,
        }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"\n  written: {args.emit}")

    print("\n" + "=" * 72)
    print("Complements the import-cone classifiers; does not replace them.")
    print("Neither shape sees the other's route.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
