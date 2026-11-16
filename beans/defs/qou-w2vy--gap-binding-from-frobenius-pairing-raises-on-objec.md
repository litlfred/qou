---
# qou-w2vy
title: 'GAP: binding_from_frobenius_pairing raises on object dtype -- latent behind term 1''s hang'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-31T04:44:27Z
updated_at: 2026-10-04T15:14:52Z
parent: qou-v2om
---

Blocks qou-i7ju together with qou-4m9u. Evidence:
docs/audits/2026-08-31-binding-energy-cannot-run.md.

## The gap

`binding_from_frobenius_pairing(1,1)` raises on main in 0.52s:

    TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))

This is the SAME failure class the COO accumulator already fixed in
unified_iterative_correction -- scipy sparse refusing object dtype the moment an
mpf enters -- and it is UNFIXED here.

## Why nobody noticed

binding_energy applies term 1 (unified_iterative_correction) FIRST, and that
never returns for A>=2. Control never reaches term 3. The crash is latent behind
the hang.

Demonstrated: stub term 1 only, leave terms 2 and 3 as main has them ->

    binding_energy(1,1) deuterium RAISES TypeError
    binding_energy(1,2) tritium   RAISES TypeError
    binding_energy(2,2) he4       RAISES TypeError
    binding_energy(3,4) li7       RAISES TypeError

4 of 4. So binding_energy for A>=2 has TWO independent blockers, and fixing only
the performance one converts a hang into a crash.

## Corroboration

computations/hadron-knot-table.witness.json:
    computedAt      2026-06-17T04:13:13
    scriptCommitSha 08ec1c0d0999b6b6d8c902a4ec8fa5344a383a2d

2.5 months old. Its binding values predate whatever broke term 3, and nothing
since has been able to reproduce them.

## Term 2 for contrast

sdp_cross_channel_contribution(1,1) = 0.0 with BOTH the current and the
corrected matrices (27.9s / 67.1s). Unaffected, and zero, AT A=2 ONLY --
sdp_cross_channel.py consumes _build_ysn_matrices directly, so larger A is
untested and must not be assumed either way.

## Not established

The corrected-family run of term 3 had not completed at 10 min and is NOT
reported. Whether the crash is independent of which matrices are used is
untested -- though a dtype-conversion error suggests it is.


## FIXED 2026-08-31 -- and the fix exposes a THIRD blocker

atom_character_raw carried the unguarded branch; TWO identical occurrences
existed, both now fixed with the same COO object accumulation term 1 got in
da645cf0f32 (O(dim*nnz), COO cached per generator, no coercion of c/d to float).

**Term 3 no longer raises. It now does not terminate.** Deuterium ran >12 min
without completing, where before it raised in 0.52s. py-spy: 3/3 samples inside
the new COO accumulation (lines 1716, 1719) in mpmath __add__/__mul__.

So term 3 has the IDENTICAL performance wall as term 1 -- Python-level mpmath
over partitions up to dim 2310 -- and it was hidden behind the crash exactly as
the crash was hidden behind term 1's hang. Two layers of masking.

BLOCKERS NOW THREE:
  1. seminormal family is not a representation (qou-4m9u, settled; term 1 moves 71-221%)
  2. term 3 object-dtype crash -- FIXED
  3. Python-mpmath performance wall in BOTH term 1 and term 3 -- term 1 partly
     (5.8x guard fix), term 3 untouched

