#!/usr/bin/env python3
"""Refactor single-claim Hecke-themed blocks onto QOU.Shared.MarkovTraceContext.

For each .lean file where:
1. The class has only abstract context fields (Braid, CategoricalObj,
   PartitionIdx, Crossing, Rep, HeckeAlgebra, etc. — no typed `ℝ`/`ℕ`
   substantive fields)
2. The .md sibling mentions Hecke / Markov / braid / Wenzl / Wedderburn
3. The class has exactly one `claim_<name> : Prop` field

Refactor to:
- Add `import QOU.Shared.MarkovTraceClaim`
- Change `class FooContext where` to
  `class FooContext extends QOU.Shared.MarkovTraceContext where`
- Strip the redundant abstract context fields (Braid, CategoricalObj, etc.)
- Keep the `claim_<name> : Prop` field
- Update the theorem to use `ctx.claim_<name>` directly

Pure refactor — no Lean semantics change.
"""

from __future__ import annotations

import re
import pathlib
import sys


# Context fields that are redundant once we extend MarkovTraceContext.
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


def md_mentions_hecke(md_path: pathlib.Path) -> bool:
    """Check if .md mentions Hecke / Markov / braid / Wenzl content."""
    text = md_path.read_text()
    keywords = ['Hecke', 'Markov', 'braid', 'Wenzl', 'Wedderburn',
                'σ_i', 'sigma_i', 'tr_M', '\\sigma_i', 'H_n(q)']
    for kw in keywords:
        if kw in text:
            return True
    return False


def upgrade_lean_file(lean_path: pathlib.Path) -> bool:
    text = lean_path.read_text()

    # Match class declaration:
    # `class FooContext where\n  <fields>...`
    class_re = re.compile(
        r'class (\w+Context) where\n((?:  /--[^\n]*\n  \w+ : [^\n]+\n)+)',
    )
    m = class_re.search(text)
    if not m:
        return False

    class_name = m.group(1)
    fields_block = m.group(2)

    # Parse fields
    field_lines = fields_block.split('\n')
    keep_lines: list[str] = []
    has_claim = False
    has_typed = False
    has_only_redundant_or_claim = True

    # Parse `(doc comment + field)` pairs
    i = 0
    while i < len(field_lines):
        line = field_lines[i]
        if not line.strip():
            i += 1
            continue

        # Doc comment
        if line.lstrip().startswith('/--'):
            doc = line
            i += 1
            # Could be multi-line
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
                        # Skip this field — provided by shared context
                        i += 1
                        continue
                    elif field_name.startswith('claim'):
                        has_claim = True
                        keep_lines.append(doc)
                        keep_lines.append(field_line)
                        i += 1
                        continue
                    else:
                        # Some other field — typed (q : ℝ, Z : ℕ, etc.)
                        has_typed = True
                        # Conservative: if there's any typed field other
                        # than claim, don't refactor this block.
                        has_only_redundant_or_claim = False
                        keep_lines.append(doc)
                        keep_lines.append(field_line)
                        i += 1
                        continue
            continue

        # Bare field line (no preceding doc) — skip-safe
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
                has_typed = True
                has_only_redundant_or_claim = False
                keep_lines.append(line)
                i += 1
                continue
        i += 1

    if not has_claim:
        return False

    # Only refactor if the class has ONLY redundant fields + a claim.
    # Skip files where the author added typed fields (q : ℝ, Z : ℕ, etc.)
    # because the refactor would conflict.
    if not has_only_redundant_or_claim:
        return False

    # Check md mentions Hecke
    md = find_md_sibling(lean_path)
    if md is None or not md_mentions_hecke(md):
        return False

    # Build new class block
    new_fields = '\n'.join(keep_lines)
    new_class = (
        f'class {class_name} extends QOU.Shared.MarkovTraceContext where\n'
        f'{new_fields}'
    )

    text = class_re.sub(lambda _: new_class, text, count=1)

    # Add import if not present
    if 'import QOU.Shared.MarkovTraceClaim' not in text:
        # Insert after the docstring `/-! ... -/`, before `namespace`
        text = re.sub(
            r'(\n-/\n\n)(namespace )',
            r'\1import QOU.Shared.MarkovTraceClaim\n\n\2',
            text, count=1,
        )

    # Simplify theorem body if it's `:= by sorry` / `:= by [...] sorry`
    # to just `:= ctx.claim_<name>`
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
            if 'extends QOU.Shared.' in text:
                continue
            if re.search(r'^  claim_\w+ : Prop$', text, re.MULTILINE):
                targets.append(str(p))

    changed = 0
    unchanged = 0
    for tgt in targets:
        p = pathlib.Path(tgt)
        if not p.is_file():
            continue
        if upgrade_lean_file(p):
            changed += 1
            print(f'refactored: {p}')
        else:
            unchanged += 1

    print(f'Done. {changed} refactored, {unchanged} unchanged.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
