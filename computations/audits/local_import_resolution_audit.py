"""Static check: does every `from <local-module> import <name>` resolve?

Pure AST analysis -- nothing is imported or executed, so no producer writes a
sibling witness while this runs. That restraint is deliberate: AGENTS.md records
that producers write sibling witnesses, and a sweep that imports them leaves a
dirty `computations/` tree reading as real work.

What it detects: a dependency renames or removes a module-level name and the
consumer's import is never updated. The consumer's OWN file hash does not
change, so every `scriptHash`-keyed staleness detector reports it healthy while
the script cannot be imported at all -- or, when the import sits inside a
function, fails only on that path. Worked case: `snappy_cusp_seeding.py` sat
`scriptHash`-IN-SYNC with its witness for three weeks while un-importable,
because `q_pochhammer_seed.IM_PERTURBATION` had become `IM_PERTURBATION_STR`
in the NO-FLOAT64 migration. Bean `qou-2cz1`.

This is AGENTS.md's import-cone drift class one step worse: there, a byte-stable
producer's NUMBER moves because a numeric module in its cone changed; here the
cone change does not move a number, it stops the producer running, which no
staleness metric can express. `witness_import_cone_staleness_audit.py` ranks by
"a cone module changed more recently than the witness" -- a recency heuristic --
and never asks whether the import resolves.

Exits 1 when anything is unresolved, so it can be used as a gate.

UNDECIDABLE, and skipped rather than guessed at:
  - a module star-importing from a package outside this tree (the
    `_precision` / `witness_base` back-compat shims re-export from
    `qou_substrate.*`, so their own AST holds neither `set_compute_dps` nor
    `WitnessBuilder`);
  - a module defining `__getattr__`, which can serve any name
    (`codata_constants` implements the 2026-05-10 `M_P_MEV` ->
    `M_P_MEV_VALIDATION` rename that way, so its imports DO resolve);
  - a module calling `globals().update(...)`;
  - an AMBIGUOUS bare name -- the same stem in two directories, where which
    file an import resolves to depends on `sys.path` order
    (`witness_provenance_audit` exists in both `computations/` and
    `computations/audits/`).

Reporting a name "missing" from a module we cannot read is the failure mode this
script is about, so each class above is excluded and counted, never resolved by
guess. Quote those counts alongside the unresolved count: they are the stated
coverage limit.

Usage:
    python3 -I computations/audits/local_import_resolution_audit.py
    python3 -I computations/audits/local_import_resolution_audit.py --selftest
"""
from __future__ import annotations

import ast
import pathlib
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent  # computations/


def discover(root: pathlib.Path) -> tuple[dict[str, pathlib.Path], set[str]]:
    """Map bare module name -> path, plus the set of ambiguous bare names."""
    seen: dict[str, list[pathlib.Path]] = {}
    for p in sorted(root.rglob("*.py")):
        if "_deprecated" in p.parts or "__pycache__" in p.parts:
            continue
        seen.setdefault(p.stem, []).append(p)
    ambiguous = {k for k, v in seen.items() if len(v) > 1}
    return {k: v[0] for k, v in seen.items() if len(v) == 1}, ambiguous


def _bind(node: ast.AST, out: set[str]) -> None:
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


class Resolver:
    def __init__(self, mods: dict[str, pathlib.Path], ambiguous: set[str]) -> None:
        self.mods = mods
        self.ambiguous = ambiguous
        self._cache: dict[str, set[str] | None] = {}

    def exports(self, stem: str, seen: frozenset[str] = frozenset()) -> set[str] | None:
        """Module-level names, or None if the module is UNDECIDABLE."""
        if stem in self._cache:
            return self._cache[stem]
        if stem in seen:
            return set()
        seen = seen | {stem}
        path = self.mods.get(stem)
        if path is None:
            return None
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            self._cache[stem] = None
            return None
        out: set[str] = set()
        for node in ast.walk(tree):
            _bind(node, out)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
               and node.name == "__getattr__":
                self._cache[stem] = None
                return None
            if isinstance(node, ast.ImportFrom) and any(a.name == "*" for a in node.names):
                base = (node.module or "").split(".")[0]
                if node.level or base not in self.mods:
                    self._cache[stem] = None
                    return None
                sub = self.exports(base, seen)
                if sub is None:
                    self._cache[stem] = None
                    return None
                out |= sub
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
               and node.func.attr == "update" \
               and isinstance(node.func.value, ast.Call) \
               and isinstance(node.func.value.func, ast.Name) \
               and node.func.value.func.id == "globals":
                self._cache[stem] = None
                return None
        self._cache[stem] = out
        return out

    def scan(self, files: list[pathlib.Path]) -> dict:
        """The single code path. Both the real run and --selftest go through it."""
        broken: list[tuple[str, int, str, str]] = []
        checked = 0
        undecidable: set[str] = set()
        ambiguous_hits: set[str] = set()
        for p in files:
            try:
                tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if not isinstance(node, ast.ImportFrom) or node.level:
                    continue
                base = (node.module or "").split(".")[0]
                if base in self.ambiguous:
                    ambiguous_hits.add(base)
                    continue
                if base not in self.mods or self.mods[base] == p:
                    continue
                names = self.exports(base)
                if names is None:
                    undecidable.add(base)
                    continue
                for a in node.names:
                    if a.name == "*":
                        continue
                    checked += 1
                    if a.name not in names:
                        broken.append((str(p), node.lineno, base, a.name))
        return {"broken": broken, "checked": checked,
                "undecidable": undecidable, "ambiguous": ambiguous_hits}


