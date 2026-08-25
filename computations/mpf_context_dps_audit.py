#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit, emits no numeric physics.
"""Catch `mp.dps = N` that silently does nothing.

Owner directive: NO FLOAT64.

## The defect

```python
import mpmath as mp
mp.dps = 50          # sets an attribute on the MODULE — a no-op
```

Precision lives on mpmath's *context object*, `mpmath.mp`. Under this import
alias the line has to read `mp.mp.dps = 50`. As written it binds a stray
attribute nobody reads, and the whole file runs at mpmath's default **15
digits** while its author believes it is at 50.

Both forms appear in this corpus and look nearly identical, which is why the
mistake survives review:

```python
from mpmath import mp     # `mp` IS the context   -> mp.dps = 50   correct
import mpmath as mp       # `mp` is the MODULE    -> mp.dps = 50   no-op
```

## Why this needs its own gate

`witness_float64_padding_audit.py` cannot see it. At `dps=15` a plain
`str(<mpf>)` prints ~15 digits, and `is_f64_padded` requires ≥20 fractional
digits before it examines a value at all — so a producer that quietly computes
at 15 and prints 15 is invisible to it. Of the seven instances found in this
corpus, **exactly one** produced padding, and only because that file writes
`mp.nstr(..., 40)`, forcing 40 digits out of a 15-digit value.

The two defects are near-orthogonal:

| | the claim | caught by |
|---|---|---|
| float64 padding | value asserts **more** precision than it has | the padding audit |
| this | value silently carries **less** than was asked for | this gate |

## It fabricates results, not just short digits

`scratch/pslq_wq.py` asked for 45 digits and ran at 15. PSLQ does not fail
loudly at insufficient precision — it invents relations:

```
15 digits:  Integer relation for rational function of y: [60, -407, 54, -68, 58, 195]
45 digits:  Integer relation for rational function of y: None
```

Spurious, with the large-coefficient signature that is the classic tell. The
other relation that script finds, `[0, -1, 1, -2, 0, 0]`, survives both because
it is the genuine identity h² = y − 2 — a useful control: the fix removes fake
relations without destroying real ones. That one did not propagate past
`scratch/`, but nothing about the defect guaranteed it wouldn't.

**Bounded, not just flagged.** Surveying every PSLQ call site in the corpus —
52 files — all of them raise working precision, typically to 1000–1500 dps with
an explicit `tol` and `maxcoeff`. `scratch/pslq_wq.py` was the only
under-precisioned one, and it is fixed. (A first pass reported three more; all
three were false positives, because it recognised only integer *literals* and
those files write `mp.mp.dps = DPS`. Worth stating: the scare was mine, and
checking it dissolved it.)

Full history: `docs/audits/2026-08-07-producer-repadding-empirical-sweep.md`.

## AST, not regex

The first sweep for this was a regex and got both failure modes:

- it anchored the import at column 0 and **missed two instances** indented
  inside a `try:` block;
- it matched the phrase `mp.dps = 60` inside a **docstring** and reported a
  file that is perfectly correct.

Parsing removes both by construction: an assignment is an assignment, wherever
it is nested, and prose is not code.

Usage:
    python3 computations/mpf_context_dps_audit.py           # report
    python3 computations/mpf_context_dps_audit.py --strict  # exit 1 on any hit
    python3 computations/mpf_context_dps_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Attributes that carry precision on the context. Setting either on the module
# is equally inert.
PRECISION_ATTRS = {"dps", "prec"}


def find_noop_dps(source: str, filename: str = "<src>") -> list[dict]:
    """Return every `<mpmath-module-alias>.dps|prec = ...` in `source`.

    Names bound to the *context* (`from mpmath import mp`) are never flagged —
    there `mp.dps` is the correct form. A name bound both ways is treated as a
    context name, which is the conservative direction: this gate would rather
    miss one than cry wolf on a correct file.
    """
    try:
        tree = ast.parse(source, filename)
    except SyntaxError:
        return []

    module_aliases: set[str] = set()
    context_names: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name == "mpmath" or a.name.startswith("mpmath."):
                    # `import mpmath` binds "mpmath"; `as X` binds X.
                    module_aliases.add(a.asname or a.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module == "mpmath":
                for a in node.names:
                    # `from mpmath import mp [as M]` binds the CONTEXT.
                    if a.name == "mp":
                        context_names.add(a.asname or a.name)

    flagged = module_aliases - context_names
    if not flagged:
        return []

    out: list[dict] = []
    lines = source.splitlines()
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AugAssign):
            targets = [node.target]
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        for t in targets:
            if (isinstance(t, ast.Attribute)
                    and t.attr in PRECISION_ATTRS
                    and isinstance(t.value, ast.Name)
                    and t.value.id in flagged):
                ln = getattr(t, "lineno", 0)
                out.append({
                    "file": filename,
                    "line": ln,
                    "alias": t.value.id,
                    "attr": t.attr,
                    "source": (lines[ln - 1].strip() if 0 < ln <= len(lines) else ""),
                    "fix": f"{t.value.id}.mp.{t.attr} = …",
                })
    return sorted(out, key=lambda d: d["line"])


# Directories reported but not gated. `scratch/` is exploratory work that no
# witness depends on, so failing CI on it would put a standing backlog in front
# of a gate that is otherwise at zero — the failure mode #4653 avoided by
# holding its own gate at baseline zero. Reported anyway: a scratch probe
# computing at 15 digits when it asked for 45 still produces wrong answers, it
# just does not block a build.
UNGATED_DIRS = {"scratch"}


def scan_repo(root: Path) -> list[dict]:
    out: list[dict] = []
    for f in sorted(root.rglob("*.py")):
        # `.claude/worktrees/<agent>/` holds checkouts of OTHER branches, so
        # every hit under it is a duplicate of some sibling branch's source at
        # a revision this checkout is not on: not fixable from here, and gone
        # the moment the worktree is pruned.  Left in, they held this gate
        # permanently RED for reasons unrelated to any diff -- and a gate that
        # is always red is a gate agents learn to skip.  `.claude/` carries no
        # tracked `.py` at all, so excluding the whole directory loses nothing.
        if set(f.parts) & {"_deprecated", "node_modules", ".claude"}:
            continue
        try:
            src = f.read_text(encoding="utf-8")
        except Exception:
            continue
        if "mpmath" not in src:
            continue
        rel = f.relative_to(root)
        gated = not (set(rel.parts) & UNGATED_DIRS)
        for hit in find_noop_dps(src, rel.as_posix()):
            hit["gated"] = gated
            out.append(hit)
    return out


CASES = [
    # (label, source, expected_hits)
    ("module alias, module scope", "import mpmath as mp\nmp.dps = 50\n", 1),
    ("module alias, indented in try", "try:\n    import mpmath as mp\n    mp.dps = 60\nexcept Exception:\n    pass\n", 1),
    ("no alias", "import mpmath\nmpmath.dps = 50\n", 1),
    ("prec, not just dps", "import mpmath as mp\nmp.prec = 200\n", 1),
    ("inside a function", "import mpmath as mp\ndef f():\n    mp.dps = 30\n", 1),
    # Correct forms — must NOT be flagged.
    ("context via from-import", "from mpmath import mp\nmp.dps = 50\n", 0),
    ("context, aliased", "from mpmath import mp as M\nM.dps = 50\n", 0),
    ("correct module form", "import mpmath as mp\nmp.mp.dps = 50\n", 0),
    ("both bindings present", "import mpmath as mp\nfrom mpmath import mp\nmp.dps = 50\n", 0),
    ("reading, not assigning", "import mpmath as mp\nx = mp.dps\n", 0),
    # The regex false positive this tool exists to avoid.
    ("docstring mentioning mp.dps = 60",
     '"""assembled by dict-polynomials at\nmp.dps = 60. phi(tau) = ...\n"""\nimport mpmath as mp\nmp.mp.dps = 60\n', 0),
    ("comment mentioning it", "import mpmath as mp\n# mp.dps = 50 would be a no-op\nmp.mp.dps = 50\n", 0),
    ("no mpmath at all", "import math\nmath.dps = 5\n", 0),
]


def self_test() -> int:
    fails = 0
    for label, src, want in CASES:
        got = len(find_noop_dps(src, "<case>"))
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any no-op is found")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    hits = scan_repo(Path(a.root).resolve())
    gated = [h for h in hits if h["gated"]]
    ungated = [h for h in hits if not h["gated"]]

    def show(hs):
        for h in hs:
            print(f"  {h['file']}:{h['line']}")
            print(f"      {h['source']}")
            print(f"      -> {h['fix']}   (`{h['alias']}` is the mpmath "
                  f"module, not the context)")

    if gated:
        print(f"mpf-context-dps: {len(gated)} no-op precision assignment(s)\n")
        show(gated)
        print("\nEach leaves the run at mpmath's default 15 digits.")
    else:
        print("mpf-context-dps: clean — no no-op precision assignments in "
              "gated paths.")
    if ungated:
        print(f"\n--- {len(ungated)} more in ungated paths "
              f"({', '.join(sorted(UNGATED_DIRS))}) — reported, not failed ---")
        show(ungated)
        print("\nNot a build failure, but not harmless either: these still run "
              "at 15 digits.")
    return 1 if (a.strict and gated) else 0


if __name__ == "__main__":
    raise SystemExit(main())
