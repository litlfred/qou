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
* **`tools/pyhecke/`** is reported separately: the registry records
  `pyhecke.gram.z` as convention C **by design** under `blocked_migrations`, and
  R9 asserts that exception rather than leaving it undetected.
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
        # tools/pyhecke/python/pyhecke/gram.py -> pyhecke.gram.
        # The LAST occurrence of the package name is the package root; the
        # first is the containing directory, which yields the nonsense
        # `pyhecke.python.pyhecke.gram`. The selftest caught that.
        parts = pathlib.Path(f).with_suffix("").parts
        pkg = next((p for p in reversed(parts[:-1]) if (pathlib.Path(*parts[:parts.index(p) + 1])).name == p
                    and p not in ("python", "src", "tools")), None)
        if pkg and pkg in parts:
            i = len(parts) - 1 - parts[::-1].index(pkg)
            mod = ".".join(parts[i:])
        else:
            mod = parts[-1]
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


def classify(path: str) -> str:
    if path.startswith(BLOCKED_BY_DESIGN):
        return "tools/pyhecke — BLOCKED on C by design (registry)"
    name = pathlib.Path(path).name
    if "/probes/" in path or name.endswith("_probe.py") or "probe" in name:
        return "probes / exploratory"
    if path.startswith("qou-mass"):
        return "qou-mass — SHIPPED PACKAGE"
    if "/sweeps/" in path:
        return "sweeps"
    return "computations — live producers"


def scan(roots=ROOTS):
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
                       classify(sp), bool(DELIBERATE.search(nm)))


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
    repo = pathlib.Path(__file__).resolve().parent.parent
    bl = blocked_symbols(repo)
    checks = [
        ("registry yields at least one blocked (module, symbol)", bool(bl)),
        ("the blocked file path resolves to an importable module path",
         any(m == "pyhecke.gram" and s == "z" for m, s, _, _ in bl)),
    ]
    if bl:
        leaks = scan_reexports(repo=repo)
        checks.append(("the known hecke_core re-export is detected",
                       any("hecke_core.py" in l[0] and l[4] == "direct" for l in leaks)))
        checks.append(("pyhecke's own modules are NOT reported as leaking",
                       not any(l[0].startswith(BLOCKED_BY_DESIGN) for l in leaks)))
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

    rows = list(scan())
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

    actionable = sum(v for k, v in buckets.items() if not k.startswith("tools/pyhecke"))
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
