---
# qou-48is
title: 'GAP: the canonical cross-species nucleon ordering p...pn...n is an unlicensed choice and tr_M depends on it by O(10%) for A>=3'
status: todo
type: task
created_at: 2026-08-09T04:34:20Z
updated_at: 2026-08-09T04:34:20Z
---


## Context (spun out of `qou-prjo` by PR #4850, 2026-08-09)

**The gap.** `atom_braid_word_3A(Z, N)` fixes the cross-species arrangement of
nucleons to the canonical string `p...pn...n`. Nothing in the corpus derives that
choice, and the canonical scalar observable depends on it.

**1. The orbit identity does NOT license it.** `tr_M(beta) = tr_M(rep)`
(`computations/atom_orbit_reduction.py`,
`docs/audits/2026-05-30-orbit-trace-identity-proof.md`) ranges over `S_Z x S_N`
only — protons among protons, neutrons among neutrons — and its Lemma 1
establishes it by showing such a permutation leaves the WORD unchanged. It says
nothing about the arrangement `pnn` vs `npn`, which is a different word.

**2. The stated reason is a COST property, not a selection rule.** The module
docstring justifies the canonical ordering as "interface-minimal (exactly one pn
crossing; every other ordering of the same multiset has >= 1 and generically
more)" and concludes "the cheapest (canonical) one is always valid" — but the
validity claim is the orbit identity, which only covers the orbit within which
the word never changes. The comparison ACROSS orderings is left unjustified.

**3. And it matters, measured** (PR #4850, certified Frobenius pairing:
tr_M(1) = 1, Markov M1 to 4e-16, constant M2 ratio to 6e-16; experimental proton
anchor; live `y_lambda_at_q0_mpmath`):

    T (1p2n)   tr_M(pnn) = tr_M(nnp) = 0.1040710573547   {pn:1, nn:1}
               tr_M(npn)             = 0.1415755179229   {pn:2}      -> +36.0 %
    He3 (2p1n) tr_M(ppn) = tr_M(npp) = 0.2065784335107   {pp:1, pn:1}
               tr_M(pnp)             = 0.1633620457246   {pn:2}      -> -20.9 %
    D (1p1n)   tr_M(pn)  = tr_M(np)                                  -> 1.5e-41

`tr_M` tracks the **interface multiset exactly** — bit-identical within a class,
O(10^-1) across classes. D is a null control: its two orderings share one
interface multiset, so its exact invariance (40 dps) shows the machinery does not
manufacture spurious differences.

**Consequence.** Every canonical mass/binding number for an `A >= 3` isotope
containing both species inherits an undetermined O(10 %) factor from an
arrangement convention.

**What would close this.** Either (a) promote interface-minimality to a derived
selection rule with an argument from the substrate (why does the physical nucleus
realise the minimal-interface arrangement?), or (b) build the observable so it
does not depend on the arrangement — e.g. an average over arrangements, which
would itself need deriving, and which is NOT the `S_Z x S_N` symmetrization
(that one is the identity map, Lean-proved in
`QOU/MassTheory/NucleonOrderingSymmetry.lean::sum_symmetrize_eq_nsmul`).

**Do NOT** pick an arrangement rule by which one lands nearest AME — that is the
forbidden fit. Derive it or report the ambiguity.

Reproducer: `computations/probes/nastokes_orbit_symmetric_readout_probe.py`
(Part B) -> `nastokes-orbit-symmetric-readout.witness.json`.
Audit: `docs/audits/2026-08-09-nastokes-orbit-symmetric-readout.md` s4, s7.
