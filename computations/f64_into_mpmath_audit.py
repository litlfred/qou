#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; runs nothing, writes no witness.
"""Find float64 substrate constants being fed into high-precision paths.

Owner directive: NO FLOAT64. This is the static detector for the shape that
directive keeps being violated by — not a proximity heuristic, a check on
which NAME a script reads.

## Why a name check finds real defects

`q_parameter` exports the same quantity twice: `Q` is a Python float (~17
significant digits), `Q_MP` / `Q_50_DIGIT_STR` carry the full 50. `pyhecke.gram`
does the same with `h`. Reading the f64 name and then computing at 50 dps
produces a number that is *typed* as high precision and is not.

Three live examples, all found this way and all now fixed:

  * `mass_at_3A_proper.atom_braid_word_3A` used the f64 `gram.h` for every
    crossing offset, so the braid word entered a 50-dps χ computation with 17
    good digits. The dual-path cross-check bottomed out at ~1e-16 for every
    atom; it now reaches ~1e-50.
  * `mass_binding_dashboard` built its q₀⁻¹ leg by dividing into
    `mp.mpf(str(q_parameter.Q))`, so the inverse-anchor leg was capped while
    the forward leg was not.
  * `chi_convention_from_values_audit` recomputed with `_avg_color_delta()`
    (f64 internally) to check witnesses that had gone exact — the audit became
    the coarser side of its own comparison.

## The tiers, and which of them can fail a run

Two tiers are **defects** and set the exit status:

`LAUNDERED` is `mpf(str(X))` where X is an f64 constant. That idiom converts a
double to a high-precision TYPE while preserving only its 17 digits, and it is
the most misleading form because the result looks exact at every later
inspection — `type()` says mpf, `mp.nstr(..., 50)` prints 50 digits. There is
no legitimate reason to write it: if you want the value, read the `_MP` or
`_50_DIGIT_STR` name.

`F64_CAST` is `float(X)` for an f64 X in a **value position** — the cast feeds
arithmetic, a comparison, a matrix entry, a cache key, a `json.dump`. This tier
is what the LAUNDERED-only reading of this audit missed for months: a sweep
could report "LAUNDERED — none" while 200-odd casts of `Q` / `HA_VAL` / `gram.z`
sat in the tree (bean `qou-840k`). Two shapes worth naming, both real:
`BlockCache(float(Q0), float(HA_VAL))` seeds a cache with doubles, and
`abs(float(q_val) - float(Q_0_FLOAT)) < 1e-12` gates a witness cache on one.

Be precise about what the cast does: `Q` is *already* a Python float, so
`float(Q)` destroys no precision **at that line** — it is idempotent. What the
tier localises is the line where a double enters a computation, i.e. the exact
place to edit when rewriting the module onto `Q_MP`. The precision was lost at
the import, not the cast; the cast is where you can see it.

Three tiers are **circumstantial** — REPORTED, never auto-failed. Reading them
as a defect list would be wrong; they are lists of places to look:

`NUMPY_ON_Q` is a numpy allocation/contraction kernel (`eye`, `trace`, `array`,
`zeros`, `dot`, `matmul`) in a module that both holds an f64 q-derived name and
uses mpmath. numpy is f64 by construction, so a q-derived matrix that goes
through one comes back a double — but plenty of modules run an unrelated numpy
kernel beside unrelated mpmath work, and the AST cannot tell which. Look, do
not bulk-edit.

`F64_DISPLAY` is a `float()` cast whose value can only reach a human — an
f-string, a `print`, a `%`-format, a `.format()`. **This is not a precision
defect**, and it is split out from `F64_CAST` precisely so the defect count is
not inflated by it: rendering `f"q0 = {float(Q):.6f}"` destroys nothing the
pipeline goes on to use. Do not "fix" these; converting them to mpmath makes
output uglier and the numbers no better.

`F64_ENGINE_ENTRY` is a call to a `pyhecke_native` entry point that HAS an
exact MPFR sibling — `chi_lambda_braid` when `chi_lambda_braid_mpfr` exists.
The f64 entry is not wrong by itself (it is ~10-30x faster and plenty of
callers want that); what makes a site actionable is calling it and then
serialising the result at more digits than f64 carries. Measured at the proton
q0, the f64 and MPFR paths agree to ~15-16 significant digits and diverge
after, so a witness carrying 50 digits of such a value carries ~35 of noise.
CIRCUMSTANTIAL — check what the caller does with the result.

This class was invisible here until 2026-08-24: `scan_source` returned early
for any module holding no f64 q-name, and a module can pass its own q straight
into the engine. 111 call sites in 63 files went unreported.

`F64_IMPORT` is a module that imports an f64 constant and also uses mpmath,
with no cast and no kernel found. The weakest signal of the six.

The display/value split is a one-directional walk up the AST (see
`_is_display_only`): a cast is display-only when its ancestors, passing through
format-transparent wrappers (`str`, `repr`, `round`, `abs`, tuples, arithmetic),
terminate in a rendering sink. Anything else — including `json.dump({"q":
float(Q)})`, which writes a double into a witness — is a value position.

Read-only and static: parses sources, imports nothing, runs no producer, writes
no witness. Safe beside any other work — including beside a running witness
wave, which is why it was widened while wave 4 held the tree.

Usage:
    python3 computations/f64_into_mpmath_audit.py
    python3 computations/f64_into_mpmath_audit.py --tier LAUNDERED
    python3 computations/f64_into_mpmath_audit.py --tier F64_CAST
    python3 computations/f64_into_mpmath_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# f64-valued substrate names. Their high-precision partners are the `_MP`
# suffix and `Q_50_DIGIT_STR`; anything here is a double by construction.
F64_NAMES = {
    "Q", "Q_INV", "HA", "HA_VAL", "HBAR_Q", "HBAR_Q_SQ", "LN_Q", "TANH_LN_Q",
    "E_CROSS", "S_SKEIN", "TWO_Q",
}
# `pyhecke.gram` re-exports the same doubles under shorter names.
F64_GRAM = {"h", "q0", "qi", "z"}
MP_MODULES = {"mpmath"}

# Modules read as objects rather than unpacked: `from pyhecke import gram` then
# `float(gram.z)`. Only these three names are treated as f64-bearing modules —
# matching on the module path alone would take `q_parameter.Q_50_DIGIT_STR` for
# a module.
MODULE_ATTRS = {"gram", "constants", "q_parameter"}

NUMPY_MODULES = {"numpy"}
# Allocation + contraction + the trace-like reductions: the calls through which
# a q-derived value would actually enter an f64 array. Not every numpy call —
# `np.argmax` over an index array says nothing about precision.
NUMPY_KERNEL_OPS = {"eye", "trace", "array", "zeros", "dot", "matmul"}

# Rendering sinks: past one of these the value is text a human reads.
DISPLAY_SINK_CALLS = {"print"}
DISPLAY_SINK_METHODS = {"format", "write", "warn", "debug", "info", "warning",
                        "error"}
# Wrappers a value passes THROUGH without becoming a computed quantity. `str`
# is transparent rather than a sink on purpose: `mpf(str(float(Q)))` must not
# read as display.
DISPLAY_TRANSPARENT_CALLS = {"str", "repr", "round", "abs", "float"}
DISPLAY_MAX_DEPTH = 6


def _pool_for(module: str) -> set | None:
    """Which f64 name pool a module path exports, or None.

    `q_parameter` is the back-compat shim under `computations/substrate/`;
    `qou_substrate.constants` is the canonical module it re-exports from, and
    was invisible to this audit until 2026-08-09 — 11 modules import their `Q`
    straight from it, bypassing the shim.
    """
    if module.endswith("gram"):
        return F64_GRAM
    if "q_parameter" in module or module.startswith("qou_substrate"):
        return F64_NAMES
    return None


def _mpmath_aliases(tree: ast.AST) -> set[str]:
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name in MP_MODULES:
                    out.add(a.asname or a.name)
        elif isinstance(n, ast.ImportFrom) and n.module in MP_MODULES:
            for a in n.names:
                out.add(a.asname or a.name)
    return out


def _numpy_aliases(tree: ast.AST) -> tuple[set[str], set[str]]:
    """(module aliases, bare kernel names).

    `import numpy as np` gives the first; `from numpy import trace` gives the
    second, which no attribute walk would ever see.
    """
    mods, bare = set(), set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name in NUMPY_MODULES:
                    mods.add(a.asname or a.name)
        elif isinstance(n, ast.ImportFrom) and n.module in NUMPY_MODULES:
            for a in n.names:
                if a.name in NUMPY_KERNEL_OPS:
                    bare.add(a.asname or a.name)
    return mods, bare


def f64_imports(tree: ast.AST) -> dict:
    """Local name -> origin, for every f64 substrate constant imported.

    Follows `as` renaming, which matters: the dashboard defect was
    `from q_parameter import Q as Q0_val`, invisible to a search for `Q`.
    """
    out = {}
    for n in ast.walk(tree):
        if not isinstance(n, ast.ImportFrom) or not n.module:
            continue
        pool = _pool_for(n.module)
        if pool is None:
            continue
        for a in n.names:
            if a.name in pool:
                out[a.asname or a.name] = f"{n.module}.{a.name}"
    return out


def f64_module_aliases(tree: ast.AST) -> dict:
    """Local alias -> (origin module, name pool), for `float(gram.z)` reads.

    Covers the two shapes the corpus uses — `from pyhecke import gram` and
    `import pyhecke.gram as gram`. A bare dotted `import pyhecke.gram` (read as
    `pyhecke.gram.z`) has no corpus instance and would need an attribute-chain
    walk; it is deliberately not handled rather than half-handled.
    """
    out = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                pool = _pool_for(a.name) if a.asname else None
                if pool is not None:
                    out[a.asname] = (a.name, pool)
        elif isinstance(n, ast.ImportFrom) and n.module:
            for a in n.names:
                if a.name not in MODULE_ATTRS:
                    continue
                dotted = f"{n.module}.{a.name}"
                pool = _pool_for(dotted)
                if pool is not None:
                    out[a.asname or a.name] = (dotted, pool)
    return out


def _parents(tree: ast.AST) -> dict:
    """child node -> parent node, so a cast's context can be walked upward."""
    out = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            out[child] = parent
    return out


