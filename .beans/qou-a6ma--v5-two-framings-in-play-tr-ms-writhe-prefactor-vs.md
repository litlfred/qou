---
# qou-a6ma
title: 'V5: TWO framings in play -- tr_M''s writhe prefactor vs T(t) as a free datum'
status: todo
type: task
priority: normal
created_at: 2026-08-10T18:34:14Z
updated_at: 2026-08-10T18:34:15Z
---

FOUND IN CORPUS (owner was right, tr_M normalization is there).
braids-and-knots/markov-axioms-primitive.md: 'the negative-crossing loop value z_-
differs from z whenever q != +-1 ... Link invariance of the Jones polynomial is
instead restored by the WRITHE PREFACTOR OUTSIDE THE TRACE.'

So tr_M alone is a FRAMED (regular-isotopy) invariant and the writhe prefactor is
the framing correction -- i.e. the framing implicit in tr_M is the writhe/
blackboard framing, DETERMINED by w.

THE TENSION: strand-twist-datum.md asserts T(t) is a FREE extra datum --
'over any fixed braid word -- hence any fixed writhe w -- there exist framings
with distinct total twist' -- and calls it 'the framing that the ribbon structure
of the braided category carries'. Two problems:
  (a) If T(t) is THE framing, it collides with the tr_M framing, which is fixed by
      the writhe prefactor. Two different framings on the same object.
  (b) In a genuine RIBBON category the twist theta is CANONICAL (determined by the
      braiding), not free. For Hecke its exponent is the content sum. So 'ribbon
      structure' and 'freely assignable' cannot both hold.
And theta = contentSum/3 was already TESTED and FAILS (n=3 gives integer charges
{+1,0,-1}, no n<=8 gives both quark charges) --
computations/ribbon_twist_charge_quantum_probe.py.

QUESTION TO SETTLE: are the tr_M framing and T(t) the same framing? If yes, T(t)
is writhe-determined and the candidate collapses. If no, the corpus carries two
unrelated framing notions and must say so explicitly.
