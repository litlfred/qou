---
# qou-fivt
title: 'Prove the three numerators 17, 5, −1 by five-term/Abel — the route that AVOIDS the Bloch group'
status: completed
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - lean
created_at: 2026-08-07T18:05:00Z
updated_at: 2026-08-07T19:20:00Z
parent: 0yqu
---


## The target

From `qou-b7cy` (Route 9), verified at 100 dps with residuals `~1e-101`, with
`wₖ = 1 + 2cos(2πk/7)` a root of `w³ − 2w² − w + 1`:

    Re[2L(wₖ) + L(−wₖ)]  =  mₖ · π²/42  =  (mₖ/7) · L(1),    m = (17, 5, −1)

`L` = Rogers dilogarithm. `Σ mₖ = 21`, `21/42 = 1/2`, which is Route 8's target
and hence the 5₂ sum rule. Denominator `42` verified minimal (all `d < 400` at
`1e-60`).

**Prove these three values.** That is the entire remaining mathematical content
of the sum rule.

## Why this bean, and not "formalize Borel"

`qou-mlbg` surveys Mathlib at the pinned rev and finds **zero** files mentioning
Bloch groups, the Borel regulator, polylogarithms, Rogers, or Steinberg, and no
`KTheory` directory at all. The Bloch–Borel argument of `qou-b7cy` is
*explanatory*: it tells you the values are rational and why. **It is not a path
to a Lean proof** — item 4 of that bean's roast (algebraic K-theory of number
fields + Borel's rank theorem) is a multi-year Mathlib project.

This route needs strictly less:

* a **real** `Li₂` on the relevant range — **QOU already has one**
  (`QOU.Archimedean.LiTwo`, with `LiTwo_reflection'` sorry-free on `(0,1)`),
* the Rogers `L` and its functional equations,
* no Bloch group, no K-theory, no Borel.

## What is already in hand

* **Reflection** `L(z) + L(1−z) = L(1) = π²/6` — the QOU `LiTwo_reflection'` is
  exactly this shape on `(0,1)`.
* **Duplication** `L(z²) = 2L(z) + 2L(−z)` — verified exactly per embedding
  (`qou-b7cy`), so `2L(w) + L(−w) = L(w) + ½L(w²)`. Either form may be the
  easier target.
* **The algebraic relation** `(1 − w)²(1 + w) = w²`, now **Lean-proved
  sorry-free** in `QOU/QBeta/FiveTwoCyclotomicBloch.lean` (`bloch_key`), and in
  the sharp form `bloch_poly`: the relation *is* the minimal polynomial. This is
  exactly the shape that generates Y-system / Frenkel–Szenes dilogarithm
  identities, which is the natural source of `mₖ/7` values.
* `w`, `1−w`, `1+w` are all **units** of `ℚ(ζ₇)⁺` (norms `−1, −1, +1`), with
  minimal polynomials `w³−2w²−w+1`, `u³−u²−2u+1`, `v³−5v²+6v−1` — the latter two
  Lean-proved (`minpoly_one_sub`, `minpoly_one_add`).

## ⚠ Branch care — do not skip

Only `w₂ = 0.5549…` lies in `(0,1)`. `w₁ = 2.2469… > 1` and `w₃ = −0.8019… < 0`,
so `Li₂` there is off the standard Rogers range and the *real part* is what the
identity is about. Any five-term manipulation must track which branch each term
sits on. **Related recorded failure:** in `qou-b7cy` a per-embedding formula
`V − L(ξ) = iπ·log[(1−w)/w]` was tried and is **FALSE** — it fails at two of the
three embeddings on exactly these grounds, while the *sum* is exact. Expect the
same trap here.

## Suggested attack

1. Reduce `2L(w) + L(−w)` to `L(w) + ½L(w²)` by duplication, then rewrite `w²`
   as `(1−w)²(1+w)` and look for a five-term configuration in `w`, `1−w`, `1+w`
   — all units, all with known minimal polynomials.
2. Compare against the classical level-7 ladder literature (Watson's identities;
   Loxton; the `A₂`/Y-system tables). Denominators of `7` in units of `L(1)` are
   that literature's signature. **`qou-g2wr` established GGM/GGMW do NOT contain
   this** — look at the ladder literature, not the resurgence papers.
