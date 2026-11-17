---
# qou-1qsw
title: pyhecke.atom carries THREE inconsistent nucleon constructions (nets differ by 24%) and different consumers read different ones
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T16:24:57Z
updated_at: 2026-10-04T15:22:49Z
parent: qou-5vkl
---

Surfaced by the `qou-cds1` takeover work (`74a52d3486`), which recorded it as
**"New, and it is a defect in the tree, not in this bean: ... Not filed as its
own bean yet."** Filing it so it stops living inside another bean's history.

## The defect

`pyhecke.atom` carries three mutually inconsistent nucleon constructions, and
their Markov-trace nets disagree by up to ~24 %:

| constructor | crossings | net |
|---|---|---|
| `build_nucleon_nf` | 9 | `-0.1883216147` |
| `build_atom_nf_exact` | 11, interleaved | `-0.2272041420` |
| `nucleon_gen_chains` | 11, gen-grouped | `-0.2332458961` |

The two 11-crossing models carry the **same multiset of typed crossings** and
differ only in ORDER — `build_atom_nf_exact` interleaves gen-0/gen-1,
`nucleon_gen_chains` emits all gen-0 then all gen-1. `H_3(q)` is not commutative
across generators, so these are genuinely different elements; their nets differ
by 2.6 %.

## Why it bites — the consumers are split

Different call sites read different constructions, so "the nucleon" is not one
object in this codebase:

- the exact atom/mass path uses `build_atom_nf_exact`
- the module constants `PROTON_NF` / `NEUTRON_NF` are `build_nucleon_nf`
- the fork-pricing probe reads `_PROTON_G0` / `_G1`

A result quoted from one path is not comparable with a result quoted from
another, and nothing in the tree marks which is which.

## Prior art the fix must respect

`build_nucleon_nf` omits the 2-`sigma_0` gluon dressing **deliberately** — its
own docstring says *"No separate gluon dressing — B_3 IS the gluon structure"*.
So this is not simply "one is missing crossings"; the 9-crossing model is a
different physical convention, not a truncation bug. Any consolidation has to
decide which convention is canonical rather than assume the longest wins.

`qou-bg3w`'s `Delta_L` (`-0.233198`) is the **gen-grouped** one, which the first
version of the cds1 exclusion probe never touched — an example of the confusion
this causes reaching a real analysis.

## What is needed

1. Determine which construction is canonical (owner call if the gluon-dressing
   convention is genuinely open).
2. Make the non-canonical ones either aliases, or explicitly-named variants that
   a reader cannot pick up by accident.
3. Re-point the split consumers; check whether any committed witness carries a
   value from a now-non-canonical constructor.

Not started. Filed from the cds1 takeover record, not re-measured here — the
numbers above are quoted from that probe's output, and step 1 should re-verify
them before acting.


## 2026-08-29 — VERIFIED, and two corrections to the entry above

The entry above was written from the cds1 takeover's record and said so. Having
now re-measured, its verdict stands but **two of its statements were wrong**,
one of them mine.

### Correction 1 — those are n-minus-p DIFFERENCES, not per-nucleon nets

The table above presents the three numbers as each construction's "net",
which reads as a property of one nucleon. It is not. The probe computes
`net = sum(delta(neutron, proton))` — the **Delta_L difference** between the
neutron and proton NFs. A per-nucleon sum gives entirely different values
(`build_nucleon_nf(['u','u','d'])` sums to `+0.9991251242`), so anyone
checking the table against a single nucleon would find it irreproducible and
conclude the record was wrong.

### Correction 2 — the consumer split is far wider than "three call sites"

Measured across `computations/`, `tools/` and `qou-mass/`, excluding
`_deprecated/` and `pyhecke.atom` itself:

| model | crossings | Delta_L (n - p) | in-repo readers |
|---|---|---|---|
| `build_nucleon_nf` | 9 | `-0.1883216147` | 10 direct, + 8 via `PROTON_NF`/`NEUTRON_NF` |
| `build_atom_nf_exact` | 11, interleaved | `-0.2272041420` | 6 |
| `nucleon_gen_chains` / `_PROTON_G0` | 11, gen-grouped | `-0.2332458961` | **53** |

Not "the fork-pricing probe" — **53 files**, and they include canonical
mass/binding producers: `binding_canonical.py`, `closed_form_tau_M.py`,
`pn_alpha_lp_dual.py`, `tau_M_proton_closed_form_phase5l1.py`,
`binding_multibond_wenzl.py`, `terms_2_3_atom_per_gen_mpfr_50dps.py`. The
gen-grouped model is not a probe-local choice; it is what most of the compute
surface actually reads.

Spreads: **23.85 %** between the extremes, **2.66 %** between the two
11-crossing models (which differ only in generator ORDER, `H_3(q)` being
non-commutative across generators).

All three values reproduced exactly by re-running
`computations/qbeta/qbeta_d1_eleven_crossing_exclusion_probe.py` on `main`.

### New, and separable — `pyhecke.atom` computes in float64

Measured on import:

    pyhecke.atom.h      -> float   0.20906029879563937
    PROTON_NF[0]        -> float  -0.0996576539713873   (all six coords float)

`build_nucleon_nf` seeds `nf = [1.0, 0, 0, 0, 0, 0]` and the module-level `h` is
a Python float, so `PROTON_NF` / `NEUTRON_NF` — module constants that 8 files
read — are float64 objects. Under AGENTS.md §"PROBES ARE NOT EXEMPT" that is a
defect on its own, independent of which construction is canonical, and it is
worth fixing first: it is mechanical, it does not require the convention ruling,
and it makes the comparison between the three models trustworthy at more than
~15 digits.

### Still not patched, deliberately

Which construction is canonical is a convention question — the 9-crossing model
omits gluon dressing **by design** — and re-pointing 53 readers on my own
judgement would be exactly the kind of unilateral move the anti-laundering rules
exist to prevent. The measurement is the deliverable here; the ruling is the
owner's.


## 2026-08-29 — the float64 half is DONE; the convention half is what remains

`build_nucleon_nf_mp` added to `pyhecke.atom` (float-free, at the true 50-dps
`q_0`), additive, no consumer moved.

**The trap worth recording, because the one-line fix is the wrong one.** The
module already has a float-free path — `hm_exact` over `Fraction` — and routing
this builder through it is a two-character change. It would have been a
regression of about eleven orders of magnitude:

    float64 builder vs mp at true q_0    1.4e-16 relative  (proton)
    Fraction path  vs mp at true q_0     1.66e-5 relative  = 16.6 ppm

