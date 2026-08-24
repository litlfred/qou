---
# qou-cxon
title: 'ADJUDICATED (qou-iayk): the D(u) closed-form law is convention-C by construction and must be re-derived in D'
status: todo
type: task
priority: normal
created_at: 2026-08-23T19:34:02Z
updated_at: 2026-08-23T19:35:38Z
---

Adjudicates `qou-iayk`, which blocked the Habiro convention-D regeneration on
2026-08-21 because the fresh values break a landed closed-form law.

**Verdict: reading (b) confirmed — the law must be re-derived in D. Reading (a)
(producer defect) is disfavoured by an independent computation.**

Audit: `docs/audits/2026-08-23-d-u-closed-form-is-convention-c.md`.

## The decisive fact

`d_u_closed_form_proof.py:18` defines `z = 1/(q^(1/2) + q^(-1/2))` — which is
`sqrt(q)/(q+1)`, **convention C**, in the detector-blind spelling from #5124.
The proof's own lines 339-340 derive the `(1+u^2)^(3A-1)` factor by *clearing
the denominator of that z*. So the law encodes C structurally:

    z_C = u/(1+u^2)   at q=u^2  ->  (1+u^2)^(3A-1)   <- the landed law
    z_D = u^6/(1+u^4) at q=u^2  ->  (1+u^4)^(3A-1)   <- the D-frame law

D-frame output was being tested against a C-frame law.

## The "irregular offset" is not irregular

Fitted on D/T/3He, predicts 4He exactly: `delta = 13 - 6Z - N`, so the fresh
exponent is `12Z + 20N + 14` — 4-for-4, small integers, same shape as the
C-frame `18Z + 21N + 1`. The "3He matches while T is off by 5" puzzle is where
that form crosses zero at (2,1).

Three parameters against four points is ONE degree of validation. This is
evidence the fresh data is structured (bearing on reading (a)); it is NOT a
derivation. Do not wire `12Z+20N+14` as canonical.

## Independent confirmation

`markov/peel_anchor_identification_probe.py` — separate code, its own landed
assertion `peel_denominator_is_convention_D` — re-run on this tree gives the
deuteron peel denominator `192*q**23*(q**2+1)**3`. **192 is exactly the fresh
Habiro deuteron prefactor**; the C value is `2^(2A+1) = 32`; `192/32 = 6`, the
uniform factor qou-iayk recorded as unexplained.

## Open sub-question this does NOT close

The `2^(2A+1)` prefactor is derived by crossing-counting, which is
convention-FREE — yet it moves 32 -> 192. So crossing-counting alone does not
determine it. That needs a real derivation, not a re-count.

Likewise the `u^shift` stays open, as the proof itself says it always was:
*"left as an open structural question (depends on the Hecke-NF reduction)"*.

## qou-iayk was right to revert

It declined to land values it could not justify. What was missing was the
justification, from a source it did not consult. The regeneration should land
**together with** the re-derived law, or the same mismatch recurs.


## 2026-08-24 — Q1 LOCALISED (not derived): the uniform 6 is one crossing

Audit: `docs/audits/2026-08-24-d-frame-prefactor-localised-to-the-interface.md`.
Producer: `computations/markov/d_frame_prefactor_localisation_probe.py`
(6/6 configurations, 5/5 assertions, exact rationals, no anchor).

    atom      A | inter=ON  ratio | inter=OFF  ratio | ON/OFF
    proton    1 |        4    1/2 |         4    1/2 |      1
    neutron   1 |        4    1/2 |         4    1/2 |      1
    D         2 |      192      6 |        16    1/2 |     12
    T         3 |      768      6 |        64    1/2 |     12
    3He       3 |      768      6 |        64    1/2 |     12
    4He       4 |     3072      6 |       256    1/2 |     12

**Three findings.**

1. With the interface off the D prefactor is exactly `2^(2A)` in every case.
   So `2A` of the C law's `2A+1` transfers to convention D unchanged; only
   the `+1` does not.
2. Switching the interface on multiplies by exactly **12**, identically for
   every A>=2 regardless of A, Z, N. Independence of nucleon count means it
   is ONE object -- which rules out any "each z picks up something"
   explanation. The C law gives that crossing a single halving, factor 2.
   **12/2 = 6**, the whole uniform 6, attached to one crossing.
3. A=1 has no second nucleon, so no interface exists, and proton/neutron
   already sit at 1/2 with `include_inter` nominally ON. Independent of
   whether the flag does what it says.

**Why a crossing count could not have found it.** `12 = 2^2 * 3` and the 3 is
not a count. The `bring_color_weighted` interface carries
`delta(q) = (q-1)^2 (1 - q^-4) / 3` (`markov_peel.py:100`, mirror of
`_li_2_q_util.flavor_split_leading`). The C proof is not WRONG about the
crossings -- it is **silent about the coefficient the interface crossing
carries**. A crossing count sees a crossing, not a colour weight. That
dissolves this bean's paradox (a convention-free derivation appearing to move
under a convention change) without either side being in error: they count
different things.

**This does NOT derive 12.** It moves the open question from "why does a
convention-free count move?" -- which had no well-posed answer -- to "derive
the interface factor 12 from delta(q)", one crossing and one known
coefficient. Smaller target, still open. Do not cite as a derivation; do not
wire `6 * 2^(2A+1)` as canonical. Scope-(a) throughout.

## Q2 (cyclotomic exponent): measured, with a caution against the obvious read

    atom   Z N A | k_D  3Z+N-1 | k_C  3A-1 | k_C-k_D  2N
    D      1 1 2 |   3       3 |   5     5 |       2   2
    T      1 2 3 |   4       4 |   8     8 |       4   4
    3He    2 1 3 |   6       6 |   8     8 |       2   2
    4He    2 2 4 |   7       7 |  11    11 |       4   4

`k_D = 3Z + N - 1` exactly (fit on three, exact on held-out 4He);
`k_C - k_D = 2N` exactly on all four. They agree only at N=0.

**Do not read `3Z + N` as a strand count.** The C derivation gets `3A-1` as
`n_strands - 1` with `n_strands = 3A`. The same reading applied to `k_D` gives
three strands per proton and ONE per neutron, which is not a plausible strand
count -- the atomic braid word carries three strands per nucleon regardless of
isospin. So the "cyclotomic power = strand count - 1" reading does not survive
the frame change.

Likely reason (HYPOTHESIS, not measured -- next thing to test): quantum
integers alias onto different cyclotomics per frame. At `q = u^2`,
`[2]_q = (u^4+1)/u^2` supplies `Phi_8 = 1+u^4` (the D cyclotomic) while
`[2]_sqrt(q) = (u^2+1)/u` supplies `Phi_4 = 1+u^2` (the C one). Each frame's
total cyclotomic power then mixes the z-count with different extra sources.

Either way this corroborates this bean's verdict from the exponent side: the D
law cannot be obtained by substituting `z_D` into the C derivation, because
the step that produces the exponent -- clearing `z^(n-1)` -- is exactly the
step that does not transfer.

## Exact relation recorded

    z_D(q) = q^2 * z_C(q^2)          (sympy: z_D - q^2 z_C(q^2) simplifies to 0)

At `q = u^2`: `z_C = u/(1+u^2)`, `z_D = u^6/(1+u^4)`. D is C under `u -> u^2`
then times `u^4`. The monomial moves only the u-exponent; the squaring maps
`Phi_4 -> Phi_8`, which is why the two laws' cyclotomic BASES correspond while
their EXPONENTS do not.
