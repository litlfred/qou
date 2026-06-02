# PROBE 4 closure test on the deuteron — Σ_w n^w_λ · ρ_w(β_D) vs empirical Δ_λ

**Date:** 2026-06-02
**Branch:** `claude/option-e-probe4-closure-deuteron-2026-06-02`
**Blocks:** Option-E **DERIVE OR FALSIFY** the live in-Option-E direction.

## What this PR tests

The Option-E ansatz for Δ_λ closure on the deuteron:

  Δ_λ(K) = Σ_w n^w_λ · ρ_w(K)

with:
- `n^w_λ` = Kazhdan-Lusztig multiplicities (V_λ multiplicity in the
  KL cell containing w)
- `ρ_w(K)` = canonical-basis-trace at crystal vertex w of β_K

This is the **only remaining live in-Option-E direction** per PR
#1516's cheap-pass refutation + the upstream
`rho_w_crystal_vertex_trace.py` regular-multiplicity refutation
(both refute the n^w_λ = 1 / single-vertex shortcuts).

## Inputs (from already-merged work)

- **`kazhdan_lusztig.py` (n ≤ 6)** — PR #1714 (this session's
  scaffold).  Provides `kl_polynomial(x, w)` for S_6, all 97k
  Bruhat pairs, 22k non-trivial polynomials.
- **`rho_w_crystal_vertex_trace.py`** — on main.  Provides the
  Hoefsmit/Young seminormal ρ_w := ⟨v_T|ρ_λ(β_K)|v_T⟩ per crystal
  vertex w = T ∈ SYT(λ).
- **`option-e-phase1-gram-h6.witness.json`** — PR #1697.  H_6
  Hoefsmit-seminormal Gram (per-block σ_k, ρ_λ(w_0)).
- **`chi-deuteron-h6-at-q0-50dps.witness.json`** — on main.
  y_λ(q_0), χ^λ(β_D), per-partition contributions at q_0.
- **`delta-lambda-empirical-tabulation.witness.json`** — on main.
  Empirical target_signed = −4.35337 for deuteron.

## Outputs

- `n^w_λ` table for S_6 (one row per w ∈ S_6, one column per λ ⊢ 6).
  Sparse: only Bruhat-comparable pairs contribute.
- `ρ_w(β_D)` table at q_0 (720 values, one per crystal vertex).
- `Δ_λ(D)` per partition from the assembled formula.
- `S = Σ_λ y_λ(q_0) · χ^λ(β_D) · Δ_λ(D)` vs `target_signed`.
- **Verdict**: closes (≤ 1% miss) / partial / refuted.

## Method

### Step A. Compute the n^w_λ table from KL cells

The two-sided cells of S_n are in bijection with partitions λ ⊢ n.
For each w ∈ S_n, the two-sided cell containing w is determined by
the **RSK shape** of w (= the common shape of P(w) and Q(w) under
the Robinson-Schensted correspondence).

The Kazhdan-Lusztig left-cell module L_w decomposes into irreps:

  L_w ≅ ⊕_λ (V_λ)^{n^w_λ}

For the **single-cell** case (each two-sided cell is a single
left-cell), the multiplicities satisfy n^w_λ = δ_{λ, shape(w)}
(Kronecker delta).  At the symmetric group S_n this single-cell
property does hold (Kazhdan-Lusztig 1979 conjecture, proved for
type A).

So **for S_6, n^w_λ = 1 if shape(w) = λ, else 0**.

This collapses the formula:

  Δ_λ(D) = Σ_{w : shape(w) = λ} ρ_w(β_D)
         = Σ_{T ∈ SYT(λ)} ρ_T(β_D)
         = Σ_{T ∈ SYT(λ)} ⟨v_T|ρ_λ(β_D)|v_T⟩
         = tr ρ_λ(β_D)
         = χ^λ(β_D)

**This is the SAME formula `rho_w_crystal_vertex_trace.py` already
refuted** (regular-multiplicity / trace-identity collapse).

