---
# qou-gdtb
title: 'ctype ''averaged'' discards the p-n colour weighting: chi wrong at 7e-4 on the interface crossing'
status: completed
type: task
priority: normal
created_at: 2026-08-10T15:23:20Z
updated_at: 2026-08-15T03:20:32Z
---


## The defect

`canonical_braid_crossings.classify_crossing(c, d, h)` reduces a Hecke
crossing triple `(c, d, g)` to a discrete ctype in
`{sigma, sigma_inv, averaged}`. The `averaged` branch accepts **two different
numbers** under one label:

```python
if (abs(d - (-h_val / 2.0)) < 1e-9                           # colour-blind
        or abs(d - (-h_val * (0.5 - delta / 4.0))) < 1e-9):  # colour-weighted
    return "averaged"
```

The deuteron's p–n interface carries the **colour-weighted** one:

    interface d       = -0.10445824776972629  = -h(1/2 - δ/4),  δ = 1.3757e-3
    colour-blind -h/2 = -0.104530149397819658
    relative diff     = 6.879e-4

Consumers of the label then use `-h/2`. So the `(gen_idx, ctype)` pair form
**structurally cannot carry the proton–neutron colour asymmetry** — the
`bring_color_weighted` convention AGENTS.md names as the p/n asymmetry
mechanism (`closed_form_tau_M.py`). One crossing in 23 is silently
de-asymmetrised.

The pair form also cannot express the interface at all in principle:
`rho_k_h3a_refinement`'s own header says `I = σ_3 − (h/2)·1` is
**operator-valued**, non-scalar for 9 of 11 partitions λ ⊢ 6, while a
`(gen_idx, ctype)` pair denotes a *pure generator*.

## Measured consequence

χ^λ(β_D), bridge (exact triples) vs refinement (classified pairs):

| λ | bridge | refinement | rel |
|---|---|---|---|
| (6) | 1.55987019956415 | 1.55975865810342 | 7.15e-05 |
| (5,1) | 3.21631734223588 | 3.21589087847331 | 1.33e-04 |
| (4,2) | 1.67439526203426 | 1.67374772222473 | 3.87e-04 |
| (3,3) | 4.24940202291766 | 4.24906940540997 | 7.83e-05 |

which is the entire residual left in `rho_k_h3a_refinement`'s Schur–Weyl check
after the convention-D migration (8.15e-5; `qou-8x1l`). The weights are not at
fault — they agree to 1.14e-8, itself just the μ–p anchor straddle.

**The bridge is the correct side**: it consumes the exact triples, and it
matches the independent Markov-peel algorithm to 3.6e-51.

## Why I did not fix it here

The pair form is shared infrastructure — `atom_canonical_crossings` feeds
`hoefsmit_symbolic.chi_lambda_symbolic` and
`hecke_character_symbolic.q_character_on_braid_word` as well. Correcting it
means threading the triples through those consumers or widening the ctype
vocabulary: a refactor with a blast radius, not a one-line fix.

There is also a framing trap in the obvious shortcut: making
`rho_k_h3a_refinement` read the bridge's χ **and** the bridge's `tr_M` turns
its Schur–Weyl check into a tautology (`Σ y·χ` compared against the same
`Σ y·χ`). That check was already largely self-consistency; the genuinely
independent validation is **bridge vs peel**, which now passes at 3.6e-51.

## To close

1. Decide the representation: thread `(c, d, g)` triples to the χ consumers,
   or extend the ctype vocabulary (`averaged_blind` / `averaged_weighted`).
2. Audit the other consumers of `atom_canonical_crossings` for the same loss.
3. Re-run `rho_k_h3a_refinement`; expect SW at 1e-40 once χ uses exact `d`,
   while recording that the check is self-consistency, not independent.

## Corroboration from the D sweep: it also CRASHES consumers

`bar_pairing_binding_observable.py` is the first failure of the 146-producer
convention-D regeneration sweep:

    ValueError: unrecognised d=-0.104458247769726289017834066290005644128
                (expected 0, -h0, or -h0/2)

That is the same colour-weighted interface value `-h(1/2 - δ/4)`, rejected by
a validator whose vocabulary is only `{0, -h, -h/2}` — it does not even carry
`classify_crossing`'s `averaged` tolerance branch.

So this defect has two faces, and I under-scoped it as one:

- **silent** in the χ path — 6.879e-4 on the crossing, 7e-5…3.9e-4 per λ,
  the whole residual Schur–Weyl failure;
- **fatal** in consumers that validate `d` against the narrow set.

Raises the priority: the colour-weighted p–n interface is not merely
approximated downstream, it is unrepresentable in more than one place. Any
fix has to settle the representation across every `d` consumer, not just the
two behind the χ discrepancy.

## Status correction (2026-08-14): the "two crash-site validators" were already fixed

A prior session's summary listed this bean's remaining work as *"two
crash-site validators still carry the narrow `{0, -h, -h/2}` vocabulary"*.
That was stale. Both had already been repaired:

- `atom_braid_active_partitions.py:95` carries `abs(d - _D_PN_WEIGHTED) < 1e-9`
  and uses the actual `d` as the identity coefficient;
- `fr_pullback_borromean_h3a_test.py:190` carries the `delta_ratio` branch
  with `id_coeff = h·δ/4`.

`canonical_braid_marshalling.py` had also grown a `_d_cw` branch in both
marshallers, so the original `bar_pairing_binding_observable` crash is gone.

**What was actually still live** was subtler than a crash, and is the defect
this bean names in its first section: `marshal_to_symbolic_braid` accepted the
colour-weighted `d` but **labelled it `"averaged"`**, and its consumer
resolves labels through `d_for_ctype` — so `-h/2` was substituted for
`-h(1/2 - δ/4)` with no error anywhere. Measured at 6.8833e-4 on 1 crossing
in 23. Fixed in PR #5018 by deleting the private classifier; canonical and
marshalled classification now agree crossing-by-crossing on p, n, D, T, ³He,
⁴He.

Item 2 of *To close* ("audit the other consumers of `atom_canonical_crossings`
for the same loss") is what turned up the nine further sites in `qou-8zjd` —
it was the right instruction and it had not been run.

**Still open here**: item 1, the representation decision. `sign_for_ctype`
now documents the projection rather than closing it — a `(gen_idx, ctype)`
pair still cannot express an operator-valued interface, which is this bean's
deeper claim.

Claimed 2026-08-15 by claude/color-channel-weighting-audit-qcaqfm. Items 2 and 3 landed via #5029/#5028/#5042 (consumer sweep + coverage test Parts A-E). Item 1 -- the REPRESENTATION decision -- is what remains: does the (gen_idx, ctype) pair form still lose information now that averaged_weighted exists and d_for_ctype is exact? Re-measuring triples-vs-pairs before deciding.



## CLOSED 2026-08-15 — item 1's second half is a CATEGORY ERROR; the first half is fixed and measured

Items 2 and 3 landed via #5029 / #5028 / #5042 (consumer sweep, coverage test Parts A-E, recipe-literal check). Item 1 was the last open piece. Both of its halves are now settled, in opposite directions.

### The label collapse was real, and is closed

Original measurement: exact triples vs classified pairs disagreed by 6.879e-4 on the interface crossing, 7e-5..3.9e-4 per chi^lambda. Re-measured today on the deuteron word with averaged_weighted in place and d_for_ctype exact:

    worst relative |d_triple - d_pair| = 2.66e-16   (float64 epsilon)
    at crossing 11, gen 2, ctype averaged_weighted

Three orders past what the bean recorded, and on the crossing that was wrong. The pair form round-trips the scalar d to machine precision.

### The 'cannot express in principle' half does NOT hold

The bean said: 'The pair form also cannot express the interface at all in principle: rho_k_h3a_refinement's own header says I = sigma_3 - (h/2)*1 is operator-valued, non-scalar for 9 of 11 partitions lambda |- 6, while a (gen_idx, ctype) pair denotes a pure generator.'

That runs two different statements together:
  (a) rho_lambda(I) is not a scalar matrix   -- TRUE, and reproduced
  (b) the pair form cannot denote I          -- FALSE

(a) is a property of the REPRESENTATION; (b) would be a property of the ENCODING. Neither implies the other. Measured symbolically in q over every lambda |- 6:

    NON-scalar rho_lambda(I): 9 of 11
    worst |I_pair - I_triple| over all lambda: 0   (EXACT, symbolic)

Both properties hold simultaneously. The reason is one line: I = sigma_g - (h/2)*1 is of the form c*sigma_g + d*1 with d SCALAR, so the pair names the generator and d_for_ctype supplies d — the reconstruction is an algebraic identity, independent of lambda and of the representation. rho_lambda(sigma_g) is non-scalar and rho_lambda(I) inherits it for free.

The header the bean quoted is itself correct: it says the branching COMBINER A^lambda_{mu,nu}(I) is operator-valued, which is about action across a Wedderburn decomposition, not about what a braid word can denote. The misreading is now annotated at the quote site.

SCOPE CLASSIFICATION (per AGENTS.md 'Before declaring refuted'): this is scope-(b), a STRUCTURAL exclusion, and the invariant is cited — the algebraic identity above, verified symbolically-exact over all 11 partitions, not a numerical near-miss. It excludes the inference, not the concern.

### What WOULD break the encoding, stated so nobody re-derives it

An interface NOT of the form c*sigma_g + d*1: a sum over several generators, or a coefficient depending on lambda. The corpus has none today. If one is introduced the encoding must carry triples or grow a ctype — and THAT is the trigger, not non-scalarity, which is universal and harmless.

One real loss remains and is already documented rather than open: sign_for_ctype collapses both averaged interfaces onto 0, because the LR wire format carries a sign and a sign cannot carry a magnitude. That is confined to that format, annotated in place, and is not the pair form's limitation.

Probe: computations/probes/ctype_pair_expressiveness_probe.py (exit 0).
