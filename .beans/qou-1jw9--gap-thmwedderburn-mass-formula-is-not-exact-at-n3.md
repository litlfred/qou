---
# qou-1jw9
title: 'GAP: thm:wedderburn-mass-formula is unfalsifiable as written — no unique M_i, no producer'
status: todo
type: task
priority: normal
created_at: 2026-08-25T07:10:47Z
updated_at: 2026-08-25T11:38:59Z
---

MEASURED, commit 933b895f17, computations/wedderburn_Mi_constructor_test.py.

The theorem states its own domain: the three invariants Phi_1/Phi_2/Phi_3
are the three EXTREMAL Wedderburn blocks, so the formula is exact only
where those exhaust the partitions of n. That is n=3 alone, i.e.
deuterium (Z=1, N=1, A=2, n=A+Z=3). D is therefore not one test among
many -- it is the single point the theorem claims exactness at.

The M_i constructor was built literally from the two blocks that define
it (def:atomic-braid + tbl:atomic-braid-table1-data + the theorem's own
"chaining the crossing matrices of all strands j > i" = suffix product
T_i * ... * T_{n-1}).

Spec-selected cell (literal reading, Phi_1-minimizing ordering n-e-p):
  predicted correction  -6.86271790 MeV
  target correction     -2.22459017 MeV  (= -B_total, AME2020)
  residual              -4.63812773 MeV  = 208.5 % of target
Sign CORRECT, magnitude not.

Sensitivity, not fit: the headline is the SPEC cell, not the smallest
residual. Across all 4 readings x 2 orderings the residual floor is
54.2 % and the ceiling 2652.6 %. No reading rescues it.

Scope (a), not (b): this constructor reading, alone, does not reproduce
D as-is. Nothing is excluded.

WHAT THIS SETTLES. Two earlier retractions in this chain were blamed on
feeding the wrong M_i (quark-level nucleon_gen_chains, then a
two-element atom_gen_chains). Feeding the RIGHT M_i does not rescue it.
The gap is in the leading-order truncation, not in the input.

DO NOT, on picking this up:
  - propose a seventh Delta_lambda closure ansatz (AGENTS.md names that
    prohibited by name, and arriving here by a fresh route is not a
    licence to retry it);
  - close the 208.5 % residual with any parameter -- only CAL-1/2/3 are
    admissible inputs (owner, this session);
  - read the sign agreement as partial success. Sign is one bit and the
    magnitude is 3x.

HONEST NEXT STEP, if any: the residual is a statement about the
truncation. The exact route is the Delta_lambda partition sum
(computations/binding_K_direct.py), which deliberately withholds a
prediction because the many-body magnitude is the documented Track A
blocker. Nothing here changes that status.


=== MORE CONTEXT (commit 61d81adaf9) — and a SCOPING CORRECTION to my own claim above ===

I went looking for what the corpus already says about this formula. Three
things turned up, and the third forces me to weaken the headline.

1. THE PUBLISHED TABLE HAS NO PRODUCER, AND ITS WITNESS NEVER EXISTED.
   tbl:mass-table-z1-20-table-data publishes 20 rows (H..Ca). Its backing
   witness `atom-mass-complete-wedderburn` is not merely absent — it never
   existed in git history. Already named a "phantom witness" in
   docs/audits/2026-07-12-exposition-drain-needs-owner-ledger.md. The 20
   values survive ONLY as a hardcoded dict at
   computations/_deprecated/feynman_qou_comparison.py:218, under a comment
   citing that phantom. mass-table-z1-20.md itself already says the rows are
   "not currently reproducible".

2. THE TABLE'S ERROR METRIC DIVIDES BY THE INPUTS, NOT THE PREDICTION.
   The formula's first three terms are INPUTS (absolute-mass excision). The
   whole predictive content is the correction, whose job is to equal
   -B_total. The base is ~99.8 % of the mass, so Delta/m measures the inputs.
   Re-scored on binding:

       metric      range over the 20 published rows
       Delta/m     0.003 % .. 0.19 %     looks excellent
       Delta/B     0.4 %   .. 28 %       the real prediction error

   And H-1 — the BEST-looking row at +0.014 % — is the correction with the
   WRONG SIGN and ~9300x the magnitude (+0.1269 MeV vs a true -1.36e-5 MeV).
   This part is pure arithmetic on published numbers; it does NOT depend on
   my constructor and stands on its own.

   H-1 needed care and I nearly got it wrong: the published masses carry 3
   decimals (+/- 0.5 keV) while hydrogen's binding is 13.598 eV, 37x finer.
   A binding read off that column is rounding, not physics. My first pass
   used it and printed a ratio of -1436; the CODATA-based figure is -9333.
   Use the second.

3. MY CONSTRUCTOR DOES NOT REPRODUCE THE TABLE EITHER.
   mine/true swings 0.47 .. 2.5e5 across H-1..C-12; pub/true sits in a
   smooth 0.78-1.28 band. Given (1), that does NOT refute the constructor —
   the table is not an independent check on anything.

