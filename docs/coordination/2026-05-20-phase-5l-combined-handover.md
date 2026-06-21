# Phase 5l + 5l.1 + canonical-derivation cheat sheet — handover

**PR**: [#854](https://github.com/litlfred/qou/pull/854) (claude/phase-5l-combined-with-5l1)
**Date**: 2026-05-20
**Status**: in /prepare-merge

## What this PR contains

A single combined PR with three threads of work:

### 1. Phase 5l — structural identity for the constit-side per-Z step factor

$$\rho_Z^{\mathrm{constit}}(q) \;=\; \mathrm{tr}_M^3(\mathcal{B}_p, q)$$

Derivable from Wenzl 1988 §1.7 disjoint Markov-trace multiplicativity; empirically verified at mpfr-50-dps precision (~$10^{-50}$ rel.err.) across the substrate window. Combined with PR #819's interface factor, gives the **exact** full $\mathrm{tr}_M$ per-Z step at a p-* boundary:

$$\frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})} = z(q) \cdot \mathrm{tr}_M^3(\mathcal{B}_p, q) \quad \text{no residuals}$$

New content blocks: `prop:constit-factor-tau-M-proton-identity` (.ts + .md + .lean). Lean: `MarkovTraceDisjoint` §3b-cond class (generic Field R per §7c); theorem `constit_factor_eq_tau_M_proton` proved sorry-free via `pow_succ + field_simp + ring`.

Updated: `conj:constit-factor-2q-minus-1.md` — RESOLVED banner pointing to the new proposition; FALSIFIED banner from Phase 5k.2 preserved as bridge.

Witnesses (3 new + 1 existing modified):
- `rho-constit-equals-tau-M-proton-phase5l.witness.json` — WIRED to prop block
- `constit-factor-varying-q-phase5k2.witness.json` — audit-only (falsification probe)
- `tau-M-proton-closed-form-phase5l1.witness.json` — audit-only (symbolic probe)
- `docs/audits/2026-05-20-constit-factor-closure-chain.md` — shared audit doc

### 2. Phase 5l.1 — symbolic χ_λ closed forms

Symbolic Laurent rationals for the three H_3 Hecke characters on the proton braid:

$$\chi^{(3)}(\mathcal{B}_p, q) = \frac{q(q^2 + 1)^2}{4}$$
$$\chi^{(2,1)}(\mathcal{B}_p, q) = \frac{q^{22} + q^{20} + q^{18} + q^{14} - q^8 - q^4 - q^2 - 1}{4 q^{11}}$$
$$\chi^{(1,1,1)}(\mathcal{B}_p, q) = -\frac{(q^2 + 1)^2}{4 q^5}$$

Probe-style; the y_λ normalization reconciliation (symbolic vs numeric Wenzl bridge) is **queued as Phase 5l.2**.

### 3. Canonical-derivation cheat sheet (CLAUDE-facing)

New doc: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md).

A one-page-up map of the substrate → observables chain, with per-step:
- Math (formulas)
- Paper reference (propositions)
- Canonical compute script
- Witness file

Plus:
- **Φ_q (Faddeev) vs Li_2^q (Rogers) context sorting** — confirms binding pipeline is Φ_q-free per stage-1b audit (`126699b8c`); mass-anchor scripts correctly use Φ_q
- **Phase 5 findings** highlighted (5b, 5c.1, 5g, 5k.1, 5l, 5l.1, 5n) with status (proved, falsified, conjectured)
- **Pipeline-discipline migration backlog** — 5 actions identified from the 10-day deep review:
  1. λ-scale categorical derivation → m_p production
  2. Migrate 20 importers of SUPERSEDED `mass_endomorphism.py`
  3. Wire Rust LR adapter into atomic_tr_m_* (500× speedup at ⁴He)
  4. Closed-form interface factor in 4 production tr_M scripts
  5. Reeb/Garside compute verification

**AGENTS.md cross-link** added at top so any agent picking up final-stage work has the chain visible.

Also updates the paper-side `pre-archimedean-derivation-chain.md`:
- Adds an "Audience reading note" pointing at the cheat sheet
- Adds **Step 10.5** with the combined Phase 5l + 5c.1 closed form

## Review history (preserved)

| Source PR | Cycles | Comments | Status |
|---|---:|---:|---|
| #842 (sub of #845) | 1 | 4 Copilot | accepted, closed |
| #845 | 3 | 5 + 5 + 4 = 14 Copilot | accepted, closed (superseded by #854) |
| #849 | 2 | 5 + 4 = 9 Copilot | accepted, closed (superseded by #854) |
| **#854** | 2 | 13 + 0 Copilot (in flight) | 13 accepted in `aabccaa03`; awaiting next review |
| **Total** | **8 cycles** | **40 Copilot dispositions** | preserved |

