"""Static check: does every `from <local-module> import <name>` resolve?

Pure AST analysis -- nothing is imported or executed, so no producer writes a
witness. Detects the class where a dependency renames a module-level name and
the consumer's import is never updated: the consumer's OWN file hash is
unchanged, so every scriptHash-keyed staleness detector reports it healthy
while the script cannot be imported at all.

A module whose exports cannot be fully enumerated -- it star-imports from a
package outside this tree, or assigns into globals() -- is UNDECIDABLE and is
skipped entirely rather than guessed at. Reporting a name "missing" from a
module we cannot read is the failure mode this script is about.

Calibrated: --selftest asserts the one known true positive is found and two
known-good imports are not flagged. It FAILS rather than passing silently, so
a future narrowing cannot report a clean tree.
"""
import ast, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent  # computations/
_seen = {}
for p in sorted(ROOT.rglob("*.py")):
    if "_deprecated" in p.parts or "__pycache__" in p.parts:
        continue
    _seen.setdefault(p.stem, []).append(p)
# An AMBIGUOUS stem (two files, one bare name) cannot be resolved statically --
# which file a consumer gets depends on sys.path order. Picking the first in
# sorted() order silently reads the wrong module: that cost 7 false positives
# here, all against `witness_provenance_audit`, which exists in both
# `computations/` and `computations/audits/`.
AMBIGUOUS = {k for k, v in _seen.items() if len(v) > 1}
mods = {k: v[0] for k, v in _seen.items() if len(v) == 1}

def _bind(node, out):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        out.add(node.name)
    elif isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name):
                out.add(t.id)
            elif isinstance(t, (ast.Tuple, ast.List)):
                out |= {e.id for e in t.elts if isinstance(e, ast.Name)}
    elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        out.add(node.target.id)
    elif isinstance(node, (ast.Import, ast.ImportFrom)):
        for a in node.names:
            if a.name != "*":
                out.add((a.asname or a.name).split(".")[0])

_cache = {}
def exports(stem, seen=None):
    """Module-level names, or None if the module is UNDECIDABLE."""
    if stem in _cache:
        return _cache[stem]
    seen = seen or set()
    if stem in seen:
        return set()
    seen = seen | {stem}
    path = mods.get(stem)
    if path is None:
        return None
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        _cache[stem] = None
        return None
    out = set()
    for node in ast.walk(tree):
        _bind(node, out)
        if isinstance(node, ast.ImportFrom) and any(a.name == "*" for a in node.names):
            base = (node.module or "").split(".")[0]
            if node.level or base not in mods:
                _cache[stem] = None          # star from outside this tree
                return None
            sub = exports(base, seen)
            if sub is None:
                _cache[stem] = None
                return None
            out |= sub
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "__getattr__":
            _cache[stem] = None          # module __getattr__ can serve any name
            return None
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in {"update"} and isinstance(node.func.value, ast.Call) \
               and isinstance(node.func.value.func, ast.Name) \
               and node.func.value.func.id == "globals":
                _cache[stem] = None          # globals().update(...)
                return None
    _cache[stem] = out
    return out

broken, checked, undecidable, ambiguous_hits = [], 0, set(), set()
for p in sorted(set(mods.values())):
    try:
        tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        continue
    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom) or node.level:
            continue
        base = (node.module or "").split(".")[0]
        if base in AMBIGUOUS:
            ambiguous_hits.add(base)
            continue
        if base not in mods or mods[base] == p:
            continue
        names = exports(base)
        if names is None:
            undecidable.add(base)
            continue
        for a in node.names:
            if a.name == "*":
                continue
            checked += 1
            if a.name not in names:
                broken.append((str(p), node.lineno, base, a.name))

if "--selftest" in sys.argv:
    hits = {(b, n) for _, _, b, n in broken}
    ok = True
    if ("q_pochhammer_seed", "IM_PERTURBATION") not in hits:
        print("SELFTEST FAIL: known true positive NOT detected"); ok = False
    for bad in [("_precision", "set_compute_dps"), ("witness_base", "WitnessBuilder"),
                ("witness_provenance_audit", "written_filenames"),
                ("witness_provenance_audit", "builder_names")]:
        if bad in hits:
            print(f"SELFTEST FAIL: known-good import flagged: {bad}"); ok = False
    print("SELFTEST PASS" if ok else "SELFTEST FAILED")
    sys.exit(0 if ok else 1)

print(f"resolvable local `from X import name` bindings checked: {checked}")
print(f"modules skipped as UNDECIDABLE (star-import out of tree / __getattr__): {len(undecidable)}")
print(f"  {', '.join(sorted(undecidable))}")
print(f"modules skipped as AMBIGUOUS (same bare name in two dirs): {len(ambiguous_hits)}")
print(f"  {', '.join(sorted(ambiguous_hits))}")
print(f"\nUNRESOLVED: {len(broken)}")
for f, ln, base, name in broken:
    print(f"  {f}:{ln}  from {base} import {name}")

if broken:
    print("\nEach line above is a script that CANNOT be imported (or, if the import\n"
          "sits inside a function, fails the moment that path is taken). The\n"
          "consumer's own file hash is unchanged, so no scriptHash-keyed staleness\n"
          "detector reports it.")
sys.exit(1 if broken else 0)