def _is_str_const(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and isinstance(node.value, str)


def _is_display_only(node: ast.AST, parents: dict) -> bool:
    """True when this expression's value can only reach a human-readable sink.

    One-directional: walk up through format-transparent wrappers and answer
    True only on reaching a sink. Every other context — an assignment, a
    comparison, a dict value, an argument to anything not listed — answers
    False, so the default is "this is a value" and a display verdict has to be
    earned. Bounded at DISPLAY_MAX_DEPTH so a pathological nest cannot hang it.
    """
    cur = node
    for _ in range(DISPLAY_MAX_DEPTH):
        p = parents.get(cur)
        if p is None:
            return False
        if isinstance(p, (ast.FormattedValue, ast.JoinedStr)):
            return True
        if isinstance(p, ast.BinOp) and (_is_str_const(p.left)
                                         or _is_str_const(p.right)):
            return True  # "%.6f" % x  /  "q=" + x
        if isinstance(p, ast.Call):
            f = p.func
            if getattr(f, "id", None) in DISPLAY_SINK_CALLS:
                return True
            if isinstance(f, ast.Attribute) and f.attr in DISPLAY_SINK_METHODS:
                return True
            if getattr(f, "id", None) in DISPLAY_TRANSPARENT_CALLS:
                cur = p
                continue
            return False
        if isinstance(p, (ast.Tuple, ast.List, ast.UnaryOp, ast.BinOp,
                          ast.keyword)):
            cur = p
            continue
        return False
    return False


def _f64_origin(node: ast.AST, names: dict, mods: dict) -> str | None:
    """Origin string if this expression names an f64 constant, else None."""
    nm = getattr(node, "id", None)
    if nm in names:
        return names[nm]
    if isinstance(node, ast.Attribute):
        entry = mods.get(getattr(node.value, "id", None))
        if entry and node.attr in entry[1]:
            return f"{entry[0]}.{node.attr}"
    return None


def laundered_calls(tree: ast.AST, names: dict, aliases: set[str]) -> list:
    """`mpf(str(X))` / `mp.mpf(str(X))` for an f64 X. Returns [(line, origin)].

    Matched structurally rather than by regex so `mp.mpf(str(Q0_val))`,
    `mpmath.mpf(str(Q))` and a bare `mpf(str(h))` all land, and a legitimate
    `mpf(str(Q_50_DIGIT_STR))` does not.
    """
    hits = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call) or not n.args:
            continue
        f = n.func
        is_mpf = (getattr(f, "id", None) == "mpf"
                  or (isinstance(f, ast.Attribute) and f.attr == "mpf"
                      and getattr(f.value, "id", None) in aliases | {"mp"}))
        if not is_mpf:
            continue
        inner = n.args[0]
        if not (isinstance(inner, ast.Call)
                and getattr(inner.func, "id", None) == "str" and inner.args):
            continue
        target = inner.args[0]
        nm = getattr(target, "id", None)
        if nm in names:
            hits.append((getattr(n, "lineno", 0), names[nm]))
    return hits


