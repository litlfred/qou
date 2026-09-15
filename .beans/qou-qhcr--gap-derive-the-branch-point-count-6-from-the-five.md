---
# qou-qhcr
title: 'GAP: derive the branch-point count 6 from the five QOU axioms (the ONE missing step in the chi = -6 chain)'
status: in-progress
type: task
priority: high
created_at: 2026-09-15T06:16:39Z
updated_at: 2026-09-15T06:46:44Z
---

Child of `qou-51l1` (which established that the χ = −6 chain is
derived-modulo-one-named-input, and named this as the one missing step).
Session `claude/chi-branch-point-count-2026-09-15`.

**Outcome: the 6 is still not derived. The ADE / finite-subgroup-of-SU(2)
route was tested and is a negative, and the negative is informative — an
orbit reading of "six branch points on `ℙ(V)`" points AWAY from the
icosahedral case, not toward it.**

Artifacts, both on the branch:

- `content/quantum-observable-universe/lean/QOU/BringsSurface/BranchPointSixNotForced.lean`
  — sorry-free (`#print axioms`: `propext`, `Quot.sound` only; several
  theorems depend on no axioms at all), import-free, `lean`-direct
  `-DautoImplicit=false -s 65536` exit 0 in 0.9 s.
- `computations/chi_branch_point_count_genericity_probe.py` +
  `computations/chi-branch-point-count-genericity.witness.json` — 18/18
  checks, exact `int`/`Fraction` throughout (no float64), independent
  re-derivation of the same arithmetic by the rational orbifold-Euler
  route rather than the Lean's cleared-denominator integer route.

## 1. How much the derived steps actually give

Step 3 (Riemann–Roch, `χ = 2 − 2g`) + Step 4 (`g ≥ 1`) constrain `χ(A)` to
**exactly the non-positive even integers, and no further** — proved both
ways (`step34_admissible_iff`). Step 6 ("the sign is negative") adds
nothing; it is implied by Step 4. So **Step 5 alone supplies `−6`, one
value out of a countably infinite set.**

This is the formal version of what `brings-surface/universality-general.md`
already says in prose — *"for any admissible Euler characteristic χ …
analogous universal objects are expected at other values of χ"* — which
`qou-51l1` flagged as the cleanest single piece of evidence in the corpus.

## 2. "Six branch points" over ℙ¹ does not fix χ even given the degree

The corpus's own six-branch-point datum is a cover of **ℙ¹**
(`brings-qou-4tuple.md:15`, degree 3; `brings-is-qou-verification.md:15`,
degree 4 with `R = 14`). Over ℙ¹, `χ = 2d − R` with `R` the **total
ramification**, not the branch count; a branch point contributes between 1
and `d − 1`. At the corpus's own `(d, b) = (4, 6)`, `R ∈ [6, 18]` and the
genus ranges over **0…6**. So the branch *count* determines nothing near
`g = 4`; the number that does the work is `R = 14`, which no block derives.

## 3. Step 5's parenthetical is false, and the real 6 is one line further on

**Already known to the corpus** — recorded at `chi-minus-six-chain.qa.json:1611`,
`content/bib-qa-verifications.json:11038` and `:11072`, and bean `qou-xz89`
— so this is a confirmation, not a discovery. Two things are new.

First, the existing flag reaches the right conclusion by a wrong route: the
`.qa.json` note says six Weierstrass points is "impossible for genus 4
(minimum 2g+2 = 10)". `2g + 2` is the **hyperelliptic branch-point** count;
Bring's curve is not hyperelliptic. The correct figure is the total
Weierstrass weight `g³ − g = 60`, all of weight 1, with `Aut(B) = S₅`
acting **transitively** (Braden & Disney-Hogg Prop. 3.3,
`library/s40879-023-00706-0/sections/sec-006-31-weierstrass-points.md:42`).

Second — and this is the useful part — the same source, one paragraph
later, gives **`60 = 6 × 10`: six Weierstrass points fixed by each of the
ten transpositions in `S₅`**. So there *is* a real 6 here, and Step 5 is
one substitution away from being coherent:

