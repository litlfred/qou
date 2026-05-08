# Coordination ledger — 1 ppb mass-prediction goal

> Per [`.claude/skills/local/coordinate.md`](../../.claude/skills/local/coordinate.md)
> §6 (merged in [#568](https://github.com/litlfred/qou/pull/568)).
>
> **Goal**: reach 1 ppb relative accuracy on QOU mass predictions
> (D…⁴⁰Ca and beyond) **without** deriving Q_β. Three calibration
> anchors stay: m_e, m_p, m_n (the last via Q_β = m_n − m_p − m_e).
> Hard floor from CAL-2 uncertainty: ~780 ppb.
>
> Append rows; do **not** rewrite other agents' rows. Cherry-pick
> across PRs is authorised; cite the source PR in commit messages.

## Ledger

| Date | PR | Phase | Status | Cherry-pick / artefact |
|------|----|-------|--------|------------------------|
| 2026-05-08 | [#564](https://github.com/litlfred/qou/pull/564) | Deep audit · derivation framework, conventions, mass tables, 1 ppb plan | landed `329be15ca` | [`AUDIT-DEEP-2026-05.md`](../../AUDIT-DEEP-2026-05.md) (workplan, formalism→compute table, baseline mass-table review) |
| 2026-05-08 | [#564](https://github.com/litlfred/qou/pull/564) | F1–F10 corrections | landed `4b356df1a` | F4 reframe (T4 derived live; T6 unit-convention escalation), F5/F8/F9 mechanical fixes |
| 2026-05-08 | [#564](https://github.com/litlfred/qou/pull/564) | P1 · §3b ledger compliance (mass chain) | landed `6ae6bfb7b` | Class-axiomatised `conj:e-hartree-categorical-derivation`; **258 → 15 violators**. Pattern: [`e-hartree-categorical-derivation.lean`](../../content/quantum-observable-universe/descartes-universe/e-hartree-categorical-derivation.lean) |
| 2026-05-08 | [#564](https://github.com/litlfred/qou/pull/564) | P4′ · T6 unit-convention resolution | landed `e578392b8` | Options A + C: no additive T6, `M = ρ_K · m_e · |tr_M|`, Mittag–Leffler complementarity is the justification. Verification: [`rho-k-leading-order-verification.witness.json`](../../folio-assistant/computations/rho-k-leading-order-verification.witness.json) |
| 2026-05-08 | [#564](https://github.com/litlfred/qou/pull/564) | P1.b · §3b ledger compliance (fluid-dynamics + EW residual) | landed `6af7be786` | 9 stub Lean classes (`QAubinLions`, `NSCounterexample`, `CriticalExponent`, `WeakSpectralCompleteness`, `EWHiggsTorusLinkTriplet`, `LeviDegeneracy`, `BlowupYekutieli`, `RegularityBreakdown`, `EWMassEigenstateCount`); **15 → 0 violators paper-wide** |
| 2026-05-08 | [#564](https://github.com/litlfred/qou/pull/564) | P4″ · ρ_K assembly path | landed `86aaeb51a` | New consumer [`atomic_mass_via_rho_k.py`](../../folio-assistant/computations/atomic_mass_via_rho_k.py); **200× improvement** vs legacy E₀ on D, T, ³He (mean 0.23 % MAE vs 36 %). Witness: [`atomic-mass-via-rho-k.witness.json`](../../folio-assistant/computations/atomic-mass-via-rho-k.witness.json) |
| 2026-05-08 | [#568](https://github.com/litlfred/qou/pull/568) | `/coordinate` skill | **merged to main** `b40222709` | Multi-agent / multi-PR coordination protocol; this ledger is the §6 deliverable. Copilot expanded with §5 review-comment handling (`18719a3`) |
| _add row_ | [#565](https://github.com/litlfred/qou/pull/565) | Compute infrastructure audit (F1–F15 + Tier 1–4 plan) | open | F8 pickle migration, F9 `sp.cancel` sweep, F11 `lp_dual_witness_validator` CI promotion |
| 2026-05-08 | [#567](https://github.com/litlfred/qou/pull/567) | Crystal R-matrix → operator-valued Sub-lemma 2.1 closure | landed `f179c3fe` + `4c6bdf61` | [`docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`](../audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md) — ~25-line proof replacing 95-line seminormal case analysis. Conditional on `conj:crystal-graph-realization`. |
| 2026-05-08 | [#567](https://github.com/litlfred/qou/pull/567) | Crystal pole-order witness (combinatorial) | landed `a814a278` + `787b272d` | [`crystal_pole_order.py`](../../folio-assistant/computations/crystal_pole_order.py) + [`crystal-pole-order.witness.json`](../../folio-assistant/computations/crystal-pole-order.witness.json) — 21/21 assertions (7 torus-knot interfaces + AXKIA chain T_{2,9}=9, T_{3,5}=10 + 6 non-column maximizer checks). `auditOnly` per F2 contract. |
| 2026-05-08 | [#567](https://github.com/litlfred/qou/pull/567) | CAL-3 + 1 ppb CI gates restored from `_deprecated/` | landed `14055739` | `git mv` `e0_calibration_audit.py` + `cross_check_trM_1ppb.py` to canonical locations; workflow steps re-added. CAL-3 (E_0 hardcode scan) + 1 ppb tr_M cross-check (Hoefsmit vs `markov_peel`, max 2.94e-15 across 5 atoms) gating again. |
| 2026-05-08 | [#567](https://github.com/litlfred/qou/pull/567) | `/coordinate` skill — §5/§7/§8 additions | landed `549f043e` + `14055739` | §5 review-comment handling (cherry-picked into #568 by Copilot in `18719a3`); §7 periodic sibling-PR triage; §8a main-watch + §8b new-PR-prompt. |
| 2026-05-08 | [#572](https://github.com/litlfred/qou/pull/572) | Hecke-NF follow-ups (cycle-composition Lean + atomic-shift bridge) | landed `5c67cac9` | Carries over the two open Lean items from #567: (a) Lean theorems `cycle_pole_torus_knot`, `axkia_pole_product`, `inter_nucleon_interface_pole` on `CrystalRMatrixSubLemma` (audit Step 4 cycle composition + AXKIA chain integer envelope = 90 + canonical pppnnn interface = 1); (b) atomic-shift-formula bridge in `crystal_pole_order.py` (`atomic_shift_formula_bridge` data section + 6 atomic-test-bench assertions verifying `shift(Z,N) = 18Z + 21N + 1` for {D, T, ³He, ⁴He, ⁵Li, ⁶Li}). 35/35 witness assertions pass. **Excludes** the two LP-theory `sorry`s in `confinement-nf-partial-proof.lean` (`strong_duality`, `complementary_slackness`) which need Mathlib LP-duality scope from a separate PR. |

## Open phases (workplan from `AUDIT-DEEP-2026-05.md` §7)

Updated as of `86aaeb51a`. Strikethrough = done; **bold** = in flight.

- ~~P1 · §3b ledger compliance (mass chain)~~
- ~~P1.b · §3b ledger (fluid + EW)~~
- ~~P4′ · T6 unit-convention resolution~~
- ~~P4″ · ρ_K assembly path (new consumer)~~
- P2 · convention freeze (partial — `q_0` literal in `joint_tower_sdp_solver_v2.py:46` fixed; remaining items are documentation)
- P3 · real `H_{3A}` Wedderburn weights → refines ρ_K beyond leading-order toward 1 ppb. **Substantive math, ~2 wk.**
- P4‴ · migrate legacy `atomic_braid_mass_table.py` and downstream consumers to the ρ_K path.
- P4ⁱᵛ · compute `|tr_M(⁴He)|` (and beyond) via `markov_trace_recursive` on the ⁴He / ⁶Li / … braid words; extend the ρ_K table.
- P5′ · quotient-braid `a(Z, N)` for A ≥ 5 (was open in legacy code as placeholder; in ρ_K path the question shifts to: are higher-A `|tr_M|` values computable, and does the leading-order ρ_K ansatz hold to ≤ 0.1 %?).
- P6 · jet-order → SDP wiring (50–500× compute speed-up; coordinate with #565).
- P8 · compound β-chain σ_shell calibration via AME data.

## Floor

CAL-2 uncertainty (`Q_β` = m_n − m_p − m_e, CODATA ±6.1 × 10⁻⁷ MeV) sets a hard floor at ~**780 ppb** absent a derivation of `Q_β` from substrate alone. The user has explicitly declined deriving `Q_β`; the floor stands.

## Resolutions held by author

| Date | Question | Resolution |
|------|----------|------------|
| 2026-05-08 | T6 unit convention (Options A/B/C/D) | **A + C**: no additive T6, ρ_K · m_e · |tr_M| is the formula, Mittag–Leffler complementarity is the rigorous justification. |
| 2026-05-08 | Class-axiomatise volume / Kashaev pair as bookkeeping (no proof attempt)? | **Yes** — already in the `class_axiomatised_conjectures` list; downstream blocks compliant. |
| 2026-05-08 | Q_β derivation? | **No** (explicit) — 780 ppb floor stands. |

## Open questions for author

(none open at PR `86aaeb51a` time of writing)

## Cherry-pick log

Format: `cherry-pick of <source PR>:<sha> into <target PR>:<sha>` plus 1-line reason.

(none yet — first cherry-pick will be when #565 lands `WitnessBuilder.wrap_legacy` and #564's `atomic-mass-via-rho-k.witness.json` is migrated to use it.)
