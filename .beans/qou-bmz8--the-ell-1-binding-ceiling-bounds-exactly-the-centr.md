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
- [x] **The derived-`w` question.** Attempted 2026-09-03; see the follow-up
      section below. Answer so far: most of the freedom is INERT, and the part
      that is not is the interface subalgebra.
- [ ] Repeat the scope measurement at tritium / ³He / ⁴He, where the committed
      ceilings differ (0.3604 / 0.6925 / 0.4335).
- [ ] Decide with the owner whether `qou-fvzm` should carry a pointer to this
      scoping. It is `completed` and closing lines of completed beans are what
      later sessions quote — this session quoted that very line twice.

---

## Follow-up measured 2026-09-03 — most of that freedom is INERT

Probe: `computations/qbeta/qbeta_derived_w_overdetermined_test_probe.py`.
The derived-`w` todo above, attempted. The answer is not the one the todo
anticipated.

### The test

`binding_canonical.py` computes `B = Q_beta(n) . (tr_M(W_free) - tr_M(W_atom))`,
`Q_beta(n) = 0.78233340931 MeV`. The dimensionless shortfall is

```
R_X = B_AME(X)/Q_beta - ( tr_M(free_X) - tr_M(atom_X) )
```

measured **2.286957** (²H), **9.953130** (³H), **8.972505** (³He) — the framework
supplies 19.6 %, 8.2 % and 9.1 % of binding. A candidate contributes
`S_X(w) = tr_M(free_X . w) - tr_M(atom_X . w)`, and the test asks whether
`c_X = R_X/S_X(w)` is the **same at every atom**. Three atoms, one constant: two
degrees of overdetermination. One atom would be fitted by construction.

### Result — five candidates, one spread

| candidate `w` | ²H | ³H | ³He | spread |
|---|---|---|---|---|
| `w = 1` (control) | 4.109206 | 11.201717 | 10.048627 | **0.83903** |
| `sigma_1` | 3.116688 | 8.496109 | 7.621531 | **0.83903** |
| `L_2 = T1T1` (Jucys–Murphy) | 3.221299 | 8.781280 | 7.877346 | **0.83903** |
| `P+` of `sigma_1` | 3.723212 | 10.149497 | 9.104721 | **0.83903** |
| `P-` of `sigma_1` | −39.636539 | −108.049420 | −96.926954 | **0.83903** |
| interface product | −4.476702 | *blocked* | *blocked* | — |

Identical to five digits because every one is a pure **rescaling** of the same
object, by an **atom-independent** constant:

```
tr_M(D.sigma_1)/tr_M(D) =  1.318452615852908     at every atom
tr_M(D.L_2)    /tr_M(D) =  1.275636097818101     at every atom
tr_M(D.P+)     /tr_M(D) =  1.103672165665516     at every atom
tr_M(D.P-)     /tr_M(D) = -0.1036721656655155    at every atom
```

Internal check, asserted in the probe: `P+` and `P-` are complementary spectral
projectors of `sigma_1`, so their ratios must sum to the `w = 1` ratio of 1 —
and `1.103672165665516 + (-0.103672165665516) = 1` exactly. That validates the
whole ratio computation, not just those two rows.

### Mechanism — derived, and it predicts which `w` can matter

Every atom's word begins with the **same intra-nucleon block**:
`atom_braid_word_3A` emits identical first-nucleon letters whatever `(Z, N)` is.
By trace cyclicity, a `w` supported there modifies a factor **common to all
atoms**, so the ratio cannot depend on the atom. Such a `w` carries no
atom-dependent information and therefore cannot supply an atom-dependent
shortfall, at any coefficient.

**Not the naive Markov factorisation over disjoint supports** — that predicts
ratio `tr_M(sigma_1) = z = 0.612688`, and the measurement is 1.318453.
`Delta_bind` is a difference of two full-length words, not a locally supported
operator. An earlier draft of this note asserted the factorisation and was
wrong; the probe docstring records both versions.

### The narrowing, which is the point

The mechanism says which `w` **can** matter: those supported where the atoms
differ. `atom_braid_word_3A` adds exactly one letter per bond — generator index
`2` at `A = 2`, `{2, 5}` at `A = 3` — so the **interface generators are the whole
of the difference**. Measured at ²H, the interface `w` breaks the pattern as
predicted: ratio **−0.917909**, a sign flip rather than a rescaling.

So `qou-bmz8`'s non-central freedom is real but **almost all of it is inert on
`Delta_bind`**. The part that can carry the shortfall is the **interface
subalgebra** — the one the corpus's own `include_inter` switch already names.
That is a large narrowing of the open question, and it is derived rather than
searched.

### 🛑 The deciding test is BLOCKED and nothing is concluded from one atom

`tr_m_atomic_mpfr` raises

```
RuntimeError: tr_m_word_lq: Case C (multiple top-1 in segment) not implemented
```

on interface-suffixed words at `n = 9`, so ³H and ³He could not be evaluated on
the fast exact path. **²H alone is one atom and one free constant — fitted by
construction, and it proves nothing.** Whether an interface-supported `w`
supplies the shortfall consistently is OPEN.

`spread < 5 %` across all three atoms: **NONE**. No candidate is put forward.

## Todo (revised)

- [x] Test the derived-`w` question on a fixed, categorically distinguished set.
- [ ] **Redo the interface candidate on the seminormal-matrix route**, which has
      no Case C, at `n = 9`. This is the deciding measurement and it is the only
      thing standing between here and an answer.
- [ ] Consider whether `tr_m_word_lq`'s Case C is worth implementing — it blocks
      a class of suffixed words, not just this one, and the failure is loud
      (RuntimeError) rather than silent, which is the good kind.
- [ ] Repeat at ⁴He once the route is settled (512 expansion terms, over the
      current `QOU_MAX_TERMS` guard).
