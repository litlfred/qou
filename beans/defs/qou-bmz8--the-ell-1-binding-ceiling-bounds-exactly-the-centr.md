---
# qou-bmz8
title: The ell-1 binding ceiling bounds exactly the CENTRE of H_n, not the family tr_M(.w) — qou-fvzm's 'not a Hecke-trace object at all' is broader than its evidence
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-02T21:56:13Z
updated_at: 2026-10-04T15:14:10Z
parent: qou-v2om
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
- [x] **Redo the interface candidate on a route with no Case C.** Done
      2026-09-03 — and the answer is NEGATIVE. See below.
- [ ] Consider whether `tr_m_word_lq`'s Case C is worth implementing — it blocks
      a class of suffixed words, not just this one, and the failure is loud
      (RuntimeError) rather than silent, which is the good kind.
- [x] Repeat at ⁴He. Done — the character route reaches `n = 12` directly, so
      all four atoms are in the test.


---

## The deciding test, 2026-09-03 — NEGATIVE, and it closes the opening

Probe: `computations/qbeta/qbeta_interface_w_deciding_test_probe.py` (5/5).
This bean opened a gap in an exclusion argument; the gap has now been followed
to the only place it could live, and there is nothing there.

### Route

`tr_m_word_lq`'s Case C blocked the fast path. It is a limitation of the
**Markov-trace recursion**, not of the character route:
`chi_q_atomic_all_partitions_mpfr` evaluates
`chi_lambda(prod_i (c_i sigma_{g_i} + d_i I))` for every `lambda |- n` directly
from the `(c, d, g)` letters — no `2^k` expansion, no recursion, no Case C — and
`tr_M = sum_lambda y_lambda chi^lambda`. It also reaches `n = 12`, so **⁴He is
in the test** and the overdetermination is three, not two.

**Generator indices are 1-BASED there and 0-based in `tr_m_atomic_mpfr`.**
Mixing them is silent at `n >= 4` (it evaluates a different word) and only
raises at small `n`. Worth knowing before using either.

**Validation first.** Reconstructing `sum_lambda y_lambda chi^lambda(beta_atom)`
reproduces the committed `tr_M_at_q0` at every atom, worst `|chi - committed|`
`2.0e-49` and worst `|tr_M - committed|` `8.0e-51`.

### Result

| candidate `w` | ²H | ³H | ³He | ⁴He | spread |
|---|---|---|---|---|---|
| `w = 1` (control) | 4.1092 | 11.2017 | 10.0486 | 31.2986 | **1.9195** |
| interface `sigma` product | −4.4767 | −12.9284 | −8.3874 | −28.1999 | **1.7575** |
| interface `sigma^-1` product | −3.6462 | −12.4687 | −8.7048 | −33.7315 | **2.0553** |
| interface averaged product | −4.0190 | −12.5391 | −8.4645 | −30.4357 | **1.9053** |
| first interface only | −4.4767 | 48.6038 | 175.8046 | 71.7717 | **2.4721** |

- spread `< 5 %`: **NONE**
- beating the control by `2x`: **NONE**
- best in the fixed set is the interface `sigma` product at 1.7575 against a
  control of 1.9195 — an 8 % improvement, which is nothing.

Two details worth keeping. All three whole-interface candidates give **negative**
`c`, so `S_X(w)` carries the opposite sign to the shortfall — the interface
operator would need a negative coefficient and *still* would not align. And
"first interface only" is wildly inconsistent (−4.48, 48.60, 175.80, 71.77),
which is what privileging one bond arbitrarily should look like.

Note also that adding ⁴He raises the **control** spread from 0.83903 (three
atoms) to 1.9195 — the framework supplies an even smaller fraction of ⁴He's
binding, so the four-atom test is stiffer than the three-atom one, not weaker.

### What this settles

**The interface route is closed.** The chain was: the ell-1 ceiling bounds only
the centre (this bean); almost all the non-central freedom is inert on
`Delta_bind`, and the mechanism narrows the live part to the interface
subalgebra (`qbeta_derived_w_overdetermined_test_probe.py`); and the interface
subalgebra, in its categorically distinguished forms, does not supply the
shortfall at four atoms with one constant.

