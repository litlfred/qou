#!/usr/bin/env python3
"""undefined_name_audit.py — a name LOADED in a file and BOUND nowhere in it.

Bean `qou-lejl`. Every mechanism in this repo that could catch a NameError
requires EXECUTION, and the ones that break this way are precisely the ones
nothing executes.

  `producer_importability_audit` imports each producer, so it sees names
  undefined at MODULE level. A name used inside a function is invisible to it:
  the import succeeds, the module looks healthy, and the NameError waits for
  whoever calls that function.

  The two test trees (`tests/`, `tools/qou-substrate/tests/`) execute 209 tests
  and none of the 300+ probes here. A probe can be dead for weeks and stay
  green.

That is not a hypothetical gap. An ad-hoc version of this scan, run against
merge-touched files on 2026-09-06, found SEVEN live defects that both
mechanisms above had passed:

  hecke_core_legacy._is_sparse_sigma   a merge took HEAD for 12 hunks while the
                                       call site auto-merged outside them; the
                                       definition went, the caller stayed.
                                       Caught by tests only because that one
                                       happened to be module-level (46 red).
  qbeta_cosine_parametrisation…        `import os as _os_sidu` injected INSIDE
  witness_failed_assertion_audit       the module docstring by a bulk rewrite,
                                       so it is not an import node at all. The
                                       atomic witness write would have raised
                                       at the end of a completed run.
  qbeta_delta_vs_deltaTbeta_settled…   `Path` used, `pathlib` never imported:
                                       dead at import for six days.
  he_nu_sdp_barfold_h9_test  (RAIL)    a q0-anchor migration rewrote the block
  he_nu_sdp_psd_count_test   (H)       `Q0 = …` / `RAIL = …` into a resolved
  he_nu_sdp_saturation_…     (RAIL)    pin and took the second line with it.
                                       All three sit on the LP SUCCESS path and
                                       all three publish witnesses.

The recurring shape is a BLOCK REWRITE that drops a definition while its
consumer, elsewhere in the file, survives. Merges, bulk transforms and
convention migrations all produce it, and none of them is careless — the
consumer is simply out of the diff's line range.

METHOD. Whole-file, deliberately: a name bound ANYWHERE in the file counts as
bound, with no scope tracking. That under-reports (a name bound only in a
sibling function is missed) rather than crying wolf, which is the right side to
err on for a detector nobody will trust after its third false positive.

WHAT IS BOUND, and why each entry is here rather than in the findings:

  assignment / for / with-as / except-as / walrus   ast.Name in Store ctx
  def, class, and their names                       incl. async def
  parameters                                        posonly, kwonly, *args, **kw
  lambda parameters                                 ← 95 false positives without
                                                      this: `key=lambda kv: kv[1]`
  comprehension targets                             Store ctx, so free
  match-statement captures                          MatchAs / MatchStar /
                                                      MatchMapping rest
  global / nonlocal declarations                    binds for this file's purpose
  imports, including `as` aliases

`from x import *` makes the analysis unsound, so such files are SKIPPED rather
than reported — an unbounded star import can supply any name.

SCOPE. A DETECTOR. It fixes nothing, and a finding is a question ("where did
this name go?"), not a verdict. Recovering the answer belongs with whoever
knows the intent: for the three `he_nu_sdp` probes the definitions were
recovered from the commit each witness records in `scriptCommitSha`, not
invented from a plausible magnitude.
"""
from __future__ import annotations

import argparse
import ast
import builtins
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

BUILTIN = set(dir(builtins)) | {
    "__file__", "__name__", "__doc__", "__spec__", "__package__",
    "__builtins__", "__loader__", "__debug__", "__path__", "WindowsError",
    "reveal_type",
}
SKIP_DIRS = ("_deprecated", "__pycache__", "node_modules", ".git")


