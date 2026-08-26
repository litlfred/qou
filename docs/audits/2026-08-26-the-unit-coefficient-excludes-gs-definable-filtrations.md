# The unit coefficient excludes every GS-definable filtration

Bean `qou-09e0` (front 5 of epic `qou-v2om`), continuing `qou-wjbd` / `wpdb`.
Fourth pass on the word-depth ↔ partition-depth bridge, after
[`2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated`](2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md)
(the identification is unstated),
[`2026-08-16-three-gb-filtrations-one-name`](2026-08-16-three-gb-filtrations-one-name.md)
(`J^•` names three inequivalent objects; two excluded), and
[`2026-08-26-no-shift-rescues-the-word-partition-bridge`](2026-08-26-no-shift-rescues-the-word-partition-bridge.md)
(the third excluded, and no re-indexing repairs it).

**Result: a scope-(b) exclusion of the whole indexing route, over a class of
filtrations named precisely enough to be checked — and an independent
refutation of one consumer site's Step 1 that does not go through the bridge at
all.** An honest negative. Nothing is closed; what was one open construction is
now a characterisation of what any construction would have to look like.

## 0. The one-line version

The previous pass left the front at: *a candidate filtration must put a second
central element in `F_1`.* It cannot, and the reason is one number.

`1 = Σ_λ e_λ` uses **every** idempotent, so the unit is at the **top** of any
idempotent-graded filtration. And `τ(e_λ) ≠ 0` — the `T_e` coefficient of every
central primitive idempotent is nonzero — so in a filtration spanned by normal
forms, the unit is dragged down to the **bottom**, into the first piece that
admits any `e_λ` at all. Top and bottom meet only when the grading is constant,
which at `n ≥ 4` it is not.

## 1. What was measured, and why measuring it was the whole job

The argument needs exactly one algebra fact:

> `τ(e_λ) ≠ 0` for every `λ ⊢ n`, where `τ(Σ_w a_w T_w) := a_e`.

`τ` is the canonical symmetrizing trace: in the AGENTS.md §7a convention
`σ² = (q − q⁻¹)σ + 1` one has `τ(T_u T_v) = δ_{u,v⁻¹}`, so `{T_{w⁻¹}}` is the
dual basis of `{T_w}` (self-checked in the probe at `n = 3`, 0 violations).
Equivalently: **`T_e` is in the support of every central primitive idempotent.**

This is standard — `τ(e_λ) = d_λ / c_λ` with `c_λ` the Schur element, nonzero at
generic `q` — but it is the load-bearing hypothesis of a scope-(b) exclusion, so
[`central_idempotent_unit_coefficient.py`](scripts/central_idempotent_unit_coefficient.py)
measures it rather than citing it.

**It is measured as a rank, which is why no idempotents had to be computed.**
Splitting `Z` into its primitive idempotents needs eigenvalues, hence factoring,
hence a labelling problem. All of that is avoidable: in the idempotent basis the
form `B(x, y) = τ(xy)` restricted to `Z` is `diag(τ(e_λ))`, so

    B non-degenerate on Z   ⟺   τ(e_λ) ≠ 0 for every λ,

and the question is a single exact rank computation on a `p(n) × p(n)` matrix.
No labelling, no factoring, no choice of basis.

| `n` | `dim Z` | `p(n)` | `rank(τ-form on Z)` | every `e_λ` touches `T_e` |
|---|---|---|---|---|
| 2 | 2 | 2 | 2 | yes |
| 3 | 3 | 3 | 3 | yes |
| 4 | 5 | 5 | 5 | yes |
| 5 | 7 | 7 | 7 | yes |

Exact throughout, no floating point anywhere: `Fraction` over `ℚ` and `𝔽_p`
(`p = 2⁶¹ − 1`), at several specialisations of `q` each. `dim Z = p(n)` at every
run, which independently validates the construction of the algebra.

**The specialisation direction is the safe one.** Every Gram entry is a Laurent
polynomial in `q`, so `rank B(q₀) ≤ rank B(q)` generically. The probe reports
**full** rank, and full rank at a specialisation forces full rank generically —
so no genericity is assumed anywhere.

## 2. Three routes to the same conclusion, and they are independent

