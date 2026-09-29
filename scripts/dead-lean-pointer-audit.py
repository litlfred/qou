#!/usr/bin/env python3
"""Find content-block `.lean` files that point at a library file which does not exist.

A content-block sibling routinely names a library module in its header prose:

    The §3b-cond class axiomatisation lives at
    [`../lean/QOU/BraidsAndKnots/Foo.lean`](../lean/QOU/BraidsAndKnots/Foo.lean)
    under the `qou` Lake package (file pending; ...).

When that file does not exist the sentence is worse than useless: it tells a reader
(increasingly, an agent) that a real formalisation lives elsewhere, which is the
D11 failure mode -- an agent began writing content into a stub on the strength of
such a header, and the file it named was not the file holding the substantive class.

WHY THIS IS NOT A FIND-AND-REPLACE. Measured on the first two instances swept by
hand, each dead pointer was wrong in FOUR independent ways at once: a library file
that does not exist, a `.md` section it cites that does not exist either, a
`-- Ref:` naming the wrong chapter directory, and a namespace that does not match
the block's own `lean.ref`. A script that fixed the path would have left three.
So this script CLASSIFIES and refuses to edit; the disposition is a human call.

Five classes. The first three are cheap, mechanical, and CORRECT-in-substance;
the fourth is the expensive one; the fifth is not a defect at all.

  WRONGPKG   the same path under a DIFFERENT library root exists. Every paper has
             its own Lake library -- `QOU`, `UGB`, `Fred2005` -- and a block in
             one paper that writes `lean/QOU/...` when its library is `UGB` names
             a file that does exist, under the right name, in the wrong package.
             A one-token fix, and calling it rot would misdescribe it.
  CROSSPAPER the file exists under ANOTHER paper's lean tree, i.e. the mention
             is a cross-paper reference written as if it were local. Currently
             EMPTY, and how it emptied is worth keeping: it held two
             `folio/visualizer/` findings that were an artifact of the
             unanchored regex above, which truncated a correct
             `../../quantum-observable-universe/lean/QOU/...` to its tail. The
             class is kept because the shape is real and cheap to detect; do not
             read `CROSSPAPER 0` as evidence nobody writes such a reference.
  MISREF     a declaration with the pointed-at leaf name EXISTS, in a
             differently-named file. The pointer is wrong about WHERE, not about
             WHETHER -- and the block may be SHADOWING a real carrier. This is
             the D11 / quantum-langlands-dual / reverse-limit shape and the one
             worth reading each instance for.
  ROT        nothing of that name exists anywhere. Pure rot.
  RECORD     the mention sits in prose that is explicitly historical ("previously
             said", "the old header advertised", "does not exist"). NOT a defect
             -- it is a fix, already applied, describing itself. Sweeping these
             would delete the record of the repair.

The first pass of this audit had only MISREF/ROT/RECORD, and it put all ten UGB
mentions in ROT. They are WRONGPKG:
`folio/unital-groebner-bases/lean/UGB/GrobnerShirshov/Basic.lean` exists.
A coarse class is not a neutral simplification -- it prices a one-token fix as
unrecoverable rot.

(That path is written in full deliberately. It first read
`lean/UGB/GrobnerShirshov/Basic.lean`, which resolves from nowhere -- a dead
pointer, in the docstring of the dead-pointer audit, caught by a check that this
sweep's own asserted paths all exist. Illustrative paths are paths.)

Usage:
    python3 scripts/dead-lean-pointer-audit.py            # summary + table
    python3 scripts/dead-lean-pointer-audit.py --json     # machine-readable
    python3 scripts/dead-lean-pointer-audit.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# A path ending in `lean/<Lib>/A/B.lean`, INCLUDING any leading directory
# segments. The anchor matters more than it looks: an earlier version read
#
#     (?:\.\./)*lean/QOU/[A-Za-z0-9_/]+\.lean
#
# which is not anchored at a path boundary, so it matched only the TAIL of a
# longer path. `../../quantum-observable-universe/lean/QOU/BringsSurface.lean`
# -- a correct, working reference -- was truncated to `lean/QOU/BringsSurface.lean`,
# resolved against the wrong paper, and reported dead. Two of the first run's
# findings were that artifact.
#
# `(?<![\w./-])` is the whole fix: it refuses to start mid-path.
POINTER_RE = re.compile(
    r"(?<![\w./-])((?:\.\./|[A-Za-z0-9_.-]+/)*lean/(?:QOU|UGB|Fred2005)/[A-Za-z0-9_/]+\.lean)"
)

# Prose that marks a mention as a historical record rather than a live claim.
# Deliberately narrow: a vague "note" or "see" does NOT qualify. The mention has
# to say, in the same neighbourhood, that the thing is absent or superseded.
RECORD_MARKERS = (
    "does not exist",
    "no longer exists",
    "no such file",
    "previously said",
    "previously read",
    "used to",
    "old header",
    "the old docstring",
    "never has",
    "dropped",
    "retired",
    "stale pointer",
    "two stale pointers",
    "was false",
    "were false",
)

RECORD_WINDOW = 6  # lines either side of the mention to scan for a marker


def paper_root(p: Path) -> Path:
    """content/<paper>/... -> content/<paper>"""
    return Path(p.parts[0]) / p.parts[1]


def resolve_candidates(src: Path, mention: str) -> list[Path]:
    """Every reading of the mention that a reader might reasonably take.

    A mention is dead only if ALL of them miss -- resolving only one way is how
    the first pass of this audit reported 98 dead pointers against a true 47.
    """
    return [
        (src.parent / mention).resolve(),                     # relative to the file
        (paper_root(src) / mention.lstrip("./")).resolve(),   # relative to the paper
        Path(mention.lstrip("./")).resolve(),                 # relative to repo root
    ]


def leaf_decl_name(mention: str) -> str:
    return Path(mention).stem


def other_library_root(src: Path, rest: str) -> str:
    """Same path, this paper's OWN lean tree, under a different library root.

    Never returns `src` itself. A file whose leaf name matches the mention it
    contains would otherwise be reported as a WRONGPKG fix pointing at itself,
    and a mechanical rewrite then turns a comment about a PLANNED module into a
    self-reference. Measured: `Fred2005/FormalGroups.lean` carries a TODO naming
    a hypothetical `lean/QOU/FormalGroups.lean` bridge; the unguarded version
    rewrote it to name the very file the comment sits in.
    """
    lean = paper_root(src) / "lean"
    if not lean.is_dir():
        return ""
    for root in sorted(d for d in lean.iterdir() if d.is_dir() and d.name != ".lake"):
        cand = root / rest
        if cand.exists() and cand.resolve() != src.resolve():
            return str(cand)
    return ""


def other_paper(src: Path, rest: str) -> str:
    """Same path under ANOTHER paper's lean tree."""
    mine = paper_root(src)
    for lean in sorted(Path("folio").glob("*/lean")):
        if paper_root(lean) == mine:
            continue
        for root in sorted(d for d in lean.iterdir() if d.is_dir() and d.name != ".lake"):
            cand = root / rest
            if cand.exists():
                return str(cand)
    return ""


