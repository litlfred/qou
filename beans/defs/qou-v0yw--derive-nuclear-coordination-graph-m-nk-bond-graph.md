---
# qou-v0yw
title: Derive nuclear coordination graph M_n(K) (bond graph) — the open geometric keystone for jet-filtration binding
status: in-progress
type: task
priority: normal
tags:
    - ungated
    - reorg-2026-10-04
created_at: 2026-07-11T17:06:19Z
updated_at: 2026-10-04T15:18:45Z
parent: qou-v2om
---


## Context (session `q-stokes-kernel-eigenfunction`, PR #3545, 2026-07-11)

The na-Stokes eigenfunction → weight-kernel program resolves everything **except**
the nuclear coordination graph. Established this session (audit
`docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md`,
Parts 1–9):

- **Derivable:** per-cluster energy `m_e·a_D^(n)` (na-Stokes, deuteron-anchored);
  per-bond-type strength `L_pp/L_pn/L_nn = log(tr_M^full/tr_M^atom)`; **Milnor
  `M_n`** of a *given* link (`μ̄`-tower, validated — Hopf lk=1, Borromean μ̄_123=±1,
  chain μ̄=0; `binding_mn_milnor_linking.py`).
- **NOT derivable (this bean):** the graph itself — *which* pairs bond
  (coordination/topology). Both routes fail:
  - ad-hoc chain (`k<A−1` in `atom_braid_word_3A`) undercounts coordination
    (~1 bond/nucleon vs data ~3) — Part 8;
  - confinement-SDP active-set is **degenerate** (`y0*=0`, active={γ}; free nucleon
    W_free=W_atom) — Part 9, `binding_sdp_bondgraph_degenerate.py`.

## The target

`B(K) ≈ m_e·Σ_{n=2}^{3} a_D^(n)·w_n·M_n(K)`, `M_n(K)` = order-n Milnor invariant of
the canonical link `𝓑_K`. Need: a **geometric / categorical coordination
construction** giving the compact bond graph (coordination ~3, nonzero `μ̄_123`
Borromean triples for the magic shells) — NOT a linear chain, NOT an LP.

- **Gated:** owner-gated s5-so3 keystone territory
  (`docs/coordination/s5-so3-keystone.md`). Do not attempt fit-based q_0 / bond
  derivation without owner sign-off.
- **Non-fit checkpoint:** once a candidate `𝓑_K` per isotope exists, compute its
  Milnor `M_n` (machinery live) and test `B(K)` vs AME across D→¹²C.

## Update 2026-07-11 (sharpened by main `a44296db` decay=binding-quadratic)

The coordination graph is NO LONGER a vague "open geometric input" — main landed the
decay=binding-quadratic finding (`qbeta_c3_barodd_binding_sdp_dual_probe.py`), which
this session reproduced (`binding_ghost_gram_quadratic.py`, audit Part 10):

- ghost `g=½(L₊−L₋)` is TRACELESS (LP-invisible ⇒ explains the Part-9 SDP degeneracy)
  with NEGATIVE Gram norm `⟨g⟩²_G=−0.4275` ⇒ **binding is a QUADRATIC Gram form**, not
  a linear LP shadow price; binding ⊥ mass.

**Concrete route (tractable, non-fit):** the bond graph is the cross-term structure
of the multi-nucleon binding quadratic form
`B ~ ⟨Σ_i g_i⟩²_G = Σ_i⟨g_i⟩²_G + 2Σ_{i<j}⟨g_i,g_j⟩_G`; pairwise `⟨g_i,g_j⟩_G` = bonds
(M₂), jointly-nonzero triples = μ̄_123 (M₃). Compute on the H₆⁺ Gram (Gram eval, not
LP). Infra exists: `gram_matrix_seminormal_h6.py`, `chi-deuteron-h6*` witnesses.

**Next step:** compute the deuteron (H₆) ghost cross-term = the first pairwise bond
as a Gram quadratic; then the coordination = graph of significant `⟨g_i,g_j⟩_G`.

## Update 2026-07-11 (post-rebase) — position vs active coordination siblings

