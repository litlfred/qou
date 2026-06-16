# Coordination ledger — low-isotope mass-error anatomy + λ_scale purge

**Owner branch:** `claude/great-galileo-ahGfj` → PR [#1089](https://github.com/litlfred/qou/pull/1089)
**Goal:** complete the PR [#1080](https://github.com/litlfred/qou/pull/1080) follow-through (purge `λ_scale` from production code, not just docs) AND surface the low-isotope mass-error structure the owner asked about (per-isotope sign-flips, KLR-positivity check, channel-assignment hidden-fitting candidates, Lean-coverage matrix).
**Started:** 2026-05-24 (this session)

## Scope map

| PR | Branch | Status | Classification | Relationship |
|---|---|---|---|---|
| **#1089** (this) | `claude/great-galileo-ahGfj` | Open, 5 commits, all review comments addressed | own | code-level migration + sign-flip diagnostic + audit doc |
| #1063 | `claude/family-a-gap-audit-2026-05-24` | Open, OWNER | **OVERLAP** — same +2.89% residual diagnosis | Sign-flip evidence falsifies its single-VolDensity framing for A ≥ 3; coordination posted 07:56Z |
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
| 1 | Remove the `lambda_scale_family_a` alias entirely (not just deprecate) | Copilot review on PR #1089 + owner directive "no lambda-scale ANYWHERE". Migrated 9 production-script call sites to `linking_weight_family_a` / `vol_density_borromean` before removal. |
| 2 | Move `lambda_yekutieli_extended_borromean.py` to `_deprecated/yekutieli-purged/` | Its imports (`lambda_scale_yekutieli_extended`) never existed after the Yekutieli purge (PR #985 + commit `71d674da1`); script was broken. README documents reanimation policy. |
| 3 | Keep historical script names `lambda_scale_all_c_i_family_a.py` / `lambda_scale_*_probe.py` | Renaming Python files has knock-on effects on witness slugs + audit references. Probe scripts are flagged EXPLORATORY in their headers. Defer to a follow-up branch if owner wants script names purged too. |
| 4 | ⁵Li / ⁶Li wiring deferred | `mass_table_ppb.py` covers `D / T / ³He / ⁴He` via census atom→knot then jumps to A ≥ 8 α-cluster, leaving A ∈ {5, 6, 7} un-wired. Needs knot census on `B/m_e ≈ Vol` for that range, or α-cluster rule extension below A=8. Both are research-tier. |
| 5 | Categorical formalization of pp/pn/nn channel-assignment deferred | The rule "pp → σ, nn → σ⁻¹, pn → σ_avg" is asserted in `isotope_record_schema.py:176-178` without a `prop:` block. Likely connects to PR #1081 Task 3 (S₅ ↔ SO(3) fiber on Bring) once that lands. Rule-14 escalation candidate. |

## Open hidden-fitting candidates (from PR #1089 audit)

Ranked by load-bearing-ness; per CLAUDE.md Rule 14, any h^k coefficient or weight not derivable from one of the 13 categorical drivers requires owner escalation before production adoption.

| Rank | Candidate | Location | Status |
|------|-----------|----------|--------|
| 🔴 | atom → knot census assignments (D↔6₂, T↔8₁₁, ³He↔L6a4) | [`mass_table_ppb.py:18-21`](../../computations/mass_table_ppb.py) | explicit AME-driven by author admission |
| 🔴 | Kashaev density rule `ρ_F ∈ {m_e, 2m_e}` | [`mass_table_ppb.py:23`](../../computations/mass_table_ppb.py) | pending formal justification per script header |
| 🟠 | pp/pn/nn channel-assignment convention | [`isotope_record_schema.py:176-178`](../../computations/isotope_record_schema.py) | no `prop:` block; PR #1081 Task 3 may resolve |
| 🟠 | ⁴He "magic A·8G shell" closure | [`isotope_record_schema.py:186`](../../computations/isotope_record_schema.py) | labelled "magic"; biggest sign-flip magnitude (+5.87%) |
| 🟡 | flavor-split (1+ℏ_q³) 3-loop factor | PR #690 / `_li_2_q_util.flavor_split_subleading` | partial Lean coverage |

## Lean-coverage matrix (production-chain ingredients)

| Ingredient | Lean? | Risk |
|---|---|---|
| linking_weight identity `(3q²+4+3q⁻²)/4` | ✅ `lambda-scale-substrate-form.lean` | LOW |
| Hecke quadratic σ⁻¹ = σ − h | ✅ Mathlib | LOW |
| Vol(𝓑₃) = 8·G (Adams 1985) | ❌ literature only | MEDIUM |
| `VolDensity(K)` per-knot decomposition | ❌ narrative only (`prop:geom-universality`) | MEDIUM |
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

---

## 2026-06-02 — census-excision + q₀-refresh coordination (PRs #1706, #1700)

**Session goal:** owner directives — (1) refresh stale q₀ in producer witnesses,
(2) "excise all non-canonical" binding from production, (3) trace the deuteron
`2.2488 MeV` derivation. Tied to the open Δ_λ gate.

### Findings
- Deuteron `2.2488 = m_e·Vol(6₂)` is a **census knot-lookup** (ρ=m_e hand-assigned,
  no Δ_λ). Canonical Path-D formula `B=m_e·Σ_λ y_λ χ^λ Δ_λ` undershoots D by −83%
  bare; the `C_knot=5.852` "fix" is retracted as a fit.
- **All composite binding is non-canonical**: census, partial-shell (interp),
  L1 empirical-(knot,ρ_K), AND α-cluster (B(⁴He) is hardcoded AME, c_αα is ¹²C-fit,
  NOT Lean-proved). ⁴He's "0.41 ppb" is the AME input echoed back.
- "census → SDP" (`gap_a1_binding_k_sdp_feasibility.py`) is **circular**:
  SDP canonically selects operator K=σ₃² but `GAP-A-1 ⊆ Δ_λ`.

### Actions (PRs)
- **#1706** — canonicity-first gate in `canonical_isotope_witness.py`: only
  α-cluster (canonical-recursive, per owner decision) ships; census/partial-shell/
  L1-empirical → `derivation-pending` + `excised` audit field. 119 shards regen,
  0 non-canonical predictions leak. Fixed ⁴He shadow-by-L1 mis-tag.
- **#1700** — `habiro-coefficients-atomic` refreshed to canonical q₀ (p/n/D).
  Completes the realizer fix #1696 (merged): both producer cache + realizer canonical.

### New Δ_λ lead (flagged to Option E #1697)
- **Δ_λ = per-block q-hyperbolic volume via quantum-6j volume conjecture**
  (Costantino–Murakami), Wedderburn-decomposed. Never among the 6 failed ansätze
  (corpus-confirmed). Zero-param test: `B_D = m_e·Σ_{λ⊢6} y_λ χ^λ(β_D)·Vol_λ`.
  Breaks 1-eqn/11-unknowns underdetermination IFF Vol_λ is categorical. Scalar
  precedent `binding_link_volumes.py`: D +0.2%, A≥3 −60% (needs per-pair JSJ split).

### Coordination posted
- **#1535** (q₀-regen): I did the deferred canonical_isotope (98) + habiro;
  drop from their batch; #1706 changes binding values (rebase, don't re-regen).
- **#1697** (Option E Δ_λ H₆): excision makes table Δ_λ-gated; flagged volume-6j lead.
- **#1507** (fit-pattern banners): complementary discipline; binding_ladder_catalog shared.

### CI triage (both pre-existing, NOT mine — witnesses-only PRs)
- #1706 validate red = `derivation_chain_validator` (c-q-q0 chain + 967 trust count);
  my PR touches 0 `*.derivation.json`.
- #1700 PDF-compile red = `verlinde1988` undefined cite — being fixed by **#1702**.

### Next concrete task (non-overlapping)
- Build the **zero-parameter volume-6j Δ_λ probe** (EXPLORATORY): compute
  `Σ_λ y_λ χ^λ(β_D)·Vol_λ` for q-6j / JSJ-per-pair `Vol_λ` candidates vs D/T/³He/⁴He,
  no free params. Coordinate with Option E #1697/#1516 before authoring any prop block.
- (Deferred) census/partial-shell → `deprecated/` move — coordinate with #1681 refactor.

## 2026-06-16 — B_sym closed form + saturation (#2343) ↔ α-cluster frontier (#2349)

- **#2343** (`claude/ecstatic-archimedes-7dkuiq`): low-isotope (²H–⁷Li) B_sym error
  budget + decomposition. Tool `computations/m_sym_error_budget.py`
  (`--decompose`/`--bonds`/`--rescore`). Audit
  `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md`.
  - **Closed form:** `B_sym = α·[(Z−1)L_pp + L_pn + (N−1)L_nn]`, exactly additive to
    the 50-dps floor ⇒ the Markov trace carries **zero** cooperative binding; the
    4-body α-unit is *entirely absent* (not under-weighted). Per-bond n-n>p-n>p-p.
  - **Saturation:** chain `(A−1)` vs all-pairs `C(A,2)` — neither works (all-pairs
    RMS 10.1→22.5 ↑, over-binds heavies); binding saturates ~linearly in A.
    Residual `Δ = B_AME − B_sym` is 10⁵–10⁷σ real and **sign-changing** (D over,
    ⁴He under) ⇒ shell structure, not a uniform/bond-count law.
  - **Convergence with prior art (corpus-grep):** `derive_binding_chain_cooperative.py`
    (signed-trace) is the sibling functor of this log-form chain — same structure,
    same ⁴He residual; `observations/magic-numbers-from-q` already gives the shell
    *positions* {2,8,20,28}. Only open lever = α-unit **magnitude** → α-cluster
    recursion (⁴He as magic input, per #1706), **not** a 7th fit (Δ_λ gate).
- **#2349** (`claude/lucid-curie-wmr42x`): same B_sym shell-structure problem, high
  end — extends the residual probe to ¹²C (3α), establishes the ¹⁶O feasibility wall
  (`tr_m_atom_zn` enumerates p(3A); ¹⁶O p(48)=147k infeasible; real unlock =
  per-block `canonical_tr_m_via_branching` past A=2). AME witness + B_c12/B_o16.
- **Relationship:** complementary, no file overlap. Intent posted on #2349
  (cross-link audits → one low-closed-form→high-α-cluster story; AME C/O entries
  auto-extend #2343's tool). No cherry-pick either way.
