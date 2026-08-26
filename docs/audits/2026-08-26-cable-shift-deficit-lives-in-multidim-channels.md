# The cable-shift deficit lives in the multi-dimensional channels

**Date** 2026-08-26 · **Branch** `claude/cable-shift-law-nonpositive-2026-08-26` ·
**PR** [#5863](https://github.com/litlfred/qou/pull/5863) ·
**Scope** (a) — a mechanism finding, not a structural exclusion.

## The question, and the fit that preceded it

The satellite front left an open question: *what is the cable-shift law for a
non-positive braid word?* The measured facts were

- `α_shift(C(K)) ≤ 4·α_shift(K)` for the 2-parallel cable `C`,
- equality iff the word is positive,
- the deviation is one-sided.

An earlier addendum answered this by scanning candidate closed forms in the
word's length `L`, writhe `W`, strand count `p` and `α_shift(K)`, and reporting
the best-scoring candidate at 10/12. **That was a fit**, retracted on the
author's challenge. Flagging a scan as "not a law" does not undo having run it;
the correct response is a derivation, which is what this document records.

## The derivation

Two facts, both formalised.

**1. The writhe quadruples, unconditionally.** The 2-parallel substitution is

$$\sigma_i \;\longmapsto\; s_{2i}\, s_{2i-1}\, s_{2i+1}\, s_{2i}$$

and for an inverse letter the image is that block reversed with every letter
inverted. Writing the letter as a signed index `g`, both cases produce the
*same list of expressions*, `[2g, 2g−1, 2g+1, 2g]` — because for `g = −i < 0`,
`−(2i+1) = 2g−1` and `−(2i−1) = 2g+1`. All four letters therefore carry the
sign of `g`, and

$$\mathrm{writhe}(C(w)) = 4\,\mathrm{writhe}(w)$$

with **no positivity hypothesis**. The only hypothesis is `g ≠ 0`, i.e. that
the letters are genuine braid generators — and that hypothesis is load-bearing,
not decorative: a degenerate zero letter gives the mixed-sign block
`[0, −1, 1, 0]` and the law fails on it.

**2. A one-dimensional channel sees only the writhe.** A one-row `(n)` or
one-column `(1ⁿ)` diagram has a single standard tableau, so the generator acts
by a scalar and `χ(w) = s^{\mathrm{writhe}(w)}` — `QOU.BraidKnot.charOf_eq_zpow`,
merged in [#5826](https://github.com/litlfred/qou/pull/5826).

**Composing them.** On the all-row and all-column channels the cable-shift law
is **exactly multiplicative by four, for every word, positive or not**. A
one-dimensional channel cannot tell a non-positive word from a positive one
except through its writhe, and the writhe quadruples either way.

## The consequence, which is the answer

The deficit

$$d(w) \;:=\; 4\,\alpha_{\text{shift}}(K) \;-\; \alpha_{\text{shift}}(C(K))$$

**cannot come from a one-dimensional channel at all** — it is identically zero
there. It can only arise when the *maximizing* partition `λ*` is intermediate,
where the character is a sum over standard-tableau paths and there is no reason
for a factor of four to survive.

> **The cable-shift law is a statement about which channel attains the maximum,
> not about the word's letters.**

That is why no closed form in `L`, `W`, `p`, `α` exists — stated as a mechanism
rather than as a failed search. And it explains, in a derived way, what
positivity was actually doing: **positivity keeps the maximum on the column
channel**, where the law is exact. Non-positivity lets the maximum migrate
inward, and the deficit is the migration.

## What was measured

[`computations/meson/cable_shift_where_the_deficit_lives_probe.py`](../../computations/meson/cable_shift_where_the_deficit_lives_probe.py)
— 7/7 assertions.

| | prediction | result |
|---|---|---|
| **P1** | `writhe(C(w)) = 4·writhe(w)` | 14/14 words |
| **P2** | valuation scales by exactly 4 on both 1-dim channels | 14/14, positive and non-positive alike |
| **P3** | deficit nonzero **only** when a multi-dim channel maximizes | 5/5 nonzero deficits have a multi-dim maximizer; 7/7 words with a 1-dim maximizer at both ends have deficit 0 |

Deficit table, measured densely at 300 dps:

| word | `α(K)` | `λ*` | `dim λ*` | `α(C(K))` | `μ*` | `dim μ*` | `d` |
|---|---|---|---|---|---|---|---|
| `σ₁` | 1 | `(1,1)` | 1 | 4 | `(1,1,1,1)` | 1 | **0** |
| `σ₁σ₂⁻¹` | 2 | `(2,1)` | 2 | 6 | `(4,2)` | 9 | 2 |
| `σ₁²σ₂⁻¹` | 3 | `(2,1)` | 2 | 10 | `(2,2,1,1)` | 9 | 2 |
| `(σ₁σ₂⁻¹)²` | 4 | `(2,1)` | 2 | 12 | `(4,2)` | 9 | 4 |
| `σ₁σ₂σ₁⁻¹` | 1 | `(2,1)` | 2 | 4 | `(3,1,1,1)` | 10 | **0** |

The two zero rows are the informative ones: `σ₁` has a one-dimensional
maximizer at both ends and its deficit vanishes; `σ₁σ₂σ₁⁻¹` is a conjugate of
`σ₂`, so its reduced form is positive and the maximum stays put.

## What was proved

[`content/quantum-observable-universe/lean/QOU/BraidKnot/CableShiftFourfold.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/CableShiftFourfold.lean)
— eleven declarations, all sorry-free (`#print axioms` gives only `propext` /
`Classical.choice` / `Quot.sound`; the three decidable witnesses depend on
nothing). Verified `lean`-direct against the real import cone, exit 0. Generic
`CommGroup` throughout — no `ℝ`, no ordering, nothing archimedean (AGENTS.md
§7c).

| declaration | content |
|---|---|
| `writhe_cableBlock_pos` / `_neg` / `writhe_cableBlock` | one letter contributes four letters of its own sign |
| `writhe_cable` **(P1)** | `writhe(C(w)) = 4·writhe(w)`, every word |
| `length_cable` | `(C(w)).length = 4·w.length` |
| `charOf_cable` | the character is a fourth power |
| `val_charOf_cable` **(P2)** | **the law**: valuation scales by exactly 4 on a 1-dim channel |
| `cable_deficit_zero_on_oneDim` **(P3)** | the deficit is identically zero there |
| `writhe_cable_nonpositive_witness` | `σ₁σ₁σ₂⁻¹` quadruples — the law is not a positive-word statement |
| `nonpositive_witness_has_inverse_letter` | that word really is non-positive |
| `writhe_cable_fails_on_zero_letter` | `g ≠ 0` is load-bearing, not noise |

## The property the law rides on — multiplicativity, not cyclicity

A sibling session raised this on [#5863](https://github.com/litlfred/qou/pull/5863)
and it sharpens the framing above, so it is recorded here rather than left in a
comment. Verified independently before adopting it.

The section above says *"a one-dimensional channel sees only the writhe"*. That
is true, but it names the **channel** where it should name the **property**. Two
properties are in play and only one separates the channels:

| | one-dimensional `χ` | multi-dimensional `χ^λ` |
|---|---|---|
| **cyclic** — `χ(xy) = χ(yx)` | ✓ | ✓ — every character is a class function |
| **multiplicative** — `χ(xy) = χ(x)·χ(y)` | ✓ | ✗ — a trace of a product is not a product of traces |

So cyclicity cannot be what distinguishes them. **Multiplicativity is.** The
migration the deficit measures is from a *multiplicative* readout to a merely
*cyclic* one — and that is precisely why the writhe stops controlling the
valuation. The writhe is exactly what a homomorphism can see; once the maximizer
is a sum over standard-tableau paths, there is no homomorphism left for the
factor of four to ride on.

Two declarations added to
[`CableShiftFourfold.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/CableShiftFourfold.lean)
make the dependence explicit rather than implicit in the choice of channel:

- `fourfold_of_multiplicative` — **any** readout that is multiplicative on
  concatenation and sends each letter to `s^{\pm 1}` quadruples under cabling,
  whatever channel it came from. Supported by `charOf_append` (the character is
  multiplicative, stated on its own), `cable_letters_ne_zero` (cabling preserves
  genuine braid letters, since `2g` is even and nonzero while `2g \pm 1` are
  odd) and `eq_charOf_of_multiplicative` (a multiplicative readout is determined
  by its values on single letters).
- `sqWritheReadout_not_fourfold` — the **converse guard**. `s^{W^2}` is cyclic
  (the writhe is invariant under cyclic permutation, hence so is its square) but
  not multiplicative, and under cabling it scales by **sixteen**, not four, for
  any word of nonzero writhe. Without this, the theorem above could be misread
  as though cyclicity sufficed.

Four more sorry-free declarations, `lean`-direct exit 0; `#print axioms` clean on
all four.

## What is NOT proved — a derived limitation, not a gap

Nothing here bounds the multi-dimensional case, and **nothing here claims the
deficit is nonzero**. That the deficit is real is a measurement, not a theorem.
The Lean proves the half that forces the deficit *out of* the one-dimensional
channels; the probe locates where it went. A theorem covering the intermediate
case would need the longest-path optimisation over the standard-tableau graph,
which is exactly the object no closed form in word-counts reaches.

## Method note — an error this probe made first, caught by a failing assertion

The first version computed the deficit table from **min-plus alone**. Min-plus
is a *bound* on the valuation
([`QOU.BraidKnot.minVal_le_val_sum`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MinPlusValuationBound.lean),
merged in #5826), not an identity, and it over-states the pole order wherever
paths cancel. On `σ₁σ₁⁻¹` — the **identity**, whose cable is therefore also the
identity — it returned `α(C(K)) = 2` against a true `0`, producing a spurious
*negative* deficit and a false counterexample to `α(C(K)) ≤ 4·α(K)`.

The lesson generalises and is worth carrying forward:

> **Min-plus is loosest exactly on the maximally cancelling words — which are
> the words a deficit analysis is most interested in.**

The table above is therefore measured densely in `mpmath` at 300 dps, with
min-plus carried alongside as a flagged cross-check and every divergence
reported.

## Provenance

- No calibration input. `α_shift` is a fibre-level valuation in the formal `q`
  and consumes none of CAL-1/2/3; it is a Laurent pole order, not a magnitude.
- Audit-only: no content blocks, nothing wired to production, no witness
  touched.
- `scripts/precision-gates.sh --changed`: exit 0, all blocking gates green.
