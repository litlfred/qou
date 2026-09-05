# The weak-vertex coupling normalisation, derived: it is the Jones–Markov relation

**Date** 2026-09-05 · **Bean** `qou-q2l7` · **PR** #6765 ·
**Branch** `claude/weak-vertex-jones-markov-derivation-2026-09-05`

**Predecessors.** `qou-egvf` derived the closed form
`W(q) = q²(q¹² + q⁸ − 1)/(q² + 1)²` (#6659). `qou-4x7c` corrected the content
blocks that quoted a buggy `0.7036` (#6689). `qou-ix74` measured that
substituting `|W|²` for the single-crossing coupling `s²` in the β-decay rate
multiplies every rate by `≈ 1.19·10⁴` (#6715). `qou-pfh7` **excluded** the
candidate family `c·(W − W(1))·bridge` — scope-(b), by proving the ratio runs —
and left one thing open: *what normalisation actually relates the two* (#6735).

This closes that. The normalisation is not a constant to be found. It is the
framing-and-rank factor of the Jones–Markov relation, and once it is named,
everything downstream is polynomial algebra over a generic field.

---

## 1. The rule, and that it is not fitted

For a braid word `β ∈ B_n` with exponent sum `e`, the canonical Markov trace of
its closure is

```
tr_M(closure β)  =  q^{2e} · V_{closure β}(q^{−2})  /  [2]_q^{n−1}
```

— a **framing** factor `q^{2e}` (the writhe correction, in the Jones variable
`t = q^{−2}`) and a **rank** factor `[2]_q^{n−1}` (the Markov normalisation
`tr_M(1) = 1` on `H_n`). Both are read off the braid word: `n` is the braid
index, `e` is the letter count with signs. There is no free parameter.

**This is checked, not asserted.** The producer evaluates both sides
independently — the left through the corpus's own trace engine
(`markov_trace_canonical.tr_M_word`, convention D `z = q³/(q²+1)`,
`h = q − q⁻¹`), the right through the classical torus-knot Jones formula — on
eight knots:

| knot | `n` | `e` | `V(t)` | rule |
|---|---|---|---|---|
| T(2,3) | 2 | 3 | `t + t³ − t⁴` | ✓ |
| T(2,5) | 2 | 5 | `t² + t⁴ − t⁵ + t⁶ − t⁷` | ✓ |
| T(2,7) | 2 | 7 | `t³ + t⁵ − t⁶ + t⁷ − t⁸ + t⁹ − t¹⁰` | ✓ |
| T(3,4) | 3 | 8 | `t³ + t⁵ − t⁸` | ✓ |
| **T(3,5)** | **3** | **10** | **`t⁴ + t⁶ − t¹⁰`** | ✓ |
| T(3,7) | 3 | 14 | `t⁶ + t⁸ − t¹⁴` | ✓ |
| T(4,3) | 4 | 9 | `t³ + t⁵ − t⁸` | ✓ |
| T(5,3) | 5 | 12 | `t⁴ + t⁶ − t¹⁰` | ✓ |

Spanning `n = 2, 3, 4, 5` and including the mirror pairs T(3,4)/T(4,3) and
T(3,5)/T(5,3) — the same knot presented at two different braid indices, where
`n` and `e` both change and the rule still holds. That is what makes it a rule
rather than a coincidence at one word.

For the weak vertex, `n = 3` and `e = 10`:

```
W · [2]_q²  =  q¹² + q⁸ − 1  =  q²⁰ · J,      J := V_{T(3,5)}(q^{−2})
                                                 =  q^{−8} + q^{−12} − q^{−20}
```

Lean: `weakVertexTrace_mul_twoQ_sq`, `jones_framing_eq_numerator`,
`weakVertexTrace_eq_jones_markov` (all sorry-free, generic field).

---

## 2. Why that removes the free constant

`V_K(1) = 1` and `V′_K(1) = 0` for **every** knot `K` (both checked on all
eight above). Therefore

```
J − 1
```

is the *canonically normalised* deviation of the weak vertex from its classical
value: the offset is `1` and the vanishing order is `2`, and both are
topological facts rather than choices. There is nothing left to rescale — which
is precisely what the excluded family was missing.

**And it says why `W − W(1)` could not work.** `W(1) = 1/4` is the Markov rank
factor `[2]_1^{n−1} = 4` showing through, not a knot invariant. `W − W(1)`
subtracts a *normalisation artefact*; `J − 1` subtracts the *invariant's* value.
That is the substantive difference between the two candidates, and it is why one
vanishes to first order and the other to second.

---

## 3. The coupling is a product of two q-differences

Exactly, with `h_k := q^k − q^{−k}`:

```
J − 1  =  − h₄ · h₆ / q¹⁰
```

The exponents `4` and `6` are the two Jones exponents of T(3,5); `q^{−10}` is
the framing. Since `h_k(1) = 0` and `h_k′(1) = 2k`:

* second-order vanishing at `q = 1` is a **consequence** of there being *two*
  q-differences — not something a bridge factor arranges;
* the leading coefficient is `−(2·4)(2·6) = −96`, and `J″(1) = −192`.

The β-decay rate's own coupling is the same shape at **half scale**:

```
s²  =  (q^{1/2} − q^{−1/2})²  =  h_{1/2}²,        h_{1/2}′(1) = 1
```

So both objects are products of two q-differences vanishing to second order.
They differ only in *which exponents*: `{4, 6}` for the trace, `{½, ½}` for the
rate.

Lean: `jonesT35_sub_one_eq_qDiff_product`, `sSq_of_sq` (stated at `q = u²`, so
it needs no square root and no ordering).

---

## 4. The ratio in closed form — no limit, no derivative

Clearing the framing makes the deviation polynomial, and the cofactors are
cyclotomic. With `G_n(q) := 1 + q + ⋯ + q^{n−1}`, so that `G_n(q)(q − 1) = qⁿ − 1`:

```
q²⁰ · (J − 1)  =  −(q⁸ − 1)(q¹² − 1)  =  −(q − 1)² · G₈(q) · G₁₂(q)
q · s²         =  (q − 1)²

  ⇒   (J − 1) / s²  =  − G₈(q) · G₁₂(q) / q¹⁹
```

The `(q − 1)²` that makes `J − 1` second order is *exactly the one in `s²`*, and
what is left over is the cyclotomic pair. So:

| | value |
|---|---|
| ratio at `q = 1` | `−G₈(1)·G₁₂(1) = −8·12 = −96` |
| ratio at `11/10` | `−39.9855973114…` |
| ratio at `q₀ = 1.10997858…` | `−37.0915139765…` |
| ratio at `3/2` | `−5.7214496383…` |
| ratio at `2` | `−1.9917011261…` |

The vanishing order, the leading coefficient **and the running** all come off
one rational function. Nothing here is a limit, a derivative, or a numerical
fit — which is why the entire Lean derivation stays over
`{K : Type*} [Field K]`. The earlier route through `hasDerivAt` was not merely
avoided; it was never necessary.

Lean: `geomCofactor`, `geomCofactor_one`, `geomCofactor_mul`,
`jones_dev_eq_sSq_mul_geom`, `couplingRatio`, `jones_dev_div_sSq`,
`couplingRatio_one`, `couplingRatio_not_constant`.

---

## 5. What this settles

**The order of the `1.19·10⁴` substitution factor is derived, and the residual is
reported.** A coupling carrying the trace's Jones content sits `≈ 10²` above `s²`,
so its square sits `≈ 10⁴` above `s⁴`, with `96² = 9216` the leading constant.
Against the measured `|W(q₀)|²/s(q₀)⁴ = 11875.4418936763`, the **overshoot is**

```
|W(q₀)|²/s(q₀)⁴ / 96²  =  1.2885679138…
```

and that measured number is what the Lean brackets, to three decimals
(`substitutionRateFactor_overshoot_of_leading_square`). The overshoot is nonzero
because `couplingRatio` runs from `−96` to `−37.09` on the way to `q₀`; it is the
size of what the leading term misses.

> **The first form of this claim is WITHDRAWN, and the reason is a directive that
> landed on `main` while this branch was open.** It read `96² < |W(q₀)|²/s(q₀)⁴ <
> 2·96²` — "good to within a factor of two" — and the PR body defended the
> two-sided form as "the honest limit, not a decoration". That defence was wrong
> on its own terms: the `2` is round *only because the measurement fits under
> it*. Nothing derives it. The 🟥 **NO FITTING, EXCEPT CAL-1/2/3** directive
> (owner, 2026-09-05) names this exact move — *"a tolerance sized to its own
> miss is a fit"*, and *"selection against the target"* covers a discrete choice
> with no continuous parameter tuned. So the window is replaced by the ratio it
> was hiding. Nothing about the derivation changed; the number that was rounded
> away is now on the record, and `1.2885679138` is something the next agent can
> attack.

**It produces no rescaling constant, and cannot.** `couplingRatio` is a
non-constant rational function (`couplingRatio_not_constant`, and
`couplingRatio_near_q0` shows it has already fallen from `−96` to `−37.09` by
`q₀`). That is consistent with `qou-pfh7`'s scope-(b) exclusion, and it now
*explains* the exclusion instead of measuring it: the framing `q^{−19}` and the
size of the Jones exponents suppress the ratio away from `q = 1`.

## 6. What this does not settle — read this before citing it

**`s²` is a formal half-scale analogue, not a Jones deviation.** Its exponents
are `½`, and a Jones exponent is an integer, so **no knot's `V − 1` equals
`s²`**. The shape match (`h_a · h_b`, second order) is exact; the
*identification* is not, and nothing above supplies one. Concretely: this work
explains the magnitude gap between the two couplings, it does **not** remove it,
and it does **not** license substituting either coupling for the other. The
`qou-ix74` negative stands unchanged.

**Scope classification.** §1–§4 are positive derivations (exact identities,
verified two ways). §5's order claim is a positive result with a stated
precision (factor of two). The non-existence of a rescaling constant is a
**scope-(b) structural exclusion** and cites its invariant: `couplingRatio` is a
non-constant rational function, decided at two rational points.

**What remains genuinely open.** Whether the β-decay rate's `s²` *should* be the
half-scale q-difference at all, or whether the rate formula's construction picks
out a specific pair of exponents the way the trace's does, is not addressed
here. That is a question about the rate's derivation, not about the trace, and
it is the live remainder on `qou-q2l7`. Three untested shapes carried forward
from `qou-pfh7` are unaffected: a ratio against another trace, a bar-parity
component, and a Jones-normalised object of a different knot.

---

## Verification

No CI exists in this repository (Actions are `workflow_dispatch`-only under the
2026-06-30 billing directive), so the agent's own verification is the gate.

* **Producer 13/13 PASS** —
  [`weak_vertex_jones_markov_normalisation.py`](../../computations/markov/weak_vertex_jones_markov_normalisation.py).
  sympy-exact throughout; mpmath at 60 dps evaluated from the exact
  expressions; serialised at 50 digits. No float is formed anywhere. The
  eight-knot rule check runs against `markov_trace_canonical`, i.e. the
  corpus's own engine rather than a re-implementation.
* **Lean `lean`-direct exit 0** on both carriers against the real import cone
  (restored oleans + `LEAN_PATH`, not a stubbed harness). `#print axioms` on
  all **16** declarations reports `[propext, Classical.choice, Quot.sound]`
  only — no `sorryAx`. Zero occurrences of `sorry`.
* **`check-sidecars.sh`** clean on the changed set:
  `WeakVertexJonesMarkov.lean` → "no ℝ, generic OK";
  `WeakVertexJonesMarkovArchimedean.lean` → "archimedean construct present,
  ℝ justified".
* **`precision-gates.sh --changed`** run. The tree-measuring audit witnesses it
  regenerated in passing were **reverted, not committed** (bean `qou-v0t8`);
  the branch diff is exactly the intended files.

Witness:
[`weak-vertex-jones-markov-normalisation.witness.json`](../../computations/weak-vertex-jones-markov-normalisation.witness.json).

### §7c note carried forward

The same MIXED-content flag noted on `qou-pfh7` is still latent in the two
earlier-merged carriers: `WeakVertexT35TraceClosedForm.lean` holds
`weakVertexTrace_near_q0` and `WeakVertexSubstitutionScale.lean` holds the two
`substitutionRateFactor` envelopes, both over `ℝ`, in otherwise generic files.
`check-sidecars.sh` only inspects *changed* files, so neither is reported unless
those files are touched. Not fixed here — moving them is a mechanical split with
no mathematical content, and doing it in this PR would obscure the derivation.
Recorded on `qou-pfh7` and again here so it is not discovered a third time.
