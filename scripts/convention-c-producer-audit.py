#!/usr/bin/env python3
"""Find convention-C definitions of the Markov parameter in live Python producers.

The producer-layer counterpart to `content/pipeline/trace-convention-audit.ts`,
which walks `content/**` only. Nothing walked the producers, and three
successive hand-greps of that surface returned 70, then 13, then 182.

## Why grep cannot do this

The corpus spells `z = 1/(q^{1/2} + q^{-1/2})` at least fifteen ways:

    1.0 / (q0**0.5 + qi0**0.5)          1 / (mp.sqrt(Q0) + 1/mp.sqrt(Q0))
    1.0 / (q0 ** 0.5 + q0 ** (-0.5))    1 / (sp.sqrt(q) + 1/sp.sqrt(q))
    1.0 / (Q0 ** 0.5 + QI ** 0.5)       1 / (np.sqrt(q) + 1.0/np.sqrt(q))
    1 / (q ** mpmath.mpf('0.5') + ...)  1 / (sqrt_q + 1 / sqrt_q)
    1 / (q0**mpf('0.5') + q0**mpf('-0.5'))

with the reciprocal named `q0`, `qi`, `qi0`, `Q_INV`, `_QI0`, `sqrt_q`, `q_val`,
or spelled inline; and the result bound to `z`, `z_mark`, `z_markov`, `Z_MARKOV`,
`z_sym`, `zmkv`, `ZS`, `z_q`, `_z`, ... A regex tuned to any subset silently
misses the rest, and a looser one (`0.5 + `) matches unrelated arithmetic. Both
failure modes actually happened, in that order.

So this walks the **AST**: any assignment whose target name contains `z` and
whose value has the shape `1 / (<something with a square root> + <anything>)`.
Shape-matching, not spelling-matching.

## What counts, and what deliberately does not

* **Deliberately C-named** targets (`z_C`, `z_c`, `z_C_expr`, ...) are excluded.
  A variable that says it is convention C is a labelled comparison, not a defect
  — the same principle the content axis uses for `C_LABEL`.
* **`tools/pyhecke/`** is reported separately, but the excuse comes from the
  REGISTRY, not from the path. Three buckets, in order of how well accounted
  the site is, and **only the first is excused from the actionable count**:

  1. **BLOCKED on C by design** — a `blocked_migrations` row names that exact
     file.
  2. **DECLARED C in `evaluators.z`, R10-waived** — the symbol is a registered
     C evaluator whose module is listed in `intra_module_split_waivers`. R9
     imports it and asserts its value numerically on every run, so this is a
     *stronger* record than a blocked row, which is only prose. It is still
     **actionable**: the waiver says in terms that the split is "an open
     defect, not an approved design". Declaring a thing does not fix it, and a
     declaration that shrinks the count is a way to make the inventory smaller
     without making the corpus better.
  3. **C with NO registry row (unexplained)** — anything else under
     `tools/pyhecke/`. Actionable.

  The path-prefix version was too generous. One row covered `gram.py::z`, and
  three *function-local* C definitions sheltered under the same label — two of
  them inside `gram.py` itself. When `z` migrated to D on 2026-08-15 (bean
  `qou-w8zz`) and the row was resolved, a prefix classifier would have gone on
  calling those three "by design" indefinitely.

  Bucket 2 exists because resolving that row correctly — emptying
  `blocked_migrations` — reclassified four fully-registered sites as
  "unexplained", so the registry and this detector disagreed about the same
  four while both worked as designed. Splitting them also stopped the blanket
  label hiding a real one: `pyhecke/atom.py:691` is a live C `z_mark`, consumed
  at :713, in a module (`pyhecke.atom`) that **no** waiver covers.
* `_deprecated/` is skipped entirely.

Results are stratified, because the layers carry very different risk: a probe
that computes a C-era number for its own consumption is not the same defect as
the shipped `qou-mass` package doing it.

## Usage

    python3 scripts/convention-c-producer-audit.py            # summary
    python3 scripts/convention-c-producer-audit.py --list     # every site
    python3 scripts/convention-c-producer-audit.py --json out.json
    python3 scripts/convention-c-producer-audit.py --selftest

Exit 1 when any non-deliberate site outside the blocked-by-design set is found,
so it can gate. It does **not** currently gate CI — auto-triggers are disabled
repo-wide (owner directive 2026-06-30, Actions billing).
"""

from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOTS = ("computations", "qou-mass", "tools")

#: A target whose own name declares it convention C is a labelled comparison.
DELIBERATE = re.compile(r"(_c\b|_C\b|C_|_c_|zc$|z_c)", re.I)

#: The registry blocks this path on C by design (`blocked_migrations`).
BLOCKED_BY_DESIGN = "tools/pyhecke/"


def is_c_form(node: ast.AST) -> bool:
    """Does this expression have the shape ``1 / (<sqrt-ish> + <anything>)``?

    Deliberately shape-based. It does not try to confirm the second summand is
    the reciprocal of the first — that would need symbolic evaluation, and any
    ``1/(sqrt(...) + ...)`` bound to a ``z``-named variable is worth a human
    look regardless.

    ``**3`` anywhere in the denominator rejects the match: convention D is
    ``q**3/(q**2+1)``, and a stray cube is a strong signal this is not the
    half-argument form.
    """
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return False
    if not (isinstance(node.left, ast.Constant) and node.left.value in (1, 1.0)):
        return False
    den = node.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return False
    # Whitespace-normalised: `ast.unparse` emits `q ** 3`, so a naive `"**3"`
    # test never fires. The selftest caught exactly that.
    src = "".join(ast.unparse(den).split())
    return ("0.5" in src or "sqrt" in src.lower()) and "**3" not in src


