---
# qou-6pt7
title: 'Framed vs writhe-normalised bonds: reconcile the two arcs and fix the pn writhe sign'
status: completed
type: task
priority: normal
created_at: 2026-09-01T04:51:51Z
updated_at: 2026-09-01T04:52:08Z
---


RESOLVED 2026-09-01 -- computations/probes/framed_vs_writhe_normalised_bonds_probe.py,
6/6.

The one convention difference between this arc (mt7r) and qou-brng was the term
-(e/2) log(1-h) that their L carries and my measured Markov traces do not. It is
not a disagreement: MINE IS THE FRAMED trace ratio -log(z+d), THEIRS IS THE
WRITHE-NORMALISED one, mu_eff = mu (1-h)^(e/2), which is the corpus's own
tabulation in stacked_interface_writhe_normalised_probe. Two objects. That is
precisely why the -log(z+d) cores agreed to 1.3e-13 while the full L values did
not -- they were never meant to.

e IS THE WRITHE, and the convention is forced: a bond sigma - beta h equals
(1-beta) sigma + beta sigma^-1 (verified symbolically), so its expected writhe is
1 - 2 beta.

DEFECT FOUND -- the pn writhe is passed with the opposite sign:

  bond  beta            1-2beta      as coded     match
  pp    0               +1           +1           yes
  nn    1               -1           -1           yes
  pn    1/2 - delta/4   +delta/2     -delta/2     NO

Source comment states the value but no justification ("# production
de['pn'] = -delta/2"). Correcting raises L_pn by 1.6133e-4 (0.0238 %), worth
2.70e-3 MeV on 4He (0.0095 %). No conclusion on either arc moves, but L_pn is
consumed by at least five probes so the fix belongs upstream, not per-probe.

THE CHOICE IS MATERIAL AND STRUCTURED. The writhe term is +0.1173 e: it raises
p-p, lowers n-n, barely moves p-n. It compresses the bond-type spread by 56 %
(0.417363 -> 0.182829), which is the quantity the mirror-pair ordering rests on.
Per isotope the conventions differ by up to 6.4 % of AME, and ONLY where Z != N
-- at Z = N the p-p and n-n shifts cancel exactly, so 2H/4He/6Li move < 0.02 %
while the mirror pair 3H/3He splits 5.8 / 6.4 %.

WHICH convention binding should use is a PHYSICS question not settled here.
Framing is Tw in Lk = Wr + Tw. Note the lead this opens: bean qou-rhfy records
the corpus asserting Q = w/2, under which (1-h)^(e/2) = (1-h)^Q is a CHARGE
normalisation -- which would explain why the two conventions differ only where
charge asymmetry lives. Following that next.

NO-DISTANCE-DECAY SURVIVES BOTH. The band generator's conjugator g = T5 T4 T3 has
writhe +3 against -3, net zero; conjugation preserves writhe, so far and adjacent
bonds carry identical writhe and no_distance_decay_in_the_trace_probe's
conclusion holds framed and normalised alike.

TRAP RECORDED: framed 3He lands at -0.01 % of AME. Coincidence of the naive sum,
not agreement -- the measured H_9 trace of the same three-bond word gives 7.0196
(pairwise_ceiling_is_overstated_probe). Only the DIFFERENCE between the columns
is meaningful in that table.
