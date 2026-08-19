---
# qou-vdvS
title: 'Bridge step 1: compute the constant in van der Veen Lemma 3 for the maximal term S~_N'
status: completed
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
updated_at: 2026-08-08T18:40:00Z
---

## The ask

Van der Veen (arXiv:math/0611181, AGT 8 (2008) 603-624; local
`library/arxiv-math-0611181v2/0611181v2.pdf`) writes the colored-Jones asymptotic of a Whitehead
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

## Resolution — done, and it went further than the ask

Lemma 3 as printed is **correct**: `S~_N ~ exp((4N/pi)Lambda(pi/4) - (1/2)log 2N)`,
i.e. `S~_N ~ e^{4N Lambda/pi} / sqrt(2N)`.  Verified numerically rather than
trusted, because the `s_n` line inside its own proof drops a factor `2pi` — the
two extreme terms of `log S~_N = -2 s_{N/4+N/2} + 2 s_{N/4} + s_{N/2}` cancel
that factor, so the lemma survives its own proof's typo.  (The mangled text
extraction the ask warned about was real; `pypdf` on `library/arxiv-math-0611181v2/0611181v2.pdf`
page 5 reads it cleanly.)

Its constant `2^{-1/2}` per unit of `c+d` is exactly what cancels the
cusp-dependence in the N-power and yields `D = 3 pi` independent of `c, d`.

**The bridge is closed, for the whole b=1 family rather than two links.**  With
`n := c+d` and `m := 4a-c+d`,

    c_sigma(W_{a,1,c,d}) = 2^{1/2-n} (n^2 + m^2)^{-1/4}

**The trap this bean recorded in advance was real, and it was not where it was
expected.**  The ask warned that `|Q_inf|/c_sigma` was c-dependent (0.8109 at
c=2, 0.8624 at c=3) and that fitting on one link would be wrong.  Both true —
but the c-dependence was not a missing normalisation.  It was an ERROR in the
committed `|Q_inf|` values, which were themselves wrong.  Van der Veen's
Lemma 2a is stated in the DISTANCES `|n'|, |k'|` where its own Taylor expansion
is signed, and folding the Step-4 Gaussian onto an orthant is an artifact of
that.  With signs restored the ratio is exactly `2^{n/2}`, with no missing
factor at all.

Three slips found in the published proof, none affecting his theorem: Lemma 2a's
absolute values; the Step-3 coefficient `A` carrying `4a+c-d` where Lemma 1 gives
`4a-c+d`; and the main theorem's `b >= 2` constant carrying the wrong sign
against its own Lemma 5.

Probe: `computations/probes/one_loop_vdv_constant_closed_form_probe.py` (rewritten;
its previous closed form is retracted in place).
Audit: `docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`.
Lean: `QOU.OneLoopPrefactorInvariance.vdv_c_sigma_iff_tau`.
Follow-ups: `qou-vdvT` (general peripheral curves), `qou-vdvP` (the phase of E).