> the carrier is a **transposition** (an involution), not an `S₃`; the 6 is
> a **per-involution fixed-point count**, not a total; and the degree-2
> quotient `B → B/⟨τ⟩` then has **genus 1** by Riemann–Hurwitz, giving
> `χ(B) = 2·χ(torus) − 6 = −6`.

That repairs the citation. It does **not** make Step 5 a derivation — it
still reads the 6 off Bring's curve, which the chain identifies at Step 7.
And the `R = 6` is not forced by `χ = −6` with `g ≥ 1` either:
`(d, h, R) = (2, 1, 6)`, `(2, 2, 2)` and `(3, 2, 0)` all give `−6`.

## 4. The torus-knot route of `EulerCharacteristicSix.lean` restates its target

That file derives `g = 4`, sorry-free, from "`T₂,₉` embeds (Seifert rank
`4 ≤ g`) and `T₂,₁₁` does not (`5 ≰ g`)". The arithmetic is right and the
file says outright that "neither step is deep". Measured how shallow:
`seifertRank(2, s) = (s−1)/2`, so for **every** genus `g` the pair
`T₂,₂g₊₁ / T₂,₂g₊₃` brackets it — and at `g = 4` that pair is exactly
`(9, 11)`. The constraint pair carries precisely the information "the genus
is 4" and nothing more.

## 5. The ADE route — tested, negative at three joints

**(a) Nothing makes `G` finite.** `su2_emergence_rank_forced` constrains
`G` (a bare `Set`) only by "unitary and `det = 1`", which `SU(2)` itself
satisfies; `qou-axioms-physical-reading.md` says axiom 5 is *"the condition
that makes the reconstructed gauge group `SU(2)`"*. The ADE/McKay list
classifies **finite** subgroups, so the classification does not apply to
the object the axioms deliver. This is prior to the type question and it is
where the route actually dies.

**(b) One axiom prunes, to four families.** Observability
(`Hom(𝟙, Ad(A)) = 0`), read literally as "the 3-dimensional adjoint has no
invariant vector", excludes exactly the **cyclic** family: a cyclic
rotation group fixes its axis. Dihedral, tetrahedral, octahedral and
icosahedral all survive. (Caution recorded in the Lean: the *physical
gloss* in `qou-axioms-physical-reading.md` — "gauge transformations that
act as the identity on every observable" — is the **kernel** of `Ad`, a
different condition, under which every binary subgroup fails since `{±1}`
is always in the kernel. The two readings are not interchangeable and
neither is formalised anywhere in the corpus; `qou_ns_in_qou` carries
observability as an opaque `Prop` field.)

**(c) Granting both, the icosahedral case does not produce a 6.** The three
exceptional orbits of the icosahedral rotation group on `ℙ(V)` have sizes
**30, 20, 12** — all ≥ 12. Six **is** an exceptional orbit size for the
**tetrahedral** (`E₆`: 6, 4, 4), **octahedral** (`E₇`: 12, 8, 6) and
**dihedral-6** groups. So an orbit reading of "branch points on `ℙ(V)`"
points *away* from `E₈`. The cone-order and orbit tables are not asserted:
they are cross-checked by Klein's relation `χ_orb = 2/|Ḡ|` (exact rational,
all 13 families in the probe), so a wrong cone order fails a theorem.

The **Sylow** reading does select `E₈` — `n₅(A₅) = 6 = |ℙ¹(𝔽₅)|`, the
source of the exceptional `A₅ ↪ A₆` — and the Sylow arithmetic is derived
here rather than asserted (`n₅ ∣ 12`, `n₅ ≡ 1 mod 5` ⟹ `n₅ ∈ {1, 6}`;
simplicity of `A₅` picks 6, cited). But the two readings **disagree on the
same group in both directions**: on the icosahedral group Sylow gives 6 and
orbits do not; on the tetrahedral group orbits give 6 and Sylow does not
(`n₃(A₄) ∈ {1, 4}`). So **6 is a property of the chosen invariant, not of
the ADE type**, and nothing in the axioms names the invariant. Choosing the
Sylow reading *because* it returns 6 is selection against the target, which
AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3" forbids.

