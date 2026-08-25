---
# qou-1jw9
title: 'GAP: thm:wedderburn-mass-formula is unfalsifiable as written — no unique M_i, no producer'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T07:10:47Z
updated_at: 2026-08-25T16:45:54Z
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
