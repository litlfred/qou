# γγ production forces the strand layout — and the Artin-vs-band fork that decides the 3-cell

**Date** 2026-09-14 · **Branch** `claude/trusting-planck-wncjcc` · **Bean** `qou-u5qs`
· **Issue** [#7394](https://github.com/litlfred/qou/issues/7394) · **PR** [#7396](https://github.com/litlfred/qou/pull/7396)

Consolidates items 1 and 2 of the 1D-sector tranche. Two results, three corrections,
and one fork that is the owner's to settle.

---

## 0. Summary

| | claim | scope | carrier |
|---|---|---|---|
| **R1** | The **Artin-adjacent** γγ vertex forces the contiguous strand layout, **uniquely** | (b), invariant named | Lean 27 decls + probe 15/15 |
| **R2** | Connected-sum multiplicativity does **not** force it — the wrap-around cycle survives | measured | probe 11/11 |
| **R3** | Closing the chain into a triangle does **not** flip `b₃` | (b), Ursell identity | probe 11/11 |
| **R4** | The **band** reading admits **every** layout — it removes the selector, it does not derive one | measured | probe 11/11 |
| **R5** | At H₃ the band reading **changes nothing** the confinement SDP selects — all six band vertices are one conjugacy class | (a), one algebra one pin | probe 8/8 |
| **C1** | The corpus refuses the Coxeter framing; `EnumeratorSelectionDegeneracy` says **bands** are the right generating set | correction | corpus-grep |
| **C2** | My own "single-letter ⟺ interval" claim was **false** (20 counterexamples) | correction | own probe |
| **C3** | `MonotoneWordTraceFactorizes`'s docstring claim that the production word is monotone is **stale** | correction | `mass_at_3A_proper.py` |

---

## 1. What was asked

`qou-9ven`'s follow-on measured that the contiguous layout — nucleon `k` on strands
`(3k, 3k+1, 3k+2)` — is corpus-uniform: **61 contiguous references across 41 files**, with
`canonical_brane_tower_decomposition.py:124` returning the cut set literally as
`[3*k+2 for k in range(A-1)]`. It found nowhere *downstream* that a non-contiguous layout
could come from. Since `NoThreeCellOnTheChain.lean` proves a linear layout carries no
triangle — hence no 3-cell, hence no `∫γ` surface-holonomy candidate for the missing
extensive binding term — the open question was upstream: **what, if anything, forces the
layout?**

Owner ruling `qou-ales` (2026-09-08) puts selection at γγ production plus the confinement
SDP, never census. So that is where the answer had to come from.

## 2. R1 — the Artin-adjacent vertex forces it, uniquely

`QOU/Mass/GammaGammaWordSelection.lean:92` defines the pair-production vertex as

```lean
def vertex (i : ℕ) : Word := [⟨i, true⟩, ⟨i + 1, false⟩]
```

— `σᵢ σᵢ₊₁⁻¹`, **adjacent** Artin generators, with its own docstring naming the strands:
*"one photon on strands `(i, i+1)` and one anti-photon on `(i+1, i+2)`"*. Since `σⱼ`
exchanges strands `j` and `j+1`, the vertex touches exactly `{i, i+1, i+2}`.

A nucleon's internal word is `β_Bor = (σ₀σ₁⁻¹)³`, three such vertices, and it is *internal*
exactly when every strand it touches lies in that nucleon's own block. **That single demand
determines the layout.**

Measured exhaustively over every partition of the `3A` strands into `A` unordered blocks of
three — [`gamma_gamma_forces_the_layout_probe.py`](../../computations/onedim/gamma_gamma_forces_the_layout_probe.py), 15/15:

| A | partitions | all-interval | γγ-internal everywhere | carrying a triangle |
|---|---|---|---|---|
| 2 | 10 | 1 | 1 | 0 |
| 3 | 280 | **1** | **1** | **234** (83.6 %) |
| 4 | 15400 | **1** | **1** | **13969** (90.7 %) |

- A 3-strand block admits an internal γγ vertex **iff** it is an interval — 324 subsets over
  `n = 6, 9, 12`, **0 mismatches**, decided by brute force over generator indices rather
  than by the interval test, so the check is not self-certifying.
- The all-interval partition is **unique** at every `A` and **is** the contiguous layout.
- Its block quotient is the path `P_A`.
- The interleaved "residue" layout `{k, k+A, k+2A}` has quotient the **cycle `C_A`**, a
  triangle at `A = 3`, and is excluded because **not one** of its blocks is an interval.

**Scope (b)**, invariant: a `σⱼ` crossing joins only *consecutive* strands, so a three-strand
set closed under an Artin-adjacent γγ vertex is an interval, and length-3 intervals tile
`[0, 3A)` uniquely.

### Formalisation

[`QOU/OneDim/GammaGammaForcesTheLayout.lean`](../../content/quantum-observable-universe/lean/QOU/OneDim/GammaGammaForcesTheLayout.lean)
— 27 declarations, `lean -DautoImplicit=false -s 65536` **exit 0**, zero warnings,
`#print axioms` on all 27 showing **no `sorryAx`** (`propext` / `Quot.sound` /
`Classical.choice` only).

`eq_triple_of_internal` is the crux: a card-3 block containing a vertex's three-element
support *equals* it. `bonded_iff_base_succ`: two disjoint triples bond iff their bases
differ by exactly 3. `no_triangle_of_triples` follows by `omega`.

**Vacuity was attacked, not assumed.** The two `False`-concluding theorems were **drop-one**
tested: for each of the six hypotheses of `no_triangle_of_triples`, a witness satisfying the
other five and refuting that one compiles — so no proper subset is already contradictory.
The obvious mutant test (deriving `0 = 1`) compiles for *every* true `False`-concluding
theorem and cannot discriminate; drop-one is the test that can. `degree_le_two`'s bound is
tight: two neighbours achievable, three not. And `residue_layout_bonded_pairwise` +
`residue_block_not_internal` are closed statements proving the excluded option space is
**non-empty** — the interleaved layout really is a triangle and really is γγ-excluded.

**Two things the file does not carry, flagged in its own docstring rather than hidden:**
it does **not** discharge `NoThreeCellOnTheChain`'s `LinearLayout` hypothesis (that
predicate is about `SimpleGraph (Fin n)`, this file is about `Finset ℕ`, and there is no
bridge lemma — it is an *independent* route to the same conclusion); and `vertexStrands` is
a hand-transcription of `GammaGammaWordSelection.vertex`, correct but checked by reading
rather than by the compiler.

