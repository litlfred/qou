---
# qou-lt8x
title: 'The convention-D blast radius does NOT cover 31 of the 43 structurally-C witnesses: read-set != write-set'
status: in-progress
type: task
priority: normal
created_at: 2026-08-11T01:13:43Z
updated_at: 2026-08-11T01:14:12Z
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
| `probe_1b_li6_orthogonality.py` | **recompute** ⚠ *(revised — see the 2026-08-15 correction below; this row originally read "premise dissolves")* | Only the PSD-dominant side is 3+ row and vanishes under D; the trace-dominant side is 1- and 2-row and stays nonzero. The question survives and the answer sharpens to an exact zero. Re-run and record it. |
| `y_lambda_macdonald_telescope.py` | **symbolic re-derivation** | `z = q**3/(q**2+1)` with a docstring reading `z = 1/(q^{1/2}+q^{-1/2})`; the hook-content telescope is derived in `Q = q²` with Wenzl level `X = Q^r`. Needs re-derivation under D, not a numeric edit. |
| `derived_chi_catalogue_build.py` | **unclear — check first** | its flagged entries are keyed `y_lambda_at_zero = 1`, not `y_lambda`. That may be a limit value rather than a weight, in which case the detector is over-reporting on this file by design (it over-reports rather than under-reports, per its own docstring). |

So "fix 5 root producers" is really: 2 weight recomputations, 1 negative
result to record, 1 symbolic re-derivation, and 1 detector-triage. Treating
them as one mechanical sweep would repeat this bean's founding error at a
smaller scale.

**Coordinate before editing.** PR #4928's merge message states both sides had
already run convention-C campaigns in parallel and converged on the same three
defects. Check for an in-flight sibling on these five before starting.

## CORRECTION (2026-08-15): probe_1b's premise does NOT dissolve — it sharpens

The classification above put `probe_1b_li6_orthogonality` under "premise
dissolves", on the reasoning that it compares `y_λ` magnitudes across
many-row PSD-dominant families which are all exactly 0 under convention D. I
wrote that the orthogonality question "does not survive the convention
change" and that the honest outcome was to record a negative.

Checking the committed witness instead of reasoning about it:

    (17, 1)        rows=2   7.080e-06
    (16, 2)        rows=2   6.924e-06
    (15, 3)        rows=2   6.206e-06
    (18,)          rows=1   5.861e-06
    ...
    (15, 2, 1)     rows=3   2.045e-06

**Both** families are present. The trace-dominant side is 1- and 2-row and
stays nonzero under D; only the PSD-dominant side is 3+ row and vanishes.

So the probe's question survives and its answer gets *sharper*: at A=6 the
PSD-dominant family contributes **exactly zero** to the trace under D, where
convention C gave 0.030% / 0.0002%. Orthogonality becomes exact rather than
approximate — a stronger result, not a dissolved one.

Revised disposition for this producer: **re-run and record the exact-zero
result**, not "record a negative". It moves from the dissolve bucket to the
recompute bucket, making that split 3 recompute / 0 dissolve / 1 symbolic
re-derivation / 1 detector triage.

**Second time in two beans today** that I asserted a consequence from a grep
without executing the thing (the other: `qou-a0j7`, where I gave a 6.88e-4
figure for a path that raises ModuleNotFoundError on every input). Both
corrections were one command away. The pattern is asserting downstream
consequences from a static read — the same error class this whole arc is
about, applied to my own reporting rather than to the code.

## The convention-C count OVERSTATES the front (2026-08-15)

Four of the five "roots" examined closely. **Three are false positives**, each
by a different mechanism, and none is a detector bug:

| producer | flag cause | verdict |
|---|---|---|
| `probe_1b_li6_orthogonality` | committed witness predates the migration; producer could not run (`KeyError: '18'`, cache stops at n=12) | **GENUINE** — migrated, 13 → 12 |
| `alpha_k_jones_markov_h12` | 3+row weights are **solver residue** (1e-18…9e-18) from a 77×77 linear solve; `z = q₀³/(q₀²+1)` is already the D parameter | false positive — snapped to exact 0, 12 → 11 |
| `derived_chi_catalogue` | `y_lambda_at_zero="1"` is a **placeholder**, per the producer's own comment | false positive — producer fixed; witness pending an explicit re-derivation (append-only guard) |
| `y_lambda_macdonald_telescope` | 14 symbolic expressions on 3+row blocks that **simplify to identically 0** — verified with sympy, 14/14 | false positive — **nothing to fix**; the producer is correct |
| `tr_m_q_hecke_seminormal` | not yet determined | in progress |

### Why none of these is a detector defect

Each flag is the correct output of a test that cannot see the distinguishing
fact:

- **Solver residue vs symbolic zero.** `DEAD_TOL = 1e-30` is set, per its own
  comment, for a float pipeline "delivering 1e-300" — underflow. A linear
  solve delivers machine-epsilon residue at 1e-18, twelve orders the wrong
  side. Same detector, different numerical route.
- **Placeholder vs weight.** A literal `"1"` in a weight field is
  indistinguishable from a computed weight. The defect is writing an unknown
  as a plausible value.
- **Syntactic vs semantic zero.** `scan_doc_symbolic`'s own docstring says it
  "screens syntactically and over-reports rather than under-reports" because
  deciding whether an arbitrary q-expression vanishes needs a CAS. It is
  behaving exactly as documented.

### Consequence for anyone reading the count

**Do not treat the remaining structural count as a count of real convention-C
carriers.** It is an upper bound. On the sample examined it overstated by 3×
(4 flags, 1 genuine). Before doing migration work on any remaining entry,
settle which of the four mechanisms it is — the cheap tests are: simplify the
expression with sympy; compare the magnitude against the smallest live weight
(y_(12) ≈ 3.97e-3); and read the producer for placeholder literals.

The corollary matters more than the count: **a witness flagged convention C is
not evidence that its producer computes convention C.** Three of these four
producers were already fully convention D.
