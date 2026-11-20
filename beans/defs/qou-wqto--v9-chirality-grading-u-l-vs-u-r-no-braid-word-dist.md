---
# qou-wqto
title: 'V9: chirality grading u_L vs u_R -- no braid word distinguishes them'
status: todo
pr: 8200
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-gen
    - 8f-open
created_at: 2026-08-10T18:57:48Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

Y = B - L is a statement about the LEFT-HANDED sector
(HyperchargeBatteryReduction.lean: LH is the only half with content; the RH half
is entailed by Q). But the corpus has no braid word distinguishing u_L from u_R
-- chirality is simply unrepresented. So 'the four LH rows come out right' is
currently a statement about four fermions, not about their left-handed
projections. Without a chirality grading the LH/RH split cannot be expressed at
all, and Y = B - L cannot be stated in the form the battery requires.
Note AGENTS.md 7b suggests Type B folding / symmetric crystals as the
chirality mechanism -- fixed points of the folded crystal = stable matter. That
is the natural place to look for a chirality grading.


STATUS 2026-08-15 (reorientation pass): PARTIAL, still open. PR #4961 landed
ChiralityIndependentOfCrossing.lean (sorry-free, no class/axiom/instance, so the
new proof-no-axiom-class-laundering ban is satisfied by construction):

  chirality_not_a_function_of_crossing      chirality CANNOT factor through the
                                            crossing sign -- u_L and u_R are both
                                            up quarks and share sigma_i
  braid_element_cannot_separate_gen1        one bit cannot separate 8 states
  gen1_determined_by_flavour_chirality_particle  three bits suffice
  flavour_and_particle_alone_insufficient   ...and are MINIMAL (drop chirality ->
  flavour_and_chirality_alone_insufficient      u_L collapses onto u_R)
  no_chirality_on_reeb_fixed_state          a Reeb-ODD bit admits no fixed state
                                            = archimedean-chirality's 'bosons are
                                            chirality-blind', as a theorem

That is SCOPE-(a): it establishes which datum canNOT be chirality and how many
independent bits the sector needs. It does NOT construct the chirality datum and
wires nothing. WHAT REMAINS is exactly the original ask -- build the grading. The
Reeb-involution reading (archimedean-chirality) is where it lives, NOT the
crossing sign, which V8 already spent on flavour. AGENTS.md 7b Type-B folding
remains the suggested route.


## V10 LANDED (2026-08-16, PR #5165): the grading is CONSTRUCTED

V9 was scope-(a) -- which datum canNOT be chirality, and how many bits the sector
needs. V10 answers the question V9 left open, and answers it exactly.

