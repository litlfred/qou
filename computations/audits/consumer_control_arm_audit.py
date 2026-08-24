#!/usr/bin/env python3
# polynomial_q_not_applicable: static source/artifact audit, not a q-series compute.
"""Find Python consumers that read a convention-C / muon-pinned witness ON PURPOSE.

WHY. The `qou-q0zk` drain has a tail of candidate convention-C witnesses. A
mechanical drain that reclassifies a witness and repoints its consumers **will
break working controls**, and no witness-level test can see it:

    THE CONTROL ARM IS A CONSUMER, NOT A WITNESS.

Worked instance, established in PR #5616. `computations/h4_markov_weights_closed_form.py`
reads the top-level convention-C, muon-pinned `alpha-k-jones-markov-h4.witness.json`
and looks exactly like a stale-frame defect. It is not. It hardcodes the published
`z` and the five published weights, evaluates its symbolic closed forms at that
`(q0, z)` to demonstrate they reproduce the published record, and then evaluates
at the proton anchor separately. Repointing or deleting its input breaks a
working cross-check.

The prior agent's error is the reason this exists: the intersection test was run
at the WITNESS layer -- candidate witnesses against the fingerprint detector's
control arms, intersection genuinely empty -- and concluded there were no control
arms in scope. The layer was wrong, not the arithmetic.

HOW IT IS DETECTED, and why not by name.
-----------------------------------------
`XCHECK_Z` / `XCHECK_WEIGHTS` is one SPELLING of a control arm's reference values.
Keying on it would be entry fourteen in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`, which catalogues thirteen
detector generations that each failed by keying on a form rather than a fact.

So this keys on the FACT: a control arm has copied numbers OUT OF the artifact it
reads INTO its own source, because that is what "reproduce the published record"
requires. That is checkable against the bytes of both files and is invariant
under every renaming.

    A1  TRANSCRIPTION (primary, name-free).  A high-precision decimal literal in
        the consumer's own code whose exact value also appears in a stale-frame
        witness the consumer READS AND DOES NOT WRITE.

    A2  SPECIFICITY (primary, name-free).  A transcribed value that occurs in at
        most SPECIFICITY_MAX witnesses corpus-wide is SPECIFIC -- it identifies
        that artifact. One occurring in hundreds is a shared physical constant
        (m_e, hbar-c, a q0 pin) and says nothing about provenance. Measured: this
        is what separates the known positive's five weights from `M_E =
        mp.mpf("0.51099895069")`, which matched 148 witnesses.

    A3  DUAL ANCHOR (corroborating, NAME-BASED, never decisive).  The consumer
        also reaches the canonical proton anchor, i.e. it evaluates twice. Stated
        separately and never used to promote a verdict, precisely because it is
        the kind of signal the taxonomy says goes blind.

WHAT THIS CANNOT SEE -- read before quoting its counts.
--------------------------------------------------------
  * A control arm that reads its reference value AT RUN TIME instead of
    transcribing it is INVISIBLE here. This is not hypothetical: PR #5616's own
    edit moved `published_q0` in the known positive from a transcription to a
    run-time read of the witness. Had it moved `XCHECK_Z` and `XCHECK_WEIGHTS`
    too, this detector would report nothing. The honest statement of the output
    is "N consumers transcribe foreign stale-frame values", NEVER "there are N
    control arms".
  * Python only. A control arm in TypeScript, Lean or shell is invisible.
  * Witness names are resolved by basename. 165 stems are duplicated in this tree
    (bean `qou-kcii`), so a bare filename can name two files with different
    payloads; every resolution is emitted so an ambiguous one is visible rather
    than silently picked.
  * The fingerprints are decimal prefixes of z_C and the muon q0. A stale-frame
    witness that serialises neither is not in the candidate set at all.

Arithmetic: `decimal.Decimal` end to end. Literals are recovered as SOURCE TEXT
from a pre-split line index and witnesses are parsed with `parse_float=Decimal`,
so no float64 exists anywhere in the comparison path.

Usage:
    python3 -u computations/audits/consumer_control_arm_audit.py
    python3 -u computations/audits/consumer_control_arm_audit.py --selftest
    python3 -u computations/audits/consumer_control_arm_audit.py --witness
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SKIP = (".git", ".claude", "_deprecated", "node_modules", "__pycache__", ".lake")

# Decimal PREFIXES of the two stale-frame fingerprints. Prefixes rather than full
# values because the corpus serialises each at several precisions.
Z_C_PREFIX = "0.4993203340"          # Markov parameter, convention C
MUON_Q0_PREFIX = "1.109978595"       # the ideal/CAL-2 (muon) pin

# A literal needs this many significant digits to be a plausible transcription.
# Below it the corpus is full of tolerances (1e-12), small rationals and counts.
MIN_SIG_DIGITS = 10

# A transcribed value in more than this many witnesses is a shared constant, not
# a fingerprint of the artifact being reproduced.
SPECIFICITY_MAX = 3

# Calls that WRITE. A witness path reaching one of these is the module's own
# output, so a literal it shares with that file was put there BY this module --
# the transcription arrow points the wrong way and the pair must be dropped.
WRITE_METHODS = {"write_text", "write_bytes", "dump", "save", "emit",
                 "write_json", "write"}

# Witness-emitting facade calls. These take the witness STEM ("b-over-a"), never
# the filename, so a detector keyed on ".witness.json" strings cannot see the
# write at all -- it is the taxonomy's own failure mode, one layer down.
# Measured: `b_over_a_evaluator.py` emits via
# `WitnessBuilder.wrap_legacy("b-over-a", ...).save()` and additionally carries a
# DEAD `out = HERE / "b-over-a.witness.json"` assignment, so the only live
# evidence of the write is the stem. It was reported as a foreign transcriber of
# its own output until this was added. 235 `wrap_legacy` call sites in tree.
#
# `witness_path` is deliberately NOT in this set. It looks like a witness facade
# and is the most common one in the tree (324 sites), but `_path_bridge.witness_path`
# RESOLVES a path and is overwhelmingly used for READS --
# `json.load(open(witness_path("q-pinning-50-digit.witness.json", HERE)))`.
# Including it suppressed 300+ pairs and would have made this audit blind to the
# exact class it exists to find: a consumer reading a stale-frame artifact.
WITNESS_BUILDER_CALLS = {"wrap_legacy", "write_witness", "emit_witness",
                         "build_witness", "WitnessBuilder"}

# A3 only. Name-based by nature; reported, never decisive.
CANONICAL_ANCHOR_NAMES = {
    "Q_50_DIGIT_STR", "q_at", "q_parameter", "qou_substrate", "constants",
    "Q_MP", "proton", "PROTON",
}

SELF_WITNESS_NAME = "consumer-control-arm-audit.witness.json"
KNOWN_POSITIVE_CONSUMER = "computations/h4_markov_weights_closed_form.py"
KNOWN_POSITIVE_WITNESS = "computations/alpha-k-jones-markov-h4.witness.json"


# ---------------------------------------------------------------- decimals
def _sig_digits(d: Decimal) -> int:
    digits = list(d.as_tuple().digits)
    while digits and digits[0] == 0:
        digits.pop(0)
    while digits and digits[-1] == 0:
        digits.pop()
    return len(digits)


def _as_decimal(value) -> Decimal | None:
    """Exact Decimal for a JSON scalar or a source-literal string. Never float."""
    if isinstance(value, bool):
        return None
    if isinstance(value, Decimal):
        return value
    if isinstance(value, int):
        return Decimal(value)
    if isinstance(value, float):
        # Reached only if a caller bypasses parse_float=Decimal. repr() is the
        # shortest round-trip decimal, so this is a normalisation, not arithmetic.
        try:
            return Decimal(repr(value))
        except InvalidOperation:
            return None
    if isinstance(value, str):
        s = value.strip().rstrip("Ll")
        if not s or len(s) > 80:
            return None
        try:
            return Decimal(s)
        except InvalidOperation:
            return None
    return None


def _norm(d: Decimal) -> str:
    return str(d.normalize())


# ---------------------------------------------------------------- witnesses
def witness_values(raw: str) -> set[str]:
    """Every scalar in the witness with >= MIN_SIG_DIGITS, as normalised text."""
    out: set[str] = set()
    try:
        doc = json.loads(raw, parse_float=Decimal, parse_int=Decimal)
    except Exception:  # noqa: BLE001
        return out
    stack = [doc]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
        else:
            d = _as_decimal(node)
            if d is not None and _sig_digits(d) >= MIN_SIG_DIGITS:
                out.add(_norm(d))
    return out


def build_witness_index():
    """path -> (frame_tag, value_set), plus a basename index and a value census."""
    raw_by_path: dict[Path, str] = {}
    for p in sorted(REPO.rglob("*.witness.json")):
        if any(x in p.parts for x in SKIP):
            continue
        # SELF-EXCLUDE THIS AUDIT'S OWN OUTPUT. It records every transcribed
        # value verbatim, so each run adds itself to the specificity census: the
        # known positive's weights went 2 -> 3 witnesses the first time the
        # witness was committed. At SPECIFICITY_MAX = 3 one more such artifact
        # tips them to `common` and the CONTROL-ARM verdict disappears with no
        # error -- a detector that goes quiet by writing down what it found.
        # Same hazard as SELF_OUTPUT_PREFIX in `compute-author` §5.1.
        if p.name == SELF_WITNESS_NAME:
            continue
        try:
            raw_by_path[p] = p.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue

    values = {p: witness_values(r) for p, r in raw_by_path.items()}

    frame: dict[Path, str] = {}
    for p, r in raw_by_path.items():
        tag = ""
        if Z_C_PREFIX in r:
            tag += "C"
        if MUON_Q0_PREFIX in r:
            tag += "M"
        frame[p] = tag

    by_base: dict[str, list[Path]] = defaultdict(list)
    for p in raw_by_path:
        by_base[p.name].append(p)

    # How many witnesses carry each value -- the specificity census (A2).
    census: Counter[str] = Counter()
    for s in values.values():
        census.update(s)

    return values, frame, by_base, census


# ---------------------------------------------------------------- consumers
def _docstring_constant_ids(tree: ast.AST) -> set[int]:
    out: set[int] = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.FunctionDef,
                                 ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        body = getattr(node, "body", None)
        if body and isinstance(body[0], ast.Expr) \
                and isinstance(body[0].value, ast.Constant) \
                and isinstance(body[0].value.value, str):
            out.add(id(body[0].value))
    return out


def _segment(lines: list[str], node: ast.AST) -> str | None:
    """The exact source text of `node`, in O(1).

    `ast.get_source_segment` re-splits the whole file on every call, which is
    quadratic over a module with many literals. Measured: it alone took the
    corpus scan past five minutes; indexing a pre-split line list is ~40x faster.
    """
    lo, hi = getattr(node, "lineno", None), getattr(node, "end_lineno", None)
    if lo is None or hi is None or hi > len(lines):
        return None
    if lo == hi:
        return lines[lo - 1][node.col_offset:node.end_col_offset]
    return None  # a multi-line literal is never a bare decimal


def source_literals(tree: ast.AST, src: str) -> dict[str, int]:
    """normalised decimal -> line, for high-precision literals in CODE.

    The value is recovered from the SOURCE TEXT rather than from the parsed
    constant, so a float literal never becomes a Python float on this path.
    Docstrings are excluded: a number quoted in prose is not a value the module
    computes with.
    """
    docs = _docstring_constant_ids(tree)
    lines = src.split("\n")
    out: dict[str, int] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or id(node) in docs:
            continue
        v = node.value
        if isinstance(v, bool) or not isinstance(v, (int, float, str)):
            continue
        if isinstance(v, str) and (len(v) > 80 or not v.strip()):
            continue
        seg = _segment(lines, node)
        d = _as_decimal(seg.strip().strip("\"'")) if seg is not None else None
        if d is None:
            d = _as_decimal(v)
        if d is not None and _sig_digits(d) >= MIN_SIG_DIGITS:
            out.setdefault(_norm(d), node.lineno)
    return out


def _basename_of(value: str, by_base) -> str | None:
    """The witness basename `value` names, whether spelled as a filename or a stem.

    Both spellings are live in this tree: `"alpha-k-jones-markov-h4.witness.json"`
    and the bare stem `"b-over-a"` handed to a WitnessBuilder facade. A stem is
    only accepted when `<stem>.witness.json` is an actual basename in the corpus,
    so this cannot promote arbitrary strings.
    """
    if not value or len(value) > 200:
        return None
    if value.startswith(("-", ".", "*")):
        return None
    if value.endswith(".witness.json"):
        return value.split("/")[-1]
    cand = value.split("/")[-1] + ".witness.json"
    return cand if cand in by_base else None


def _witness_name_strings(tree: ast.AST, by_base) -> set[str]:
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            base = _basename_of(node.value, by_base)
            if base:
                out.add(node.value)
    return out


def _bindings(tree: ast.AST, by_base) -> dict[str, set[str]]:
    """variable name -> witness names assigned into it (one hop, either spelling)."""
    inv: dict[str, set[str]] = defaultdict(set)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        names = {c.value for c in ast.walk(node.value)
                 if isinstance(c, ast.Constant) and isinstance(c.value, str)
                 and _basename_of(c.value, by_base)}
        if not names:
            continue
        for t in node.targets:
            if isinstance(t, ast.Name):
                inv[t.id] |= names
    return inv


def written_witness_names(tree: ast.AST, by_base) -> set[str]:
    """Witness-name strings this module WRITES.

    Two call shapes, and the second is the one a receiver-only check misses:
    `out.write_text(...)`, and `with open(path, "w") as f: json.dump(doc, f)`,
    where the path never touches the write call at all -- the MODE argument to
    `open` is the only evidence. Measured: without the `open` shape, two
    self-writing probes were reported as foreign transcribers.
    """
    inv = _bindings(tree, by_base)

    def names_reachable(node: ast.AST) -> set[str]:
        found: set[str] = set()
        for c in ast.walk(node):
            if isinstance(c, ast.Constant) and isinstance(c.value, str):
                if _basename_of(c.value, by_base):
                    found.add(c.value)
            elif isinstance(c, ast.Name):
                found |= inv.get(c.id, set())
        return found

    out: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else \
            (fn.id if isinstance(fn, ast.Name) else None)
        if name == "open":
            mode = ""
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                mode = str(node.args[1].value)
            for kw in node.keywords:
                if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                    mode = str(kw.value.value)
            if any(ch in mode for ch in "wax") and node.args:
                out |= names_reachable(node.args[0])
        elif name in WITNESS_BUILDER_CALLS:
            # The stem is a positional argument to the facade; the path is built
            # inside the library and never appears in this module.
            for arg in list(node.args) + [k.value for k in node.keywords]:
                out |= names_reachable(arg)
        elif name in WRITE_METHODS:
            if isinstance(fn, ast.Attribute):
                out |= names_reachable(fn.value)
            for arg in list(node.args) + [k.value for k in node.keywords]:
                out |= names_reachable(arg)
    return out


def references_canonical_anchor(tree: ast.AST) -> bool:
    """A3 -- name-based, corroborating only, never promotes a verdict."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in CANONICAL_ANCHOR_NAMES:
            return True
        if isinstance(node, ast.Attribute) and node.attr in CANONICAL_ANCHOR_NAMES:
            return True
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", None) or ""
            parts = set(mod.split(".")) | {a.name.split(".")[0] for a in node.names}
            if parts & CANONICAL_ANCHOR_NAMES:
                return True
    return False