SCOPING CORRECTION. The heading of this bean, and commit 933b895f17, say
"the formula is NOT exact at n=3". Too strong. What is established:
  - no reading of M_i reproduces D (54 % .. 2653 %), AND
  - no construction reproduces the published table, AND
  - the published table has no producer.
The defensible statement is that thm:wedderburn-mass-formula is currently
UNFALSIFIABLE AS WRITTEN: its M_i prose does not determine a unique
construction, and nothing in the corpus can adjudicate between candidates.
Weaker than "the formula is false"; stronger than "my probe failed".

This also explains the two earlier retractions in this chain. I reached for
the wrong helper twice (quark-level nucleon_gen_chains, then the
two-generator atom_gen_chains) not through carelessness alone but because
THERE IS NO RIGHT HELPER — atom_gen_chains returns 2 chains for every (Z,N)
and is an H_3-shaped approximation, explicitly disclaimed for this formula.

TWO SEPARATE DEFECTS FOUND, both actionable, neither fixed here:
  a) content/quantum-observable-universe/observations/
     neutron-proton-mass-splitting-proof.md:35 still asserts
     "**Witness**: atom-mass-complete-wedderburn.witness.json" with NO
     caveat. The sibling wedderburn-mass-formula-proof.md:143 was rescoped;
     this one was missed. A live content block cites a witness that never
     existed.
  b) def:atomic-braid's ground-state rule ("minimize Phi_1 over all
     permutations") is exponential in A: C(40,20) = 1.4e11 for Ca. As
     written the definition is not computable for the table it underwrites.

STILL PROHIBITED, unchanged: no seventh Delta_lambda ansatz; no closing the
residual with any parameter (only CAL-1/2/3 admissible); sign agreement is
one bit and is not partial success.


=== BOTH DEFECTS FIXED (commit a060ad07ed) — and defect 1 was bigger than reported ===

DEFECT 1 (phantom witness) — fixed, and the fix exposed a third problem.
Corpus-grepped first: neutron-proton-mass-splitting-proof.md was the ONLY
live block citing the phantom without a caveat. mass-table-z1-20.md and
wedderburn-mass-formula-proof.md were already scoped.

With no witness, the only check is re-derivation from the block's own rules
(computations/pn_splitting_proof_provenance_probe.py). It does NOT confirm
the block:

  THE READING IS PINNED, BY THE PROTON. Convention C + suffix-inclusive
  Phi_1 gives Phi_p = -0.8785233 vs the quoted -0.8785 — exact at the quoted
  precision, and the only one of 8 readings that lands.

  THE NEUTRON DOES NOT FOLLOW. Same reading gives Phi_n = -1.2677888, not
  the quoted -1.2261. Because the reading is pinned by its partner, this is
  NOT reading ambiguity.

  source                      |dPhi|      dm MeV    vs CODATA
  as stated in the block      0.3476      1.3016     +0.63 %
  re-derived, convention C    0.3892655   1.4576     +12.7 %
  re-derived, convention D    0.3354835   1.2562     -2.87 %

So the block's headline +0.63 % agreement is NOT REPRODUCIBLE. It is also
convention C throughout (excised by the owner ruling of 2026-08-15); under
D its own construction gives -2.87 %.

Scope (a): 8 readings, not exhaustive. NO replacement value proposed. The
block now carries a provenance-and-scope note saying the +0.63 % cannot
currently be checked and must not be cited as a confirmed prediction.

DEFECT 2 (exponential ground-state rule) — recorded, NOT "fixed" by
invention. def:atomic-braid clause 1 ranges over C(A,Z) arrangements: 924
for C-12, 1.4e11 for Ca-40. Clause 2 is already greedy/polynomial; the
asymmetry is unexplained. I did not substitute a polynomial rule — that
would be inventing mathematics the corpus has not derived. The definition
stands with the cost recorded, plus the note that any computation quoting a
ground-state ordering for A >~ 14 is using an unstated restriction and
should say which.

GATE NOTE, worth carrying forward: precision-gates --changed exits 1 here on
`import-time dps ratchet` + `raw-float64 ratchet`. Those are RED ON CLEAN
MAIN — verified by stashing the whole change and re-running, which
reproduces the identical two reds. Do not attribute them to a branch that
touches computations/, and do NOT widen a baseline to clear them.

NEW OPEN ITEM: the pn-splitting proof's +0.63 % needs either a derivation
that reproduces Phi_n from the pinned reading, or retraction of the figure.
Under the canonical convention D the same construction gives -2.87 %. That
is a question about the block's numbers, NOT a licence to fit Phi_n.


=== RETRACTION (commit 40d7a8e427): the witness DID exist ===

I asserted in THREE PRs — #5743 and #5753 (both MERGED) and #5758 — that
`atom-mass-complete-wedderburn.witness.json` never existed in git history.
FALSE. Added 2026-04-10, commit 1359fe23ac, at
folio-assistant/computations/atom-mass-complete-wedderburn.witness.json;
left the tree with the platform code in the miga migration.

WHY EVERY SEARCH MISSED IT — mine and the 2026-07-12 audit's alike: they
looked under `computations/`. It lived under `folio-assistant/computations/`.
A negative existence claim about history is only as good as the paths it
searched, and this repo has moved whole subtrees between repos. Search by
BASENAME across all refs:
    git log --all --diff-filter=A -- "*/<name>"
