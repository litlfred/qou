# α_EM from-the-Lagrangian derivation + exposition audit + jet rewrite

**Date:** 2026-06-11. **Branch:** `claude/hopeful-feynman-y0zsyy`.
**Owner directive:** *"make sure exposition in paper is clear on these matters…
look for old/wrong statements. make sure story is present, one voice. prove
Status section: the from-the-Lagrangian derivation. go on rewrite."*

## Context (corpus-grounded)

`prop:em-coupling-bring-zero-mode`
([`predicted-spectra/em-coupling-bring-zero-mode.md`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md))
already establishes, as a **§3b-cond conditional theorem**:

$$\frac{1}{\alpha_{EM}} = q[9]_q[10]_q + \frac{2g}{4\pi(g-1)} + \mathcal O(\alpha),\quad g=4,$$

with `bring_zero_mode_additive_form` (Lean, sorry-free modulo
`BringZeroModeBlochClass`). The `2/(3π)` term has the **Gauss–Bonnet/Hodge**
reading `2g/(4π(g-1)) = dim H¹(M_Bring)/Area(M_Bring)`; the "/3" is **(g−1)=3**.

The block's **Status section** flags one piece as open: the *from-the-Lagrangian*
derivation — *why* the photon IR contribution equals `dim H¹/Area`. The block
records a **failed naive attempt**: harmonic zero-mode on `M_Bring × S¹`
(3-manifold) gives `(2g+1)/(8π²(g-1)) = 9/(24π²) ≈ 0.038`, 5.6× too small.

The existing Lean routes the open part through the **Bloch-group/dilogarithm**
angle `θ` (`BlochWigner_unit_circle θ = 2/(3π)`), Phase-3 research-grade and
PSLQ-refuted on canonical angles (PR #952). That is a *different* route from the
Hodge one the owner asks to prove.

## The resolution (this tranche)

**The naive attempt failed because it used the wrong manifold.** The photon IR
zero-mode is the harmonic 1-form sector on the **2-dimensional surface**
`M_Bring` itself (the gauge field's flat-connection moduli), normalised by the
surface area — **not** a 3-manifold `M × S¹`. The heat-kernel zero-mode of the
1-form Laplacian `Δ₁` has rank `b₁(M) = 2g`, each contributing a constant mode
`1/Area`, so the zero-momentum shift is

$$\delta\!\left(\tfrac1{\alpha}\right)_{\text{IR}} = \frac{\dim\ker\Delta_1}{\operatorname{Area}(M)} = \frac{b_1(M_g)}{\operatorname{Area}(M_g)} = \frac{2g}{4\pi(g-1)} \xrightarrow{g=4} \frac{2}{3\pi}.$$

Crossing with `S¹` adds a spurious generator (`b₁ → 2g+1`) and a spurious
`2π` of volume — that is exactly the naive failure.

## Deliverables

1. **Proof (Lean + content).** New proposition: the photon IR zero-mode shift =
   `b₁(M_g)/Area(M_g) = 2g/(4π(g-1))`, via (i) `b₁(genus-g) = 2g`, (ii)
   Gauss–Bonnet `Area = −2πχ = 4π(g-1)`, (iii) heat-kernel zero-mode `= b₁/Vol`
   (standard, cited). Lean: `eulerChar_genus`, `area_gaussBonnet`,
   `betti1_genus`, `photon_zero_mode_eq_hodgeRatio`, and the
   `naive_cross_S1_ne` refutation (`(2g+1)/(8π²(g-1)) ≠ 2/(3π)` at g=4).
2. **Exposition audit.** Update the `em-coupling-bring-zero-mode.md` Status
   section (conjectural → derived via surface zero-mode); sweep the paper for
   old/wrong "α_EM correction is open / round-ball" statements; one-voice the
   touched `.md`; correct the merged step-6/6b witness framing (which presented
   the secondary `V(B³)/Vol(S³)` reading as primary and called the derived "/3"
   open).
3. **Jet rewrite.** Place the terms in the SW-period jet tower
   (`jet-sw-tau-decomposition`): `q[9]_q[10]_q` tree, `2/(3π)` the n=1 IR
   zero-mode, and the n=2 self-energy — whose established form (PR #1495 thread)
   is `α·[2]_q/(8π)·(1−h²α)`, with denominator `8π = π·dim H¹(M_Bring) = π·b₁`
   grounded in the same proven `b₁=2g=8` (boundary: `b₁` topological, `π`
   archimedean, `[2]_q` substrate).

Tiered honesty: the topological/geometric core is rigorous (Lean); the
heat-kernel zero-mode = b₁/Vol is a cited standard result; the upstream
archimedean-uniqueness (`BlochSuslinUniqueness`) that makes `τ_arch` land here
remains the named conditional input. The advance is **resolving the photon
mechanism + proving the geometric core**, not removing every upstream conjecture.
