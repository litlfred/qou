# Real per-nucleus SDP wiring — workplan

**Date:** 2026-05-31
**Trigger:** post-session "what's next" pick — drop the abstract empty-SDP layer + wire the *real* per-nucleus SDP.
**Status:** Workplan only. The substantive math is multi-PR / multi-week per nucleus.

## Context

The SDP-uniqueness infrastructure landed in PR #1537 (parameterised module + 10 isotope wrappers + 118 elements) and extended through #1542 (252 stable nuclides) / #1566 (12,804 all known isotopes) certifies T_w uniqueness at the **abstract empty-constraint SDP** level:

```
cost := identity matrix
constraints := none (ι = Empty)
optimum := Φ⋆ = 0
dualSlack := identity (trivially PosDef)
⟹ sorry-free uniqueness via real_strict_complementarity_unique_of_dualSlack_posDef
```

This is the **framework demonstration**. It says: "for any nucleus at strand count `n = 3A`, the empty-constraint SDP has a unique optimum." This is structurally important (proves the framework can certify uniqueness) but doesn't prove uniqueness of the *actual* T_w that consumes the mass formula.

## The real per-nucleus SDP

For an actual nucleus with mass-formula constraints, the SDP looks like:

```
cost      := T_w-derived cost matrix (multi-term, from mass formula)
constraint(i) := A_i (linear constraint encoding quark-content / sheet-structure)
rhs(i)    := b_i (matching scalar, from per-nucleus AME2020 data)
optimum   := Φ_w⋆ ∈ Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ
```

The cost matrix depends on:
- Multi-term mass-formula assembly (`mass-formula-6term-mpfr-50dps.witness.json` style)
- The Hoefsmit seminormal basis for `H_n(q)` at `n = 3A`
- The Wenzl Markov-trace weights `y_λ` at the substrate `q_0`

The constraints depend on:
- Quark composition (proton uud × neutron udd for ²H, etc.)
- Per-sheet color-flavor mapping
- Conservation laws (charge, baryon number, etc.)

## What's gated

The existing per-nucleus theorem qualifiers in `Applied<Nucleus>Uniqueness.lean` files name exactly what's missing:

| Nucleus | Theorem | Pending what |
|---|---|---|
| ²H | `deuteron_uniqueness_via_empty_sdp_pending_multiterm` | multi-term cost from mass formula |
| ³H | `tritium_uniqueness_via_empty_sdp_pending_hoefsmit` | Hoefsmit H_5 basis (Python port) |
| ³He | `helium3_uniqueness_via_empty_sdp` | (none — closed via `_unique_of_dualSlack_posDef`) |
| ⁴He | `helium4_uniqueness_via_empty_sdp` | multi-term cost (Sprint 2 partial) |
| ⁶Li..¹¹B | various | Hoefsmit + cost |

## Approach: smallest case first

Start with the **deuteron** (²H, A=2, n=6, `heckeDim 6 = 720`). It's the smallest case where the multi-term cost is non-trivial.

### Phase A — define the cost matrix structurally

1. Express `T_w(deuteron)` as an explicit element of `H_6(q)` via the canonical atom-braid recipe (`atom_braid_word_3A(1, 1)`).
2. Compute the Markov-trace eigenphase decomposition `T_w = Σ_λ y_λ χ_λ(T_w) · projection_λ`.
3. Define the cost matrix `C_deuteron := Σ_λ c_λ · projection_λ` where `c_λ` are mass-formula-derived coefficients.

### Phase B — define the constraints

1. Identify the 9-pair color-flavor decomposition (2·(u,u) + 4·(u,d) + 1·(d,u) + 2·(d,d)) — from PR #1445.
2. Each pair contributes a linear constraint on `Φ`. 4 distinct constraints (after symmetry).
3. RHS values derived from AME2020 deuteron binding energy.

### Phase C — strong-duality witness

1. Solve the SDP numerically (cvxpy / clarabel) at `q_0` to get `(Φ⋆, y⋆, S⋆)`.
2. Verify dualSlack `S⋆ = T - Σᵢ yᵢ⋆ Aᵢ` and check whether it's PosDef.
3. If yes → sorry-free uniqueness via `_unique_of_dualSlack_posDef`. If no → strict-complementarity hypothesis is class-axiomatised (§3b-cond).

### Phase D — Lean wiring

1. Replace `deuteron_emptySDP` with `deuteron_realSDP` in `AppliedDeuteronUniqueness.lean`.
2. Re-prove `deuteron_uniqueness_closed` using the real SDP.
3. Migrate downstream consumers.

## Effort estimate per nucleus

| Phase | Effort |
|---|---|
| A. Cost matrix structural | 1-2 days per nucleus |
| B. Constraints | 1 day per nucleus |
| C. Strong-duality witness | 1-2 days per nucleus (depends on whether dualSlack PosDef closes) |
| D. Lean wiring | 1 day per nucleus |

**Per-nucleus total: ~1 week.**

7 QOU-tracked light nuclei × ~1 week each = **~7 weeks of focused work** to bring the real-SDP layer to QOU R5-full coverage.

For all 252 stable nuclides — multi-month campaign. For all 12,804 isotopes — out of scope at this granularity; the parameterised abstract layer suffices.

## Dependencies / blockers

1. **Hoefsmit seminormal basis Lean formalisation** — Sprint 5 IwahoriHecke landed the skeleton (#1525); concrete cell-content recurrence is open.
2. **Multi-term cost wiring** — need a clean Lean expression of the mass-formula assembly (currently a Python compute, not yet typed in Lean).
3. **Color-flavor 9-pair decomposition** — PR #1445's `ColorFlavorCompatible` class is the typed interface; needs concrete instances per nucleus.
4. **SDP solver bridge** — current Python/clarabel solver outputs JSON; need a Lean axiom layer importing the verified numerical witness.

## What this workplan is NOT

- Not a 1-PR job
- Not LSP-verifiable in this container (lake unavailable)
- Not blocking the existing empty-SDP demonstration layer (which is already merged + sorry-free)

## Cross-references

- [`docs/coordination/2026-05-30-sdp-uniqueness-status.md`](../coordination/2026-05-30-sdp-uniqueness-status.md) — current status
- [`docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md`](2026-05-31-witness-lean-uniqueness-ref-wiring.md) — witness-side wiring (sibling effort)
- PRs #1537, #1542, #1554, #1557, #1559, #1566 — abstract SDP infrastructure
- PRs #1445, #1525 — uniqueness scaffolds + Hoefsmit Sprint 5
