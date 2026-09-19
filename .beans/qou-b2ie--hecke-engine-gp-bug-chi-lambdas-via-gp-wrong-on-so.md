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

## 2026-09-14 (settled) — the 30/30 → 2/30 move is NOT a GP bug. The braid word changed.

Chased to a cause. **It is not this bean's.**

### The decisive signature

Of 30 partitions of `n = 9`, exactly **2** still match, and they are

    lambda = (9,)                    ->  q^35    ( +70 in half-exponents)
    lambda = (1,1,1,1,1,1,1,1,1)     -> -q^-35   ( -70 in half-exponents)

the **trivial and sign representations** — the only two whose character depends
on nothing but the **writhe**. Every cell that can distinguish one braid word
from another disagrees; the only two that cannot, agree. That is not what a
kernel bug looks like; it is what comparing two *different words of equal
writhe* looks like.

### Confirmed directly — the catalogue records the word it used

    CATALOGUE braid_word : sigma_1·sigma_1·sigma_1·sigma_1·sigma_1·sigma_1·sigma_1·sigma_2·… (35 crossings)
    TODAY     braid_word : sigma_1·sigma_2·sigma_1·sigma_2·sigma_1·sigma_2·sigma_1·sigma_1·… (35 crossings)
                           >>> DIFFERENT <<<

**Grouped** then, **interleaved** now — same 35 crossings, same writhe `+35`.
Both sides pass the exact trivial-rep identity `chi_[n](T_b) = q^writhe`, and
`chi_gp_trivial_rep_consistent` returns `True`, so **neither** the stored table
nor the fresh one is wrong in the way this bean's guard detects.

### Mechanism, and it belongs to another bean

`derivation_ref` names `atom_braid_word_3A` from
`computations/mass_at_3A_proper.py` — and that is still where it lives. Four
commits have touched that file since the catalogue was built, three of them
`qou-5c64`, whose own messages are about **grouped vs interleaved** bond
ordering ("grouped reproduces ANY pre-2026-09-05 number"). So the word changed
under the catalogue; the kernel did not change under it.

**Consequence.** The committed `derived-chi-catalogue-production-wire-demo`
witness is **stale w.r.t. the word convention**, not wrong w.r.t. the GP kernel,
and its "30/30 cells match" is a true statement about a word that is no longer
the production word. Refreshing it is `qou-5c64`'s arc, not this one — and per
the note above, not from this container.

### Two wrong turns of mine on the way here, both caught before they landed

- **"The stored table is degenerate."** I read `(7,2)` and `(7,1,1)` as having
  *identical* stored characters, and `(6,3)`/`(6,2,1)` as exactly `2:1`
  proportional, and was about to report that as evidence the stored side was
  broken. Both were artifacts of reading the **first six terms** of truncated
  output. Measured over the full polynomials: **0 identical pairs and 0
  proportional pairs, in BOTH tables.** Retracted before publication.
- **"The generator moved to `_deprecated/`."** A grep for
  `def atom_braid_word_3A` matched `atom_braid_word_3A_sdp_gluon` in
  `_deprecated/atom_braid_sdp_gluon.py` — a **different function sharing the
  prefix**. The real generator never moved. Anchoring a grep to a `def` line is
  not anchoring it to a *name*.

**Still open for THIS bean:** the 3 un-run producers of the risk set, and the
output-path fix that would replace the substring attribution.

## 2026-09-14 (triage fixed) — the output-path fix is NOT implementable; a different discriminator is

I said the fix was to "key on the producer's declared output path, not on a
substring of the payload". **Measured, that cannot be done** — the corpus does
not carry the data:

| candidate key | coverage |
|---|---|
| a declared producer field (`producer`, `computation.script`, `witness.producer`) | **18 of a 400 sample — 4.5 %** |
| the witness-name → producer naming convention (`foo_bar.py` → `foo-bar.witness.json`) | **1780 of 3474 — 51.2 %** |

