#!/usr/bin/env python3
"""Refuse float64 entry points in mpmath probes.

There are four separate beans about float64 leaking into high-precision work --
`j0th`, `qou-gqt5`, `qou-ny4j`, `qou-t0rf` -- and no gate. That is why it keeps
recurring: every instance was found by someone noticing a suspicious digit, and
noticing does not scale. This is the gate.

WHAT IT CATCHES, AND WHY EACH ONE
---------------------------------
1. **Non-exact float / complex literals in expression position.**
   `mpf(1) + 1j*mpf("0.4")` is full precision; `1 + 0.4j` is float64, because
   `0.4` is not representable in binary. mpmath will happily promote it and the
   whole computation silently drops to ~16 digits. Route 22's first run failed at
   exactly `4.3e-16` for this reason.

   `mpf("0.4")` passes -- the constant is a *string*. `mpf(0.4)` is flagged, and
   should be: the float is built before mpf ever sees it.

   Pure-imaginary literals with integral imaginary part (`1j`, `2j`) are exact
   and are allowed; they are the house idiom in `exp(1j*phi)`.

2. **`float(...)` and `complex(...)` calls.** Usually `round(float(x))` to
   extract an integer from an mpf. Use `int(nint(x))` -- `nint` rounds at working
   precision. `complex(...)` is the same collapse one type up: it takes an `mpc`
   and returns binary64.

3. **Lossy float literals handed to a CALL.** `sqrt(0.1)`, `findroot(f, 0.1)`,
   `quad(f, [0, 0.1])`, `complex(0.1, 0)` — all reach mpmath at float64, and none
   of them is a BinOp or an `mpf(...)` argument, so none was caught. Until this
   rule existed the guard reported **clean** on a file containing seven of them,
   which is the failure the guard exists to prevent, committed by the guard
   itself. Container literals are walked, because `quad(f, [0, 0.1])` is the
   common shape. Tolerance comparisons stay exempt.

4. **`math` / `numpy` / `cmath` / `statistics` imports.** All float64.

USAGE
-----
    python3 scripts/probe-float64-guard.py                    # survey, exit 0
    python3 scripts/probe-float64-guard.py --strict           # survey, exit 1 if any
    python3 scripts/probe-float64-guard.py --diff <files...>  # GATE, exit 1 on a hit

`--diff` is the CI form: it only inspects the files handed to it, so a PR is
gated on what it touches rather than on the whole backlog. Paths outside
`computations/` are ignored.

Add `# float64-ok: <reason>` on the offending line to allow a deliberate one.
"""

import argparse
import ast
import pathlib
import sys
from decimal import Decimal, InvalidOperation
from fractions import Fraction


def loses_digits(src_text: str, value) -> bool:
    """Did writing this literal as a Python float actually lose anything?

    `2.5`, `1.5`, `1e9` are exactly representable in binary — writing them costs
    nothing, and flagging them buries the real hits. `0.3`, `0.4`, `1.4` are not:
    the double stored is already a different number from the decimal written.

    Compares the exact rational the author *wrote* against the exact rational the
    double *holds*. Unparseable source falls back to "assume lossy", which errs
    toward reporting."""
    if src_text is None:
        return True
    try:
        written = Fraction(Decimal(src_text.rstrip("jJ")))
    except (InvalidOperation, ValueError, ArithmeticError):
        return True
    try:
        stored = Fraction(value)
    except (ValueError, OverflowError):
        return True
    return written != stored

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCOPE = "computations"
BANNED_MODULES = {"math", "numpy", "cmath", "statistics", "scipy", "np"}
ALLOW_MARKER = "float64-ok"