## 3. C1 — the correction: the corpus refuses the Coxeter framing, and leans to bands

The first write-up of R1 said *"there is no derivable non-linear layout"*. **Too strong.**
A six-path corpus-grep found:

- `eightfold-intro.md:12-17` and `docs/coordination/2026-08-07-l2-volume-binding-cluster.md:34`
  both record that `B_n` has Coxeter type `A_{n-1}` **by construction**, in terms:
  *"It is not a structural theorem about the substrate, and **nothing is derived from it**."*
  So the Coxeter type is **not** the invariant, and naming it as one would overstate R1.
- The path ⇒ no-triangle ⇒ no-3-cell chain is already proved sorry-free **three times** —
  `LinearLayoutNoBulk.lean` (`degree_le_two`, `not_linearLayout_of_degree_ge_three`,
  `adj_iff`), `NoThreeCellOnTheChain.lean`, `Hecke/LayoutConflict.lean`
  (`adjacent_pair_unique`) — none of them via Coxeter. The braid-side half is
  `StrandLayoutForcesChain.no_single_generator_joins_nonadjacent`.
- **`EnumeratorSelectionDegeneracy.lean:110-130`** says the obstruction is *"**not** the
  strand layout … It is the **generator set**"*; that relabelling strands is *"a
  conjugation, which the Markov trace cannot see"*; counts inter-nucleon band generators in
  `B₉` at **27 against the 2** an enumerator searched; and concludes **"the band
  presentation *is* the right generating set."**
- **The corpus already builds triangles with BKL bands.**
  `helium4_mu4_cluster_moment_probe.py`, `gap10_tjon_correlation_probe.py` and
  `a4_h12_brunnian_deficit_measure_probe.py` bond *non-adjacent* nucleons to get the
  complete graph at `A = 4` — 6 bonds, **4 triangles**.