The coordination graph is actively worked on main: `bk_coordination_contact_binding.py`
(#3549/#3551) reads M(A)=z(A)=A−1 (nucleon coordination) + α-cluster contact-graph
edges (predicts Ne/Mg/Ca <0.5%); #3548 does the W_λ connected multi-bond transfer
matrix (tr_M side). BUT they COUNT bonds and ASSUME each contributes equally — the
"single-link multiplier = coordination number" bond-extensive hypothesis is flagged
**conditional, not derived from the 13 drivers**.

**This bean's distinct value-add:** the Gram-quadratic cross-term ⟨g_i,g_j⟩_G
(Part 10) is the DERIVATION of the per-bond weight the siblings assume. H₆ deuteron
cross-term = the single pairwise bond as a negative-norm Gram quadratic; if constant
across bonds ⇒ upgrades the bond-extensive hypothesis conditional→derived; if not ⇒
reveals bond-strength structure. Complementary to the count (#3549) and the tr_M
transfer matrix (#3548), not a duplicate.

**Next compute (coordinate with #3548 first):** H₆ deuteron ghost cross-term via the
per-block seminormal infra (`gram_matrix_seminormal_h6.py`). Do NOT launch solo before
checking #3548's connected-tr_M overlap — same object, two lenses (Gram-norm vs trace).

## Update 2026-07-11 (b* bridge PROVED) — two lenses unified

The per-bond b* is NOT a separate build: #3548's connected tr_M part == this
session's centered/ghost Gram-quadratic norm, EXACT identity (binding_bstar_bridge.py,
audit Part 12): C(w)=tr(w²)−tr(w)² = tr_M((w−⟨w⟩)²)=⟨δw⟩²_G, via tr_M(1)=1. Verified
bit-identical on H_2 (both 0.8550672621). So #3548 deuteron connected 0.193 = b*;
one build (their PROBE 2) serves both lenses. Ties main a44296db (binding=quadratic).

**Remaining open (the actual keystone):** NOT b* (pinned), NOT bond-extensivity
(derived, Part 11) — only the EDGE SET / coordination graph (which pairs bond in a
compact nucleus; chain under-binds, complete over-binds). = #2089's "open edge set".
Owner-gated geometric construction (s5-so3). b* value = #3548 PROBE 2 (coordinate).

## Update 2026-07-11 (edge-set SELECTION PRINCIPLE) — narrows the last open piece

Edge set is not free: binding-max (B~Σ_bonds b*, b* const) ⇒ MAX-CONTACT 3D packing
(binding_edge_set_selection.py, audit Part 13). Between chain (A−1) and complete
(C(A,2)); = simplex C(A,2) for A≤4. Resolves #2089 chain-vs-complete: NEITHER, max-
contact. ⁴He surplus = 3-body M_3 (Part 7), not edges.

**Now-open residual (narrowed):** max-contact packing numbers for A≥5 (case-by-case
geometry) + cluster/halo deviations below max-contact (⁶Li α+d, ⁹Be). = s5-so3 gated;
α-level = #3551 Brink deltahedra (the α instance of this max-contact principle).
The PRINCIPLE (variational selection) is derived; the specific compact geometry per
isotope is the residual nuclear-structure input.

## Update 2026-07-11 (🟧 OWNER RULING — gate LIFTED) — the residual is now UNGATED

The residual above ("= s5-so3 gated") is **no longer gated**. Owner ruling (step-9 ledger
cont.11, audit `docs/audits/2026-07-11-subgoal2-owner-reversal-open-for-all.md`): Subgoal-2
opened for ALL agents — the geometric `M_n(K)` edge-set / A≥5 max-contact geometry / s5-so3
keystone / derived `R(q,x)` routes are in scope, no per-item sign-off.

- **Done (non-gated, fit-free):** the 2-body backbone `M_2=C(A,2)` (#3588, deuteron-pinned
  w_2), converging with the Part-13 max-contact simplex.
- **Open + now ungated:** the M₃/M₄ geometric weights (A≥5 max-contact packing numbers,
  cluster/halo deviations, the derived `R(q,x)` / Milnor bond-count). Work directly, not
  deferred.
- **Anti-fit rule STILL STANDS (orthogonal to the gate):** anchor-inverted `wₙ(K)` is a fit,
  not canonical; only a *derived* bond-count may wire to production.

## 2026-09-05 — RE-PROMOTED: the graph is where the binding error lives

This bean was implicitly demoted on 2026-09-04 by an edge-set comparison
reporting three edge sets within 0.6 % of one another (`qou-h7mh`). **That
measurement was rigged and is withdrawn**: its all-pairs member had been
renormalised to `A-1` bonds, which divides out the quadratic bond growth that
is the only difference between a path and a complete graph.

Raw, over 2548 AME nuclides
(`computations/qbeta/qbeta_chain_cannot_carry_coulomb_or_surface_probe.py`):

| edge set | median `B_AME / B_pred` | p5-p95 |
|---|---:|---:|
| chain | 0.886414 | 1.2250 |
| all-pairs (raw) | 0.013558 | 9.8864 |

A factor of **65.4** in the median. Neither endpoint is right — all-pairs
over-binds as badly as the chain under-binds — which is the shape of a problem
with a real answer strictly between them, i.e. exactly this bean.

**Two of the three missing SEMF terms are forced by the edge set, by
counting:** a path carries `2/Z` of the proton pairs (2.44 % at Z=82), so no
letters give a `Z^2` Coulomb term; and a path's interior degree is the constant
2, so nothing in it grows like `A^(2/3)`. See `qou-nial` for the full statement.
The acceptance criterion in this bean — a derived coordination, no fitted
constant — is unchanged; what changed is that it now has a measured target
between two known-wrong endpoints instead of an assertion that it does not
matter.

## 2026-09-05 (later) — scope narrowed: this bean cannot deliver Coulomb

Re-promoting this bean above was right, and it is worth saying precisely what it
can and cannot buy, so a successor does not attempt the impossible half.

- **Surface: YES.** A bounded-degree packing's boundary deficit gives the SEMF
  volume-minus-surface shape with `a_S/a_V = c(k-k')/k` — closed today by a
  sibling (`qou-kqdn`, `QOU/Mass/CoordinationSurfaceDeficit.lean`).
- **Coulomb: NO, for every graph this bean could produce.** Degree-sum bound:
  max degree `d` covers at most `d/(Z-1)` of the proton pairs, 14.81 % at Z=82
  even at close packing (`qou-556v`, `QOU/Hecke/BoundedDegreeCoulomb.lean`).

So the coordination graph remains the open keystone for the SURFACE/volume
structure and for `M_n(K)`, and is a dead end for Coulomb. A successor who reads
the 65x chain-vs-all-pairs gap above as "the right graph fixes everything"
should read this section first.

## Round 68 Formalization Progress (PR #8285)
- Formalized `QOU.Mass.CoordinationSurfaceDeficit.bondCount_deficit_and_uniform_eq` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/twobody_deficit_regulator_sdp_milnor_probe.py`, `scriptHash: 39a564805d3e`, Commit 1 `70bec575bb493c7f91cf1b39cb54e58ef8343777`, Commit 2 / Witness `250465c60a6cea44d9f569e88cc79ee2c8d8051b`, PR `litlfred/qou#8285`).