QOU/StandardModel/ChiralityGradingConstruction.lean (lean-direct exit 0, no
warnings; #print axioms clean on all ten decls).

### V9's one positive result was weaker than it looked

`reeb_moved_state_admits_chirality` builds `fun x => decide (x = s)`. That
satisfies the odd condition at the single pair (s, iota s) and says nothing
anywhere else. A grading has to be odd EVERYWHERE. Asking for that turns the
open item into a question with an exact answer:

  a globally iota-odd grading exists  <->  iota is FREE (no fixed point)

Necessity is V9's boson clause read globally (`free_of_reeb_odd_grading`).
Sufficiency is the construction.

### The construction

An iota-odd grading IS a choice of one element per orbit. `OrbitSection`
packages that (rep lands in the orbit; rep is constant on the orbit), and

    chirOf T s := decide (s = T.rep s)

is odd whenever iota is free. Freeness is exactly what keeps the two cases
exclusive. The section is a HYPOTHESIS -- that is where choice would enter for
an infinite state space -- so the construction itself is choice-free, and the
axiom audit confirms it: five decls depend on nothing, five on `propext` ONLY.
No Classical.choice, no Quot.sound.

### The payoff: instantiated, it IS the corpus's bit

`gen1_chirality_is_the_constructed_grading`: with `flipChirality` (u_L <-> u_R
etc.) and the transversal `repL` picking the left-handed member,
`chirOf gen1Section = chirality` -- V9's hand-written function -- pointwise on
all eight states, definitionally (cases x <;> rfl).

So this is not a parallel invention that resembles the labelling; it reproduces
it. Plus `reeb_odd_grading_unique_up_to_flip`: no section could return anything
else up to the global flip.

Also `flavour_and_particle_even_under_flip` -- the other two bits are Reeb-EVEN,
so the grading separates exactly its own datum and disturbs neither of the other
two V9 showed independent. That is what makes the three bits compatible rather
than merely distinct.

### STILL OPEN (this is scope-(a)-plus, NOT scope-(b))

The Reeb involution on the PHYSICAL state space is not identified. That is CR
geometry, and archimedean-chirality.md asserts rather than derives it. Every
theorem here is conditional on iota being whatever involution the Reeb field
induces; they say what follows ONCE it is one. Nothing is wired to compute and
no observable is predicted. The SM labels still enter as the target to be
reproduced, never as derived output.

Type-B folding (AGENTS.md 7b) remains untried -- it would be the route to
DERIVING the involution rather than taking it as given.

So: 'the mechanism has the right shape' -> 'here is the grading, here is exactly
when it exists, and it is the corpus's one'. Open on the geometric
identification.

## V11 (2026-08-16): Type-B folding is NOT untried — and its own reading blocks it

This bean said twice that "Type-B folding (AGENTS.md §7b) remains untried". The
corpus-grep checklist says to check before declaring an item open, and doing so
here changes the answer. Type-B folding is already in the corpus:

    folio/quantum-observable-universe/nuclear-interactions/type-b-folding-cpt.md
    (+ .ts, .lean, .qa.json)

`conj:type-b-folding-closure` states the folding with the involution
`ι : α_i ↔ α_{n-i}` on the sl_n Cartan datum, and adds the clause that decides
the matter:

  > Stable matter = fixed points of the folded crystal; antimatter = the
  > ι-orbit complement.

That collides with V10's existence criterion, and the collision is a theorem,
not a preference. V10's `free_of_reeb_odd_grading` says a GLOBALLY ι-odd grading
forces ι to have NO fixed point. The folding conjecture puts stable matter
exactly AT the fixed points. One involution cannot do both.

### Formalized: QOU/StandardModel/TypeBFoldingChiralityObstruction.lean

lean-direct exit 0, no warnings. `#print axioms` on all four: "does not depend
on any axioms" (not even propext). No sorry, no axiom, no native_decide.

  stable_matter_and_global_chirality_incompatible
      the bare dilemma: no ι both fixes a state and carries a global odd grading
  no_state_chirality_of_folding_fixed_point
      the obstruction TRANSFERS along any intertwiner π (π ∘ foldι = stateι ∘ π).
      One fixed point upstairs kills the grading downstairs. π need be neither
      injective nor surjective — one point carries it.
  global_chirality_forces_no_fixed_matter
      contrapositive, the usable form
  folding_inducing_gen1_chirality_is_free
      instantiated: flipChirality is PROVED free (V10, by decide on 8 states),
      so any folding inducing it is itself fixed-point free — no stable matter
      in the conjecture's sense

The last one is the sharp form: the separation is not hypothetical. The corpus
already carries a chirality involution whose fixed-point structure is proved,
and it is the OPPOSITE of the folding conjecture's.

### Scope — (a), deliberately, per the refuted/ruled-out discipline

EXCLUDED: the Type-B folding involution, read as the conjecture reads it
(fixed points = stable matter), cannot itself be the chirality involution.
Backed by a proved fixed-point/parity invariant, so structural FOR THAT
IDENTIFICATION.

NOT EXCLUDED — do not read this as killing the route: folding keeps every other
role the conjecture gives it (bar-invariance of GS normal forms, the C/P/T
decomposition, the crystal structure). Folding may still CONTAIN the chirality
datum — via an orbit map, a sub-crystal, or a SECOND involution on the folded
object — just not by its own fixed-point involution serving directly as ι.

### What this does to the search

The bean pointed at Type-B folding as "the natural place to look". That pointer
is now narrowed, not removed: whatever supplies ι must be fixed-point free on
the physical states, so it is NOT the folding's matter/antimatter involution.
Anyone resuming should look for a free involution on the folded object (or an
orbit-level map), and should NOT try to read chirality off the matter-fixing ι.

Still open, unchanged: the geometric identification of the Reeb involution on
the physical state space (CR geometry; archimedean-chirality asserts rather than
derives it). Nothing here is wired to compute and no observable is predicted.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


---

## 🛑 THIS BEAN'S TITLE IS STALE AGAINST ITS OWN BODY — and I repeated it four times before reading it (2026-10-11)

The title says *"no braid word distinguishes them"*. That is **V9's framing from
2026-08-10**. The body already records V10 (2026-08-16) **constructing** the
grading and V11 **excluding** Type-B folding from that role. I propagated the
title into four artifacts without opening the body:

- the `qou-h0zz` append of 2026-10-10 ("chirality is untouched");
- issue **#7711**, §"What stays open";
- PR **#7712** body, §"What this does NOT change";
- three chat reports naming `wqto` as the next item in those terms.

**This is the second instance in two days of one pattern**, and that makes it a
pattern rather than a slip. The first was `htw2`, whose correction is appended
to `qou-h0zz` and whose lesson I wrote into the epic `qou-8lxd` — *"read the
beans a bean cites AND the beans that cite it"* — and then did not apply here.

**The sharper diagnosis, which the `htw2` note did not reach.** Both failures
came from reading a bean's **title out of a listing**, where the body is not
visible. `beans list` and the session-start sweep print title + status and
nothing else, so a front's "open items" read as their titles by default. The
`htw2` note blamed its `scrapped` status; that was only half of it — `wqto` is
`todo` and failed identically. **The common cause is the listing, not the
status.** Treat any claim about a bean sourced from a listing as unverified
until its body is read.

### Verification of what the body claims (measured, not carried)

All three carriers, `lean -DautoImplicit=false -s 65536`, exit status captured
directly:

    ChiralityIndependentOfCrossing.lean    rc=0  0 diagnostics  228 lines  11 decls
    ChiralityGradingConstruction.lean      rc=0  0 diagnostics  295 lines  16 decls
    TypeBFoldingChiralityObstruction.lean  rc=0  0 diagnostics  135 lines   5 decls

0 `axiom`, 0 `native_decide` in all three. Six key declarations resolve by
name: `chirOf`, `free_of_reeb_odd_grading`,
`gen1_chirality_is_the_constructed_grading`,
`reeb_odd_grading_unique_up_to_flip`,
`stable_matter_and_global_chirality_incompatible`,
`folding_inducing_gen1_chirality_is_free`.

**One apparent discrepancy, resolved.** `grep -c '\bsorry\b'` on
`ChiralityIndependentOfCrossing.lean` returns **1**, against this bean's claim
that it is sorry-free. The match is the module docstring heading
`## What is proved (all sorry-free)` — the word inside prose asserting the
opposite. The bean is right and the grep is not.

That is the **third** instance of this false positive in one session and the
**second in a corpus file** (the other being a docstring I had just written
myself). So: **`grep -c '\bsorry\b'` is not a usable gate in this tree.** The
honest signals are `rc=0` with no `declaration uses 'sorry'` warning — Lean
emits one for every real `sorry` — or a grep that excludes comment and
docstring regions.

### The open item, scoped correctly

Not the title's question. What remains is **the geometric identification of the
Reeb involution on the physical state space** — CR geometry. Its only corpus
statement is
[`brings-surface/archimedean-chirality.md`](../folio/quantum-observable-universe/brings-surface/archimedean-chirality.md),
which is a **single paragraph, one line of file**: the Reeb field `ξ` carries a
natural orientation, `Θ(ξ) = 1` picks a direction, and *"chirality is encoded in
the ±-eigenspaces of the Reeb involution `ξ ↦ −ξ`"*. It **asserts** the
involution; nothing derives it, and the whole V10/V11 tower is conditional on
`ι` being whatever that involution induces.

V11's constraint narrows the search and should be carried by anyone resuming:
`ι` must be **fixed-point free on the physical states**, so it is **not** the
Type-B folding's matter/antimatter involution (which fixes stable matter by
construction). Look for a free involution on the folded object, or an
orbit-level map.