So **`qou-fvzm`'s practical conclusion survives, on better grounds than it
had.** Its stated ground — the ell-1 ceiling — genuinely does not cover
non-central `w`, and that scoping stands. But the uncovered region has now been
measured where it is reachable, and it is empty. The correction to `qou-fvzm` is
therefore to its *argument*, not to its *verdict*.

**Still not proved in general.** "The categorically distinguished interface
elements do not supply it" is not "no non-central `w` supplies it". The
candidate set was fixed in advance and is small. What has been removed is the
obvious place to look.

## Todo (revised)

- [x] `qou-fvzm` now carries a scoping note (2026-09-03). Added rather than
      altered: its verdict is NOT withdrawn, and the note says so in its first
      sentence. Safe to do unilaterally only because the measurement came back
      negative — had the gap been non-empty it would have been a challenge to
      someone's conclusion and an owner call.
- [x] `tr_m_word_lq` Case C — investigated, and the answer is **do not fix it
      that way**. It is a missing branch of the reduction, not a mathematical
      wall: the recursion branches on how many `top-1` sit in the segment after
      the top generator's innermost occurrence — none applies
      `sigma^2 = h.sigma + 1`, exactly one applies the braid relation, and more
      than one is unimplemented. But **PR #886 deliberately declined an
      automatic chain out of Case C**, calling it "a MATHEMATICAL condition
      where the Rust kernel is inapplicable and the right answer may differ", so
      silently routing to the sympy Ocneanu fallback would mask a discrepancy
      instead of surfacing one. The right move is what this arc actually did:
      take the CHARACTER route, which is a different algorithm reaching the same
      number, and validate it against the committed witnesses first. Recorded as
      a TRAP in `.claude/agent-memory/compute-precision-auditor/MEMORY.md`,
      together with the 1-based/0-based generator-index difference, which is
      silent at `n >= 4`.

## TAKEOVER 2026-09-06 — re-run the deciding test against the REGENERATED caches

Taken over under the stalled-claim protocol (`local/todo-manager` §Stalled-claim
takeover).  Evidence it was stale rather than live: last bmz8 commit
**`40412156f2`, 2026-09-03**, three days idle against a 3 h threshold, and its
work is already merged to `main` — the bean was left `in-progress` after landing
rather than being actively worked.

**Scope of this takeover is ONE item.** Not the bean's wider agenda.

### Why

This bean's verdict — *"the interface route is CLOSED — the deciding test is
negative"* (`2e68bb647d`) — was computed against the `chi-<atom>-h<n>-at-q0-50dps`
caches as they stood on 2026-09-03.  Those caches were **26 days stale** to the
2026-09-05 intra-ordering ruling (`qou-hu1f`) and were **regenerated** on
2026-09-06 under a second owner ruling (`qou-92u9`).

`qbeta_interface_w_deciding_test_probe.py` is the one downstream consumer the
regeneration sweep could **not** refresh: it timed out at 180 s in the sweep and
again at **2400 s** on a re-run, reaching section 3 of 3 and being killed
mid-table.  It wrote nothing, so its witness still carries
`computedAt 2026-09-03T06:32:21` — pre-regeneration data.

**So the verdict is untested under the data the corpus now holds**, and this
session is a direct demonstration that a verdict of that shape can invert: the
O3′ atom-independence result was measured 6/6, merged twice, and reversed to 4/6
by exactly this regeneration.

### What is being claimed, and what is NOT

Claimed: re-run the probe with a budget past 40 minutes and report what the
deciding test says against regenerated caches.

**NOT claimed:** that the verdict is wrong.  It may well reproduce.  The point is
that "CLOSED" currently rests on inputs that no longer exist, and nobody has
checked.  Whichever way it lands is a result.

### Falsifier

If the re-run reproduces a negative deciding test, the CLOSED verdict stands and
this note becomes a confirmation rather than a challenge.


## RESULT 2026-09-06 — the CLOSED verdict SURVIVES; every number under it moved

