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
- 2026-09-01 — bean `t7qv`: split `measurement-hygiene-traps.md` out. Six traps,
  each one a claim I had to withdraw. **`abs(x) > tol` on a sign-proven
  quantity** caught structurally-impossible negative gaps (solver noise) and
  produced a knife-edge that did not exist — assert the sign, and treat any
  sign violation as your noise floor announcing itself. **Single-root bisection**
  on a margin with no root in range returned a meaningless `2.0009`; scan for
  brackets first. **An unverified linear solve** gave a plausible weak-transition
  operator with residual `1.3e-1` (transposed matrix); print the residual beside
  every solve. **Assertion thresholds written from prose** rather than from the
  printed value failed three probes whose measurements were fine. **A container
  reset silently moved the checkout to another branch** — same probe, different
  `pyhecke`, `0.477` became `0.679`, and I nearly filed two fabricated defects;
  the tell is `ModuleNotFoundError: mpmath`, so run `git branch --show-current`
  first. **`--depth=1` poisons `merge-base`**, which then returns empty and makes
  `git log -1 $(...)` silently report HEAD; ancestry counts read `7`/`33685`
  against a true `119`/`1343`. Also: the stored f64 `y_lambda` tables set a
  `~1e-8` agreement floor on anything routed through `load_cost` — quote seven
  digits there, not fourteen, while single-route quantities reach `1e-13`/`1e-16`.
  **Exact at both endpoints is not exact in between** — a `p-n` writhe exponent
  was settled by two independent routes agreeing on `+delta/2` (an interpolation
  from `e_pp=+1`/`e_nn=-1`, and my own operator identity), against production's
  `-delta/2`. Both were wrong by `217x`: the averaged-exponent and per-diagram
  forms agree *exactly* at the two endpoints and nowhere else, so the only two
  bonds anyone had checked could not detect it, and an interpolation anchored on
  them reproduces itself while looking like a derivation. Test at an interior
  point, and before averaging a parameter that sits in an exponent, check whether
  the physics sums or multiplies — `f(mean(x)) = mean(f(x))` only for affine `f`.