3. Only after a paper proof exists, formalize — and note the branch handling will
   need the complex `Li₂` unless the argument is arranged to stay real, which is
   worth designing for from the start (it would dodge `qou-ph1k`/`qou-gkco` too).

## Honest prior

Nine routes tried on the parent bean; seven refuted, two reductions. This is the
first target that is a **finite, explicit, classical-shaped** statement rather
than an opaque constant — but "classical-shaped" is not "done", and the branch
structure is exactly where the last two attempts broke.

**Sum rule status: verified to 80 dps, unproved.**

## Refs

* parent `qou-0yqu`; `qou-b7cy` (Route 9), `qou-8v3k` (Route 8), `qou-mlbg` (the gap survey)
* `QOU/QBeta/FiveTwoCyclotomicBloch.lean` — the Lean-proved algebra
* PR #4658

---

## 2026-08-07 — MECHANISM IDENTIFIED: the numerators are a Bernoulli `B₂`

Probe `computations/probes/qbeta_5two_route10_kubert_distribution_probe.py`,
witness `computations/qbeta-5two-route10-kubert-distribution.witness.json`,
6 gates at 60 dps, all pass.

**The three numerators are not three constants.** They are a quadratic in `k`:

    mₖ = 3k² − 21k + 35        (and k ↦ 7−k symmetric, as cos(2πk/7) demands)

and that quadratic is a **Bernoulli polynomial**: `mₖ/7 = 21·B₂(k/7) + 3/2`
with `B₂(x) = x² − x + 1/6`.

`B₂` is the Fourier signature of the dilogarithm at roots of unity —
`Σₙ cos(2πnx)/n² = π²B₂(x)`, i.e. **`Re Li₂(ζ₇^k) = π²·B₂(k/7)`** (gate G2,
verified to 1e-61). And `wₖ = ζ₇^k + ζ₇^{−k} + 1` exactly (G3).

So the entire remaining content of the 5₂ sum rule is one **distribution
relation**:

> `Re[2·L(wₖ) + L(−wₖ)] = (7/2)·Re Li₂(ζ₇^k) + π²/4`,  `wₖ = ζ₇^k + ζ₇^{−k} + 1`

### Why this reframing is worth more than the numerators themselves

1. **It kills the "fitted" objection.** `17, 5, −1` looked like three lucky
   integers. They are one Bernoulli polynomial evaluated at `k/7`. Nothing is
   fitted.
2. **The hard-looking half is the elementary half.** `Re Li₂(ζ₇^k) = π²B₂(k/7)`
   is the cosine Fourier series of `B₂` — real analysis and `Cl₂`, **no complex
   `Li₂` continuation**. So this side does *not* depend on `qou-clx8`/`qou-ph1k`,
   and the corpus already has the `Cl₂` infrastructure from #4666
   (`summable_clausen`, `Cl_2_duplication`, `Cl_2_neg`, `Cl_2_add_two_pi` in
   `QOU/Archimedean/BlochWignerLobachevsky.lean`).
3. **It names the object.** "Prove three integers" becomes "prove a distribution
   relation" — Kubert / multiplication-relation territory, with standard
   technique, rather than a coincidence to be explained.

Note the pleasing symmetry with Route 4: that route *died* on the Kubert relation
(six new unknowns for one relation, applied at `Li₂(y²) = Li₂((1−y)³)`). The same
machinery reappears here in a form that nets positive, because Route 8 first
moved the problem to a field where the roots of unity are the natural arguments.

### ⚠ Still not a proof

The distribution relation is **verified, not derived** — same status as
everything upstream. **Sum rule: verified to 80 dps, unproved.**

### Next

Derive the relation. The `Re Li₂(ζ₇^k) = π²B₂(k/7)` half is standard and should
be attacked first, in `Cl₂` terms, since it is both the easier half and the one
already supported in the corpus. The remaining step then relates `L` at the real
unit `ζ₇^k + ζₜ^{−k} + 1` to `Li₂` at `ζ₇^k` — which is where the actual
multiplication relation lives.

### 2026-08-07 (later) — two structural facts for the derivation, and one honest negative

Gates **G7**, **G8** added to the Route-10 probe.

**G7 — the cyclotomic dictionary.** Every object a derivation needs, in `ζ = ζ₇`:

    w   = 1 + ζ^k + ζ^{−k}  =  ζ^{−k}·(1 − ζ^{3k})/(1 − ζ^k)  =  sin(3πk/7)/sin(πk/7)
    w²  = (1 + ζ^k + ζ^{2k})(1 + ζ^{−k} + ζ^{−2k})
    1−w = −(ζ^k + ζ^{−k})
    1+w = 4cos²(πk/7)

