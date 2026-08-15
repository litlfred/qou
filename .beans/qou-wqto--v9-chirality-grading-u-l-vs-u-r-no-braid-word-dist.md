---
# qou-wqto
title: 'V9: chirality grading u_L vs u_R -- no braid word distinguishes them'
status: todo
type: task
priority: normal
created_at: 2026-08-10T18:57:48Z
updated_at: 2026-08-15T22:32:24Z
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
