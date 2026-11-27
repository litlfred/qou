#!/usr/bin/env python3
r"""Advisory: a content-block hypothesis that a SIBLING content block proves.

Bean `qou-sibdup`. Content-block `.lean` files cannot import each other, so a
block may assume, as an explicit hypothesis, the very statement that the file
next to it proves. The worked case (fixed by the WeilZeta library lift,
qou-qspc) was

    spectral-half-line.lean
      theorem reeb_spectrum_on_critical_line (W : WeilZeta)
          (hw : ∀ i, ‖W.eigenvalues i‖ = W.q ^ (1 / 2 : ℝ)) : ...
    hasse-weil-bound.lean
      theorem hasse_weil_bound (Z : WeilZeta) [IsWeilZeta Z] :
          ∀ i, ‖Z.eigenvalues i‖ = Z.q ^ (1 / 2 : ℝ)

Method: per chapter directory, collect every declaration's explicit
hypotheses and every declaration's conclusion, alpha-rename each
declaration's own parameter names to positions (`#0`, `#1`, …), and report a
hypothesis whose canonical text equals a conclusion in a DIFFERENT file of the
same directory. The same-file case is `lean-self-assuming-audit.py`'s job.

Specificity filter (owner ruling 2026-11-21, docs/coordination/owner-rulings.md):
a match counts only if the shared statement names at least one non-parameter
identifier of 3+ characters outside a small list of generic names. Without
it the corpus gives 232 pairs at 127 sites, almost all `q ≠ 0` / `0 < q` side
conditions matched by generic lemmas; with it the worked case still hits and
the corpus gives 0 (measured 2026-11-21, `main` 313bff6b2c7).

ADVISORY ONLY. A syntactic match cannot tell "the sibling proves it under
hypotheses I also have" from "the sibling proves it under different
hypotheses", so a hit is a prompt to read both files, not a verdict. It has no
ledger category and exits 0 whatever it finds; `--selftest` exits 1 on a
regression.

Usage:
    python3 scripts/lean-sibling-hypothesis-audit.py [root ...]   # default: folio
    python3 scripts/lean-sibling-hypothesis-audit.py --selftest
    python3 scripts/lean-sibling-hypothesis-audit.py --json out.json [root ...]
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "_self_assuming", _HERE / "lean-self-assuming-audit.py")
sa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sa)

IDENT = r"[A-Za-z_][A-Za-z0-9_'₀-₉]*"
DATA_BINDER = re.compile(r"(Type\*?|Type \S+|Sort \S+|ℕ|ℤ|ℚ|ℝ|ℂ|Prop|Bool)")
SPECIFIC_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_']{2,}")
GENERIC = {
    "Real", "Nat", "Int", "Rat", "Complex", "Set", "Finset", "Function",
    "sqrt", "exp", "log", "abs", "sin", "cos", "sinh", "cosh", "card", "Fin",
    "True", "False", "fun", "Type", "Prop", "Even", "Odd",
}


def split_sig(body: str):
    """(binder text, conclusion) of a declaration body, or None."""
    idx, d = -1, 0
    for i, ch in enumerate(body):
        if ch in sa._OPEN:
            d += 1
        elif ch in sa._CLOSE:
            d = max(0, d - 1)
        elif d == 0 and body.startswith(":=", i):
            idx = i
            break
    sig = body[:idx] if idx >= 0 else body
    d, at = 0, -1
    for i, ch in enumerate(sig):
        if ch in "([{":
            d += 1
        elif ch in ")]}":
            d -= 1
        elif ch == ":" and d == 0 and not sig.startswith(":=", i):
            at = i
            break
    if at < 0:
        return None
    return sig[:at], sa.norm(sig[at + 1:])


def params(binders_txt: str):
    """Ordered (names, type, explicit?) for every binder group."""
    out = []
    for rx, expl in ((sa.BINDER, True), (sa.BINDER_INST, False),
                     (sa.BINDER_IMPL, False)):
        for b in rx.finditer(binders_txt):
            out.append((b.start(), b.group("names").split(),
                        sa.norm(b.group("type")), expl))
    out.sort()
    return [(n, t, e) for _, n, t, e in out]


def canon(t: str, names: set[str]) -> str:
    """Alpha-rename the declaration's own parameter names to positions."""
    order: dict[str, str] = {}

    def rep(m):
        w = m.group(0)
        if w in names:
            order.setdefault(w, f"#{len(order)}")
            return order[w]
        return w

    return re.sub(rf"(?<![.\w]){IDENT}", rep, t)


def is_specific(canonical: str) -> bool:
    return bool(set(SPECIFIC_TOKEN.findall(canonical)) - GENERIC)


def content_block_dirs(root: Path):
    """Chapter dir -> content-block .lean files (library `lean/` trees skipped)."""
    blocks: dict[Path, list[Path]] = {}
    files = [root] if root.is_file() else root.rglob("*.lean")
    for p in files:
        rel = p.relative_to(root).parts[:-1] if root.is_dir() else ()
        if ".lake" in p.parts or "lean" in rel:
            continue
        blocks.setdefault(p.parent, []).append(p)
    return blocks


