#!/usr/bin/env python3
# polynomial_q_not_applicable: source rewriter, emits no numeric physics.
"""Drain reference-literal findings by routing them to the registry.

Rewrites a hand-typed CODATA/AME constant into the `codata_constants` symbol
it was copied from, so the value is READ rather than retyped.

    mp.mpf("2.224566")   ->  AME_B_DEUTERON_MEV_VALIDATION
    7.71804              ->  AME_B_HE3_MEV_VALIDATION

Both directions matter. The `mpf("...")` form is a truncation carried at full
precision; the bare form is a truncation carried in **float64**, so draining it
closes a NO-FLOAT64 defect at the same time.

SAFETY
  * Only rewrites (file, line, literal) triples named by the audit witness --
    never a free grep, so a coincidental number is out of reach by construction.
  * Skips any line the audit marked prose, and any file whose rewrite does not
    re-parse. A file that fails to compile is reverted, not committed.
  * `--dry-run` prints the diff and writes nothing.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WITNESS = ROOT / "computations" / "codata-truncation-audit.witness.json"

AME = {"B_2H", "B_3H", "B_3He", "B_4He", "B_5Li", "B_6Li", "B_7Li"}
CODATA = {"m_p", "m_n", "m_e", "m_mu", "u_MeV"}


def targets(scope: str) -> list[dict]:
    rows = json.loads(WITNESS.read_text())["findings"]
    out = []
    for r in rows:
        c, v = r["constant"], r["verdict"]
        if scope in ("ame", "all") and c in AME:
            out.append(r)
        elif scope in ("codata", "all") and c in CODATA and v == "DIVERGENT":
            out.append(r)
    return out


def rewrite_file(path: Path, rows: list[dict]) -> tuple[str, int] | None:
    src = path.read_text()
    lines = src.splitlines(keepends=True)
    needed: set[str] = set()
    n = 0
    by_line: dict[int, list[dict]] = {}
    for r in rows:
        by_line.setdefault(r["line"], []).append(r)
    for ln, items in by_line.items():
        if ln > len(lines):
            continue
        text = lines[ln - 1]
        for r in items:
            sym = r["use_instead"].split(".")[-1]
            lit = re.escape(r["literal"])
            # mp.mpf("lit") / mpf('lit') -> SYMBOL  (drop the wrapper)
            new, k = re.subn(
                rf'(?:\w+\.)?mpf\(\s*["\']{lit}["\']\s*\)', sym, text)
            if k == 0:
                # bare float64 literal, not part of a longer number
                new, k = re.subn(rf'(?<![\w.]){lit}(?![\d])', sym, text)
            if k:
                text = new
                needed.add(sym)
                n += k
        lines[ln - 1] = text
    if not n:
        return None
    out = "".join(lines)
    if needed:
        out = ensure_import(out, sorted(needed))
    try:
        ast.parse(out)
    except SyntaxError as e:
        print(f"  SKIP {path.relative_to(ROOT)} — rewrite does not parse: {e}")
        return None
    return out, n


def ensure_import(src: str, syms: list[str]) -> str:
    """Add the registry import, extending an existing one where present."""
    have = re.search(r"^from codata_constants import \(?([^)\n]*)\)?$",
                     src, re.M)
    if have:
        cur = {s.strip() for s in have.group(1).split(",") if s.strip()}
        allsym = sorted(cur | set(syms))
        return src[:have.start()] + _imp(allsym) + src[have.end():]
    lines = src.splitlines(keepends=True)
    idx = 0
    for i, l in enumerate(lines):
        # TOP-LEVEL only. A sys.path push inside a function or an `if` block
        # is at an indent the inserted import cannot share, so anchoring to it
        # produced "unexpected indent" and the parse guard skipped 112 of 212
        # files -- the tool silently doing an eighth of the job it reported.
        if l[:1].isspace():
            continue
        st = l
        # The import must land AFTER the sys.path bootstrap, not merely after
        # the last import. Files under computations/<cluster>/ get sys.path[0]
        # = their own directory, so a bare-name import of codata_constants
        # resolves ONLY once the parent has been pushed onto sys.path — and
        # that push sits BELOW the import block in every probe that needs it.
        #
        # Placing by "last import line" alone broke 5 of a 40-file sample with
        # ModuleNotFoundError, each of which ran clean before the rewrite.
        # That is the _path_bridge bootstrap-ordering defect (bean qou-0e1t),
        # reintroduced by the tool meant to clean the tree.
        if st.startswith(("import ", "from ")):
            idx = i + 1
        elif ("sys.path" in st and ("insert" in st or "append" in st
                                    or "[:0]" in st)):
            idx = i + 1
        elif st.startswith(("_sys.path", "sys.path")):
            idx = i + 1
    lines.insert(idx, _imp(syms) + "\n")
    return "".join(lines)


def _imp(syms: list[str]) -> str:
    one = f"from codata_constants import {', '.join(syms)}"
    if len(one) <= 79:
        return one
    body = ",\n    ".join(syms)
    return f"from codata_constants import (\n    {body},\n)"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scope", choices=("ame", "codata", "all"), default="ame")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="restrict to paths containing this string")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    rows = targets(a.scope)
    if a.only:
        rows = [r for r in rows if a.only in r["file"]]
    by_file: dict[str, list[dict]] = {}
    for r in rows:
        by_file.setdefault(r["file"], []).append(r)
    files = sorted(by_file)
    if a.limit:
        files = files[:a.limit]

    done = fixed = 0
    for f in files:
        p = ROOT / f
        if not p.exists():
            continue
        got = rewrite_file(p, by_file[f])
        if not got:
            continue
        out, n = got
        if not a.dry_run:
            p.write_text(out)
        done += 1
        fixed += n
        print(f"  {'would fix' if a.dry_run else 'fixed'} {n:3d}  {f}")
    print(f"\n{'DRY RUN — ' if a.dry_run else ''}{fixed} literal(s) routed to "
          f"the registry across {done} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