class Context(ast.NodeVisitor):
    """Pre-pass: classify where each float literal sits.

    A float in a *comparison* (`worst < 1e-30`) is a tolerance — it never enters
    the arithmetic, and flagging those buries the real hits under thousands of
    them. A float in *arithmetic*, or handed to `mpf`/`mpc`, is the dangerous
    case: `mpf(0.4)` has already lost the digits before `mpf` sees it.
    """

    def __init__(self):
        self.tolerance = set()      # id(node) of floats used only in comparisons
        self.arithmetic = set()     # id(node) of floats in BinOp / unary arithmetic
        self.constructor = set()    # id(node) of floats passed to mpf/mpc/mpmathify
        self.call_arg = set()       # id(node) of floats handed to ANY other call

    def visit_Compare(self, node):
        for operand in [node.left, *node.comparators]:
            for sub in ast.walk(operand):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, float):
                    self.tolerance.add(id(sub))
        self.generic_visit(node)

    def visit_BinOp(self, node):
        for operand in (node.left, node.right):
            if isinstance(operand, ast.Constant) and isinstance(operand.value, float):
                self.arithmetic.add(id(operand))
        self.generic_visit(node)

    def visit_Call(self, node):
        name = None
        if isinstance(node.func, ast.Name):
            name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            name = node.func.attr
        if name in {"mpf", "mpc", "mpmathify", "matrix"}:
            for a in node.args:
                if isinstance(a, ast.Constant) and isinstance(a.value, (float, complex)):
                    self.constructor.add(id(a))
        else:
            # Every OTHER call: a float literal handed to `sqrt`, `findroot`,
            # `quad`, `complex`, … reaches mpmath just as surely as one in a
            # BinOp, and until this branch existed the guard reported CLEAN on a
            # file containing seven of them. Container literals are walked too,
            # because `quad(f, [0, 0.1])` is the common shape.
            for a in [*node.args, *(k.value for k in node.keywords)]:
                for sub in ast.walk(a):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, float):
                        self.call_arg.add(id(sub))
        self.generic_visit(node)


