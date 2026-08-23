# Red-team: is α_em "derived from q₀", or a selected-crossing fit conditional on an open κ?

**Date:** 2026-08-22
**Author:** adversarial audit agent (read-only; Critical-distance license, AGENTS.md)
**Scope:** the framework's claimed derivation of the fine-structure constant
`α_em⁻¹ ≈ 137.036` from the Hecke substrate. Fifth in the red-team series
(`2026-08-16-ck-ladder-red-team.md`, `2026-08-22-mK-mpi-l2-red-team.md`,
`2026-08-22-avol-binding-redteam.md`, `2026-08-22-mp-fbor-massformula-redteam.md`).

**Standing on the shoulders of the corpus's own honesty.** Unlike the four
prior red-teams, this one does **not** find an over-claim live on `main`. Beans
`qou-gwio` and `qou-93ap` already record the −467.6 ppb structural gap; PR #5361
already corrected a false "resolved at 6.7 ppb" claim in `DERIVATION-STATUS.md`;
the deprecated PSLQ forms are already labelled "DO NOT REVIVE"
(`2026-06-10-alpha-em-legacy-empirical-forms.md`). This doc **consolidates** that
honest state into one DOF-vs-precision ledger, and adds **two new findings** the
existing docs miss (the δ_q(T_{3,5}) linchpin, and the internal selection-rule
inconsistency in the meson EM factor).

---

## TL;DR verdict

**"α_em derived from q₀" is honest only at the ~0.15 % level, and no route reaches
CODATA precision without a ruled-out fit.**

- The **bare** form `α_em⁻¹ = q·[9]_q·[10]_q = 136.8232` is a genuine 1-parameter
  structural postdiction to **0.155 %** (3 significant figures). The crossing
  pair **(9,10) is Diophantine-forced** — this is real, and materially stronger
  than the m_K (3,4) pair, which was a scan hit. But the forcing rests on three
  modeling choices *and* one **unverified linchpin** (see finding 1).
- Every attempt to close the remaining 0.15 % splits cleanly into two piles, with
  an **inverse correlation between precision and honesty**:
  - **structural forms** (bare; the Chern–Simons resummed tower) → best case
    **−467.6 ppb**, i.e. **~300× outside** CODATA's 1.5 ppb error bar;
  - **CODATA-precision forms** (the `45[3]_q(1+δ_CS+8q·δ_CS²)` PSLQ form, 2.6 ppb;
    the legacy "6.7 ppb") → **ruled out** as single-point fits with post-hoc
    integer factors.
- **No Lean file proves the value.** All three routes are class-axiomatized
  conjectures with **no instance** (the honest open state), or carry the CODATA
  match itself as an *assumed hypothesis*. The m_K red-team's "conditional on an
  open Witten-κ sorry" is accurate in substance: the Gram-determinant κ is an
  `opaque` Prop with no instance. Axiomatization is not a proof.

**Bottom line:** the *bare* q·[9]_q·[10]_q is a legitimate, quotable ~0.15 %
categorical postdiction of α_em⁻¹, and (9,10) is genuinely forced modulo modeling
— that is a real and unusual result. But **"α_em derived from q₀ [to its known
precision]" is NOT honest.** The last 468 ppb has never been closed by structure;
it has only ever been closed by fits that the corpus itself rules out.

---

## The live formulas (grep-confirmed on `main`)

Three distinct forms coexist. All share the same bare core.

| # | Form | value at q₀ | vs CODATA | status |
|---|------|-------------|-----------|--------|
| bare | `α_em⁻¹ = q·[9]_q·[10]_q` | 136.8232089 | −0.155 % (−1.55×10⁶ ppb) | **derived** (algebraic) |
| CS-tower | `bare·(1 + c₁/(1 − c₁κ))` | 137.0359351 | **−467.6 ppb** | derived-structural, **misses** |
| fixed-point | cubic `P(α)=0`, `α⁻¹ = bare + 2/(3π) + α·H·(1−h²α)` | root ≈ CODATA | assumes CODATA | **conditional, no instance** |
| ~~gluon-octet~~ | `45·[3]_q·(1+δ_CS+8q·δ_CS²)` | 137.035944 (2.6 ppb) | 2.6 ppb | **RULED OUT** (PSLQ fit) |

- Producer: [`computations/meson_em_sinh_closed_form.py`](../../computations/meson_em_sinh_closed_form.py)
  (`_alpha_em_inv_derived`, exact resummation); witness
  [`meson-em-sinh-closed-form.witness.json`](../../computations/meson-em-sinh-closed-form.witness.json)
  (`alpha_em_inv_derived_exact = 137.035935093976`,
  `alpha_em_source = "derived (q·[9]_q·[10]_q dressed by the CS tower); NOT the experimental value"`,
  `cs_tower_converges_but_not_to_measurement = true`).
