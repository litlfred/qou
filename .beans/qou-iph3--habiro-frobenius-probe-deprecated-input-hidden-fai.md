---
# qou-iph3
title: 'habiro-frobenius probe: deprecated input, hidden failing test, half-integer full trace'
status: todo
type: task
priority: normal
created_at: 2026-08-22T22:55:17Z
updated_at: 2026-08-23T00:58:09Z
---

Split out of the `qou-lwyo` scoping pass (2026-08-22), which carries the full
measurement. Three independent defects in
`computations/probes/habiro_frobenius_probe.py` and its witness — none blocks
`qou-lwyo`'s Lean instance, all three affect what the block
`def:qou-motivic-galois-instance` can claim, whose `.ts` says
`computation.status: "verified"`.

**1. Input is a `_deprecated/` witness.** Resolves to
`computations/_deprecated/habiro-coefficients-atomic-fast.witness.json`. Live
per-atom witnesses exist for all five atoms, plus a live aggregate at
`computations/habiro/habiro-coefficients-atomic.witness.json`.

Not a mechanical repoint — the deprecated file is **deeper**: proton 10 vs 9,
deuteron 14 vs 13, tritium 19 vs 16, ³He 20 vs 16, neutron 9 vs 9. Fewer
coefficients ⇒ the Pochhammer mechanism (`2p ≤ n_coeffs`) covers fewer primes.
Which generation is canonical is an author call.

**2. The witness headline omits the test that fails.**
`summary.step2_all_atoms_compatible: true` is the numerator-only test. The same
script computes `step2_full_trace_passed` — **False at 45/45** (5 atoms × 9
primes) — and the top-level `summary` never surfaces it. Reading `summary` alone
gives the opposite impression to the per-prime data.

Fix: surface `step2_full_trace_compatible` in the top-level summary alongside the
numerator result, so the witness reports both tests it runs.

**3. The full-trace failure is a uniform factor of 2 — probe it before reading it
as a refutation.** Proton: `frob_full` missing at p=3 (`denominator vanishes mod
Phi_{2p}`); at the remaining eight primes the full Galois trace is a
**half-odd-integer** — −4/3, −1/4, then 1/2, −5/2, 3/2, −7/2, 5/2, −9/2 at
p = 7,11,13,17,19,23. So past the Pochhammer range, `2·Tr(full)` is an odd
integer, uniformly. That is the shape of a missing normalisation, not of a broken
claim, and it is the one lead in this area with a visible pattern.

Per the "(a)/(b) scope" discipline: `step2_full_trace_compatible: false` is a
**scope-(a)** negative — this normalisation of the full trace, as computed, is not
integral. It is **not** a structural exclusion of full-trace compatibility, and
nothing in the corpus should cite it as one.


## CORRECTION (same session, 2026-08-22) — "uniform factor of 2" is WRONG

Defect 3 above says the full-trace failure is *"a uniform factor of 2 — `2·Tr(full)`
is an odd integer, uniformly"*. **That is false.** I measured the **proton only**
and generalised to all five atoms without checking. Measured denominators of
`Tr(full)`, all 5 atoms × 9 primes:

| atom | p=2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---|---|---|---|---|---|---|---|---|
| proton | 3 | — | 4 | 2 | 2 | 2 | 2 | 2 | 2 |
| neutron | 3 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| deuteron | 30 | — | — | 16 | 32 | 32 | 16 | 8 | 32 |
| tritium | 90720 | — | — | — | 32 | 128 | 64 | 64 | 128 |
| ³He | 90720 | — | — | — | 64 | 16 | 128 | 64 | 128 |

Denominator 2 occurs for the **proton alone**, and only at p ≥ 7. The neutron is
uniformly 4; the composites run 8 → 128 and grow with A.

A second thing I assumed and did not check: I reasoned that
`Tr(num)/Tr(full)` recovers `denom`, having verified it at p=2 (−16 / (−4/3) = 12).
It does not — the Galois trace is not multiplicative, and `denom` is not
Galois-invariant, so that quotient is meaningless wherever the orbit is bigger.
It came out non-integral at most primes, which is the symptom of the assumption
being wrong rather than of anything in the data.

## What the corrected measurement actually shows — a better lead than the wrong one

**Away from p = 2, the obstruction is exactly 2-adic.** For every atom and every
p ∈ {5,7,11,13,17,19,23} the denominator of `Tr(full)` is a **power of 2**:
`Tr(full) ∈ ℤ[1/2]`, with `v₂` running 1..7 and increasing with A.

**Every non-2-power denominator in the whole 45-cell table sits at p = 2**:
3 (proton, neutron), 30 (deuteron), 90720 (tritium, ³He). p = 3 has no `frob_full`
at all (`denominator vanishes mod Phi_{2p}`).

So `step2_full_trace_passed` fails for a *structured* reason — non-integrality is
2-adic away from the prime 2, and only at p = 2 do odd primes enter the
denominator. That is a sharper and more suggestive shape than the one I wrote
first, and it is the actual lead. It remains a **scope-(a)** negative: this
normalisation of the full trace is not integral. Nothing here excludes full-trace
compatibility structurally.