def is_c_form_halfarg(node: ast.AST):
    """Convention C written in the HALF-ARGUMENT variable: ``z = r/(r**2 + 1)``.

    With ``r = q^{1/2}``,

        1/(q^{1/2} + q^{-1/2}) = 1/(r + 1/r) = r/(r² + 1)

    so this is the same convention with no square root visible anywhere — no
    ``sqrt`` call, no ``0.5`` exponent, nothing for `is_c_form` to match. It was
    a false-negative class of the audit until `y_lambda_cyclotomic_factor.py:48`
    turned up still on C after the surface had been reported clear.

    The trap is that it looks like convention D. D is ``q**3/(q**2+1)``; this is
    ``r**1/(r**2+1)``, and in the half-argument variable D reads
    ``r**6/(r**4+1)``. Same silhouette, different exponents.

    Returns the base symbol source, or None.
    """
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return None
    num = ast.unparse(node.left)
    den = node.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return None
    d = "".join(ast.unparse(den).split())
    return num if d in (f"{num}**2+1", f"1+{num}**2") else None


def _defines_convention_d(src: str, sym: str) -> bool:
    """Does `src` bind `sym` to the convention-D Markov parameter?

    Matches `<sym> = <base>**3 / (<base>**2 + 1)` modulo whitespace and the
    choice of base name -- the same normalisation `is_c_form` uses, since
    `ast.unparse` spells it `q ** 3`. Assignment only, at module level or not;
    a comment mentioning D does not count.
    """
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return False
    for n in ast.walk(tree):
        if not isinstance(n, (ast.Assign, ast.AnnAssign)):
            continue
        targets = n.targets if isinstance(n, ast.Assign) else [n.target]
        if not any(isinstance(t, ast.Name) and t.id == sym for t in targets):
            continue
        if n.value is None:
            continue
        s = "".join(ast.unparse(n.value).split())
        base = s.split("**3", 1)[0]
        if base and s in (f"{base}**3/({base}**2+1)", f"{base}**3/(1+{base}**2)"):
            return True
    return False


def _module_path_of(file: str) -> str:
    """`tools/pyhecke/python/pyhecke/gram.py` -> `pyhecke.gram`.

    The LAST occurrence of the package name is the package root; the first is
    the containing directory, which yields the nonsense
    `pyhecke.python.pyhecke.gram`. The selftest caught exactly that, which is
    why this is a named function with its own fixtures rather than four lines
    inline reading from the live registry.
    """
    parts = pathlib.Path(file).with_suffix("").parts
    pkg = next((c for c in reversed(parts[:-1])
                if c not in ("python", "src", "tools", "lib")), None)
    if pkg and pkg in parts:
        i = len(parts) - 1 - parts[::-1].index(pkg)
        return ".".join(parts[i:])
    return parts[-1] if parts else file