because `_Q_FRAC = Fraction(111, 100)`, i.e. the Fraction path is exact
arithmetic at `q = 1.11`, not at `q_0 = 1.1099785827513808`. gram.py documents
the 1.93e-5 gap on `q` itself at `_Z_FRAC`; the 1.66e-5 above is what that
propagates to on this builder's output, measured. **Float-free and correct are
different properties**, and a NO-FLOAT64 sweep that reaches for the nearest
Fraction path will silently trade 1e-16 for 1e-5. The docstring says this at
the site where the next person will reach for `hm_exact`.

Also checked rather than assumed: `_hm_mp` tests `nf[si] == 0` where the float
`hm` tests `abs(nf[si]) < 1e-15`. Had the mp twin inherited that cutoff the
whole mp path would have been capped at float64 no matter the dps.

**Nothing moved.** The float builder was already correct to its own precision,
so this extends precision rather than fixing a value; `PROTON_NF`/`NEUTRON_NF`
and all 53 readers are untouched.

### What is left on this bean

Only the convention question, and it is unchanged: which of the three nucleon
constructions is canonical, given that the 9-crossing model omits gluon
dressing by design. That needs the owner. When it is settled, the mp builder is
the precision-correct base to re-point onto — and the same warning applies to
whatever is done for the two 11-crossing models: build them on `hm_mp`, not on
`hm_exact`.


## 2026-08-29 — RESOLVED on the owner's criterion (gamma-gamma + SDP), and the split is worse than filed

Owner: *"what are the three? it should follow \g\g and SDP. investigate and
resolve"* — and, separately, *"why would we omit gluon by design? i did not
design that"*.

### RETRACTION: "omits gluon dressing by design" was never a design decision

Every prior entry on this bean, and two PR bodies, said the 9-crossing model
omits the gluon term **by design**. That phrasing is mine. Its only source is
`build_nucleon_nf`'s own docstring — *"No separate gluon dressing — B_3 IS the
gluon structure"* — an unsourced assertion that cites no proposition, no ILP
and no SDP. AGENTS.md is explicit that a source file's own status note is not
authoritative, and I treated one as a ruling and propagated it. Withdrawn.

### The three, precisely

| # | builder | word | crossings |
|---|---|---|---|
| 1 | `build_nucleon_nf` -> `PROTON_NF`/`NEUTRON_NF` | B_3(6) + quarks(3) | **9** |
| 2 | `build_atom_nf` / `build_atom_nf_exact` | B_3(6) + quarks(3) + gluon 2.sigma_0(2), **in braid order** | **11** |
| 3 | `nucleon_gen_chains` + `binding_canonical._nucleon_word` | the same 11, **re-sorted to all-gen-0 then all-gen-1** | **11** |

### Resolution part 1 — the gluon term is derived, so 9 is excluded

`computations/sdp_gamma_gamma_to_qqbar.py` decomposes the proton into FOUR SDP
components:

    H_3 SDP for the inner Borromean braid B_3
    H_3 SDP for each quark pair (uu, ud, dd)
    H_2 SDP for the 2.sigma_0 gluon self-coupling      <-- separate component
    LR cross-level embedding to combine into H_3

6 + 3 + 2 = **11**. The gluon self-coupling is its own SDP, not something B_3
already contains, and `prop:mass-endomorphism-tower` carries its ILP
derivation (cited at the gluon lines of `build_atom_nf`). So the 9-crossing
model drops a derived component. **Excluded.** Docstring corrected in place.

### Resolution part 2 — the re-sorting is NOT trace-preserving, and it is 82 %

Measured at 50 dps on the REAL module constants (`_PROTON_G0`/`_G1`), not a
hand transcription. The two 11-crossing forms carry an **identical multiset**
of (template, generator):

    Counter({('sigma',0): 6, ('inv',1): 3, ('avg',0): 1, ('avg',1): 1})

for both. They differ only in ORDER. Yet:

    tr_M braid-order  = 0.62932840220292191817
    tr_M gen-grouped  = 1.1457596924573008697
    relative diff     = 0.820607        <-- 82 %, not the 2.66 % filed above

**The 2.66 % in the entry above is on `net`, not on `tr_M`.** `net` is a sum of
NF coordinates; `tr_M` is what `binding_canonical` actually feeds into
`closed_form_tau_M`. On the quantity that reaches the physics the disagreement
is 82 %.

sigma_0 and sigma_1 do not commute in H_3(q), so re-sorting a braid word is not
a re-parameterisation — it is a different element. Nothing in the SDP framework
licenses it: it says the components are solved separately and then **LR
cross-level embedded**, which is not "concatenate all gen-0 crossings then all
gen-1".

### Where the fault actually lies — NOT in `nucleon_gen_chains`

`nucleon_gen_chains` is legitimate **as a per-generator decomposition**. Its
intended consumer is `_chain_V_full` / `atom_per_generator_volumes`, which
multiplies within ONE generator and ADDS the two — it never forms `g0 . g1`.
Used that way there is no defect.

The defect is `binding_canonical._nucleon_word(g0, g1)`, which concatenates
them into a word and hands it to `tr_M_via_wenzl_bridge_mpfr` as tau_p / tau_n.
That is the one step that is unlicensed, and it is on the canonical binding
path.

### Verdict

**Canonical = #2, the 11-crossing braid-order word.** #1 drops a derived SDP
component; #3 is #2's crossings in an order no relation justifies, differing by
82 % on the trace.

### NOT executed — this needs sequencing, not a unilateral sweep

Correcting `_nucleon_word` moves canonical binding numbers by ~82 % on tau_p /
tau_n. That is not a change to make in the same turn as the finding. What is
done here: the false docstring is corrected (no number moves), and the finding
is recorded with its evidence. The remediation — and which of the 53 readers
are on the volume path (fine) versus the word path (not) — is the next piece.


## 2026-08-29 (later) — the reader split, and a fairness correction

Measured over the 53 readers of `_PROTON_G0`/`_NEUTRON_G0`/`nucleon_gen_chains`
(excluding `_deprecated/` and `pyhecke.atom` itself), classifying each by
whether it CONCATENATES the chains into a `(c, d, gen)` word or feeds them to
the per-generator volume path:

    WORD-PATH   18   (16 live + 2 in the generated qou-mass mirror)
    volume/other 35

