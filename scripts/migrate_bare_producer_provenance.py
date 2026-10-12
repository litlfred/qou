#!/usr/bin/env python3
"""Add producer provenance to the bare `computations/` producers (bean qou-4un2).

A "bare" producer writes its witness with `json.dump` / `write_text` and never
calls `WitnessBuilder`, so nothing stamps `scriptFile` / `commitSha` / `engine`.
The field on disk was added downstream, which is why RE-RUNNING one deletes it:
the `migrate(q0) batch*` sweep did exactly that to 17 witnesses on 2026-08-24.

WHAT THIS INSERTS

Immediately before the statement that writes the witness:

    import os as _os
    from qou_substrate.witness import WitnessBuilder as _WB
    <payload>.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        <payload>, script_path=__file__, engine=None, q0_anchor=False)

`stamp_staleness_metadata` is the corpus's own helper for "the filename is
non-standard and wrap_legacy().save() cannot be applied", which is precisely
this population. Two of those four lines exist for reasons worth stating:

* **the `setdefault`**, because the helper does NOT write `scriptFile` -- it
  stamps scriptHash / scriptCommitSha / commitSha / engine / computedAt /
  durationMs. The first pass of this migration omitted the line and therefore
  added staleness metadata to 282 producers while leaving every one of their
  witnesses still unable to name its producer. `setdefault` rather than `=`
  so an existing attribution is never silently rewritten: a regenerator such
  as `regenerate_y_lambda_orphans_conventionD.py` writes witnesses belonging
  to OTHER producers, and it is in this population.
* **`engine=None`**, the "keep what the payload already declares" sentinel
  added to the helper alongside this pass. Without it the helper's
  unconditional `payload["engine"] = engine` downgrades a producer's own value
  -- measured, `"sympy+mpmath"` -> `"python"` with `engineVersion` left reading
  `"sympy 1.14.0, mpmath 1.4.1"`, an internally contradictory witness produced
  by a pass whose whole purpose was better provenance.

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

TWO WAYS TO BUILD THE POPULATION, AND ONLY ONE OF THEM WORKS

The first pass of this migration built the population WITNESS-FIRST: walk every
`*.witness.json`, read its `scriptFile`, resolve that to a producer, keep the
ones that never call `WitnessBuilder`. That found 287 and it undercounts by
~48 %, because it can only ever see a producer that some witness NAMES:

  * a witness with NO provenance field has no `scriptFile` to resolve, so its
    producer is skipped -- and 248 of the 2842 witnesses (8.7 %) are in exactly
    that state. The scan is blindest to precisely the defect it hunts.
  * a witness whose `scriptFile` names the WRONG file sends the scan to the
    wrong producer. `free-neutron-decay.witness.json` names `derived_masses.py`,
    which only ever READS it; the real producer, `free-neutron-decay.py`, is a
    bare `json.dump` and was invisible to the whole first pass.
  * a witness naming a shim whose write is delegated (`per_irrep_pole_proton_h3`
    -> `per_irrep_pole_atom`) sends the scan to a file with no write at all.

WRITER-FIRST is the correct construction and is now the default: walk every
`computations/**/*.py`, keep the ones that contain a witness write the AST can
find and no `WitnessBuilder`. It asks "does this file write a witness without
stamping it", which is the actual question, and it does not depend on any field
that might be missing or wrong. It finds 260 producers the witness-first pass
never saw, disjoint from the 282 it migrated.

`--scan witness` is kept only to reproduce the first pass for comparison.

Usage:
    python3 scripts/migrate_bare_producer_provenance.py --dry-run
    python3 scripts/migrate_bare_producer_provenance.py --apply --limit 10
    python3 scripts/migrate_bare_producer_provenance.py --scan witness --dry-run
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

#: How to recognise a file this script has already touched, and whether it got
#: the `scriptFile` line. The first pass omitted that line -- see `apply_one` --
#: so a file with the first marker and not the second needs the upgrade.
STAMP_MARKER = "_WB.stamp_staleness_metadata("
SCRIPTFILE_MARKER = '_os.path.basename(__file__)'


def resolve_producer(witness_path: pathlib.Path, script_file: str):
    """Locate the producer named by a witness's `scriptFile`, sibling-first."""
    if not script_file:
        return None
    base = pathlib.Path(script_file).name
    sib = witness_path.parent / base
    if sib.exists():
        return sib
    cands = [c for c in COMP.rglob(base) if ("_deprecated" not in c.parts and "fsh-guts" not in c.parts)]
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
        cands = [c for c in COMP.rglob(mod + ".py") if ("_deprecated" not in c.parts and "fsh-guts" not in c.parts)]
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