def selftest() -> int:
    """Calibration. Exits non-zero unless the resolver behaves on known shapes.

    The POSITIVE is a synthetic fixture, NOT a live corpus defect.

    It was keyed on `q_pochhammer_seed.IM_PERTURBATION` for exactly one day.
    That defect was then fixed -- which is the whole point of the audit -- and
    the selftest began FAILING on a clean tree, reporting the repair as a
    regression in itself. A calibration that dies when the corpus is repaired is
    unusable; and the tempting alternative, asserting a hardcoded True, is the
    self-certifying calibration of taxonomy row 45: an audit whose calibration
    cannot fail cannot discover its own blind spot.

    The fixture runs through `Resolver.scan`, the same method the real run uses.
    An earlier version re-implemented the check inline, and a mutation test
    exposed that: blinding the real resolver left the selftest passing. A
    calibration that does not exercise the code under test is worth nothing, so
    it must go through `scan` and nowhere else.

    The NEGATIVES are corpus-resident on purpose. Each is a real shape that made
    an earlier version over-report -- two star re-export shims, one ambiguous
    stem, one module `__getattr__` -- and unlike the positive, a negative does
    not evaporate when a defect is fixed: these modules are load-bearing.
    """
    ok = True
    with tempfile.TemporaryDirectory() as td:
        fx = pathlib.Path(td)
        (fx / "fixture_dep.py").write_text("PRESENT = 1\ndef also_present(): pass\n")
        (fx / "fixture_use.py").write_text(
            "from fixture_dep import PRESENT, ABSENT_NAME\n"
            "from fixture_dep import also_present\n"
        )
        fmods, famb = discover(fx)
        res = Resolver(fmods, famb).scan([fx / "fixture_use.py"])
        got = [n for *_, n in res["broken"]]
        if got != ["ABSENT_NAME"]:
            print(f"SELFTEST FAIL: fixture expected ['ABSENT_NAME'], got {got}")
            ok = False
        if res["checked"] != 3:
            print(f"SELFTEST FAIL: fixture expected 3 bindings checked, got {res['checked']}")
            ok = False

    mods, ambiguous = discover(ROOT)
    files = sorted(set(mods.values()))
    hits = {(b, n) for _, _, b, n in Resolver(mods, ambiguous).scan(files)["broken"]}
    for bad in [("_precision", "set_compute_dps"),                     # star shim
                ("witness_base", "WitnessBuilder"),                    # star shim
                ("witness_provenance_audit", "written_filenames"),     # ambiguous stem
                ("witness_provenance_audit", "builder_names"),         # ambiguous stem
                ("codata_constants", "M_P_MEV")]:                      # __getattr__
        if bad in hits:
            print(f"SELFTEST FAIL: known-good import flagged: {bad}")
            ok = False

    print("SELFTEST PASS" if ok else "SELFTEST FAILED")
    return 0 if ok else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    mods, ambiguous = discover(ROOT)
    res = Resolver(mods, ambiguous).scan(sorted(set(mods.values())))
    print(f"resolvable local `from X import name` bindings checked: {res['checked']}")
    print("modules skipped as UNDECIDABLE "
          f"(star-import out of tree / __getattr__ / globals().update): "
          f"{len(res['undecidable'])}")
    print(f"  {', '.join(sorted(res['undecidable']))}")
    print("modules skipped as AMBIGUOUS (same bare name in two dirs): "
          f"{len(res['ambiguous'])}")
    print(f"  {', '.join(sorted(res['ambiguous']))}")
    print(f"\nUNRESOLVED: {len(res['broken'])}")
    for f, ln, base, name in res["broken"]:
        print(f"  {f}:{ln}  from {base} import {name}")
    if res["broken"]:
        print("\nEach line above is a script that CANNOT be imported (or, if the import\n"
              "sits inside a function, fails the moment that path is taken). The\n"
              "consumer's own file hash is unchanged, so no scriptHash-keyed staleness\n"
              "detector reports it.")
    return 1 if res["broken"] else 0


if __name__ == "__main__":
    sys.exit(main())
