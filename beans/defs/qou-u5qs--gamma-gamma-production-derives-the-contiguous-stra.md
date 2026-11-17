---
# qou-u5qs
title: gamma-gamma production DERIVES the contiguous strand layout, uniquely — and that is why there is no 3-cell
status: in-progress
pr: 8268
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T19:44:28Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
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


## 2026-09-14 — item C answered: the band reading does not DERIVE a layout, it removes the selector

Owner picked C (measure bands first) + B (re-read γγ on bands) + fix the
`MonotoneWord` docstring. C is done and it substantially collapses B.

`computations/onedim/band_gamma_gamma_vertex_admits_everything_probe.py`, 11/11.

**The band vertex, defined by keeping the Artin vertex's actual structure.**
`GammaGammaWordSelection.vertex`'s own docstring says the vertex is *"one photon
on strands `(i, i+1)` and one anti-photon on `(i+1, i+2)`"* — two crossings of
opposite sign **sharing exactly one strand**. Keep that, drop adjacency:

    band vertex = a_{ts} a_{t's'}^{-1}  with  |{s,t} ∩ {s',t'}| = 1

Verified a strict generalisation, not a different object:
`σᵢσᵢ₊₁⁻¹ = a_{i+1,i} a_{i+2,i+1}⁻¹` exactly (CHECK 3).

**Measured:**

| reading | A=2 | A=3 | A=4 |
|---|---|---|---|
| partitions | 10 | 280 | 15400 |
| **Artin admits** | **1** | **1** | **1** |
| **band admits** | **10** | **280** | **15400** |
| band, with a triangle | 0 | 234 | 13969 |

Every three strands `a < b < c` are the support of `a_{b,a} a_{c,b}⁻¹` (they
share `b`) — verified on all C(9,3)=84 and C(12,3)=220 triples. **So the band
reading imposes no layout constraint at all.**

Also verified: every band generator has **writhe 1** (conjugate of a single
crossing), so every band vertex has writhe **0** and **passes
`writhe_eq_zero`** — the corpus's writhe test structurally cannot separate the
two readings. And a non-adjacent band vertex is **not** a `GammaGammaWord`:
`a_{2,0}a_{3,2}⁻¹` expands to sign pattern `(+,+,−,−)`, violating the inductive
definition.

**What this does to the question.** The fork is not "does the framework have a
3-cell". It is **where the selection happens**:

- *Artin*: the γγ half of `qou-ales` picks the LAYOUT uniquely (contiguous),
  the confinement SDP then picks the WORD within it. No 3-cell.
- *Band*: the γγ half is **vacuous as a layout selector**. Every layout is
  admissible, 83.6 % / 90.7 % carry a triangle, and the whole burden falls on
  the confinement SDP alone (reading 3, Frobenius positivity, owner ruling
  2026-09-12).

Adopting the band reading *because* it yields a 3-cell would be selection
against the target — it yields one by yielding everything. **What would make it
a derivation is running the confinement SDP over the enlarged candidate set.**
`EnumeratorSelectionDegeneracy` counts **27** inter-nucleon band generators in
`B₉` against the **2** an enumerator has searched, so that space is real and
almost entirely unexplored. That is what B now means, and it is a compute task
rather than a definitional one.

Independently: a triangle does not by itself flip `b₃` — measured `b₃ < 0` on a
triangle whenever all three bonds are repulsive
(`single_letter_interface_forces_bond_product_probe.py` CHECK 6), and both
derived bond families are repulsive. So the band reading reopens the
**surface-holonomy** route to the extensive term, not the Mayer route.


## 2026-09-15 — pick B's H₃ leg closes as a negative; and three corrections

**B at H₃: the band reading selects exactly what Artin does.**
`computations/onedim/band_vertex_h3_frobenius_selector_probe.py`, 8/8, 60 dps,
proton pin, reusing the corpus's Hoefsmit reps and convention-D `y_λ`.