def inline_dict_node(node: ast.AST):
    """The inline `Dict` a write call is dumping, through any wrappers.

    Mirrors `innermost_name`'s walk but returns the NODE rather than the
    sentinel, because hoisting needs the literal's own source span.
    """
    while True:
        if isinstance(node, ast.Dict):
            return node
        if isinstance(node, ast.BinOp):
            node = node.left
            continue
        if isinstance(node, ast.Call) and node.args:
            node = node.args[0]
            continue
        return None


def find_inline_writes(tree: ast.AST):
    """Every write statement whose payload is a dict literal at the write site.

    Returned newest-line-first so a caller rewriting them in order does not
    invalidate the line numbers of the ones it has not reached yet.
    """
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Expr) or not isinstance(node.value, ast.Call):
            continue
        f = node.value.func
        if not (isinstance(f, ast.Attribute) and f.attr in ("dump", "write_text")
                and node.value.args):
            continue
        d = inline_dict_node(node.value.args[0])
        if d is not None:
            out.append((node, d))
    return sorted(out, key=lambda x: x[0].lineno, reverse=True)


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


def payload_bindings(tree: ast.AST, name: str):
    """Every value expression bound to `name`, INCLUDING via tuple unpacking.

    Tuple unpacking is not a corner case here: `report, scanned, deprecated =
    {}, 0, 0` is a common idiom in the audit scripts, and a check that only
    looks at `Assign.targets[0]` sees a `Tuple` rather than a `Name` and
    reports the payload as never assigned. That produced two false "never
    bound" findings before this function existed.
    """
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id == name:
                    out.append((n.lineno, n.value))
                elif isinstance(t, ast.Tuple):
                    for i, el in enumerate(t.elts):
                        if isinstance(el, ast.Name) and el.id == name:
                            out.append((n.lineno,
                                        n.value.elts[i]
                                        if isinstance(n.value, ast.Tuple)
                                        and i < len(n.value.elts) else None))
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) \
                and n.target.id == name:
            out.append((n.lineno, n.value))
    return sorted(out, key=lambda x: x[0])


def payload_is_dict(tree: ast.AST, name: str, before_line: int) -> bool:
    """Whether the binding of `name` LIVE AT `before_line` is provably a dict.

    Nearest-preceding, not "any binding anywhere". One name is routinely bound
    to both shapes in one file -- the accumulator idiom

        out = []          # line 62,  a list built inside an earlier function
        ...
        out = {...}       # line 238, the witness itself
        json.dump(out, f) # line 270

    -- and 11 of the 13 list-bound payloads in this population look exactly like
    that. An "any binding is a dict" test passes them for the right reason by
    accident; it would equally pass the reverse order, where the live value at
    the write really is a list. Taking the last binding above the write answers
    the question actually being asked.

    THIS IS A CORRECTNESS GATE, NOT A TIDINESS ONE. `stamp_staleness_metadata`
    does `payload["scriptHash"] = ...`, so a non-dict payload raises TypeError
    AT RUN TIME -- `list indices must be integers or slices, not str`. Measured
    on this population: 13 producers bind the write payload to a LIST and 8 more
    to a string / bytes / opaque call, because a file that merely READS a
    witness passes a "mentions .witness.json" filter while its `write_text`
    actually emits markdown or a text report. Stamping those 21 would have
    broken 21 working scripts.

    Deliberately conservative: a payload assembled by a helper (`w =
    build_witness()`) is not provably a dict here and is reported rather than
    stamped. Under-reaching costs a follow-up; over-reaching costs a crash.
    """
    prior = [v for ln, v in payload_bindings(tree, name) if ln < before_line]
    return bool(prior) and isinstance(prior[-1], (ast.Dict, ast.DictComp))


