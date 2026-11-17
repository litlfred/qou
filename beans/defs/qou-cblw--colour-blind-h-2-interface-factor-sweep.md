---
# qou-cblw
title: 'p-n interface factor: colour-BLIND z - h/2 where canonical is z - h*(1/2 - delta/4)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T21:35:00Z
updated_at: 2026-11-17T07:26:20Z
parent: qou-10v9
---

Found 2026-08-25 while validating an exact-rational evaluation pipeline for the
Habiro chi cache (bean `qou-lrnd`). My own first implementation had this exact
bug, which is how it surfaced: I mapped every non-`sigma` crossing to
`-h/2` and all 11 cached deuteron characters came back wrong — by a
*different* ratio per partition, not a global scale, which is the signature of
one wrong factor rather than a normalisation slip.

## The two forms

    colour-WEIGHTED (canonical)   z - h*(1/2 - delta/4)
    colour-BLIND                  z - h/2

with `z = markov_z(q) = q^3/(q^2+1)` (convention D), `h = q - 1/q`, and

    delta = flavor_split_leading(q) = (q-1)^2 * (1 - q^-4) / 3

(`computations/_li_2_q_util.py`, and `flavor_split_leading_sym` in
`computations/tr_m_algebraic_q.py`). Note delta is a RATIONAL function of q —
which is what makes an exact-arithmetic evaluation of the whole atom possible.

AGENTS.md records the owner ruling of **2026-08-15 (R3): `bring_color_weighted`
is the canonical p/n convention.** So `z - h/2` is wrong wherever canonical is
intended.

## Why it is a trap rather than a typo

`closed_form_tau_M.py` (~lines 305-330) documents the mechanism in its own
comments: `canonical_interface_kinds(...)` by default emits only
`{positive, negative, averaged}`. A consumer dispatching on those three and
mapping `averaged -> z - h/2` **silently gets the colour-blind factor**. In the
file's own words it "fails by returning a slightly smaller number rather than
by raising". The `averaged_weighted` label exists, and is opt-in via
`weighted_labels=True`, precisely so a consumer either handles the weighting or
raises on an unknown kind.

`interface_factor(kind, q)` handles only the three blind kinds and raises on
anything else — so it **cannot** emit the weighted value at all.

The Rust side documents both forms in
`tools/hecke-engine/src/color_weight.rs` (`z - h/2` for `strict_averaged`,
`z - h*(1/2 - delta/4)` for `bring_color_weighted`), with the comment that the
delta-aware value "lives in the factor layer, not the label layer".

## Scope of the sweep

A background agent is sweeping `computations/`, `tools/`, `content/` for:
1. p-n / averaged interface factors computed as `h/2`;
2. three-kind `{positive, negative, averaged}` dispatches with no
   `averaged_weighted` branch in factor-computing code;
3. callers of `canonical_interface_kinds` that omit `weighted_labels=True`
   and then compute a factor from the labels;
4. Rust callers hardcoding the strict/blind form where canonical is intended.

**Not every `h/2` is a defect.** Deliberate `strict_averaged` implementations,
C-vs-D comparison probes, and tests asserting the blind value on purpose are
legitimate and must be separated out. That separation is the substance of the
sweep, not the grep.

## Open

Sweep results pending. Any genuine finding changes a NUMBER, so each needs the
usual treatment: confirm the site intends canonical, check whether a committed
witness carries the blind value, and fix at the producer.


---

# 2026-08-25 — CONFIRMED 11-0 against the committed cache

`computations/probes/exact_rational_chi_gauge_probe.py` settles this from the
corpus's own numbers rather than from the ruling. Running one exact-arithmetic
pipeline over the deuteron's 11 cached symbolic characters, at three
independent rational `q`:

    colour-weighted   d = -h*(1/2 - delta/4)     11 / 11 match
    colour-blind      d = -h/2                    0 / 11 match

