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
same value on every atom in a class. **So no function of the Epstein–Penner decomposition alone
can separate 13 atoms whose binding spans nine orders of magnitude.** Scope-(b) structural; the
invariant is that a constant cannot separate a varying quantity.

### 3.4 …and the blocker is the dictionary, not the geometry

`classify_nuclear_knot(Z, N)` is a four-branch dispatch that **factors through `A = Z + N`** —
verified over a `30 × 34` grid, assertion `classifier_depends_on_A_only`. It discards the braid
word entirely, and it has **exactly one consumer in the tree** (`hadron_knot_table.py`); it lives
in a file named `hecke_core_legacy.py`. The live binding law attaches to the braid word (a `tr_M`
ratio), a strictly finer object.

Two consequences, and the second is the useful one:

- The §3.3 exclusion is **conditional**: it excludes an Epstein–Penner invariant *of the
  dictionary-assigned knot*. An Epstein–Penner invariant of the **actual per-atom braid closure**
  is untested, and testing it would first require identifying that closure — which the corpus
  does not currently do.
- AGENTS.md flags per-case dispatch on `A` as a fitting smell in its own right ("a formula that
  branches on `A` … has one free choice per branch"). The dictionary is such a dispatch. So the
  finding here reflects on the dictionary at least as much as on the route.

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

## 5. Planck length — already answered in the corpus, both halves

Neither half of this is new; both are live content blocks found by corpus-grep path 2.

**Forbidden as an input.**
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

So `ℓ_P` may enter only as a dimensionless ratio derived from `(m_e, 𝔇_β, 𝔇_π)`; never as an
input, and never to pin the substrate. The one question here that is *not* already answered, and
that needs no new dimensional constant, is whether the fibre `S_p` is the right object to attach a
decomposition to — a question about the categorical statement above. That is a paragraph, not a
tranche, and it is left open.

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

**The one live route, and it is not a geometry problem.** To revive this, identify the actual
per-atom braid closure and ask whether *its* canonical decomposition varies with `A`. That is
blocked on the dictionary being a four-branch dispatch, and unblocking it is a modelling decision
with real consequences — the same decision bean `qou-imkb` records as blocked for Model B. Attacking
a better invariant of a knot the dispatch has already collapsed cannot help.

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