### Step A — pessimistic reading

The KL-cell decomposition for S_n IS the trivial n^w_λ = δ formula,
which means **the Option-E ansatz Δ_λ = Σ_w n^w_λ · ρ_w collapses
to χ^λ(β_D), which we already know does NOT close**.

So the simplest reading of "PROBE 4 closure" is: **PROBE 4 cannot
close via standard KL/Kashiwara crystal data alone**.  This is a
DERIVATIVE refutation — `rho_w_crystal_vertex_trace.py` already
established it; my KL recursion + n^w_λ cell-decomposition merely
confirms the structural reason.

### Step B — exploring non-trivial assemblies

If the standard n^w_λ collapses to a refutation, the Option-E
direction needs to invoke a NON-STANDARD multiplicity or a
DIFFERENT crystal-vertex weight beyond the Hoefsmit/Young seminormal
diagonal.  Candidates worth probing on this branch:

1. **W-graph edge weights μ(z, w)** — these are the off-diagonal
   structure constants of canonical-basis multiplication.  Could
   serve as a multiplicity beyond cell membership.
2. **Quantum dimension qdim_λ(q_0)** — substituted for f^λ in the
   trace-identity collapse.  At q_0 ≠ 1 this is a non-trivial
   deformation.
3. **Type-B folded multiplicities** — per CLAUDE.md §7b, the
   chirality / CPT-correct crystal is the Type-B folded crystal of
   S_n, not S_n directly.  This changes the n^w_λ structure.
4. **Demazure sub-crystal multiplicities** — restricting to a
   Demazure sub-crystal corresponds to projecting onto a specific
   weight-space slice; may give non-trivial n^w_λ.

Each of these is a separate probe.  The PR's plan is to enumerate
the structural options here, test the cheap ones, and report which
(if any) close.

## Microcommit plan

1. **commit 1**: this design doc + initial scaffold script that
   loads inputs + checks the trivial-collapse hypothesis (Step A).
2. **commit 2**: Step A — implement n^w_λ via RSK shape extraction;
   confirm collapse to χ^λ(β_D).  Refuted.
3. **commit 3**: Step B candidate 2 — quantum-dim weighted variant.
4. **commit 4**: Step B candidate 4 — Demazure sub-crystal probe.
5. **commit 5**: Step B candidate 1 — W-graph edge-weight variant.
6. **commit 6**: Type-B folded crystal scaffolding (if any of 3-5
   suggest the right structural shape).
7. **commit 7**: Witness + per-variant verdict summary; final
   audit-doc / ledger update.

If Step A's pessimistic verdict holds across all four Step-B
variants, the closure result is: **Option-E refuted on deuteron via
standard KL/crystal data**; pivot to GAP-A-3/A-4 per CLAUDE.md §L2.

If any Step-B variant closes to within 1%, escalate to Lean
formalisation (PROBE 3 in the master ledger).

## Coordination

- **Parent: PR #1714** (KL recursion scaffold).  Provides the
  S_6 KL polynomials this branch consumes.  PROBE 4 closure work
  here is downstream of #1714 landing.
- **Adjacent: PR #1516** (Option-E Phase 2 entry-point + PROBE 4
  cheap-pass).  Already refuted the four ad-hoc single-vertex
  candidates.  This PR is the FULL-MACHINERY counterpart.
- **Adjacent on main: `rho_w_crystal_vertex_trace.py`**.  Already
  refuted the regular-multiplicity sum (trivial n^w_λ = 1).
- **Adjacent on main: `probe_q6j_jm_spectral_delta_lambda.py`
  (just landed via 0959c2e2d8)**.  Adjacent geometric direction
  (q-6j JM-spectral volume).  If both this PR and that one
  refute, Option-E is structurally exhausted within current
  framework.
- **Adjacent: PR #1709** (volume-Wedderburn refutation).  Now merged.