def f64_casts(tree: ast.AST, names: dict, mods: dict,
              parents: dict) -> tuple[list, list]:
    """`float(X)` for an f64 X. Returns (value-position, display-only) hits.

    The split is the whole point of the tier: a cast in a value position is a
    precision defect, a cast that only feeds an f-string is a formatting
    convenience. Counting them together would report a number nobody can act on.
    """
    value, display = [], []
    for n in ast.walk(tree):
        if (not isinstance(n, ast.Call)
                or getattr(n.func, "id", None) != "float" or not n.args):
            continue
        origin = _f64_origin(n.args[0], names, mods)
        if origin is None:
            continue
        hit = (getattr(n, "lineno", 0), origin)
        (display if _is_display_only(n, parents) else value).append(hit)
    return value, display


def numpy_kernel_ops(tree: ast.AST, mods: set[str], bare: set[str]) -> list:
    """[(line, op)] for numpy allocation/contraction calls in this module."""
    hits = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if (isinstance(f, ast.Attribute) and f.attr in NUMPY_KERNEL_OPS
                and getattr(f.value, "id", None) in mods):
            hits.append((getattr(n, "lineno", 0), f"np.{f.attr}"))
        elif getattr(f, "id", None) in bare:
            hits.append((getattr(n, "lineno", 0), f"np.{f.id}"))
    return hits


