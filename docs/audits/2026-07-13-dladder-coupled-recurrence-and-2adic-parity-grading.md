# The exact D-ladder: no coupled ℚ(√3) recurrence + a crisp 2-adic parity grading

**Date:** 2026-07-13 · **Branch:** `claude/faddeev-phi-b-construction-wp7xau` ·
**PR:** #3737 · **Tier:** exact-arithmetic (rational linear algebra + p-adic
valuation; no floats, no PSLQ, no fit) · **Scope:** (a) — no `c_k` wired, no
tier change, registry untouched.

Advances the **exact D(ũ) ladder** (`S = h·D(ũ)`, the bar-odd c₃ S-leak;
`h = q − q⁻¹` the anchor-blind bar-odd carrier, `D` the bar-even ℚ(√3) ladder).
Builds directly on the merged structure hunt
([`2026-07-12-bar-odd-s-deformed-rung-followup.md`](2026-07-12-bar-odd-s-deformed-rung-followup.md) §Route 2, PR #3716)
and its divergence correction
([`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md)):
`D(ũ) = Σ_k d_k ũ^k` has exact coefficients `d_k = a_k + b_k√3` (`a_k, b_k ∈ ℚ`),
is super-exponentially divergent (q-Gevrey, radius → 0), and has no **classical**
P-finite recurrence for `a_k` or `b_k` **taken separately over ℚ**.

This audit reports two exact results the merged hunt did not.

## Result 1 — no *coupled* ℚ(√3) P-recurrence (the class #3716 skipped)

The merged probe tested P-finiteness of `a_k` and `b_k` **separately over ℚ**.
But `d_k` is a single ℚ(√3) object, and a recurrence *over ℚ(√3)*

$$\sum_{i=0}^{r} P_i(k)\,d_{k-i} = 0,\qquad P_i \in \mathbb{Q}(\sqrt3)[k],$$

does **not** reduce to separate ℚ-recurrences of the same order: applying the
√3-Galois conjugation couples the two rational components into a 2-vector
`v_k = (a_k, b_k)ᵀ` obeying a **matrix** recurrence

$$\sum_{i=0}^{r} M_i(k)\,v_{k-i} = 0,\qquad M_i(k) \in \mathrm{Mat}_2(\mathbb{Q}[k]),\ \deg_k \le D,$$

whose off-diagonal (√3-mixing) entries a separated scalar test structurally
cannot see. A coupled recurrence can therefore exist where both separated ones
fail — this is the exact ℚ(√3) P-finiteness question for `D(ũ)`.

**Probe** ([`qbeta_dladder_coupled_qsqrt3_recurrence_probe.py`](../../computations/qbeta/qbeta_dladder_coupled_qsqrt3_recurrence_probe.py)):
the exact rational null space of the integer constraint matrix over all valid
`k`. The recurrence has only `2·(r+1)·(D+1)` unknowns — the coefficients of the
two polynomials `A_i, B_i` in `P_i = A_i + B_i√3` — since the √3-algebra ties the
matrix diagonal to `A_i` and the off-diagonal to `B_i` (a correctness + efficiency
fix from the `@gemini-code-assist` review on PR #3737; an unconstrained
`Mat₂(ℚ[k])` would double the unknowns and force premature data-starvation
skips). With the correct count, the `d_1…d_21` already in hand cover a robust
window: **no coupled ℚ(√3) P-recurrence** for order `r ≤ 2` through degree
`D ≤ 4`, `r = 3` through `D ≤ 3`, and `r = 4` through `D ≤ 2` (all exact,
over-determined). This **extends** #3716's "not P-finite (separated)" to the
coupled ℚ(√3) case,
tightening the corpus's q-Gevrey / resurgent reading of the bar-odd S-leak: the
D-ladder is not (q-)holonomic of low order even as a coupled ℚ(√3) object.

*(This is the right refinement to run, not a re-open of a settled frontier: a
negative here further **constrains** the resurgent class; a positive would have
been an exact closed-form characterization. Either way it is decisive and
exact.)*

## Result 2 — the exact 2-adic parity grading (headline)

Writing `d_k = a_k + b_k√3` and reading the **2-adic valuation of the
denominators**, an exact ℤ/2 grading emerges — crisper than the merged hunt's
"the small-denominator part alternates by parity":

> **`v₂(den b_k) = 0` if and only if `k` is odd**, and the rational part is the
> mirror: **`v₂(den a_k) ≤ 1` if and only if `k` is even**.

Equivalently: **the 2-adically singular ℚ(√3)-component of `d_k` alternates with
`k`-parity** — it is the rational part `a_k` for odd `k`, the √3-part `b_k` for
even `k`. Holds **exactly** for every computed `k` (the committed run covers
`k = 1…21`; the higher-ORD extension on this PR pushes it further):

| k | parity | v₂(den a_k) | v₂(den b_k) | 2-singular part |
|---|--------|-------------|-------------|-----------------|
| 1 | odd  | 3  | 0  | a (rational) |
| 2 | even | 1  | 5  | b (√3) |
| 3 | odd  | 8  | 0  | a (rational) |
| 4 | even | 1  | 10 | b (√3) |
| 5 | odd  | 14 | 0  | a (rational) |
| 6 | even | 1  | 16 | b (√3) |
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |
| 21 | odd | 61 | 0 | a (rational) |

The 3-adic and ≥5 (factorial-smooth, Ohtsuki–Habiro) parts grow in **both**
components (~linear in `k`) — those are the known 3-smooth normalization. What is
new and clean is the **2-adic** channel: it is *pure* — a component either
carries the full 2-power or is 2-integral — and it is graded exactly by `k`
parity.

**Interpretation.** This is the arithmetic shadow of the **sinh/cosh
(bar-odd / bar-even) split** that defines the whole bar-parity program
(`QOU.QBeta.bar_parity_decomposition`; the sinh/cosh = decay/mass faces). `sinh`
carries the odd Taylor tower, `cosh` the even; the 2-adic denominators of the
substrate expansion inherit that parity as a clean ℤ/2 valuation grading. It is
exactly the kind of **structural invariant** the formalize-first discipline asks
to be isolated before any wider numerical search — here it also *is* the exact
content that a Domb–Sykes radius (refuted) or a fitted singularity never was.

## Formalize-first note (the invariant, and what proving it needs)

The grading is a precise, exact, non-fitting statement. Formalizing it as a Lean
theorem requires the D-ladder *construction* (`O/h` via `ser_div`, the substrate
`ũ = b·ℏ_q²` expansion) to exist in Lean, which it does not yet — the current
Lean D-ladder object is `QOU.QBeta.BarOddLadderShape`, the phenomenology carrier
`S = A/u³`, not the coefficient construction. So this audit **states the
invariant precisely** (an exact, machine-checked arithmetic fact at every
computed order) as the formalization target, rather than laundering it through a
premature axiom. The natural Lean home is a `p`-adic valuation statement over the
coefficient sequence once the construction is formalized.

## Discipline

Scope-(a) throughout: exact rational linear algebra + `v₂` valuations, no floats,
no PSLQ, no fit, no `c_k` wired, no tier change. Adjacent **live sibling PR
#3683** runs Borel / alien-calculus resurgence on the **κ-tower** — a distinct
object; this audit is holonomicity + arithmetic grading of the **D-ladder**, the
complementary structural question. Nothing here closes `S` or changes any
precision leg.

## Cross-references
- Merged structure hunt: [`2026-07-12-bar-odd-s-deformed-rung-followup.md`](2026-07-12-bar-odd-s-deformed-rung-followup.md) §Route 2 (#3716).
- Divergence correction: [`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md).
- Bar-parity split: `QOU.QBeta.bar_parity_decomposition`; `qbeta_even_channel_bar_split_probe.py` (`S = h·D(u)`).
- Phenomenology carrier: `QOU.QBeta.BarOddLadderShape`.
- Adjacent resurgence sibling: PR #3683 (κ-tower Borel / alien calculus).
