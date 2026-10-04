---
# qou-n9qf
title: '[HEADLINE WITHDRAWN 2026-09-03 — see the closed form] Delta_tr IS extensive and at A<=4 that is the failure: flat 0.29/nucleon vs B/A moving 6.4x, and two corpus scales for it differ 5.5x'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T10:37:26Z
updated_at: 2026-10-04T15:11:48Z
---

Probe: computations/qbeta/qbeta_extensivity_is_the_failure_probe.py (5/5). Refines qou-imcd / qou-78pt rather than disputing them.


## Measured (four atoms, from the committed deciding-test witness)

| atom | A | `Delta_tr` | `Delta_tr/A` | B (MeV) | B/A | deficit/nucleon |
|---|---|---|---|---|---|---|
| ²H | 2 | 0.55654466 | 0.27827233 | 2.2246 | 1.112 | 5.11 |
| ³H | 3 | 0.88853613 | 0.29617871 | 8.4818 | 2.827 | 12.20 |
| ³He | 3 | 0.89290858 | 0.29763619 | 7.7180 | 2.573 | 11.05 |
| ⁴He | 4 | 1.11980901 | 0.27995225 | 28.2957 | 7.074 | **32.30** |

- relative spread of `Delta_tr/A`: **0.0672**
- relative spread of `B/A`: **1.7552** — *26x larger*
- `B/A` max/min: **6.36**
- deficit per nucleon: **5.11 … 32.30**, i.e. **not a constant**

## What this says

`Delta_tr` — the quantity `B = Q_beta(n) . (tr_M(W_free) - tr_M(W_atom))`
actually evaluates — **is extensive**: flat to 6.7 % per nucleon across
A = 2..4. And that is precisely the obstruction, not the achievement. `B/A`
moves 6.4x over the same four atoms, so the falling "fraction supplied"
(19.6 %, 8.2 %, 9.1 %, 3.1 %) is not four separate disappointments: it is one
flat number divided by a rising one.

**Consequence for every add-a-term attack.** The per-nucleon deficit runs
5.1 → 32.3. A missing term that is any fixed multiple of an extensive quantity
cannot close that, whatever the multiple. This is also the structural reason the
interface deciding test (`qou-bmz8`) returned every candidate near spread 2: it
asked for one constant `c` with `R_X = c . S_X(w)` while `R_X` is dominated by a
term varying 6.4x and the candidates supply flat ones. That test was fair; the
answer was structural rather than unlucky.

**The calibration atoms are the wrong place to check extensivity.** `B/A`
reaches its ~8.5 MeV/nucleon plateau only well above A = 4; at A = 2 it is 1.11.
All four atoms sit where the semi-empirical surface, Coulomb and pairing terms
dominate. "The extensive term has the right shape" is a claim about the
asymptotic regime being tested against non-asymptotic data — it can be true and
useless at the same time.

## Relation to prior work — refining, not disputing

`qou-imcd` measured the A-exponent of `log Z(3A)` as exactly 1.0 and concluded
the residual is "a pure multiplicative constant, not a shape error";
`qou-78pt` calls it "a pure convention choice". **Neither is disputed.** Both
measure the **normaliser**. What is added here is the same measurement on the
**binding law's own quantity**, which is extensive too — plus the observation
that at A <= 4 extensivity is the problem.

## 🛑 Two corpus figures for the same quantity differ by 5.5x — for the owner

Both are presented as the framework's extensive energy per nucleon:

```
qou-imcd, via the normaliser :  3 . log(1 + q0^2) . m_e  = 1.2309 MeV/nucleon
the binding law, via the trace:  Q_beta . <Delta_tr/A>    = 0.2253 MeV/nucleon
                                                    ratio = 5.46
```

with correspondingly different deficits against the 8.5 plateau: **6.91x**
(normaliser) versus **37.72x** (binding law). They are different objects with
different energy scales, so this need not be an error — but the corpus offers
both as "how far off the extensive term is", and they cannot both be that.
Which is the prediction changes what "a pure multiplicative constant" is a
constant *of*.