### A point I checked and am NOT claiming as new

The obvious next thought is that the grading's domain must **exclude bosons** —
`archimedean-chirality` says bosons are purely horizontal hence chirality-blind,
i.e. Reeb-fixed, and V10 needs `ι` free, so the domain on which `ι` must be free
is the fermionic sector. **The corpus already has this.**
`ChiralityIndependentOfCrossing.no_chirality_on_reeb_fixed_state:209` states
exactly it — an odd chirality admits no fixed state — and its own docstring
names the boson clause as the physical reading. V10's
`free_of_reeb_odd_grading` is the global form. Recorded as checked-and-not-new
rather than offered as a finding.

### Nothing closed, nothing wired

No conjecture closes, no observable is predicted, no witness or dashboard row
moves. The SM labels still enter as the target to be reproduced. Per rule 13a
this bean stays `todo`.


---

## Measured: the involution is PARAMETERISED, never instantiated — and the corpus already holds a candidate (2026-10-11)

The scoping question from the previous append was whether the open item is
*instantiate an existing object* or *build one from CR geometry*. Measured: it is
**instantiate**, and the candidate was already on disk, unremarked.

### The gap is an instantiation gap

V10's `ChiralityGradingConstruction.lean` quantifies over `reeb : State → State`
and `free_of_reeb_odd_grading` is a statement *about* such a map. **Nothing in
the corpus instantiates it.** Searched every `def`/`abbrev` whose name contains
`reeb` (case-insensitive) across `folio/**/*.lean` excluding `.lake`: twelve
hits, none of them an involution on a state space. They are a period
(`reebPeriod`), vector fields (`qReebVectorField` ×2), a flow sector, a spectrum
example, a bundle-complement predicate, a horizontality predicate
(`ReebDecomposition.isPurelyHorizontal`), a divisor predicate, a weight-
decomposition constructor — and the three **Reeb operators** on the Bring cone.

