# L1 certification complete: all six production atoms at 1 ppQ (⁴He closed)

**Date:** 2026-07-13 · **Branch:** `claude/l1-4he-certified-2026-07-13` ·
**Follow-through of:** the 1 ppQ deep analysis (#3753/#3755, strand c) — the one
remaining L1 gap was ⁴He ("chi-cache partial, no H₁₂; needs the Rust kernel").

## What closed it

The Rust toolchain turned out to be available in this sandbox (cargo 1.94.1), so
`pyhecke-native` 0.9.0 was **built from source** (maturin, release profile) and
installed. With the Geck–Pfeiffer Rust kernel live:

1. `derived_chi_catalogue_sweep.py --max-A 4 --merge-existing` — ⁴He (H₁₂,
   77 partitions of 12) computed in **0.47 s**.
2. `canonical_tr_m_via_chi_cache.py` — the combiner now reports
   **helium-4: 77/77 partitions** (was `partial_cache`), trace
   `0.0553584262667831…` (50 dps).
3. `cross_check_trM_1ppb.py` — full run including the previously
   environment-blocked **χ-engine closed-form anchor: 6/6 matches (worst
   |Δ| = 5.6e-50)**, and

   **atoms compared: 6 · certified 1 ppQ: 6 · uncertified: 0 · divergent: 0.**

   ⁴He upgrades from UNCERTIFIED to **OK**: the two color-weighted exact methods
   (peel + chi-cache) agree exactly; the residual 1.8e-4 vs the Habiro leg is
   the expected color-blind convention gap (informational, not gated).

## Status change

The L1 (compute ≤ 1 ppQ) leg is now **certified across every production atom**
(p, n, D, T, ³He, ⁴He) with the external character anchor live — no float64
anywhere in the hot path. Remaining L1 hardening (optional, defense-in-depth):
a genuinely independent color-weighted third method (color-weighted
Hoefsmit-mpfr), since peel + chi-cache share the `Σ y_λ χ^λ` definition (the
6/6 closed-form anchor covers the χ engine itself).

Downstream unblocked by the kernel build: the A=4 SDP knot-ID feasibility
(B₅/H₁₂ Hecke data now computable in-sandbox — the ⁴He binding-link frontier).

No fits; no wiring; witnesses refreshed by their canonical producers.