So the **committed chi cache is colour-weighted**. A consumer using `h/2` for a
p-n interface therefore disagrees with the corpus's own recorded numbers — not
merely with a convention preference. That raises the stakes on the sweep: any
genuine finding is a number that contradicts a committed witness.

The blind arm is kept in the probe permanently as the control; without it the
weighted result would be an assertion rather than a discrimination.


---

# 2026-08-25 — SWEEP RESULTS: 9 genuine, 24 benign, 3 borderline

Sweep complete. **9 genuine findings / 8 distinct defects**: 2 Python probes,
2 Rust sites (one module), 5 content blocks. 24 `h/2` sites were examined and
**excluded with reasons** — that separation is the substance; a raw grep would
have reported ~36.

I independently re-verified the four highest-stakes claims rather than taking
them on trust. All four hold.

## The finding that matters most

**`tools/hecke-engine/src/color_weight.rs` implements `PnConvention::
BringColorWeighted` and has ZERO callers.** Verified: its only mention anywhere
in `tools/` is `lib.rs:53: pub mod color_weight;`.

Meanwhile the blind form is what is actually wired, twice:

    gram.rs:726   nf = hm(&nf, 1.0, -half_h, 0, h);   // pn/np: mixed
    gram.rs:888   (1.0, -0.5 * h, m_pn.unwrap_or(crossings_per_pair))

inside `build_atom_nf` and `atom_per_generator_volumes`, both exported to Python
(`pyhecke-native/src/lib.rs:119-121, 139-151`) and dispatched from
`pyhecke/gram.py:994-1000`. Neither takes a `PnConvention` parameter.

**So the engine ships the canonical convention dead and the superseded one
live.** That is a sharper defect than a stale formula: someone wrote the
canonical module and never connected it.

Provenance worth recording: findings 3-4 are the byte-for-byte Rust port of
`hecke_core_legacy.py:598, 911, 1195` — which carries a `DEPRECATION-CANDIDATE`
banner saying "Symbols here are NOT on the canonical derivation chain". **The
port kept the numbers and dropped the banner.**

## Genuine findings

| # | site | note |
|---|---|---|
| 1 | `deltalambda/mu4_rhoF_cluster_derivation_probe.py:93` | `FAC = {"pp": Z, "nn": Z-H, "pn": Z-H/2}`; docstring calls these the "categorically-DERIVED" factors. Verified. |
| 2 | `deltalambda/wlambda_nuclear_braid_connected_probe.py:106` | p-n branch `(1, -H/2)` declared as *the* nuclear-quotient template |
| 3 | `hecke-engine/src/gram.rs:726` | `build_atom_nf` inter-nucleon crossing. Verified. |
| 4 | `hecke-engine/src/gram.rs:888` | `atom_per_generator_volumes`. Verified. |
| 5 | `mass-theory/canonical-braid-interface-composition-table1-data.md:4` | a **definition** block presenting blind as canonical |
| 6 | `appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md:225` | documents wire label `averaged` while citing a module that emits `averaged_weighted` |
| 7 | `mass-theory/eigenvalue-product-expansion-proof.md:12` | a **proof** block; its `[2]/2` eigenvalues follow only from `d = -h/2` |
| 8 | `mass-theory/knot-operator-transition.md:5-9` | every transition operator crosses p-n, all written blind |
| 9 | `mass-theory/crystal-bases-path-a-table1-data.md:5` | interface symbol, blind, unlabelled |

## Witnesses carrying a blind number

Discriminator at the proton pin: `z - h/2 = 0.50815788774…` vs
`z - h(1/2 - delta/4) = 0.50822978937…`, gap `h*delta/4 = 7.190163e-05`.