### The candidate: the SQUARE of a Reeb operator IS negation

`QOU/BringCone.lean` defines `BringCone R := Quaternion R` and
`reebM_i p := p * ⟨0,1,0,0⟩`, right-multiplication by a quaternionic unit. Those
operators have **order four**, and their square is negation:

    reebM_i (reebM_i p) = p · i · i = p · (−1) = −p

which is *literally* the `ξ ↦ −ξ` that
[`brings-surface/archimedean-chirality.md`](../folio/quantum-observable-universe/brings-surface/archimedean-chirality.md)
names — and that block is one paragraph, one line of file, asserting it.

Hand-verified independently in exact rationals before writing any Lean, on
`p = (2,3,5,7)`: all three squares return `(−2,−3,−5,−7) = −p`, and
`reebM_i⁴ p = p`. So `reebM_i` itself is **not** the involution; its square is.

**And negation satisfies V10's criterion where it matters.** `−p = p` iff
`p + p = 0`, so on a cone where `2` is cancellable the only fixed point is the
origin — negation is **fixed-point free on the punctured cone**, which is
exactly the hypothesis `free_of_reeb_odd_grading` needs. V11's constraint (the
involution must be free, so it is *not* the Type-B folding's matter-fixing one)
is met by construction rather than by assumption.

### Lean added to `QOU/BringCone.lean` (additive)

| decl | statement |
|---|---|
| `reebM_i_sq` / `reebM_j_sq` / `reebM_k_sq` | `reebM_x (reebM_x p) = -p` |
| `reebM_i_quartic` | `reebM_i⁴ = id` — order four, so `M_i` is not itself the involution |
| `neg_involutive_cone` | `-(-p) = p` |
| `neg_fixed_iff_add_self_eq_zero` | `-p = p ↔ p + p = 0` |
| `neg_free_of_ne_zero` | `2` cancellable on the cone + `p ≠ 0` ⟹ `-p ≠ p` |