## Todo

- [ ] **Owner:** which of the two scales is the framework's prediction for
      energy per nucleon? The 6.91x and 37.72x deficits are quoted in different
      places for what reads as the same claim.
- [x] ~~Test the prediction at larger A.~~ **BLOCKED BY A HARD WALL, and the
      wording above was wrong twice.** See "The A-scan cannot be extended"
      below.
- [ ] The missing term must be **strongly A-dependent in the light region** —
      surface-like — not a constant multiple of anything flat. That is a real
      negative constraint on candidates and it is derived, not guessed.


---

## The A-scan cannot be extended past A = 4, and two corrections to this bean

### Correction 1 — "better at larger A" was backwards

The todo above said the framework should track `B` *better* at larger A. It
should not. Fraction supplied is

```
Q_beta . (Delta_tr/A) / (B/A)  =  0.2253 / (B/A)
```

so as `B/A` rises the supplied fraction **falls**, toward ~2.65 % at the
8.5 MeV/nucleon plateau. The correct prediction is that the **deficit stops
varying**: it runs 5.1 → 32.3 across A = 2..4 and should asymptote near 37.7
once `B/A` flattens. ⁶Li is the interesting probe because `B/A` is
NON-monotonic there — 7.07 at ⁴He falls to 5.33 — so a flat `Delta_tr/A`
predicts the deficit falls too, testing against a dropping target rather than
only a rising one.

### Correction 2 — the test is not merely expensive, it is unavailable

Probe: `computations/qbeta/qbeta_chi_witness_convention_split_probe.py` (7/7).

The corpus has complete `chi` witnesses at n = 15 (⁵Li) and n = 18 (⁶Li), but
only in `sign-only-crossings`, and the calibration atoms are
`colour-weighted-averaged-crossing`. Recomputing lithium in the calibration
convention is what the extension needs — and it **cannot be done**:

| n | partitions | max Specht dim | |
|---|---|---|---|
| 12 | 77 | 7,700 | ⁴He — tractable, ~4 min |
| 15 | 176 | **292,864** | |
| 18 | 385 | **16,336,320** | |

The colour-weighted route evaluates
`chi_lambda(prod_i (c_i sigma_{g_i} + d_i I))` by building seminormal
**matrices**, because a general shift `d` is not a braid generator. A
16,336,320-square matrix is not a slow computation, it is an impossible one.
`sign-only` reaches n = 18 precisely because `chi_q_via_gp` is
character-theoretic and never forms a matrix — but that method requires the
crossings sign-quantised, which is the very information the colour-weighted
convention exists to preserve.

The multilinear escape does not rescue it: only the `2A + 1` averaged letters
carry a general `d`, so expanding just those gives `2^(2A+1)` braid words — 32
at A = 2, which is how the light atoms were done, but **8192 at A = 6**, each
still needing a full all-partition sweep.

**Attempted and killed.** A colour-weighted ⁶Li run was stopped after
**5 h 03 m** without completing the first of its two words.

### So the convention split is FORCED, not accidental

This also answers the question the sibling probe only observed. The corpus's
conventions divide exactly where the computational method has to change, and the
one that reaches the larger atoms is necessarily the one that discards the
colour weighting. That is worth knowing before anyone else tries to extend an
A-scan and reads the convention field as a labelling choice.

**Consequence for `qou-n9qf`:** the extensivity prediction is **untestable past
A = 4 with current tooling**. Not "not yet done" — unavailable by the method.
Testing it needs either a character-theoretic evaluator that accepts a general
shift `d`, or an independent route to `Delta_tr` that never forms the matrices.

## Todo (revised)

- [ ] **Owner:** which of the two extensive scales is the prediction
      (1.2309 vs 0.2253 MeV/nucleon, deficits 6.91x vs 37.72x)? Unchanged, and
      now the more answerable of the two open questions.
- [ ] A character-theoretic evaluator accepting a general shift `d` would unlock
      the whole A >= 5 range in the calibration convention. That is the single
      capability standing between here and the extensivity test, and it is a
      tooling question rather than a physics one.


