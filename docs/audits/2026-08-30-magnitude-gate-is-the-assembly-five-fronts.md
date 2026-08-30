# The binding-magnitude gate is the assembly functional — five fronts worked

**Date:** 2026-08-30 · **Branch:** `claude/canonical-derivation-magnitude-3uxb5l` ·
**PR:** [#6101](https://github.com/litlfred/qou/pull/6101) ·
**Milestone:** `qou-m2ay` (beans `qou-nf4z`, `qou-bhzt`, `qou-9nt7`, `qou-90b1`,
`qou-u8mu`, `qou-p76y`)

**Type:** currency + four formalize-first units + one measurement. **No fit, no
wiring, no seventh ansatz.** Every negative is scope-(a) unless a proved
invariant is cited; the two that cite one say so.

---

## 0. Verdict

**The gate is the assembly functional, and the corpus's two assemblies are now
both proved incapable of the measured connected 3-body cumulant.** Deriving the
bond functional cannot close it, because the bond functional is not what fails.

The five fronts, in the order they were worked:

| # | front | outcome |
|---|---|---|
| M0 | cheat-sheet currency | the hub named two superseded gates; corrected |
| M1 | replace the assembly | **§10a's Cauchy step is orthogonal to the defect** — proved for *every* bond functional, not only the log |
| M2 | fixed-depth vs super-exponential | **machine-checked incompatibility**; which side gives is not decided |
| M3 | ramified double cover | **measured, and it does not close** — a dichotomy by kernel depth |
| M4 | SU(4) `[1⁴]` shell object | a single common scale **refuted**; the sign-capability claim **corrected below** — it is analytic and discriminates nothing |
| M5 | `M_n(K)` under the Option-A ruling | the "blocked upstream" clause is **stale**; the counts are fixed and cannot supply the surplus |

---

## M0 — the cheat sheet was stale on its own headline question

[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
is the designated coordination hub. Measured on `main` before this branch: across
all 923 lines, `Ursell`, `cumulant`, `body-order`, `w_3`, `a_D`, `Mayer` and
`Milnor` appeared **zero times**, while §9.3 named *"the full per-rep `θ_λ`
magnitude"* and §9.5 *"the per-depth `α_k` assignment rule"* as the open gate.
Both were superseded 2026-08-29/30.

Corrected by a currency banner rather than by deletion: the tower numbers and the
`α_k` measurement stand as records; only the diagnosis attached to them was
wrong.

---

## M1 — the §10a Cauchy derivation cannot reach the 3-body cumulant

**Bean `qou-bhzt`. Lean:
[`QOU/Mass/PairwiseCumulantVanishing.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/PairwiseCumulantVanishing.lean),
`lean`-direct exit 0, 0 sorry, `#print axioms` = `[propext]` on all five.**

[`2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`](2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md)
§10a derives the functional's shape: `tr_M` is multiplicative over **independent**
subsystems, energy is extensive over **non-interacting** ones, so the map
satisfies `f(xy) = f(x) + f(y)` and `f = c·ln x` is forced. Bean `qou-edt7` names
the independence hypothesis as the likely unstated one.

**Measured, and it is sharper than an unstated hypothesis.** §10a determines the
**bond functional**; the binding is then assembled by **summing `f` over bonds**.
Every such assembly is pairwise-additive, and a pairwise-additive set function has
identically vanishing connected cumulants above order two — **for every `f`**.
`b3_eq_zero_ofBondFunctional` carries no hypothesis on `f` at all: not
continuity, not Cauchy, nothing. So the Cauchy step is orthogonal to the defect.

This completes a dichotomy with `MayerThreeBodySign.lt_of_b3_pos` already on
`main`:

| assembly | forces | status |
|---|---|---|
| multiplicative / Mayer `W = 1 − ∏ f` | `b₃ > 0` needs `f_pn > 2/3`; largest measured is `z_D = 0.61269` ⇒ **`b₃ < 0`** | sorry-free on `main` |
| pairwise-additive `B = Σ f(μ)` | **`b₃ = 0`** identically, every `f` | sorry-free, this branch |
| AME2020 | `b₃ = +1.426222` MeV | measurement |

**Not new to the corpus in framing.** `b4_value_cumulant_target_probe.py`'s own
docstring already says *"`B_sym` is 2-body ADDITIVE ⇒ connected `b_k = 0` for
`k ≥ 3`"*. What is new is the **generality** — it holds for every bond
functional, so §10a's determination of `f` cannot help — and the machine check.

**Scope.** Nothing here refutes §10a's premises, and the conclusion that `f` is a
logarithm *on the sector where they hold* is untouched. What is established is
that the sector is the wrong one: the premises constrain `f` on **disjoint**
clusters, and the failing observable is a **connected** quantity, which vanishes
by construction on anything assembled by summing over disjoint pairs.

---

## M2 — a constant-kernel recurrence grows at most exponentially

**Bean `qou-9nt7` (finding `qou-9yqb`). Lean:
[`QOU/Mass/ConstantKernelGrowthBound.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/ConstantKernelGrowthBound.lean),
`lean`-direct exit 0, 0 sorry, `#print axioms` =
`[propext, Classical.choice, Quot.sound]`.**

`prop:prolonged-periods-fixed-depth` asserts an **n-independent** kernel;
`QOU.Mass.SWPeriodSuperExponential` (PR #6052) proves the classical period ratio
unbounded. `exists_exponential_bound` gives `|a n| ≤ M·Kⁿ` for any depth and any
constant kernel, and `not_isConstKernelRec_of_superExponential` closes the
contradiction. This converts `qou-9yqb`'s argument into a machine-checked
incompatibility.

**It does not decide which side gives**, and that is deliberate. Three
candidates: the identification `a_D^(n) = I(n)/n`; the finite-rank
abelianisation; or the word "n-independent". By the super-exponential side's
**own** scope note the identification is the cheapest suspect — its docstring
records that `Σ_{λ⊢n} f^λ = I(n)` (RSK) is open here (`qou-m3xr`, `qou-jlam`,
both blocked on the missing Mathlib `StandardYoungTableau` layer). That is their
scoping, not a preference of mine, and the collision is flagged on #6052 rather
than asserted as a verdict about their Lean.

Second independent crack; the first,
`BodyOrderRecurrenceDepth.no_equivariant_prolongation` (merged), reaches it from
equivariance rather than growth.

> **🛑 CORRECTION 2026-08-30, and it is against this unit — two things, one of
> them a partial duplication I did not detect.**
>
> **(a) The unit partially duplicates `QOU/MassTheory/FixedDepthGrowthBound.lean`
> on PR #6088**, which proves the same geometric bound (`abs_le_geometric`) and
> the factorial case (`not_factorial_growth`), and which landed on that branch
> roughly forty minutes before this file was written. **It has priority.** The
> corpus-grep that preceded this unit was run against `main` and `.beans/`, where
> bean `qou-9yqb` still listed the Lean as its *"next unit"*; the sibling landed
> it in the interval, and announced it in a comment on **#6052** — a thread this
> branch had not read. Recorded as a limit of the six-path checklist rather than
> as an excuse: **a sibling branch's Lean is not on any of the six paths**, and a
> PR comment thread is not either.
>
> What survives as an increment is the **generality**: the hypothesis here is
> `SuperExponential` — exceeds *every* geometric sequence — rather than factorial
> specifically, so the contradiction covers growth classes strictly between
> exponential and factorial. That is real but modest; if #6088's maintainers
> prefer one home, this file should be folded into theirs and deleted, and I have
> said so on both threads.
>
> **(b) This file's header cited the wrong declaration, and the sibling caught
> the same slip in themselves first.** It named `involution_ratio_unbounded`
> (*"`I` leaves every geometric class"*) as the super-exponential half. That is
> too quick: **a geometric upper bound does not forbid unbounded two-step
> ratios** — a sequence may dip far below `K ^ n` at some `n` and jump back,
> making `a(n+2)/a(n)` arbitrarily large while never exceeding `M·Kⁿ`. The
> load-bearing declaration is `factorial_le_involution_two_mul` (`n! ≤ I(2n)`),
> not the ratio lemma.
>
> **The theorems are unaffected** — `SuperExponential` is defined here as the
> negation of the geometric bound itself, which is the property that genuinely
> conflicts, so `not_isConstKernelRec_of_superExponential` was correct as proved.
> Only the header's citation was wrong, and it is fixed.
>
> **The bridge is not formalised here.** Factorial growth on the even indices
> does imply `SuperExponential` (`Kⁿ/n! → 0`), but that argument belongs next to
> the factorial lemma in #6088's file. It is stated rather than proved, and
> deliberately not left as a `sorry`: nothing in this file needs it, since the
> theorems are stated for the general predicate directly. My first attempt at it
> also carried a real error — I bounded `M·Kⁿ` when the index is `2n` and the
> bound must be on `K^(2n)` — which is a further reason it should be written
> where its reader can check it against the factorial statement.

**Consequence for `qou-i5yp`.** That bean asks whether a depth-≤8 Bring
Gauss–Manin recurrence admits `a₂ : a₃ : a₄ = 1 : −0.52 : +4.45`. If the
fixed-depth picture is what gives, the question is moot — settle this first.

---

## M3 — the ramified double cover does not supply `w_3`

**Bean `qou-90b1` (question `qou-v8qx`). Lean:
[`QOU/Mass/DoubleCoverOddBranchSeed.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/DoubleCoverOddBranchSeed.lean),
`lean`-direct exit 0, 0 sorry, `#print axioms` = *does not depend on any
axioms*.**

[`2026-08-29-w3-closeability.md`](2026-08-29-w3-closeability.md) recorded this as
*"untried, and the one route nothing measured here excludes"*, asking: `n=2` seeds
the even branch, what seeds the odd branch?

Index the odd branch directly, `v k := w(2k+1)`, so `v 0 = w_1` and `v 1 = w_3`.
**The one-body seed is forced to vanish** — `w_1` is the binding of a single free
nucleon, zero by definition, which is also why the Ursell inversion starts at
`b₂`. Then:

- **Depth 1** — `v(k+1) = r·v k`. The forced seed propagates: `w_3 = 0`, hence
  `b₃ = 0`, contradicting the measurement. Refuted structurally, for every `r`.
- **Depth 2** — `v(k+2) = p·v(k+1) + s·v k`. For **every** kernel `(p,s)`, two
  solutions agree on the forced one-body seed and take any two prescribed values
  at `w_3`. The route renames the unknown.

Neither horn closes it. The bean's own disposition covers the second: *"if it is
another free constant, the route renames `w_3` and should be recorded as such."*
This is that record; the route moves from **untried** to **measured**.

**Scope.** Depth 1 is a real structural exclusion *of that depth*, invariant
cited (vanishing one-body binding). Depth 2 is not a refutation — it restates
that a rank-2 problem needs two boundary conditions after the base change.
Nothing excludes the base change, its slope computation, or the kernel's
existence on the cover. Depth ≥ 3 is untreated and is strictly worse by the same
counting.

---

## M4 — SU(4) `[1⁴]`: a common scale refuted, and my sign-capability claim corrected

**Bean `qou-u8mu`. Probe:
[`computations/probes/su4_supermultiplet_body_order_sign_probe.py`](../../computations/probes/su4_supermultiplet_body_order_sign_probe.py)
— mpmath at 60 dps, no `float()`, AME from the canonical
`ame_2020_binding_energies` table, no witness, nothing wired.**

>**🛑 RE-SCOPED 2026-08-30.** The Milnor exclusion this section leans on
>(`qou-klgu`) has been re-scoped **(b) → (a)** by its own author: its premise
>*"every bonded pair has `lk = 1`"* is contradicted by the corpus's own triton
>model (`BORROMEAN`, pairwise `lk = [0,0,0]`, on three **bonded** pairs), and
>on the branch that saves the premise `M₃(T) = 0` makes `e₃` a division by
>zero. The conditional survives; its hypothesis is not established. So "the one
>named candidate left" below overstates how narrow the field is — the μ̄ route
>is **not** structurally excluded, only conditional. See
>[`bonded_pair_linking_inconsistency_probe.py`](../../computations/probes/bonded_pair_linking_inconsistency_probe.py)
>and the note on that audit.

After the Milnor exclusion (`qou-klgu`) the one named candidate left for the
super-pairwise content is the **non-link-invariant** Wigner SU(4) `[1^n]`
antisymmetriser, `dim = C(4,n)`, vanishing for `n > 4`
(`SU4SupermultipletGate`, sorry-free). Given M1, the first question is not "does
it hit 9.24 MeV" but the one that killed its two predecessors.

**Leg 1 — sign capability. 🛑 CORRECTED 2026-08-30, against my own claim.**
`C(4,n) > 0` for `n = 2,3,4`, so with positive per-order energies every
connected cumulant is positive. I wrote that this makes SU(4) *"the first
candidate in the corpus not sign-obstructed at 3-body"*. **That overstates it.**
The property is `C(4,n) > 0` — binomial arithmetic — so it is **analytic**, and
it holds for *any* object with positive per-order weights whether or not it has
anything to do with binding. It discriminates nothing, and every
positive-weight assembly is equally "sign-capable".

What actually singles the object out is structural, not numerical: it is a
**non-link-invariant, non-pairwise** object, so neither the Milnor `μ̄`
indeterminacy exclusion nor `PairwiseCumulantVanishing` reaches it. **Cite the
exclusions it survives, never its positivity.**

This is the failure mode bean `qou-04ub` AMENDMENT 1 already recorded against
the *same object one step over* — a choice-free candidate whose definite
prediction is **analytic rather than synthetic** — and I walked into the
neighbouring instance of it while citing that object. Their diagnostic question
is the one to apply: *could the prediction have come out otherwise, given the
specification?* For `C(4,n) > 0`, no. See
[`prereg_su4_prediction_is_analytic_probe.py`](../../computations/meson/prereg_su4_prediction_is_analytic_probe.py).

**Leg 2 — zero-parameter ratio test.** A single common scale forces the ratios:

| | predicted `C(4,n)/C(4,2)` | measured | err |
|---|---:|---:|---:|
| `b₃/b₂` | 0.666666666667 | 0.641122822059 | **−3.83 %** |
| `b₄/b₂` | 0.166666666667 | 4.15514025161 | +2393 % |

**A single common scale is refuted by the `b₄` row** — scope-(a).

**Leg 3 — genericity control, and it cuts against the near-match.** Two
corrections were needed before this could be reported, and both are recorded
because each would have inflated the result:

1. The window was first normalised by the **measured** value while the miss in
   Leg 2 is normalised by the **candidate**. That is the normalisation trap
   AGENTS.md records for the `c₃` 3.47 %/3.35 % pair, and it excluded `2/3` from
   its own window.
2. The count was over `(p,q)` pairs rather than **values**, so `4/6` and `6/9`
   were counted as distinct from `2/3`, inflating the window from 2 to 4.

Corrected: `2/3` is alone only at `q ≤ 6`; at `q ≤ 9` it is joined by `5/8`, at
`q ≤ 12` by `7/11`. **So the 3.83 % agreement discriminates weakly and must not
be reported as an identification.** And Leg 1's sign result does **not** rescue
it — that is analytic, per the correction above, so neither leg discriminates.
What survives is neither leg's number but a structural fact they do not measure:
the object is **non-link-invariant and non-pairwise**, so it escapes both the
Milnor and the pairwise-additivity arguments.

**Leg 4 — required per-order energies (diagnostic, not a derivation).** Under
the SU(4) weighting, `e₂ : e₃ : e₄ = 1 : 0.9617 : 24.93`. Against the
multiplicative model's required `1 : −0.5198 : +4.4504` (`qou-i5yp`), the SU(4)
weighting **removes the sign alternation** — all three required ratios are
positive — and concentrates the difficulty in a large 4-body enhancement at the
closed shell, which is where the "non-transferable shell closure" language
already puts it. Reading these off the anchors and wiring them would be the
anchor inversion the Δ_λ gate forbids; they are printed as a falsifiable target,
exactly as `qou-i5yp` is framed.

---

## M5 — the `M_n(K)` blocker is stale, and the counts cannot supply the surplus

**Bean `qou-p76y`.**

[`2026-08-29-w3-closeability.md`](2026-08-29-w3-closeability.md) §R3b argues a
few-body truncation helps only if `M_n(K)` is **derived** from the canonical
braid, and says that is *"blocked upstream"* because the deuteron's link is
undetermined — citing
[`2026-08-21-deuteron-knot-assignment-adjudication.md`](2026-08-21-deuteron-knot-assignment-adjudication.md).

**That clause is stale.** The owner ruled **Option A** on 2026-08-29
([`2026-08-29-deuteron-knot-owner-decision.md`](2026-08-29-deuteron-knot-owner-decision.md)):
the deuteron knot is the canonical braid closure, with the explicit corollary
that the 2-body binding is **not** a hyperbolic-volume term and is sourced from
the Gram/Frobenius pairing plus confinement SDP. The two documents are the same
day and R3b cites the earlier adjudication, which is how they crossed.

**What the lifted blocker actually buys, measured.** With the deuteron link
fixed, the topological counts for `A ≤ 4` are determined rather than free:
`M₂ = C(A,2)` (derived fit-free, #3588) and `M₃ = M₄ = 0` (Milnor indeterminacy
— **conditional, re-scoped 2026-08-30**, see the note in M4:
on the max-contact tetrahedron, `qou-klgu`). The tower then predicts

```
B(⁴He) = 6·b₂ = 13.3473972 MeV   against AME 28.2956624 MeV   (47.2 %)
surplus the counts cannot supply = 14.9482652 MeV
```

reproducing `qou-klgu`'s 14.948 MeV exactly, from the other direction.

**So M5's contribution is a narrowing, not a closure.** The topological side is
**not** where the remaining freedom lives for `A ≤ 4` — the counts are fixed and
they under-predict by a factor 2.12. That sharpens M1: the freedom is in the
body-order weights and the assembly that combines them, which is exactly where
M1 shows the current functional cannot go.

---

## What this tranche does and does not establish

**Establishes:**

- Both corpus assemblies are proved incapable of `b₃ > 0` (M1 completes the
  dichotomy).
- The fixed-depth and super-exponential claims are machine-checked incompatible
  (M2), without adjudicating between them.
- The double-cover route is measured and does not supply the missing base case
  (M3).
- The SU(4) `[1⁴]` object is sign-capable, and a single common scale for it is
  refuted (M4).
- The `M_n(K)` "blocked upstream" clause is stale, and the fixed counts
  under-predict ⁴He by 14.948 MeV (M5).

**Does not establish, and must not be read as:**

- **Nothing here closes the magnitude. The gate remains OPEN.**
- No `(b)` structural exclusion is claimed beyond the two that cite an invariant
  (M3 depth-1, via the vanishing one-body binding; and the pre-existing ones
  quoted). Convention D is not impugned, the Mayer assembly is not excluded as a
  *component*, the SU(4) route is not derived, and §10a's premises stand.
- The M4 ratio agreement is **not** an identification — the genericity control
  says so explicitly, and two of my own errors in constructing that control are
  recorded above rather than quietly fixed.
- No per-order weight is derived anywhere here, and none is wired.

## Reproduce

```bash
python3 -u computations/probes/su4_supermultiplet_body_order_sign_probe.py
# Lean, against a restored olean cone (lake-cache/qou-v4-24-0):
lean content/quantum-observable-universe/lean/QOU/Mass/PairwiseCumulantVanishing.lean
lean content/quantum-observable-universe/lean/QOU/Mass/ConstantKernelGrowthBound.lean
lean content/quantum-observable-universe/lean/QOU/Mass/DoubleCoverOddBranchSeed.lean
```
