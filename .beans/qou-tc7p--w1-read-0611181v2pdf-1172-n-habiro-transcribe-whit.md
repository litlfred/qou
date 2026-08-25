---
# qou-tc7p
title: 'W1: read 0611181v2.pdf + 1172-N (Habiro) — transcribe Whitehead single-sum with 4-anchor verification'
status: completed
type: task
priority: normal
created_at: 2026-07-27T02:53:05Z
updated_at: 2026-08-02T08:30:00Z
---

DONE (PR #4400). Sources read in full: `library/arxiv-math-0611181v2/0611181v2.pdf` (van der
Veen, arXiv:math/0611181 v2, all 12 pages via pypdf) and
`library/1172-3/1172-3.pdf` identified as Habiro "On the colored Jones
polynomials of some simple links" (RIMS Kōkyūroku 1172, 10 pages; the
other 1172-N files are L²-torsion / Hikami / WRT papers).

Transcription: `computations/whitehead_vdv_lemma1.py` — BOTH layers:
the generic-t tangle formula (T/B/C, p. 4, with the c+d=1 framing
factor rule) and Lemma 1's Kashaev-point closed forms (b=1 phase sum;
b≥2 single n=M slice for N=2M+1 odd, zero for even N).

All 4 anchors PASSED (`whitehead-vdv-lemma1.witness.json`):
- A1 internal t-form ↔ sin-form: worst rel err 3.5e-19 (b=1,2,3).
- A2 external W_{0,1,1,1} ↔ corpus GL2011/Habiro Borromean: ≤ 1e-41.
- A3 volume rate → 4G: W-link fit err 1.3e-3; b=2 chain err 9.3e-5.
- A4 structural: S_{M,k} > 0; log S_{n,k} = 2(s_{n+k}−s_k)−s_n;
  even-N vanishing; |J| = N^b (Σ_k S_{M,k})^{c+d} for b≥2 N odd.

KEY FINDING for W2 (route selection): for b ≥ 2 chains at odd N the
modulus is EXACTLY the phase-free positive sum N^b (Σ_k S_{M,k})^{c+d}
— fully elementary squeeze territory (1D, single n=M slice, reuses the
S(k)/masterErr bricks). The b=1 Whitehead link proper carries outer
phases χ_{N,n}^{−1} whose non-cancellation is vdV Lemma 4 (Gaussian/
erfc stationary phase) — NOT elementary; will be a cited conditional
class. Same-volume target either way: Vol = 8(c+d)Λ(π/4); c+d=1 ⇒ 4G.