- Held literature: `library/arxiv-0802.1072v2` §2.1 (Birman–Menasco) — the band presentation
  of `B₃` uses a **cyclically ordered** generating set `⟨a₁,a₂,a₃⟩`, i.e. the *same group*
  has a presentation whose adjacency graph is a triangle.

**So "no triangle" is a property of the γγ / `atom_braid_word_3A` layout, not of the
framework.** R1 stands exactly as stated — an *Artin-adjacent* vertex forces the contiguous
layout — and now reads as a **tension between two things on `main`**, which is more useful
than the closure first claimed.

*Method note:* `corpus_search` (path 0) was **unavailable** — the `paper-assistant` MCP
server failed to connect. The six greps are the whole surface actually searched.

## 4. Item 1 — what the bond-product family rests on

### C3 — the grounding changed and one docstring did not follow

`UrsellPartitionFunctionB3.lean` grounds `Z_S = ∏_e f_e` in
`MonotoneWordFactorizes.tr_stabWord_eq_prod_tr`. But `mass_at_3A_proper.py` records
(measured 2026-09-07, bean `qou-m6gp`):

> The 2026-09-05 alternating core `(σ₀σ₁⁻¹)³` is **NOT monotone**, so the monotone ⇒
> `#T(2,k)` ⇒ `Vol = 0` argument no longer applies. … What survives unchanged is the
> **connected-sum structure: each interface is a single letter**, so every atom branch
> closure is the connected sum of its `A` nucleon pieces (800/800 branches over
> ²H/³H/³He/⁴He decompose into exactly `A` summands).

`MonotoneWordTraceFactorizes.lean`'s docstring still asserted the production word is
monotone. Corrected in place: the **identity survives** (the Markov trace is blind to letter
order *inside* a summand, so `tr_M(W_atom)/tr_M(W_free)` is identical under both
intra-orderings to `~1e-60` at `A = 2, 3, 4`) but the **stated reason does not**. That
file's theorems are untouched — they are about an arbitrary `stabWord` and prove exactly
what they say. Only the claim that the *production* word is one of them was stale.

### R2 / C2 — single-letter interfaces do NOT force the path

[`single_letter_interface_forces_bond_product_probe.py`](../../computations/onedim/single_letter_interface_forces_bond_product_probe.py)
was written to claim *single-letter interfaces ⟺ every block is an interval*. **Its own
CHECK 4 refuted it on the first run: 20 counterexamples.** Claim withdrawn; nothing
downstream of it was written.

The counterexamples are the content:

| A | all-single-letter | of which all-interval | **carrying a triangle** |
|---|---|---|---|
| 3 | 3 | 1 | **2** |
| 4 | 19 | 1 | **16** |

The `A = 3` pair are the **wrap-around** partitions `{0,1,8} {2,3,4} {5,6,7}` and
`{0,7,8} {1,2,3} {4,5,6}` — one block straddling the two ends of the strand line, quotient
the cycle `C₃`, every interface still a single letter.

**So connected-sum multiplicativity is compatible with a cyclic coordination graph and does
not exclude the 3-cell.** Only the γγ interval condition does. **One route to the layout,
not two.**

### R3 — closing the chain does not flip `b₃`

The wrap-around cycle is the obvious next thing to try after R2. It does not work, and the
reason is one line of the Ursell identity. On a triangle all three bonds are present, so
`g₁₃ ≠ 0` and

```
φᵀ₃ = g₁₂g₁₃ + g₁₂g₂₃ + g₁₃g₂₃ + g₁₂g₁₃g₂₃
```

With every bond repulsive (`f = μ ∈ (0,1)`, `g = −u`, `u ∈ (0,1)`) that is
`u₁₂u₁₃ + u₁₂u₂₃ + u₁₃u₂₃ − u₁₂u₁₃u₂₃ > 0`, since `u₁₂u₁₃u₂₃ < u₁₂u₁₃`. Hence **`b₃ < 0`
on the cycle too.** Scope (b), invariant = the Ursell identity plus `f ∈ (0,1)`.

