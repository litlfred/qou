# Lean "placeholder/TODO" beans are grep-inflated — audit (2026-06-26)

**Bean:** `ylgh` (bean-backlog hygiene) · keystone-drain session follow-on
**Method cache:** `lake-cache/qou-v4-24-0` (lean-direct, warm oleans)

## Finding

The cluster of auto-generated **"Resolve N placeholders/TODOs in
qou/lean/`<dir>`"** beans (`1osq`, `ekb8`, `b3pe`, `95jh`, `i6p9`, `ixx4`,
and the sibling `xj99`/`ldup`/`zslh`/`mlt7`/`doth`) **overstates the actionable
remediation work by 3–10×**, and at least one (`1osq`) is **fully stale**. The
counts track a naive `grep -c 'sorry|TODO|placeholder'`, which matches four
classes of **non-actionable** strings:

1. **`sorry-free` docstrings** — every *"What's PROVED (sorry-free)"* /
   *"proved … sorry-free"* comment matches the substring `sorry`. **Dominant
   inflation source** (e.g. Substrate's 3 naive hits are all `sorry-free`).
2. **`-- TODO upstream:` markers** on **proved, sorry-free** lemmas
   (`MathlibExt.lean` — Mathlib-upstreaming candidates, not in-repo work).
3. **Comment-prose** describing the §3b pattern, e.g. the literal text
   *"the Lean encoding below is a `theorem … : ctx.holds := by sorry`
   placeholder"* — a description, not a `sorry`.
4. **Legitimate §3b open-conjecture `sorry`** markers — per
   [`AGENTS.md §3b`](../../AGENTS.md) these **represent the open conjecture**;
   they are **not** "to-resolve placeholders".

## Verified counts (refined grep + hand-read, 2026-06-26)

| dir | bean | bean-claimed | naive grep | refined "actionable" | hand-read truth |
|-----|------|--------------|-----------|----------------------|-----------------|
| `Substrate` | `1osq` | 5 | 3 | **0** | **0 — FULLY STALE** (all 3 are `sorry-free`) |
| `Interactions` | `ekb8` | 17 | 18 | 5 | **1 genuine** (`QIntegerMassFormula.fits_AME`); other 4 are §3b/comment |
| `Archimedean` | `b3pe` | 87 | 49 | ~11 | refined; subset are §3b instances |
| `BraidKnot` | `95jh` | 213 | 316 | ~23 | refined; many are §3b instances |
| `QOU` (whole) | — | — | 757 | ~157 | loose upper bound on all lean `sorry` tokens |

**Refined grep** = `(:= sorry | := by sorry | ^\s*sorry$ | <;> sorry)` minus
`sorry-free | sorries | 'sorry' | "sorry"`. The Interactions deep-dive shows
even *that* over-counts (4 of 5 refined hits were comment-prose / §3b), so the
true actionable backlog is **≤ the refined column** and should further exclude
§3b open-conjecture `sorry`s.

## Recommendation (owner closes beans per AGENTS.md §4a)

- **Close `1osq`** — Substrate has **0** actionable sorries (confirmed
  `lean`-direct: `MuOverDetermination`/`ColorAntisymmetric` are `sorry-free`).
- **Re-scope** `ekb8` / `b3pe` / `95jh` / `i6p9` / `ixx4` to their verified real
  counts, and **exclude §3b open-conjecture `sorry`s** from the remediation
  scope (those are intentional, per §3b — discharging them would be *wrong*).
- The single genuine actionable Interactions sorry is
  `QOU/Interactions/QIntegerMassFormula.lean:180` (`fits_AME := sorry`, an
  AME-fit claim) — a real follow-up target.
- **Future placeholder-bean generation** should use a `sorry`-aware counter
  (exclude `sorry-free`, comment lines, and §3b `ctx.holds` instances) — or
  better, the authoritative `lean`-direct *"declaration uses 'sorry'"* warning
  count.

## Why this matters

This is the **third** "stale/misclassified Lean bean" found this session
(after the H3 `H3HeckeIdempotents` §7c stale flag, #2821, and the entire `bwkg`
"3 deep-broken files" premise, #2827 — all three files actually compile clean).
The pattern is consistent: **auto-generated beans assert un-verified Lean
status**. Verifying with the warm `lake-cache` olean set before acting prevents
agents from spending effort "fixing" already-healthy code or "resolving"
non-actionable string matches.
