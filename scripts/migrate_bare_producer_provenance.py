#!/usr/bin/env python3
"""Add producer provenance to the bare `computations/` producers (bean qou-4un2).

A "bare" producer writes its witness with `json.dump` / `write_text` and never
calls `WitnessBuilder`, so nothing stamps `scriptFile` / `commitSha` / `engine`.
The field on disk was added downstream, which is why RE-RUNNING one deletes it:
the `migrate(q0) batch*` sweep did exactly that to 17 witnesses on 2026-08-24.

WHAT THIS INSERTS

Immediately before the statement that writes the witness:

    WitnessBuilder.stamp_staleness_metadata(
        <payload>, script_path=__file__, q0_anchor=False)

plus the import if absent. `stamp_staleness_metadata` is the corpus's own
helper for "the filename is non-standard and wrap_legacy().save() cannot be
applied", which is precisely this population.

WHY AST AND NOT A REGEX

The payload is not always a bare name at the write site. Three shapes occur:

    out.write_text(json.dumps(witness, indent=2))
    json.dump(witness, f, indent=2)
    out.write_text(json.dumps(_serialize(witness), indent=2))   # <-- wrapped

The third is why a textual pass is wrong: stamping the SERIALIZED value would
either stamp a different object or push the stamp through a converter that was
not written to expect it. This walks to the innermost `Name` and stamps the
dict itself, before serialization.

WHY `q0_anchor` IS A PER-PRODUCER DECISION

`stamp_staleness_metadata` resolves and stamps an anchor unless told not to,
and the resolver has no "no anchor" outcome. Measured over this population:
196 of 287 producers do not reach q0 even one import hop out, so stamping
unconditionally would add ~196 INERT anchors -- byte-identical to load-bearing
ones, and roughly doubling the class PR #5884 reported. Hence `q0_anchor=False`
(added in this branch's first commit) for the ones that provably do not.

The asymmetry matters and the default leans safe: an inert anchor is a
LABELLING problem, while a missing anchor on a genuinely q0-dependent witness
is the ambiguity the field exists to prevent. So anything this script cannot
show to be q0-free gets `q0_anchor=None` (resolve and stamp), including every
producer whose q0 use is only reachable further out than the one import hop
measured here.

Usage:
    python3 scripts/migrate_bare_producer_provenance.py --dry-run
    python3 scripts/migrate_bare_producer_provenance.py --apply --limit 10
"""
from __future__ import annotations

import argparse
import ast
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "computations"
sys.path.insert(0, str(COMP / "audits"))
sys.path.insert(0, str(COMP))

from _source_normalise import code_only  # noqa: E402

#: Names whose presence (in code, not comments) means the producer reaches q0.
Q_MARKERS = ("q_parameter", "Q_50_DIGIT", "qou_substrate.constants", "q_at", "Q_MP")

STAMP_IMPORT = (
    "from qou_substrate.witness import WitnessBuilder  "
    "# noqa: E402 -- provenance stamp, bean qou-4un2"
)


def resolve_producer(witness_path: pathlib.Path, script_file: str):
    """Locate the producer named by a witness's `scriptFile`, sibling-first."""
    if not script_file:
        return None
    base = pathlib.Path(script_file).name
    sib = witness_path.parent / base
    if sib.exists():
        return sib
    cands = [c for c in COMP.rglob(base) if "_deprecated" not in c.parts]
    return cands[0] if len(cands) == 1 else None


def _imports(src: str):
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            out += [a.name.split(".")[0] for a in n.names]
        elif isinstance(n, ast.ImportFrom) and n.module:
            out.append(n.module.split(".")[0])
    return out


_MOD_SRC: dict[str, str] = {}


def _module_source(mod: str) -> str:
    if mod not in _MOD_SRC:
        cands = [c for c in COMP.rglob(mod + ".py") if "_deprecated" not in c.parts]
        _MOD_SRC[mod] = code_only(cands[0].read_text(errors="ignore")) if len(cands) == 1 else ""
    return _MOD_SRC[mod]


def reaches_q0(src: str) -> bool:
    """Source plus ONE import hop. Deliberately conservative: anything this
    cannot rule out is treated as q0-dependent, so the anchor is stamped."""
    if any(m in src for m in Q_MARKERS):
        return True
    return any(any(k in _module_source(m) for k in Q_MARKERS) for m in set(_imports(src)))


#: Returned instead of a name when the payload has no variable to stamp.
INLINE_DICT = object()


def innermost_name(node: ast.AST):
    """The `Name` a write call is ultimately dumping, through any wrappers.

    Returns `INLINE_DICT` when the payload is built inline at the write site,
    which is a different migration and is reported separately rather than
    silently lumped in with parse failures.
    """
    while True:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, (ast.Dict, ast.DictComp)):
            return INLINE_DICT
        # `write_text(json.dumps(w, ...) + "\n")` — the trailing-newline idiom.
        # The payload hides in the LEFT operand; without this the whole file
        # reads as having no write call at all. 29% of the population was
        # skipped for this and the inline-dict case together, so the two are
        # worth separating rather than reporting as one opaque failure.
        if isinstance(node, ast.BinOp):
            node = node.left
            continue
        if isinstance(node, ast.Call) and node.args:
            node = node.args[0]
            continue
        return None