This is the corpus's `b3corpus_neg` reached from the **layout** rather than from the bond
values, and it matters because it separates the two routes: **the 3-cell reopens the
surface-holonomy route to the extensive term, not the Mayer route.**

### The target, normalisation-free

`b₃ > 0` iff `Z₁₂₃ < f₁₂ + f₂₃ − 1` (the additive value), and the bond product
`Z₁₂₃ = f₁₂f₂₃` **overshoots** that by exactly `g₁₂g₂₃ = |b₃|`. So route (b) needs a
three-body correction to `Z₁₂₃` that is **negative and at least**

- **0.293278112721** (³H)
- **0.190468485549** (³He)

*(cited from `UrsellPartitionFunctionB3` / bean `qou-rwhv`; not recomputed here)*

— same units as `Z`, no normalisation ambiguity.

> **🛑 CORRECTED 2026-09-15. This paragraph first continued *"equivalently, an aggregator
> convex through the origin, `b3Agg_nonneg_of_convexOn`, bean `qou-82mc`"*. Both halves are
> wrong.**
>
> **The bean is retired.** `qou-82mc` is **`completed`** and carries its own header —
> *"🛑 TITLE IS NOW MISLEADING 2026-09-13 — convexity is SUFFICIENT but STRICTLY
> UNNECESSARY"* — naming **`qou-2ss0`** (in-progress) as the live carrier.
>
> **And the equivalence does not hold for a chain.** `b3Agg Φ g := Φ(3g) − 3Φ(g)`
> (`AggregatorConvexityDichotomy.lean:101`), whose own docstring says `g` is the common bond
> weight and **`3` the three-body bond count** — i.e. the statement is at the **triangle's**
> `m₃ = 3`. The production `A = 3` word is a **two-bond chain**, and that is forced
> (`QOU.Mass.StrandLayoutForcesChain`). At chain counts the quantity is `Φ(2g) − 3Φ(g)`, and
> convexity-through-the-origin yields only `Φ(2g) ≥ 2Φ(g)`, hence `≥ −Φ(g)` — **no sign at
> all.** So the convex-aggregator route does not even apply to the object in question
> without first closing the chain.
>
> **The route is circular anyway, and that is a theorem.**
> `B3AggSecantCharacterisation.sign_carries_no_information_beyond_the_secant`: for `g > 0`,
> `0 ≤ b3Agg Φ g` **iff** `Φ(g)/g ≤ Φ(3g)/(3g)`. Because it is an *iff*, exhibiting a `Φ`
> with `b₃ > 0` **is the assumption rewritten** — selection against the target under
> §"NO FITTING". "Find a convex `Φ`" is not a closable task.
>
> **The live non-circular reformulation is the SCALING route.** `b3Agg_of_scales`: if
> `Φ(3g) = c·Φ(g)` then `b₃ = (c−3)·Φ(g)`, with no convexity or differentiability
> hypothesis; hence `b3Agg_pos_iff_exponent_gt_one` — for a `p`-homogeneous law,
> **`b₃ > 0` ⟺ `p > 1`**. A homogeneity degree is fixed by how the assembly responds to
> rescaling the bond weight, not chosen to fix a sign, so it can in principle be settled
> without reference to the measured `b₃`. The open question becomes: **is the framework's
> assembly law superlinear in the bond count, and why?** The production `B = −α·log(…)` sits
> at `p < 1`.
>
> Surfaced by a corpus-grep this session, then verified at source rather than taken on
> trust. Two of that grep's own claims did not survive the check: it reported *no derived
> convex aggregator anywhere in the corpus* (confirmed — every derived assembly is concave
> or exactly affine), but it also quoted the interleaved cross term's convention-D closed
> form as `−(q⁴+q²+1)/(q²+1)²`. That is `markovDefect_convD`, the **defect** `z²−hz−1`
> (−0.752702); the **cross term** `crossTerm_neg_convD` carries the `z·` prefix and is
> −0.461172, which is the figure in the table above.

The corpus holds **one** exact cross term of the right **sign**:
`MarkovTraceInterleavedCrossTerm` gives `z(z² − hz − 1)` between the interleaved
`g₀g₁g₀g₂g₁` and the sequential `g₀²g₁²g₂` —

