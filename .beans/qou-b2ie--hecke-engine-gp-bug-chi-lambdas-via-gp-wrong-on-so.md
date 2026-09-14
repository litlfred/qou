---
# qou-b2ie
title: 'hecke-engine GP bug: chi_lambdas_via_gp wrong on some plain words (min reproducer [(1,6),(1,7),(-1,9),(1,8),(-1,7)] at H12, chi_[12] != q); seminormal mpfr correct — fix Rust GP path + add trivial-rep regression'
status: in-progress
type: bug
created_at: 2026-07-14T01:32:09Z
updated_at: 2026-09-08T04:00:00Z
---

## Guard landed (2026-07-17, PR #3812) — silent-wrong closed; full reduction still open

Exact trivial-rep cross-check `χ_[n] = q^{writhe}` added to the Rust GP path
(`geck_pfeiffer::trivial_rep_char`, `chi_gp_trivial_rep_consistent` — also
exported to Python). `chi_lambda_via_geck_pfeiffer` / `chi_lambdas_via_geck_pfeiffer`
now **panic** on `[n]`-row disagreement instead of returning silently-wrong
characters (refuse-on-disagreement). Regression tests green (`cargo test --lib
geck_pfeiffer` 16/16); pyhecke-native `cargo check` clean. Audit:
`docs/audits/2026-07-17-gp-kernel-trivial-rep-guard.md`.

**Still open:** the necessary-condition guard closes the *silent-wrong* hazard but
is not a completeness fix. The full remedy is the Geck–Pfeiffer 2000 §3.2
cuspidal-move reduction (reach true minimal length for all classes at n≥7) OR
routing every GP consumer to the seminormal kernel. Bean stays open for that
milestone; GP consumers on longer/structured words must pre-screen with
`chi_gp_trivial_rep_consistent` until it lands.

## RESOLVED (2026-07-17) — guard + cyclic-shift completion