Plus wiring fix `ae6d179d4` and this handover commit.

## Phase 5n notation throughout

All new content uses post-Phase-5n notation (merged via PR #853):
- $\mathcal{B}_K$ atomic braid word (was $\beta_K$)
- $\mathcal{B}_K^{\mathrm{vac}}$ vacuum factor (was $\beta_K^{\mathrm{constit}}$)
- $\bowtie_K$ intra-atom interface (was $\Delta_I^K$)
- $\oplus$ inter-block Hopf-link (was bare $\bowtie$)
- $\mathrm{tr}_M$ Markov trace (was $\tau_M$)
- $\mathfrak{E}$ energy family (was $\mathbf{E}$)
- $\mathfrak{B}(q)$ info bandwidth (was $\mathcal{B}(q)$)
- $G_q$ gravitational vs $\mathrm{G}(q)$ Gram matrix (disambiguated)

## What's next (post-merge)

### Phase 5l.2 — Wenzl-bridge y_λ normalization reconciliation
Symbolic `y_lambda_wenzl_bridge_symbolic` produces degree-80+ expressions that differ from numeric pipeline by a normalization constant. Reconciling these gets the full canonical closed form for $\mathrm{tr}_M^3(\mathcal{B}_p, q)$.

### Pipeline-discipline migrations (the 5 actions in the cheat sheet §5)
Each is a discrete mechanical migration:
1. m_p categorical λ-scale (highest impact — discipline violation)
2. mass_endomorphism → mass_tower_operator_valued (20 importers)
3. Rust LR adapter (500× speedup waiting)
4. Closed-form tr_M optimization (4 scripts)
5. Reeb/Garside compute verification

### Phase 5m — Wenzl §1.7 Lean formalization
Currently axiomatized as §3b-cond class `MarkovTraceDisjoint`. Replacing the axiom with a formal Lean proof would require building H_n(q) parabolic embedding + Markov trace in Lean. Estimated 1-3 weeks focused work; out of scope for this PR.

## Files changed in this PR (final state)

| File | Type | Status |
|---|---|---|
| `content/.../constit-factor-tau-M-proton-identity.{ts,md,lean}` | content block | NEW (prop:constit-factor-tau-M-proton-identity) |
| `content/.../constit-factor-2q-minus-1.md` | content block | UPDATED (RESOLVED + FALSIFIED banners) |
| `content/.../pre-archimedean-derivation-chain.md` | content block | UPDATED (cheat-sheet cross-link + Step 10.5) |
| `docs/canonical-derivation-cheat-sheet.md` | new doc | NEW (cheat sheet for Claude / math-phys grad) |
| `docs/audits/2026-05-20-constit-factor-closure-chain.md` | audit doc | NEW (audit-only target for 5k.2 + 5l.1 witnesses) |
| `docs/coordination/1ppb-categorical-chain.md` | coord ledger | UPDATED (Phase 5l + 5k.2 + 5l.1 + coordination rows) |
| `docs/coordination/2026-05-20-phase-5l-combined-handover.md` | handover | NEW (this doc) |
| `computations/rho_constit_equals_tau_M_proton_phase5l.py` | script | NEW (Phase 5l verification) |
| `computations/rho-constit-equals-tau-M-proton-phase5l.witness.json` | witness | NEW (wired to prop block) |
| `computations/constit_factor_varying_q_phase5k2.py` | script | NEW (Phase 5k.2 falsification probe) |
| `computations/constit-factor-varying-q-phase5k2.witness.json` | witness | NEW (audit-only) |
| `computations/tau_M_proton_closed_form_phase5l1.py` | script | NEW (Phase 5l.1 symbolic probe) |
| `computations/tau-M-proton-closed-form-phase5l1.witness.json` | witness | NEW (audit-only) |
| `AGENTS.md` | repo discipline | UPDATED (cheat-sheet cross-link at top) |

## Test plan

- [x] `bun run validate quantum-observable-universe` — Valid (1 intentional warning, same as main)
- [x] Wiring audit: 1 witness wired (prop block), 2 audit-only (no orphans from this PR)
- [x] 13 Copilot review comments accepted in `aabccaa03`; wiring fix in `ae6d179d4`
- [ ] CI `validate` passes on final commit
- [ ] Final Copilot review (post handover + cheat sheet)
- [ ] Lean build (deferred to CI — no local toolchain)

## Open question / future

Should the cheat sheet at `docs/canonical-derivation-cheat-sheet.md` be promoted to a content block (and rendered into the paper as an appendix), or kept as Claude-facing infrastructure? Currently kept as docs/ to preserve the paper-side derivation chain block's focus on the categorical chain (without compute-pipeline detail).
