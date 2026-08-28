---
# qou-iph3
title: 'habiro-frobenius probe: deprecated input, hidden failing test, half-integer full trace'
status: completed
type: task
priority: normal
created_at: 2026-08-22T22:55:17Z
updated_at: 2026-08-28T18:39:38Z
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


## Option investigation 2026-08-23 — the framing on this bean was WRONG

I recorded item 1 as *"the probe reads a `_deprecated/` witness that is DEEPER
than the live one, so repointing loses primes"* — i.e. a staleness/depth
trade-off. **Measured, that is not what the difference is.**

### The coefficients differ from m = 0, not past a truncation point

| atom | dep n | live n | first differing m |
|---|---|---|---|
| proton | 10 | 9 | **1** |
| neutron | 9 | 9 | **0** |
| deuteron | 14 | 13 | **0** |
| tritium | 19 | 16 | **0** |
| ³He | 20 | 16 | **0** |

Neutron `a₀`: **8** (dep) vs **2** (live). Ratios are not constant across `m`
(proton `a₁`: −240 vs −172; `a₂` leading: 1417 vs 865), so it is not a rescaling
either. These are different series, and depth is a side effect.

### The driver, and it is semantic

`include_inter` differs — and `binding_canonical.py:306-308` says what it means:

    atom_elem = build_atom_symbolic(Z, N, include_inter=True,  ...)   # BOUND
    free_elem = build_atom_symbolic(Z, N, include_inter=False, ...)   # FREE

so the flag is the **bound-vs-free** distinction, whose *difference* is the
binding. Both settings are meaningful objects; neither is "old".

    deprecated:  proton False   neutron False   deuteron/tritium/³He True
    live:        all five True

**The deprecated aggregate mixes the two conventions inside one file** — its A=1
atoms are FREE, its composites are BOUND. The probe reads all five uniformly.

### Three structural hypotheses, all REFUTED by exact symbolic test

I eyeballed the live deuteron's `tr_M` as a product of the proton and neutron
numerators and it is not. Tested with `sympy.simplify(together(...)) == 0`:

- live deuteron = live proton × live neutron — **False**
- live tritium = p·n², live ³He = p²·n — **False**
- live deuteron = dep_proton × dep_neutron — **False**
- dep proton = live proton, dep deuteron = live deuteron — **False** (so even
  where the flag AGREES the traces differ; deprecated deuteron is an expanded
  degree-52 ratio, live is a two-factor product form)

So the generational difference is **not** explained by `include_inter` alone.
Different producers, different eras, no simple relation.

### One more constraint on the options

`_habiro_coefficient_extract.py:288` **hardcodes** `"include_inter": True`. The
live extractor structurally cannot emit the free variant, so "regenerate the
deprecated file with the current producer" is not available without editing that
line.

## The three options, honestly

**A — repoint the probe to the live per-atom witnesses.** Uniform (all BOUND),
current, per-atom. Costs: shallower (proton 10→9, tritium 19→16, ³He 20→16), so
the Pochhammer truncation mechanism covers fewer primes; and the A=1 atoms change
meaning from free to bound, which changes what `frobenius_at` is a Frobenius *of*.

**B — keep the deprecated aggregate.** Deeper, but its A=1 atoms are FREE while
its composites are BOUND, so the probe's five-atom comparison is across two
different object classes. Every current conclusion on this bean (`frob_num` ≠ 0
at 45/45; numerator test 45/45 pass; full-trace 45/45 fail) is computed from that
mixed file and inherits the mix.

**C — regenerate all five uniformly with the current producer** (recommended).
Requires un-hardcoding line 288 so the flag is a parameter again, then emitting
both variants explicitly. Only option that yields a uniform, current, documented
dataset — and it makes the bound/free pair available, which is what
`binding_canonical` wants anyway.

**This needs the author's call**, because A-vs-C is a question about what the
motivic Frobenius should be built from — a free nucleon or a bound one — not a
mechanical repoint. I have not changed any producer or witness.

## RESOLVED (option C run) — and TWO of my own claims here were wrong

Ran the producer end-to-end: `python3 -u _habiro_coefficient_extract.py`,
**236.4 s, FAILURES: 0**, all 20 canonical atoms + the mass-table summary,
regenerated uniformly from one `(τ_p, τ_n)`.