Over generic `{R : Type*} [CommRing R]` per §7c — pure ring identities, no
ordering, no `Real`, no new import. The cancellation hypothesis is explicit
rather than a typeclass for the same reason; it holds in any `R` of
characteristic `≠ 2` without zero divisors, so in `ℝ` for the archimedean
specialisation.

### Corpus-grep before writing

`reebM_i (reebM_i`, `reebM_i ∘ reebM_i`, `reeb_square`, `reebM_sq`: **0 hits**.
Negation-as-an-involution on the cone: **0 hits** — the `bar-involution.lean`
and `spin-involution.lean` matches are a different statement (`bar(−x) =
−bar(x)`, that an involution *commutes* with negation, not that negation *is*
one). `BringCone.lean` held exactly four declarations before this: the abbrev,
the three operators, and the three twist identities.

### 🛑 THIS IS A CANDIDATE, NOT A DERIVATION — the gap, named

Proved: the **algebra**. That each Reeb operator squares to negation, that
negation is involutive, and exactly when it is free.

**Not** proved, and not proved anywhere in the corpus:

1. that the **Bring cone is the physical state space** — the cone is a
   quaternionic model of the contact link, and V10's `State` is the eight-element
   gen-1 label set in its instantiation; no map between them exists;
2. that the involution the **Reeb field induces on physical states** is this
   negation. `archimedean-chirality` asserts the eigenspace reading in one
   paragraph; nothing derives it.

So this narrows the open item from *"identify an involution"* to *"show the
asserted Reeb involution on states is the cone's negation, or exhibit the map
that transports one to the other"* — a smaller and better-posed question, with
the first concrete object to aim at. The whole V10/V11 tower stays conditional
on step 2. Nothing is wired, no observable is predicted, and
`conj:sm-hypercharge-invariant` stays open; per rule 13a this bean stays `todo`.

---

## 2026-10-12 — negation is trivial on states; the Reeb operator itself has V10's shape (owner request "1 2")

**Correction of the previous append.** `reebM_x² = −id` cannot be V10's `ι` on **states**. A state is a ray, and `−p = (−1)•p` (`neg_eq_unit_smul`), so negation fixes every state. `neg_free_of_ne_zero` is about vectors.

**What does work, on the quaternionic model** (Lean in `QOU/BringCone.lean`, generic `[CommRing R]`):
- `Γ p := i·p·i` combines left multiplication by `i` with `M_i`.
- `Γ² = id` (`chiralGamma_sq`), and `Γ = −1` on span(1, i), `+1` on span(j, k) (`chiralGamma_apply`).
- `M_i` commutes with `Γ`, and **`M_j` anticommutes** (`chiralGamma_anticomm_reebM_j`), so it swaps the eigenspaces (`reebM_j_flips_eigen`).
- `M_j` has no eigen-ray unless `c² + 1 = 0` (`reebM_j_ray_free`).

So on rays, `M_j` is a fixed-point-free involution that flips `chir := Γ`, which is V10's shape on states, with `ι` the Reeb operator itself, not its square.

Verification: lean-direct (`-DautoImplicit=false -s 65536`) exit 0 on BringCone and on its dependent BringConeSplit, the latter compiled against the new BringCone olean. `#print axioms` on all 7 new declarations gives `[propext, Quot.sound]`.