Also: the clone here is SHALLOW, which can only manufacture FALSE "never
existed" verdicts, never false "exists" ones. A negative from a shallow clone
is weak evidence; I treated it as strong.

I found it only because a sweep I wrote to generalise the defect
(computations/audits/content_witness_citation_audit.py) classified it REMOVED
rather than NEVER EXISTED, contradicting what I had asserted all session. The
tool was right and I was wrong.

THE RECOVERED ARTIFACT IS WORSE NEWS THAN THE PHANTOM CLAIM WAS.

It reproduces the published table exactly (20 rows; 1H 938.910, 4He 3734.624,
7Li 6534.188; mean 0.074 %, max 0.1917 %). So the table HAS a producer. But
its own parameters show that producer did not compute the published formula:

  alpha    3.74446      = m_e*8G                       matches
  beta2   -6.087415     = -2[3]_q = -6.0874146         matches
  beta3    0.0499       vs h_A^2  =  0.043707282       MISMATCH, 14.2 %
  Vol_B3   7.32772475   is exactly 8G                  MISLABELLED
  m_p    938.230457     CODATA 938.27208816            -44 ppm
  m_n    939.532005     CODATA 939.56542052            -36 ppm
  fitted   0            asserts zero fitted parameters

beta3 has NO stated derivation anywhere and sits beside a no-fits flag. The
base masses are not CODATA and their error (-0.042 MeV) is ~1/3 of 1H's whole
quoted delta of 0.127 MeV. A field named for the Borromean volume holds
8*Catalan to 16 digits.

DO NOT, on picking this up: reconstruct beta3, fit it, or adjust the
published formula to match. Which of the two is correct is an authoring
question about published content. Do NOT restore the witness into
computations/ — that would imply it certifies the current formula, which it
demonstrably does not.

SWEEP RESULT (the generalisation): 143 witnesses cited across content/**.md —
137 resolve, 3 REMOVED, 3 NEVER EXISTED. The NEVER EXISTED three are
evaluation-phiq-pair-knot-markov-trace, evaluation, representation
(.witness.json), cited by spin-involution-lp-dual-invariance-proof.md,
he4-channel-active-set.md + markov-pair-z2.md, and
six-term-mass-formula-complete-table-data.md. NOT yet triaged — and after
today, verify each with a BASENAME search before calling any of them a
phantom.

The pn-splitting Phi_n finding is UNAFFECTED: that block's numbers are
quark-level and appear nowhere in this atomic-mass witness.


=== TRIAGE OF THE 3 "NEVER EXISTED" (commit 7ba6da945a) — the sweep was wrong ===

My own sweep under-reported the corruption it found, in the same direction as
the mistake it was written to prevent.

Its regex was [A-Za-z0-9_.-]+\.witness\.json — no space. So a citation reading
`he4-sdp-compositional-canonical evaluation.witness.json` was captured as just
`evaluation.witness.json` and reported as a missing witness with a plausible
name. It is not a missing witness; it is a CORRUPT citation — a hyphen
replaced by a space inside a filename. The truncation also collided two
distinct citations onto one name, so the real count is 4, not 3.

  'adjacent-vs-full-canonical evaluation.witness.json'
      mass-theory/markov-pair-z2.md
  'atomic-tr-m-mpfr-exact representation.witness.json'
      mass-theory/six-term-mass-formula-complete-table-data.md
  'canonical evaluation-phiq-pair-knot-markov-trace.witness.json'
      mass-theory/spin-involution-lp-dual-invariance-proof.md
  'he4-sdp-compositional-canonical evaluation.witness.json'
      mass-theory/he4-channel-active-set.md

TWO of the four sit inside MARKDOWN LINK TARGETS, where an unescaped space
truncates the URL — those links are broken in the rendered page as well as
pointing at nothing.

NOT FIXED, DELIBERATELY. Each was checked BOTH as written AND with the space
repaired to a hyphen; none resolves either way, so the intended target is
UNKNOWN. Nearby files exist with related stems —
  adjacent-vs-full-probe.witness.json
  he4-sdp-compositional-probe.witness.json
  atomic-tr-m-mpfr-50dps.witness.json
  (nothing at all for the phiq-pair one)
— but mapping a citation onto a nearby filename is GUESSING, and guessing a
provenance citation is precisely the failure this line of work is about. DO
NOT wire them to the nearby candidates without an authoring decision.

Introducing commit UNDETERMINED: `git log -S` across all refs does not
complete in 2 min on this repo. Not pursued.

The audit now matches internal spaces, reports CORRUPT as its own class, and
states in its output that both spellings were checked — so the next reader is
not invited to guess either.

STILL OPEN from the sweep: the 3 REMOVED citations
(atom-mass-complete-wedderburn — recovered and analysed above;
co-molecular-binding, cited by molecular-construction/co-triple-bond-energy.md;
mass-qvalue-by-level, cited by mass-theory/unified-iterative-correction-proof.md).
The latter two are NOT triaged. Recover each with a basename search before
saying anything about it.
