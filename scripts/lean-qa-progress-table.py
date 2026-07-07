#!/usr/bin/env python3
"""Per-chapter Lean proof-progress + QA-sidecar stats table.

Walks every chapter of content/quantum-observable-universe, classifies each
provable block's Lean formalization (sorry-free / has-sorry / trivial stub /
missing), and aggregates QA results from the <block>.qa.json sidecars
(latest entry per criterion; staleness via source-hash drift).

Usage:
    python3 scripts/lean-qa-progress-table.py            # TSV to stdout
    python3 scripts/lean-qa-progress-table.py --md OUT   # markdown report

"Lean proved" means the resolved .lean source is sorry-free; compile status
is whatever the last CI build verified (this script does not run lake).
"""
import hashlib, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "content/quantum-observable-universe"
LEAN_ROOT = ROOT / "lean"

PAPER_TS = ROOT / "quantum-observable-universe.ts"
CHAPTERS = re.findall(r'dir: "([^"]+)"', PAPER_TS.read_text())

PROVABLE = {"theorem", "lemma", "proposition", "corollary"}
KINDS = PROVABLE | {"definition", "conjecture", "remark", "example", "prose",
                    "equation", "diagram", "simulator", "proof", "table",
                    "algorithm"}

BUILDER_RE = re.compile(r"export\s+default\s+(\w+)\s*\(")
LEAN_REF_RE = re.compile(r'lean:\s*\{\s*ref:\s*"([^"]+)"')
SORRY_RE = re.compile(r"\bsorry\b")
STUB_RE = re.compile(r":\s*True\s*(?:∧\s*True\s*)?:=")


def h12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def strip_comments(src: str) -> str:
    """Blank out Lean comments (nested /- -/ blocks and -- line comments)
    while preserving line structure and string literals, so `sorry`
    mentions in docstrings/comments are not mistaken for proof holes and
    `--` inside string literals (URLs) does not truncate code."""
    out = list(src)
    i, n = 0, len(src)
    depth = 0
    in_str = False
    in_line = False
    while i < n:
        c = src[i]
        if c == "\n":
            in_line = False
            i += 1
            continue
        if in_line or depth > 0:
            if depth > 0 and src.startswith("/-", i):
                depth += 1
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if depth > 0 and src.startswith("-/", i):
                depth -= 1
                out[i] = out[i + 1] = " "
                i += 2
                continue
            out[i] = " "
            i += 1
            continue
        if in_str:
            if c == "\\":
                i += 2
                continue
            if c == '"':
                in_str = False
            i += 1
            continue
        if c == '"':
            in_str = True
            i += 1
            continue
        if src.startswith("/-", i):
            depth = 1
            out[i] = out[i + 1] = " "
            i += 2
            continue
        if src.startswith("--", i):
            in_line = True
            out[i] = " "
            i += 1
            continue
        i += 1
    return "".join(out)


def resolve_lean(block_ts: Path, ts_src: str):
    """Return the block's .lean path: sibling first, then the lean.ref
    library file. Prefix-path candidates only count when the file actually
    contains the declaration's final name segment (an aggregator module
    like lean/QOU.lean must not swallow unresolved refs); otherwise fall
    back to a declaration-name search over the library tree (mirrors the
    pipeline's grep fallback), else None."""
    sib = block_ts.with_suffix(".lean")
    if sib.exists():
        return sib
    m = LEAN_REF_RE.search(ts_src)
    if not (m and m.group(1).startswith("qou:")):
        return None
    parts = m.group(1)[4:].split(".")
    decl = parts[-1]
    decl_re = re.compile(r"\b" + re.escape(decl) + r"\b")
    for cut in range(len(parts), 0, -1):
        cand = LEAN_ROOT.joinpath(*parts[:cut]).with_suffix(".lean")
        if cand.exists() and decl_re.search(cand.read_text(errors="ignore")):
            return cand
    decl_def_re = re.compile(
        r"^\s*(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev|structure|class|instance)\s+"
        + re.escape(decl) + r"\b", re.M)
    for cand in sorted(LEAN_ROOT.rglob("*.lean")):
        if decl_def_re.search(cand.read_text(errors="ignore")):
            return cand
    return None


def classify_lean(p: Path) -> str:
    src = strip_comments(p.read_text(errors="ignore"))
    if STUB_RE.search(src):
        return "stub"
    if SORRY_RE.search(src):
        return "sorry"
    return "proved"


REF_RE = re.compile(r"--\s*Ref:\s*(.*)")
REF_KEY_RE = re.compile(r"\[([^\]]+)\]")


