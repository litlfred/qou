# compute-precision-auditor — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`. Confirm entries as you use them.

---

## STABLE — the gates and where they live

- `scripts/precision-gates.sh` — the whole NO-FLOAT64 family in one pass:
  two ratchets (raw-float64, float64-padding), three source-level gates
  (`mpf(<float>)`, `mp.dps` no-op, module-const), the q₀ anchor-flip and
  drift gates, plus the no-free-parameter certificate as advisory. Exits 1
  on any blocking red; does not stop at the first failure. `--changed`
  makes it cheap.
- `scripts/check-sidecars.sh` — maps changed files → applicable QA sidecar
  criteria; also runs the §7c base-ring check on un-sidecar'd library Lean.
- `scripts/precommit-precision-warn.sh` — a `PreToolUse` Bash hook that runs
  the **raw-float64 ratchet only** on commits touching a witness or a
  `computations/` script.
- `computations/lp_dual_witness_validator.py` — LP/SDP dual-field presence.
- `computations/witness_staleness_triage.py` — see the triage entry below.

## STABLE — why the hook is warn-only, and runs one gate

Three deliberate properties; do not "improve" them away. **It always exits
0** — a `PreToolUse` hook exiting non-zero stops the tool call, and a bare
container (no `mpmath`/`numpy`/`scipy`) is the *default* here, exactly when
a blocking hook would brick every commit; warn-on-commit was the owner's
choice 2026-08-25 and the push-side block was offered and **declined**.
**Ratchet only** — measured, ratchet 1.8 s vs full `precision-gates.sh`
3 m 12 s, and a hook runs before the tool call, so wiring the family in
buys avoidance, not safety. **Not a substitute for the preflight** — run
the family yourself.

## STABLE — CI will not catch this; asked and answered

The gates were already strict in `.github/workflows/witness-staleness.yml`
and three dirty witnesses reached `main` anyway (bean `qou-mnrd`). That
workflow is `workflow_dispatch:` only under the 2026-06-30 Actions-billing
directive, so on a push it never runs. Leaving it dispatch-only was
**reaffirmed by the owner 2026-08-09** with that failure cost on the table,
against both a path-filtered trigger and full push+PR triggers. Do not
re-propose enabling it without a new reason.

Beans `qou-mnrd` and `qou-82ur` reached the same finding from opposite
directions: dirty witnesses land, get drained, and are replaced by
different dirty witnesses.

## STABLE — probes are not exempt (owner directive 2026-08-18)

In any `computations/` script, probes included:

1. **Never compute in `float`.** Carry `mpmath.mpf` end to end. `float(x)`
   is permitted only inside an f-string for display, and prefer `mp.nstr`.
   `hf = float(G.h)` followed by arithmetic is a computation, not a display.
2. **Never aggregate with `statistics`/`math` over floats** — `st.mean`,
   `st.pstdev`, `math.sqrt`, `sum()` over floats all accumulate error. Use
   `mpmath` equivalents, or `Fraction` when the quantity is exact.
3. **A float64 input poisons the whole result.** If a probe reads a float64
   table (e.g. `pyhecke.trace.TR_M`), the output resolves to ~1e-16 *no
   matter what is true*. Find the exact route (symbolic `ℚ(q)`, `Fraction`,
   NF/GS basis over an exact ring) or state the question **unanswered**.
4. **Never call a float64 agreement "exact"/"identical"/"to N digits".**

The directive followed a probe that ran a Markov-trace multiplicativity test
against the float64 `TR_M` table, wrote "the product formula is exact …
interleaved − product = 7.4e-17", and filed the float64 resolution as a
scope caveat rather than as a reason the test could not answer the question.

## TRAP — witness staleness: `scriptCommitSha` drift is NOT staleness

