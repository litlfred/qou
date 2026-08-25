# The Brunnian route to the μ₃ trace-convention question is structurally CLOSED (2026-08-07)

**Verdict:** scope-(b) **structural exclusion** — cited invariant: Brunnian-ness is a property
of *braid group* elements, and the μ₃ A=3 words are not braid group elements.
**Bean:** `qou-8jq2` (trace-convention reconciliation) — this closes its first proposed route.

## What was proposed, and why

[`2026-08-07-mu3-door-status-consolidated.md`](2026-08-07-mu3-door-status-consolidated.md)
§4quater flagged that the μ₃ arc computes on the **non-cyclic perblock**
`g = Σ_λ y_λ |χ_λ|` while the corpus canonical is the **signed cyclic Markov trace**
`tr_M = Σ_λ y_λ χ_λ`.

A mitigation looked available. On the **Brunnian** family the two forms coincide to machine
precision ([`2026-08-01-deltalambda-milnor-exact-coefficient.md`](2026-08-01-deltalambda-milnor-exact-coefficient.md),
Route C: "on this Brunnian family the two **coincide** to machine precision"). So: if the A=3
words could be re-expressed Brunnian-ly, the convention question would collapse and no
re-designation would be needed.

**That route is not available, and the reason is structural rather than numerical.**

## The finding

The Brunnian coincidence is established on `brunnian_word(A)` — left-normed iterated
commutators of pure-braid **band generators** `(i, j, ±1)`. Those are **braid group elements**.

The μ₃ A=3 words (`mass_at_3A_proper.atom_braid_word_3A`) are lists of `(c, d, gen)` triples
denoting `c·σ_gen + d·1` — **Hecke algebra elements**. Measured:

| | T | ³He |
|---|---|---|
| total factors | 35 | 35 |
| pure braid generators (`d = 0`) | 16 | 18 |
| **identity-admixed** (`d ≠ 0`) | **19** | **17** |
| interface bonds (`gen % 3 == 2`) | 2 | 2 |
| …of which admixed | **2** | **1** |

Roughly half of every word carries an identity admixture (19/35 for T, 17/35 for ³He). A factor `c·σ + d·1` with `d ≠ 0` is
**not in the braid group** — it is a genuine algebra element. "Brunnian" is not merely *false*
for such a word; it is **undefined**, because the delete-strand map is a homomorphism of braid
groups, not of the Hecke algebra. There is nothing to test.

## Why the admixture cannot simply be removed

It is not an artifact. The admixed factors are the **averaged crossings** that carry the color
weighting — the p–n interface is `σ − h(½ − δ/4)·1` with `δ = flavor_split_subleading(q₀)`,
canonical per the owner directive of 2026-06-01 (`pn_convention="bring_color_weighted"`,
[`2026-06-03-color-averaging-wiring-audit.md`](2026-06-03-color-averaging-wiring-audit.md)).
The intra-nucleon chains carry `−h` and `−h/2` admixtures on the same footing.

Stripping the admixture to obtain a braid word would mean abandoning the canonical color
convention. That is a much larger change than the convention question it was meant to sidestep.

The interface row differs between the isotopes, and the asymmetry is informative. ³He (Z=2,
N=1) has one p–p and one p–n interface: the p–p is pure `σ` (isospin-distinct already, no color
weight) and only the p–n is admixed — 1 of 2. T (Z=1, N=2) has **both** interface bonds
admixed — 2 of 2. Either way, **at least one identity admixture sits on a bond whose
presence/absence `Δ²g` differences over**, which is what makes the admixture load-bearing for
this question rather than incidental.

*(An earlier draft of this section stated "exactly one in each isotope"; that was generalised
from the ³He run alone and is wrong for T. Corrected against the committed witness.)*

## The sharper consequence: `g` is not a trace

Following the type honestly explains the rest of §4quater's findings at one stroke.
`χ_λ(w)` is a linear functional on the algebra; `|χ_λ(w)|` is not. So

    g = Σ_λ y_λ |χ_λ(w)|

is a **non-linear, norm-like functional on `H_n(q)`** — not a trace. Three things follow, which
had been recorded separately as unrelated observations:

1. **It is non-cyclic.** `tr(AB) = tr(BA)` is a consequence of linearity plus the trace
   property; `|·|` destroys it. The corpus name *"non-cyclic perblock"* is exactly right and is
   not a loose label.
2. **It cannot inherit the Brunnian coincidence** even in principle — that coincidence is a
   statement about braid group elements evaluated under a genuine trace.
3. **It is the object the corpus already deprecated.** *"The double-modulus form was a
   non-archimedean misuse"*
   ([`2026-06-13-binding-method-reconciliation-and-defit-program.md`](2026-06-13-binding-method-reconciliation-and-defit-program.md)
   §1) is the same observation reached from the binding side.

## Impact on the open questions

**Unaffected** (all sign-only, and the sign is unchanged between conventions):

- the §2 exclusions — proved statements about an operator *class*, no numbers enter;
- the §4.2 `sign(y_λ)` rule — proved from the Wenzl form, independent of trace convention;
- every Lean theorem in the arc — abstract, never references the trace object;
- the door verdict — closed under both readings.

**Affected:** the trace-convention question of `qou-8jq2` stands open, now with its cheapest
proposed escape closed. It must be answered on the merits — an owner call on which object is
canonical for the μ₃ context — not sidestepped.

**Weakened further:** the `r* = μ₃/c₃ = 1.585185` vs `log₂3 = 1.584963` near-match (0.014 %).
It was already labelled *"numerology coincidence"* in its own probe source
(`habiro_magnitude_a3_probe.py`). It is now additionally known to be computed from a
**non-linear functional of an algebra element**, and to be convention-sensitive at ~5–8 %
against a ~1 % tolerance. Three independent reasons not to build on it.

## Process note (the honest part)

The Brunnian route was proposed *by this session*, in the §4quater write-up, without first
checking what kind of object the A=3 words are. The type check that closed it takes about a
minute. Proposing a route whose feasibility turns on the type of the input, without inspecting
that type, is the failure mode the formalize-first discipline exists to prevent — *"find the
invariant the whole class must satisfy"* before running the search. Recorded so the pattern is
visible, not just the result.

## Artifacts

- Probe: `computations/deltalambda/brunnian_route_feasibility_probe.py`
- Witness: `computations/deltalambda/brunnian-route-feasibility.witness.json`
- Word builder inspected: `computations/mass_at_3A_proper.py::atom_braid_word_3A`
- Brunnian reference implementation: `computations/deltalambda/milnor_exact_coefficient_probe.py::brunnian_word` / `delete_strand_band`