class _Binder(ast.NodeVisitor):
    """Collect every name BOUND anywhere, and every name LOADED anywhere."""

    def __init__(self) -> None:
        self.bound: set[str] = set()
        self.loads: list[tuple[int, str, int]] = []   # (node id, name, lineno)
        self.ann_only: set[int] = set()      # id() of Name nodes inside annotations
        self.star_import = False
        self.dynamic = False                 # module-level exec()/eval()

    # ---- loads and plain binding contexts -------------------------------
    def visit_Name(self, n: ast.Name) -> None:
        if isinstance(n.ctx, ast.Load):
            self.loads.append((id(n), n.id, n.lineno))
        else:                                   # Store, Del
            self.bound.add(n.id)

    def visit_Call(self, n: ast.Call) -> None:
        # `exec(open(...).read())` injects names no static pass can see. One
        # such family here (computations/hecke/jm_*_probe.py) execs a sibling
        # probe's source for its `build`. Treat the file as unsound rather than
        # report a name that IS defined at runtime.
        f = n.func
        nm = f.id if isinstance(f, ast.Name) else None
        if nm in ("exec", "eval"):
            self.dynamic = True
        self.generic_visit(n)

    def _mark_annotation(self, node) -> None:
        if node is None:
            return
        for x in ast.walk(node):
            if isinstance(x, ast.Name):
                self.ann_only.add(id(x))

    def visit_AnnAssign(self, n: ast.AnnAssign) -> None:
        self._mark_annotation(n.annotation)
        self.generic_visit(n)

    # ---- imports ---------------------------------------------------------
    def _alias(self, names) -> None:
        for a in names:
            if a.name == "*":
                self.star_import = True
            else:
                self.bound.add(a.asname or a.name.split(".")[0])

    def visit_Import(self, n: ast.Import) -> None:
        self._alias(n.names)

    def visit_ImportFrom(self, n: ast.ImportFrom) -> None:
        self._alias(n.names)

    # ---- callables -------------------------------------------------------
    def _params(self, a: ast.arguments) -> None:
        for x in list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs):
            self.bound.add(x.arg)
        if a.vararg:
            self.bound.add(a.vararg.arg)
        if a.kwarg:
            self.bound.add(a.kwarg.arg)

    def _fn(self, n) -> None:
        self.bound.add(n.name)
        self._params(n.args)
        a = n.args
        for x in list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs):
            self._mark_annotation(x.annotation)
        self._mark_annotation(n.returns)
        self.generic_visit(n)

    visit_FunctionDef = visit_AsyncFunctionDef = _fn

    def visit_Lambda(self, n: ast.Lambda) -> None:
        self._params(n.args)
        self.generic_visit(n)

    def visit_ClassDef(self, n: ast.ClassDef) -> None:
        self.bound.add(n.name)
        self.generic_visit(n)

    # ---- everything else that binds --------------------------------------
    def visit_ExceptHandler(self, n: ast.ExceptHandler) -> None:
        if n.name:
            self.bound.add(n.name)
        self.generic_visit(n)

    def visit_Global(self, n: ast.Global) -> None:
        self.bound.update(n.names)

    def visit_Nonlocal(self, n: ast.Nonlocal) -> None:
        self.bound.update(n.names)

    def visit_MatchAs(self, n) -> None:
        if n.name:
            self.bound.add(n.name)
        self.generic_visit(n)

    def visit_MatchStar(self, n) -> None:
        if n.name:
            self.bound.add(n.name)
        self.generic_visit(n)

    def visit_MatchMapping(self, n) -> None:
        if n.rest:
            self.bound.add(n.rest)
        self.generic_visit(n)


def scan_source(src: str, filename: str = "<src>"):
    """-> (findings, skipped_reason). findings = [(name, lineno)] sorted.

    A name is only reported when at least one of its loads is OUTSIDE an
    annotation. `derivation_chain.py` carries
    `M_HECKE_PIPELINE_AT_Q0: dict[str, mp.mpf]` with mpmath never imported —
    under `from __future__ import annotations` that annotation is a string and
    is never evaluated, so it raises nothing at runtime. Reporting it would
    have put a false alarm on a module 27 files import, which is how a
    detector loses its readers.
    """
    try:
        tree = ast.parse(src, filename)
    except SyntaxError as e:
        return [], f"SyntaxError:{e.lineno}"
    v = _Binder()
    v.visit(tree)
    if v.star_import:
        return [], "star-import"
    if v.dynamic:
        return [], "exec-or-eval"
    seen: dict[str, int] = {}
    for nid, name, ln in v.loads:
        if name in v.bound or name in BUILTIN:
            continue
        if nid in v.ann_only:
            continue                       # annotation-only: never evaluated
        seen.setdefault(name, ln)
    return sorted(seen.items(), key=lambda kv: kv[1]), None


