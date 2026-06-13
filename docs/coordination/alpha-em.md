# α_EM canonical derivation — master ledger

> Single source of truth for the **α_EM canonical derivation** goal.
> α_EM is the EM coupling constant; the framework's prediction must
> derive it from substrate primitives (q₀, knot invariants) without
> CAL-anchoring.

## Status (as of 2026-05-31)

| Sub-goal | Status | Evidence |
|----------|--------|----------|
| **α_EM closure to 4.18 ppm** | NEAR-MATCH | `8cd964a99` (categorical re-identification — Bring zero-mode shift) |
| **α_EM Habiro element `[2]_q · (1−h²α)`** | **DERIVED** ✓ | PR #1511 (merged 2026-05-30) — Habiro Taylor coefficients are binomial-exact: `c_k = 2·C(1/2, k/2)·(1/4)^(k/2)` |
| **Bring residue → resolvent form** | DERIVED | `f963fbe69` — single Bring-residue class closes shared open math |
| **α_EM 1/(8π) factor** | DERIVED via Bring | PR #1552 — `1/(8π) = 1/(π·dim H¹(M_Bring))` |
| **RT Phase 3 Schwinger structural form** | in-flight | PR #1549 |
| **RT Phase 4 closure** | open | PR #1552 (RT Phase 4 derivation) |
| **Categorical 1-loop interpretation** | open | PR #1521 |
| **B_4 PSLQ depth** | PARTIAL refutation | `396762dbb` — depth chain complete, refutation partial |

## Why this ledger exists

α_EM is the **template** the c_k flip-flop saga (1ppQ-Q_β ledger) is
trying to mirror. PR #1511 cleanly closed α_EM's "next-order factor"
by identifying the Habiro element `[2]_q · (1 - h² α)`. The Q_β probe
`probe-qbeta-habiro-element-search` looks for the analogous element
for Q_β.

This ledger captures the active α_EM threads + their PR dependencies
so a coordinating agent can see at-a-glance where each piece sits.

## Active PRs (5)

| PR | Branch | Scope |
|----|--------|-------|
| #1505 | `claude/alpha-em-canonical-chain-walkthrough-2026-05-30` | walkthrough: α_EM through the canonical derivation chain (Cat→Alg→Geom→Arch) |
| #1521 | `claude/alpha-em-habiro-categorical-1loop-2026-05-30` | derive: Habiro element `[2]_q·(1-h²α)` IS closed fermion loop in fundamental rep |
| #1549 | `claude/alpha-em-rt-phase-3-2026-05-30` | derive(alpha_em): RT Phase 3 — Schwinger `(1-h²α)` structural derivation |
| #1552 | `claude/alpha-em-rt-phase-4-2026-05-30` | derive(alpha_em): RT Phase 4 — `1/(8π) = 1/(π·dim H¹(M_Bring))` Bring mesh |
| #1508 (merged) | — | Lean conditional theorem for α_EM⁻¹ full form (§3b-cond pattern; the c_3 / c_4-c_7 classes mirror this) |

## Open probes (queue file `todos/alpha-em-queue.json` — TBD)

This ledger does not yet have a populated queue file; the active PRs
above each track their own scope. When a new tranche needs a queue,
follow the `1ppq-qbeta-queue.json` schema.

Items that would belong in such a queue:

- [ ] **Close α_EM final ppm** — current 4.18 ppm near-match (`8cd964a99`); is the residual a numerical floor or a structural gap?
- [ ] **Lean §3b-cond classes for the Bring-zero-mode shift** — extend the existing `EmAlphaInvNextOrderBlochClass` pattern (PR #1508)
- [ ] **Cross-check the Habiro `[2]_q·(1-h²α)` element against Q_β** — does the same element apply? (this is `probe-qbeta-habiro-element-search` in `1ppq-qbeta-queue.json`)
- [ ] **B_4 PSLQ closure** — `396762dbb` left the depth chain complete but refutation partial; close or refute
- [ ] **κ_Coulomb = Bring × √3 hypothesis** — `0eab531a4` coord note suggested this; verify or refute

## Anti-patterns (DO NOT repeat)

- ❌ Yekutieli h² extraction for T(2,9)+T(3,5) — REFUTED route (`a87221e2f`)
- ❌ Bring-CM B_3 off-unit-circle PSLQ — STRONGER refutation (`0c4c46e87`)
- ❌ q-hyperbolic B_3 PSLQ — PARTIAL refutation (`c418cb2c2`)
- ❌ Habiro/full-Jones as alternative tree identification — REFUTED (`833f99e98`)
- ❌ NEAR-MATCH on `1/j(i)` candidate — refuted in 12-candidate sweep (`6a17848a8`)

## Sessions log

| Date | Agent / branch | Intent | Results |
|------|----------------|--------|---------|
| 2026-05-31 (cont. 3) | Claude / `claude/coord-ledgers-option-e-followup-2026-05-31` | backfill this ledger to track α_EM threads | landed; active PRs catalogued; anti-patterns cross-linked from refuted commits |
| 2026-06-11 | Claude / `claude/hopeful-feynman-y0zsyy` (PR #2114) | prove from-the-Lagrangian `2/(3π)` (n=1) + coordinate n=2 with #1495 | Lean `PhotonIRZeroMode` sorry-free: `b₁(M_Bring)=2g=8`, Gauss–Bonnet `Area=4π(g-1)`, `2/(3π)=b₁/Area` (surface harmonic zero-mode, **not** the failed `M×S¹`); same `b₁=8` grounds #1495 RT-plan **Identity 1** `[2]_q/(8π)=[2]_q/(π·dim H¹)` → **n=1 & n=2 unified on genus-4 Hodge data**; `em-coupling-bring-zero-mode.md` + `alpha-em-derivation-open-problems.md` Status corrected (3-manifold guess → proven surface). Boundary: `b₁` topological, `π` archimedean, `[2]_q` substrate (τ_arch-evaluated). |
| 2026-06-12/13 | Claude / `claude/wizardly-ride-zml15z` (PRs #2205, #2208, #2210, #2233) | finish the α_{basis-knot} per-force selection + close `conj:e-hartree` to a single gap + RT C2.3/C1.3 | **(a)** α_{basis-knot} located (PRs #2100/#2107/#2114 were already merged; workplan status was stale) + **per-force selection rule** derived (conditional on `conj:e-hartree`): EM = transpose-**pair** coupling into the unique self-transpose `(2,2)` scalar block; strong `T_{2,9}`/weak `T_{3,5}` = the two single-carrier channels; **invariant `α_s·α_W = α_EM`** exact; even-strand singlet ladder `dim Hom(1,A^n)=Catalan(n/2)` gives exactly 2 slots at n=4 (`alpha_k_*`). **(b)** `conj:e-hartree` rounds 19–20: bare χ = classical hook theorem (round-17 table exact, `(2,2)`-zero structural); dressed `(2,2)` activates `χ₂₂=h([4]/[2])²` at K-shell m=5; **trace-ratio `ρ_(2,2)=χ₂₂/(q[9][10])² = C(q)·α_EM²` exact**, `C(q)=h(q²+q⁻²)²` (the α² shape closes the algebraic side). Conjecture now reduced to **one** gap: is the LP-dual `y_cov` normaliser the squared force-carrier complexity (Mechanism B)? + the `m_e c²` transport. **(c)** RT C2.3 Schwinger sign forced (exact in H₂(q): `(σ²−1)e₋=−(h/q)e₋`); C1.3 consolidated (denom `8π=π·b₁` is the proven #2114 `b₁=8`). Lean `EHartreeTraceRatio` (bracket reduction + factorisation) authored, CI-gated (sandbox mathlib oleans incomplete). |

## Cross-refs

- PR #2233 — `conj:e-hartree` rounds 19–20: dressed `(2,2)` activation + trace-ratio `ρ_(2,2)=C(q)·α_EM²` (algebraic side closed); RT C1.3 consolidation; Lean `EHartreeTraceRatio` (CI-gated). Producers: `e_hartree_round19_dressed_scalar_block.py`, `e_hartree_round20_trace_ratio.py`, `rt_identity_chain_consolidation.py`, `rt_c23_singlet_sign_core.py`.
- PR #2208 — α_{basis-knot} per-force **selection rule** (conditional): self-transpose `(2,2)` scalar block + `α_s·α_W=α_EM`; even-strand singlet ladder. Producers: `alpha_k_four_strand_singlet_selection.py`, `alpha_k_selection_rule_conditional.py`, `alpha_k_split_pole_order_audit.py`. Scoping audit: `docs/audits/2026-06-12-alpha-k-per-force-selection-scoping.md`.
- PR #2114 — α_EM **n=1** photon IR zero-mode `= b₁/Area` on Bring's surface (sorry-free Lean `PhotonIRZeroMode`); `b₁=2g=8` grounds #1495 Identity 1 (`8π = π·dim H¹`)
- PR #1495 — α/(4π) thread ledger + RT 2-loop plan; the **n=2** self-energy `α·[2]_q/(8π)·(1−h²α)` track (Identity 1 `[2]_q/(8π)`, Identity 2 `−h²α` fermion loop)
- PR #1511 (merged) — α_EM Habiro element `[2]_q · (1-h²α)` (the structural template)
- `docs/audits/2026-05-30-qbeta-habiro-derivation-gap-plan.md` — Q_β analog plan
- `docs/coordination/1ppq-qbeta.md` — sibling c_k saga
- CLAUDE.md §Precision goals — L2 / Subgoal-1 / Subgoal-2 framing
- CLAUDE.md §Rendering Hecke-Skein convention §7a — Iwahori-Hecke H_n(q) notation