So `w` is a **ratio of cyclotomic numbers** and `w²` is a norm — which is why
`w`, `1−w`, `1+w` are units, and why the distribution relation is the right
frame.

**G8 — the Galois action is an order-3 Möbius map.** `1/wₖ = 1 − w_{k+1}`
cyclically, i.e. `w_{k+1} = 1 − 1/wₖ = T(wₖ)` with `T(x) = (x−1)/x`, `T³ = id`
(all verified to `~1e-61`). **The three embeddings are a single `T`-orbit**, so
the cyclic Galois group of ℚ(ζ₇)⁺ acts as the classical order-3 map whose Rogers
cocycle is the Landen/inversion relation.

**⚠ The honest negative, recorded so nobody mistakes the coincidence for a
derivation:** the `T`-orbit sum `Re[L(w) + L(Tw) + L(T²w)]` is the *same* for all
three `k` (it is one orbit) and is **irrational** — `0.27318…·π²`. So the 3-cycle
**alone does not produce the rational value**. The rational combination is
`2[w] + [−w]`, which is *not* the orbit sum. The Möbius structure is real and
probably load-bearing, but it is not by itself the proof.

**Still: verified to 80 dps, unproved.** The derivation is not done.

---

## ✅ 2026-08-07 — DERIVED. The three numerators follow from the five-term relation.

Probe `computations/probes/qbeta_5two_route11_fiveterm_certificate_probe.py`,
witness `computations/qbeta-5two-route11-fiveterm-certificate.witness.json`,
6 gates, all pass. **This bean's stated goal is met.**

### Step 1 — reduce to `(0,1)`

Only `w₂` lies in `(0,1)`. Using the three standard extensions of the real
Rogers dilogarithm — each **verified on generic points, not just our `w`s**:

    reflection  L(x) + L(1−x)     = L(1) = π²/6     (0 < x < 1)
    inversion   L(x) + L(1/x)     = 2·L(1)          (x > 1)
    Landen      L(x) + L(x/(x−1)) = 0               (x < 0)

everything reduces. With `a = L(w₂)`, `q = w₁/(1+w₁)`, `r = w₂/(1+w₂)`, `s = −w₃`
(and the pleasant accident `1/w₁ = w₃/(w₃−1) = 1−w₂`), the targets become, in the
basis `[L(1), a, L(q), L(r), L(s)]`:

    T₁ = (−3/7,  2, −1,  0, 0)      T₂ = (−5/7, 2, 0, −1, 0)      T₃ = (−13/7, 2, 0, 0, 1)

### Step 2 — the argument set is CLOSED under the five-term relation

`{w₂, q, r, s}` plus reflections is closed; **15** closed instances exist, of
which three are independent:

    R₁ (x=y=w₂)      : 2L(w₂) − L(1−q) − 2L(r)                  = 0
    R₂ (x=1−w₂, y=q) : L(1−w₂) + L(q) − L(1−q) − L(1−s) − L(w₂) = 0
    R₃ (x=w₂,  y=s)  : L(w₂) + L(s) − L(1−w₂) − L(1−s) − L(1−r) = 0

### Step 3 — the certificate (exact `Fraction` arithmetic)

    T₁ = (2·R₁ − 4·R₂ + 1·R₃)/7
    T₂ = (1·R₁ − 2·R₂ + 4·R₃)/7
    T₃ = (4·R₁ − 1·R₂ + 2·R₃)/7

`rank(R) = rank(R ∪ T) = 3`. The coefficient triples are cyclic shifts of
**`(1, 2, 4)` — the quadratic residues mod 7 — and that `1/7` is exactly where
the `mₖ/7` denominators come from.** The level-7 structure is visible in the
certificate itself.

### ⚠ What this does and does not settle

**Derived:** the three numerators `17, 5, −1`. Not fitted, not verified-only.

**NOT thereby proved: the sum rule.** The chain still runs through **Route 8's
analytic transport** — the envelope theorem along GGM's deformation plus the
branch integer `k = 0` on `|x| = 1`, which is *argued* (integrality + local
constancy on a collision-free arc) but **not proved**. **That is now the weakest
link, and it is analytic rather than arithmetic** — a different kind of gap from
the one this bean opened against.