def _selftest() -> int:
    cases = [
        ("def f():\n    return RAIL\n", ["RAIL"],
         "the type case: used in a function, bound nowhere"),
        ("RAIL = 1e5\ndef f():\n    return RAIL\n", [],
         "bound at module level, used in a function"),
        ("import os as _o\ndef f():\n    return _o.sep\n", [],
         "an aliased import binds the alias"),
        ("def f():\n    return sorted(x, key=lambda kv: kv[1])\n", ["x"],
         "LAMBDA PARAMS BIND -- kv is not a finding, x is"),
        ("d = {}\nprint([v for v in d])\n", [],
         "comprehension target binds"),
        ("try:\n    pass\nexcept ValueError as e:\n    print(e)\n", [],
         "except-as binds"),
        ("def f(a, *rest, k=1, **kw):\n    return a, rest, k, kw\n", [],
         "every parameter kind binds"),
        ("from x import *\ndef f():\n    return WHATEVER\n", [],
         "star import makes it unsound -- skipped, not reported"),
        ('"""import os as _os_sidu is inside this docstring."""\n'
         "def f():\n    return _os_sidu.replace(1, 2)\n", ["_os_sidu"],
         "an import swallowed by a docstring is NOT an import (the real bug)"),
        ("def f():\n    return len([1]) + int('2')\n", [],
         "builtins are not findings"),
        ("def f():\n    if (m := g()) is not None:\n        return m\n"
         "def g():\n    return 1\n", [],
         "walrus binds"),
        ("class C:\n    def m(self):\n        return C\n", [],
         "a class name binds"),
        ("from __future__ import annotations\n"
         "X: dict[str, mp.mpf] = {}\n", [],
         "ANNOTATION-ONLY: never evaluated, so not a runtime NameError"),
        ("from __future__ import annotations\n"
         "X: mp.mpf = mp.mpf(1)\n", ["mp"],
         "...but a real load of the same name IS reported"),
        ("exec(open('x').read())\ndef f():\n    return build(1)\n", [],
         "exec() injects names statically invisible -- unsound, so skipped"),
    ]
    bad = 0
    for src, want, why in cases:
        got = [n for n, _ in scan_source(src)[0]]
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} want={want!s:12} got={got!s:12}  {why}")
    print(f"\nselftest: {len(cases) - bad}/{len(cases)} passed")
    return 1 if bad else 0


def _tracked_py() -> list[str]:
    out = subprocess.run(["git", "ls-files", "*.py"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    return [f for f in out if not any(d in f.split("/") for d in SKIP_DIRS)]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-witness", action="store_true")
    ap.add_argument("paths", nargs="*")
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()

    files = a.paths or _tracked_py()
    findings, skipped, dynamic, unparsed = [], [], [], []
    for f in files:
        p = ROOT / f if not pathlib.Path(f).is_absolute() else pathlib.Path(f)
        try:
            src = p.read_text(encoding="utf-8")
        except OSError:
            continue
        miss, why = scan_source(src, str(f))
        if why and why.startswith("SyntaxError"):
            unparsed.append(f)
        elif why == "exec-or-eval":
            dynamic.append(f)
        elif why:
            skipped.append(f)
        for name, ln in miss:
            findings.append({"file": str(f), "line": ln, "name": name})

    if a.json:
        print(json.dumps({"findings": findings, "skipped_star_import": skipped,
                          "skipped_exec_or_eval": dynamic,
                          "unparsed": unparsed, "scanned": len(files)}, indent=2))
        return 1 if findings else 0

    print("=" * 78)
    print("names LOADED but BOUND NOWHERE in their file — static, no execution")
    print("=" * 78)
    print(f"  scanned                     : {len(files)} tracked .py")
    print(f"  skipped (star import)       : {len(skipped)}")
    print(f"  skipped (exec/eval)         : {len(dynamic)}")
    print(f"  unparsed                    : {len(unparsed)}")
    print(f"  FINDINGS                    : {len(findings)}")
    by_file: dict[str, list] = {}
    for x in findings:
        by_file.setdefault(x["file"], []).append(x)
    for f in sorted(by_file):
        print(f"\n  {f}")
        for x in by_file[f]:
            print(f"      line {x['line']:>5}  {x['name']}")
    if not a.no_witness:
        from witness_base import WitnessBuilder      # noqa: E402
        w = WitnessBuilder("undefined-name-audit", engine="python")
        w.set_description(
            "Names loaded in a file and bound nowhere in it, found by static "
            "AST over every tracked .py — no execution. Complements "
            "producer_importability_audit, which imports each producer and so "
            "sees only MODULE-level NameErrors: a name used inside a function "
            "that no test calls is invisible to it, and the 300+ probes here "
            "are executed by neither test tree. An ad-hoc run on 2026-09-06 "
            "found 7 such live defects, all from a block rewrite that dropped "
            "a definition while its consumer survived outside the diff range. "
            "Whole-file scoping is deliberate: it under-reports rather than "
            "false-alarming. Bean qou-lejl.")
        w.add_data("scanned_files", len(files))
        w.add_data("skipped_star_import", len(skipped))
        w.add_data("skipped_exec_or_eval", len(dynamic))
        w.add_data("unparsed", len(unparsed))
        w.add_data("findings", findings)
        w.add_assertion("no name is loaded while bound nowhere in its file",
                        computed=len(findings), expected=0)
        w.set_audit_only("computations/audits/undefined_name_audit.py")
        out = w.save()
        print(f"\n[witness] {out}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