NEXT: lp_accumulator_step_traces_mpfr (built, merged in #6337) was written for
term 1's loop. Term 3's loop has the same shape -- identity start, per-crossing
M <- c(M.sigma) + dM, rescale, trace -- so the same kernel SHOULD serve both.
That is asserted FROM THE SHAPE, not measured. Wiring it into both is the next
concrete step, and it needs a value-equality gate the way the guard fix did.

## First 2026-09-04 pass (recovered from a stray file — see the note at the end)

*Sections below this heading were written first; the three CORRECTION sections
that follow them supersede parts of this text. Read forward.*


## Re-measured 2026-09-04 — the headline crash is FIXED, same day this bean was written

`binding_from_frobenius_pairing(1,1)` no longer raises. Blocker 2 was closed by
**`d943f2acfac`** (2026-08-31), whose message names this bean:

> `atom_character_raw` … carried the UNGUARDED sparse branch … That is term 1's
> PRE-FIX code: the COO object fallback added to `unified_iterative_correction`
> in `da645cf0f32` was never ported here. TWO occurrences of the identical block
> existed; both are fixed.

The same commit reports that fixing it **exposed blocker 3** — the Python-mpmath
performance wall, which had been hidden behind the crash exactly as the crash was
hidden behind term 1's hang. `815b2a46a08` (2026-09-02, `qou-sv7h`) then wired
the Rust LP-accumulator into **both** loops, and `7b8625230c4` reports the live
issue: `binding_energy` runs and **its sign is wrong**, systematically, confirmed
at tritium.

So the arc is 2 blockers → 3 → the sign. This bean's stated gap is closed; the
live successor is `qou-sv7h`.

### A wiring detail that will mislead a grep

`_HAS_LP_KERNEL` appears at exactly ONE call site (inside term 1), which reads as
"the kernel is wired into term 1 only". It is not: `atom_character_raw` reaches it
through the `_lp_kernel_steps` wrapper, which is where the availability check
lives. Resolve the wrapper before concluding term 3 is unwired — I nearly filed
that as a finding.

### The kernel's precision claim is vacuous at its own call site

`_lp_kernel_steps` states in its docstring:

> Coefficients cross the boundary as decimal **STRINGS: nothing narrows to f64**.

and it returns `mp.mpf` values. Its consumer then does

    _tr, _ln = _ks[-1]
    return (float(_tr), float(_ln), int(dim))

so the MPFR result is narrowed to float64 **one line after** the kernel produced
it. Two things are true and should not be conflated:

- **It is NOT a regression.** The pre-existing non-kernel return is
  `return (float(chi), float(log_norm), int(dim))` — float64 is this function's
  established contract, and the kernel path merely matches it.
- **It does make the claim vacuous HERE.** "Nothing narrows to f64" holds up to
  the FFI boundary and not past it, so at this call site the MPFR kernel buys
  speed, not precision. Anything downstream that reports agreement from this path
  is reporting the float64 floor, which AGENTS.md forbids describing as exact.

**And it is NOT the cause of the sign defect.** The sign is a ~100 % error;
float64 narrowing is ~1e-16. Do not connect them.

**Recommended, and marked as judgement rather than finding:** leave the return
contract alone for now. Changing it to `mpf` ripples to every caller of
`atom_character_raw` / `atom_markov_trace`, and the binding path has an open
sign defect that must be settled first — a precision change landed underneath a
wrong sign would just make the wrong number more precise. Revisit once
`qou-sv7h` closes.

### What is NOT established here

`binding_from_frobenius_pairing(1,1)` did not complete within **300 s** in this
container, with `_HAS_LP_KERNEL = True`. That is consistent with slow rather than
broken — AGENTS.md records deuterium running a full 50 minutes and being killed by
its own timeout — so it is reported as a non-completion, not a failure. A longer
run was launched; if it is not recorded below, it did not finish either.

> **Forward pointer, added when this was recovered.** The "not established"
> paragraph immediately above is answered by the CORRECTION section that
> follows: the run DID finish, at 958.5 s. And the `float(_tr)` finding two
> sections up is **NOT** among the things the THIRD CORRECTION retracts — it is
> **strengthened** by it. That correction establishes the KERNEL path is the one
> that executes, and `float(_tr)` sits on the kernel's own return, so the MPFR
> result is narrowed to float64 one line after it is produced, **on the live
> path**. What the third correction retracts is the separate claim about the
> Python fallback's float64 `ysn` matrices and the ambient `mp.dps`, which
> describe a path this input never takes.


## CORRECTION 2026-09-04 -- term 3 DOES terminate; the ">12 min" was a timeout

The section above states, flatly: **"It now does not terminate."** That is a
claim about termination drawn from a 12-minute observation, and it is wrong.

MEASURED, deuterium (Z=1, N=1), both halves that
`binding_from_frobenius_pairing` composes, on `main`:

    atom (include_inter=True )   503.6 s   type=mpf   0.89486186364004106
    free (include_inter=False)   454.9 s   type=mpf   3.2936269985705353
    ------------------------------------------------------------------
    total                        958.5 s = 15.97 min

`E_0*(|free| - |atom|) = 1.8766341061441356`, reproducing an earlier untraced
run of the whole function that returned `1.87663410614414` in 871.1 s. Two
independent runs, ~10 % apart in wall time, same value to every printed digit.

**So the bean stopped watching at 12 minutes on a 16-minute computation.** This
is the mirror of the trap AGENTS.md already records for `hadron_knot_table`
("a timeout is not proof of success") -- here a timeout was read as proof of
NON-termination. Neither direction is available from a timeout.

What survives unchanged: the **cost**. ~16 min for the FIRST bound atom is the
performance wall blocker 3 describes, and the `lp_accumulator_step_traces_mpfr`
wiring is still the right next step. Only the word "terminate" was wrong.

Reproduce (~16 min; do not re-run casually):

    python3 -u - <<'PY'
    import sys, time; sys.path.insert(0, "computations")
    import hecke_core_legacy as H
    for inter in (True, False):
        t0 = time.time(); v = H.atom_markov_trace(1, 1, None, include_inter=inter)
        print(f"{inter}: {time.time()-t0:.1f}s {type(v).__name__} {v!r}", flush=True)
    PY


## AND THE 16 MINUTES IS SPENT IN FLOAT64 ARITHMETIC (2026-09-04)

The run above printed, before doing any work, `mp.dps = 15`.

That is mpmath's **default**, and `mp.dps = 15` is `mp.prec = 53` -- exactly
float64's significand. Verified rather than assumed: at the default precision
2000/2000 random `mpf` values satisfy `mpf(x) == mpf(float(mpf(x)))`, i.e. every
mpf IS a float64. At `dps = 50` the same test fails, as it must.

**So an `mpf` return type is not evidence of precision**, and the COO mpmath
accumulation that blocker 3 measures is doing float64 arithmetic slowly.

Where the precision is not established, measured on `main`:

  * `hecke_core_legacy.py` -- **0** occurrences of `mp.dps`, `workdps`,
    `workprec`, or any `_precision` import, module-wide.
  * `atom_character_raw` (lines 1715-1818, 104 lines) -- **0** `workdps`,
    **0** `workprec`, **0** `mp.dps`, **0** `mpf(`, and **6** `float(`.
    It ends `chi = _trace_dim(M, dim)` / `return (float(chi), float(log_norm),
    int(dim))`, and `log_norm` accumulates through `math.log(m_max)`.
  * `computations/phase5/phase3_triton_binding_convention_b.py` -- the ONE
    external caller of `binding_from_frobenius_pairing` -- imports
    `mpmath as mp` at line 78 and **never sets `mp.dps`**.

The right pattern exists three files away and is not on this path:
`tools/pyhecke/python/pyhecke/atom.py:508` opens
`with _mpm.workdps(max(_mpm.mp.dps, 60)):` -- a FLOOR, so an ambient 15 becomes
60. `atom_character_raw` has no such floor.

**Scope, stated precisely:**

  * NOT a regression. This is legacy code and predates the COO fix; the fix
    changed the dtype handling, not the precision.
  * NOT the cause of anything measured here -- the termination result and the
    wall-clock stand on their own.
  * NOT covered by the existing gates. `precision-gates.sh` catches
    `mpf(<float>)` and an `mp.dps` no-op; **"nobody ever set dps" is a different
    hole**, and neither gate fires on it. A file with zero `mp.dps` occurrences
    is indistinguishable, to those gates, from a correct one.
  * "It is the EXPLORATORY path" is NOT an exemption -- the producer's own
    comment at line 84 says exploratory, and AGENTS.md is explicit that PROBES
    ARE NOT EXEMPT.

**NOT MEASURED, and it decides how much this matters:** what precision the
*inputs* carry. If the Hecke matrices reaching `atom_character_raw` are
themselves float64, raising `dps` buys nothing -- "a float64 input poisons the
whole result." I did not trace the input cone, so this is a ceiling I have
demonstrated, not a loss I have quantified. Establishing that is the next step,
and it is cheaper than the 16-minute run: instrument `_crossing_in_partition`
and `sigmas` for their element types.

**Related, same shape, one function over:** the `float(_tr)` narrowing at the
`_lp_kernel_steps` consumer already recorded on this bean. Two independent
float64 boundaries on the same term-3 path.

## SELF-CORRECTION, same day: the "NOT MEASURED" gap above was ALREADY CLOSED

The section above ends: *"NOT MEASURED, and it decides how much this matters:
what precision the inputs carry."* I then measured it — and the corpus had the
answer four days earlier, with the mechanism I did not have.

[`docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md`](../docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md)
states it directly:

> Both paths are float64-limited **because the YSN matrices are built in
> float64** (`a_rho = h/q_int(rho)` with float `h`; `off = math.sqrt(...)`), so
> exact agreement is unobtainable until the matrices themselves are exact.

and draws the consequence this bean should have drawn:

> The 2026-08-30 document recommended: fix the guard, export the Rust matmul,
> then fix precision. **That order is wrong.** Its own equality gate cannot be
> satisfied while the matrices are float64, and the matrices are not merely
> imprecise — they are not a representation.

So the ambient-`mp.dps` finding above is real but **subordinate**: raising `dps`
cannot help while `entry['ysn']` is float64, and the audit's ordering already
subsumes it. Do not open a precision item against `atom_character_raw` — the
open item is the matrices, and it is `qou-4m9u`.

**What my census does add is EXTENT, not the fact.** The audit reasons from the
construction (`a_rho`, `math.sqrt`); a census of the live table confirms there
is no exception anywhere in it. Measured on `main`, `H._PARTITION_TABLE`:

    entries                                682
      empty ysn (n < 2, no generators)     489
      SCIPY-SPARSE dtype=float64           124
      nested Python sequence of float        69
      mpf / object dtype                      0
    max dim                                2310

**193 of 193 non-empty entries are float64; zero exceptions.** So the float64
ceiling is a property of the whole partition table, not of a sparse/dense
branch or a size threshold.

**What this contaminated.** Two artifacts pushed ~20 minutes before this note:
the section above, and PR #6660's body, both of which present the input
precision as an open question and name tracing `_crossing_in_partition` /
`sigmas` as "the next step". That step was already taken on 2026-08-31. Read
both with this correction attached.

**The lesson is the checklist's own.** I ran the measurement first and the
corpus-grep second. Reversed, path 1 (`grep -rln ysn docs/audits/`) returns
that audit as its first hit and the whole detour is unnecessary — and the
detour was the cheap half; the expensive half was writing a "next step" into a
bean and a PR body for work already done.

## THIRD CORRECTION, same day: the precision thread above describes a path this input NEVER TAKES

Both precision sections above rest on one unstated premise — that the 958 s was
spent in the Python `entry['ysn']` loop. **It was not.** I inferred the
execution path from wall-clock time instead of instrumenting the dispatch.

`atom_character_raw` calls `_lp_kernel_steps` FIRST and returns early on
success; the Python `entry['ysn']` accumulation is only the FALLBACK:

    _ks = _lp_kernel_steps(entry['partition'], [...])
    if _ks:
        _tr, _ln = _ks[-1]
        return (float(_tr), float(_ln), int(dim))      # <- kernel path, returns
    for kkk in range(A):                               # <- fallback, never reached

Measured by wrapping `_lp_kernel_steps` in a spy, `Z=1, N=1`, across the whole
dimension range of the partition table:

    dim     1  (2,)                 total    0.00s   kernel    0.00s   KERNEL
    dim    14  (4, 3)               total    0.00s   kernel    0.00s   KERNEL
    dim    70  (3, 2, 2, 1)         total    0.03s   kernel    0.03s   KERNEL
    dim   300  (4, 4, 1, 1)         total    0.48s   kernel    0.48s   KERNEL
    dim  1540  (5, 3, 1, 1, 1)      total   18.09s   kernel   17.78s   KERNEL
    dim  1540  (5, 2, 2, 1, 1)      total   28.67s   kernel   28.65s   KERNEL
    dim  2310  (5, 3, 2, 1)         total   90.65s   kernel   90.64s   KERNEL
    dim  2310  (4, 3, 2, 1, 1)      total   49.01s   kernel   49.00s   KERNEL

**8 of 8 served, with essentially 100 % of wall time inside the kernel**
(90.65 total against 90.64 in-kernel). The kernel builds its own
`seminormal_matrices_mpfr` -- the braid-satisfying family -- at MPFR precision
with coefficients crossing as decimal strings.

**So three claims I pushed today are void for this path:**

  1. "the COO mpmath accumulation is doing float64 arithmetic slowly" -- the
     COO path does not run.
  2. the 193/193 float64 census of `entry['ysn']` -- correct as a measurement,
     but of the FALLBACK.
  3. the ambient `mp.dps = 15` ceiling -- likewise about the untaken path.

**The census is not worthless, it is MIS-SCOPED.** `pyhecke_native` cannot be
`pip install`ed and a container without it is the DEFAULT (AGENTS.md, project
structure). With `_HAS_LP_KERNEL = False` the fallback runs, and then the
float64 non-representation matrices ARE what computes. So the census describes
the bare-container path exactly, and says nothing about a container that has
the extension. State which one you mean.

**What survives, and one thing that improves:**

  * Term 3 terminates: 958.5 s, both halves `mpf`, reproducing
    `1.87663410614414` from an independent run. UNTOUCHED by all of this.
  * The cost is real and is now LOCALISED: it is Rust kernel time dominated by
    the largest partitions (dim 2310 at 49-91 s each, 193 entries). That is a
    better answer than "Python mpmath is slow" -- the remaining performance
    work is inside the kernel, not in porting Python to Rust, which is done.

**BLOCKER 3 ABOVE IS STALE.** It reads "Python-mpmath performance wall in BOTH
term 1 and term 3 -- term 3 untouched". Term 3 IS wired to the kernel and IS
served: `815b2a46a08` (2026-09-03, "wire the Rust kernel into both loops")
postdates this bean by three days. Do not use blocker 3 to justify a port.

**Method note, because this is the second instance today.** I inferred the
execution path from wall-clock time; earlier I inferred precision from a
`repr`. Both are the same error -- reading a proxy instead of the object. The
spy that settled this costs three lines and ran in under two minutes.


## Filing defect in this bean's own history (2026-09-04)

The four sections under "First 2026-09-04 pass" above did not originally live in
this file. Commit `1da825fc997` wrote them to
`.beans/qou-w2vy--gap-binding-from-frobenius-pairing-raises-on-obje.md` — the
same slug **truncated one character short** (`obje` for `objec`). That file had
no YAML front-matter and no `# qou-w2vy` header, so `beans` and
`scripts/bean-completion-candidates.py::load_beans` (which requires an id line
plus `status` and `updated_at`) both skipped it silently. Two real findings —
the `_HAS_LP_KERNEL` grep trap and the `float(_tr)` narrowing — were invisible
to the tracker for the whole session, while PR #6660's body described them as
recorded.

Caught by the pre-merge file listing, not by any checker. A near-miss slug is
indistinguishable from a new bean to anything that globs `.beans/*.md`, and
nothing validates that a bean file carries the header its name implies.


---

## Round 48 Execution Update (2026-11-16, PR #8181)

- **PR:** https://github.com/litlfred/qou/pull/8181 (`e3a0c2e1773d8a4bc1635ead95154cb8d9babb4d`)
- **Probe & 50-dps Witness:**
  - `computations/probes/spin_orbit_magic_rstar_mirror_probe.py`
  - `computations/probes/spin-orbit-magic-rstar-mirror-probe.witness.json`
- **Findings Verified:**
  1. Both the Rust MPFR LP kernel (`_lp_kernel_steps`) and the Python cached COO object-dtype fallback (`_HAS_LP_KERNEL = False`, accumulating in `dtype=object` via row/col index arrays) in `computations/hecke_core_legacy.py` execute cleanly without raising `TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))`, with `0.0` relative difference at `k_cap = 3` (`(2, 1)` block).
  2. Live post-`qou-oiz3` return-type contract recorded: `atom_character_raw` casts `(chi, log_norm)` to `(float, float)` at its return boundary, while `atom_markov_trace`, `atom_frobenius_norm_sq`, and `binding_from_frobenius_pairing` return `mpmath.mpf`. Per the bean recommendation, `atom_character_raw`'s public `(float, float, int)` return signature is left unchanged so downstream callers (`sdp_cross_channel.py`) are unaffected.
- **Status:** Kept at `in-progress` pending owner review and PR merge.