All three are Lean-proved sorry-free in
[`GSFiltrationUnitObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/GSFiltrationUnitObstruction.lean).
Each concludes **`gbDepth` is constant on partitions of `n`**, which
`gbDepth_ne_on_H4` refutes from `n = 4` up.

**Route A — the unit is in degree `0`.** `1 ∈ Z ∩ F_0 = V_c` and `1 = Σ_λ e_λ`
forces every stratum at or below `c`; the filtration starting at `0` forces
every stratum at or above `c`. Needs **no monomiality** — so it also excludes
the most natural "fourth filtration" candidate, the **Jucys–Murphy content
filtration** `Z_{≤d} =` symmetric functions in the `L_i` of degree `≤ d`, whose
degree-`0` piece is `R·1`. (`unit_in_degree_zero_forces_constant_grading`.)

**Route B — monomial in the normal-form basis.** If `F_k = span{T_w : w ∈ S_k}`
then either `e ∈ S_k`, so `1 ∈ F_k`, or `τ` vanishes identically on `F_k`.
Since `τ(e_λ) ≠ 0`, the first piece admitting **any** `e_λ` admits `1`, hence
admits **all** of them. *There is no `F_1` with two central elements and not all
of them.* (`monomial_filtration_forces_constant_grading`.)

**Route C — the anti-diagonal strata pairing.** Independent of the word side
entirely; see §4.

## 3. The quantifier — stated precisely, because it is the crux

The sibling pass was careful to record that the identification is **not** false
in the abstract: a filtration inducing the `gbDepth` grading exists trivially,
by filtering by the Wedderburn blocks, `F_k := ⊕_{gbDepth λ ≤ k} R·e_λ`. Any
exclusion has to be about filtrations *definable from the Gröbner–Shirshov
data*, not about all filtrations, and getting that quantifier right is the whole
difficulty. So, explicitly:

> **Excluded (scope (b)), for every `n ≥ 4` and every shift `c`:** any
> filtration of `H_n(R, q)` that **either** places the unit in degree `0`
> **or** is **monomial in the Gröbner–Shirshov normal-form basis** — i.e. each
> `F_k` is spanned by a subset of `{T_w}`.

**Why that is the right reading of "definable from the GS data".** The GS
machinery produces a rewriting system on braid words, the normal-form basis
`{T_w}`, and a depth statistic on words. A filtration read off that data assigns
a degree to each normal form and takes spans — which is exactly monomiality. All
three corpus readings of `J^•` are monomial *and* have `1 ∈ F_0`, so each is
excluded twice over. A non-monomial filtration cannot be read off the GS data,
because the GS data has no vocabulary for a linear combination of normal forms
other than its support.

**Not excluded, and this is not a hedge.** The Wedderburn-block filtration
satisfies every hypothesis except monomiality, and except `1 ∈ F_0` (its unit
sits in degree `n`). Those two hypotheses are therefore exactly what separates
the excluded class from the realisable one, and neither is idle — verified
mechanically, see §6.

**What could still escape:** a filtration built from GS data by some
*non-monomial* construction whose unit sits in positive degree. Nothing here
rules that out. What §5 does is say what such a thing would have to look like.

## 4. Route C — one site is not repaired by fixing the bridge

`prf:quantum-dilogarithm-stratified` Step 1 states, **of the centre**,

    ⟨Z^(k)(A), Z^(ℓ)(A)⟩ = 0   whenever k + ℓ ≠ N,

and calls the residual `Z^(k) × Z^(N−k) → R` the *Poincaré duality of
curvature-rank strata*. It cites `prf:spectral-sequence-collapse`
§"Frobenius duality of strata" — which states an **annihilator** duality
`(J^ℓ)^⊥ = J^{N−ℓ}` for the ideal filtration of the **whole algebra** `A`.

That is a reasonable statement about a Frobenius algebra. Transporting it to the
centre's *idempotent* strata is not. On `Z` the pairing is `⟨a,b⟩ = φ(ab)`, and
distinct central primitive idempotents **annihilate each other**, so the pairing
matrix in the idempotent basis is `diag(φ(e_λ))` — **diagonal**. A stratum pairs
with **itself**. The anti-diagonal law can hold only if every occupied depth
satisfies `2k = N`, i.e. only for a single stratum.

So this site's own Step 1 is already inconsistent with a non-constant grading,
**without reference to the word filtration at all** — and therefore is *not*
repaired by supplying the missing word/partition bridge. That is a different
disposition from the other five sites, which is why it is recorded separately.
(`antidiagonal_pairing_forces_constant_grading`.)

The Lean takes `φ` as a bare function into a type with a zero — linearity and
ring structure on the coefficients are never used — and takes the block's
displayed hypothesis **restricted to the spanning idempotents**, i.e. strictly
weaker than what the block asserts. Both choices strengthen the refutation.

## 5. What a next agent should try

The negative comes with a positive characterisation, and it is sharp. Under the
identification, `1 ∈ Z ∩ F_k = V_{k+c}` holds **iff** `k + c ≥ n`. So:

> **Any filtration realising the identification must place the unit in the
> *top* occupied filtration degree, `n − c` — never in degree `0`.**

That is exactly what the Wedderburn-block filtration does (`1 ∈ F_n \ F_{n−1}`),
and it is why that one works. So the search is not for a cleverer depth
statistic on words: **any statistic with `d(empty word) = 0` is dead on
arrival**, whatever else it does. A candidate must assign the empty word the
*maximal* depth, which is not a shape any rewriting-depth notion naturally has.

Concretely, in descending order of what I would try:

1. **Take the characterisation seriously as a negative result about GS data.**
   A GS depth is a complexity measure on words; the empty word is the simplest
   one. Being forced to make it the *deepest* is strong evidence the indexing
   should be re-founded, not repaired. That is a judgement, not a finding.
2. **Re-found `lem:bond-order-eq-jet-degree` on the partition side directly.**
   `gbDepth λ` is a definition, and `Z = ⊕_λ R·e_λ` is the Wedderburn
   decomposition; bucketing blocks by `gbDepth` is a free construction needing
   no word proposition at all. The corpus's own `gbDepth_eq_content_spread`
   already relocates the partition side onto the Jucys–Murphy content axis,
   which is the algebra's own coordinate. Nothing in this audit touches that.
3. **If a word-side statement is genuinely wanted**, the object to look for is
   not a filtration of `H_n(q)` but a map from word data to *partitions* — the
   support map `T_w ↦ supp(T_w)` — after which `gbDepth` does the grading. The
   corpus already writes `k⋆(T_w) := max{gbDepth λ : λ ∈ supp(T_w)}` that way.
4. **Do not re-test the Geck–Rouquier class-element basis as a rescue.** It is
   a basis of `Z` supported within conjugacy classes, so the induced filtration
   has `1 ∈ F_0` (the class of the identity is `{e}`) and Route A applies.

## 6. Discipline

- `lean`-direct **exit 0** (overlay farm; never `lake build` on a RESTORED
  tree). `#print axioms` on all **9** declarations: `propext` / `Quot.sound` /
  `Classical.choice` only — no `sorryAx`, no custom axiom. No `sorry`, no
  `native_decide`, no `: True`.
- §7c: generic `{R : Type*} [CommRing R]` throughout (and `[Zero R]` where that
  suffices); `check-sidecars` reports *library Lean — no ℝ, generic OK*.
- **Non-vacuity is proved, not asserted.** `monomial_hypotheses_satisfiable`
  discharges every §3 hypothesis simultaneously over `ℤ`, so the theorems are
  genuine implications rather than `False → _`. And a delete-a-binder sweep
  confirms all **12** named hypotheses are load-bearing: removing any one of
  `hV`, `hu`, `huZ`, `heZ`, `hπe`, `hτ`, `hmono`, `hid`, `hbot`, `hunit0`,
  `ha`, `hb` stops the file compiling.
  The model that satisfies everything is the degenerate one — one stratum —
  which is the `n ≤ 3` situation. The excluded class is realisable exactly where
  the partition grading has nothing to say.
- Probe arithmetic exact only; no float64 anywhere; specialisation direction
  stated and safe.
- Corpus-grepped before writing: no prior monomial-filtration or
  support-based exclusion exists in `docs/audits/`, `content/`, `computations/`,
  the coordination ledgers, or `library/`.

## 7. What this does **not** claim

- **Not** that the identification is false in the abstract (§3).
- **Not** that any mass or binding number moves. `J^•` enters as an **indexing**
  — which body order an `a_D^{(n)}` belongs to — not as a magnitude. The
  magnitude is a Seiberg–Witten period and is untouched. **A win here is
  necessary, not sufficient.** Unaffected: the Wedderburn decomposition, the
  Markov trace, `tr_M`, `y_λ`, the idempotents themselves, and `gbDepth` as a
  definition.
- **Not** a refutation of `prop:curvature-rank-gb-stratification`'s own
  statement, which is about words and may well be true of words. What fails is
  reading a *partition* grading off it.

## 8. Consumer-site disposition

The previous pass split the six sites into Class A (needs the grading only as a
definition — sound, should stop citing the word proposition) and Class B (needs
genuine compatibility with the word filtration — should be re-scoped as
conditional on a named conjecture). **That split stands, with two changes:**

- **The Class B conjecture should now record that the route is excluded, not
  merely candidate-free.** The previous wording was "all three candidate
  readings are excluded, so it is open without a candidate construction". The
  stronger statement available now is that **no GS-definable filtration can be
  such a construction**, and that any construction must put the unit in the top
  degree. A conjecture whose only known models are non-GS-definable is a
  different object from one merely awaiting a candidate, and whoever names it
  should say so.
- **`prf:quantum-dilogarithm-stratified` moves out of both classes.** Per §4 its
  Step 1 fails independently of the bridge, so it is repaired by neither
  re-citing (Class A) nor conditionalising on the bridge (Class B). It needs its
  own correction: the strata pairing is diagonal, and there is no Poincaré
  duality of curvature-rank strata on the centre.

**This pass deliberately does not rewrite the six sites.** They cite the
proposition for different things, and mechanical editing across sites whose uses
differ is how this defect got in — the same reason the previous pass gave, and
it has not weakened.
