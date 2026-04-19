# Why the Kähler series diverges on T / 3He

## The series

The Kähler expansion used in `unified_lift.unified_lift` is

  exp(ℏ_q · θ)(z · V̂)(q)  =  Σ_{k ≥ 0} (ℏ_q^k / k!) · θ^k (z · V̂)(q)

evaluated at q = q₀, where θ := q · d/dq is the Euler operator and
V̂(q) is the symbolic (rational in q) per-generator Wedderburn
volume.  Empirically on D / T / 3He the series diverges on T and
3He from order 1 onward; D converges.

## Why divergence — the near-singularity picture

V̂(q) is built from the partition-sum Markov trace on a Hecke
word.  In the Hoefsmit seminormal basis, the matrix entries of
σ_k involve factors of

  a_ρ(q)  :=  h(q) / (1 − q^{−2 ρ})

where ρ = c_T(k+1) − c_T(k) is the content difference between
adjacent entries in an SYT T.  The denominator 1 − q^{−2 ρ}
vanishes at q^{2 ρ} = 1, i.e., at q = exp(π i m / ρ) for integer
m — these are 2ρ-th roots of unity on the unit circle.

At q₀ = 1.11 (real, close to 1), the nearest root of unity to q₀
is at distance O(|1 − q₀|) = O(0.1) for small ρ.  For ρ = 1 the
nearest is at q = ±1 (distance ≈ 0.11 to q₀).  For ρ = 2 at
q = ±1, ±i (distance ≈ 1.49 to q₀).

The radius of convergence of the Taylor series of V̂(q) at q₀
is bounded BELOW the nearest complex singularity.  Since the
Euler operator θ = q d/dq acting through ℏ_q steps corresponds
to a translation by factor ~exp(ℏ_q) ≈ 1.10 in q, the series
probes the region |q − q₀| ≲ ℏ_q · q₀ ≈ 0.11.

**That radius already touches the ρ = 1 singularities.**

## Why D converges but T and 3He don't

The set of ρ values contributing to V̂(q) depends on the SYT
contents of partitions of n = 3A:

- **D (A = 2, n = 6):** partitions include (6), (5,1), (4,2),
  (4,1,1), (3,3), (3,2,1), (3,1,1,1), (2,2,2), (2,2,1,1),
  (2,1,1,1,1), (1⁶).  Content differences ρ ∈ {−5, −4, …, +5}.
  Crucially, the Wedderburn weights w_λ = d_q(λ)² / [n]_q!  down-
  weight the high-dimensional partitions; the partitions with
  problematic ρ = 1 singularities (e.g., (3,2,1) with dim 16,
  contents spanning −2…+2) have small w_λ relative to the
  dominant (6) and (1⁶) which have only ρ = ±5 singularities
  well OUTSIDE the ℏ_q disk.

- **T / 3He (A = 3, n = 9):** partitions up to (9), (1⁹), with
  dominant weight on (3,3,3) and (3,2,1,1,1,1) — partitions with
  ρ = 1 singularities at HIGH multiplicity.  These partitions'
  Taylor coefficients θ^k V̂^λ(q₀) grow factorially because of the
  (q^{2·1} − 1)^{−k}-like behaviour in the k-th derivative.  The
  Plancherel weight w_λ doesn't kill this growth.

For D the fraction of weight on high-ρ-density partitions is small;
for T/3He it's dominant.  Hence D converges, T/3He diverge.

## Empirical data (session unified-lift.witness.json)

| Order | D err   | T err   | 3He err |
|------:|--------:|--------:|--------:|
| 0     | 0.0038% | 0.0301% | 0.0035% |
| 1     | 0.0208% | 0.7783% | 0.8303% |
| 2     | 0.0232% | 3.0306% | 3.4976% |
| 3     | 0.0228% | 4.5523% | 6.0016% |
| 4     | 0.0227% | 5.1090% | 6.9554% |
| 5     | 0.0226% | 5.2424% | 7.2026% |

