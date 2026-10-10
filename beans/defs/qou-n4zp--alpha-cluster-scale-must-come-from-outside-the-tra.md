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


## 🛑 SECOND CORRECTION 2026-09-03 — the percentages are NOT scale-free; scope (a), not (b)

The "go" question: **are `a_V`, `a_S`, `a_C` derived anywhere in the framework?**
Corpus-wide grep (content/, computations/, docs/, .beans/, lean): **no — all three
are empirical imports**, and the corpus says so in four places:

| where | what it says |
|---|---|
| `observations/bw-mass-decomposition-dictionary.md:7` | *"The empirical `a_V ≈ 15.6` MeV and `a_S ≈ 17.2` MeV are **conjectured** to be artifact parameters of fitting a classical drop to a q-deformed Markov trace; deriving them from the trace (rather than fitting) is open."* |
| `QOU/Mass/SaturationPeakStructure.lean` §Scope | *"Nothing here derives `a_V`, `a_S` or `a_C`"* — the file proves what follows FROM the SEMF shape |
| `QOU/MassTheory/CoulombFromCrossingCounts.lean` §Scope | *"`a_C` is nowhere, the `1/R` is not derived"* |
| `QOU/Mass/AffineCountIsNotASurfaceTerm.lean` | scope-(b) PROVED: the affine crossing count `12A−1` cannot be a surface term (`12m − m⁻²` strictly monotone, `no_constant_surface_coefficient`) |

**And the energy scale itself is not derived either** — bean `qou-59j5`
(2026-08-31, completed) established that `E₀ = m_e/(q₀(q₀−1))` is CAL-1, a
calibration, and that *"no N× claim about the extensive term means anything"*
until a scale is pinned. **This bean is an N× claim about the extensive term.**
It inherits the defect.

New probe `extensive_carrier_scale_inversion_probe.py` (4/4) inverts the ratio
into the falsifiable form `E_req = T / L` and compares against every scale the
corpus carries:

    close one alpha   29.800 MeV -> E_req = 12.372 MeV = 2.956 × E₀
    close the bulk    63.048 MeV -> E_req = 26.175 MeV = 6.253 × E₀

    m_e                 0.511 MeV   0.122 × E₀   no
    E₀                  4.186 MeV   1.000 × E₀   no
    ℏ_q²·m_N            9.218 MeV   2.202 × E₀   no   (SaturationPeakStructure's unit)
    m_p/tr_M(proton) 1662.730 MeV 397.214 × E₀   YES  — excised (qou-exam), overshoots 134×

**What changes:**
- `20.6–33.8 %` and `9.8–16.0 %` are **E₀ figures**. At `ℏ_q²·m_N` the same
  trace supplies **74.5 % of one alpha** and **35.2 % of the bulk**. "Two thirds
  to four fifths not in this channel" is an E₀ statement; at the other live
  scale it is "one quarter".
- The exclusion **survives** every live scale (largest is 1.34× short of one
  alpha, 2.84× short of bulk) — direction robust, numbers not.
- A larger scale closes it and nothing bounds the scale from above ⇒ **scope
  (a)**, not (b). Do not write "the trace channel cannot carry the extensive
  term" without "at any energy scale the corpus currently carries".

No scale is derived here. `qou-59j5`'s open item stays open.
