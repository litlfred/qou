# Coordination ledger — low-isotope mass-error anatomy + λ_scale purge

**Owner branch:** `claude/great-galileo-ahGfj` → PR [#1089](https://github.com/litlfred/qou/pull/1089)
**Goal:** complete the PR [#1080](https://github.com/litlfred/qou/pull/1080) follow-through (purge `λ_scale` from production code, not just docs) AND surface the low-isotope mass-error structure the owner asked about (per-isotope sign-flips, KLR-positivity check, channel-assignment hidden-fitting candidates, Lean-coverage matrix).
**Started:** 2026-05-24 (this session)

## Scope map

| PR | Branch | Status | Classification | Relationship |
|---|---|---|---|---|
| **#1089** (this) | `claude/great-galileo-ahGfj` | Open, 5 commits, all review comments addressed | own | code-level migration + sign-flip diagnostic + audit doc |
| #1063 | `claude/family-a-gap-audit-2026-05-24` | Open, OWNER | **OVERLAP** — same +2.89% residual diagnosis | Sign-flip evidence falsifies its single-Geom_full framing for A ≥ 3; coordination posted 07:56Z |
| #1081 | `claude/categorical-bijection-h4-bor3-2026-05-24` | Open, OWNER | **SUPPLIER** — Tasks 2+3 supply categorical inputs to PR #1089 deferred items | Intent posted; Task 3 (S₅ ↔ SO(3) fiber) is candidate source for channel-assignment rule |
| #1080 | merged 2026-05-24 03daeb1b4 | merged | source of canonical reference doc | PR #1089 implements its code-level follow-through |
| #1076 | one-voice criterion 11 | Open | independent | no overlap |
| #1062 | library workplan (Copilot) | Draft | independent | no overlap |

## Coordination comments posted

- PR #1063 — sign-flip evidence + recommended PR amendment splitting "uniform p/n baseline" from "A ≥ 3 channel variance" diagnosis. Posted 07:56Z. [Link](https://github.com/litlfred/qou/pull/1063#issuecomment-4527775365)
- PR #1081 — supplier relationship; flagged Task 3 as candidate categorical source for pp/pn/nn channel-assignment rule (PR #1089's open hidden-fitting candidate). Posted this turn. [Link to come once webhook delivers]

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Remove the `lambda_scale_family_a` alias entirely (not just deprecate) | Copilot review on PR #1089 + owner directive "no lambda-scale ANYWHERE". Migrated 9 production-script call sites to `linking_weight_family_a` / `geom_full_borromean` before removal. |
| 2 | Move `lambda_yekutieli_extended_borromean.py` to `_deprecated/yekutieli-purged/` | Its imports (`lambda_scale_yekutieli_extended`) never existed after the Yekutieli purge (PR #985 + commit `71d674da1`); script was broken. README documents reanimation policy. |
| 3 | Keep historical script names `lambda_scale_all_c_i_family_a.py` / `lambda_scale_*_probe.py` | Renaming Python files has knock-on effects on witness slugs + audit references. Probe scripts are flagged EXPLORATORY in their headers. Defer to a follow-up branch if owner wants script names purged too. |
| 4 | ⁵Li / ⁶Li wiring deferred | `mass_table_ppb.py` covers `D / T / ³He / ⁴He` via census atom→knot then jumps to A ≥ 8 α-cluster, leaving A ∈ {5, 6, 7} un-wired. Needs knot census on `B/m_e ≈ Vol` for that range, or α-cluster rule extension below A=8. Both are research-tier. |
| 5 | Categorical formalization of pp/pn/nn channel-assignment deferred | The rule "pp → σ, nn → σ⁻¹, pn → σ_avg" is asserted in `isotope_record_schema.py:176-178` without a `prop:` block. Likely connects to PR #1081 Task 3 (S₅ ↔ SO(3) fiber on Bring) once that lands. Rule-14 escalation candidate. |

## Open hidden-fitting candidates (from PR #1089 audit)

Ranked by load-bearing-ness; per CLAUDE.md Rule 14, any h^k coefficient or weight not derivable from one of the 13 categorical drivers requires owner escalation before production adoption.

| Rank | Candidate | Location | Status |
|------|-----------|----------|--------|
| 🔴 | atom → knot census assignments (D↔6₂, T↔8₁₁, ³He↔L6a4) | [`mass_table_ppb.py:18-21`](../../folio-assistant/computations/mass_table_ppb.py) | explicit AME-driven by author admission |
| 🔴 | Kashaev density rule `ρ_F ∈ {m_e, 2m_e}` | [`mass_table_ppb.py:23`](../../folio-assistant/computations/mass_table_ppb.py) | pending formal justification per script header |
| 🟠 | pp/pn/nn channel-assignment convention | [`isotope_record_schema.py:176-178`](../../folio-assistant/computations/isotope_record_schema.py) | no `prop:` block; PR #1081 Task 3 may resolve |
| 🟠 | ⁴He "magic A·8G shell" closure | [`isotope_record_schema.py:186`](../../folio-assistant/computations/isotope_record_schema.py) | labelled "magic"; biggest sign-flip magnitude (+5.87%) |
| 🟡 | flavor-split (1+ℏ_q³) 3-loop factor | PR #690 / `_li_2_q_util.flavor_split_subleading` | partial Lean coverage |

## Lean-coverage matrix (production-chain ingredients)

| Ingredient | Lean? | Risk |
|---|---|---|
| linking_weight identity `(3q²+4+3q⁻²)/4` | ✅ `lambda-scale-substrate-form.lean` | LOW |
| Hecke quadratic σ⁻¹ = σ − h | ✅ Mathlib | LOW |
| Vol(𝓑₃) = 8·G (Adams 1985) | ❌ literature only | MEDIUM |
| `Geom_full(K)` per-knot decomposition | ❌ narrative only (`prop:geom-universality`) | MEDIUM |
| Δm/M_N flavor split `(1+ℏ_q³)` factor | ⚠️ partial | MEDIUM |
| pp/pn/nn channel-assignment rule | ❌ no `prop:` block | MEDIUM |
| Atom → knot census (D ↔ 6₂, etc.) | ❌ AME-driven | HIGH |
| Kashaev density `ρ_F = m_e` | ❌ pending justification | HIGH |
| q₀ substrate value (CAL-2) | ❌ numerical anchor | LOW (acknowledged) |

## Watch state

- `main` polled via Monitor task `b2hrjp822` (5-min poll). New commit `daefd43f` (integration-watcher §2c) noted — skill doc only, no overlap.
- PR #1089 webhook subscription active; all 7 inline review comments (5 Gemini + 2 Copilot) addressed and marked outdated.

## Next concrete tasks (priority order)

1. **Surface ⁵Li/⁶Li gap explicitly** in `mass_table_ppb.py` (add the atoms with `B_pred = None` + explicit "no rule" status row) so the witness output makes the gap visible rather than just omitting the rows. Write follow-up audit doc identifying knot-census or α-cluster extension paths.
2. **Wait for PR #1081 Task 3 (S₅ ↔ SO(3) fiber)** before authoring the `prop:` block for pp/pn/nn channel-assignment. Cross-coordinate authoring once Task 3 lands.
3. **Periodic sibling triage** every 3-5 commits per `/coordinate` §7.

## Anti-patterns avoided

- ❌ Did NOT silently merge main (only fast-forward fetches; no rebase needed since PR #1089 is purely additive to current main).
- ❌ Did NOT silently rewrite framing when sign-flip evidence contradicted PR #1063's diagnosis — posted a coordination comment instead.
- ❌ Did NOT split-the-difference on the alias-removal Copilot finding (Copilot wanted full removal, my initial draft kept a back-compat alias; full removal won).
- ❌ Did NOT cherry-pick from sibling PRs without source attribution.