Neither can replace the substring match. Recording that as a negative rather
than leaving a fix in the bean that the next agent would spend a session
discovering is impossible.

**What DOES separate the false positive** is how many producer stems the witness
names. An audit or inventory witness lists every script it audited, so a
substring hit means *"it catalogued this producer"*, not *"this producer wrote
it"*. Measured on the six candidates:

    catalogue witnesses : 579, 132, 1595 producer stems named
    real GP products    : 3, 4, 4

Two orders of magnitude apart, no overlap, so the threshold is not delicate.
Set at 20; the script prints each witness's count so a reader can see where it
falls, and lists what it excluded (15 witnesses, up to **2162** stems named).

    witnesses naming a grep-matched stem  : 55
      producer never calls GP             : 40
      live GP call, post-guard            : 12
      live GP call, pre-guard or undated  :  3   <-- RISK SET

### 🛑 The fixed script returns the SAME 3 the buggy one did — that is not vindication

My original `next(...)`-over-a-set version also printed 3, with the same
membership. It got there by nondeterministically attributing three witnesses to
prose-only producers; the fixed version gets there by correctly excluding three
audit catalogues. **A right answer by an unsound route is still unsound** — the
membership would have differed on the next run, and the agreement here is
coincidence, not evidence the bug was harmless.

### Where the risk set now stands

| witness | status |
|---|---|
| `derived-chi-catalogue-bridge-factor-omega` (2026-07-06) | **re-run: mathematically IDENTICAL** — clean |
| `derived-chi-catalogue-production-wire-demo` (2026-07-07) | **settled: a grouped→interleaved WORD change, not a GP bug** (`qou-5c64`) |
| `derived-chi-catalogue-matrix-m-mu-n-prototype` (2026-06-08) | **not examined** |

So this bean's re-run half is down to **one** unexamined witness — and neither
of the two examined ones turned out to carry a pre-fix GP number.

## 2026-09-14 (residual answered) — 0 committed witnesses carry a pre-fix GP number

The last candidate, `derived-chi-catalogue-matrix-m-mu-n-prototype`, was a
**fourth** defect in my triage: `derived_chi_catalogue_matrix_m` is a stem
**prefix** of `derived_chi_catalogue_matrix_m_mu_n`, so a bare substring match
credited the shorter producer with the longer one's witness. Running the shorter
producer is what exposed it — it writes `...-matrix-m-validation`, not
`...-mu-n-prototype`. The real owner **does not mention a GP symbol at all**.
Measured hazard: 1 of 30 GP-grep stems, and that one has three superstring
siblings. Fixed with a word-boundary match.

**The substring attribution failed in four distinct ways, every one found by
RUNNING something rather than by reading the code:**

1. prose-only mentions (16 of 30 producers),
2. audit/catalogue witnesses (up to 2162 stems named),
3. nondeterministic `next(...)` over a set (silently halved the set),
4. stem-prefix collision.

**Final disposition of this bean's re-run residual:**

| candidate | disposition |
|---|---|
| `bridge-factor-omega` (2026-07-06) | re-ran **mathematically identical** |
| `production-wire-demo` (2026-07-07) | moved — but the **braid word** changed grouped→interleaved (`qou-5c64`), not the kernel |
| `matrix-m-mu-n-prototype` (2026-06-08) | misattributed; real producer never touches GP |

**So no committed witness carries a pre-fix GP number**, and the "re-run of
GP-witness consumers" half of the residual is answered. The wheel half was
answered above (maturin runs here; reproducer passes).

**What this does NOT close.** The bean's 2026-07-17 text sets a further
milestone — *"the Geck–Pfeiffer 2000 §3.2 cuspidal-move reduction … OR routing
every GP consumer to the seminormal kernel"* — and then reports the cyclic-shift
completion landing and validating against the seminormal kernel on the H₁₂
reproducer plus an n=4..8 random battery. Whether that **meets** the §3.2
milestone or merely covers the tested range is a mathematical judgement about
completeness, not something this session measured. Status left `in-progress` on
that ground alone.
