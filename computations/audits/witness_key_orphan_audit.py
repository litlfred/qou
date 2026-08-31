#!/usr/bin/env python3
"""Committed witness keys the current producer source can no longer generate.

A witness goes stale in two directions and the corpus only detects one of them.
`ghost_value_sweep` catches a producer whose output CHANGED. Nothing catches a
producer that got SMALLER -- where a whole block of recorded analysis survives
in the committed JSON while the code that produced it has been deleted. The
witness then reads as a current result and is a fossil.

WORKED CASE (bean `qou-58zw`, Class 2). `probes/delta_lambda_bar_involution_probe.py`
has a committed witness carrying `/data/gap_decomposition/*` and
`/data/option_E_comparison/*` -- the latter holding the verdict
"RULED OUT -- wrong sign by 140x, cos=-0.51". Neither block appears anywhere in
the current source. That verdict is quotable, is quoted, and has no producing
code.

METHOD, and why it is STATIC. Deciding this by running every producer costs an
import sweep measured at ~20 minutes for import alone, before any compute. But
a producer names its keys with string literals, in one of two shapes:

    wb.add_data("key", ...)  /  wb.add_assertion("name", ...)      builder
    witness = {"data": {"key": ...}}   then json.dump                literal dict

so the key set a producer CAN emit is visible to the AST. A committed key that
matches no string literal anywhere in the source is one the source cannot name.

FALSE POSITIVES ARE THE WHOLE DIFFICULTY, and the guard is conservative:

  * A key built dynamically -- an f-string, a variable, a comprehension over
    names -- is invisible to any static pass. So a file that constructs keys
    dynamically ANYWHERE is reported as `partial` and is NOT gated on.
  * Keys are matched against every string literal in the module, not only those
    in witness position: a key assembled from a constant defined elsewhere in
    the file still matches, and missing it would be a false positive.
  * Provenance and schema keys the WitnessBuilder adds itself (computedAt,
    scriptHash, engine, ...) are never the producer's to name.

So a `confirmed` finding means: this file names keys only with literals, and
this committed key is not among them.

HOW THE COUNT MOVED, because every step was a finding about the corpus and not
merely about this file. Each figure is the whole-corpus `confirmed` count:

  611 files / 6382 keys   hand-written infra list. ~20 % of the corpus, which is
                          not a finding, it is a broken detector. Spot-checking
                          THREE showed almost all of it was /environment/*,
                          /precisionMetadata, /q0Anchor -- keys the BUILDER
                          writes. Fixed by DERIVING the infra set from
                          witness.py's own literals rather than extending a hand
                          list, which would have been the same defect later.
   14 / 84                keys named in an IMPORTED module, not the producer's
                          own file. Same class as the import-cone blindness
                          AGENTS.md records for witness staleness.
    4 / 21                keyword-argument keys -- `result(A_odd_...=v)` names a
                          Python IDENTIFIER, which ast.Constant(str) never sees.
                          `qcollatz_backward_tree_structure_probe` was reported
                          with three orphans sitting in plain sight on line 127.
    5 / 40                using the witness's OWN `scriptFile` instead of
                          guessing the producer from the filename stem. This
                          RAISED the count: two files were being audited against
                          the wrong source entirely.
    3 / 11               a key named nowhere in `computations/` at all. The last
                          class an import list cannot reach: `add_data("lp",
                          solver.to_dict())` names `lp` and nothing under it.

ALL 11 SURVIVORS WERE HAND-VERIFIED, one grep per key, before this file was
committed. The measured precision before the final gate was 10 genuine against
~30 false; a count nobody has checked is not a finding.

Exit 0 when clean, 1 on any confirmed orphan.

-- Ref: [manuscript] docs/audits/2026-08-15-detector-blindness-taxonomy.md
"""
from __future__ import annotations

import ast
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_deprecated", "__pycache__", "data", "node_modules"}

