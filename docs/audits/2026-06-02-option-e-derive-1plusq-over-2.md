# Option-E PROBE 1 — is the v9 `(1+q)/2` closure factor DERIVED or a NEAR-MATCH (fit)?

**Trigger:** author directive "work on Δ_λ binding-energy Gram closure" → ledger
[`docs/coordination/option-e.md`](../coordination/option-e.md) **PROBE 1** ("Derive `(1+q)/2`
structurally"), the explicitly-designated next-session keystone.

**Branch / PR:** `claude/option-e-derive-1plusq-over-2-2026-06-02` / #1707
**Probe:** [`computations/option_e_probe1_derive_1plusq_over_2.py`](../../computations/option_e_probe1_derive_1plusq_over_2.py)
**Witness:** `computations/option-e-probe1-derive-1plusq-over-2.witness.json` (audit-only)

## VERDICT: **NEAR-MATCH (fit)** — with a STRUCTURAL-BUT-STALE staleness correction

`(1+q)/2` is **not** structurally forced by the Hecke/Hoefsmit/Markov machinery. It is
an empirical correction selected to close the A=3 mirror-pair residual. The A=3 mirror
closure remains **OPEN**. `(1+q)/2` stays **un-wired**. This corroborates and refines the
prior PARTIAL record (#1579, #1581) with three new findings (staleness, direct
required-factor disproof, Hoefsmit/projector raw tests).

## The object under test

```
B_T − B_³He = m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2
```

Every factor EXCEPT `(1+q)/2` is derived: `m_π` (CAL-3), `ℏ_q = (q−1)/q` (substrate),
`y_λ·χ` (Markov weights × Hoefsmit characters), and the bar-symmetric transpose pair
`(χ^λ + χ^{λᵀ})/2` (structural). `(1+q)/2` was SELECTED from a substrate-candidate list.

## STEP 0 — staleness refresh (the published 0.11% is stale)

The v9 source [`option_e_v9_all_symmetries.py`](../../computations/option_e_v9_all_symmetries.py)
hardcodes `Q_0 = 1.1097090249` — the **pre-2026-05-28 muon-anchor** value (q0-repin
staleness class). Refreshed at the current canonical proton q₀ = `1.1099785827513808`
(`from q_parameter import q_at`):

| q₀ used | v9 prediction (MeV) | residual vs target 0.763738 MeV |
|---|---|---|
| stale literal `1.1097090249` (v9 source) | 0.7628735 | **−0.1132%** (the published "0.11%") |
| **canonical proton** `1.1099785827…` | 0.7646598 | **+0.1207%** |
| muon cross-check `1.1099785955…` | 0.7646599 | +0.1207% |

The refreshed residual **flipped sign** (−0.11% → +0.12%) and is marginally **worse**.
The published 0.11% near-match was an artefact of the stale muon-anchor literal. The
proton and muon pins agree to ~1e-8 (they differ by only ~11.5 ppb), so the staleness is
the stale-LITERAL gap, not a proton-vs-muon difference.

## The 4 structural hypotheses — does any FORCE `(1+q)/2` algebraically?

Each candidate computed RAW at canonical q₀ and compared to `(1+q₀)/2 = 1.0549892914`.
"FORCING" requires an algebraic identity, not a numerical near-match.

| Hyp | Construction | value @ q₀ | rel. to `(1+q)/2` | forces it? |
|---|---|---|---|---|
| H1 | `[2]_q/2` (unbalanced `[2]_q = 1+q`) | 1.0549892914 | +0.000% | **tautology** |
| H2a | `tr ρ_(2,1)(σ_1) = q−q⁻¹ = h` | 0.2090603 | −80.18% | NO |
| H2b | `h/2` | 0.1045301 | −90.09% | NO |
| H2c | `(q+1)/2` principal-spec form | 1.0549892914 | +0.000% | **tautology** |
| H3a | `1/[2]_q` (Hoefsmit axial-distance diag, balanced) | 0.4972905 | −52.86% | NO |
| H3b | `√([3][1])/[2]` (Hoefsmit off-diagonal) | 0.8675841 | −17.76% | NO |
| H4a | `q/[2]_q` (symmetric-channel projector, balanced) | 0.5519819 | −47.68% | NO |
| H4b | `q/(1+q)` (symmetric-channel projector, unbalanced) | 0.5260615 | −50.14% | NO |

**Reading.** Only H1 and H2c "match" — but `[2]_q/2` (unbalanced) and `(q+1)/2` are
*literally the same algebraic expression* as `(1+q)/2`. They are **tautologies**, not
independent derivations: writing `(1+q)/2` as `[2]_q/2` renames it; it does not produce
it from a Hecke/Hoefsmit construction. Every genuinely-independent structural object —
the standard-rep trace of σ₁ (= h), the Hoefsmit seminormal diagonal `1/[2]_q` and
off-diagonal `√([3][1])/[2]`, the symmetric-channel projector weight `q/[2]_q` — lands
**18–90% away**. No Hoefsmit normalization supplies `(1+q)/2`.

This answers the prompt's specific reverse-justification concern (hypothesis 1): the
bar-symmetric average `(χ^λ + χ^{λᵀ})/2` does **not** carry a hidden `[2]_q`
normalization that the v9 search absorbed into the prefactor — if it did, the required
closure factor would equal `[2]_q/2 = (1+q)/2` exactly. It does not (next section).

## DECISIVE FIT TEST — required closure factor vs `(1+q)/2`

A structural factor is the SAME algebraic expression at every anchor (q the only
variable). Define the **required closure factor** `R(q) = target / (m_π · ℏ_q · S)`, the
number `(1+q)/2` *must* equal to close the mirror pair to zero. With the structural sum
`S = 0.05241232…` (at canonical q₀):

| pin | required `R` | `(1+q)/2` | residual |
|---|---|---|---|
| proton (canonical) | 1.0537174683 | 1.0549892914 | **+0.1207%** |
| muon (cross-check) | 1.0537173578 | 1.0549892978 | +0.1207% |

`(1+q)/2 ≠ R` at the SAME pin: they differ by `|(1+q)/2 − R| = 0.00127` (+0.12%). This is
**not an algebraic identity** — a structural factor would satisfy `(1+q)/2 = R` exactly.

The proton-vs-muon pin-swap discriminator is inconclusive *here* only because the two
pins are ~11.5 ppb apart (drift = 1e-5 pct-points), so the residual is identical at both
pins. The decisive evidence is therefore the **same-pin** inequality `(1+q)/2 ≠ R` (0.12%),
not the pin-swap. The gap factor needed to make `(1+q)/2` exact is `R/[(1+q)/2] = 0.998794`;
no clean substrate object lands on it (`1−ℏ_q²/2 = 0.99509`, `1−h²/8 = 0.99454`,
`1/(1+ℏ_q²) = 0.99028` are all ≥ 0.4% off). The residual is an unexplained 0.12% miss,
not an absorbed structural correction.

## Relation to prior work (corpus-grep)

| prior | finding | this probe adds |
|---|---|---|
| PR #1581 (Finding C) | `(1+q)/2` unique within 0.11% across 33 q-arithmetic candidates — a **scan** | confirms scan-selection = fit-selection |
| PR #1579 / [`2026-05-31-v9-one-plus-q-categorical-derivation.md`](2026-05-31-v9-one-plus-q-categorical-derivation.md) | verdict **PARTIAL**: categorical *narrative* (chirality-odd `1 + h/2`) but the `(1+σ)/2` vs `(σ+σ⁻¹)/2` choice is ad-hoc; the production convention is the bar-symmetric `(σ+σ⁻¹)/2` | the residual is **stale** (−0.11% → +0.12%, sign-flipped at canonical q₀); `(1+q)/2 ≠ R_required` directly (0.12%); Hoefsmit diag/off-diag + symmetric projector raw tests all fail (new) |
| [`isospin-mirror-v9-empirical-near-match.md`](../../content/quantum-observable-universe/observations/isospin-mirror-v9-empirical-near-match.md) | already records it as "exploratory shape-hint, not a closure" | content record is correct; this audit supplies the canonical-q₀ numbers |

The narrative in #1579 (`(1+q)/2 = 1 + h/2` is the first-order *chirality* correction)
remains the most defensible framing — but as #1579 itself states, the choice of the
chirality-odd `(1+σ)/2` over the production bar-symmetric `(σ+σ⁻¹)/2` is **not forced**
by the canonical chain. The same-pin disproof here (`(1+q)/2 ≠ R` by 0.12%) shows that
even the chirality-odd `1+h/2` does not close the mirror pair exactly — so it is at best
a shape-hint, not a closure.

## Why this is the EXPECTED, valuable result

This matches the pre-stated prior (parallel to the c_3 flip-flop): a clean-looking
substrate factor selected from a candidate list, looking canonical but not derived. The
discipline value is recording it honestly so the next session does not re-promote it.

- **No v10 ansatz proposed.** This probe tests the EXISTING `(1+q)/2` only.
- **No fit.** Structural hypotheses computed FIRST; compared to the required factor LAST.
- `(1+q)/2` stays un-wired; the A=3 mirror closure remains OPEN.

## Ledger update

The ledger PROBE-1 entry is upgraded from "NOT YET TESTED" to "TESTED → NEAR-MATCH";
the v9 table row's residual is corrected from the stale 0.11% to the canonical +0.12%.

## What would upgrade to DERIVED (research-grade follow-up, NOT this session)

Per #1579 follow-up: a categorical proof that mirror-pair differences project onto the
chirality-odd component of the canonical averaging operator (Hopf-antipode `S(σ)=σ⁻¹`
under `Z↔N`), AND a structural correction supplying the residual 0.12% gap. Until both
exist, `(1+q)/2` is a near-match. PROBE 3 (Lean §3b-cond class) stays blocked.
