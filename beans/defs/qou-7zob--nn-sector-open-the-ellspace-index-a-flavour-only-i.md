---
# qou-7zob
title: 'NN sector: space index gives only ell mod 2 -- parked; 3S1/1S0 split now via spin-only twist (qou-ulj0), sign defect via qou-ales'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T03:11:32Z
updated_at: 2026-10-11T05:45:00Z
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

## 2026-10-10 — strand -> ell map: none exists; only ell mod 2 is derivable (PR #7612, f086f6e0400)

Search covered the six grep paths, including library sections and ocr; corpus_search was unreachable. No derived map from braid or strand data to ell, or to a 3D direction r-hat, exists.
- The Bring orbital blocks (orbital-space-normal-bundle, orbital-fourier-decomposition) are conjectures about the electron orbital, and their SO(3) action is asserted, not derived. Their prose is also internally inconsistent: it gives a curve in a surface a rank-2 normal bundle, and it says multiplicity 2 per ell while claiming dimension 2ell+1.
- The A5 subset SO(3) material maps ell -> strand data, many-to-one, and only at n = 5.
- The ribbon twist's SU(2) is the Schur–Weyl dual of V = C^2, which is already used for isospin.

Lean: `QOU/Hecke/OrbitalIndexCarrier.lean` (generic CommRing, sorry-free, exit 0; axioms propext/Classical.choice/Quot.sound):
- `exchange_even_same_scalar`: no polynomial in the exchange separates ell = 0 from ell = 2. Exchange acts as (-1)^ell on relative position, so strand data sees only ell mod 2.
- `wigner_lock_same_scalar`: the Wigner-SU(4) degeneracy, stated with no binding functional chosen.
- `mixing_not_in_letter_algebra`: any ell = 0 -> ell = 2 coupling lies outside the one-letter algebra. The scope is one-letter algebras only; multi-letter words, a second tensor factor and framing remain open.

**This bean's body (2026-08-09) predates later work that changes its premise:**
- audit 2026-08-16-interface-graded-by-t3 §5: T-grading via P+- already splits the S-wave channels;
- audit 2026-09-03-tensor-coupling-cannot-unbind-singlet with TensorCouplingCannotUnbindSinglet.lean: S12 annihilates the spin singlet and only binds the triplet harder;
- InterfaceScalar.separable_interface_degenerate and space_index_separability_probe.

So a space index cannot fix the NN sign defect, which now sits with qou-ales (gamma-gamma word selection). Its only remaining use would be 3S1-3D1 mixing, and the corpus has no target for that: "quadrupole moment" has zero hits in docs, folio, computations and beans.

Suggested re-scope (owner decision, NOT enacted): "only ell mod 2 is derivable from interface letters; a space index cannot address the sign defect"; reopen when a deuteron D-state or quadrupole target exists. Next object if built: a second Schur–Weyl factor carrying spatial SU(2). Not recommended, because nothing in the corpus forces it.

## 2026-10-11 — RE-SCOPE ENACTED (owner ofri, thread "full-tower mass weight": "Re-scope bean qou-7zob, as offered above")

- Interface letters can derive only ell mod 2 (exchange acts as (-1)^ell; QOU/Hecke/OrbitalIndexCarrier.lean, PR #7612). A space index cannot fix the NN sign defect (nn > pn > pp).
- The tensor door is closed: TensorCouplingCannotUnbindSinglet (S12 annihilates the singlet). The P± isospin grading already separates the channels (audit 2026-08-16 §5).
- The sign defect is owned by qou-ales (gamma-gamma word selection + confinement SDP).
- The 3S1/1S0 split is now pursued in qou-ulj0. A spin-only ribbon twist gives D/S = q0^2 (TwistedChannelSplitting.lean), conditional on theta_iso = 1. Its derivation and the sign of the split are being worked on PR #7612.
- Reopen trigger: a deuteron D-state or quadrupole target, or a corpus structure that forces a spatial SU(2) Schur–Weyl factor.
Status stays todo (priority lowered): the question is parked, not answered.
