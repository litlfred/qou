---
# qou-p88a
title: 'GAP: metallic_q_symbolic_galois_proofs recommends Lean-formalising two identities its own check says are FALSE (0/5, 0/15), while reporting allPassed true'
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-30T14:27:45Z
updated_at: 2026-10-04T15:15:42Z
parent: b9cj
---


Surfaced while draining `qou-srvu` slice `srvu-d` (the vacuous-green witness
population). This is NOT a `qou-srvu` drain and was deliberately not drained --
see "Why I did not just add the assertion" below.

## Measured on the committed witness

`computations/metallic-q-symbolic-galois-proofs.witness.json`:

    identities.I1_galois_pair_character_sum.all_verified  : false   0 of 5
    identities.I2_metallic_integer.all_verified           : false   0 of 15
    identities.I3_algebraic_integer_landing.all_verified  : false   6 of 24
    identities.I5_silver_cost_coincidence.verified        : true
    identities.I6_pisot_property.all_verified             : true

    allPassed : true          (there are no `assertions`, so all([]) is True)

## The contradiction

The same witness carries, as a durable recommendation:

    "what_we_can_now_lean_formalize": [
      "(I.1) Galois-pair character sum identity — pure algebraic",
      "(I.2) Metallic-q integer specialisation of (I.1)",
      "(I.5) Silver LP cost-coincidence as algebraic identity",
      "All three are sorry-free in Lean once the character formula is in place"
    ]

I.1 and I.2 are on that list. Its own symbolic check says both are FALSE at
**every** tested point -- 0 of 5 and 0 of 15, not a marginal failure. So the
producer is recommending Lean-formalisation of two identities it has just
symbolically refuted, and the file's summary print is
`'verified' if all(...) else '✗ check'`, i.e. the failure is visible on stdout
and nowhere a consumer looks.

The claims themselves:

    I.1   chi^lam(sigma) + chi^{lam'}(sigma)  ?=  dim(lam) * (q - 1/q)
    I.2   the same at q = delta_n              ?=  dim(lam) * n

## Why this is not the same as `qou-ad4t`

`qou-ad4t` is 111 witnesses carrying `allPassed: false` that nothing reads --
the detector fired and was ignored. This is the inverse and is invisible to
that scan: the failing verdicts are ordinary *data* keys, not `assertions`, so
`allPassed` never sees them and the witness reads GREEN. Neither
`qou-ad4t`'s scan nor `vacuous_green_witness_audit.py` can distinguish it from
a witness with nothing to say.

## Why I did not just add the assertion

Adding `I1_verified_count computed=0 expected=5` would be honest and would turn
the witness red -- and per AGENTS.md item 10 an honest negative is a valuable
result. I did not, because **I have not established whether `all_verified:
false` is a genuine mathematical negative or a defect in the checker.** The
plausible third reading is that I.1 holds only on a sub-family (e.g. only for
self-conjugate lambda, which `verify_I1_galois_sum` records as
`self_conjugate` but does not condition on). Asserting `expected = 5` would be
asserting a form of the identity I have not verified is the intended one --
the mirror of the invented-assertion move this drain exists to forbid.

## Next honest step

Decide which of these three it is, in this order:

1. Read `chi_sigma` / `dim_specht` against the intended character convention;
   a 0-of-5 rate on a "pure algebraic" identity is far more consistent with a
   convention or normalisation mismatch than with the identity being false.
2. If the checker is right, the `what_we_can_now_lean_formalize` list must lose
   I.1 and I.2 -- it is currently a durable artifact recommending the
   formalisation of a refuted claim, which is what AGENTS.md
   "Axiomatization is NOT a Proof" is about.
3. Only then add the assertion, with `expected` set to whatever the corrected
   claim actually is.

Scope note per AGENTS.md: this records a **scope-(a)** observation -- these
identities as currently written and checked do not hold at the tested points.
It is NOT a claim that the Galois-pair character sum is false as mathematics;
no invariant has been cited that would justify that.
