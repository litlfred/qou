# TL₁₈ / N=7 cable engine — design note (feasibility, no build)

Status: design-only. The certified categorical q\*-test ladder stands at
N = 3, 4, 5, 6 (merged #3927, #4032, #4034-via-#4078, #4078). The N=7
rung needs J'₇ of 5₂ via the Jones–Wenzl 6-cable on **TL₁₈**:
Catalan(18) = **477 638 700** basis diagrams — 49.3× the TL₁₅ state
space that the current engines handle.

## Why the current design does not extend

Both merged engines (`tl_cable` dense-f64, `tl_cable_mpfr` MPFR-192)
precompute per-generator right-multiplication tables:

| item | TL₁₅ (N=6) | TL₁₈ (N=7) |
|---|---|---|
| basis diagrams | 9 694 845 | 477 638 700 |
| packed tables (17 gens × u32) | 543 MB (14 gens) | **32.5 GB** |
| index map (u64 → u32) | ~0.4 GB | **~19 GB** |
| one dense MPFR-192 vector | ~0.5 GB | **~27 GB** |
| one dense f64 vector | 78 MB | 3.8 GB |

MPFR is out on a 16 GB box on the vector alone; even dense-f64 dies on
the tables + index map. Also u32 indices overflow nothing (477M < 2³¹)
but the LP-bit packing must move to bit 31 of u32 (still fine).

## Candidate designs

1. **On-the-fly composition + f64 vectors** (minimal change): drop the
   tables; apply the specialized `mul_u` rule per (diagram, generator)
   per transfer step, using the Dyck-mask codec. Costs a decode +
   re-encode + index lookup per entry per generator (~100–200 ns) —
   ~50–100 s per generator application single-thread, ×~450 gen-apps
   ≈ 6–12 h/eval before rayon (÷4 → 1.5–3 h/eval, ~9 evals ≈ days).
   Index map still needs ~19 GB unless replaced by **rank/unrank**
   (Dyck-word ranking is a classical O(n) combinatorial bijection —
   eliminates the hash map entirely; needs a small precomputed ballot
   table). Memory then: 2 f64 vectors ≈ 7.6 GB — fits. Precision:
   f64-grade gates only (~1e-8), plus a double-double variant (~1e-30,
   2× memory, ~3× time) if a certified rung is wanted.

2. **Plat / half-diagram basis** (the right long-term object): the
   Markov closure of the cable braid can be computed in the TL
   **cup-basis** (link-pattern) representation of dimension
   Catalan(9) = 4862 per side… but the closure trace over the full
   algebra needs all through-strand sectors: Σ_k (irreducible sector
   dims)². The transfer in the plat basis for a *closure* (not plat)
   still requires the full bilinear pairing — effectively the same
   state space unless the trace is decomposed per Jones–Wenzl sector:
   tr = Σ_λ [weights]·tr_λ, with each sector matrix of dimension
   ≤ dim V_λ(TL₁₈) ≈ ≤ 4.5M. Sector-wise transfer cuts memory ~10×
   and parallelizes per sector — the clean design, but needs the
   TL-sector projectors implemented (Wenzl towers per through-strand
   count) and validated against N ≤ 6.

3. **Modular / CRT integer evaluation** (exact route): evaluate J' at
   rational q = p/q as exact rationals via CRT over ~64-bit primes
   (the hecke-engine `v10_crt` pattern). Removes precision cost per
   limb but the state space is unchanged — combine with (1)'s
   rank/unrank.

## Recommendation

Design 1 + Dyck rank/unrank + double-double is the pragmatic rung
(days of compute, ~8 GB); design 2 (sector decomposition) is the
principled engine if the ladder is to continue past N=7. Neither is
session-sized; park as a bean until the N-ladder's marginal value at
N=7 justifies the spend (the capstone constraint already fails on four
certified faces).

Bean: `qou-69pr` follow-up (N=7 rung). No build scheduled.