22 witness files contain the blind constant. Two are directly downstream of
genuine findings — `deltalambda/mu4-rhoF-cluster-derivation.witness.json`
(whose `description` calls the results "the DERIVED (0-fit, q0-only) rho_F
cluster integrals" — **verified**) and
`deltalambda/wlambda-nuclear-braid-connected.witness.json`. Three are
deliberate two-value comparisons and must NOT be drained. The remaining 17 are
unadjudicated.

## Not defects, recorded so they are not "fixed"

Three probes (`probe_9b_gate_interface_algebra`, `probe_9b_laurent_degree_10a5`,
`probe_9b_manybody_expansion`) key the label `"averaged"` to the WEIGHTED value.
They look exactly like the documented trap and are correct. `closed_form_tau_M.
py:238` is the *definition* of the blind kind and is right as written.

## Next

Not a sweep-and-replace. Each genuine site changes a number, so: confirm intent,
check the downstream witness, fix at the producer. The Rust pair (3-4) is the
highest-value single fix — wiring `color_weight.rs` in would close both, and it
is the one place where the canonical implementation already exists.

## 2026-08-25 — the two Rust sites now NAME their convention (`d85f1d581b`)

Not flipped — **named**. `gram.rs` open-coded `-0.5 * h` at both p-n sites
(items 3-4). They now call `color_weight::pn_offset{,_from_h}` under a
`GRAM_PN_CONVENTION` constant whose doc records that it is `StrictAveraged`
while canonical is `BringColorWeighted`, gap `h*delta/4 = 7.19e-05` at the
proton pin.

This also gives `color_weight.rs` its **first caller**. It was a fully ported,
self-checking, 50-dps-validated implementation of the canonical convention with
zero consumers outside its own tests — which is precisely how the blind form
survived next to it.

`gram_pn_convention_is_still_the_blind_one` asserts the live state, so the
eventual flip breaks a test by design: flip + corpus migration land in one
commit or not at all.

**Blast radius of the actual flip (measured, unchanged): 51 Python files, 18
committed witnesses.** Owner-scoped; not an agent edit. Item 3-4 is therefore
*prepared*, not closed.

### Verification lesson worth keeping

`cargo test --lib` reported **212 passed** and that proved **nothing** about
this change: the only atom tests in the suite are `build_atom_nf_vacuum` and
`build_atom_nf_hydrogen`, and **neither has a p-n bond**. A green suite over a
path no test crosses is not evidence, and I nearly reported it as if it were.

Established empirically instead: stashed the change and diffed `build_atom_nf`
+ `atom_per_generator_volumes` at 17 significant digits over deuteron / 4He /
7Li / 3He — identical. Now pinned in-suite as
`pn_offset_is_bit_identical_to_the_open_coded_form` (`assert_eq!` on `f64`,
deliberately not a tolerance).

### A structural note on `build_atom_nf`

It takes `(z, n, h)` — no `q` — so `delta(q)` is not directly reachable there.
That is a **soft** obstruction, not a structural one: `h = q - 1/q` inverts
uniquely on `q > 0` as `q = (h + sqrt(h^2+4))/2`. `pn_offset_from_h` does that,
is exact (no inversion) for the blind convention, and round-trips the
`q`-carrying form under both. Worth recording so the h-only signature is not
later cited as a reason the colour weighting *cannot* be applied there.

### One finding retracted mid-task

I planned to write a test asserting the two conventions differ by `h*delta/4`.
It **already existed** — `colour_weighting_is_a_real_shift_not_a_no_op`.
Corpus-grepped before writing, which is the only reason it did not become a
duplicate. Second time this session that the thing I was about to build was
already there.

## 2026-08-25 — findings 1 and 2 LABELLED (`42d2537721`)

Same posture as the Rust pair: **named, not flipped.** Both probes now
state at the point where the factor is set that they use
`strict_averaged`, that canonical is `bring_color_weighted`, and that the
gap is `h·δ/4 = 7.190163e-05` at the proton pin.

For finding 1 the docstring was the actual defect, not the code line: it
called the per-bond factors *"categorically-DERIVED … Lean-proved exact"*,
which a reader reasonably takes as covering the p-n convention. It does
not. The caveat now says the DERIVED claim covers the **shape** of the
factors, and that the ρ_F results are 0-fit but **convention-conditional**.

Findings 3-9 status: 3-4 done (`d85f1d581b`), 5-9 are content blocks and
remain open.

### A second defect, found only by re-running

Both probes **hand-build** their witness dict (`json.dump`, not
`WitnessBuilder.save`), so `q0Anchor` / `q0Value` / `q0AnchorReason` —
added downstream by transcription — were **deleted on every re-run**.

This is the **"bare producer"** hazard AGENTS.md names in the
witness-staleness triage: *"re-running one deletes the field this audit
keys on … fix the producer to emit provenance first."* Worth recording
because of **how** it fired: on exactly the workflow that document
recommends. A comment-only edit, re-run to refresh `scriptHash` — the
"cheap probe: just re-run" case — and all three keys vanished. I nearly
committed that as a clean regeneration; the only thing that caught it was
diffing the witness for substantive fields before staging.

**So "cheap probes: just re-run" is not safe on its own.** Diff the
witness for *deletions* too, not just for moved numbers. Both producers
now emit the three keys themselves.

Verified across both witnesses: the only diffs are timestamps, commit
shas and the reason text. No computed number moved.

## 2026-08-26 — findings 6, 8, 9 done. ALL NINE dispositioned (`2553296ad5`)

| # | site | disposition |
|---|---|---|
| 1 | `mu4_rhoF_cluster_derivation_probe.py` | LABELLED (`42d2537721`) |
| 2 | `wlambda_nuclear_braid_connected_probe.py` | LABELLED (`42d2537721`) |
| 3 | `gram.rs:726` | NAMED via `GRAM_PN_CONVENTION` (`d85f1d581b`) |
| 4 | `gram.rs:888` | NAMED via `GRAM_PN_CONVENTION` (`d85f1d581b`) |
| 5 | `canonical-braid-interface-composition` | LABELLED (`b63c718177`) |
| 6 | `recursive-atom-knot-atlas-registry` | **FIXED OUTRIGHT** (`2553296ad5`) |
| 7 | `eigenvalue-product-expansion-proof` | SCOPED (`d79217f440`) |
| 8 | `knot-operator-transition` | **MEASURED, conclusion vindicated** (`2553296ad5`) |
| 9 | `crystal-bases-path-a-table1-data` | LABELLED (`2553296ad5`) |

### Finding 6 was NOT a convention choice — the doc was wrong about the code

The registry's inter-nucleon table described generator `3k+2` with the
**intra**-nucleon label and formula (`averaged`, `σ − h/2`) while citing
`atom_canonical_crossings` as its authority. Measured against that producer
for D / ³He / ⁴He: generator `3k+2` returns `sigma`, `sigma_inv` or
`averaged_weighted` — **never** `averaged`. `averaged` is real and the same
producer emits it (six times for ³He), but only for intra-nucleon quark
crossings.

So this one is fixed outright and no number moves: the code was already
canonical here. **Worth generalising** — "the doc disagrees with the code" and
"the code uses the blind convention" look identical from a grep, and only the
first is free to fix. Check which one you have before assuming the flip is
owner-scoped.

### Finding 8 needed a measurement, and I nearly asserted it instead

Its claims are the *Dominant NF* and *Knot type* columns — about which basis
element **dominates**, not about the coefficient. My first instinct was to write
"a 0.07 % perturbation cannot flip a dominance ordering", which is plausible and
was **not** established.

Computed it instead: the H₃ normal form of all five operators under both
conventions.

    p  -> D      (1,0,2) both   margin 9.567x
    D  -> 3H     (2,0,1) both   margin 4.783x
    D  -> 3He    (2,0,1) both   margin 9.567x
    3H -> 4He    (2,1,0) both   margin 9.567x
    3He-> 4He    (2,1,0) both   margin 4.732x

Same dominant element every time; margins 4.7×–9.6× against a relative
perturbation of `δ/2 = 6.9e-4`. Four orders of magnitude of headroom. The
block's conclusions are convention-**independent**; only its written operators
are blind.

Because the block now *asserts* those margins, the check is a real producer —
`computations/probes/knot_operator_transition_convention_robustness_probe.py`,
8 assertions, linked from the block. Exact sympy throughout, evaluated once at
the end at 30 digits.

### What is NOT done

The convention **flip** itself: still owner-scoped, still 51 Python files and
18 committed witnesses. Every disposition above is "name it" or "the code was
already right", never "change the number". Also still unadjudicated: the 17
blind-value witnesses noted in the sweep results (3 of the 22 are deliberate
two-value comparisons and must not be drained).

## 2026-08-26 — the flip is NOT free: the canonical convention is not bar-invariant

Owner asked why the colour weighting applies only at p-n. Answering it turned
up something bigger, and it **changes the flip decision**.

### The structure (five exact identities, none previously in the corpus)

With `bar` = the involution `q ↦ 1/q`:

    bar(z) = 1/(q(q²+1)) = z − h

so **f_pp and f_nn are bar-conjugates of each other**, and

    f_pn(strict)    = (f_pp + bar(f_pp))/2                    ← the bar-symmetriser
    f_pn(canonical) = w_p·f_pp + w_n·f_nn,  w = ½ ± δ/4,  w_p + w_n = 1

**That is the answer to the owner's question.** The p-n factor *is* the
weighted mean **of** the other two; the colour weighting is a δ-**tilt** of
that mean. A like-flavour bond has no mean to tilt — averaging `f_pp` with
itself returns `f_pp` for any weights summing to one — so "colour-averaging
the p-p bond" is a no-op **by construction**, not an omission.

It also makes the producers' name literal: *"uniform bar-invariant
projection"* is not a description of the strict form, it **is** the
bar-symmetrisation of `f_pp`.

### The defect

`δ` is bar-MIXED (`bar(δ) = −q²·δ`), so the tilt breaks bar-invariance:

    bar(f_canonical) − f_canonical = (q−1)⁵(q+1)³(q²+1) / (12q⁵)

nonzero for `q ≠ 1`; **1.67e-05** at the proton pin.

`prop:pn-averaging-uniqueness` states *"…the uniform bar-invariant form and
the Bring color-tube weighted form. **Both satisfy bar-invariance**…"* —
which is **hypothesis (a) of its own uniqueness theorem**. The colour-weighted
candidate does not satisfy it.

**The Lean is fine.** `pn_averaging_unique` is the §3b-cond conditional-class
pattern; `BarInvariant` is an instance hypothesis, so it proves the
implication and is silent on which candidate discharges it. The prose
restating the antecedent as established for both is the
*conditional-proved ≠ premise-established* pattern.

Corrected as **scope**, not resolved: the uniqueness statement covers the
bar-invariant class; the convention made canonical on 2026-08-15 (R3) lies
**outside its hypotheses**. This does not say the colour weighting is wrong.

### What this does to the flip decision

Flipping is **not** merely "re-run 42 producers and move binding by 1.5e-4".
It trades an **exact bar-symmetry** for a flavour-asymmetry correction, and
bar-parity is load-bearing here — a stated hypothesis of a published
proposition. Two of the eight blind-only witnesses (`confined-knot-binding`'s
exact channel cancellation, `b4-connected-bar-parity`'s parity
classification) are plausibly downstream of exactly that symmetry.

**Owner picked "settle bar-parity first" over flipping. That was the right
call and this is why.**

Landed: `84056a59ae` (finding + content), `a1f5a1eed6` (inert-field fix +
a correction to 84056a59ae's own verification line).

### Measured blast radius, corrected from the earlier figures

| quantity | earlier | measured |
|---|---|---|
| Python consumers of the two gram fns | 51 | **54** (42 emit/handle a witness) |
| witnesses carrying a blind constant | 22 | **12** |
| of those, deliberate two-value comparisons | 3 | **4** (carry BOTH constants) |
| unadjudicated | 17 | **8** |

Binding shift from the flip: **−1.46e-4** (²H), −6.4e-5 (³He), −2.0e-5 (⁴He),
−1.8e-6 (⁷Li), −6.7e-8 (¹²C) — falling with A, because canonical ordering
`pᶻnᴺ` has **exactly one** p-n bond. Compare the open many-body binding
magnitude gap, `r* ≈ 1.585`: the flip is ~4 orders of magnitude below it.
It does **not** touch the L2 scoreboard — that producer has zero references to
the interface machinery, and its `m_D`/`m_T` entries are CODATA validation
targets, not framework predictions.

### Verification lesson

I reported "zero issues naming either block" off a `grep -c` count, twice.
A count is not evidence about *which* lines matched. There was one hit
(pre-existing, `chapter:` unknown field); found only by going back for the
line itself. Corrected in `a1f5a1eed6`.


## §3 CLOSED as a negative, 2026-08-26 — PR #5841

Owner authorised §3 with "1y" at the start of the 2026-08-26 session. Result:
**the criterion cannot pick an `E`, and the frame `eps = q*delta*E/4` is
narrower than the set of bar-even p-n factors it was meant to parametrise.**

Lean `QOU.MassTheory.PnOffset`, 12 declarations, sorry-free:

* `weightForm_barOdd` — bar-odd for EVERY bar-even `E`; the criterion selects
  nothing inside the class.
* `weightForm_cubic_factor` — `E` regular at `q=1` forces `eps = O((q-1)^3)`,
  since `delta` vanishes to third order.
* `bond_barInvariant_iff_barOdd` — the factor criterion is the shadow of
  Kazhdan–Lusztig bar-invariance of the BOND element `sigma + d*1`, not a fact
  about the trace.
* `geomMean_*` — a SECOND derived bar-even factor exists: the geometric mean
  of the bar orbit, `sqrt(f_pp*f_nn) = z/q^2`, with bar-odd offset
  `eps = -(q^2-1)/(2(q^2+1))`. It is a genuine convex bond, weights
  (0.448, 0.552) — and it is OUTSIDE the class: its `E` has a double pole
  (`(q-1)^2*E -> -3/2` at `q=1`, not 0).

Measured at the proton pin: `|eps_geom / eps_canonical| = 151.1`, opposite
sign. Not two variants of one convention.

Four candidate narrowing constraints checked and all vacuous as selectors —
confluence, convex weights (`|E(q0)| <= 1310`), the Markov bond form, and the
cubic vanishing order. Probe
`computations/probes/pn_offset_bar_odd_class_probe.py`, 16 assertions.

**No `E` selected.** Fitting one to an isotope anchor would be a fit. What
this leaves is the prior question, which HAS a structural route: does the p-n
bond interpolate its neighbours arithmetically (the Markov trace is linear in
the bond element) or geometrically (the closed form is a product over bonds)?
That is the item worth opening next; "which bar-even E" is not.

Also on the same PR: corrected a claim that landed on main the same morning
(`b858635ee6`, #5828) that `z - h/2` is not q-bar invariant "under either
convention". Under D it IS — `bar(z) = z - h` exactly — and
`MassTheory.strictPn_eq_barSymmetriser` had proved so since #5769, so main was
internally inconsistent. Six further sorry-free declarations in
`ClosedFormInterfaceFactors` §3a.


---

## Cross-reference from PR #5918 — one of the deferred regenerations, metered

`computations/mass-table-comprehensive.witness.json` is one of the witnesses
this bean's flip (`543e30adfd`) deliberately left un-regenerated. Measured
while draining that witness's float64:

  * `B_qCLT_MeV` moves by a **constant -7.92e-4 MeV** and `m_approx_MeV` by
    +7.92e-4, on every row from D (A=2) to 40Cl (A=40) — the once-per-atom
    p-n signature.
  * Established by running the pristine `origin/main` producer against the
    drained one **in the same process**, so the movement is attributed to this
    flip and not to the drain (the drain itself moves these by 2.8e-16 to
    5.5e-14).

PR #5918 re-runs the producer, so this witness lands on the canonical
colour-weighted value there. No action needed on this bean; recorded so the
regeneration is not double-counted or mistaken for a regression.

**One number does not reconcile and is left open in `qou-q3f7`:** the implied
`d(sum_log_V) = 2.1153e-4` is **1.4949x** this bean's single-crossing
`1.41497e-4`, and that is not 3/2 (3/2 would need 2.12246e-4, outside the
6-dp error bar). Either a multiplicity, or the sibling commit `879419b0ac`
also contributing. Untested.


## 2026-09-07 — counts re-measured (10 days on), and one detector false positive fixed

The §"What is NOT done" figures are from 2026-08-28. Re-measured with
`scripts/pn-convention-audit.py` on `main` `e17faad57c`:

| | bean (2026-08-28) | now |
|---|---|---|
| blind-value **witnesses** | 17 (of 22, 3 deliberate) | **6** actionable |
| deliberate two-value comparisons | 3 | **10** (`BOTH`, never drain) |
| witnesses on the canonical value | — | **30** |
| label-only | — | **4** |
| source sites | "51 Python files" | **33 BLIND + 25 MIXED**, plus 35 `COMPARISON` and 5 `DECLARED_BLIND` |

So the **witness side has drained 17 → 6** while the source side is broadly
unchanged — consistent with the flip (`543e30adfd`) having landed and the
deferred regenerations proceeding, and with the source flip still being
owner-scoped.

### A detector false positive, found and fixed

`bond-extensivity-equal-weight.witness.json` was reported as an actionable
**BLIND** witness. Its producer, `bond_extensivity_equal_weight.py:77`, is
listed by the *same audit* as **DECLARED_BLIND** — *"the MODULE DOCSTRING
declares a colour-blind regime: 'EQUAL-WEIGHT'"*. The source scan carved it out;
the witness scan did not, because the two scans had no link.

**A witness now inherits its producer's declared regime** — keyed on the
witness's own `scriptFile` and running the *same* docstring test the source scan
uses, so the two cannot drift apart. It can only ever REMOVE rows from the
actionable list, and a witness whose producer is missing or does not declare is
left BLIND. Result: witness `BLIND` **7 → 6**, new bucket `DECLARED_BLIND: 1`;
source buckets unchanged at 33/5, confirming nothing else moved. `--selftest`
PASS (both conventions reproduce, 14 Python AST probes, 3 Rust regex probes).

Why it matters here rather than cosmetically: this bean's remaining decision is
**owner-scoped**, and it was being presented against an inflated actionable
count.

### One known false positive left, NOT special-cased

`witness-value-copy-audit.witness.json` is reported BLIND on
`findings[152].literal` and `findings[155].literal`. It is a **tree-measuring
audit that quotes literals found in other files** — it asserts no convention of
its own. The producer-inheritance rule cannot catch it (its producer declares
nothing), and keying on a `findings[` path prefix would be a guess about one
file's shape rather than a property of the class. Left visible and named, on the
same reasoning the dangling-path audit leaves PROPOSALS unfiltered.

**True actionable witness count: 5.**

### Unchanged

The convention **flip** itself stays owner-scoped. Nothing here changes a
number; this is a count and a classifier.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Implementation & Witness Progress (PR #8253)
- Branch: `qou-10v9-4e5k-742w-9bei-cblw-fv0s` (`52305a7a1e7f9836f16e0d5d8d454bd72705f9b1`), PR: `litlfred/qou#8253`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/deuteron_trace_discrepancy_m1_rho_constant_sdp_zero_threshold_pn_colour_factor_and_sign_wire_loss_probe.py` -> `computations/probes/deuteron-trace-discrepancy-m1-rho-constant-sdp-zero-threshold-pn-colour-factor-and-sign-wire-loss.witness.json` (`allPassed: true`, `scriptHash: ece5f27ee4a5`, `scriptCommitSha: 1c76aa0739f7803dab0155515577d8888a08fc68`)
