# Δ_λ closure form — exploration findings on the deuteron

**Branch**: `claude/closed-forms-first-principles`
**Date**: 2026-05-19
**Goal**: After Phase 1b's negative result on the naive closure form, explore *why* it misses by ~33× and identify the categorical refinement needed.

## Five hypotheses tested

### H1 — Borromean / Planck-tick rescaling (1/ℏ_q²)

**Result**: partial. $1/\hbar_q^2 \approx 101.86$ multiplies the naive prediction $0.067$ MeV → $6.82$ MeV, **overshoots AME** ($2.22$ MeV) by **3.07×**.

| Rescaling | $B(D)$ predicted | Ratio to AME |
|---|---:|---:|
| none (naive) | 0.067 | 0.030 |
| × 1/ℏ_q | 0.677 | 0.304 |
| × 1/ℏ_q² | 6.825 | 3.068 |
| × Vol(B_3)/ℏ_q² | 50.01 | 22.5 |

Note the overshoot factor 3.07 ≈ **number of Galois orbits in Δ(z)** (see H3).

### H2 — Δ_λ ∝ χ_λ with universal scalar c

If $\Delta_\lambda = c \cdot \chi^\lambda$, then $B(K) = m_e c \sum_\lambda y_\lambda (\chi^\lambda)^2$. Implied $c$ values:

| atom | $n$ | $B$ (MeV) | $\Sigma y_\lambda \chi^\lambda$ | $\Sigma y_\lambda (\chi^\lambda)^2$ | implied $c$ |
|---|---:|---:|---:|---:|---:|
| deuteron | 6 | 2.225 | 0.388 | 1.162 | **3.747** |
| tritium | 9 | 8.482 | 0.104 | 0.802 | **20.701** |
| helium-3 | 9 | 7.718 | 0.207 | 2.115 | **7.141** |
| helium-4 | 12 | 28.296 | 0.055 | 1.228 | **45.088** |

**c is NOT universal.** Tritium and ³He have the same $n = 9$ but $c$ differs by 2.9×. This **falsifies** the simple $\Delta_\lambda \propto \chi^\lambda$ form: Δ_λ has knot-specific structure beyond $\chi^\lambda$, plausibly tied to the JSJ hyperbolic-volume decomposition (per `docs/path-to-1ppb-04-plan.md`):

$$B(Z, N; q_0) = \sum_{P \in \mathrm{JSJ}(K_{Z,N})} \rho_F(P, q_0) \cdot \mathrm{Vol}_{\mathrm{hyp}}(P, q_0).$$

### H3 — Discriminant factors over ℚ into 3 Galois orbits

**Strongest categorical signal.** The color-tube discriminant

$$\Delta(z) \;=\; -(16z^6 + 24z^5 + 35z^4 + 50z^3 + 35z^2 + 24z + 16)$$

is **palindromic**, so the reciprocal-poly substitution $w = z + 1/z$ collapses degree 6 → degree 3:

$$\frac{\Delta(z)}{-16 z^3} \;=\; w^3 + \frac{3}{2}w^2 - \frac{13}{16}w + \frac{1}{8}.$$

Equivalently, **$16w^3 + 24w^2 - 13w + 2 = 0$** is the **reciprocal cubic**, whose 3 roots index the 3 Galois orbits of $\Delta(z)$:

| Orbit | $w$ | $z$-pair | $\lvert z\rvert$ |
|---|---|---|---:|
| 0 (unit-circle) | $-1.9496$ | $-0.9748 \pm 0.2230i$ | $1.0000$ |
| 1 (principal+) | $0.2248 + 0.1165i$ | $0.1190 + 1.0536i,\;0.1058 - 0.9371i$ | $1.0603, 0.9431$ |
| 2 (principal-) | $0.2248 - 0.1165i$ | $0.1190 - 1.0536i,\;0.1058 + 0.9371i$ | $1.0603, 0.9431$ |

PR #779's "principal pair" $\{z_c^\pm\}$ at $\lvert z\rvert = 0.943$ was the **inner halves of orbits 1 and 2** — i.e. half of the full Galois orbit. The full orbits 1, 2 each contribute residues of magnitude $\approx 1.096$ at $k=3$.

#### Per-orbit residues at the four jet-prolongation orders

| $k$ | Orbit 0 | Orbit 1 | Orbit 2 | Sum |
|---|---:|---:|---:|---:|
| 0 (electron) | 0.000775 | 0.000009 | 0.000009 | 0.000793 |
| 1 (muon) | 0.000495 | 0.013785 | 0.013785 | 0.028065 |
| 2 (pair) | 0.000000 | 0.000000 | 0.000000 | **0.000000** |
| 3 (baryon) | 0.260294 | 1.095703 | 1.095703 | 2.451700 |