# `pyhecke_native` entry points that have an EXACT (MPFR) sibling.
#
# Hardcoded on purpose: `pyhecke_native` is NOT on PyPI (404, no publish step
# in its workflow), so a container without the extension built is the DEFAULT,
# not an anomaly. Deriving this table by `dir(pyhecke_native)` would make the
# audit silently report zero on exactly the machines most likely to run it.
# `--self-test` checks the table against the live module when it IS importable.
#
# The f64 entry is not a defect by itself — it is ~10-30x faster and plenty of
# callers legitimately want that. What makes a site actionable is calling it
# and then SERIALISING the result at more digits than f64 carries. Measured
# 2026-08-24 against `chi_lambda_braid_mpfr` at 50 dps, proton q0:
#
#     H3  sigma_1        rel diff 2.917e-16
#     H3  borromean-ish  rel diff 7.746e-16
#     H6  deuteron-ish   rel diff 7.362e-16
#
# i.e. ~15-16 real digits. A witness carrying 50 is carrying ~35 of noise.
# The MPFR entry takes `q_str` as a DECIMAL STRING specifically to avoid the
# lossy f64 conversion at the boundary — its own docstring says so.
NATIVE_EXACT_SIBLING = {
    "chi_lambda_all_partitions_f64": "chi_lambda_all_partitions_mpfr",
    "chi_lambda_braid": "chi_lambda_braid_mpfr",
    "chi_lambdas_braid": "chi_lambdas_braid_mpfr",
    "chi_q_atomic": "chi_q_atomic_mpfr",
    "chi_q_atomic_all_partitions": "chi_q_atomic_all_partitions_mpfr",
}


# The Python wrapper around the same kernel. Its `precision=` keyword selects
# the path and DEFAULTS TO f64 ("Default: f64 fast path" —
# `hecke/hecke_characters.py`), so a caller that omits it silently gets f64
# even though `precision="mpfr_50dps"` is one keyword away. Measured
# 2026-08-24: 20 of 30 wrapper call sites omit it.
#
# Worth knowing before "fixing" one: the wrapper handles the boundary
# correctly when asked. Passing `q_value` as a STRING routes it to MPFR
# untouched; passing a float makes it `format(float(q), ...)` first, which its
# own comment calls "implicit acceptance of f64 boundary loss". So the fix is
# `precision="mpfr_50dps"` AND a string q, not the keyword alone.
WRAPPER_MODULES = {"hecke_characters", "hecke.hecke_characters"}


def wrapper_default_f64_calls(tree: ast.AST) -> list:
    """[(line, "fn(precision=?)")] for wrapper calls that omit `precision=`."""
    bare: set[str] = set()
    mods: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and (n.module or "") in WRAPPER_MODULES:
            bare |= {a.asname or a.name for a in n.names
                     if a.name in NATIVE_EXACT_SIBLING}
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.name in WRAPPER_MODULES:
                    mods.add(a.asname or a.name.split(".")[-1])
    if not bare and not mods:
        return []
    hits = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        fn = None
        if (isinstance(f, ast.Attribute) and getattr(f.value, "id", None) in mods
                and f.attr in NATIVE_EXACT_SIBLING):
            fn = f.attr
        elif isinstance(f, ast.Name) and f.id in bare:
            fn = f.id
        if fn and not any(k.arg == "precision" for k in n.keywords):
            hits.append((getattr(n, "lineno", 0), f"{fn}(precision=?)"))
    return hits


_MPFR_CALL = re.compile(r"\b\w+_mpfr\s*\(")


def native_entry_disposition(src: str) -> str:
    """Split an F64_ENGINE_ENTRY module into deliberate / harmless / actionable.

    Encodes the triage rule directly: the f64 entry is ~10-30x faster and is
    frequently the RIGHT call, so what makes a site actionable is not the call
    but whether the module then SERIALISES above what f64 carries (~15-16
    significant digits, measured).

    Two hand-verified cases the raw count would have mis-sold, both of which
    this proxy classifies correctly:

    * `chi_4he_binding_lossless.py` calls the f64 entry ON PURPOSE, as a
      same-convention cross-check floor for its MPFR result. Its own comment
      says so. -> deliberate.
    * `atomic_chirality_residue.py` does `float(mp.log(abs(chi)))` three lines
      after the call; the whole downstream is f64, so MPFR would buy nothing.
      -> harmless.

    A proxy, not a verdict: confirm per site before editing.
    """
    if _MPFR_CALL.search(src):
        return "deliberate"
    if re.search(r"\bfmt\s*\(", src):
        return "actionable"
    for m in re.finditer(r"nstr\s*\([^,]+,\s*([A-Za-z_0-9]+)", src):
        tok = m.group(1)
        # A non-literal is a `dps` variable, which is >= 18 everywhere here.
        if not tok.isdigit() or int(tok) >= 18:
            return "actionable"
    return "harmless"


def native_f64_entry_calls(tree: ast.AST) -> list:
    """[(line, "fn -> fn_mpfr")] for calls to an f64 native entry that has an
    exact sibling.

    Matches both `pyhecke_native.chi_lambda_braid(...)` and a bare
    `chi_lambda_braid(...)` brought in by `from pyhecke_native import ...`.
    A local function of the same name would false-positive; the bare form is
    therefore only honoured when the module actually imports that name from
    `pyhecke_native`.
    """
    bare: set[str] = set()
    mods: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and (n.module or "") == "pyhecke_native":
            bare |= {a.asname or a.name for a in n.names
                     if a.name in NATIVE_EXACT_SIBLING}
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.name == "pyhecke_native":
                    mods.add(a.asname or a.name)
    hits = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        fn = None
        if isinstance(f, ast.Attribute) and getattr(f.value, "id", None) in mods:
            fn = f.attr
        elif isinstance(f, ast.Name) and f.id in bare:
            fn = f.id
        if fn in NATIVE_EXACT_SIBLING:
            hits.append((getattr(n, "lineno", 0),
                         f"{fn} -> {NATIVE_EXACT_SIBLING[fn]}"))
    return hits


