#!/usr/bin/env python3
"""Heuristic-based sub-claim summary extractor.

For .lean files with generic claim_i, claim_ii, ... fields, walk the
sibling .md, locate each numbered sub-claim block (1., 2., 3., ...),
and extract its leading sentence / formula as a sub-claim docstring
summary.

Replaces:

    /-- Manuscript sub-claim (i). -/
    claim_i : Prop

with:

    /-- Manuscript sub-claim (i): <first-sentence-or-formula>. -/
    claim_i : Prop

This is a docstring-only enrichment — no Lean code changes.
"""

from __future__ import annotations

import re
import pathlib
import sys


ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']


def find_md_sibling(lean_path: pathlib.Path) -> pathlib.Path | None:
    """Find the .md sibling for a given .lean file by name."""
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


def extract_numbered_subclaims(md_text: str) -> dict[int, str]:
    """Walk .md, locate numbered sub-claims (1., 2., 3., ...),
    return dict[index → first-sentence-or-formula summary].

    Returns up to 10 entries.  Falls back to empty string if no
    summary text is found.
    """
    lines = md_text.split('\n')
    subclaims: dict[int, str] = {}
    current_n: int | None = None
    current_buf: list[str] = []

    for line in lines:
        # Detect start of a numbered sub-claim.
        m = re.match(r'^\s*(?:\*\*)?(\d+)\.(?:\*\*)?\s+(.*)$', line)
        if m:
            n = int(m.group(1))
            rest = m.group(2)
            if 1 <= n <= 10 and (current_n is None or n == current_n + 1):
                # Flush previous
                if current_n is not None and current_buf:
                    subclaims[current_n] = _summarize(current_buf)
                current_n = n
                current_buf = [rest]
                continue

        if current_n is not None:
            current_buf.append(line)

    # Flush last
    if current_n is not None and current_buf:
        subclaims[current_n] = _summarize(current_buf)

    return subclaims


def _summarize(buf: list[str]) -> str:
    """Take the first meaningful sentence / formula from the buffer.

    Strips bold markup, takes up to ~100 chars.
    """
    text = '\n'.join(buf)
    # Pull the first sentence (up to period or first display equation)
    text = text.strip()
    # Replace markdown bold and italic
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    # Take the first paragraph
    paragraph = text.split('\n\n')[0]
    # Strip trailing markdown reference links / footnotes
    paragraph = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', paragraph)
    # Take the first sentence
    sentence = re.split(r'\.(?:\s|$)', paragraph, maxsplit=1)[0]
    sentence = sentence.strip().replace('\n', ' ')
    sentence = re.sub(r'\s+', ' ', sentence)
    # Cap length
    if len(sentence) > 120:
        sentence = sentence[:117] + '...'
    # Escape Lean's `/-` doc-comment terminator
    sentence = sentence.replace('-/', '- /')
    return sentence


def upgrade_lean_file(lean_path: pathlib.Path) -> bool:
    """Apply the upgrade.  Returns True if changed."""
    text = lean_path.read_text()

    # Find all generic /-- Manuscript sub-claim (X). -/\n  claim_X : Prop blocks
    pattern = re.compile(
        r'(  /-- )Manuscript sub-claim \((' + '|'.join(ROMAN) + r')\)(\. -/\n  claim_\2 : Prop)',
    )

    matches = list(pattern.finditer(text))
    if not matches:
        return False

    md = find_md_sibling(lean_path)
    if md is None:
        return False
    subclaims = extract_numbered_subclaims(md.read_text())
    if not subclaims:
        return False

    def replace_match(m: re.Match[str]) -> str:
        roman = m.group(2)
        index = ROMAN.index(roman) + 1
        summary = subclaims.get(index, '')
        if not summary:
            return m.group(0)
        return f'{m.group(1)}Manuscript sub-claim ({roman}) — {summary}{m.group(3)}'

    new_text = pattern.sub(replace_match, text)
    if new_text == text:
        return False
    lean_path.write_text(new_text)
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
            # print(f'enriched: {p}')
        else:
            unchanged += 1

    print(f'Done. {changed} enriched, {unchanged} unchanged.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
