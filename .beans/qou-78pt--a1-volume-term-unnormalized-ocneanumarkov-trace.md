---
# qou-78pt
title: 'A1: volume term = unnormalized Ocneanu/Markov trace'
status: completed
type: task
priority: normal
created_at: 2026-08-07T08:37:45Z
updated_at: 2026-08-31T06:48:56Z
parent: qou-kemt
---

Markov normalization is exponential in strand count => its log is linear in A (extensive). Insertion: Hecke->trace step, BEFORE normalization. Axiom source: Markov moves + Ocneanu z (already in HnMarkovTrace.lean). **ROAST (severe):** 'do not normalize' is a 1-PARAMETER FAMILY -- Kauffman bracket vs Markov trace vs HOMFLY conventions differ by (-q^1/2-q^-1/2) and writhe factors. Picking the one that yields a_V IS a fit. Strands-per-nucleon (n vs 3A) is also undetermined. Must fix the convention FROM THE AXIOMS first, or the option is unfalsifiable. Numerically N=2 gives ~2.91 MeV/strand vs a_V~15.6 (5.4x short).

## 2026-08-31 — A1 is **REFUTED**, not unfalsifiable. The convention family is too narrow to be a fit.

Probe: `computations/probes/markov_normalisation_convention_span_probe.py`
Witness: `markov-normalisation-convention-span-probe.witness.json` (2 assertions, both pass).

The ROAST called A1 unfalsifiable because *"do not normalize"* is a convention
family and *"choosing the member that lands on `a_V ≈ 15.6` IS a fit"*, and set
pinning the convention from the axioms as "the actual work". **Pinning is not
needed: measured, there is no member to choose.**

**1. The family is discrete, not a free continuous parameter.** The two leading
normalisers differ by exactly one factor of `q` per strand —

    (1 + q²) / (q + q⁻¹) = q          exact, to 35 digits

which is the framing/writhe step the ROAST names. One discrete choice, not a dial.

**2. The whole family spans 1.33×, the deficit is 6–15×.**

| normaliser | MeV/nucleon (3 strands) |
|---|---|
| `q^{1/2}+q^{-1/2}` (Kauffman variable) | 1.0647 |
| `[2]_q = q + 1/q` (unframed loop) | 1.0709 |
| `[2]_Q = 1 + q²` (corpus partition fn) | 1.2309 |
| `1 + q⁴` (over-shoot control) | 1.4156 |

Span **1.065 … 1.416** = 1.33×. Deficit **6.00×–7.98×** vs the `B/A` plateau,
11×–15× vs `a_V`. The convention freedom is two orders of magnitude short of the
gap it was accused of closing by fiat.

**3. What closure would actually require.** At 3 strands/nucleon, a loop value of
**255.9** (the family offers ≈ 2.0–2.5); or, at the corpus normaliser, **20.7
strands per nucleon** (the corpus fixes 3, from `n_strands = 12` at ⁴He). Neither
is a convention.

**So A1 fails uniformly over the family rather than at a chosen member** — which
is a stronger result than "unfalsifiable". It closes the option instead of parking
it, and it does so without needing the axiom-pinning work the ROAST scoped.

**Unreconciled, flagged not buried.** The ROAST reports *"the N=2 reading gives
~2.91 MeV/strand"*. Every member measured here gives 0.355–0.472 MeV/strand, 6–8×
smaller. The ROAST does not show its construction and I did not reconstruct it. If
2.91 is right the conclusion strengthens, because the *span* argument is a ratio
and is unaffected — but the discrepancy is real and should be resolved by whoever
owns that number.

**Reading this together with `qou-imcd`.** That probe found the map's A-*exponent*
is exactly right (1.0, matching the SEMF volume term) with the residual a pure
multiplicative constant. This one finds the constant cannot be supplied by
convention choice. Together: the extensive term has the right *shape* and the
wrong *size*, and the size is not hiding in the normalisation. Whatever supplies
~7× is a different object.

---

## 2026-08-31 — VERDICT WITHDRAWN. A1 is not refuted; the ROAST was right.

I closed this bean with "A1 REFUTED, not unfitted", on one argument: the
convention family spans 1.33× while the deficit is 6–15×, "two orders of
magnitude too small to be the thing that closes the gap".

**The deficit figure was an energy-scale artifact.** My probe multiplied its
dimensionless logs by `m_e = 0.511 MeV` with no reason given; the corpus's
binding machinery uses `E₀ = m_e/(q₀(q₀−1)) = 4.18598 MeV` — 8.1917611722×
larger. At `E₀`:

    family:              8.722 … 11.597 MeV/nucleon
    vs a_V 15.8:         1.36× … 1.81× short
    span:                1.33×   —  the SAME SIZE as the deficit

When the span is comparable to the gap, choosing the member that lands on `a_V`
**is** a fit. That is verbatim the ROAST's charge, and my refutation only worked
because I had shrunk the family by 8.19×. **A1 reverts to "unfalsifiable as
written"; pinning the normalisation from the axioms is again the actual work.**

The "number I could not reproduce" was the tell and I filed it as open instead
of chasing it: the ROAST's 2.91 MeV/strand divided by `E₀` is `ln 2` to 0.3 %,
its own stated `E₀ log N` construction — while at `m_e` it is *unreachable*,
needing a normaliser with `log = 5.695` against a family spanning 0.694–0.923.

Survives untouched: the framing factor `(1+q²)/(q+1/q) = q` (a ratio, exact,
scale-free) and the discreteness of the family.

Full accounting and what would close it: bean `qou-59j5`. Probe:
`computations/probes/extensive_term_energy_scale_reconciliation_probe.py`.
The probe docstring, its witness verdict and its plateau assertion are all
annotated in place, with the original text kept.

---

## 2026-08-31 (later) — CLOSED, for a structural reason rather than a numerical one.

`qou-ssz6` settles it. `Z(n) = (1+Q)ⁿ` is a grand partition function with
`Q = q₀²` a fugacity conjugate to the strand-state count `k`, and its
coefficients are the **bare binomials** — no Boltzmann weight, so the spectrum is
linear in `k` and only the product `βμ = 2η₀` is fixed. `β` never appears alone.

What A1 proposes to keep is `log Z = S + βμ⟨k⟩`: a Shannon entropy plus a
dimensionless field term, both pure numbers **by construction**. No member of the
normalisation family and no choice among the four `E₀` conventions can make it an
energy, because the framework contains no `1/β`.

So A1 is dead — **not** because "no family member reaches the target" (my
withdrawn numerical claim, which turned out to be an `m_e`-vs-`E₀` artifact) but
because **no family member is an energy**. That is the disposal the ROAST asked
for, and it does not depend on pinning the convention it said was "the actual
work" — the convention question is moot once the quantity is not an energy.