def find_write(tree: ast.AST):
    """(stmt, payload) for the statement writing the witness JSON.

    `payload` is a variable name, or `INLINE_DICT` when the dict is built at
    the write site. Returns None when no write call is present at all.
    """
    best = None
    inline_only = False
    for node in ast.walk(tree):
        if not isinstance(node, ast.Expr) or not isinstance(node.value, ast.Call):
            continue
        call = node.value
        f = call.func
        is_dump = isinstance(f, ast.Attribute) and f.attr == "dump" and call.args
        is_wt = isinstance(f, ast.Attribute) and f.attr == "write_text" and call.args
        if not (is_dump or is_wt):
            continue
        payload = innermost_name(call.args[0])
        if payload is INLINE_DICT:
            inline_only = True
            continue
        if payload:
            best = (node, payload)       # last write wins: the final emit
    if best is None and inline_only:
        return "inline"
    return best


def plan_one(path: pathlib.Path):
    raw = path.read_text(errors="ignore")
    src = code_only(raw)
    if "WitnessBuilder" in src:
        return None, "already uses WitnessBuilder"
    try:
        tree = ast.parse(raw)
    except SyntaxError as exc:
        return None, f"unparseable: {exc}"
    hit = find_write(tree)
    if hit == "inline":
        return None, ("payload is an inline dict literal at the write site — "
                      "needs binding to a name first, a different migration")
    if hit is None:
        return None, "no json.dump / write_text call found"
    stmt, payload = hit
    return {
        "path": str(path.relative_to(ROOT)),
        "line": stmt.lineno,
        "payload": payload,
        "q0": reaches_q0(src),
        "col": stmt.col_offset,
    }, None


def apply_one(plan: dict) -> str | None:
    """Insert the import + stamp call. Returns an error string, or None on ok.

    The import goes at the stamp site, not the module top. Two reasons:

      * these producers have no `_path_bridge` preamble and no uniform import
        block, so "after the last import" is not a well-defined line in a file
        that may put imports inside a `if __name__` guard;
      * a local import cannot change module-import order or introduce a cycle
        in a file that never imported this package before.

    `qou_substrate` resolves without any sys.path bootstrap in this repo (309
    in-repo importers rely on that), so no path manipulation is emitted.
    """
    path = ROOT / plan["path"]
    lines = path.read_text(errors="ignore").split("\n")
    idx = plan["line"] - 1                 # ast lineno is 1-based
    if idx >= len(lines):
        return f"line {plan['line']} past EOF"
    # Indentation comes from the SOURCE LINE, not from the node's col_offset.
    # They differ whenever the write sits in a compound one-liner:
    #
    #     with open(out, "w") as f: json.dump(w, f, indent=2)
    #
    # there the `json.dump` Expr has col_offset 29 -- its position after the
    # colon -- so padding to it produced a 29-space block against a 4-space
    # line and the file stopped parsing. Caught by the post-apply syntax check
    # on 1 of 281 files; the line's own leading whitespace is what "the
    # indentation here" actually means, and it is right for the simple case
    # too. Inserting before a compound line still places the stamp before the
    # `with`, which is correct: the payload is already built by then.
    line = lines[idx]
    pad = line[:len(line) - len(line.lstrip())]
    anchor = "None" if plan["q0"] else "False"
    note = ("resolve and stamp the q0 anchor" if plan["q0"]
            else "no q0 in this producer's cone; stamp provenance only")
    block = [
        f"{pad}# Provenance stamp (bean qou-4un2): this producer writes its",
        f"{pad}# witness directly, so nothing else records which script made",
        f"{pad}# it -- and a re-run of an unstamped producer DELETES the",
        f"{pad}# scriptFile a downstream pass had added. {note}.",
        f"{pad}from qou_substrate.witness import WitnessBuilder as _WB",
        f"{pad}_WB.stamp_staleness_metadata(",
        f"{pad}    {plan['payload']}, script_path=__file__, q0_anchor={anchor})",
    ]
    lines[idx:idx] = block
    path.write_text("\n".join(lines))
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true", default=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", default="", help="apply only to paths containing this")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    producers: dict[str, None] = {}
    for w in sorted(COMP.rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        try:
            d = json.loads(w.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        p = resolve_producer(w, d.get("scriptFile"))
        if p is None:
            continue
        if "WitnessBuilder" in code_only(p.read_text(errors="ignore")):
            continue
        producers[str(p)] = None

    plans, skips = [], []
    for p in sorted(producers):
        plan, why = plan_one(pathlib.Path(p))
        (plans if plan else skips).append(plan or (p, why))

    if args.only:
        plans = [p for p in plans if args.only in p["path"]]
    if args.limit:
        plans = plans[:args.limit]

    if args.json:
        print(json.dumps({"plans": plans, "skips": [list(s) for s in skips]}, indent=2))
        return 0

    if args.apply:
        # Deepest line first per file is unnecessary (one insert per file), but
        # sorting by path keeps the applied order deterministic and reviewable.
        done, failed = 0, []
        for p in sorted(plans, key=lambda x: x["path"]):
            err = apply_one(p)
            if err:
                failed.append((p["path"], err))
            else:
                done += 1
        print(f"  applied : {done}")
        for path, err in failed:
            print(f"  FAILED  : {path}  {err}")
        return 1 if failed else 0

    q0_yes = sum(1 for p in plans if p["q0"])
    print(f"  bare producers found        : {len(producers)}")
    print(f"  transformable               : {len(plans)}")
    print(f"    -> stamp anchor (q0 seen) : {q0_yes}")
    print(f"    -> q0_anchor=False        : {len(plans) - q0_yes}")
    print(f"  NOT transformable           : {len(skips)}")
    from collections import Counter
    for why, n in Counter(w for _, w in skips).most_common():
        print(f"      {n:>3}  {why}")
    if skips:
        print("\n  first few skipped:")
        for p, why in skips[:5]:
            print(f"      {pathlib.Path(p).name[:52]:<52} {why[:40]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