def plan_one(path: pathlib.Path):
    raw = path.read_text(errors="ignore")
    src = code_only(raw)
    try:
        tree = ast.parse(raw)
    except SyntaxError as exc:
        return None, f"unparseable: {exc}"
    if STAMP_MARKER in src and SCRIPTFILE_MARKER not in src:
        # First-pass file: it has the stamp call but no `scriptFile` line.
        call = next((n for n in ast.walk(tree)
                     if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                     and n.func.attr == "stamp_staleness_metadata"), None)
        if call is None or not call.args or not isinstance(call.args[0], ast.Name):
            return None, "first-pass stamp present but its payload is not a plain name"
        stmt = next(n for n in ast.walk(tree)
                    if isinstance(n, ast.Expr) and n.value is call)
        return {
            "path": str(path.relative_to(ROOT)),
            "line": stmt.lineno,
            "payload": call.args[0].id,
            "q0": False,          # unused on the upgrade path
            "col": stmt.col_offset,
            "upgrade": True,
        }, None
    if "WitnessBuilder" in src:
        return None, "already uses WitnessBuilder"
    hit = find_write(tree)
    if hit == "inline":
        return None, ("payload is an inline dict literal at the write site — "
                      "needs binding to a name first, a different migration")
    if hit is None:
        return None, "no json.dump / write_text call found"
    stmt, payload = hit
    if not payload_is_dict(tree, payload, stmt.lineno):
        return None, (f"payload {payload!r} is not provably a dict — stamping a "
                      "non-dict raises TypeError at run time")
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
    if plan.get("upgrade"):
        # The file already carries this script's stamp from the first pass but
        # not the `scriptFile` line; insert only the missing line.
        block = [f"{pad}{plan['payload']}.setdefault("
                 f'"scriptFile", _os.path.basename(__file__))',
                 f"{pad}import os as _os  # noqa: E402 -- provenance stamp"]
        block.reverse()
        lines[idx:idx] = block
        path.write_text("\n".join(lines))
        return None
    block = [
        f"{pad}# Provenance stamp (bean qou-4un2): this producer writes its",
        f"{pad}# witness directly, so nothing else records which script made",
        f"{pad}# it -- and a re-run of an unstamped producer DELETES the",
        f"{pad}# scriptFile a downstream pass had added. {note}.",
        f"{pad}import os as _os  # noqa: E402 -- provenance stamp",
        f"{pad}from qou_substrate.witness import WitnessBuilder as _WB",
        # `stamp_staleness_metadata` does NOT write `scriptFile` -- it stamps
        # scriptHash / scriptCommitSha / commitSha / engine / computedAt /
        # durationMs (+ q0Anchor). So the field this bean is actually about has
        # to be set here, or the migration adds staleness metadata and still
        # leaves the witness unable to name its producer. Measured: the first
        # pass shipped exactly that gap on 282 files.
        #
        # `setdefault`, not `=`: filling a MISSING attribution is this bean's
        # goal, but overwriting an existing one would silently re-attribute a
        # regenerator's output (e.g. `regenerate_y_lambda_orphans_conventionD`
        # writes witnesses belonging to other producers) to the regenerator.
        # A wrong-but-deliberate `scriptFile` is a separate defect and is not
        # something a bulk pass should "fix" unverified.
        f"{pad}{plan['payload']}.setdefault("
        f'"scriptFile", _os.path.basename(__file__))',
        f"{pad}_WB.stamp_staleness_metadata(",
        f"{pad}    {plan['payload']}, script_path=__file__, engine=None, q0_anchor={anchor})",
    ]
    lines[idx:idx] = block
    path.write_text("\n".join(lines))
    return None