| pin | `z_D` | `h²` | `z(z²−hz−1)` |
|---|---|---|---|
| proton | 0.6126880371464653 | 0.04370620853252199 | **−0.4611715803243431** |
| muon | 0.6126880506382724 | 0.04370621829759422 | **−0.4611715908455492** |

**Not claimed to be the correction.** It lives on three *adjacent* generators in `H₄`, while
the chain's bond generators sit at `3k+2` and are **three apart**, so they far-commute and
no reordering of the chain's bonds can produce it. It is evidence the family can be left at
all, and it says where: adjacent, non-commuting interfaces.

## 5. R4 — the band reading admits everything

Owner picked **C** (measure bands before wiring). Done —
[`band_gamma_gamma_vertex_admits_everything_probe.py`](../../computations/onedim/band_gamma_gamma_vertex_admits_everything_probe.py), 11/11.

The band vertex is defined by keeping the Artin vertex's actual structure — two crossings of
opposite sign **sharing exactly one strand** — and dropping only adjacency:

```
band vertex = a_{ts} a_{t's'}⁻¹    with  |{s,t} ∩ {s',t'}| = 1
```

where `a_{ts} = (σ_{t−1}⋯σ_{s+1}) σ_s (σ_{s+1}⁻¹⋯σ_{t−1}⁻¹)`. Verified a strict
generalisation, not a different object: `σᵢσᵢ₊₁⁻¹ = a_{i+1,i} a_{i+2,i+1}⁻¹` **exactly**.

| | A=2 | A=3 | A=4 |
|---|---|---|---|
| partitions | 10 | 280 | 15400 |
| **Artin admits** | **1** | **1** | **1** |
| **band admits** | **10** | **280** | **15400** |
| band, with a triangle | 0 | 234 | 13969 |

Every three strands `a < b < c` are the support of `a_{b,a} a_{c,b}⁻¹` (they share `b`) —
verified on all `C(9,3)=84` and `C(12,3)=220` triples. **The band reading imposes no layout
constraint at all.**

Also measured: every band generator has **writhe 1** (a conjugate of a single crossing), so
every band vertex has writhe **0** and **passes `writhe_eq_zero`** — the corpus's writhe test
structurally cannot separate the two readings. And a non-adjacent band vertex is **not** a
`GammaGammaWord`: `a_{2,0}a_{3,2}⁻¹` expands to sign pattern `(+,+,−,−)`, violating the
inductive definition.

## 5b. R5 — and at H₃ the band reading selects exactly what Artin does

Owner picked **B** as well as C. Its H₃ leg is done —
[`band_vertex_h3_frobenius_selector_probe.py`](../../computations/onedim/band_vertex_h3_frobenius_selector_probe.py), 8/8,
60 dps, proton pin. This is step 3 of `qou-ales` redone on the enlarged set.

`H₃` has exactly three BKL bands — `a₍₁,₀₎ = σ₀`, `a₍₂,₁₎ = σ₁`,
`a₍₂,₀₎ = σ₁σ₀σ₁⁻¹` — and every pair shares exactly one strand, so all six ordered pairs
give a band γγ vertex, against the **one** the Artin reading admits.

Under the owner's 2026-09-12 ruling the SDP means **reading 3**, Frobenius positivity. Under
convention D the two-row truncation gives `y₍₁³₎ = 0`, and `χ₍₃₎ = q^writhe = 1` on any
vertex power, so **`(2,1)` alone decides** — the enlarged candidate set does not enlarge the
set of deciding blocks.

| | feasible `k` (1…10), reading 3 | minimal non-trivial | Artin cost | band cost |
|---|---|---|---|---|
| `a₍₁,₀₎a₍₂,₁₎⁻¹` (**the Artin vertex**) | **{3, 6, 9}** | 3 | **6** | 6 |
| the other five band vertices | **{3, 6, 9}** each | 3 | 12 | 6 |

`χ₍₂,₁₎` for the Artin vertex, `k = 1…10`: `−1.0437062, −0.91067735, 1.9941858, −1.1706668,
−0.77235364, 1.9767771, −1.2908208, −0.62953933, 1.9478749, −1.4034698` — the sign pattern
`− − + − − + − − + −` of `qou-ales` step 7, reproduced.