Also: the three extension formulas are verified on generic points here, not
derived. They are standard, but this probe does not prove them.

### A dead end worth recording

Before finding the certificate, PSLQ over `[L1, a, L(q), L(r), L(s)]` returned
`[−4, 4, −3, 4, 3]`. **That relation is a linear consequence of the three targets
and carries no new information** — the `a` coefficient cancels (`4−6+8−6 = 0`) and
the remainder is `−4L(1) + 28π²/42 ≡ 0`. Numerical relation-hunting on this basis
will keep rediscovering it. The five-term closure is what actually supplies
independent equations.

**Next, and it is now the only mathematical gap:** make Route 8's transport
rigorous — see `qou-8v3k`.

---

## ✅ 2026-08-07 — Route 11's certificate is now LEAN-PROVED, sorry-free

`QOU/QBeta/FiveTwoLevelSevenLadder.lean`, built in-tree (707 jobs), axioms
`[propext, Classical.choice, Quot.sound]`, zero `sorry`:

| theorem | content |
|---|---|
| `numerators_of_five_term` | the three targets, from three five-term instances + reflection |
| `sum_of_numerators` | their sum, `21·L1` — Route 8's target, hence the sum rule |

`L` is **abstract** and reflection is an explicit hypothesis — the same style as
the corpus's `FiveTwoSaddleSumRule.lean`. So this depends on **no** dilogarithm
implementation, not on `qou-clx8`, and not on the Bloch group.

### Two corrections the formalisation forced

**1. My R-labels were permuted against the certificate coefficients.** The
`span.py` search returned rows in the order `[R₃, R₂, R₁]` relative to the labels
used in the write-up, so the published triples `(2,−4,1)/7` etc. were attached to
the wrong instances. Re-derived against the labels:

    7·T₁ =   hA − 4·hB + 2·hC
    7·T₂ = 4·hA − 2·hB +   hC
    7·T₃ = 2·hA −   hB + 4·hC

Still cyclic shifts of `(1,2,4)`, the quadratic residues mod 7 — the structural
claim survives; only the assignment was wrong. **Lean caught this**, because a
permuted certificate simply does not typecheck.

**2. The divided form is FALSE in characteristic 7.** Stating the targets as
`Tₖ = mₖ/7·L1` over a general `Field` fails — `ring` correctly refuses, since
`7 = 0` there. Clearing the `7` gives **integer** coefficients and the result
holds over any `CommRing`. A `Field` + `CharZero` version would also work, but the
cleared form is strictly more general and needs no typeclass at all.

That second point is worth keeping: the `/7` that looked like the interesting
arithmetic content is exactly the part that must be cleared to state the theorem
correctly.

**Still not proved:** the five-term relation itself, the inversion/Landen
extensions, and Route 8's transport (`qou-trns`). **Sum rule: verified to 80 dps,
unproved.**

### Characteristic 7: answered, and Lean-proved

Asked whether the statement can be rewritten to be true in characteristic 7. It
already is — the cleared form holds over any `CommRing`. But it is **degenerate**
there, and `char_seven_forces` now proves why rather than leaving it implicit:

> With `(7 : R) = 0`, the certificate combination `hA − 4·hB + 2·hC` — which
> equals `−3·L1 + 14·L w₂ − 7·L q` identically — collapses to `−3·L1 = 0`.
> **The hypotheses force `3·L1 = 0`.**

Over a field of characteristic 7 that gives `L1 = 0` (`3` is invertible mod `7`),
and every target reads `0 = 0`.

So the divided form cannot be rescued in characteristic 7, and for a sharper
reason than "`7⁻¹` does not exist": **the hypotheses are themselves inconsistent
with `L1 ≠ 0` there.** The cleared form is the honest statement — true
everywhere, with content exactly where `7` is invertible.

