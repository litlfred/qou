# RT-route research frontiers: W ≈ √2 correction + Habiro-ring unification + Heegaard state-sum

**Date:** 2026-05-24
**Trigger:** Remaining queue items from [PR #1119](https://github.com/litlfred/qou/pull/1119) §"Next round (deferred, research-grade)":
1. Pentagon-coherent Heegaard state-sum at k=9 (~1 week)
2. Habiro-ring unification of real-q_0 and root-of-unity chains
3. W-specific structural correction investigation

This audit synthesizes findings across all three frontiers, with the
**W-correction probe** in this session as the only computational
deliverable. The Habiro and Heegaard topics are documented as
structural framing for future research-grade probes.

## §1. W ≈ √2 correction finding (this session's probe)

Per [`rt_route_w_specific_correction_probe.py`](../../computations/probes/rt_route_w_specific_correction_probe.py):

**Direct-solve** for the multiplicative W-only correction needed to
match SM ratios:

| target | C_W needed |
|---|---:|
| W/Z = cos θ_W = 0.882 | **1.4054** |
| W/H = 0.643 | **1.4570** |
| **average** | **1.4312** |
| Δ between targets | 0.0516 (≈ 3.7%) |

The average **1.43 is very close to √2 = 1.4142** (off by ~1.2%). The
slight inconsistency Δ = 0.0516 is comparable to the existing Z/H ratio
deviation (3.54% from PR #1119) — i.e., the W-correction is consistent
with the same precision as the framework's other torus-chain ratios.

### Structural interpretation candidates

The factor ≈ √2 is suggestive but lacks a clean categorical derivation:

| candidate origin | value | match | comment |
|---|---:|---|---|
| $\sqrt{2}$ (qubit norm) | 1.4142 | within 1% | matches if W's structure has a spinor norm factor |
| $\sqrt{\dim \mathrm{fund}(\mathrm{SU}_q(2))} = \sqrt{[2]_q}$ at $q_0$ | varies (close to 1.43) | very close | $\sqrt{[2]_q}$ at $q_0 \approx 1.11$ is $\sqrt{2.105} \approx 1.451$ |
| $\frac{6}{4}$ (Z/W twist count ratio) | 1.5 | within 5% | naive twist-count adjustment |
| $\cos \theta_W$ inverse = $1/0.882$ | 1.134 | doesn't fit | wrong magnitude |

The **$\sqrt{[2]_q}$ at $q_0$** candidate (1.451) is the most
categorically natural — it's the quantum dimension of the fundamental
SU_q(2) representation, which is exactly what couples to the W's
charge ±1 in any RT-style mass-formula extension.

### Open: derive the W-correction categorically

If the W-correction is $\sqrt{[2]_q}$ specifically, the categorical
chain that supplies this factor involves:
- The W's CHARGED status (Z, H neutral; W± charged)
- The fundamental representation's quantum dimension
- A spinor-like coupling to the substrate

This is a concrete categorical target: derive a formula
$$m_{W^\pm} = m_e \cdot |J_N(T(2,4), q_0)| \cdot \sqrt{[2]_{q_0}} \cdot \text{(other factors)}$$
from first principles, and check whether the prediction matches m_W
within the framework's L1 precision.

## §2. Habiro-ring unification of real-q_0 and root-of-unity chains

The framework currently uses:
- **Real** $q_0 \approx 1.1097$ for the **hyperbolic** chain (VolDensity)
- **Root-of-unity** $q = \exp(\pi i / (k+2))$ for the **torus** chain (RT)

This split is structural, but it raises a foundational question: why
two specializations of the same substrate parameter?

### The Habiro ring (Garoufalidis–Zagier 2024)

The **Habiro ring** is
$$\hat{H} = \varprojlim_n \mathbb{Z}[q, q^{-1}] / ((q; q)_n)$$
where $(q; q)_n = \prod_{j=1}^{n} (1 - q^j)$ is the q-Pochhammer.

Each element $f \in \hat{H}$ has both:
- **Real specializations** at any $q \in (-1, 1) \cup (1, \infty)$
- **Root-of-unity specializations** at $q = \exp(2\pi i / N)$ for any $N$

The Habiro ring of a **number field** $K$ (Garoufalidis–Zagier 2024, arXiv:2310.20308)
extends this to elements with coefficients in $K$, glueing arithmetic
data across both specialization types.

### Connection to QOU framework

**Conjectural unification**: the framework's substrate $q_0$ is the
real specialization of a Habiro-ring element $\widetilde{q_0} \in \hat{H}_K$
for some number field $K$ (likely a cyclotomic field $\mathbb{Q}(\zeta_n)$).
The hyperbolic-chain VolDensity at $q_0$ is the real specialization;
the RT-chain at $\exp(\pi i / (k+2))$ is the root-of-unity specialization.

**Predictions** if this conjecture is right:
1. The "missing W-correction $\sqrt{[2]_q}$ at $q_0$" would equal a
   specific Habiro-ring element evaluated at $q_0$.
2. The RT-level $k = 9$ best-among-naive-candidates (per PR #1119
   scan) corresponds to a specific cyclotomic field index in $\hat{H}_K$.
3. The Borromean Markov-trace closed form $\mathrm{tr}_M = (4+h^2-3h^4-h^6)/(h^2+4)$
   (PR #1081) is the real specialization of a Habiro-ring element;
   its root-of-unity specializations should give the colored Jones
   $J_N(\mathcal{B}_3, q = \exp(2\pi i / N))$.

### Cross-validation test

Compute $\mathrm{tr}_M$ at $q = \exp(2\pi i / N)$ for $N = 2, 3, 4, 5$
and compare to the direct colored Jones $J_N(\mathcal{B}_3)$ at the
same q. If the Habiro-ring conjecture holds, the values should match
exactly (modulo a Habiro-ring normalization).

This is a CHEAP cross-validation (~30 lines) that would directly test
the unification. Queued.

### References

- [Garoufalidis–Zagier, "Knots, perturbative series and quantum modularity"](https://people.mpim-bonn.mpg.de/zagier/files/preprints/KnotsAndQuantumModularity.pdf) — Habiro ring of number field
- [Habiro 2008, "A unified Witten–Reshetikhin–Turaev invariant for integral homology spheres"](https://link.springer.com/article/10.1007/s00222-008-0142-z) — original Habiro-ring construction

## §3. Pentagon-coherent Heegaard state-sum (scaffold)

### Setup

For a torus knot $T(p, q)$, the complement $S^3 \setminus T(p, q)$
admits a **Heegaard splitting** of genus 1 (it's a Seifert-fibered
manifold over $S^2$ with 2 exceptional fibers). The standard splitting:
$$S^3 \setminus T(p, q) = U_1 \cup_{T^2} U_2$$
where $T^2$ is the Heegaard surface (a torus) and $U_1, U_2$ are
genus-1 handlebodies.

### RT state-sum on genus-1 Heegaard

The RT partition function on a closed 3-manifold $M$ with Heegaard
splitting $M = U_1 \cup_{T^2} U_2$ is computed as:
$$Z_k(M) = \sum_{i} \dim_q V_i \cdot \langle \psi_{U_1} | \phi(M) | \psi_{U_2} \rangle$$
where:
- $V_i$ are irreps of $\mathrm{SU}_q(2)$ at level $k$
- $\psi_{U_j}$ are the "vacuum states" of each handlebody
- $\phi(M) \in \mathrm{Maps}(T^2)$ is the gluing element of the
  mapping class group

For the torus knot $T(2, k)$, this state-sum reduces to:
$$Z_k(T(2, k)) = \sum_{j=0}^{k/2} \dim_q V_j \cdot J_{2j+1}(T(2, k), q_k)$$
where $q_k = \exp(\pi i / (k+2))$ and the $\dim_q V_j$ are the quantum
dimensions.

### Pentagon coherence

The Pentagon identity ensures invariance under **Heegaard stabilization**:
gluing a trivial handle to $U_1$ (raising the Heegaard genus from 1 to 2)
should NOT change the partition function. Pentagon coherence at the
6j-symbol level enforces this.

For the torus chain, the Heegaard genus is always 1 (since torus
knots are Seifert-fibered with genus-1 Heegaard splittings); Pentagon
coherence is automatic.

### What this scaffold gives

The **Heegaard state-sum** formulation reproduces the colored Jones
$J_N$ as the SUM over $j = 0, 1/2, \ldots, k/2$ weighted by quantum
dimensions. This is EXACTLY what the [`rt_route_root_of_unity_level_scan.py`](../../computations/rt_route_root_of_unity_level_scan.py)
probe (PR #1119) computes implicitly — the state-sum framing makes
the Pentagon coherence explicit but doesn't add NEW structure.

### What's missing (would resolve the W ratio)

The **Pentagon-coherent Heegaard state-sum** as a categorical
derivation chain does NOT, on its own, supply the $\sqrt{[2]_q}$
factor needed for the W. That factor must come from elsewhere:
- A **2-form** on the Heegaard torus that couples to charged states
- A **Chern-Simons boundary term** for charged 4d theories
- A specific irrep-of-irrep structure (W is in the spinor rep of
  $\mathrm{SU}_q(2)$ tensored with a charge-±1 irrep)

These are research-grade extensions of the RT state-sum, beyond the
scope of a session's compute.

## §4. Synthesis: three layers of the SM mass-derivation chain

Combining this session's findings with prior session results:

```
Layer 1: Hyperbolic VolDensity (PR #1063, #1081, #1100, #1103)
  - Free p, n: structural Markov × 5/2 → +1.948% gap (PR #1081)
  - Multi-nucleon ²H, ³H, ³He: inter-nucleon channel weights
    (PR #1089 sign-flip diagnostic; PR #1102 reconciliation)
  - ⁴He shell binding: absent from framework (PR #1102 §L3)

Layer 2: RT-route for torus knots (PR #1116, #1119, this PR)
  - Z, H ratios validated within ~5% (PR #1119 Z/H = -3.54%)
  - W needs ≈ √2 correction (this PR W-correction probe)
  - RT level k = 9 best naive candidate (PR #1119 scan)
  - Habiro-ring unification with hyperbolic chain (§2, queued)

Layer 3: Pentagon coherence (PR #1100 T2b NEGATIVE; this PR §3)
  - Single-pair Pentagon does NOT give Borromean -3/4 (NEGATIVE)
  - Multi-pair Pentagon does NOT give Borromean -3/4 (NEGATIVE)
  - Heegaard state-sum framing exists but doesn't supply W's √2
  - Habiro cyclotomic expansion (route d in #1081 broad-context)
    is the only known route that completes — Borromean h⁴ = -3/4
    derived via Jones polynomial / Markov-trace closed form
```

## §5. Concrete next-step probes (queued)

1. **Habiro-ring cross-validation** (cheap, ~30 lines): test whether
   $\mathrm{tr}_M(\beta_\mathrm{Bor})$ at $q = \exp(2\pi i / N)$ matches
   the direct $J_N$ colored Jones for $N = 2, 3, 4, 5$.

2. **W = $\sqrt{[2]_q}$ probe** (cheap, ~50 lines): apply the
   conjectured $\sqrt{[2]_{q_0}}$ factor to W's mass formula and
   check whether absolute $m_W$ + W:Z:H ratios both match SM.

3. **Pentagon-coherent Heegaard state-sum at k = 9** (heavy, 1+ weeks):
   compute the full 6j-symbol weighted state-sum and check whether
   the Pentagon-coherent invariant supplies the structural factors
   missing from naive $|J_N|$.

4. **Borromean Habiro element identification** (research-grade): find
   the specific Habiro-ring element whose real specialization is the
   Borromean Markov trace + whose root-of-unity specializations are
   the colored Jones.

## §6. Cross-references

- [`docs/audits/2026-05-24-sm-particle-categorical-map-rt-route.md`](2026-05-24-sm-particle-categorical-map-rt-route.md) — SM particle map (parent)
- [`docs/audits/2026-05-24-rt-level-selection-bring-genus-or-embedding-max.md`](2026-05-24-rt-level-selection-bring-genus-or-embedding-max.md) — level selection (sibling)
- [`docs/audits/2026-05-24-pentagon-identity-broad-context.md`](2026-05-24-pentagon-identity-broad-context.md) — Pentagon's 8 literatures
- [`docs/audits/2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md`](2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md) — L1/L2/L3 framework
- [`computations/probes/rt_route_w_specific_correction_probe.py`](../../computations/probes/rt_route_w_specific_correction_probe.py) — W ≈ √2 finding (this PR)
- [`computations/rt_route_root_of_unity_level_scan.py`](../../computations/rt_route_root_of_unity_level_scan.py) — k=9 best (PR #1119)
- [`computations/rt_route_cross_particle_ratio_quantum_dim.py`](../../computations/rt_route_cross_particle_ratio_quantum_dim.py) — Z/H match (PR #1119)
- [`computations/probes/pentagon_rt_torus_knot_higgs_probe.py`](../../computations/probes/pentagon_rt_torus_knot_higgs_probe.py) — Q2 absolute mass (PR #1116)
- Garoufalidis–Zagier 2310.20308 — Habiro ring of number fields
- Habiro 2008 (Inv. Math.) — original Habiro ring construction
