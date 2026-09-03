---
# qou-n4zp
title: 'Alpha-cluster scale must come from outside the trace channel: 20.6-33.8% supplied'
status: completed
type: task
priority: normal
created_at: 2026-09-03T04:19:27Z
updated_at: 2026-09-03T04:24:42Z
---

## Measured 2026-09-03 — `alpha_scale_is_outside_the_trace_probe.py`, 4/4

The corpus's remaining extensive carrier is the alpha-cluster term
(`2026-08-02-alpha-cluster-su4-extensive-term.md`): STRUCTURE derived via the
proved SU(4) gate `dim [1^A] = C(4,A)`, **SCALE open** at ~29.8 MeV/alpha
(B/n_alpha constant to CV 0.053 across 4He/8Be/12C/16O).

**Can the trace channel supply that scale? No.**

    A=4 chain (3 adjacent bonds)     ->   6.152 MeV
    A=4 complete graph, best order   ->  10.083 MeV
    alpha-cluster scale                  29.800 MeV/alpha

    trace supplies 20.6 % to 33.8 % of ONE alpha

and the upper figure already assumes the complete graph with every interference
term, which the preceding work showed is the most the bond topology can produce
(additive capped at 20.649 MeV with per-bond values FREE; non-additive at 10.083
with the A=4 many-body sign measured NEGATIVE). **Two thirds to four fifths of
every alpha is not in this channel.**

### A structural fact, already known, extended

Schur-Weyl support is entirely two-row: nonzero/total = 2/3, 4/11, 5/30, 7/77,
8/176 at n = 3,6,9,12,15, max rows 2 everywhere. **NOT NEW** — the t7qv witness
records it (verified there at n=6, n=9); added here are n=3,12,15 and the counts.

### The inference NOT drawn

"The trace is two-row, `[1^4]` is four-row, therefore the trace cannot carry
it" is **INVALID**. Two-row is about partitions of the STRAND count `n=3A`
(Hecke); `[1^4]` is a partition of the NUCLEON count `A` (SU(4) spin-isospin).
Different spaces — the arity/space conflation the corpus carries a STRICT
section on. The two-row fact is a candidate explanation only; the exclusion
that IS established is the numerical one, which needs no rep-theory bridge.

### What it sharpens

`[1^4]` is a four-body SU(4) object, not a bond-graph object, so neither the
additive cap nor the A=4 sign applies to it. The bond-topology exclusions
**remove the bond graph as a competitor**, leaving the alpha-cluster term as the
carrier that must supply the missing bulk — and this bounds that bulk from
below. **No mechanism proposed**; doing so on the strength of a ratio would be
numerology.


## 🛑 CORRECTION same day — the target was the OBSERVED value, not the extensive one

Reading `QOU.Mass.SaturationPeakStructure` (landed 2026-08-30) after opening
#6443 shows the comparison above answers the wrong question for an EXTENSIVE
term.

That file proves the per-nucleon curve `f(u) = a_V - a_S/u - a_C*u^2` **never
attains** its bulk coefficient `a_V` — the surface term keeps it strictly below
at every mass number — and records, in units of `hbar_q^2 * m_N`:

    a_V  (bulk volume coefficient)   1.71  ->  15.762 MeV/nucleon
    observed peak, 62Ni              0.954 ->   8.794
    238U                             0.821 ->   7.568

**So the `~8 MeV/nucleon` in the alpha-cluster audit is the OBSERVED peak.** An
extensive term must supply `a_V`, 1.79x larger; surface and Coulomb then subtract
to give the observed curve. Against the bulk requirement:

    bulk for 4 nucleons   4 x 15.762 = 63.048 MeV
    trace chain             6.152 MeV  ->   9.8 %
    trace complete graph   10.083 MeV  ->  16.0 %

**The exclusion is about TWICE as strong as first stated** — 9.8-16.0 % of the
bulk, against 20.6-33.8 % of the observed 4He binding. Both framings are kept
because they answer different questions; the bulk one is what an extensive term
must meet, and it is the stricter.

NOT to be read into the 1.71: it is `a_V/(hbar_q^2*m_N)` computed FROM the
empirical `a_V` — a re-expression of the SEMF constant in substrate units, not a
derivation. `1.71 * hbar_q^2 * m_N ~ 15.8 MeV` is arithmetic, not a prediction.