- Content: [`prop:em-coupling-projection`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-projection.md)
  (bare), [`prop:alpha-em-categorical-trace-ratio`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-categorical-trace-ratio.md)
  (trace-ratio), [`prop:force-carrier-bring-uniqueness`](../../content/quantum-observable-universe/predicted-spectra/force-carrier-bring-uniqueness.md)
  (the (9,10) forcing).
- Lean: [`em-coupling-chern-simons.lean`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.lean),
  [`em-coupling-fixed-point.lean`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-fixed-point.lean).

---

## (a) Every ingredient traced: derived / calibration / selected-knob

### The bare form `q·[9]_q·[10]_q`

| Ingredient | Origin claimed | Verdict |
|---|---|---|
| `q` (= q₀) | CAL-2 substrate modulus | **calibration input** (legit; the one input) |
| `9, 10` | crossing numbers of T_{2,9}, T_{3,5}, the genus-4-saturating torus knots on Bring's Σ₄ | **forced modulo modeling** (see finding 1) |
| `q^{-1}` prefactor | the singlet idempotent `e₋` normalization | **modeling choice** |
| product `[9]_q·[10]_q` | "force-carrier categorical complexity" = product of the two crossings | **modeling choice** (why the *product*?) |

### The Chern–Simons resummed tower (the −467.6 ppb form)

`c₁ = (CS(T₂,₉)+CS(T₃,₅))·([2]_q/2)·(1−q⁻¹)²/bare`, `κ = det G_cl / det G_q`.

| Ingredient | Value / origin | Verdict |
|---|---|---|
| CS(T_{2,9}), CS(T_{3,5}) | `π²(m²−1)(n²−1)/(12mn)` = 10/9·π², 16/15·π² | derived-from-selected-knots |
| `[2]_q/2` factor | asserted | **selected knob** |
| `(1−q⁻¹)² = ℏ_q²` | substrate Planck² | modeling choice |
| `sl = 8` (self-linking) | `(m−1)(n−1)` for T_{2,9} | **selected** |
| `linking = 17` | `|2·5 − 3·9|` | **selected combination** |
| 2×2 Gram matrices G_cl, G_q | bespoke Chern–Simons pairing on Σ₄ | **selected construction** (κ ≈ 1.72) |

**~6 discrete structural choices** beyond the bare pair, and the result is still
−467.6 ppb. The construction *converges* (the tower is geometric, ratio c₁κ ≈
2.7×10⁻³) — but "converges" is not "converges to the measurement." The witness
says so explicitly.

### The fixed-point cubic

