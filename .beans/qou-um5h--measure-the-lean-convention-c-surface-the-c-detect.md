---
# qou-um5h
title: 'Measure the LEAN convention-C surface: the C detector is rglob(''*.py'') and has never scanned .lean'
status: todo
type: task
priority: normal
created_at: 2026-08-23T15:45:00Z
updated_at: 2026-08-23T15:45:43Z
---

NOT A NEW DISCOVERY -- a measurement gap. QOU/BraidKnot/MarkovParameterFibreRank.lean:15 already records C as "used by >= 8 corpus sites and hard-coded", and MathlibExt/MarkovNormalisation.lean argues D is DERIVED (Wenzl r=2) rather than chosen. What is missing is a count and a post-ruling migration decision.

THE DETECTOR CANNOT SEE LEAN. scripts/convention-c-producer-audit.py walks rglob("*.py") and parses Python ASTs; the older one walked content/** only. So the .lean surface is outside EVERY existing detector, and AGENTS.md guidance to "treat the remaining C surface as UNMEASURED rather than clear" applies to it in full.

FIXED-STRING GREP over content/quantum-observable-universe/lean/QOU finds C-spellings in ~11 files. Live DEFINITIONS (not docstrings) include:
    Braiding/HnMarkovTrace.lean:82            z := 1/(Real.sqrt q + 1/Real.sqrt q)   -- in a class DOCSTRING calling it "the canonical Wenzl Markov parameter"
    BraidKnot/JonesNuclearQuotient.lean:70    markovZ q := 1/(Real.sqrt q + 1/Real.sqrt q)
    BraidKnot/QBetaQStarClosedFormExclusion.lean:78   let z := ...
    BraidKnot/QBetaPerBlockChiClosedForms.lean:1051   THEOREM asserting markov_parameter q = 1/(sqrt q + 1/sqrt q)
    HadronicMass/pair_skein_mass_formula.lean:47      class field divides by (sqrt q + 1/sqrt q)

A NAIVE COUNT OVER-REPORTS, and this is the trap to write down: JHopfQOneProvenance.lean:69 defines loopValue q = -(sqrt q + 1/sqrt q), which is the JONES LOOP FACTOR delta, NOT the Markov parameter z. Different object, same sqrt-q + 1/sqrt-q shape. Any Lean C-detector must separate delta from z or it will report loop factors as convention violations. This is the .lean analogue of the AGENTS.md warning that a grep for the bad NAME does not imply a bad NUMBER.

DIRECT RELEVANCE TO qou-g8i1: my (z+d) bond rule was derived and verified with D (z = q^3/(q^2+1)) and matches to 4.45e-31 over 16 nuclei. MarkovTraceTower carries C. So a Lean formalisation of the bond rule MUST NOT be built on MarkovTraceTower as it stands -- it would silently be a C-frame statement about a D-frame result. Use MathlibExt/MarkovNormalisation (D, derived) or state z abstractly.

SCOPE: measure and catalogue; do NOT mass-migrate. The C-frame Hopf closed form in HnMarkovTrace (q^{5/2} - q^{1/2} + q^2 + q)/(q^2+q) is a proved result whose re-derivation under D is its own piece of work.