Genericity sanity check: of 16 natural integer invariants of `A₅` (irrep
dimensions 1,3,3,4,5; conjugacy class sizes 1,15,20,12,12; orbit sizes
30,20,12; Sylow counts 5,10,6), exactly **one** equals 6. So 6 is not
*generic* for `A₅` — but it is also not *selected*, which is the point.

## 6. The one narrowing found that is not a read-off

**Laing & Singerman, "Transitivity on Weierstrass points", Ann. Acad. Sci.
Fenn. Math. 37 (2012), Theorem 15** — quoted as Theorem 3.4 of
`[braden-disney-hogg-2022]` at
`library/s40879-023-00706-0/sections/sec-006-31-weierstrass-points.md`, and
independently noted in `content/bib-qa-verifications.json:11038` for the
arXiv note `2211.08164v2`:

> a Riemann surface of genus `g > 2` with `g³ − g` Weierstrass points on
> which `Aut` acts **transitively** is Bring's curve (`g = 4`), Klein's
> quartic (`g = 3`), or a genus-3 curve with `Aut ≅ S₄`.

The hypothesis is a **homogeneity** statement — *no Weierstrass point is
distinguishable from any other, and none is distinguished by weight* — in
the same register as the observability axiom, and it says nothing about the
number 6. It narrows `χ(A)` from the infinite set of §1 to **exactly two
values, `{−4, −6}`**. Separating them needs one further input: an
automorphism of **order 5**, since by Cauchy `5 ∣ 120` while `5 ∤ 168` and
`5 ∤ 24`.

**This is not a closure and must not be reported as one.** It replaces one
unsourced input (the integer 6) with two structural ones, neither derived
from the five QOU axioms here. Its value is that both are group-theoretic
statements of a kind an axiom could plausibly supply, whereas "exactly six
branch points" is not — and that the narrowing is *honest*, in that it
leaves genus 3 open rather than landing on 4.

## Scope, per AGENTS.md §"Before declaring refuted"

- §5(c) is a **scope-(b) structural exclusion** of the *specific*
  implication "icosahedral type ⟹ six branch points on `ℙ(V)`". The
  invariant is the orbit-size formula `|Ḡ|/mᵢ` and it is proved. It is
  **not** a claim that no finite-group route can produce a 6 — three other
  ADE types do.
- §4 is likewise an exclusion of the *form* of the torus-knot constraint,
  not of its conclusion (`g = 4` may still be right).
- §5(a) is a structural insufficiency: an explicit infinite model (`SU(2)`
  itself) satisfies the hypotheses.
- Everything else is **scope-(a)**: these constructions, alone, do not
  derive the 6.

## Still open — the sharpest statement of what would source it

> **Steps 3 + 4 pin `χ(A)` to the non-positive even integers and nothing
> more. Every candidate source tested either restates the target (the
> torus-knot bracket), reads it off Bring's curve (the Weierstrass /
> transposition fixed-point count), or fails to produce a 6 at all (the ADE
> orbits). The one hypothesis that narrows without naming 6 is
> transitivity of `Aut` on the Weierstrass points, which gives
> `χ ∈ {−4, −6}`; separating those two needs an order-5 automorphism.**

So the next question is **not** "derive 6". It is:

1. **Does an axiom supply homogeneity?** — i.e. does the QOU substrate
   force `Aut(M₀)` to act transitively on the Weierstrass points, with all
   weights 1? Observability is the natural candidate (*"no hidden global
   symmetries"* / no distinguished internal direction), and it is currently
   an opaque `Prop` field, so the question is open and formalisable.
2. **Does an axiom supply an order-5 automorphism?** The corpus's `ζ₅`
   pentad, the Bring–Jerrard quintic and the `(2,4,5)` triangle group all
   carry one — but all three are Bring-derived, so as things stand this is
   the same read-off one level down. An axiom-level source for order 5 is
   the harder half and I did **not** find one.

Both are group-theoretic. Neither is an integer to be guessed.

## Not done, deliberately

No content block was edited. Correcting Step 5's parenthetical is arguably
AGENTS.md exemption 2 (a held source decides it), but *what Step 5 should
say instead* is a reading of the chain, and that is the owner's call — the
same disposition `qou-51l1` took on `chapter-overview.md:30`.