`α⁻¹ = q·[9]_q·[10]_q + 2/(3π) + α·H·(1−h²α)`, `H = [2]_q/(8π)`. Ingredients:
`2/(3π)` Bring zero-mode (proved sorry-free upstream), `8π = π·b₁` (b₁ = dim
H¹(Σ_Bring), proved), Habiro `(1−h²α)` (PR #1511). **The O(α²) normalization
`H = [2]_q/(8π)` as a B₃(ℂ) Bloch class is the sole open conjectural input** — and
the class *also* carries `codata_consistent : |1/α − 137.035999177| < 1e-3` as a
**field**, i.e. the CODATA match is a hypothesis, not a conclusion.

---

## (b) DOF-vs-precision accounting

CODATA 2022: **137.035999177(21)** — 12 sig figs, relative uncertainty **1.53 ppb**.

| Form | discrete integers/structures beyond q₀ | reproduces | miss | inside CODATA bar? |
|---|---|---|---|---|
| bare `q[9]_q[10]_q` | 1 forced pair {9,10} + q^{−1} | ~3 sig figs | **0.155 %** | no (×10⁶) |
| bare + `2/(3π)` | + 1 zero-mode | ~4 sig figs | −4260 ppb | no (×2800) |
| CS-tower resummed | + ~6 (κ, sl, linking, CS knots, [2]_q, ℏ_q²) | ~6 sig figs | **−467.6 ppb** | **no (×305)** |
| `45[3]_q(1+δ_CS+8qδ_CS²)` | 4 factors (only "45" derived) | ~9 sig figs | 2.6 ppb | yes — but **RULED OUT** (fit) |

**The pattern is the whole story:** precision improves monotonically with added
structural DOF (136.82 → 137.0353 → 137.0359) and then **plateaus at −468 ppb**.
The only forms that cross into CODATA territory are the PSLQ single-point fits,
whose extra integer factors (`[3]_q`, `ℏ_q⁴[5]_q`, `8q`) are post-hoc and which
disagree with the structural forms at every q ≠ q₀ — the signature of a
zero-crossing fit, not an identity. Adding *honest* structure cannot close the
last 468 ppb; adding a *fit* can, and the corpus correctly refuses to.

---

## Two new findings (not in the existing docs)

### Finding 1 — the δ_q(T_{3,5}) = q¹⁰ − q⁻¹⁰ linchpin is UNVERIFIED, and the actual Jones invariant is *not* a clean binomial

The trace-ratio derivation
([`alpha-em-categorical-trace-ratio.md`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-categorical-trace-ratio.md))
gets `[10]_q` from the assertion:

> "For the 3-strand torus knot T_{3,5}, the Rosso–Jones formula … Summing the
> contributions from V_(3), V_(2,1), V_(1,1,1) with their respective eigenvalue
> powers **yields** δ_q(T_{3,5}) = q^{10} − q^{−10} = h·[10]_q."

For the **2-strand** T_{2,9} this collapse is genuine: the unnormalized 2-strand
Markov trace is `q^k·1 + (−q⁻¹)^k·1 = q^9 − q⁻⁹` for odd k — a real binomial. For
the **3-strand** T_{3,5} the analogous sum runs over *three* irreps with distinct
q-dimension weights and eigenvalue powers, and generically is a multi-term Laurent
polynomial. The block asserts the clean binomial but **does not show the 3-term
sum**. The standard Jones polynomial of T(3,5) is (symbolically, exact):

```
V(T_{3,5})(t) = t⁴ + t⁶ − t¹⁰      (a genuine 3-term polynomial, NOT q¹⁰ − q⁻¹⁰)
```

That the *only* invariant of T_{3,5} needed for α_em happens to be the clean
`[10]_q` — whose exponent equals the knot's crossing number, exactly paralleling
the (legitimate) T_{2,9} case — is the load-bearing, unverified step. **This is
where "10" could be reverse-engineered from the crossing number** rather than
derived from the actual 3-strand Rosso–Jones trace. Until the explicit 3-term
sum is shown to collapse to `h·[10]_q`, `[10]_q` should be tiered
**asserted, not derived** — and the whole "(9,10) is Diophantine-forced" claim
inherits this caveat, because the Diophantine argument only fixes the *knots*
{T_{2,9}, T_{3,5}}; it does not by itself say the α_em observable is
`[crossing]_q · [crossing]_q`.

*(The Diophantine step itself I confirm is real: genus g(T_{p,q}) = (p−1)(q−1)/2 =
4 ⟺ (p−1)(q−1) = 8, and with p<q coprime the only solutions are (2,9) and (3,5).
So IF force carriers = genus-4-saturating torus knots AND the observable is the
product of their crossing-number q-integers, then {9,10} is forced. Two IFs and a
linchpin.)*

### Finding 2 — the meson EM factor `(3q²−1)/(2q²)` uses a *different, inconsistent* selection rule for its "3"

The producer docstring and `2026-05-28-meson-mass-ratio-derived-vs-fitted.md`
read the numerator `3q²−1` as "**3** = the three generation torus knots
**T(2,3), T(2,5), T(2,7)** on Bring's surface." Those are the **genus-1, 2, 3**
2-strand knots — a *completely different* selection principle from the force-carrier
rule, which selects the **genus-4** knots {T_{2,9}, T_{3,5}}. The same document,
in the same sector, invokes "the same Diophantine uniqueness that fixes the
force-carrier set" to justify the "3" — but the force-carrier set is genus-4 and
these are genus-1/2/3. This is a post-hoc structural gloss on a rational
polynomial that was found by series-truncation (`1 + ℏ_q − ℏ_q²/2`, the first
three terms of `1 + log(1+ℏ_q)`), not a derivation. Tier the `(3q²−1)/(2q²)`
factor **fitted/post-hoc**, consistent with `2026-08-22-mK-mpi-l2-red-team.md`.

---

## (c) Tiered verdict per piece

| Piece | Tier | Reason |
|---|---|---|
| `q₀` as the single input | **calibration** | legit CAL-2 |
| Diophantine {T_{2,9}, T_{3,5}} from genus 4 | **derived** | (p−1)(q−1)=8, gcd=1 ⟹ exactly these two — verified |
| observable = `q·[9]_q·[10]_q` (product of crossings) | **modeling choice** | why the product; why crossing-number q-integers |
| `[10]_q = δ_q(T_{3,5})/h` | **asserted, NOT derived** | actual Jones of T(3,5) is 3-term; collapse to binomial unshown (finding 1) |
| bare value 136.823 (0.155 %) | **derived postdiction** | genuine, quotable at ~0.15 % |
| CS tower (κ, sl, linking, …) | **selected knobs** | ~6 discrete choices; still −468 ppb |
| `(3q²−1)/(2q²)` meson EM factor | **fitted/post-hoc** | truncation + inconsistent "3-generations" gloss (finding 2) |
| `45[3]_q(1+δ_CS+8qδ_CS²)` (2.6 ppb) | **ruled out** | single-point PSLQ fit; off-q₀ disagreement |
| Lean value proof | **not proved** | opaque/class, no instance; or assumes CODATA |

---

## (d) The open κ / no-instance state — Lean audit

| Lean object | File | State |
|---|---|---|
| `ChernSimonsGramDeterminantIdentityHolds` | em-coupling-chern-simons.lean | `opaque … : Prop`, **no proof** |
| `ChernSimonsCorrectionConjecture` | " | `class`, **no instance** (history: was an `axiom` — laundering, removed) |
| `AlphaEmGluonOctetConjecture` | " | `class` with `matches_codata` field, **no instance**; deprecated form |
| `AlphaEmFixedPointNormalization` | em-coupling-fixed-point.lean | `class` with `b3_normalization` **and** `codata_consistent` fields, **no instance** |
| `alpha_em_is_fixed_point_root` | " | sorry-free **theorem**, but *conditional* on the class above, which **assumes** CODATA |

So the m_K red-team's phrasing "α_em is conditional on an open Witten-κ `sorry`"
is correct in substance. The current spelling is cleaner than a `sorry` — an
`opaque` Prop with no instance is the honest open state per AGENTS.md §3b-tax —
but functionally it is the same: **the Gram-determinant κ that would turn the
bare form into the 137.0359 value is unproved**, and even if proved it lands at
−468 ppb, not CODATA. The fixed-point route's `codata_consistent` field is the
sharper concern: a "theorem" whose class *hypothesis* is "the answer is CODATA"
proves nothing about the value; it is the §3b-cond structure being used to carry
the empirical target rather than derive it. (The non-degeneracy check passes —
the theorem derives `P(α)=0`, not the CODATA field — so this is not a vacuous
self-projection; but it is also not evidence for the value.)

---

## (e) Blunt bottom line

Deriving α_em parameter-free would be extraordinary, so hold it to an
extraordinary-evidence bar. Against that bar:

1. **The bare `q·[9]_q·[10]_q = 136.82` is a genuine ~0.15 % structural
   postdiction, and (9,10) is genuinely forced modulo modeling — that is real,
   and it is *better* than the m_K (3,4) scan hit.** Quote it as such: a
   3-significant-figure categorical postdiction of α_em⁻¹ from one calibration
   input, with the crossing pair Diophantine-selected. That much is honest and
   unusual.

2. **But "α_em derived from q₀" — meaning to its known precision — is NOT
   honest.** The known value is good to 1.5 ppb; the best *structural* form
   misses by 468 ppb (~300× the bar) and cannot be pushed further without a fit;
   the only fits that reach CODATA precision are ruled out. There is a clean
   inverse correlation across the whole family: **structure ⟺ imprecision, fit
   ⟺ precision.** That is exactly the signature of a formula whose leading term
   is real physics and whose sub-percent tail is being chased by numerology.

3. **The corpus already knows this** (beans `qou-gwio`, `qou-93ap`; PR #5361;
   the legacy-forms deprecation) — no live over-claim was found on `main`, which
   is to the framework's credit. This red-team's *new* contributions are the two
   findings above: the **δ_q(T_{3,5}) = q¹⁰−q⁻¹⁰ linchpin is unverified** (the
   actual Jones of T(3,5) is 3-term, so `[10]_q` may be crossing-number-matched
   rather than derived), and the **meson EM factor's "3 generations" gloss uses
   a selection rule inconsistent with the force-carrier rule it cites.**

**If (9,10) is genuinely forced, it is a big deal — but it is forced only *given*
that the α_em observable is the product of the two crossing-number q-integers,
and *given* the unshown δ_q(T_{3,5}) collapse. Close those two and the bare
0.15 % postdiction becomes a real derivation of the leading term. The remaining
468 ppb is, on all current evidence, not derivable from this structure.**
