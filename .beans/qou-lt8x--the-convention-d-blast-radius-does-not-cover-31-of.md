---
# qou-lt8x
title: 'The convention-D blast radius does NOT cover 31 of the 43 structurally-C witnesses: read-set != write-set'
status: in-progress
type: task
priority: normal
created_at: 2026-08-11T01:13:43Z
updated_at: 2026-08-16T13:48:41Z
---



## The gap

`.work/convention-d-blast-radius.json` was built by one question — *which
producers **read** one of the four witnesses the D migration moved?* (146
producers, 188 witnesses). The campaign then treated that queue as the
convention-C work list.

It is not. Measured against the content detector:

| | |
|---|---|
| structurally-C witnesses (`convention-c-witness-audit.py --list`) | 43 |
| of those, written by a blast-radius producer | **12** |
| **not reachable by the sweep at all** | **31** |

Reading a moved witness and *being* convention C are different properties.
A producer can carry convention C entirely on its own — the `chi-*-at-q0-50dps`
family, the `rho-k-h3a-*` siblings, `a-K-via-lp-dual` — without reading any of
the four. The sweep cannot fix what it never visits, and it exits reporting
success.

This is the same shape of error as the two that came before it, one level out:

- fingerprint list ⇒ finds only `n = 3` (reopened `qou-eea0`);
- content tests ⇒ miss derived-value witnesses (`qou-8x1l`, fourth class);
- **read-set queue ⇒ misses producers that are C on their own.**

Each detector was correct about the property it tested and was then used to
answer a question it does not answer.

## Complement, resolved

`.work/convention-c-complement.json` — 31 witnesses, producer resolution
attempted for each. 18 resolve to a live producer and are runnable:

    aK_via_lp_dual{,_full}, alpha/alpha_k_jones_markov_h12,
    binding_a3plus_{full_theta_assembly,joint_ji_combiner},
    categorical_bypass_volmatch_demo, chi_4he_binding_lossless,
    chi_at_q0_via_hoefsmit_mpfr (x3), derived_chi_catalogue_build,
    habiro/habiro_h9_spectral_decomposition, probe_1b_li6_orthogonality,
    probe_option_e_phase2_crystal_vertex_candidates,
    probe_pauli_young_delta_lambda_the3_signtest,
    rho_k_h3a_{co_casimir,counit_canonical_integral,frobenius_pairing}

13 do not, in three kinds:

| kind | count | witnesses |
|---|---|---|
| **Rust binary** | 4 | `rust-chi-q-via-gp-lossless`, `matrix-m-chi-q-via-gp` — the layer `qou-j6il` found returning C while its source read D. Do not regenerate before the convention gate reaches the binary. |
| producer in `_deprecated/` | 6 | the `y-lambda-*` / `wenzl-y-lambda-h{9,12}` family — `qou-8x1l` already showed "retire it" is unsafe here, since six live producers read them |
| no `scriptFile` at all | 3 | `chi-dineutron-h6`, `chi-diproton-h6`, `rho-w-crystal-vertex-trace` |

## To close

1. Run the 18 resolvable producers (serially, same harness, own journal).
2. Re-run `--list`; the 13 should be all that remains, each with a recorded
   reason rather than an omission.
3. Fix the queue-construction defect itself: the work list should be the
   **union** of (reads a moved witness) and (fails a content test), not either
   alone. Both are already computable.

## The native work list already asks the right question (2026-08-11)

The harness's own `work_list()` is keyed on **being** convention C — the
three content tests — not on reachability. The `--from blast-radius` override
is what substituted the wrong question; the default was correct all along.

Measured programmatically (importing `work_list()`, not grepping `--plan`):

| | |
|---|---|
| native `work_list()` | **67** witnesses — 41 with a producer, 26 orphan |
| this bean's complement | 31 |
| complement already in native | **27 / 31** |
| in complement, NOT native | **4** |

