---
# dgpc
title: 'Tier C: family chains — one chain drains many witnesses'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-10-04T15:14:14Z
parent: qou-5vkl
---

Parent dgap. 66 witnesses across producers that emit MORE THAN ONE witness. The audit matches
producers by BASENAME, so one `script:` note in one chain claims the whole family — highest
yield per chain authored.

Queue (re-run the categorizer for current counts):
  26  _habiro_coefficient_extract.py
   6  nucleus_real_sdp.py
   4  compute_atom_chi_rust.py
   4  chi_at_q0_via_matrix_m_mpfr.py
   3  bar_pairing_binding_observable.py
   3  chi_via_rust_lossless.py
   2  A_operator_extract_at_level.py / alpha_k_jones_markov_h3.py / _h4.py / others

DONE: canonical_isotope_witness.py (120 shards) — see the worked example in the program doc
for what a composition chain may and may not claim.

---
2026-08-18 PROGRESS. Two families drained (branch claude/dgpc-habiro-family-chain-2026-08-18):
 - canonical_isotope_witness.py  -> 122 witnesses (composition/orchestration chain)
 - _habiro_coefficient_extract.py -> 26 witnesses (genuine symbolic extraction: Phase 5q closed
   form -> u=q^(1/2) rational form -> sequential cyclotomic division into the Habiro basis
   (u;u)_m, with the witnesses' own falsifiable checks all_integral + reconstruction_matches
   + tr_M_at_q0_rel_err = 0)
Trust audit: derivation-backed 7 -> 155; computational-only 2630 -> 1722.

METHOD NOTE (cost me a wrong conclusion, worth recording): I first judged the 27 habiro
witnesses "thin" because a quick check looked for habiro_coefficients under data.{...}. These
witnesses carry it at the TOP LEVEL. The witnesses are rich; the check was wrong. Inspect a
full witness before concluding a family is empty -- and note the two families needed DIFFERENT
chain shapes (composition vs extraction), so shape must be read per family, never assumed.

REMAINING families are small (6, 4, 4, 3, 3, then 2s) -- diminishing yield per chain authored.
After these, tier D (per-compute authoring) is where the bulk sits.


## 2026-08-19 — batch 2 (PR #5289)

Drained: `nucleus_real_sdp.py` (6) + the sign-only chi family (7).
**1723 -> 1710** computational-only; derivation-backed 161 -> 168.

**The categorizer's families are not always one derivation.** Four
producers group as "chi" by basename; only two share a derivation.
Measured, not read off docstrings (which are stale on precision):

| producer | deuteron chi^(6) | convention | in chain? |
|---|---|---|---|
| `chi_at_q0_via_matrix_m_mpfr` | 11.02137498091048471910 = q_0^23 | sign-only | yes |
| `chi_via_rust_lossless` | (5Li/6Li; same convention, declared) | sign-only | yes |
| `compute_atom_chi_rust` | 1.55987030806094099130 | averaged | **no** |
| `derived_chi_catalogue_matrix_m_mpfr` | (mu_p/mu_n LR factorisation) | different construction; its 2 witnesses sit on DIFFERENT q0 pins | **no** |

The `q_0^23` identity cross-checks against the crossing count already in
`atomic-braid-recipe-d.derivation.json` — an independent confirmation the
chain now records as its step 5.

**Rule for the rest of the queue:** before authoring a family chain,
check that the family shares a *derivation*, not just a producer prefix.
Merging on the prefix is the arity conflation AGENTS.md warns about.

### Two tool defects found while running the preflights (both fixed in #5289)

1. `derivation_chain_validator.py` re-evaluated `c-q-q0` against the
   module-level (proton) `Q_0` while the chain declares the muon pin —
   a layer straddle. `c_q` amplifies ~10x, so the 11.5 ppb mu-p tension
   read as `rel_diff 1.16e-07` and the chain had been **FAILING on main**.
   Now validates at the pin the chain declares.
2. `mpf_context_dps_audit.py` walked `.claude/worktrees/`, so
   `precision-gates.sh` was **RED for every agent in this container** on
   findings from a sibling branch's checkout. Excluded.

### Remaining tier C (~21 witnesses, all families <= 4)

`compute_atom_chi_rust` (4, averaged convention — own chain),
`derived_chi_catalogue_matrix_m_mpfr` (2, own chain),
`bar_pairing_binding_observable` (3), `chi_via_rust_lossless` [drained],
then 2s. **Yield has flattened**: batch 1 was 26/chain, batch 2 was 6-7,
the rest are 2-4. Worth asking whether the tier-D boundary (1233
singletons) or the tier-E provenance triage (186 orphans) is the better
next spend before grinding 2-witness chains.


## 2026-08-19 — tier-E orphan triage (owner: "move those without provenance into _deprecated/")

**1711 -> 1698** computational-only; **E-orphan 186 -> 169**.

- **13 deprecated** (`git mv`, never `git rm`): scriptFile null, no producer
  under any name/suffix, zero refs outside the six inventory witnesses.
- **4 recovered** as false orphans — the categorizer had three
  over-reporting defects (scanned only `computations/`, only `*.py`,
  and guessed `.py` unconditionally so `substrate/*.sage` producers
  sitting beside their own witness did not match). Fixed.
- **6 rescued from the move** by checking f-string templates, not just
  literal basenames: `chi-{atom}(-free)-h{n}-at-qinv-50dps` is written AND
  read by `bar_pairing_binding_observable.py`. **A witness whose name is
  built by an f-string is invisible to basename analysis** — general lesson.