`H₃` has three BKL bands (`σ₀`, `σ₁`, `σ₁σ₀σ₁⁻¹`); every pair shares exactly one
strand, so **six** band γγ vertices against the **one** Artin admits. All six are
Frobenius-feasible at exactly `{3, 6, 9}`; minimal non-trivial power **3** for
every one — the same `β_Bor`. Artin cost: the Artin vertex's cube is strictly
cheapest (6 vs 12). Band cost: all six tie. Both reported; picking the cost that
gives the preferred answer would be selection against the target.

**The reason is measured, not asserted.** All six share ONE character vector
`(1.0, −1.04370620853, 1.0)` — one conjugacy class, and `χ_λ` is a class
function. `a₍₂,₀₎`'s character agrees with `σ₀`'s on every block below 1e-40.
Convention D kills the alternating block and `χ₍₃₎ = q^writhe = 1`, so `(2,1)`
alone decides. **Scope (a)** — one algebra, one pin. `H₆` untouched, and that is
where the two readings could still part company.

**CORRECTION 1 — `qou-82mc` is retired.** It is `completed` and carries its own
header *"🛑 TITLE IS NOW MISLEADING 2026-09-13 — convexity is SUFFICIENT but
STRICTLY UNNECESSARY"*, naming **`qou-2ss0`** (in-progress) as live carrier. My
2026-09-14 entry cited it as the live escape.

**CORRECTION 2 — "equivalently an aggregator convex through the origin" is WRONG
FOR A CHAIN, and that was mine.** `b3Agg Φ g := Φ(3g) − 3Φ(g)`
(`AggregatorConvexityDichotomy.lean:101`), whose own docstring says `3` is the
**three-body bond count** — the triangle. The production `A=3` word is a
**two-bond chain**, forced by `StrandLayoutForcesChain`. At chain counts the
quantity is `Φ(2g) − 3Φ(g)`, and convexity through the origin gives only
`Φ(2g) ≥ 2Φ(g)`, hence `≥ −Φ(g)`: **no sign at all.** And the route is circular
anyway — `sign_carries_no_information_beyond_the_secant` makes it an *iff*, so
exhibiting a convex `Φ` **is the assumption rewritten**.

**The live non-circular route is SCALING.** `b3Agg_of_scales`: `Φ(3g) = c·Φ(g)`
⟹ `b₃ = (c−3)·Φ(g)`, no curvature hypothesis; hence
`b3Agg_pos_iff_exponent_gt_one` — `b₃ > 0` ⟺ `p > 1` for a `p`-homogeneous law.
Derive `p` from a Hecke-side structural property; do not choose `Φ`. The
production `B = −α·log(…)` sits at `p < 1`.

**CORRECTION 3 — a sibling's report is not a primary source.** The corpus-grep
that surfaced all this quoted the interleaved cross term's convention-D closed
form as `−(q⁴+q²+1)/(q²+1)²`. Checked at source: that is `markovDefect_convD`,
the **defect** `z²−hz−1` = **−0.752702**. `crossTerm_neg_convD` carries the `z·`
prefix and is **−0.461172** — the figure already recorded here. Verified rather
than propagated.

**Confirmed and adopted from that grep:** there is **no derived convex aggregator
anywhere in the corpus**. Every derived assembly is concave (`multiplicative_W`,
`b₃ = −(f−1)²(f+2) ≤ 0`) or exactly affine (log free energy; bond-functional sum;
and the γγ-selected assembly, whose non-affineness its own author predicted and
then measured at `±1.6e-61`, the arithmetic floor).

**New open item:** `b3Agg` is stated at `m₃ = 3`; `UrsellChainMismatch.lean`
formalises the chain/triangle divergence — but neither it nor
`UniformBondSimpleGraphExclusion.lean` contains the string "aggregator". **The
two arcs have never been joined**, and joining them is a small, well-posed Lean
task.


## 2026-09-15 — B's H₆ leg closes too; the fork reduces to something smaller

