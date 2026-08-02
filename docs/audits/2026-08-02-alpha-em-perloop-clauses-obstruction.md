# α_EM per-loop measure: Clause B derived, Clause A conditional, one open wall (2026-08-02)

Branch `claude/q-deformed-saddle-offsets-bdn992` (PR #4598). Resolves bean qou-5et6
(option C — the one genuinely-open *derivation* lever from the close-1ppq survey). This
is the least-negative of the session's findings: real derivation, one precise open wall.

## Answer

Neither clause is flatly open or closed. The corpus has already refactored both onto a
single shared hypothesis (the "B2" τ-lift), which is **genuinely open with a named
structural obstruction** — and the derivation **imports no CODATA α_em** (verified
grep-clean + numerically α_em-insensitive at 0.007 ppm).

## Clause B — channel count = 2: genuinely DERIVED (and it is the *right* 2)

The quadratic Hecke relation `(σ−q)(σ+q⁻¹)=0` splits H₂(q) into **exactly two**
idempotents `e₊=(σ+q⁻¹)/[2]_q`, `e₋=(q−σ)/[2]_q` (`e₊+e₋=1`, `e₊e₋=0`,
`σ=q·e₊−q⁻¹·e₋`) — sympy-proved + sorry-free Lean `channel_count_2_…`. This "2" is the
dim of the fundamental Hecke rep / #eigenvalue channels of the braid generator — it is
*why* the framework has a q-deformed skein at all. **Adversarial check passed:** this is
NOT the treacherous "2" that masqueraded as derived four times this session (nucleon
types, bar-parity, isospin, exchange-spectrum). It is categorically load-bearing and
real. (Separately, the `½` in `measure = ½·a₀` is NOT the channel *weights* — those are
`(q²/(q²−1), −1/(q²−1)) = (5.31, −4.31)` at q₀, equal only at q²=−1.)

## Clause A — a₀ = 1/4π: DERIVED as spectral geometry, CONDITIONAL as a per-loop id

The per-mode heat-kernel weight `a₀ = 1/(4π)` (leading Seeley–DeWitt coefficient,
Gauss–Bonnet form) is machine-verified metric-independent
(`Tr e^{tΔ}·(4πt)/Area → 1` to ≤1e-6 across square/hex/skew/9:1 metrics). That a₀ *exists
and equals 1/4π* is textbook. What is conjectural: that **this** a₀ weights **this** loop
tower — which needs the loop mode-space to inherit the conformal class, i.e. the B2 lift.

## The single open wall: the B2 τ-functor lift (the honest core)

Both clauses collapse to one hypothesis: "the τ-functor carries the fibre reality
structure ρ (q↦q̄) to the Hodge conjugation of H¹(Bring)." Mapping the involutions
through the nome q = e^{2πiτ} reveals a **precise structural obstruction**:

| q-involution | modular image | analytic type |
|---|---|---|
| bar `q↦q⁻¹` | `τ↦−τ` | holomorphic |
| channel-swap `q↦−q⁻¹` | `τ↦½−τ` | **holomorphic** |
| Hodge conjugation `H^{1,0}↔H^{0,1}` | `τ↦−τ̄` | **ANTI-holomorphic** |

A holomorphic τ-functor **cannot** identify the (holomorphic) Hecke channel-swap with
(anti-holomorphic) Hodge conjugation — an analytic-type mismatch. The anti-holomorphic
conjugation has to enter through the *fibre's* complex structure (the Im(q)
fibre-vs-observable distinction), i.e. through the unproved categorical→archimedean
τ-dictionary. **That dictionary is the open, multi-week input.** This is a genuine
"conditional-proved ≠ premise-established": the §3b conjecture-class scaffold exists
(Lean-locked), the premise is not derived (milestone `qou-b5qg` still todo).

## Anti-fit + payoff reality check

- **No CODATA α_em imported** — grep-clean (no `137`/`codata` in the measure-chain
  probes) AND numerically α_em-insensitive: swapping CODATA→derived α inside the measure
  term moves the total by **0.007 ppm**. Not circular.
- **Payoff is a last-correction, not a ppq win.** Even with A+B fully derived, the α_EM
  tower still misses CODATA by **−8.4 ppm** (residual = the deferred genus-4
  polarized-Epstein determinant, #3911). Closing A+B de-loads the dilog conjecture and
  would feed a derived α into m_K/m_π (Roast 1) — it does **not** by itself reach
  ppq/ppb L2 accuracy.

## Correction to Roast 1 (this session's own error)

The α_EM agent's normalization check exposed an error in
`2026-08-02-ppq-attack-vectors-roast.md` §Roast 1: the "derived α_em⁻¹ ≈ 609 → −157,000
ppb" figure used a wrong `ℏ_q²` numerator instead of the skein amplitude `(q−q⁻¹)²`. The
**correct** production derived α_em⁻¹ = `q·[9]_q·[10]_q` = **136.82** (−1553 ppm from
CODATA). With that, m_K/m_π degrades from ~47 ppb (experimental α_em) to **~363 ppb**
(derived) — ~8×, not four orders. Roast 1's *conclusion* (m_K/m_π's 100×-passing
precision is α_em-anchored, not parameter-free) **survives**; the magnitude was
overstated and is now corrected in that audit + bean qou-5ipv.

## Net

Option C is the session's one partial-positive: **Clause B's channel count = 2 is a
genuine derivation** (the real dim-2 Hecke split, not the false "2"), and Clause A's
a₀ = 1/4π is real spectral geometry. Both are gated on a **single, precisely-localized,
genuinely-open** obstruction — the holomorphic-vs-anti-holomorphic τ-lift — which no fit
can close. That is the honest state: not blocked-and-hopeless, not closed; one named wall.