**Krasnov (`library/arxiv-2104.01786v1`), read for the octonion question.** One generation is `S₊ = 𝕆 ⊗ 𝕆̃`, with two commuting complex structures:
- Lorentz handedness = `±i` split of `J̃` on the split octonions (§3.4).
- **Weak L vs R** (`SU(2)_L` vs `SU(2)_R` doublets, which is what `u_L` vs `u_R` means here) = `±i` split of `J = E⁴` on the **ordinary** octonions `𝕆` (§6.1: (1,0) = L ⊕ Q is (2,1), (0,1) = L̄ ⊕ Q̄ is (1,2)), and the map between them is conjugation relative to `J`.
- So in that model `u_L`/`u_R` lives on the octonions that also carry colour (`OctonionComplexStructure.lean`, `Le_sq_eq_neg_id`).
- V10's eight labels {u,d}×{L,R}×{particle,anti} are **not** the octonion's 8 (= 1 lepton + 3 colours, complex).

**Still open (rule 13a, stays `todo`):**
1. Nothing attaches `L_i` to the Reeb field.
2. `BringCone` is the Hopf model, not Bring's cone (`qou-rydq`).
3. There is no map from the `Gen1Quark` labels into these rays.

Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB

## 2026-10-12 — gap 1 narrowed: L_i is forced into the commutant of the Reeb triad (issue #7774)

Lean in `QOU/BringCone.lean` (generic `CommRing`, lean-direct exit 0, axioms propext + Quot.sound):
- `leftMul_comm_reebM_{i,j,k}`: left multiplications commute with every Reeb operator.
- `commutes_reeb_triad_iff_leftMul`: an R-linear map commuting with M_i, M_j, M_k is left multiplication by f(1).

So the operators commuting with the Reeb triad are exactly the left multiplications. The second complex structure in Γ = J·J′, if it commutes with the Reeb field, must be some L_u; the remaining freedom is the unit u, not the kind of map. This is the quaternionic shadow of Krasnov's two commuting complex structures.

Still open (rule 13a, stays `todo`):
1. Which u. The commutant does not pick one.
2. Bring's own cone versus the Hopf model (`qou-rydq`).
3. A map from V10's eight `Gen1Quark` labels into the rays.

Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB

## 2026-10-13 — which unit `u`: the shape is forced, the point is not (STOP per owner ordering)

Owner's ordering, relayed: fix `u` from structure only, before testing anything about chirality; if nothing forces `u`, stop and do not move on to Bring's own cone or the `Gen1Quark` → rays map. **Nothing forces `u`, so this tranche stops at (a).**

Lean added to `QOU/BringCone.lean` (generic `CommRing`, sorry-free, lean-direct `-DautoImplicit=false -s 65536` exit 0 on it and on its dependent `BringConeSplit`; axioms ⊆ propext / Classical.choice / Quot.sound on all 21):

| what | declaration |
|---|---|
| `L_u` is a complex structure iff `u·u = −1` | `leftMul_complex_iff` |
| for pure `u`: iff `normSq u = 1` | `sq_eq_neg_one_iff_normSq_of_pure` |
| over a domain, `2 ≠ 0`, `−1` not a square (e.g. ℝ): every root of `−1` is pure | `re_eq_zero_of_sq_eq_neg_one` |
| `Γ_u := L_u ∘ M_i` is a grading for every such `u` | `chiralGammaU_sq` |
| for EVERY `u`: `M_i` commutes, `M_j`, `M_k` anticommute with `Γ_u` | `chiralGammaU_comm_reebM_i`, `_anticomm_reebM_j`, `_anticomm_reebM_k` |
| `L_{1−vu}` (commutes with the triad) carries `Γ_u` to `Γ_v` | `intertwiner_mul`, `leftMul_intertwines_chiralGammaU` |
| `L_{q̄} ∘ L_q = normSq q •`, `normSq(1−vu) = 2(1+u·v)` | `leftMul_star_leftMul`, `normSq_intertwiner` |
| `Γ_{−u} = −Γ_u` (the global L↔R flip) | `chiralGammaU_neg` |
| radial unit `p` is a `Γ_u = −1` eigenvector iff `u = p·i·p̄` (Hopf image; pure, norm `normSq p²`) | `chiralGammaU_eigen_iff`, `re_hopf`, `normSq_hopf` |

**Forced:** `u` is a pure unit quaternion (a point of `S²`). Over a ring where `−1` is a square (ℂ) the scalar `√−1` also qualifies; excluded by hypothesis, not hidden.