### Correction 1 — "the driver is semantic: `include_inter`" was WRONG

`canonical_interface_kinds(1,0)` and `(0,1)` both return **`[]`**, so the
interface product is `1` and **free ≡ bound at A = 1**. The flag cannot be what
made the deprecated proton differ from the live one. `include_inter: True` at
line 288 is a **correct descriptive label** — this producer always multiplies in
the interface product — not a hardcoded switch suppressing a variant.

**So the "blocker" I reported to the author does not exist.** Nothing had to be
un-hardcoded. Emitting a genuine *free* variant would mean omitting
`_interface_product_symbolic`, which is a different change, and at A = 1 it would
be a no-op anyway.

### Correction 2 — "the committed composites cannot be reproduced" was OVERSTATED

That came from comparing `tr_M_in_q` with `sp.simplify(together(...))`. At the
coefficient level, measured per atom:

    proton, neutron        reproduce EXACTLY (tr_M string-equal, all a_m equal)
    deuteron, ³He          coefficients IDENTICAL; only the tr_M SERIALISATION
                           differs (expanded vs factored — same expression)
    tritium                genuinely differs (16 -> 15 coefficients, from m=1)

Four of five reproduced. One did not.

### What the full run actually found — 16 of 20, and the split is exact

| | |
|---|---|
| coefficients changed | **16** atoms |
| unchanged | proton, neutron, deuteron, ³He |

**The split is predicted perfectly (20/20) by one property: whether the atom's
`canonical_interface_kinds` contain `negative`/`averaged`.** Every atom with a
`negative` interface changed; every all-`positive` atom did not.

Both generations are self-consistent: old **and** new carry
`reconstruction_matches: True` (exact symbolic `Σ a_m (u;u)_m = p(u)`), and both
`deg_p_u` and `denom_in_u` changed on all 16. So these are exact expansions of
**different input polynomials**, not a precision or truncation artefact.

### Attribution — localised, NOT settled

`_markov_z_q` documents its own migration: `z = q³/(q²+1)` (**convention D**),
"was `1/(q^{1/2}+q^{-1/2})`, convention C, excised by the owner ruling of
2026-08-09 … the audit keyed off an assignment TARGET and this computes straight
into its return, so it had no name to match" — the detector-blindness class.

The tempting conclusion is "the 16 were computed under convention C". **I am not
asserting that, and the data argues against it:** the deuteron's only interface
factor **is** `z`, and the deuteron is **unchanged**. A C→D change in `z` would
have moved it. So the difference sits in the `negative`/`averaged` branch —
`(z − h)` / `(z − h/2)` — not in `z` itself.

Which upstream edit did it is **not established here**. Do not write "the
mass-table witnesses were convention-C" anywhere on the strength of this bean.

### Verification

- `scripts/precision-gates.sh --changed` → **all blocking gates green, EXIT=0**.
  (The one `!!` is a pre-existing untraceable literal in
  `qbeta_t4_stokes3_crux_probe.py:60`, unrelated.)
- All regenerated files: `reconstruction_matches: True`.
- Diff is `computations/habiro-coefficients-*` only.

### Not merged, deliberately

The ask was five atoms; the honest run touches **16**, and it rewrites
mass-table witnesses with downstream consumers. That is 3× the requested blast
radius with an unresolved attribution, so it goes up as a PR for the author, not
onto main.

---

## RESOLVED for defect 1 (2026-08-23) — the table is convention D, all 25, merged

The two cautions above were right about **their own evidence** and are now
superseded by a different measurement. Recorded rather than deleted, because
the reasoning is the instructive part.

