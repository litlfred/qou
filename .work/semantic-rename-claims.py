#!/usr/bin/env python3
"""Rename generic `claim_i, claim_ii, ...` to semantic identifiers.

Reads the enriched docstring `Manuscript sub-claim (X) — <summary>`
and uses keywords from the summary to construct a semantic name like
`claim_i_<noun_phrase>`.

Only renames; doesn't change types. Pure cosmetic improvement.
"""

from __future__ import annotations

import re
import pathlib
import sys


ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']


STOPWORDS = {
    'a', 'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'of', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'from', 'as', 'and',
    'or', 'but', 'if', 'then', 'else', 'when', 'where', 'this', 'that',
    'these', 'those', 'it', 'its', 'their', 'his', 'her', 'our',
    'has', 'have', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'must', 'can', 'shall', 'each', 'every',
    'all', 'any', 'some', 'no', 'not', 'only', 'just', 'also', 'too',
    'very', 'so', 'such', 'than', 'one', 'two', 'three', 'four', 'five',
}


def make_semantic_id(summary: str) -> str:
    """Build a snake_case identifier from the first 2-3 noun phrase words."""
    # Strip leading parenthetical "(Universal factorization.)" and
    # markdown remnants
    text = re.sub(r'^\([^)]+\)\s*', '', summary)
    text = re.sub(r'[^\w\s\$]+', ' ', text)
    text = re.sub(r'\$[^$]+\$', '', text)  # drop math
    text = re.sub(r'\s+', ' ', text).strip().lower()

    words = text.split()
    # Filter stopwords, single letters, numbers
    kept: list[str] = []
    for w in words:
        if w in STOPWORDS:
            continue
        if len(w) <= 1:
            continue
        if w.isdigit():
            continue
        kept.append(w)
        if len(kept) >= 3:
            break

    if not kept:
        return ''
    return '_'.join(kept)


def find_md_sibling(lean_path: pathlib.Path) -> pathlib.Path | None:
    base_underscore = lean_path.stem
    base_hyphen = lean_path.stem.replace('_', '-')

    root = pathlib.Path('content/quantum-observable-universe')
    if not root.is_dir():
        return None

    candidates: list[pathlib.Path] = []
    for name in (base_hyphen, base_underscore):
        candidates.extend(root.glob(f'**/{name}.md'))

    candidates = [c for c in candidates if 'lean/' not in str(c)]
    if candidates:
        candidates.sort(key=lambda p: len(p.parts))
        return candidates[0]
    return None


def upgrade_lean_file(lean_path: pathlib.Path) -> bool:
    text = lean_path.read_text()

    # Match: /-- Manuscript sub-claim (X) — <summary>. -/\n  claim_X : Prop
    pattern = re.compile(
        r'(  /-- Manuscript sub-claim \((' + '|'.join(ROMAN) + r')\)) '
        r'—\s*([^\n]+?)\.?\s*-/\n  claim_\2 : Prop',
    )

    matches = list(pattern.finditer(text))
    if not matches:
        return False

    # Build rename plan
    renames: dict[str, str] = {}  # claim_i → claim_i_xxx
    for m in matches:
        roman = m.group(2)
        summary = m.group(3)
        semantic = make_semantic_id(summary)
        if not semantic:
            continue
        new_name = f'claim_{roman}_{semantic}'
        if len(new_name) > 60:
            # too long, truncate
            new_name = new_name[:60].rstrip('_')
        renames[f'claim_{roman}'] = new_name

    if not renames:
        return False

    # Apply renames, longest first to avoid prefix issues
    for old, new in sorted(renames.items(), key=lambda x: -len(x[0])):
        # Replace `claim_X : Prop` definitions
        text = re.sub(
            rf'(\b){re.escape(old)}(\s*:\s*Prop\b)',
            rf'\1{new}\2',
            text,
        )
        # Replace `ctx.claim_X` references
        text = re.sub(
            rf'\bctx\.{re.escape(old)}\b',
            f'ctx.{new}',
            text,
        )

    lean_path.write_text(text)
    return True


def main() -> int:
    targets = sys.argv[1:]
    if not targets:
        targets = []
        for p in pathlib.Path('content/quantum-observable-universe/lean/QOU').rglob('*.lean'):
            text = p.read_text()
            if re.search(r'^  claim_i : Prop$', text, re.MULTILINE):
                targets.append(str(p))

    changed = 0
    unchanged = 0
    for tgt in targets:
        p = pathlib.Path(tgt)
        if not p.is_file():
            continue
        if upgrade_lean_file(p):
            changed += 1
            # print(f'renamed: {p}')
        else:
            unchanged += 1

    print(f'Done. {changed} renamed, {unchanged} unchanged.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
