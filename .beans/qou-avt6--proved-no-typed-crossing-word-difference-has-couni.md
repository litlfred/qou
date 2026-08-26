---
# qou-avt6
title: 'PROVED (scope-b): no typed-crossing word difference has counit epsNPq — Q_A''s element cannot exist as described'
status: completed
type: task
priority: high
created_at: 2026-08-26T07:07:45Z
updated_at: 2026-08-26T07:35:21Z
---

Parent: `qou-avtq`. Follows `qou-avt5` (which established that `eps(Delta)` has
no exhibited element). This one proves the element cannot exist AS DESCRIBED.

## What the corpus says

`qbeta-counit-closed-form.md` opens: *"Let Delta = NF(n) - NF(p) be the
single-wrap normal-form difference of the neutron and proton TYPED-CROSSING
ELEMENTS in H_3(q)"*, and asserts `eps(Delta) = h^2/2 - h`, formalised as the
bare def `QOU.Interactions.QBetaEnergyScale.epsNPq`. `Q_A = -E_0*eps(Delta)`.

## Step 1 — what a typed crossing IS (derived)

`word_to_mpfr` recognises four templates by `d`: `0`, `-h`, `-h/2`,
colour-weighted. The Hecke relation gives `sigma^-1 = sigma - h`, so a crossing
`(c=1, d)` is the element `sigma_g + d` and the templates read off as
sigma / sigma^-1 / the average -- which is what the code calls them. Hence

    eps(sigma_g + d) = q + d  in  { q, 1/q, [2]_q/2 }
    => eps(ANY typed word) = q^m * ([2]_q/2)^c

VERIFIED: `eps(beta_p) = q^3([2]/2)^2`, `eps(beta_n) = q([2]/2)^2`, and their
difference reproduces `chi_block_3` **SYMBOLICALLY** --

    eps(beta_n - beta_p) = -(q-1)(q+1)(q^2+1)^2/(4q) = chi_block_3   [exact]

a second, independent confirmation of avt5's side B (the first was numeric).

## Step 2 — the exclusion, PROVED and unbounded

`epsNPq = h(h-2)/2 = (q^2-1)(q^2-2q-1)/(2q^2)` carries the irreducible factor
`(q^2-2q-1)`, whose root is the **SILVER RATIO** `q = 1+sqrt2`. So epsNPq
vanishes there. If it were a typed-word difference, that difference would vanish
at the silver ratio, forcing

    (1+sqrt2)^(m1-m2) = (sqrt2)^(c2-c1)     [since [2]_q/2 = sqrt2 EXACTLY there]

Absolute norms in `Z[sqrt2]`: `|N(1+sqrt2)| = 1` (the fundamental unit, N = -1)
and `|N(sqrt2)| = 2`. So `1 = 2^(c2-c1)` => `c1 = c2`; then
`(1+sqrt2)^(m1-m2) = 1` and `1+sqrt2` is not a root of unity => `m1 = m2`; the
difference is IDENTICALLY ZERO, which epsNPq is not. Contradiction. QED

CONTROL, so the argument does not prove too much: `chi_block_3` IS such a
difference, so it must NOT vanish at the silver ratio -- and
`chi_block_3(1+sqrt2) = -12 - 8*sqrt2 != 0`, with exponents `(1,2)` and `(3,2)`.
A bounded sweep (m in [-14,14], c in [0,9]; 84100 pairs at three generic q)
independently returns ZERO solutions for epsNPq and finds exactly that one for
chi_block_3.

## The fork this forces — NOT adjudicated here

The corpus's description of Delta and its asserted counit are MUTUALLY
INCONSISTENT. Either

  (a) Delta is NOT a typed-crossing word difference -- the prose is wrong and the
      real element is still unexhibited; or
  (b) epsNPq is wrong, and with it Q_A and the ladder phase `eps - tr_M`.

Deciding needs the owner of the counit block. I am not guessing.

## Scope discipline

**scope-(b)** per AGENTS.md: a structural exclusion resting on a PROVED
invariant (the norm form on `Z[sqrt2]`), cited above, not a failed search.

It excludes the class "difference of two typed-crossing words" and NOTHING
WIDER. A colour-weighted crossing contributes `q - h(1/2 - delta/4)`, which is
not of the form `q^a`, so words containing one fall outside the
`q^m([2]/2)^c` normal form and outside this argument. A=1 nucleon words carry no
colour-weighted crossing (no p-n interface), which is why the class is the right
one here -- but do NOT quote the exclusion for words that do.

## Next

Lean it. The argument is elementary (a norm computation in `Z[sqrt2]` plus
"1+sqrt2 is not a root of unity") and would make this a permanent, citable
scope-(b) row rather than a probe.

Probe: computations/qbeta/qbeta_single_wrap_element_cannot_exist_probe.py (10/10)


## Lean landed 2026-08-26

`content/quantum-observable-universe/lean/QOU/QBeta/SilverRatioCounitExclusion.lean`
formalises the arithmetic core -- the corpus-specific part, previously unrecorded
anywhere:

  - `epsNP_silver`             : `epsNP (1+sqrt2) = 0`
  - `bracket2half_silver`      : `[2]_q/2 = sqrt2` there, exactly
  - `chiBlock3_silver_ne_zero` : the CONTROL does NOT vanish there
  - `silver_separates_target_from_control` : the two together, as one citable row

lean-direct EXIT=0; `#print axioms` on all five gives
`[propext, Classical.choice, Quot.sound]` -- no `sorryAx`.

DELIBERATELY NOT FORMALISED: the unit-group step
`(1+sqrt2)^a = (sqrt2)^b => a = b = 0`. That is standard algebraic number theory
(norms in `Z[sqrt2]`: `|N(1+sqrt2)| = 1`, `|N(sqrt2)| = 2`), not corpus-specific.
It is left OUTSIDE Lean rather than `sorry`-ed: nothing in the file asserts it and
no theorem depends on it. Formalising it needs `Zsqrtd 2` + norm multiplicativity.

## Next

The fork above (prose-wrong vs `epsNPq`-wrong) is an OWNER call and stays open.
Optional follow-up: close the unit-group step over `Zsqrtd 2` to make the
exclusion end-to-end machine-checked.
