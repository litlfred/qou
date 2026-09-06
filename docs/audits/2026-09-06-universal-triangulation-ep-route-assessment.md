# Universal triangulation: what the Epstein–Penner route can and cannot do for the binding gap

**Date:** 2026-09-06 · **Branch:** `claude/universal-triangulation-binding-gap-hjatfd`
**Issue:** #6941 · **PR:** #6942
**Beans:** `qou-utri` (session), `qou-ptgd` (prune), `qou-eptr` (reachability + candidate),
`qou-plck` (Planck), `qou-unob` (universal object)
**Scope:** assessment + two prunes + two measurements. **Nothing is wired, no production number
moves, no witness is refreshed on the strength of a proposal.** Every "is" below is cited to a
file or to an assertion in a witness emitted by this branch.
**Method:** corpus-grep paths 1–6 run by hand (path 0 `corpus_search` unavailable — the
`paper-assistant` MCP server failed to connect this session, so every absence recorded here is
*lexical*).

---

## 0. The claim, flatly

1. **The route aims at the right thing.** Of the four missing pieces of the binding gap, three
   are structurally located and the open one is the irreducibly many-body term: measured
   connected 3-body cumulant `b₃ = +1.4262 MeV` against a model value of exactly `0`, where
   `QOU.Mass.CrossingModelPairLocality.b3_eq_zero_of_pairLocal` proves pair-locality forces that
   zero ([2026-09-05 audit §1.2](2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md)).
   A canonical cell decomposition is **extensive** (a sum over cells, so it dodges
   `exchangeDet_pow_two_le_four`), **4-body per cell** (so not pair-local), **canonical** (so it
   clears the NO-FITTING directive), and **bounded-degree** (the regime
   `QOU.Mass.CoordinationSaturation` forces). No previous candidate had all four at once.

2. **Its central categorical claim is false, and the falsity is now Lean.** "The Epstein–Penner
   decomposition is the terminal object of the Ptolemy groupoid" fails on both horns of a
   dichotomy proved sorry-free in §2. This refutes the *word*, not the *object*: a canonical
   decomposition still exists and is still unique, as a distinguished choice rather than a limit.

3. **The route reaches almost every atom and still cannot supply the shape residual, for a
   reason that has nothing to do with hyperbolicity.** 15 of the 16 atoms with non-zero binding
   have hyperbolic complements — but the live dictionary uses only **two distinct manifolds**,
   and **13 atoms share one of them** while their binding energies span a factor of `1.67e9`
   (§3). An Epstein–Penner invariant is a function of the manifold, hence constant on that class.
   No such invariant can separate its members.

4. **The natural candidate observable vanishes where it can be computed.** The Pachner distance
   between the triangulation this framework *derives* from the braid word and the canonical one
   is **0** on `4_1`, the only knot for which the corpus can produce both (§4). And on the
   framework's principal manifold the canonical decomposition is **not a triangulation at all** —
   it is two regular ideal octahedra — so the groupoid whose objects are ideal *triangulations*
   does not contain the object the proposal wants to distinguish.

5. **Both remaining questions were already answered in the corpus, in live content blocks.** The
   Planck length is a fourth calibration and is forbidden as an input; the admissible reading —
   "below Planck scale" as a *categorical* statement — is already written (§5). A universal
   object is already conjectured, in `C_χ` with Bring's curve at `χ = −6`, and that is a category
   of universes rather than a groupoid, so it survives the §2 prune (§6).

6. **Recommendation (judgement, not finding).** The binding-relevant part of this route is
   blocked by the *dictionary*, not by the geometry. If it is to be revived, the thing to attack
   is the four-branch dispatch in §3.4 — not a better invariant of a knot the dispatch has
   already collapsed. **Default — do nothing — is safe: nothing here changes any production
   number.**

---

## 1. Two errors in the dialog, both measured

### 1.1 The gluing equation is false at its own stated solution