The 18 include the canonical mass/binding surface: `binding_canonical`,
`closed_form_tau_M`, `binding_multibond_wenzl`, `binding_threebody_joint_trace`,
`tau_M_proton_closed_form_phase5l1`, `mass_at_3A_proper`, `chi_4he_binding_lossless`.
Heuristic classifier, spot-verified on two — see the correction below, which is
one of them.

### FAIRNESS CORRECTION to the entry above: "unlicensed" overstates it

The previous entry called the concatenation a defect that "no relation
licenses". The mathematics is unchanged — sigma_0 and sigma_1 do not commute,
so re-sorting is a different element, and tr_M differs by 82 %. But calling it
an accident is wrong, and `closed_form_tau_M` says so in its own words:

    # The chain is (c, d, gen) and MONOTONE (all gen 0, then all gen 1),

That is deliberate and documented. So the corpus does not contain one correct
convention and one slip; it contains **two deliberate, mutually incompatible
orderings** — braid order in `build_atom_nf`, monotone order in the tau_M /
binding path — and they disagree by 82 % on the quantity that reaches the
physics.

That changes what the remediation IS. It is not swatting a bug: it is
overturning a documented convention on the strength of the gamma-gamma/SDP
criterion, which says the components are LR cross-level embedded rather than
concatenated monotonically. Whoever executes it should expect the monotone
ordering to have load-bearing justifications elsewhere that must be found and
answered, not merely edited around.

### Sequencing, unexecuted

1. Establish why monotone was chosen — `closed_form_tau_M`'s comment asserts
   it without a citation, exactly as `build_nucleon_nf`'s gluon docstring did.
   That parallel is a reason for caution, not for confidence.
2. Only then re-point the 18, with tau_p/tau_n moving ~82 %.
3. The 35 volume-path readers are unaffected: `_chain_V_full` multiplies within
   ONE generator and `atom_per_generator_volumes` adds, so ordering across
   generators never arises there.


## 2026-08-29 — PROVENANCE OF THE MONOTONE CONVENTION: it is an algorithm's input
## restriction, and one canonical consumer obeys it gratuitously

Owner asked for the provenance. It is fully traced, and it is not physics.

### The chain

1. **The physics is interleaved.** `B_3 = (sigma_0 sigma_1^-1)^3` is the
   Borromean confinement braid, interleaved by construction — the alternation
   IS the Borromean structure. `computations/confinement-operator-selection.py`
   carries it under exactly that name in the operator-selection candidate set,
   i.e. it is the form the confinement SDP itself ranks.

2. **`chi_all_lambda` accepts only monotone words**, and enforces it:

       for d_mp, g in gens:                  # group + assert monotone
           if g < last:
               raise ValueError(f"non-monotone word: gen {g} after {last}")

   This is structural, not a check that could be relaxed: it is a fine-Bratteli
   transfer matrix that applies `O_g` once per generator in increasing order,
   advancing the Young shape one box at a time (`for g in range(0, n-1)`).
   There is no state for returning to gen 0 after gen 1.

3. **So the word was re-sorted to fit the routine.** `closed_form_tau_M` says
   so in the only justification either construction ever offers:

       # The chain is (c, d, gen) and MONOTONE (all gen 0, then all gen 1),
       # which is what `chi_all_lambda` requires.

   `nucleon_gen_chains` exists to emit that shape.

### What it costs: the monotone word is a DIFFERENT LINK

Measured at 50 dps, on `B_3` **alone**:

    (s0 s1^-1)^3   tr_M = 0.99856216383678726595     <- Borromean
    s0^3 s1^-3     tr_M = 0.18006453953550109830     <- monotone re-sort
    relative diff       = 0.81967618

The full-nucleon discrepancy is 0.820607, so **essentially all of it is B_3**
— the quark and gluon crossings contribute almost nothing to the gap. Flattening
the alternation does not perturb the Borromean braid; it replaces it with a
different link, and "confinement" is precisely what the alternation encodes.

### The finding that makes this actionable NOW

`binding_canonical` does **not** use `chi_all_lambda`. It uses
`tr_M_via_wenzl_bridge_mpfr`, and that routine has **no monotonicity
restriction** — verified by feeding it the interleaved word directly:

    interleaved -> 0.629328402202921918   (accepted, Borromean order)
    monotone    -> 1.14575969245730087

So the canonical binding path is passing a distorted word **gratuitously**. It
inherited the monotone shape from `nucleon_gen_chains` — whose shape exists for
a *different* routine — and nothing in its own trace path required it.

### Verdict on provenance

The monotone convention has **no physics derivation**. Its entire justification
is one routine's input precondition, and it is applied in at least one place
where that routine is not even used. The earlier framing on this bean — "two
deliberate incompatible conventions" — is too generous: one is the SDP's own
candidate and the other is an artifact of a fast character algorithm's
restriction, propagated past its origin.

### Consequence for the remediation

The 18 word-path readers split further, and the split matters:

* **Consumers on `tr_M_via_wenzl_bridge_mpfr` or any non-monotone-restricted
  trace** — fixable immediately by passing braid order. `binding_canonical` is
  one, confirmed.
* **Consumers genuinely on `chi_all_lambda`** — blocked on a character routine
  that can take a non-monotone word. That is a real piece of work
  (the fine-Bratteli transfer matrix does not generalise for free), and it is
  the actual blocker behind the whole convention.


## 2026-08-29 — RETRACTION: "braid order is canonical" is REFUTED by an independent route

I attempted the gratuitous-consumer fix and it produced a result that refutes
my own verdict two entries up. Recording it rather than the fix.

### What I did

Added `pyhecke.atom.nucleon_braid_word` (braid order, mp) and re-pointed
`binding_canonical`'s closed-form path onto it. Deuteron, closed-form path:

    BEFORE (monotone)     tr_M_atom = 0.575172243917772   B = 0.435403481607429
    AFTER  (braid order)  tr_M_atom = 0.151968339204232   B = 0.115039528912109

### Why it is reverted

`binding_canonical`'s own comment says the monotone value is *"exactly that
bean's bridge/peel value"* (qou-4e5k). Checked instead of taking it on trust —
and the check goes against me. `binding_combiner_markov_peel_fallback.py`
builds from **`atom_braid_word_3A`**, the 3A-strand word. It never passes
through `nucleon_gen_chains`, so it shares no ordering assumption with the H_3
form. Its committed witness carries

    0.575172243917771870826535

i.e. the **monotone** value, to 24 digits — not the braid-order one.

