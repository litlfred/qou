# Provenance audit of the seven `N = 3` exclusions

**Bean:** `qou-bhfg`. **Date:** 2026-08-25.

**Trigger.** Owner question, this session: *"note that some excluded route may
be based on old probes using incorrect compute — ok to be skeptical if not lean
proved exclusion."*

That is the right question to ask of this table. The `N = 3` exclusion list in
[`sm-eightfold-derivation-cheat-sheet.md` §4-A](../sm-eightfold-derivation-cheat-sheet.md)
is load-bearing: it is what makes the eightfold surface's live question a
*single* one, and AGENTS.md §"Formalize-first probe discipline" instructs agents
to treat that table **as the prune** rather than re-run a scan it covers. A
route excluded on stale compute would therefore not merely be one wrong row —
it would be a permanently closed door with nothing behind the lock.

The corpus has live reasons for the worry. Convention C (`z = √q/(q+1)`) was
excised in favour of convention D (`z = q³/(q²+1)`) on 2026-08-09 and re-affirmed
2026-08-15, and AGENTS.md records that the C surface should be treated as
**unmeasured rather than clear**. Separately, the `Q_β` `c_k` ladder is
C-frame throughout and is *not* re-derived. If an exclusion consumed either, it
would be conditional on a superseded convention and would not know it.

## Result

**It does not pay out, and that is worth stating as plainly as a positive would
be.** Seven routes, seven checked:

- **Zero** rest on float64 arithmetic.
- **Zero** consume the Markov/Ocneanu parameter `z`, so **none** is
  convention-C-conditional.
- **Six of seven** stand on a proved invariant, an exact symbolic identity, or
  an elementary dimension count.
- **Two** carry citation defects — a true-but-uncited claim and a dead pointer.
  Both are presentation, not substance.

| # | Route | Backing | Kind | Verdict |
|---|---|---|---|---|
| 1 | Odd-dim summand of `V^⊗n` | `QOU/Eightfold/Sym2GateParity.lean`, sorry-free | Clebsch–Gordan + Frobenius–Schur parity, `[fulton-harris1991]` §11 | **sound** |
| 2 | Permutation `S₃ = W(A₂)` 3-dim rep | same criterion (odd dim ⇒ FS `+1`) | as (1) | **sound** |
| 3 | Re-tune the Ocneanu parameter to `N = 3` | `y_{(2,1)}/y_{(3)} = q[2]_q[N−1]_q/[N+2]_q` | exact symbolic ratio in `(q, N)`; the non-proportionality **now Lean-proved** (see below) | **sound** |
| 4 | Hecke centralizer on regular `H₃` | `QOU/StandardModel/ColourHeckeRegularHost.lean`, sorry-free | exact `ℚ` matrices, `dim ≤ 6 < 8` | **sound**, scope stated in-file |
| 5 | 4-form → `Spin(7)` → `G₂` → `SU(3)` | one table row, no citation | elementary dimension count | **true, uncited** — see below |
| 6 | `S₄` / Fano bridge → Klein quartic | "marked-pair obstruction" | pointer resolves nowhere | **unresolved citation** |
| 7 | Tetraplectic / quaternionic | supplies `SU(2)`, already spent | structural | **sound**, but see the scope note |

## Route 3 — the one the worry actually targeted

The Ocneanu parameter is the closest thing on this surface to the object the
C→D excision moved, so it is where a stale-compute exclusion would most plausibly
hide. It does not: the exclusion is
[`2026-08-07-two-row-projection-is-the-pairwise-cap.md`](2026-08-07-two-row-projection-is-the-pairwise-cap.md)'s
closed form

    y_{(2,1)} / y_{(3)}  =  q [2]_q [N−1]_q / [N+2]_q

which is an identity in the two free symbols. No anchor, no pin, no
floating-point evaluation, and no dependence on the Markov parameter `z` enters.
It is convention-independent in the sense that matters here.

### But the last step was a sample, and now is not

**Correcting this file's own first draft.** It reported route 3 as resting on
"exact symbolic" work full stop. The *formula* is symbolic; the **inference** was
not. The source concludes non-proportionality because the ratio *"differs at
every `q` tested"* — a finite sample. An audit whose whole point is provenance
should not let that pass, so it is proved instead.

At `N = 2` the ratio is `q [2]_q [1]_q / [4]_q`, at `N = 3` it is
`q [2]_q [2]_q / [5]_q`. Cancelling the common nonzero `q [2]_q`, they agree iff
`[1]_q [5]_q = [2]_q [4]_q`. And there is an exact identity:

    [2]_q [4]_q  −  [1]_q [5]_q  =  [3]_q

so the discrepancy is not merely nonzero on a sample — it **is** `[3]_q`.

| declaration | statement |
|---|---|
| `QOU.Eightfold.OcneanuTwoThreeNotProportional.qb_shift_identity` | `[n+1]_q[n+3]_q − [n]_q[n+4]_q = [3]_q` for **every** `n` |
| `…​.qb_two_four_sub_one_five` | `[2]_q[4]_q − [1]_q[5]_q = [3]_q` (the `n = 1` case) |
| `…​.ratio_eq_iff_qb_three_eq_zero` | the two ratios are equal **iff** `[3]_q = 0` |
| `QOU.Archimedean.OcneanuTwoThreeSubstrate.qb_pos` | every `[m]_q` is positive at `q > 1` |
| `…​.ocneanu_ratio_N2_ne_N3` | at real `q > 1` the `N=2` and `N=3` ratios differ |
| `…​.ocneanu_ratio_adjacent_ne` | **and so do the ratios at `N` and `N+1`, for every `N`** |

### The exclusion is stronger than it was recorded

