---
# qou-1jw9
title: 'GAP (closed): thm:wedderburn-mass-formula''s three invariants were carried — Phi_2/Phi_3 now derived, Phi_1 recomputed under convention D, D table adopted'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-25T07:10:47Z
updated_at: 2026-11-20T09:30:00Z
parent: qou-wp3h
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
  a) folio/quantum-observable-universe/observations/
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


=== THE OTHER TWO RECOVERED (commit b562732c2a) — a migration class ===

All three REMOVED citations recover from the SAME place, SAME cause: added
under folio-assistant/computations/, lost when the platform moved out in miga.

  atom-mass-complete-wedderburn   2026-04-10  1359fe23ac
  co-molecular-binding            2026-04-13  a3e8c2c82d
  mass-qvalue-by-level            2026-04-15  e2814e577f

Retrieve any with:  git show <commit>:folio-assistant/computations/<name>

mass-qvalue-by-level — I FIRST READ IT WRONG. I reported "no results rows, no
1H" after reading `assertions` and stopping. It has data.mass_by_level with 19
rows H..208Pb, so the citing block's range claim is fair, and its BW(k=5)
column is ACCURATE (3H->3He 0.018228 vs 0.01861 exp, ~2%). allPassed honestly
false. Read `data` before judging a witness.

The real defect: 7 assertions test the INACCURATE NF-trace column with a
tolerance set just above each miss —
  Q(3H->3He)  2.4412 vs 0.0186  tol 2.6648  13017% err  PASSED
  Q(14C->14N) 3.0678 vs 0.1565  tol 3.2024   1861% err  PASSED
  Q(60Co)     ... 508% ... Q(137Cs) 280% ... Q(90Sr) 258% ... Q(210Bi) 68%
  B(D) k=5    2.8435 vs 2.2242  tol 1.5551     28% err  PASSED
A tolerance ~10% wider than its own miss is a bound chosen after the fact. The
argument is the contrast INSIDE the file: B(T) and B(3He) carry tolerances of
0.0004/0.0001 and are recorded FAILING at 0.0% error.

co-molecular-binding — three findings:
  1. FITTED SCALE, ON H2. calibration_factor = 0.23879110765149733;
     0.687012518457808 * 27.296143240836667 * 0.23879110765149733 = 4.478000 eV
     = H2's measured bond energy. Its own H2_cross_check records the
     UNcalibrated 18.75279 eV (4.19x too large), and 4.478/18.753 = 0.23879
     exactly. A FOURTH CALIBRATION on a molecular observable — outside
     CAL-1/2/3, so this one needs an OWNER decision.
  2. "E_hartree_eV" = 27.296143240836667 vs CODATA 27.211386245988, +0.31%.
     Not the Hartree.
  3. WITNESS CONTRADICTS ITS BLOCK. co-triple-bond-energy.md says sigma
     contributes the largest |V| and pi smaller; the witness gives all three
     the IDENTICAL delta_Phi1_per_bond and k=3 = exactly 3x k=1. The block also
     claims the witness records LP duals y1,y2,y3 — it records NONE (y0_star,
     y_star, active_set, primal_obj, dual_obj, duality_gap all absent, the
     fields AGENTS.md requires of every LP/SDP witness).
  Its assertion "CO triple bond within 25% of observed" (D_0 = 11.09 eV) passes
  at +21.1% — inside a loose bar, reached via a factor fitted on H2.

NOTHING restored, re-fitted, or edited in a citing block. Each needs an
authoring decision; the co calibration needs an owner one.

SWEEP NOW FULLY TRIAGED: 144 cited, 137 resolve, 3 REMOVED (all recovered
above), 4 NEVER EXISTED (all corrupt-with-space, targets unknown, recorded).


=== 🟧 OWNER DIRECTIVE 2026-08-25: "no fitting!!!" (commits 41fa123648, d8bff83024) ===

Put to the owner as the one item I said was not mine to decide. Read straight
it settles that item AND the other two of the same kind. ALL THREE recovered
witnesses carry a fit, and none is admissible:

  co-molecular-binding   calibration_factor = 0.23879110765149733
                         = 4.478/18.753 exactly — the ratio making the
                         uncalibrated result equal H2's MEASURED bond energy.
                         A fourth calibration, on a molecular observable.
  mass-qvalue-by-level   7 assertion TOLERANCES each ~10% above its own
                         discrepancy, so they cannot fail. Q(3H->3He) passes
                         at 13017% error. A bound fitted to a miss is a fit.
  atom-mass-complete-    beta3 = 0.0499 vs published h_A^2 = 0.043707282,
  wedderburn             14.2% apart, no derivation, beside "fitted": 0.

CONSEQUENCE: none is live (all lost in miga), so nothing to un-wire. What it
means is that RECOVERING THEM CANNOT REHABILITATE THE CITING CLAIMS. Both
citing blocks are now scoped in-tree:
  molecular-construction/co-triple-bond-energy.md
  mass-theory/unified-iterative-correction-proof.md

DOES NOT FOLLOW: reconstructing beta3, re-deriving the CO scale from
CAL-1/2/3, or adjusting any tolerance. "No fitting" forbids the fit; it does
not license a replacement invented by an agent.

STILL OPEN, untouched by the directive: the published formula and the
computation that made the table DISAGREE — h_A^2 vs beta3. Which is wrong is
an authoring question.

=== GATE CLAIM CORRECTED — mine went stale within the hour ===