---

## 🛑 HEADLINE WITHDRAWN 2026-09-03 — the chain has a CLOSED FORM

Probe: `computations/qbeta/qbeta_chain_closed_form_probe.py` (6/6). Prompted by
a direct question — can this be settled symbolically instead of by computing
ever-larger atoms? It can, and the symbolic answer contradicts what four data
points suggested.

### The closed forms

**Free trace factorises exactly.** The Ocneanu trace is multiplicative over
disjoint strand ranges and `beta_free` is A disjoint nucleon blocks by
construction, so

```
tr_M(beta_free) = t_p^Z . t_n^N          relative error ~1e-40
t_p = tr_M(proton,  H_3) = 1.1457596924573008697
t_n = tr_M(neutron, H_3) = 0.98774368811580957163
```

verified at ²H, ³H, ³He to every digit. **Two H₃ numbers give the free trace for
every atom** — no n = 18 matrices, no convention problem, no wall.

**Atom trace is geometric on a homogeneous chain**, ratio constant to 22 digits
across two independent measurements, and the ratio is DERIVED rather than
matched to a candidate — `tr_m_word_lq` returns exact Laurent polynomials, the
A = 1 and A = 2 words expand into 32 and 1024 positive braid words, and the
ratio is taken symbolically:

```
           (q^8 + q^4 + q^2 + 1)(q^14 + q^12 + q^10 - 1)
    r(q) = ---------------------------------------------      [2]_q = (q^2+1)/q
                        4 q^9 [2]_q^3
```

`r(q_0) = 0.7019932570132013578` against a measured `0.7019932570132007939`.

**Validated out of sample.** `r(q)` was derived from A = 1 and A = 2 only, so
A = 3 and A = 4 are predictions rather than fits:

| A | | predicted | measured | rel |
|---|---|---|---|---|
| 3 | atom | 0.564624112450980111 | 0.56462411245097933 | 1.4e-15 |
| 4 | atom | 0.396362319687651586 | 0.396362319687651834 | 6.3e-16 |
| 4 | free | 1.72335266162679288 | 1.72335266162679656 | 2.1e-15 |

the numeric side being float64-limited by the weight routine. **A = 4 cost
1958.9 s (33 min) by the matrix route; the closed form is instant**, and A = 6
is not merely slow by matrices but impossible.

### Why the headline is wrong

`Delta_tr(A) = t_p(t_p^(A-1) - r^(A-1))`, and `t_p > 1 > r`:

| A | 2 | 3 | 4 | 6 | 10 | 20 | 40 |
|---|---|---|---|---|---|---|---|
| `Delta_tr/A` | 0.254 | 0.313 | 0.332 | 0.345 | 0.385 | 0.760 | **5.777** |

**A shallow region, then exponential growth** — `Delta_tr` is asymptotically
`~t_p^A`. The four calibration atoms sat in the flat-looking part of an
exponential. And the reason those atoms in particular look flat is now visible:
`t_p = 1.1458 > 1` while `t_n = 0.9877 < 1`, so for `Z ~ N` the free trace hugs
`(t_p t_n)^(A/2) = 1.0638^A` and barely moves. **Flatness is a property of
near-symmetric light nuclei, not a law.**

### What survives

The measurement this bean was built on: over A = 2..4, `Delta_tr/A` varies 6.7 %
while `B/A` varies 6.4x, so the per-nucleon deficit runs 5.1 → 32.3 and is not a
constant. **That stands.** The word "extensive" does not, and neither does the
inference that the framework "supplies a flat per-nucleon quantity" as a
structural fact.

### The wall is bypassed, and that changes the open list

`qou-n9qf` previously recorded the A-scan as untestable past A = 4 because the
colour-weighted route needs 16,336,320-square matrices at n = 18. The closed
form does not need matrices at any A. That earlier entry stands as a correct
statement about the MATRIX route; it is no longer a statement about the
question.

### Scope — what is NOT derived

