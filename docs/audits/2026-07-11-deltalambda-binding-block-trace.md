# Track-A binding test: the Δ_λ magnitude is the regular-rep BLOCK trace (dim²), not the irrep (dim)

**Date:** 2026-07-11 · **Axis:** Δ_λ closure (strong sector), binding magnitude ·
**Follows:** g_ρ derivation ([PR #3542](https://github.com/litlfred/qou/pull/3542)) +
magnitude reduction ([PR #3537](https://github.com/litlfred/qou/pull/3537)) ·
**Gate:** Track-A (owner-reversed) · **Tier:** measurement (reuses previous work) ·
**No fit selected; nothing wired.**

## Scope

The owner authorised working the Track-A binding closure. This is a **decisive test**
of the derived Δ_λ against the actual deuteron binding, **reusing previous work** (the
co-Casimir binding witness), plus a **structural lead** for the magnitude. It is **not**
a closure and — critically — **does not select a fitted magnitude** (see Discipline).

Probe [`deltalambda_binding_block_trace_probe.py`](../../computations/deltalambda/deltalambda_binding_block_trace_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-binding-block-trace.witness.json) (4/4).

## Reusing previous work

The co-Casimir witness `computations/rho-k-h3a-co-casimir.witness.json` already carries
`y_λ·χ^λ` per λ⊢6 at the deuteron and the target `−B_D/m_e = −4.35337`, via
`B = Σ_λ (y_λ χ^λ)·Δ_λ`. We plug in the **derived** sign
`sgn(w₀^{S_{λ'}}) = (−1)^{n(λ)}` (#3542, jet-order / fake-degree valuation) with several
magnitude candidates.

## Results

| magnitude | Δ_λ | B / target |
|---|---|---|
| irrep dim | `sgn·dim(λ)` | **0.171** (17%) — **REFUTED** as closure |
| **block dim** | `sgn·dim(λ)²` | **0.909** (91%, classical) |
| block q-dim | `sgn·dim_q(λ)²` | 1.014 (101%, quantum @q₀) |
| mixed | `sgn·dim·dim_q` | 0.960 (96%) |

Two findings:

- **The derived sign is validated in-context.** The irrep-trace sum is `−0.744` — the
  **right sign** and a coherent sum — whereas co-Casimir (a refuted ansatz) gave the
  **wrong sign** `+0.145`. So the jet-order sign derivation (#3542) holds up inside the
  actual binding formula, where the six ansätze failed on sign.
- **The magnitude is the BLOCK trace, not the irrep trace.** `dim(λ)²` is the **Wedderburn
  block dimension** — `V_λ` appears in the regular representation with multiplicity
  `dim(λ)`, so the λ-isotypic component has `dim(λ)²` elements. Thus `Δ_λ = sgn·dim² =
  tr g_ρ over the regular-rep λ-block` (not the bare irrep). It reaches ~91–101%, a **5×
  improvement** over the irrep trace — the right *direction* for the magnitude.

## Q-deformation resolution (by the trace convention, not the 100% match)

The classical-vs-quantum question (`dim²` 91% vs `dim_q²` 101%) is **resolved on
structural grounds**, independent of the target:

- The binding `Δ_λ` is defined as a **quantum Markov trace** — the co-Casimir selector is
  `Δ_λ = tr_M(C_dim_q·1_λ) = 1/dim_q(λ)`, and `dim_q` is manifestly quantum (non-integer:
  5.22, 9.67, …). The weights `y_λ(q₀)`, `χ^λ(q₀)` are also q₀-evaluated. So the **whole
  formula `B = Σ_λ y_λ χ^λ Δ_λ` is a quantum trace.**
- Therefore the block magnitude must be the **quantum** block dimension `dim_q(λ)²`, not
  the classical integer count `dim(λ)²`. Classical `dim²` mixes a classical integer into a
  quantum trace — **convention-inconsistent**. So the trace convention **selects `dim_q²`**
  (101.4%) — *not* because it lands nearest 100% (that would be the gated 7th fit), but
  because it is the only q-consistent block trace.
- **This revises #3537:** its "magnitude is classical (q=1), not q₀" conclusion described
  the **refuted** irrep-trace; the **working** block trace is **quantum**.

## Discipline (STRICT — Δ_λ gate, "Axiomatization is NOT a Proof")

- The q-deformation is resolved by **convention** (quantum `tr_M`), not by fitting to 100%.
  What remains **open** is the **1.45% residual** (higher-body corrections, or the exact
  block-trace form beyond `dim_q²`) — to be **derived, not fitted**.
- **Single-isotope caveat:** this is the deuteron only; `dim_q²` at ~101% could be
  coincidental until cross-checked on ³H / ⁴He (whose binding witnesses would be needed).
- **Nothing wired.** No production `Δ_λ` value proposed. Per "Axiomatization is NOT a
  Proof", a structural argument reaching ~101% is a **lead**, not a completed derivation.

## Net

- **Refuted:** `Δ_λ = sgn·dim` (irrep trace) closes the deuteron — it reaches only 17%.
- **Derived/validated:** the **sign** holds up in the binding formula (right sign, where
  the six ansätze failed).
- **Localized + q-resolved:** the magnitude is the **quantum regular-rep block dimension**
  `dim_q(λ)²` (≈101%) — selected by the quantum `tr_M` trace convention, not by fitting.
  The remaining Track-A step is deriving the **1.45% residual** (higher-body / exact
  block-trace form) and cross-checking beyond the deuteron — not fitting it.

## Cross-references

- g_ρ derivation: [PR #3542](https://github.com/litlfred/qou/pull/3542)
- Magnitude reduction: [PR #3537](https://github.com/litlfred/qou/pull/3537)
- Co-Casimir binding witness (reused): `computations/rho-k-h3a-co-casimir.witness.json`