def scan_source(src: str) -> dict:
    """Classify one module. Pure over text — self-tested below.

    Always returns the full evidence (`laundered` / `casts` / `display` /
    `numpy` / `f64`); `tier` is only the headline severity, so a caller
    tiering by blast radius can read the counts without re-deriving them.
    """
    blank = {"tier": None, "laundered": [], "casts": [], "display": [],
             "numpy": [], "native": [], "f64": {}}
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return blank
    native = native_f64_entry_calls(tree) + wrapper_default_f64_calls(tree)
    names = f64_imports(tree)
    mods = f64_module_aliases(tree)
    if not names and not mods:
        # A module can reach the f64 engine without importing any f64 q-name —
        # it passes its own q straight in. That whole class was invisible here
        # until 2026-08-24 because this early return fired first.
        if native:
            return {"tier": "F64_ENGINE_ENTRY", "laundered": [], "casts": [],
                    "display": [], "numpy": [], "native": native, "f64": {}}
        return blank
    aliases = _mpmath_aliases(tree)
    parents = _parents(tree)
    laundered = laundered_calls(tree, names, aliases)
    casts, display = f64_casts(tree, names, mods, parents)
    numpy = numpy_kernel_ops(tree, *_numpy_aliases(tree))

    if laundered:
        tier = "LAUNDERED"
    elif casts:
        tier = "F64_CAST"
    elif native:
        tier = "F64_ENGINE_ENTRY"
    elif numpy and aliases:
        tier = "NUMPY_ON_Q"
    elif display:
        tier = "F64_DISPLAY"
    elif names and aliases:
        tier = "F64_IMPORT"
    else:
        # Holds an f64 but never reaches mpmath: not this audit's business.
        tier = None
    return {"tier": tier, "laundered": laundered, "casts": casts,
            "display": display, "numpy": numpy, "native": native,
            "f64": names}


