---
# qou-47sx
title: 'Convention-D atom.py caller sweep: measure the true blast radius, regenerate only what is cheap and verifiable'
status: in-progress
pr: 8190
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T12:34:42Z
updated_at: 2026-11-16T20:28:40Z
parent: qou-9nnz
---

## The caller count: "31" is refuted — the true live figure is 20 modules, 15 of them producers

`grep -rln atom_per_generator_volumes --include=*.py` returns 79 files and the
commit message for b846d3767 says "31 callers". Both count **docstring and
comment mentions**. Measured with an AST taint pass (function-level: a function
is tainted iff it calls a name resolving to the seed; modules propagate through
`from <mod> import <tainted_fn>`):

| set | count |
|---|---|
| definition sites | 1 live (`tools/pyhecke/python/pyhecke/atom.py`) |
| **live modules reaching the symbol** | **20** |
| — of which library/dispatch | 2 (`atom.py`, `gram.py`) |
| — of which tests | 2 (`test_gram_values.py`, `test_native.py`) |
| — of which stray root scratch file | 1 (`test_pb.py`, hardcodes `/Users/litlfred/...`) |
| — **computation modules** | **15** |
| — of those, **owning a committed witness** | **12** (17 witness files, 5 are duplicate copies under `qou-mass/`) |
| `_deprecated/` modules | 30 (excluded by policy) |

Modules the grep hits but that never call it (docstring-only): `canonical_tower.py`,
`wedderburn_pair_volumes.py`, `mass_at_3A_proper.py`, `canonical_brane_tower_decomposition.py`,
`vhat_per_crossing_chain.py`, `probes/brane_tower_{full_channel_trace_audit,two_avenues_probe}.py`.
Two more **import but never call** it — `pn_alpha_lp_dual.py` (dead import,
`from pyhecke.gram import atom_per_generator_volumes`) and
`mass_formula_6term_mpfr_50dps.py`.

Attribute-form calls (`hecke_core.atom_per_generator_volumes(...)`) were checked
separately, since my first resolver would have missed them: the only sites are the
`gram.py` dispatcher and the two test files. No gap.

One caller is reachable **only transitively**: `r5_full_canonical_knot_solver.py`
→ `mass_formula_6term.term_23_brane_tower` → seed.

## Both existing queues miss almost all of it

| | |
|---|---|
| witness-owning callers in `.work/convention-d-blast-radius.json` | **2 / 12** (`mass_table_comprehensive`, `paper_six_term_isotope_sweep`) |
| witness-owning callers in the qou-lt8x complement `.work/convention-c-complement.json` | **0 / 12** |
| **in neither queue** | **10 / 12** |

This is qou-lt8x's defect one level further out. The blast radius asks *which
producers READ a moved witness*; the complement asks *which witnesses ARE
structurally C*. A producer whose numbers move because a **library function**
changed satisfies neither predicate — it reads nothing that moved and its
witness contains no √q fingerprint. Third detector, third question it does not answer.

## Environment note: the native wheel is pre-convention-D and is being refused

`pyhecke_native` 0.9.0 is installed in this container and **fails** the
convention-D self-check in `gram._verify_native_convergence`, so `_native_ok()`
returns False and every run takes the pure-Python (D) path. Verified directly
(`has_native()=True`, `_native_ok()=False`). The refusal is loud and correct —
but it means every producer run here emits a RuntimeWarning, and any host with a
*rebuilt* wheel would exercise a different code path than these measurements did.

## Measured: convention shift isolated from drift

Regenerating against the committed witness conflates four things — convention
C→D, interpreter/library drift (this container is python 3.11.15 / mpmath 1.4.1;
the witnesses were written under 3.13.12 / mpmath 1.3.0), a CODATA `m_p` update,
and timestamps. So each producer was run **twice in the same environment**, once
with `atom.py` at origin/main (C) and once at HEAD (D), and only the C-vs-D delta
is reported below.