The dialog gives the figure-eight edge equation as `z(1−z)⁻¹z(1−z)⁻¹ = 1` with solution
`z = e^{iπ/3}`. At that `z`, `z/(1−z) = e^{iπ/3}/e^{−iπ/3} = e^{2iπ/3}`, so the left-hand side is
`e^{4iπ/3}`. Evaluated: `−0.5000000000000001 − 0.8660254037844387i`. Not `1`.

The correct edge equation is `z₀z₁(1−z₀)(1−z₁) = 1`, which holds because `z(1−z) = 1` is exactly
`z² − z + 1 = 0`, the sixth-root condition. Evaluated at the same `z`: `1.0000000000000000`.

**This repo derived that form from the braid word yesterday**, with SnapPy nowhere in the
computation — [`2026-09-06-nz-gluing-data-from-braid-monodromy.md`](2026-09-06-nz-gluing-data-from-braid-monodromy.md),
Lean `figure_eight_gluing_at_sixth_root`, sorry-free. So the corrected statement is not merely
available, it is *internal*.

### 1.2 Three smaller ones

- **Epstein–Penner is a cell decomposition, not always a triangulation.** The Whitehead link's is
  a single ideal octahedron. So the proposal's category — objects are ideal *triangulations* —
  need not contain the object it distinguishes. §4 shows this is not hypothetical here: it is the
  case for the manifold 13 of 19 atoms are assigned.
- **The volume is not "the Chern–Simons 3-form integrated".** `Vol + i·CS` is the complexified
  invariant; the volume comes from the Bloch–Wigner dilogarithm `D(z)`, and `CS(4₁) = 0` because
  the figure-eight is amphichiral. The dialog's own audit trail agrees on the amphichirality.
- **`Vol(4₁) = 2·Cl₂(π/3) = 2.02988` is not "twice a Catalan constant variant".** Catalan's
  constant is `Cl₂(π/2) = 0.9160`, a different number; the two differ by `0.099`. AGENTS.md
  carries a STRICT guard on exactly this Λ-vs-`Cl₂` confusion, and the reachability probe now
  carries it as the assertion `catalan_is_not_cl2_pi_over_3`.
- **A 3-form restricted to a 2-manifold vanishes by degree.** The dialog's "restricting this
  3-form to Bring's surface evaluates to identically zero" is arity, not a computation. The
  corpus separately holds a substantive zero of this shape — the Bloch volume leg proved 0 for the
  deuteron — and the two should not be confused.

---

## 2. The prune: a groupoid has no distinguished terminal object

