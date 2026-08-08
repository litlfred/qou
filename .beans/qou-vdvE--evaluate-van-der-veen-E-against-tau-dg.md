---
# qou-vdvE
title: 'Bridge step 2: test van der Veen E against |tau_DG|^{-1/2} — the Gukov-Murakami conjecture, for links'
status: todo
type: task
priority: high
tags:
    - one-loop
    - c-sigma
    - adjoint-torsion
    - van-der-veen
    - gukov-murakami
    - whitehead-link
    - borromean-rings
created_at: 2026-08-08T14:07:16Z
updated_at: 2026-08-08T14:07:16Z
---

## The ask

Van der Veen's closing paragraph defers exactly this:

> "In the same paper it is also conjectured that the number E is determined by
> the Ray-Singer torsion of the complement twisted by the holonomy
> representation. We hope to investigate these conjectures for the Whitehead
> chains in a subsequent publication."

**He never wrote it.** A literature search (2026-08-08) finds his later work
moves to spin networks and then to algorithmic knot invariants, and finds no
other author computing this constant for a multi-cusped link in his setting
(colored Jones of a link in S^3 at `e^{2 pi i/N}`).

So the conjecture is open, for links, and this corpus is unusually well placed:
it has the torsion side (`|tau_DG|`, triangulation-invariant, validated on 13
manifolds x 25 randomised triangulations) and now the Jones side in closed form.

## What is already done

`computations/probes/one_loop_vdv_constant_closed_form_probe.py` evaluates the
integral van der Veen left unevaluated. It is an `(n+1)`-dimensional Gaussian
ORTHANT probability, elementary exactly for `n <= 2`, and the two links sit
inside that window:

    Whitehead  W_{0,1,1,0}  n=1, A=1-i : I = arctan(sqrt A)/(pi sqrt(A/2))
                                           = 0.3359741489681530919776
                                           + 0.05792312441439105494502 i
    Borromean  W_{0,1,1,1}  n=2, A=2   : I = 1/2 + (2 arcsin(-1/sqrt3)
                                                    + arcsin(1/3))/pi
                                           = 0.2163468959387854596583

Both checked against quadrature to < 1e-25; the Whitehead value also reproduces
an independent evaluation of the un-reduced 2-D Step-5 integral, which validates
the derived prefactor `C = 2 psi 2^{-n/2}`.

## Blocked on

`qou-vdvS` — the `S~_N` constant from Lemma 3, plus the J-vs-J' normalisation.
Without those, `Q_inf` is not `c_sigma` and the comparison is not the
conjecture.

## What a result would be

If `E` comes out as `|tau_DG|^{-1/2}` up to the universal constant, that is:
  * the first evaluation of van der Veen's `E`;
  * the Gukov-Murakami conjecture checked on a LINK, where no theorem reaches;
  * `c_sigma(L5a1) = 2^{-3/4}` upgraded from calibrated to derived on the Jones
    side, independent of the torsion route entirely.

A NEGATIVE result is equally valuable and must be reported as such: it would
falsify the prefactor form for links, which is the corpus's one carried
assumption.

## Scope guards

* `n >= 3` (more clasps) has NO elementary closed form — Plackett reduction
  only. Do not promise the family, only these two.
* Pandey-Wong arXiv:2105.08805 proves the AEC with a torsion 1-loop term for
  fundamental shadow link pairs, but in the RELATIVE Reshetikhin-Turaev
  Chen-Yang setting at `e^{2 pi i/(N+1/2)}` — a different invariant at a
  different root of unity. It does NOT close this, and must not be cited as
  though it did.

Audit: `docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`