`computations/onedim/band_vertex_h6_interface_selector_probe.py`, 11/11, 4.2 s.

`H₆` is where the inter-nucleon bond lives and where a band can join strands in
**different** nucleon blocks — the one place the two readings could part
company. Of 15 BKL bands, **nine** cross the interface (3×3) and exactly one is
an Artin generator, so eight join non-adjacent nucleon strands. Convention D
leaves only the four two-row blocks deciding; seven are silent.

Over all **120** band γγ vertices, **108 of them inter-block**:

- **1** distinct character vector `(1.0, 1.95629379147, −0.131118625598, −1.08741241707)`
- **1** distinct feasible set, `{3, 6, 9}`, for all 120
- minimal non-trivial survivor **3** for every one
- Artin cost picks `G³` (six letters); band cost ties all at 6

Anchored first: `a₍₃,₂₎a₍₄,₃₎⁻¹ = σ₂σ₃⁻¹` on every deciding block, deviation 0.

**Attacked rather than reported**: "all 120 agree" is the shape of a broken
construction. The 120 words are distinct and give **120 distinct matrices** on
block (4,2), so equal characters are conjugacy, not collapse.

### What the fork reduces to

Under **either** reading the SDP selects the same word — `β_Bor` inside a
nucleon, `G³` at the interface. They differ only on the layout, and in a way
that helps neither:

| reading | layout | word | 3-cell |
|---|---|---|---|
| Artin | forced contiguous, uniquely | `β_Bor`, `G³` | excluded |
| band | wholly unconstrained | `β_Bor`, `G³` (identical) | permitted, never selected |

**A non-contiguous layout is not derived under either reading.** Artin forbids
it; band permits it while selecting nothing. So the 3-cell is underivable from
γγ + SDP as the rule currently stands — and the reason is not the generating
set. It is that the γγ half constrains the layout either completely or not at
all, while the SDP half is blind to the layout, acting on the word whose
selected form is identical either way.

**Scope (a)** — two algebras (`H₃`, `H₆`), one pin, reading 3. Does not
structurally exclude the band reading at `A ≥ 3`. At `q = 1` the reason is
visible (a band is a transposition; `a·b⁻¹` is a 3-cycle; all 3-cycles are one
`S_n` class) but that is an observation about the classical limit, **not a
proof** — whether every band γγ vertex lies in one `B_n` class for all `n` is
open.

**Corrected in this probe, my arithmetic:** the first run asserted "exactly six
bands cross the interface". It is **nine** (|block 0| × |block 1| = 3×3). The
check now states the correct count and says where the wrong one came from.


## 2026-09-15 — WITHDRAWN: my own chain/triangle correction was wrong

The 2026-09-15 entry above says the convex-aggregator route *"does not even
apply"* to the production chain, because `b3Agg` is stated at `m₃ = 3` while the
chain has 2 bonds. **That is wrong and is withdrawn.**
`computations/onedim/b3_bond_count_and_the_scaling_criterion_probe.py`, 7/7.

**The `3` in `b3Agg Φ g = Φ(3g) − 3Φ(g)` is two different numbers.** The Ursell
inversion is `b₃ = B(3-cluster) − Σ over the C(3,2) = 3 PAIRS of B(pair)`. The
first `3` is the cluster's **bond count**; the second is the **pair count**,
which is 3 for *any* 3-cluster whatever its bond graph. On a chain the unbonded
pair contributes `Φ(0) = 0` — the through-the-origin condition already assumed —
so the chain form is `Φ(2g) − **2**Φ(g)`. The claim used the chain's bond count
with the triangle's pair count.

**Both consequences reverse:**

- **Convexity IS sufficient on the chain.** Jensen at `0` and `m` with weights
  `(1−1/m, 1/m)` gives `Φ(1) ≤ Φ(m)/m`, hence `b₃(m) ≥ 0` for every `m ≥ 1`. The
  chain is the `m = 2` case of the identical argument.
