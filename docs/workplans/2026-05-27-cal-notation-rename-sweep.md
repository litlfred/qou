# Workplan: CAL notation rename sweep

**Date:** 2026-05-27
**Driver:** PR #1354 (merged) — finalized CAL-1=m_e, CAL-2=𝔇_β, CAL-3=𝔇_π

## Scope

889 references to old CAL notation across the codebase:
- Content .md files: 113
- Content .ts files: 13
- Compute .py files: 373
- AGENTS.md: 4 (already updated in #1354)
- Docs: 386

## Old → New mapping

| Old | New | Notes |
|-----|-----|-------|
| CAL-2 = m_μ/m_e | CAL-2 = 𝔇_β | β-decay width → Q_β → q₀ |
| CAL-3 = Q_β | CAL-3 = 𝔇_π | pion decay width → m_π |
| "mass ratio" language | "decay width" language | consistent with fraktur notation |

CAL-1 = m_e is unchanged.

## Already done (PR #1354)

- codata_constants.py CAL table header
- AGENTS.md precision-goals preamble
- meson-scale-independence.md calibration table
- unified_meson_mass_formula.py m_π import

## Remaining (this sweep)

1. Content .md: update 113 CAL references
2. Content .ts: update 13 CAL references (tags, comments)
3. Compute .py: update 373 references (comments, docstrings)
4. Docs: update 386 references (audit docs, workplans, coordination)

## Method

Mechanical sed/grep replacement with manual review of edge cases.
The content is "CAL-2 = m_μ/m_e" → "CAL-2 = 𝔇_β" and
"CAL-3 = Q_β" → "CAL-3 = 𝔇_π". Context-dependent cases
(where the old meaning is mathematically correct in situ)
need individual judgment.