def find_declaration(leaf: str, lean_roots: list[Path]) -> list[str]:
    """Files declaring `class|structure|theorem|def <leaf>`, anywhere in the tree.

    Keyed on the DECLARATION, not on the file name: the whole point of the misref
    class is that the declaration lives in a differently-named file.
    """
    # Modifiers may precede the keyword. Omitting them is not a small miss: the
    # first version required the keyword at line start, so every
    # `noncomputable def <leaf>` was invisible and its pointer was classified
    # ROT -- "nothing of that name exists anywhere" -- when the declaration was
    # sitting in the library. All three of this audit's original ROT findings
    # were that bug, so ROT went 3 -> 0 when it was fixed.
    mods = r"(?:noncomputable\s+|private\s+|protected\s+|partial\s+|unsafe\s+|scoped\s+)*"
    decl = re.compile(
        rf"^\s*{mods}(?:class|structure|theorem|lemma|def|abbrev|instance)\s+{re.escape(leaf)}\b",
        re.M,
    )
    hits = []
    for root in lean_roots:
        for f in root.rglob("*.lean"):
            if ".lake" in f.parts:
                continue
            try:
                if decl.search(f.read_text(errors="replace")):
                    hits.append(str(f))
            except OSError:
                continue
    return hits


def is_record(lines: list[str], idx: int) -> bool:
    lo = max(0, idx - RECORD_WINDOW)
    hi = min(len(lines), idx + RECORD_WINDOW + 1)
    window = " ".join(lines[lo:hi]).lower()
    return any(m in window for m in RECORD_MARKERS)