# ---------------------------------------------------------------- scan
def scan():
    values, frame, by_base, census = build_witness_index()
    edges = []          # one per (consumer, resolved stale-frame witness) pair
    c_reads = []        # every foreign READ of a convention-C witness
    stats = {
        "witnesses_scanned": len(values),
        "witnesses_frame_C": sum(1 for t in frame.values() if "C" in t),
        "witnesses_frame_muon": sum(1 for t in frame.values() if "M" in t),
        "witnesses_stale_frame": sum(1 for t in frame.values() if t),
        "duplicated_witness_basenames": sum(1 for v in by_base.values() if len(v) > 1),
        "python_files_scanned": 0,
        "python_files_naming_a_witness": 0,
        "self_written_pairs_dropped": 0,
        "unresolvable_name_references": 0,
        "ambiguous_name_references": 0,
    }

    self_path = Path(__file__).resolve()
    for path in sorted(REPO.rglob("*.py")):
        if any(x in path.parts for x in SKIP):
            continue
        # Self-exclude. This module names the known positive's witness as a
        # string constant, so it reads as a foreign consumer of a convention-C
        # artifact -- of itself. Bean `qou-a6yh` names the cost directly: "a
        # detector that flags its own control arm trains the reader to ignore
        # it."
        if path.resolve() == self_path:
            continue
        try:
            src = path.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        stats["python_files_scanned"] += 1
        # Cheap prefilter: a module that never spells ".witness.json" cannot
        # produce an edge, and parsing it costs more than reading it.
        if ".witness.json" not in src:
            continue
        try:
            tree = ast.parse(src)
        except Exception:  # noqa: BLE001
            continue

        names = _witness_name_strings(tree, by_base)
        if not names:
            continue
        stats["python_files_naming_a_witness"] += 1

        written_names = written_witness_names(tree, by_base)
        # Resolve WRITES to PATHS first. A module can spell one artifact two ways
        # -- "b-over-a.witness.json" at the write site and
        # "computations/b-over-a.witness.json" in its header -- and excluding by
        # spelling then lets the second spelling through as a foreign read.
        # Measured: that is exactly how `b_over_a_evaluator.py` was reported as a
        # foreign transcriber of its own output.
        written_paths: set[Path] = set()
        for nm in written_names:
            b = _basename_of(nm, by_base)
            if b:
                written_paths.update(by_base.get(b, []))

        literals = source_literals(tree, src)
        dual_anchor = references_canonical_anchor(tree)

        for nm in sorted(names):
            base = _basename_of(nm, by_base)
            resolved = by_base.get(base, []) if base else []
            if not resolved:
                stats["unresolvable_name_references"] += 1
                continue
            if len(resolved) > 1:
                stats["ambiguous_name_references"] += 1
            for wpath in resolved:
                if not frame[wpath]:
                    continue
                if wpath in written_paths:
                    stats["self_written_pairs_dropped"] += 1
                    continue
                shared = set(literals) & values[wpath]
                if "C" in frame[wpath]:
                    c_reads.append({
                        "consumer": str(path.relative_to(REPO)),
                        "witness": str(wpath.relative_to(REPO)),
                        "transcribes": bool(shared),
                        "dual_anchor_reference": dual_anchor,
                    })
                if not shared:
                    continue
                specific = sorted(v for v in shared if census[v] <= SPECIFICITY_MAX)
                common = sorted(v for v in shared if census[v] > SPECIFICITY_MAX)
                # WHICH frame is the consumer deliberately on? The witness tag
                # says what the ARTIFACT carries; it does not say which axis the
                # consumer actually depends on, and a drain can get the two
                # wrong independently. Split the evidence:
                #   z_C_transcribed   -- the convention constant is IN THE
                #                        CONSUMER'S SOURCE, so a convention fix
                #                        breaks it directly.
                #   muon_transcribed  -- likewise for the muon pin.
                #   payload_transcribed -- values that are neither, i.e. results
                #                        the consumer reproduces. These inherit
                #                        whatever frame the artifact was computed
                #                        at, and the source does not record which.
                z_c = sorted(v for v in shared if v.startswith(Z_C_PREFIX))
                muon = sorted(v for v in shared if v.startswith(MUON_Q0_PREFIX))
                payload = sorted(set(shared) - set(z_c) - set(muon))
                frame_evidence = {
                    "witness_carries": frame[wpath],
                    "z_C_transcribed": bool(z_c),
                    "muon_q0_transcribed": bool(muon),
                    "payload_transcribed": len(payload),
                    "deliberate_on": (
                        ("C" if z_c else "") + ("M" if muon else "")
                    ) or "inherited-only",
                }
                edges.append({
                    "consumer": str(path.relative_to(REPO)),
                    "witness": str(wpath.relative_to(REPO)),
                    "witness_frame": frame[wpath],
                    "name_ambiguous": len(resolved) > 1,
                    "specific_values": specific,
                    "common_values": common,
                    "census": {v: census[v] for v in sorted(shared)},
                    "lines": {v: literals[v] for v in sorted(shared)},
                    "dual_anchor_reference": dual_anchor,
                    "frame_evidence": frame_evidence,
                    "verdict": "CONTROL-ARM" if specific else "SHARED-CONSTANT-ONLY",
                })

    # dedupe identical (consumer, witness) pairs produced by two spellings
    seen, deduped = set(), []
    for e in edges:
        key = (e["consumer"], e["witness"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(e)

    seen_c, c_ded = set(), []
    for r in c_reads:
        key = (r["consumer"], r["witness"])
        if key in seen_c:
            continue
        seen_c.add(key)
        c_ded.append(r)
    stats["convention_C_foreign_read_edges"] = len(c_ded)
    stats["convention_C_consumers"] = len({r["consumer"] for r in c_ded})
    return deduped, stats, c_ded


# ---------------------------------------------------------------- output
def _print_report(edges, stats, c_reads) -> None:
    print("=" * 78)
    print("consumer-side convention-C / muon control-arm audit")
    print("=" * 78)
    for k, v in stats.items():
        print(f"  {k:34s} {v}")

    arms = [e for e in edges if e["verdict"] == "CONTROL-ARM"]
    shared = [e for e in edges if e["verdict"] != "CONTROL-ARM"]
    print(f"\n  foreign-transcription edges              {len(edges)}")
    print(f"    CONTROL-ARM (>=1 specific value)       {len(arms)}"
          f"   consumers: {len({e['consumer'] for e in arms})}")
    print(f"    shared-constant only                   {len(shared)}"
          f"   consumers: {len({e['consumer'] for e in shared})}")

    print("\n" + "-" * 78)
    print("CONTROL ARMS -- a drain MUST NOT repoint or delete these inputs")
    print("-" * 78)
    for e in arms:
        print(f"  {e['consumer']}")
        print(f"      reads   {e['witness']}  [frame {e['witness_frame']}]"
              f"{'  (AMBIGUOUS NAME)' if e['name_ambiguous'] else ''}")
        print(f"      transcribes {len(e['specific_values'])} specific value(s) "
              f"from it:")
        for v in e["specific_values"][:8]:
            print(f"          {v}   (line {e['lines'][v]}, "
                  f"in {e['census'][v]} witness(es) corpus-wide)")
        if e["common_values"]:
            print(f"      also shares {len(e['common_values'])} shared constant(s): "
                  f"{[(v, e['census'][v]) for v in e['common_values'][:3]]}")
        fe = e["frame_evidence"]
        print(f"      frame the consumer is DELIBERATELY on: {fe['deliberate_on']}"
              f"   (artifact carries {fe['witness_carries']})")
        print(f"          z_C in consumer source     {fe['z_C_transcribed']}")
        print(f"          muon q0 in consumer source {fe['muon_q0_transcribed']}")
        print(f"          payload values reproduced  {fe['payload_transcribed']}"
              f"  (frame INHERITED from the artifact, not stated in the source)")
        print(f"      dual-anchor reference (A3, name-based, not decisive): "
              f"{e['dual_anchor_reference']}")

    print("\n" + "-" * 78)
    print("SHARED-CONSTANT ONLY -- the match is a pin / m_e / hbar-c, not a")
    print("transcription. NOT evidence of a control arm, and NOT evidence")
    print("against one. These need the ordinary per-file drain judgement.")
    print("-" * 78)
    for e in shared:
        vals = [(v, e["census"][v]) for v in e["common_values"][:2]]
        print(f"  {e['consumer']}")
        print(f"      reads {e['witness']} [{e['witness_frame']}]  shares {vals}")

    print("\n" + "-" * 78)
    print("DRAIN SCOPE -- every foreign READ of a convention-C witness.")
    print("This is the population a qou-q0zk drain touches. A row marked")
    print("transcribes=False is NOT cleared: it only means this detector")
    print("has nothing to say about it, so it needs a hand verdict.")
    print("-" * 78)
    if not c_reads:
        print("  (none)")
    for r in sorted(c_reads, key=lambda x: (x["witness"], x["consumer"])):
        mark = "TRANSCRIBES" if r["transcribes"] else "unmeasured "
        print(f"  [{mark}] {r['consumer']}")
        print(f"                reads {r['witness']}"
              f"   dual-anchor={r['dual_anchor_reference']}")

    print("\n" + "=" * 78)
    print("SCOPE. This reports transcription, not control arms. A control arm")
    print("that reads its reference at run time is invisible here -- PR #5616")
    print("made exactly that change to one field of the known positive. Treat")
    print("the non-CONTROL-ARM population as UNMEASURED, not clear.")
    print("=" * 78)


def _write_witness(edges, stats, c_reads) -> Path:
    doc = {
        "compute": "consumer_control_arm_audit",
        "description": (
            "Python consumers that transcribe values out of a convention-C or "
            "muon-pinned witness they read but do not write. Such a consumer is a "
            "deliberate control arm: it reproduces a published record at that "
            "frame, so a qou-q0zk drain that repoints its input breaks a working "
            "cross-check. The control arm is a CONSUMER, not a witness, so no "
            "witness-level classification can see it."
        ),
        "status": "audit",
        "bean": "qou-okkz",
        "arithmetic": (
            "decimal.Decimal end to end; source literals recovered as text via "
            "a pre-split line index and witnesses parsed with parse_float=Decimal, "
            "so no float64 exists on the comparison path"
        ),
        "parameters": {
            "z_C_prefix": Z_C_PREFIX,
            "muon_q0_prefix": MUON_Q0_PREFIX,
            "min_significant_digits": MIN_SIG_DIGITS,
            "specificity_max_witnesses": SPECIFICITY_MAX,
        },
        "counts": stats,
        "control_arms": [e for e in edges if e["verdict"] == "CONTROL-ARM"],
        "convention_C_foreign_reads": c_reads,
        "shared_constant_only": [e for e in edges if e["verdict"] != "CONTROL-ARM"],
        "known_blind_spots": [
            "a control arm that reads its reference value at run time instead of "
            "transcribing it (PR #5616 made this change to published_q0 in the "
            "known positive itself)",
            "control arms outside Python (TypeScript, Lean, shell)",
            "witness names resolved by basename; duplicated stems (bean qou-kcii) "
            "are flagged via name_ambiguous but not adjudicated",
            "a stale-frame witness serialising neither fingerprint is not in the "
            "candidate set at all",
        ],
        "how_to_use": (
            "Before draining a qou-q0zk candidate, check whether any consumer here "
            "reads it. A CONTROL-ARM edge is a stop: leave the artifact where it "
            "is. Everything else still needs the ordinary per-file verdict -- this "
            "audit narrows the drain, it does not clear it."
        ),
    }
    out = HERE / SELF_WITNESS_NAME
    out.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true",
                    help="exit 1 unless the known positive is detected")
    ap.add_argument("--witness", action="store_true",
                    help="write consumer-control-arm-audit.witness.json")
    args = ap.parse_args(argv)

    edges, stats, c_reads = scan()

    if args.selftest:
        hit = [e for e in edges
               if e["consumer"] == KNOWN_POSITIVE_CONSUMER
               and e["witness"] == KNOWN_POSITIVE_WITNESS
               and e["verdict"] == "CONTROL-ARM"]
        if not hit:
            print("SELFTEST FAIL: the known positive was not detected.")
            print(f"  expected {KNOWN_POSITIVE_CONSUMER}")
            print(f"        -> {KNOWN_POSITIVE_WITNESS}  verdict CONTROL-ARM")
            print("  A scan that cannot find the case it was built from is "
                  "measuring itself, not the corpus.")
            return 1
        e = hit[0]
        print("SELFTEST PASS: known positive detected.")
        print(f"  {e['consumer']}")
        print(f"    -> {e['witness']} [frame {e['witness_frame']}]")
        print(f"    {len(e['specific_values'])} specific transcribed value(s): "
              f"{e['specific_values'][:6]}")
        return 0

    _print_report(edges, stats, c_reads)
    if args.witness:
        out = _write_witness(edges, stats, c_reads)
        print(f"\nwrote {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
