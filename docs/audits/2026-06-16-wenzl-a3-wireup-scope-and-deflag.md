# Wenzl A≥3 wire-up: status, inert-extract de-flag, and Rust-port scope (2026-06-16)

**Branch:** `claude/wenzl-a3-wireup-scope-deflag-2026-06-16`
**Context:** closes the loop on the closure-b interface-operator line
([#2353](https://github.com/litlfred/qou/pull/2353),
[#2360](https://github.com/litlfred/qou/pull/2360),
[#2366](https://github.com/litlfred/qou/pull/2366) — all merged), the
least-squares-fit audit ([#2362](https://github.com/litlfred/qou/pull/2362),
merged), and the sibling fusion verification
([#2365](https://github.com/litlfred/qou/pull/2365), merged). It (1) corrects an
over-attribution in the fit audit, (2) de-flags the inert min-norm extracts, and
(3) scopes the remaining Rust port — the genuine ¹⁶O A≥3 speedup unlock.

## 1. Status of the closure-b interface operator (where things stand)

The interface operator `A^λ_{μν}(I)` of the operator-valued Wenzl branching
combiner is now established as a **closed-form categorical** object — *not* a
least-squares fit:

$$A^\lambda_{\mu\nu}(I) \;=\; \Pi_{\mu\nu}\,\rho_\lambda(I)\,\Pi_{\mu\nu}$$

the `(μ,ν)`-isotypic diagonal block of the seminormal interface-generator matrix.
Verified, exact (50 dps), on `main`:

| Result | Where | Precision |
|---|---|---|
| `A = Π ρ_λ(I) Π` reconstructs `χ^λ` (deuteron) | `a_operator_categorical.py` (#2353) | 1.5e-49 |
| gauge-aligned `A_combiner` in `ρ_μ⊗ρ_ν` coords, full combiner identity | `a_operator_gauge_align.py` (#2360) | 6.7e-49 |
| **H₉ universality** — generic multi-strand H₆ inner words | `a_operator_gauge_align.py` (#2360) | 7.1e-50 |
| `V_μ⊗V_ν⊗ℂ^c` multiplicity structure resolved | `a_operator_gauge_align.py` (#2360) | exact |

The sibling fusion line ([#2365](https://github.com/litlfred/qou/pull/2365),
`computations/wenzl_a3_cross_check.py`) **independently verified the same formula**
at A=3 (f64, ~1e-12), using Jucys–Murphy central-element projectors where this
line uses transposition class-sum projectors — **mathematically equivalent**
(both compress `ρ_λ(I)` to its `(μ,ν)`-isotypic diagonal blocks). The two lines
are **complementary, not duplicative**: #2365 proves the formula; the closure-b
line builds the gauge-aligned, exact-precision, H₉-universal construction.

## 2. De-flag: the H₉⁺ min-norm extracts are inert (audit #2362 correction)

The fit audit ([#2362](https://github.com/litlfred/qou/pull/2362)) listed the H₉/
H₁₂/H₁₅/H₁₈ least-squares `A^λ_{μν}` extracts as **"production-consumed"**. Tracing
the consumer chain shows this is an **over-attribution** — they are loaded into a
filename map but **superseded before use**, so they feed **no live A≥3 value**:

- [`canonical_tr_m_via_branching.py:367`](../../computations/canonical_tr_m_via_branching.py)
  — for **A≥3 the value comes from the lossless fine-Bratteli transfer matrix**
  `tr_m_atom_via_transfer.tr_m_atom_zn` (Σ_{λ⊢3A} y_λ χ^λ over all partitions at
  50 dps; ≡ `char_fast` full Hoefsmit to 4.7e-15).
- [`canonical_tr_m_via_branching.py:200,263`](../../computations/canonical_tr_m_via_branching.py)
  — `compute_chi_lambda_via_branching` **returns `None` for A≥3**, *before* the
  H₉⁺ extracts in `EXTRACT_FILENAMES` are ever applied.
- [`canonical_mass_table_extended.py`](../../computations/canonical_mass_table_extended.py)
  — the production mass table's default methods are `markov_peel` (exact
  symbolic-q) / `laurent_q_rust`; the extract/branching path is opt-in and still
  defers A≥3 to the transfer.

**Conclusion:** the live A≥3 mass/binding values come from exact/lossless paths
(`markov_peel` / `laurent_q` / transfer). The suspect min-norm extracts are
**suspect-but-inert**. Only the **H₆ deuteron extract (full-rank, correct)** is
actually consumed (A=2). #2365's merge did not change this. The fit audit's
"top-3 concerning / production-consumed" framing is amended here: the fits are a
**latent** hazard (wrong if ever wired), not a **live** one.

This does *not* downgrade the audit's value — the fits are still the right thing
to remove, and the categorical construction is the right replacement; it only
corrects the urgency/blast-radius framing.

## 3. Scope: the Rust port + recursion wiring (the real A≥3 unlock)

What remains for the operator-valued combiner to *replace the transfer matrix*
at A≥3 (the ¹⁶O feasibility unlock, per
[`docs/workplans/2026-06-16-wenzl-branching-a3-unlock.md`](../workplans/2026-06-16-wenzl-branching-a3-unlock.md))
is **performance**, not correctness — the formula and gauge alignment are proven.
The pure-mpmath construction is **O(r⁶)** per block (the intertwiner null-space
SVD), so it does *not* beat the `p(3A)`-bound transfer in Python. The genuine
speedup needs a Rust kernel.

### What already exists (do not re-port)
- **Exact MPFR seminormal matrices** `ρ_λ(σ_i)` — `seminormal_mpfr::seminormal_matrices_mpfr`, exposed as `pyhecke_native.seminormal_matrices_mpfr` (#2353).
- **LR coefficients** — `littlewood_richardson.rs`; **cross-level embedding** — `cross_level_embedding.rs`.

### What the Rust port adds
1. **Isotypic projectors** `Π_{μν}` — transposition class-sum (separates all 11 H₆ irreps at q₀, min eigen-gap 1.15; the q≠1 deformation breaks the q=1 `(4,1,1)/(3,3)` content-sum degeneracy) + Lagrange spectral projection, in `rug::Float`.
2. **Intertwiner / gauge-alignment** — the `(I⊗g̃ − Rᵀ⊗I)vec(U)=0` null-space solve and the `A_combiner = partial-trace(U⁻¹ Ĩ U)` (the O(r⁶) bottleneck), at scale.
3. **Recursion kernel** — `compute_chi_lambda_via_branching` for A≥3: peel one H₃ block per level, computing the inner `ρ_μ(W_inner)` recursively (the `_build_rho_recursive` the current Python `return None` placeholder names), cost `Σ_level Σ_{μ,ν} dim(μ)·dim(ν)` ≪ `p(3A)`.
4. **PyO3 binding + production wiring** — route A≥3 in `canonical_tr_m_via_branching.py` through the Rust operator-branching, replacing the transfer fallback once cross-validated.

### Discipline gates (per CLAUDE.md)
- **No-regression:** cross-validate the Rust combiner against the transfer matrix at **1e-25** for every atom D…⁶Li before wiring; run both precision dashboards (L1 `onepb-status-dashboard`, L2 `per-observable-100x-status`) and report deltas (must not regress).
- **MBA-appendix sync:** the A≥3 combiner realises Steps 9–11 of the canonical chain → update the matching `alg:`-block in `appendix-mass-binding-algorithms/` in the same PR.
- **Speedup-only, not a value change:** the A≥3 `tr_M` value is already validated; this changes the *route*, not the number. No fit, no fourth calibration.

### Verification anchor
The Python categorical construction (`a_operator_gauge_align.py`,
`gauge_aligned_A_combiner_general`) is the **exact-precision spec** the Rust port
must match bit-for-bit at 1e-25 — it is the oracle.

## 4. Disposition of the audit's 5 suspect fits

| # | File:line | Status after this analysis |
|---|---|---|
| 1 | `a_operator/A_operator_extract_at_level.py:351` | inert (superseded by transfer); annotated; replaced-by → categorical construction |
| 2 | `sublemma_2_1_A_operator_extract_h9.py:416` | inert; annotated |
| 3 | `sublemma_2_1_A_operator_extract_h12_nn.py:309` (+ `…_streamed.py:259`) | inert; annotated |
| 4 | `per_nucleon_shift_derivation.py:354` | contained (no production consumer) — framing flag only, per audit |

**Witness regeneration (categorical replacements for the inert extracts)** is a
low-priority follow-up — since the extracts are inert, regenerating them is
correctness-of-record, not a live fix; it can ride on the Rust-port PR (which
produces the categorical `A` at scale anyway).

## Cross-references
- [`docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md`](2026-06-16-categorical-interface-operator-closure-b-design.md) — the categorical construction (renamed from "analytic" per #2366).
- [`docs/audits/2026-06-16-unjustified-least-squares-fitting-audit.md`](2026-06-16-unjustified-least-squares-fitting-audit.md) — the fit audit this amends (#2362).
- [`docs/workplans/2026-06-16-wenzl-branching-a3-unlock.md`](../workplans/2026-06-16-wenzl-branching-a3-unlock.md) — the A≥3 / ¹⁶O workplan.
- `computations/wenzl_a3_cross_check.py` — sibling fusion verification (#2365).
- [`computations/canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py) — the combiner (A≥3 currently → transfer).
