#!/usr/bin/env python3
"""Read-only corpus audit for monograph fourth-wall Lean leaks, voice leaks, and chapter-order anachronisms.

Scans every .md file under folio/quantum-observable-universe/ (excluding lean/, .lake/,
and rendered/) in exact monograph reading order (from quantum-observable-universe.ts
and each chapter's <dir>/<dir>.ts manifest), classifying all hits across four categories:

  - Class L1 (lean-prose-mention):
      Explicit prose mentions of Lean, Lean carrier, Lean sibling, Lean backing,
      Lean file, Lean module, Lean theorem, Lean proof, Mathlib, formalised/formalized in,
      proved formally / formally proved.
  - Class L2 (lean-ident-in-prose):
      Backticked Lean FQNs (`QOU.Foo...`, `Mathlib...`), Lean typeclass/type names
      (`CommRing`, `IsQGeneric`, `Fin n`, etc.), raw backticked block IDs
      (`def:foo`, `thm:bar`), or Lean snake_case / camelCase declaration identifiers
      (`dimQK0_eq_evDimQ_chernCharacter`, `su2Character_one`, `exteriorSquareDim_ne_zero_iff`)
      appearing in narrative .md prose outside fenced code blocks.
  - Class L3 (first-second-person):
      First-person (`we`, `our`, `ours`, `us`, `let's`, `I`, `my`) and second-person
      (`you`, `your`, `yours`) pronouns in narrative .md prose outside fenced code,
      inline code, and math mode.
  - Class L4 (chapter-order-anachronism in Part I Foundations, Ch 1 & Ch 2):
      (L4a) Premature forward-concept leaks in Chapter 1 (`quantum-universes/*.md`)
            referencing substrate parameter q, quantum integers [n]_q, Hecke algebras
            H_n(q), cyclotomic polynomials Phi_d(q), SU_q(2), or the archimedean wall
            before Chapter 2 Section 7 (`sec:substrate-parameter`).
      (L4b) Forward cross-reference links `](#label)` in Chapters 1 and 2 where the
            target block appears later in monograph reading order than the citing block.

Zero float64, read-only on all manuscript files.
Witness: computations/audits/monograph-lean-and-voice-leak-audit.witness.json
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in (
    "computations",
    "computations/substrate",
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80

FOLIO_DIR = Path(ROOT) / "folio" / "quantum-observable-universe"

# ---------------------------------------------------------------------------
# Section 1: Parse monograph chapter & block reading order from .ts manifests
# ---------------------------------------------------------------------------
CHAPTER_REF_RE = re.compile(r'chapterRef\(\{\s*dir:\s*"([^"]+)"')
BLOCKS_ARRAY_RE = re.compile(r"blocks:\s*\[([^\]]*)\]", re.DOTALL)
STRING_LITERAL_RE = re.compile(r'"([a-zA-Z0-9_-]+)"')
BLOCK_KIND_LABEL_RE = re.compile(
    r'export\s+default\s+(definition|theorem|proposition|lemma|corollary|conjecture|remark|example|proof|prose|table)\s*\(\s*\{[\s\S]*?\blabel:\s*"([^"]+)"',
    re.MULTILINE,
)


def load_monograph_structure() -> tuple[
    list[str],
    dict[str, list[str]],
    dict[str, tuple[str, int, int]],
    dict[str, str],
]:
    """Return (chapter_dirs, chapter_to_blocks, label_to_pos, block_key_to_label).

    label_to_pos maps full label (e.g. 'def:frobenius-hopf-substrate') -> (chapter_dir, chapter_idx, global_block_idx).
    """
    paper_ts = (FOLIO_DIR / "quantum-observable-universe.ts").read_text(encoding="utf-8")
    chapter_dirs = CHAPTER_REF_RE.findall(paper_ts)

    chapter_to_blocks: dict[str, list[str]] = {}
    label_to_pos: dict[str, tuple[str, int, int]] = {}
    block_key_to_label: dict[str, str] = {}

    kind_prefix = {
        "definition": "def",
        "theorem": "thm",
        "proposition": "prop",
        "lemma": "lem",
        "corollary": "cor",
        "conjecture": "conj",
        "remark": "rem",
        "example": "ex",
        "table": "tab",
    }

    global_idx = 0
    for ch_idx, ch_dir in enumerate(chapter_dirs):
        ch_ts_path = FOLIO_DIR / ch_dir / f"{ch_dir}.ts"
        blocks: list[str] = []
        if ch_ts_path.exists():
            ch_src = ch_ts_path.read_text(encoding="utf-8")
            # Strip line comments before extracting block names
            ch_src_nocomment = re.sub(r"//[^\n]*", "", ch_src)
            for arr_match in BLOCKS_ARRAY_RE.finditer(ch_src_nocomment):
                for b_name in STRING_LITERAL_RE.findall(arr_match.group(1)):
                    if b_name not in blocks:
                        blocks.append(b_name)
        chapter_to_blocks[ch_dir] = blocks

        for b_name in blocks:
            global_idx += 1
            b_ts_path = FOLIO_DIR / ch_dir / f"{b_name}.ts"
            if b_ts_path.exists():
                b_src = b_ts_path.read_text(encoding="utf-8")
                m = BLOCK_KIND_LABEL_RE.search(b_src)
                if m:
                    kind, raw_label = m.group(1), m.group(2)
                    if ":" in raw_label:
                        full_label = raw_label
                    elif kind in kind_prefix:
                        full_label = f"{kind_prefix[kind]}:{raw_label}"
                    else:
                        full_label = raw_label
                    label_to_pos[full_label] = (ch_dir, ch_idx, global_idx)
                    label_to_pos[raw_label] = (ch_dir, ch_idx, global_idx)
                    block_key_to_label[f"{ch_dir}/{b_name}"] = full_label
            # Also index by block stem for bare `#block-stem` references
            if b_name not in label_to_pos:
                label_to_pos[b_name] = (ch_dir, ch_idx, global_idx)

    return chapter_dirs, chapter_to_blocks, label_to_pos, block_key_to_label


# ---------------------------------------------------------------------------
# Section 2: Leak Detectors (Classes L1, L2, L3, L4)
# ---------------------------------------------------------------------------

# Class L1: Explicit prose mentions of Lean / Mathlib / formalisation mechanics
L1_LEAN_PROSE_RE = re.compile(
    r"\bLean\s+(?:4\b|carrier|sibling|backing|file|module|proof|theorem|lemma|definition|declaration|structure|formalisation|formalization|implementation|companion|namespace|typeclass|code|source|verify|verification)"
    r"|\bin\s+Lean(?:\s+4)?\b"
    r"|\bLean's\b"
    r"|\bLean\b"
    r"|\bMathlib\b"
    r"|\bproved\s+formally\b"
    r"|\bformally\s+proved\b"
    r"|\bformali[sz]ed\s+in\b"
    r"|\bdischarges?\s+the\s+axiom"
    r"|\bstays\s+at\s+`CommRing`",
    re.IGNORECASE,
)

# Class L2: Backticked Lean identifiers or raw block IDs in narrative prose
BACKTICK_SPAN_RE = re.compile(r"`([^`\n]+)`")

L2_FQN_RE = re.compile(
    r"^(?:QOU|Mathlib|Real|Nat|Int|Rat|Finset|Matrix|Polynomial|Complex|CategoryTheory|Algebra|Ring|LinearAlgebra)\.[A-Za-z0-9_.']+$"
)
L2_LEAN_FILE_RE = re.compile(r"^[A-Za-z0-9_./-]+\.lean$")
L2_RAW_BLOCK_ID_RE = re.compile(
    r"^(?:def|thm|prop|lem|cor|conj|rem|ex|sec|chap|app|tab):[a-z0-9-]+$"
)
L2_LEAN_TYPE_OR_DECL_RE = re.compile(
    r"^(?:"
    r"CommRing|Field|LinearOrderedField|IsQGeneric|Fintype|DecidableEq|Nonempty|Unique"
    r"|\[[A-Z][A-Za-z0-9_ ]+\]"  # Lean typeclass binders like `[Add H]`, `[CommRing R]`
    r"|[A-Z][a-zA-Z0-9]+(?:\s+[A-Za-z0-9_]+)+"  # Lean type applications like `HochschildZero R A`
    r"|[a-z][a-zA-Z0-9]*_[a-zA-Z0-9_]+"  # snake_case / mixed snake+camel Lean theorem names
    r"|[a-z][a-z0-9]+(?:[A-Z][a-z0-9]+){1,}"  # camelCase Lean declarations (e.g. traceOnHochschildZero, exteriorSquareDim)
    r"|Is[A-Z][a-zA-Z0-9]+"  # Lean Prop predicates IsFooBar
    r")$"
)

# Exclude legitimate domain/data tokens inside backticks (e.g., Liquid/witness keys or Python/algorithm appendix tokens)
L2_EXEMPT_TOKENS = {
    "plain",
    "KnKp",
    "Kp3",
    "nuc11_interleaved",
    "nuc11_gen_grouped",
    "true",
    "false",
}

# Class L3: First-person and second-person pronouns in narrative prose
L3_FIRST_SECOND_PERSON_RE = re.compile(
    r"\b(?:we|we're|we've|we'll|our|ours|us|let's|you|you're|you'll|your|yours)\b"
    r"|\bthe\s+reader\s+(?:will|can|may|might|should|finds?|knows?|notices?|observes?|sees?)\b",
    re.IGNORECASE,
)

# Class L4a: Premature Chapter 1 (`quantum-universes`) forward concepts before Ch 2 §7 (`sec:substrate-parameter`)
L4A_CH1_PREMATURE_CONCEPT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("substrate-parameter-phrase", re.compile(r"\bsubstrate\s+(?:parameter|anchor)\b", re.IGNORECASE)),
    ("archimedean-wall-phrase", re.compile(r"\barchimedean\s+wall\b", re.IGNORECASE)),
    ("hecke-basis-or-decomposition", re.compile(r"\bHecke\s+(?:basis|decompositions?|algebras?|-type)\b", re.IGNORECASE)),
    ("cyclotomic-polynomial-Phi_d", re.compile(r"\\Phi_[0-9d]\b|\b[Cc]yclotomics?\b")),
    ("q-deformed-or-quantum-group-SU_q", re.compile(r"\bq-deformed\b|\\mathrm\{SU\}_q\(2\)|quantum\s+groups?\s*\(\s*\$?q\s*\\neq\s*1", re.IGNORECASE)),
    ("quantum-integer-bracket-q", re.compile(r"\[[0-9nm+ -]+\]_q\b")),
    ("dim_q-notation-before-q", re.compile(r"\\dim_q\b")),
    ("laurent-ring-Z-q-qinv", re.compile(r"\\mathbb\{Z\}\[q,\s*q\^\{-1\}\]")),
]

# Class L4b: Markdown internal cross-reference links `](#label)`
MD_INTERNAL_LINK_RE = re.compile(r"\[([^\]]+)\]\(#([a-zA-Z0-9_:-]+)\)")


def strip_math_and_links_for_prose(line: str) -> str:
    """Strip inline/display math, backtick spans, link targets, and Liquid tags before scanning prose words."""
    s = re.sub(r"\{\{[^}]*\}\}", " ", line)
    s = re.sub(r"\$\$[^$]*\$\$", " ", s)
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"`[^`]+`", " ", s)
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r":(?:refterm|defterm)\[([^\]]*)\]\{#[^}]*\}", r"\1", s)
    return s


def scan_md_file(
    md_path: Path,
    ch_dir: str,
    ch_idx: int,
    block_name: str,
    global_block_idx: int,
    label_to_pos: dict[str, tuple[str, int, int]],
) -> dict[str, list[dict[str, object]]]:
    """Scan a single .md file and return hits keyed by L1, L2, L3, L4."""
    rel_path = str(md_path.relative_to(FOLIO_DIR))
    lines = md_path.read_text(encoding="utf-8").splitlines()

    hits: dict[str, list[dict[str, object]]] = {
        "L1": [],
        "L2": [],
        "L3": [],
        "L4": [],
    }

    in_fence = False
    in_display_math = False

    for line_idx, raw_line in enumerate(lines):
        line_no = line_idx + 1
        stripped_line = raw_line.strip()

        if stripped_line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # Track multi-line $$ ... $$ blocks
        if stripped_line == "$$":
            in_display_math = not in_display_math
            continue

        prose_line = strip_math_and_links_for_prose(raw_line)

        # --- Class L1: Lean / Mathlib / formalisation mentions in prose ---
        if not in_display_math:
            for m1 in L1_LEAN_PROSE_RE.finditer(prose_line):
                token = m1.group(0)
                # Guard against mathematical "lean" verb if any (case-sensitive check for bare 'Lean')
                if token.lower() == "lean" and token != "Lean":
                    continue
                hits["L1"].append(
                    {
                        "file": rel_path,
                        "chapter": ch_dir,
                        "block": block_name,
                        "line": line_no,
                        "match": token,
                        "excerpt": stripped_line[:220],
                    }
                )

        # --- Class L2: Backticked Lean identifiers or raw block IDs in prose ---
        if not in_display_math:
            # Remove markdown link targets `](...)` first so backticks inside URLs don't fire
            line_no_urls = re.sub(r"\]\([^)]*\)", "]", raw_line)
            for m2 in BACKTICK_SPAN_RE.finditer(line_no_urls):
                code_token = m2.group(1).strip()
                if code_token in L2_EXEMPT_TOKENS:
                    continue
                l2_kind = None
                if L2_FQN_RE.match(code_token):
                    l2_kind = "lean-fqn"
                elif L2_LEAN_FILE_RE.match(code_token):
                    l2_kind = "lean-file-ref"
                elif L2_RAW_BLOCK_ID_RE.match(code_token):
                    l2_kind = "raw-block-id-backtick"
                elif L2_LEAN_TYPE_OR_DECL_RE.match(code_token):
                    l2_kind = "lean-decl-or-type"
                if l2_kind is not None:
                    hits["L2"].append(
                        {
                            "file": rel_path,
                            "chapter": ch_dir,
                            "block": block_name,
                            "line": line_no,
                            "subkind": l2_kind,
                            "match": f"`{code_token}`",
                            "excerpt": stripped_line[:220],
                        }
                    )

        # --- Class L3: First-person / second-person pronouns in prose ---
        if not in_display_math:
            for m3 in L3_FIRST_SECOND_PERSON_RE.finditer(prose_line):
                tok = m3.group(0)
                # Exclude uppercase "US" (country) if any
                if tok == "US":
                    continue
                hits["L3"].append(
                    {
                        "file": rel_path,
                        "chapter": ch_dir,
                        "block": block_name,
                        "line": line_no,
                        "match": tok,
                        "excerpt": stripped_line[:220],
                    }
                )

        # --- Class L4a: Premature q / Hecke / cyclotomic / archimedean-wall concepts in Chapter 1 ---
        if ch_dir == "quantum-universes":
            for subkind, pat in L4A_CH1_PREMATURE_CONCEPT_PATTERNS:
                m4a = pat.search(raw_line)
                if m4a:
                    hits["L4"].append(
                        {
                            "file": rel_path,
                            "chapter": ch_dir,
                            "block": block_name,
                            "line": line_no,
                            "subkind": f"L4a:{subkind}",
                            "match": m4a.group(0),
                            "excerpt": stripped_line[:220],
                        }
                    )

        # --- Class L4b: Forward cross-reference links in Chapters 1 and 2 ---
        if ch_dir in ("quantum-universes", "quantum-observable-universes") and global_block_idx > 0:
            for m4b in MD_INTERNAL_LINK_RE.finditer(raw_line):
                link_text, target_label = m4b.group(1), m4b.group(2)
                if target_label in label_to_pos:
                    t_ch, t_ch_idx, t_global_idx = label_to_pos[target_label]
                    if t_global_idx > global_block_idx:
                        direction = (
                            f"cross-chapter forward ref -> {t_ch} (#{target_label})"
                            if t_ch_idx > ch_idx
                            else f"intra-chapter forward ref -> {t_ch} (#{target_label}, +{t_global_idx - global_block_idx} blocks ahead)"
                        )
                        hits["L4"].append(
                            {
                                "file": rel_path,
                                "chapter": ch_dir,
                                "block": block_name,
                                "line": line_no,
                                "subkind": "L4b:forward-ref",
                                "match": f"[{link_text}](#{target_label})",
                                "target_chapter": t_ch,
                                "detail": direction,
                                "excerpt": stripped_line[:220],
                            }
                        )

    return hits


def main() -> int:
    chapter_dirs, chapter_to_blocks, label_to_pos, _ = load_monograph_structure()

    # Track active blocks from chapter .ts manifests (plus *-table*-data.md whose parent block is active)
    ordered_scan_units: list[tuple[Path, str, int, str, int]] = []
    active_md_set: set[Path] = set()

    global_idx = 0
    for ch_idx, ch_dir in enumerate(chapter_dirs):
        active_stems = set(chapter_to_blocks.get(ch_dir, []))
        for b_name in chapter_to_blocks.get(ch_dir, []):
            global_idx += 1
            md_path = FOLIO_DIR / ch_dir / f"{b_name}.md"
            if md_path.exists():
                active_md_set.add(md_path.resolve())
                ordered_scan_units.append((md_path, ch_dir, ch_idx, b_name, global_idx))

        # Include *-table*-data.md files belonging to active blocks in this chapter
        ch_path = FOLIO_DIR / ch_dir
        if ch_path.is_dir():
            for extra_md in sorted(ch_path.glob("*-table*-data.md")):
                parent_stem = re.sub(r"-table\d+-data$", "", extra_md.stem)
                if parent_stem in active_stems and extra_md.resolve() not in active_md_set:
                    active_md_set.add(extra_md.resolve())
                    ordered_scan_units.append((extra_md, ch_dir, ch_idx, extra_md.stem, global_idx))

    # Aggregate results per chapter and globally
    chapter_summary: dict[str, dict[str, int]] = {}
    all_hits: dict[str, list[dict[str, object]]] = {"L1": [], "L2": [], "L3": [], "L4": []}
    ch1_ch2_hits: dict[str, list[dict[str, object]]] = {"L1": [], "L2": [], "L3": [], "L4": []}

    for ch_dir in chapter_dirs:
        chapter_summary[ch_dir] = {"md_files": 0, "L1": 0, "L2": 0, "L3": 0, "L4": 0, "total": 0}

    for md_path, ch_dir, ch_idx, b_name, g_idx in ordered_scan_units:
        chapter_summary[ch_dir]["md_files"] += 1
        file_hits = scan_md_file(md_path, ch_dir, ch_idx, b_name, g_idx, label_to_pos)
        for cls in ("L1", "L2", "L3", "L4"):
            cnt = len(file_hits[cls])
            chapter_summary[ch_dir][cls] += cnt
            chapter_summary[ch_dir]["total"] += cnt
            all_hits[cls].extend(file_hits[cls])
            if ch_dir in ("quantum-universes", "quantum-observable-universes"):
                ch1_ch2_hits[cls].extend(file_hits[cls])

    total_md_files = sum(v["md_files"] for v in chapter_summary.values())
    totals_by_class = {cls: len(all_hits[cls]) for cls in ("L1", "L2", "L3", "L4")}

    print("=" * 104)
    print("QOU MONOGRAPH FOURTH-WALL LEAN, VOICE, AND CHAPTER-ORDER ANACHRONISM AUDIT")
    print("=" * 104)
    print(
        f"{'#':>2}  {'Chapter / Appendix Directory':<38} {'MDs':>5}  {'L1(Lean)':>8}  {'L2(`id`)':>8}  {'L3(we/you)':>10}  {'L4(Order)':>9}  {'Total':>6}"
    )
    print("-" * 104)
    for idx, ch_dir in enumerate(chapter_dirs, start=1):
        s = chapter_summary[ch_dir]
        print(
            f"{idx:>2}  {ch_dir:<38} {s['md_files']:>5}  {s['L1']:>8}  {s['L2']:>8}  {s['L3']:>10}  {s['L4']:>9}  {s['total']:>6}"
        )
    print("-" * 104)
    print(
        f"    {'TOTAL ACROSS MONOGRAPH':<38} {total_md_files:>5}  {totals_by_class['L1']:>8}  {totals_by_class['L2']:>8}  {totals_by_class['L3']:>10}  {totals_by_class['L4']:>9}  {sum(totals_by_class.values()):>6}"
    )
    print("=" * 104)

    print("\nDETAILED HITS IN CHAPTER 1 (quantum-universes) & CHAPTER 2 (quantum-observable-universes):")
    for cls, label in (
        ("L1", "Class L1 (lean-prose-mention)"),
        ("L2", "Class L2 (lean-ident-in-prose)"),
        ("L3", "Class L3 (first-second-person)"),
        ("L4", "Class L4 (chapter-order-anachronism)"),
    ):
        print(f"\n--- {label}: {len(ch1_ch2_hits[cls])} hit(s) in Ch 1-2 ---")
        for h in ch1_ch2_hits[cls]:
            extra = f" [{h.get('subkind', '')}]" if "subkind" in h else ""
            detail = f" ({h.get('detail', '')})" if "detail" in h else ""
            print(f"  {h['file']}:{h['line']}{extra} -> {h['match']}{detail}")
            print(f"      {h['excerpt']}")

    root_causes = {
        "gap_1_paper_commentary_audit_exemption": (
            "folio/pipeline/paper-commentary-audit.ts lines 11-12 & 74 explicitly exempted naming Lean "
            "declarations/carriers ('Naming the Lean declaration that states a result is fine; grading the Lean is not') "
            "and required 'Lean (backing|carrier|sibling|file)' to be followed within 80 chars by 'does not|doesn't|cannot'."
        ),
        "gap_2_qa_checkers_voice_backtick_stripping": (
            "folio-assistant/cat-harness-tools/pipeline/qa-checkers-voice.ts strips all inline backtick spans "
            "(`replace(/`[^`]+`/g, '')` in scanProse line 180 and stripInlineCode line 572) and has no detector "
            "for backticked Lean FQNs (`QOU.Foo`), Lean declaration identifiers (`foo_bar`), or raw block IDs (`def:foo`)."
        ),
        "gap_3_first_person_pronoun_narrow_regex": (
            "qa-checkers-voice.ts checkFirstPersonWork (line 286) only matches work-tracker futures/pasts "
            "('we'll add/fix', 'we should fix', 'we went ahead and'), and checkScholarlyDefault (lines 744, 754) "
            "only matches 'So what we...', 'Now we want...', or 'we proved/showed... above/earlier'. General "
            "first-person plural ('we can speak', 'we chose', 'We require', 'for us', 'our') is completely unguarded."
        ),
        "gap_4_chapter_1_anachronism_leak": (
            "Automated wall/q-usage checkers do not flag premature substrate-parameter q, [n]_q, Phi_d(q), "
            "Hecke basis, SU_q(2), or archimedean-wall discourse inside Chapter 1 (quantum-universes), even though "
            "the substrate parameter q is not introduced until Chapter 2 Section 7 (sec:substrate-parameter) and "
            "the Frobenius-Hopf substrate is not introduced until Chapter 2 Section 9 (sec:algebraic-substrate-reeb)."
        ),
    }

    checks = [
        (
            "scanned_all_36_monograph_chapters_and_appendices",
            len(chapter_dirs) == 36 and total_md_files >= 1100,
            f"Scanned {total_md_files} active monograph .md files across {len(chapter_dirs)} chapters/appendices in reading order",
        ),
        (
            "reproduced_all_owner_reported_ch1_ch2_leaks",
            (
                any(h["file"] == "quantum-universes/chern-character.md" and h["line"] == 31 for h in ch1_ch2_hits["L1"])
                and any(
                    h["file"] == "quantum-universes/su2-characters-and-quantum-dimension.md" and h["line"] == 17
                    for h in ch1_ch2_hits["L1"]
                )
                and any(
                    h["file"] == "quantum-universes/quantum-universe.md" and h["line"] == 38
                    for h in ch1_ch2_hits["L2"]
                )
                and any(
                    h["file"] == "quantum-observable-universes/quantum-observable-universe.md" and h["line"] in (33, 34)
                    for h in ch1_ch2_hits["L1"]
                )
                and any(
                    h["file"] == "quantum-universes/quantum-universe-axiom-motivation.md" and h["line"] == 5
                    for h in ch1_ch2_hits["L3"]
                )
                and any(
                    h["file"] == "quantum-universes/axiom-independence.md" and h["line"] == 3
                    for h in ch1_ch2_hits["L3"]
                )
            ),
            "Every owner-reported leak in Chapters 1 and 2 is captured with exact file:line coordinates",
        ),
    ]

    w = WitnessBuilder("monograph-lean-and-voice-leak-audit")
    w.set_description(
        "Read-only corpus audit of all 35 chapters and appendices under folio/quantum-observable-universe/ "
        "for Class L1 (Lean/Mathlib prose mentions), Class L2 (backticked Lean identifiers and raw block IDs in prose), "
        "Class L3 (first/second-person pronouns), and Class L4 (Chapter 1-2 reading-order anachronisms and forward refs)."
    )
    w.add_data("dps", 80)
    w.add_data("total_chapters_and_appendices", len(chapter_dirs))
    w.add_data("total_md_files_scanned", total_md_files)
    w.add_data("totals_by_class", totals_by_class)
    w.add_data("root_causes_of_checker_gaps", root_causes)
    w.add_data("chapter_summary", chapter_summary)
    w.add_data("ch1_ch2_detailed_hits", ch1_ch2_hits)
    w.add_data("corpus_hits_L1_lean_prose_mention", all_hits["L1"])
    w.add_data("corpus_hits_L2_lean_ident_in_prose", all_hits["L2"])
    w.add_data("corpus_hits_L3_first_second_person", all_hits["L3"])
    w.add_data("ch1_ch2_hits_L4_anachronisms_and_forward_refs", all_hits["L4"])
    w.add_caveat(
        "Read-only audit diagnostic witness: classifies candidate fourth-wall Lean leaks, first/second-person "
        "pronouns, and Part I reading-order anachronisms across the monograph corpus."
    )
    for name, passed, detail in checks:
        w.add_assertion(name, "1" if passed else "0", "1", "0", source=detail)

    out_path = w.save(
        {
            "q0Anchor": "independent",
            "q0AnchorReason": (
                "Purely textual and structural audit of monograph markdown files and chapter manifests; "
                "independent of the numerical substrate parameter q_0."
            ),
        }
    )
    print(f"\nWrote witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