| producer | s (per leg) | fields moved by convention alone | headline |
|---|---|---|---|
| `catalan_binding.py` | 0.5 | **73** | `formula_2_tower_per_block[2].err_pct` 4.4298 % → **16.8864 %**; `formula_1_wedderburn_log[2].err_pct` 12.9977 % → **−8.3265 %** |
| `entanglement_orders.py` | 19.3 | **46** | `particles[4].orders.5.contribution` 186.403 → **3641.807** (18.5×); `particles[2].orders.3.contribution` 6116.15 → **33372.13** |
| `rho_k_graded_atomic_mass.py` | 0.8 | **55** | `table[2].err_pct` 0.04572 % → **0.17374 %**; `table[0].err_pct` −0.016109 % → **+0.0090388 %** |
| `per_atom_hyperbolic_volume_witness.py` | 10.4 | **7** | `Vol_p` **flips sign**: −0.0404102 → **+0.0226378**; `Vol_4He` −4.60965 → −3.52907 |
| `multi_level_jet_sum.py` | 0.5 | **4 numeric** | `results[0].B_pred_MeV` −0.0236284 → **−0.0563776** |
| `li2q_fbor_expansion_probe.py` | 1.5 | **0** | convention-invariant |
| `r5_full_canonical_knot_solver.py` | 13.2 | **0** | convention-invariant |

## Refuted hypotheses — recorded so nobody re-runs them

1. **"Every caller's witness is stale in convention."** False. `li2q_fbor_expansion_probe`
   and `r5_full_canonical_knot_solver` call the function (r5 transitively) and produce
   **byte-identical** output under C and D. Calling it is necessary, not sufficient:
   both consume only convention-insensitive projections. 2 of 7 runnable cheap
   producers, i.e. **29 % of the cheap front is a false positive**.
2. **"A dirty diff after regeneration measures the convention shift."** False, and
   badly so. `li2q`'s regeneration flips `allPassed` **true → false** — with a
   *zero* convention delta. Cause measured, not inferred: CODATA `m_p` moved
   938.27208816 → 938.27208943, a relative shift of **1.3536 ppb**, and the
   witness's `err_full_ppb` moved 0.000404 → **1.3507**, i.e. a shift of 1.3503 ppb.
   Agreement to 0.25 %. Nothing to do with convention C.
3. **"The regression I caused was the convention's fault."** False. Regenerating
   `catalan_binding` moved the raw-float64 ratchet **35 → 47** on that witness.
   The 12 added fields are all `B_AME` under `formula_1_wedderburn_log[]` and
   `formula_2_tower_per_block[]` — the *producer* gained that output since the
   witness was committed (2026-07-07), independent of convention.

## What I did NOT do, and why

`catalan-binding.witness.json` was **reverted**, not committed and not baselined.
The obvious "fix at the producer" is a `_str` shadow companion, but
`_is_full_precision_shadow` only accepts a companion carrying **more than f64
significant digits**, and `B_AME` are experimental AME binding energies with ~7 —
a conforming shadow would have to *fabricate* precision. That is a worse defect
than the one it silences, and the right fix (source `B_AME` from the AME registry
as mpf) belongs to the raw-float64 drain, not to a convention sweep. So the
convention-D number for catalan-binding is recorded in the table above and the
file is left stale, deliberately.

`li2q` and `r5` were reverted as **measured-invariant**: committing them would
have been pure churn. r5's diff is 1199 substantive lines of braid-word change
(`2,2,2` → `−2,1,−2`) belonging to the NO-FLOAT64 braid-word fix, not to this work.



**Branch:** `claude/conv-d-atom-callers-sweep-wt` (authoritative), worktree `/tmp/qou-agent`. Claimed 2026-08-16.


## Expensive producers: all three exceed 900 s (measured, not inferred)

Run serially under `timeout 900`, each in its own process group, witnesses
restored by `git checkout --` on kill so no half-written file could land:

| producer | witnesses | measured |
|---|---|---|
| `pyhecke_h3_vs_h3a_impact_comparison.py` | 1 | **timeout at 900.1 s** — cost is a lower bound, not a value |
| `sweeps/paper_six_term_isotope_sweep.py` | 1 | **timeout at 900.1 s** |
| `probes/adjacent_vs_full_probe.py` | 4 | **timeout at 900.1 s** |

All three restored cleanly (`changed=0`). Note these need **2×** their cost to
get an isolated convention delta, since that requires a C leg and a D leg, so
each is a ≥30-minute measurement before any verification is possible.

*Measurement caveat, stated because it affects reproducibility:* this container
suspends between tool calls, so wall-clock-vs-elapsed diverges for background
work. Every number above and in the cheap table was taken from `time.time()`
inside the runner around a single `subprocess.communicate`, so they are process
elapsed time and unaffected — but a naive `date`-difference around a background
job here would not be.

## Gates — honest state

`bash scripts/precision-gates.sh` on the final tree: **RED on the raw-float64
ratchet.** Exactly one entry, and it is not mine:

```
NEW dirty witnesses            : 0
REGRESSED (count increased)    : 1
       3 -> 4       computations/rho-k-co-casimir-extended.witness.json
```

That is the known pre-existing qou-mnrd failure (needs a ≥24 GiB host). **Zero
NEW dirty witnesses and zero regressions attributable to this work** — the one I
did cause (catalan-binding 35→47) was reverted rather than baselined.

Also still red/advisory and pre-existing, named so this is not read as a green run:
the no-free-parameter cert has 1 UNTRACEABLE literal (`qbeta_t4_stokes3_crux_probe.py:60`,
`A_omega = 3`), and the advisory audits-tree scan has 6 dirty witnesses under
`docs/audits/scripts/` — none touched here.

## Two audit self-outputs committed because COUNTS moved

The gate run regenerates its own witnesses and asks for the count to be named:

* `q0-value-drift-audit.witness.json` — `STALE` **314 → 313**, `proton-pin`
  **801 → 802**. The witness that moved class is
  `computations/multi-level-jet-sum.witness.json`, whose q0 went from the stale
  `1.1099785955541805` to the canonical `1.1099785827513808`. Regenerating it
  drained a STALE q0 anchor — a side benefit of the convention work, measured, not hoped for.
* `witness-raw-float64-audit.witness.json` — `total_fields` **533,831 → 533,812**
  (−19), `drained_files` **30 → 31**.

## Final tally

4 of 12 witness-owning callers regenerated (`entanglement-orders`,
`rho-k-graded-atomic-mass`, `per-atom-hyperbolic-volume`, `multi-level-jet-sum`).
Of the other 8: 1 blocked on a raw-float64 conflict (catalan-binding), 1 blocked
on a pre-existing producer crash (brane-tower-isospin-diagnosis, 3 witness
copies), 3 exceed 900 s, 1 parked by owner decision (mass-table-comprehensive,
qou-53p1), and 2 measured convention-invariant and deliberately not regenerated
(li2q-fbor-expansion-probe, r5-full-canonical-knot-solver).


## 2026-09-06 — the "pre-existing producer crash" is the LEAST of that producer's problems

Re-measured while descending `scripts/bean-staleness-triage.py` (13th of 291
artifact beans). The final tally above lists `brane-tower-isospin-diagnosis`
(3 witness copies) as *"blocked on a pre-existing producer crash"*. It still
crashes, and the crash is real — but **fixing it would be the wrong move**, so
recording the verdict rather than the patch.

### The crash, and it is a genuine defect not a guard

    computations/brane_tower_isospin_diagnosis.py:180
    phi_vals = [float(Phi_q(v)) for v in vols]
    TypeError: unhashable type: 'dict'

