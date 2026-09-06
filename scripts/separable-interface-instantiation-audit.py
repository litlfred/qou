#!/usr/bin/env python3
"""Is `separable_interface_degenerate` ever APPLIED, or only cited in prose?

`QOU.QBeta.InterfaceScalar.separable_interface_degenerate` is the theorem the
two-nucleon channel-asymmetry closure rests on.  Its hypotheses

    hplus  : fSpin s1 = fIso t1
    hminus : fSpin s0 = fIso t0

are the "equal projector scalars" identification that bean `qou-brng` records as
the residue of the whole question.  But `fSpin` and `fIso` are *arbitrary
functions on arbitrary types*: the hypotheses are the antecedent of a
universally-quantified implication, not a claim about anything in this corpus.
They become a claim about the corpus only when the theorem is INSTANTIATED at
the corpus's own scalars — so "is it ever instantiated?" is the question that
decides whether there is a claim to settle at all.

This script answers it mechanically, and is a guard rather than a one-off: the
answer was 0 application sites on 2026-09-05, and the moment somebody writes one
the `--strict` gate goes red so the audit doc and the bean can be corrected
instead of quietly going stale.

WHAT COUNTS AS AN APPLICATION.  Comments are stripped first — Lean block
comments `/- -/`, doc comments `/-- -/`, module docs `/-! -/`, and line comments
`--` — and only then is the name searched for.  A hit in the surviving code of a
`.lean` file is an application site.  Everything else (audit docs, probe
docstrings, beans, agent memory, and Lean *docstrings*) is prose.

The declaration's own `theorem separable_interface_degenerate` line is excluded:
declaring it is not applying it.

Usage:
    python3 scripts/separable-interface-instantiation-audit.py            # report
    python3 scripts/separable-interface-instantiation-audit.py --strict   # exit 1 on any application site
    python3 scripts/separable-interface-instantiation-audit.py --selftest # prove the stripper works
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

NAME = "separable_interface_degenerate"
ROOT = Path(__file__).resolve().parent.parent


def strip_lean_comments(src: str) -> str:
    """Blank out Lean comments, preserving line structure so line numbers survive.

    Handles nested block comments, which Lean allows and a regex does not.
    """
    out = list(src)
    i, n = 0, len(src)
    depth = 0
    while i < n:
        if depth == 0:
            if src.startswith("/-", i):
                depth = 1
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if src.startswith("--", i):
                j = src.find("\n", i)
                j = n if j < 0 else j
                for k in range(i, j):
                    out[k] = " "
                i = j
                continue
            i += 1
        else:
            if src.startswith("/-", i):
                depth += 1
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if src.startswith("-/", i):
                depth -= 1
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if src[i] != "\n":
                out[i] = " "
            i += 1
    return "".join(out)


def selftest() -> int:
    cases = [
        ("/-- doc mentioning X -/\ntheorem a := X", 1, "doc comment stripped"),
        ("/-! module doc X -/\nY", 0, "module doc stripped"),
        ("-- line X\nZ", 0, "line comment stripped"),
        ("/- outer /- nested X -/ still X -/\nW", 0, "nested block stripped"),
        ("theorem t := X -- X\n", 1, "code kept, trailing comment stripped"),
    ]
    bad = 0
    for src, want, label in cases:
        got = strip_lean_comments(src).count("X")
        ok = got == want
        bad += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}: {got} X in code, expected {want}")
    if bad:
        print(f"SELFTEST FAILED ({bad} case(s))")
    else:
        print("SELFTEST PASSED (5/5) — the comment stripper is not the thing being measured")
    return 1 if bad else 0


def tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.splitlines()
    return [ROOT / p for p in out]


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    strict = "--strict" in sys.argv

    prose: list[tuple[str, int, str]] = []
    applications: list[tuple[str, int, str]] = []
    declaration: list[tuple[str, int, str]] = []

    for path in tracked_files():
        try:
            src = path.read_text(encoding="utf-8", errors="replace")
        except (OSError, IsADirectoryError):
            continue
        if NAME not in src:
            continue
        rel = str(path.relative_to(ROOT))
        raw_lines = src.split("\n")
        if path.suffix == ".lean":
            code_lines = strip_lean_comments(src).split("\n")
        else:
            code_lines = [""] * len(raw_lines)
        for idx, raw in enumerate(raw_lines):
            if NAME not in raw:
                continue
            in_code = NAME in code_lines[idx] if idx < len(code_lines) else False
            entry = (rel, idx + 1, raw.strip())
            if not in_code:
                prose.append(entry)
            elif re.search(r"\b(theorem|lemma|def)\s+" + NAME, code_lines[idx]):
                declaration.append(entry)
            else:
                applications.append(entry)

    print(f"`{NAME}` — instantiation audit")
    print(f"  declaration sites : {len(declaration)}")
    for rel, ln, txt in declaration:
        print(f"      {rel}:{ln}  {txt[:80]}")
    print(f"  APPLICATION sites : {len(applications)}")
    for rel, ln, txt in applications:
        print(f"      {rel}:{ln}  {txt[:80]}")
    print(f"  prose citations   : {len(prose)}"
          f"  (in {len({r for r, _, _ in prose})} files)")
    by_ext: dict[str, int] = {}
    for rel, _, _ in prose:
        by_ext[Path(rel).suffix or "(none)"] = by_ext.get(Path(rel).suffix or "(none)", 0) + 1
    for ext, k in sorted(by_ext.items(), key=lambda kv: -kv[1]):
        print(f"      {ext:8s} {k}")

    print()
    if applications:
        print("The theorem IS applied. Its hypotheses are therefore a claim about the")
        print("objects it is applied to — read those sites before repeating that the")
        print("equal-scalars identification is unexamined.")
        return 1 if strict else 0
    print("ZERO application sites: every occurrence outside the declaration is prose.")
    print("So `hplus`/`hminus` are not a claim about this corpus that a D9 witness")
    print("could settle — they are the antecedent of a statement quantified over all")
    print("scalar assignments. Making them a corpus claim requires instantiating the")
    print("theorem at the corpus's own constructions, which nothing does.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
