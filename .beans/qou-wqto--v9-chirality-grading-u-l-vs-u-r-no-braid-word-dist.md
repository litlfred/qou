---
# qou-wqto
title: 'V9: chirality grading u_L vs u_R -- no braid word distinguishes them'
status: in-progress
type: task
priority: normal
created_at: 2026-08-10T18:57:48Z
updated_at: 2026-08-16T02:43:04Z
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
