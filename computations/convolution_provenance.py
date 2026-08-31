#!/usr/bin/env python3
"""The q-convolution realisation, as a single source of truth for witnesses.

Owner directive 2026-08-30: the knot-operator realisation of the convolution
"should be recorded in the SDP solution when doing the generative production
of isotopes." Generative production composes nucleon normal forms, and that
composition IS an instance of the q-convolution — so every producer that
builds an atom NF and then solves an operator-selection LP/SDP should stamp
its witness with what the convolution *is* and how it was realised.

This module exists so that record has ONE home. A block copied into six
producers decays exactly the way a hand-maintained count does; imported, it
cannot drift.

WHAT THE CONVOLUTION IS, from the corpus rather than from inference:

  * `prop:categorical-fourier-transform-exists` — for the ground ring
    R_q = Z[q, q^-1], the Peter-Weyl decomposition yields a categorical
    Fourier transform F, a monoidal functor intertwining the **q-convolution**
    with the **pointwise product** on irreducible components.
  * `def:categorical-laplace-transform` — L likewise intertwines q-convolution
    with pointwise product, "uniquely characterising it as the mate of the
    comultiplication Delta_q on H_q". That is the sharpest identification the
    corpus makes: the convolution is the Delta_q-mate.
  * `q-resolvent` works "in the convolution algebra H_q".

On characters the Delta_q-mate is the tensor product of Specht modules, i.e.
**Littlewood-Richardson fusion** — the same operation
`conj:diagrammatic-double-magic-lr-fusion` conjectures is *rigid*
(multiplicity one, single self-conjugate nu) at doubly-magic (Z, N). The
convolution and the magic-number conjecture are therefore the same object
viewed from two sides, which is why stamping it here is worth doing.

WHAT IS NOT KNOWN. Which **knot operation** realises this convolution --
connected sum, satellite, cabling -- is not identified by any block found in
the corpus. Recorded as OPEN rather than absent: the search was a keyword
grep for "convolution" over `content/` and `computations/` plus a read of the
hits, which is a narrow surface and not a proof of absence.
"""

#: Stamp this into any witness whose producer composes nucleon NFs and then
#: solves an operator-selection LP/SDP:  ``w.add_data("convolution", CONVOLUTION)``
CONVOLUTION = {
    "operator": "q-convolution = mate of the comultiplication Delta_q on H_q",
    "corpus_refs": [
        "prop:categorical-fourier-transform-exists",
        "def:categorical-laplace-transform",
        "def:q-resolvent",
        "conj:diagrammatic-double-magic-lr-fusion",
    ],
    "character_level_realisation":
        "tensor product of Specht modules, i.e. Littlewood-Richardson fusion; "
        "F and L intertwine it with the pointwise product on irreducibles",
    "braid_level_realisation": {
        "per_nucleon_B3": "3 x (sigma_0, sigma_1^-1)  [confinement]",
        "quark_proton":
            "uu -> sigma_0 ; ud -> sigma_0 mixed (-h/2) ; ud -> sigma_1 mixed (-h/2)",
        "quark_neutron":
            "ud -> sigma_0 mixed (-h/2) ; ud -> sigma_0 mixed (-h/2) ; "
            "dd -> sigma_1^-1 (-h)",
        "gluon": "2 x sigma_0 per nucleon",
        "inter_nucleon_pp": "sigma_0        (c=1, d=0)     EM repulsion",
        "inter_nucleon_nn": "sigma_0^-1     (c=1, d=-h)    nuclear attraction",
        "inter_nucleon_pn": "colour-weighted (c=1, d=D_PN)  mixed nuclear",
        "electron_pe": "sigma_1^-1 per electron (EM channel)",
        "which_part_is_the_convolution":
            "the inter-nucleon double loop over all previously placed nucleons; "
            "the per-nucleon block builds the factor being convolved",
    },
    "knot_operator_identification": "UNRESOLVED",
    "knot_operator_candidates": ["connected sum", "satellite", "cabling"],
    "knot_operator_status":
        "No content block identifies which knot operation realises this "
        "convolution. The Fourier / Laplace / resolvent blocks name the "
        "algebraic operator (the Delta_q-mate) but not its knot-diagram "
        "counterpart. OPEN, not absent: the search surface was a keyword grep "
        "over content/ and computations/ plus a read of the hits.",
    "bean": "qou-mgq3",
}
