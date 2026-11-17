---
# qou-5pgl
title: 'AUDIT: hecke_core.z flipped C->D under every importer — 8 files carry constants calibrated before it'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T13:23:16Z
updated_at: 2026-11-17T08:14:00Z
parent: qou-cdx1
---

Generalises the `alpha_high_precision` finding (`qou-l1gv`) from one file to its
class. Filed from PR #5622 (`qou-cds1`).

## The mechanism

`hecke_core` / `pyhecke.gram` were migrated to convention D (`5046347e53`,
`fcf09d2ff6`). Every file importing `z` from them therefore had its `z` change
by **+22.70 %** with **no edit to the file itself** — a file-local `git diff`
shows nothing. This is the import-cone drift class.

Confirmed instance: `alpha_high_precision.py`'s α* moved **+14.74 %** while the
producer sat at one unchanged commit, and the corpus still records the
pre-migration value (`docs/canonicalization-review.md` α* ≈ 0.305807).

**17 files import `z` from a D-migrated module.** Inheriting D is *correct* —
that is the ruling. The hazard is a **hardcoded constant calibrated before the
flip**, which now silently disagrees with the compute around it. That is the
same defect as the `6.17` (fa94034954), the `0.3948` (a24fdac8a1) and α* itself.

## Candidates — a HIGH-RECALL list, not a verdict

    3  computations/multiterm_cost_he3_l6a4_probe_algebraic.py   0.998367, 1.2999219630934102
    3  computations/multiterm_cost_deuteron_hopf_probe.py        2.224566, 1.1007832370743025, 1.636
    2  computations/alpha/alpha_high_precision.py                0.30, 0.32          <- CONFIRMED (qou-l1gv)
    1  computations/sweeps/paper_six_term_isotope_sweep.py       3.74446989
    1  computations/proton_residual_rootcause.py                 1.0
    1  computations/pn_alpha_lp_dual.py                          2.22452
    1  computations/mass_formula_6term.py                        0.0
    1  computations/hh-trefoil-corrected.py                      1.0

Triage by eye before spending a run on any of them:

- **Likely calibrated, worth checking first**: `1.2999219630934102` (17 digits —
  no physical constant is written that way by hand) and `3.74446989` (9 digits).
- **Experimental, convention-INDEPENDENT — do not chase**: `2.224566` / `2.22452`
  are the deuteron binding energy from AME, and `1.1007832370743025` is a q-like
  value. These are inputs, not calibrated outputs.
- **Trivial**: the `0.0` / `1.0` entries are almost certainly initialisers.

So the real queue is ~3 files, not 8.

## Method note — my FIRST detector reported a false clean

The first pass keyed on `expected=`, `assert abs(...) <`, and
`TARGET|REF|EXPECTED|CORPUS` names. It returned **0 of 17**, including for
`alpha_high_precision.py` — a file I had already *verified by hand* carries
`a_hi = mp.mpf('0.32')`. None of those spellings match a bare bracket bound.

Had I not had a known positive to check it against, I would have reported the
whole class clean. The rewritten detector carries a `SELFTEST` assertion on that
exact string and refuses to run if it stops matching. **Do not re-report this
list from a detector without a known-positive selftest** — this is the
thirteen-blind-spellings problem in AGENTS.md, and it caught me on the first
try here.

## Next step

Per candidate: `git log` the constant's introducing commit, check whether it
predates `5046347e53`, then run the producer and compare. Cheap for the three
real candidates. Do NOT mass-run all 17.


## Candidates CONFIRMED pre-flip (dates, 2026-08-24)

    D migration landed          5046347e53   2026-08-16
    both candidate constants    f9ad94d750   2026-08-01     (15 days earlier)

      1.2999219630934102  multiterm_cost_he3_l6a4_probe_algebraic.py
      3.74446989          sweeps/paper_six_term_isotope_sweep.py

So both were calibrated under convention C and have had the ground moved under
them. That upgrades them from "suspected" to **confirmed pre-flip**; what is
still unmeasured is how far each one now disagrees with its own compute, which
needs the producer run.

**And `f9ad94d750` is the same commit that introduced `alpha_high_precision.py`
and wrote α* ≈ 0.305807** (`qou-l1gv`). So this is not three unrelated files —
it is **one 2026-08-01 landing whose constants were all calibrated in convention
C**, with the 2026-08-16 migration moving the ground under the whole set. The
one member already measured drifted **+14.74 %**.

