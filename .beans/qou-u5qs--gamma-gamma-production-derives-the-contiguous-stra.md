---
# qou-u5qs
title: gamma-gamma production DERIVES the contiguous strand layout, uniquely — and that is why there is no 3-cell
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T19:44:28Z
updated_at: 2026-09-14T19:59:39Z
---

## 2026-09-14 — the measurement (probe 15/15, exact combinatorics, read-only)

`computations/onedim/gamma_gamma_forces_the_layout_probe.py`.

**The question.** `qou-9ven`'s follow-on probe measured that the contiguous
layout `nucleon k -> strands (3k, 3k+1, 3k+2)` is corpus-uniform (61 refs / 41
files) and found nowhere DOWNSTREAM a non-contiguous one could come from.
`NoThreeCellOnTheChain.lean` proves a linear layout has no triangle, hence no
3-cell -- but takes `LinearLayout` as a HYPOTHESIS. So: what forces it?
Owner ruling `qou-ales` says selection is gamma-gamma + confinement SDP,
never census -- so the answer had to come from there.

**The hypothesis, stated before the run.** `GammaGammaWordSelection.lean`
defines `vertex i = [sigma_i, sigma_{i+1}^{-1}]` -- ADJACENT Artin generators.
`sigma_j` exchanges strands `j, j+1`, so the vertex touches exactly
`{i, i+1, i+2}`. A nucleon's internal word `beta_Bor = vertex(0)^3` is
internal iff the strands it touches lie in that nucleon's own block.

**Measured, exhaustively over every 3-uniform partition of the 3A strands:**

| A | partitions | all-interval | gg-internal everywhere | carrying a triangle |
|---|---|---|---|---|
| 2 | 10 | 1 | 1 | 0 |
| 3 | 280 | 1 | 1 | **234** (83.6 %) |
| 4 | 15400 | 1 | 1 | **13969** (90.7 %) |

1. A 3-block admits an internal gamma-gamma vertex **iff** it is an interval
   (324 subsets over n = 6, 9, 12; 0 mismatches; decided by brute force over
   generator indices, not by the interval test, so it is not self-checking).
2. The all-interval partition is **UNIQUE** at every A, and it IS the
   contiguous layout. So the layout is not merely constrained -- it is
   DETERMINED.
3. Its block quotient is the path `P_A` -- which supplies the `LinearLayout`
   hypothesis `NoThreeCellOnTheChain.lean` assumes.
4. No all-interval partition carries a triangle; 83.6 % / 90.7 % of the
   others do. **The exclusion has content.**
5. The interleaved "residue" layout `{k, k+A, k+2A}` -- the obvious
   non-linear candidate -- has block quotient the **cycle C_A**, a triangle at
   A = 3. It is excluded because NOT ONE of its blocks is an interval, so
   under the Artin-adjacent reading no nucleon of it can carry an internal
   gamma-gamma word at all.

**So the contiguous layout is DERIVED, and the missing 3-cell is downstream of
the gamma-gamma definition rather than of a convention.** That closes the
`qou-9ven` follow-on question in the direction opposite to the one being
looked for: there is no derivable non-linear layout, and the failure to find
one is the result.

**Scope (b)**, invariant named: a `sigma_j` crossing joins CONSECUTIVE strands
only, so a 3-strand set closed under a gamma-gamma vertex is an interval, and
length-3 intervals tile `[0, 3A)` uniquely.

**NOT excluded, and it is the one real decision here:** a BAND-generator
reading. `a_{ts} = (sigma_{t-1}...sigma_{s+1}) sigma_s (...)^{-1}` crosses two
non-adjacent strands with writhe 1, so a band vertex `a_{ts} a_{t's'}^{-1}`
has writhe 0 and passes `writhe_eq_zero` while NOT being a `GammaGammaWord`
under the corpus's inductive definition. Under a band reading the
non-contiguous layouts reopen. Which reading the physics means is
definitional; choosing the one that yields a 3-cell would be selection against
the target (AGENTS.md "NO FITTING"), so it is left open for the owner.

Next: formalize (1)-(3) in Lean so `NoThreeCellOnTheChain`'s hypothesis is
supplied rather than assumed.


## 2026-09-14 — TWO CORRECTIONS to the entry above, both against me

### 1. Corpus-grep: the arc is largely ALREADY CLOSED, and my framing overstates it

Six-path checklist run on "is the linear layout forced by the Coxeter type".
Verdict: **do not write it that way — the corpus explicitly refuses that
attribution.**

- `eightfold-intro.md:12-17` and `2026-08-07-l2-volume-binding-cluster.md:34`
  both record that `B_n` has Coxeter type `A_{n-1}` **by construction**, and
  say in terms: *"It is not a structural theorem about the substrate, and
  nothing is derived from it."*
- The path ⇒ no-triangle ⇒ no-3-cell chain is already PROVED sorry-free three
  times — `LinearLayoutNoBulk.lean` (`degree_le_two`,
  `not_linearLayout_of_degree_ge_three`, `adj_iff`),
  `NoThreeCellOnTheChain.lean`, `Hecke/LayoutConflict.lean`
  (`adjacent_pair_unique`) — and **none of them mentions Coxeter**. The
  braid-side half is `StrandLayoutForcesChain.no_single_generator_joins_nonadjacent`.
