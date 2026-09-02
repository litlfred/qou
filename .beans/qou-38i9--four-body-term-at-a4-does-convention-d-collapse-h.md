---
# qou-38i9
title: 'Four-body term at A=4: does convention D collapse H_12 to two-row partitions?'
status: completed
type: task
priority: normal
created_at: 2026-09-01T05:16:22Z
updated_at: 2026-09-01T05:34:40Z
---


RESOLVED 2026-09-01 -- computations/probes/four_body_term_and_the_h12_collapse_probe.py,
6/6. Yes, it collapses, and the four-body term is measured.

THE WALL WAS AN ARTIFACT. Convention D puts the three-strand q-antisymmetriser in
the radical (y_alt = 0) -- the N=2 specialisation -- and that does not stop at
n=3: EVERY partition with >= 3 rows has weight exactly zero at every strand
count. Verified against load_cost: n=6 has 4 nonzero blocks of 11, n=9 has 5 of
30. The survivors have a closed form,

    y_(n-k,k) = [n - 2k + 1]_q / Z,   Z from sum(y . dim) = 1,   q = q0

with [m]_q the balanced q-integer. Exact at n=9 (0.0e0); 1.14e-8 at n=6, which is
load_cost's own stored-f64 floor, so the closed form is the MORE precise of the
two.

H_12 IS THEREFORE 7 BLOCKS, NOT 77: dims 1, 11, 54, 154, 275, 297, 132, largest
297, built in 0.04 s, sum y.dim = 1.000000000000000. For scale, qou-sv7h reports
278 s for a single A=2 deuteron through the production path.

REACH (note the largest block is NOT at the largest k -- at n=18 it is at k=7):
    A=4  n=12  largest  297  dense, comfortable
    A=5  n=15  largest 2002  dense, comfortable
    A=6  n=18  largest 13260 needs sparse handling
    A=7  n=21  largest 90440 out of reach

CROSS-VALIDATED BEFORE USE. H_12 reproduces L_pp/L_pn/L_nn to 1.3e-13..3.4e-13,
band-routed bonds at separation 2 AND 3 to 3.4e-13 (extending no-distance-decay
one step further out), and the ppn triangle to 3.69e-10 at matching bond order.

NEW ARTIFACT FOUND ON THE WAY -- BOND INSERTION ORDER. Bonds do not commute, so
the order they enter the word changes the answer: 11.12 % over the six orderings
of one A=3 triangle, 38-40 % over 4He's six bonds (B ranging 8.04..12.43 MeV).
Four of the six triangle orderings agree exactly; the two outliers are precisely
those with the band-routed bond sandwiched between the two adjacent ones -- the
only pair that fails to commute. atom_gen_chains fixes an INTERLEAVED order
(N0.N1.b01.N2.b02.b12.N3.b03.b13.b23) that had never been lifted to the strand
picture. This artifact is much larger than the framed/writhe-normalised question
qou-6pt7 and qou-kb25 spent two probes on.

CORRECTS qou-bc09. That probe appended all bonds after all nucleon words, giving
ppn = 1.607030798 where production gives 1.503488161673; its three-body term for
ppn moves from -0.236512 to -0.340055. Still negative and LARGER, so its
conclusion strengthens. Its A1/A2 (attachment rank), A5 (no-decay) and A6
(ceiling direction) do not depend on bond order. Forward pointer added there.

THE FOUR-BODY TERM (Mobius inversion over nucleon subsets, production order):

    order   L_K4        sum c2     sum c3      c4          B (MeV)   vs AME
    ppnn    2.4814437   4.104448  -1.378216  -0.2447883   10.38728  -63.29 %
    pnpn    2.4479530   4.104448  -1.411419  -0.2450763   10.24709  -63.79 %
    pnnp    2.4456031   4.104448  -1.184297  -0.4745478   10.23725  -63.82 %
    nppn    2.4457390   4.104448  -1.638540  -0.0201687   10.23782  -63.82 %
    npnp    2.4479530   4.104448  -1.411419  -0.2450763   10.24709  -63.79 %
    nnpp    2.4814437   4.104448  -1.378216  -0.2447883   10.38728  -63.29 %

NEGATIVE in all six, and in 80/80 random bond orders -- the sign survives the
ordering artifact entirely. sum c2 = 4.104448 reproduces the independent naive
sum L_pp + 4 L_pn + L_nn to 1.7e-12.

THE BOUND CLOSES, UNCONDITIONAL AND WORSE:
    B(2H)  exact                2.833163 MeV
    B(4He) MEASURED            10.387277 MeV   AME 28.295661   -63.29 %
    model B(4He)/B(2H) = 3.6663   AME 12.7196   short 3.4693x

qou-bc09's conditional bound was 2.0975x; measuring the missing term moved it to
3.4693x, in the predicted direction. Even the most favourable ordering convention
tried (12.4267 MeV) is short by 2.8999x. alpha cancels throughout.

FOR L2 1PPQ: end of the line for the bond graph. 8 meV of 28.3 MeV against a
construction that is 2.9-3.5x short with every many-body term measured pushing
the wrong way. The convention questions in qou-6pt7 / qou-kb25 move 1-3 % and are
irrelevant at this scale.

CAVEAT: the n=12 weights are RECONSTRUCTED (no y_lambda source exists for n=12).
The closed form is verified at n=6 and n=9 before use and every H_12 quantity
with an H_6/H_9 counterpart is cross-checked, but it remains a reconstruction.
