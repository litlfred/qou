# Categorical binding wiring — state, the refuted (1+q)/2, and the non-fitting direction

> **Bean.** [`cbnf`](../../.beans/cbnf--categorical-binding-wiring-no-fitting.md) (parent `qz9k`).
> **Discipline.** NO fitting — the Δ_λ gate forbids a seventh fit-ansatz; report tiered.
> This is a **state-pin + grounded structural observation**, NOT a probe run (the live
> probe is infra-gated, see §4). No production wiring changed.

## 1. Wired vs exploratory (pin the state)

| Form | Status | Where |
|------|--------|-------|
| **B_sym** (log-trace Kashaev) | **WIRED (production)** | `binding_canonical.py`, `tr_m_atom_via_transfer.py::tr_m_atom_zn`; α-cluster atoms via `alpha_cluster_recursion.py` |
| **B_magic** (⁴He doubly-magic) | **WIRED (production)** | scalar Borromean-volume form `ρ_F·m_e·A·8G` |
| LP/SDP dual-emission | **WIRED (contract)** | `lp_dual_solver.py` + `lp_dual_witness_validator.py` (CI) |
| B_lin / B_qCLT(_fac) | exploratory (diagnostic) | `binding_single_pipeline_comparison.py` |
| **Option-E v9 `(1+q)/2`** | **exploratory — refuted near-match (§2)** | `option_e_v9_*` (witness-only, un-wired) |

The canonical dashboard (`dashboard-low`, `dashboard-sweep`) runs the **trace** forms
(B_sym / B_magic / q-CLT) off the one canonical Jones–Markov trace; per-partition Δ_λ is
the **open gate** that B_sym consumes.

## 2. The (1+q)/2 A=3 mirror factor is a REFUTED near-match — do NOT re-chase

