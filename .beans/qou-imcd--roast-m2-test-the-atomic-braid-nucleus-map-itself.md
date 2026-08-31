---
# qou-imcd
title: 'ROAST-M2: test the atomic-braid -> nucleus map itself, not just the trace'
status: completed
type: task
priority: normal
created_at: 2026-08-07T08:37:56Z
updated_at: 2026-08-31T03:03:05Z
parent: qou-kemt
---

All six options assume the missing piece is a TERM. The intensive/extensive obstruction might instead mean the A-nucleons-to-n-strands identification is the defective step. If the geometry is wrong, every add-a-term attack fails identically -- which is consistent with SIX ansatze having failed. Nobody has tested the map itself. Cheap first probe: does the framework's predicted A-scaling of ANY observable match, independent of magnitude?

## 2026-08-31 — RUN. The exponent test **PASSES**, which refutes this bean's own hypothesis.

Probe: `computations/probes/braid_nucleus_map_exponent_probe.py`
Witness: `braid-nucleus-map-exponent-probe.witness.json` (2 assertions, both pass).

**Result.** The 3-strands-per-nucleon map reproduces the extensive exponent exactly.

| | |
|---|---|
| corpus normaliser | `Z(n) = (1 + q²)ⁿ` — **verified against `markov_weights_symbolic`'s own partition sum**, `n = 2…6`, not inferred |
| strand rule | `n = 3A` (⁴He braid words carry `n_strands = 12`) |
| A-exponent of `log Z(3A)` | **1.0**, exact |
| SEMF volume-term exponent | 1 |
| extensive coefficient | `3·log(1+q₀²)·m_e =` **1.2309 MeV/nucleon** |
| shortfall vs `B/A` plateau (8.5) | **6.906×** |
| shortfall vs SEMF `a_V` (15.8) | 12.836× |

**So the map's A-scaling is not the defective step.** This bean proposed that six
identically-failing ansätze pointed at a wrong geometry; the cheap discriminator it
specified has now been run and the geometry passes it. The residual is a **pure
multiplicative constant, not a shape error** — which is the opposite of what a broken
map would produce.

**The test also selects a reading, which is the useful part for A1 (`qou-78pt`).**
`Z(3A)` itself is exponential in `A` (`5.5e16` at `A = 16`); only its *logarithm* is
extensive. "Stop discarding the normalisation" therefore has to mean `log Z` enters the
energy, not `Z`. A1 was called *unfalsifiable as written* by the ROAST; it now has a
falsifiable form, and the number it must produce is 6.906.

**The test is not vacuous.** The competing normaliser named in
`markov_weights_symbolic`'s own header, `[n]_q!`, has measured A-exponent **1.674** on
`A = 2…64`, rising to **1.995** on `A = 1024…4096` (asymptotically 2 — the linear term
in `log [n]_q! ~ (log q)n²/2 − n·log(q − 1/q)` converges slowly). Not 1 either way. An
affine strand rule `n = 3A + c`, `c ≠ 0`, would also break the exact slope.

**Deliberately not done:** the constant 6.906 is reported and **not** matched to
anything. ROAST §R0.1 found the memo's headline coincidence had been convention-shopped
— a discipline stated in its §2.1 and violated in its §4.3. Hunting a structural origin
for this constant is that same failure mode.

**One number corrected mid-run.** I first wrote the `[n]_q!` exponent as "~2" from the
asymptotic form while the probe printed 1.674. The note now reports measured values
across widening windows instead of a predicted one.

**Consequence for the ROAST's R3 ordering.** Item 3 (`qou-imcd`) resolves NEGATIVE for
the map hypothesis, so A1–A7 are *not* moot on those grounds and item 5 (`qou-78pt`,
pin the Markov normalisation from the axioms) is promoted: it is now the live one, with
a concrete target.