That sharpens the queue definition considerably: the candidate set is
*constants introduced by `f9ad94d750` in files that import `z` from a
D-migrated module*. Worth checking whether `f9ad94d750` touched other such
files beyond the three found by the literal scan — a constant can be
C-calibrated without being a bare decimal literal (it may be built from an
expression), which the literal detector cannot see. **The 8-of-17 count is a
floor, not a total.**


## 🛑 RETRACTION (same session): the "one 2026-08-01 landing" narrative is a SHALLOW-CLONE ARTIFACT

The note above says both candidate constants were "introduced by `f9ad94d750` on
2026-08-01", and infers **"one landing whose constants were all calibrated in
convention C"**. That inference is **withdrawn.**

    $ git rev-parse --is-shallow-repository    ->  true
    $ git log --reverse | head -1              ->  f9ad94d750  2026-08-01
    $ git show --name-only f9ad94d750 | wc -l  ->  28348

`f9ad94d750` is the **shallow-clone boundary** — the oldest commit this clone
has. A grafted root appears to add the entire tree, which is why it "touches"
28,348 files and why **all 17** z-importers are in it. Co-occurrence there is
evidence of nothing: everything is in it.

Likewise `git log -S<constant>` terminating at `f9ad94d750` means only *"the
constant is present at the clone boundary"* — not that it was authored there.

**What survives, and it is the part that matters:** the constants exist at
2026-08-01 and the D migration (`5046347e53`) landed 2026-08-16, so they **do**
predate the flip. The candidates are still confirmed pre-flip. What is withdrawn
is the stronger story that they form one deliberately co-calibrated set.

This is the exact hazard AGENTS.md names — *"a sha can be missing merely because
the history was never fetched"* — and I walked into it by reading a boundary as
a landing. **Do not date-reason from `git log` in this clone without checking
`--is-shallow-repository` first.**


## Triage CORRECTED — digit count is the wrong heuristic; z-dependence is the right one

I ranked the candidates by "looks calibrated" (many decimal places). Read in
context, that picked the **wrong constant twice** in the same file.

| constant | what it actually is | z-dependent? | verdict |
|---|---|---|---|
| `3.74446989` | `ALPHA_BORROMEAN_MEV`, commented `m_e · 8G` (`prop:binding-scale-catalan`) | **no** — m_e and Catalan's G carry no Markov parameter | **PRUNE** |
| `1.2999219630934102` | `M_E_SIGMA_9`, used as the additive `T4 (MeV)` term | no evidence it is | deprioritise |
| `0.998367` | `TRM_L6A4` — a **Markov trace**, used as `b_desc = RHO * m_e * TRM_L6A4` | **YES** — tr_M is defined through z | **the real candidate** |

I had flagged the 17-digit `M_E_SIGMA_9` as "no physical constant is written
that way by hand" and never looked at the 6-digit `0.998367` sitting two lines
above it. Precision of the literal says nothing about whether the *quantity*
moves with the convention.

**Corroboration for `0.998367` being a trace, and that its convention was
already doubted:** it recurs across `computations/_deprecated/` as the λ=[3]
value for proton / neutron / ³He, and
`_deprecated/probe_multi_term_tau_M_corrected.py:35` annotates the row
*"(registry; convention TBD)"*. A prior agent flagged the convention question
and it was never closed; the live file still hardcodes the number.

**Revised rule for this audit:** triage a hardcoded constant by asking *"is this
quantity defined through z?"* — traces, Markov weights, `V̂`, blend parameters
yes; masses, CODATA values, Catalan/π products no. Not by how many digits it
carries.

## Incidental: `3.74446989` does not reproduce its own stated closed form

Pruned from this audit as z-independent, but recording the measurement since I
made it:

    m_e(CODATA 0.51099895069) * 8 * Catalan  =  3.74445965994
    the file's constant                      =  3.74446989
    relative difference                      =  2.73e-6   (~2.7 ppm)

So the comment `# m_e · 8G` does not reproduce the literal to better than
~2.7 ppm. That is not a convention issue and not urgent — most likely an older
m_e vintage or a slightly different intended factor — but the constant and its
stated closed form do not currently agree. Not filed separately; noted here for
whoever touches `prop:binding-scale-catalan`.


## SAME CLASS, A SURFACE THIS BEAN DOES NOT REACH: `markov_peel`, and the DOCS (2026-09-05)

This bean covers the **code** surface — files carrying constants calibrated
before a C→D flip. There is a second flip of the same shape, and its damage is
in **durable prose**, which nothing here scans.

**The flip:** `c1a3299434` (2026-08-16) — *"markov_peel: the docstring said
convention C; the live path is D"*. Every number measured through
`markov_peel.word_to_element` **before** that date is a convention-C
measurement wearing no C label.

