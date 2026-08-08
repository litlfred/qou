# Updated workplan — post-#4086, week of 2026-08-08

Snapshot after PR #4086 (OV brick-3b bricks + ρ-naturality) merged to `main`.
This branch (`claude/askey-derivation-gap-canonical-xaf8h7`) was restarted fresh
off `main` (it was 1803 commits behind; the merged PR is finished per the
merged-PR rule) and now carries the follow-up lanes below.

## What landed on `main` this week (1694 commits)

| Theme | ~count | Substance |
|---|---|---|
| `lean` | 251 | Specht/Hecke/keystone proof work; wall-side §7c base-ring ports |
| `beans` | 214 | work-plan churn (now **163 in-progress**, ~15.4k todo) |
| `fix`/`chore` | ~300 | QA soundness audit added to the pre-commit preflight; witness/sidecar upkeep |
| `probe` | 120 | derivation attacks — Δ_λ, μ₀, Kashaev, α_EM |
| `audit` | 93 | per-block verdicts; wall-side §7c reviews |
| `wall-side`/`§7c` | 20 | generic-`R` base-ring cleanup (bean `20vb`) |

## Active research/formalization frontier (in-progress EPICs)

- **`sp00` Specht/S_n Lean** — Phase D `sp08` = OV seminormal. My lane.
  `seminormalVector_base_exists` is **still a `sorry`** on main; the brick-3b
  bricks from #4086 are landed and the annihilation lemma is preserved in
  [`docs/audits/2026-07-19-ov-base-vector-column-superstandard-verification.md`](../audits/2026-07-19-ov-base-vector-column-superstandard-verification.md),
  ready to land once the `Core → … → JucysMurphy` olean cone builds cleanly.
- **`qou-x631` Δ_λ covariance** — full attack plan (Stein+Kerov / Jack / DPP
  kernel / β=2 maximises). Headline research front.
- **`bws0` keystone full formal closure**; **`qou-hnhg` Hecke-semisimplicity
  Mathlib gap**; **`qou-6ufi` α_EM B2 τ-identification**; **`qou-ch8w` μ₀ −9%
  closure**; **`qou-b1je` P≠NP-in-QOU**; **`qou-atsd` atomicity from self-duality**.
- Drains: **`qou-gqt5`** 452 float64-padded witnesses; **`cscb`** content-sibling repair.

## This branch's lanes (owner-selected 2026-08-08: all four)

1. **`sp08` OV brick-3b annihilation** (foreground, Lean) — resume + verify on
   current main; land `colGarnir_fullgroup_annihilation_of_collision` +
   `colGarnir_single_column_of_collision`, then the column-superstandard
   collision geometry toward closing `seminormalVector_base_exists`.
2. **`qou-x631` Δ_λ covariance** (background agent, Python probe) — one tractable
   leg (e.g. A2 `Cov_Planch` remainder).
3. **A drain** (background agent) — `qou-gqt5` float64-padded witnesses or
   `cscb` content-siblings, bounded slice.
4. **This workplan doc** — the durable record of the above.

## folio-assistant

Updated to latest (`/home/user/folio-assistant`, linked into repo). New features
present; run `cd content && bun run validate` to confirm pipeline integration
before content edits.
