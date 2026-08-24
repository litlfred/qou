# Tier-E orphan triage (2026-08-19)

Owner instruction: *"move those without provenance put into a `_deprecated/`
directory."*

The derivation-gap categorizer reported **186 tier-E orphans** — witnesses with
"no producer on disk; provenance is gone". Taken at face value that reads as 186
retirements. It is not: **13** are genuinely dead, **4** were never orphaned, and
the remaining **169** have lost their producer while still being *consumed*.

## Verdict

| Class | Count | Disposition |
|---|---:|---|
| Dead — no producer, no consumer, no doc reference | **13** | **Deprecated** (`git mv` to `computations/_deprecated/`) |
| False orphan — producer on disk, tool could not see it | **4** | **Categorizer fixed** (no witness touched) |
| Live consumers, lost producer | 147 | **Keep** — see §3, needs its own workstream |
| Prose/doc reference only | 17 | **Keep / freeze** — historical evidence (precedent below) |
| Cited by an open audit objection | 1 | **Keep / freeze** — see §2 |

`computational-only` **1711 → 1698**; `E-orphan` **186 → 169**.

Precedent followed throughout:
[`2026-06-13-orphaned-legacy-witness-triage.md`](2026-06-13-orphaned-legacy-witness-triage.md)
— same criterion (0 code consumers **and** 0 doc references), same convention
(`git mv` to `_deprecated/`, never `git rm`), same owner directive of 2026-06-13:
**deprecate now, delete later** (git history preserves everything).

## 1. Deprecated (13)

All 13 have `scriptFile: null`, no producer under any name or suffix anywhere in
the tracked tree, and **zero** references outside the audit inventory witnesses
that enumerate every witness in the repo (`derivation-chain-audit`,
`witness-producer-executes-audit`, `q0-anchor-consistency-audit`,
`witness-provenance-audit`, `raw-float64-baseline`, `q0-value-drift-audit`).

`binding-damping-rate` · `binding-delta-derivable` ·
`bring-coordinate-linking-weight-probe` · `complete-mass-sweep-2026-05-28` ·
`geom-linking-weight-h7-probe` · `habiro-a0-universal-law` ·
`habiro-binding-linking-weight` · `hoefsmit-h3-std-matrices` ·
`interface-quadratic-structure` · `linking-weight-h4-correction` ·
`sigma3-eigenvalue-h6` · `spectral-borromean-figure-eight` ·
`spectral-phase-ladder-connection`

These are the 2026-05/06-era one-off analysis witnesses — descriptions opening
`STRUCTURAL DISCOVERY:`, `AUDIT:`, `DERIVABLE:`, and one literally titled
*"Complete mass sweep across all sectors after marathon session. 16 PRs
merged."* Session artifacts, not pipeline outputs.

## 2. Kept despite scoring "dead" (1)

`binding-lp-delta-audit.witness.json` has no producer and no code consumer, but
is **named in a live devil's-advocate objection** —
[`2026-06-24-devils-advocate-wave4.md`](2026-06-24-devils-advocate-wave4.md) §
`null-dual`, one of 11 LP/SDP witnesses emitting dual-certificate keys with
`null` values. Deprecating a witness an *open* objection points at would quietly
retire the evidence rather than answer it. Frozen, matching the prior triage's
"keep as historical evidence" disposition.

## 3. The finding that matters: 147 orphans are load-bearing

The tier name invites the wrong action. Of the 186, **147 are read by live
code** — including production consumers (`aK_via_lp_dual.py`,
`low_isotopes_binding_sweep.py`, `binding_depth_stratified_lr.py`), a **content
block** (`mba-step09b-per-isotope-binding.ts`), a **Lean file**
(`BraneGeometricResummation.lean`), and **`content/values/registry.ts`** — the
witnessed-values registry.

That is a worse state than either "dead" or "healthy": a value flows into the
paper from a file **nobody can regenerate**. If one of these is ever found
wrong, there is no producer to fix and re-run. Retiring them is not an option
and neither is leaving them unlabelled. This wants its own workstream —
reconstruct the producer, or freeze the witness explicitly as a declared
constant input. Not attempted here.

## 4. Categorizer fixes (4 false orphans recovered)

Three defects in `derivation_gap_categorize.py`, all in the same direction —
**over**-reporting orphans, i.e. recommending retirement for witnesses whose
producer was on disk the whole time:

| Defect | Recovered |
|---|---|
| `on_disk` scanned only `computations/`, so producers in `docs/audits/scripts/` were invisible | `keystone-step1-gate-wrt-vs-wlambda` |
| `on_disk` globbed only `*.py`, so a `scriptFile` naming a `.lean` never matched | `deltalambda/mu3-submodularity-vacuous-deuteron` |
| `_guess_producer` appended `.py` unconditionally, so `computations/substrate/*.sage` producers sitting **next to their own witness** did not match | `substrate/bring-jacobian-isogeny-factors`, `substrate/lever1-bring-period-trB` |

The widened scan excludes `.claude/worktrees/` — those are checkouts of other
branches, and a producer existing only there is not on disk for this checkout.
(Same blind spot fixed the same day in `mpf_context_dps_audit.py`, where it had
held `precision-gates.sh` red for every agent in the container.)

## 5. The `chi-*-at-qinv-*` class — not orphans, confirming the 2026-06-13 audit

Six of the twenty-two zero-reference candidates were `chi-{atom}(-free)-h{n}-at-qinv-50dps`
witnesses. They are **live**: `bar_pairing_binding_observable.py` both writes and
reads them via the template `chi-{atom}-{kind}-h{n}-at-{q_tag}-50dps.witness.json`
with `q_tag ∈ {q0, qinv}` (see its `_free_atom_chi_via_native(..., "qinv", 50)`
call). The categorizer missed them because a **programmatically constructed**
filename cannot be found by grepping for the literal basename, and the guessed
producer name (`chi_helium_3_free_h9_at_qinv_50dps.py`) does not exist.

This independently reproduces, on current code, the 2026-06-13 audit's finding
that the `chi-*` class self-heals and must not be retired. **A witness whose name
is built by an f-string is invisible to basename analysis** — the general lesson,
and the reason the 13 above were each checked against templates as well as
literals before moving.

## Method

For each of the 186: resolve `scriptFile`; search every **tracked** file for a
producer of that basename under any of `.py`/`.sage`/`.lean`/`.sh`; grep the
tree for the witness basename **and** its `computation` id; classify references
as enumerator (a file mentioning ≥ 20 of the orphans — i.e. an inventory) versus
real; then split real references into code (`.py`/`.ts`/`.lean`/`.sh`) and prose.
Only the intersection of *no producer*, *no code reference*, *no prose reference*
was moved.

---

# Part 2 — provenance investigation of the paper-feeding orphans

Owner follow-up: *"if feeding paper that's bad. go to original commit/PR to
investigate source."*

## 0. Two corrections to Part 1 before the findings

**(a) The tier-E count was still inflated.** Part 1 fixed three
over-reporting defects in `derivation_gap_categorize.py`. There were two more,
both larger:

- The categorizer read only `scriptFile`. `witness_producer_executes_audit.py`
  already resolves producers correctly — three spellings (`scriptFile` /
  `producer` / `script`) plus `computation.script`, repo-wide, across Python,
  Rust and Lean, with a prose guard. The categorizer now **reuses** that
  resolver instead of keeping a second, worse one. Five of the twelve
  "paper-feeding orphans" declared `producer: computations/deltalambda/*_probe.py`
  and the file was on disk the whole time.
- `.rs` was missing from the producer suffixes, so
  `joint-tower-sdp-rust.witness.json` (`scriptFile: joint_tower_sdp.rs`, present
  at `tools/hecke-engine/src/bin/`) read as an orphan.

**E-orphan 186 → 137; paper-feeding 12 → 7.**

**(b) `.claude/worktrees/` has now broken a third audit tool.**
`witness_producer_executes_audit.resolve()` searches repo-wide and requires a
**unique** hit. `joint_tower_sdp.rs` returned **six** — one real, five from
stale sub-agent worktrees — so the uniqueness guard rejected the match and the
producer resolved to `None`. Same root cause as `mpf_context_dps_audit.py`
(Part 1 §4), different symptom. Fixed by excluding `.claude` there too.

The pattern is worth stating once: **a gitignored directory holding checkouts
of other branches silently corrupts every repo-wide `rglob` in the audit
layer**, and it corrupts each one differently — a phantom RED in one tool, a
false orphan in another. Any audit that globs the repo needs the exclusion.

## 1. Local git cannot answer the provenance question — the clone is shallow

`git log` on `4he-binding-full-pipeline.witness.json` shows **one** commit, a
2026-07-25 alpha-EM probe touching 27,229 files and adding 2,782 witnesses.
That is not a mass drive-by commit: `.git/shallow` exists, `git rev-parse
--is-shallow-repository` is `true`, and that commit is simply the shallow
boundary. **Nothing about the repository's history is damaged.** The real
history is intact on the remote and was read through the GitHub API.

Recorded because the intermediate reading — "the history was rewritten" — is
alarming, wrong, and easy to reach from `git log` alone in this environment.