def audit(content_root: Path = Path("folio")) -> list[dict]:
    lean_roots = sorted(
        d for d in content_root.glob("*/lean/QOU") if d.is_dir()
    )
    findings: list[dict] = []
    for src in sorted(content_root.rglob("*.lean")):
        if ".lake" in src.parts or "/lean/QOU/" in str(src):
            continue
        try:
            text = src.read_text(errors="replace")
        except OSError:
            continue
        lines = text.splitlines()
        seen: set[str] = set()
        for i, line in enumerate(lines):
            for mention in POINTER_RE.findall(line):
                if any(c.exists() for c in resolve_candidates(src, mention)):
                    continue
                key = f"{mention}@{i}"
                if key in seen:
                    continue
                seen.add(key)
                decls: list[str] = []
                fix = ""
                if is_record(lines, i):
                    kind = "RECORD"
                else:
                    # everything after `lean/<Lib>/`
                    parts = mention.split("/")
                    li = len(parts) - 1 - parts[::-1].index("lean")
                    rest = "/".join(parts[li + 2:])        # A/B.lean
                    alt = other_library_root(src, rest)
                    cross = other_paper(src, rest)
                    if alt:
                        kind, fix = "WRONGPKG", alt
                    elif cross:
                        kind, fix = "CROSSPAPER", cross
                    else:
                        decls = find_declaration(leaf_decl_name(mention), lean_roots)
                        kind = "MISREF" if decls else "ROT"
                findings.append(
                    {
                        "file": str(src),
                        "line": i + 1,
                        "mention": mention,
                        "class": kind,
                        "declared_at": decls,
                        "exists_at": fix,
                        "text": line.strip()[:120],
                    }
                )
    return findings


def self_test() -> int:
    """Guard the two ways this audit has already been wrong.

    1. Single-candidate resolution over-reports (98 vs a true 47).
    2. A historical record reads as a live dead pointer, which would send an
       agent to "fix" the very sentence that documents the fix.
    """
    ok = True

    m = "lean/QOU/Foo.lean"
    src = Path("folio/quantum-observable-universe/mass-theory/x.lean")
    cands = resolve_candidates(src, m)
    if len(cands) != 3:
        print("FAIL: expected 3 resolution candidates, got", len(cands))
        ok = False
    if not any("quantum-observable-universe/lean/QOU/Foo.lean" in str(c) for c in cands):
        print("FAIL: paper-relative candidate missing -- this is the over-report bug")
        ok = False

    import tempfile, os
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "QOU"
        (root / "Sub").mkdir(parents=True)
        (root / "Sub" / "Particles.lean").write_text(
            "namespace QOU\nnoncomputable def qExtDeriv (x : Nat) : Nat := x\nend QOU\n"
        )
        if not find_declaration("qExtDeriv", [root]):
            print("FAIL: `noncomputable def` not seen -- this is the ROT=3 bug")
            ok = False

    long = "../../quantum-observable-universe/lean/QOU/BringsSurface.lean"
    got = POINTER_RE.findall(f"see [`x`]({long})")
    if got != [long]:
        print("FAIL: unanchored regex truncated a correct long path ->", got)
        ok = False

    rec = ["The old header advertised", "`../lean/QOU/A/B.lean`", "That file does not exist."]
    if not is_record(rec, 1):
        print("FAIL: historical record not detected as RECORD")
        ok = False
    live = ["The class axiomatisation lives at", "`../lean/QOU/A/B.lean`", "under the qou package."]
    if is_record(live, 1):
        print("FAIL: live pointer misdetected as RECORD")
        ok = False

    print("self-test: PASS" if ok else "self-test: FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--only", choices=["WRONGPKG", "CROSSPAPER", "MISREF", "ROT", "RECORD"])
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    findings = audit()
    if args.only:
        findings = [f for f in findings if f["class"] == args.only]

    if args.json:
        print(json.dumps(findings, indent=2))
        return 0

    counts = {k: 0 for k in ("WRONGPKG", "CROSSPAPER", "MISREF", "ROT", "RECORD")}
    for f in findings:
        counts[f["class"]] += 1
    files = {f["file"] for f in findings if f["class"] != "RECORD"}
    actionable = sum(v for k, v in counts.items() if k != "RECORD")

    for f in findings:
        print(f"{f['class']:10} {f['file']}:{f['line']}")
        print(f"           -> {f['mention']}")
        if f.get("exists_at"):
            print(f"              exists at: {f['exists_at']}")
        for d in f["declared_at"]:
            print(f"              declared at: {d}")

    print()
    print("  ".join(f"{k} {v}" for k, v in counts.items()))
    print(f"actionable mentions: {actionable} across {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
