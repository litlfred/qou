---
# qou-1u56
title: 'main is RED on the raw-float64 ratchet: 4 witnesses regenerated without a baseline update'
status: completed
type: task
priority: normal
created_at: 2026-09-06T13:28:11Z
updated_at: 2026-09-08T07:45:48Z
---

## Measured on `main`, not on a branch

The raw-float64 ratchet reports **4 REGRESSED** and a net **−38 fields** on a
tree freshly rebased onto `origin/main`. All four are `main`'s:

| baseline | live | witness |
|---|---|---|
| 25 | 55 | `probes/he4-channel-split-categorical-constraint-probe.witness.json` |
| 23 | 34 | `probes/he4-partition-dominance-audit-probe.witness.json` |
| 7 | 18 | `probes/option-a-vol-per-knot-light-series.witness.json` |
| 24 | 26 | `probes/he4-9-3-trace-dominant-correction-probe.witness.json` |

**Attribution is byte-exact, not inferred.** All four files are
`sha256`-identical to `origin/main`, and `origin/main`'s **own**
`raw-float64-baseline.json` still carries the OLD counts (25 / 23 / 7 / 24).
So the witnesses were regenerated and the baseline was not updated in the same
change — the ratchet is red on `main` independently of any branch.

Traced to two commits, both of which regenerate witnesses in bulk:

- `9b009da0e6e` — *"rebase(6854): integrate 485 commits of main, and RE-DERIVE
  the six conflicting witnesses rather than picking a side"*
- `3cc4b2aab10` — *"sweep(qou-92u9): 64 downstream producers run — 50 witnesses
  refreshed, and the new word BREAKS A ROUTE rather than just moving its
  numbers"*

Both did the right thing by the witnesses. Neither re-ran the ratchet.

## Why I did not just fix it

The ratchet is **drain-only**: `--rebaseline` floors every entry at its previous
value and prints `NOT BANKED` for anything that would grow, precisely so an
agent cannot make a red run green by widening the baseline. These four *would*
grow. Banking them is the move AGENTS.md forbids in as many words —
*"NEVER make a red run green by widening a baseline… baselines drain, never
grow."*

So there are exactly two honest resolutions and both need someone who has read
these producers:

1. **The growth is real and wanted** — the regenerated witnesses legitimately
   carry more float64, in which case the four entries need a deliberate,
   reviewed baseline raise with the reason recorded. That is a decision, not a
   sweep.
2. **The growth is a defect** — the regeneration introduced float64 where the
   producer previously serialized through `fmt`, in which case the fix is at
   the producer and the baseline never moves.

`he4-channel-split` more than doubled (25 → 55) and `option-a-vol-per-knot`
more than doubled (7 → 18), which leans toward (2), but I have not read those
producers and am not guessing.

## Note for whoever picks this up

The ratchet currently runs **ADVISORY** here (`exit 0` despite the findings), so
this does not block a merge and will not announce itself. That is why it needed
a bean rather than a comment: nothing else will surface it.


## RESOLVED 2026-09-07 — the answer was neither of my two options

I framed this as "either the growth is wanted (needs a reviewed baseline raise)
or it is a producer defect (fix at the source)", and said it needed someone who
had read the producers. Having now read them: **it is a third thing, and it
makes the resolution ordinary.**

The growth is a **downstream symptom of a deliberate, owner-ruled upstream
change**, and the four witnesses were already serializing through `float()`.
More data flowed through an existing float64 boundary, so the count rose. That
needs **neither** a baseline raise **nor** an upstream fix — just the same drain
every other bucket-B producer gets.

**All four now report 0.** `REGRESSED: 0`, and the baseline came down
1008 / 31,069 → 1004 / 30,990 without banking a single grown entry.

## What actually changed upstream

`option-a-vol-per-knot-light-series` was the decisive one, because its entire
growth (7 → 18) sits on one path: `.data.rows[].canonical_braid_word_first_6`.
Comparing the snippet across the regeneration:

    OLD  [[1,0,0], [1,0,0], [1,0,0], [1,0,0], [1,-0.10453014939781965,0], [1,0,0], '…']
    NEW  [[1,0,0], [1,-0.2090602987956393,1], [1,0,0], [1,-0.2090602987956393,1], ...]

The weight is **exactly 2×** the old, its multiplicity went **1-in-6 → 3-in-6**,
and the third component flipped 0 → 1. That is `atom_braid_word_3A`'s
**intra-ordering change of 2026-09-05** (bean `qou-hu1f`, owner ruling): each
nucleon's confinement core went from *grouped* (three σ₀ then three σ₁⁻¹) to
*alternating*, because σ₀ and σ₁ do not commute and only the alternating word is
β_Bor. The function's own docstring documents it, including that absolute traces
moved by 14.325× at ⁴He — which is also why the three `he4_*` probes, all of
which read ⁴He tr_M contributions, moved at the same time.

**The alternating core carries a non-zero weight on three letters in six instead
of one, so there is simply more of the same weight to write.** Wanted change,
existing float64 boundary, higher count.

## Two things I got wrong on the way, both caught before they were written down

- **"A live probe imports its canonical braid word from `_deprecated/`."** False.
  `grep -rl 'def atom_braid_word_3A'` returns the deprecated copy first, but the
  probe imports `from mass_at_3A_proper import ...`, which is live. Check which
  definition the importer names, not which one grep prints first.
- **"That field is not a braid word — it holds 3-vectors identical across every
  knot."** Both halves are true and neither is a finding. The triples are
  `(c, d, gen_idx)` and `atom_braid_word_3A`'s docstring already carries a
  **MISNOMER** note saying the block is not a braid; and the word depends on
  `(Z, N)` alone, so identical rows are correct — the rows vary the *knot volume
  assignment*, not the atom.

## Note on `option-a`

Its single assertion `proton_per_block_under_uniform_within_1pct` was failing
before this change and still is (`allPassed: false` → `false`). That is the
probe's own documented point — per-block undershoots m_p by ≈ 2.38×, stated in
its docstring as the owner-gated finding — not a regression.

## 2026-09-08: canonical tracker for the recurring "raw-float64 ratchet is RED on main" event is qou-sknx (most recent OPEN one, 2026-09-04); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 6 / §7.3 C7. Seven beans (08-11 … 09-06) record one recurring event; this one is kept as-is because its body carries its own finding.
