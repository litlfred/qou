---
# qou-qb8e
title: 'HH^1 carrier: the MAGNITUDE channel — the actual open gate for c_3'
status: todo
type: task
priority: high
created_at: 2026-08-08T10:15:00Z
updated_at: 2026-08-08T10:15:00Z
---

Successor to qou-qb8b + qou-qb8d, which between them settled the PARITY channel
for the HH^1 fibre-level c_3 carrier:

- qou-qb8b: bar-parity of the outer CLASS is normalization-dependent
  (Hilbert 90 over Q(zeta)/Q(zeta)^+) -- carries no information.
- qou-qb8d: bar-parity of the tr_M-PAIRED NUMBER is well defined against
  structural pins (He-Nie generator + Ocneanu trace), is NOT trace-blind, and
  is MIXED with a NONZERO bar-ODD component.

Net: the bar-parity obstruction that closed every real-q0 route does NOT close
the HH^1 route. The parity screen is PASSED. That was the cheap channel.

THE ACTUAL GATE IS MAGNITUDE, and it is untouched. Nothing so far reproduces
c_3's value (-2.0202 at the cache q0) or, more importantly, its ANCHOR SWING
-- the cross-anchor variation that is the whole reason c_3 is tier
'cal-anchored' rather than 'derived'
(docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).

What a real attack needs, in order:

1. **A map from the outer class to a NUMBER at the substrate anchor.** The
   n=3 pairing gives numbers in Q(zeta)[z]. c_3 is evaluated at real q0 ~
   1.10998, which is NOT a root of unity. Per AGENTS.md §"Im(q) at fibre vs
   observable level" the correct target is a HABIRO-RING element whose
   archimedean evaluation at q0 reproduces c_3 at THAT anchor. So the
   root-of-unity values must ASSEMBLE (over all zeta) into a Habiro element --
   that assembly is the real content and is not started.

2. **The Bring case.** n=3 is the mechanism; the Bring fibre is H_5 at zeta_5
   (bean qou-jcmw, for the DIMENSION count -- explicitly NOT its parity leg,
   see qou-qb8b).

3. **A falsifiable magnitude prediction BEFORE looking at the target.**
   Formalize-first: state what the construction predicts, then compare. Fitting
   a normalization to land on -2.0202 is a FIT, is the seventh-ansatz failure
   mode the corpus already names, and must not be wired.

ANTI-FIT GUARDRAIL (load-bearing): the parity result is NECESSARY, NOT
SUFFICIENT. Do not let "the parity works" license a magnitude fit. A derived
c_3 must come out of the construction with its normalization pinned in advance.