Proving it generalised it. The right-hand side of `qb_shift_identity` **does not
depend on `n`**: the cross-product discrepancy between the weight ratios at `N`
and `N+1` is `[3]_q` at *every* `N`, not just at `N = 2`.

So the recorded reason — *"the `N=2` and `N=3` traces are not proportional"* — is
the first case of a fact that holds all the way up. No re-tuning to an adjacent
`N` reproduces the weighting, and each one misses by the same amount. The row
could be restated at that width; it is left as-is here because widening an
exclusion is a change to the prune, not an audit finding, and belongs in the
cheat sheet with the author's eyes on it.

Stated as an `iff` on purpose: it says exactly what would have to hold for the
traces to be proportional, rather than asserting they are not. The archimedean
file rules it out via `[3]_q = q² + 1 + q⁻² > 0`.

Two things worth noting. `sub_inv_ne_zero` records that the `q`-brackets are
well-defined **exactly** on `q² ≠ 1` — by
`HeckeBraidingNonSymmetric.double_braiding_eq_one_iff`, exactly the
non-symmetric locus, so the two Lean strands on this branch meet. And the scope
is unchanged: the ratio formula itself is consumed from the source audit and not
re-derived here, so this strengthens the exclusion's *stated reason* from sampled
to proved and claims nothing further about `N = 3`.

Verified `lean`-direct, exit 0 on both files against the real Mathlib import
cone, zero `sorry`, `#print axioms` giving only `propext`, `Classical.choice`,
`Quot.sound`.

## Route 1 — the failure mode was real, and was already caught

Worth recording because it is the exact shape the owner asked about, and the
corpus caught it without prompting. The original argument for route 1 came from
`computations/state_space_natural_three_sym2_gate.py` and reasoned: *every
`SU(2)` representation is self-dual, therefore no summand of any `V^⊗n` passes
the gate.* **That inference is invalid** — self-duality splits by the
Frobenius–Schur indicator, and even-dimensional (symplectic) summands *do* pass.

The correction landed 2026-08-07 and is formalised: `Sym2GateParity.lean` proves
`gate_fails_iff_odd_dim`, and `self_duality_does_not_decide_gate` records the
counterexample pair **specifically so the invalid inference cannot be re-derived
from the file**. The physics conclusion survives on the corrected criterion —
colour needs `dim W = 3`, which is odd — but it now rests on parity rather than
on self-duality.

Two scope notes so this row is not read wider than it is. The exclusion is about
summands of tensor powers of the **2-dimensional fibre**; it says nothing about
a genuinely non-isomorphic fibre, which is why it *forces* the surviving
question rather than closing it. And the representation theory that makes
`Sym²(𝟑) = 𝟔` irreducible is a declared **Mathlib gap** (`qou-8fl1`), honestly
flagged in `Sym2Gate.lean`'s own docstring — the exclusion does not depend on it.

## Route 5 — true, and checkable in two lines

The claim is uncited and appears in exactly one place in `docs/`, which is a
defect. The content, however, is elementary and now verified:

| quantity | value |
|---|---:|
| `dim Λ⁴(ℝ⁸) = C(8,4)` | 70 |
| `dim GL(8,ℝ)` | 64 |
| `dim Spin(7)` | 21 |
| Cayley orbit `= 64 − 21` | 43 |
| codim `= 70 − 43` | **27** |

`64 < 70` forbids an open `GL(8,ℝ)`-orbit on `Λ⁴(ℝ⁸)` outright, on dimension
grounds alone — the stronger orbit-structure fact is not even needed. Both
numbers in the table row are right. Add the citation; do not re-open the route.

## Route 6 — the pointer, not the claim, is the problem

`S₄`/Fano is excluded on a "marked-pair obstruction", and that phrase resolves
to an unrelated τ-coherence construction elsewhere in `docs/audits/`. The
cheat-sheet gloss (*`S₄` has no orbit of size ≤ 2 on `ℙ²`; the `S₄`-invariant
quartics form an infinite pencil*) is a different and more specific statement
than the audit's. **Neither is refuted here** — this is a citation defect, and
the route should stay excluded pending someone re-deriving the pencil claim.
Do not treat this row as re-opened.

## Route 7 — a scope note, not a downgrade

"Supplies `SU(2)`, already spent on electroweak" is a *wrong-object* argument,
not an impossibility proof. Under AGENTS.md §"Before declaring refuted", it is
a scope-(a) negative wearing scope-(b) phrasing: it says the construction does
not yield the object wanted, which is correct, rather than that no such
construction can. The row is fine; its **tier label** is a shade strong.

## What this does and does not license

- **Does not re-open any route.** Six stand outright; the two with citation
  defects have defective *pointers*, not defective *reasoning*.
- **Does license spending the `N = 3` effort on the surviving direction** — the
  non-neutral Tannakian gerbe (`qou-y7vg` / `qou-8p1i`) — rather than on
  re-auditing the prune. That was the actionable question.
- **Records the negative.** Someone will ask this again. The answer is that the
  prune was checked at provenance level on 2026-08-25 and held.
- **One row got stronger under the check**, which is the useful kind of outcome:
  route 3's non-proportionality moved from a finite sample to a machine-checked
  identity. The worry did not find a rotten row, but asking it improved one.

## Adjacent finding — the literature is absent

Separately measured this session (bean `qou-tzfm`): the surviving direction has
**no corpus support to read**. Across `library/`'s 400 ingested documents,
`INDEX.md` returns **one** Tannakian hit (a dissertation on Tannakian categories
of perverse sheaves on abelian varieties) and **zero** on gerbes, non-neutral
Tannakian categories, or inequivalent fibre functors. An agent attacking §4-A
today is deriving against an empty shelf.