def scan(root: Path, specific_only: bool = True):
    hits, stats = [], {"files": 0, "hypotheses": 0, "conclusions": 0}
    for chap, files in sorted(content_block_dirs(root).items()):
        concl: dict[str, list] = {}
        hyps = []
        for f in sorted(files):
            stats["files"] += 1
            src = sa.strip_comments(f.read_text(encoding="utf-8",
                                                errors="replace"))
            for m in sa.DECL.finditer(src):
                r = split_sig(m.group("rest"))
                if not r:
                    continue
                btxt, c = r
                ps = params(btxt)
                names = {n for ns, _, _ in ps for n in ns}
                if c:
                    concl.setdefault(canon(c, names), []).append(
                        (f, m.group("name"), c))
                    stats["conclusions"] += 1
                for ns, t, expl in ps:
                    if not expl or DATA_BINDER.fullmatch(t):
                        continue
                    for n in ns:
                        hyps.append((f, m.group("name"), n, t, canon(t, names)))
                        stats["hypotheses"] += 1
        for f, d, n, t, ct in hyps:
            if specific_only and not is_specific(ct):
                continue
            for g, e, _c in concl.get(ct, []):
                if g == f:
                    continue
                hits.append(dict(chapter=str(chap), file=str(f), decl=d,
                                 hypothesis=n, type=t, sibling_file=str(g),
                                 sibling_decl=e))
    return stats, hits


_FIXTURE = {
    "hasse-weil-bound.lean": (
        "theorem hasse_weil_bound (Z : WeilZeta) [IsWeilZeta Z] :\n"
        "    ∀ i, ‖Z.eigenvalues i‖ = Z.q ^ (1 / 2 : ℝ) := by\n"
        "  sorry\n"),
    "spectral-half-line.lean": (
        "theorem reeb_spectrum_on_critical_line (W : WeilZeta)\n"
        "    (hw : ∀ i, ‖W.eigenvalues i‖ = W.q ^ (1 / 2 : ℝ)) : True :=\n"
        "  trivial\n"
        # generic side condition: must NOT match the generic lemma below
        "theorem uses_q_ne_zero (q : ℝ) (hq : q ≠ 0) : q * q ≠ 0 :=\n"
        "  mul_ne_zero hq hq\n"),
    "generic-lemma.lean": (
        "theorem some_q_ne_zero (q : ℝ) (h : 1 < q) : q ≠ 0 := by\n"
        "  positivity\n"),
}


def selftest() -> int:
    bad = []
    with tempfile.TemporaryDirectory() as td:
        chap = Path(td) / "chapter"
        chap.mkdir()
        for name, text in _FIXTURE.items():
            (chap / name).write_text(text, encoding="utf-8")
        _, filtered = scan(Path(td))
        _, raw = scan(Path(td), specific_only=False)
    got = sorted((h["decl"], h["hypothesis"], h["sibling_decl"]) for h in filtered)
    want = [("reeb_spectrum_on_critical_line", "hw", "hasse_weil_bound")]
    if got != want:
        bad.append(f"filtered hits {got!r} != {want!r}")
    else:
        print("  ok  worked case (hw = hasse_weil_bound) caught")
    if not any(h["hypothesis"] == "hq" for h in raw):
        bad.append("unfiltered scan no longer matches the generic `q ≠ 0` pair")
    elif any(h["hypothesis"] == "hq" for h in filtered):
        bad.append("specificity filter let the generic `q ≠ 0` pair through")
    else:
        print("  ok  generic `q ≠ 0` side condition dropped by the filter")
    if bad:
        print("\nSELFTEST FAILED:", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 1
    print("\nselftest ok")
    return 0


def main() -> int:
    argv = sys.argv[1:]
    if "--selftest" in argv:
        return selftest()
    out = None
    if "--json" in argv:
        i = argv.index("--json")
        out = argv[i + 1]
        del argv[i:i + 2]
    specific = "--unfiltered" not in argv
    argv = [a for a in argv if a != "--unfiltered"]
    roots = [Path(r) for r in (argv or ["folio"])]
    total = {"files": 0, "hypotheses": 0, "conclusions": 0}
    hits = []
    for root in roots:
        stats, h = scan(root, specific_only=specific)
        hits += h
        for k in total:
            total[k] += stats[k]
    if total["files"] == 0:
        print("error: scanned 0 content-block .lean files — nothing was audited.",
              file=sys.stderr)
        return 2
    print(f"content-block .lean files {total['files']}, explicit hypotheses "
          f"{total['hypotheses']}, conclusions {total['conclusions']}, "
          f"sibling matches {len(hits)}"
          + ("" if specific else " (UNFILTERED)"))
    for h in hits:
        print(f"- {h['file']} :: {h['decl']} ({h['hypothesis']} : "
              f"{h['type'][:110]})\n    = conclusion of "
              f"{Path(h['sibling_file']).name} :: {h['sibling_decl']}")
    print("advisory: a match is a prompt to read both blocks, not a verdict.")
    if out:
        Path(out).write_text(json.dumps(hits, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
