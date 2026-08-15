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
  REGISTRY, not from the path. A site is "BLOCKED on C by design" only while a
  `blocked_migrations` row names that exact file; anything else under
  `tools/pyhecke/` is reported as **C with NO registry row (unexplained)** and
  counts as actionable.

  The path-prefix version was too generous. One row covered `gram.py::z`, and
  three *function-local* C definitions sheltered under the same label — two of
  them inside `gram.py` itself. When `z` migrated to D on 2026-08-15 (bean
  `qou-w8zz`) and the row was resolved, a prefix classifier would have gone on
  calling those three "by design" indefinitely.
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


def classify(path: str, blocked_files=()) -> str:
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
    if path.startswith(BLOCKED_BY_DESIGN):
        return "tools/pyhecke — C with NO registry row (unexplained)"
    name = pathlib.Path(path).name
    if "/probes/" in path or name.endswith("_probe.py") or "probe" in name:
        return "probes / exploratory"
    if path.startswith("qou-mass"):
        return "qou-mass — SHIPPED PACKAGE"
    if "/sweeps/" in path:
        return "sweeps"
    return "computations — live producers"


def scan(roots=ROOTS, blocked_files=()):
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
            for n in ast.walk(tree):
                if not isinstance(n, (ast.Assign, ast.AnnAssign)):
                    continue
                targets = n.targets if isinstance(n, ast.Assign) else [n.target]
                names = [t.id for t in targets if isinstance(t, ast.Name)]
                if not any("z" in nm.lower() for nm in names):
                    continue
                if n.value is None:
                    continue
                if not (is_c_form(n.value) or is_c_form_halfarg(n.value)):
                    continue
                nm = names[0]
                yield (sp, n.lineno, nm, ast.unparse(n.value),
                       classify(sp, blocked_files), bool(DELIBERATE.search(nm)))


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
    checks += [
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
    rows = list(scan(blocked_files=blocked_files))
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
    actionable = sum(v for k, v in buckets.items() if "BLOCKED on C by design" not in k)
    print(f"\n  ACTIONABLE (excludes blocked-by-design): {actionable} sites")

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
