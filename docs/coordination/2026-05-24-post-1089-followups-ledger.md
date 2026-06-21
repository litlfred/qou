# Coordination ledger — post-PR-#1089 follow-ups (Tier 1 + Tier 2)

**Owner branch:** `claude/post-1089-followups-2026-05-24`
**Goal:** address all 8 follow-up items surfaced at PR [#1089](https://github.com/litlfred/qou/pull/1089) merge:

| # | Tier | Title | Status |
|---|------|-------|--------|
| 1 | 1 | Wire ⁵Li / ⁶Li / ⁷Li predictions | knot-census + multi-knot VolDensity path audit |
| 2 | 1 | Categorical formalization of pp/pn/nn channel-assignment | `conj:` block authored, conditional on PR #1081 Task 3 |
| 3 | 1 | Sign-flip diagnostic interpretation | audit authored, R² = 0.83 confirmed, color-tube reading |
| 4 | 1 | Rename remaining `lambda_scale_*` script filenames | deferred to follow-up commit (invasive) |
| 5 | 2 | Atom → knot census Rule-14 escalation | audit authored, ρ_F = ν_SDP hint surfaced |
| 6 | 2 | Kashaev density rule formal justification | audit authored, exact ν_SDP match on D/T/³He |
| 7 | 2 | ⁴He "magic A·8G shell" closure analysis | audit authored, color-tube saturation hypothesis |
| 8 | 2 | Coordinate / sibling status | this ledger; PR #1063 + #1081 advisory notes pending |

**Started:** 2026-05-24 (this session)
**Parent ledger:** [`2026-05-24-low-isotope-mass-anatomy-ledger.md`](2026-05-24-low-isotope-mass-anatomy-ledger.md) (PR #1089 ledger)

## Deliverables this branch

### Audits
- [`docs/audits/2026-05-24-sign-flip-interpretation.md`](../audits/2026-05-24-sign-flip-interpretation.md) — item #3, color-tube reading of R² = 0.83
- [`docs/audits/2026-05-24-4he-magic-shell-color-tube-audit.md`](../audits/2026-05-24-4he-magic-shell-color-tube-audit.md) — item #7
- [`docs/audits/2026-05-24-a5-a7-knot-census-candidates.md`](../audits/2026-05-24-a5-a7-knot-census-candidates.md) — item #1 (research-agent authored)
- [`docs/audits/2026-05-24-rule14-atom-knot-census.md`](../audits/2026-05-24-rule14-atom-knot-census.md) — item #5 (research-agent authored)
- [`docs/audits/2026-05-24-rule14-kashaev-density.md`](../audits/2026-05-24-rule14-kashaev-density.md) — item #6 (research-agent authored)

### Content blocks
- [`content/quantum-observable-universe/braids-and-knots/inter-nucleon-channel-color-tube.{md,ts}`](../../content/quantum-observable-universe/braids-and-knots/inter-nucleon-channel-color-tube.md) — item #2, `conj:inter-nucleon-channel-color-tube`

### Code changes
- [`computations/isotope_record_schema.py:178-194`](../../computations/isotope_record_schema.py) — added NOTE pointing at the new conjecture block

## Cross-PR coordination

| Sibling PR | Relationship | Action |
|------------|--------------|--------|
| [#1081](https://github.com/litlfred/qou/pull/1081) | **SUPPLIER** for items #2, #7 (S₅↔SO(3) Task 3 supplies categorical class) | Advisory comment with channel-assignment + ⁴He saturation hypothesis cross-link |
| [#1063](https://github.com/litlfred/qou/pull/1063) | **OVERLAP** for items #3, #7 (Family A gap, single-VolDensity framing) | Advisory note pointing at sign-flip interpretation + ⁴He color-tube reading |

## Key findings

### Item #2 — channel-assignment categorical mechanism identified
The Bring color-tube weighting (9 color-pair averaging per inter-nucleon arc, per cheat-sheet Phase 5q open finding) is the conjectured categorical mechanism for the channel-assignment rule. The current `(pp → σ, nn → σ⁻¹, pn → σ_avg)` form is identified as the **flavor-only projection** of the color-tube refinement.

### Item #3 — sign-flip diagnostic delivers R² = 0.83 on n_inter
The per-isotope error is dominated by the **count** of inter-nucleon arcs (linear coefficient −2.23%/arc), not by their signed Hecke weights (R² = 0.26). This localises the closure work to the per-arc Hecke generator structure — i.e. precisely where color-tube weighting acts.

### Item #6 — ρ_F = ν_SDP (Wedderburn multiplicity) exact match
The Kashaev density rule `ρ_F ∈ {m_e, 2m_e}` matches `ν_SDP` (Wedderburn-decomposition multiplicity of canonical T_w element) exactly on the three SDP-confirmed atoms: D:1, T:2, ³He:2. Strong categorical-derivation candidate.

### Item #7 — ⁴He magic-shell as color-tube saturation
The "magic A·8G shell" closure (`A=4` for ⁴He) is hypothesised as the categorical realisation of color-tube saturation — the 12-sheet (4 nucleons × 3 colors) system fills the `SU(3)_color × S_4` 12-dim irrep, ending the per-arc additive correction regime. Quantitative cross-check pending the `1/(1 − h_q · q_0^{10}) ≈ 2.45` Faddeev resummation factor.

### Item #5 — atom→knot census admits PSD-cone fragility
Per the existing `atom-knot-mass-derivation.md`, ²H ↔ 6₂ is NOT PSD-feasible alone (α* = 0.89, only top 45%) while ³He ↔ L6a4 is PSD-top-17%. The census map is scaffolding — R5-full SDP solver supersedes it when it lands.

### Item #1 — ⁵Li / ⁶Li / ⁷Li await PR #1081 Task 3 multi-knot VolDensity
No SnapPy single-knot candidate cleanly matches the target volumes 51.5 / 62.6 / 76.8 (or the 2m_e half-values 25.8 / 31.3 / 38.4). ⁵Li is unbound (resonance → Demazure sub-crystal, per AGENTS.md §7b); ⁶Li is naturally `α + d` link; ⁷Li has J^π = 3/2⁻ spin sector. Recommendation: wait for `VolDensity(K_1 ⊔ K_2)` multi-knot evaluation from PR #1081 Task 3.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Author `conj:inter-nucleon-channel-color-tube` as a **conjecture** (not proposition) | Conditional on PR #1081 Task 3 (S₅↔SO(3)) which is itself open; per AGENTS.md §3b, the class instance carries the only sorry |
| 2 | Defer script renames (item #4) | Mechanical but invasive — affects witness slugs + audit refs across the repo; cleaner as standalone follow-up |
| 3 | Author Rule-14 escalations BEFORE owner sees them, with explicit "owner decision needed" sections | Per AGENTS.md production-vs-exploratory rule 14, the escalation IS the deliverable; owner judgement is the next step |
| 4 | Use **color-tube weighting** as the unifying categorical mechanism across items #2, #3, #7 | Per owner directive 2026-05-24 "use color tube weighting as appropriate" — the three audits all converge on the same Phase 5q open finding |

## Anti-patterns avoided

- Did NOT invent ⁵Li/⁶Li/⁷Li atom→knot assignments by census-search (would extend the existing CAL-4-equivalent risk surfaced by Rule-14 escalation #5)
- Did NOT promote `conj:inter-nucleon-channel-color-tube` to `proposition` despite the cheat-sheet's strong evidence (would violate §3b-cond — needs the class formalised first)
- Did NOT touch script names (item #4) inline with this PR — file-rename PRs are best handled standalone for clean review
- Did NOT split inconsistencies between sign-flip and PR #1063's framing silently — sign-flip audit explicitly **falsifies** the single-VolDensity framing for A ≥ 3 and recommends amendment

## Owner decisions 2026-05-24 (Rule-14 items)

| Item | Owner decision | Status |
|------|----------------|--------|
| #5 (atom→knot census) | **Wait for R5-full SDP** (option 3 of §5 menu) | ⏸️ Deferred. Current census assignments tagged EXPLORATORY in `mass_table_ppb.py`; no `prop:` block. |
| #6 (Kashaev density ρ_F = ν_SDP) | **Promote to `prop:` block** | ✅ Authored as `conj:kashaev-density-equals-sdp-multiplicity` (`.md` + `.ts`) with conditional-on-class Lean axiomatisation. Compute field `rho_factor` renamed to `nu_sdp`. |

## Open work after this branch

- **PR #1081 Task 3** lands → revisit items #2 and #7; promote channel-assignment block to `proposition` with conditional-on-class banner
- **R5-full SDP solver** lands → revisit item #5 (atom→knot census derivation supersedes the EXPLORATORY assignments); also confirm `ν_SDP(⁴He) = 2` extrapolation per `conj:kashaev-density-equals-sdp-multiplicity` open R&D
- **Color-tube weighting implementation** in `closed_form_tau_M.py` `pn_convention="bring_color_weighted"` — currently raises `NotImplementedError`
- **Sign-flip diagnostic** re-run with ⁴He included + color-tube prediction column — quantitative test of the saturation hypothesis
- **Script rename PR** for `lambda_scale_*.py` files — separate branch when owner is ready

## Cross-references

- Parent PR ledger: [`2026-05-24-low-isotope-mass-anatomy-ledger.md`](2026-05-24-low-isotope-mass-anatomy-ledger.md)
- λ_scale-absorbed canonical reference: [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- 13-driver categorical menu: [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../audits/2026-05-23-lambda-scale-canonical-unification.md)
- Bring color-tube cheat-sheet entry: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- Sibling: PR [#1081](https://github.com/litlfred/qou/pull/1081) (s4-s3 bijection + Tasks 2/3)
- Sibling: PR [#1063](https://github.com/litlfred/qou/pull/1063) (Family A gap audit)