(Post 1·σ₀ gluon patch — pre-patch numbers were similar divergence.)

D converges to ~0.023% after order 2.  T / 3He blow up to
~5–7% monotonically.

## Iterative / partition-indexed reformulation (Candidate 4)

Instead of computing V̂ = Σ_λ w_λ V̂^λ and then Kähler-lifting the
scalar, carry the partition index through:

  V̂^λ(q)  (rational in q, per-partition)
     ↓
  Kähler-lift V̂^λ(q)  =  exp(ℏ_q · θ) V̂^λ(q)  per partition
     ↓
  Sum over λ:  V̂^K(q₀) = Σ_λ w_λ · V̂^λ_Kähler(q₀)

At per-partition level the divergence becomes visible: partitions
with ρ = 1 in their content set produce divergent Kähler series;
partitions without produce convergent ones.

**Iterative strategy:**

1. For each partition λ ⊢ n, compute V̂^λ(q) symbolically (rational
   in q) via the seminormal Markov trace on the braid word.
2. Determine the radius of convergence R_λ of the Taylor series of
   V̂^λ at q₀ — estimated by the nearest (q^{2ρ} − 1) = 0
   singularity where ρ appears in SYT(λ).
3. Kähler-lift per partition:
     - If R_λ > ℏ_q · q₀: evaluate exp(ℏ_q · θ) V̂^λ directly.
     - If R_λ ≤ ℏ_q · q₀: series diverges — use alternative
       (e.g., evaluate V̂^λ at the SHIFTED point q₀ · exp(ℏ_q)
       directly, bypassing the Taylor series).
4. Sum over λ with Plancherel weight.

**Benefit.** Each partition's convergence is self-contained; we no
longer apply one-size-fits-all Kähler order.  Partitions whose
Taylor series converges get the accuracy of high-order Kähler;
partitions whose series diverges fall back to direct evaluation
at the shifted q.

**Cost.** Symbolic V̂^λ(q) per partition is expensive.  For n = 9
the 30 partitions each require a symbolic seminormal trace; this
was already the bottleneck for `binding_canonical` (see session
log — canonical symbolic path is ~145 s on D).  Doing it per
partition over a pre-computed Kähler series cache could amortise.

**Alternative (cheaper):** Borel resummation (Candidate 5).  The
divergent series Σ a_k t^k / k! has Borel transform B(t) = Σ a_k t^k.
If B is analytic in a sector and has polynomial growth, then

  S(ℏ_q)  =  ∫_0^∞ e^{−t/ℏ_q} B(t) dt

is the **Borel sum** — finite even when the original series diverges.
For the Kähler expansion, Borel summability requires that |θ^k V̂|
grows no faster than k! × (1/R)^k with R > 0.  Empirically on T/3He,
θ^k V̂ grows like (k!)^α · (1/ℏ_q)^k with α ~ 1; Borel sum is
typically tractable for α ≤ 1 (Gevrey-1).

**Session decision:** both Candidate 4 (iterative per-partition
Kähler) and Candidate 5 (Borel sum) are research-open.  The
iterative Candidate 4 is more concrete (simpler to implement,
diagnostic even if not an optimiser); Candidate 5 is the deeper
fix but requires Gevrey class estimates.

## Connection to the 1·σ₀ patch

The 1·σ₀ gluon patch (commit b607e3e) dropped the Kähler-order-0
error on D from 0.018% to 0.0038%.  It does NOT fix the Kähler
divergence on T/3He — the divergence is about the ANALYTIC
structure of V̂(q) near q₀, not about the gluon count.  However,
with a better V̂ baseline, the divergence tails shown above MAY
be less aggressive (session order-1 T err with 2·σ₀ was 0.78%;
with 1·σ₀ it's 0.78% … actually unchanged — the post-patch
divergence kinematics are above: order 1 on T still goes to 0.78%
because the divergence is in the analytic structure, not the
constant).

The gluon patch and the Kähler-series control are orthogonal
levers.