I recorded (commit + PR #5758 body) that BOTH `import-time dps ratchet` and
`raw-float64 ratchet` are red on clean main. True at ~11:00Z, STALE by 12:20Z:
a sibling landed 0b72b8fcca "import-time dps gate GREEN" / fee0eb8fb1.

Re-measured after merging origin/main:
                            main (0b72b8fcca)   this branch
  mpf_import_time_dps_audit rc=0, lossy 0       rc=0, lossy 0
  precision-gates.sh        RED: raw-float64    RED: raw-float64

CORRECT STATEMENT: ONE gate red (raw-float64), identical on main and branch.
import-time dps is GREEN on both.

LESSON WORTH KEEPING: "red on main, not mine" is the claim that lets a branch
merge past a red gate. When half of it silently goes stale the next reader
either dismisses a real red as inherited, or re-investigates a fixed one. A
gate claim carries a timestamp whether or not you write one down — so write
one down, and re-measure before repeating it.



=== TAKEOVER 2026-08-25T16:1xZ (stalled-claim policy, AGENTS.md work-plan §2) ===

Taken over from branch claude/phantom-witness-and-groundstate-2026-08-25
(PR #5758), last commit 1d7bede2f6 at 12:37:25Z -- 3h35m stale at pickup,
no in-flight CI (auto-triggers disabled repo-wide), so presumed abandoned.
NOT force-pushed; continued from that tip on claude/stalled-agent-recovery-iwjb5y.

TWO CORRECTIONS TO THE HANDOFF, both measured:

1. Vol_B3 IS NOT MISLABELLED.  The recovery audit called the field
   'mislabelled: this is exactly 8G, not a volume'.  Wrong, and inverted:
   Vol(Borromean) = 2*V_oct = 8G is an identity (V_oct = 4G), and the corpus's
   own binding_link_volumes.py:112 sets VOL_B3 = 8*catalan under the comment
   'Vol(L6a4) = 8G = Vol(Borromean)'.  A closed-form value was read as a
   substitute for the quantity it is the closed form OF.

2. THE 'AUTHORING CALL' IS DECIDABLE, AND IS NOW DECIDED.  The audit left
   'either the published h_A^2 is wrong or beta3 is undocumented' open on the
   ground that the artifact cannot distinguish them.  Derivability does, and
   needs no artifact:

     h_A^2 = (q - 1/q)^2 = [3]_q - 3   exact (3e-51), PROVED IN LEAN sorry-free
     0.0499                            no construction; 16 pre-declared
                                       candidates, closest 63.7 % off against
                                       a 0.1 % window for a 3-digit literal

   Sharper consequence, with no q in it at all: since beta2 = -2[3]_q and
   beta3 = [3]_q - 3, the pair must satisfy 2*b3 + b2 + 6 = 0.  The recorded
   (-6.087415, 0.0499) gives +0.012385.  So the witness's two numbers are
   MUTUALLY INCONSISTENT AS A PAIR -- any q, any pin, either convention.

   Lean: QOU/Mass/WedderburnMassFormulaCoefficients.lean, generic Field R, no
   archimedean construct, no substrate q0.  lean-direct exit 0 against the real
   import cone; #print axioms on all four decls = propext/Classical.choice/
   Quot.sound, no sorryAx.
   Probe: computations/wedderburn_beta3_provenance_probe.py.

3. PRECISION DEFECT SEPARATED FROM FIT.  The published digits 0.043707282 are
   (q-1/q)^2 at a 5-decimal-ROUNDED q = 1.10998 (2.05e-9), not at either pin
   (2.4e-5 off).  mu-p gap is 1.2e-8 in q and cannot explain it.  Rounded input
   != fit; the construction is exact.  Re-publishing at unrounded q0 is an
   authoring change, left to the author.

NOT DONE, deliberately (owner 2026-08-25, 'no fitting!!!'): beta3 not
reconstructed, published formula not adjusted, table not re-derived, no
tolerance touched.

STILL PROHIBITED, unchanged: no seventh Delta_lambda ansatz; only CAL-1/2/3
admissible; sign agreement is one bit.


=== RETRACTION carried into this bean, 2026-08-25 ===

Item 1 above still reads 'ITS WITNESS NEVER EXISTED'.  THAT IS FALSE and is
retracted.  atom-mass-complete-wedderburn.witness.json was added 2026-04-10 in
1359fe23ac under folio-assistant/computations/ and left the tree with the
platform code in the miga migration.  All three 'lost' witnesses recover the
same way; it is a repo-split class, not three accidents.  The searches that
missed it (mine and the 2026-07-12 audit's) looked under computations/ only --
search by BASENAME across all refs, and note a shallow clone can manufacture
false 'never existed' verdicts but never false 'exists' ones.

So the table DOES have a producer.  What section 3a establishes is that the
producer is not the published formula -- which is the stronger finding, not a
weaker one.



=== STATUS 2026-08-25T18:2xZ — coefficient sub-question CLOSED on main; PARENT GAP STILL OPEN ===

Merged to main as dc72e4494 (PR #5771, rebase-merge; #5758 closed as superseded,
branch retained per rule 9).  On main now:
  computations/wedderburn_beta3_provenance_probe.py
  folio/quantum-observable-universe/lean/QOU/Mass/WedderburnMassFormulaCoefficients.lean

UNCLAIMING deliberately (status -> todo).  I am no longer working this, and a
bean left at in-progress reads as an ACTIVE CLAIM -- which is what triggered
this very takeover.  Do not infer from the merge that the bean is done.

WHAT IS CLOSED: only the third-coefficient question.  h_A^2 = [3]_q - 3 exactly
(Lean, sorry-free); 0.0499 has no construction; the recorded pair violates
2*b3 + b2 + 6 = 0 by 0.012385, so it is inconsistent for any q.

WHAT IS STILL OPEN -- the bean's actual title.  thm:wedderburn-mass-formula
remains UNFALSIFIABLE AS WRITTEN: its M_i prose still does not determine a
unique construction, no reading reproduces D (54 % .. 2653 %), and the
published table still has no producer that is the published formula.  The
coefficient result NARROWS this (the correction term carries one q-integer
DOF, not two); it does not close it.

CHEAPEST NEXT STEP, if anyone picks this up: what the _deprecated/ producer's
0.0499 actually was.  That is script archaeology on next_partition_levels.py's
history, not physics -- and it is the only lead that does not require deciding
the M_i reading first.

STILL PROHIBITED, unchanged: no seventh Delta_lambda ansatz; only CAL-1/2/3
admissible; no fitting (owner, 2026-08-25); sign agreement is one bit.

TAKEOVER 2026-08-25T16:20Z. Prior session (session_01Y49zmah825kkwu2aB8CbAY) stalled on
branch claude/phantom-witness-and-groundstate-2026-08-25 at 1d7bede2f (last commit
12:37:25Z, >3h idle, PR #5758 draft, no reviews, no in-flight CI). Continuing from that
tip on claude/agent-stalled-no-fitting-a5ur1w. Not force-pushing the stalled branch.

Picking up its ONE stated open item: the published formula's h_A^2 = 0.043707282 and the
recovered producer's beta3 = 0.0499 disagree by 14.2 %. Under the owner's no-fitting
ruling that is an authoring call, but it is premature to ask it until the measurement is
done: does the published formula, evaluated with h_A^2, reproduce the published table at
all? The producer with beta3 does (20 rows, mean 0.074 %). If h_A^2 does not, the call is
settled by measurement rather than by preference.


RESOLVED the '#5758 Left open' item by measurement, PR #5773.

beta3 = 0.0499 reproduces 20/20 published M_pred to 0.00049 MeV; the published
h_A^2 = 0.0437073 reproduces 0/20 at the 3 dp the table quotes. Published
summary figures are beta3's too (0.0740 % / 0.1917 % vs h_A^2's 0.0746 % /
0.1909 %). So: the table is NOT the published formula's output -- confirmed.

The OTHER branch of the disjunction is NOT supported and must not be quoted as
if it were: on accuracy the two coefficients are indistinguishable, h_A^2 being
marginally BETTER on the worst row. Phi_3 enters ~50x more weakly than Phi_1, so
a 14.2 % coefficient change moves the table < 1 part in 30 000. The table
carries NO evidence about which coefficient is correct. Scope (a).

Foreclosed for beta3: not h_A^2 at either pin (both 0.0437062, flat to 13
digits); ratio 1.1416862 = q0^1.26992, not an integer/half-integer power; 3 sig
figs where alpha has 6 and beta2 has 7.

NOT DONE, deliberately: regenerating the 20 published values under h_A^2. It is
the option that would make the block's own 'zero fitted parameters' claim true
and costs 0.0006 pp of mean accuracy, but changing twenty published numbers is
the author's call. Replacement values are already in the probe's results block.

Probe: computations/audits/wedderburn_beta3_vs_hA2_discrimination.py
Audit:  docs/audits/2026-08-25-wedderburn-table-is-not-the-published-formula.md


MERGED 2026-08-25T18:43Z as PR #5773 (merge 265ae726df). All 5 files verified on
main; the false 'not currently reproducible' sentence is gone from
mass-table-z1-20.md and the corrected text is live.

WHAT LANDED (the takeover's own contribution, after the sibling #5763 took the
overlap): the reproduction measurement -- beta3 reproduces 20/20 published
M_pred to 0.00049 MeV, published h_A^2 reproduces 0/20 -- plus the measured cost
of the repair and the block correction neither takeover had made.

WHAT REMAINS OPEN, and it is an AUTHORING call, not a measurement:
regenerate the 20 published values under h_A^2. Cost is measured: shifts run
-0.024 MeV (1H) to +1.205 MeV (40Ar), mean error 0.0740 -> 0.0746 %, worst row
IMPROVES 0.1917 -> 0.1909 %. Replacement values are in the probe's results
block; no new derivation needed. Use h_A^2 at the UNROUNDED q0 pin -- the
published digits 0.043707282 are (q-1/q)^2 at a 5-decimal-rounded q=1.10998,
a 2.4e-5 defect (effect on the table <= 2.1e-4 MeV, invisible at 3 dp).

DO NOT, on picking this up: treat the alternative ('keep the numbers, document
beta3') as an equal option. Post-#5763 it is close to untenable -- beta3 is
unreachable from the construction its own sibling coefficients use, inside a
block whose headline claim is zero fitted parameters.


REGENERATION DONE, PR #5781 (owner said 'go' 2026-08-25).

New evidence found doing it, independent of both prior probes: the 2nd and 3rd
coefficients are LOCKED. [3]_q - 3 = (q-1/q)^2 = h_A^2, so beta2 = -6 - 2*h_A^2
identically in q. The superseded witness's beta2 = -6.087415 IS that identity at
h_A^2 = 0.043707282; 0.0499 would have forced beta2 = -6.0998. The old witness
contradicts its own third coefficient in its own arithmetic. Residual exactly 0,
asserted in the new witness.

Table now: mean 0.0745925 %, max 0.190854 % (worst row improves), 0 fitted
parameters, proton pin. Correction is PROVENANCE not fit -- Phi_3 enters ~50x
more weakly than Phi_1, so accuracy is materially unchanged. Do not present this
as an accuracy improvement.

Block is now witness-backed: computations/wedderburn_mass_table_z1_20.py ->
wedderburn-mass-table-z1-20.witness.json, wired in the table .ts.

TWO THINGS REMAIN, both recorded as caveats, neither authorised here:
  1. Phi_1/Phi_2/Phi_3 are CARRIED from the recovered witness, not re-derived.
     The transfer-matrix computation behind them is still unreproduced in-tree.
     This is the deeper provenance gap and is the natural next item.
  2. Base masses are 44/36 ppm below CODATA -- ~1.5 MeV at Z=20, i.e. LARGER
     than the coefficient fix on heavy rows. Separate defect.


=== ARC REVIEW 2026-08-29 — where this stands after three sibling PRs ===

Returning to this arc after main moved ~2500 commits. Reviewed rather than
resumed, because most of what I left open was closed by other sessions while
I was away — and two of my own claims did not survive.

MY CLAIMS, ADJUDICATED
  RETRACTED (theirs, correct — verified independently here). "Vol_B3 is
    mislabelled: 8G, not a volume." WRONG. Vol(Borromean) = 2*V_oct = 8G IS
    the volume, V_oct = 4G, and binding_link_volumes.py:112 already sets
    VOL_B3 = 8*catalan under that exact comment. I mistook a closed form for a
    substitution — and the check that catches it is the same corpus-grep my
    own audit section 1 invokes. I failed to run my own discipline.
    Worse than a wrong claim: alpha = m_e*8G and Vol_B3 = 8G are the SAME
    number because alpha = m_e * Vol(B^3). Calling it a mislabelling destroyed
    a real structural coherence.
  SUPERSEDED, by a strictly stronger argument. I left "either the published
    h_A^2 is wrong or beta3 is undocumented" open, saying the artifact cannot
    distinguish. It can be settled without the artifact: h_A^2 = [3]_q - 3
    exactly, so beta2 = -2[3]_q forces 2*beta3 + beta2 + 6 = 0 IDENTICALLY IN
    q. The recorded pair misses by 0.012385 — inconsistent for EVERY q. Mine
    needed q0 and produced a 14.2 % gap at one anchor. Verified both here.
  STANDS. The Delta/B vs Delta/m recast (the published error metric divides by
    the inputs); the four space-corrupted citations; the migration class
    (three witnesses lost to folio-assistant/computations/ in miga); the
    basename-search discipline.

WHAT LANDED WHILE I WAS AWAY
  #5763, #5773 (265ae726df), #5781. Net: the table was REGENERATED under
  h_A^2 — mean 0.0745925 %, max 0.190854 % (worst row improves), 0 fitted
  parameters, proton pin, and the block is now witness-backed by
  computations/wedderburn_mass_table_z1_20.py. My own PR #5758 was closed
  WITHOUT merging, but all of its content reached main by rebase at
  2026-08-25T20:16Z — verify content, not PR state, before assuming work was
  lost.

THE TWO REMAINING ITEMS — and item 1 is my n=3 finding, which nobody has
connected:

  1. Phi_1/Phi_2/Phi_3 are CARRIED VERBATIM from the recovered witness, not
     re-derived (wedderburn_mass_table_z1_20.py:30, :69, :204 say so
     explicitly). Named there as "the deeper provenance gap and the natural
     next item".
     *** THIS IS EXACTLY WHAT computations/wedderburn_Mi_constructor_test.py
     ATTEMPTED AND FAILED. *** That probe reconstructs Phi from the content
     blocks (def:atomic-braid + tbl:atomic-braid-table1-data +
     thm:wedderburn-mass-formula) and misses D by 54 %-2653 % across four
     readings of the M_i prose. So the gap is not merely unclosed — its size
     is already MEASURED, and the measurement says the published prose does
     not determine the construction. Anyone taking item 1 should start from
     that probe, not from scratch, and should treat "which reading" as the
     open question rather than assuming one.
     This also re-scopes my "unfalsifiable as written" finding correctly: the
     TABLE is now reproducible (witness-backed, 0 fitted parameters); it is
     the DERIVATION of Phi from the atomic braid that is not.

  2. Base masses 44/36 ppm below CODATA (M_P = 938.230457, M_N = 939.532005),
     explicitly not fixed. Measured here against binding, since "larger than
     the coefficient fix" is true but not the right yardstick:
        D      -0.0750 MeV   3.37 % of B
        4He    -0.1501 MeV   0.53 %
        12C    -0.4503 MeV   0.49 %
        40Ca   -1.5009 MeV   0.43 %   (vs +1.205 coefficient fix — larger, yes)
        208Pb  -7.6241 MeV   0.47 %
     Real, and worst at D where B is smallest — but ~0.4 % of B on heavy rows
     against a reported Delta/B near 9.9 %, so NOT the dominant term. Fixing it
     will not close the table; treat it as hygiene, not as the accuracy story.

NEXT, my judgement and open to being overruled: item 1, entered through the
existing constructor probe. Item 2 is cheaper and certain, but it is hygiene —
it moves 0.4 %-of-binding on rows already 9.9 % out. Item 1 is where the
framework's claim actually rests, and it already has a measurement waiting.

STILL PROHIBITED, unchanged: no seventh Delta_lambda ansatz; no fitting (owner,
2026-08-25); do not close the D residual with any parameter; only CAL-1/2/3
admissible.


=== ITEM 1, ONE THIRD CLOSED (commit 63b99a84ba) ===

Entered item 1 through the existing constructor probe, as the review proposed.

DERIVED, not observed. Every tbl:atomic-braid-table1-data crossing has
chirality ratio lam_sym/lam_alt equal to -q^2, -q^-2 or +-1:
    pp,ee -> -q^2 (+2 units of ln q)   nn,pe -> -q^-2 (-2)   pn,ne -> +-1 (0)
These are the three cases ALREADY PROVED sorry-free in
QOU/BraidKnot/HeckeLinearReduction.lean (symAltRatio_zero/_full/_half) plus the
identity. So Phi_3 is FORCED to be an EVEN integer multiple of ln q — no
ordering, no M_i reading, no anchor needed.

MEASURED. All 20 carried Phi_3 = w*ln q, integer w, every w even. Residuals are
NOT noise: a constant RELATIVE 1.22e-5 = (1.10998 - q0_proton)/q0_proton. The
producer used its own recorded 5-decimal q; at that q, |w - Phi_3/ln q| <= 4.3e-6
on every row.

REFUTED — do not quote. w = -Z(2N - Z + 1) matches 18/19 non-hydrogen rows and
FAILS Ar (recorded -498, formula -486). Ar is the ONLY row with N-Z > 1; every
other row is N=Z or N=Z+1. Read off a sample blind to the (N-Z) dependence, and
the one row testing it kills it. Scope (a).

STATUS
  Phi_3 quantum ..... DERIVED (Lean, sorry-free)
  Phi_3 integer w ... OPEN, one candidate refuted
  Phi_1, Phi_2 ...... UNTOUCHED — neither is quantised, so this does not reach
                      them. Phi_3 was the tractable third; the other two are not
                      easier for this being done.

NEXT for w, needing no new mathematics: w = 2*sum_j m_j*s_j, s_j the crossing
sign, m_j the number of chains M_i containing crossing j. So w is a
POSITION-WEIGHTED CROSSING COUNT, and finding it is a question about the
ground-state ORDERING — the exponential minimisation this arc already flagged.
The obstacle is one we already named, which is why I did not push further.

=== A THIRD GATE CATEGORY, worth carrying forward ===

`q0-anchor refill ratchet` was RED on the branch with "NEW (not in baseline): 1"
and GREEN on clean main — so it read as mine. It was NEITHER mine NOR
pre-existing: the branch was 37 commits behind, and a witness main had since
stamped read as newly-unstamped against the newer baseline. MERGING MAIN
CLEARED IT.

So a gate red has THREE possible owners, not two: the branch's change, main's
state, or the branch's STALENESS. Check the third before attributing. Final
state here: this branch's five reds are byte-identical to clean main's five.

Also caught: the stash/checkout dance for the baseline comparison left OTHER
AGENTS' bean edits in my working tree. Reset to HEAD and re-applied only my own
file. A baseline comparison that touches the tree can pick up neighbours' work —
check `git status` before every commit, not just at the end.


=== THE ORDERING IS NOT THE OBSTACLE — I named it wrong (commit fb27763501) ===

The previous entry derived Phi_3's quantum and named the ground-state ORDERING
as the next obstacle for w(Z,N). WRONG, and here is the refutation.

What I missed: w is an EXACT INTEGER already in the tree, so the ordering can be
INVERTED rather than derived. Enumerate every ordering def:atomic-braid allows
(each electron immediately before its proton), compute w, compare.

RESULT over 4 readings of the M_i prose x every allowed ordering, He/Li/Be/B/C:
16 of the 20 (atom x reading) cells do not merely miss — the target is OUTSIDE
the achievable range entirely.

And the failure is STRUCTURED. For Li, Be, B, C the recorded w sits strictly
BETWEEN the weakest weighting (m_j = 1) and the next weakest (m_j = j-1):

    atom  target   max at m=1   max at m=j-1
    Li      -18        -6           -24
    Be      -28        -8           -44
    B       -40       -10           -70
    C       -42       -12           -90

The ordering only slides w WITHIN a family; the target is in the gap BETWEEN
families. No ordering reaches it.

WHY THIS MATTERS MORE THAN THE NEGATIVE. def:atomic-braid's ground-state rule is
an exponential minimisation (C(40,20) = 1.4e11 at Ca), already flagged by this
arc as intractable as written. I had put it on the critical path for Phi_3. IT IS
NOT ON THAT PATH. That removes the one genuinely unsolvable-as-written step from
the Phi_3 problem.

WHERE THE OBSTACLE ACTUALLY IS: upstream of the ordering — the crossing-sign
assignment (Table 1 as read), the chain structure, or the strand content.

SCOPE (a): this construction over these orderings/readings does not reach the
integers. Excludes the ORDERING as the search target, not a construction. He is
reachable (m=1 family) and is least constrained, so it weighs little.

DO NOT, on picking this up: solve for a weight profile m_j that WOULD hit the
targets. That is fitting a construction to its own outputs and the owner
directive of 2026-08-25 forbids it. I deliberately did not do it.

STATUS NOW
  Phi_3 quantum ....... DERIVED (Lean, sorry-free)
  Phi_3 integer w ..... OPEN — but the ordering is RULED OUT as the obstacle,
                        and one closed form (-Z(2N-Z+1)) is refuted by Ar
  Phi_1, Phi_2 ........ UNTOUCHED — not quantised, so neither argument reaches
                        them

NEXT, and it is now a narrower question than before: which of the three upstream
candidates is wrong — the crossing signs, the chain structure, or the strand
content. The Phi_3 integers are 19 exact constraints to test any candidate
against, which is a far sharper instrument than the MeV corrections I started
this arc with.


=== ANSWERED: THE CHAIN STRUCTURE — and two invariants are now RE-DERIVED (4366709e74) ===

Which of crossing signs / chain structure / strand content is wrong: the CHAIN
STRUCTURE, and the error is MINE, not the corpus's.

thm:wedderburn-mass-formula says M_i chains "the crossing matrices of all
strands j > i". I read that as a SUFFIX PRODUCT OF ADJACENT crossings and tested
four variants of that misreading. It means what it says: for strand i, cross
with EVERY strand j > i. Summing over i visits every PAIR once. ALL-PAIRS, with
NO ordering dependence — which is exactly why the ordering inversion failed and
why the target sat in the gap BETWEEN ordering-dependent families.

The corpus already said so: markov-pair-z2.md:137 — the pair weight holds
"regardless of its position in the braid, matching the empirically-verified
all-pairs set". I did not connect it.

RETRACTION, and it is on MAIN. My claim in this arc and in PRs #5743 + #5753
(both merged) that "the published prose does not determine the construction" and
that the formula is "unfalsifiable as written" is WRONG and withdrawn. The prose
determines it; I misread one preposition four ways and never tried the plain
reading. THAT CLAIM IS LIVE ON MAIN AND NEEDS CORRECTING THERE — in
computations/wedderburn_Mi_constructor_test.py's SCOPED banner and
wedderburn_table_binding_recast.py's docstring. Not done in this commit.

RE-DERIVED (signs from HeckeLinearReduction.lean's sorry-free ratio lemmas;
pair counts forced by strand content Z p, N n, Z e):

  Phi_3 = w*ln q,  w = 2[2*C(Z,2) - C(N,2) - Z^2] = -2Z - N(N-1)
      19/19 EXACT, including Ar — the row that REFUTED the earlier candidate
      -Z(2N-Z+1). Held-out confirmation, not a fit.
  Phi_2 = Z*N*ln(1 + h^2/4)
      19/19, worst rel err 5.0e-6 = the 6-decimal publication precision.

Phi_2 also discriminates the pn coefficient: only pn has |det| != 1, and the
recorded values match the UN-DOUBLED (1, -h/2), NOT Table 1's doubled (2, -h).
Both give chirality ratio -1, so Phi_3 is unaffected — which is why Phi_3 held
at 19/19 while Phi_2 decides. (1, -h/2) is symAltRatio_half's exact hypothesis.

CONVENTION C EXCISED (owner directive, received mid-work). Costs nothing here:
Phi_2 and Phi_3 are CONVENTION-FREE — neither uses z at all. The C/D ruling does
not reach them; both stand under D unchanged. Phi_1 is the ONLY invariant using
z, hence the only convention-dependent one.

PHI_1 — NOT SHIPPED, finding recorded here instead. Its probe computed in
convention C and was DELETED rather than committed; zero C sites in what landed.
The provenance finding, as a fact about the recovered artifact and an input to
the C-excision effort:
  Under convention C, minimised over orderings (def:atomic-braid's own
  ground-state rule), Phi_1 reproduced He (-5.55890166 vs -5.558902) and Li
  (-9.83864166 vs -9.838642) at published precision. Be missed under the
  "electron immediately before its proton" constraint, so that constraint is
  too strong or the true ground state lies outside it.
  => the April-2026 producer appears to have been CONVENTION-C. That bears on
     whether the published table is C-frame. OWNER DECISION, not mine.

STATUS
  Phi_2 ..... RE-DERIVED, 19/19, convention-free
  Phi_3 ..... RE-DERIVED, 19/19, convention-free
  Phi_1 ..... open; convention-dependent; C evaluation excised

NEXT: (1) correct the "unfalsifiable as written" claim on main — it is my own
and it is wrong; (2) Phi_1 under convention D, which is the honest way to ask
whether the table survives the C excision at all.


=== BOTH NEXT ITEMS DONE (cf660aaa4f) ===

(1) RETRACTION AT SOURCE. The "unfalsifiable as written / prose does not
determine a unique construction" claim is corrected in the two files on main
that carried it: wedderburn_Mi_constructor_test.py (SCOPED banner) and
wedderburn_mass_table_z1_20.py (my cross-reference). The constructor probe's
numbers are kept as the record of a REFUTED READING and now say so. The table
producer's caveat now says the remaining gap is PHI_1 ALONE, not all three.

(2) PHI_1 DOES NOT SURVIVE THE C EXCISION — measured, convention D only.

    atom   carried Phi_1   min over D    reachable?   rel gap
    He        -5.558902    -4.064853         NO        0.269
    Li        -9.838642    -6.979815         NO        0.291
    Be       -18.272718   -10.642315         NO        0.418
    B        -22.803608   -14.999845         NO        0.342
    C        -24.310734   -17.239301         NO        0.291

0/5. Every carried value lies BELOW convention D's reachable minimum, by
27-42 %. The carried Phi_1 — and therefore the published mass table computed
from it — is a CONVENTION-C ARTIFACT.

COST OF THE EXCISION: excising C does NOT leave the table intact. Phi_1 must be
recomputed under D, moving every published row. OWNER DECISION, same kind as
the beta3 repair. Not taken here.

WHAT IT DOES NOT COST: Phi_2 and Phi_3 are convention-free (neither uses z) and
stay re-derived at 19/19 under D. So the excision's blast radius is EXACTLY ONE
INVARIANT — which is the useful part of the measurement.

Probe: computations/phi1_convention_d_probe.py (D only; the earlier C-computing
probe was deleted, not committed).

SCOPE (a): 400-arrangement cap (reported per row, hit for B and C), five light
atoms, one chain structure. Not a claim that no convention-D construction
reaches these values — only that the one which works for Phi_2 and Phi_3 does not.

=== ARC STATUS ===
  Phi_2 ..... RE-DERIVED 19/19, convention-free
  Phi_3 ..... RE-DERIVED 19/19, convention-free
  Phi_1 ..... open, convention-dependent, and shown to be C-frame
  item 2 .... base masses 44/36 ppm below CODATA, untouched

NEXT, and it is now an owner call rather than a research question: recomputing
Phi_1 under D moves every published row of the mass table. Someone has to decide
whether the table is regenerated (as beta3 was, PR #5781) or the C-frame
provenance is documented and the table left as-is. The measurement needed to
make that decision is done; the decision is not mine.


=== CONVENTION D REGENERATION DONE (97fe14f6d7) — and it is 2.4x LESS ACCURATE ===

Owner authorised 2026-08-29: "recompute Phi_1 (and anything else convention
C -> D)". Done. Producer: computations/wedderburn_mass_table_convention_d.py

TWO OF THE THREE STOPPED BEING CARRIES. Phi_2 and Phi_3 are no longer taken from
the recovered witness at all — both are DERIVED:
    Phi_3 = (-2Z - N(N-1)) * ln q
    Phi_2 = Z*N * ln(1 + h^2/4)
Both reproduced all 19 carried values exactly, so the swap is value-neutral, and
both are CONVENTION-FREE (neither uses z) so C->D does not move them.
Phi_1 is the only z-dependent invariant and is the only thing actually recomputed.

MINIMISATION: exponential (C(40,20) = 1.4e11 at Ca), so swap hill-climbing with
restarts — VALIDATED, not assumed: finds the exact global minimum on all five
atoms where exhaustive enumeration is feasible (He, Li, Be, B, C). Rows record
their regime: 5 exact, 14 local.

THE RESULT:
                        mean |err|     max |err|
    published (conv C)   0.0745925 %   0.190854 %
    recomputed (conv D)  0.182721  %   0.321365 %

2.4x worse on the mean, 1.7x on the max. Every D row shifts POSITIVE, +11 to
+53 MeV. THE CONVENTION EXCISION COSTS ACCURACY ON THIS TABLE.

WHAT IT DOES NOT MEAN: that convention C is right. The 2026-08-15 ruling settled
that on other grounds, and a table fitting better in the superseded convention is
exactly what you expect if it was BUILT in that convention. What it DOES mean:
the published Z=1..20 accuracy figures were convention-C figures, and the honest
D-frame numbers are the ones above.

NOT DONE — OWNER DECISION: replacing the published table. This producer stands
BESIDE the convention-C one rather than overwriting it, because swapping a
20-row published table for one 2.4x less accurate is a content decision. The
numbers needed to make it are in the producer's output.

ARC STATUS
  Phi_2 ..... DERIVED, convention-free, replaces the carry
  Phi_3 ..... DERIVED, convention-free, replaces the carry
  Phi_1 ..... RECOMPUTED under D; costs 2.4x accuracy
  item 1 .... effectively CLOSED — nothing is carried any more
  item 2 .... base masses; the D producer already uses CODATA, so this is
              folded in here rather than outstanding separately

NEXT: the owner call above (adopt the D table or keep C-frame with documented
provenance). No research question is blocking.



=== THE D TABLE IS ADOPTED (owner, 2026-08-29: "adopt the convention-D table") ===

The entry immediately above says "NOT DONE — OWNER DECISION: replacing the
published table. This producer stands BESIDE the convention-C one rather than
overwriting it." THAT IS NOW FALSE and is the reason for this entry: the owner
took the decision and the swap is done. A reader who stops at the previous
section will conclude the C table is still published.

WHAT CHANGED, on branch claude/arc-workplan-review-2026-08-29 (PR #6043):
  - mass-table-z1-20-table-data.ts  -> script/witness rewired to
    computations/wedderburn_mass_table_convention_d.py and its witness.
  - mass-table-z1-20-table-data.md  -> REGENERATED from the D witness. It is
    generated, never transcribed; do not hand-edit a row.
  - mass-table-z1-20.md             -> two new sections: what convention D
    costs (with the C->D and base-mass changes SEPARATED, not quoted together)
    and what is now derived vs carried.
  - wedderburn_mass_table_convention_d.py -> emits a witness via WitnessBuilder
    (it previously printed and saved nothing, so the .ts had nothing to cite).

THE ACCURACY LOSS IS PUBLISHED, NOT BURIED. mean |Delta|/m 0.0746 % -> 0.1827 %,
max 0.1909 % -> 0.3214 %. The block states this as measured and explicitly says
it is not an improvement.

THE TWO CHANGES WERE SEPARATED, because quoting them together would have
misattributed the loss:
    published, conv C, recorded base masses ....... 0.0746 %
    conv C -> D, base masses held fixed ........... 0.1787 %
    base masses recorded -> CODATA, D held ........ 0.1827 %
The convention accounts for nearly all of it. Note the direction of the last
row: using the CORRECT CODATA base masses makes agreement slightly WORSE, which
is what you expect if the formula had been absorbing part of the input error.
I nearly published a wrong D-vs-C attribution by comparing the D producer
(CODATA base masses) against the C table (recorded ones) in one step.

LEAN. The algebra the two derived invariants rest on is proved, sorry-free,
axiom-clean, in QOU/BraidKnot/HeckeLinearReduction.lean: detT_zero / detT_full /
detT_id / detT_half (the |det| = 1 dichotomy that collapses Phi_2 to one term
per p-n pair), one_add_hSq_div_four, symAltRatio_zero / _full / _half, and
chiralityCount_collapse. All over a generic CommRing or Field with h free — no
q, no z, no anchor — which is WHY Phi_2 and Phi_3 are convention-independent.
A tautology I wrote to dodge CommRing division (detT_half_four_mul: A = B - (A - A'))
was DELETED, not kept: it is the vacuous pattern AGENTS.md 1a bans.

TITLE. This bean's title asserted "unfalsifiable as written" until now. I
retracted that claim (see the RETRACTION entries above): "all strands j > i"
means ALL-PAIRS, and I had tested four variants of one misreading without ever
testing the plain one. The filename still carries the older "is not exact at
n=3" phrasing — beans files are named at creation and it cannot be renamed
without minting a new ID. Read the title, not the filename.

ARC STATUS
  Phi_2 ..... DERIVED, convention-free, Lean-proved algebra, 19/19
  Phi_3 ..... DERIVED, convention-free, Lean-proved algebra, 19/19
  Phi_1 ..... RECOMPUTED under D and PUBLISHED; costs 2.4x accuracy
  item 1 .... CLOSED. Nothing is carried.
  item 2 .... CLOSED. The D producer uses CODATA base masses.

WHAT IS ACTUALLY LEFT, and it is not a research question: the owner's judgement
on whether a 2.4x accuracy loss is acceptable now that it is visible in the
published block. If the answer is no, the honest move is to document the C-frame
provenance and revert the adoption — NOT to re-fit Phi_1. Still prohibited,
unchanged: no seventh Delta_lambda ansatz, no parameter beyond CAL-1/2/3, and
sign agreement remains one bit.



=== QUEUED LEAD (not worked): the xzrj arc on main derives a z-dependence I only measured ===

Noticed on a check-in, recorded so it does not evaporate. NOT investigated, NOT
claimed to transfer. Do not treat the connection below as established.

WHAT LANDED ON MAIN (b1e9af9538 .. 9ce3ed2942, bean qou-xzrj, q-beta sector):
"ALL of mu's convention-dependence is derived; only a pure-q constant is still
identified", reaching mu = -dim/([3]_q * y_(2,1)) with the residual gap a
z-FREE constant. Verified same object, not merely the same letter:
qbeta_mu_is_block_invariants_probe.py evaluates y_(2,1)(z_D) at the proton pin
under convention D — the same Markov parameter z = q^3/(q^2+1) that Phi_1 uses.

WHY IT MIGHT BEAR ON PHI_1. Phi_1 is the one z-dependent invariant of the three,
and this arc RECOMPUTED it numerically under D rather than deriving its
z-dependence. The xzrj route factorises a z-dependent scalar into NAMED block
invariants (y_(2,1), [3]_q, dim) and isolates a z-free residue. If Phi_1's
z-dependence admits the same treatment, the D recomputation stops being a
number and becomes a derivation — which is what would actually answer the
2.4x accuracy question rather than merely reporting it.

WHY IT PROBABLY DOES NOT TRANSFER, and this is the honest half. mu is a SCALAR
NORMALISATION. Phi_1 is a MINIMUM over arrangements — exponential in A, hit by a
400-arrangement cap in the earlier probe and by hill-climbing in the producer
(5 rows exact, 14 local). A minimisation over a combinatorial set is not the
kind of object a factorisation into block invariants closes; the min operator
is exactly what blocks a closed form. Different sector too: q-beta decay, not
the mass table.

SO: a lead, at maybe-low odds, whose value is that it is CHEAP TO KILL — read
qbeta_mu_is_block_invariants_probe.py and ask whether anything in it survives
a min(). If the answer is no, write that down and close the lead; a recorded
negative is worth more than an unexamined maybe.

STILL PROHIBITED, unchanged: no seventh Delta_lambda ansatz; NO FITTING; only
CAL-1/2/3 admissible; and a factorisation that reproduces Phi_1 by tuning a
constant against the table is a fit, not a derivation.



=== THE xzrj LEAD IS DEAD — and my objection to it was wrong (PR #6137) ===

Worked the lead I queued above. It dies, but NOT for the reason I recorded, and
the difference matters for anyone who picks this up.

WHAT I HAD WRITTEN: "mu is a scalar normalisation, Phi_1 is a MINIMUM over
arrangements, and min() is exactly what a factorisation into block invariants
does not close."

THAT IS WRONG ABOUT THE MECHANISM. I reasoned from the shape of Phi_1 instead
of reading the producer. In wedderburn_mass_table_convention_d.py::V the
transfer recursion builds (a, b) from the crossing content ALONE, and z enters
exactly once, at the end:

    def V(chain):
        a, b = mp.mpf(0), mp.mpf(1)
        for c, d in chain:
            a, b = a*(c*H + d) + b*c,  a*c + b*d
        return Z_D * a + b            # z appears HERE and nowhere else

So V is AFFINE in z with z-FREE coefficients (verified: divided second
difference over three z points is exactly 0.0), and

    Phi_1(seq) = sum_i log |z*a_i + b_i|.

A min over a finite set of z-free (a_i, b_i) multisets is NO obstacle to a
closed form at all. The min was never the problem.

WHY IT DIES ANYWAY — the coupling I had not considered. The argmin ARRANGEMENT
moves with z. Exhaustive over all arrangements at z_D and z_C:

    atom   Z   N   #arrangements   argmin stable?
    He     2   2               6   yes
    Li     3   4              35   yes
    Be     4   5             126   yes
    B      5   6             462   yes
    C      6   6             924   NO -- it moves

One of five. There is no fixed multiset to factorise: the combinatorial
selection carries its own convention-dependence, and that is what blocks the
xzrj route.

TWO THINGS WORTH KEEPING, so this is not merely "closed, no":

  1. NEAR-SEPARABILITY. 4 of 5 stable means the coupling is weak and localised,
     not pervasive. A future attempt has a sharp question rather than a vague
     one: are the z-free a_i, b_i named block invariants, and is the argmin
     instability confined to a characterisable set of atoms? That is a better
     starting point than the lead had.

  2. A SUBSTANTIVE FACT ABOUT THE ADOPTED TABLE. For carbon, the C and D tables
     do not merely evaluate the same arrangement at two z -- THEY MINIMISE AT
     DIFFERENT ARRANGEMENTS. Stronger than "Phi_1 moved", and not previously
     recorded anywhere in the corpus.

Probe: computations/phi1_z_separability_probe.py (mpmath 50 dps end to end, no
float64; q0 from q_at(50), not the f64 constants.Q). SCOPE (a): five light
atoms, two z points, exhaustive over arrangements. Not a claim about all Z or
all z, and nothing is excluded.

METHOD NOTE FOR MYSELF: I recorded the lead WITH an objection and the objection
was the wrong one. Queuing a lead with a reason it will fail is still better
than queuing it bare -- it made the test obvious -- but the reason has to be
checked against the code, not inferred from the shape of the formula. Reading
V() took two minutes and overturned it.

## 2026-09-12 — Φ₁ IS closed, and no real *z* makes it the recorded column

Probe [`phi1_closed_form_and_no_z_reproduces_it_probe.py`](../computations/probes/phi1_closed_form_and_no_z_reproduces_it_probe.py),
19/19; audit [`2026-09-12-phi1-closed-form-and-no-z-reproduces-it.md`](../docs/audits/2026-09-12-phi1-closed-form-and-no-z-reproduces-it.md).

**Φ₁ was recorded as "NOT closed" in `phi_allpairs_reconstruction.py`'s own
header. It is closed.** Every crossing in Table 1 is `c·σ + d·1` in the *same*
`σ = [[h,1],[1,0]]`, so one diagonalisation gives

    Φ₁(z) = Σ_i ln|P_i(z + 1/q) + Q_i(q − z)| − (n−1)·ln(q + 1/q),
    P_i = Π_{j>i}(c q + d),   Q_i = Π_{j>i}(−c/q + d)

verified against the literal 2×2 matrix product to **3.1e-39**. Φ₁ is closed in
exactly the per-pair data that closed Φ₂ and Φ₃; what it is not is per-pair
*additive*. At `z ∈ {q, −1/q}` one factor drops and it collapses to
`Σ_{i<j} ln|c q + d|` — the sibling probe's eigenvalue condition, confirmed
numerically (3.3e-39).

**🛑 And I predicted the opposite about ordering.** From the non-multiplicativity
of `f` I expected Φ₁ to depend on the strand arrangement and on the order of `j`
inside `M_i`, and said so before measuring. Measured: identical to 10 digits
across five arrangements and both `j`-orders (spread 1.3e-39). The inference was
invalid — the matrices commute exactly (max commutator **0** over all 81 ordered
pairs), being polynomials in one `σ`; the transfer algebra is `ℝ[x]/(x²−hx−1)`.
So this bean's own retraction (*"an ALL-PAIRS braid with no ordering
dependence"*) is right, and right for a stronger reason than it gives: it covers
Φ₁ too, not only the two multiplicative invariants.

**No real `z` reproduces the recorded Φ₁ column.** Φ₁(z) has `n−1` poles and is
unbounded below, so the test is consistency — one parameter, 19 constraints.
Best achievable worst-miss ≈ **5.2 (520 %)** at Ar on `A+Z`, ≈ **6.4 (640 %)** on
the electron-free `A` reading. **Quote the order of magnitude, not the
minimiser** — the best `z` moves with the scan grid (1.0537 at 2001 points, 0.926
at 401) because the basin is shallow and ragged. The three documented `z` fail
two ways independently: Φ₁ > 0 at C, D and `z=q` on every row from B up while
every recorded value is negative; and Φ₁ is Θ(n²) (density varies 6.1× over
`n = 6..60`) while the recorded column is Θ(n) (12.4×, falling monotonically).

**What it relocates.** The β₃ probe established the recorded **Φ₃** column *is*
the theorem's Φ₃ at the documented anchor. So the recovered producer agrees with
the published formula on **Φ₂ and Φ₃** and disagrees on **Φ₁** — two of three
invariants shared. The 14.2 % β₃ departure and the Φ₁ disagreement sit on the
same object and neither is explained by the anchor: the table is neither the
formula's output nor unrelated to it.

**Scope.** Scope-(a) turning on a named class — the theorem's own Φ₁, all-pairs
reading, Table 1's crossings, any **real** `z`, on `A+Z` and `A`. Not excluded: a
different `M_i` reading, a complex `z`, a different crossing table, or the
recorded column being some other quantity. The quark readings (`3A`, `3A+Z`) are
**not testable here** — Table 1's rows are nucleon- and electron-typed. No
replacement `z` or coefficient is proposed.

**Still open, so this bean stays open (rule 13a):** what the recorded Φ₁ column
actually *is*, if not the theorem's Φ₁; the β₃ vs `h_A²` authoring question
(owner's call); whether a quark-level crossing table would change the `z` scan.

## 2026-09-12 (later) — the recorded Φ₁ column matches NO reading of the theorem's Φ₁

Probe [`phi1_recorded_column_matches_no_reading_probe.py`](../computations/probes/phi1_recorded_column_matches_no_reading_probe.py), 15/15; PR #7232.

The entry above showed no real `z` reproduces the recorded column under the
**all-pairs** reading. This asks whether it is some *other* reading — the four
`wedderburn_Mi_constructor_test.py` swept and then retracted were tested against
the **deuteron**, never against the **Φ₁ column** — and the answer is no.

**The growth exponents settle it with no fit.** Log-log least squares over the
table's own range `n = 6..60`: recorded column **0.911** (essentially linear),
theorem's Φ₁ at `z_D` **2.704** (faster than quadratic). `z` cannot move an
exponent — it enters each of the `n−1` terms as a bounded factor, `O(n)` total.

**And no reading fits**, each at its own best `z` over a 401-point scan on
`[−20,20]`: chain length `L=1` 33.8 %, `L=2` 95.2 %, `L=3` 33.0 %, `L=5` 64.8 %,
`L=all` 604 %; any linear-in-`(Z,N)` form 146 % (at He); the all-pairs counts
with three free coefficients 59.9 % (at C). The linear family needs only **one**
least-squares: the adjacent-pair counts for `p^Z n^N e^Z` span the same affine
space as `(Z, N, 1)`, and the two give byte-identical residuals (check 4 asserts
this rather than assuming it).

**🛑 Corrects the entry above, and its audit doc and PR body.** Both said *"Φ₁ is
Θ(n²) — its per-pair density varies only 6.1× across n = 6..60"*. The label is
right asymptotically; the parenthetical offered as **evidence** shows the
opposite, since a density that *rises* 6.1× is growing faster than `n²`. The
conclusion (incompatible growth) is unaffected and is stronger. Fixed in the
audit doc, the probe docstring and the PR body — not in one place only.

**What it means.** With the recorded **Φ₃** column being the theorem's Φ₃ at the
documented anchor, the recovered producer shares **two of three** invariants with
the published formula and its Φ₁ is a different object. Identifying that object
now needs the **recovered witness itself**: every reading the definition admits
is excluded.

**Scope.** Scope-(a) on a named class — readings expressible as a product of
Table 1 crossings along `p^Z n^N e^Z`, via the theorem's bilinear form, real `z`
in `[−20,20]`. **Not excluded:** a different crossing table; a **complex** `z`; a
reading that is **not a product of crossings at all** — the theorem's own table
calls Φ₁ *"trace of Markov-weighted product"*, and a **single trace** rather than
a sum over generators is **untested**; or a transcription error in the column. No
candidate generator is proposed or adopted.

**Bean stays open** (rule 13a): the single-trace reading is untested, and what
the column actually is remains unknown.


## 2026-09-12 — the single-trace reading is EXCLUDED too; growth class localises it

The line immediately above says the single-trace reading is untested. **It is now
tested, and it fails.** `computations/probes/phi1_single_trace_reading_is_excluded_too_probe.py`
(25/25, exit 0, PR #7250), on the 13 rows whose per-atom `ordering` survives in
the recovered witness.

**Excluded.** Best member of the whole z family: **71.2 %** of the recorded
column's own RMS — **20.90 absolute** against a column RMS of **29.34** — and the
minimiser sits **on the scan boundary** at z = 20. Widening the scan does not
rescue it: the z → ∞ limit with a free additive constant is **94.2 %** (adjacent)
/ 104.4 % (all-pairs), *worse* than the boundary. The `+ln` sign convention is
118.7 % / 295.2 %. On 12 of 13 rows the sign is simply opposite — the recorded
column is negative and falling, the single trace positive and rising.

**The informative half — the growth class matches.** Effective exponents over the
same 13 rows: recorded **1.078**, adjacent single trace **1.001**, all-pairs
single trace 2.067, the theorem's displayed sum **2.704**. Neither z nor an
additive constant can move an exponent. So the producer's Φ₁ is a **linear-in-n
object on the adjacent chain**, and the theorem's sum-over-chains is the **wrong
growth class outright** — a stronger objection than any residual. First candidate
to get the growth right and the values wrong.

**Quote the exponent with its population.** 0.911 (n = 6..60, all 20 published
rows, sibling probe) and 1.078 (n = 6..40, the 13 rows with surviving orderings)
are different row sets. Both measured; **neither corrects the other**; the
exponent drifts down as heavier atoms enter. Both far below 2.704.

**A structural argument I expected to make and could not.** The crossings commute
(all are `c·σ + d` in one σ), so the adjacent product has eigenvalues
`P = Π(cq + d)`, `Q = Π(d − c/q)` and `ln|tr M| = ln|P + Q|`. I expected one to
dominate — which would collapse it to a sum of per-pair constants and make this
test a redundant special case of the already-excluded adjacent-additive class.
**Measured: no dominance.** `|Q/P|` runs **0.812 … 2.839**, no decay with n. The
interference term survives; the test was independent.

**Two corrections, both mine, made before the probe landed.** An earlier draft
called the z → ∞ limit "strictly more generous than any finite z" — the families
are **not nested** and the numbers contradict it. And it carried **78.7 %** for
that tail from a throwaway scratch script; two independent standalone
recomputations give **94.2 %**. Do not quote 78.7 %.

**Where this leaves the bean.** With the single-trace reading gone, **no reading
of the theorem's Φ₁ built from Table 1's crossings matches the recorded column** —
not the all-pairs chain, not any truncated chain, not any linear-in-(Z,N) form,
not the whole adjacent-additive class with six free constants, and not the single
trace. What the producer computed is **unknown**, and the only positive constraint
in hand is the growth class: linear in n, on the adjacent chain.

No replacement functional, coefficient or generator is proposed — fitting one to
the column is the selection-against-the-target the 2026-09-05 anti-fit directive
forbids.

**Bean stays open** (rule 13a).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-12 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Domain & adjacent-chain growth constraints formalized in Lean and verified in `wedderburn_Mi_constructor_test.py` (PR #8145)

- **Lean formalization (`folio/quantum-observable-universe/mass-theory/wedderburn-mass-formula.lean` & `folio/quantum-observable-universe/lean/QOU/Mass/WedderburnMassFormulaCoefficients.lean`, wired into `QOU.lean`):**
  - Strengthened `extremal_irreps_count` with a non-vacuous proof (`d_std = n - 1 ∧ d_std >= 2` using `hn : n >= 3`).
  - Proved `extremal_exhausts_iff_n_le_three` (`extremalIrrepCount n = partitionCountLow n <-> n <= 3` on `1 <= n <= 4`) and `non_extremal_irreps_at_n_eq_four` (`partitionCountLow 4 - extremalIrrepCount 4 = 2`, corresponding to `[2,2]` and `[2,1,1]`).
  - Proved `adjacentChainPairCount_eq_allPairsCount_at_two` (`1 = 1` at `A = 2`) and `adjacentChain_twice_lt_allPairs_twice` (`2 * adjacentChainPairCount A < A * (A - 1)` for all `A >= 3`).
- **Python probe & witness (`computations/wedderburn_Mi_constructor_test.py` -> `computations/wedderburn-mi-constructor-test.witness.json`, 4/4 assertions passed):**
  - Verifies the partition-exhaustion boundary (`n <= 3` vs `n >= 4`), the adjacent-chain vs all-pairs growth table (`A = 2..6`), the exact algebraic coefficient relation `2*beta_3 + beta_2 + 6 = 0` (`< 1.1e-50` at 50 dps), and the 8-cell constructor grid on deuterium.
- Status kept `in-progress` (rule 13a / owner decision on `Phi_1` table adoption). PR #8145 (`ed78b60a0ffe233f132df45a37bb1456ec237832`).

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

Claim released. Blocked on the owner decision about adopting the D Φ₁ table (entries above). Open batch PR #8145 (W4's queue) adds counting lemmas and a probe; not reviewed here. Stays open (rule 13a).
