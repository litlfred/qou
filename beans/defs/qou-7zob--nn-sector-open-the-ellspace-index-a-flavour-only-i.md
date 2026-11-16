---
# qou-7zob
title: 'NN sector: open the ell/space index -- a flavour-only interface CANNOT split 3S1 from 1S0, proved degenerate'
status: in-progress
pr: 8198
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T03:11:32Z
updated_at: 2026-11-16T20:55:00Z
parent: qou-10v9
---


Branch: claude/anchor-followups-2026-08-08. Opened by owner directive after
qou-kj4v landed. This is the ONLY remaining lever on the NN sector.

## Why this is forced, not optional

qou-kj4v derived that the two-nucleon interface is selected by the isospin
label T, not by a crossing count, and Lean-proved that under convention D the
singlet always binds harder (mu- < mu+ for every q, since
2z - h = (q^4+1)/(q(q^2+1)) > 0). Sign correct, no fit.

But it ALSO proved the ceiling. In S-wave, Pauli LOCKS spin to isospin: space
symmetric => spin and isospin symmetry opposite, so S=1 <=> T=0 and S=0 <=> T=1.
A Pauli-consistent interface therefore carries a projector in EACH SU(2), and

    mu(3S1) = mu+^spin * mu-^iso  =  mu-^spin * mu+^iso  =  mu(1S0)

EXACTLY degenerate, because multiplication commutes. So:

  A FLAVOUR-ONLY INTERFACE CANNOT SPLIT 3S1 FROM 1S0 AT ALL, WHATEVER THE
  FUNCTIONAL. This is not a magnitude problem to be tuned away; it is a
  degeneracy theorem about the whole class.

In the Standard Model that splitting is the TENSOR force (3S1-3D1 mixing), a
spin-SPACE coupling. The Hecke interface has ONE index -- the strand -- and no
space index to carry it. That is the gap.

## What exists, and what does not

The corpus has an ell in exactly two places, NEITHER connected to the interface:

  content/.../knots-particles-confinement/shell-transition-knot.md:20
      HO levels ell = N, N-2, ... with the j = ell +/- 1/2 split. Shell model
      IMPORTED as structure, not derived from the trace.
  content/.../predicted-spectra/skein-coulomb-enhancement.md:41
      a partial-wave sum over ell inside a scattering amplitude.

MISSING and not cheap: there is NO map from strand position to orbital angular
momentum anywhere in the corpus. sigma_i is indexed by strand position; ell is a
representation label of spatial rotations. Nothing currently connects them.

## Acceptance / falsifier

A candidate space index must, at minimum:
  1. break the mu(3S1) = mu(1S0) degeneracy above -- state HOW, not that it
     might;
  2. do it WITHOUT a fitted parameter (this bean exists because the m_*
     multiplicity route was refuted for being content-keyed; do not replace one
     fit with another);
  3. be derived from the braid/trace structure, not imported from the shell
     model -- importing HO levels and reading off ell would be assuming the
     answer, the same error `decuplet_forces_three` makes for N=3;
  4. leave the qou-kj4v sign result intact (singlet binds harder for every q).

Falsifier for the whole programme: exhibit a two-nucleon observable that
requires L and show the Hecke interface provably cannot carry it -- that would
close the NN sector as scope-(b) rather than leaving it open.

## Do NOT

- Do not tune m_pp/m_pn/m_nn. Refuted in qou-kj4v: they are content-keyed and
  the two pn channels share content.
- Do not reach for N=3 / the eightfold way. Corpus-swept 2026-08-09: no forcing
  argument exists (RowCapObstruction.lean:66, qou-8pl3:78,
  pgl3-higher-teichmuller §2a answers the knot-complement route "NO" -- rank-1
  holonomy REINFORCES dim V = 2). NN channels are 2(x)2 = 3+1, entirely at N=2,
  and do not need it.

Full write-up:
  docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md
  (section 4 = the degeneracy theorem; section 6b = the ell addresses)
Lean: QOU/QBeta/InterfaceScalar.lean, sections IsospinOrdering + ChannelSelection.

## Round 54 Progress (PR #8198)
- [x] Added `additive_separable_interface_degenerate`, `coupled_spin_space_splitting_identity`, and `coupled_spin_space_splitting_of_singlet_zero` to `folio/quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean` (`0 sorry`, `0` vacuity hits).
- [x] Verified 80-dps separable degeneracy and spin–space tensor coupling splitting in `computations/probes/boxcontent_ward_nv_interface_binding_probe.py` (`computations/probes/boxcontent-ward-nv-interface-binding.witness.json`).
- [ ] Await CI verification and Merge Manager merge of PR #8198 (`1f80984f96ba3e6334bf43a2df76dd82a90eba3e`).
