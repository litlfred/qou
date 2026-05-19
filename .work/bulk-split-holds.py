#!/usr/bin/env python3
"""Bulk-transform `holds : Prop` → `claim_i : Prop ∧ ... ∧ claim_N : Prop`.

For each .lean file with `holds : Prop` field + `ctx.holds` theorem:
1. Find the .md sibling
2. Count distinct numbered sub-claims (1., 2., 3., ... or **N.**, etc.)
3. If 2+ sub-claims: split `holds` into `claim_i, claim_ii, ...`, make
   theorem prove the conjunction.  Otherwise: rename `holds` → `claim`.

This is a mechanical transformation — sub-claim descriptions are generic
("Manuscript sub-claim (N)") rather than hand-crafted.  Substantive
content per block requires manual editing.
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

    # Search content/quantum-observable-universe/ for matching .md
    root = pathlib.Path('content/quantum-observable-universe')
    if not root.is_dir():
        return None

    candidates: list[pathlib.Path] = []
    for name in (base_hyphen, base_underscore):
        candidates.extend(root.glob(f'**/{name}.md'))

    # Skip the lean/ tree — we want the manuscript .md, not its sibling.
    candidates = [c for c in candidates if 'lean/' not in str(c)]

    if candidates:
        # Prefer shortest path (most direct match)
        candidates.sort(key=lambda p: len(p.parts))
        return candidates[0]
    return None


def count_numbered_subclaims(md_text: str) -> int:
    """Count distinct numbered sub-claims in the .md body.

    Looks for line-starting `N.` or `**N.**` patterns, requires
    consecutive numbering starting from 1.  Caps at 10.
    """
    lines = md_text.split('\n')
    seen: set[int] = set()
    for line in lines:
        stripped = line.lstrip()
        # Match `N.` (with optional bold) at start of line
        # Or `**N.**` boldformat
        m = re.match(r'(?:\*\*)?(\d+)\.(?:\*\*)?\s+', stripped)
        if m:
            n = int(m.group(1))
            if n <= 10:
                seen.add(n)

    # Only count if 1, 2, ... starting from 1 is present
    if 1 not in seen:
        return 0
    n = 1
    while n in seen and n <= 10:
        n += 1
    return n - 1  # final count


def upgrade_lean_file(lean_path: pathlib.Path) -> tuple[bool, int]:
    """Apply the bulk upgrade. Returns (changed, sub_claim_count)."""
    text = lean_path.read_text()

    # Pattern: `/-- ... -/\n  holds : Prop` followed somewhere by `ctx.holds`
    if not re.search(r'^  holds : Prop$', text, re.MULTILINE):
        return False, 0
    if 'ctx.holds' not in text:
        return False, 0

    md = find_md_sibling(lean_path)
    n_claims = count_numbered_subclaims(md.read_text()) if md else 0
    n_claims = min(n_claims, 6)  # cap at 6 — beyond that the .md is unusual

    if n_claims >= 2:
        # Build replacement fields
        roman_list = ROMAN[:n_claims]
        new_fields_lines = []
        for r in roman_list:
            new_fields_lines.append(
                f'  /-- Manuscript sub-claim ({r}). -/\n'
                f'  claim_{r} : Prop'
            )
        new_fields = '\n'.join(new_fields_lines)

        # Replace `/-- The Prop-valued claim of the lemma. -/\n  holds : Prop`
        old_pattern = (
            r'  /-- The `Prop`-valued claim of the lemma\. -/\n'
            r'  holds : Prop'
        )
        text = re.sub(old_pattern, new_fields, text, count=1)

        # Replace theorem signature `ctx.holds := by sorry` with conjunction
        conj = ' ∧ '.join(f'ctx.claim_{r}' for r in roman_list)
        constr = '⟨' + ', '.join(f'ctx.claim_{r}' for r in roman_list) + '⟩'

        # Match `theorem foo [ctx : FooContext] : ctx.holds := by\n ...sorry`
        # Note: theorem may be indented further if in a sub-namespace.
        theorem_pattern = re.compile(
            r'(theorem \w+ \[ctx : \w+\]) : ctx\.holds := by\n'
            r'(?:[ \t]*--[^\n]*\n)*'
            r'[ \t]*sorry',
            re.MULTILINE,
        )
        replacement = lambda m: (
            f'{m.group(1)} :\n    {conj} :=\n  {constr}'
        )
        text = theorem_pattern.sub(replacement, text, count=1)
    else:
        # Just rename `holds` → `claim`
        text = re.sub(
            r'(  /-- The `Prop`-valued claim of the lemma\. -/\n  )holds( : Prop)',
            r'\1claim\2',
            text, count=1,
        )
        text = text.replace('ctx.holds', 'ctx.claim')

    # Also update the boilerplate at the bottom of the docstring
    text = text.replace(
        'The Lean encoding below is a `theorem foo [ctx] : ctx.holds := by sorry`\n'
        '    placeholder; the `ctx.holds : Prop` field carries the residual claim,\n'
        '    awaiting per-block type-level translation.',
        'The Lean encoding below splits the manuscript claim into named\n'
        '    sub-claim fields; the residual sub-claim Props are still abstract.',
    )

    lean_path.write_text(text)
    return True, n_claims


def main() -> int:
    targets = sys.argv[1:]
    if not targets:
        # Default: all .lean files with holds:Prop in QOU/
        targets = []
        for p in pathlib.Path('content/quantum-observable-universe/lean/QOU').rglob('*.lean'):
            text = p.read_text()
            if re.search(r'^  holds : Prop$', text, re.MULTILINE):
                targets.append(str(p))

    changed_with_split = 0
    changed_with_rename = 0
    unchanged = 0

    for tgt in targets:
        p = pathlib.Path(tgt)
        if not p.is_file():
            print(f'SKIP (no file): {tgt}')
            continue
        changed, n = upgrade_lean_file(p)
        if changed:
            if n >= 2:
                changed_with_split += 1
                print(f'split {n}: {p}')
            else:
                changed_with_rename += 1
                # print(f'rename: {p}')
        else:
            unchanged += 1
            print(f'unchanged: {p}')

    print(f'\nDone. {changed_with_split} split, {changed_with_rename} renamed, '
          f'{unchanged} unchanged.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