def sorry_refs(p: Path):
    """For each real `sorry` statement (comments/docstrings blanked out),
    find the nearest `-- Ref:` citation in the preceding 5 lines (the
    AGENTS.md §1 acceptability rule). Returns list of (line_no, ref)."""
    raw = p.read_text(errors="ignore")
    lines = raw.splitlines()
    code_lines = strip_comments(raw).splitlines()
    out = []
    for i, code in enumerate(code_lines):
        if not SORRY_RE.search(code):
            continue
        ref = None
        for j in range(i, max(-1, i - 6), -1):
            m = REF_RE.search(lines[j])
            if m:
                k = REF_KEY_RE.search(m.group(1))
                ref = k.group(1) if k else m.group(1).strip()[:60]
                break
        out.append((i + 1, ref))
    return out


def collect():
    rows, drill, sorries = [], {}, []
    for num, ch in enumerate(CHAPTERS, 1):
        d = ROOT / ch
        if not d.is_dir():
            continue
        s = dict(blocks=0, thm=0, lem=0, prop=0, cor=0, prov=0,
                 proved=0, sorry=0, stub=0, missing=0,
                 qa_side=0, qa_fail_blocks=0, qa_fail_crit=0, qa_stale=0,
                 da_fail=0)
        fails_here = []
        for ts in sorted(d.glob("*.ts")):
            if ts.stem == ch:
                continue
            src = ts.read_text(errors="ignore")
            m = BUILDER_RE.search(src)
            kind = m.group(1) if m else None
            if kind not in KINDS:
                continue
            s["blocks"] += 1
            abbrev = {"theorem": "thm", "lemma": "lem",
                      "proposition": "prop", "corollary": "cor"}
            if kind in abbrev:
                s[abbrev[kind]] += 1
            if kind in PROVABLE:
                s["prov"] += 1
                lp = resolve_lean(ts, src)
                if lp is None:
                    print(f"BINGO: {ch} / {ts.name}")
                    s["missing"] += 1
                else:
                    cls = classify_lean(lp)
                    s[cls] += 1
                    if cls == "sorry":
                        sorries.append((ch, ts.stem, kind,
                                        lp.relative_to(REPO), sorry_refs(lp)))
        for qa in sorted(d.glob("*.qa.json")):
            try:
                data = json.loads(qa.read_text())
            except Exception:
                continue
            s["qa_side"] += 1
            failing = [c for c, e in (data.get("criteria") or {}).items()
                       if e and e[-1].get("result") == "fail"]
            s["qa_fail_crit"] += len(failing)
            s["da_fail"] += sum(1 for c in failing if c.startswith("da-"))
            if failing:
                s["qa_fail_blocks"] += 1
                fails_here.append((data.get("label") or qa.stem, sorted(failing)))
            sh = data.get("source_hashes") or {}
            for ext in ("md", "ts"):
                f = qa.with_name(qa.name.replace(".qa.json", "." + ext))
                if sh.get(ext) and f.exists() and h12(f) != sh[ext]:
                    s["qa_stale"] += 1
                    break
        rows.append((num, ch, s))
        drill[ch] = fails_here
    return rows, drill, sorries


def fail_by_criterion():
    out = {}
    for qa in ROOT.rglob("*.qa.json"):
        try:
            data = json.loads(qa.read_text())
        except Exception:
            continue
        for c, e in (data.get("criteria") or {}).items():
            if e and e[-1].get("result") == "fail":
                out[c] = out.get(c, 0) + 1
    return out


def totals(rows):
    T = {k: 0 for k in rows[0][2]}
    for _, _, s in rows:
        for k in T:
            T[k] += s[k]
    return T