`atom_per_generator_volumes` returns dicts; `Phi_q` is memoised. The file
**already contains the fix** — `abs_mpf(v)` at line 168 does
`x = v["full"] if isinstance(v, dict) else v`, and the line immediately above
the crash uses it. One of two sibling call sites was updated and the other was
not. `TypeError` is a builtin, not a corpus-defined domain exception, so by
AGENTS.md's own discriminator this is a crash and not a refusal.

### But the producer sits on a function documented as WRONG for exactly its inputs

`pyhecke.atom.atom_per_generator_volumes` opens with

> ⚠️ KNOWN BUG (audit 2026-05-25, PR #1238): This function uses HARDCODED H_3
> Wedderburn weights regardless of atom size A. For A > 1 (deuteron, ⁴He, ⁶Li,
> …), the braid lives in H_{3A}(q), not H_3(q), and the H_3 weights are
> systematically wrong. The CANONICAL replacement is
> `computations/mass_at_3A_proper.per_generator_V_hat_3A(Z, N)`.

`main()` diagnoses **proton, neutron, deuteron, tritium, helium-3, helium-4** —
**five of six at A ≥ 2**, i.e. precisely the regime the banner excludes. Its
whole headline (the T-vs-³He isospin asymmetry, converted to MeV through a
hardcoded `E_0 = 7.947423e-04`) is computed from those weights.

### And its kernel is float64 with an mpf twin sitting beside it

`mass_endomorphism.Phi_q` computes in `float` (`product = 1.0`, `1e-300`
underflow guard, `1e-15` break). `Phi_q_mp` is defined **in the same file** at
line 280, carrying `mpf`, with the f64 thresholds re-expressed as mp-scaled
ones. So the non-crashing path violates §PROBES-ARE-NOT-EXEMPT item 1 while the
correct routine is one import away.

### Verdict: do NOT resurrect it

Repairing line 180 would take a producer that (a) uses weights its own upstream
documents as systematically wrong for five of its six subjects and (b) computes
in float64 where an mpf twin exists, and make it emit a witness again. That is
strictly worse than leaving it crashed — a crash is visible; a green witness
carrying known-wrong weights is not.

The committed `brane-tower-isospin-diagnosis.witness.json` is dated
**2026-05-03**, `auditOnly: true`, `allPassed: null` — so the numbers on disk
predate the dict change and carry the H_3 weights. Nothing downstream should
read them.

**Two honest dispositions, neither of them "fix the TypeError":**

1. **Port it** — `per_generator_V_hat_3A(Z, N)` for the volumes, `Phi_q_mp` for
   the kernel — and re-derive. That is a real piece of work and changes every
   number it prints.
2. **Retire it**, with the witness marked superseded.

The wider H_3-vs-H_3A question already has a carrier in **`qou-2tuv`** (*"the
proper sum is infeasible past A=12"*), so this is not a new front; **27 live
non-deprecated modules** still reach `atom_per_generator_volumes`, and this one
is simply the instance this bean's tally happened to name.

## 2026-09-08: canonical ledger for the convention-C excision family is qou-wgta (the P0 excision tracker; owner-ruling milestone qou-cdx1, S2 science blocker qou-cds2); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 2 / §7.3 C3. Nine trackers, previously linked only cds2↔8iru and htsi→t9r1, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carrier M7 (qou-g16t) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

`atom_per_generator_volumes` caller sweep is its own migration (a shape
change), reached via the convention work but not a convention-C site. Keep
open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## Progress Update (2026-11-16, PR #8190)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/Float64EngineReachabilityAndGramInverse.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/float64_engine_reachability_and_gram_inverse_probe.py` and stamped witness `computations/probes/float64-engine-reachability-and-gram-inverse.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 2ed61761fb447e7b912df4f3ef73e8603236969a`).
- [ ] Awaiting merge of PR [`litlfred/qou#8190`](https://github.com/litlfred/qou/pull/8190) (`345a3f9ff4ba913bb465b8884e861bfccde997ca`).