So an independent route agrees with monotone and disagrees with braid order.
The monotone form looks like the correct H_3 **reduction** of the 3A braid,
even though it is demonstrably not the literal per-nucleon sub-braid.

### What survives, and what does not

SURVIVES:
* The provenance. The monotone shape was chosen to satisfy `chi_all_lambda`'s
  precondition; `closed_form_tau_M` says so and cites nothing else. That is
  still the origin.
* The measurement. The two orderings are different elements of H_3(q), 82 %
  apart on tr_M, essentially all of it from B_3 (81.97 % on B_3 alone).
* The 9-vs-11 finding, which is independent of ordering: the gamma-gamma SDP
  decomposition has four components including the H_2 gluon self-coupling, so
  the 9-crossing model drops a derived one.

DOES NOT SURVIVE:
* **"Canonical = the braid-order word."** Retracted. Provenance being
  algorithmic does not make the result wrong, and I treated it as if it did —
  the inference "chosen for convenience, therefore incorrect" is exactly the
  genetic fallacy, and an independent route now contradicts its conclusion.
* **"binding_canonical obeys the constraint gratuitously."** Half wrong for a
  second reason: the path I patched is behind `use_closed_form`, and the
  default run uses the TRANSFER path via `atom_braid_word_3A`. My first re-run
  produced byte-identical output, which is how I found this. The default
  binding numbers were never affected by the monotone question at all.

### The real open question, restated

Not "which ordering is right" but: **what is the correct H_3 reduction of the
3A-strand nucleon, and why does the monotone form reproduce it?** The 3A word
gives each nucleon its own strand triple, so the crossings may legitimately
group by generator under the reduction. If that is so, the monotone shape is
right for a structural reason and `chi_all_lambda`'s precondition merely
happened to coincide with it — which would be worth writing down, because
nothing currently records the reason and the next reader will re-run this
whole investigation.

`nucleon_braid_word` is kept as a comparison object, with a docstring that says
plainly it is NOT established as the correct reduction and must not be swapped
in.


## 2026-08-29 — the "next question" was already answered on main, and my framing had a category error

I proposed as the next open item: *"what is the correct H_3 reduction of the 3A
nucleon, and why does the monotone form reproduce it?"* It is substantially
answered by work that landed 2026-08-25, four days before I posed it. I grepped
the ordering question but not the closure question, which is the corpus-grep
discipline failing in the direction it always fails: I checked whether my
*answer* was known and not whether my *question* was.

### 1. Monotone is the 3A word's OWN convention

`atom_braid_word_3A`'s docstring:

    Matches the chain-walk convention of hecke_core.atom_per_generator_volumes:
    for each nucleon k, apply intra g_0, intra g_1, then (if include_inter)
    the appropriate pp/nn/pn crossing at gen 3k+2.

So the 3A word lays each nucleon down as all-g_0-then-all-g_1 at generators
3k, 3k+1. `nucleon_gen_chains` mirrors that faithfully. The Markov peel
agreeing with the monotone H_3 value is therefore **not** independent
corroboration of a coincidence — both express the same corpus-wide convention.
That is a better reason to keep monotone than "an independent route agrees",
which is what I said in the retraction above; the retraction's conclusion was
right and its stated reason was weaker than the real one.

### 2. My "different link" framing was in the wrong category

From `docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`:

    `atom_braid_word_3A` does not return a braid word. Each letter is a triple
    (c, d, g) meaning c.sigma_g + d.1 — an element of H_n(q), not of the braid
    group.

The averaged crossings are literally weight-1 averages over crossing sign
(`sigma - (h/2).1 = ½sigma + ½sigma^-1`). For 2H there are 5 non-braid letters
(= 2A+1 in general), so by linearity `tr_M(W)` is a weighted sum of **2^5 = 32**
link invariants. **There is no single closure to ask about.**

So "the monotone re-sort substitutes a different link for the Borromean braid"
is a statement about an object the full nucleon word is not. What survives is
the narrower claim, which is a genuine braid comparison because both words are
pure sigma / sigma^-1 with no averaged letters:

    (s0 s1^-1)^3  tr_M = 0.99856216383678726595
    s0^3 s1^-3    tr_M = 0.18006453953550109830     81.97 % apart

That stands. Its extension to the full nucleon does not.

### 3. And the consequence is already measured, not conjectural

The same audit reports, SnapPy-verified: **all 32 branch closures for 2H are
non-hyperbolic** — each branch braid is monotone, so its closure is a connected
sum of (2,k) torus links — with **Vol = 0 for every one**. Beans qou-2pnv,
qou-d5e8, qou-9ot5; the audit's own headline is that the volume route therefore
cannot justify `B_sym`.

That is the real downstream consequence of the monotone convention, it is
established, and it is a strictly bigger finding than the ordering question I
opened here.

### Where that leaves this bean

* **9-vs-11 (the gluon term)** — still live, still unresolved, and untouched by
  any of the above. The gamma-gamma SDP has four components; `build_nucleon_nf`
  drops one. Docstring corrected; no consumer moved.
* **The ordering question** — closed. Monotone is the corpus convention, applied
  consistently from the 3A word down. Not a defect.
* **What I added** — `build_nucleon_nf_mp` (float-free, true q_0) and
  `nucleon_braid_word` (comparison object, marked not-canonical). Both additive.


## 2026-08-29 — WHY the gluon component was dropped: it was not, on any stated
## ground — and the term's own derivation is now stale

Owner: *"why was it one component dropped. it should not have been, i dont
think"*. Traced, and the owner's instinct is right in the way that matters —
but the finding is larger than "someone dropped it".

### The gluon term HAD a derivation, and it was a stability argument

`computations/_deprecated/integer-lp-gluon.py`:

    For each nucleon (proton uud, neutron udd), the 9-crossing element
    B_3 x Delta_3(quarks) is LP UNSTABLE (Frobenius positivity Gx[gamma] < 0).
    The integer LP enumerates all feasible gluon combinations from
    {sigma_0, sigma_1, L+, L-} and selects the one with minimum |tr_M|
    that is stable at every intermediate step.

    Results:
      Proton:  sigma_0 -> sigma_0  (2 crossings, 11 total), |tr_M| = 0.027
      Neutron: L+ -> L-            (4 crossings, 13 total), |tr_M| = 0.112

and the commit that validated it across 82 nuclides
(`validate_isotope_nf_stability`) records the mechanism:

    Path stability: 2/11 intermediate steps are unstable per nucleon —
    the terminal gluon pair restores stability (this is by design per
    integer-lp-gluon.py).