- **The scaling criterion is `p > 1` at every bond count.** `b₃(m) = C(mᵖ − m)`,
  so `b₃ > 0` ⟺ `mᵖ > m` ⟺ `p > 1`, and `m` cancels out.

**Validated by reproducing two independent corpus results from one formula.**
With `b₃(m) = Φ(m) − m·Φ(1)` and the multiplicative assembly `Φ(m) = 1 − fᵐ`:
`m = 3` → `−(f−1)²(f+2)` = `MayerThreeBodySign.b3_le_of_nonneg`; `m = 2` →
`−(f−1)²` = the corpus's chain `−g₁₂g₂₃` at equal bonds. Symbolic, deviation 0.

**How it got in, and the lesson.** The claim came from a corpus-grep that marked
it explicitly as *its own algebra, not the corpus's*, and asked for it to be
checked. I checked its two **corpus** claims — the bean's status and `b3Agg`'s
definition, both correct — and propagated its **algebra** unchecked, in the same
entry where I wrote *"a sibling's report is not a primary source"* about a
different claim of the same report. Checking the corpus half of a mixed report
is not checking the report.

**Net effect on `qou-2ss0`:** none. Its scaling target is unchanged, and the
"join the two arcs" Lean task filed above is **not needed for this purpose**.
What survives from that grep and remains useful: no derived convex aggregator
exists in the corpus, and `sign_carries_no_information_beyond_the_secant` makes
"find a convex Φ" circular — so scaling is still the non-circular route.


## 2026-09-15 — item 3 closed (R8), and my own commit message was stale

`computations/onedim/tl_open_chain_string_band_probe.py`, **24/24**, `mp.dps = 50`,
both pins. **Independently re-run by me on the blob at HEAD: 24 PASS, 0 FAIL,
exit 0.** Also confirmed: tree clean, HEAD blob byte-identical to the version
that was reported, and the two headline numbers reproduced from scratch at 40 dps
— `ξ = 1/ln Δ = 184.038545493` and `B(0) = 4(Δ−1)²/Δ = 0.0001180982535690475`,
the latter rounding to the periodic probe's independently-recorded `1.180983e-4`.

**Headline: the periodic band IS the TL chain's band; the periodic SPECTRUM is
not.**

- **The Hermiticity worry does not bite**, and the premise behind it was wrong:
  the boundary field `((q−q⁻¹)/2)(σᶻ₁−σᶻₙ)` is reflection-**odd**, not
  anti-Hermitian. Diagonal in `σᶻ` with real entries for real `q > 1`, so
  `H_TL^open` is real symmetric — `max|Hᵢⱼ − Hⱼᵢ| = 0` **identically**.
  Reflection *is* broken (`2(q−1/q) = 0.4181206`).
- **Right about the band.** At `q = 3` (`ξ = 1.96`) inverting the open levels
  through the periodic `E₂(k)` gives an evenly spaced ladder with one common
  `L_eff` — the whole band, not just its edge (10 levels clear the continuum at
  `N = 24`, spread 3.9 %). The `n = 3` band is there too.
- **Incomplete about the spectrum, twice.** (1) The boundary operators **add a
  state the ring lacks** — `E = 0`, degenerate with the vacuum, **above** the
  whole `n = 2` band, every magnon sector, the `U_q(sl₂)` vacuum descendant,
  localised at one end with ratio **exactly `1/q`** (dev `2.005e-50`), decay
  length `1/ln q` = 9.584 sites; not finite-size. (2) They **remove momentum** —
  only `k → 0` survives extremal search, and exponential `z^N` convergence
  becomes a power law.
- **Honest negative at the substrate, scope (a).** `ξ = 1/ln Δ` = **184 sites**;
  one level clearing the thermodynamic edge needs `N ≈ 291`. At `N ≤ 24` the
  string is not resolved at all, and the finite-`N` edge manufactures a positive
  (+0.104 above it, −0.067 below the thermodynamic one, at `N = 24`).