[`QOU/Mass/GroupoidTerminalDichotomy.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/GroupoidTerminalDichotomy.lean),
five declarations, sorry-free.

The content is one cancellation. For `f g : X ⟶ Y`, both `f ≫ t_Y` and `g ≫ t_Y` lie in `X ⟶ T`,
which a terminal `T` makes a subsingleton; in a groupoid `t_Y` is invertible hence monic, so
`f = g`. With `t_Y⁻¹ ∘ t_X` inhabiting every hom-set, each is a singleton and the groupoid is
equivalent to the one-object-one-morphism category.

| declaration | says |
|---|---|
| `hom_subsingleton_of_isTerminal` | the cancellation |
| `homOfIsTerminal` | every hom-set is inhabited |
| `isTerminal_of_isTerminal` | **first horn** — one terminal object makes *every* object terminal |
| `endo_eq_id_of_isTerminal` | every endomorphism is the identity |
| `isEmpty_isTerminal_of_ne_id` | **second horn** — one non-identity endomorphism rules out a terminal object everywhere |
| `terminal_dichotomy` | either none is terminal or all are; no middle case |

**Both horns bite, on the two readings of "the Ptolemy groupoid".** Penner's version has objects
= mapping-class-group orbits of ideal triangulations — that is what makes it yield presentations
of the mapping class group from the pentagon relation — so its automorphism groups are
non-trivial and the *second* horn applies: no terminal object exists. The unquotiented flip
groupoid is connected and, if the relations among flips are exactly the Harer–Penner
pentagon/involution/commutation ones, simply connected — so the *first* horn applies: every
object is terminal and terminality distinguishes nothing.

**The `Groupoid` hypothesis is load-bearing, not decoration.** A general category may perfectly
well have a terminal object alongside objects with non-trivial automorphisms; it is invertibility
of `t_Y` that collapses the whole thing.

**Scope.** Scope-(b) STRUCTURAL exclusion per AGENTS.md §"Before declaring refuted"; the
invariant cited is the proof itself. It refutes the framing, not the geometry. The correct
statement is that Epstein–Penner is a canonical *choice* — natural under isometry, the unique
minimiser of the convex-hull functional — i.e. a section of a forgetful functor. That distinction
is not pedantry: "terminal object" is precisely what would have made the construction functorial
for free, and it does not.

---

## 3. Reachability: the route reaches the atoms and cannot separate them

Producer: [`ep_decomposition_reachability_probe.py`](../../computations/probes/ep_decomposition_reachability_probe.py)
(9/9 assertions, `q0Anchor: independent`, no float64, no `q`, no Markov parameter).

### 3.1 The dictionary

| label | atoms | manifold | hyperbolic |
|---|---|---|---|
| trivial | proton, neutron, protium (`A = 1`) | unknot | no |
| satellite | deuterium (`A = 2`) | — | **no** |
| figure-eight | tritium, he3 (`A = 3`) | `4_1` | yes |
| Borromean | he4 … fe56 (`A ≥ 4`) | `L6a4` | yes |

19 atoms; 16 with non-zero binding; **15 of those 16 are hyperbolic**.

### 3.2 The deuteron is excluded twice over, independently

The dictionary calls `A = 2` a **satellite** knot. Thurston's trichotomy — a knot is exactly one
of torus, satellite, hyperbolic — makes a satellite complement non-hyperbolic, so it carries no
Epstein–Penner decomposition. This is *derived from the corpus's own classification* and does not
depend on the 2026-08-29 owner ruling that puts the deuteron on a `Vol = 0` braid closure. The
two agree, which is worth recording: the ruling and the live table are consistent here.

### 3.3 The decisive number

**The whole dictionary uses two distinct hyperbolic manifolds**, and

| class | atoms | binding range (MeV) | max/min |
|---|---|---|---|
| `4_1` | 2 | `−3.3606` … `−2.5843` | `0.769` |
| `L6a4` | **13** | `0.7183` … `1.1977e9` | **`1.667e9`** |

An Epstein–Penner decomposition is a function of the *manifold*. Every quantity derived from it —
cell count, volume, cusp shape, Pachner distance to any other triangulation, 3d-index — takes the
same value on every atom in a class. **So no function of the Epstein–Penner decomposition of the
DICTIONARY-NAMED knot can separate 13 atoms whose binding spans nine orders of magnitude.**
Scope-(b) structural; the invariant is that a constant cannot separate a varying quantity.

> **🛑 Read that as a statement about ONE FIELD, not about the framework. Corrected 2026-09-06 on
> owner challenge — *"are you saying that you can't distinguish atoms with A ≥ 4?"*** No, and the
> wording that invited the question ("the dictionary collapses every atom with `A ≥ 4` onto one
> knot") is a true statement about `classify_nuclear_knot` that reads as a false one about the
> framework's discriminating power. Measured over the same 13 atoms in
> `hadron-knot-table.witness.json`, exactly one field is constant:
>
> | field | distinct values |
> |---|---|
> | `knot_type` | **1 / 13** — the only collapse |
> | `n_terms` | 1 / 13 (NF basis size, constant by construction — the 6-element H₃ basis) |
> | `net` | **13 / 13** |
> | `ln\|tr_M\|` | **13 / 13** |
> | `B_MeV` | **13 / 13** |
> | `V_per_gen` | **13 / 13** |
>
> So every *physical* quantity separates all 13, and so do the per-atom braid words (§3.5). The
> exclusion above is narrow by exactly that much: it forbids sourcing the shape residual from an
> Epstein–Penner invariant *of the label*, and says nothing about the framework's ability to tell
> these atoms apart, which is total.

### 3.4 …and the blocker is the dictionary, not the geometry

`classify_nuclear_knot(Z, N)` is a four-branch dispatch that **factors through `A = Z + N`** —
verified over a `30 × 34` grid, assertion `classifier_depends_on_A_only`. It discards the braid
word entirely, and it has **exactly one consumer in the tree** (`hadron_knot_table.py`); it lives
in a file named `hecke_core_legacy.py`. The live binding law attaches to the braid word (a `tr_M`
ratio), a strictly finer object.

Two consequences, and the second is the useful one:

- The §3.3 exclusion is **conditional**: it excludes an Epstein–Penner invariant *of the
  dictionary-assigned knot*. An Epstein–Penner invariant of the **actual per-atom braid closure**
  is untested.

  > **🛑 CORRECTED 2026-09-06 — this clause originally ended "…which the corpus does not
  > currently do", and that was wrong.** See §3.5: the per-atom canonical braid word is computed
  > live by `canonical_braid_crossings.atom_canonical_crossings(Z, N)` for any `(Z, N)`, and it is
  > a function of `(Z, N)` rather than of `A`. So the object the route needs already exists here.
  > What is missing is the *knot type* of each closure — a knot-recognition problem with a
  > definite answer, not a modelling decision awaiting a ruling. This session also framed
  > `qou-imkb` as the blocking owner decision for this route; that bean governs **Model B's `T1`
  > registry** and is a separate matter.
- AGENTS.md flags per-case dispatch on `A` as a fitting smell in its own right ("a formula that
  branches on `A` … has one free choice per branch"). The dictionary is such a dispatch. So the
  finding here reflects on the dictionary at least as much as on the route.

### 3.5 The per-atom braid closure exists, and varies with `(Z, N)`

Producer: [`per_atom_braid_closure_probe.py`](../../computations/probes/per_atom_braid_closure_probe.py)
(5/5, `q0Anchor: independent`).

`atom_canonical_crossings(Z, N)` returns a canonical braid word for any atom, and over a
ten-atom sample the words are **pairwise distinct, 10 of 10**. The sharp case is `tritium (1,2)`
against `he3 (2,1)`: same mass number, same length of 35 crossings, and they still differ — at
four positions, with different crossing *types* (`averaged_weighted` vs `sigma`,
`averaged` vs `sigma`), and with different exponent sums, **4 against 8**. Word *length* does
factor through `A` (12 crossings per nucleon), which is why length alone is not the
discriminator; the word does not.

**What this does not establish.** Distinct braid *words* do not imply distinct *closures* —
Markov moves and conjugation routinely identify different words with the same link — and the
probe performs no knot recognition and no hyperbolicity test. Recognising the closure of a
143-crossing braid on 36 strands (carbon-12) is a hard computation. But it is a computation with
a definite answer, and that is the difference from where §3.4 originally placed this.

**So the two live questions are, in order:** are the closures distinct links, and are they
hyperbolic? Both are open. Neither is blocked on an owner decision.

---

## 4. Cell structure, and the Pachner-distance candidate

Producer: [`canonical_cell_structure_probe.py`](../../computations/probes/canonical_cell_structure_probe.py)
(7/7 assertions, `q0Anchor: independent`).

| quantity | value |
|---|---|
| `Vol(regular ideal tetrahedron) = Cl₂(π/3)` | `1.014941606409653625` |
| `Vol(regular ideal octahedron) = 4·Catalan` | `3.6638623767088760602` |
| `Vol(4_1) / V_tet` | **`2.0`** |
| `Vol(L6a4) / V_oct` | **`2.0`** |
| `Vol(L6a4) / V_tet` | `7.21984861704459` — **not an integer** |
| `V_oct / V_tet` | `3.609924308522295` — **not an integer** |

**The candidate observable is zero where it can be computed.** The Floyd–Hatcher layered
triangulation of `S³∖4₁`, derived from the braid word with no SnapPy input, has **two**
tetrahedra with both shapes at the sixth root of unity — the regular ideal tetrahedron. The
canonical decomposition of the figure-eight is *also* two regular ideal tetrahedra. They coincide,
so the Pachner distance is **0** and the observable carries no information on the one case the
framework can derive.

**The principal manifold's canonical decomposition is not a triangulation.** `L6a4` decomposes
into two regular ideal *octahedra*, and its volume is not an integer multiple of the regular ideal
tetrahedron's, so it cannot be re-read as a tetrahedral decomposition. This makes §1.2's first
bullet concrete on the manifold 13 of 19 atoms are assigned.

**Scope, so neither result is over-read.** A volume identity is *consistent* with a cell structure;
it does not prove one. The two-tetrahedron and two-octahedron decompositions are classical
(Thurston) and are cited as such; what this probe contributes is that the corpus's own registry
agrees with them, that the Borromean volume admits no tetrahedral re-reading, and that the
candidate is `0` on `4_1`. It is **not** a claim that a Pachner distance is uninformative on some
manifold where the two decompositions differ — no such manifold is currently derivable here, which
is itself the finding.

**One measurement hygiene note.** The derived volume is serialized by its producer at **45
significant digits**, so comparing it against the registry's full-precision value at the corpus
tolerance of `1e-62` fails by `4.94e-45` — which *is* that truncation, not a disagreement. The
probe's tolerance for that one comparison is set to the recorded precision of the input with five
digits of margin, and says so in the assertion text. This is not a widened baseline: the two
values agree to every digit the witness records.

---

## 5. Planck length — symbolic in `q`, and NOT a calibration

> **🛑 THIS SECTION ORIGINALLY SAID THE OPPOSITE, AND IT WAS WRONG. Corrected
> 2026-09-06 on owner instruction — *"plank length is not a calibration.. written symbolic in
> q"*.** The section was headed "already answered in the corpus, both halves" and led with
> "**Forbidden as an input**", generalising `meridian-exceptional-divisor-note.md` into a
> prohibition on the Planck length as such. That note forbids something narrower: pinning the
> **substrate** at `m_Planck`, i.e. importing SI `G` as an input that fixes `q₀`. Writing
> `ℓ_P(q)` as a `q`-expression is a different move, it is **already done in this corpus**, and it
> introduces no calibration. `g-q-closed-form.md` says so in its own words: the SI value of `G`
> "functions strictly as the human-scale rescaling ... enters as a unit-system datum, **not as a
> fit parameter on `q`**".

Producer: [`planck_symbolic_in_q_probe.py`](../../computations/probes/planck_symbolic_in_q_probe.py)
(8/8).

With the corpus's own forms `ħ_q = (q−1)/q`, `c_q = 1/(q−1)`, `G_q = q²/(q−1)⁴`:

| quantity | closed form in `q` |
|---|---|
| `G` in Planck units | `G_q·(ħ_q/c_q)² = 1` **identically**, as a rational function |
| `ℓ_P = √(ħ_q G_q / c_q³)` | `√q` |
| `m_P = √(ħ_q c_q / G_q)` | `(q−1)²/q^{3/2}` |
| `t_P = √(ħ_q G_q / c_q⁵)` | `√q·\|q−1\|` (`= √q·(q−1)` on `q > 1`) |

Each is a function of `q` **alone** — no `m_e`, no CODATA, no SI `G` — so none of them is a
calibration. The `G_Planck = 1` identity is a real consistency win: it is asserted in
`g-q-closed-form.md` and now verified as an exact rational-function identity rather than a
numerical coincidence.

### 5.1 Three different objects are called "the Planck length" here

| name | expression | at proton `q₀` |
|---|---|---|
| normalised total ([`discrete-planck-step.md`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md)) | `ħ_q · q/(q−1) = 1` | `1` |
| per-step share ([`p5-counterexample.md`](../../content/quantum-observable-universe/fluid-dynamics/p5-counterexample.md), written `ℓ_q`) | `(q−1)/q = ħ_q` | `0.0990817` |
| dimensional (derived above; **no corpus block carries it**) | `√q` | `1.0535552` |

The corpus already separates the first two — `discrete-planck-step.md` says outright *"This is
the **normalised total** ... It is not the same object as the local `ℓ_P^step ∼ ħ_q`"*. The third
is new here. The share and the dimensional form differ by a factor of **10.633** at `q₀`.

**Recorded, not resolved.** This is a notation collision of exactly the kind the register exists
to catch, and which of the three a given block *means* is an author question, not one a probe
should decide. Nothing here claims `√q` is the "right" Planck length or that either corpus form
is wrong.

### 5.2 What the corpus does forbid, precisely

**Pinning the substrate at `m_Planck`.**
[`meridian-exceptional-divisor-note.md`](../../content/quantum-observable-universe/braids-and-knots/meridian-exceptional-divisor-note.md):
*"Identifying the computational tick with the Planck time would pin the substrate at
`m_Planck`, i.e. introduce Newton's constant `G` — an input outside the three-calibration weak
sector … That is a fourth calibration and a substrate-scale derivation, which the framework does
not undertake."* Independently blocked by the 2026-08-02 forever-gate on substrate-`q₀`
derivation.

**The admissible reading is already written.**
[`approach-to-exceptional-divisor.md`](../../content/quantum-observable-universe/brings-surface/approach-to-exceptional-divisor.md):
*"'Below Planck scale' in QOU is a **categorical** statement, not a metric one. The relevant
geometry switches from the base `M` to the fibre `S_p`."* And
[`g-q-closed-form.md`](../../content/quantum-observable-universe/observations/g-q-closed-form.md)
carries `G` in Planck units as a dimensionless `q`-rational with `G_Planck = 1` — i.e. as a
*ratio*, which is the only way a gravitational scale is admitted.

So the prohibition is on *pinning `q₀` with SI `G`*, not on the Planck length. Written in `q` it
is already there and costs nothing. The one question that is genuinely open, and that needs no new
dimensional constant, is whether the fibre `S_p` is the right object to attach a decomposition to —
a question about the categorical statement above. That is a paragraph, not a tranche, and it is
left open.

---

## 6. Universal object — already conjectured, in a different category

[`universality-general.md`](../../content/quantum-observable-universe/brings-surface/universality-general.md):
*"For any admissible Euler characteristic `χ`, the category `C_χ` of ℂ quantum observable
universes with `χ(S) = χ` should admit a terminal object determined by the unique maximally
symmetric Riemann surface of the corresponding genus. Bring's curve distinguishes the Descartes
case `χ = −6`, but analogous universal objects are expected at other values of `χ`."*

That is the corpus's universal-object claim, and it lives in a category of **universes**, which is
not a groupoid — so it is untouched by the §2 prune and is the correct home for such a claim. See
also `terminal-morphism-brings`. The dialog conflates two different universality claims, and the
one it names ("terminal object") is the one that fails; the one the corpus already has is the one
that stands.

---

## 7. What survives

**Not refuted, and worth keeping on the shelf:** the *reason* a cell decomposition was attractive
— extensive, 4-body per cell, canonical, bounded-degree — is untouched by anything here. §3.3 and
§4 are statements about the dictionary's knots and about `4_1`, not about cell decompositions in
general.

**The live route, and it is NOT blocked on an owner decision.**

> **🛑 CORRECTED 2026-09-06.** This paragraph originally said the route was "blocked on the
> dictionary being a four-branch dispatch", that unblocking it "is a modelling decision with real
> consequences", and pointed at bean `qou-imkb`. §3.5 measures otherwise: the per-atom canonical
> braid word is computed live for any `(Z, N)` and is a function of `(Z, N)`, not of `A`.
> `qou-imkb` governs **Model B's `T1` registry**, which is a different question.

Three questions, in dependency order, none of them requiring a ruling:

1. **Are the per-atom closures distinct links?** Distinct words need not close to distinct links.
   Answerable by invariants that are cheap on a braid closure (Jones via the Markov trace the
   framework already computes, Alexander, linking numbers) before any knot recognition is
   attempted.
2. **Are they hyperbolic?** Thurston's trichotomy makes this a real question with a real answer,
   and the corpus already has the gate (`sw_hyperbolicity_gate`) for named knots — what it lacks
   is recognition of an unnamed 143-crossing closure.
3. **Does the canonical decomposition then vary across atoms?** Only this one is the original
   route, and it is downstream of both.

The cheapest thing that could kill the whole route is question 1 returning "the closures coincide".
The cheapest thing that could *advance* it is the `H₄`-layering literature question of §9.1, which
is a search rather than a derivation.

**What still cannot help:** a better invariant of the *dictionary-named* knot. §3.3 is unaffected by
any of the above.

**A tempting move to name and refuse.** Any Pachner or volume quantity selected because it lands
near `b₃` is a fit, is forbidden by the NO-FITTING directive, and would be caught by the
three-calibration discipline review. The correct posture is that the gap stays visible.

---

## 8. Verification limits

- **CI is `workflow_dispatch`-only in this repo**, so the agent's own verification is the gate.
  Lean: `lean`-direct with `-DautoImplicit=false -s 65536` against the restored olean cache, exit
  0, zero warnings; no `sorry`, no `axiom`, no `native_decide`; `#print axioms` on all five
  declarations reports only `[propext, Classical.choice, Quot.sound]`.
- **Corpus-grep path 0 (`corpus_search`) was unavailable** — the `paper-assistant` MCP server
  failed to connect. Every absence claimed here is therefore *lexical*, and a prior treatment
  written in different vocabulary would not have been found. "Ptolemy groupoid" occurs nowhere in
  `content/`, `docs/` or `computations/`; it occurs in exactly two library files, one of which is
  a duplicate of the other.
- **The knot dictionary is read from `hadron-knot-table.witness.json`**, which AGENTS.md records
  as the one file on `main` still carrying the retired muon `q₀` pin in `q0Value`. Every field
  read here — `knot_type`, `Z`, `N`, `A`, `B_MeV` — is a label or a binding energy, and the
  measurement is over labels and set cardinalities, so that staleness does not bear on §3. It is
  recorded because a reader should not infer the witness is clean.
- **The seven contended tree-measuring audit witnesses moved during the precision-gate run and
  were reverted, not committed**, per the gate script's own instruction and bean `qou-v0t8`.
- **The precision gates report nine RED ratchets, and they are PRE-EXISTING — measured, not
  assumed.** `scripts/precision-gates.sh` was run twice: once on this branch (`--changed`, which
  decides *whether* the suite runs, not which gates run) and once on a detached worktree at the
  branch point `1352b02c2` with none of this work present. The `RED:` and `ADVISORY:` lines are
  **byte-identical** between the two (`md5 6df99989672bb93b302c5fdc3ade55b9` on both):

  ```
  RED: q0-anchor flip · q0-anchor refill ratchet · import-time dps ratchet ·
       never-raises-dps ratchet · float64-padding ratchet · q0-value drift ratchet ·
       CODATA stale-edition · hardcoded braid word (self-test) · mixed mpf/f64 -> serializer
  ```

  So this branch introduces no new precision-gate failure. It is worth stating the negative
  precisely: this is evidence that *these nine gates* are unchanged by this work, **not** evidence
  that the tree is clean — the nine are red on `main` and stay red, and nothing here drains them.
  Both probes are `q0Anchor: independent` with no `q`, no Markov parameter and no CODATA value in
  either, which is consistent with the result but is not what establishes it; the two-run
  comparison is.

---

## 9. Families of hyperbolic knots with known ideal triangulations — what is held

Owner question, verbatim: *"do we know any relations between families of hyperbolic knots and
ideal triangulation?"* **Yes, and this corpus holds the literature for the two families that
matter here.** The organising object in both cases is a word in `R, L` — equivalently a path in
the Farey tessellation — and the triangulation is *layered* one tetrahedron per letter.

| family | word | triangulation | held as |
|---|---|---|---|
| once-punctured-torus bundles | LR word of the monodromy in `SL₂(ℤ)` | Floyd–Hatcher / Jørgensen layered | [`arxiv-0808.2716v4`](../../library/arxiv-0808.2716v4/) (Futer–Kalfagianni–Purcell, *Cusp areas of Farey manifolds*) §2.2 |
| two-bridge links `S(p,q)` | LR word of the continued fraction of `p/q` | Guéritaud layered | same, §2.4 |
| two-bridge knots (1-loop = torsion) | — | ideal triangulation power series | [`arxiv-2411.03801v2`](../../library/arxiv-2411.03801v2/) |
| 2-bridge coloured Jones | — | — | [`kmj-48-2-255`](../../library/kmj-48-2-255/) |

The first row is **already internal to this repo**: the 2026-09-06 braid-monodromy probe derives
the `4₁` layered triangulation from the canonical 3-braid with no SnapPy input. The second row is
the one that matters for reach, because it covers **`4₁ = S(5,2)` and `5₂ = S(7,3)` under one
functor** — the cross-knot gate the `A_ω` arc needs. It is already beaned as `qou-yvyd`.

### 9.1 The Bring route, and the caveat that decides whether it works

Owner proposal: *"if we fix on brings, then every hyperbolic knot convolution gets knot
complement. from there to triangulation."*

The corpus holds the relevant paper — [`arxiv-2402.08782v1`](../../library/arxiv-2402.08782v1/),
Kattan–Singerman, *Hecke–Farey coordinates for Bring's surface*. Its content: Bring's surface is
`H/H₄(5)`, the main result is the 20-sided hyperbolic polygon presenting it, and it develops
**Hecke–Farey fractions** and **Farey circuits** on that surface. So the Farey combinatorics —
the same object that indexes layered triangulations — *is* available on Bring's surface, which
is the substance behind the proposal.

**But the Hecke group is not the same one, and that gap is load-bearing.** The layered-triangulation
machinery of the table above runs on the **modular group `Γ = H₃ = PSL(2,ℤ)`**: the Farey
tessellation there is the once-punctured-torus Teichmüller combinatorics, and `R, L` generate it.
Bring's surface is presented by **`H₄`**, a *different* Hecke group. Kattan–Singerman's own framing
is that `H₃` studies triangular maps and they use `H₄` for the `{5,4}` map of genus 4. Nothing
found in the corpus or the held library asserts an `H₄` analogue of the Floyd–Hatcher/Guéritaud
layering, and this audit does **not** claim one exists.

**So the honest status of the Bring route is:** the combinatorial vocabulary transfers (Farey
coordinates exist on Bring's surface, and are held), and the *theorem* that would carry a word to a
layered ideal triangulation does not, at `H₄`, in anything this corpus holds. That is a literature
question with a definite answer — either the `H₄` layering exists in the literature and is not yet
held here, or it is genuinely open — and it is the cheapest next thing to settle, because it
decides whether "fix on Bring's" reaches a triangulation at all or only reaches a tessellation.

Recorded as bean `qou-brfy`. Note also the standing caution from §1.2: a Farey/flip story on a
**surface** is 2-dimensional, and Pachner 2–3 moves on a 3-manifold triangulation are not the same
moves. The two are related through *bundles* over the surface, which is exactly what the first row
of the table is; keeping that distinction is what makes the route checkable rather than suggestive.