**A confirmed instance, corrected today.**
`docs/audits/2026-08-08-borromean-trace-convention-forcing.md` carried a
"Decisive test" table whose three figures were all pre-migration, and whose
headline sentence **inverted**:

| object | as published | re-run today |
|---|---|---|
| `(σ₀σ₁⁻¹)³` true β_Bor | 0.998366622585715967 | **0.998562163836787266** |
| `σ₀³σ₁⁻³` grouped core | 0.0685558643198896 | **0.180064539535501098** |
| `atom_braid_word_3A(1,0)` | 1.06530614425444993 | **1.145759692457300870** |
| atomic word vs D | 6.68 % | **14.74 %** |

It concluded *"The pure Borromean word reproduces **convention C** exactly"*.
It reproduces **D** exactly — `probe3qrv.py`, re-run unchanged, prints
`|interleaved beta_Bor| / D = 1.0000000000000000000`. Cross-checked against an
independent implementation (Frobenius pairing `Σ_λ y_λ χ^λ`, mpmath 60 dps,
Hoefsmit seminormal), which agrees with `tr_M_element` at **ratio 1.0**.

**Scope of the class, MEASURED — and it is a candidate list, not a defect
list.** Audit docs dated before 2026-08-16 that cite `markov_peel` or
`tr_M_atomic`: **75**, of which **34** quote a ≥10-digit decimal somewhere.
Beans last touched before that date citing them: **7**. Most of those 34
decimals will have nothing to do with `markov_peel` — the filter is
"quotes a long decimal", not "quotes a markov_peel-derived number", and
separating them needs per-document work.

**Do NOT sweep off these numbers.** Each candidate needs its own re-run to
decide, and a doc that merely *mentions* the module is not contaminated.
The cheap discriminator, worth building before any drain: the probe or
snippet each doc cites is usually still in the tree and still runnable —
re-run it and diff, which is exactly how the confirmed instance was caught.

Found while answering `qou-hu1f`. Probe:
`computations/probes/nf_vs_canonical_word_order_probe.py`.

## 2026-09-05 — the discriminator exists; the class is 15-19 % mechanically decidable, not 78 %

**Tool:** `scripts/stale-audit-discriminator.py` (808 lines; modes `--reconcile`, `--json`, `--rerun N [--dry-run]`, `--rerun-doc`). **Run from the repo root** — it resolves `REPO` via `git rev-parse`.

### Counts: my 75 / 34 / 7 reproduce EXACTLY, and are narrower than the defect

Under this bean's own wording the counts are confirmed — 75 audits and 7 beans, reproduced to the number. The wider reading is legitimately larger, and the difference is definitional on three axes:

| topic regex | audits <2026-08-16 | +≥10sf | beans by `updated_at` | by `created_at` |
|---|---|---|---|---|
| NARROW `markov_peel\|tr_M_atomic` (this bean) | **75** | 36 | **7** | 19 |
| WIDE + `word_to_element`, `tr_m_atom` | 96 | 42 | 13 | 26 |

1. **`word_to_element` is the function `c1a3299434` actually migrated** and this bean's regex omits it: 75 → 96.
2. **Bean date basis.** `updated_at` gives 7; `created_at` gives 19 — and a bean *authored* pre-migration is as exposed as any audit doc. `qou-3qrv` sits in exactly that gap.
3. **Glob depth.** Top-level `docs/audits/*.md` misses ~27 files in subdirectories.

Full scan (wide regex, rglob): **80 candidates** — 51 audits, 4 coordination, 25 beans.

### 🛑 The 78 % decidability figure is misleading and must not enter a drain plan

Raw split: DECIDABLE-NOW 63 (78 %), RUNNABLE-BUT-OFF-CONE 9, SCRIPT-GONE 4, NO-SCRIPT-CITED 4.

But **33 of 80 (41 %) quote no decimal on a Markov-adjacent line at all** — filter (c) is "quotes a long decimal", not "quotes a markov-derived number", exactly as this bean warned. Net: **tractable core = 30 docs over 26 scripts (37 %)**, and of 5 actually re-run, **2 returned a verdict**.

**Realistic: ~12-15 of 80 (15-19 %) are mechanically decidable today.** Four structural failure modes, not incidental:

- **The script prints fewer digits than the doc quotes** (2 of 3 failures) — a doc quotes 15-18 digits from a 50-dps run whose *display* was 6. This, not SCRIPT-GONE (4 of 80), is the binding constraint.
- **A cited script is not a source script.** A doc citing `mass_at_3A_proper.py:256` as a *reference* is not saying its figures came from running it.
- **`UNDECIDED-LEANS-STALE` is not a verdict** — "no figure reproduced" is equally consistent with staleness and with the wrong script being picked. **The mechanical stage flags; an agent decides.** A drain built on the raw flag will produce false corrections.
- **A doc corrected in place looks stale forever** unless decimals near a correction marker are excluded (now filtered).