def population_writer_first() -> dict[str, None]:
    """Every `computations/**/*.py` that writes a witness without stamping it.

    This asks the actual question and depends on no witness field, so a missing
    or misattributed `scriptFile` cannot hide a producer from it. See the
    module docstring for the three ways the witness-first construction fails.
    """
    out: dict[str, None] = {}
    for p in sorted(COMP.rglob("*.py")):
        if ("_deprecated" in p.parts or "fsh-guts" in p.parts):
            continue
        raw = p.read_text(errors="ignore")
        src = code_only(raw)
        # A file already carrying THIS script's stamp but not its `scriptFile`
        # line is a first-pass file needing the upgrade, so it stays in scope
        # even though `WitnessBuilder` is present.
        needs_upgrade = (STAMP_MARKER in src
                         and SCRIPTFILE_MARKER not in src)
        # The `.witness.json` literal must be in CODE, not a comment: it is what
        # distinguishes a witness write from any other `json.dump` in the file.
        if not needs_upgrade and ("WitnessBuilder" in src
                                  or ".witness.json" not in src):
            continue
        try:
            tree = ast.parse(raw)
        except SyntaxError:
            continue
        if not needs_upgrade and find_write(tree) is None:
            continue
        out[str(p)] = None
    return out


def population_witness_first() -> dict[str, None]:
    """The original construction, kept only for comparison. Undercounts ~48 %."""
    out: dict[str, None] = {}
    for w in sorted(COMP.rglob("*.witness.json")):
        if ("_deprecated" in w.parts or "fsh-guts" in w.parts):
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
        out[str(p)] = None
    return out