The geometric law and `r(q)` are for a **homogeneous** pure-proton chain. Real
atoms mix p and n, so their p-p, p-n and n-n interfaces need a multi-state
transfer matrix rather than a single ratio. Not done here. The free-trace
factorisation DOES hold for real atoms and is verified.

## Todo (revised again)

- [x] **The mixed chain closes too (2026-09-03).** See below. `b_pp` turns out
      to be the Markov parameter `z`.
- [ ] **Owner:** which of the two extensive scales is the prediction
      (1.2309 vs 0.2253 MeV/nucleon)? Unchanged, and sharpened: with `Delta_tr`
      asymptotically exponential, "extensive energy per nucleon" needs restating
      before either number means what it says.
- [ ] `QOU/Hecke/MarkovTraceProduct.lean`'s `markov_trace_product` is
      **vacuous**: the structure carries `traceValue` as a free field plus
      `factorization : traceValue = prod ...` as an invariant, so the theorem
      constructs a record with `traceValue := <the product>` and proves `rfl`.
      Its conclusion mentions no Markov trace and nothing ties the field to one.
      Two literature citations sit on it. The file's other two results are fine
      (`markov_trace_product_recursion` is honestly conditional on
      `[MarkovTraceAxioms]`; `chainProduct_append` is a real list lemma).
      Checked: the existing vacuity audits catch `def X : True` and do NOT flag
      this pattern, so it is unrecorded.


---

## The MIXED chain closes: five numbers give `Delta_tr` for every atom

Probe: `computations/qbeta/qbeta_mixed_chain_closed_form_probe.py` (5/5).

**The form is derived, not guessed.** `atom_braid_word_3A` builds
`ordering = ['p']*Z + ['n']*N` and inserts the pp / pn / nn crossing at
generator `3k+2` for each `k < A-1` — read from the source. So `(Z,N)` carries
`Z-1` p-p bonds, one p-n bond, and `N-1` n-n bonds, giving one factor per bond:

```
tr_M(beta_atom(Z,N)) = t_p^Z . t_n^N . b_pp^(Z-1) . b_pn^[Z,N>=1] . b_nn^(N-1)
```

### `b_pp` is the Markov parameter

From the pure-proton chain, `b = tr_atom(A)/t_p^A` is constant in A:

| A | b (taking the (A−1)-th root) |
|---|---|
| 2 | 0.61268803714646479409 |
| 3 | 0.612688037146464828 |
| 4 | 0.61268803714646537953 |
| | **z = 0.6126880371464652516** |

`b_pp - z = -4.6e-16`. **One number read off the chain lands on a constant the
framework already defines**, to sixteen digits. Not fitted to it.

    b_pn = 0.50822978937673896258     (from 2H)
    b_nn = 0.40362773835082593617     (from 3H)

### Held out

| atom | predicted | measured | rel |
|---|---|---|---|
| ³He | 0.403767036851427869 | 0.40376703685142817 | 7.5e-16 |
| ⁴He | 0.160974145442407262 | 0.160974145442407382 | 7.5e-16 |

Two parameters fixed on two atoms; the other two are predictions, residual at
the float64 floor of the measured inputs.

### The consequence

```
Delta_tr(Z,N) = t_p^Z t_n^N . (1 - b_pp^(Z-1) b_pn^[Z,N>=1] b_nn^(N-1))
```

**Five numbers give `Delta_tr` for every atom.** No matrices at any A — so the
`n >= 15` dimension wall recorded above does not bear on the question it was
blocking. And it reconciles with the homogeneous derivation: `t_p . z =
0.7019932570132013578` against the symbolically derived `r =
0.70199325701320135779`, so the earlier `r(q)` is `t_p(q) . z(q)` and the two
routes agree.

### 🛑 What is derived and what is not

**Derived:** the form (chain structure + Ocneanu multiplicativity over disjoint
strand ranges); `t_p`, `t_n` as H₃ traces; `b_pp = z` as an *identification*
holding to 4.6e-16 rather than an imposition.

