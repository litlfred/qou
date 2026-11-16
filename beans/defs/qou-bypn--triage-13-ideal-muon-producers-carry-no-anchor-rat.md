---
# qou-bypn
title: 'TRIAGE: 13 ideal_muon producers carry no anchor rationale in their own source'
status: in-progress
pr: 8184
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T19:40:03Z
updated_at: 2026-11-16T20:16:00Z
parent: qou-2002
---

Split out of `qou-1c4y` (the tracked muon->proton migration) after re-measuring
the manifest on 2026-08-25. Related: `qou-aj91` (85 producers read the
anchor-defining witness directly), `qou-dkm2` (`load_q_50dps()` defaults muon),
`qou-7vm4` (one producer whose manifest entry and code disagree).

## The claim

`computations/q0_anchor_manifest.json` lists **35** stems under `ideal_muon`.
`qou-1c4y` justifies **7** of them:

    3  refuse a proton run loudly   atomic_tr_m_mpfr_50dps, cross_check_trM_1ppb,
                                    he4_stage2_ranking_seminormal_xcheck
    2  straddle silently            chi_lambda_he4_full_partition_table,
                                    bwhk_st_matrix_corroboration
    1  defines the anchor           q_pinning_50_digit
    1  needs BOTH pins              q0_anchor_consistency_audit

Of the remaining 28, **13 carry no anchor rationale anywhere in their own
source** — no `muon`, no `CAL-2`, no 50-digit muon literal, no anchor-mode
docstring. They are on the muon pin because a JSON file says so, and
`ideal_muon` is a **live control input**: `q_parameter` applies the muon anchor
to any stem listed there (`gen_q0_anchor_manifest.py` header; the classifier
refuses to auto-propose `ideal_muon` for exactly this reason).

## The 13, split by HOW they get q0 — the split decides the fix

**A. via `q_parameter` (5) — the manifest entry is the live re-pin.**
Removing the stem moves the number by ~11.5 ppb. Each needs a decision, not a
sweep.

    computations/alpha/alpha_5_lp_dual_crystal.py
    computations/block_swap_binding.py
    computations/probes/gram_norm_binding_probe.py
    computations/hadron_knot_table.py
    computations/he3_tritium_cosh_asymmetry_diagnosis.py

**B. read `q-pinning-50-digit.witness.json` directly (7) — the manifest entry is
decorative.** These are `qou-aj91` mechanism-5 producers: they bypass
`q_parameter` entirely, so they get muon from the file whether or not the stem
is listed. Removing the stem changes nothing; the fix is to route them through
`q_parameter`, and only then does the pin move.

    computations/hydrogen_step_by_step.py
    computations/low_isotope_sign_flip_diagnostic.py
    computations/mass_sweep_wiring_status.py
    computations/qbeta/qbeta_decay_sdp_extended_ck.py
    computations/qbeta/qbeta_fsc_g_pattern_comparison.py
    computations/qbeta/qbeta_symbolic_sdp_strict_complementarity.py
    computations/verify_isospin_bar_anomaly.py

**C. `load_q_50dps()` (1)** — inherits the muon default; blocked behind
`qou-dkm2`.

    computations/binding_via_interface_knot.py

## Two FALSE POSITIVES, recorded because the heuristic produced them

The scan keyed on muon-vocabulary in the source. That over-flags:

  * `chi_lambda_he4_full_partition_table` — zero muon words, but it is one of
    the two deliberately-kept silent straddlers; the reason lives in `qou-1c4y`,
    not in the file. **Absence of a rationale in the source is not absence of a
    rationale.**
  * `terms_2_3_atom_per_gen_mpfr_50dps` — zero muon words, but its docstring
    documents an explicit dual-layer mode with `"experimental" (DEFAULT) proton
    pin`. It is a deliberate both-anchor producer.

So this is a **triage list, not a defect list**. Two of fifteen candidates were
already answered; expect more of the thirteen to be.

A third trap: `git ls-files` resolves the stem
`terms_2_3_atom_per_gen_mpfr_50dps` to **two** files, one of them under
`_deprecated/`. A first-match lookup picks the deprecated copy and reports the
producer as dead. Both share a stem, so `q_parameter` pins both identically.

## Definition of done

For each of the 13: either a one-line in-source note saying why the muon pin is
required (and, for group B, a `q_parameter` route so the declaration is real),
or removal from `ideal_muon` with the witness regenerated at proton. Not a
sweep — `ideal_muon` entries are numerical decisions one at a time.


---

## UPDATE 2026-09-04 — group A's "each needs a decision" is superseded for at least one member

This bean is dated 2026-08-25. The owner's ruling of **2026-08-30** (recorded
in AGENTS.md §q₀ anchor convention, reaffirming the 2026-08-15 directive for
the `qou-p77d` tranche) post-dates it and supplies exactly the decision rule
group A was waiting for:

> *"it should be proton unless it is an explicit comparison / discussion on
> CAL 123 math ideal or so."*

with two named exceptions — **(E1)** the producer's *purpose* is measuring the
proton-vs-muon difference, **(E2)** it is *about* the ideal CAL-1/2/3 layer as
mathematics — and the burden explicitly on the exception: *"'it is in the
`ideal_muon` list' is NOT a reason — that list is what is being migrated."*

So group A's five are no longer "a decision each" in the sense this bean meant.
They are: name E1 or E2, or they are proton.

**Worked for one of the five, `computations/hadron_knot_table.py`:** neither
exception can be named. The docstring names no pin, no comparison and no CAL
layer — it computes *"mass formulas and Q-value predictions"*, observable
evaluation — and its witness's `q0AnchorReason` is **`None`**. Under the ruling
it is a **proton** producer.

What blocks acting on it is cost, not the decision: constraint 4 requires the
manifest change and the re-pinned witness to land together, and this producer
is the corpus's one that cannot finish (`qou-i7ju`, `qou-r4w5`). The other four
of group A are not known to have that problem and should be cheaper to settle
the same way.

The ~11.5 ppb this bean cites as the cost of removing a stem is still right and
is still the reason not to sweep — but it is now the *size* of a change the
ruling has already authorised for the non-exception cases, rather than a reason
to hold each one for the author.

## Progress Update (2026-11-16, PR #8184)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/AnchorManifestTriageAndAmeFloatDrain.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/anchor_manifest_triage_and_ame_float_drain_probe.py` and stamped witness `computations/probes/anchor-manifest-triage-and-ame-float-drain.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 100f1be37af2187c6d27ac18b72a859b25538c6c`).
- [ ] Awaiting merge of PR [`litlfred/qou#8184`](https://github.com/litlfred/qou/pull/8184) (`0a6bb0fe54cf925fb3bdc7285374e8ee0913d6dd`).

