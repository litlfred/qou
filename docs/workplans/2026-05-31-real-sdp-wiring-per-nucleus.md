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

## Generalization to all nuclides/isotopes (2026-05-31, PR #1582)

**Question:** does the Phase B constraint machinery generalize beyond ²H?

**Answer:** the *method* generalizes exactly; the *dense per-nucleus SDP
compute* caps at A ≈ 4–5.

### What generalizes (no new physics)

Method 5's constraint rows come from the **Littlewood–Richardson
branching** `H_{3A} ⊃ (H_3)^Z × (H_3)^N`, i.e. the iterated-LR formula
already canonicalised in
[`computations/UNIVERSAL-BRANCHING-PLAN.md`](../../computations/UNIVERSAL-BRANCHING-PLAN.md):

    χ_free(λ) = Σ_{(μ_1,…,μ_A), μ_i ⊢ 3} c^λ_{μ_1,…,μ_A} · Π_i χ^{μ_i}(K_i)

For a nucleus (Z protons, N neutrons), the constituents are Z proton-H_3
blocks and N neutron-H_3 blocks. The deuteron's `H_6 ⊃ H_3 × H_3` is the
A=2 case. The LR coefficients are integers; the constituent characters
are computed once at q_0 — **no fitting at any A**. (Use the corrected
LR coefficient, not the skew-concatenation `f^{λ/⊔μ_i}` which was
refuted in `docs/audits/2026-05-30-universal-branching-multinucleon-gap.md`.)

### Scaling walls

| Wall | Effect | Cap |
|---|---|---|
| `heckeDim(3A) = (3A)!` | SDP matrix size | H_6=720, H_9≈3.6e5, H_12≈4.8e8 — dense SDP feasible to ~A≤4–5 |
| iterated-LR tuple count | constraint-row assembly | combinatorial but sparse (most c=0) |

### Tiered coverage (consistent with #1575)

- **A ≤ 4–5 (²H, ³H, ³He, ⁴He, light Li/Be):** full real per-nucleus SDP
  via the branching route — feasible, this PR's method 5 is the template.
- **252 stable nuclides:** branching method still exact, but dense SDP
  compute is multi-month; needs a sparse / symmetry-reduced solver
  (the §7b Type-B-fold from method 1 is the natural reduction — it halves
  the block count via conjugate-pairing).
- **All 12,804 isotopes:** out of scope for the dense per-nucleus SDP;
  the abstract empty-SDP layer (#1537/#1542/#1566) already covers these
  at the framework-demonstration level.

**Net:** branching = the generalizable constraint source; the bar-fold
(method 1) is the key to pushing the compute wall higher by symmetry
reduction.

## Shell coverage census (2026-06-01, PR #1582)

**Q: can we do all shells?** Real-SDP character data exists only for A≤4.

| Shell / nucleus | A | n=3A | χ_λ witness | y_λ source | real SDP |
|---|---|---|---|---|---|
| proton / neutron | 1 | 3 | ✅ chi-{proton,neutron}-h3 | inline | ✅ wired |
| ²H deuteron | 2 | 6 | ✅ chi-deuteron-h6 (11) | inline | ✅ wired |
| ³He / ³H | 3 | 9 | ✅ chi-{helium-3,tritium}-h9 (30) | wenzl-h9 | ✅ wired |
| ⁴He | 4 | 12 | ✅ chi-lambda-he4-full (77) | wenzl-h12 | ✅ wired |
| ⁶Li | 6 | 18 | ❌ none | ❌ none | abstract only |
| ⁹Be | 9 | 27 | ❌ none | ❌ none | abstract only |
| ¹¹B | 11 | 33 | ❌ none | ❌ none | abstract only |
| ¹²C | 12 | 36 | ❌ none | ❌ none | abstract only |

**A=1 finding (2026-06-01).** Wiring the single-nucleon shell
(`nucleus-real-sdp-{proton,neutron}.witness.json`) shows the Frobenius
Gram is **positive-definite** at A=1 — all 3 H_3 blocks carry positive
q-trace norm, the bar-fold reduction is 3/3, and the operator-selection
solve is bounded with no forbidden channels. The indefiniteness that
makes the deuteron program ill-posed (3 negative-norm blocks,
unbounded) therefore **onsets at A≥2**: it is a property of the bound
*pair*, not of the individual nucleon q-trace. This is consistent with
the Phase B reading that color-flavor (proton uud × neutron udd)
constraints are what regularize the A≥2 program.

**Verdict:** the generic resolver (`nucleus_real_sdp.py`) covers every
nucleus for which a per-nucleus χ_λ witness exists — currently A=1…4. The
Lean abstract empty-SDP uniqueness covers all of Li-6…C-12, but their
*real* SDP needs χ_λ(β_K) at H_18…H_36, which is past the `(3A)!`
compute wall (H_18 = 6.4e15 dim) and has no witness. Producing those is
the multi-week-per-nucleus campaign #1575 scopes; the bar-fold symmetry
reduction is the lever, but a sparse Hoefsmit evaluator at H_18+ is the
prerequisite that does not yet exist. **Adding a shell = produce its
χ_λ witness + Wenzl y_λ at that n**, then one registry line.

## y_λ convention — canonical source settled (2026-06-01, PR #1582)

A pipeline-correctness investigation (user: "pipeline may have errors")
found my `nuclide_braid_pipeline.py` used the WRONG y_λ weight.
Three weights were in play; only one matches the per-nucleus χ witnesses:

| candidate | formula | matches true witness? |
|---|---|---|
| balanced Wenzl | `d_q(λ)² / [n]_q!` (balanced q-int) | ❌ (gives (9)=(1⁹), no sign) |
| q-Schur Markov | `q^{c(λ)} / [n]_q!` | ❌ (fails y_λ·y_{λᵀ}=1/[n]!²) |
| **principal-spec Schur** | `s_λ(1,q,q²,…) / Z`, `Σ y_λ f^λ = 1` | ✅ **9.8e-49 exact** |

**Canonical y_λ** = `schur_principal_mpmath.y_lambda_at_q0_mpmath(n, q0)`.
The integer `f^λ` (SYT count) is the dimension that appears in the
witness `dim` field — NOT the quantum dimension `d_q`. y_λ can be
**signed** (e.g. (6,1,1,1) < 0), which immediately rules out any
`d_q²` form.

The asymmetry between λ and λᵀ comes from the **principal
specialization** `s_λ(1,q,q²,…)` (content-graded), NOT from an
asymmetric q-integer and NOT from Bring/Brioschi.

**χ_λ precision:** the character itself was exact only to 2.66e-14
because `chi_lambda_of_word` uses float64 numpy. Switching to
`char_fast.chi_lambda_fast_mp` (mpmath 50-dps) brings χ to ~1e-49,
matching y_λ. The pipeline now computes both at 50-dps.