So the resolution is not to merge two queues: it is to **drop `--from` and run
the harness natively**. The complement was a symptom of the override, and 27
of its 31 entries were never outside the real list.

The four genuinely outside it need explaining before any sweep claims
completeness — a structurally-C witness absent from a convention-C-keyed work
list is either a `_deprecated/` exclusion, an unparseable doc, or a detector
disagreement:

    computations/binding-a3plus-full-theta-assembly.witness.json
    computations/binding-a3plus-joint-ji-combiner.witness.json
    computations/chi-helium-4-h12-numeric.witness.json
    computations/probe-option-e-phase2-crystal-vertex-candidates.witness.json

(`chi-helium-4-h12-numeric` is already documented in
`computations/_deprecated/README.md` as a live input with no producer — the
mis-filed-orphan case — so at least one of the four has a known cause.)

### A measurement error worth recording

First attempt at this comparison grepped the `--plan` stdout and reported
"16 of 31 missing". That was wrong: `--plan` prints producers as
`producer -> N witness(es)` and names witnesses **only** on ORPHAN lines, so
any witness owned by a producer was invisible to the grep. The real number is
4. Same shape as the defects this bean is about — measuring the artifact
instead of the property — which is why it is written down rather than quietly
fixed.

## Roots vs derived — what re-running can and cannot fix (2026-08-11)

The sweep's negative (11/41, not one witness moved C -> D) has a structural
explanation. Splitting the 44 producer-owned convention-C witnesses by whether
their producer READS another convention-C witness:

| | |
|---|---|
| ROOTS — producer reads no C witness | **29** |
| DERIVED — producer reads C | **15** |

Re-running can only fix a ROOT. A derived witness reproduces C faithfully
however many times its producer runs, because the C enters through its input.
That is why 41 green `ok`s would not have been a migration.

The 29 roots are the actual front:

    all-nuclides-wedderburn-spectral-v2   alpha-k-jones-markov-h12/h3
    binding-k-enumerator                  bond-extensivity-equal-weight
    categorical-bypass-volmatch-demo      chi-helium-4-h12-at-q0-50dps-binding
    chi-lithium-5-h15 / -6-h18            chi-tritium-h9-at-q0-50dps-matrix-m
    derived-chi-catalogue                 deuteron-tower-fusion-frame-probe
    e0-lambda-composite                   entanglement-orders
    gram-matrix-dual                      h2o-bond-angle-magnitude-vsepr
    markov-z-fibre-rank-bar-covariance    option-e-phase1-h3-cross-check
    pentagon-to-borromean-h4-probe        per-irrep-pole-deuteron-h6 / -proton-h3
    probe-1b-li6-orthogonality            q-hecke-seminormal-character-closure-probe
    qbeta-c3-barodd-binding-sdp-dual      qbeta-counit-substrate-consistency
    rho-k-h3a-refinement                  tr-m-q-hecke-seminormal
    v-hat-z-transfer-phase5d-4            weight-factor-audit

But note the sweep already re-ran several of these (alpha-k-jones-markov-h3,
bond-extensivity-equal-weight, weight-factor-audit, all-nuclides-...) and they
stayed C. So being a root is necessary, not sufficient: those producers carry
convention C **in their own code**, not in an input. Fixing them is a source
edit, like the `z_sym` one-liner in `y_lambda_wenzl_bridge_extended.py`, not a
re-run.

The correct sequencing is therefore: fix root PRODUCERS at the source, re-run
them, then let dependency ordering carry it to the 15 derived. A sweep that
re-runs everything in place cannot do this and should not be launched again as
though it could.

## RE-BASELINED after the convention-D migration landed (2026-08-14)

PR #4928 ("Move the corpus to convention D: migrate the y_λ root, fix the run
order, and prove the branching step") landed on `main`. **It did most of this
bean's work.** Re-measuring with the same detector rather than trusting the
numbers above:

| | then | now |
|---|---|---|
| structurally convention C | 43 | **13** |
| symbolically convention C | — | 1 |
| the "29 roots" front | 29 | **~5 Python producers** |

