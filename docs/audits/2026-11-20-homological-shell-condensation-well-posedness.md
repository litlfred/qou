# Homological shell condensation: what a well-posed statement needs

Bean `qou-6qbv`. Owner, 2026-11-20: "Can you prove the conjecture", then chose
option 1, "make it well-posed, then attempt it".
Block: [`conj:homological-shell-condensation`](../../folio/quantum-observable-universe/mass-endomorphism/homological-shell-condensation.md).

## 1. The statement as written

For `n ∈ 𝔐 = {2, 8, 20, 28, 50, 82, 126}`, the Białynicki-Birula (BB) spectral
sequence on the jet algebra `A_n` has `E_∞^{p,q}(n) = 0` for `p ∈ ℕ`, `q > 0`.

## 2. Gaps, each checked against the corpus

| # | Object | What the corpus says | Gap |
|---|---|---|---|
| G1 | `A_n` | `A_{n+1} = J¹(A_n) = A_n ⊗ Ω¹(A_n)`, `Ω¹ = ker(m)` (`prop:jet-prolongation`) | A tensor product of an algebra with a bimodule. No multiplication is defined on it; "inherits a canonical Frobenius–Hopf structure" is asserted, not constructed. |
| G2 | the index `n` | `n` is the tower level | The magic numbers are nucleon counts. `magic-numbers-bring` reads them as ranks of period sub-lattices, not as tower levels. Level 126 of the tower has `dim A_126` growing like `d^(3^126)`, which no reading of the physics uses. |
| G3 | the ℂ^× action | induced by the "descent involution" `τ̂` | `def:descent-involution` proves `τ̂² = τ̂`: it is an **idempotent**, not an involution. An idempotent gives at best the weight split `im τ̂ ⊕ ker τ̂` (weights 0 and 1), so a BB filtration with two steps. |
| G4 | `H^q(gr^p_F A_n)` | not specified | Sheaf, Hochschild, or the cohomology of some complex: none is named. |
| G5 | the "equivalently" clause | the trace on `J^ℓ/J^{ℓ+1}` | That is the confinement filtration on the Hecke algebra, a different object; and that filtration is not preserved by the Hochschild differential (`gb_spectral_sequence_h3_probe.py`). |

## 3. The Lean carrier is satisfiable with no content

`QOU.ShellCondensation.HomologicalConjecture` takes the page entries `EInfty p q`
as free types. Setting every entry to `PUnit` gives an instance for every
saturated `n`; this compiles (`lean -DautoImplicit=false`, exit 0, scratch
file, not committed). So the Lean class records the shape of the claim but
constrains nothing.

## 4. Readings that make it precise, and what each gives

| Reading | Algebra | Filtration | Cohomology | Result |
|---|---|---|---|---|
| R1 | `H_n(q)`, `n` = nucleon count | Coxeter length (`prop:gb-spectral-sequence`) | Hochschild | `HH^k = 0` for `k > 0` whenever `H_n(q)` is semisimple (Hochschild 1945), which holds at the real `q₀` for every `n`. So `E_∞^{p,q} = 0` for `p ≥ 0, q > 0` at **every** `n`. Checked exactly at `n = 3`: `E_∞` lies in total degree 0 at filtration degrees `0, −2, −3`. |
| R2 | any commutative `A_n` | any | sheaf cohomology on `Spec A_n` | Affine, so `H^q = 0` for `q > 0` at **every** `n` (Serre vanishing). |
| R3 | `End(A_{n+1})` with `τ̂` | two-step split `im τ̂ ⊕ ker τ̂` | Hochschild | Needs G1 first. When `C` is semisimple, `End_C(A_{n+1})` is a finite product of matrix algebras, hence separable, so `HH^{>0} = 0` at **every** level. |

## 5. Conclusion

Under every precise reading found, the vanishing holds for all `n`, so it does
not single out the magic numbers. That is a scope-(a) finding about these
readings, not an exclusion: a reading under which non-magic `n` fail would need
a non-separable algebra or a cohomology with coefficients other than the
algebra itself, and none is in the corpus. The conjecture's intended content,
that the vanishing is special to `𝔐`, is therefore not yet stated.

What would make it attemptable:

1. Fix `n` as the nucleon count (G2).
2. Name the algebra, the grading and the cohomology (G1, G3, G4), choosing ones
   under which some non-magic `n` gives a nonzero entry. Otherwise the
   statement is true and empty.
3. Rebuild the Lean carrier on that construction, so the page entries are
   computed rather than supplied.

## 6. Formalize-first derivation (owner: "Formalize first and try to derive")

Lean, sorry-free, `QOU/ShellCondensation/SelectorPrune.lean` (lean-direct exit 0;
axioms `propext`, `Quot.sound`, plus `Classical.choice` for the first):

- `offDiag_vanish_iff_pure`: for a first-quadrant limit page with entries of
  dimension `E p q` abutting to `H k = Σ_{p+q=k} E p q`, the conjectured
  vanishing `E p q = 0` for `q > 0` holds **iff** every `H k` sits entirely in
  filtration degree `k`. So the conjecture is a **purity** statement: the
  grading must make cohomology pure. It is not the statement "`H^{≥1} = 0`".
