---
# qou-vdvS
title: 'Bridge step 1: compute the constant in van der Veen Lemma 3 for the maximal term S~_N'
status: todo
type: task
priority: high
tags:
    - one-loop
    - c-sigma
    - van-der-veen
    - volume-conjecture
    - whitehead-link
    - borromean-rings
created_at: 2026-08-08T14:07:16Z
updated_at: 2026-08-08T14:07:16Z
---

## The ask

Van der Veen (arXiv:math/0611181, AGT 8 (2008) 603-624; local
`uploads/0611181v2.pdf`) writes the colored-Jones asymptotic of a Whitehead
chain as

    J_N(W) ~ exp{ (1/2pi)[ (Vol + iCS) N + D log N + E ] }

and reduces `E` to `Q_inf`, a quantity his Lemma 4 expresses through the
maximal term `S~_N` of the dominating sum:

    J_{N,a,1,c,d} ~ C N^{(c+d+3)/2} S~_N^{c+d} e^{iCS/2pi}       (Lemma 4)
    S~_N ~ ...                                                    (Lemma 3)

**`Q_inf` is now in closed form** for both links this corpus uses — see
`qou-vdvE` and `computations/probes/one_loop_vdv_constant_closed_form_probe.py`.
What is NOT known here is the constant part of `S~_N`, which is the other half
of the bridge to `c_sigma`.

Compute it. Lemma 3 states the asymptotic of `S~_N` in terms of the Lobachevsky
function; the `exp(Vol N/2pi)` piece is what supplies the volume, and the
SUBLEADING constant is what this bean wants. The text extraction of Lemma 3 in
`/tmp/.../scratchpad/vdv.txt` is mangled around the formula — re-extract or read
the PDF page directly rather than trusting it.

## Why it is worth doing

It is bounded work inside one published proof, not research. With it plus the
J-vs-J' normalisation, `c_sigma` for the Whitehead link stops being CALIBRATED
and becomes DERIVED on the Jones side — independently of the torsion story, and
independently of DGLZ's convention mess.

## The trap, stated in advance

Do NOT fit the bridge on the Whitehead link alone. Measured,

    |Q_inf| / c_sigma  =  0.8108743408  at c = 2
                       =  0.8623779498  at c = 3

so the missing factor is genuinely cusp-dependent — expected, since `S~_N`
enters raised to the `(c+d)` power. A single-link fit would look clean and be
wrong at `c = 3`. This arc has already made that class of error twice
(the retracted `2^{(c-1)/2}` per-cusp factor; the "DGLZ's /2 IS our k" claim).

## Definition of done

The constant part of `S~_N` extracted from Lemma 3, in closed form, with a
numerical cross-check against the committed colored-Jones data at BOTH links.

Audit: `docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`
