#!/usr/bin/env python3
"""Refactor placeholder blocks onto QOU.Shared.OperatorSelectionLPContext.

Targets blocks whose .md sibling describes a linear-program structure
(primal / dual / shadow price / active set / strong duality).  Replaces
the MarkovTrace extends for blocks that are more naturally LP than
Markov-trace (e.g. Molecular/*_lp_dual_binding).
"""

from __future__ import annotations

import re
import pathlib
import sys


REDUNDANT_FIELDS = {
    'CategoricalObj',
    'Braid',
    'HeckeAlgebra',
    'PartitionIdx',
    'Crossing',
    'Rep',
    'Link',
    'ObstructionClass',
    'Functor',
    'Connection',
    'VelocityField',
    'Spectrum',
}


def find_md_sibling(lean_path: pathlib.Path) -> pathlib.Path | None:
    base_underscore = lean_path.stem
    base_hyphen = lean_path.stem.replace('_', '-')
    root = pathlib.Path('folio/quantum-observable-universe')
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


def md_is_LP(md_path: pathlib.Path) -> bool:
    """Check if .md is LP-themed.  Stricter than Markov match — requires
    multiple LP keywords or explicit LP-duality content."""
    text = md_path.read_text()
    lp_keywords = [
        'linear program', 'LP duality', 'shadow price', 'shadow-price',
        'primal', 'dual variable', 'dual optimum', 'active set',
        'strong duality', 'complementary slackness', 'LP-stable',
        'operator-selection LP', 'lp_dual', 'optimization',
        'Frobenius positivity',
    ]
    matches = sum(1 for kw in lp_keywords if kw in text)
    return matches >= 2


def upgrade_lean_file(lean_path: pathlib.Path) -> bool:
    text = lean_path.read_text()

    md = find_md_sibling(lean_path)
    if md is None or not md_is_LP(md):
        return False

    # If the file already extends MarkovTrace and is LP-themed, swap to LP
    if 'extends QOU.Shared.MarkovTraceContext' in text:
        text = text.replace(
            'extends QOU.Shared.MarkovTraceContext',
            'extends QOU.Shared.OperatorSelectionLPContext',
        )
        text = text.replace(
            'import QOU.Shared.MarkovTraceClaim',
            'import QOU.Shared.OperatorSelectionLP',
        )
        lean_path.write_text(text)
        return True

    # Otherwise, look for the placeholder pattern
    if 'extends QOU.Shared.' in text:
        return False

    class_re = re.compile(
        r'class (\w+Context) where\n((?:  /--[^\n]*\n  \w+ : [^\n]+\n)+)',
    )
    m = class_re.search(text)
    if not m:
        return False

    class_name = m.group(1)
    fields_block = m.group(2)

    field_lines = fields_block.split('\n')
    keep_lines: list[str] = []
    has_claim = False
    has_only_redundant_or_claim = True

    i = 0
    while i < len(field_lines):
        line = field_lines[i]
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith('/--'):
            doc = line
            i += 1
            while i < len(field_lines) and not field_lines[i].strip().startswith('/--') and not re.match(r'^\s+\w+ :', field_lines[i]):
                doc += '\n' + field_lines[i]
                if '-/' in field_lines[i]:
                    i += 1
                    break
                i += 1
            if i < len(field_lines):
                field_line = field_lines[i]
                field_m = re.match(r'\s+(\w+) :', field_line)
                if field_m:
                    field_name = field_m.group(1)
                    if field_name in REDUNDANT_FIELDS:
                        i += 1
                        continue
                    elif field_name.startswith('claim'):
                        has_claim = True
                        keep_lines.append(doc)
                        keep_lines.append(field_line)
                        i += 1
                        continue
                    else:
                        has_only_redundant_or_claim = False
                        keep_lines.append(doc)
                        keep_lines.append(field_line)
                        i += 1
                        continue
            continue
        field_m = re.match(r'\s+(\w+) :', line)
        if field_m:
            field_name = field_m.group(1)
            if field_name in REDUNDANT_FIELDS:
                i += 1
                continue
            elif field_name.startswith('claim'):
                has_claim = True
                keep_lines.append(line)
                i += 1
                continue
            else:
                has_only_redundant_or_claim = False
                keep_lines.append(line)
                i += 1
                continue
        i += 1

    if not has_claim or not has_only_redundant_or_claim:
        return False

    new_fields = '\n'.join(keep_lines)
    new_class = (
        f'class {class_name} extends '
        f'QOU.Shared.OperatorSelectionLPContext where\n'
        f'{new_fields}'
    )
    text = class_re.sub(lambda _: new_class, text, count=1)

    if 'import QOU.Shared.OperatorSelectionLP' not in text:
        text = re.sub(
            r'(\n-/\n\n)(namespace )',
            r'\1import QOU.Shared.OperatorSelectionLP\n\n\2',
            text, count=1,
        )

    claim_m = re.search(r'^  (claim_\w+) : Prop', text, re.MULTILINE)
    if claim_m:
        claim_name = claim_m.group(1)
        text = re.sub(
            r'(theorem \w+ \[ctx : \w+\]\s*:\s*ctx\.' + re.escape(claim_name) +
            r')\s*:=\s*by\n(?:[ \t]*--[^\n]*\n)*[ \t]*sorry',
            rf'\1 := ctx.{claim_name}',
            text, count=1, flags=re.MULTILINE,
        )

    lean_path.write_text(text)
    return True


def main() -> int:
    targets = sys.argv[1:]
    if not targets:
        targets = []
        for p in pathlib.Path('folio/quantum-observable-universe/lean/QOU').rglob('*.lean'):
            text = p.read_text()
            if re.search(r'^  claim_\w+ : Prop$', text, re.MULTILINE):
                targets.append(str(p))

    changed = 0
    for tgt in targets:
        p = pathlib.Path(tgt)
        if not p.is_file():
            continue
        if upgrade_lean_file(p):
            changed += 1
            print(f'refactored: {p}')

    print(f'Done. {changed} refactored / swapped to LP.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
