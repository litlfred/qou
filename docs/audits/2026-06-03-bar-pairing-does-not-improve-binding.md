# The Hecke bar-pairing does not improve binding — the archimedean observation stays |χ(q₀)|

**Date:** 2026-06-03
**Compute:** [`derive_binding_bar_pairing.py`](../../folio-assistant/computations/derive_binding_bar_pairing.py)
→ `derive-binding-bar-pairing.witness.json`
**Status:** DERIVATION (zero fit) — honest NEGATIVE result. Follow-up to the
#1738 modulus → bar/signed cleanup.

## The question

#1738 corrected a non-archimedean misuse: the categorical binding scalar was
`|tr_M_free| − |tr_M_atom|` (archimedean `|·|` applied per-trace before the
difference); it is now the **signed** `Δtr_M`. The general (non-archimedean-
compatible) norm is the Hecke **bar-pairing** `χ^λ(q)·χ^λ(q⁻¹)` (bar-involution
`q ↦ q⁻¹`, defined over any base ring). The natural question — raised by the
author 2026-06-03, *"it might help compute errors"* — is whether realizing the
per-block binding with the bar-LENGTH

    ‖χ^λ‖_bar = √( χ^λ(q₀) · χ^λ(q₀⁻¹) )

instead of the archimedean `|χ^λ(q₀)|` lands closer to AME.

## Result (zero fit) — it does NOT

Deuteron (n = 6, 2.5 s, pure-Python Hoefsmit χ at q₀ and q₀⁻¹, Wenzl y_λ):

| per-block realization | B (MeV) | err vs AME (2.2246) |
|---|---|---|
| **archimedean** `Σ_λ y_λ \|χ^λ(q₀)\|` | 2.304 | **+3.6 %** |
| **bar-length** `Σ_λ y_λ √(χ^λ(q₀)·χ^λ(q₀⁻¹))` | 0.660 | **−70.3 %** |

The archimedean per-block beats the bar-length at the substrate anchor for the
deuteron. (T, n = 9, behind `QOU_BAR_INCLUDE_T=1`, did **not** complete within the
compute budget — χ at both q₀ and q₀⁻¹ over the dim-≤42 Hoefsmit matrices is
minutes-slow in pure Python — so the finding rests on D, which is decisive: a
−70 % vs +3.6 % gap is far beyond any A-dependence. A Rust per-partition χ kernel
would make the T/³He/⁴He confirmation cheap.)

## Why — growth channels (imaginary bar-length)

~half the Wedderburn channels are **growth channels**: `χ^λ(q₀)·χ^λ(q₀⁻¹) < 0`
(deuteron 4/5 free, 5 atom), so the bar-length is genuinely **imaginary** — the
q-Reeb arccosh / hyperbolic regime (cf. `binding_reeb_phase_decomposition.py`).
Taking its magnitude discards that phase. And the bar evaluates `χ^λ` at the
**mirror** point q₀⁻¹, a systematically smaller value than the observation at q₀.

## Conclusion — consistent with #1738, not a reversal

- The **categorical / fibre** convention is correctly **signed/bar**: the trace
  object lives over generic `q`, and the bar `q↦q⁻¹` is its natural involution
  (this is what #1738 fixed, and what the q-usage discipline requires — do not
  assume the real place upstream).
- The **archimedean observation** at the substrate anchor is **`|χ^λ(q₀)|`**,
  *not* the mirror pairing `√(χ(q₀)·χ(q₀⁻¹))`. The +3.6 % archimedean deuteron
  stands; the bar does not "fix" the binding magnitude.

Recorded so a later agent does not naively bar-ify the observation step. The bar
remains the right tool for the **fibre-level** identities (Habiro recursion,
α_EM `[2]_q·(1−h²α)`, the c_k flip-flop fibre framing) — it is the archimedean
**realization** that must stay the modulus, by Im(q₀)=0.
