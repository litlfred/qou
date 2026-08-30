# The remaining self-fulfilling assertions, triaged by disposition

**Date:** 2026-08-30 · **Bean:** `qou-3e5m` · **PR:** #6060

---

## 🛑 CORRECTION, same day: 30 is now 11, and my headline was resolved better elsewhere

Written before rebasing onto a `main` that had moved 990 commits. A sibling ran
bean **`qou-26f2`** as a multi-batch campaign over the same population and got
there first. Re-measured with the same detector against both trees:

| tree | MEASURED |
|---|---|
| `main` when this file was written | 56 |
| `main` now | **17** |
| this branch on top of it | **11** |

So the live count is **11**, not 30, and this branch's marginal contribution is
**6**, not 26. Every disposition below still applies to the 11 that remain —
they are `fr_pullback_borromean_h3a_test`, `phi0_normalization_disproof`,
`intermediate_knot_detection`, `lambda_scale_all_c_i_family_a`,
`probe_9b_manybody_expansion`, `probe_bring_residue_resolvent`,
`casimir_q_factorial_probe`, `qbeta_5two_saddle_sum_rule_and_provenance_probe`,
`qbeta_5two_v3_from_borel_poles_probe`, `qbeta_c3_phib_gluing_discriminant_probe`
and `qbeta_uw_reparam_probe` — 7 class R, 3 class D, 1 class C.

**The headline finding below is resolved, and not by me.** I wrote that
`brundan_kleshchev_audit.py:189` asserts a theorem it never tests, called it the
one entry needing an author decision, and recommended rename-and-demote. The
sibling found the same thing and did better: they renamed it
`partition_count_p_{n}`, gave it `expected=KNOWN_P_N[n]` — an independent table
— and wrote the distinction into the source:

> *"Note what IS and is NOT checked. This checks the enumerator against the
> partition function, and it can fail. The identification of p(n) with
> dim Z(H_n) is Brundan-Kleshchev's theorem, cited in `source` — nothing here
> computes a centre dimension, and no assertion should imply it does."*

That keeps a falsifiable check where my recommendation would have removed one.
**Prefer their disposition to mine wherever the two differ**, and the same holds
for `qbeta_5two_stokes_population_bridge_probe` (they derive the expected count
from its three factors) and `qbeta_decay_sdp_extended_ck` (one loop over
`mp.isfinite`, against my three copy-pasted flags and a hand-rolled helper).

**What survives, and is worth more than the count.** Two agents partitioned the
same 56 sites independently, from different starting points, and converged on
compatible dispositions — including on the one case I singled out as needing
human judgement. The four classes below and the discriminators between them are
therefore not one agent's taxonomy; they are the second independent derivation
of it. One place where the sibling's rule is sharper than mine and should be
adopted: **assert `> 0` when finding nothing is the outcome the name exists to
exclude; demote only when finding nothing is a legitimate result.** By that rule
my demotion of `mn_flavor_split_h4_plancherel` was wrong and theirs is right,
and my demotion of `alpha_em_4pi_q_hyperbolic_b3_pslq` (`pslq_executed…`, where
finding no relation IS the answer) is right.

---

A triage, not a sweep. Each of the 30 `MEASURED` self-comparisons still live on
`main` is read at its source and assigned one of four dispositions, with the
evidence that decides it. Nothing here is applied — see §Why this is a document
and not a commit at the end.

## What a MEASURED self-fulfilling assertion is

`add_assertion(name, computed=X, expected=X)`. It computes a quantity, compares
it to itself, and is recorded in the witness as an assertion that **passed**. It
looks like a check from every consumer's point of view — the witness's
`allPassed`, the audits that count assertions, a reader scanning the file — and
it cannot fail. The quantity can invert, go NaN, or drift by a factor of ten and
the record is unchanged.

The population is 56 on `main`; this PR resolves 26; these are the other 30.

The partition below is total and disjoint: **1** misnamed claim + **12**
repairable + **9** author-documented recordings + **8** counts and labels = 30.
Two files contribute two findings each (`li6_h18_amplification_discriminator`,
`shift_from_nf_basis`) and one contributes three (`mass-from-q-symbolic`), so
the file count is lower than the finding count throughout.

---

## The one that is not like the others

**`computations/audits/brundan_kleshchev_audit.py:189`** — `dim_centre_eq_pn_{n}`

```python
pn = len(partitions_of(n))
builder.add_assertion(
    name=f"dim_centre_eq_pn_{n}",
    computed=pn,
    expected=pn,
    source="number of partitions p(n) = dim Z(H_n)",
)
```

Every other entry below is a *recording* wearing an assertion's clothes. This
one is a **theorem name over a tautology**. The declared claim is
`dim Z(H_n) = p(n)` — Brundan–Kleshchev's graded-simples count for the KLR
principal block. The producer computes `p(n)` and compares it to `p(n)`. It
**never computes a centre dimension at all**, and has no route to one: nothing
in the file constructs `Z(H_n)`.