Re-run completed: **6691 s (1 h 51 m)**, exit 0, 16/16 assertions, witness
rewritten at `computations/qbeta/qbeta-interface-w-deciding-test.witness.json`.
Log tee'd during the run; pre-regeneration witness snapshotted for the diff.

**The falsifier fired the way it was written.** The takeover note said *"If the
re-run reproduces a negative deciding test, the CLOSED verdict stands and this
note becomes a confirmation rather than a challenge."* It reproduced. Under the
regenerated (borromean) caches, exactly as under the stale (grouped) ones:

- candidates reaching the 5 % spread bar: **NONE**
- candidates beating the control by 2×: **NONE**

So the interface route stays CLOSED and `2e68bb647d`'s conclusion is upheld —
now on data that exists.

### But "reproduces" is not "unchanged" — 41 of 113 recorded values moved

The probe calls `atom_braid_word_3A` itself (lines 163-164, `include_inter`
True/False), so it consumed the intra-ordering change directly rather than only
through the caches. Its validation section still reconstructs every committed
`chi` and `tr_M` — worst error **1.07e-49**, slightly *better* than the
1.03e-48 it managed against the old caches.

**The shortfall widened by EXACTLY the R_quark factor, on all four atoms.**
`dtr_req` (what the binding needs) is byte-identical; `dtr_pred` (what the
interface supplies) scaled down by 1/R_quark:

| atom | fraction supplied, pre | post | pre/post | R_quark (qou-hu1f) | rel |
|---|---|---|---|---|---|
| ²H  | 0.19572514  | 0.051713246  | 3.784816  | 3.785  | 4.9e-5 |
| ³H  | 0.081955677 | 0.010416112  | 7.868164  | 7.868  | 2.1e-5 |
| ³He | 0.090508981 | 0.013135018  | 6.890663  | 6.891  | 4.9e-5 |
| ⁴He | 0.030961059 | 0.0021613555 | 14.324834 | 14.325 | 1.2e-5 |

Four atoms, four different factors, agreement to the rounding of the recorded
4-figure constants. **That the ratio IS R_quark is measured; WHY is a
hypothesis** — the natural reading is that the interface term carries the
intra-nucleon confinement core as a factor, but this probe does not establish
that and nothing here should be cited for it.

Consequence for the verdict: the interface supplied **3–20 %** of the
requirement under the stale ordering and supplies **0.2–5 %** under the
canonical one. The route is *further* from closing, not nearer — the
regeneration strengthens CLOSED rather than merely failing to overturn it.

### One rank inversion, held below the bar by the gate

Spread, and spread relative to the control:

| candidate w | pre | post | pre/ctl | post/ctl |
|---|---|---|---|---|
| w = 1 (control) | 1.9195412 | 2.7275977 | 1.000 | 1.000 |
| interface σ product | 1.757517 | 2.6038765 | 0.916 | 0.955 |
| interface σ⁻¹ product | 2.0553138 | 2.8118116 | 1.071 | 1.031 |
| interface averaged product | 1.9053336 | 2.7085538 | 0.993 | 0.993 |
| **first interface only** | **2.4721179** | **1.9302124** | **1.288** | **0.708** |

`first interface only` is the **only** row that improved in absolute terms
while the control and every other candidate got worse — it went from ranking
*last* (1.29× the control's spread) to ranking *best* (0.71×). A reader of the
pre-regeneration witness would have ranked it bottom.

**It does not reach the promotion bar** — 2.7276/1.9302 = **1.41×**, against
the 2× the probe demands — which is exactly what stops this being over-read,
and is why that bar is stated in advance rather than after seeing the numbers.
Recorded because the *ordering* flipped, not because anything is put forward:
per the probe's own banner, a small spread would be a target to check a future
derivation against, never a derivation.

### Scope

This closes **only** the one item claimed by the 2026-09-06 takeover. The
bean's wider agenda — the `tr_M(x·w)` family freedom that `qou-fvzm`'s "not a
Hecke-trace object at all" overstated — is untouched and remains open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 88 (`https://github.com/litlfred/qou/pull/8405`, head `094b162d955cf25f57c026bb5dce25006b9627d4`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