Q50 = "Q_50_DIGIT_STR"
CASES = [
    ("the laundering idiom is a defect",
     "import mpmath as mp\nfrom q_parameter import Q\nx = mp.mpf(str(Q))\n",
     "LAUNDERED"),
    # The dashboard's actual shape: renamed on import, so a text search for
    # "mpf(str(Q))" misses it entirely.
    ("renamed on import is still caught",
     "import mpmath as mp\nfrom q_parameter import Q as Q0_val\n"
     "x = mp.mpf(str(Q0_val))\n", "LAUNDERED"),
    ("bare mpf() is caught",
     "from mpmath import mpf\nfrom q_parameter import HA\ny = mpf(str(HA))\n",
     "LAUNDERED"),
    ("gram's short names count too",
     "import mpmath as mp\nfrom pyhecke.gram import h\nz = mp.mpf(str(h))\n",
     "LAUNDERED"),
    # The whole point of the name check: same shape, correct source.
    (f"mpf(str({Q50})) is CORRECT, not a hit",
     f"import mpmath as mp\nfrom q_parameter import {Q50}\n"
     f"x = mp.mpf(str({Q50}))\n", None),
    ("the _MP family is correct too",
     "import mpmath as mp\nfrom q_parameter import Q_MP\nx = Q_MP * 2\n", None),

    # --- F64_CAST: the tier the LAUNDERED-only reading missed (qou-840k) ---
    ("a cast in a value position is a defect",
     "import mpmath as mp\nfrom q_parameter import Q\n"
     "x = mp.mpf(1) / float(Q)\n", "F64_CAST"),
    # wedderburn_jones_markov.y_lambda_at's cache gate, in miniature.
    ("a cast inside a tolerance comparison is a defect",
     "import mpmath as mp\nfrom q_parameter import Q as Q_0_FLOAT\n"
     "hit = abs(float(q_val) - float(Q_0_FLOAT)) < 1e-12\n", "F64_CAST"),
    ("a cast read through a module alias is caught",
     "import mpmath as mp\nfrom pyhecke import gram\nz = float(gram.z)\n",
     "F64_CAST"),
    # 11 modules import Q from the canonical module, bypassing the shim.
    ("qou_substrate.constants exports the same doubles",
     "import mpmath as mp\nfrom qou_substrate.constants import Q\n"
     "x = float(Q) * 2\n", "F64_CAST"),
    # A double written into a witness is the opposite of display: it persists.
    ("a cast into a json payload is a defect, not display",
     "import json\nimport mpmath as mp\nfrom q_parameter import Q\n"
     "json.dump({'q': float(Q)}, fh)\n", "F64_CAST"),
    # `str` is transparent, not a sink — otherwise this would read as display.
    ("laundering through a cast is a value position",
     "import mpmath as mp\nfrom q_parameter import Q\n"
     "x = mp.mpf(str(float(Q)))\n", "F64_CAST"),

    # --- F64_DISPLAY: split out so it cannot inflate the defect count ---
    ("a cast that only feeds an f-string is NOT a precision defect",
     "import mpmath as mp\nfrom q_parameter import Q\n"
     "print(f'q0 = {float(Q):.6f}')\n", "F64_DISPLAY"),
    ("%-formatting is display too",
     "import mpmath as mp\nfrom q_parameter import Q\n"
     "s = '%.6f' % float(Q)\n", "F64_DISPLAY"),
    ("a rounded cast inside a format call is still display",
     "import mpmath as mp\nfrom q_parameter import Q\n"
     "s = '{}'.format(round(float(Q), 6))\n", "F64_DISPLAY"),
    ("bare print(float(X)) is display",
     "import mpmath as mp\nfrom q_parameter import Q\nprint(float(Q))\n",
     "F64_DISPLAY"),

    # --- NUMPY_ON_Q: circumstantial, requires both an f64 name and mpmath ---
    ("a numpy kernel beside mpmath on a q-holding module is circumstantial",
     "import mpmath as mp\nimport numpy as np\nfrom q_parameter import Q\n"
     "M = np.eye(3)\n", "NUMPY_ON_Q"),
    ("a bare `from numpy import trace` is caught too",
     "import mpmath as mp\nfrom numpy import trace\nfrom q_parameter import Q\n"
     "t = trace(M)\n", "NUMPY_ON_Q"),
    # An f64 held for a numpy kernel with no mpmath anywhere is out of scope —
    # flagging it would bury the real hits under hundreds of non-findings.
    ("f64 with no mpmath at all is out of scope",
     "import numpy as np\nfrom q_parameter import Q\na = np.array([Q])\n",
     None),

    # --- F64_ENGINE_ENTRY: the class the early return used to hide ---
    ("a native f64 entry with an exact sibling is caught",
     "import pyhecke_native\n"
     "c = pyhecke_native.chi_lambda_braid([2, 1], w, 1.1)\n",
     "F64_ENGINE_ENTRY"),
    # The case that motivated the tier: NO f64 q-name is imported, so every
    # other detector returns blank and `scan_source` used to return early.
    ("caught even with no f64 q-name imported at all",
     "import mpmath as mp\nimport pyhecke_native\n"
     "c = mp.mpf(str(pyhecke_native.chi_q_atomic(3, 2, 1.1)))\n",
     "F64_ENGINE_ENTRY"),
    ("a bare from-import of the f64 entry is caught",
     "from pyhecke_native import chi_lambdas_braid\n"
     "c = chi_lambdas_braid([2, 1], w, 1.1)\n", "F64_ENGINE_ENTRY"),
    ("aliased on import is still caught",
     "import pyhecke_native as pn\nc = pn.chi_lambda_braid([2, 1], w, 1.1)\n",
     "F64_ENGINE_ENTRY"),
    # The whole point of the tier is that an exact sibling EXISTS. Calling the
    # MPFR entry is the fix, so it must never be flagged as the problem.
    ("calling the MPFR sibling is NOT flagged",
     "import pyhecke_native\n"
     "c = pyhecke_native.chi_lambda_braid_mpfr([2, 1], w, qs, 50)\n", None),
    ("a native entry with no exact sibling is out of scope",
     "import pyhecke_native\ng = pyhecke_native.gram_matrix(3, 1.1)\n", None),
    # A same-named local function is a real false-positive risk, so the bare
    # form is honoured only when the name is actually imported from the engine.
    ("a same-named local function is not the engine",
     "def chi_lambda_braid(a, b, c):\n    return 0\n"
     "x = chi_lambda_braid([2, 1], w, 1.1)\n", None),
    # A cast is a defect; an engine entry is a choice. Severity must not flip.
    ("F64_CAST still outranks an engine entry in the same module",
     "import mpmath as mp\nimport pyhecke_native\n"
     "from q_parameter import Q\nx = mp.mpf(1) * float(Q)\n"
     "c = pyhecke_native.chi_lambda_braid([2, 1], w, float(Q))\n",
     "F64_CAST"),

    # --- the wrapper hop: `precision=` defaults to f64 ---
    ("a wrapper call omitting precision= gets the f64 default",
     "from hecke_characters import chi_lambda_braid\n"
     "c = chi_lambda_braid(shape, word)\n", "F64_ENGINE_ENTRY"),
    ("passing precision= is the fix, so it is NOT flagged",
     "from hecke_characters import chi_lambda_braid\n"
     "c = chi_lambda_braid(shape, word, precision='mpfr_50dps')\n", None),
    ("the wrapper reached as a module attribute is caught",
     "import hecke_characters\n"
     "c = hecke_characters.chi_q_atomic(3, 2, q)\n", "F64_ENGINE_ENTRY"),
    # `closed_form_tau_M.py` names these as CONVENTION strings; a text search
    # counts them as calls. Measured: that mistake inflated a census 120 vs 51.
    ("the same name as a string literal is not a call",
     "PnConvention = ['chi_lambda_braid', 'strict_averaged']\n", None),

    ("f64 import beside mpmath, no cast, no kernel, is the weakest tier",
     "import mpmath as mp\nfrom q_parameter import Q\nQ_LOCAL = Q\n",
     "F64_IMPORT"),
    ("a module touching neither is silent", "x = 1\n", None),
    ("unparseable source is skipped, not guessed", "def (\n", None),
]


