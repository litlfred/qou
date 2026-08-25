# The proton/neutron test does not establish writhe-independence

**Date:** 2026-08-10
**Status:** proved sorry-free; scope-(a) — about the published argument, not about `Y`

## The question

`flavor-charge-assignments.md` and `eightfold-open-problems.md` item 2 rest the
entire hypercharge programme on one requirement:

> The writhe map is falsified as a hypercharge assignment: the proton and
> neutron share `Y = +1` while their writhes differ. The framework therefore
> requires a second crossing invariant, **independent of the writhe**, to
> instantiate `Y`.

Same argument in the originating audit
[`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md),
with derived framing writhes `w(p) = +2`, `w(n) = −2`.

Three questions: is the independence requirement **Lean-proved**? Is the
**physics argument** valid? What is needed from the **literature**?

## 1. Lean-proved? — No

No Lean declaration in the corpus proves either the writhe-falsification or
the independence requirement. Searching every `.lean` mentioning both
`writhe` and `hypercharge` returns only `HyperchargeBatteryReduction.lean` and
`SecondCrossingInvariant.lean`, both from PR #4597, and neither proves it.
The requirement is prose, sourced to a prose audit.

## 2. Physics argument? — the premise is right, the inference is not

Equal `Y` at *distinct* writhes falsifies an **injective** writhe→`Y` map — in
particular the linear `Y = c·w` the framing phase `q^{w·c}` would give. It says
nothing against a *non-injective* function of the writhe: a function may take
the same value at two different points.

Concretely, **`Y = w²/4` reproduces both rows**: `(+2)²/4 = 1`, `(−2)²/4 = 1`.
So the p/n test is *consistent* with `Y` factoring through the writhe, and
cannot be what forces independence.

Proved in
[`WritheIndependenceCriterion.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/WritheIndependenceCriterion.lean):

| Theorem | Statement | Axioms |
|---|---|---|
| `pn_test_admits_writhe_only_map` | an explicit writhe-only map gives `Y = +1` at `w = ±2` | `[propext, Classical.choice, Quot.sound]` |
| `injective_writhe_map_is_falsified` | what the test *does* establish: no **injective** `f` works | `[propext]` |
| `equal_writhe_distinct_Y_forces_non_factoring` | equal writhe + different `Y` ⟹ `Y` is not **any** function of `w` | `[propext]` |

## 3. The requirement is probably still right — the reason is what fails

The corpus already has the correct argument *shape*.
`SecondCrossingInvariant.lean`'s `baryon_vacuum_separating` exhibits two states
of **equal writhe** (`0` — the Borromean baryon, per the s5-so3 audit) with
**different** baryon number (`1` vs `0`). Under `Y = B` on the non-strange
sector that is exactly `equal_writhe_distinct_Y_forces_non_factoring`.

But that lemma takes its writhe and `B` values as **hypotheses**; it derives
neither. So independence today is *supported by a correct argument shape whose
premises are assumed*, not proved. **Closing it needs two derived facts:** the
writhe of the baryon and of one state with different `Y` at the same writhe.

## 4. What is needed from the literature

The internal gap above is a corpus task, not a literature one. What the
literature *is* needed for is making the writhe side well-posed at all, and the
four papers uploaded in `2988eb82` are exactly the right set:

- **Kauffman 1987**, *State models and the Jones polynomial*, Topology 26 395
  (`library/1-s20-0040938387900097-main/1-s2.0-0040938387900097-main.pdf`). The load-bearing point: the
  **writhe is not an ambient-isotopy invariant** — it shifts by `±1` under
  Reidemeister I. It is a *regular-isotopy* / framed quantity. So "`Y` is a
  function of the writhe" is not even well-posed until a framing convention is
  fixed; and once fixed, `w` is part of framed data, not knot data.
- **Moffatt & Ricca 1992**, Proc. R. Soc. A 439 411
  (`library/procrsoclondona92/procrsoclondona92.pdf`). Călugăreanu–White–Fuller `Lk = Tw + Wr`:
  the framed invariant of which the writhe is one summand. This is what decides
  whether "independent of the writhe" is even a stable notion — under a *fixed*
  framing, `Tw` and `Wr` are not independent.
- **Kirby 1978**, Invent. Math. 45 35 (`library/kirbycal/kirbycal.pdf`). Framed links,
  where framing `+n` and `−n` are distinguished on an amphichiral knot.
- **Reshetikhin & Turaev 1990**, CMP 127 1 (`library/reshetikhin-turaev/Reshetikhin_Turaev.pdf`).
  The ribbon twist `θ` — the categorical form of the same datum.

The sharpest consequence of the Kauffman point, and it is not yet recorded in
the chapter: **if the framing is fixed, then by CWF the writhe and the twist
are not independent** (`Wr = Lk − Tw`). So a second invariant that is
"independent of the writhe" but built from the *framing* is at risk of being
the writhe in disguise. That directly threatens the chapter's own
ribbon-framing-twist candidate `T(t)`, and it is the reverse of the tension
recorded for lepton number in
[`2026-08-10-lepton-number-grading-obstruction.md`](2026-08-10-lepton-number-grading-obstruction.md),
where `L` appeared to *need* framing.

## Honest scope

**Scope-(a)**, about what the published argument establishes. It does **not**
show `Y` factors through the writhe (it very likely does not), and does not
weaken the search for a second invariant. It shows the *stated justification*
is insufficient, and names the test that would suffice.

## Verification

`lean`-direct exit 0; `#print axioms` as tabled, no `sorryAx`; negative control
(breaking the rewrite chain) fails as it should; 0 `sorry`, 0 `native_decide`.
`ℤ`-valued writhe, `ℚ`-valued charge, no `Real` (§7c). CI unavailable
repo-wide; the above is the gate.