def declared_c_files(repo: pathlib.Path):
    """Files whose C is DECLARED in the registry — registered, not unexplained.

    `blocked_migrations` is no longer the only way the registry accounts for a
    convention-C symbol. A site can also be recorded as a C entry under
    `evaluators.z`, where R9 imports it and asserts its value numerically, with
    its module listed in `intra_module_split_waivers`. That is a STRONGER
    record than a blocked row ever was: a blocked row is prose, an evaluator
    entry is checked against the running code on every validator run.

    Without this, emptying `blocked_migrations` -- which is what resolving the
    gram.py row correctly DID -- silently reclassifies four fully-registered
    sites as "NO registry row (unexplained)". The registry and this detector
    then disagree about the same four sites while both are working as designed.

    Declared does NOT mean excused. The R10 waiver says in terms that the split
    is "an open defect, not an approved design", so these stay ACTIONABLE and
    stay in the count; only the LABEL changes. A positive declaration has to be
    visible in the count rather than swallowed by it, or the declaration
    becomes a way to make the inventory smaller without making the corpus
    better.
    """
    reg = repo / "docs/coordination/trace-convention-registry.json"
    try:
        r = json.loads(reg.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    waived = set(r.get("intra_module_split_waivers", []))
    out: dict[str, list] = {}
    for e in r.get("evaluators", {}).get("z", []):
        if e.get("convention") != "C":
            continue
        mod, sym = e.get("module", ""), e.get("symbol", "")
        if mod not in waived:
            continue
        f = e.get("file") or _file_of_module(repo, mod)
        if f:
            out.setdefault(f, []).append(sym)
    return {f: sorted(set(syms)) for f, syms in out.items()}


def _file_of_module(repo: pathlib.Path, mod: str):
    """Best-effort module dotted-path -> repo-relative file."""
    tail = mod.replace(".", "/") + ".py"
    for cand in repo.rglob("*/" + tail):
        if "_deprecated" not in str(cand) and "node_modules" not in str(cand):
            return str(cand.relative_to(repo))
    return None


def blocked_symbols(repo: pathlib.Path):
    """The (module, symbol) pairs the registry deliberately leaves on C.

    Read from `blocked_migrations` rather than hardcoded, so a registry edit
    re-arms this automatically — the same rule the content axis follows.
    """
    reg = repo / "docs/coordination/trace-convention-registry.json"
    try:
        rows = json.loads(reg.read_text()).get("blocked_migrations", [])
    except (OSError, json.JSONDecodeError):
        return []
    out = []
    for r in rows:
        f, sym = r.get("file", ""), r.get("symbol", "")
        if not f or not sym:
            continue
        # VERIFY THE PREMISE. A blocked row asserts the symbol is still C; if
        # the file has since moved to D, every "leak" derived from this row is
        # a false positive, and the row itself is the defect.
        #
        # This is not hypothetical. gram.py moved to D on 2026-08-15 (bean
        # qou-w8zz) and this row was not updated with it, so R9 went red on
        # main and this detector reported 25 production sites "receiving
        # convention C" that were receiving D. A detector that trusts a record
        # inherits the record's staleness -- the same failure the whole
        # excision has been unpicking, arriving in the tool built to find it.
        src_path = repo / f
        try:
            src = src_path.read_text()
        except OSError:
            src = ""
        if src and _defines_convention_d(src, sym):
            print(f"  REGISTRY STALE: {f}::{sym} is registered as convention "
                  f"{r.get('stays', '?')} under blocked_migrations, but the file "
                  f"defines it as convention D. Every leak derived from this row "
                  f"is a false positive; fix the registry, not the callers.")
            continue
        mod = _module_path_of(f)
        out.append((mod, sym, r.get("reason", ""), r.get("bean", "")))
    return out


#: A name that plausibly denotes the substrate parameter.
_Q_LIKE = re.compile(r"^_?[qQ][A-Za-z0-9_]{0,6}$")

#: A binding that names a Markov trace or a Wedderburn weight -- the
#: quantities that are rational in q under convention D, so a half-integer
#: power in one is z_C showing through.
TRACE_OR_WEIGHT = re.compile(
    r"tr_?M|trace|^W\d|_W\d|\bW\d+\b|y_lam|y_lambda|weight|wenzl|hopf|census",
    re.I)


def _is_q_like(node: ast.AST) -> bool:
    return isinstance(node, ast.Name) and bool(_Q_LIKE.match(node.id))


def _half_integer(node: ast.AST):
    """If `node` is a half-but-not-whole number, return it; else None.

    Accepts the literal `0.5`/`1.5`, `mp.mpf("1.5")`, `sp.Rational(3, 2)` and
    `sp.Rational(1, 2)` — the spellings this corpus actually uses for a
    half-integer exponent.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        v = float(node.value)
        return v if (v * 2) % 2 == 1 else None
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        inner = _half_integer(node.operand)
        return None if inner is None else -inner
    if isinstance(node, ast.Call):
        fn = ast.unparse(node.func)
        if fn.endswith("mpf") and node.args:
            return _half_integer(node.args[0]) if not isinstance(
                node.args[0], ast.Constant) or not isinstance(
                node.args[0].value, str) else (
                    float(node.args[0].value)
                    if (float(node.args[0].value) * 2) % 2 == 1 else None)
        if fn.endswith("Rational") and len(node.args) == 2:
            try:
                num, den = node.args[0].value, node.args[1].value
                return num / den if den == 2 and num % 2 == 1 else None
            except (AttributeError, TypeError, ZeroDivisionError):
                return None
    return None


def scan_closed_forms(roots=ROOTS):
    """Find CONVENTION-C-SPECIALISED CLOSED FORMS -- the third blind spot.

    Migrating `z` is not migrating the file. Quantities DERIVED from `z` get
    written out in closed form, and a closed form derived under convention C
    carries `z_C`'s square root where the general identity has none:

        tr_M(sigma_1^2) = h*z + 1        at z_C  ->  1 + (q-1)/q^{1/2}
        y_(2)  = (q*z + 1)/(q^2 + 1)     at z_C  ->  (q^{3/2}+q+1)/(q^3+q^2+q+1)

    `scan()` cannot see either: it keys on an assignment target containing
    `z`, and these are named `trM_sigma1_sq`, `W2`, `W11`, `census_hopf`. Four
    such sites had to be found by hand after the producers they live in were
    already reported migrated, and one of them (`trM_symbolic`) was missed even
    then -- caught only because the file cross-checks its symbolic path against
    its numeric one.

    So the fingerprint is not the name, it is the EXPONENT. Convention D is
    rational in `q`; a half-integer power of the substrate parameter cannot
    arise from it. Two shapes are matched:

        sqrt(q) / q**0.5 / q**1.5 / q**mpf("1.5") / q**Rational(3,2)
        rt = sqrt(q)  ...  rt**3            (indirect, one hop)

    `sqrt` of a COMPOUND expression is not matched — `mp.sqrt(q**4+q**2+1)` is
    a legitimate polynomial norm, not `q^{1/2}`.

    Reported only for files that ALSO define `z` the convention-D way: in a
    file still wholly on C a square root is expected and is `scan()`'s
    business, whereas in a migrated file it is a leftover.

    ## Narrowed to trace/weight bindings, deliberately

    The first version of this matched any half-power of `q` in a D-migrated
    file and returned 50 sites, most of them legitimate. `q^{1/2}` is not by
    itself a convention-C marker: `q^{1/2}+q^{-1/2}` is `[2]_{sqrt q}`, the
    Temperley–Lieb loop parameter at half-argument, and it turns up in Wenzl
    positivity, in pair-skein formulas, and in the Jones variable change
    `t = q^{-2}`, `A^2 = -q`. `trace-convention-audit.ts` records the same
    finding on the content side: 58 files carry the expression and flagging
    them "would repeat the loose-grep error that once reported 70 producers
    where the truth was 13".

    So the match is narrowed to a half-power appearing in a binding whose NAME
    says it is a trace or a Wedderburn weight — `trM`, `tr_m`, `W2`, `W11`,
    `y_lambda`, `weight`, `hopf`, `census`. That is exactly the claim the
    detector makes: those quantities are rational in `q` under D, so a square
    root in one is `z_C` showing through. A half-power anywhere else is
    somebody's legitimate `sqrt`, and not this detector's business.

    Bindings whose name declares convention C (`..._C`, `census_hopf_C`) are
    exempt, matching how `scan()` treats deliberately C-named targets: a
    labelled cross-convention reference is a comparison, not a defect.
    """
    out = []
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp_ = str(p)
            if "_deprecated" in sp_ or "/from_scratch/" in sp_:
                continue
            try:
                src = p.read_text()
                tree = ast.parse(src)
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            # Only files that have already moved to D. Elsewhere a square root
            # is the unmigrated z itself, which `scan` already reports.
            if "**3" not in "".join(src.split()).replace("* *", "**"):
                continue
            if not any(_defines_convention_d(src, t.id)
                       for n in ast.walk(tree)
                       if isinstance(n, ast.Assign)
                       for t in n.targets if isinstance(t, ast.Name)) \
               and not any(_returns_convention_d(fn) for fn in ast.walk(tree)
                           if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef))):
                continue

            # locals bound to sqrt(q), for the one-hop `rt**3` shape
            roots_of_q = {
                t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
                for t in n.targets if isinstance(t, ast.Name)
                if isinstance(n.value, ast.Call)
                and ast.unparse(n.value.func).endswith("sqrt")
                and n.value.args and _is_q_like(n.value.args[0])
            }

            def _half_power_in(node):
                """First half-power of q inside `node`, or None."""
                for n in ast.walk(node):
                    if isinstance(n, ast.Call) and ast.unparse(n.func).endswith("sqrt") \
                            and n.args and _is_q_like(n.args[0]):
                        return f"sqrt({ast.unparse(n.args[0])})"
                    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow):
                        if _is_q_like(n.left) and _half_integer(n.right) is not None:
                            return ast.unparse(n)
                        if (isinstance(n.left, ast.Name) and n.left.id in roots_of_q
                                and isinstance(n.right, ast.Constant)
                                and isinstance(n.right.value, int)
                                and n.right.value % 2 == 1):
                            return f"{ast.unparse(n)}  (with {n.left.id} = sqrt(q))"
                return None

            # Only bindings that NAME a trace or a Wedderburn weight. See the
            # docstring: a half-power elsewhere is somebody's legitimate sqrt.
            for n in ast.walk(tree):
                names, value = [], None
                if isinstance(n, ast.Assign) and n.value is not None:
                    names = [t.id for t in n.targets if isinstance(t, ast.Name)]
                    value = n.value
                elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    names, value = [n.name], n
                if not names or value is None:
                    continue
                if not any(TRACE_OR_WEIGHT.search(nm) for nm in names):
                    continue
                if any(DELIBERATE.search(nm) for nm in names):
                    continue
                hit = _half_power_in(value)
                if hit:
                    out.append((sp_, getattr(value, "lineno", n.lineno),
                                f"{names[0]} <- {hit}"))
    return out


def _returns_convention_d(fn) -> bool:
    """Does this function return `q**3/(q**2+1)`?"""
    for r in ast.walk(fn):
        if not isinstance(r, ast.Return) or r.value is None:
            continue
        v = r.value
        while isinstance(v, ast.UnaryOp) and isinstance(v.op, ast.UAdd):
            v = v.operand
        s = "".join(ast.unparse(v).split())
        b = s.split("**3", 1)[0]
        if b and s in (f"{b}**3/({b}**2+1)", f"{b}**3/(1+{b}**2)"):
            return True
    return False


def scan_reexports(roots=ROOTS, repo: pathlib.Path = None):
    """Find where a registry-BLOCKED convention-C symbol escapes its module.

    `blocked_migrations` records a symbol that stays on convention C for a
    stated reason — for `pyhecke.gram.z` it is that `G_INV = np.linalg.inv(G)`
    runs at module import and the Markov–Gram is singular under D, so flipping
    the line silently corrupts every consumer of `G_INV`.

    That exception is only sound while the symbol stays *inside* the blocked
    module. It does not:

        computations/substrate/hecke_core.py:61
            from pyhecke.gram import (z, W_SYM, W_STD, W_ALT, ...)

    and then production computations do `from hecke_core import z as Z_MARKOV`
    and use it as the Markov parameter. The registry's containment is a
    statement about one file; nothing checked that the file kept it.

    `is_c_form` cannot see this — there is no `1/(sqrt(q) + ...)` anywhere, just
    an import. So the audit reported the producer surface clear while the
    shared substrate module was handing convention C to every caller that asked
    for `z`.

    Two levels are reported: modules importing the blocked symbol directly, and
    modules importing it from *those* (the actual consumer surface).
    """
    repo = repo or pathlib.Path(".")
    blocked = blocked_symbols(repo)
    if not blocked:
        return []

    direct, out = {}, []
    for mod, sym, reason, bean in blocked:
        tail = mod.rsplit(".", 1)[-1]
        for r in roots:
            base = pathlib.Path(r)
            if not base.exists():
                continue
            for p in sorted(base.rglob("*.py")):
                sp = str(p)
                if "_deprecated" in sp or sp.startswith(BLOCKED_BY_DESIGN):
                    continue
                try:
                    tree = ast.parse(p.read_text())
                except (SyntaxError, UnicodeDecodeError, OSError):
                    continue
                for n in ast.walk(tree):
                    if not isinstance(n, ast.ImportFrom) or not n.module:
                        continue
                    if not (n.module == mod or n.module.endswith(f".{tail}") or n.module == tail):
                        continue
                    for a in n.names:
                        if a.name != sym:
                            continue
                        out.append((sp, n.lineno, f"{mod}.{sym}", a.asname or sym,
                                    "direct", reason, bean))
                        direct[pathlib.Path(sp).stem] = a.asname or sym

    # Second hop: who imports the re-exported name from the leaking module.
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp = str(p)
            if "_deprecated" in sp or sp.startswith(BLOCKED_BY_DESIGN):
                continue
            if pathlib.Path(sp).stem in direct:
                continue
            try:
                tree = ast.parse(p.read_text())
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            for n in ast.walk(tree):
                if not isinstance(n, ast.ImportFrom) or not n.module:
                    continue
                src = n.module.rsplit(".", 1)[-1]
                if src not in direct:
                    continue
                for a in n.names:
                    if a.name == direct[src]:
                        out.append((sp, n.lineno, f"{src}.{a.name}", a.asname or a.name,
                                    "via " + src, "", ""))
    return out


def _half_argument_vars(tree: ast.AST) -> set:
    """Names `t` for which the file declares `<q-like> = t ** 2`.

    Such a `t` IS `sqrt(q)`, so `z = 1/(t + 1/t)` is convention C written with
    no square root anywhere -- no `sqrt` call, no `0.5` exponent, and not the
    `t/(t**2+1)` shape `is_c_form_halfarg` matches either. It is the third
    spelling of C and it defeated both z-detectors:

        t = sp.symbols("t", positive=True)
        q = t ** 2
        z = 1 / (t + 1 / t)          # <- convention C, invisible

    Shape alone cannot decide this, and that is the point: `1/(q + 1/q)` is
    `1/[2]_q`, the Temperley-Lieb loop reciprocal, which the selftest requires
    NOT be flagged. The two are character-for-character identical and differ
    only in whether the variable is `q` or `sqrt(q)`. So the file has to say
    so, and here it does -- `q = t ** 2` is the declaration.
    """
    out = set()
    for n in ast.walk(tree):
        if not isinstance(n, ast.Assign) or n.value is None:
            continue
        if not any(_is_q_like(t) for t in n.targets):
            continue
        v = n.value
        if (isinstance(v, ast.BinOp) and isinstance(v.op, ast.Pow)
                and isinstance(v.left, ast.Name)
                and isinstance(v.right, ast.Constant) and v.right.value == 2):
            out.add(v.left.id)
    return out


def is_c_form_reciprocal(node: ast.AST, half_vars: set):
    """`1 / (t + 1/t)` where `t` is a declared half-argument variable."""
    if not half_vars:
        return None
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return None
    if not (isinstance(node.left, ast.Constant) and node.left.value in (1, 1.0)):
        return None
    den = node.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return None
    d = "".join(ast.unparse(den).split())
    for t in half_vars:
        if d in (f"{t}+1/{t}", f"1/{t}+{t}"):
            return t
    return None


def classify(path: str, blocked_files=(), declared_files=()) -> str:
    """Bucket a site. `blocked_files` comes from the registry, not from here.

    This used to label EVERY site under `tools/pyhecke/` "BLOCKED on C by
    design", justified by a single `blocked_migrations` row for
    `gram.py::z`. The blanket was too wide: the row covered the module-level
    `z` and nothing else, while three function-local C definitions sheltered
    under the same label -- two of them inside `gram.py` itself.

    When `gram.py::z` moved to D and the row was resolved, those three stopped
    having any registry basis at all, and a path-prefix classifier would have
    gone on calling them "by design" forever. Deriving the label from the
    registry means a site is only excused while a row actually excuses it.
    """
    if path in blocked_files:
        return "tools/pyhecke — BLOCKED on C by design (registry)"
    if path in declared_files:
        return ("tools/pyhecke — DECLARED C in evaluators.z, R10-waived "
                "(open defect, still actionable)")
    if path.startswith(BLOCKED_BY_DESIGN):
        return "tools/pyhecke — C with NO registry row (unexplained)"
    # computations/from_scratch/README.md declares the whole directory
    # DEPRECATED for production (2026-05-29, #1422 decision A') -- kept for
    # pedagogy, "not re-pursued". Same status as _deprecated/, which is
    # skipped outright; bucketed rather than skipped so it stays countable.
    if "/from_scratch/" in path:
        return "from_scratch — DEPRECATED for production (its own README)"
    if "/sage-examples/" in path:
        return "tools/sage-examples — examples, not producers"
    name = pathlib.Path(path).name
    if "/probes/" in path or name.endswith("_probe.py") or "probe" in name:
        return "probes / exploratory"
    if path.startswith("qou-mass"):
        return "qou-mass — SHIPPED PACKAGE"
    if "/sweeps/" in path:
        return "sweeps"
    return "computations — live producers"


def scan(roots=ROOTS, blocked_files=(), declared_files=()):
    """Yield (path, lineno, target_name, source, bucket, deliberate)."""
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp = str(p)
            if "_deprecated" in sp:
                continue
            try:
                tree = ast.parse(p.read_text())
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            half_vars = _half_argument_vars(tree)
            for n in ast.walk(tree):
                if not isinstance(n, (ast.Assign, ast.AnnAssign)):
                    continue
                targets = n.targets if isinstance(n, ast.Assign) else [n.target]
                names = [t.id for t in targets if isinstance(t, ast.Name)]
                if not any("z" in nm.lower() for nm in names):
                    continue
                if n.value is None:
                    continue
                if not (is_c_form(n.value) or is_c_form_halfarg(n.value)
                        or is_c_form_reciprocal(n.value, half_vars)):
                    continue
                nm = names[0]
                yield (sp, n.lineno, nm, ast.unparse(n.value),
                       classify(sp, blocked_files, declared_files),
                       bool(DELIBERATE.search(nm)))

            # RETURNED, not assigned. The scan above keys off an assignment
            # TARGET, so a function that computes the convention straight into
            # its return statement has no target to match and was invisible:
            #
            #     def z_mp(dps=...):
            #         ...
            #         return +(1 / (_mp.sqrt(q) + _mp.sqrt(qi_)))
            #
            # That is `pyhecke.gram.z_mp`, a public 50-dps entry point, and it
            # went unreported through every sweep that claimed the surface was
            # clear. The analogue of "target name contains z" is "function name
            # contains z", which keeps the same guard against matching
            # unrelated `1/(sqrt(...)+...)` arithmetic.
            for fn in ast.walk(tree):
                if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if "z" not in fn.name.lower():
                    continue
                # A function that returns BOTH a C form and the D form is a
                # convention DISPATCHER, not a defect -- its C branch is the
                # labelled comparison, by construction.
                #
                # qbeta_kc21_parity_convention_immunity_probe.z_of(q, conv)
                # returns sqrt(q)/(1+q) for "C", q**3/(q**2+1) for "D", and
                # q/(1+q**2) for "X (control, in no channel; genericity probe
                # only)". The half-argument matcher fired on the X CONTROL --
                # `q/(1+q^2)` is exactly the r/(r^2+1) shape -- and a control
                # deliberately chosen to be in no channel is the opposite of a
                # convention-C leak.
                #
                # The DELIBERATE exemption could not catch it: it keys on the
                # target NAME, and here the name is `z_of` with the label in a
                # docstring and a branch guard. Returning D somewhere in the
                # same function is the machine-checkable signal.
                dispatcher = _returns_convention_d(fn)
                for r in ast.walk(fn):
                    if not isinstance(r, ast.Return) or r.value is None:
                        continue
                    val = r.value
                    # `+expr` is used in this corpus to pin mpmath precision;
                    # unwrap it or the shape never matches.
                    while isinstance(val, ast.UnaryOp) and isinstance(val.op, ast.UAdd):
                        val = val.operand
                    if not (is_c_form(val) or is_c_form_halfarg(val)):
                        continue
                    yield (sp, r.lineno, f"{fn.name}() -> return",
                           ast.unparse(val),
                           "convention dispatcher (returns C and D) — labelled comparison"
                           if dispatcher else classify(sp, blocked_files, declared_files),
                           bool(DELIBERATE.search(fn.name)) or dispatcher)


def selftest() -> int:
    """Prove the matcher accepts every spelling in the corpus and rejects D.

    A detector that cannot fail is worse than none — the same rule the content
    axis is held to. These fixtures are the real spellings found in
    `computations/`, plus the convention-D forms that must NOT match.
    """
    should_match = [
        "1.0 / (q0**0.5 + qi0**0.5)",
        "1.0 / (q0 ** 0.5 + q0 ** (-0.5))",
        "1.0 / (Q0 ** 0.5 + QI ** 0.5)",
        "1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))",
        "1 / (sp.sqrt(q) + 1 / sp.sqrt(q))",
        "1.0 / (np.sqrt(q) + 1.0 / np.sqrt(q))",
        "1 / (sqrt_q + 1 / sqrt_q)",
        "1 / (q ** mpmath.mpf('0.5') + qi ** mpmath.mpf('0.5'))",
        "1 / (q0 ** mpf('0.5') + q0 ** mpf('-0.5'))",
        "1 / (mp.sqrt(q0) + mp.sqrt(qi))",
    ]
    half = [
        ("t / (t ** 2 + 1)", True),        # convention C in r = sqrt(q)
        ("r/(r**2 + 1)", True),
        ("t ** 6 / (t ** 4 + 1)", False),  # convention D in r = sqrt(q)
        ("q ** 3 / (q ** 2 + 1)", False),  # convention D in q
    ]
    should_not = [
        "q ** 3 / (q ** 2 + 1)",          # convention D
        "q0**3 / (q0**2 + 1)",            # convention D
        "1 / (q + 1 / q)",                # 1/[2]_q — the TL loop reciprocal, not z
        "2 / (a + b)",                    # not a reciprocal of the right shape
        "1 / (q ** 3 + q ** 0.5)",        # cube present -> rejected
    ]
    bad = 0
    for src in should_match:
        ok = is_c_form(ast.parse(src, mode="eval").body)
        print(f"  {'ok  ' if ok else 'FAIL'}  matches: {src}")
        bad += not ok
    for src in should_not:
        ok = not is_c_form(ast.parse(src, mode="eval").body)
        print(f"  {'ok  ' if ok else 'FAIL'}  rejects: {src}")
        bad += not ok
    for src, want in half:
        got = is_c_form_halfarg(ast.parse(src, mode="eval").body) is not None
        ok = got == want
        verb = "flags" if want else "clears"
        print(f"  {'ok  ' if ok else 'FAIL'}  half-arg {verb}: {src}")
        bad += not ok
    # The re-export detector. `is_c_form` is blind to these by construction --
    # there is no arithmetic to shape-match, only an import -- so it needs its
    # own fixtures or it could silently match nothing forever.
    # Fixtures, not the live registry. These used to assert "the registry has
    # a blocked row", which passed only while one existed -- so resolving
    # gram.py::z turned two green checks red without any logic changing. A
    # selftest that fails when the DATA moves is testing the data.
    checks = [
        ("package root is the LAST occurrence, not the first",
         _module_path_of("tools/pyhecke/python/pyhecke/gram.py") == "pyhecke.gram"),
        ("a plain package path resolves",
         _module_path_of("src/foo/bar.py") == "foo.bar"),
        ("a bare file resolves to its stem",
         _module_path_of("gram.py") == "gram"),
    ]
    # The return-form blind spot. `scan` keyed off an assignment target, so a
    # function returning the convention directly had nothing to match on --
    # five live producers and pyhecke.gram.z_mp went unreported through every
    # sweep that called the surface clear.
    def _returns_found(src: str) -> int:
        tree = ast.parse(src)
        n = 0
        for fn in ast.walk(tree):
            if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if "z" not in fn.name.lower():
                continue
            for r in ast.walk(fn):
                if not isinstance(r, ast.Return) or r.value is None:
                    continue
                v = r.value
                while isinstance(v, ast.UnaryOp) and isinstance(v.op, ast.UAdd):
                    v = v.operand
                n += is_c_form(v) or bool(is_c_form_halfarg(v))
        return n

    # The closed-form scanner. Its whole risk is over-breadth -- the first
    # version returned 50 sites in D-migrated files, nearly all legitimate
    # square roots, which is the loose-grep error this repo has now made
    # twice. These fixtures pin the narrowing.
    def _cf(src: str) -> int:
        import tempfile
        d = pathlib.Path(tempfile.mkdtemp())
        (d / "m.py").write_text("z = q ** 3 / (q ** 2 + 1)\n" + src)
        cwd = pathlib.Path.cwd()
        try:
            import os
            os.chdir(d.parent)
            return len(scan_closed_forms(roots=(d.name,)))
        finally:
            os.chdir(cwd)

    # The reciprocal form `1/(t + 1/t)` with `q = t**2` declared. Decidable
    # ONLY from that declaration: it is character-for-character `1/[2]_q`, the
    # Temperley-Lieb loop reciprocal, which must not be flagged. These two
    # fixtures are the whole justification for reading the declaration.
    def _hv(src):
        return _half_argument_vars(ast.parse(src))

    def _recip(src, decl="t = sp.symbols('t')\nq = t ** 2\n"):
        tree = ast.parse(decl + src)
        hv = _half_argument_vars(tree)
        return any(is_c_form_reciprocal(n.value, hv)
                   for n in ast.walk(tree)
                   if isinstance(n, ast.Assign) and n.value is not None)

    checks += [
        ("`q = t ** 2` declares t as the half-argument variable",
         _hv("t = sp.symbols('t')\nq = t ** 2\n") == {"t"}),
        ("no such declaration -> no half-argument variables",
         _hv("q = sp.symbols('q')\nx = q * 2\n") == set()),
        ("`z = 1/(t + 1/t)` with q = t**2 IS convention C",
         _recip("z = 1 / (t + 1 / t)\n")),
        ("the same shape WITHOUT the declaration is 1/[2]_q, not z",
         not _recip("z = 1 / (q + 1 / q)\n", decl="q = sp.symbols('q')\n")),
        ("convention D in the half-argument variable is not flagged",
         not _recip("z = t ** 6 / (t ** 4 + 1)\n")),
        ("a trace closed form with sqrt(q) is flagged",
         _cf("def trM_hopf(q):\n    return 1 + (q - 1) / mp.sqrt(q)\n") == 1),
        ("a Wedderburn weight with q**1.5 is flagged",
         _cf("def wenzl_weights(q):\n    W2 = (q ** 1.5 + q + 1) / d\n    return W2\n") >= 1),
        ("`rt = sqrt(q)` then `rt**3` is flagged through the alias",
         _cf("rt = sp.sqrt(q)\nW2 = (rt ** 3 + q + 1) / d\n") == 1),
        ("sqrt of a POLYNOMIAL is not a half-power of q",
         _cf("def trM_x(q):\n    return mp.sqrt(q ** 4 + q ** 2 + 1)\n") == 0),
        ("a half-power OUTSIDE a trace/weight binding is left alone",
         _cf("def loop_param(q):\n    return mp.sqrt(q) + 1 / mp.sqrt(q)\n") == 0),
        ("a deliberately C-named trace form is exempt",
         _cf("def trM_hopf_census_form_C(q):\n    return 1 + (q - 1) / mp.sqrt(q)\n") == 0),
        ("a file with no convention-D z is not scanned at all",
         len(scan_closed_forms(roots=("nonexistent-dir-xyz",))) == 0),
        ("a bare `return 1/(sqrt(q)+1/sqrt(q))` is found",
         _returns_found("def z_factor(q):\n    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))\n") == 1),
        ("mpmath's precision-pinning unary + does not hide it",
         _returns_found("def z_mp(d):\n    return +(1 / (_mp.sqrt(q) + _mp.sqrt(qi_)))\n") == 1),
        ("a convention-D return is NOT flagged",
         _returns_found("def z_mp(d):\n    return q ** 3 / (q ** 2 + 1)\n") == 0),
        ("a function whose name has no z is left alone",
         _returns_found("def loop(q):\n    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))\n") == 0),
        # The three pyhecke buckets. Only a blocked_migrations row excuses a
        # site; a registry DECLARATION accounts for it without excusing it,
        # which is the distinction that stopped four registered sites reading
        # as "unexplained" when blocked_migrations was correctly emptied.
        ("a blocked_migrations row excuses a site",
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  blocked_files={"tools/pyhecke/python/pyhecke/gram.py"})
         .startswith("tools/pyhecke — BLOCKED")),
        ("a DECLARED site is labelled as declared, not unexplained",
         "DECLARED C in evaluators.z" in
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})),
        ("declaring a site does NOT excuse it -- it stays actionable",
         "still actionable" in
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})),
        ("an undeclared pyhecke site is still unexplained",
         classify("tools/pyhecke/python/pyhecke/atom.py",
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})
         .endswith("(unexplained)")),
        ("a blocked row outranks a declaration for the same file",
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  blocked_files={"tools/pyhecke/python/pyhecke/gram.py"},
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})
         .startswith("tools/pyhecke — BLOCKED")),
        # declared_c_files reads the LIVE registry: a C evaluator whose module
        # is NOT waived must not be silently treated as declared.
        ("an unwaived C evaluator does not count as declared",
         "pyhecke/atom.py" not in
         " ".join(declared_c_files(pathlib.Path(".")))),
        # A convention DISPATCHER is a labelled comparison by construction.
        # qbeta_kc21_parity_convention_immunity_probe.z_of returns C, D and an
        # X control (q/(1+q^2), "in no channel"); the half-argument matcher
        # fired on the CONTROL. DELIBERATE could not help -- the label is in a
        # docstring and a branch guard, not the name.
        ("a function returning BOTH C and D is a dispatcher, not a defect",
         _returns_convention_d(ast.parse(
             "def z_of(q, conv):\n"
             "    if conv == 'C': return mp.sqrt(q) / (1 + q)\n"
             "    if conv == 'D': return q ** 3 / (q ** 2 + 1)\n"
             "    return q / (1 + q ** 2)\n").body[0])),
        ("a function returning only C is NOT a dispatcher",
         not _returns_convention_d(ast.parse(
             "def z_mp(d):\n    return 1 / (mp.sqrt(q) + mp.sqrt(qi))\n").body[0])),
        ("a file defining z the convention-D way is recognised as D",
         _defines_convention_d("z = q0 ** 3 / (q0 ** 2 + 1)", "z")),
        ("the reversed-denominator spelling is recognised as D",
         _defines_convention_d("z = q ** 3 / (1 + q ** 2)", "z")),
        ("a convention-C definition is NOT mistaken for D",
         not _defines_convention_d("z = 1 / (q ** 0.5 + q ** (-0.5))", "z")),
        ("a mere comment mentioning D does not count as a definition",
         not _defines_convention_d("# convention D: q**3/(q**2+1)\nz = 0.4993", "z")),
    ]
    for name, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'}  reexport: {name}")
        bad += not ok

    total = len(should_match) + len(should_not) + len(half) + len(checks)
    print(f"selftest: {total - bad}/{total}"
          + ("" if bad else " — matcher accepts every corpus spelling and rejects convention D."))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print every site")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return 1 if selftest() else 0

    blocked_files = {r.get("file", "") for r in
                     __import__("json").loads(
                         pathlib.Path("docs/coordination/trace-convention-registry.json")
                         .read_text()).get("blocked_migrations", [])}
    declared_files = declared_c_files(pathlib.Path("."))
    rows = list(scan(blocked_files=blocked_files,
                     declared_files=set(declared_files)))
    live = [r for r in rows if not r[5]]
    deliberate = [r for r in rows if r[5]]

    buckets = Counter(r[4] for r in live)
    files = defaultdict(set)
    for r in live:
        files[r[4]].add(r[0])

    print("convention-C Markov-parameter definitions in live Python (AST-verified)\n")
    for k, v in buckets.most_common():
        print(f"  {v:4d} sites / {len(files[k]):3d} files   {k}")
    print(f"\n  {len(deliberate):4d} sites               deliberately C-named — labelled comparisons, not defects")

    # Only a site with a live registry row is excused. "unexplained"
    # pyhecke sites count as actionable -- that is the whole point of
    # deriving the label from the registry instead of the path.
    # Excused: a live registry row, or a directory whose own README declares
    # itself out of production. tools/sage-examples is NOT excused -- nothing
    # declares it dead, and an example teaching convention C is arguably worse
    # than a producer using it, because examples get copied.
    _EXCUSED = ("BLOCKED on C by design", "DEPRECATED for production")
    actionable = sum(v for k, v in buckets.items()
                     if not any(e in k for e in _EXCUSED))
    print(f"\n  ACTIONABLE (excludes blocked-by-design): {actionable} sites")

    closed = scan_closed_forms()
    if closed:
        print(f"\n  C-SPECIALISED CLOSED FORMS: {len(closed)} trace/weight binding(s) in "
              f"convention-D files still carry a half-integer power of q.")
        print("  Migrating z is not migrating the file: h*z+1 and (q*z+1)/(q^2+1) are")
        print("  rational under D, so a square root in one is z_C showing through.")
        for path, line, what in closed:
            print(f"    {path}:{line}   {what}")

    leaks = scan_reexports(repo=pathlib.Path("."))
    if leaks:
        direct = [l for l in leaks if l[4] == "direct"]
        hops = [l for l in leaks if l[4] != "direct"]
        print(f"\n  BLOCKED-SYMBOL LEAKS: {len(direct)} module(s) re-export a registry-blocked "
              f"convention-C symbol; {len(hops)} further consumer(s) import it from them.")
        print("  The registry exempts a symbol INSIDE its module. Nothing kept it there.")
        for path, line, sym, asname, how, reason, bean in direct:
            print(f"    {path}:{line}   {sym}  ->  {asname}   [{bean or 'no bean'}]")
        if args.list:
            for path, line, sym, asname, how, _, _ in hops:
                print(f"      {how:16s} {path}:{line}   {sym} -> {asname}")
        elif hops:
            print(f"    (--list to see the {len(hops)} downstream consumers)")

    if args.list:
        print()
        for path, line, nm, src, bucket, _ in sorted(live):
            print(f"  {path}:{line}\n      {nm} = {src[:90]}")

    if args.json:
        pathlib.Path(args.json).write_text(json.dumps([
            {"path": p, "line": l, "target": nm, "source": s,
             "bucket": b, "deliberate": d}
            for p, l, nm, s, b, d in rows
        ], indent=2))
        print(f"\n  json -> {args.json}")

    return 1 if actionable else 0


if __name__ == "__main__":
    sys.exit(main())
