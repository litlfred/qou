#!/usr/bin/env python3
"""numpy_mpmath_dtype_leak_audit — find silent BLAS-to-Python demotions.

THE PATTERN (proposed P35; measured 2026-08-15, bean qou-5qwb)
---------------------------------------------------------------
A numpy float64 array is combined arithmetically with an **mpmath** value.
Numpy has no float64 representation for `mpf`, so it silently promotes the
result to `dtype=object` — an array of Python objects. Every subsequent
operation on it leaves BLAS and runs in the interpreter, one Python-level
multiply at a time.

Three properties make this the worst kind of performance bug:

  1. **Silent.** No error, no warning, no dtype in the output.
  2. **Correct.** The answer is right, so tests pass and nothing looks wrong.
  3. **Sticky.** If the demoted array is reassigned into the accumulator
     (`M = M @ cross`), *every later iteration is demoted too* — one bad
     value at step 11 of 35 costs you steps 11 through 35.

Measured instance, `hoefsmit_numpy.chi_numpy` (fixed in 0bfb2a48ab):
`d_for_ctype` returns `float` for three crossing types and `mpf` for
`averaged_weighted`. On tritium (n=9, dim=120, 35 crossings) the first
`averaged_weighted` crossing is at index 11, and per-matmul cost goes

    0.0005 s  ->  2.7 s      and never recovers

One partition: **66 s -> 0.16 s** after adding `float()`. That is ~4000x on
a 120x120 matmul, on a machine whose numpy does a 600x600 matmul in 5 ms.

WHY A DEDICATED SCANNER
-----------------------
`compute_audit_scan.py` did not flag it — there is no `sympy.simplify` to
find, no missing cache, no bad normalisation. The cost is invisible at the
source level and only shows up as "this script is mysteriously slow", which
is exactly how it got misfiled as an environment limit for six hours.

Worse, the workaround was **folklore**: four of the five numpy consumers of
`d_for_ctype` already wrapped it in `float()`, each having presumably hit
this independently. Nothing enforced it and nothing wrote it down, so the
fifth author had no way to know. A convention that lives only in four call
sites is one new caller away from regressing.

WHAT THIS FLAGS
---------------
Per file that imports both numpy and mpmath, lines where an mpmath-valued
expression meets numpy array arithmetic without a `float()` / `complex()` /
`.astype()` barrier. High-recall by design: the verdict is an agent's, and
a `float()` already present is treated as the barrier it is.

Usage:
    python3 computations/numpy_mpmath_dtype_leak_audit.py
    python3 computations/numpy_mpmath_dtype_leak_audit.py --self-test
    python3 computations/numpy_mpmath_dtype_leak_audit.py --json
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Calls/values known to yield mpmath objects.
MPMATH_VALUE = re.compile(
    r"\b(?:mp|mpmath)\.(?:mpf|mpc|matrix|sqrt|exp|log|cos|sin|pi|e)\b"
    r"|\bmpf\s*\(|\bmpc\s*\("
    r"|\bd_for_ctype\s*\("          # the measured offender
    r"|\bQ_50_DIGIT_STR\b"
)

# numpy array-producing expressions.
NUMPY_ARRAY = re.compile(
    r"\bnp\.(?:eye|zeros|ones|array|empty|full|identity|diag)\s*\("
    r"|\bnumpy\.(?:eye|zeros|ones|array|empty|full|identity|diag)\s*\("
)

# A cast that stops the promotion.
BARRIER = re.compile(r"\bfloat\s*\(|\bcomplex\s*\(|\.astype\s*\(|\bnp\.float64\s*\(")

ARITH = re.compile(r"[-+*@/]")

# Explicit opt-out, same idiom as the compute-audit catalogue's `# noqa: P31`.
# Needed because some code is SUPPOSED to contain the leak: the P28 benchmark
# reconstructs the pre-fix `chi_numpy` in-process so the two callers can be
# timed on one machine, and that reconstruction only means anything if it
# keeps the bug. A detector with no way to say "yes, deliberately" forces the
# author to either delete the measurement or silence the gate wholesale.
NOQA_P35 = re.compile(r"#\s*noqa:\s*P35\b")

# An explicit object dtype means the author WANTS python objects in there.
DTYPE_OBJECT = re.compile(r"dtype\s*=\s*(?:object|'O'|\"O\"|np\.object_)")


# `name = np.eye(...)` — binds a numpy array to a variable.
NP_ASSIGN = re.compile(
    r"^\s*(\w+)\s*=\s*.*\b(?:np|numpy)\."
    r"(?:eye|zeros|ones|array|empty|full|identity|diag|asarray)\s*\(")


def scan_text(text: str) -> list[tuple[int, str, str]]:
    """(lineno, line, reason) for suspicious lines in one file's source.

    Two passes, because the measured bug is invisible to a single-line regex.
    In `chi_numpy` the offending line was

        cross = sigma + d_val * eye

    with no `np.` on it at all — `eye` was bound to `np.eye(dim)` earlier and
    `d_val` to `d_for_ctype(...)` earlier still. Matching only lines that
    literally contain `np.something(` would therefore MISS the one instance
    this scanner exists to catch, while matching every line containing any
    mpmath call floods the output with scalar arithmetic like
    `h = q0 - mp.mpf(1)/q0`, which never touches an array (measured: 12 of 17
    first-cut candidates were exactly that).

    So: pass 1 collects the file's numpy-array variables and its
    mpmath-valued variables; pass 2 flags lines where the two meet in
    arithmetic with no cast between them.
    """
    if not re.search(r"^\s*(?:import numpy|from numpy)", text, re.M):
        return []
    if not re.search(r"^\s*(?:import mpmath|from mpmath|import mpmath as)", text, re.M):
        return []

    lines = text.split("\n")
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []

    # Scope per FUNCTION, not per file. char_fast.py taught this the hard
    # way: one function binds `I = np.eye(dim, dtype=complex)` (numpy) and
    # another binds `I = mp.eye(dim)` (mpmath). A file-wide name table scores
    # the second function's all-mpmath line as if its `I` were the first
    # function's numpy array — a confident false positive on a file that is
    # entirely correct. Scoping also lets docstrings fall out naturally,
    # since only real statements are walked.
    # Partition every statement to its NEAREST enclosing function (or the
    # module). `ast.walk` alone will not do: it descends into nested defs, so
    # a "module scope" built that way silently contains every function's body
    # and reintroduces the exact file-wide bleed this scoping exists to
    # prevent — char_fast.py stayed a false positive until this was fixed.
    FUNC = (ast.FunctionDef, ast.AsyncFunctionDef)
    buckets: dict[int, list] = {}

    def collect(node, owner: int) -> None:
        for child in ast.iter_child_nodes(node):
            if isinstance(child, FUNC):
                collect(child, id(child))
            else:
                buckets.setdefault(owner, []).append(child)
                collect(child, owner)

    collect(tree, id(tree))

    out: list[tuple[int, str, str]] = []
    for stmts in buckets.values():

        np_vars: set[str] = set()
        mp_vars: set[str] = set()
        for node in stmts:
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = (node.targets if isinstance(node, ast.Assign)
                       else [node.target])
            names = [t.id for t in targets if isinstance(t, ast.Name)]
            if not names or node.value is None:
                continue
            src = ast.unparse(node.value)
            if BARRIER.search(src):
                continue
            if NUMPY_ARRAY.search(src):
                # `np.zeros(..., dtype=object)` is a DELIBERATE object array,
                # not an accidental demotion. garside-irrep-qvalues.py does
                # exactly this on purpose, with a comment citing Copilot #2050:
                # a float64 dtype there would silently coerce away mp.mpf
                # precision, so object is the CORRECT choice and mpmath values
                # are supposed to land in it. Flagging it would be telling the
                # author to reintroduce a precision bug.
                if not DTYPE_OBJECT.search(src):
                    np_vars.update(names)
            elif MPMATH_VALUE.search(src):
                mp_vars.update(names)

        if not np_vars:
            continue
        np_tok = re.compile(r"\b(?:" + "|".join(map(re.escape, np_vars)) + r")\b")
        mp_tok = (re.compile(r"\b(?:" + "|".join(map(re.escape, mp_vars)) + r")\b")
                  if mp_vars else None)

        for node in stmts:
            if not isinstance(node, (ast.Assign, ast.AugAssign, ast.Expr,
                                     ast.Return)):
                continue
            # Docstrings and printed banners are ast.Expr wrapping a string
            # constant. `ast.unparse` renders their whole text, so a docstring
            # that merely *mentions* mpmath and a matrix scores as arithmetic
            # — 4 of the 15 second-cut candidates were exactly this.
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                continue
            # `print("""...""")` is Expr -> Call, so the Constant check above
            # misses it while ast.unparse still renders the whole banner text.
            if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                    and isinstance(node.value.func, ast.Name)
                    and node.value.func.id == "print"):
                continue
            lineno = getattr(node, "lineno", None)
            if lineno is None:
                continue
            src = ast.unparse(node)
            if not ARITH.search(src) or BARRIER.search(src):
                continue
            if not (np_tok.search(src) or NUMPY_ARRAY.search(src)):
                continue
            if NUMPY_ARRAY.search(src) and not mp_tok and not MPMATH_VALUE.search(src):
                continue
            raw = lines[lineno - 1].strip() if lineno <= len(lines) else src
            if NOQA_P35.search(lines[lineno - 1] if lineno <= len(lines) else ""):
                continue
            if MPMATH_VALUE.search(src):
                out.append((lineno, raw,
                            "mpmath call meets a numpy array in arithmetic"))
            elif mp_tok and mp_tok.search(src):
                out.append((lineno, raw,
                            "mpmath-valued variable meets a numpy array "
                            "(the chi_numpy shape)"))

    # Dedupe: Module scope and a function scope can both see a statement.
    seen, uniq = set(), []
    for item in sorted(out):
        if item[0] in seen:
            continue
        seen.add(item[0])
        uniq.append(item)
    return uniq


def self_test() -> int:
    """Prove the detector fires on the measured bug and not on its fix."""
    # Verbatim shape of the measured bug: the array and the mpmath value are
    # BOTH variables bound on earlier lines, so the offending line names
    # neither np. nor mp.
    buggy = (
        "import numpy as np\n"
        "import mpmath as mp\n"
        "eye = np.eye(dim)\n"
        "d_val = d_for_ctype(ctype, h)\n"
        "cross = sigma + d_val * eye\n"
    )
    fixed = (
        "import numpy as np\n"
        "import mpmath as mp\n"
        "eye = np.eye(dim)\n"
        "d_val = float(d_for_ctype(ctype, h))\n"
        "cross = sigma + d_val * eye\n"
    )
    inline = (
        "import numpy as np\n"
        "import mpmath as mp\n"
        "eye = np.eye(dim)\n"
        "cross = sigma + mp.mpf(2) * eye\n"
    )
    no_numpy = "import mpmath as mp\nx = mp.mpf(2) * y\n"
    no_mpmath = "import numpy as np\nM = np.eye(3) * 2.0\n"
    # The dominant false positive of the first cut: scalar-only mpmath
    # arithmetic in a file that happens to import numpy elsewhere.
    scalar_only = (
        "import numpy as np\n"
        "import mpmath as mp\n"
        "h = q0 - mp.mpf(1) / q0\n"
    )

    cases = [
        ("the measured chi_numpy bug is caught (both operands are vars)",
         buggy, True),
        ("the float() fix is NOT flagged", fixed, False),
        ("an inline mpmath call into an array IS caught", inline, True),
        ("mpmath without numpy is NOT flagged", no_numpy, False),
        ("numpy without mpmath is NOT flagged", no_mpmath, False),
        ("scalar-only mpmath arithmetic is NOT flagged", scalar_only, False),
        ("an explicit # noqa: P35 opts out", buggy.replace(
            "cross = sigma + d_val * eye",
            "cross = sigma + d_val * eye  # noqa: P35"), False),
    ]
    failed = 0
    for name, src, want in cases:
        got = bool(scan_text(src))
        ok = got == want
        failed += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    print()
    if failed:
        print(f"SELF-TEST FAILED — {failed} case(s).")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases, "
          f"including the measured chi_numpy bug.")
    return 0



# ── Second detector: the PARAMETER-fill leak (bean qou-d8gq) ─────────
#
# `scan_text` above returns [] unless the file imports mpmath. That is right
# for the chi_numpy shape it was built for, and structurally BLIND to the one
# actually measured in syt_prefix_cache.py:
#
#     def build_seminormal_matrices_cached(shape, *, cache, q_val=None):
#         M = np.zeros((dim, dim))        # float64 — no dtype
#         M[r, c] = v                     # v is an mpf when q_val is an mpf
#
# That module imports numpy and `math`, never mpmath: the mpf arrives through
# the SIGNATURE. So the precondition fired and the scanner never looked, while
# every mpf entry was silently truncated to 53 bits and the downstream matmul
# left BLAS (measured 642x at dim=162).
#
# A library that receives its numeric type from its caller cannot be cleared by
# looking at its own imports. This detector therefore ignores the mpmath
# precondition and asks a narrower question instead: is there a dtype-LESS
# numpy allocation that is later filled by subscript assignment? Such an array
# silently defines the precision of whatever it is handed.
#
# Reported as a separate, non-blocking tier: `dtype=` is genuinely optional in
# plenty of honest f64 code, so this is a list of places to look, not a defect
# list — the same convention the f64-into-mpmath audit uses for its
# circumstantial tiers.

# The negative lookahead must scan the REST OF THE LINE, not `[^)]*`: in
# `np.zeros((dim, dim), dtype=object)` the first `)` closes the shape tuple, so
# a `[^)]*` lookahead stops before it ever reaches `dtype` and the fixed call
# gets flagged as unfixed. Caught by testing the detector against the pre- and
# post-fix versions of the bug it was written for (bean qou-d8gq).
ALLOC_NO_DTYPE = re.compile(
    r"^\s*(\w+)\s*=\s*(?:np|numpy)\."
    r"(?:zeros|empty|ones|full)\s*\((?!.*\bdtype\b)")
SUBSCRIPT_FILL = re.compile(r"^\s*(\w+)\s*\[[^\]]+\]\s*=\s*(\w+)")


def scan_param_fill(text: str) -> list[tuple[int, str, str]]:
    """Dtype-less numpy allocations later filled by subscript assignment."""
    if not re.search(r"^\s*(?:import numpy|from numpy)", text, re.M):
        return []
    lines = text.split("\n")
    allocs: dict[str, int] = {}
    for i, ln in enumerate(lines, 1):
        m = ALLOC_NO_DTYPE.match(ln)
        if m:
            allocs[m.group(1)] = i
    if not allocs:
        return []
    out = []
    for i, ln in enumerate(lines, 1):
        m = SUBSCRIPT_FILL.match(ln)
        if m and m.group(1) in allocs and not NOQA_P35.search(ln):
            out.append((i, ln.strip(),
                        f"dtype-less numpy alloc at line {allocs[m.group(1)]} "
                        f"filled by subscript; an mpf here truncates silently"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--self-test", "--selftest", dest="selftest",
                    action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        print("=" * 74)
        print("NUMPY/MPMATH DTYPE-LEAK AUDIT — self-test")
        print("=" * 74)
        return self_test()

    findings: dict[str, list] = {}
    param_fill: dict[str, list] = {}
    scanned = 0
    for p in sorted(ROOT.rglob("*.py")):
        if "_deprecated" in p.parts or ".lake" in p.parts:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        hits = scan_text(text)
        if hits:
            findings[p.relative_to(ROOT).as_posix()] = hits
        pf = scan_param_fill(text)
        if pf:
            param_fill[p.relative_to(ROOT).as_posix()] = pf
        if re.search(r"^\s*(?:import numpy|from numpy)", text, re.M):
            scanned += 1

    if args.json:
        print(json.dumps(findings, indent=2))
        return 0

    print("=" * 74)
    print("NUMPY/MPMATH DTYPE-LEAK AUDIT — silent BLAS-to-Python demotions")
    print("=" * 74)
    print(f"  numpy-importing files    : {scanned}")
    print(f"  files with candidates    : {len(findings)}")
    print(f"  candidate lines          : {sum(len(v) for v in findings.values())}")
    print()
    print(f"  ADVISORY param-fill      : {len(param_fill)} file(s), "
          f"{sum(len(v) for v in param_fill.values())} line(s)")
    if param_fill:
        print()
        print("  UNDERCOUNTS by ~30%: these are regexes approximating an AST")
        print("  question. An independent scope-aware AST reference over the same")
        print("  corpus finds 91 lines / 37 files where these find 64 / 33 — 27")
        print("  lines missed, chiefly multi-line allocations where the `dtype=`")
        print("  kwarg or the subscript target falls on a continuation line.")
        print("  Treat the count as a FLOOR, not a total (bean qou-d8gq).")
        print()
        print("  Dtype-less numpy allocations filled by subscript. NOT a defect")
        print("  list — `dtype=` is optional in honest f64 code. These are the")
        print("  places an mpf handed in through a PARAMETER would be truncated")
        print("  silently, which the main scan cannot see (it requires a local")
        print("  mpmath import). Bean qou-d8gq measured one at 642x.")
        for path, hits in sorted(param_fill.items(), key=lambda kv: -len(kv[1]))[:12]:
            print(f"    {path}  ({len(hits)})")
            for ln, src, _why in hits[:2]:
                print(f"       L{ln}: {src[:72]}")
        print()
    if not findings:
        print("  No BLOCKING candidates. (The known instance in hoefsmit_numpy.py")
        print("  is fixed; the other four d_for_ctype consumers already cast.)")
        return 0

    for path, hits in sorted(findings.items(), key=lambda kv: -len(kv[1])):
        print(f"  {path}  ({len(hits)})")
        for ln, src, why in hits[:4]:
            print(f"      {ln:>5}: {src[:88]}")
            print(f"             {why}")
    print()
    print("  These are CANDIDATES — an agent decides. The question for each:")
    print("  does an mpmath value reach a numpy array without a float() cast?")
    print("  If yes, the array silently becomes dtype=object and every later")
    print("  operation on it leaves BLAS. Measured cost: ~4000x (bean qou-5qwb).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
