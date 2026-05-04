/-!
# Sibling stub: Markov-axiom recursive ascent

The actual Lean scaffold for the recursive-ascent algorithm lives in
`QOU.Interactions.MarkovPeel` (under the `qou` Lake package).  This
sibling file is a placeholder so the content-validation pipeline
recognises that the definition has a Lean formalization.

See `qou:QOU.Interactions.markov_peel` for the abstract definition
and `qou:QOU.Interactions.markov_pair_z2` for the reference identity
([prop:markov-pair-z2](#prop:markov-pair-z2)).
-/

import QOU.Interactions.MarkovPeel

-- Re-export the canonical declaration under the local namespace so
-- `lean.ref` lookups resolve from this sibling file as well.
export QOU.Interactions (markov_peel)