def self_test() -> int:
    fails = 0
    for label, src, want in CASES:
        got = scan_source(src)["tier"]
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    # The detector must not fire on its OWN prose, which quotes every idiom.
    ok = scan_source(Path(__file__).read_text(encoding="utf-8"))["tier"] is None
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  the audit does not flag itself")
    total = len(CASES) + 1

    # The pair table is hardcoded so the audit works without the extension
    # (pyhecke_native is not on PyPI). When it IS importable, check the table
    # against reality — a hardcoded table decays exactly like a hardcoded
    # count, and a NEW f64/mpfr pair added to the Rust crate would otherwise
    # go unaudited forever with nothing to notice.
    try:
        import pyhecke_native as _pn  # noqa: PLC0415
    except Exception:  # noqa: BLE001
        print("  skip  NATIVE_EXACT_SIBLING vs live module "
              "(pyhecke_native not importable — this is the DEFAULT, "
              "it is not published)")
    else:
        live = {x for x in dir(_pn) if not x.startswith("_")}
        derived = {}
        for n in live:
            if n.endswith("_mpfr") and n[:-5] in live:
                derived[n[:-5]] = n
            if n.endswith("_f64") and n[:-4] + "_mpfr" in live:
                derived[n] = n[:-4] + "_mpfr"
        ok = derived == NATIVE_EXACT_SIBLING
        fails += not ok
        total += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  NATIVE_EXACT_SIBLING matches "
              f"the live module")
        if not ok:
            for k in sorted(set(derived) - set(NATIVE_EXACT_SIBLING)):
                print(f"        MISSING from the table: {k} -> {derived[k]}")
            for k in sorted(set(NATIVE_EXACT_SIBLING) - set(derived)):
                print(f"        STALE in the table:     {k}")

    print(f"\n{total - fails}/{total} passed")
    return 1 if fails else 0