- **The sharp one.** `EnumeratorSelectionDegeneracy.lean:110-130` says the
  obstruction is **not** the layout but **the generator set**, that
  re-labelling strands is *"a conjugation, which the Markov trace cannot
  see"*, counts inter-nucleon band generators in `B_9` at **27 against the 2
  the enumerator searched**, and concludes: *"the band presentation **is** the
  right generating set."*
- **The corpus already BUILDS triangles with BKL bands.**
  `helium4_mu4_cluster_moment_probe.py`, `gap10_tjon_correlation_probe.py` and
  `a4_h12_brunnian_deficit_measure_probe.py` bond non-adjacent nucleons to get
  the complete graph at `A = 4` (6 bonds, 4 triangles). So "no triangle" is
  **false of the corpus's coordination graphs in general** — it is true only
  of the γγ / `atom_braid_word_3A` layout.
- Held literature: `library/arxiv-0802.1072v2` §2.1 (Birman–Menasco) — the
  band presentation of `B_3` uses a **cyclically ordered** generating set
  `<a1,a2,a3>`, i.e. the SAME group has a presentation whose adjacency graph
  is a triangle.

**So the correct scope is narrower than I wrote**, and the band reading is not
merely "an open definitional question": `EnumeratorSelectionDegeneracy` has
already concluded the band presentation is right. The γγ result stands exactly
as: *an **Artin-adjacent** γγ vertex forces the contiguous layout uniquely* —
and that now reads as a **tension** between two things on `main`, not as a
closure.

Nothing was found for: the Coxeter attribution itself (0 hits, all six paths,
including a whole-corpus co-occurrence scan); `Out(B_n)` / Dyer–Grossman;
affine `Ã_{n-1}` as a layout route; type-B/D folding as one. `corpus_search`
(path 0) was UNAVAILABLE this session — the `paper-assistant` MCP server
failed to connect — so the six greps are the whole surface actually searched.

### 2. My own second probe refuted its own headline claim on its first run

`single_letter_interface_forces_bond_product_probe.py` was written to claim
*single-letter interfaces ⟺ every block is an interval*. CHECK 4 returned **20
counterexamples**. Claim withdrawn; nothing downstream of it was written.

The counterexamples are the interesting object. Measured exhaustively:

| A | all-single-letter | of which all-interval | carrying a TRIANGLE |
|---|---|---|---|
| 3 | 3 | 1 | **2** |
| 4 | 19 | 1 | **16** |

The `A = 3` pair are the **wrap-around** partitions `{0,1,8} {2,3,4} {5,6,7}`
and `{0,7,8} {1,2,3} {4,5,6}` — one block straddling the two ends of the
strand line, quotient the cycle `C_3`. **So connected-sum multiplicativity is
compatible with a cyclic coordination graph and does not exclude the 3-cell.**
Only the γγ interval condition does. One route to the layout, not two.

**And closing the chain does not escape anyway** (new, CHECK 6): on a triangle
all three bonds are present and all are repulsive, so
`φᵀ₃ = u₁₂u₁₃ + u₁₂u₂₃ + u₁₃u₂₃ − u₁₂u₁₃u₂₃ > 0` (since `u₁₂u₁₃u₂₃ < u₁₂u₁₃`),
hence `b₃ < 0` still. That is the corpus's `b3corpus_neg` reached from the
LAYOUT rather than from the bond values — worth having, because the
wrap-around partition is the obvious next thing to try.

### What route (b) is left needing — normalisation-free

`b₃ > 0` iff `Z₁₂₃ < f₁₂ + f₂₃ − 1`, and the bond product overshoots that by
exactly `g₁₂g₂₃ = |b₃|`. So: a three-body correction to `Z₁₂₃`, negative, of
size ≥ **0.293278112721** (³H) / **0.190468485549** (³He). Equivalently an
aggregator convex through the origin — the corpus's own
`AggregatorConvexity.b3Agg_nonneg_of_convexOn`, bean `qou-82mc`.

The corpus holds one exact cross term of the right SIGN,
`z(z²−hz−1) = −0.4611715803` (proton) / `−0.4611715908` (muon), from
`MarkovTraceInterleavedCrossTerm`. Not claimed to be the correction: it lives
on three ADJACENT generators in `H₄` and the chain's bond generators are three
apart, so no reordering of the chain's bonds can produce it.

### Reported, not fixed (ask-first)

`MonotoneWordTraceFactorizes.lean`'s docstring asserts the production word is
monotone. `mass_at_3A_proper.py` records (measured 2026-09-07, bean
`qou-m6gp`) that the live alternating core is **not** monotone and that the
monotone ⇒ `#T(2,k)` argument no longer applies. Two files on `main` give
different groundings for the same identity; the identity survives on connected
sums, the Lean file's stated reason does not.