So the witness records five passing assertions (n = 2..6) named for a theorem
that was not tested. That is materially different from recording a number, and
it is the reason this file leads the triage rather than sitting in class C.

It is also the disposition I will not pick alone. Two options, and they are not
close in cost:

- **Compute the centre dimension** — real work, and the honest version of what
  the name promises.
- **Rename and demote** — `p(n)` recorded as data, the Brundan–Kleshchev claim
  moved to prose or to a Lean statement where it can be stated without
  pretending to be measured.

Recommendation, marked as my judgement: **rename and demote**, because the
alternative silently expands a Hecke-centre computation into an audit script,
and the claim's real home is Lean.

---

## Class R — a real check is available, and the producer already holds it

Eleven sites, twelve lines. In each, the falsifiable claim is already stated in
the assertion's own `name` or `source`; only the `expected` argument is wrong.

| site | the claim its own name/source makes | the repair |
|---|---|---|
| `probes/qbeta_5two_v3_from_borel_poles_probe.py:383` | `V3_measured` is closer to GGM than to the legacy literal | `expected=0.0, tolerance=d_leg` — passes iff `d_ggm < d_leg` |
| `shift_from_nf_basis.py:256` | proton H₃ shift is finite | **delete**: lines 271-278 already assert it against `expected=20, tolerance=2` |
| `shift_from_nf_basis.py:262` | neutron H₃ shift is finite | **delete**: same, `expected=16` at line 278 |
| `probes/casimir_q_factorial_probe.py:212` | *"If > 0, at least one q-deformation reproduces classical Casimir"* | `computed=1 if n_sub_one_pct else 0, expected=1` |
| `probe_bring_residue_resolvent.py:59` | `\|1 − h_q·qⁿ\| > 0 at q₀` | nonzero flag, `expected=1` |
| `hecke/phi0_normalization_disproof.py:146` | the gap `\|N_h2 − N_h4\|` is **large** (~72) ⇒ no constant Φ₀ | threshold flag |
| `binding_shell_enhancement_derivation.py:211` | best derived `f` leaves **≥ 12 %** on A ≥ 3 | threshold flag |
| `probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py:338` | the legacy pair **violates** the exact relation | the sibling at line 333 shows the form: real `expected` + `tolerance` |
| `probes/qbeta_5two_stokes_population_bridge_probe.py:235` | σ-pair amplitude overshoots the Habiro scale **by > 1e4** | threshold flag |
| `qbeta/qbeta_markov_trace_norm_probe.py:309` | shapes **differ** per channel (non-zero expected) | nonzero flag |
| `qbeta/qbeta_uw_reparam_probe.py:290` | `v` leading ε-coefficient **≠ 0** | flag; siblings at 284 and 296 already use real `expected` (`"0"`, `"2"`) |
| `intermediate_knot_detection.py:206` | knot detected — the real test is `cos_sim > 0.7` | assert the threshold, **outside** the `if` that currently guarantees it |

Three notes that generalise beyond the table.

**The claim was never missing; it was in the wrong field.** In every row above,
someone wrote the falsifiable statement down — in the name, or in `source` prose —
and then passed the measured value as its own expectation. The information needed
to make the check real was in the file the whole time.

**Four of the twelve sit next to a correctly-formed sibling.** `qbeta_uw_reparam`
has real `expected` values on the lines immediately above and below;
`qbeta_5two_saddle_sum_rule` has one four lines up; `shift_from_nf_basis` has two
fifteen lines down that make the tautological pair redundant outright. Proximity
to a correct example is not protective.

**`intermediate_knot_detection.py:206` is the subtlest.** Its assertion sits
inside `if final['cos_sim'] > 0.7:`. So the guard already encodes the real test,
and the assertion inside it can only ever run when the test passed — a
conditional that makes its own body vacuous. Moving the threshold into the
assertion and dropping the guard is the whole fix.

---

## Class D — the author said so in the source

Nine lines across seven files. Each carries prose stating that the value is
recorded rather than checked. These need no judgement about intent; they need
`add_data`.

| site | the author's own words |
|---|---|
| `deltalambda/li6_h18_amplification_discriminator_probe.py:544` | *"recorded value, self-referential by design (no target smuggling)"* |
| `deltalambda/li6_h18_amplification_discriminator_probe.py:550` | *"recorded verdict, self-referential by design"* |
| `fr_pullback_borromean_h3a_test.py:564` | name is `..._recorded`; source ends *"(self-consistent run)"* |
| `mass-from-q-symbolic.py:518` | `expected=P_p_num,  # self-consistent (no independent measurement)` |
| `mass-from-q-symbolic.py:527` | same, neutron |
| `mass-from-q-symbolic.py:576` | same, Skein ratio |
| `probe_9b_manybody_expansion.py:279` | source opens *"informational:"* |
| `qbeta/qbeta_c3_phib_gluing_discriminant_probe.py:152` | *"recorded exact-locus distance ... (informational)"* |
| `qbeta/qbeta_singularity_cross_anchor_probe.py:303` | *"Recorded, not gated: this probe reports the premise's status, it does not assert it."* |