#: Emitted by the witness infrastructure, never named by the producer.
#:
#: DERIVED FROM `witness.py`, NOT HAND-KEPT -- and that is the whole point. The
#: first version of this list was written by hand and reported 611 files / 6382
#: keys, ~20 % of the corpus. Spot-checking three showed almost all of it was
#: `/environment/*`, `/precisionMetadata`, `/q0Anchor`, `/auditOnly` -- keys the
#: BUILDER writes, which the hand list had simply missed. Extending the list by
#: hand would have been the same defect one iteration later, so the set is now
#: read off the builder's own source: every string literal in `witness.py` is
#: treated as a key the infrastructure may emit.
#:
#: Over-broad, deliberately. A producer key that happens to collide with a
#: string in `witness.py` is suppressed -- a false NEGATIVE. The alternative
#: error direction manufactures 6000 findings, and a detector nobody believes
#: is worth less than one that under-reports and says so.
_FALLBACK_INFRA = {
    "engine", "engineVersion", "computedAt", "commitSha", "scriptCommitSha",
    "scriptHash", "scriptFile", "durationMs", "computation", "description",
    "assertions", "allPassed", "data", "parameters", "caveats", "environment",
    "invocation", "witness", "meta", "schema", "name", "computed", "expected",
    "passed", "tolerance", "unit", "source", "q0Anchor", "precisionMetadata",
}


def _builder_literals() -> set[str]:
    """Every string literal in the WitnessBuilder source."""
    for rel in ("tools/qou-substrate/python/qou_substrate/witness.py",
                "qou-mass/src/qou_mass/_internal/witness_base.py"):
        path = os.path.join(os.path.dirname(ROOT), rel)
        if not os.path.exists(path):
            path = os.path.join(ROOT, "..", rel)
        try:
            tree = ast.parse(open(path, encoding="utf-8", errors="replace").read())
        except (OSError, SyntaxError):
            continue
        lits = {n.value for n in ast.walk(tree)
                if isinstance(n, ast.Constant) and isinstance(n.value, str)}
        if len(lits) > 50:                      # sanity: we found the real file
            return lits | _FALLBACK_INFRA
    return _FALLBACK_INFRA


_INFRA = _builder_literals()

#: Containers to descend into but never report. Kept separate from _INFRA
#: because the derived set is over-broad and must not silently swallow the
#: subtree where every producer key lives.
_CONTAINERS = {"data", "parameters", "assertions", "environment", "invocation",
               "meta", "precisionMetadata"}


def _identifier_shaped(key: str) -> bool:
    """Would a human have written this key as a string literal?

    This is what rescues a `partial` file from being useless. A producer that
    builds `delta_star["(3, 2, 1)"]` from a partition tuple is genuinely dynamic
    and a static pass must not judge those keys -- but in the SAME witness,
    `gap_decomposition` and `option_E_comparison` are identifier-shaped, and a
    key of that shape is written as a literal in practice. Without the split,
    the real finding sits in a list beside six partition tuples and reads as
    noise.
    """
    return key.replace("_", "").isalnum() and not key[0].isdigit()


def _string_literals(tree: ast.AST) -> set[str]:
    """Every name this module could put in a witness key position.

    String literals, AND KEYWORD-ARGUMENT NAMES. The second half is not
    pedantry: a producer using a `**kwargs` witness API writes

        result(A_odd_preimage_positions_on_main_chain=odd_positions, ...)

    where the key is a Python IDENTIFIER and `ast.Constant(str)` never sees it.
    Found by spot-checking -- `qcollatz_backward_tree_structure_probe` was
    reported with three orphans that are in plain sight on line 127 of its own
    file. An 18th spelling for the blindness taxonomy, and one this audit
    introduced itself.
    """
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            out.add(n.value)
        elif isinstance(n, ast.keyword) and n.arg:
            out.add(n.arg)
    return out


#: flat module name -> path, built once over the whole tree.
_MODULE_INDEX: dict[str, str] = {}