- `not_upward_closed`, `not_downward_closed`: no predicate on `n` that is
  preserved by `n ↦ n+1`, or by `n+1 ↦ n`, agrees with the magic set on
  `0..126`. The witnesses are `2, 3` and `8, 3`.

What this derives, for each candidate reading:

| Reading | Selector it offers | Verdict |
|---|---|---|
| Hecke `H_n` at generic or real `q`, Hochschild | none: true at every `n` | `cor:hecke-length-limit-page-vanishing` |
| Hecke `H_n` at a root of unity of order `e` | semisimplicity, which by Dipper–James fails exactly for `n ≥ e` | upward closed, so excluded by `not_upward_closed` (scope (b) for semisimplicity as the selector) |
| BB on a smooth projective variety with isolated fixed points | purity | holds for every such variety (cell decomposition), so no selection |
| Hochschild of `H_n` with a chosen coefficient module | depends on the module | **open** |
| Bring-surface `S_5 × τ̂` period sub-lattices (`magic-numbers-bring`) | already indexed by the magic ranks | **open**, and the only reading where the corpus links the magic numbers to anything |

So the derivation narrows the target. A working reading needs a **purity**
criterion whose truth set in `n` is **neither upward nor downward closed**.
Every selector built from semisimplicity, separability or generic vanishing is
monotone or constant, and is excluded. The two open rows are where a derivation
could still succeed; neither has a definition in the corpus that would let the
spectral sequence be written down.

## 7. The two open readings, tested (owner chose both)

Both are **scope (b)** for the objects tested. Neither reading can select the
magic numbers.

**Bring-surface lattices.** `computations/probes/bring_s5_sublattice_rank_probe.py`
(integers and `Fraction` only) builds Bring's curve as the S₅-cover of P¹ with
signature (2,4,5), checks genus 4 by Riemann–Hurwitz, and gets the character of
`H_1` from Lefschetz fixed-point counts: `(8,−4,0,2,2,0,−2)` on the classes
`1,(12),(12)(34),(123),(123)(45),(1234),(12345)`. Inner products give
`H_1(Bring, Q) = 2·(std ⊗ sgn)`, a single 4-dimensional isotypic type (checked
again by hand: ⟨χ,std⊗sgn⟩ = 2, ⟨χ,std⟩ = 0, ⟨χ,χ⟩ = 4). So **every S₅-stable
sublattice of `H_1^{⊕k}` has rank divisible by 4**: 2, 50, 82 and 126 are not
ranks, and 4 is a rank that is not magic. Lean
`QOU/ShellCondensation/BringLatticeRanks.lean`: `finrank_dvd_of_isotypic`,
`four_dvd_finrank_of_isotypic`, `bring_H1_character`, `chiH1_eq_two_stdSgn`,
`magic_four_dvd_iff`, `four_dvd_ne_saturated`. Not mechanised: the construction
of `H_1(Bring)` and its S₅ action (the character is an input checked by the
probe), and the step from lattice rank to the dimension of the rational span.
Not covered: lattices stable only under a subgroup of S₅.

The corpus never constructs the τ̂ action on `H_1`, and τ̂ is an idempotent, so
"S₅ × ⟨τ̂⟩" is not a group. A τ̂ commuting with S₅ only shrinks the family of
stable sublattices, so divisibility by 4 still holds.

**Corpus error found on the way.** `mass-theory/substrate-cohomology-calibration-story.md:3`
says `H^1 = 2 × standard`. The character above gives `2 × (standard ⊗ sign)`.
Not edited here.

**Coefficient modules.** `computations/probes/hochschild_coefficient_purity_probe.py`
(mod 1000003 and 999983, at q = 2 and 3, all four runs agree). `H_n` is
separable at real `q > 1`, so `HH^k(H_n, M) = 0` for `k ≥ 1` and **every**
bimodule `M` (Weibel Thm 9.2.11; not formalised, since Mathlib has no
Hochschild cohomology). The limit page then lives in degree 0, where it is the
graded `M^A`.

- The literal statement (`p ≥ 0, q > 0`) is true for every `n` and every `M`.
- Read as purity of `M^A`, it fails for every `n ≥ 2` when `M = H_n` or
  `H_n^*`: the weight-0 slice is 1-dimensional while `dim M^A = p(n) ≥ 2`. It
  holds for every `n` for the 1-dimensional bimodules.

Each bimodule tested gives a predicate on `n` that is constant for `n ≥ 2`.
`not_upward_closed` excludes all of them. Lean
`QOU/ShellCondensation/CoefficientPurity.lean`:
`offDiag_vanish_of_higher_vanish`, `finrank_add_le_of_pure`.

## 8. Where this leaves the conjecture

Every reading tested selects nothing, so the conjecture is **open with no
known reading under which it has content**:

- generic Hecke algebra;
- Hecke algebra at a root of unity;
- Białynicki-Birula purity on a smooth projective variety;
- seven natural coefficient bimodules;
- S₅-stable Bring lattices.

For any future reading, the binding constraints are three:

- purity, not mere vanishing;
- a truth set in `n` that is neither upward nor downward closed;
- for lattice readings, a rank invariant compatible with 2, 50, 82 and 126.
