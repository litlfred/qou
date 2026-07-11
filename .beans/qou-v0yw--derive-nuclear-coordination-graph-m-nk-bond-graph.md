---
# qou-v0yw
title: Derive nuclear coordination graph M_n(K) (bond graph) — the open geometric keystone for jet-filtration binding
status: todo
type: task
created_at: 2026-07-11T17:06:19Z
updated_at: 2026-07-11T17:06:19Z
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