- **Edge-independent confirmation, and the reusable form:** a real composite has
  `L_eff = N − c`. At controls `L_eff − N` is stable (3.1 %); **at the pins the
  stable statistic is `L_eff/N ≈ 0.49→0.50`** (2.6 %) — a box that is a fixed
  *fraction* of the chain is not a box.
- **The trap to carry forward:** the pins show a **cleaner** `N⁻²` law than the
  controls (2.045–2.053 vs 2.32–2.60), **and the cleanliness is the artifact** —
  `L_eff ∝ N` gives exactly 2 by construction. A tidy power law is evidence
  *against* a formed string.
- **Band bottom unreachable at any `N`:** `E₂(π) = −4Δ` is strictly interior to
  the two-magnon spectrum (`−4Δ > −8Δ − 8` for every `Δ > 0`; 196 levels below it
  at `N = 24`). Momentum is what separated it on the ring.

**Re-scoped in place, not retracted:** `xxz_n_string_band_probe.py`'s own
bridging sentence said the boundary operators "do not change a bulk band … but
that step is an argument, not something this probe measured". The argument has
now been run; it is right about the band and incomplete about the spectrum. That
probe flagged its own gap correctly and its formula stands.

**And my own commit message is stale.** `577ad180f` checkpointed this file as
"IN PROGRESS, NOT VERIFIED". The blob at HEAD is byte-identical to the version
that passed 24/24 (`git diff HEAD` empty; CHECK 18/19 present at HEAD), so a
reader trusting that message would discount a passing probe. Corrected in the
follow-up commit rather than by rewriting pushed history.


## 2026-09-15 — R9: the scaling route measured; it is not a new escape

`computations/onedim/scaling_route_on_the_derived_assemblies_probe.py`, 8/8.

`b3Agg_of_scales` gives **`b₃ > 0` ⟺ `c > 3`** where `Φ(3g) = c·Φ(g)`, with no
convexity, differentiability or homogeneity hypothesis. **`p > 1` is the special
case `c = 3ᵖ`** and applies only to a `p`-homogeneous `Φ` — which matters here,
because the corpus's multiplicative assembly is **exponential** in bond count,
not a power, so the `p` framing does not apply to it and the `c` one does.

| derived assembly | `Φ(m)` | `c = Φ(3)/Φ(1)` | `b₃ > 0` iff |
|---|---|---|---|
| multiplicative `W = 1−Z` | `1 − fᵐ` | `1 + f + f²` | **`f > 1`** |
| log free energy | `m·φ` | **3 exactly** | never (`b₃ = 0`) |

`c > 3` for the multiplicative assembly factors as `(f+2)(f−1) > 0` ⟺ `f > 1` —
**the attractive-bond escape `qou-q8vl` already closes** for every derived bond
family. Cross-checked by recovering `MayerThreeBodySign.b3_le_of_nonneg`'s
`−(f−1)²(f+2)` from the `c`-form exactly.

**So the scaling route, on the assemblies the corpus derives, is the
attractive-bond question in different coordinates. Not a new escape.**

**Where a new one would have to come from, and the convergence that makes it
credible:** a different `Φ` means a non-multiplicative trace, i.e. a cross term
`X`. On the two-bond chain `b₃ = −(f−1)² − X`, so `b₃ > 0` ⟺ `X < −(f−1)²` —
**the same target derived independently from the Ursell side** (`Z₁₂₃` below the
additive value by at least `|b₃|`), since `(f−1)² = g² = |b₃|` at equal bonds.
Two routes, one target.

🛑 **NOT settled, and deliberately not claimed:** whether the corpus's one exact
cross term (`−0.4611715803`, proton pin) is large enough. It is a difference of
**traces**; `Z` is a **ratio**. No conversion is attempted here and the
comparison must not be made until one is. What *is* settled: it lives on
adjacent generators in `H₄` while the chain's interface generators sit at
`3k+2`, three apart and far-commuting, so no reordering of the chain's bonds
produces it.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-15 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.