## Follow-up measurement — orbit size REFUTED, extensivity in A measured

Exact integer arithmetic on `v₂(denominator of Tr(full))`, 31 cells (5 atoms ×
p ∈ {5,…,23}; p=2 excluded as the documented odd-prime exception, p=3 has no
`frob_full`).

**Refuted: `v₂` does not track the Galois orbit size.** Orbit size is `p−1` and
rises monotonically across the row, while `v₂` does not. Deuteron, p = 7 … 23:

    orbit   6  10  12  16  18  22
    v₂      4   5   5   4   3   5

Non-monotonic, and it *falls* at p=19 where the orbit is second-largest. Tritium
and ³He behave the same way. So the natural "the trace is a sum over a
(p−1)-element orbit, hence the 2-power" explanation is **wrong** — worth
recording, since it is the first hypothesis anyone will reach for.

**Measured: `v₂` is extensive in the constituent count A.**

| A | atom | v₂ range over p |
|---|---|---|
| 1 | proton | 1–2 |
| 1 | neutron | 2 (constant in p) |
| 2 | deuteron | 3–5 |
| 3 | tritium | 5–7 |
| 3 | ³He | 4–7 |

The A=1 and A=2 bands are **disjoint** (2 vs 3); A=2 and A=3 overlap by one.
Increment is roughly 2 per unit of A.

**I am deliberately not fitting a formula.** Three distinct A values, 31 points,
and two of the five atoms share A=3 — that is far too little to separate `2A`,
`2(A−1)+c`, or anything else, and fitting one here is the numerology this repo's
discipline exists to prevent. The claim is the **shape**: extensive in A, not a
function of the orbit.

**One asymmetry worth a look.** The neutron's `v₂` is exactly **constant** (2 at
every prime); the proton's varies (2 at p=5, 1 at p≥7). Same A, same
`n_coeffs` to within one. p/n asymmetry is a recurring theme in this corpus, and
this is a clean, small instance of it.

**Why the extensivity is interesting rather than incidental:** `183aa45d06` landed
on main the same day — *"the surviving binding normalisation is N(q)^{A-1},
extensive in constituent count A"*. An extensive 2-adic valuation is the shape an
`X^{A−1}`-style normalisation would leave behind. **Stated as a question, not a
claim** — I have not read that derivation, and matching two things that are both
"extensive in A" is weak evidence on its own. Whoever picks this up should read
`183aa45d06` first and decide whether the exponents are even commensurable.


## The extensivity is DEFLATED — it is the Habiro denominator's integer content

I flagged the `v₂`-extensive-in-A finding as possibly resonating with
`183aa45d06` (*"the surviving binding normalisation is `N(q)^{A-1}`, extensive in
constituent count A"*), and said whoever picked it up should read that derivation
first. I read it, then ran the control I should have run before flagging anything:
**is there a mundane source of a 2-power that grows with A?**

There is, and it accounts for the whole effect. `frob_full = frob_num / denom`,
and `denom_in_u` carries an integer content that is a pure power of 2:

| atom | A | `denom_in_u` leading terms | content | `v₂` |
|---|---|---|---|---|
| proton | 1 | `4u²⁸ + 4u²⁴ + 4u²⁰` | 4 | 2 |
| neutron | 1 | `4u²⁴ + 4u²⁰ + 4u¹⁶` | 4 | 2 |
| deuteron | 2 | `32u⁷⁶ + 128u⁷² + 288u⁶⁸ + …` | 32 | 5 |
| tritium | 3 | `128u¹⁶⁶ + 896u¹⁶² + …` | 128 | 7 |
| ³He | 3 | `128u¹⁶⁴ + 896u¹⁶⁰ + …` | 128 | 7 |

Measured over the 30 cells with p ≥ 5:

    v₂(denominator of Tr(full))  ≤  v₂(content of denom_in_u)     30/30, no violation
    equality attained                                            in every atom

and the per-atom **maxima match exactly, 5/5**: 2, 2, 5, 7, 7.

So the "extensive in A" behaviour of `v₂` is a property of the Habiro expansion's
own denominator normalisation, and the A-dependence is inherited from how
`denom_in_u` is built. It is **not** a signal about the motivic channel, and the
`N(q)^{A-1}` resonance is **withdrawn** — two things are "extensive in A" for
unrelated reasons, which is precisely the coincidence-of-vocabulary this repo's
discipline warns about. Nobody should spend a pass chasing it.

**What survives.** The bound `v₂(den Tr(full)) ≤ v₂(content(denom_in_u))`, tight
per atom, is a real and useful statement: it says `step2_full_trace_passed`'s
failure is bounded by, and traceable to, a *known and inspectable* normalisation
constant rather than anything mysterious. That makes the fix concrete — if the
full trace should be integral, the place to look is the content of `denom_in_u`,
not the Galois theory.

**Sequencing note for the next agent.** Both wrong turns here (the "uniform factor
of 2", then the `N(q)^{A-1}` resonance) came from reporting a pattern before
running the cheap control that could kill it. The control was three lines and one
field of the input witness. Run it first.