**Not derived:** `b_pn` and `b_nn` are extracted from ²H and ³H. They should
yield to the same exact-Laurent treatment that produced `r(q)`. Until that is
done they are two measured constants, and calling the whole thing "closed form"
without this caveat would make it a fit with two knobs.

## Todo (revised)

- [x] **Derived 2026-09-03 — zero fitted constants remain.** See below.
- [ ] **Owner:** which of the two extensive scales is the prediction
      (1.2309 vs 0.2253 MeV/nucleon)? Now more pressing — with `Delta_tr(Z,N)`
      in closed form, "energy per nucleon" can be stated exactly rather than
      estimated from four atoms.
- [ ] `QOU/Hecke/MarkovTraceProduct.lean`'s `markov_trace_product` is vacuous
      (unchanged; the existing vacuity audits do not catch this pattern).


---

## All five constants DERIVED — the knobs are gone

Probe: `computations/qbeta/qbeta_bond_factors_derived_probe.py` (7/7). Same
exact-Laurent route that produced `r(q)`.

```
t_p  = (q^22+q^20+2q^18+2q^16+3q^14+2q^12+q^10-q^8-q^4-q^2-1) / (4q^9(q^2+1)^2)
t_n  = (q^18-q^16+2q^14-2q^12+4q^10-3q^8+3q^6-2q^4+q^2-1)     / (4q^9)
b_pp = q^3/(q^2+1)
b_pn = (q^10-2q^9+7q^8-2q^6+4q^5+4q^4+q^2-2q+1)               / (12q^5(q^2+1))
b_nn = 1/(q^3+q)
```

All five reproduce their measured values to `~1e-20`, and the closed form
reproduces `Delta_tr` for all four atoms to **1e-35**.

### Three identities, each simplifying to exactly zero

| | |
|---|---|
| `b_pp - z` | **0** — the p-p bond factor **IS** the Ocneanu parameter. The previous probe could only say it matched to 4.6e-16. |
| `b_pp/b_nn - q^4` | **0** — the two same-species bond factors differ by exactly `q^4`, and `b_nn = 1/(q(q^2+1))` is the simplest of the five. |
| `r_previous - t_p . z` | **0** — `r_previous` came from the homogeneous chain, derived from *different words in a separate computation*. Two independent derivations agreeing symbolically is the strongest available check that neither is an expansion artefact. |

### A trap this method could have fallen into

The builder emits four shift values, and two of them —
`-h/2` (colour-BLIND) and `-h(1/2-delta/4)` (colour-WEIGHTED, with
`delta = (q-1)^2(1-q^-4)/3`) — differ by only **7.2e-5** at `q_0`
(`-0.104530149` against `-0.104458248`). A loose matcher would silently map the
colour-weighted p-n shift onto the colour-blind one and return a `b_pn` that
still looked plausible. The probe asserts the four are separable before matching
and matches at `1e-25`.

### The result

```
Delta_tr(Z,N) = t_p^Z t_n^N (1 - b_pp^(Z-1) b_pn^[Z,N>=1] b_nn^(N-1))
```

an exact rational function of `q` for **every** atom — no fitted constant, no
matrices, no dependence on the `n >= 15` wall.

### 🛑 What this does not say

It derives the CONSTANTS of a form whose structure was established and validated
earlier (held-out ³He and ⁴He at 7.5e-16). It does **not** say the binding law is
right. `Delta_tr` is what the law evaluates; how far that sits from `B` is the
open physics question, and the deficit measured at 5.1 → 32.3 per nucleon is
untouched by any of this.

## Todo (revised)

- [ ] **Owner:** which of the two extensive scales is the prediction
      (1.2309 vs 0.2253 MeV/nucleon)? Now fully answerable — `Delta_tr(Z,N)` is
      exact in `q`, so "energy per nucleon" can be stated as a closed form
      rather than estimated from four atoms.
- [x] **Done 2026-09-03 — the whole AME2020 table, and it changes sign.** See
      below.
