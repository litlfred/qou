# Main-review workplan — week of 2026-08-02 → 08-08 (~1172 commits)

**Date:** 2026-08-08 · **Purpose:** synthesize the week's main landings into a prioritized,
honest workplan (what's proved/closed, what's walled, what's open-and-live). Companion to
`docs/precision-goals.md` + the 2026-08-02 FOREVER-GATE lever map. STATUS.md is stale
(June-dated) — do not trust its counts.

## The one hard result of the week

**The deuteron Δ_λ binding magnitude is proved genuinely ABSENT, not mis-weighted.** The
ℓ¹-ceiling proof (`docs/audits/2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md`,
bean `qou-kemt`, PR #4664): `Σ|y_λ χ^λ Δ_λ| / target ∈ [0.36, 0.59] < 1` for D/T/³He/⁴He —
even perfect constructive interference of the *existing* terms reaches ≤59% of AME. So **no
re-signing, no re-weighting, no Δ_λ re-derivation can close it**; a genuinely NEW additive,
super-pairwise, knot-dependent term is required. This retroactively explains every walled
route (they were all re-weightings of the same insufficient terms).

## Proved / closed this week (do NOT redo)

| item | verdict | ref |
|---|---|---|
| Δ_λ magnitude absent (ℓ¹ ceiling ≤59%) | proved | `qou-kemt` / #4664 |
| N=2 cannot host the flavor octet | proved | `qou-8pl3` |
| substrate-q₀ derivation | FOREVER-GATED (unchanged) | `qou-eic1` |
| q-integer convention = balanced (bar-even), forced | derived | `qou-qint` |
| RSZ C1-∞ route | closed | `2026-08-08-rsz-c1-infinity-route-closed.md` |
| three-row-dominated / torsion=ν_SDP / naive-z / saddle-offset | refuted | option-e.md |
| **transverse NA-Stokes surface-curvature pairing** (this session, PR #4798) | scope-a negative — built + under-determined (O(100× log-branch gauge freedom) | `qou-prjo` |

## Walled (dead ends — do not re-pitch)

DT/Behrend count *for the binding magnitude* (distinct object — closing it still gives
B(D)=0.380 MeV, −82.9%, #4601); flavor-N=3 import (no N=3 to import, `qou-8pl3`); driver-14
as internal (irreducibly external, #4601); any **convention-selected** normalization ratio
(ROAST §R0.1 — convention-shopping); b4-cumulant / A4-interface one-scalar fit gate.

## Open-and-live — prioritized

### 1. Extended-Bloch tetrahedron term for the binding magnitude (HIGHEST leverage)
Beans `qou-78pt` / `qou-l2t2`; `docs/audits/2026-08-07-extended-bloch-group-fixes-the-normalization-fit.md`.
Neumann's **extended Bloch group** (Vol + i·CS tetrahedron count) is the ONLY surviving
candidate satisfying all three constraints the ℓ¹-ceiling + pairwise-cap proofs impose:
**additive/extensive** (sum over tetrahedra), **super-pairwise ≥3-body** (4-vertex simplex
escapes the proved `ρ_A ≤ C(A,2)` cap, `exchangeDet_pow_two_le_four`), and **knot-dependent**.

> **Direct link to this session's PR #4798.** My na-Stokes probe found the transverse
> surface-curvature pairing carries **O(100× log-branch / germ gauge freedom** the corpus
> does not fix (c₂ ranged 0…897, never ≈1). The extended Bloch group **canonically fixes
> exactly that log-branch ambiguity** (the flattening from the gluing equations). So PR #4798
> is not just a dead end — it *localizes why* the naive surface pairing fails and points at
> the extended-Bloch flattening as the fix. **Next unit:** derive the flattening from the
> trefoil gluing equations (NOT fitted), then recompute the tetrahedron term — the successor
> to `qou-prjo`.

### 2. Q_β c₃ derivation (unlocks 3 of 5 L2 misses)
`2026-08-08-qbeta-l2-assessment-post-week-landings.md`. Q_β's whole 1248 ppb residual is the
**c₃-and-beyond truncation**; c₃ is currently cal-anchored (self-indicted as not-a-prediction).
The alien-calculus Stokes multiplier (`qou-vkg5` / `qou-xufp`, after the RSZ route closed)
feeds this. Q_β drives the Q_β/m_n/Δ_pn trio (3 of 5 L2 misses).

### 3. A3 prolongation-symbol amplitude `E` (keystone)
Bean `qou-jqof`; option-e.md. The anti-self-adjoint lift isolated the deuteron wall to
**exactly one** free/unique scalar `E`; deriving it from the prolongation symbol closes
r*≈1.585. Proved-to-be-one-scalar; the derivation is the open keystone.

### 4. Mechanical / infra
- Land the `per_observable_100x_status.py` witness-loader fix (tier auto-promotion was dead
  code — flat name resolution missed `qbeta/qbeta-ck-cache.witness.json`).
- Drain the wall-side §7c weak-triage queue (med65 second half: 13 LEGIT + 3 BLOCKED).
- **Adopt the new folio-assistant Lean-triviality checkers on qou's Lean** (see below).

## folio-assistant update (done this session — synced +115 → `a0144ab`)

New QA infra now available to qou (symlinked sibling; setup re-verified, exit 0). Highest-value
for our discipline — run these on qou's `.lean`:
- `proof-not-machine-trivial`, `proof-no-placeholder-stub`, `proof-compile-cost`,
  `proof-no-cost-regression` — auto-detect vacuous/`True`-stub proofs + cost regressions
  (the machine complement to "sorry-free ≠ derived").
- `lean-ref-owns-decl`, `uses-formal-coverage`, `uses-editorial-hygiene` — dep/coverage integrity.
- `cite-named-theorem`, `voice-agent-speak`, `voice-probe-narrative` — citation + voice.
- New `folio-core` skills: `dispatch-agent`, `exposition-swarm-drain`, `uses-editorial-review`.
- Also on main this week: vacuity detector now catches `axiom X : True` + anonymous-constructor
  `rfl` witnesses (#4779); soundness audit in the pre-commit preflight (`28c7286e1`).

**Adoption item:** run `proof-not-machine-trivial` + `proof-no-placeholder-stub` across the
QOU library to sweep for any vacuous proofs the older detectors missed — a bounded, high-value
next tranche.

## Recommended immediate next
Given this session's PR #4798 localized the na-Stokes log-branch freedom, the highest-leverage
continuation is **workplan #1**: derive the extended-Bloch flattening from the trefoil gluing
equations and recompute the tetrahedron term — the direct, principled successor that fixes the
gauge freedom #4798 exposed.
