---
# qou-bdpo
title: 'DECISION: discharge the alg-geom opaque BlochWignerD with the corpus''s concrete BlochWigner_lob'
status: completed
type: task
priority: normal
created_at: 2026-09-04T09:05:59Z
updated_at: 2026-09-05T05:49:04Z
---

OPEN, for the author. Now that BlochWignerD is typed UpperHalfPlane -> R (qou-rj44), the opaque can be discharged as

    noncomputable def BlochWignerD (z : H) : R := QOU.Archimedean.BlochWigner_lob (z : C)

turning a permanent black box into a definition the corpus already owns. Under the OLD R -> R typing this was impossible: any such wiring hit BlochWigner_lob_ofReal and forced volume = 0.

WHAT IT BUYS. The class stops being conditional on an uninterpreted symbol. It is non-vacuous: 3*D(y_+) = Vol(5_2) at the 5_2 saddle shape, matched to 20 digits (bean qou-ma3u), and D(y_+) = 0.9427073627769277209 is nonzero.

WHAT IT COSTS. An import of QOU.Archimedean.BlochWignerLobachevsky into a file whose header says the siblings are built self-contained (that note is about cross-SIBLING content-block imports, not library modules - but the author set the policy). It also changes what the conjecture ASSERTS: pole_cusp_matched stops saying 'volume equals some opaque D at the shape' and starts saying 'volume equals Milnor's Lambda-sum at the shape', which is a stronger and more falsifiable claim.

WHAT IT RISKS. Nothing computational - no witness, no number, no producer touches this file. The risk is definitional: if the intended D is not the Lobachevsky form (e.g. the deformed complex volume for the bar-odd leg, conj:binding-qbeta-complex-volume), pinning it here would be wrong.

DEFAULT IF NOTHING IS DONE. The opaque stays; the class is correctly typed and honestly open, and the file's docstring already records the option. Nothing breaks.

ALSO STALE. The opaque's docstring justification ('until Mathlib provides a complete formalisation of the classical dilogarithm') is stale on the Lobachevsky route - the corpus supplied one itself. Corrected in the module docstring on this branch.

MEASURED 2026-09-04 - the substitution was APPLIED to a scratch copy and COMPILED, not reasoned about.

  lean-direct on the whole file with the import + def:  EXIT 0, 16 s
  all 12 declarations still elaborate:                  yes
  #print axioms algebraic_geometric_equivalence:        [propext, Classical.choice, Quot.sound]
  #print axioms ...asymptotic_volume:                   [propext, Classical.choice, Quot.sound]
  axiom delta vs the opaque version:                    NONE, byte-identical

So the two plausible objections - 'it will not compile' and 'it will drag in axiom debt' - are both FALSE, measured. The exact edit tested:
  import QOU.Archimedean.BlochWignerLobachevsky
  noncomputable def BlochWignerD (z : UpperHalfPlane) : R := QOU.Archimedean.BlochWigner_lob (z : C)

WHAT REMAINS IS A MATHEMATICAL QUESTION, ONE WORD: is the D of conj:algebraic-geometric-dilog-equivalence the REAL Lobachevsky volume, or the DEFORMED COMPLEX volume of the bar-odd leg (conj:binding-qbeta-complex-volume)? If real: discharge, and the conjecture becomes falsifiable at no cost. If complex or unsure: leave it opaque - a vague-but-safe assertion beats a sharp-and-wrong one, and this file has already been wrong once in exactly that direction (the R -> R typing).

Full analysis: docs/audits/2026-09-04-two-decisions-bdpo-gh8l.md.