So the gluon pair is **load-bearing**: it is what makes the per-nucleon path
LP-stable. Dropping it leaves the nucleon at an LP-infeasible object. That is
the sense in which it should not have been dropped, and `build_nucleon_nf`'s
"B_3 IS the gluon structure" never engaged with any of it.

### TWO further findings, and they cut the other way

**(a) The neutron's ILP answer was never implemented.** The LP gives the
neutron `L+ -> L-`, **4 crossings, 13 total** — a different gluon term from the
proton's. Every live builder gives the neutron the proton's `2 sigma_0` instead:
`nucleon_gen_chains` appends `(1,0)` twice unconditionally, and
`build_atom_nf`'s neutron branch does the same. So the neutron has been carrying
the proton's gluon term since the beginning.

**(b) The ILP's premise does not reproduce under convention D.** Measured at
50 dps with the current D Gram, checking Frobenius positivity at EVERY
intermediate step (the LP's own criterion, not just the endpoint):

    proton  uud   9  (no gluon)      unstable steps: NONE
    proton  uud   11 (2 sigma_0)     unstable steps: NONE
    proton  uud   13 (L+ then L-)    unstable steps: NONE
    neutron udd   9  (no gluon)      unstable steps: NONE
    neutron udd   11 (2 sigma_0)     unstable steps: NONE
    neutron udd   13 (L+ then L-)    unstable steps: NONE

Nothing is unstable, so **LP stability no longer selects a gluon term at all**.

The reason is visible in the ILP's own source. It is built on two things the
corpus has since retired:

    line 29:  z = 1.0 / (q0**0.5 + qi0**0.5)     <- convention C
    line 32:  # Corrected Gram matrix (tr_M(e-) = z^3)

Convention C was excised 2026-08-15, and `tr_M(e-) = z^3` is exactly the trace
rule `gram.py` marks `# fix 2026-05-19 (was _Z_FRAC ** 3)`. The file also sits
in `_deprecated/` and computes in float64.

### Where that leaves 9-vs-11

The honest position is neither "9 is right" nor "11 is right":

* The gluon term is **derived**, not decorative — so dropping it silently, on a
  docstring assertion, was wrong. The owner is right about that.
* But its derivation is **stale in both conventions**: convention C and the
  pre-2026-05-19 trace rule. Under D its selecting argument evaporates.
* And the derivation's own neutron result (13 crossings, L+L-) was never
  implemented, so even on its own terms the corpus does not follow it.

**What is needed is a re-run of the integer LP under convention D with the
corrected trace rule.** Until then the gamma-gamma/SDP criterion cannot
adjudicate 9 vs 11 — not because it is the wrong criterion, but because the
computation that applied it is out of date. That is a bounded, well-specified
piece of work: the LP is ~200 lines and the D Gram already exists
(`gram_matrix_mp`).

Not executed here: re-deriving it is a new compute artifact, not a correction,
and it should be its own scoped piece rather than a tail on a review branch.


## 2026-08-29 — the integer LP RE-RUN under convention D: the premise does not survive

Owner: *"rerun integer LP under convention D"*. Done —
`computations/qbeta/integer_lp_gluon_convention_d.py`, witness alongside.

Held fixed so the comparison isolates the convention: both 9-crossing base
words letter for letter, the op set `{s0, s1, L+ = s0.s1, L- = s1.s0}` (both
L's are POSITIVE crossings, not inverses — I had this wrong in an earlier
throwaway check), the every-intermediate-step Frobenius criterion, the
minimum-|tr_M| objective, `max_depth = 3`. Changed: convention D via
`gram_matrix_mp` / `tr_m_mp` (so the corrected `tr_M(e-)` rule is used), mpmath
50 dps, no float64.

### The premise fails

    proton   9-crossing base    LP stable under D?  True
    neutron  9-crossing base    LP stable under D?  True   min(G.nf) = 0.2175

The convention-C LP added a gluon term BECAUSE the base was infeasible. Under D
both bases are feasible, so **there is no stability pressure to add any
crossings**.

### And with the constraint slack, the objective selects on its own

    proton   optimal under D:  s0   ->  1 crossing, 10 total
    neutron  optimal under D:  s0   ->  1 crossing, 10 total

(41 feasible solutions each.) So under D the LP supports **neither** the shipped
construction (2 sigma_0, 11 crossings, for both nucleons) **nor** its own
convention-C answer (11 proton / 13 neutron).

### What that means, stated carefully

This does not show the gluon term is wrong. It shows the argument that
*selected* it is gone: minimising |tr_M| is a tie-breaker, and it was only ever
meant to choose among stability-feasible options. With stability non-binding the
LP is answering a different question from the one it was written for, and a
minimum-trace principle is not on its own a physical selection criterion.

**So the gamma-gamma/SDP criterion still cannot adjudicate 9 vs 11** — not
because it is the wrong criterion, but because under D the LP that applied it
has no constraint left to bite. Settling the crossing budget needs a selection
principle that is binding under D. Candidates worth considering, none pursued
here: the H_2 SDP for the gluon vertex that `sdp_gamma_gamma_to_qqbar.py`
actually names (as opposed to this LP's Frobenius-positivity proxy), or the LR
cross-level embedding it lists as the fourth component.

### Also fixed at source

The first run emitted an unstamped witness and tripped the **q0-anchor refill
ratchet** — a new red, and mine. That ratchet exists to drain exactly the
backlog of unstamped witnesses, so refilling it while investigating a staleness
problem would have been the wrong kind of irony. Stamped `q0Anchor`/`q0Value` at
the producer; not baselined.


## 2026-08-29 — H_2 gluon-vertex SDP vs LR embedding: the H_2 route HAS a binding
## constraint under D, and it is PARITY, not the normalisation

Owner asked for the results and implications of the two candidate selection
principles. Measured both.

### Option 1 — the H_2 gluon-vertex SDP

`sdp_gamma_gamma_to_qqbar.py` sets it up: `H_2(q)` has NF basis `{1, sigma_0}`,
`T_w = c_1.1 + c_sigma.sigma_0`, and the Wedderburn projections are 1x1 blocks

    sym  (2)    : c_1 + q.c_sigma      >= 0
    alt  (1,1)  : c_1 - q^-1.c_sigma   >= 0

**Its stated normalisation is the wrong thing to lean on.** With `tr_M(T_w) = 1`
imposed, measured at D:

    identity              PSD   tr_M = 1.0                  meets it
    sigma_0               NOT PSD (alt = -0.900918)         tr_M = 0.6127
    sigma_0^2 = h.s0 + 1  PSD   tr_M = 1.1280887441144      VIOLATES it

so the feasible set under that constraint is the identity alone — the script's
own comment says as much (*"The minimal PSD T_w with tr_M = 1 is T_w =
identity"*). Read that way the H_2 SDP selects nothing, exactly as the D re-run
LP selected nothing.

**But the PSD condition alone IS binding, and it is a parity rule.** The
antisymmetric projection of `sigma^k` is exactly

    alt(sigma_0^k) = (-1/q)^k

so `alt >= 0 <=> k EVEN`. Measured, k = 0..6:

     k    sym            alt              PSD?
     0    1.0            1.0              PSD
     1    1.10997858    -0.900918284      no
     2    1.23205245     0.811653754      PSD
     3    1.36755184    -0.731233708      no
     4    1.51795325     0.658781817      PSD
     5    1.68489560    -0.593508584      no
     6    1.87019803     0.534702735      PSD

**This is the constraint that survives convention D.** It is exact and
algebraic — no numerics, no anchor, no Gram — so unlike the Frobenius-positivity
proxy in the deprecated LP it cannot go stale with a convention or a trace rule.

Implications, and they are sharp:

* It **rules out the D-LP's answer.** That re-run returned `s0` — ONE crossing,
  10 total — for both nucleons. Odd, hence not PSD at the vertex. My own
  re-run's optimum is excluded by this rule.
* It **selects 2 sigma_0 over 1 and 3**, i.e. the shipped 11-crossing
  construction, as the minimal NON-ZERO even option.
* It is **consistent with the C-era neutron answer too**: `L+ -> L-` is 4
  crossings, also even.
* It does **not** by itself force k > 0 — `k = 0` is PSD. So parity narrows
  {0, 2, 4, ...} and the remaining step, that the vertex is present at all, is a
  physical input rather than a PSD consequence.

### Option 2 — LR cross-level embedding

Machinery exists and is live: `lr_coeff` implemented in three non-deprecated
places (`meson/cut_entropy_is_A_independent_probe.py`,
`probe_9b_perlambda_brane_tower.py`), plus `probes/lr_hecke_character_probe.py`
and `computations/UNIVERSAL-BRANCHING-PLAN.md`. So this is not a from-scratch
build.

But it is the wrong tool for THIS question. LR coefficients govern how
representations COMBINE across levels — how the H_2 vertex and the H_3 blocks
fuse. They constrain the embedding, not the multiplicity of crossings at the
vertex being embedded. Nothing in the LR data distinguishes 9 from 11: both are
H_3 elements, and the embedding acts identically on either. LR becomes
load-bearing at the NEXT step — assembling the four SDP components into the
nucleon — which is a real open piece, just not the adjudicator here.

### Recommendation (my judgement, not a finding)

**Take the H_2 PSD parity rule as the selection principle, and drop the
tr_M = 1 normalisation from that role.** It is the only candidate examined that
is binding under D, it is exact rather than numerical, it excludes my own LP's
answer, and it independently reproduces the even crossing count both C-era
answers had. It leaves exactly one honest gap — why the vertex is present at all
— which is a smaller and better-posed question than "which of 9, 10, 11, 13".

Do NOT wire anything on this yet: it selects the parity, and the corpus should
decide whether "gluon vertex present" is an axiom or is itself derived before
the crossing budget is declared canonical.


## The H₂ selector is PSD parity, not tr_M = 1 (owner ruling 2026-08-30)

Owner: *"H₂ PSD parity rule; drop tr_M = 1 from the selecting rol"*. Adopted.

**The rule, proved.** For the gluon vertex `σ₀^k` in `H₂(q)` the two Wedderburn
projections are one-dimensional and are ring homomorphisms, so they send
`σ₀^k` to the `k`-th power of the generator's eigenvalue: sym `q^k`, alt
`(−q⁻¹)^k`. With `0 < q` the sym block is positive at every `k` and is never
the binding constraint, so

    σ₀^k is PSD  ⇔  k is even.

`folio/quantum-observable-universe/lean/QOU/QBeta/GluonVertexPsdParity.lean`
— seven declarations, `lean`-direct exit 0, `#print axioms` shows only
`propext / Classical.choice / Quot.sound` on all seven. Stated over a generic
ordered field (`[Field R] [LinearOrder R] [IsStrictOrderedRing R]` — this
Mathlib has no `LinearOrderedField`); the algebraic half is over a bare
`DivisionRing`.

**Why this form and not a re-run.** The rule it replaces was a Frobenius
positivity test against a Gram matrix in `_deprecated/integer-lp-gluon.py`,
built at convention C's Markov parameter and on the superseded `tr_M(e⁻) = z³`
rule; under D its premise does not hold and it selects nothing
(`computations/qbeta/integer_lp_gluon_convention_d.py`). The parity statement
mentions no Markov parameter, no Gram matrix, no trace rule and no anchor, so
a convention change cannot invalidate it.

**What it settles.** `σ₀²` — the shipped gluon term — is the minimal non-zero
admissible vertex. The single `σ₀` that the convention-D integer-LP re-run
returns as its optimum is EXCLUDED. The convention-C neutron answer
(`L₊ → L₋`, four crossings) is even and admissible.

**What it does not settle.** `k = 0` is PSD, so parity does not force the
vertex to be present at all. That stays open and is not answered by this.

## tr_M = 1 dropped from the selecting role

Recorded in `computations/sdp_gamma_gamma_to_qqbar.py` at both sites.

Imposed as a constraint it admits only the identity, so it rejects `σ₀²` —
which is PSD but has `tr_M = 1.128…` at the substrate. **A condition that
rejects the construction the file ships cannot be what selected it.** It is a
normalisation of the trace, not a selection principle.

**A second defect found while removing it.** The demo's printed reading argued
`σ₀³` is not canonical because *"tr_M ≈ 0.73 … is NOT 1"*. `0.73` was never
the trace — the code prints `tr_M = 0.8485`, and `0.7312` is the **magnitude
of the alt eigenvalue** sitting three lines above it. So the withdrawn
argument was quoting the wrong quantity as well as using the wrong criterion.
The parity rule gives the stronger and correct replacement: `σ₀³` has `k = 3`
odd, hence is not PSD — which is exactly what the file's own `psd_at_q_0`
already printed as `False`, an independent empirical check of the Lean.

**Noted in passing, NOT acted on** (untouched producer; the pin migration is
the tracked sweep `qou-1c4y`, and the witness re-run would have *downgraded*
the environment record `sympy 1.14.0 -> 1.12` while moving no number, so it
was reverted): `sdp_gamma_gamma_to_qqbar.py` evaluates at
`q₀ = 1.10997859564273903916…`, which is neither the proton pin nor the frozen
canonical muon pin — it is the **CODATA-2022 lepton-tower muon** value
(`…5956427390…`), the third of the three values AGENTS.md warns are all called
"the muon q₀". The parity rule is anchor-free, so nothing here depends on it.


## 2026-08-30 — the 9-crossing model is RETIRED, and the measurement's answer was not the one I predicted

Owner authorised "measure first, then retire the 9-crossing". Both done. Three
corrections to my own framing along the way, all recorded because each was a
counting or category error of the same kind.

### The fix is ONE function, not a reader migration

`build_nucleon_nf` now applies the σ₀² gluon self-coupling — two `hm(nf, 1, 0,
0)` at generator 0, the same term `build_atom_nf` already applied. Every
consumer picks it up automatically, including `computations/substrate/
hecke_core.py` and the **generated** `qou-mass/_internal/hecke_core.py`, both of
which *import* from `pyhecke.atom` rather than defining their own copy — so the
vendor mirror needs no hand-edit (which AGENTS.md forbids anyway).

Framing it as "re-point 13 readers" was wrong. The model was defective; making
it correct is a one-site change.

### A third independent argument, and it is structural

`shift_from_nf_basis.build_nucleon_nf_sym_atomic` documents
`atomic_braid_to_crossings`'s convention as **"7 at gen_idx 0 + 4 at gen_idx 1
= 11 generators"**, explicitly contrasted against "the 9-generator
hecke_core.build_nucleon_nf". With the gluon term:

    B₃ = (σ₀σ₁⁻¹)³      3 at gen 0, 3 at gen 1
    quark pairs         2 at gen 0, 1 at gen 1
    gluon σ₀²           2 at gen 0
    ------------------------------------------
                        7 at gen 0, 4 at gen 1  = 11

**Exact match.** The gluon term is precisely what the 9-generator form was
missing, and this was not fitted for — the term was added on the γγ SDP
decomposition and `vertex_psd_iff_even`. The two conventions in this corpus
now agree, and that docstring's stated contrast is retired.

Δ_L(n−p) goes **−0.18829060147138277044 → −0.22715971176556957097** at 50 dps,
against `build_atom_nf_exact`'s recorded −0.2272041 — agreement to four
digits, a second cross-check.

### The measurement result: ZERO published numbers move

I predicted ~21 % movement across five publishers. Measured, re-running every
publisher I could:

| producer | result |
|---|---|
| `compound_shift_nf` | byte-identical |
| `shift_from_nf_basis` | environment metadata only (`sympy 1.14.0 → 1.12`) |
| `integer_lp_gluon_convention_d` | byte-identical |
| `atom_mass_derived` | `scriptCommitSha` only; **10/10 assertions still pass** |
| `hadron_knot_table` | NOT RUN — >50 min, does not finish (AGENTS.md) |

**No number moved anywhere**, despite `PROTON_NF` net moving 20.9 % and Δ_L
20.6 %. `pyhecke` suite: **222 passed / 13 skipped**, identical to before.

That is the useful finding, and it explains the defect's longevity: **the
9-crossing model was wrong with no published consequence**, so nothing ever
flagged it. It also means the change is safe to land — the one genuine unknown
is `hadron_knot_table`, which cannot be run to completion here.

Worth noting on its own: a 21 % change to a module constant passes 222 tests.
Nothing asserts on `PROTON_NF`.

### Three counting errors of mine, for the record

1. **Reader counts from the bean, quoted without re-measuring**: 18/6 stated,
   13/30 actual.
2. **grep counted docstrings and comments as consumers.** By AST the real
   figure is **7 consumers, 6 text-only mentions** — `shift_from_nf_basis`
   does not import the builder, it *reimplements* it.
3. **A category error in the options I put to the owner**: `build_atom_nf(Z,
   N)` is the ATOM-level builder and `nucleon_gen_chains(quarks)` is
   per-nucleon. "Retire #2 in favour of #3" was not a coherent operation and
   was **not executed**; the authorisation was given for something I had
   described wrongly. Recorded in
   `docs/audits/2026-08-30-nucleon-construction-reader-measurement.md`.

### Also fixed

`build_atom_nf`'s docstring still read *"No separate gluon dressing — B₃ IS
the gluon structure"* — the same unsourced claim, sitting directly above the
code that applies the gluon term. Corrected. Both builders now say the same
true thing.


## CORRECTION (same day) — "zero published numbers move" was FALSE

A **fourth** counting error, same class as the other three, and this one
inverted the conclusion.

**What went wrong.** The AST scan that produced "7 real consumers" matched
`ast.Name` nodes carrying the target identifiers — which matches **assignment
targets** as well as uses. `computations/atom_mass_derived.py` was counted as a
consumer when it in fact **defines its own**:

```python
PROTON_NF  = build_nucleon(['u', 'u', 'd'])   # line 271, its OWN build_nucleon
NEUTRON_NF = build_nucleon(['u', 'd', 'd'])
```

It never imports `pyhecke.atom`. Its witness not moving was *expected* and said
nothing about the change — and I had reported it as the primary evidence that
the change was inert.

**Corrected consumer set**, resolving by import rather than by name: **6 true
consumers**, 1 defining its own, 6 text-only. Layer-2 via `hecke_core` adds
nothing new. **Of the six, exactly one publishes a witness —
`hadron_knot_table` — and it is the one that could not be run.** So the "five
publishers, zero movement" measurement covered five producers of which **none
consumed the changed function**.

**The actual blast radius, measured directly** against the committed witness.
`hadron_knot_table` calls `build_nucleon_nf` only for the rows passing
`quarks` — `("proton", 1, 0, "uud")` and `("neutron", 0, 1, "udd")`; every
other row goes through the untouched `build_atom_nf`:

| assertion | committed (9×) | new (11×) | change | Frobenius |
|---|---|---|---|---|
| `tr_M(proton)` | 0.419562177934 | **0.629328402203** | **+50.00 %** | stable |
| `tr_M(neutron)` | 0.301675079767 | **0.475133517156** | **+57.50 %** | stable |

21 of 23 assertions unaffected.

**And a third exact cross-check falls out of it.** The new `tr_M(proton) =
0.629328402203` matches the braid-order value recorded further up this bean —
`tr_M braid-order = 0.62932840220292191817` — to every printed digit. The
11-crossing `build_nucleon_nf` reproduces the braid-order nucleon exactly.
That is what it *should* do, and it is a check the change was not tuned
against.

### Consequence — PR #6214 must not merge yet

Landing the code makes `computations/hadron-knot-table.witness.json` stale by
50 % on two assertions, and **the witness cannot be regenerated in this
container** (the producer does not finish; deuterium alone >50 min). Hand-
editing the two numbers is forbidden; truncating the ATOMS list would produce a
*different* witness rather than a regenerated one.

Correct sequencing: regenerate that witness in an environment that can run the
producer to completion, **in the same change as the code**.

### The pattern, since this is now four for four

Every one of my four errors on this bean was a **proxy mistaken for the
thing**: a bean's recorded count for a live count; a grep hit for a call site;
an atom-level builder for a per-nucleon one; and an assignment target for a
use. The corrective in each case was to resolve to the actual object —
re-measure, parse, read the signature, follow the import. Worth keeping as the
method rather than as four separate embarrassments.



## 🛑 CORRECTION 2026-09-12 (from PR #7212) — the net figures in this bean's tables are at q = 111/100

Both tables in this bean quote the three nucleon-model nets as

  build_nucleon_nf     ( 9 crossings)  -0.1883216147
  build_atom_nf_exact  (11, interl.)   -0.2272041420
  nucleon_gen_chains   (11, gen-grp)   -0.2332458961

Every one of those matches **q = 111/100** to every digit quoted, and none
matches the substrate proton pin:

  model                                q=111/100        substrate proton
  build_nucleon_nf     ( 9 crossings)  -0.18832161472   -0.18829060147
  build_atom_nf_exact  (11, interl.)   -0.22720414203   -0.22715971177
  nucleon_gen_chains   (11, gen-grp)   -0.23324589607   -0.23319771132

q = 111/100 is `pyhecke.gram._H_FRAC`'s exactness device, **185 ppm** off the
substrate — roughly 16000x the 11.54 ppb mu-p tension. Diagnosed 2026-09-04 in
`docs/audits/2026-09-04-delta-net-canon-and-crossing-count-analysis.md` §(ii)
and asserted in `qbeta_delta_candidate_census_probe`; the correction had not
reached this bean.

WHY IT MATTERS HERE SPECIFICALLY. This bean's second table gives CONSUMER
COUNTS against these figures — 53 files for the gen-grouped model, "and they
include canonical" ones. Those counts are about the MODEL, not about the
figure, so they are unaffected; but any consumer that took the decimal from
this bean rather than recomputing has a 185 ppm error. I have NOT measured how
many did, and that is a distinct question from the 53.

Cross-check that fixes the figures: the gen-grouped substrate value is the
calibration constant `qbeta_option_e_order_dof_range_probe` (merged) asserts at
1e-30, -0.23319771131565870204...

NOT closing this bean; only recording the correction. Status left as the owning
agent set it.


## 2026-09-13 — ALL THREE constructors are excluded, so picking among them does not help

From the `qou-99qc` parity work (`d6ca6af2f0d`, `c33e7d8914a`, both merged /
open on #7336). This does not resolve which constructor is canonical; it
changes what resolving it would buy.

**The alternating character's sign is `(-1)^length`** over the corpus alphabet
(`QOU.Mass.AltCharShiftMultiset.wordChar_sign`, sorry-free): every letter has
strictly negative character, so a product of them is decided in sign by nothing
but how many there are. Under the owner-selected SDP scope **(B) whole
element** (2026-09-13) the alternating block is one-dimensional, so PSD there
is exactly `0 <= character`.

**All three constructors in the table above have ODD crossing counts — 9, 11,
11 — so all three are excluded.** The 24 % net disagreement this bean is about
is real and still worth settling, but no choice among the three produces an
element admissible in the alternating block. They differ by 2, so they do not
even differ in parity.

**Where the obstruction actually sits:** core `B_3 = (sigma_0 sigma_1^-1)^3` is
6 letters (EVEN), the quark block is 3 (ODD), the gluon dressing 2 (EVEN). Only
the quark block is odd, so `gluon_dressing_must_be_odd` — the whole question
reduces to the dressing's parity, and every count the corpus proposes (2, and
the retracted 4) is even.

**And the obvious repair is closed**: `even_dressing_cannot_repair` (sorry-free)
— appending an even-length dressing preserves inadmissibility, and gamma-gamma
words are even by `GammaGammaWordSelection.length_even`. So **no amount of
gamma-gamma pair-production can fix any of the three.** Whatever supplies the
missing odd letter is by that fact not gamma-gamma-produced.

Swept confirmation: 364 dressings over the alphabet at lengths 0..5, uniformly
admissible at every odd length and uniformly excluded at every even one, no
mixed length (`qbeta_crossing_budget_gluon_parity_probe.py`, 6/6).

### 🛑 Separately — the net figures in the table above are SUPERSEDED

They are quoted at `q = 111/100`, not at the substrate pin.
`qbeta_d1_eleven_crossing_exclusion_probe.py` corrected them on 2026-09-12 and
records the correction explicitly; this bean still carries the pre-correction
values:

    constructor           this bean (q=111/100)   corrected (substrate pin)
    build_nucleon_nf      -0.1883216147           -0.1882906015
    build_atom_nf_exact   -0.2272041420           -0.2271597118
    nucleon_gen_chains    -0.2332458961           -0.2331977113

185 ppm, about 16000x the mu-p tension. The 24 % disagreement the bean is about
is unaffected — it is far larger than this — so the defect stands exactly as
filed; only the three decimals are wrong. Flagged rather than edited in place,
since the table is this bean's own record of what it found.

## Round 70 Formalization Progress (PR #8297)
- Formalized `QOU.QBeta.GluonVertexPsdParity.four_crossings_psd_and_two_prod_one` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/tl_uniqueness_threerow_factorisation_shadow_gluon_probe.py`, `scriptHash: 3ae4cba85e90`, Commit 1 `1f88e71305a6e71d41389edf2285daae1528f7d8`, Commit 2 / Witness `cfb7f3d64020483db10298c3ccdd51ae1d1bd7d8`, PR `litlfred/qou#8297`).
