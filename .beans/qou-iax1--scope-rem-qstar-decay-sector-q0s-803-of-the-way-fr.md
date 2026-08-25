---
# qou-iax1
title: 'SCOPE: rem-qstar-decay-sector-q0''s ''80.3% of the way from proton to muon'' is convention-C; under D q* leaves the anchor interval entirely'
status: todo
type: task
priority: normal
created_at: 2026-08-23T16:55:28Z
updated_at: 2026-08-23T17:10:03Z
---

Found while checking whether the C-frame alpha in QBetaQStarClosedFormExclusion.lean (qou-um5h) endangers the q* exclusion argument. IT DOES NOT -- but it does move q*.

WHAT MOVES. The closed-form shape Phi(q) = Q_A_over_me * cos(alpha - b*hbar^2/2) * (1-u^2) * (1 - Vol41*u^3) carries alpha = (z-1)h/2, and z is convention-dependent. At q0: z_C = 0.49932 -> alpha = -0.052336; z_D = 0.61269 -> alpha = -0.040487, a 23% shift. Rooting Phi(q) = Q_codata/m_e:

    conv C   q* = 1.10997859340   INSIDE the [proton, muon] anchor interval
    conv D   q* = 1.11023370740   19,921 ANCHOR-GAPS OUTSIDE it

The anchor interval is only 1.281e-8 wide (proton 1.1099785827513808, muon 1.10997859555733471), and D displaces q* by 2.55e-4.

CONSEQUENCE FOR THE CONTENT BLOCK. content/quantum-observable-universe/mass-theory/rem-qstar-decay-sector-q0.md states "It lies ~80.3% of the way from the proton anchor toward the muon anchor." THAT SENTENCE IS CONVENTION-C-FRAME. Under D, q* is not between the anchors at all.

WHAT SURVIVES, and this matters:
 * The block SKEPTICAL CONCLUSION is unaffected, and is if anything strengthened. Its argument is that the 80.3% is "a reading of Vol(4_1) own value" -- every constant in a window of width 0.0491 places a zero between the anchors -- so the position was never evidence. Under D the position is not even in the window.
 * The LEAN IS UNTOUCHED. qstarRootStrictMonoInAnchor and qstarRootUniqueInAnchor are stated about an ABSTRACT Phi with a StrictMonoOn hypothesis and never mention qstarShape, z or alpha. And the numerical premise still holds under D: Phi(q*) = -3.606 (vs -3.631 under C), nonzero and same sign. The exclusion result is convention-independent.
 * qstarShape itself is a C-frame def that NOTHING in the file consumes -- it is documentation of the shape.

RELIABILITY CAVEAT ON MY OWN NUMBER. My Phi is a reconstruction from the Lean def, not the block producer. Under C it lands 3.35e-10 relative from the block stated q*, which is 2.9% of the 1.28e-8 anchor gap -- so MY PERCENTAGE POSITION UNDER C (83.2%) IS NOT RELIABLE and should not be quoted against the block 80.3%. The D result is insensitive to that: a 2.55e-4 displacement is 20,000 gaps, so no plausible constant-vintage difference changes it.

ACTION: re-scope the one sentence, or re-derive q* under D with the canonical producer. Do NOT delete the block reasoning -- it is careful and its conclusion holds.

CONFIRMED WITH THE CANONICAL PRODUCER 2026-08-19, and a SECOND finding fell out.

Probe: computations/qbeta/qstar_anchor_interval_convention_probe.py -- ASSERTIONS PASS, mpmath end to end at 50 dps, no float().

1. THE CANONICAL CHAIN IS CONVENTION-C AT ITS ROOT, not just my reconstruction. qbeta_utils.substrate_ladder_quantities line 155 sets z = 1/(sq + 1/sq) = 0.499320334183694452, exactly the C form; the same module markov_parameter at line 53 returns sqrt(q)/(1+q), the other C spelling. Both C spellings in one file, mirroring the Lean. alpha_C = -0.052336120268, alpha_D = -0.040485777341.