def _iter_rows(tier: str | None):
    """[(tier, relpath, record)] for every in-scope module under ROOT."""
    rows = []
    for p in sorted(ROOT.rglob("*.py")):
        # `.claude` excluded because agent worktrees live under
        # `.claude/worktrees/<agent-id>/` — a full second checkout of the repo,
        # gitignored (.gitignore:120) and carrying 0 tracked files. Without
        # this, every scanned file appears TWICE and every count this audit
        # reports is inflated by whatever agent worktrees happen to exist.
        # Measured on 2026-08-22 with one worktree present: 7321 in-scope .py
        # files, of which 3648 (49.8%) were the mirror — i.e. roughly double.
        #
        # The inflation is environment-dependent, which is the worse property:
        # the same commit audits differently depending on whether an agent
        # worktree is checked out, so the numbers are not reproducible across
        # machines and cannot support a baseline. Its sibling
        # `witness_raw_float64_audit` is correctly scoped (0 worktree hits);
        # this one had simply not been given the exclusion.
        if {"_deprecated", "node_modules", ".lake", ".claude"} & set(p.parts):
            continue
        if p.resolve() == Path(__file__).resolve():
            continue
        try:
            r = scan_source(p.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if r["tier"] and (not tier or r["tier"] == tier):
            rows.append((r["tier"], p.relative_to(ROOT).as_posix(), r))
    return rows


def _print_sites(rows: list, key: str, cap: int = 40) -> None:
    shown = 0
    for _, path, r in rows:
        for line, origin in r[key]:
            if shown >= cap:
                print("  … and more; re-run with --tier for the full list")
                return
            print(f"  {path}:{line}  <- {origin}")
            shown += 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=("LAUNDERED", "F64_CAST",
                                       "F64_ENGINE_ENTRY", "NUMPY_ON_Q",
                                       "F64_DISPLAY", "F64_IMPORT"))
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    rows = _iter_rows(a.tier)
    laundered = [r for r in rows if r[0] == "LAUNDERED"]
    casts = [r for r in rows if r[0] == "F64_CAST"]
    native = [r for r in rows if r[0] == "F64_ENGINE_ENTRY"]
    numpy = [r for r in rows if r[0] == "NUMPY_ON_Q"]
    display = [r for r in rows if r[0] == "F64_DISPLAY"]
    imports = [r for r in rows if r[0] == "F64_IMPORT"]

    if laundered:
        n = sum(len(r["laundered"]) for _, _, r in laundered)
        print(f"LAUNDERED — mpf(str(<f64>)): {len(laundered)} file(s), "
              f"{n} site(s). These are defects.")
        _print_sites(laundered, "laundered", cap=10 ** 6)
    else:
        print("LAUNDERED — none.")

    if casts:
        n = sum(len(r["casts"]) for _, _, r in casts)
        print(f"\nF64_CAST — float(<f64>) in a value position: {len(casts)} "
              f"file(s), {n} site(s). These are defects.")
        # The nuance lives in this module's docstring, which nobody sees when
        # they run the tool — so it is repeated here. Measured 2026-08-24: an
        # agent read the detector and this print block, concluded "the casts
        # are no-ops, the tier is overstated", and spent a sweep re-deriving
        # what the header already said. Second-order cost: the obvious
        # "remedy" for a tier labelled only "defects" is to delete the casts,
        # which drains the counter and changes nothing.
        print("      NOTE: `Q` is ALREADY a float, so `float(Q)` loses nothing "
              "AT THAT LINE.\n"
              "      The tier localises where a double ENTERS A COMPUTATION. "
              "Do NOT drain it by\n"
              "      deleting casts — that is metric-gaming. The fix is at the "
              "IMPORT: read the\n"
              "      `_MP` name and carry mpf through, which is a per-module "
              "decision that\n"
              "      changes numbers. Some sites are correct as-is: a module "
              "built on an f64\n"
              "      engine (`pyhecke.gram`, `BlockCache`, numpy) is an f64 "
              "pipeline by design.")
        _print_sites(casts, "casts")
    else:
        print("\nF64_CAST — none.")

    n_np = sum(len(r["numpy"]) for _, _, r in numpy)
    n_np_all = sum(len(r["numpy"]) for _, _, r in rows)
    print(f"\nNUMPY_ON_Q — numpy kernel in a module holding an f64 q-name and "
          f"using mpmath: {len(numpy)} file(s), {n_np} op(s) where this is the "
          f"worst tier ({n_np_all} op(s) corpus-wide, the rest inside files "
          f"already counted as a defect above). "
          f"CIRCUMSTANTIAL — review, do not bulk-edit.")
    for _, path, r in numpy[:40]:
        ops = ", ".join(sorted({op for _, op in r["numpy"]})[:4])
        print(f"  {path}  ({len(r['numpy'])}x: {ops})")
    if len(numpy) > 40:
        print(f"  … and {len(numpy) - 40} more")

    # Counted over ALL rows, like F64_DISPLAY below: a file whose headline
    # tier is F64_CAST can still call the f64 engine, and that site is just as
    # actionable as one in a file with nothing worse.
    n_nat_all = sum(len(r.get("native", [])) for _, _, r in rows)
    print(f"\nF64_ENGINE_ENTRY — pyhecke_native f64 entry called where an "
          f"exact MPFR sibling exists: {len(native)} file(s) with nothing "
          f"worse, {n_nat_all} site(s) corpus-wide. CIRCUMSTANTIAL.")
    print("      The f64 entry is ~10-30x faster and is often the right "
          "choice. It becomes a\n"
          "      defect when the result is then SERIALISED at more digits "
          "than f64 carries:\n"
          "      measured at the proton q0, f64 and MPFR agree to ~15-16 "
          "significant digits,\n"
          "      so 50 digits in a witness is ~35 of noise. The MPFR entry "
          "takes q as a\n"
          "      DECIMAL STRING to avoid the lossy conversion at the "
          "boundary.")
    # The count alone over-sells the class. Split it by the triage rule, over
    # ALL rows carrying a native site, so the actionable number is reproducible
    # rather than living in someone's scratch file.
    split: dict[str, list] = {"deliberate": [], "harmless": [], "actionable": []}
    for _, path, r in rows:
        if not r.get("native"):
            continue
        try:
            src = (ROOT / path).read_text(encoding="utf-8")
        except OSError:
            continue
        split[native_entry_disposition(src)].append((path, len(r["native"])))
    for k, why in (("deliberate", "also calls an _mpfr entry — a cross-check"),
                   ("harmless", "never serialises above 17 digits"),
                   ("actionable", "serialises wide from an f64 value")):
        v = split[k]
        print(f"      {k:11s} {len(v):3d} file(s) {sum(n for _, n in v):3d} "
              f"site(s)  — {why}")
    print("      ACTIONABLE candidates (a proxy, not a verdict — confirm "
          "per site):")
    for path, n in sorted(split["actionable"]):
        print(f"        {n}x  {path}")

    # Counted over ALL rows: a file whose headline tier is F64_CAST can still
    # carry display casts, and those must not land in the defect count.
    n_disp = sum(len(r["display"]) for _, _, r in rows)
    print(f"\nF64_DISPLAY — float(<f64>) reaching only an f-string / print / "
          f"format: {len(display)} file(s) with nothing worse, {n_disp} "
          f"site(s) corpus-wide. NOT precision defects — do not 'fix' these.")

    print(f"\nF64_IMPORT — imports an f64 constant and uses mpmath, no cast, "
          f"no kernel: {len(imports)} file(s). CIRCUMSTANTIAL.")
    for _, path, r in imports[:40]:
        print(f"  {path}  ({', '.join(sorted(r['f64'])[:4])})")
    if len(imports) > 40:
        print(f"  … and {len(imports) - 40} more")

    print("\nFix by reading the high-precision name: Q_50_DIGIT_STR / the _MP\n"
          "family / flavor_split_leading(q) — not by widening a tolerance.\n"
          "Exit status reflects LAUNDERED + F64_CAST only; "
          "F64_ENGINE_ENTRY,\n"
          "NUMPY_ON_Q, F64_DISPLAY and F64_IMPORT never fail a run.")
    return 1 if (laundered or casts) else 0


if __name__ == "__main__":
    raise SystemExit(main())
