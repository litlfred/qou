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
