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

## TRAP — an `mpf` can be mpf-TYPED and float64-VALUED; check the SOURCE, not the type

`pyhecke.wedderburn.q_hook_product` / `q_factorial` / `wedderburn_weight` accumulate
`mp.mpf(1) * q_int(k)` over **`q_parameter.q_int`, which is float64** (`Q` is a
Python float). They return `mpf`, print 40 digits, and carry ~16. So `isinstance(x,
mpf)` is **not** evidence of precision and neither is the digit count of its repr —
resolve the value to its arithmetic source. The exact route already exists:
`qou_substrate.constants.q_int_at`, or `(Q_MP**n - Q_INV_MP**n)/HA_MP`.

Measured 2026-09-12 on `C_λ = m_e·H_q·y_λ·ρ_λ`: excising the float64 from `μ_λ`/`s_*`
removes **2.4946976e-16** and the `q_int` route still **leaves 1.0212424e-15** —
4× more than was removed. Root fix is 124 py files / 243 witnesses (`qou-oiz3`), so it
is an owner call, not a sweep. **`_Q_FRAC` from `pyhecke.gram` is NOT the exact q**:
it is the engine's rational `1.11`, 1.93e-5 from the anchor. `_Q_MP` carries 50
digits (9.91e-52 from `q_at(90)`) — **below `OUTPUT_DPS = 60`**.

## TRAP — a CACHED mpf inherits the ambient dps of whoever touched it FIRST

`hecke_core_legacy._partition_table` is built once and reused for the process.
mpmath rounds to the **ambient** `mp.dps`, which is **15** in a bare import. So every
mpf in it was 70 digits when `unified_iterative_correction` (which carries its own
`workdps`) got there first and **15** when any of the eight probes / two audits that
touch `_PARTITION_TABLE` directly did — with **no signal either way**. Measured:
`q_factorial(4)` parts company with itself at the 17th digit across the two contexts.
Generalise it: **a memo/`lru_cache`/module-level cache over mpf is a precision bug
unless the builder sets its own `workdps`.** Fixed by wrapping the body; a probe that
re-measures must call the *function*, not read the cache twice.

## TRAP — a per-block float64 bound does NOT transfer to a cancelled total

PR #7237 reported the `μ_λ` gap as "2.54432e-16, the floor of float64, so it bounds
the damage". True **per block** and false for the accumulated per-atom total: at
`k_exact = 4` the ⁸Be gated total moved **8.44e-16** (3.8× eps) and its ungated total
**6.66e-15** (30×), because that total is 1.3e-3 MeV assembled from O(1)
contributions. **Absolute** shifts were ~1e-17 MeV everywhere, including there — so
report both, and say which one the "floor" claim is about. Neither direction rescues
the old value: agreement at the floor never was evidence of correct rounding.

## TRAP — an IMPORT can reassign the global `mp.dps` inside your `workdps`