The remaining 14, fully resolved — no unexplained entries:

| class | n | witnesses / producers |
|---|---|---|
| **Rust binary** | 8 | the whole `chi-*-at-q0-50dps-matrix-m` family (proton, neutron, deuteron, ³He, ⁴He, ⁵Li, ⁶Li, tritium) → `matrix-m-chi-q-via-gp`, `rust-chi-q-via-gp-lossless`, `chi_via_rust_lossless.py`. **Still do not regenerate**: `qou-j6il` found this layer returning C while its source read D, so the convention gate must reach the binary first. |
| **Python, actionable** | 4 | `alpha_k_jones_markov_h12.py`, `derived_chi_catalogue_build.py`, `probe_1b_li6_orthogonality.py`, `tr_m_q_hecke_seminormal.py` |
| **symbolic** | 1 | `y_lambda_macdonald_telescope.py` — half-integer power of q in a closed form, a different fix from the numeric ones |
| **orphan** | 1 | `chi-helium-4-h12-numeric` — no producer, 3 live readers, already documented in `_deprecated/README.md` |

### What this bean got right, and what it cost

The **sequencing** conclusion was right and is what #4928 acted on: fix root
producers at the source, then let dependency ordering carry the derived ones.
A sweep re-running everything in place could not have done it.

The **numbers** went stale the moment that landed, and they are the part a
later agent would have acted on. I nearly launched a 29-producer campaign for
work already done — caught only by re-running the detector before starting,
which is the corpus-grep discipline applied to one's own bean rather than to
the corpus. Worth stating plainly: **a bean that records a measurement is
stale from the moment it is written**; the measurement, not the bean, is
authoritative.

### Next step, re-scoped

Four Python producers, not twenty-nine. Each needs the source diff first
(`git diff` the producer) to see whether it carries convention C in its own
code or inherits it — the bean's own ROOT/DERIVED distinction still applies,
just to a much smaller set. The Rust family stays blocked on the binary gate.

### The 5 are ROOTS, not derived — and the first measurement said otherwise

Intersecting each producer's witness references against the 14 remaining C
witnesses first suggested 3 of 5 were derived. **That was an artifact**: the
regex matched each producer's *own output* filename, which it necessarily
mentions in order to write it. A read and a write look identical to a grep
over source text.

Reading it correctly — inputs only:

| producer | inputs | verdict |
|---|---|---|
| `alpha_k_jones_markov_h12.py` | `q-pinning-50-digit` (clean) | **ROOT** |
| `derived_chi_catalogue_build.py` | none | **ROOT** |
| `probe_1b_li6_orthogonality.py` | `y-lambda-at-q0` (clean) | **ROOT** |
| `tr_m_q_hecke_seminormal.py` | 3 clean (`atomic-tr-m-helium4`, `atomic-tr-m-mpfr-50dps`, `tr-m-jones-markov-cross-check`) | **ROOT** |
| `y_lambda_macdonald_telescope.py` | none | **ROOT** |

All five carry convention C **in their own code**, so all five need a source
edit — a re-run fixes none of them. That is this bean's original conclusion,
now holding over 5 producers instead of 29.

This is the third time in this bean's history that measuring the artifact
instead of the property produced a wrong number — `--plan` stdout, then the
read-set-vs-content-test confusion, now read-vs-write in a source grep.
Recorded rather than quietly fixed, because the pattern is the finding.

## The detector warning was actioned; the root is clean (verified 2026-08-14)

[`docs/audits/2026-08-10-convention-d-ylambda-root-and-derivation.md` §2](../docs/audits/2026-08-10-convention-d-ylambda-root-and-derivation.md)
warns: *"The same blindness should be assumed in
`scripts/convention-c-witness-audit.py` — the 'selftest 7/7' canonical
detector — until checked."* Checked: it **has** been fixed.
`scan_doc_symbolic` now carries two tests (the `SQRT_Q` spelling marker and
the defining 3+-row-nonzero-expression property) and its docstring documents
exactly that blind spot. So the 13+1 figure is not an undercount of the kind
the audit doc feared.

