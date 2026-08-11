# The writhe's level of definition, and what survives the vertical move

**Date:** 2026-08-10
**Beans:** epic `qou-qia8`; `qou-ap47` (V7), `qou-rhfy` (V10), `qou-yz26` (V11),
`qou-owft` (V12)
**PR:** [#4961](https://github.com/litlfred/qou/pull/4961)
**Lean:**
[`WritheMarkovInvariance.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/WritheMarkovInvariance.lean),
[`WritheLevelParity.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/WritheLevelParity.lean)

## 1. The collision

Two published claims cannot both hold as written.

[`markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md):

> Conjugation `β ↦ γβγ⁻¹` is the horizontal direction … Markov's theorem
> dictates that **horizontal and vertical moves exhaust the gauge freedom.**

[`sm-lagrangian-selection-rules.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-lagrangian-selection-rules.md):

> Conserved quantities are functions on states **constant on gauge orbits**.
> The framework currently exhibits two such invariants without fitted
> parameters: the Coulomb charge `Q = w/2` … and the writhe-to-isospin
> assignment `w ↦ I₃`.

Vertical is Markov II, `β ∈ B_n ↦ βσ_n^{±1} ∈ B_{n+1}`, which presents the
**same link** and shifts the writhe by `±1`. A writhe-derived quantity therefore
cannot be constant on gauge orbits that include the vertical direction. This
reaches production: `Q` and `I₃` are wired, not merely discussed.

The corpus already knew the diagram-level twin of this fact — the Lean file
[`reidemeister-mass-invariance.lean`](../../content/quantum-observable-universe/mass-theory/reidemeister-mass-invariance.lean)
carries `writhe_R1_changes` with the docstring *"Writhe is NOT a knot invariant
(R-I changes it)"*. `sm-lagrangian-selection-rules.md` contradicts a theorem in
its own corpus.

## 2. Owner ruling

**Reading 1: Gröbner–Shirshov normal forms are the states.** Reading 2 (gauge
freedom includes vertical moves, so `Q` and `I₃` are not state functions at all)
is kept open but is not the working convention.

The sharper principle the owner supplied is what makes Reading 1 work:

> the observable at a point is the trace on the lowest part of the substrate
> tower.

That is not a quotient by the vertical move — it is a **canonical section** of
it. One destabilises down the tower (`tr_M(x T_n) = z · tr_M(x)`) to the minimal
level and evaluates there. The construction is well-posed because:

* the minimal level is the **braid index**, itself a link invariant;
* at the minimal level the surviving moves are conjugation (and exchange), which
  `writhe_conj` proves preserve the writhe;
* so the writhe *evaluated at the bottom of the tower* is a number, and `Q` and
  `I₃` are observables of that datum.

Nothing numerical changes. What changes is the wording: `Q` and `I₃` are
constant on **horizontal** orbits at the tower's lowest level, not on the full
Markov orbit.

The Markov *trace* is consistent in a way the bare writhe is not: `tr_M` is
invariant under both moves, which is why it descends to links unaided.

## 3. What is proved

All sorry-free, `lean`-direct exit 0, `#print axioms` clean (no `sorryAx`),
three-arm negative control rejected as required.

### `WritheMarkovInvariance.lean`

| Theorem | Content |
|---|---|
| `writhe_append`, `writhe_inv` | additivity; inversion on the inverse word |
| `writhe_conj` | **Markov I is safe** — `writhe(γβγ⁻¹) = writhe(β)` |
| `writhe_stabilize`, `writhe_stabilize_neg` | **Markov II is not** — shifts by exactly `±1` |
| `coulombCharge_not_stabilization_invariant` | `Q = w/2` shifts by `±1/2` under a move that does not change the link |

### `WritheLevelParity.lean`

| Theorem | Content |
|---|---|
| `markovPair_parity` | **soundness** — `(w − n) mod 2` is invariant under both Markov-II moves |
| `markovPair_of_even` | **completeness** — any two level pairs of equal parity are Markov-equivalent, so `(w − n) mod 2` is *the* invariant of the pair |
| `writhe_not_pair_invariant`, `writhe_sub_level_not_pair_invariant`, `writhe_add_level_not_pair_invariant` | `w`, `w − n`, `w + n` are each **not** invariant — nothing coarser than the parity survives |
| `writhe_sub_length_even` | `writhe β ≡ length β (mod 2)` — the one framework-side step, unconditional |
| `component_parity_of_permSign` | **conditional** on the classical cycle-sign identity (hypothesis carried explicitly, cited): `c ≡ w − n (mod 2)` |
| `carrier_components` | component counts **computed** from the braid words via the underlying permutation |
| `carrier_component_parity` | the identity verified on all seven corpus carriers |
| `statistics_reading_fails_on_gluon` | the fermion/boson reading of component parity is refuted |
| `leptonNumber_collapses_at_minimal_level` | `L = sign(w)` dies under the minimal-level ruling too |

## 4. `(w − n) mod 2` — what it is and what it is not

Markov II acts on the pair `(w, n)` as `(w ± 1, n + 1)`. The complete invariant
of that action is `(w − n) mod 2`, and by the permutation-sign identity it is the
**component parity of the closure**. Computed on every carrier the corpus names:

| carrier | word | `w` | `n` | `c` | `(w−n) mod 2` | `c mod 2` |
|---|---|---:|---:|---:|---:|---:|
| `ν_e` | `σ₁ ∈ B₂` | 1 | 2 | 1 | 1 | 1 ✓ |
| Hopf link | `σ₁² ∈ B₂` | 2 | 2 | 2 | 0 | 0 ✓ |
| `e⁻` | `σ₁³ ∈ B₂` | 3 | 2 | 1 | 1 | 1 ✓ |
| gen. 2 | `σ₁⁵ ∈ B₂` | 5 | 2 | 1 | 1 | 1 ✓ |
| gen. 3 | `σ₁⁷ ∈ B₂` | 7 | 2 | 1 | 1 | 1 ✓ |
| gluon unit | `σ₁σ₂⁻¹ ∈ B₃` | 0 | 3 | 1 | 1 | 1 ✓ |
| Borromean baryon | `(σ₁σ₂⁻¹)³ ∈ B₃` | 0 | 3 | 3 | 1 | 1 ✓ |

The Borromean row is a genuine check: the component count is computed from the
braid word's permutation and comes out `3`, the number of Borromean rings.

**The statistics reading is refuted.** Odd component count ↔ fermion matches the
leptons (1 component) and the Borromean baryon (3 components), all fermions. It
fails on the **gluon unit**: `σ₁σ₂⁻¹` has a 3-cycle permutation, so its closure
is a *single* component, hence odd, hence "fermion". The gluon is a boson.
(This corrects an in-session verbal claim that the gluon unit closes to two
components; it does not.)

So `carrier_component_parity` is a theorem about permutation cycles with **no
framework content**, and the physical reading of it is dead. **Do not wire it.**
Its legitimate use is as a *consistency check* on level-crossing claims: it
carries one bit and cannot carry `Q`, `I₃`, or a `δ_q` magnitude. Under the owner
ruling the substitute for the writhe is its value at the braid index, not this
parity.

## 5. Downstream blast radius (audit sweep)

585 files mention `writhe`; the overwhelming majority merely mention it. The
sweep classified every block or script that **asserts or depends on a level**.

### 5a. Corrected in this PR — definitely wrong

| File | Was | Now |
|---|---|---|
| `appendix-standard-model/sm-lagrangian-selection-rules.md` | `Q`, `I₃` "constant on gauge orbits" | constant on **horizontal** orbits at the tower's lowest level, with the Lean cited |
| `climax-volume-mass/q-momentum.md` | `p_q` = writhe of *a* representative, called a property of the particle | writhe of the **canonical** (GS normal form, minimal level) representative, with a new *"Why the representative must be canonical"* paragraph |
| `mass-theory/torus-knot-delta-q-writhe.md` | `w = (m−1)p` for `T_{m,p}` | with `m ≤ p`, so `m` is the **braid index** (Morton–Williams). Without it, `T_{2,3} ≅ T_{3,2}` would get `w = 3` *or* `4`, i.e. two `δ_q` for the same knot; `10_124` gets `10` or `12`. The compute already presents every carrier with `m < p`, so **no number changes** |
| `observations/strangelet-crossing-energy.md` | `Q = 0` called "this topological invariant" | invariant of the canonical `n = 3` presentation, not of the closure |

### 5b. Corrected in this PR — suspect, one clause each

| File | Fix |
|---|---|
| `appendix-standard-model/strand-twist-datum.md` | "descends to gauge orbits" → descends to the **horizontal** (`S_n`, fixed-`n`) orbits; vertical behaviour flagged as **untested**. This matters most of the four: the twist datum is the *candidate hypercharge invariant*, and stabilisation adds a strand hence a new `t_{n+1}` |
| `appendix-standard-model/sm-gauge-truncation.md` | `Q` evaluated at the tower's lowest level; noted that the `I₃` nucleon comparison is at fixed `n` so the caveat does not weaken it |
| `knots-particles-confinement/electroweak-triplet-…-involution-slot.md` | neutrality ⇔ vanishing writhe scoped to the even-twist `B₂` slot family (the writhe-`±1` unknot is a counterexample outside it). The Lean is a clean statement about `w ∈ ℤ` and needs no change |
| `computations/chiral_fermion_braid_words_probe.py` | was **stale** — the `.md` and `.lean` carried the refutation, the producer still advertised `all_corpus_rows_match: True` as support. Now leads with `VERDICT: REFUTED`, computes both refutations, and renames the field to `all_rows_match_at_the_AS_WRITTEN_levels` with an explanation of why that match is an artefact |

### 5c. The eightfold / hypercharge cone — **not affected**

The `p`/`n` same-`Y` argument (`eightfold-way/flavor-charge-assignments.md`,
`sm-hypercharge-invariant.md`/`.lean`, `eightfold-open-problems.md`,
`sm-open-problems.md`, `u1_hypercharge_assignment.py`) compares the proton and
neutron **both at `n = 2`**. It is a fixed-level comparison and survives
untouched. `WritheIndependenceCriterion.lean`'s narrowing of that argument to
*injective* writhe→`Y` maps is likewise unaffected.

`inter_nucleon_linked_channel.py` is also **not** a defect: it pins
`strand_count = 2` for all three channels, and its own note records that the
production `pp = +1` / `nn = −1` datum is the **linking number** of a Hopf link —
a genuine link invariant. The name "writhe ladder" is misleading; the datum is
safer than the name.

### 5d. Mass / binding — mild, no numbers move

`delta_lambda_exponent_from_crossings.py` and
`deltalambda/c_knot_nonuniversal_pinned_weight_probe.py` compare writhes across
isotopes that sit at different braid indices (`n = 3(Z+N)`). Under the owner
ruling the fixed canonical words **are** the states, so the comparisons stand;
they want a framing note naming the level. The `c_knot` result is a **negative**
(same `w`, different `C_knot` ⇒ no writhe-only factor) and survives regardless.
Queued as `qou-yz26`.

### 5e. Needs author intent — not changed

`climax-volume-mass/noether-theorem-callout.md` has the row

> Spatial translation │ Braid stabilisation │ Momentum `p` │ `p_q(β)` (writhe) │ Markov II shift

which assigns `p_q = w` as the *conserved* Noether charge of the symmetry that is
exactly the move changing it. Two readings: (a) `w` is the conjugate
**coordinate** of the tower translation, not the conserved charge — the row is
mislabelled; (b) the "Markov II shift" column is already flagging the anomaly
deliberately. The text does not distinguish them. Left alone.

### 5f. The correct pattern, already in the corpus

These are the templates the fixes follow, and the strongest evidence the
framework already knows the right level:

* `mass-theory/reidemeister-mass-invariance.lean` — `writhe_R1_changes`,
  with `writhe_R2_invariant`/`writhe_R3_invariant` proved separately.
* `mass-theory/hecke-charge-mass-duality.md` — places `Q` and `𝔈_cross` under
  *"Horizontal / Conjugation (within a fibre)"* and opens §16 with
  *"Restricting to a single level of the brane tower"*.
* `nuclear-interactions/box-braid-irreducibility-proof.md` — the braid index of
  `T(m,n)` is `min(m,n)` (Morton–Williams), Lean-proved. This is the owner's
  "lowest level", already in the corpus, and it is the free fix for the torus-knot
  finding.
* `predicted-spectra/hydrogen-shell-writhe.md` — *"the writhe **in its minimal
  diagram**"*, and it *uses* R-I sensitivity deliberately.
* `computations/gb_winding_parity_wire_probe.py` — *"it is a FRAMED readout, not
  yet a knot invariant … must be writhe-normalised first"*.

## 6. A second refutation of `L = sign(writhe)`

The Markov-II refutation (recorded 2026-08-10, PR #4943) left one escape: if
states are GS normal forms, Markov moves do not act within the state space, so
`L = sign(w)` is well-defined.

**The minimal-level ruling closes that escape.** The corpus assigns
`ν_e = K_{0₁} = T(2,1)` — the **unknot**, braid index `1`. Its minimal-level
normal form is the *empty* word, and so is its mirror's. At the level where the
framework says observables live, `ν_e` and `ν̄_e` are the **same state**, so no
function of the state separates them — quite apart from `sign(0) = 0 ≠ +1`.
Proved as `leptonNumber_collapses_at_minimal_level`.

This is `LeptonNumberCarrierChirality.lean`'s amphichirality obstruction
reappearing once the canonical representative is pinned: the escape used there
was *"the carrier is the braid word, not the knot type"*, and at minimal level
the braid word **is** determined by the knot type.

So `L = sign(w)` is refuted under **both** readings — Markov II kills it if
gauge orbits include the vertical move, the minimal-level ruling kills it if they
do not. **Scope-(a)**: this refutes the candidate, not lepton number and not the
`Y = B − L` route. What it locates is that `L` must come from data the writhe
does not carry — the framing or the smoothing history, not the crossing sum.

## 7. Honest scope

**Scope-(a) throughout.** Section 1 is an inconsistency between two published
claims, with the invariant cited (writhe additivity under stabilisation). It does
**not** show `Q = w/2` is wrong; it shows the *level* at which it is defined is
not the one `sm-lagrangian-selection-rules.md` asserted. **No number changes
anywhere in this PR.**

`markovPair_parity` / `markovPair_of_even` are statements about the pair `(w, n)`
under the moves' action *on that pair*, which is all Markov II determines. They
do **not** claim every pair of braids with matching parity is Markov-equivalent
as braids — that is false and much stronger.

`component_parity_of_permSign` is **conditional** on a textbook fact, carried as
an explicit hypothesis and named `_of_` per AGENTS.md §3b-cond.