**"Do not write that the mass-table witnesses were convention-C."** They were.
Measured by reconstructing every committed `tr_M_in_q` from `(τ_p, τ_n)` under
each convention — exact arithmetic, three perfect-square rationals so `√q` is
exact (`computations/habiro/habiro_mass_table_convention_attribution_probe.py`,
PR #5543):

    before:  C 25/25   D 2/25      after:  D 25/25   C 2/25

The 2 either way are proton and neutron: empty interface product, so C and D
make the same statement about them.

**"The deuteron is unchanged, so `z` did not change."** The deuteron DID change
— in every field except the one that was compared. `tr_M_at_q0` moved
0.565089262867502 → 0.6933894087146489 (+22.7 %) and `denom_in_u` went from
`(q+1)`-type to `(q²+1)`-type factors; only `p_in_u` held. And `p_in_u` is the
one field that CANNOT move for an all-`positive` atom: `p(u) := u^shift · denom
· tr_M(u²)`, so for a pure power `z^k` the swap is absorbed wholesale by
`denom`. Put `z` inside a sum `(z − h)` and the numerator moves. **The 16/4
split is the signature of the swap, not evidence against it.**

**"Not merged, deliberately — 3× the requested blast radius."** The owner was
asked and chose to go wider still: regenerate all 25. Merged as `cde2fbcd89`.

The blast radius was in fact **25**, not 16 — `ATOMS` had 20 entries while
`main` carried 25 committed atom witnesses, all five extras naming this same
producer. They had been dropped from the list, so every run silently covered 20
of 25. That is the mechanism by which a mixed-convention table arises, and it
would have survived a merge of the 20-atom version.

Two gate failures surfaced by adding them, both fixed at the producer, no
baseline widened: the `raw-float64` ratchet went RED (summary regressed 21 → 26,
exactly +5 — now 21 → 0, corpus 487570 → 487524), and the environment block
would have recorded less than the witnesses on disk (numpy/scipy missing,
mpmath downgraded) — the exact versions were installed and the run repeated.

**Defects 2 and 3 are untouched by all of this and remain open:** the witness
headline still omits `step2_full_trace_passed` (False at 45/45), and the uniform
half-odd-integer full trace still wants a probe before it is read as a
refutation.


## RESOLVED for defects 1 and 2 — PR #5884 (2026-08-28)

Branch `claude/habiro-probe-convention-d-2026-08-28`, two commits.

**Defect 1 (deprecated input) — fixed.** Repointed to the symbolic-q
aggregate `habiro-coefficients-atomic.witness.json`, with the fallback
removed deliberately (a missing canonical source is now an error, not a
silent substitution). The "which generation is canonical is an author
call" framing in the bean body is now settled by measurement, not by
judgement: on `cdbdc84af1` the symbolic-q aggregate matches the per-atom
convention-D witnesses **5/5**; the deprecated fast path matches **0/5**.
The deprecated file was never regenerated for convention D, so the depth
advantage it had (proton 10 vs 9, etc.) was depth in superseded data.

**Defect 2 (hidden failing test) — fixed.** The top-level summary now
carries `step2_all_atoms_full_trace_compatible`,
`n_atoms_step2_full_trace_passed`, `n_cells_truncated`,
`n_cells_step2_full_trace_passed`, `cells_step2_full_trace_passed`, and a
`summary_note` naming which of the two tests is the headline. Both print.

This mattered more than the bean anticipated. The body says the full-trace
test is "False at 45/45", so surfacing it would have surfaced a uniform
negative. On convention-D data it is **2/45**: the proton and the neutron
at p=2, both with `Tr(full) = -1`. The omission was hiding a signal, not a
uniform false.

**Defect 3 — DEAD, and so is its correction.** Both the original
"uniform factor of 2" claim and the corrected denominator table above
were measured on the deprecated pre-convention-D coefficients. On the
convention-D data **17 of the 45 cells have an odd part 3** in the
denominator — 192, 96, 768, 384, 3. The half-odd-integer pattern that
made defect 3 "the one lead in this area with a visible pattern" does not
exist in the canonical data. Do not carry it forward; it was an artifact.

The scope-(a) framing in the bean body still stands and still applies:
`step2_full_trace_compatible: false` on 43 of 45 cells is a scope-(a)
negative about this normalisation as computed, not a structural exclusion.

**Also fixed in passing:** a NO-FLOAT64 defect the repoint exposed —
`frob_complex` / `abs_frob` went through `complex(...)`, collapsing 30 dps
to binary64 and serializing raw floats. Fixed at the producer (`sp.N` at
module dps, carry `mpmath.mpf`, serialize via `_precision.fmt`). No
baseline touched. `precision-gates.sh --changed` clears the raw-float64
ratchet; the two remaining REDs reproduce on pristine main.

**Still open — the successor question.** `j=2` head divisibility: is
`a_0 + a_1(1-zeta)` divisible by `(1-zeta)(1-zeta^2)` in Z[zeta_{2p}]?
This feeds `QOU.Habiro.habiroEval_ne_zero_of_head_not_dvd` (#5513, merged,
sorry-free) and would upgrade the numerical "45/45 nonzero" observation to
a proof at each p where it holds. Note `j=1` is vacuous for odd p —
`1 - zeta_{2p}` is a unit there (`Norm = Phi_{2p}(1) = 1` for 2p not a
prime power), which is exactly what `head_criterion_vacuous_of_isUnit`
records. `j=2` is non-vacuous at every p because `1 - zeta_p` has norm p.
Now answerable from the regenerated coefficients.


## Defect 4 (the successor question) — ANSWERED, same PR #5884

The j=2 head criterion resolves, and it gives more than the numerical
sweep did.

For odd p, Z[zeta_{2p}] = Z[zeta_p], the ramified prime is
p = (1 - zeta_p) with residue field F_p in which zeta_{2p} = -1, and
(1 - zeta) is a unit. So divisibility of the head H = a_0 + a_1(1 - zeta)
by (zeta;zeta)_2 collapses to ONE INTEGER per atom:

    A := a_0(-1) + 2*a_1(-1)     criterion fires  <=>  p does not divide A

  atom       A       factors      silent at
  proton     8       2^3          no odd prime
  neutron    2       2            no odd prime
  deuteron   192     2^6 * 3      p = 3 only
  tritium    384     2^7 * 3      p = 3 only
  3He        1536    2^9 * 3      p = 3 only

So Frob_p != 0 for all five atoms at every prime p outside {2, 3}. At
p = 2 the reduction does not apply (2p = 4 IS a prime power); done by
exact Z[i] arithmetic, fires for the neutron only.

This is strictly stronger than the frobenius sweep, which is bounded by
coefficient depth and covers 9 primes. The criterion reads only a_0 and
a_1, so it is depth-independent and covers infinitely many p.

**Silence is not vanishing** — scope-(a), not scope-(b). Where the
criterion is silent the sweep still measures nonzero (proton at p=2,
frob_num = 16; deuteron at p=3, Tr(num) = 24). It is a sufficient
condition for non-vanishing and nothing more should be read into its
failing.

Cross-checked against brute-force divisibility in Z[u]/Phi_{2p}(u) at 14
primes: agree 70/70. That check validates the residue-field reduction,
which is otherwise a hand argument.

Landed: computations/probes/habiro_head_divisibility_probe.py (exact
integer arithmetic, no float anywhere) plus three sorry-free Lean
declarations in QOU/Habiro/CyclotomicEvaluation.lean — habiroEval_two,
qPochDiag_two, habiroEval_ne_zero_of_head_not_dvd_two. Verified
lean-direct exit 0 against the real import cone; #print axioms shows no
sorryAx on any of the three.

The j=1 vacuity I predicted is confirmed as the reason the shipped
_one form was unusable: Norm(1 - zeta_n) = Phi_n(1) = 1 unless n is a
prime power, so 1 - zeta_{2p} is a unit at every odd prime.


## CLOSED — PR #5884 merged to main as ef261ff5b6 (2026-08-28)

All three defects resolved or retracted, plus the successor question answered:

- defect 1 (deprecated input) — fixed, repointed to the convention-D symbolic-q
  witness with the fallback removed deliberately;
- defect 2 (hidden failing test) — fixed, the full-trace test now reaches the
  top-level summary, where it reads 2/45 rather than the uniform false the
  bean expected;
- defect 3 (half-odd-integer full trace) — RETRACTED as a stale-data artifact,
  along with my own earlier correction to it. On convention-D data 17 of 45
  cells carry an odd part 3;
- defect 4 (j=2 head divisibility) — answered, and then some: Frob_p != 0 at
  EVERY prime for the five on-disk atoms. Odd primes via the closed form
  A(Z,N) = 2^(3Z+N) * 12^[mixed] (j=2 for p not dividing A, j=3 for p=3);
  p=2 by direct exact evaluation in Z[i], where Frob_2 = -2^(1-2M) is never
  zero.

Successor bean qou-9w5z carries the structural follow-up (where the factor of
3 comes from, why p=2 resists the criterion, and three further retractions).