**And the reason is measured, not asserted.** All six vertices share **one** character vector
`(1.0, −1.04370620853, 1.0)` across the three blocks — characters separate classes here, so
the six are **one conjugacy class**, and `χ_λ` is a class function. (`a₍₂,₀₎` is itself a
conjugate of `σ₀`: its character agrees with `σ₀`'s on every block to below `1e-40`.)

**Cost is a choice, so both are reported.** A band is a conjugate of one crossing, so it has
Artin length 3 but band length 1. Under Artin cost the Artin vertex's own cube is strictly
cheapest (6 against 12); under band cost all six tie. Picking the cost function that gives
the preferred answer would be selection against the target.

**Scope (a)** — one algebra, one pin. It does **not** settle `H₆`, where the interface bond
lives and where a band could join non-adjacent nucleon blocks. That is where the two readings
could still part company, and it is the next step of B.

## 6. The fork, stated properly

It is **not** "does the framework have a 3-cell". It is **where the selection happens**:

| reading | γγ half of `qou-ales` picks | SDP then picks | 3-cell |
|---|---|---|---|
| **Artin** | the **layout**, uniquely (contiguous) | the word within it | no |
| **band** | **nothing** — vacuous as a layout selector | *everything*: layout and word | 83.6 % / 90.7 % of admitted layouts carry one |

**Adopting the band reading because it yields a 3-cell would be selection against the
target** (AGENTS.md §"NO FITTING"): it yields one by yielding everything. What would make it
a *derivation* is running the confinement SDP — reading 3, Frobenius positivity, per the
owner ruling of 2026-09-12 — over the enlarged candidate set, and reporting what survives
without reading AME. `EnumeratorSelectionDegeneracy` counts **27** inter-nucleon band
generators in `B₉` against the **2** an enumerator has searched, so that space is real and
almost entirely unexplored.

## 7. Open

1. **Run the confinement SDP over the band candidate set** (owner's pick B, now a compute
   task rather than a definitional one). Steps 3–7 of `qou-ales` all assume `(σ₀σ₁⁻¹)^k`, so
   `β_Bor` selection, the `G³` pp bond and the −4.47 keV diproton would all need
   re-deriving under bands and could move.
2. **Bridge lemma**, if the stronger sentence is wanted: produce `LinearLayout G` for the
   contiguous block graph, connecting `GammaGammaForcesTheLayout` to
   `NoThreeCellOnTheChain` in Lean rather than in prose.
3. **Formalise `vertexStrands`** as a theorem about `GammaGammaWordSelection.vertex` — give
   `Word` a strand-support function and prove `support (vertex i) = vertexStrands i`.
4. **The aggregator route** — reframed, see the correction in §4. `qou-82mc` is retired;
   the live carrier is **`qou-2ss0`**. Measured this session: there is **no derived convex
   aggregator anywhere in the corpus** — every derived assembly is concave (`multiplicative_W`,
   `b₃ = −(f−1)²(f+2) ≤ 0`) or exactly affine (the log free energy, the bond-functional sum,
   and the γγ-selected assembly, whose non-affineness its own author predicted and then
   measured as `±1.6e-61`, the arithmetic floor). The live task is the **scaling** question:
   derive the assembly law's homogeneity degree `p` from a Hecke-side structural property and
   read the sign off `p > 1`, rather than choosing a `Φ`.
5. **The chain-vs-triangle bond-count mismatch.** `b3Agg` is stated at `m₃ = 3`; the
   production word is a two-bond chain. `QOU/Mass/UrsellChainMismatch.lean` formalises that
   divergence, but neither it nor `UniformBondSimpleGraphExclusion.lean` contains the string
   "aggregator" — **the two arcs have never been joined**, and joining them is a small,
   well-posed Lean task.
6. **The periodic-vs-open band gap**: the XXZ n-string band was measured on the *periodic*
   chain while `tl_is_the_xxz_chain_probe` identifies TL with the *open* chain plus a
   boundary field `((q−q⁻¹)/2)(σᶻ₁ − σᶻₙ)`. Under investigation.
