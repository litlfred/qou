# The canonical binding is INTENSIVE; A≥3 needs an EXTENSIVE term — a zero-fit derivation

**Date:** 2026-06-02
**Derivation:** [`derive_binding_per_block_archimedean.py`](../../computations/derive_binding_per_block_archimedean.py)
→ `derive-binding-per-block-archimedean.witness.json`
**Status:** DERIVATION (zero fitted parameters). Reframes the Δ_λ gate.

## Why this exists

A session of *probes* tested guessed per-block weights `Δ_λ` against AME binding —
i.e. **fitting**, the antipattern the 3-calibration discipline forbids. Stepping
back: the canonical binding formula (`binding_canonical.py`) is

$$B(K) = E_0\,\bigl(|\mathrm{tr}_M(W_{\text{free}})| - |\mathrm{tr}_M(W_{\text{atom}})|\bigr),
\qquad \mathrm{tr}_M = \sum_\lambda y_\lambda \chi^\lambda,$$

with `E_0` a **calibration-fixed** scale (`𝔈₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV`, or
`Q_β = 0.782 MeV`). This is a **derivation** — `y_λ` (Wenzl), `χ^λ` (Hoefsmit),
`E_0` (calibration); **zero free parameters**. We evaluate it (and its
"observe-per-block" form `E_0·Σ_λ y_λ(|χ^λ_free|−|χ^λ_atom|)`) directly.

## Result (zero fit)

| isotope | derived per-block (`𝔈₀`) | err | AME |
|---|---|---|---|
| D | 2.304 | **+3.6 %** | 2.225 |
| T | 3.253 | −61.7 % | 8.482 |
| ³He | 3.467 | −55.1 % | 7.718 |
| ⁴He | 3.804 | −86.6 % | 28.296 |
| **A-growth B(⁴He)/B(D)** | **1.65** | — | **12.72** |

- **The deuteron is genuinely derived: +3.6 %, no fit.** "Observe-per-block"
  (`Σ|·|`) beats "collapse-first" (`|Σ·|`) there (+3.6 % vs +12.0 %), confirming
  the *preserve-information-until-observation* principle at A=2.
- **A≥3 collapses.** The derived binding is **nearly A-independent**
  (1.65× growth vs the required 12.72×). It saturates at ~3–4 MeV.

## The reframing — intensive vs extensive

`B = E_0·Δtr_M` is an **intensive** observable: `|tr_M|` is a bounded trace,
and its free−atom difference saturates (~3–4 MeV) — it does **not** scale with
mass number. **Nuclear binding is extensive** (`B ∝ A` to leading order). So the
canonical formula is **structurally missing the extensive / additive term** —
the per-bond / per-nucleon-pair part of nuclear binding (the JSJ /
inter-nucleon-channel sum).

**Consequence for the Δ_λ programme.** No per-block *weight* `Δ_λ` can convert an
intensive quantity into an extensive one — a re-weighting of a saturating trace
difference still saturates. This is **why every Δ_λ ansatz (the six failed ones
+ this session's probes) failed**, and why probing was the wrong tool: they were
searching for a density to multiply an intensive carrier, when the missing
object is an **additive extensive term**, not a multiplicative weight.

- ✅ The intensive part (deuteron, the single inter-nucleon bond) **is derived**
  to +3.6 %.
- 🔴 The extensive part (A≥3, the sum over bonds/pairs) is **absent from the
  canonical trace-difference formula** — it is the genuine missing structure.

## The corrected target (derive, not fit)

A≥3 binding needs a **derived extensive term**: an additive sum over the
inter-nucleon channels of the canonical braid (each bond an intensive
`E_0·Δtr_M`-like contribution), i.e. `B(K) = Σ_{bonds b} B_b` where each `B_b`
is the derived single-bond binding. This is the **operator-valued / per-bond**
structure — consistent with the cheat-sheet §9 "operator-valued combiner"
(#1698) and the `bowtie ⨝_K` inter-nucleon channel decomposition — and it is a
**derivation** (sum the derived bond bindings), not a weight-fit. The deuteron
(one bond) being derived to +3.6 % is the per-bond base case; A≥3 is its additive
extension over the JSJ/bowtie channels.

**Net:** the Δ_λ gate is mis-framed as "find the per-block density." The zero-fit
derivation shows the real gap is **the extensive (additive-over-bonds) term**,
with the per-bond intensive piece already derived (deuteron +3.6 %). Stop
fitting weights; derive the per-bond sum. Cross-ref the inter-nucleon-channel
content blocks (`bowtie`, `inter-nucleon-channel-color-tube`).
