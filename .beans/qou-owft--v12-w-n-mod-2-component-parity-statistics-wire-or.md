---
# qou-owft
title: 'V12: (w-n) mod 2 = component parity = statistics -- wire or decline'
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:30:52Z
updated_at: 2026-08-15T22:31:55Z
---

OPPORTUNITY, and it needs a ROAST before anyone wires it.
(w-n) mod 2 = component parity, and the framework's tube counts then give:
  lepton 1 comp -> 1 -> fermion ; meson 2 -> 0 -> boson
  baryon 3 comp -> 1 -> fermion ; Hopf/gluon 2 -> 0 -> boson
i.e. the ONLY Markov invariant of (writhe, level) is exactly fermion/boson
statistics, parameter-free.

ROAST FIRST -- two reasons this is weaker than it looks:
 (a) (w-n) mod 2 = c mod 2 is a STANDARD braid-theory identity (permutation
     sign), not a discovery about the framework. Zero framework content.
 (b) The physics alignment follows from the TUBE-COUNT assignment (baryon=3,
     meson=2) plus the fact that 3 is odd and 2 is even. It is close to
     definitional, NOT an independent prediction.
What WOULD be content: deriving the tube counts, or finding a state where
component parity and the assigned statistics DISAGREE (a falsification test).
Do not wire this as a derivation of spin-statistics.


DECIDED 2026-08-11: **DECLINE**. The roast above was right, and worse -- the
physics alignment does not merely lack content, it FAILS.

The gluon unit sigma_1 sigma_2^-1 in B_3 has a 3-CYCLE permutation, so its
closure has ONE component, hence odd, hence 'fermion' under the reading. The
gluon is a boson. (This also corrects an in-session claim that the gluon unit
closes to two components; it does not.) Proved in WritheLevelParity.lean as
statistics_reading_fails_on_gluon, and the seven-carrier table is computed from
the braid words rather than asserted.

So (w-n) mod 2 = c mod 2 stands as a theorem -- it is the COMPLETE Markov
invariant of the level pair (markovPair_parity soundness + markovPair_of_even
completeness, with w, w-n, w+n each shown non-invariant) -- but it is a standard
permutation-sign identity with zero framework content, and its physical reading
is refuted. DO NOT WIRE. Legitimate use: a one-bit consistency check on
level-crossing claims.

Task was 'wire or decline'; the decision is made, so this is closed rather than
scrapped. Bean was left at 'todo' after PR #4961 merged.