def main():
    rows, drill, sorries = collect()
    T = totals(rows)
    crit = fail_by_criterion()

    if "--md" in sys.argv:
        idx = sys.argv.index("--md")
        if idx + 1 >= len(sys.argv):
            sys.exit("Error: --md requires an output file path.")
        out = Path(sys.argv[idx + 1])
        L = []
        L.append("# Lean proof progress + QA sidecar report — per chapter\n")
        L.append("Generated by `scripts/lean-qa-progress-table.py`. "
                 "**proved** = resolved Lean source is sorry-free (compile "
                 "status is per last CI, not re-verified here); **sorry** = "
                 "drafted with `sorry`; **stub** = trivial `: True` "
                 "placeholder; **none** = provable block with no resolvable "
                 "Lean. QA columns read the latest entry per criterion in "
                 "each `<block>.qa.json`; **stale** = sidecar source hashes "
                 "drifted from current `.md`/`.ts`.\n")
        L.append("## Per-chapter table\n")
        L.append("| # | Chapter | blocks | thm/lem/prop/cor | prov | proved | sorry | stub | none | QA sidecars | QA fail blocks | QA fail crit | da-* fails | stale |")
        L.append("|--:|---|--:|:-:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
        for num, ch, s in rows:
            L.append(f'| {num} | {ch} | {s["blocks"]} | {s["thm"]}/{s["lem"]}/{s["prop"]}/{s["cor"]} | {s["prov"]} | {s["proved"]} | {s["sorry"]} | {s["stub"]} | {s["missing"]} | {s["qa_side"]} | {s["qa_fail_blocks"]} | {s["qa_fail_crit"]} | {s["da_fail"]} | {s["qa_stale"]} |')
        L.append(f'| | **TOTAL** | **{T["blocks"]}** | **{T["thm"]}/{T["lem"]}/{T["prop"]}/{T["cor"]}** | **{T["prov"]}** | **{T["proved"]}** | **{T["sorry"]}** | **{T["stub"]}** | **{T["missing"]}** | **{T["qa_side"]}** | **{T["qa_fail_blocks"]}** | **{T["qa_fail_crit"]}** | **{T["da_fail"]}** | **{T["qa_stale"]}** |')
        L.append("\n## Failing criteria, corpus-wide\n")
        L.append("| Fails | Criterion |")
        L.append("|--:|---|")
        for c, n in sorted(crit.items(), key=lambda x: -x[1]):
            L.append(f"| {n} | `{c}` |")
        L.append("\n## Sorry acceptability — `-- Ref:` citation audit (AGENTS.md §1)\n")
        L.append("A `sorry` is acceptable only with a bibliographic `-- Ref:` "
                 "citation on or just above it. Uncited sorries are review "
                 "failures.\n")
        ok = sum(1 for *_, refs in sorries if refs and all(r for _, r in refs))
        L.append(f"**{len(sorries)} provable blocks carry sorries; "
                 f"{ok} fully cited (acceptable), {len(sorries) - ok} have "
                 "at least one uncited sorry.**\n")
        L.append("| Chapter | Block | Lean file | sorries | cited | Ref keys / ⚠ uncited lines |")
        L.append("|---|---|---|--:|--:|---|")
        for ch, blk, kind, lp, refs in sorries:
            cited = [r for _, r in refs if r]
            unc = [str(ln) for ln, r in refs if not r]
            keys = ", ".join(f"`{k}`" for k in dict.fromkeys(cited))
            if unc:
                keys += (", " if keys else "") + f"⚠ uncited @ {', '.join(unc)}"
            L.append(f"| {ch} | `{blk}` ({kind}) | `{lp}` | {len(refs)} | {len(cited)} | {keys} |")
        L.append("\n## Block-level drill-down (blocks with failing criteria)\n")
        for num, ch, s in rows:
            if not drill[ch]:
                continue
            L.append(f"### {num}. {ch} — {s['qa_fail_blocks']} failing blocks\n")
            L.append("| Block | Failing criteria |")
            L.append("|---|---|")
            for label, failing in drill[ch]:
                L.append(f"| `{label}` | {', '.join('`'+c+'`' for c in failing)} |")
            L.append("")
        out.write_text("\n".join(L) + "\n")
        print(f"wrote {out}")
        return

    hdr = ["#", "chapter", "blocks", "thm/lem/prop/cor", "prov", "proved",
           "sorry", "stub", "none", "qa_side", "qa_fail_blocks",
           "qa_fail_crit", "da_fail", "qa_stale"]
    print("\t".join(hdr))
    for num, ch, s in rows:
        print("\t".join(str(x) for x in [
            num, ch, s["blocks"],
            f'{s["thm"]}/{s["lem"]}/{s["prop"]}/{s["cor"]}', s["prov"],
            s["proved"], s["sorry"], s["stub"], s["missing"], s["qa_side"],
            s["qa_fail_blocks"], s["qa_fail_crit"], s["da_fail"], s["qa_stale"]]))
    print("\t".join(str(x) for x in [
        "", "TOTAL", T["blocks"],
        f'{T["thm"]}/{T["lem"]}/{T["prop"]}/{T["cor"]}', T["prov"],
        T["proved"], T["sorry"], T["stub"], T["missing"], T["qa_side"],
        T["qa_fail_blocks"], T["qa_fail_crit"], T["da_fail"], T["qa_stale"]]))


if __name__ == "__main__":
    main()