- **1 frozen**: `binding-lp-delta-audit` scores dead but is named in an
  OPEN devil's-advocate objection (wave4, `null-dual`).

### The finding that needs its own bean

**147 of the 186 orphans are read by live code** — `aK_via_lp_dual.py`,
`low_isotopes_binding_sweep.py`, `binding_depth_stratified_lr.py`, a content
block (`mba-step09b-per-isotope-binding.ts`), a Lean file, and
`content/values/registry.ts` (the witnessed-values registry). A value flows
into the paper from a file **nobody can regenerate**. Worse than either dead
or healthy; not a retirement job. Needs: reconstruct the producer, or freeze
the witness explicitly as a declared constant input.

Audit: `docs/audits/2026-08-19-tier-e-orphan-triage.md`


## 2026-08-19 — Parts 2-4: provenance trace + the gate that let it through

**One real paper defect.** `content/values/registry.ts` pins
`B_4He_AME_MeV = 28.295674` from a producerless artifact; the corpus's own
AME2020 source says `28.295673`, and all five compute consumers use the AME
value. **The paper prints a different last digit than the compute layer.**
Which digit is right needs the actual AME table — a back-of-envelope from mass
excesses gave a third value (~28.29566). This is the `fvxq` UNSAFE class.

Source: commit `e52487a2` (2026-04-20) records that run as a FAILURE
("blows up to 1.98M MeV"); the registry pins its experimental **by-product**
field. Producer never committed.

**The gate.** `witness_provenance_audit.classify` scored by emptiness, and a
prose marker is a non-empty string — so the I14 campaign reached
`completeness_ratio: 1.00` partly by *writing* the marker. Fixed: a prose
`scriptFile` now counts as missing. `PROV_MISSING 49 -> 54`, completeness
`0.981 -> 0.979`. Five surface, including both paper-facing ones and three not
previously known.

**Caught my own over-fire before shipping:** the first version ran the prose
predicate over all of `REQUIRED_FIELDS` and flagged 49 `engine` descriptions
(`"sympy + pyhecke_native"`). Restricted to `PATH_VALUED_FIELDS`.

**Retracted:** the `rho-k-markov-multiplicativity` "PROVED" flag. Live witness,
live producer, and the content correctly cites Wenzl 1988 Thm 5 as the proof
with the witness as corroboration. It only *looked* producerless because a
`_deprecated/` twin made the resolver's uniqueness test ambiguous.

### The pattern worth carrying forward

Four instances, two directories that must never appear in an audit's repo-wide
`rglob`: **`.claude/`** (checkouts of other branches) and **`_deprecated/`**
(retired copies). Both are invisible in review and both fail *toward* the
dangerous verdict — a phantom red that trains agents to skip a gate, or a false
orphan whose recommended disposition is deletion.

### Tier-E accounting, Parts 1-4

`186 -> 134`. **28% tool error, 7% genuinely dead, 65% load-bearing.**

Open owner decisions: re-point `B_4He_AME_MeV` (gated on `fvxq`); downgrade or
reconstruct the two `mba-step02` blocks at `status: "verified"`; which of the
five prose witnesses belong on the acknowledged floor.



## Reclassified 2026-09-05 — mechanical backlog, misfiled into an owner-gated cluster

This is a Tier-C drain queue with per-family counts and recorded progress (two
families drained on `claude/dgpc-habiro-family-chain-2026-08-18`). There is no
decision in it. It was swept into owner-gated Cluster 7 as "a `status:
verified` downgrade", which is a step *inside* the work, not a question for the
author. Off the owner-gated queue; ordinary backlog.


## Correction to my reclassification note above (2026-09-05)

The note says *"There is no decision in it."* That is right about the thing
Cluster 7 attributed to this bean (a `status: verified` downgrade, which is a
step inside the work) and **wrong about the bean as a whole**. The Tier-E
accounting at the end names three open owner decisions:

- re-point `B_4He_AME_MeV` (gated on `fvxq`);
- downgrade or reconstruct the two `mba-step02` blocks at `status: "verified"`;
- which of the five prose witnesses belong on the acknowledged floor.

Those are real and they stay. What does not belong on the owner-gated queue is
the **drain** — the family-chain work itself, which is mechanical and has
recorded progress. Stays open as backlog; the three decisions above are its own,
not Cluster 7's.

**Its transferable finding is worth more than its queue position**, and it is
the same family as today's detector work: two directories must never appear in
an audit's repo-wide `rglob` — **`.claude/`** (checkouts of other branches) and
**`_deprecated/`** (retired copies) — because both are invisible in review and
both fail *toward* the dangerous verdict: a phantom red that trains agents to
skip a gate, or a false orphan whose recommended disposition is deletion. Its
Tier-E accounting quantifies that: `186 → 134`, **28 % tool error**, 7 %
genuinely dead, 65 % load-bearing.

Compare today's vacuity-detector blind spot (a reducible `abbrev` made a
verbatim self-assuming projection character-different, so the cleanest instance
of four went unreported). Same shape: the detector was right about what it
measured and blind to how the tree was spelled.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 94 PR (`litlfred/qou#8500`)**: Formalized `FamilyChainErrorPartitionLedger`, `canonicalFamilyChainErrorPartitionLedger`, `family_chain_three_way_decomposition`, and `family_chain_cubic_factorization` in `QOU.Foundations.LeafOleanConeBatchingDeferredStructuralCleanupSiblingVerificationClassificationFamilyChainErrorPartitionSubstrateProbeCancelHotspot` with 80-dps witness (`HEAD = 37841388326f8fad43c7ffaa9f1c59e901153736`).
