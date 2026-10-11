---
# qou-wqto
title: 'V9: chirality grading u_L vs u_R -- no braid word distinguishes them'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-gen
    - 8f-open
created_at: 2026-08-10T18:57:48Z
updated_at: 2026-10-11T07:45:12Z
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

    content/quantum-observable-universe/nuclear-interactions/type-b-folding-cpt.md
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