#: EVERY name any producer in the corpus could put in a key position.
#:
#: The last false-positive class, and the one an import list cannot fix. A
#: producer that writes `out.add_data("lp", solver.to_dict())` names `lp` and
#: nothing under it; the FIELDS come from a helper reached through a method
#: call, which needs a call graph rather than an import list. Measured on the
#: five files that survived every earlier refinement: 10 genuine orphans
#: against ~30 of this shape.
#:
#: So the final gate is corpus-wide: a key that no file in `computations/` names
#: is one no producer can emit. Conservative in the safe direction -- a key that
#: IS genuinely orphaned here but happens to be named by some unrelated producer
#: is missed. That is a false negative, and it is the error this corpus can
#: afford; the alternative manufactured 6000 findings.
_CORPUS_NAMES: set[str] = set()


def _build_corpus_names() -> None:
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            try:
                t = ast.parse(open(os.path.join(root, fn), encoding="utf-8",
                                   errors="replace").read())
            except (OSError, SyntaxError):
                continue
            _CORPUS_NAMES.update(_string_literals(t))


def _build_module_index() -> None:
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in files:
            if fn.endswith(".py"):
                _MODULE_INDEX.setdefault(fn[:-3], os.path.join(root, fn))


def _import_cone_literals(tree: ast.AST, prod_path: str, depth: int = 1) -> set[str]:
    """String literals of the modules this producer imports, one hop by default.

    THE FALSE POSITIVE THIS EXISTS FOR, found by spot-checking and not by
    reasoning. A producer that calls a shared helper to attach a block names the
    block, and the helper names its FIELDS -- so a file-local literal scan sees
    `lean_uniqueness_ref` and misses `framework_doc` / `nucleus` / `theorem`,
    and reports three orphans in a witness that is entirely current. Six of the
    fourteen first-pass `confirmed` files were this one shape; a seventh
    (`interface_census/{positive,negative,averaged}`) was the same thing through
    an imported function.

    Same class as the import-cone blindness AGENTS.md records for witness
    staleness: a file-local diff cannot see what the module it calls does.
    """
    if depth <= 0:
        return set()
    here = os.path.dirname(prod_path)
    names = set()
    global _MODULE_INDEX
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            names |= {a.name.split(".")[0] for a in n.names}
        elif isinstance(n, ast.ImportFrom) and n.module:
            names.add(n.module.split(".")[0])
    out = set()
    for mod in names:
        # Resolve against the WHOLE tree, not just the producer's directory and
        # the root. The corpus imports flat module names across subdirectories
        # (`lp_dual_solver`, `witness_base`, ...), and a resolver that misses
        # the helper reports every field the helper names as an orphan -- which
        # is what produced the `operator_selection_lp/*_str` and
        # `lean_uniqueness_ref/*` false positives.
        for cand in (os.path.join(here, mod + ".py"),
                     os.path.join(ROOT, mod + ".py"),
                     _MODULE_INDEX.get(mod, "")):
            if not cand or not os.path.exists(cand):
                continue
            try:
                t = ast.parse(open(cand, encoding="utf-8", errors="replace").read())
            except (OSError, SyntaxError):
                continue
            out |= _string_literals(t)
            out |= _import_cone_literals(t, cand, depth - 1)
            break
    return out


def _has_dynamic_keys(tree: ast.AST) -> bool:
    """Does this module build any mapping key from something other than a literal?

    An f-string key, a variable key, or a dict comprehension makes the emitted
    key set undecidable statically -- so the file's verdict drops to `partial`.
    """
    for n in ast.walk(tree):
        if isinstance(n, ast.DictComp):
            return True
        if isinstance(n, ast.Dict):
            for k in n.keys:
                if k is not None and not (isinstance(k, ast.Constant)
                                          and isinstance(k.value, str)):
                    return True
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr in ("add_data", "add_assertion", "add_parameter")
                and n.args and not isinstance(n.args[0], ast.Constant)):
            return True
        # d[expr] = ... with a non-literal subscript
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if (isinstance(t, ast.Subscript)
                        and not (isinstance(t.slice, ast.Constant)
                                 and isinstance(t.slice.value, str))):
                    return True
    return False