## 2. `4he-binding-full-pipeline.witness.json` → `content/values/registry.ts`

**Origin: commit [`e52487a2`](https://github.com/litlfred/qou/commit/e52487a21f4843c60d66d39256e0b00b3655bf37), 2026-04-20**, *"Address review comments + 4He result + derivation audit"*. Its own message records what the run produced:

> 4He full-pipeline result (n=12 Ocneanu inversion, 10.6 min): … tower at
> kahler_order=0: V̂ values 1.52, 1.60, 1.65 past Φ_q pole → **blows up to 1.98M
> MeV**. Tower formula doesn't extend to 4He without a Kähler lift.

A real 10.6-minute compute (`time_sec: 930.9`) whose *result was a documented
failure* (`err_pct: 52959.6`, `precision: f64_numeric_fallback`). The producer
script was never committed.

The registry does not pin the result. It pins the run's **experimental
reference by-product**, `B_AME_MeV`:

```ts
B_4He_AME_MeV: { witnessFile: "computations/4he-binding-full-pipeline.witness.json",
                 witnessPath: "B_AME_MeV", defaultPrecision: 6, units: "MeV" }
```

### The defect: the paper and the compute layer disagree in the last digit

| source | value |
|---|---|
| `content/values/registry.ts` → the rendered paper | **28.295674** |
| `computations/ame-2020-binding-energies.witness.json` → `data.B_he4_MeV` | **28.295673** |

Difference `1e-6 MeV`, at exactly the precision the registry renders
(`defaultPrecision: 6`). Every compute consumer uses the AME source value —
`alpha_cluster_binding_scaling_probe.py`, `binding_multibody_scaling_probe.py`,
`rho_f_volume_binding_gap.py`, `atom_vhyp_closure_matrix_m.py`,
`pauli_young_spin_isospin_delta_lambda_probe.py` all read `B_he4_MeV`. **The
paper prints one last digit for ⁴He's experimental binding energy; the whole
compute layer uses another.**

This is precisely the class `ame-registry-routing-triage.witness.json` (bean
`fvxq`) exists to catch: *"UNSAFE = near but not exact → routing changes the
value … value-reconciliation decisions that must precede any route."*

**Not asserted here: which digit is correct.** Reconciling against the actual
AME2020 table is required — a back-of-envelope from mass excesses gave a
*third* value (~28.29566), which is exactly why this needs the table and not an
agent's recollection. What is established is that the corpus disagrees with
itself and the paper is on the side with no producer.

**Recommendation:** re-point `B_4He_AME_MeV` at
`ame-2020-binding-energies.witness.json` → `data.B_he4_MeV` **after** the
`fvxq` reconciliation decides the digit. An experimental constant should not be
sourced from the by-product field of an abandoned probe run under any
circumstances.

## 3. `hecke-core-symbolic-migration.witness.json` → two appendix blocks

**Origin: commit [`35f1ba7e`](https://github.com/litlfred/qou/commit/35f1ba7edfb66872da172d46c6fb483559e1859d), 2026-05-02 (PR #511)**, a commit whose stated purpose was addressing three Gemini review comments. From its message:

> Also captures previously-uncommitted artifacts: `hecke-core-symbolic-migration.witness.json`
> (**emitted by the §3·E subagent shortly after the original commit**)

A sub-agent emitted it in-session; the script was never committed. Then on
**2026-05-08 (`42934566`)** its assertions were **hand-written into the JSON**:

> Hand-curated audit witnesses (**no producer script — assertions written
> directly to JSON**) … hecke-core-symbolic-migration (0 → 4):
> `alpha_em_inv_symbolic_vs_numerical_lt_1e_13`,
> `alpha_em_inv_numerical_matches_codata_2pp_per_billion`, …

Today two appendix blocks declare it as their evidence:

- `mba-step02-gs-reduction.ts` — `computation.witness`, **`status: "verified"`**
- `mba-step02-gs-reduction.md` — *"**Canonical witness**: … Records the input
  braid, the output basis-decomposition vector … **and a hash of the rewriter
  source for reproducibility**"*
- `e-hartree-categorical-derivation.ts` — `computation.witness`, **`status: "verified"`**

A block claiming `status: verified`, against a hand-curated JSON with no
producer, whose `.md` advertises reproducibility. The witness's own `scriptFile`
field says `"(legacy — no matching producer found; provenance pending manual
triage)"`.

## 4. How this reached a green gate: the I14 provenance campaign

Both witnesses above are among the **3 witnesses** the provenance campaign
could not resolve. Commit
[`f893cc92`](https://github.com/litlfred/qou/commit/f893cc929fb6c862ab54fc9e3406fd550701cda3),
2026-05-19, *"fix(I14 provenance): batch 3 — 56 → 0, completeness 1.0"*:

> grep'd every `.py` … 53 of 56 had a real producer … **The 3 true orphans get
> an explicit "no matching producer found" scriptFile marker** so future agents
> can triage them. … The 3 orphan-marked witnesses are flagged for follow-up but
> **no longer block the closure assertion**.

| field | before | after |
|---|---:|---:|
| `prov_missing` | 56 | **0** |
| `completeness_ratio` | 0.91 | **1.00** |
| `no_missing_provenance` | FAIL | **PASS** |

The 53 recoveries were real work and the marker was honest — it says exactly
what is wrong, and this investigation found the witnesses *by* that marker. The
defect is the **gate**: `prov_missing: 0` and `completeness_ratio: 1.00` are
true of *the field being populated*, not of provenance existing. Three
witnesses with no provenance were counted as complete, and the assertion that
was supposed to notice went green. Two of the three now back paper values.

This is the same shape as the trivial-`True` and axiomatization anti-patterns
AGENTS.md already forbids: a check satisfied by a statement *about* the gap
rather than by closing it. **A provenance field whose value is prose should
count as missing, not present.**

## 5. Remaining paper-feeding orphans (7)

| witness | consumer | what it feeds |
|---|---|---|
| `4he-binding-full-pipeline` | `content/values/registry.ts` | **a rendered numeric value** (§2) |
| `hecke-core-symbolic-migration` | 2 appendix blocks, `status: verified` | canonical-witness claim (§3) |
| `canonical-mass-table-242ppb` | `mba-step09b-per-isotope-binding.ts` | `computation.witness`, `status: "experimental"` (honestly labelled) |
| `rho-k-markov-multiplicativity` | `rho-k-graded-expansion.{ts,md}` | backs a **"PROVED via Markov multiplicativity"** status claim (3.2e-14) |
| `wlambda-covariance-epic-A2-fractional-moment-family` | `YoungDiagramKernelPincer.lean` | docstring evidence for an FMP target |
| `whitehead-volume-identification` | surreals audit block | prose evidence |
| `one-loop-ambiguity-group` | `content/bib-qa-verifications.json` | needs re-check; the grep context did not confirm a functional use |

## 6. Recommended next actions

1. **Make a prose provenance field count as missing** in
   `witness_provenance_audit.py`; re-measure `completeness_ratio` honestly.
2. **Re-point `B_4He_AME_MeV`** at the AME source, gated on the `fvxq`
   last-digit reconciliation (§2).
3. **Downgrade `status: "verified"`** on the two `mba-step02` blocks, or
   reconstruct the producer (§3).
4. **Re-check the `rho-k-markov-multiplicativity` "PROVED" claim** — a proof
   status resting on an unregenerable witness.
5. The remaining 130 non-paper-feeding orphans stay as Part 1 left them.

---

# Part 3 — closing the gate that let it through

Recommendation 1 of Part 2, applied.

## The mechanism, exactly

`computations/audits/witness_provenance_audit.py::classify` scored a witness
by emptiness:

```python
missing = [f for f in REQUIRED_FIELDS if not body.get(f)]
```

A prose marker is a **non-empty string**, so
`"(legacy — no matching producer found; provenance pending manual triage)"`
counted as *present*. The I14 campaign reached `completeness_ratio: 1.00` in
part by **writing that marker**, and the check that should have noticed
returned `PROV_OK`. The marker is honest; counting it as provenance was the
defect.

`_has_provenance` now rejects a `scriptFile` whose value is an explanation
rather than a path, using the same predicate shape as
`witness_producer_executes_audit.is_prose` — kept in sync deliberately, since
two different answers to "is this a real producer reference?" is how the wrong
one gets acted on.

## Measured

| | before | after |
|---|---:|---:|
| `PROV_OK` | 2291 | **2284** |
| `PROV_EXEMPT_NO_READER` | 215 | **217** |
| `PROV_MISSING` | 49 | **54** |
| `completeness_ratio` | 0.981 | **0.979** |

Seven witnesses carried a prose `scriptFile`. Five surface as `PROV_MISSING` —
including **both** paper-facing ones (`4he-binding-full-pipeline`,
`hecke-core-symbolic-migration`) and three not previously known to this
investigation: `codata-2022-validation-masses`,
`rho-k-leading-order-verification`, `chi-helium-4-h12-numeric`. The other two
(`tau-hat-n-proton-level-1-empty`, `wall-violations`) fall to
`PROV_EXEMPT_NO_READER`, which is correct — they are the frozen-as-evidence
class from the 2026-06-13 triage and nothing reads them.

## An over-fire caught before shipping

The first version applied the prose predicate to **all** of
`REQUIRED_FIELDS = (engine, scriptFile, commitSha)`. Measured before
committing: it flagged **50** values, of which **49 were `engine`** —
`"sympy + pyhecke_native"`, `"mpmath (witness-fed; no new tr_M compute)"`,
`"pyhecke_native seminormal-mpfr 50dps (chi_lambda_all_partitions_mpfr) …"`.
Those are informative descriptions, not evasions: `engine` is free text by
design, and the predicate was written for a **path**-valued field.

Shipping it would have manufactured 49 false `PROV_MISSING` and moved
`completeness_ratio` on noise — a gate made red by a bad check, which is the
mirror of the failure this whole part is about. The check is now restricted to
`PATH_VALUED_FIELDS = ("scriptFile",)`. `commitSha` wants a sha-shaped
validator; that is a separate change and is not attempted here.

## Not done, deliberately

The five surfaced witnesses are **not** added to
`provenance-acknowledged-floor.json`. The floor is the right mechanism for a
witness that genuinely cannot carry a producer — its discipline requires a
reason from a completed investigation, and Part 2 supplies one for two of them
— but floor-ing them turns the gate green again, and for
`hecke-core-symbolic-migration` that would bless the `status: "verified"`
claim on two appendix blocks rather than fix it. Which of the five belong on
the floor, and which need their block status corrected instead, is an owner
decision; recommendations 2–4 of Part 2 stand.

---

# Part 4 — recommendation 4 investigated: no defect, and a fourth glob bug

## `rho-k-markov-multiplicativity` — the flag was mine, not the corpus's

Part 2 listed this as backing a **"PROVED via Markov multiplicativity"** status
claim from an unregenerable witness. **That was wrong.** The witness is live at
`computations/probes/rho-k-markov-multiplicativity.witness.json`, its producer
is live at `computations/probes/rho_k_markov_multiplicativity_probe.py`, and it
carries two passing assertions (`wenzl_branching_identity_machine_precision`,
`branching_verified_all_lambda_6`).

The content is also accurate about what it rests on. `rho-k-graded-expansion.md`
says the witness *"numerically verifies the [Wenzl 1988] branching identity"* —
the **proof** is Wenzl 1988 Theorem 5, cited as such; the witness is
corroboration, not the proof. That is the correct shape and no downgrade is
warranted.

## Why it looked producerless: `_deprecated/` breaks the same uniqueness test

`witness_producer_executes_audit.resolve()` requires a **unique** hit. The
producer exists at **both** `computations/probes/` and
`computations/_deprecated/` — a live script and its retired twin — so the
uniqueness test rejected the match and the producer resolved to `None`.

A `_deprecated/` copy is **by definition not the producer**. Every other scan in
this repo already skips that directory (`_scan` in the categorizer,
`scan` in the provenance audit); this resolver did not. Fixed in both the
narrow and wide search paths. **E-orphan 137 → 134.**

## The pattern, now four instances

| tool | ambiguity source | symptom |
|---|---|---|
| `mpf_context_dps_audit` | `.claude/worktrees/` | 28 phantom no-ops; `precision-gates.sh` RED for every agent in the container |
| `derivation_gap_categorize` | `computations/`-only + `*.py`-only | 4 false orphans, disposition = *retire* |
| `witness_producer_executes_audit` | `.claude/worktrees/` | `joint_tower_sdp.rs` → 6 hits → `None` |
| `witness_producer_executes_audit` | `_deprecated/` | live producer with a retired twin → `None` |

Two directories that must never appear in an audit's repo-wide `rglob`:
**`.claude/`** (checkouts of other branches) and **`_deprecated/`** (retired
copies). Both are invisible in review — the glob looks correct — and both fail
*toward* the dangerous verdict: a phantom red that trains agents to skip the
gate, or a false orphan whose recommended disposition is deletion.

## Net effect of Parts 1–4 on the tier-E count

| stage | E-orphan |
|---|---:|
| as first reported | 186 |
| − 13 genuinely dead (deprecated) | 173 |
| − 4 (`docs/audits/scripts/`, `.lean`, 2 × `.sage`) | 169 |
| − 31 (`producer`/`script` keys, `.rs`, `.claude` in `resolve`) | 138 → 137 |
| − 3 (`_deprecated` twins) | **134** |

**28% of the original tier was tool error, 7% was genuinely dead, and the
remaining 65% is the load-bearing population Part 1 §3 describes.**