**40 of 63 primaries are producers, only 3 are probes** — that is the cost driver: a producer is slow *and* dirties the tree with sibling witnesses.

### The confirmed finding: ONE stale figure, THREE carriers

`tr_M_atomic(1,0)`: published **1.0653**, today **1.14575969245730086969** (+7.552 %); implied `m_p/m_e` 1960 → **2108.59**; gap vs the exact object 6.7 % → **14.741 %**.

| carrier | state |
|---|---|
| `docs/audits/2026-08-08-borromean-trace-convention-forcing.md` | corrected 2026-09-05 (#6712) |
| `.beans/qou-3qrv` — said *"not staleness"*, now exactly inverted | corrected 2026-09-05 (#6712) |
| `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md` L54-55 | **corrected 2026-09-05 (this PR)** — the outstanding one |

Verified three independent ways, all agreeing: `probe3qrv.py` re-run; re-deriving the carrier's own formula `m_p/m_e = 2·(Vol(4₁)/ℏ_q²·|tr_M|·[3]_q!/q³ − 6)` at 60 dps, which reproduces **1959.683** from the *published* trace and so validates the reconstruction before applying it; and `atom_intra_block_is_not_a_braid_probe.py`, whose independently measured `rel 0.147409` against the Lean-proved closed form is the same 14.741 %.

The carrier-3 **conclusion survives** — "the towers are fitting experiment" holds with more room, since the formula→exact gap more than doubled. Only magnitudes moved.

**Carrier 3 was found by following carrier 2's own cross-reference, not by the tool.** That is the AGENTS.md failure mode verbatim — a wrong figure surviving elsewhere after being fixed in one place — and the mechanical scan did not produce it.

### Two operational findings

- **The Greek-letter blind spot bit on the first run.** The keyword gate was ASCII-only (`tr_M|trace|markov|hecke|braid`) and the confirmed table row is `` | `(σ₀σ₁⁻¹)³` — true β_Bor | 0.998562… | ``, matching none of them: **1 of 3** figures scored, **3 of 3** after adding Greek. Same class as the thirteen-blind-spellings problem.
- **A float64 smell in `probe3qrv.py` that is INERT — reporting the negative.** Line 26 does `hn = float(h0)`. Measured rather than assumed, same word both ways: float64 `h` → `0.998562163836787265951213135147`; exact 50-dps `h` → **byte-identical**. The coefficient enters symbolically and the substitution carries the precision. Tested for the interleaved Borromean word only; the cast is worth removing on principle, but the 18 quoted digits are **not** contaminated by it.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

8 files carrying constants CALIBRATED before `hecke_core.z` flipped C->D. A
constant fitted under C and left in place is invisible to any detector that
reads `z`, because the `z` is gone and only its consequence remains. Live,
same class as `qou-46ab`.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

---

## 2026-10-10 — verdict on the two top candidates: NEITHER is convention-calibrated. One carries a DIFFERENT live defect.

Re-audit of the C→D migration tracker (session epic `qou-am5t`). This bean named
two constants as "likely calibrated, worth checking first". Both were run down.
**Neither is a convention issue, and this bean's own §141 table already said so
for both** — so the queue here is narrower than the 8-candidate list reads.

### `3.74446989` — NOT convention-calibrated, and the bean already prunes it

`computations/sweeps/paper_six_term_isotope_sweep.py:1151`:

```python
ALPHA_BORROMEAN_MEV      = 3.74446989    # m_e · 8G  (`prop:binding-scale-catalan`)
```

`m_e · 8G` carries **no Markov parameter** — neither `m_e` (CAL-1, a CODATA
input) nor Catalan's `G` is a function of `z`, so no C→D flip can move it. This
bean's §141 table marks it **PRUNE** for exactly that reason, and that verdict
is correct. Closing it as a convention candidate.

### But the same grep confirms the §161 "Incidental", and it is SHARPER than recorded

§161 of this bean records *"`3.74446989` does not reproduce its own stated closed
form"*. Recomputed here at `mp.dps = 30` with CODATA-2022 `m_e = 0.51099895069`
and `mpmath.catalan`:

```
8G          = 7.327724753417752120436828
m_e · 8G    = 3.7444596599416103248
literal     = 3.74446989
residual    = +2.73205 ppm   (literal HIGH)
```

That reproduces the figure in `qou-3nva` and in the QA sidecar
`folio/quantum-observable-universe/mass-theory/six-term-per-derivation-weights-proof.qa.json`
(both report `3.744459660`) **to every digit they publish** — three independent
measurements, one value.

**What is new here: the two charitable readings are both excluded.** A 2.7 ppm
gap on a product of two constants invites "stale CODATA edition" or "a different
Catalan truncation". Inverting the literal against each factor in turn:

| if the other factor is right | literal implies | actual |
|---|---|---|
| `8G` correct ⇒ implied `m_e` | `0.51100034676569` | 2022 `0.51099895069`, 2018 `0.51099895000`, 2014 `0.5109989461` |
| `m_e` correct ⇒ implied `G` | `0.91596809664282` | `0.91596559417722` |

The implied `m_e` matches **no** CODATA edition — all three agree to seven digits
at `0.5109989x`, and the implied value diverges at the sixth. The implied `G`
diverges from Catalan's constant at the seventh digit and is not any published
truncation of it. So this is **not** edition drift and **not** a truncation
choice: it is a transcription/arithmetic error in a hardcoded literal, which is
the stronger claim and the one that makes it fixable rather than a convention
question.

**Not fixed here.** It is one digit in a production sweep that feeds the
six-term isotope table, it belongs to `qou-3nva`'s arc rather than to this
bean's, and per AGENTS.md §🟥 ASK THE OWNER a correction outside the two
exemptions waits. Exemption 2 (*derived from the corpus*) arguably reaches it —
the comment on the same line states the closed form the value violates, and a
QA sidecar publishes the right number — so this is a candidate for a one-line
corpus-derived fix, flagged rather than taken.

### `1.2999219630934102` — NOT convention-calibrated, and it lives in TWO files

```
computations/multiterm_cost_he3_l6a4_probe_algebraic.py:39   M_E_SIGMA_9 = mp.mpf("1.2999219630934102")
computations/multiterm_cost_he3_l6a4_probe.py:61             M_E_SIGMA_9 = mp.mpf("1.2999219630934102")
```

This bean's §141 table lists it as *"`M_E_SIGMA_9`, used as the additive `T4
(MeV)` term — no evidence it is [convention-calibrated] — **deprioritise**"*,
and nothing found here contradicts that. **One correction to the bean's own
record: it names only `..._algebraic.py`. The constant is in two files**, so a
drain keyed on the single path it lists would leave the second copy behind. Same
17-digit literal in both; not re-measured against a closed form, because no
closed form is stated for it in either file.

### Net effect on this bean

Both named "check first" candidates are **off** the convention queue. This bean
remains `todo` because the mechanism it documents is real and its remaining
candidates are unmeasured — the `alpha_high_precision` instance (`qou-l1gv`,
α* +14.74 % at one unchanged commit) is still the only *confirmed* member of the
class, and the corpus still records the pre-migration α* ≈ 0.305807.

**Why no detector can close this bean.** A constant calibrated before the flip
has no `z` left in it to evaluate, so the value-based audit
(`scripts/convention-c-value-audit.py`) is structurally blind to it — it walks
bindings and evaluates their RHS, and there is no RHS here, only a literal. The
shape audit is blinder still. This is the same class as `qou-46ab` /
`qou-u5z0`: **a recorded NUMBER, not a binding.** Closing it needs a per-constant
derivation of what it *should* be, which is hand work, one constant at a time.

Reproduce:

```sh
grep -rn "3.74446989" --include=*.py computations/
grep -rn "1.2999219630934102" --include=*.py . | grep -v _deprecated
python3 -c "from mpmath import mp,mpf,catalan; mp.dps=30; me=mpf('0.51099895069'); \
  v=me*8*catalan; print(mp.nstr(v,20), mp.nstr((mpf('3.74446989')-v)/v*10**6,6))"
```

## Implementation & Witness Progress (PR #8273)
- Branch: `qou-10v9-34oo-43v0-580o-5ovu-5pgl` (`f56a97d3d6ca66bf63033f62ab41236e038a488a`), PR: `litlfred/qou#8273`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/Probe2ShortfallFrameChiCacheClobberPslqDetectorSpellingStage2CacheGuardAndBorromeanLiteral.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/probe2_shortfall_frame_chi_cache_clobber_pslq_detector_spelling_stage2_cache_guard_and_borromean_literal_probe.py` -> `computations/probes/probe2-shortfall-frame-chi-cache-clobber-pslq-detector-spelling-stage2-cache-guard-and-borromean-literal.witness.json` (`allPassed: true`, `scriptCommitSha: e98d91d4e01bb7197ccdfc0c0a05bab481cf2839`)
