# Reflection-rep closed form, tr-decay, and symmetry — what is proved, measured, and open

**Date:** 2026-08-30
**Directives (owner):** try proving `tr(ρ_λ Ω₂)` decays with `b(λ)`; explore
representation stability as the framework for closed forms + the bound; can the
q̄-involution / S₃, S₅ actions cut the compute in half; prove what you can, then
optimize.

## 1. Rigorous facts (proved)

- **`tr(Ω₂_λ) = 0` for every λ** (the control). `Ω₂ = ½Σ[A_a,A_b]` is a sum of
  commutators; `tr` of a commutator vanishes by cyclicity. This is asserted and
  passes in every probe run. (It is why `tr(ρ_λ Ω₂_λ)` is a *cancellation*, which
  is what makes fat partitions small — §3.)
- **`tr(ρ_{(n)} Ω₂) = 0`** (trivial rep, `b=0`). On the 1-dim trivial rep each
  `σ_g` acts as the scalar `q`, so `A_g = q·∂_q(q)·q⁻¹ = 1` (scalar), all
  commutators vanish, `Ω₂ = 0`. Matches the measured `b=0 → 0`.
- **Reflection-rep sign, A=2..13: `tr(ρ_{(n-1,1)} Ω₂) < 0` for every A tested.**
  Measured (dim `3A-1`, exact mpf). This is the dominant term (§4 of the growth
  audit), so the negative sign of `P(A)` is carried by a term that is negative at
  every A through A=13. (Proof for *all* A is open — see §2.)

## 2. 🛑 Closed form — numerical hunt INCONCLUSIVE (a retracted over-claim)

Reflection-rep `tr(ρ_{(n-1,1)} Ω₂)`, A=2..13:

```
 -337.95, -2271.09, -12210.78, -58915.24, -266114.43, -1149199.90,
 -4803499.73, -19589226.89, -78371733.14, ... (A=11,12,13 continue negative)
```

Inter-A ratios: 6.72, 5.38, 4.82, 4.52, 4.32, 4.18, 4.08, **4.001**, 3.94, 3.89,
**3.85** — monotonically decreasing, **still drifting at A=13**.

**Earlier I reported "base = 4, coefficient ≈ −74.7." That is RETRACTED.** It was a
transient: `tr/4^A` rises to −74.74 at A≈9–10 then *falls back* (−73.6, −71.6,
−69.0 at A=13), and the ratio passes *through* 4 on its way down. Nine points
looked converged; thirteen show it was not. **The growth base is < 4 and not
numerically resolved; there is no clean closed form from fitting.** Lesson: this
sequence converges too slowly to guess a closed form — a closed form must be
**derived** (the reflection rep is concrete: `σ_g` on the `(3A−1)`-dim standard
rep is explicit, and the germ `A_g` is its log-derivative), not fitted. That
derivation is the open C2 target; the A=2..13 data is the resource for it.

## 3. Proving `tr(ρ_λ Ω₂)` decays with `b(λ)` — strategy and status (OPEN)

The measured decay (growth audit §1) is real but **not proved**. The obstruction
and the route:

- The naive bound `|tr(ρ_λ Ω₂_λ)| ≤ q^L·dim_λ` is uselessly loose — it gives the
  non-decaying 0.5 tail (growth audit §2). The decay is a **trace cancellation**
  (`tr(Ω₂)=0`), not a norm effect.
- **Route (Kerov–Olshanski / shifted-symmetric functions).** The normalised trace
  `tr(ρ_λ X)/dim_λ` for a fixed algebra element `X` is a *shifted-symmetric
  function* of λ of degree bounded by the "content-degree" of `X`. `Ω₂` is built
  from germs (log-derivatives of generators) of bounded degree, so
  `tr(ρ_λ Ω₂_λ)/dim_λ` should be a bounded-degree polynomial in the content
  power-sums of λ. A bounded-degree shifted-symmetric function, evaluated on λ
  with `λ₁ = n−b`, is controlled by its top-degree part; the traceless-ness of
  `Ω₂` should kill the leading pieces that would otherwise grow with `b`. Making
  this precise (identifying the degree and proving the leading cancellation) is
  the concrete open problem — and it is exactly a **cluster/cumulant** statement,
  matching the ingested Procacci–Yuhjtman / Rebenko papers.
- **What is proved toward it:** the two base cases (§1) and the empirical decay
  rate (~0.1 per `b`-level at low `b`). The general theorem is **open**.

## 4. Representation stability (the framework) — status

The opposite-trend evidence (growth audit §3) points at FI-stability: `|tr|/dim`
decays more steeply with `b` as A grows. The clean stability statement would be
that, organised by the *below-first-row shape* `μ` (so `λ = (n−|μ|, μ)`), the
normalised contribution converges as `n→∞` to a limit depending only on `μ`.
**Caveat measured here:** the underlying object is *not* a fixed element — the
word `ρ` and `Ω₂` grow with A (12A−1 crossings) — so this is a *family* stability,
subtler than textbook FI-stability, and the slow, non-converged reflection-rep
base (§2) shows the limit is approached slowly. Establishing the stability (and
its rate) is the same open problem as §3, from the representation side.

## 5. q̄-involution and S₃ / Sᵤ symmetries — can they halve the compute?

- **q̄ (bar) involution `q ↔ q⁻¹`: does NOT halve the partition sum.** Its
  λ-level manifestation is the transpose `λ ↔ λ′`, and transpose covariance of
  `tr(ρ_λ Ω₂_λ)` was **measured and REFUTED** (14/14 conjugate pairs, no ±1
  relation; prior audit). The specific braid-word density ρ breaks it. So no
  factor-2 from bar/transpose at the partition level.
- **Palindrome / braid-reversal (Z=N nuclei).** The Markov trace is reversal-
  invariant, and for Z=N words (²H, ⁴He, ⁶Li…) the proton/neutron blocks give the
  word a p↔n exchange symmetry. This is a genuine symmetry of ρ that could halve
  the *distinct* commutator/trace work for those nuclei — **untested here**;
  worth a measured check before relying on it.
- **S₃ (nucleon-internal) and `S_Z × S_N` (nucleon-permutation).** Each nucleon is
  3 strands (an S₃ block); the A nucleons split into Z protons and N neutrons,
  and the word is built from shifted copies, so `S_Z × S_N` permutes identical
  blocks. In the **branching tower** (steps 1–3, on main) these are symmetries of
  the transfer-matrix chain — repeated identical local tensors — so they reduce
  the tower's work (compute a nucleon tensor once, reuse it), not the flat sum.
  This is the right place to exploit them and is a **step-4 optimisation**, not a
  standalone halving.

## 6. Honest bottom line

- **Proved:** `tr(Ω₂)=0`; trivial-rep vanishing; reflection-rep negative through
  A=13 (the sign's leading term).
- **Retracted:** the "base 4 / C≈−74.7" closed form (transient; not converged).
- **Open (the real targets):** the `tr`-decay-with-`b` theorem (§3, via
  Kerov–Olshanski + traceless cancellation ≈ cluster expansion) and the
  reflection-rep closed form (§2, needs derivation). Both are representation-
  stability statements.
- **Symmetry for compute:** bar/transpose gives nothing (refuted); the real
  savings are the `S_Z×S_N` / S₃ block symmetries inside the tower (step-4), plus
  the mpfr 4× — constant/structural, not a partition-halving.
