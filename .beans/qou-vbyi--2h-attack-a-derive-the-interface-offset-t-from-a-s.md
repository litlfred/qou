---
# qou-vbyi
title: '2H ATTACK A: derive the interface offset t from a SPACE index (3S1-3D1 tensor channel) - the only route past the proved flavour-only degeneracy'
status: todo
type: task
priority: normal
created_at: 2026-08-25T18:37:51Z
updated_at: 2026-08-31T04:07:18Z
parent: qou-9ot5
---

## 2026-08-25 — this is now one of only TWO surviving routes for 2H

Every braid-word freedom at A=2 is eliminated (docs/audits/2026-08-25-deuteron-attack-c-convergence.md,
follow-up section): interface element (no principled one lands), bridge crossing count
(even m unbinds, odd m needs ~29), topology (chain == complete graph at A=2, one bond),
ordering (one arrangement), multiplicity (forbidden), alpha (pinned by beta-decay),
and any flavour-only mu (exactly degenerate).

Surviving: (1) the functional form B = -alpha*ln|tr_M|, which is POSITED - no derivation,
nothing in Lean, only a notation-table row, and a dead citation; and (2) THIS - a space
index carrying L, the only route past the degeneracy and the only place 3S1-3D1 tensor
mixing can live.


## 2026-08-31 — the PREMISE needs narrowing: a space FACTOR cannot do this

This bean is titled "the only route past the proved flavour-only degeneracy".
Checked before building, and the obvious reading of it -- add a space factor --
does not work. The counter is in `qou-kj4v`'s own sentence:

  "In S-wave Pauli LOCKS spin to isospin (SPACE SYMMETRIC => spin and isospin
   symmetry opposite): S=1 <=> T=0, S=0 <=> T=1."

**Both pn channels are S-wave.** 3S1 and 1S0 are both `S` in the term symbol
2M+1 L_J, i.e. L = 0. So a factor keyed on L takes the SAME value on both, and a
common factor cannot separate what is already equal.

PROVED, axiom-free:
`QOU.QBeta.InterfaceScalar.separable_interface_degenerate` -- for an arbitrary
separable interface fSpin(S) * fIso(T) * fSpace(L), with the Pauli lock as
hypothesis and one and the same `ell` on both sides, the channels are equal for
EVERY fSpace. Not specific to L: it covers any space index entering
multiplicatively and keyed on anything constant across the two channels.
Companion `common_factor_preserves_degeneracy`, also axiom-free.

Guard: `computations/probes/space_index_separability_probe.py` (4/4). Reproduces
this bean cluster's degenerate value 0.18614164195799085217 to 4.8e-21, and
mu+ + mu- = 1 exactly.

## What this does NOT close -- the bean stays open, with a sharper target

The Standard Model's tensor force is a spin-space **COUPLING**, and a product of
a spin function and a space function is exactly what a coupling is not. A
**non-separable** interface -- one whose value depends jointly on (S, L) and does
not factor -- is untouched by the above and is the live shape.

So the construction target is sharper than this bean states: **the space index
must enter as a COUPLING, not as a factor.** That is checkable before anything is
built, which is the point of recording it here.

Also worth separating: 3S1-3D1 mixing IS a genuine L = 0 vs L = 2 admixture
within the deuteron, and a space index is the right home for it. It is simply
not what separates the deuteron from the virtual state -- both of those are
S-wave. The bean currently runs the two together.

Scope (b) for the exclusion, invariant cited (commutativity + a common factor).
The physics input -- both channels S-wave -- is quoted from qou-kj4v, not derived
here; it is standard.