**This class is the argument for the API gap.** Nine times, an author knew the
value was not a check, wrote that down in the code, and used `add_assertion`
anyway — because `WitnessBuilder` offered no other way to get a named scalar
into the witness's assertion-shaped record. The last one is the sharpest: a
comment saying *"it does not assert it"* attached to an `add_assertion` call.

---

## Class C — a count or a label recorded as an assertion

Eight files. Same shape as the seventeen already demoted in this PR: the
quantity is a cardinality, an enumeration, or a name, and there is nothing to
compare it against.

| site | what is being "asserted" |
|---|---|
| `basis_knot_tables.py:183` | per-operator e⁻ pair count |
| `photon_operator_table.py:205` | per-operator e⁻ pair count (identical shape) |
| `crystal_shift_nf_atomic.py:537` | `len(results)`, named `crystal_pole_counter_well_defined` |
| `per_observable_100x_status.py:798` | number of rows in the observable table |
| `universal-ilp.py:275` | the selected operator's **name** (a string) |
| `lambda_scale_all_c_i_family_a.py:161` | each `c_i` of a closed-form expansion, stringified |
| `tau-lepton-nf.py:191` | per-lepton NF net amplitude |
| `hadron_knot_table.py:258` | per-atom `tr_M` |

Two carry a caveat.

**`lambda_scale_all_c_i_family_a` and `tau-lepton-nf` are class C only if you
decline the second route.** Both record a value with a stated derivation — a
closed-form expansion of `(3q² + 4 + 3q⁻²)/4` in `h`, and a Chebyshev /
Morgan–Voyce recurrence. Either could be independently re-derived symbolically
in the same script and compared, which would move them to class R. That is a
real check and real work; demotion is the honest floor, not the ceiling.

**`hadron_knot_table.py` is the expensive one.** Any change to it requires
regenerating its witness, and this producer runs **> 50 minutes for a single
bound atom** (measured 2026-08-24; AGENTS.md records the run, killed by its own
timeout at deuterium). Budget it separately from the other six, which are
seconds.

---

## Why this is a document and not a commit

Every disposition above — demotion included — changes what a producer writes,
so it requires regenerating that producer's witness. **This container cannot do
that honestly.** It was replaced partway through the session and the replacement
is strictly weaker than the one the witnesses record:

| | recorded in the witnesses | this container |
|---|---|---|
| python | 3.13.12 | **3.11.15** |
| mpmath | 1.4.1 | **1.3.0** |
| numpy | 2.5.0 | **2.4.6** |
| scipy | 1.18.0 | **1.17.1** |
| clarabel | 0.11.1 | **absent** |

**And the tooling's protection does not cover this case — read it before
assuming it does.** `save()` guards the environment on the *preserve* path:
when `_witnesses_substantively_equal(existing, witness)` holds, a weaker block
"still preserves (never degrade a file we were not otherwise rewriting)". That
is a real guard and it would cover an idle re-run. It does **not** cover any
disposition in this triage, because every one of them — demote, threshold,
delete — changes the `assertions` array, so the witnesses are *not*
substantively equal, `save()` takes the rewrite path, and the weaker block goes
in. The one condition under which the guard fires is the one condition under
which there was nothing to protect.

`_check_environment_regression` names the damage and why it survives review:
*"the numbers may be untouched while the file now claims they came from a
weaker environment than they did"* — bean `qou-y0xk`, where a stripped block
was merged and the corrected re-run changed **zero** physics fields. The loss is
pure provenance, and provenance damage is invisible in a diff of values. The
check is warn-only by design, so nothing would stop the commit.

The python version cannot be matched at all here, so this is not a
`pip install` away.

So the measurement is the deliverable, and applying it belongs to a container
that matches. The order I would work them in, cheapest-first:

1. **`shift_from_nf_basis.py`** — delete two redundant lines; the real
   assertions already exist. No behaviour change beyond removing a false pass.
2. **The nine class-D sites** — mechanical, author intent already written down.
3. **The eleven class-R sites** — each needs the threshold read out of its own
   `source` prose, one at a time. This is where the value is: eleven checks that
   currently cannot fail become eleven that can.
4. **Class C, minus `hadron_knot_table`** — mechanical.
5. **`hadron_knot_table`** — schedule the > 50 min run.
6. **`brundan_kleshchev_audit`** — author decision first.

## The API gap underneath all four classes

Sixteen of the thirty (classes D and C) exist because `add_assertion` was the
only way to get a named scalar into the record. `add_data` takes a dict and
reads as a payload, not as a named finding; `add_parameter` reads as an input.
Nothing expresses *"this run measured X, and X is a result rather than a
check"* — nor the three shapes class R keeps re-implementing by hand: **is
nonzero**, **is finite**, **exceeds a threshold**.

Every repair in class R above encodes one of those three as a `1`/`0` flag with
`expected=1`. That works, and this PR uses it. But eleven hand-rolled flags is
the signature of a missing constructor, and until one exists this population
will regrow. That is the deeper fix, and it is not proposed here.