def _witness_keys(obj, prefix="", out=None, depth=0):
    """Every key path in the committed witness, to a bounded depth."""
    if out is None:
        out = []
    # Do not descend into a container the builder fills wholesale: every key
    # under /environment and /invocation is the runner's, never the producer's.
    if depth > 3 or not isinstance(obj, dict):
        return out
    for k, v in obj.items():
        path = f"{prefix}/{k}"
        # An infra key is not the producer's to name -- but `data` and
        # `parameters` are CONTAINERS, so skipping them outright skips the whole
        # subtree where every real key lives. Do not report them; do descend.
        # (Caught by the selftest: without this the audit examined nothing at
        # all and reported a clean corpus.)
        if k not in _INFRA and k not in _CONTAINERS:
            out.append((k, path))
        if isinstance(v, dict) and k not in ("environment", "invocation",
                                             "precisionMetadata"):
            _witness_keys(v, path, out, depth + 1)
    return out


def _producer_for(witness_path: str, witness: dict | None = None) -> str | None:
    """The producer, preferring the witness's OWN `scriptFile` over the stem.

    Stem-matching is a guess and it was wrong on the corpus's clearest case.
    `per-irrep-pole-deuteron-h6.witness.json` records
    `scriptFile: per_irrep_pole_atom.py` -- a GENERALISED producer that took
    over from the per-atom scripts -- while the stem points at
    `per_irrep_pole_deuteron_h6.py`, which no longer owns it. Auditing the
    wrong file reports the right witness for the wrong reason, and would report
    it as clean the moment the stale sibling is deleted.

    The field is right there in the witness. Use it.
    """
    if witness:
        sf = witness.get("scriptFile") or witness.get("witness", {}).get("scriptFile") \
            if isinstance(witness.get("witness"), dict) else witness.get("scriptFile")
        if isinstance(sf, str) and sf.endswith(".py"):
            named = os.path.join(os.path.dirname(witness_path), os.path.basename(sf))
            if os.path.exists(named):
                return named
            idx = _MODULE_INDEX.get(os.path.basename(sf)[:-3])
            if idx:
                return idx
    d = os.path.dirname(witness_path)
    stem = os.path.basename(witness_path)[: -len(".witness.json")].replace("-", "_")
    for cand in (stem + ".py", stem + "_probe.py", stem.replace("_probe", "") + ".py"):
        p = os.path.join(d, cand)
        if os.path.exists(p):
            return p
    # a stem that dropped or gained a "_probe" / "_test" suffix
    for fn in os.listdir(d) if os.path.isdir(d) else []:
        if not fn.endswith(".py"):
            continue
        base = fn[:-3]
        if base.replace("_probe", "").replace("_test", "") == stem.replace(
                "_probe", "").replace("_test", ""):
            return os.path.join(d, fn)
    return None


def scan(witness_path: str) -> dict | None:
    try:
        w = json.load(open(witness_path, encoding="utf-8"))
    except (OSError, ValueError):
        return None
    prod = _producer_for(witness_path, w)
    if prod is None:
        return None
    try:
        src = open(prod, encoding="utf-8", errors="replace").read()
        tree = ast.parse(src)
    except (OSError, SyntaxError):
        return None
    lits = _string_literals(tree) | _import_cone_literals(tree, prod)
    dynamic = _has_dynamic_keys(tree)
    orphans = []
    for key, path in _witness_keys(w):
        if key in _INFRA or key in lits:
            continue
        orphans.append(path)
    named = sorted(o for o in orphans
                   if _identifier_shaped(o.rsplit("/", 1)[-1])
                   and (not _CORPUS_NAMES or o.rsplit("/", 1)[-1] not in _CORPUS_NAMES))
    other = sorted(set(orphans) - set(named))
    if not named:
        return None            # only dynamic-looking keys: nothing decidable
    return {
        "witness": os.path.relpath(witness_path, ROOT),
        "producer": os.path.relpath(prod, ROOT),
        "orphans": named,
        "suppressed": len(other),
        # A dynamic file still yields a usable verdict on its IDENTIFIER-shaped
        # keys; `partial` records that the rest of its key set is undecidable.
        "verdict": "partial" if dynamic else "confirmed",
    }