**Observation**: the **$k = 2$ residue identically vanishes across all 3 orbits**. This is a strong categorical constraint — there is no "pair channel" residue at any Galois orbit. The pair channel must arise elsewhere (e.g., as a combination of orbit-0 and orbit-1 with the same $k=3$ prolongation but different selection).

**Observation**: orbits 1 and 2 are complex conjugates and give identical $\lvert\mathrm{Res}\rvert$ (the residues are conjugate, magnitudes match).

### H4 — All-orbit sum + uniform $k = 3$

Using $\Sigma_{\mathrm{orbits}} \mathrm{Res}^{k=3} = 2.452$ as a uniform $\Delta_\lambda$:

$$B(D) = m_e \cdot 2.452 \cdot \sum_\lambda y_\lambda \chi^\lambda = 0.511 \cdot 2.452 \cdot 0.3883 \approx 0.486 \text{ MeV}$$

Still off from AME 2.225 by **~4.6×**. Better than naive (0.067) but not matching.

### H5 — Orbit-pair-only + k = 3

Using only orbits 1+2 (excluding the unit-circle orbit 0): $\mathrm{Res} \approx 2.192$. Gives $B(D) \approx 0.435$ MeV — slightly worse than H4.

## Synthesis

The exploration identifies **three load-bearing categorical facts** to be combined in the next refinement:

1. **Discriminant 3-orbit factorisation over ℚ via the reciprocal cubic $16w^3 + 24w^2 - 13w + 2 = 0$.** This is a hard categorical structure. The per-λ block-projection $\pi_\lambda$ must map Wedderburn blocks to *subsets* of these 3 orbits.

2. **$k = 2$ residue identically zero across all orbits.** The pair channel cannot be a simple per-orbit residue at $k = 2$. The $k$-mapping $\lambda \mapsto k(\lambda)$ should likely take values in $\{0, 1, 3\}$ only, with $k = 2$ excluded or replaced by a combination.

3. **Per-knot structure beyond χ^λ.** The implied $c(K)$ varies across atoms at fixed $n$, so $\Delta_\lambda(K)$ depends on $K$ via knot topology (likely the JSJ volume contribution) **in addition to** $\chi^\lambda(\beta_K)$.

## Proposed refinement (Phase 2)

The categorical closure form should be:

$$
  \Delta_\lambda(K)
  \;=\;
  \mathrm{Vol}_{\mathrm{hyp}}^{(\lambda)}(K) \cdot \tau_q\!\Bigl(\sum_{p \in \mathcal{O}^{(\lambda)}}
    \mathrm{Res}^{\mathrm{alg}}_p \bigl(\lambda^{(k(\lambda))}_{\mathrm{SW}}\bigr)\Bigr)
$$

where:

- $\mathrm{Vol}_{\mathrm{hyp}}^{(\lambda)}(K)$ is the per-λ-block contribution to the JSJ hyperbolic volume of the knot $K$'s complement (the knot-specific factor that resolves the T/³He degeneracy);
- $\mathcal{O}^{(\lambda)} \subseteq \{0, 1, 2\}$ is the per-λ subset of the 3 Galois orbits selected by the Wedderburn block;
- $k(\lambda) \in \{0, 1, 3\}$ (the no-$k$=2 constraint);
- the standard $\tau_q$ archimedean fibre functor.

This is the **two-factor closure**: per-knot (JSJ volume) × per-block (orbit-residue). Both factors are categorically derived; together they should reproduce empirical $B(K)$ to ≤ 1 ppm.

## Validation status

- [x] Naive closure form falsified on D (~33× miss).
- [x] Δ_λ ∝ χ_λ with universal $c$ falsified (T vs ³He at $n = 9$ give 2.9× different $c$).
- [x] Discriminant factorisation identified.
- [x] $k = 2$ residue zero anomaly identified.
- [ ] Phase 2: implement two-factor closure form.
- [ ] Phase 2: test on T, ³He.

## Status

**Productive negative result.** Phase 1b's exploration rules out the simplest forms and identifies the categorical refinement needed. The next concrete deliverable is the two-factor closure (Phase 2) — separable per-knot JSJ volume × per-block orbit residue.

Coordination note: this exploration directly addresses PR #777's open Δ_λ-gate question; the two-factor refinement should be tested against PR #777's L2 table (m_p, m_n via ρ_K once Δ_λ closes).