- [ ] `QOU/Hecke/MarkovTraceProduct.lean`'s `markov_trace_product` is vacuous
      (unchanged; the existing vacuity audits do not catch this pattern).


---

## The framework against ALL 3554 nuclides — it CROSSES the data near A = 150

Probe: `computations/qbeta/qbeta_full_ame_scan_probe.py` (6/6). Until now the
binding law had only ever been evaluated on four atoms, because anything larger
needed seminormal matrices at `n = 3A`. The closed form makes the whole table
instant.

| A | Z | N | B_AME (MeV) | B_pred (MeV) | B/B_pred |
|---|---|---|---|---|---|
| 2 | 1 | 1 | 2.225 | 0.4354 | 5.109 |
| 4 | 2 | 2 | 28.296 | 0.8761 | 32.30 |
| 12 | 6 | 6 | 92.162 | 1.643 | 56.10 |
| 20 | 9 | 11 | 154.403 | 2.324 | 66.43 |
| 40 | 18 | 22 | 343.810 | 6.906 | 49.78 |
| 56 | 25 | 31 | 489.347 | 16.02 | 30.54 |
| 100 | 43 | 57 | 859.512 | 134.6 | 6.384 |
| 150 | 63 | 87 | 1236.202 | 1413.6 | **0.8745** |
| 208 | 84 | 124 | 1630.586 | 15600 | 0.1045 |
| 238 | 94 | 144 | 1801.270 | 47529 | **0.0379** |

**The deficit changes SIGN.** It rises on the light flank, and the heaviest A
whose median ratio still exceeds 1 is **A = 150**; by ²³⁸U the framework
**overshoots by a factor of 26**. **1641 of 3554 nuclides are overshoots (46 %).**

Worst undershoot over the whole table: **A = 39, Z = 11, N = 28 at 95.45x** — a
very neutron-rich sodium isotope, not on the median slice. (The 66x at A = 20 is
a median, not a maximum; only the 95.45x is a bound.)

### Why: an exponential crossing a line

`Delta_tr` is dominated by `t_p^Z t_n^N` with `t_p = 1.1458 > 1`, so `B_pred`
grows **exponentially in Z** while real binding grows roughly **linearly in A**.
Two such curves cross exactly once, and they do.

### What it settles

Three claims resting on the four light atoms are now visibly artefacts of where
those atoms sit — all six A ≤ 4 nuclides lie **below** the deficit peak, on the
rising flank:

* *"the framework supplies 8–20 % of binding"* — false above A ~ 150, where it
  supplies **more than 100 %**.
* *"the missing term must be added"* — for nearly half the table it would have
  to be **subtracted**.
* *"`Delta_tr` is extensive"* — already withdrawn on the closed form; this is the
  same fact seen against data.

### 🛑 Scope

Nothing is refuted about the **algebra**: the closed form reproduces every
measured `Delta_tr` to 1e-35 with no fitted constant. What is measured here is
the fit of `B = Q_beta . Delta_tr` to nature, and it fails in two opposite
directions on either side of A ~ 150. Entries with non-positive `B_AME` or
`B_pred` are excluded and counted, not silently dropped.

## Todo (revised)

- [ ] **Owner:** the two extensive scales (1.2309 vs 0.2253 MeV/nucleon) — and
      now a sharper question behind it. With the law overshooting half the
      table, "how far off is the extensive term" has no single answer; the sign
      of the error depends on A.
- [x] **Settled 2026-09-03: no regime of validity.** See below.
- [ ] `QOU/Hecke/MarkovTraceProduct.lean`'s `markov_trace_product` is vacuous
      (unchanged; the existing vacuity audits do not catch this pattern).


---

## No choice of scale rescues the law — 4.59 decades at the OPTIMUM

Probe: `computations/qbeta/qbeta_no_regime_of_validity_probe.py` (5/5).

`Q_beta` enters `B = Q_beta . Delta_tr` only as an overall scale, so the
question is whether the A ~ 150 crossover is structural or an accident of that
constant. Settled by finding the **best possible** scale and showing it fails —
the optimum is computed in order to be refuted, which is the opposite of a fit.

