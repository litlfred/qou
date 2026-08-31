# Typed bond scalars, and a corrected map of what the extensive-term prunes actually cover

**Date:** 2026-08-30
**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/TypedBondSiteInvariance.lean` (sorry-free, axioms clean)
**Beans:** `qou-edt7` (the negative half this extends), `qou-brng` (the amplitude question it narrows onto)
**PR:** #6229

This audit records two things: a new sorry-free classification, and a
correction to the map of what the extensive-term prune family covers. The
second matters as much as the first, because the map I was handed named four
results and the tree holds at least nine.

## 1. The result

Let a nucleus be a graph `G` on `A` sites with isospin-typed bond scalars
`L_pp`, `L_pn`, `L_nn`, and let `S` be the set of proton sites. Write the
doubled bond sum

```
2·B(S) = Σ_{u,v} [u ∼ v] · L_{type(u),type(v)}
```

(doubled so no division is needed and the base ring stays a generic
`CommRing`, per AGENTS.md §7c).

**Site invariance** is the physical requirement: a nucleus has no
arrangement, so `B` may depend only on *how many* protons there are, not on
*which* sites carry them.

> **Theorem (classification).** For `G` on `A ≥ 3` sites carrying both a bond
> and a non-bond between distinct sites, site invariance holds **iff** `G` is
> regular **and** `L_pp + L_nn = 2·L_pn`.
>
> **Corollary (collapse).** Under those conditions,
> `2·B(S) = k·(L_pp·Z + L_nn·N)` — linear in the nucleon counts.

`QOU.Mass.TypedBondSiteInvariance.regular_of_siteInvariant`,
`.mean_of_siteInvariant`, `.B2S_collapse`.

The proof pivot is `bondOf_eq`: the three-case typed scalar **is** the
bilinear form `L_nn + (L_pn − L_nn)(χa + χb) + (L_pp − 2L_pn + L_nn)·χa·χb`,
after which the master identity `B2S_eq` writes the bond sum in degree /
induced-edge coordinates and both structural theorems are a choice of `S` —
`|S| = 1` gives regularity, `|S| = 2` gives the mean condition.

## 2. Why this was not already covered

`QOU.Mass.UniformBondSimpleGraphExclusion` proves `b₃ ≤ 0` for a **uniform**
bond weight on any simple graph, and names its own escape hatch:

> "What is excluded is the conjunction *uniform bond weight* ∧ *simple graph*.
> Dropping either escapes it."

There are **two** ways to drop uniformity, and the corpus had only been
reading one of them:

| escape | status before this PR | status now |
|---|---|---|
| **coordination-dependent** `ε(z)` | identified as the survivor (`qou-edt7`), open number `ε(2)/ε(1) = 1.2137076` | untouched — this PR narrows *onto* it |
| **isospin-typed** `L_pp`/`L_pn`/`L_nn` | believed closed by `ChainBondOrderDependence`; **it was not** | closed here |

### The arity error that hid it

`ChainBondOrderDependence.orderIndependent_iff` proves arrangement-invariance
**iff** `L_pp = L_pn = L_nn`, and it is tempting to read that as *"physical ⇒
uniform bonds"*. It does not say that. It is a theorem about `bondSum` — the
sum over **adjacent pairs of a `List Bool`**, i.e. the *linear chain*
specifically. Its LHS quantifies over `List.Perm` of a chain, not over site
assignments on an arbitrary bond set.

The counterexample is immediate: **on the complete graph the typed sum is
site-invariant for arbitrary `L_pp, L_pn, L_nn`**, because the three pair
counts `C(Z,2)`, `Z·N`, `C(N,2)` are fixed by `(Z,N)` alone. So the chain's
conclusion does not generalise, and `L_pp + L_nn = 2·L_pn` — strictly weaker
than uniformity — genuinely suffices on a regular graph.

The chain's *stronger* conclusion is an artifact of the chain being
**irregular**: its endpoints have degree 1. That is precisely the hypothesis
`regular_of_siteInvariant` extracts, and it is the whole content of the
difference between the two theorems.

This is the `da-arity-conflation` class from AGENTS.md §"Grep the claim SHAPE"
— one specific functional's theorem read as a statement about a family. It
survived a topic-grep, as that section warns they do.

## 3. The two kills

**Regular branch.** Along `N = Z` the collapse gives
`2·B(A) = k_A·Z·(L_pp + L_nn)`, so with `k₂ = 1` (the only graph on two sites
carrying a bond) and the simple-graph degree bound `k ≤ A − 1`:

```
B(⁴He)/B(²H) = 2·k₄ ≤ 2·(4−1) = 6        AME2020: 28.2956624 / 2.224566 = 12.7196…
```

Refuted by a factor of more than two, with two nuclei and no fit. The
invariant is the degree bound — the same counting bound
`UniformBondSimpleGraphExclusion` cites, one coordinate over.

**Complete branch — and this is a genuine gap in the existing prune.**
`CoordinationSaturation.complete_graph_no_saturation` assumes a single
`ε > 0`, so it does **not** cover mixed signs. `complete_A2_coefficient`
computes that the `A²` coefficient of the isobaric complete-graph typed sum
is `L_pp + L_nn + 2L_pn`, which **can cancel** — a saturating complete-graph
family exists, and the existing lemma does not see it. It dies one step
later: under exactly that cancellation `complete_b3_eq` gives `b₃ = −2·b₂`,
so a bound deuteron (`b₂ = 2.224566 MeV > 0`) forces `b₃ = −4.449 MeV`
against the measured `b₃ = +1.426222 MeV`.

Worth stating plainly, because it is the more interesting half: **the
saturation prune as currently stated has a hole, and it is the sign
assumption.** The hole is closed here, but by a different invariant (the
three-body cumulant sign), not by extending the saturation argument.

## 4. The corrected prune map

The brief this work started from named four results. The tree holds at least
nine bearing directly on the extensive term. Recorded so the next agent does
not re-derive one of the five that were missing.

| result | what it excludes | assumes |
|---|---|---|
| `Mass/CoordinationSaturation` | complete-graph `z = A−1` cannot saturate | one uniform `ε > 0` |
| `MassTheory/ChainBondOrderDependence` | the linear chain is arrangement-dependent unless bonds are uniform | the **chain** bond set specifically |
| `MassTheory/BodyOrderRecurrenceDepth` | depth ≥ 3 forced; 3 terms cannot test it | — |
| `MassTheory/MayerThreeBodySign` | multiplicative `W = 1 − ∏f` forces `b₃ < 0` at `f_pn ≤ 2/3` | any edge set |
| **`MassTheory/ChainBindingNoSaturationPeak`** | the chain form has **no interior maximum in `A`** — exactly a hyperbola `c₁ + c₂/A`, and `c₁` is *independent of the isospin excess* | constants fixed along an isobar |
| **`Mass/UniformBondSimpleGraphExclusion`** | **the whole coordination-multiplicity family** gives `b₃ ≤ 0` — invariant `e₃ ≤ 3` | **uniform** bond weight |
| **`Mass/PairwiseCumulantVanishing`** | pairwise-additive assembly gives `b₃ = 0` for **every** bond functional `f` | the complete pair set |
| **`Mass/SU4CasimirIsAffineInPairCount`** | the SU(4) Casimir route — `S(n) = −(5/8)·C(n,2)` exactly, so constant per pair | — |
| **`Mass/TypedBondSiteInvariance`** (this PR) | isospin-typed, transferable, well-defined-on-a-nucleus | — |

Bold = not in the brief. The three that most change the picture are
`UniformBondSimpleGraphExclusion` (which is what made this PR's target
identifiable at all), `PairwiseCumulantVanishing` (which is *orthogonal* to
this PR rather than stronger — it fixes the pair set and varies the bond
*function*, this varies the *edge set and typing* at fixed pairwise shape;
neither subsumes the other), and `ChainBindingNoSaturationPeak`.

## 5. What actually survives

Reading the corrected map together, the pairwise class is exhausted along
every axis the corpus has tested:

- vary **which pairs bond** → `UniformBondSimpleGraphExclusion` (`b₃ ≤ 0`)
- vary the **bond function `f`** → `PairwiseCumulantVanishing` (`b₃ = 0`)
- vary the **isospin typing** → this PR (collapses to one-body, `2·k₄ ≤ 6`)
- vary the **assembly** to multiplicative → `MayerThreeBodySign` (`b₃ < 0`)

**One axis is left: the bond weight depending on the coordination number,
i.e. non-transferability across mass number.** That is `qou-edt7`'s surviving
mechanism and its open number is

```
ε(2)/ε(1) = 1.2137076        (the bond is 21.4 % stronger at coordination 2)
ε(3)/ε(1) = 2.1200
```

Bean `qou-edt7` already records `1.2137` vs `1.7467` as **43.9 % apart**,
which refutes single-ratio (Markov-power) scaling `ε(z) = ε(1)·r^{z−1}` for
every `r` — so even the surviving axis has its simplest form excluded.

**The upgrade this PR provides is epistemic, not directional.** `qou-edt7`
concluded "the rise is non-transferability" after excluding the uniform
family; that is now *proved* rather than *asserted-after-one-exclusion* — it
is non-transferability, and **not isospin typing either.**

## 6. Note on the framing I was asked to test, and why it was backwards

The brief proposed: *physical (arrangement-free) ⇒ uniform bonds ⇒ bounded
degree ⇒ constant `B/A`*, and asked whether that leaves "no room for a
super-pairwise extensive term at all".

Link 1 is false (§2). Link 2 does not hold either as stated — nothing about
uniformity constrains degree; what forces bounded degree is *saturation*,
independently. And the conclusion points the other way: the arrangement-
invariant pairwise family collapses to a one-body linear form and is
empirically dead, so a genuine super-pairwise term is **forced**, not
excluded.

That is the honest reading, and it agrees with where AGENTS.md already places
the open problem — "a separate, super-pairwise additive extensive object".
This PR does not find that object. It removes one more thing it cannot be.