**Free, exactly:** one point `u ∈ S²` of pure units.
- No condition relating `Γ_u` to the Reeb triad distinguishes points: all commutation relations hold for every `u`.
- Any two points with `1 + u·v` invertible (times 2) are conjugate by `L_{1−vu}`, an automorphism commuting with the whole triad. Antipodal points are related by the sign `Γ_{−u} = −Γ_u`, which only relabels L↔R (V10's `reeb_odd_grading_unique_up_to_flip`).
- The one thing that does pick `u` is a base point: requiring a chosen radial direction `p` to be a chirality eigenvector gives `u = p·i·p̄`, the Hopf projection of `p`. That is choosing a point of the Hopf base, not deriving one.

So on the model cone the choice of `u` is inessential up to triad-commuting automorphisms plus the orientation sign — but it is still a choice, and nothing in the corpus makes it. Corpus-grep for a selecting structure (Lean: `leftMul`, `second complex structure`, `pure unit quaternion`, Hopf map; `docs/`, `beans/defs/`, `library/INDEX.md`, `library/*/ocr` for 3-Sasakian / quaternionic structure): no hit that selects a unit. That is a statement about those surfaces, not a proof that no selecting structure could exist.

**Not attempted, by the owner's ordering:** (b) moving the Reeb involution onto Bring's own cone (link `UT(Σ₄)`, `qou-rydq`), and (c) a `Gen1Quark` → rays map. Note for whoever picks up (b): on Bring's cone the analogue of "a point of the Hopf base" would be a point (or section) over `Σ₄`, and the Euler number −6 of the link fibration (vs −1 for Hopf) is the known obstruction to a global quaternionic triad there.

Stays `todo` (rule 13a).

Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB

---

## 2026-11-15 — owner ruling (option 1): `u` is a gauge choice; then (b) and (c) — PR #7820

**(a) Covariance.** `QOU/BringConeGauge.lean`, generic `[CommRing R]`:
- `exists_triad_equiv_conj_chiralGammaU`: let `u`, `v` be pure units, and suppose either `IsUnit (2(1+u·v))` or (`v = −u` and some pure `w ⊥ u` has unit norm). Then a linear automorphism `e` exists that commutes with `M_i, M_j, M_k` and satisfies `e ∘ Γ_u = Γ_v ∘ e`. The intertwiners are `L_{1−vu}` and `L_w`.
- `exists_triad_equiv_conj_chiralGammaU_ordered`: the same with **no extra hypothesis** over a linearly ordered field (ℝ). WLOG `u = i` holds there.
- `TriadGauge.eigen_iff` transports eigenvectors and eigenvalues. Every Γ-statement in BringCone.lean therefore holds for all admissible `u`. `reebM_{j,k}_flips_eigenU` and `reebM_i_preserves_eigenU` give the `u`-generic flips.
- **NOT covariant:** `isUnit_two_of_triadGauge_i_j` shows that a triad gauge `Γ_i → Γ_j` forces `IsUnit 2`. Over ℤ the choice of `u` is not a gauge choice. `chiralGamma_apply` (coordinates) holds only in the gauge `u = i`.

**(b) Bring's own cone.** `QOU/BringConeSplitChirality.lean`, split model `M₂(R)`, the sl₂ triad of `UT(Σ₄)`:
- `M_j² = M_k² = id`. `M_j` fixes `1+j` (`M_j_not_ray_free`), so the Hopf flip `ι = M_j` fails here (V10 necessity).
- `M_i` (fibre rotation) is the only ray-free Reeb operator (`M_i_ray_free`). It anticommutes with `M_j`, and `M_j` is itself a grading. That gives V10's shape from the triad alone.
- `commutes_span_scalar`: if `L_u` commutes with a set whose span contains `i, j`, then `u` is scalar. So `L_u` does not descend to `SL₂/Γ₄`.
- GAP 1: the spanning of `Γ₄` (Borel density) is a hypothesis; it is not in the corpus or the library.
- GAP 2: on points of the link only `M_i` acts (norm +1); `M_j` and `M_k` are module operators. Which object the states are (rays, points of `UT(Σ₄)`, sections) is not fixed. Bean `qou-pu2x`.

**(c) Gen1Quark → rays.** `QOU/StandardModel/Gen1QuarkRays.lean`:
- `no_vector_equivariant_map`: the flip matches `M_j` only projectively.
- `gen1Ray seed`: L goes to `Γ_u=−1` and R to `+1` (`gen1Ray_gamma`); the flip becomes `±M_j` (`gen1Ray_flip`); only the 4 left-handed values are free (`gen1Ray_unique`).
- particle↔anti cannot be `M_j` or `M_k` (`reebM_{j,k}_not_chirality_preserving`).
- **Flavour (and particle placement) are the free `seed`.** The constant seed collapses `uL`/`dL` (`constSeed_collapses_flavour`).

Lean-direct `-DautoImplicit=false -s 65536` exit 0 with 0 warnings on all three files and on `BringConeSplit`. `#print axioms` on all 38 new declarations ⊆ {propext, Classical.choice, Quot.sound}.

Stays `todo` (rule 13a). The physical identification of the Reeb involution on states is still open.

Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB

## 2026-11-15 — does Bring's S₅ single out `u`? No (owner ruling, option 2; PR #7818)

Preregistered before measuring: `docs/audits/2026-11-15-bring-s5-distinguished-unit-preregistration.md` (commit `5b76d41e08`; results in §5, rules unchanged).

- **Action leg — outcome (iii).** The corpus has no action of Bring's `S₅` or `A₅` on the model cone or its admissible units. Its `A₅`'s act on Klein's `ℙ(V)` and on `Σ₄`; the `S²` of `u` is the Hopf base of the model (`qou-rydq`). `S₅` has no faithful real 3-dim rep, so only `A₅` could act, and its two icosahedral embeddings (Galois `√5 ↦ −√5`, measured to have different characters) are swapped by `S₅`'s odd coset.
- **Assuming the action through `2I` by left multiplication** (the only triad-respecting linear shape): it acts on `u` by conjugation (`leftMul_conj_chiralGammaU`). No `u` is fixed (R0 empty; Lean via `i, j ∈ 2I`, and exact compute). The maximal-stabiliser rule picks one orbit: the **12 vertex directions** (6 axes, stabiliser `C₅`); the other exceptional orbits are 20 (`C₃`) and 30 (`C₂`).
- **And it cannot fix a handedness.** Each exceptional orbit contains `−u` for every `u` (moved there by 5 / 3 / 2 perpendicular half-turns), and `leftMul_flips_chiralGammaU` shows such a half-turn carries `Γ_u` to `−Γ_u`. So the `A₅` symmetry identifies L with R. The orbit also moves with the placement of `2I` inside the unit quaternions, which the triad does not fix.

Lean: `QOU/BringConeIcosahedral.lean`, 7 decls, sorry-free, lean-direct (`-DautoImplicit=false -s 65536`) exit 0, axioms ⊆ propext / Classical.choice / Quot.sound. Probe: `computations/probes/bring_cone_icosahedral_unit_orbits_probe.py` (exact ℚ(√5), 12/12). Gap opened as `qou-b5ic`. Stays `todo` (rule 13a).

Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB

## Progress (2026-11-16, PR #8200)
- [x] Formalized `Gen1ChiralState`, `flipStateChirality`, `stateChiralitySign`, `dropChiralityBit`, and `gen1_chirality_involution_and_projection_collapse` in `folio/quantum-observable-universe/lean/QOU/Eightfold/TauAnchoredRatioChiralBraidWritheAndSpectralCubicPowerSums.lean` + 50-dps mpmath witness (`qou_wqto_gen1_chirality_involution_and_projection_collapse`) in PR #8200 (`ec7070e7f1b47f4548cd7f98fc2a7948b28854b0`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8200, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