`y_lambda_su_n` calls `set_compute_dps(50)` at module scope, which ASSIGNS
`mp.dps = 50`. A lazy `from y_lambda_su_n import …` inside a
`with mp.workdps(70):` block drops the rest of that block to 50 digits, and
there is no signal. Measured 2026-10-13 (PR #7785, `aK_v2`): a_K moved at the
51st digit; contributions summed outside the block disagreed with the total
computed inside it by 1.2e-51. Import such modules at module scope, and
assert `mp.mp.dps == dps` before the final reduction. Same mechanism makes the
six-term isotope sweep run at 50 dps from its first `aK_v2` call onward.

**Root cause FIXED 2026-10-13 (branch `claude/sweep-global-dps-2026-10-13`):**
`y_lambda_su_n` now builds its constants in a local `mp.workdps(COMPUTE_DPS)`
and leaves the global alone (the import-time-dps and module-const audits both
accept `workdps` at module scope). Sweep re-run: 440 fields moved, max rel
8.78e-49; baseline arm reproduced the committed witness with 0 moved. The
GENERAL trap stands: any module-scope `set_compute_dps(N)` in a LIBRARY
module is this bug — grep for it before trusting a caller's declared dps.
Second live instance, measured 2026-11-15: `chi_free_via_lr` calls
`set_compute_dps()` (-> 70) at module scope and is imported lazily inside
`tr_m_atom_zn`, so `binding_canonical` printed its 50-digit traces at 70 via
`nstr(x, mp.mp.dps)`. **Serialize at the value's own width, never at ambient dps.**
The `qou-mass/_internal/` mirror still carries the old line until a
`sync-qou-mass-vendor.py --apply` (12 modules already drifted on main).

## TRAP — `chi_all_lambda_any` carries its OWN `dps=50`, not the ambient `mp.dps`

`chi_general_word.chi_all_lambda_any(word, n, *, dps=50, …)` computes at its
keyword default whatever `mp.mp.dps` the caller set, so a probe at 60 dps
that omits `dps=` gets 50-digit characters and only its `y_λ` at 60. Symptom
(measured 2026-09-12, bean `qou-vn6h`): an Ursell round-trip at A = 7 —
cumulants of magnitude ~37 with binomial weights up to 35 cancelling to 2.7 —
failed a `1e-50` check at ~1e-48 while the same check passed at A = 4 in
#7200, because four digits of cancellation ate the 50 that were actually
there. Pass `dps=DPS` explicitly at every call site; a green at small A is
not evidence the precision is what the header says.

## TRAP — a FINITE-SIZE threshold is an artifact in its own right, and it manufactures positives

Distinct from "thresholds that encode your prose": there the *assertion* was
wrong, here the *threshold* was. Measured on the XXZ two-magnon bound state
(`qou-6b9y`): a level was counted as "above the continuum" against a continuum
edge rebuilt from the FINITE-N one-magnon spectrum. At k = 0 that edge is exact
(the momentum pair `(a, -a)` contains `a = 0`), so the k = 0 numbers were fine —
but in ODD momentum sectors the same construction is short by
`8|cos(pi m/N)|(1 - cos(pi/N))`, which at N = 14 is **21-53x the quantity being
detected**. Eight sectors were reported bound that in fact sit BELOW the true
edge. **Whenever a detection reads "X exceeds T", measure T's own finite-size
error against the size of X** — and report the count against BOTH the finite and
the thermodynamic threshold, never only the one you built.

Two companions from the same measurement:

- **Before extrapolating in system size, compute the object's own length scale.**
  The bound state's extent is `xi = 1/log(Delta)` = **184 sites** at q0 against
  4.48 at a q = 2 control; N = 8..14 was 13x too small and NO accessible dense ED
  would have converged. The fix was not a bigger N, it was a **reduction**: the
  two-magnon block at fixed momentum is exactly real-symmetric TRIDIAGONAL in the
  relative coordinate (dim ~N/2, not ~N^2/2), and Sturm-sequence bisection gives
  its top eigenvalue in O(N). N = 4096 then costs **2.6 s** where N = 14 had been
  the ceiling. Ask for the reduction before asking for the cluster.
- **A finite-size ratio quoted as an order of magnitude is a FLOOR.** "1.5-2
  orders of magnitude below the control", read off N <= 14, is **3.23 orders**
  (1693.5) in the limit — the N = 14 reading was 24x short and still climbing.

## TRAP — mpmath `eig` fails where `eighe`/`eigsy` succeed; for a tridiagonal use Sturm

`mpmath.eig` runs a generic nonsymmetric QR and raises
`RuntimeError: qr: failed to converge after N steps` on matrices the Hermitian
routine handles without complaint — measured on a **12x12 real symmetric
tridiagonal** and a **52x52 Hermitian** momentum block, both fine under
`eighe(H, eigvals_only=True)`. A probe that builds a Hermitian matrix and calls
`eig` is one size increase away from a crash that looks like a physics wall.
For a symmetric tridiagonal go further: Sturm-sequence bisection counts
eigenvalues below `lam` in O(n) per evaluation and reaches any single eigenvalue
to full working precision, which is what makes n ~ 2000 cheap.

## TRAP — an IMPORT cone is not an EXPOSURE count; instrument the call

Measured 2026-09-19 (`qou-oiz3`, PR #7443). The float64 `q_int` has an import cone of
**1290 files / 919 committed witnesses**, and that number is correct for its question and
useless for planning a refresh. Instrumenting `q_int` with a call counter and running 100
in-cone producers: **56 of 57 that completed call it exactly SIX times, all at import time
inside `pyhecke/constants.py`** (`_bare_alpha_em`/`_bare_alpha_inv` at `:112-113`,
`FIG8_F_COUL` at `:257`). One called it 67,934 times — and that one is the only witness in
the whole exercise that moved besides the 15-call case.

So the before/after mover rate was **1 of 18 = 5.6 %**, against a plan sized off 919. The
predicate that actually identifies the exposed set is *"calls the primitive at RUNTIME"*,
which a counter decides in one run per producer and no grep can.

**State it as a floor.** 43 of the 100 were untraced (45 s timeout, and `atexit` does not
fire on a kill) — and the heavy producers are exactly the likely runtime users.

## TRAP — mpmath rounds to the CONTEXT's precision, not the operands'

The sibling of the cached-mpf trap and it bites the FIX rather than the bug. Making an
input exact does nothing if the accumulator is seeded under a low ambient `mp.dps`:
`H = mp.mpf("1.0")` at the bare-import default of **15** throws the exact factors away one
multiplication at a time. Worse, it can REGRESS — 15 dps is fewer digits than the float64
route being replaced (~15.95). Every primitive that accumulates (`q_hook_product`,
`q_factorial`, `q_dimension`, `wedderburn_weight`) needs an explicit `mp.workdps(floor+10)`
around the body and a `+x` round to the floor on return.

And **memoise the anchor**: `q_at` is an uncached `findroot`, so routing a hook loop
through it is O(n²) Newton solves. Key the cache on the dps and build inside the precision
context. Measured side-effect of getting this right: `aoperator_a5_crosscheck`
**102.3 s → 8.0 s**.

## TRAP — a sweep that cleans "stray" root witnesses by PATTERN deletes TRACKED ones

`for f in listdir(ROOT): if f.endswith(".witness.json"): remove(f)` — a reasonable-looking
cleanup for producers that write CWD-relative — silently deleted
`strong-na-stokes-kernel.witness.json`, which is **tracked on `main` and written by no
producer in the tree**. Caught by a sibling reading `git status`, not by me. Delete only
what `git ls-files --others --exclude-standard` reports.

## TRAP — `git checkout -- computations/` ate a source edit AGAIN (2026-09-19)

Already recorded below; hit again the same way, on `computations/substrate/q_parameter.py`,
while reverting an anchor witness after a verification run. The revert-by-name rule is not
enough on its own — **name the single file**, never the directory, even when the thing you
are reverting really is under `computations/`.

## BASELINE — mover rate depends on CONSTANT vs RUNTIME, and the two are opposite

Both measured 2026-09-19, same harness, before arm baselined from a revision:

| arc | what changed | mover rate |
|---|---|---|
| `qou-oiz3` | a FUNCTION (`q_int`) most producers only touch at import | **1 / 18 = 5.6 %** |
| `qou-5eg1` | a CONSTANT family (`_MP`, `_DPS_DEFAULT` 50 → 70) | **8 / 9 = 88.9 %** |

The mechanism is the whole finding: every consumer of a truncated **constant** inherits the
truncation; only a runtime **caller** inherits a function's. Do not carry one arc's rate
into the other. Arc B's moves all sit at **1e-50 … 1e-52** — digits 51+.

## STABLE — `_DPS_DEFAULT` is 70; `Q_50_DIGIT_STR` is pinned at 50

`qou_substrate/constants.py`, since 2026-09-19. It was a survivor of the old serialization
floor (`precision.py:80-82` records the 2026-05-31 move to 60/70 and did not carry it), so
the whole `_MP` family ran 20 digits below what `COMPUTE_DPS` entitles a caller to assume.
`Q_50_DIGIT_STR` is deliberately NOT on `_DPS_DEFAULT` — its name is its specification, and
leaving it at 50 is what holds the blast radius at **116** committed witnesses rather than
**525**. That second 50-dps channel (`mpf(Q_50_DIGIT_STR)`, e.g.
`pyhecke.constants.alpha_em_inv_mp`) is **still open**.

Not an anchor change, and verify it the same way if you touch it:
`q_pinning_50_digit.py` passes the dps EXPLICITLY (`q_at(mp.dps)` at `:108`), so the
anchor-defining witness is a function of `COMPUTE_DPS`, never of `_DPS_DEFAULT` —
re-running it across the bump leaves `q0Value` byte-identical.

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

## TRAP — `binding_energy` depends on whether cvxpy is INSTALLED, and no stamp records it

Measured 2026-10-13, same commit, same proton pin: `binding_energy(1, 1)` =
**−15.814194895935406** without cvxpy and **+0.5381481252873015** with it (cvxpy
1.9.3 in a private `--target` dir). `sdp_cross_channel` falls back to a scalar LP
when `import cvxpy` fails; its status is then not `optimal`, so the SDP leg is
silently **0.0**. With cvxpy the leg is ≈ +16.35 MeV. The witness `environment`
block lists python/numpy/scipy/sympy/mpmath/clarabel and **not cvxpy**, so a
committed binding number cannot be traced to its branch. This is the first
CONFIRMED environment case (the 48 % `binding_canonical` case was import-cone).
Install extras with `pip install --target <scratch>` and delete any numpy it
drags in, or you change the environment of every sibling on the container.

## TRAP — the convention-D zero-weight skip does NOT apply to `binding_energy`

Its accumulator weights by `lp_shadow_price = w/d − 1/[k]_q!` (Plancherel-based)
and its Frobenius leg by Plancherel `w_λ` — neither vanishes on ≥3-row shapes.
Exactly-zero scale occurs only on the twelve 1-dim trivial/sign blocks (and not
on (7),(8),(9),(11) and their columns: `w/d − 1/[k]!` cancels only to a
rounding residue, scale 5e-74 … 1.3e-73 MeV, measured). ≥3-row shapes
are 96–98.5 % of kernel time (k = 8, 9), so a convention-D re-weighting would
be a ~25–70× speedup (from those shares) — and a PHYSICS change, owner-gated. What did ship is a
byte-identical memo: the accumulator, the SDP leg and the Frobenius
`include_inter=True` leg send the kernel the IDENTICAL request.

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

## TRAP — a gate that is ALREADY red hides every new red in the same gate

On 2026-10-13, 10 of the 11 RED gates on `main` were already red at the shallow-clone
boundary (`7d0e674f04`, 2026-10-05), so each new defect landed as "same RED set".
Worked case: `079fd5e51b` committed `two_body_interface_bond_probe.py` AND its witness
as **0-byte files** and its message says *"precision-gates --changed: same RED set and
counts"* -- true of the gate NAMES, while it added a `Q0_PARSE_ERROR`. **Compare the
per-gate COUNTS before/after, never the RED list.** Dating trick that works on a shallow
clone: a detached worktree at the boundary commit (1.9 G here) + the 11 gate scripts run
directly with `PYTHONPATH` set to that tree's substrate -- ~5 min, says "already red then".

## TRAP — `physical_proton` is a MANIFEST KEY, not a `q0Anchor` token

`q0_anchor_manifest.json` groups stems under `physical_proton` / `ideal_muon`; the
witness field takes `proton` / `muon` / `ambiguous` / `independent` / `comparison`.
Five probes wrote the key name and were filed `Q0_ANCHOR_UNRECOGNISED` (= "nothing
checked", and blocking under `--strict`). Watch for duplicate `q0AnchorReason` keys
when adding a reason to a dict literal that already has one -- Python keeps the LAST.

## TRAP — four detector blind spots seen 2026-10-13 (none fixed; owner-gated)

- `mpf_import_time_dps_audit`: a probe that `exec()`s another probe's prelude inherits
  its `mp.dps = 25`; the AST pass cannot see it (deltalambda `rev_e_infinity_xbot_*`).
- `codata_truncation_audit`: a literal split across two ADJACENT string literals is
  read as its first piece only -> a full 70-digit pin reported "TRUNCATED"
  (`intra_ordering_value_fingerprint_audit.py:87`).
- `codata_corpus_literal_scan` counts the literal TEXT of an f-string inside `print()`
  as a CODE site (e.g. `"CODATA 1/a = 137.035999084"`); its own footer says it is
  "NOT a gate by default", yet the runner passes `--strict`.
- raw-float64 timing carve-out is a substring test on `dur`/`elapsed`: `wall_seconds`
  is read as payload. Rename at the producer to a declared key (`elapsed_seconds`);
  do NOT widen the mask (`qou-ywee`).

## TRAP — re-running in a thin container DOWNGRADES the environment stamp

The masked diff hides it (`environment` is ephemeral). This container had mpmath 1.3.0
and no clarabel; 9 re-run witnesses silently recorded the weaker env (4 of them also mpmath 1.4.1 -> 1.3.0). Before re-running
any producer: `pip install mpmath==1.4.1 clarabel==0.11.1` (match what the witness
records), then diff `environment` against `origin/main` for every touched witness. If a
witness itself records 1.3.0, re-run under 1.3.0: mpmath renders `str(mpf('inf'))` as
`+inf` in 1.3.0 and `inf` in 1.4.1, which churns unrelated fields.

## BASELINE — re-measure, do not quote

Everything here is a *method*, not an answer.

| what | command | last seen | when |
|---|---|---|---|
| `substantive` verdict over-flag rate | full producer sweep, baselined from `git show origin/main:<witness>` | 58% move / 128 completed — over-flags by ~41% | 2026-08 |
| producers that genuinely fail | the seven-requirement runner above | 2 (`su4_1111_markov_trace_probe`, `qbeta_habiro_element_probe`) | 2026-08-24 |
| missing-dual LP/SDP witnesses | `python3 computations/lp_dual_witness_validator.py` | run it — do not cite a dated baseline | — |
| `path_bridge` bootstrap defects | `python3 computations/audits/path_bridge_bootstrap_audit.py` | 6 | 2026-08-29 |
| `binding_energy(1,1)` cost | cProfile per term, proton pin, no cvxpy | **1052 s** clean: UIC 333 + Frobenius 719 (two kernel passes); **99.75 %** in `lp_accumulator_step_traces_mpfr`. After the kernel memo: ²H-with-cvxpy CPU 1267 → 628 s, ³H CPU 1654 → 1091 s. Cost ≈ 15.5 s × total chain letters (all partitions); full 16-bound-atom table ≈ 64 h → 38 h. | 2026-10-13 |
| `binding_energy(1,1)` wall cost | `hecke_core_legacy.binding_energy(1, 1)`, kernel live | **1233.9 s** (1278.5 s on `origin/main`) for the SMALLEST bound atom; A ≥ 3 strictly worse — `uic_binding_a_series_kernel_live_probe` exits 124 at 2400 s with no rows | 2026-09-12 (superseded row, kept for its method) |

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
- 2026-09-05 — beans `qou-brkp` / `qou-49vn` / `qou-16yn`: the tr_M provenance arc.
  **Six traps split into `measurement-hygiene-traps.md`** — all mine, all caught by
  measurement: comparing an input's change date to the consumer's NEW run instead of
  its previous one; reading a commit timestamp as a compute timestamp; a data
  dependency through a witness JSON being invisible to any import-cone audit; a field
  named `convention` that does not carry the convention you mean; reading a truncated
  numeric string as a value; and a stale BASELINE sitting in a source comment that
  reads *"Measured after the fix, with the binary built"*. Plus the BASELINE for the
  +48.1039 % `tr_M` move (a y_λ weight-table regeneration) and the p–n colour-weight
  localisation. **Read that file before auditing any witness-to-witness dependency.**
- 2026-09-12 (`qou-oiz3`, PR #7245): owner directive **"excise float64"**, acting on
  the finding PR #7237 / `qou-t6be` left. Three TRAPs above are new and all three cost
  me a wrong sentence first: mpf-typed-but-float64-valued, the cached-table dps, and
  the per-block bound not transferring to a cancelled total. Four more, worth carrying:
  * **The cited lines are where the previous report LOOKED, not the surface.** Two
    became **nine** sites + the cache. Two of the nine (`atom_markov_trace`,
    `atom_frobenius_norm_sq`) are on a *different leg* of `binding_energy`
    (`binding_from_frobenius_pairing`) that the original framing never reached.
  * **Run BOTH arms before attributing a stale witness.** `uic-binding-a-series` is
    3.9e-15 off; the obvious read is "my change moved it". The baseline arm gives the
    **same value as post-fix**, so it is upstream drift. Cost: a second 21-min run.
    And the arms agreeing is **not** evidence the numbers agree — `binding_energy`
    returns `float(B)`, so the comparison happened after a cast to 53 bits.
  * **A timing in PROSE defeats every field-name mask** (already in
    `measurement-hygiene-traps.md`; hit again). `binding-word-3A-reembedding` "moved"
    in 4 fields, all four wall-clock, two inside an assertion's sentence.
  * **`git checkout -- computations/` is what the gate PRINTS and it eats source
    edits.** Revert the 11 contended audit witnesses BY NAME.
- 2026-09-19 (`qou-oiz3` + `qou-5eg1`, PR #7443): landed both arcs, owner-authorised
  ("measure first AND land now" on both). Five TRAPs above are new. Gates: family run
  **twice** — once on the branch, once with all five changed files materialised at
  `origin/main` in the same tree — **identical 11-red list, 529-line logs differing in 5
  lines**, four of them explained (my file count, +21 long literals from my refreshed
  witnesses, tree-dirtiness) and one **not mine at all** (`numpy-importing files`
  1246 → 623, because a sibling removed two stale agent worktrees between the runs — a
  reminder that the tree a gate measures includes `.claude/worktrees/`). Raw-float64
  ratchet NEW 0 / REGRESSED 0 both arms. Three operational notes: **the exposure
  instrumentation is worth more than the sample** (a call counter decided in one run what
  a 919-witness cone could not); **refresh only witnesses whose BEFORE arm reproduces the
  committed value** — five of eight Arc-B movers carry unrelated upstream drift a refresh
  would sweep into the PR, and `fr-pullback-cosh-h` did not move under my change at all
  yet differs from its committed witness in 73 fields; and **a relative move of 1.000 can
  be nothing** — `hecke-log-decomposition-probe` "doubled" from 1.811e-71 to 3.622e-71,
  which is a residue at the arithmetic floor.
- 2026-09-14 (`qou-6b9y`, PR #7372): extracted the XXZ n-string band the sibling
  probe could not, `E_n(k) = -2(q^n + q^-n - 2 cos k)/[n]_q`. Gates: family run in
  full via `precision-gates.sh --changed` — **EXIT 1, 10 blocking reds, ALL
  pre-existing**; my files appear in **zero** of the 525 log lines, and the branch
  touches nothing else under `computations/`. `probe-float64-guard --strict` clean
  on all three `onedim/` files. Two new TRAPs above, both mine before they were
  caught. Three operational notes: **the gate run reverts the ephemeral-only audit
  witnesses itself** and names the substantive movers separately — revert THOSE by
  name, never `git checkout -- computations/`; **a concurrent sibling on the same
  checkout committed my uncommitted working-tree edit into its own commit**
  (`9534fba59`) while I ran the gates, which is the `git commit -- <paths>` rule
  from 2026-09-04 seen from the other side — commit before a 5-minute gate run, not
  after; and **`q_at(mp.dps)` is the right anchor call for a probe** (proton pin,
  production default) with explicit rational controls beside it.
- 2026-10-13 (#7735 triage, `claude/precision-gates-triage-2026-10-13`): full family on
  `main` `e43d2617f2` = **11 RED**; 10 were already red at the 2026-10-05 boundary
  (raw-float64 went red 2026-10-10, `4dea60d6e5`). Fixed at producers: q0 token (5 probes),
  module-scope dps (8), READ-value / timing / L_inf padding (4), registry literals (5),
  stale E_0 witnesses (3). After: **10 RED** (raw-float64 green), every other count equal or
  lower. Blocked producers worth knowing: `rho_binding_constancy_probe` and
  `saddle_offset_zero_location_probe` CRASH at HEAD; `qbeta_derived_w_overdetermined_test_probe`
  hits tr_m_word_lq Case C (do not chain, see above).
- 2026-10-13 (PR #7785): `aK_v2` float64 -> mpf. Sweep witness padding 45 -> 0;
  gates `--changed` 9 reds = pristine-main's 10 minus `float64-padding`. HEAD
  producer reproduced the committed witness first (0 moves), so all 227 moves
  (max rel 2.3e-14) are the fix. Kernel got 7x FASTER (7m32s -> 1m07s) by
  skipping y=0 (>2-row) shapes. New TRAP above (import reassigns dps).
- 2026-10-13 (PR #7788, owner-authorised sweep): refill ratchet 202→51, value-copy
  35→25, all at the producer. Four TRAPs, each one cost me something:
  * **Emitting `scriptFile` can CREATE a copy-ratchet NEW.** The copy audit drops a
    script's own witness from the carrier set, so `E_INF_7335` fell from 4 carriers
    (SHARED, unreported) to 3 (NARROW, NEW). It was a real copy, so I fixed it with a
    read. Re-measure the copy ratchet after any provenance change.
  * **A typed constant can be a STALE PIN, not just a short one.**
    `atom_braid_active_partitions.HA` was h at an earlier q0 (off by 1.1e-7). It was
    used as a 1e-12 classification tag, so the exact h flips D's verdict
    (allPassed True→False). Run origin/main's producer beside yours before you
    commit a "same value" read.
  * **A batch restore keyed on "finished but not OK" will eat good results if the
    reviewer that defines OK crashes silently** (a missing `.res` file). That cost
    6 re-runs. Make the review step fail loudly and gate the restore on it.
  * **`pkill -f <pattern>` kills the Bash call that runs it** when the pattern is in
    its own command line (exit 144). Use `pgrep -f '[p]attern'`.
  The rest is operational. gmpy2 is absent here, so `pip install --target <scratch>`
  and put it on PYTHONPATH per run. Background tasks die at 30 min unless given a
  long `timeout`. Most refill NEWs are ONE producer each: there is no
  many-witnesses group, and the mechanical groups are by fix SHAPE (manifest,
  near-miss key, save(extra)).
- 2026-10-13 (PR #7791, aK_v2 import-cone refresh, 7 witnesses): only **1 of 7** was a
  clean cone refresh (vhat, 37 fields, 5.35e-15). The two-arm run (parent of the fix
  commit vs HEAD) split the rest: `proton-mass-full-tower` carried both the 5e-15 fix
  delta AND 0.416 drift that predates the fix. `d-from-scratch` (1.43) and
  `cross-check-trM-1ppb` (an allPassed True->False flip) had fix delta 0. Held all
  three. Skipped: mass_formula_6term (li2q guard crash at both arms), six_term_model_b
  (refuses, `qou-imkb`), and term5_aK_audit (>34 min; it never calls aK_v2). **TRAP:**
  a list of "import-cone stale" witnesses is not a list of fix-attributable moves.
  Without the base arm, three would have shipped large drift under a 1e-14 label.
  **TRAP:** the pip editable installs of qou-substrate/pyhecke pointed at a sibling
  worktree (`/home/user/wt-pgt`). Set PYTHONPATH to your own `tools/*/python`. Gates:
  the red set was identical to pristine main (10).
- 2026-10-13 (PR #7792, owner-authorised c_3 provenance trace): proton c_3 typed as
  -2.0693425728 in 7 probes vs -2.06934257711516783787971951725 from every producer
  (`qbeta_ck_cache`, the canonical extraction; re-run reproduces it byte-for-byte).
  Replaced with `qbeta_utils.c3_proton_extracted(dps)`. Two TRAPs worth carrying:
  * **A typed EXTRACTED constant can be checked by the residual it is defined to zero.**
    c_3 := (Q/Q_N2 - 1)/u^3, so the N=3 residual must be ~0; with the typed copy it was
    2.666e-6 ppb, with the extraction 3.4e-42. Cheaper and more decisive than enumerating
    pins/editions, which here reproduced NOTHING (2018 ratio, 2018 m_e, Q_NEUTRON_MEV,
    muon pins, float64 q/m_e/Q, the float64 q grid -1..+8 ulps).
  * **Any extraction through 1/u^k loses ~k*2.07 digits; carry guard digits.** At 60 dps
    c_3 parted from its 70-dps value at digit ~55, and `fmt` would have published the
    rest as manufactured digits. Helper computes at d+15, rounds to d.
  Gates: `--changed` EXIT 1, 9 reds, all pre-existing (none of 8 touched files in log);
  copy ratchet NARROW 212->206. `mcp__github__create_pull_request` not offered and
  `gh pr create` 403s (GraphQL): `gh api -X POST repos/litlfred/qou/pulls --input` works.
- 2026-10-13 (rulings D/E/G/H on #7788 leftovers). **TRAP — a stale tag literal + a bare
  `except` = a vacuous PASS.** `atom_braid_active_partitions` compared letters to a typed
  `HA` 1.11e-7 off at 1e-12; every word raised `ValueError`, `except` stored `None`, and
  "0 active <= bound" passed for months against a 2026-05-25 audit recording the opposite.
  Grep `except Exception` near any threshold test before trusting its PASS. **TRAP — a
  "stale literal" may be DEAD code or in a mismatched normalisation**: `rho_f_categorical`'s
  0.388 fallback is overridden by the peel witness at import; `deuteron_delta_i_audit` is
  dead by construction and pairs D with p/n in another basis. And the "live" 0.5751 the
  ruling cited is itself stale on main (canonical deuteron 0.151968…). Measure what the
  literal actually FEEDS before swapping it. Baseline drains: write `old − measured_fixed`
  by hand, never `--rebaseline` (main carried 51 NEW unstamped / 25 NEW copies).
- 2026-10-13 (`binding_energy` profile, branch `claude/binding-energy-profile-2026-10-13`):
  99.75 % in one Rust call; memoised it byte-identically (²H, ³H, ²H+cvxpy:
  every per-step mpf `_mpf_`-equal). Gates `--changed`: my file in 0 of 609
  lines, raw-float64 NEW 0 / REGRESSED 0. Two TRAPs above (cvxpy dependence;
  conv-D skip inapplicable). The `float(_tr)` narrowing in `atom_character_raw`
  is already on bean `qou-w2vy`; the Frobenius mpf carries a 52-bit mantissa.
- 2026-10-13 (PR #7795, owner-authorised "owning deuteron tr_M"). Canonical = borromean word,
  convention D, proton pin `0.151968339204231607592665697751`; 0.575 is the GROUPED word
  (qou-hu1f ruling 2026-09-05, factor R_quark 3.784816689 reproduced by `intra_order` alone);
  0.388 is grouped + convention C. Three TRAPs, all found by building the full grid
  (ordering × word-pin × eval-pin) instead of reading witnesses:
  * **TRAP — a prefix-keyed anchor map silently retires with its pin.** `tr_m_wenzl_bridge_mpfr`
    keyed muon on `1.10997859555` (retired pin A); the live muon pin C (`…564…`) got anchor None
    and the PROTON y_λ table → muon word/χ with proton y, 1.19e-8 on the deuteron. And the
    parsed-table cache key carried no q, so a proton call answered every later muon call. The
    tell was internal: bridge-vs-peel agreed to 1e-51 at proton and 1e-8 at muon. A pin change
    moves both methods together; a method SPLIT that appears at one pin only is a straddle.
  * **TRAP — env `QOU_Q0_ANCHOR=ideal` vs file suffix `-muon`.** The chi-cache producer and
    consumer built filenames from the RAW env string; the substrate maps ideal/muon/canonical
    to one anchor. Under the documented `=ideal` run the consumer missed every `-muon` cache and
    fell back to proton χ (T/3He/4He) or the GROUPED symbolic caches (p/n/D) — with no error.
    Normalise through `qou_substrate.witness.resolve_q0_anchor`.
  * **Two agents "contradicting" each other can both be right about different FILES**:
    "the chi-cache gives 0.152" (proton witness) vs "0.575" (`-muon` witness, built 2026-08-30,
    before the ordering ruling). Resolve by naming the file, then measure.
- 2026-11-15 (q0Anchor refill slice, branch `claude/precision-anchor-refill-c-2026-11-15`). Two TRAPs:
  * **A manifest `physical_proton` entry is INERT for a producer whose payload records two pins.**
    `build()` stamps payload-first; a payload carrying both a proton and a muon `q` resolves
    `ambiguous`, and only muon/proton are stamped, so the witness stays unstamped. Check with
    `resolve_q0_anchor_payload_first(w, script, require_declared=True)` before choosing the manifest;
    for a two-pin payload stamp `ambiguous` + reason via `save(extra=...)`.
  * **`git checkout -- computations/` after `precision-gates.sh` also reverts UNCOMMITTED producer
    edits.** Commit producer changes before running the gate family, then revert.
- 2026-11-15 (q0Anchor refill slice, branch `claude/precision-anchor-refill-a-2026-11-15`):
  9/21 stamped by re-run. TRAPs: (1) a CORPUS-MEASURING audit (raw-float64 backlog,
  intra-ordering fingerprint) cannot be "stamped, re-run, numbers unchanged" -- its
  counts track the tree; fix the producer, hold the witness. (2) 3 rev_* producers
  already carried q0Anchor in source; their witnesses were simply never re-run. (3) a
  stale CONSUMER shows up as added rows (`rev-edge-relaxation-window` reads the
  k<=12 exact-maximiser witness; committed copy saw k<=10). Run the upstream with its
  committed env (`REV_EXACT_KMAX=12`) first. (4) parallel agents share
  `<scratch>/maturin.log`/`cargo.log`; name logs per agent.