### The constant is not the problem

| | |
|---|---|
| optimal scale (geometric mean of `B/Delta_tr`) | **0.9482640138 MeV** |
| corpus `Q_beta` | 0.7823334093 MeV |
| ratio | **1.2121** |

The corpus value is already within 21 % of the best a single scale can achieve.

### And no scale works

With that optimal scale the residual `B/(scale . Delta_tr)` still runs

```
min 0.00201403    max 78.7504    max/min = 39101   =  4.59 DECADES
```

A one-parameter scale multiplying an exponential cannot track a roughly linear
function. Multiplying by a constant slides the curve; it cannot change that one
side grows like `t_p^Z` and the other like `a_V A`.

### So the crossover LOCATION is not structural

Along fixed `N/Z` the growth per proton is `c = ln t_p + (N/Z) ln t_n`, with
`ln t_p = +0.1360679039`, `ln t_n = -0.01233203987`:

| N/Z | c per proton | 10× scale moves Z* by | ΔA |
|---|---|---|---|
| 1.0 | 0.12373586 | 18.61 | ~37 |
| 1.2 | 0.12126946 | 18.99 | ~42 |
| 1.5 | 0.11756984 | 19.58 | ~49 |

"The law works near A = 150" is a property of the chosen `Q_beta`, movable by
~40 mass units per decade. What **is** structural is that a crossover exists at
all: `c > 0`, so an exponential and a line cross exactly once whatever the
constants.

### 🛑 The conclusion

**`B = Q_beta . Delta_tr` has no regime of validity in A.** It can be made to
agree at isolated points by choosing the scale, and then fails on both sides.
Agreement at any particular A is a coincidence of the calibration, not evidence
of a working law there.

### Scope — the algebra is untouched

`Delta_tr(Z,N)` is closed-form, derived with **zero fitted constants**, and
reproduces every measured value to 1e-35. What is refuted is the physical ansatz
that binding is a constant times that quantity. Whether some *other* functional
of the same operator works is untouched — and this arc's earlier results
constrain that: the missing piece is not a reweighting (`qou-bmz8`), not
reachable by larger `N` (`qou-fvzm`), and not in the interface subalgebra
(`qou-bmz8` deciding test).

## Todo (revised)

- [ ] **Owner:** the two extensive scales question is now answered in a way that
      dissolves it. Neither 1.2309 nor 0.2253 MeV/nucleon is "the" prediction,
      because no single scale is: the best possible one leaves 4.6 decades. The
      live question is whether `B = scale . Delta_tr` should remain the stated
      law at all.
- [ ] `QOU/Hecke/MarkovTraceProduct.lean`'s `markov_trace_product` is vacuous
      (unchanged; the existing vacuity audits do not catch this pattern).

**2026-09-04 — the arc's terminus.** The multiplicative law is closed
(`qbeta_no_regime_of_validity_probe.py`: 4.59 decades at the optimum) and the
replacement is measured: `B = E_0 . log(tr_M(free)/tr_M(atom))`, p5-p95 spread
**1.225x** vs **1592x** over the 2548 AME nuclides with measured binding
energies, consuming the SAME derived bond factors. `log` is the unique
multiplicative-to-additive map, so it is forced rather than chosen.

Knot-dependence of the scale is answered NO on three counts: the atom object is
not in `rho(B_n)` so there is no writhe (2A+1 averaged letters, `2^(2A+1)` branch
links); every derived `mu^(3A-1)` rate misses the required -0.0619/nucleon by
>=23.8x with the right sign, or has the wrong sign; and the scale that would work
regresses onto `-ln t_p` / `-ln t_n`, i.e. the trace's own output inverted, which
is a fit and is refused.

Options, pros/cons and six open avenues:
`docs/audits/2026-09-04-binding-law-options-decision-frame.md`. Carried to `gm4q`
(claimed), which is where the owner decision sits.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] title "HEADLINE WITHDRAWN — see the closed form"; superseded; STALLED in-progress since 2026-09-03 [M]
