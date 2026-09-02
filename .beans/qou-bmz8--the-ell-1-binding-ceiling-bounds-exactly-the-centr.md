---
# qou-bmz8
title: The ell-1 binding ceiling bounds exactly the CENTRE of H_n, not the family tr_M(.w) — qou-fvzm's 'not a Hecke-trace object at all' is broader than its evidence
status: in-progress
type: task
created_at: 2026-09-02T21:56:13Z
updated_at: 2026-09-02T21:56:13Z
---

Scope correction on a closed conclusion. Probe: computations/qbeta/qbeta_l1_ceiling_is_one_point_of_a_family_probe.py (6/6). Does NOT close the binding gap.


## The argument being scoped

`computations/deltalambda/l1_ceiling_d_frame_remeasure.py` computes per atom

```
ceiling = ( sum_lambda |y_lambda . chi^lambda(beta_atom) . Delta_lambda| )
          / |B_AME / m_e|
```

and finds it `< 1` everywhere in the D frame — deuteron 0.5661, tritium 0.3604,
³He 0.6925, ⁴He 0.4335. The numerator takes the absolute value of every term, so
it is the most generous reweighting available: **no choice of coefficients on
`{Delta_lambda}` reaches the binding target.**

`qou-fvzm` (completed, closed for good 2026-08-07 by `f92a8b15`) combines that
with `N = 2` being locked and closes with

> **THE MISSING ADDITIVE TERM IS NOT A HECKE-TRACE OBJECT AT ALL.**

## What the ceiling fixes, and what it leaves free

`chi^lambda(beta_atom)` is evaluated at **one element**. The ceiling ranges over
*coefficients* at that fixed point and never varies the point. But `tr_M(x . w)`
is a Markov trace for every `w` — a Hecke-trace object, inside the `N = 2`
carrier, not row-capped. The corpus reads `w = 1`. Nothing has bounded the rest.

The owner's steer of 2026-09-02 names the same freedom from the other side: an
operator's order-0 shadow is not one number. `E_2(Delta_bind)` already carries
two coordinates, `tr_M(Delta)` and `tr_M(Delta . sigma_1)`.

## Measured (deuteron, n = 6, 11 partitions)

**Validation first — without it the rest is noise.** `rho_lambda(beta_atom)`
built from Hoefsmit seminormal matrices reproduces every committed `chi_lambda`
in `chi-deuteron-h6-at-q0-50dps.witness.json` to **3.8e-49**, and the ceiling at
`w = 1` comes out **0.5661374** against the committed **0.5661**.

| | |
|---|---|
| `tr_M(beta)` — what the corpus reads | 0.57517224 |
| `tr_M(beta . sigma_0 … sigma_4)` | 0.75834, 0.19823, 1.20425, 0.78980, 0.14009 |
| rank of `{(chi^lambda(beta.w))_lambda}` over 36 systematic words | **11 = every partition** |
| `ceiling(w)` over that sample | **[0.0913, 2.2867]**, vs `ceiling(1) = 0.5661` |
| sampled `w` above `ceiling(1)` | 21 / 36 |
| sampled `w` above 1 | 7 / 36 |

## The sharp version: the ceiling bounds exactly the CENTRE

For central `z`, Schur gives `rho_lambda(z) = c_lambda . I`, hence

```
chi^lambda(beta . z) = c_lambda . chi^lambda(beta)
```

— which *is* a reweighting `y_lambda -> c_lambda y_lambda`, the move the ceiling
already bounds. Verified on the transposition class-sum: scalar on every block,
`chi(beta.z) = c_lambda.chi(beta)` to **3.6e-49**.

So the statement is not "the ceiling misses multiplication by anything". It is:

> **The ell-1 ceiling bounds precisely the centre of `H_n`. The freedom it never
> touched is exactly the non-central part.**

## 🛑 What this does NOT license

**It does not close the binding gap and this bean must not be read as claiming
it does.** `beta_atom . w` is a *different element of the algebra* — it is not
the deuteron — so a large `ceiling(w)` is a fact about `H_6`, not about binding.
**No `w` was selected.** The sample is systematic (identity, both crossings of
every generator, every ordered pair) and the figure reported is a range.
Selecting a `w` for proximity to the target and calling it a derivation would be
exactly the defect recorded against the electroweak residual in `qou-4qno`.

What it licenses is narrow and worth stating on its own: **`qou-fvzm`'s closing
line is broader than its evidence.** Its two inputs exclude (i) reweightings and
(ii) escape to larger `N`. A non-central `w` is neither, and it is a Hecke-trace
object.

## Todo

- [x] Measure whether the family is non-degenerate and what it spans.
- [x] Establish that the centre is exactly what the ceiling bounds.
- [ ] **The derived-`w` question, which is the only one worth pursuing.** Is
      there a *categorically distinguished* non-central `w` — a Jucys–Murphy
      element, a Temperley–Lieb projector, the interface operator the corpus
      already builds — rather than a searched one? A derived `w` would be a
      candidate additive term; a fitted one is worthless. Note the full twist is
      **central**, so it is already excluded and is not the answer.
- [ ] Repeat the scope measurement at tritium / ³He / ⁴He, where the committed
      ceilings differ (0.3604 / 0.6925 / 0.4335).
- [ ] Decide with the owner whether `qou-fvzm` should carry a pointer to this
      scoping. It is `completed` and closing lines of completed beans are what
      later sessions quote — this session quoted that very line twice.
