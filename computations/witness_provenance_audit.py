#!/usr/bin/env python3
# polynomial_q_not_applicable: static provenance audit, emits no numeric physics.
"""Does a witness's `scriptFile` actually WRITE that witness?

Owner directive: NO FLOAT64 — this is the provenance half of the same
discipline: a number is only as trustworthy as the claim about where it came
from.

## The defect

`scriptFile` is treated everywhere as "the producer": `run_pipeline.py`
regenerates through it, `producer_repad_sweep.py` attributes padding by it, and
the P30 triage in
`docs/audits/2026-08-07-producer-repadding-empirical-sweep.md` counted with it.
**Nothing checks it.**

Six `chi-*.witness.json` name `delta_lambda_empirical_tabulation.py`. That
script reads them as `chi_witness` *inputs* and never writes them — nor does
any other script in the corpus. Re-running the named producer therefore does
nothing at all, which is exactly what was measured: `rc=0`, no `scriptHash`
gained, not one value moved. A witness naming a real script is not evidence
that the script produces it.

## Three verdicts, and the middle one is the point

Writing is not statically decidable in general — a path can be built from
variables, a loop, a config. So this reports what it can prove and refuses to
guess:

| verdict | meaning |
|---|---|
| `WRITES` | a `WitnessBuilder` name matches the stem, **or** the filename provably reaches a write sink — literal, or an f-string matched as a pattern |
| `UNCONFIRMED` | the script mentions *some* witness, or builds one under a computed name — cannot confirm, cannot deny |
| `NOT_A_PRODUCER` | the script mentions **no witness at all** — the claim cannot be true |

## Hand-rolled writers: follow the path to the sink

`WitnessBuilder` is not the only way to write one. 250 producers assemble the
payload by hand, write it to an explicit path, and stamp the metadata
afterwards (`stamp_staleness_metadata`, 185 call sites). Recognising only the
builder left every one of those `UNCONFIRMED` — 466 of 2250.

So a filename is also `WRITES` when it can be traced from a literal to a write
sink. Sinks are asymmetric **on purpose**: `write_text` / `write_bytes` and
`open(…, "w"|"a"|"x")` count; `read_text` and a bare `open()` do not. That
asymmetry is the entire safeguard — `delta_lambda_empirical_tabulation.py`
*contains* `"chi-proton-h3.witness.json"`, but only ever hands it to a read, so
it stays `UNCONFIRMED` while the file it genuinely writes is confirmed. A
"mentions it" test cannot tell those apart; that is the error this tool exists
to not repeat, and a corpus case (not just a unit test) pins it.

Path idioms resolved, each with a paired negative test: `Path(x)`, `HERE / x`,
`os.path.join(…, x)`, `p.with_name(x)`, and any of those reached through a
variable (depth-limited). Together: **466 → 32 `UNCONFIRMED`**.

The upgrade can only move `UNCONFIRMED → WRITES`. It cannot manufacture a
`NOT_A_PRODUCER`, because that verdict is reached only when the source mentions
no witness at all — a condition finding *more* writes never creates. Measured
across all three extensions, `NOT_A_PRODUCER` held at the same three witnesses,
by name and not merely by count.

`UNCONFIRMED` is deliberately not folded into either neighbour. The `chi-*`
case is a filename that *appears* in the named script, so a "mentions it" test
would have called it a producer and reproduced the original error. Only
`NOT_A_PRODUCER` is asserted as wrong; `UNCONFIRMED` is asserted as unchecked,
which is a different and honest thing to say.

**Three times the rule was too aggressive, and each cost an order of
magnitude** — 324 → 189 → 28 → 3. Missing `WitnessBuilder.wrap_legacy` (229
call sites); treating an f-string name as unknowable rather than as a pattern;
and requiring the *concrete* filename when a script may write through a
computed path. Each intermediate was a plausible number, and each died on
reading one cited file. Hence the final rule's conservatism: absence is only
claimed when the script mentions no witness whatsoever.

## Why not just re-run and see

Because a re-run that writes nothing is indistinguishable from a producer whose
output happens to be unchanged — and that is the confusion this whole audit
arc keeps paying for. Static attribution answers "is this claim structurally
possible", which is the question `run_pipeline` needs before it decides a
witness is current.

## The three survivors, triaged

All three verified by hand; each has a different cause, and none is fixable by
re-running:

- **`kite_tail_reconciliation.witness.json`** — rename residue. The script
  writes `kite-tail-reconciliation` (hyphens) via `WitnessBuilder`, and the
  underscore-named file is a stale duplicate left behind by the rename. **Both
  are committed.** The tool is right to reject the claim: the named script
  produces the *other* file.
- **`psl27-irrep-verification.witness.json`** — no script in the corpus
  mentions it. A true orphan.
- **`sigma-all-evaluator.witness.json`** — its only producer,
  `build_sigma_all_evaluator_witness.py`, lives in `_deprecated/`. Orphaned by
  a deprecation.

None can be regenerated, and `run_pipeline` treats all three as current.
Deleting or re-attributing them is a corpus decision, not a tool fix, so this
records rather than acts.

## The 466 UNCONFIRMED, triaged — and why the obvious upgrade is unsafe

| | witnesses | shape |
|---:|---|---|
| **250** | no `WitnessBuilder` at all | hand-rolled `json.dump` / `write_text` |
| **197** | imports it, no resolvable constructor | `WitnessBuilder.stamp_staleness_metadata(...)` — 185 call sites |
| 15 | a builder exists, but no name matches | |
| 2 | name from a variable | |
| 2 | syntax error | |

The 197 are a **fourth** builder shape, found the same way as `wrap_legacy`:
`adjacent_vs_full_probe.py` assembles the payload by hand, writes it to
`Path(__file__).parent / "adjacent-vs-full-probe.witness.json"`, then calls
`stamp_staleness_metadata` for the metadata. They genuinely do produce their
witness, and the concrete filename is right there as a literal.

**The tempting upgrade — "literal filename present + the file writes something
⇒ WRITES" — is exactly the original bug.** `delta_lambda_empirical_tabulation`
contains the literal `"chi-proton-h3.witness.json"` *and* writes a witness of
its own; that rule would call it the producer of six witnesses it only reads,
which is the error this tool exists to catch. Upgrading these needs real
dataflow — the literal must reach a write, not merely coexist with one — so
they stay `UNCONFIRMED` until someone does that properly.

Usage:
    python3 computations/witness_provenance_audit.py
    python3 computations/witness_provenance_audit.py --strict     # exit 1 on NOT_A_PRODUCER
    python3 computations/witness_provenance_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import re
import json
import sys
from pathlib import Path

_DYNAMIC = "\x01re:"
_OPAQUE = "\x01opaque"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def _fstring_pattern(node: ast.JoinedStr) -> str:
    """An f-string is still a pattern: its literal segments pin the shape.

    `f"A-operator-extract-h{n}-{iface}"` becomes `^A\-operator\-extract\-h.+\-.+$`.
    Treating a parameterised name as unknowable instead put ~135 witnesses in
    NOT_A_PRODUCER on an earlier cut.
    """
    parts = [re.escape(v.value) if isinstance(v, ast.Constant)
             and isinstance(v.value, str) else None for v in node.values]
    return _DYNAMIC + "^" + "".join(p if p is not None else ".+" for p in parts) + "$"


def _matches(names: set[str], target: str) -> bool:
    if target in names:
        return True
    return any(n.startswith(_DYNAMIC) and re.match(n[len(_DYNAMIC):], target)
               for n in names)


_WRITE_METHODS = {"write_text", "write_bytes"}
_RESOLVE_DEPTH = 5


def _assignments(tree: ast.AST) -> dict:
    """Name -> every value ever assigned to it, module-wide.

    Scope is ignored deliberately: over-collecting can only widen what a path
    might denote, which risks a false WRITES on a name reused for two files —
    a real limitation, and the reason this never downgrades anything.
    """
    out: dict = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out.setdefault(t.id, []).append(n.value)
        elif isinstance(n, (ast.AnnAssign, ast.AugAssign)) and isinstance(n.target, ast.Name):
            if n.value is not None:
                out.setdefault(n.target.id, []).append(n.value)
    return out


def _resolve(node, assigns: dict, depth: int = 0):
    """Literal filenames (or patterns) this path expression may denote."""
    if depth > _RESOLVE_DEPTH or node is None:
        return
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        yield node.value
    elif isinstance(node, ast.JoinedStr):
        yield _fstring_pattern(node)
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        # HERE / "x.witness.json" — the basename is the right operand.
        yield from _resolve(node.right, assigns, depth + 1)
    elif isinstance(node, ast.Name):
        for v in assigns.get(node.id, []):
            yield from _resolve(v, assigns, depth + 1)
    elif isinstance(node, ast.Call):
        f = node.func
        fn = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
        if fn == "Path" and node.args:
            yield from _resolve(node.args[0], assigns, depth + 1)
        elif fn == "witness_path" and node.args:
            # _path_bridge.witness_path("x.witness.json", HERE) — this repo's
            # own resolver, 208 call sites. Basename is the first argument.
            yield from _resolve(node.args[0], assigns, depth + 1)
        elif fn == "with_name" and node.args:
            # script_path.with_name("x.witness.json") — the borromean cluster.
            yield from _resolve(node.args[0], assigns, depth + 1)
        elif fn == "join" and node.args:
            # os.path.join(dir, …, "x.witness.json") — basename is the LAST
            # argument, mirroring the `/` case above. The alpha_em probes are
            # written this way throughout; without it they read as non-writers.
            yield from _resolve(node.args[-1], assigns, depth + 1)


def written_filenames(tree: ast.AST) -> set:
    """Witness filenames that provably REACH a write in this module.

    This is the whole difference between producing a witness and mentioning
    one. `delta_lambda_empirical_tabulation` contains the literal
    "chi-proton-h3.witness.json" inside a dict it feeds to json.load; that
    literal reaches no write, so it is not collected here. A test pins it.

    Sinks are asymmetric on purpose: `write_text`/`write_bytes` and
    `open(..., "w")` count; `read_text` and `json.load` do not.
    """
    assigns = _assignments(tree)
    out: set = set()

    def collect(path_node):
        for lit in _resolve(path_node, assigns):
            if ".witness.json" in lit or lit.startswith(_DYNAMIC):
                out.add(lit)

    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if isinstance(f, ast.Attribute) and f.attr in _WRITE_METHODS:
            collect(f.value)                      # p.write_text(...)
        elif isinstance(f, ast.Attribute) and f.attr == "open":
            if _is_write_mode(n):
                collect(f.value)                  # p.open("w")
        elif getattr(f, "id", "") == "open" and n.args:
            if _is_write_mode(n, mode_index=1):
                collect(n.args[0])                # open(p, "w")
    return out


def _is_write_mode(call: ast.Call, mode_index: int = 0) -> bool:
    args = list(call.args)
    cand = args[mode_index] if len(args) > mode_index else None
    for kw in call.keywords:
        if kw.arg == "mode":
            cand = kw.value
    if cand is None:
        return False          # no mode given => "r"
    return isinstance(cand, ast.Constant) and isinstance(cand.value, str) \
        and any(c in cand.value for c in "wax")


def builder_names(tree: ast.AST) -> set[str]:
    """Witness stems this script constructs a WitnessBuilder for.

    Accepts `WitnessBuilder("stem")` and `WitnessBuilder(name="stem")`; a
    non-literal name is unknowable statically and is skipped, which pushes the
    witness to UNCONFIRMED rather than to a false NOT_A_PRODUCER.
    """
    out: set[str] = set()
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        # Two shapes construct a named witness:
        #   WitnessBuilder(...)                — direct
        #   WitnessBuilder.wrap_legacy(stem,…) — 229 call sites, and missing it
        #                                        put 300+ witnesses in
        #                                        NOT_A_PRODUCER on the first cut.
        if isinstance(f, ast.Attribute):
            owner = getattr(f.value, "id", "")
            if not (owner == "WitnessBuilder" and f.attr == "wrap_legacy"):
                continue
        elif getattr(f, "id", "") != "WitnessBuilder":
            continue
        cand = list(n.args[:1]) + [kw.value for kw in n.keywords if kw.arg == "name"]
        for c in cand:
            if isinstance(c, ast.Constant) and isinstance(c.value, str):
                out.add(c.value)
            elif isinstance(c, ast.JoinedStr):
                out.add(_fstring_pattern(c))
            else:
                out.add(_OPAQUE)   # name from a variable: unknowable either way
    return out


def classify(source: str, witness_filename: str) -> str:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return "UNCONFIRMED"
    stem = witness_filename[: -len(".witness.json")]
    names = builder_names(tree)
    if _matches(names, stem):
        return "WRITES"
    # A hand-rolled writer is still a writer: the payload is assembled by hand,
    # written to an explicit path, and the metadata stamped afterwards
    # (WitnessBuilder.stamp_staleness_metadata, 185 call sites). Confirming
    # those needs the filename to REACH a write, not merely appear.
    if _matches(written_filenames(tree), witness_filename):
        return "WRITES"
    if _OPAQUE in names:
        # The script builds a witness whose name is computed. Cannot confirm it
        # is this one; cannot assert it is not. That is what UNCONFIRMED is for.
        return "UNCONFIRMED"
    # Conservative: a script that mentions ".witness.json" AT ALL may be writing
    # this one through a path this resolver cannot follow — a loop over a table
    # of names, a config value, a helper that takes the stem as an argument.
    # `binding_canonical.py` is the live example: it constructs a WitnessBuilder
    # whose name is not a literal, so nothing here can pin it either way. Only a
    # script that never mentions a witness can be asserted not to produce one.
    return "UNCONFIRMED" if ".witness.json" in source else "NOT_A_PRODUCER"


# Producers that are not Python, and not under `computations/`. A witness may
# legitimately be written by a Rust binary or carry a Lean file as its
# provenance, and the Python index below can never resolve either — so before
# this, every such witness was SCRIPT_MISSING *by construction*, which asserts
# "the claim cannot be true" about a script that is sitting in the repo.
#
# Measured: 2 of the 5 SCRIPT_MISSING were this artefact —
# `joint_tower_sdp.rs` (tools/hecke-engine/src/bin/) and
# `DeuteronFirstOrderCluster.lean` (content/…/MassTheory/). The other 3 are
# real: those `.py` files exist nowhere in the tree.
#
# Resolved ones become UNCONFIRMED, never WRITES: `classify()` reads Python —
# WitnessBuilder names, write sinks — so it can neither confirm nor deny a
# `.rs`/`.lean` producer. UNCONFIRMED is exactly the audit's documented middle
# verdict for "cannot confirm, cannot deny", and claiming WRITES here would be
# the laundering this tool exists to catch. Bean qou-w9s3.
_NON_PY_PRODUCER_SUFFIXES = (".rs", ".lean")


def _find_non_py_producer(root: Path, name: str) -> Path | None:
    """Locate a non-Python producer anywhere in the tree, by basename."""
    if not name.endswith(_NON_PY_PRODUCER_SUFFIXES):
        return None
    skip = {".git", "node_modules", ".lake", "_deprecated", "__pycache__"}
    # sorted: `rglob` yields in os.scandir order, so an unsorted first-match
    # returns a filesystem-dependent answer. This one only feeds an
    # exists/does-not-exist decision (UNCONFIRMED vs SCRIPT_MISSING), so a
    # different pick does not change the verdict — but the returned path is
    # reported, and a report that varies by machine is not reproducible.
    # Bean qou-kcii.
    for cand in sorted(root.rglob(name)):
        if not skip & set(cand.parts):
            return cand
    return None


def scan(root: Path) -> list[dict]:
    comp = root / "computations"
    # Index EVERY candidate per basename, not one. This was
    #     {p.name: p for p in comp.rglob("*.py")}
    # — a last-wins dict over an unsorted rglob, so for a duplicated basename
    # the surviving entry was whichever copy the filesystem happened to yield
    # last. `classify()` then read THAT source and stamped the verdict, which
    # means the audit could grade a witness against a script that did not
    # produce it. `witness_provenance_audit.py` is itself one of the four
    # duplicated basenames (root + audits/, and per bean qou-2r42 those are two
    # different audits), so the tool was exposed to this on its own witness.
    # Bean qou-kcii.
    by_name: dict[str, list[Path]] = {}
    for p in sorted(comp.rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        by_name.setdefault(p.name, []).append(p)

    def _resolve_producer(name: str, witness: Path) -> tuple[Path | None, list[Path]]:
        """The producer for `witness`, preferring the copy beside it.

        Producers emit next to themselves, so the witness's own directory is
        the correct tie-break — not the root, and not scandir order. Returns
        (chosen, candidates); chosen is None only when the basename is
        genuinely ambiguous and no copy sits beside the witness.
        """
        cands = by_name.get(name, [])
        if len(cands) <= 1:
            return (cands[0] if cands else None), cands
        for c in cands:
            if c.parent == witness.parent:
                return c, cands
        if (comp / name) in cands:
            return comp / name, cands
        return None, cands
    out: list[dict] = []
    for w in sorted(comp.rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        sf = d.get("scriptFile")
        if not sf or sf.startswith("("):
            # No claim, or a prose annotation someone already triaged by hand.
            continue
        src_path, _cands = _resolve_producer(Path(sf).name, w)
        if src_path is None and len(_cands) > 1:
            out.append({"witness": w.relative_to(root).as_posix(), "scriptFile": sf,
                        "verdict": "AMBIGUOUS_PRODUCER",
                        "candidates": [c.relative_to(root).as_posix()
                                       for c in _cands],
                        "note": "basename resolves to several scripts and none "
                                "sits beside this witness; not graded rather "
                                "than graded against a guess"})
            continue
        if src_path is None:
            # A non-Python producer that EXISTS is not a missing script; this
            # tool simply cannot read it. See _find_non_py_producer.
            if _find_non_py_producer(root, Path(sf).name) is not None:
                out.append({"witness": w.relative_to(root).as_posix(),
                            "scriptFile": sf, "verdict": "UNCONFIRMED",
                            "note": "non-Python producer found in tree; "
                                    "not statically analysable by this audit"})
                continue
            out.append({"witness": w.relative_to(root).as_posix(), "scriptFile": sf,
                        "verdict": "SCRIPT_MISSING"})
            continue
        try:
            src = src_path.read_text(encoding="utf-8")
        except Exception:
            continue
        out.append({"witness": w.relative_to(root).as_posix(), "scriptFile": sf,
                    "verdict": classify(src, w.name)})
    return out


CASES = [
    ("builder positional", 'WitnessBuilder("chi-proton-h3")', "chi-proton-h3.witness.json", "WRITES"),
    ("builder keyword", 'WitnessBuilder(name="foo-bar", engine="python")', "foo-bar.witness.json", "WRITES"),
    ("wrap_legacy (229 call sites)", 'WitnessBuilder.wrap_legacy("foo-bar", payload)', "foo-bar.witness.json", "WRITES"),
    ("wrap_legacy for a different stem", 'WitnessBuilder.wrap_legacy("other", p)', "foo-bar.witness.json", "NOT_A_PRODUCER"),
    ("f-string name resolves as a pattern",
     'WitnessBuilder(f"A-operator-extract-h{n}-{iface}")',
     "A-operator-extract-h9-pn.witness.json", "WRITES"),
    ("f-string pattern that does NOT match",
     'WitnessBuilder(f"A-operator-extract-h{n}-{iface}")',
     "unrelated-thing.witness.json", "NOT_A_PRODUCER"),
    ("name from a variable: unknowable, so UNCONFIRMED",
     'WitnessBuilder(nm)', "anything.witness.json", "UNCONFIRMED"),
    ("unrelated attribute call", 'x.some_method("foo-bar")', "foo-bar.witness.json", "NOT_A_PRODUCER"),
    # The exact shape that fooled the original triage: the filename is present,
    # but only as an input the script READS.
    ("reads it as an input", '{"chi_witness": "chi-proton-h3.witness.json"}',
     "chi-proton-h3.witness.json", "UNCONFIRMED"),
    # (A "hand-rolled write" case sat here asserting UNCONFIRMED, back when the
    # tool could not follow a path to its sink. Same source now appears below
    # as "write_text on a literal path", expecting WRITES.)
    ("never mentions a witness at all", 'x = 1\n', "orphan.witness.json", "NOT_A_PRODUCER"),
    ("templated path via a helper", 'OUT = f"chi-{atom}-h{n}.witness.json"',
     "chi-deuteron-h6.witness.json", "UNCONFIRMED"),
    ("builder for a DIFFERENT witness, no other mention",
     'WitnessBuilder("other")', "orphan.witness.json", "NOT_A_PRODUCER"),
    ("non-literal keyword name: also UNCONFIRMED, never asserted absent",
     'WitnessBuilder(name=nm)', "orphan.witness.json", "UNCONFIRMED"),
    ("syntax error degrades to unconfirmed", 'def (:', "x.witness.json", "UNCONFIRMED"),
    # --- dataflow: the literal must REACH a write ---
    ("write_text on a literal path",
     'Path("out.witness.json").write_text(j)', "out.witness.json", "WRITES"),
    ("HERE / literal, via a variable",
     'out = HERE / "adjacent-vs-full-probe.witness.json"\nout.write_text(j)',
     "adjacent-vs-full-probe.witness.json", "WRITES"),
    ("open(path, 'w')",
     'p = HERE / "o.witness.json"\nwith open(p, "w") as f:\n    json.dump(d, f)',
     "o.witness.json", "WRITES"),
    ("f-string path reaching a write",
     '(HERE / f"chi-{atom}-h{n}.witness.json").write_text(j)',
     "chi-deuteron-h6.witness.json", "WRITES"),
    # THE REGRESSION. This is the shape the whole tool exists to reject: the
    # literal is present, the script writes a witness of its OWN, but the
    # literal only ever reaches a read.
    ("literal reaches only a read, while the file writes something else",
     'cfg = {"chi_witness": "chi-proton-h3.witness.json"}\n'
     'd = json.loads((HERE / cfg["chi_witness"]).read_text())\n'
     'out = HERE / "delta-lambda-empirical-tabulation.witness.json"\n'
     'out.write_text(j)',
     "chi-proton-h3.witness.json", "UNCONFIRMED"),
    ("os.path.join reaching open(…, 'w')",
     'out = os.path.join(_here(), "alpha-em-b5-assembly.witness.json")\n'
     'with open(out, "w") as f:\n    json.dump(w, f)',
     "alpha-em-b5-assembly.witness.json", "WRITES"),
    ("os.path.join reaching only a read",
     'p = os.path.join(_here(), "upstream.witness.json")\n'
     'd = json.load(open(p))\n'
     'out = os.path.join(_here(), "mine.witness.json")\n'
     'open(out, "w").write(j)',
     "upstream.witness.json", "UNCONFIRMED"),
    ("with_name reaching a write",
     'out = script_path.with_name("borromean-qzeil-fixedq.witness.json")\n'
     'out.write_text(j)',
     "borromean-qzeil-fixedq.witness.json", "WRITES"),
    ("with_name reaching only a read",
     'src = script_path.with_name("upstream.witness.json")\n'
     'd = json.loads(src.read_text())\n'
     'script_path.with_name("mine.witness.json").write_text(j)',
     "upstream.witness.json", "UNCONFIRMED"),
    ("witness_path reaching a write",
     'CHI = _pb.witness_path("chi-deuteron-h6.witness.json", HERE)\n'
     'CHI.write_text(json.dumps(p))',
     "chi-deuteron-h6.witness.json", "WRITES"),
    ("witness_path reaching only a read",
     'src = _pb.witness_path("chi-proton-h3.witness.json", HERE)\n'
     'd = json.loads(src.read_text())\n'
     '_pb.witness_path("mine.witness.json", HERE).write_text(j)',
     "chi-proton-h3.witness.json", "UNCONFIRMED"),
    ("read_text is not a write sink",
     'Path("x.witness.json").read_text()', "x.witness.json", "UNCONFIRMED"),
    ("open without a mode is a read",
     'open(HERE / "x.witness.json")', "x.witness.json", "UNCONFIRMED"),
]


def self_test() -> int:
    fails = 0
    for label, src, wf, want in CASES:
        got = classify(src, wf)
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any witness names a script that cannot produce it")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--list", choices=["NOT_A_PRODUCER", "UNCONFIRMED", "SCRIPT_MISSING", "WRITES"])
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    rows = scan(Path(a.root).resolve())
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print(f"witness-provenance: {len(rows)} witnesses carry a scriptFile claim\n")
    for k in ("WRITES", "UNCONFIRMED", "NOT_A_PRODUCER", "SCRIPT_MISSING"):
        print(f"  {k:<16} {counts.get(k, 0)}")
    if a.list:
        print(f"\n--- {a.list} ---")
        for r in rows:
            if r["verdict"] == a.list:
                print(f"  {r['witness']}  -> {r['scriptFile']}")
    bad = counts.get("NOT_A_PRODUCER", 0)
    if bad:
        print(f"\n{bad} witness(es) name a script that provably cannot produce them.")
        print("Re-running those regenerates nothing; run_pipeline still treats them as current.")
    return 1 if (a.strict and bad) else 0


if __name__ == "__main__":
    raise SystemExit(main())