def hoist_inline_dicts(path: pathlib.Path, check_only: bool = False):
    """Bind each inline witness dict to a name, then stamp it before the write.

        out.write_text(json.dumps({ ... }))                       # before

        _prov_payload_1 = { ... }                                 # after
        _prov_payload_1.setdefault("scriptFile", ...)
        _WB.stamp_staleness_metadata(_prov_payload_1, ...)
        out.write_text(json.dumps(_prov_payload_1))

    Returns (n_rewritten, error). This is the migration the insertion pass could
    not do: there is no variable at the write site to stamp, so the literal has
    to be given a name first -- a structural edit rather than an insertion,
    which is why these 27 files were held back rather than force-fitted.

    THE LITERAL'S SOURCE IS HOISTED VERBATIM, indentation and all. That looks
    wrong for a multi-line dict whose continuation lines keep their original
    columns, but Python's implicit line joining makes indentation inside
    brackets free-form, so the hoisted text parses to the same object. Verified
    per site rather than assumed: the new binding's value is compared to the
    original literal by `ast.dump`, and a mismatch aborts the file with nothing
    written.
    """
    src = path.read_text(errors="ignore")
    try:
        tree = ast.parse(src)
    except SyntaxError as exc:
        return 0, f"unparseable: {exc}"
    sites = find_inline_writes(tree)
    if not sites:
        return 0, None
    q0 = reaches_q0(code_only(src))
    lines = src.split("\n")
    originals = []

    for i, (stmt, dnode) in enumerate(sites):
        n = len(sites) - i                      # bottom-up, so number top-down
        var = f"_prov_payload_{n}" if len(sites) > 1 else "_prov_payload"
        line = lines[stmt.lineno - 1]
        pad = line[:len(line) - len(line.lstrip())]
        if stmt.col_offset != len(pad):
            # A compound one-liner (`with open(p) as f: json.dump({...}, f)`).
            # Replacing the statement's line range would take the `with` header
            # with it. Rare enough to report rather than guess at.
            return 0, (f"write at line {stmt.lineno} is inside a compound "
                       "one-liner; needs splitting by hand first")
        dict_src = ast.get_source_segment(src, dnode)
        stmt_src = ast.get_source_segment(src, stmt)
        if dict_src is None or stmt_src is None:
            return 0, f"no source segment for the write at line {stmt.lineno}"
        if stmt_src.count(dict_src) != 1:
            return 0, (f"the literal at line {stmt.lineno} is not uniquely "
                       "locatable inside its write statement")
        anchor = "None" if q0 else "False"
        note = ("resolve and stamp the q0 anchor" if q0
                else "no q0 in this producer's cone; stamp provenance only")
        block = [
            f"{pad}# Provenance stamp (bean qou-f1rs): the witness dict was built",
            f"{pad}# INLINE at the write below, so there was nothing to stamp. It",
            f"{pad}# is bound to a name here so this producer records which script",
            f"{pad}# wrote it -- a re-run of an unstamped producer DELETES the",
            f"{pad}# scriptFile a downstream pass had added. {note}.",
            f"{pad}import os as _os  # noqa: E402 -- provenance stamp",
            f"{pad}from qou_substrate.witness import WitnessBuilder as _WB",
            f"{pad}{var} = {dict_src}",
            f'{pad}{var}.setdefault("scriptFile", _os.path.basename(__file__))',
            f"{pad}_WB.stamp_staleness_metadata(",
            f"{pad}    {var}, script_path=__file__, engine=None, q0_anchor={anchor})",
            # `get_source_segment` returns the statement WITHOUT its leading
            # indentation, so splicing it back verbatim drops it to column 0
            # inside an indented block. Only the first line needs `pad`: any
            # continuation lines keep their original absolute columns, which is
            # legal because they are inside brackets. This is what made 25 of
            # the 27 files fail to re-parse on the first attempt -- and the two
            # that passed were module-level, where `pad` is empty, so a sample
            # of the successes would have shown nothing.
            *[(pad + ln if i == 0 else ln) for i, ln
              in enumerate(stmt_src.replace(dict_src, var).split("\n"))],
        ]
        lines[stmt.lineno - 1:stmt.end_lineno] = block
        originals.append((var, dnode))

    new_src = "\n".join(lines)
    try:
        new_tree = ast.parse(new_src)
    except SyntaxError as exc:
        return 0, f"rewrite does not parse: {exc}"

    # The hoist is faithful only if the bound value IS the original literal.
    bound = {}
    for node in ast.walk(new_tree):
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id.startswith("_prov_payload")):
            bound[node.targets[0].id] = node.value
    for var, dnode in originals:
        if var not in bound:
            return 0, f"{var} missing from the rewrite"
        if ast.dump(bound[var]) != ast.dump(dnode):
            return 0, f"{var} is not the original literal — hoist would change it"

    if not check_only:
        path.write_text(new_src)
    return len(sites), None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true", default=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", default="", help="apply only to paths containing this")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--scan", choices=("writer", "witness"), default="writer",
                    help="how to build the population; 'witness' reproduces the "
                         "first pass and undercounts (see module docstring)")
    ap.add_argument("--hoist-inline", action="store_true",
                    help="bean qou-f1rs: bind inline witness dicts to a name and "
                         "stamp them (the migration the insertion pass cannot do)")
    args = ap.parse_args()

    if args.hoist_inline:
        targets = sorted(
            p for p in population_writer_first()
            if find_inline_writes(ast.parse(pathlib.Path(p).read_text(errors="ignore")))
        )
        if args.only:
            targets = [t for t in targets if args.only in t]
        if args.limit:
            targets = targets[:args.limit]
        done = sites = 0
        failed = []
        for t in targets:
            n, err = hoist_inline_dicts(pathlib.Path(t), check_only=not args.apply)
            if err:
                failed.append((t, err))
            elif n:
                done += 1
                sites += n
        verb = "would rewrite" if not args.apply else "rewrote"
        print(f"  files with an inline witness dict : {len(targets)}")
        print(f"  {verb:<32}: {done}  ({sites} write sites)")
        print(f"  FAILED                            : {len(failed)}")
        for t, err in failed:
            print(f"      {pathlib.Path(t).name[:44]:<44} {err}")
        return 1 if failed and args.apply else 0

    producers = (population_witness_first() if args.scan == "witness"
                 else population_writer_first())

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

    # The q0 split covers FRESH plans only. An upgrade inserts the `scriptFile`
    # line and no `q0_anchor` kwarg at all, so its plan carries a placeholder
    # `q0: False` that is never emitted -- counting those made the reported
    # split 467/66 against a true tree state of 378/154, i.e. the summary
    # described the plan dict rather than the code it writes.
    fresh = [p for p in plans if not p.get("upgrade")]
    upgrades = len(plans) - len(fresh)
    q0_yes = sum(1 for p in fresh if p["q0"])
    print(f"  bare producers found        : {len(producers)}")
    print(f"  transformable               : {len(plans)}")
    print(f"    -> fresh stamp            : {len(fresh)}")
    print(f"       - q0_anchor=None (q0 seen) : {q0_yes}")
    print(f"       - q0_anchor=False          : {len(fresh) - q0_yes}")
    print(f"    -> scriptFile upgrade only: {upgrades}  (no q0_anchor written)")
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