Rebase-merge rewrites every branch commit sha, so that field is
stale-on-arrival for any producer committed on a branch, and no branch-side
refresh can fix it — the merge *is* the rewrite. It is informational
provenance only; the enforcement paths already ignore it
(`witness_dependency_drift.py` keys on `scriptHash` alone; `witness.py`
masks it in `_EPHEMERAL_META_FIELDS`). Measured cost of the old wording:
two false positives, zero true positives (bean `qou-wsha`). **Never
mass-refresh it.**

Genuine `scriptHash` drift is weaker but the same waste when the producer is
expensive: it is a **whole-file hash**, so a comment- or docstring-only edit
drifts it while the recomputed payload is byte-identical. Worked case:
`canonical-ordering-dof` drifted `87418d646ff1` → `894cafe018ee` on +21
lines that are **all comment** (bean `qou-zv2l`).

## TRAP — run the triage before spending the witness budget

`computations/witness_staleness_triage.py` normalises both producer versions
through `ast.unparse` (comments, docstrings, formatting gone). Re-measured
three times across 1564 commits of `main`: **zero** of ~700 self-stale
witnesses were safe to refresh. Source-identical is necessary, not
sufficient — two further gates bite:

- **Import-cone drift — the one that actually bites.** A producer's source
  can be byte-stable while a module it *calls* changed.
  `binding_canonical.py` is source-stable across its drift window, yet
  `tr_M_atom` moved `0.388 → 0.575` (48%) because
  `tr_m_atom_via_transfer.py` changed. A file-local `git diff` cannot see
  this — use `computations/witness_import_cone_staleness_audit.py`.
- **Bare producers.** Some never emit provenance; the `scriptHash` on disk
  was added downstream. Re-running one *deletes the field the audit keys on*
  (measured: 15 keys in, 7 and 9 out). Fix the producer first.

**Environment is a hazard, not a measured cause here.** The 48% above was
first reported as an environment effect; that was wrong — re-run with
`pyhecke_native 0.9.0`, every recorded package matched and it reproduces
byte-identically. Check the `environment` block, but this corpus has not yet
produced a confirmed environment case.

## TRAP — `fmt()` is not the universal answer (see `draining-raw-float64.md`)

Right for a **computed** value, **wrong for a READ one**: `fmt(mpf("2.2245662"))` prints
a 9-sig-fig measurement to 60 digits — emit the source's decimal **text verbatim**
(`ame_2020_binding_energies.py`). **Read `draining-raw-float64.md` first**: float→string
is not automatically a drain (`mp.dps` defaults to **15**); raising dps *manufactures*
digits against a ±1e-12 divisor; a 2⁻⁵⁴/2⁻⁵⁵ residue is the arithmetic floor.

## TRAP — producers write SIBLING witnesses

The isotope producer rewrote 21 `canonical-isotope-witness-Z*.json` files
the sampler never targeted. Anything that re-runs producers to compare must
restore the **whole** `computations/` tree afterwards, not the one file it
was looking at, or it leaves a dirty tree that reads as real work.

## TRAP — judging a producer's exit code (see `producer-health.md`)

A non-zero exit is **not** a defect and a traceback is **not** either. Four
producers exit non-zero *by design* and explain themselves on **stdout**,
which a stderr-only harness never sees; one raises a guard exception its own
cone defines. "14 crash" was corrected to **2** on 2026-08-24 once the runner
was fixed. Setting `PYTHONPATH` — which the runner needs — **masks** a whole
defect class (`import _path_bridge` before the `sys.path` bootstrap; six such
scripts were live on `main`, bean `qou-0e1t`).

Read **`producer-health.md`** in this directory before running producers in
bulk: it carries the seven-requirement runner contract, the by-design
refusals by name, and the `path_bridge` case in full.

## TRAP — mask volatile keys or you measure your own harness

`timestamp`, `elapsed_seconds`, `measured_at`, `start_time_monotonic` and
the `/invocation/*` block change every run. Also **record WHICH fields
moved**, so a mask gap is re-classifiable from the checkpoint instead of
costing another full sweep. Both errors were made before being caught, the
first one twice.