2. THE POSITION IS CONVENTION-DEPENDENT. Running the shipped chain unchanged except for z:

     conv C   q* = 1.109978593403397377552   83.180188 %   INSIDE the interval
     conv D   q* = 1.110233707395498707329   1992234.6 %   19921.3 gaps OUTSIDE

   anchor gap 1.2806e-8; C->D displacement 2.551e-4 = 19921.5 gaps.

3. SECOND FINDING -- THE BLOCK FIGURE IS ALSO STALE, independently of convention. The shipped c3_target_at roots at 1.1099785934034; the block states 1.10997859303152. That is 3.35e-10 relative, which is 2.9% OF THE 1.281e-8 ANCHOR GAP. So today producer puts the landmark at 83.2%, not the block 80.3%. Constant vintages, presumably. Any percentage quoted in this interval is hypersensitive at the 1e-10 level and should carry that warning.

WHAT IS NOT CLAIMED: the D column is NOT "q* under convention D". Substituting z_D into a C-frame relation is the move AGENTS.md forbids for the c_k ladder, and the objection applies here. The D column measures SENSITIVITY, which is all that is needed to scope one sentence. A real D-frame q* needs the ladder re-derived (qou-cds1).

BLOCK ARGUMENT UNAFFECTED and arguably strengthened -- its point is that the position was never evidence because every constant in a 0.0491-wide window places a zero between the anchors; under D it is not even in the window.

ACTION REMAINING: re-scope the one sentence AND refresh the 80.3 -> 83.2 figure, or state the figure with its sensitivity. Not applied here.

RETRACTION 2026-08-19, same day. MY "SECOND FINDING" WAS WRONG.

I reported that the block stated q* and its 80.3% were STALE against today producer. THEY ARE NOT. I drew Q_codata from experimental_constants.Q_NEUTRON_MEV (0.7823334093100222) while the block own producer uses substrate.codata_constants.Q_BETA_MEV (0.78233341). The two differ by 8.8e-10 relative, and at dq*/dQ_beta = -0.539 that is a 3.7e-10 shift in q* -- 2.9% of the 1.281e-8 anchor interval, EXACTLY the discrepancy I saw and attributed to the block.

With the producer own constants the probe reproduces q* = 1.109978593031523288402328, matching the block 1.10997859303152 to 2.96e-15, at 80.2763% -- the block 80.3%. Running the cited producer qbeta_c3_imq_qstar_ladder_amplification_probe.py directly gives q* = 1.109978593031523288402328 and 79.744% muon-ward. THE BLOCK IS FAITHFUL TO ITS PRODUCER and both of its 80.3% figures are correct.

I also verified the block internal consistency claim before the retraction, and it HOLDS: the q* anchor-interval position and the Vol(4_1) window position agree to 8.6e-6 percentage points. The block "the same figure" is exact.

WHAT THE ERROR INADVERTENTLY DEMONSTRATED is the block OWN point: an 8.8e-10 change in Q_beta moves the landmark ~3 percentage points across the anchor interval. That is precisely the hypersensitivity the block warns about (dq*/dQ_beta = -0.539), arrived at by walking into it.

WHAT STANDS, unchanged: the CONVENTION finding. With the correct constants,
    conv C   q* = 1.109978593031523288402   80.276273 %   INSIDE
    conv D   q* = 1.110233707021087740936   1992231.7 %   19921.3 gaps OUTSIDE
C->D displacement 2.551e-4 = 19921.5 gaps, which is 690,000x the constant-choice artifact. The block sentence placing the landmark between the anchors remains CONVENTION-C-FRAME.

REMAINING ACTION is now SMALLER than I said: no figure refresh is needed. Only the convention scoping, and that still wants a D re-derivation (qou-cds1) rather than a z-swap.