- Guard (merged PR #3812): exact trivial-rep check `χ_[n]=q^{writhe}` makes
  the GP path refuse (panic) instead of returning silently-wrong characters;
  correct seminormal migration target certified in Rust.
- Full fix (this branch): `reduce_basis_to_minimal_length_complete` +
  `find_length_decreasing_path` add the Geck-Pfeiffer cyclic-shift escape,
  so the GP q-MN path reaches genuinely minimal-length reps. Validated:
  GP(complete) == direct seminormal on the H12 reproducer (6 partitions) AND
  a randomized battery (n=4..8, 20 words x 2 q x every partition, 1e-6).
  19/19 Rust tests green. Audit:
  docs/audits/2026-07-17-gp-kernel-cyclic-shift-completion.md
- Deployment residual: pyhecke-native wheel rebuild (maturin, CI/dev) +
  re-run of GP-witness consumers; not runnable in sandbox.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.

## 2026-09-14 — the residual's premise is stale; and the risk set is 6, named

**"Not runnable in sandbox" is false.** `cargo 1.94.1` and `maturin 1.15.0` are
both on PATH, and `pyhecke_native 0.9.0` is installed and **post-fix**.

**The minimal reproducer PASSES.** `σ₆σ₇σ₉⁻¹σ₈σ₇⁻¹` at H₁₂, writhe +1:

    chi_gp_trivial_rep_consistent(12, word) -> True
    chi_lambdas_via_gp([(12,)], 12, word)   -> [[(2, '1')]]  = q^1 = q^writhe  ✓

**The convention was calibrated BEFORE the answer was read**, on three control
words whose correct value is known independently: writhe `+1 → 2`, `+2 → 4`,
`−1 → −2`, `0 → 0`. The Laurent exponent is in `q^{1/2}` units, so `2` is `q¹`.
Without that step `[[(2,'1')]]` against an expected `q¹` reads as WRONG and the
bug gets re-filed when it does not exist.

So the **wheel-rebuild half of the residual is done**. What is left is the
re-run half, and it is now bounded.

### The re-run half: 55 candidates → 6

[`computations/audits/gp_witness_risk_triage.py`](../computations/audits/gp_witness_risk_triage.py),
read-only. The guard (PR #3812, 2026-07-17) makes the GP path *refuse* rather
than return a wrong value, so only a **pre-guard** witness whose producer makes
a **live** GP call can carry a wrong number.

    grep-matched producers                : 30
      with a LIVE GP call (AST)           : 14
      prose/docstring only                : 16
    witnesses naming a grep-matched stem  : 55
      producer never calls GP             : 29
      live GP call, computedAt >= guard   : 20
      live GP call, pre-guard or undated  :  6   <-- RISK SET

    (undated)  he4_binding_k_fingerprint_stage1_probe -> witness-staleness-triage.witness.json
    (undated)  he4_binding_k_stage2_probe            -> audits/consumer-control-arm-audit.witness.json
    2026-06-08 derived_chi_catalogue_matrix_m        -> derived-chi-catalogue-matrix-m-mu-n-prototype.witness.json
    2026-06-30 derived_chi_catalogue_lr_scaffold     -> audits/canonical-script-input-audit.witness.json
    2026-07-06 derived_chi_catalogue_bridge_factor_deuteron -> derived-chi-catalogue-bridge-factor-omega.witness.json
    2026-07-07 derived_chi_catalogue_production_wire_demo   -> derived-chi-catalogue-production-wire-demo.witness.json

**16 of 30 grep-matched producers name GP only in a docstring or comment.** A
grep for the symbol therefore over-counts "routes a published value through GP"
by more than 2×; the AST call check is what separates them. Aliased imports
(`import chi_q_via_gp as f`) would evade that check — measured **0**, and the
script reports the count rather than assuming it stays 0.

### 🛑 A bug of mine inside the triage itself, worth more than the number

The first version reported **3**, and re-running it gave 3 again, so it looked
stable. It was not: it picked a witness's producer with

    hit = next((s for s in stems if s in blob), None)

over a **set**. A witness blob can name more than one producer, and iteration
order over a Python set is not stable across processes — so the same witness was
attributed to a prose-only producer in one run and a live one in the next,
**silently halving the risk set**. It only surfaced because the committed copy
and my scratch copy disagreed, 6 against 3.

Fixed by collecting *all* matching stems and treating the witness as at risk if
**any** of them makes a live GP call; verified deterministic over three runs. The
script also excludes itself, since it names all three GP symbols in its own
docstring.

This is a candidate row for
[`2026-08-15-detector-blindness-taxonomy.md`](../docs/audits/2026-08-15-detector-blindness-taxonomy.md)
— a *nondeterministic single-pick over an unordered collection*, which is a new
shape there: every existing row fails the same way every run. Not added, because
the row count is quoted in AGENTS.md and updating it is its own edit.

**Still open:** re-run those 6 producers and diff against the committed
witnesses. Producers write SIBLING witnesses, so that needs a whole-tree
snapshot and restore, not a single-file one.

## 2026-09-14 (later) — 3 of the 6 re-run: one clean, one MOVED 30/30 → 2/30, cause NOT established

Tree snapshotted and **restored** afterwards (`git checkout -- computations/`,
verified clean); nothing regenerated was committed, for a reason given below.

| witness | verdict on re-run |
|---|---|
| `derived-chi-catalogue-bridge-factor-omega` (2026-07-06) | **mathematically IDENTICAL** — only `durationMs` and `engineVersion` moved |
| `derived-chi-catalogue-production-wire-demo` (2026-07-07) | **MOVED**: `matches 30 → 2`, `compute_mismatches 0 → 28`, `allPassed True → False` |
| `derived_chi_catalogue_lr_scaffold` | exit 0, wrote **no** tracked witness — see the attribution defect below |

### The move is measured; its CAUSE is not, and three explanations survive

The committed witness says *"30/30 cells match direct compute"*; re-running now
gives **2/30**, against a catalogue of 342 loaded cells. It is exactly the shape
the bean predicts — a pre-guard witness recording an agreement the fixed kernel
no longer reproduces — and that is **not** sufficient to conclude it:

- **(A) the committed catalogue carries pre-fix GP numbers.** Both sides were
  computed the same wrong way in July, so they agreed; the kernel is fixed, the
  stored catalogue is not, so they now disagree.
- **(B) the environment.** This container is **downgraded** relative to the
  witness: python `3.13.12 → 3.11.15`, numpy `2.5.0 → 2.4.6`, scipy
  `1.18.0 → 1.17.1`. The producer's own guard flagged exactly this, unprompted.
- **(C) the catalogue file changed** independently since 2026-07-07.

**The discriminator is the 28 cells themselves**: a `q`-exponent shift is (A),
float noise is (B). The producer prints only the count, so getting them needs a
small change to it or a standalone comparison — **not done.**

Naming (A) because it fits is the error this repo has made before — the
`binding_canonical` 48 % move was reported as environment and was import-cone
drift. One run does not separate them.

**Scope.** `production_wire_demo` is a *demo* whose verdict field is a wire-up
readiness check, so a mismatch is not by itself a published physics number being
wrong. It **is** evidence about the catalogue it reads, and that catalogue has
other consumers.

### 🛑 This container CANNOT legitimately refresh these witnesses

The producers' own environment guard refuses the direction: *"the environment
block records LESS than the witness on disk … install it and re-run rather than
committing the weaker record; the numbers can be identical while the provenance
silently degrades."* So a re-run here is a **measurement only**. Refreshing needs
a container at python 3.13 / numpy 2.5 / scipy 1.18 or newer.

### A second attribution defect in my own triage

`derived_chi_catalogue_lr_scaffold` exited 0 and wrote **no** tracked witness,
yet the triage lists it against `audits/canonical-script-input-audit.witness.json`.
The triage matches on *"the witness blob contains the producer's stem"*, which is
**not** "the producer owns that witness" — an audit witness naming the scripts it
audited matches too. That over-counts in the same direction as the two traps its
docstring already names. The fix is to key on the producer's declared output
path, not on a substring of the payload; **not done**, and the 6 should be read
as an upper bound until it is.

### Environment note

`mpmath`, `numpy`, `sympy`, `scipy` were absent on this container and were
installed to run any of this at all — the bare-container default AGENTS.md
documents. Versions are those listed under (B), i.e. **older** than the witnesses
record.

**Still open:** the 3 un-run producers, the 28-cell discriminator, and the
output-path fix to the triage.