And **baseline from git** (`git show origin/main:<witness>`), never from a
tree your own sweep writes to — a contaminated baseline produced a 73%
figure of which two of three spot-checked verdicts were false.

**And a MOVED verdict is usually the harness, not the arithmetic.** Measured
over 99 producers in two sweeps (`qou-y98b`, #6454/#6493): five distinct causes
of a false mover — an unlisted field name, a timing formatted into PROSE (no
field-name mask reaches it), a CLI argument the witness itself records, a
CWD-relative write that strays the witness to the repo root, and one genuinely
stale consumer. **Zero were environment drift.** Full worked cases:
`measurement-hygiene-traps.md`.

## STABLE — long-compute logging discipline

Any background Python expected to run > 5 min (mass table beyond ⁴He,
A-operator extracts at H_9+, joint-tower SDP, PSLQ basis > 30, anything
calling `markov_peel.tr_M_atomic` with A ≥ 4) launches as:

```sh
python3 -u script.py 2>&1 | tee /tmp/<script>.log
```

`-u` defeats stdout buffering. The script emits progress every ~10 s or ~5%
of work with wall elapsed + ETA. A silent end with 0-byte output inside the
expected window means it crashed — re-launch with stricter logging, do not
silently abandon. Report bottlenecks in the end-of-task summary.

## TRAP — `tr_m_word_lq` Case C is a MISSING BRANCH, and #886 forbids auto-chaining

`tr_m_atomic_mpfr` / `tr_m_word_lq` raise

    RuntimeError: tr_m_word_lq: Case C (multiple top-1 in segment) not implemented

The recursion (`tools/hecke-engine/src/tr_m_word_lq.rs`) finds the top generator,
takes the `segment` after its innermost occurrence and branches on how many
`top-1` it contains: **none** → apply `sigma^2 = h.sigma + 1`; **exactly one** →
apply the braid relation; **more than one** → unimplemented. So it is a gap in a
reduction algorithm, not a mathematical wall, and it fires on ordinary suffixed
words — appending an interface generator to a 9-strand atom word is enough.

**Do not "fix" it by chaining to the sympy Ocneanu fallback.** PR #886 declined
that deliberately: Case C is *"a MATHEMATICAL condition where the Rust kernel is
inapplicable and the right answer may differ"*, so an automatic switch would
mask a discrepancy rather than surface one. `canonical_mass_table_extended.py`
carries that decision in a comment and narrows its own fallback to a MISSING
extension (an environment fact) rather than to Case C (a case distinction).

**The validated detour is the CHARACTER route.** Case C belongs to the
Markov-trace *recursion*; `chi_q_atomic_all_partitions_mpfr` computes
`chi_lambda(prod_i (c_i sigma_{g_i} + d_i I))` for every `lambda |- n` straight
from the `(c, d, g)` letters — no expansion, no recursion, no Case C — and
`tr_M = sum_lambda y_lambda chi^lambda`. It reaches `n = 12`. Measured
2026-09-03 against the committed `chi-<atom>-h<n>-at-q0-50dps` witnesses: worst
`|chi - committed|` 2.0e-49, worst `|tr_M - committed|` 8.0e-51. Validate against
those witnesses before trusting it — a third route to the same number is only
worth anything once it reproduces the first.

**Its generator indices are 1-BASED**; `tr_m_atomic_mpfr`'s are 0-based. Mixing
them is SILENT at `n >= 4` (it just evaluates a different word) and only panics
at small `n`, where the index falls out of range.

## TRAP — `git checkout -- computations/` (what the gate PRINTS) eats your source edits

`precision-gates.sh` says, of the regenerated contended audit witnesses (**six**
on 2026-09-04, not four — the count moves, so name the files the run prints
rather than assuming a fixed set):
*"DO NOT COMMIT THESE. Revert them: `git checkout -- computations/`"*. That
command is **path-scoped**, and essentially every probe and producer in this
repo lives under `computations/`. Run it verbatim and it discards every
uncommitted edit in the tree.

Measured 2026-09-04: an unstaged supersession banner on
`computations/qbeta/dt_d1b_arrow_count_forced_by_gabriel_probe.py` was silently
destroyed by following the instruction as printed. Untracked files survive (not
in the index), so the loss falls **only** on tracked files you edited — and
`git status` afterwards looks clean, so nothing flags it.

Revert only what the gate named: `git checkout -- computations/witness-*-audit.witness.json`.
Or commit source edits BEFORE running the gates; a clean index going in is the
cheapest protection.

## BASELINE — re-measure, do not quote

Everything here is a *method*, not an answer.

| what | command | last seen | when |
|---|---|---|---|
| `substantive` verdict over-flag rate | full producer sweep, baselined from `git show origin/main:<witness>` | 58% move / 128 completed — over-flags by ~41% | 2026-08 |
| producers that genuinely fail | the seven-requirement runner above | 2 (`su4_1111_markov_trace_probe`, `qbeta_habiro_element_probe`) | 2026-08-24 |
| missing-dual LP/SDP witnesses | `python3 computations/lp_dual_witness_validator.py` | run it — do not cite a dated baseline | — |
| `path_bridge` bootstrap defects | `python3 computations/audits/path_bridge_bootstrap_audit.py` | 6 | 2026-08-29 |

**Read the over-flag row's history before quoting anything near it.** Two
earlier figures were wrong in opposite directions and both were an agent's
own: 39% came from PER-WITNESS sampling when 119 of 268 witnesses shared one
producer, so one "did not move" fact counted ~119 times; 73% came from the
contaminated baseline above. This is the single strongest argument in this
file for the BASELINE rule.

`hadron_knot_table` **does not crash — it is very slow.** The three A=1
atoms complete, then deuterium ran a full **50 minutes** and was killed by
its own timeout (`exit 124`) with zero tracebacks. "Does not crash" is
established by the *code* (an exact chain provably never reaches a scipy
call after `da645cf0f32`/`46dcfc62a57`); the run corroborates and does not
prove it. What the run establishes on its own is the **cost**: > 50 min for
one bound atom of nineteen. Do not expect the table to finish.

---

## Session log

One line per audit: what you gated, what the gates returned, any entry above
you confirmed or corrected. Keep under ~200 lines — prune the log, never the
TRAPs.
- 2026-09-01 — bean `t7qv`: split `measurement-hygiene-traps.md` out. **Read that
  file** — six traps, each a claim I had to withdraw: `abs(x) > tol` on a sign-proven
  quantity; single-root bisection with no bracket; an unverified linear solve
  (residual `1.3e-1`); assertion thresholds written from prose; a container reset that
  silently moved the checkout to another branch; `--depth=1` poisoning `merge-base`.
  Two operational facts worth carrying inline, because they change what you compute:
  **the stored f64 `y_lambda` tables set a `~1e-8` floor on anything through
  `load_cost`** (quote seven digits there, not fourteen), and **atom bonds do not
  commute** — insertion order is worth `11 %` at `A=3` and `38-40 %` at `A=4`, so take
  the order from `atom_gen_chains` (interleaved) and quote it with any trace.
  **BEFORE OPTIMISING ANY HECKE TRACE:** convention D zeroes every partition with
  `>=3` rows at *every* strand count. `n=12` is **7 nonzero blocks of 77**, largest dim
  `297`, built in `0.04 s` — `A=4` was believed to need `H_12` and be unreachable; it
  is under a second. `A=5` comfortable (2002), `A=6` sparse (13260), `A=7` out.
  Weights `y_(n-k,k) = [n-2k+1]_q / Z`, `sum(y*dim)=1` at `q0`; exact against
  `load_cost` at `n=9`. Full derivation and cross-checks in the detail file.

- 2026-09-03 (qou-pdg9): exact leading-order coefficients by running the
  duck-typed `Fraction` seminormal pipeline over power series; three traps
  (valuation, constant allocation, `reject_float64_q` vs short decimals) —
  see `exact-series-route.md`.
- 2026-09-04 (qou-btqh): drained the braid-encoding-audit float64 ECHO CHAIN,
  6→0 (option-b 8→0 too, both baseline entries REMOVED). Three lessons worth
  keeping. (1) **Fixing the source clears pass-through echoes automatically,
  but audit-COMPUTED fields do not** — `braid_encoding_audit` reads upstream
  tr_M and also *computes* two relative-error assertions from them; once the
  upstream became strings those assertions must parse to mpf, compute in exact
  arithmetic and fmt the `computed` (add_assertion takes str; `passed` coerces
  with float()). The bean said "6 echoes can't be fixed in the audit" — true
  for the 4 pass-throughs, false for the 2 computed assertions + 1 literal.
  (2) **`option_b` fed the float64 alias `q_parameter.Q` to a lambdified
  trace, then `float()`-cast** — DOUBLE float64-poisoning; fix is
  `set_compute_dps()` + `mpf(Q_50_DIGIT_STR)` fed in, mpf out, fmt. Confirmed
  clean in import-time-dps because `set_compute_dps()` sits at module scope
  ABOVE the `Q0_MPF` constant (the pattern that gate demands). (3) **A content
  block `\approx 1.88432` (6 sig figs) → carry the VERBATIM string "1.88432",
  never fmt-pad to 60** (draining-raw-float64 READ row, confirmed against a
  real `\approx` quote). The hand-maintained `markov-trace-assembly-proton.derivation.json`
  target_value was carried verbatim from its exact-source witness
  (`atomic-tr-m-mpfr-50dps-proton`), `float(new_str)==old_f64`. Also: also
  corrected a stale option_b assertion comparing the D value against the
  retired C reference 1.63315 (failed by 0.25) → 1.88432, now passes. Family
  reds are the documented inherited-main set; the 2 NEW raw-float64 files
  (probe-toroidal-legendre-weinberg-gate, c2-diagonal-insertion) and the 1 NEW
  import-time-dps (probe_toroidal_reeb_deformation.py) are all unmodified
  pre-existing backlog, not mine.

- 2026-09-03 — SM gauge-coupling row (params 14-16). Gate family: **EXIT 1**,
  10 blocking reds, all pre-existing. Four carry-forwards:
  * **`precision-gates.sh` DIRTIES THE TREE** — it regenerates the eight
    tree-measuring audit witnesses it runs. `git checkout -- computations/`
    afterwards, every time; never commit them from a branch (bean `qou-v0t8`).
  * **A bare container needs `pip install mpmath` then
    `pip install -e tools/qou-substrate`** or the family exits **2** with
    "PREFLIGHT FAILED … This is NOT a gate failure. Nothing was examined."
    Exit 2 is neither green nor red.
  * **A producer that HARDCODES its q₀ literal is invisible to three detectors
    at once**: absent from `q0_anchor_manifest.json` (stem lookup never fires),
    witness has no `q0Anchor` (filed `Q0_ANCHOR_MISSING`, not `Q0_FLIP`), and
    `hardcoded_literal_audit` keys only on `codata_constants.py` entries, which
    q₀ is not. Case: `alpha_em_form_ladder_probe.py` carries the **retired**
    muon pin A `1.10997859555733471`; 193 py/lean sites still do.
  * **sympy→`numpy.complex128` is a float64 route no gate sees.**
    `mpf_mixed_arithmetic_audit` looks for mpmath/f64 *mixing*; a producer that
    never imports mpmath and casts exact sympy matrices to `np.complex128` for
    `np.linalg.eigvals` passes it while being f64 end to end. Case:
    `close_321_weinberg_gap.py` — witness declares `engine: sympy`,
    `compute_dps: 70`, carries **127** raw-f64 fields, `det_product:
    -0.9999999999999998`.
- 2026-09-04 — `computations/deltalambda/` q₀ re-pin tranche (qou-9ugp), 23 units.
  Gate family run in full: **EXIT 1, 11 blocking reds, ALL pre-existing** — raw-float64
  ratchet NEW 3 / REGRESSED 3 and every one has **0 commits on this branch**; only 4
  `deltalambda` lines in a 435-line log, none a file I changed. `deltalambda` anchor
  stamps `None` 125 → 105, `proton` 67 → 83, `comparison` 0 → 3, `ambiguous` 0 → 2,
  false `independent` 24 → 23. LP-dual validator: 6 missing-dual witnesses corpus-wide,
  **none** in this directory. Six carry-forwards, the first two new TRAPs:
  * **TRAP — "38 producers carry a literal" was 23.** A `grep -F` on the retired pin
    matches the HISTORICAL NOTE a previous drain leaves behind: 13 of the 38 were
    already fixed and carry the literal only in a comment saying so. Classify by AST
    (comment / docstring / live line) before sizing a tranche. Conversely the same
    grep MISSES a 17-digit transcription (`1.1099785955573347`) — the pin forks at the
    19th digit into three tails, `…4711748…` (he4, 7.3e-18 apart) vs `…4719899…`.
  * **TRAP — `wrap_legacy(...).save()` does NOT stamp `q0Anchor`.** `build()` writes it
    only when the pin is POSITIVELY declared: a `q0_anchor_manifest.json` entry, the
    env var, or **q0 evidence in the payload**. Importing `q_parameter` is not enough
    for this shape. Record `context.q0` AND list the stem, or the witness stays
    `Q0_ANCHOR_MISSING` after a correct migration.
  * **A false `independent` is the signature defect of a hardcoded pin.**
    `c_knot_tau_transfer_artifact` declared `q0Anchor: independent` citing an AST
    import-cone walk that found no `q_parameter` — true of the imports, false of the
    computation, because the pin was typed in. 5 of its 6 published quantities move
    (h, 1/h, μ₀ at 1.11e-7; E_rot, τ-ratio at 3.06e-9); only `C_knot` is genuinely
    q₀-free. An import-cone detector is blind precisely to the producer that freezes
    its pin — the two defects select for each other.
  * **Migrating the CODE does not migrate the WITNESS PROSE.** After the 2026-08-29
    drain, 7 committed witnesses here published `q0_convention: "muon-canonical"`
    beside `q0Anchor: "proton"`, and 5 carried `q0AnchorReason: "producer declared
    q0-independent (q0_anchor=False)"` beside `proton` — the arg was removed, the
    string outlived it, because a preserved top-level key is not re-derived.
  * **`fmt()` on a low-dps value MANUFACTURES digits — the mirror of float64.**
    `mu3_anchor_consistency` runs at `set_compute_dps(40)`; `fmt` renders at
    `OUTPUT_DPS=60`, so `fmt(rel_q*1e9)` invented 20 digits and diverged from truth at
    digit 33. Also `mp.nstr(Q_PROTON, 50)` of a 40-dps mpf padded ten digits into the
    anchor field. Recompute in `mp.workdps` **from the canonical STRINGS**; verify the
    rendering is stable across two working precisions (60 dps was NOT: `…666793612`
    vs `…667054978` at 80/120).
  * **Run the HEAD producer before attributing ANY move.** Two cases here.
    `deltalambda-bareven-b4-magnitude`: 25 of 31 diffs reproduce at HEAD, including a
    verdict flipping "rho3=6.0 (+58%)" → "rho3=2.466 (−35.3%)"; the pin was 4 fields at
    2.4e-10. `he4-binding-k-fingerprint-stage1`: the whole top-10 ranking, a 2.91×
    target and a 1.4% `cp_trace` all reproduce at HEAD — a **stale consumer** of
    `canonical-tr-m-via-chi-cache` whose sibling reading the same field was current.
    Pin sensitivity there is **4.02**, not the 1.2e6 a 1.4%-is-the-pin reading implies.
  * **Two agents on one checkout: use `git commit -- <paths>`, never `add` then
    `commit`.** A sibling's `git commit` swept my staged files into its own message
    while I lost the race for `.git/index.lock`. The pathspec form never leaves
    anything in the shared index. Also: a sibling's untracked-file cleanup deleted my
    `_headcopy_*.py` mid-run and the producer died at `file_content_hash()`.
  * **TRAP — check the input's change date against the consumer's PREVIOUS run,
    not its new one.** Asked why `option_e_multi_isotope_delta_lambda_probe_v3`'s
    `tr_M` jumped +48.1 % on 2026-08-23, I checked whether its chi-* inputs changed
    *at* that regeneration. They had not, and I wrote "stale inputs — REFUTED".
    Wrong endpoint: the inputs changed on **08-10**, and the consumer had last run
    on **08-09**. That test is *guaranteed* to report "unchanged" for exactly the
    drift class being looked for, because a sweep re-runs the consumer without
    touching its inputs. The window is `[consumer.computedAt_prev,
    consumer.computedAt_new]`.
  * **TRAP — a commit timestamp is not a compute timestamp.** In the same
    investigation I argued from `2c68d7f34a` "landing 19:24:58Z" that the value was
    "already computed from post-convention-D inputs". The witness *inside* that
    commit has `computedAt 2026-08-09T00:41` — 42.7 h earlier, and a day and a half
    *before* the commit I was ordering it against. Read `computedAt`, never `%ad`.
  * **TRAP — a data dependency through a witness JSON is invisible to every
    import-cone audit.** `option_e…v3` imports only stdlib, mpmath, `_path_bridge`
    and `_precision`, and takes its `tr_M` from `json.load` of a chi witness (its
    line 129 copies `tr_M_at_q0` verbatim). `witness_import_cone_staleness_audit.py`
    walks Python imports, so it sees none of this. Checking the *consumer's* imports
    for a *data* dependency answers a question nobody asked — and the real drift was
    one level up, in the chi producer's cone (`tr_m_wenzl_bridge_mpfr`).
  * **TRAP — a field named `convention` need not carry the convention you mean.**
    The chi-* witnesses' `convention` reads `colour-weighted-averaged-crossing` —
    the **p/n colour** axis, not Markov C-vs-D. I used it to "refute convention D";
    the reading was empty, not exculpatory. Resolve the Markov question from the
    y_λ table's `z` (`0.4993…` = C, `0.6126…` = D).
  * **TRAP — never read a truncated numeric string as a value.** The ≥3-row weights
    in `y-lambda-mpfr-proton-witness.json` print as `2.188243022053045885…` under a
    40-char slice and are `2.188243…e-72`. I was one commit from filing a live "the
    two y_λ tables disagree on support" defect off that slice. They agree; one
    serialises a vanishing quantity as exact `0.0`, the other keeps the residue.
  * **BASELINE (2026-09-05) — the +48.1039 % `tr_M_atom` move is a y_λ WEIGHT-TABLE
    regeneration.** `computations/probes/trm_provenance_chain_probe.py` (11/11).
    Deuteron `0.38835714…` → `0.57517224…` in `7e4d1aa6d0`; every `chi_lambda` and
    every provenance field (`scriptHash c36a8a393fcd`, `q0Anchor`, `q0Value`,
    `dps 50`) byte-identical, every `y_lambda` changed. Trigger: `fcf629cf41`
    switched `_Y_LAMBDA_DEFAULT` 33 s earlier — but the *size* is not the μ–p pin
    (11.5 ppb, three orders too small); both y_λ tables had been regenerated that
    day, moving weight mass onto the ≤2-row partitions ((3,3) ×1.071 → (6,) ×1.948,
    ≥3-row → ~1e-72). **`scriptHash`-keyed staleness structurally cannot see this.**