The cascade root is migrated. All **223** three-plus-row entries in
`y-lambda-wenzl-bridge-symbolic-witness.json` are now exactly `0` — convention
D's defining property (Schur-Weyl on a two-dimensional fibre). Verified by
reading the file, not by its absence from the detector's output.

## The 5 roots are four DIFFERENT kinds of work, not one sweep

Classifying by what each producer is *for*, before editing any of them — the
bean already records a case (`weight-factor-audit` C8) where a producer
deliberately evaluates the C formula and "fixing" it would be wrong:

| producer | kind | what closing it means |
|---|---|---|
| `alpha_k_jones_markov_h12.py` | **production weights** | recompute y_λ over 77 partitions of 12 under D; most vanish |
| `tr_m_q_hecke_seminormal.py` | **production weights** | canonical Wenzl Schur-principal weight, D form |
| `probe_1b_li6_orthogonality.py` | **premise dissolves** | the probe compares y_λ magnitudes across PSD-dominant many-row families — (3,3,3,3,2,2,2), (5,5,5,3), (4,4,4,3,3). Under D every one is exactly 0, so the orthogonality question it asks does not survive the convention change. The honest outcome is to record that, **not** to refresh numbers. |
| `y_lambda_macdonald_telescope.py` | **symbolic re-derivation** | `z = q**3/(q**2+1)` with a docstring reading `z = 1/(q^{1/2}+q^{-1/2})`; the hook-content telescope is derived in `Q = q²` with Wenzl level `X = Q^r`. Needs re-derivation under D, not a numeric edit. |
| `derived_chi_catalogue_build.py` | **unclear — check first** | its flagged entries are keyed `y_lambda_at_zero = 1`, not `y_lambda`. That may be a limit value rather than a weight, in which case the detector is over-reporting on this file by design (it over-reports rather than under-reports, per its own docstring). |

So "fix 5 root producers" is really: 2 weight recomputations, 1 negative
result to record, 1 symbolic re-derivation, and 1 detector-triage. Treating
them as one mechanical sweep would repeat this bean's founding error at a
smaller scale.

**Coordinate before editing.** PR #4928's merge message states both sides had
already run convention-C campaigns in parallel and converged on the same three
defects. Check for an in-flight sibling on these five before starting.

---

## A fourth class the complement also does not cover: library-level convention change (2026-08-16, qou-47sx)

Branch `claude/conv-d-atom-callers-sweep-wt`. This bean records that the
read-set queue (blast radius) misses producers that are C on their own. Fixing
`pyhecke/atom.py::z_mark` (qou-jm5i, b846d3767) exposes a class that **neither**
this bean's complement **nor** the blast radius covers: a producer whose numbers
move because a *library function it calls* changed convention. It reads no moved
witness, and its own witness carries no √q fingerprint, so it satisfies neither
predicate.

Measured against the 12 witness-owning callers of `atom_per_generator_volumes`
(AST taint, not grep — see qou-47sx for why the circulating "31" is wrong; the
true live figure is 20 modules, 15 producers, 12 with witnesses):

| | |
|---|---|
| in `.work/convention-d-blast-radius.json` | **2 / 12** |
| in `.work/convention-c-complement.json` | **0 / 12** |
| **in neither** | **10 / 12** |

So the union proposed in "To close" item 3 — (reads a moved witness) ∪ (fails a
content test) — is still not enough. It needs a third term: **(calls a function
whose convention moved)**, which is a source-graph property, not a witness
property. `scripts/convention-c-taint.py` already computes the witness-graph
fixpoint; the source-graph analogue does not exist yet.

### Regenerated (4 of 12), convention delta isolated by A/B

