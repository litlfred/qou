---
# qou-um5h
title: 'Measure the LEAN convention-C surface: the C detector is rglob(''*.py'') and has never scanned .lean'
status: completed
type: task
priority: normal
created_at: 2026-08-23T15:45:00Z
updated_at: 2026-08-23T16:48:24Z
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

MEASURED 2026-08-19. docs/audits/2026-08-19-lean-convention-c-surface.md.

   raw hits on the C shape           97
   files containing at least one     52
   code lines (rest are prose)       11
   GENUINE convention-C z-defs        5

Counting hits over-reports by ~19x, files by ~10x. THE LEAN C SURFACE IS OVERWHELMINGLY DOCUMENTATION: 86 of 97 hits are docstrings describing the parameter, not defining it.

THE FIVE REAL SITES:
   Braiding/HnMarkovTrace.lean:82                  instance field z := 1/(sqrt q + 1/sqrt q)
   BraidKnot/JonesNuclearQuotient.lean:70          def markovZ
   BraidKnot/QBetaPerBlockChiClosedForms.lean:1037 def markov_parameter := sqrt q/(1+q)  -- the OTHER C spelling; thm at 1051 proves the two agree
   BraidKnot/QBetaQStarClosedFormExclusion.lean:78 let z, feeding alpha := (z-1)h/2
   BraidKnot/volume_perturbation.lean:64           class field z_def

Two notes. QBetaPerBlockChiClosedForms carries BOTH C spellings plus a proof they coincide -- a detector keyed on one spelling misses the other. And QBetaQStarClosedFormExclusion z feeds alpha = (z-1)h/2, so THAT alpha -- the same object this session identified as (eps - tr_M)/2 -- is C-FRAME.

FALSE POSITIVES, which are the point:
 1. JHopfQOneProvenance.lean:69 loopValue := -(sqrt q + 1/sqrt q) is the JONES LOOP FACTOR delta, documented as such. delta and z share the shape and are DIFFERENT OBJECTS. Flagging it would be a false positive; FIXING it would be a defect.
 2. MathlibExt.lean:197 proves q^(1/2)+q^(-1/2) = sqrt q + 1/sqrt q -- an rpow-vs-sqrt notational identity, convention-neutral.
 3. hden / hsum / hsum_pos positivity obligations sit next to definitions already counted.

The .lean analogue of "a grep for the bad NAME does not imply a bad NUMBER", inverted: a grep for the bad SHAPE does not imply the bad OBJECT.

DOES NOT LICENSE A MIGRATION. Five is small, but HnMarkovTrace C-frame Hopf closed form is a PROVED result whose re-derivation under D is its own work, and QBetaQStarClosedFormExclusion alpha is load-bearing for the q* exclusion. Recorded, not swept.

If a Lean C-detector is written it MUST separate delta from z and match BOTH C spellings, or it reproduces the 19x over-count.
