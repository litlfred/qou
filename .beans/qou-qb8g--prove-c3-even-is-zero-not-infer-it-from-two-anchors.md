---
# qou-qb8g
title: "c_3's bar-parity is UNDETERMINED — neither named split is derived"
status: todo
type: task
priority: medium
created_at: 2026-08-08T11:45:00Z
updated_at: 2026-08-08T12:05:00Z
---

*** REWRITTEN 2026-08-08 (same day). The original title was "Prove c_3^even = 0".
    That premise came from an argument in qou-qb8f that turned out to be
    CIRCULAR and was withdrawn. c_3^even = 0 is NOT indicated. The real question
    is below. ***

## What the withdrawal changed

qb8f first argued: the canonical `c_3^odd = kappa_(2,1)(q)*S` split reproduces
the 2026-07-07 audit's S values under `c_3^even = 0`, therefore c_3 is purely
bar-odd. That was circular — S is DEFINED as `S := a_1/kappa_(2,1)` with
`a_1 = -c_3` (qbeta_s_complex_volume_rigidity_probe.py:69;
2026-06-13-qbeta-root-of-unity-residue-program.md:177), so the "reconstruction"
was an identity. The agreement (4.1e-5 / 1.1e-5) sat inside the 4-s.f. rounding
window (5.5e-5 / 5.6e-5) of the quoted numbers — the signature of the same
number.

So `c_3^even = 0` has NO support. Nor does `c_3^even = -Vol(4_1)`.

## The actual open question

**c_3's bar-parity is undetermined by the present corpus.** Two obstacles, both
structural:

1. **Not empirically accessible.** `c_3^even(q) = (c_3(q)+c_3(1/q))/2` needs c_3
   at `q ~ 0.901`. Both anchors sit at `q ~ 1.10998`. No amount of anchor data
   determines the split.

2. **Neither named "split" is derived.** Both are definitions applied to c_3:
       S_leak := c_3 + Vol(4_1)
       S      := -c_3 / kappa_(2,1)
   c_3 is recovered exactly from either, both ways (<1e-40) — reparametrisations
   carrying no information. Neither can adjudicate the other, and neither
   supplies a parity.

## What would actually settle it

A genuinely DERIVED decomposition of c_3 — one where the bar-even and bar-odd
parts come out of a construction with their normalisation pinned in advance,
rather than being defined as "c_3 minus/over <fixed thing>".

Candidate route, unstarted: c_3 as an archimedean evaluation of a fibre-level
(Habiro) element, where the bar-involution acts on the FIBRE object and the
parity is read off there — not inferred from two archimedean anchors that
cannot see it. This is the same target as qou-qb8e (magnitude channel), so the
two may close together.

## A parity tension to resolve on the way (recorded in qb8f)

`kappa_(2,1) = (q-1)^3(q+1)/q^2` is verifiably bar-ODD. The 2026-07-07 audit
also says S "inherits bar-odd from Q_beta". odd x odd = EVEN would make
`c_3 = -kappa*S` bar-EVEN and the label "c_3^odd" a misnomer. With
`S := -c_3/kappa` the tension dissolves (S's parity is whatever makes the
identity hold) — but it is worth stating explicitly in whichever artifact
carries the split, because as written the labels invite the wrong reading.

## Anti-fit guardrail

Do not resolve this by choosing whichever parity makes a downstream number work.
A derived parity comes from the construction; a chosen one is a fit.
