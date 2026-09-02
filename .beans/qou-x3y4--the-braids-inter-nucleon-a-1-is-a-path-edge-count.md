---
# qou-x3y4
title: The braid's inter-nucleon A-1 is a PATH edge count, not the coordination degree z=A-1
status: completed
type: task
priority: normal
created_at: 2026-08-30T19:49:52Z
updated_at: 2026-08-30T19:51:34Z
---

RESOLVED 2026-08-30 (PR #6313) as a scope-(a) NEGATIVE, with an exact
arithmetic exclusion proved sorry-free.

QUESTION. bk-coordination-multiplicity.md reads the many-body multiplicity off
AME2020 (M_need = B_AME/(m_e*Vol_A) gives 2.003 for 3H and 2.061 for 3He
against z = A-1 = 2) and identifies it with the PER-NUCLEON COORDINATION
NUMBER -- "the number of nucleon-nucleon bonds incident to one nucleon in the
fully coordinated cluster". A read-off is not a derivation. Toggling
include_inter on atom_braid_word_3A gives exactly A-1 inter-nucleon letters,
the same integer. Can the braid DERIVE the multiplicity?

ANSWER: no. The two A-1s are different objects.

MEASURED (computations/probes/braid_inter_nucleon_adjacency_probe.py, exit 0,
6/6 checks; adjacency DERIVED from generator indices -- nucleon = strand//3,
sigma_g joins g//3 and (g+1)//3, so g is inter iff g % 3 == 2 -- not read off
the emission loop):

    A                    2   3   4   6   8  12  16
    inter-crossings      1   2   3   5   7  11  15   = A-1
    distinct bonds       1   2   3   5   7  11  15   = A-1
    max nucleon degree   1   2   2   2   2   2   2   = min(2, A-1)
    K_A degree z=A-1     1   2   3   5   7  11  15
    K_A edges C(A,2)     1   3   6  15  28  66 120

The bond set is the PATH GRAPH P_A: {(k,k+1)}, degrees [1,2,...,2,1].

WHY NO MEASUREMENT COULD HAVE SETTLED IT. |E(P_A)| = A-1 is an EDGE count;
deg_K_A(v) = A-1 is a VERTEX DEGREE. They are the SAME AFFINE FUNCTION OF A, so
no value of A separates them and a table of matching rows is not evidence. The
separation is arity: an extensive total read as an intensive per-nucleon
degree (da-arity-conflation).

PROVED, sorry-free, lean-direct exit 0, #print axioms clean on all 11 decls
(propext / Classical.choice / Quot.sound, no sorryAx):
QOU/MassTheory/BraidPathNotCoordination.lean.

  handshake_forces_le_two -- the decisive one, and it needs nothing about the
  braid's shape beyond its edge count. Feed the handshake A*z = 2*|E| the
  braid's |E| = A-1 and the block's z = A-1:  A*(A-1) = 2*(A-1), hence A <= 2.
  So the identification is IMPOSSIBLE for every A >= 3, not merely
  unsupported -- proved for all A where the probe measured eight.

  card_bonds_eq_choose_two_iff -- P_A = K_A iff A <= 2. The deuteron is the
  ONLY nucleus whose braid bond set is the fully coordinated cluster. Note the
  slots part company at different places: the DEGREE slot agrees for A <= 3
  (exactly the two rows the block calibrates on), but BOTH slots only at A = 2,
  since |E(P_3)| = 2 against C(3,2) = 3.

  degree_le_two -- DERIVED from the measured bond set, not posited as a closed
  form. With two_lt_coordination_degree: at A >= 4 no nucleon reaches z.

THREE QUANTITIES IN THIS CORPUS ARE WRITTEN A-1 (the finding worth carrying):
  (i)   bk_crossing_coordination.py:106  def z_coord(A): return A - 1
        -- a PYTHON LITERAL in A alone. B_K does NOT enter it, so z is
        identical for 3H (8_11) and 3He (L6a4). The block's title,
        "the coordination number of B_K", invites reading z as derived from
        the link; it is not. Consistent with the block's own text -- the
        link-dependence lives entirely in Vol, which carries the mirror split.
  (ii)  deg_K_A(v) = A-1, Mass.CoordinationBinding.coordination_degree.
  (iii) the braid's path edge count.
Recorded as an authorNotes caveat on the block (kind: caveat, 2026-08-30).

TWO OBJECTS MUST BE KEPT APART. B_K is the CENSUS LINK (8_11, L6a4) whose
volume carries isospin; the include_inter count belongs to the 3A-STRAND WORD.
atom_braid_word_3A's own docstring forbids reading any topological quantity off
that word -- its averaged letters lie outside the image of rho: B_n -> H_n(q),
so it is a Hecke element, not a braid. The probe reads NO invariant: it records
which STRAND PAIRS each letter acts on, well defined either way. That sharpens
the verdict -- A-1 is not a "topological reading" of anything.

m_pp / m_pn / m_nn. They repeat the SAME crossing at the SAME generator m
times: per-bond-type crossing multiplicities, ALL DEFAULTED TO 1 BY FIAT.
Grepped: NO live producer sets any of them != 1 -- every non-default call site
is a pass-through (qou-mass/_internal mirror, pyhecke) or under
computations/_deprecated/, which includes atom_knot_search.py, a SHELVED
SEARCH over m_* values. Untouched here. qou-h7mh's warning stands verbatim:
"DO NOT JUST FIT m_*. Tuning them to reproduce 2.15 buys a good table and
costs the parameter-free claim."

SCOPE. (a) for the physics: THIS CONSTRUCTION, ALONE, does not derive the
coordination multiplicity. It does NOT exclude the bond picture and does not
touch the Vol leg. The exclusion proved is the exact arithmetic one in
handshake_forces_le_two, invariant named (the handshake identity).

RELATION TO THE NEIGHBOURS.
  * qou-m07y (completed) excluded the linear CHAIN scope-(b) at q != 1
    (orderIndependent_iff + InterfaceScalar.charge_independence_iff). This bean
    is the complementary half: qou-m07y says the chain is not well defined as a
    binding functional; this says its COUNT was never the coordination degree
    in the first place. Together: the bond set is a path, the path's count is
    not a degree, and the path is not well defined at the substrate.
  * qou-h7mh (todo) is the repair site -- change the BOND SET. The negative
    here tells it not to look for the coordination degree inside the existing
    word.
  * Mass.CoordinationSaturation: the braid's mean degree 2(A-1)/A -> 2 is
    BOUNDED (constant B/A), the complete graph gives the unbounded
    B/A = eps(A-1)/2, which observed saturation refutes. So the braid's graph
    has the RIGHT saturation behaviour and the WRONG multiplicity -- worth
    noting for whoever attacks qou-h7mh.

STILL OPEN (not claimed here): whether any derived bond set reproduces
M_need's A-dependence without a fitted constant. That is qou-h7mh / qou-v0yw.