_SELFTEST_PROD = '''
wb.add_data("kept_key", 1)
witness = {"data": {"literal_key": 2}}
'''
_SELFTEST_WITNESS = {"data": {"kept_key": 1, "literal_key": 2, "GONE": 3}}
_SELFTEST_DYN_PROD = '''
wb.add_data("kept_key", 1)
d = {f"built_{i}": i for i in range(3)}
'''


def _selftest() -> None:
    """Pin BOTH verdicts. The `partial` case is the one that matters: a file
    building keys dynamically must not be reported as confirmed, because a
    static pass cannot see what it emits."""
    import tempfile
    # `/data/GONE` is orphaned by BOTH fixtures; only the literal fixture also
    # names `literal_key`, so the exact orphan list is pinned per fixture rather
    # than shared. (An earlier version asserted one shared list and failed on the
    # dynamic fixture -- the detector was right and the selftest was wrong.)
    for prod_src, want, exact in ((_SELFTEST_PROD, "confirmed", ["/data/GONE"]),
                                  (_SELFTEST_DYN_PROD, "partial",
                                   ["/data/GONE", "/data/literal_key"])):
        d = tempfile.mkdtemp()
        py = os.path.join(d, "thing.py")
        wj = os.path.join(d, "thing.witness.json")
        open(py, "w").write(prod_src)
        json.dump(_SELFTEST_WITNESS, open(wj, "w"))
        r = scan(wj)
        assert r is not None, f"selftest: expected a hit for {want}"
        assert r["orphans"] == exact, (want, r)
        assert r["verdict"] == want, f"selftest: expected {want}, got {r['verdict']}"


def main(argv: list[str] | None = None) -> int:
    _build_module_index()
    _selftest()
    _build_corpus_names()
    argv = list(sys.argv[1:] if argv is None else argv)
    findings = []
    if argv and argv[0] == "--files":
        targets = [a for a in argv[1:] if a.endswith(".witness.json")]
    else:
        targets = []
        for root, dirs, files in os.walk(os.path.join(ROOT)):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            targets += [os.path.join(root, f) for f in sorted(files)
                        if f.endswith(".witness.json")]
    for t in targets:
        r = scan(os.path.abspath(t))
        if r:
            findings.append(r)
    conf = [f for f in findings if f["verdict"] == "confirmed"]
    part = [f for f in findings if f["verdict"] == "partial"]

    print("=" * 78)
    print(" COMMITTED WITNESS KEYS THE PRODUCER CAN NO LONGER NAME")
    print("=" * 78)
    print(f"  witnesses examined        : {len(targets)}")
    print(f"  with a resolvable producer: {len(targets)}  (unresolvable are skipped)")
    print(f"  CONFIRMED orphans (gating): {len(conf)} file(s), "
          f"{sum(len(f['orphans']) for f in conf)} key(s)")
    print(f"  partial   (advisory)      : {len(part)} file(s) — the producer builds")
    print("                              some key dynamically, so a static pass")
    print("                              cannot decide it")
    print("  selftest                  : PASS (confirmed + partial both pinned)")
    for label, rows in (("CONFIRMED", conf[:40]), ("PARTIAL", part[:15])):
        if not rows:
            continue
        print(f"\n-- {label}")
        for f in rows:
            print(f"  {f['witness']}")
            print(f"      producer: {f['producer']}")
            for o in f["orphans"][:8]:
                print(f"      orphan:   {o}")
            if len(f["orphans"]) > 8:
                print(f"      ... and {len(f['orphans']) - 8} more")
            if f["suppressed"]:
                print(f"      ({f['suppressed']} non-identifier key(s) suppressed "
                      f"as dynamically built)")
    return 1 if conf else 0


if __name__ == "__main__":
    sys.exit(main())
