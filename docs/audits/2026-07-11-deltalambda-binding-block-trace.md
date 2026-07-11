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

## Discipline (STRICT — Δ_λ gate, "Axiomatization is NOT a Proof")

- This test **scans** magnitude candidates. `dim_q²` lands at 101.4%, but **selecting it
  because it is nearest 100% would be the gated 7th fit-based ansatz** — so we do **not**.
  `dim²` is structurally motivated (block trace); the **classical-vs-quantum choice**
  (91% vs 101%) and the **residual few-%** are **unresolved** and must be **derived**
  (correct q-deformation of the block trace, higher-body corrections), not fitted.
- **Tension with #3537** flagged, not decided: the magnitude reduction pruned `dim_q` for
  the *irrep* magnitude; the *block* trace may q-deform differently.
- **Nothing wired.** No production Δ_λ value proposed. The scan reaching ~100% is a
  **lead**, not a derivation of the binding.

## Net

- **Refuted:** `Δ_λ = sgn·dim` (irrep trace) closes the deuteron — it reaches only 17%.
- **Derived/validated:** the **sign** holds up in the binding formula (right sign, where
  the six ansätze failed).
- **Localized (open):** the magnitude is the **regular-rep block dimension** `~dim²`
  (~91–101%) — the closure direction. Deriving the exact block magnitude (classical vs
  quantum, residual) — not fitting it — is the remaining Track-A step.

## Cross-references

- g_ρ derivation: [PR #3542](https://github.com/litlfred/qou/pull/3542)
- Magnitude reduction: [PR #3537](https://github.com/litlfred/qou/pull/3537)
- Co-Casimir binding witness (reused): `computations/rho-k-h3a-co-casimir.witness.json`