class Finder(ast.NodeVisitor):
    def __init__(self, src_lines, ctx=None, src=None):
        self.lines = src_lines
        self.ctx = ctx or Context()
        self.src = src
        self.hits = []

    def _allowed(self, node):
        line = self.lines[node.lineno - 1] if 0 < node.lineno <= len(self.lines) else ""
        return ALLOW_MARKER in line

    def _flag(self, node, kind, detail):
        if not self._allowed(node):
            self.hits.append((node.lineno, kind, detail))

    def _text(self, node):
        """Source text of a literal. `ast.get_source_segment` re-splits the whole
        file on every call, which is O(file × constants); literals are always on
        one line, so slice the already-split lines instead.

        `col_offset` is a **UTF-8 byte** offset, not a character offset — this
        corpus is full of Greek letters, and slicing the str directly silently
        returns the wrong substring (it reported `j` for `1j` on such lines,
        which then failed the representability test and produced phantom hits)."""
        if not (0 < node.lineno <= len(self.lines)):
            return None
        if node.end_lineno != node.lineno:
            return None
        raw = self.lines[node.lineno - 1].encode("utf-8")
        try:
            return raw[node.col_offset:node.end_col_offset].decode("utf-8")
        except UnicodeDecodeError:
            return None

    def visit_Constant(self, node):
        v = node.value
        src = self._text(node)
        if isinstance(v, bool):
            pass
        elif isinstance(v, float):
            if not loses_digits(src, v):
                pass                      # exactly representable: nothing was lost
            elif id(node) in self.ctx.constructor:
                self._flag(node, "float-into-mpf",
                           f"mpf({v!r}) -- the digits are gone before mpf sees them; "
                           f"use mpf(\"{src}\")")
            elif id(node) in self.ctx.arithmetic and id(node) not in self.ctx.tolerance:
                self._flag(node, "float-in-arithmetic",
                           f"{src} -- build it as mpf(\"{src}\") instead")
            elif id(node) in self.ctx.call_arg and id(node) not in self.ctx.tolerance:
                self._flag(node, "float-call-arg",
                           f"{src} -- passed into a call at float64; "
                           f"build it as mpf(\"{src}\") first")
        elif isinstance(v, complex):
            # `1j`, `2j` are exact; `0.4j` is not
            if v.real != 0 or loses_digits(src, v.imag):
                self._flag(node, "complex-literal",
                           f"{src} -- not exactly representable; use mpf/mpc strings")
        self.generic_visit(node)

    def visit_Call(self, node):
        f = node.func
        if isinstance(f, ast.Name) and f.id == "float":
            self._flag(node, "float-call",
                       "float(...) -- use int(nint(x)) to pull an integer out of an mpf")
        elif isinstance(f, ast.Name) and f.id == "complex":
            # the exact analogue of `float(...)`, one type up: it takes an mpc
            # and returns binary64. Missed for the same reason `float(...)` was
            # caught -- somebody wrote one rule and not the other.
            self._flag(node, "complex-call",
                       "complex(...) -- collapses an mpc to float64; use mpc(re, im)")
        self.generic_visit(node)

    def visit_Import(self, node):
        for a in node.names:
            if a.name.split(".")[0] in BANNED_MODULES:
                self._flag(node, "float64-module", f"import {a.name}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module and node.module.split(".")[0] in BANNED_MODULES:
            self._flag(node, "float64-module", f"from {node.module} import ...")
        self.generic_visit(node)


def scan(path: pathlib.Path):
    try:
        src = path.read_text()
    except (OSError, UnicodeDecodeError):
        return []
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [(e.lineno or 0, "syntax-error", str(e))]
    ctx = Context()
    ctx.visit(tree)
    f = Finder(src.splitlines(), ctx, src)
    f.visit(tree)
    return sorted(f.hits)


def in_scope(p: pathlib.Path) -> bool:
    try:
        rel = p.resolve().relative_to(ROOT)
    except ValueError:
        return False
    return rel.parts[:1] == (SCOPE,) and p.suffix == ".py"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--diff", nargs="*", default=None,
                    help="gate mode: only these files, exit 1 on any hit")
    ap.add_argument("--strict", action="store_true",
                    help="survey mode, but exit 1 if anything is found")
    args = ap.parse_args()

    missing: list[pathlib.Path] = []
    if args.diff is not None:
        named = [pathlib.Path(f) for f in args.diff]
        # A named path that does not exist is a caller error, not a clean file.
        # Dropping it silently is how a gate passes by scanning nothing — the
        # same failure this lane hit with an audit that returned [] on a parse
        # error. Report it, and fail on it.
        missing = [f for f in named if not f.exists()]
        files = [f for f in named if f.exists() and in_scope(f)]
        gate = True
    else:
        files = sorted((ROOT / SCOPE).rglob("*.py"))
        gate = args.strict

    total, dirty = 0, 0
    for f in files:
        hits = scan(f)
        if not hits:
            continue
        dirty += 1
        rel = f.resolve().relative_to(ROOT)
        print(f"\n{rel}")
        for lineno, kind, detail in hits:
            total += 1
            print(f"  {rel}:{lineno}  [{kind}]  {detail}")

    if args.diff is not None:
        scanned = (f"{len(files)} of {len(args.diff)} named file(s) in scope "
                   f"({SCOPE}/), {len(missing)} missing")
    else:
        scanned = f"{len(files)} file(s) under {SCOPE}/"

    if missing:
        print("\nprobe-float64-guard: named path(s) do not exist — nothing was scanned "
              "for them, so this run proves nothing about:")
        for f in missing:
            print(f"  {f}")
        return 1

    if args.diff is not None and not files:
        print(f"probe-float64-guard: nothing to scan -- {scanned}. "
              "This is NOT a pass; it means no in-scope file was handed to the gate.")
        return 0

    if total == 0:
        print(f"probe-float64-guard: clean -- {scanned}, no float64 entry points.")
        return 0

    print(f"\nprobe-float64-guard: {total} hit(s) in {dirty} file(s) ({scanned}).")
    print("Fix, or annotate the line with `# float64-ok: <reason>` if deliberate.")
    return 1 if gate else 0


if __name__ == "__main__":
    raise SystemExit(main())
