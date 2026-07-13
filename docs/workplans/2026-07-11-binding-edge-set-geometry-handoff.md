# Binding-derivation program — reduced state + edge-set geometry hand-off

**Date:** 2026-07-11
**Session:** `claude/q-stokes-kernel-eigenfunction-y0pso2` (PR #3545)
**Audit:** [`docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md`](../audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md) (Parts 1–13)
**Bean:** `qou-v0yw`
**Siblings folded in:** #3534, #3548, #3551, #3560, main `a44296db`

## Purpose

State precisely where the per-isotope binding-derivation program stands after this
session, so the **one remaining open piece** — the compact nuclear geometry (edge
set for A ≥ 5 + cluster/halo structure) — can be picked up as a scoped, owner-gated
(s5-so3) sub-problem without re-deriving the settled upstream.

## The binding law (assembled, term by term)

    B(K)  ~  Σ_i ⟨g_i⟩²_G   +   Σ_{(i,j)∈E(K)} b*   +   Σ_{(i,j,k)} μ̄₁₂₃(i,j,k)·b₃
             └── per-nucleon ──┘  └── pairwise bonds ──┘  └── irreducible 3-body ──┘
                (rest / self)        (edge set E(K))         (Milnor triple linking)

with `g_i = ½(L₊−L₋)_i` the bar-odd **ghost** mode of nucleon `i`.

## What is DERIVED (settled this session; cross-validated across PRs)

| ingredient | result | where |
|---|---|---|
| per-cluster energy `m_e·a_D⁽ⁿ⁾` | na-Stokes period `S(n)/n`, deuteron-anchored | Parts 1–5; `conj:binding-manybody-eq-jet-filtration` |
| binding = **quadratic**, not linear | ghost is traceless (LP-invisible) with negative Gram norm | Part 10; main `a44296db`; #3548 |
| per-bond `b*` | `= ` #3548 connected `tr_M` part `=` centered Gram-quadratic norm (exact identity) | Part 12 (`binding_bstar_bridge.py`) |
| bond-extensivity `B ~ (#bonds)·b*` | derived from bond **translation-invariance** (identical couplings) | Part 11 |
| irreducible 3-body `M₃` | Milnor triple linking `μ̄₁₂₃` (Borromean = 1, chain = 0), validated | Part 7 (`binding_mn_milnor_linking.py`) |
| mass ⊥ binding | bar-even (`Re CVol`) ⊥ bar-odd (`Im CVol`); `×ζ₄` translator | Part 10; #3560 |
| edge-set **selection principle** | binding-max ⇒ **max-contact 3D packing** (resolves #2089 chain-vs-complete) | Part 13 |

## What is REFUTED (do not retry)

- **algebraic weight kernel `R(q,x)`** — Frobenius/SDP dual normalizes `tr_M` to
  trivial/constant (Parts 4, 9); the weight is geometric, not algebraic.
- **full jet tower summed to `A`** — super-exp `a_D` × amplifying weight overshoots
  (+2×10⁶ % at ¹²C); binding is few-body-truncated (Part 5).
- **SDP-active-set bond graph** — degenerate (free nucleon `W_free=W_atom`), Part 9.

## The ONE open piece — edge-set geometry (this hand-off)

The **edge set `E(K)`** for `A ≥ 5` and the **cluster/halo** deviations are the
sole residual. The selection principle (Part 13) fixes it *modulo* geometry:
`E(K) = ` max-contact sphere packing, but:

1. **A ≥ 5 max-contact numbers** are case-by-case sphere-packing contact counts
   (triangular bipyramid 9, octahedron 12, …) — a known combinatorial-geometry
   input, not yet tabulated in the corpus for the isotope range.
2. **Cluster/halo nuclei** (⁶Li = α+d, ⁹Be = 2α+n, …) sit *below* max-contact
   (loosely bound) — genuine nuclear structure; the α-cluster contact-graph level
   is #3551's Brink-deltahedra scope (the α-instance of the same principle).
3. **⁴He magic** is the 3-body `M₃` (Milnor `μ̄₁₂₃`) surplus on top of the pairwise
   simplex edges — needs the `μ̄`-tower `M₃`/`M₄` evaluated on the compact link.

### Scoped sub-problem (s5-so3, owner-gated)

Derive `E(K)` = the compact ground-state contact graph from the framework's
canonical link `𝓑_K`, rather than inputting Brink geometries: `E(K)` = the pairwise
**linking graph** of `𝓑_K` (`lk(K_i,K_j) ≠ 0` ⇔ edge; `M₃` = `μ̄₁₂₃`), with the
ground state selected by binding-maximization (max-contact) subject to 3-D
realizability. The gated question is the **`𝓑_K` assignment per isotope** — which
link represents the compact A-nucleon ground state.

### Non-fit checkpoints (when a candidate `E(K)` / `𝓑_K` exists)

- `M₂(K)` = #edges = coordination (compare to `#bonds/A → ~3` plateau, #3551).
- `M₃(K)` = `μ̄₁₂₃` triples (⁴He, ¹²C magic shells).
- `b*` from #3548's connected `tr_M` (PROBE 2) — already pinned.
- Predict `B(K)` across D→¹²C; a per-isotope free constant ⇒ fit ⇒ refute (STRICT).

## Division of labor (live)

- **#3545 (this):** the Gram-quadratic framing + `b*` bridge + bond-extensive
  derivation + edge-set selection principle + Milnor `M_n` machinery.
- **#3548:** connected-`tr_M` / PROBE-2 `b*` value (H₆⁺ seminormal build).
- **#3551:** α-cluster Brink-deltahedra contact geometry (A > 4).
- **#3560:** the `×ζ₄` bar-even↔bar-odd (mass↔binding) Lean translator.