Each producer was run twice in one environment — `atom.py` at origin/main (C) and
at HEAD (D) — because a plain diff against the committed witness also picks up
python 3.13.12→3.11.15, mpmath 1.3.0→1.4.1 and a CODATA `m_p` update.

| witness | s | fields moved | headline C → D |
|---|---|---|---|
| `entanglement-orders` | 19.3 | 46 | `particles[4].orders.5.contribution` 186.403 → **3641.807** |
| `rho-k-graded-atomic-mass` | 0.8 | 55 | `table[2].err_pct` 0.04572 % → **0.17374 %** |
| `per-atom-hyperbolic-volume` | 10.4 | 7 | `Vol_p` **sign flip** −0.0404102 → **+0.0226378** |
| `multi-level-jet-sum` | 0.5 | 4 | `results[0].B_pred_MeV` −0.0236284 → **−0.0563776** |

### Ordered queue — what remains, with measured cost

**1. `catalan-binding.witness.json` — BLOCKED on a raw-float64 conflict.** 0.5 s to
run; convention delta is the largest measured anywhere (**73 fields**;
`formula_2_tower_per_block[2].err_pct` 4.4298 % → 16.8864 %). Regenerating moves the
ratchet **35 → 47** on this file: 12 new raw-f64 `B_AME` fields the producer gained
after the witness was written. Not baselineable, and not shadow-fixable —
`_is_full_precision_shadow` demands a companion with **more than f64 digits** and
`B_AME` are experimental AME values with ~7. Needs `B_AME` sourced from the AME
registry as mpf first. Cheapest real win once unblocked.

**2. `brane-tower-isospin-diagnosis.witness.json` (+2 duplicate copies under
`qou-mass/`) — BLOCKED, producer is broken.** Fails in 0.3 s at
`brane_tower_isospin_diagnosis.py:179`, `TypeError: unhashable type: 'dict'`
(`phi_vals = [float(Phi_q(v)) for v in vols]` — `atom_per_generator_volumes`
returns dicts). **Verified pre-existing**: fails identically with `atom.py` reverted
to convention C, so it is not fallout from b846d3767. Cheap to fix, cheap to run.

**3–5. The three expensive producers** — costs measured under `timeout 900`, see
qou-47sx for the final numbers. `pyhecke_h3_vs_h3a_impact_comparison.py`,
`sweeps/paper_six_term_isotope_sweep.py`, `probes/adjacent_vs_full_probe.py`
(4 witnesses) all exceed 200 s. `paper_six_term_isotope_sweep` is one of only two
callers the blast radius already knew about.

**6. `mass-table-comprehensive.witness.json` — DO NOT TOUCH.** Owner decision
pending on qou-53p1.

**Not queued (measured invariant, do not re-run):** `li2q-fbor-expansion-probe`
and `r5-full-canonical-knot-solver` call the function but produce **identical**
output under C and D. See qou-47sx for the two refutations in full — in
particular `li2q`'s regeneration flips `allPassed` true→false for a reason that is
**entirely** CODATA `m_p` drift (1.3536 ppb predicted, 1.3503 ppb observed) and
nothing to do with convention.

Gates after the four regenerations: `bash scripts/precision-gates.sh` RED on the
raw-float64 ratchet with exactly one regressed entry,
`rho-k-co-casimir-extended` 3 → 4 — the known pre-existing qou-mnrd failure, not
mine. Zero NEW dirty witnesses attributable to this work.


**Costs measured (2026-08-16, qou-47sx):** the three expensive callers all
**timeout at 900.1 s** — `pyhecke_h3_vs_h3a_impact_comparison.py`,
`sweeps/paper_six_term_isotope_sweep.py`, `probes/adjacent_vs_full_probe.py` (4
witnesses). Each needs 2× that for an isolated C-vs-D delta. All restored cleanly.
Regenerating `multi-level-jet-sum` also drained a STALE q0 anchor
(`q0-value-drift-audit`: STALE 314→313, proton-pin 801→802).