[`option-e.md`](../coordination/option-e.md) §"v9 canonical closure" + PROBE 1
(PR #1707, audit `2026-06-02-option-e-derive-1plusq-over-2.md`):

- The v9 mirror-pair formula `B_T − B_³He = m_π·ℏ_q·(1+q)/2·Σ_λ y_λ·(χ^λ(β_T)+χ^{λᵀ}(β_³He))/2`
  was reported at 0.11% — but that figure was a **stale muon-anchor literal**
  (`q=1.1097…`). At the **canonical proton q₀** the required closure factor is
  `R = 1.05372` while `(1+q)/2 = 1.05499` — off by **+0.12%, sign-flipped**.
- **Four structural hypotheses REFUTED** (PR #1707): σ_1 standard-rep trace (−80%),
  Hoefsmit `1/[2]_q` (−53%), `√([3][1])/[2]` (−18%), `q/[2]_q` (−48%). The only
  "matches" — `[2]_q/2`, `(q+1)/2` — are tautological renamings of `(1+q)/2`.
- **Verdict:** `(1+q)/2` is empirically close but **NOT structurally forced**. It stays
  **un-wired**; A=3 closure is **OPEN**; per AGENTS.md there is **no v10 ansatz**.

So `cbnf`'s acceptance is **not** "derive (1+q)/2" (a refuted near-match). It is to record
that refutation and point at the genuine non-fitting direction (§3).

## 3. The non-fitting direction: GAP-A-3 two-layer factorisation

Nine partition-statistic / induction / stabilisation ansätze are closed (the six Δ_λ-gate
failures + Bratteli #1841 + Markov-trace #1850 + Kashiwara-single-statistic #1860). The
survivor is **GAP-A-3** ([`gap-a3 scope`](2026-06-04-gap-a3-brane-tower-level-selection-scope.md)):
factor the per-isotope Δ_λ as
$$
\Delta_\lambda(K) \;=\; \underbrace{A(K)}_{\text{Phase-4, derived}} \cdot \underbrace{P_\lambda(K)}_{\text{partition projection (open)}},\qquad
A(K)=\frac{\mathrm{Vol}_{\mathrm{hyp}}(K)}{[8]_q}\,[3]_q^{2(Z-1)}\bigl(q^{1/2}+q^{-1/2}\bigr)^{4N}
$$
with `A(K)` already substrate-derived (≤ 2.5% zero-parameter). The closure reduces (since
`A(K)` is λ-independent) to
$$
A(K)\cdot\sum_{\lambda\vdash 3A} y_\lambda(q_0)\,\chi^\lambda(\beta_K)\,P_\lambda(K) \;=\; -B(K)/m_e .
$$
**Why this is not the 7th fit:** `A(K)` is taken as already-derived; `P_λ(K)` is sought as a
**brane-tower content count** (color `V_1` / spin `V_{1/2}` / normalisation `V_{7/2}`
channels, scope §4), not a fitted scalar.

## 4. A grounded structural observation (sharpens the §4 probe)

The sum `Σ_λ y_λ(q_0) χ^λ(β_K)` is, by the canonical **Frobenius pairing**, exactly the
Markov trace: `tr_M(β_K) = Σ_λ y_λ χ^λ(β_K)` (canonical-chain step "Frobenius pairing
tr_M = Σ_λ y_λ χ_λ"). Therefore:

> **Setting `P_λ ≡ 1` recovers `A(K)·tr_M(β_K)` exactly.** Hence `P_λ(K)` is precisely the
> **per-partition deviation of binding from the flat (mass / Markov-trace) distribution**:
> the `P_λ ≡ 1` baseline reproduces the *mass*-side weighting; binding `B(K)` lives entirely
> in the redistribution `P_λ(K) − 1` reweighted by `y_λ χ^λ`.

Two consequences for the GAP-A-3 §4 probe, free and grounded:

1. **A built-in baseline.** Each candidate channel (color/spin/normalisation) should be
   scored **against the `P_λ ≡ 1` flat baseline** `A(K)·tr_M(β_K)` — a channel that does not
   beat flat is not carrying binding structure. (The scope §4 compares to `−B(D)/m_e`
   directly; adding the flat baseline tells you *how much* of the gap the channel closes.)
2. **A bar-symmetry constraint.** The v9 closure symmetrises `χ^λ` with `χ^{λᵀ}` (transpose),
   i.e. it is bar-even (`q↦q⁻¹`). Since `tr_M` itself is the `P_λ≡1` point, any admissible
   `P_λ(K)` must preserve that bar/transpose covariance — a candidate channel whose
   `P_λ` breaks `λ↔λᵀ` symmetry is refuted on paper before scanning.

This reframes GAP-A-3 from "guess a P_λ" to "find the categorical content that reweights the
canonical Markov trace into the binding distribution while staying bar-even" — tying the open
binding gate directly to the canonical-chain Frobenius step.

## 5. Honest blocker — why no probe is run here

The §4 probe is "one cheap sympy/mpmath script per channel," but it still needs the
**canonical `χ^λ(β_D)` at q₀** and the **plethystic content multiplicities** `m_{V}(λ)`
(scope §7: "not yet wired"). The χ^λ infra is the **same blocker as Hoefsmit Stage B** — the
Python `chi_lambda_braid` fallback only supports `q==q_0` and the canonical Markov-trace
projection must not be re-derived in-script (convention drift; Stage-B scope §"Infra
blocker"). Running the probe blind in this sandbox (no `pyhecke_native`, no verified Lean
LSP) would violate "don't iterate compute blind when verification is unavailable." So Stage:
**scoped + structurally sharpened here; the probe is the next step on an infra-enabled
session.**

## 6. Appendix-sync contract (for whoever wires P_λ)

Any Δ_λ / binding wiring change MUST sync, in the same PR
(AGENTS.md §"Mass-and-Binding-Algorithms appendix sync"):

- `appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure` — the Δ_λ closure gate (update the witness contract to name the mechanism)
- `appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding` — the per-isotope binding consumer (Algorithm + Python-API sections)
- `appendix-mass-binding-algorithms/mba-sidecar-lp-sdp-dual-emission` — if any operator-selection LP/SDP is used, emit the full primal+dual contract via `lp_dual_solver.py`

## 7. Cross-references

- [`option-e.md`](../coordination/option-e.md) — master ledger (v1–v9, the (1+q)/2 PROBE 1 refutation)
- [`gap-a3 scope`](2026-06-04-gap-a3-brane-tower-level-selection-scope.md) — the two-layer factorisation + §4 channels
- [`delta-lambda gating context`](2026-05-18-delta-lambda-gating-context.md) — the six original failed ansätze
- [`hoefsmit-stage-b scope`](../scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md) — the shared χ^λ infra blocker