Three theorems in `FiveTwoLevelSevenLadder.lean`, all sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`: `numerators_of_five_term`,
`sum_of_numerators`, `char_seven_forces`.

### `numerators_original_form` — the Lean now covers Route 11 end to end

The earlier theorem started from the `(0,1)` form, so the reduction itself was
still only on paper. `numerators_original_form` closes that: from the **original**
`2·L wₖ + L(−wₖ)` to `mₖ·L1` (with the `7` cleared), taking the three extension
formulas as hypotheses at the points used —

    inversion at w₁ > 1 (with 1/w₁ = 1 − w₂),
    Landen at −w₁, −w₂, w₃  (images q, r, 1 − w₂),
    s = −w₃, already in (0,1)

plus reflection and the three five-term instances.

**Checked for vacuity before committing.** A theorem with unsatisfiable
hypotheses proves nothing, so all nine were evaluated against the real Rogers `L`
at the actual `wₖ`: every one holds to `≤ 3.4e-41`, and the conclusions
`7(2L wₖ + L(−wₖ)) = mₖ·L1` hold to `≤ 5.5e-40`. The hypotheses are satisfiable
and the statement has content.

Four theorems now, all sorry-free, axioms `[propext, Classical.choice, Quot.sound]`:
`numerators_of_five_term`, `numerators_original_form`, `sum_of_numerators`,
`char_seven_forces`.

---

## 2026-08-08 — CLOSED: the numerators are proved in Lean, unconditionally

This bean's route — derive `17, 5, -1` from five-term/Abel, avoiding the Bloch
group — is complete, and it did avoid the Bloch group entirely. `qou-mlbg` was
right that Borel is out of reach; this route never needed it.

```lean
numerators_of_root : x^3 - 2x^2 - x + 1 = 0 → 1/2 < x → x < 1 →
  7*(2*(π²/6) + 2*L x - L (1/(2-x))) = 17*(π²/6) ∧ … ∧ …
extended_sum      : … = π²/2
```

sorry-free, `lake` green, cross-checked numerically (residuals `< 5e-40`).

Two corrections to this bean's own record, both recorded in `qou-rstq`:

* the PSLQ dead end and the Galois 3-cycle dead end stand;
* but its advice "derive the `Re Li₂(ζ₇^k)` half first" was already superseded
  by Route 11 and is now definitively moot — the numerators were derived without
  ever evaluating `Li₂` at a root of unity.

---

## ⚠ 2026-08-08 — the level-7 ladder is CLASSICAL. Watson (1937).

Literature arrived (`library/arxiv-hep-th-9408113v2/9408113v2.pdf` — Kirillov, *Dilogarithm identities*,
hep-th/9408113). **§1.2.2 gives Watson's relations**, and they are this lane's.

Kirillov: let `α, −β, −1/γ` be the roots of `x³ + 2x² − x − 1 = 0`, with
`α = ½sec(2π/7)`, `β = ½sec(π/7)`, `γ = 2cos(3π/7)`. Then

    L(α) − L(α²) = (1/7)·L(1)
    2L(β) + L(β²) = (10/7)·L(1)
    2L(γ) + L(γ²) = (8/7)·L(1)

Under `x ↦ −x` his cubic **is** `x³ − 2x² − x + 1`, ours, and

    α = −w₃,   β = w₂,   γ = 1/w₁

verified to `1e-30` (`qbeta_5two_route18_watson_classical_probe.py`, 6 gates).

**So `numerators_of_root` formalizes a known identity family.** The
`(17, 5, −1)/7` are different combinations of the same `L`-values in the same
field `ℚ(ζ₇)⁺`, with the same denominator 7. This bean, and the commits behind
it, presented the numerators as "DERIVED" with a tacit implication of novelty.
**That implication was wrong and is withdrawn.**

### What remains this lane's

* **The route.** Kirillov proves accessibility from the **duplication formula**;
  this lane derived it from the **five-term relation**. Genuinely different.
* **The formalization.** Watson, Loxton, Lewin, Kirillov and Zagier all work on
  paper. `rogersL_fiveTerm`, `numerators_of_root`, `extended_sum` are sorry-free
  Lean, which the literature does not provide.

Both are worth having. Neither is a new theorem.

### Two further confirmations from Zagier (`library/the-dilogarithm-function-*.pdf`)

* **`FiveTwoRogersExtend.extend` is Zagier's definition verbatim** — `L(0)=0`,
  `L(1)=π²/6`, `L(x)=2L(1)−L(1/x)` for `x>1`, `L(x)=−L(x/(x−1))` for `x<0`.
  Route 13's repair was the standard one; now checked against the source rather
  than from memory.
* **`hasDerivAt_rogersL` is Zagier's `L′(x)` verbatim**, and he names exactly
  that formula as the route to "these and all other functional equations" —
  which is how Abel was proved here. The method was right for the documented
  reason.
