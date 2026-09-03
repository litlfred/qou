---
# qou-9ay6
title: 'hecke_core_legacy.binding_energy is unrunnable: unified_iterative_correction >120s at A=2, and binding_from_frobenius_pairing dies in scipy.sparse'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T20:31:59Z
updated_at: 2026-08-31T02:51:48Z
---


Split out of `qou-c7g8` 2026-08-30. Two defects in
`computations/hecke_core_legacy.py::binding_energy`, both reached only at A≥2
(it opens `if A <= 1: return 0.0`).

## (a) `unified_iterative_correction` — >120 s on the SMALLEST A=2 input

    unified_iterative_correction(1, 1)     >120s     <- bottleneck
    sdp_cross_channel_contribution(1, 1)   0.01s
    binding_from_frobenius_pairing(1, 1)   TypeError -- see (b)

Z=1, N=1 is deuterium, the smallest case that reaches this code at all. Callers
iterate far past it — `hadron_knot_table.ATOMS` runs to **ca40 (A=40)**. So any
producer that calls `binding_energy` over a nuclide table is not slow, it is
**unrunnable**, and raising a timeout does not reach it.

Known blast radius so far: `hadron_knot_table` (cannot finish; therefore also
the corpus's single Q0_FLIP, since it cannot be re-run to repin), and
`q0_migration_decompose`, which appears to "time out" only because it runs
`hadron_knot_table` twice under a 900 s child cap. Other callers of
`binding_energy` are not yet enumerated — do that before estimating scope.

## (b) `binding_from_frobenius_pairing` cannot run at all

    scipy/sparse/_sputils.py  upcast(*map(np.dtype, args))
    TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))

An object dtype — almost certainly mpmath `mpf` — reaches a `scipy.sparse`
operation, and sparse supports no object dtype.

**This is currently invisible**: (a) times out first, so nothing ever gets here.
It will surface the moment (a) is fixed. Do not treat fixing (a) as finishing
the job.

Two candidate causes, neither tested:
- this container runs **scipy 1.17.1 / numpy 2.4.6**, newer than whatever built
  the June witness; an older scipy may have tolerated the upcast;
- or it is a genuine leak of `mpf` values into a matrix that must be numeric.

Distinguish before fixing: if it is the leak, casting to float64 to silence it
would silently drop 50-dps precision, which the NO-FLOAT64 directive forbids.
Find where the object dtype enters, do not coerce at the boundary.

## How this was localized

Bisected `compute_atom("deuterium", 1, 1)` call by call. `build_atom_nf`,
`nf_tr`, `nf_net`, `check_frobenius`, `classify_nuclear_knot` and
`ground_state_ordering` are **all 0.00 s**; only `binding_energy` is slow.

⚠️ Note for whoever picks this up: `binding_energy` and
`compute_per_generator_volumes` BOTH short-circuit below A=2, so the first A=2
atom is the first time either runs. That made `ground_state_ordering` look
guilty on the evidence of the per-atom output alone. It is innocent — measure,
do not infer, which of the two is slow.

## 2026-08-31 — (b) FIXED at the root. And my first fix was wrong.

### The defect was a MISSING BRANCH, in 2 of 3 places

`_step_chain_generic` yields mpmath `mpf` coefficients (`d = -h`, i.e. ℏ_q —
correctly so), so `c * Msig + d * M_run` promotes the float64 accumulator to an
OBJECT array, and the next float64 `csr_matrix.dot` rejects it. Confirmed by
reading the failing frame's locals rather than inferring:

    sig_sparse : csr_matrix   dtype=float64  shape=(35,35)
    M_run      : ndarray      dtype=object   shape=(35,35)

`unified_iterative_correction` **already handled this**, with a comment naming
the exact TypeError and even naming the consequence — *"which is why this
producer had been dead: its witness is from 2026-06-17"*, i.e. hadron_knot_table.
But the identical loop appears at **three** sites, and only that one had the
object branch:

    unified_iterative_correction    had the branch
    atom_character_raw              BARE .dot   <- died here
    _contrib_single_partition       BARE .dot

So the defect is the divergence between three copies of one loop, not a bug in
any single one of them.

### 🛑 My first attempt was wrong and is reverted

I patched all three to `float(c) * Msig + float(d) * M_run`, reasoning that
`sig_sparse` is float64 so precision is capped anyway. The existing code refutes
that, in writing, at the site I was about to overwrite:

    > Densify and multiply with object arithmetic rather than coercing c/d to
    > float — that would silently discard the precision the mpf exists to carry
    > (AGENTS.md: never compute in float).

That is exactly the coercion this bean's own "Fix" section warned against
("casting to float64 to silence it would silently drop 50-dps precision... Find
where the object dtype enters, do not coerce at the boundary"). Reverted before
committing.

### What landed instead

Extracted the working logic into `_msig_object_safe(sig_sparse, M_run, gen,
coo_cache)` and wired all three sites to it. Extracted rather than copied a
third time — the divergence IS the defect. Complexity preserved per the
original's own note: accumulating over σ's nonzeros is O(dim·nnz), the same
order the float64 branch gets from sparse BLAS, whereas densifying σ is O(dim³)
in object arithmetic and does not finish.

    3 call sites via the helper, 0 bare `.dot` remaining
    pytest tools/qou-substrate/tests/ tests/  ->  145 passed

`binding_from_frobenius_pairing(1,1)` no longer raises: it previously failed in
well under a second with the TypeError, and now proceeds into real computation.

### (a) still open — and now clearly separate

The dtype crash and the >120 s cost are independent. `unified_iterative_correction`
never crashed; it was always slow, and it is slow *because* object arithmetic
replaces vectorised BLAS — which the corpus accepts deliberately, to keep the
mpf precision. So (a) is not a bug to fix but a design cost to engineer around:
making it fast means finding a formulation that keeps precision without
per-element Python arithmetic, not switching to float64.

## 2026-08-31 — (b) CONFIRMED FIXED by measurement

    binding_from_frobenius_pairing(1,1):
      before   TypeError in well under a second
      after    >600s with NO TypeError — it now computes

The dtype crash is gone. The function is slow for reason (a), which is a
different problem in a different function.

## (a) remains open — and it is a DESIGN COST, not a bug

`unified_iterative_correction` is slow *because* it does object arithmetic to
keep mpf precision, which the corpus chose deliberately and documented in
place:

    > Densify and multiply with object arithmetic rather than coercing c/d to
    > float — that would silently discard the precision the mpf exists to carry
    > (AGENTS.md: never compute in float).

So there is nothing here to "fix" in the sense of correcting a mistake. The
existing code already avoids the two obvious wrong answers: coercing to float64
(loses 50-dps precision, violates NO-FLOAT64) and densifying σ (O(dim³) in
object arithmetic, measured >10 min on the A=2 atom alone). It already reduced
the inner product to O(dim·nnz), the same order sparse BLAS achieves.

Making it fast therefore means a different formulation, not a patch. Options
worth someone's time, none attempted here:

- carry the mpf part as a SCALAR alongside a float64 matrix where the chain
  allows it, so BLAS does the matrix work and mpf only tracks scale;
- move the accumulation into the Rust `hecke-engine` with a high-precision
  scalar type, alongside the existing float64 path;
- exploit that `c` is `int` at every crossing measured and only `d` is mpf —
  the update `M_run = c·Msig + d·M_run` may factor.

**Do not "fix" this by lowering precision.** That is the one direction the
corpus has already ruled out in writing, and a fourth agent rediscovering the
float coercion is the likely failure mode here — I was the third.

## 2026-08-31 (later) — (a) was NOT a design cost. It was a factorial enumeration.

I called (a) "a design cost, not a bug" and said it was slow *because* object
arithmetic replaces vectorised BLAS. **Profiling refutes that**, and it is the
fourth wrong inference this pair of beans has produced from indirect evidence.

Profile of `unified_iterative_correction(1,1)` — the smallest input reaching the
code — over 90 s:

    hecke_core_legacy.py:351(fill)   80.342 s tottime   26,028,387 calls
    all of mpmath combined           < 1 s

`_count_syts_by_12_relation` enumerated EVERY standard Young tableau of shape λ
by backtracking, to classify each by where the value 2 sits. The count of those
is d(λ), which grows factorially — so the cost was the irrep dimension itself:
tens of millions of tableaux built to produce two integers.

### The closed form

In any SYT, 1 sits at (0,0), so 2 can only occupy (0,1) or (1,0) — the only
cells whose predecessors are filled. Therefore

    n_row = f^{λ/(2)}     n_col = f^{λ/(1,1)}     n_mix = 0, always

Both are skew-SYT counts, computed by a memoised corner recursion (`_f_skew`)
that never materialises a tableau. `n_mix` stays in the return signature because
`partition_character_sigma1` multiplies it by `h`; it is provably the zero it
always was.

Verified against the old implementation on all 137 partitions of n = 2..10:
**zero mismatches**, `n_mix == 0` everywhere. λ=(6,4,3,2,1), which has 1,153,152
tableaux, now returns instantly. 145 tests pass. Landed in `2121201f1`.

### What is left, and the next lead

After the fix `fill` is gone from the profile entirely and the remaining cost is
genuine mpf matrix multiplication — `_matmul_dim` at 72.8 s cumulative over 643
calls. So the original "object arithmetic" story describes the REMAINDER, not
what was dominating.

Within that remainder there is a concrete, precision-free win still on the
table: **6,186,121 `from_float` conversions**. `_build_ysn_matrices` seeds its
dense matrices with `M = [[0.0] * dim ...]` — Python floats — and then writes
`q0` / `-qi`, which are mpf. The matrices are therefore MIXED, and since YSN
matrices are sparse most multiplications hit a `0.0` operand and convert it to
mpf every time. Seeding with `mp.mpf(0)` instead is the same value with no
conversions. `_matmul_dim` has the same shape in its accumulator (`s = 0.0`).

Untested as of this note — do not assume the size of the win, measure it.

### The `from_float` lead is DEAD — and my premise for it was wrong

I proposed seeding the YSN matrices with `mp.mpf(0)` because their nonzero
entries `q0` / `-qi` "ARE mpf". **They are not.** Measured:

    q0 : float = 1.1099785827513808
    qi : float = 0.9009182839557415
    h  : float = 0.20906029879563937

All three come from `q_parameter` as Python floats, so the YSN matrices are
uniformly float and my change would have MIXED them rather than unmixed them.
Reverted before commit. (Fifth wrong inference in this bean pair; the fix was
written and thrown away in the same turn.)

The only mpf in the whole pipeline is `_PROTON_G1` / `_NEUTRON_G1`, built in
`pyhecke.atom.nucleon_gen_chains`, and it is deliberate — its own comment cites
the owner directive:

    > NO FLOAT64 (owner directive). `pyhecke.gram.h` is a Python float —
    > 2.61e-16 relative against the 50-dps closed form — and using it here put
    > every INTRA-nucleon crossing into the braid word at ~17 good digits.
    > [...] Built at >= 60 dps whatever the caller's ambient precision.
    > Consumers that genuinely need f64 (the numpy paths) cast at their own
    > boundary, where the loss is visible rather than baked in here.

So converting it is the exact move the corpus forbids, and the sanctioned
escape already exists: `nucleon_gen_chains(..., allow_float64=True)`.

### ⚖️ For the owner: precision is not accuracy here

Worth a ruling, because it decides whether (a) is worth engineering at all.

`hecke_core_legacy` is **float64 at both ends**. Its `q0`, `qi` and `h` are
Python floats, and `_build_ysn_matrices` fills its matrices with `q0` / `-qi`,
so the matrices are float64. The ONLY high-precision quantity entering is the
chain coefficient `d` from `_PROTON_G1` / `_NEUTRON_G1` at ≥60 dps.

That single mpf coefficient promotes the accumulator to dtype `object`, which
forces every subsequent matrix multiplication out of vectorised BLAS and into
per-element Python arithmetic — the entire remaining cost of (a). But it is
carrying 60 digits through a computation whose `q0` is already only good to
~17: `nucleon_gen_chains`'s own comment measures `pyhecke.gram.h` at 2.61e-16
relative. The extra digits are precision, not accuracy — they cannot survive
contact with a float64 `q0`.

If that reading is right, `unified_iterative_correction` is exactly the
"consumer that genuinely needs f64" the comment describes, and the correct fix
is the sanctioned one: cast at ITS boundary via `allow_float64=True`, visibly,
rather than paying object arithmetic to carry digits the inputs never had.

**Not doing this unilaterally.** It is a NO-FLOAT64 boundary decision and the
directive is the owner's. Recorded with the evidence so the ruling can be made
on measurements rather than on my say-so.


## 2026-09-03 — NO FLOAT64 EVER: excised the f64 I had preserved on purpose

Owner restated the directive. Three things went, two of which I had built or
kept myself:

1. **`_build_ysn_matrices(q=...)`** dispatched arithmetic on the operand type
   (`pyhecke.syt_prefix_cache._sqrt_for`) so a float `q` produced float
   matrices. I wrote that to keep `sdp_cross_channel`'s sweep bit-identical to
   the private copy the builder replaced — i.e. I preserved an f64 path
   deliberately. Bit-compatibility with an f64 predecessor is not a reason to
   keep computing in f64. It now promotes whatever it is handed.

2. **Both q-sweeps in `sdp_cross_channel`** (`q_sweep_sdp_atom` and
   `q_sweep_regime_detection` — a second copy of the same shape) carried f64
   through mu_λ, the YSN matrices, the characters and the pair couplings.
   Now mpf throughout; the reported `q` is a decimal string rather than
   `float(q)`, because downcasting on the way out is the same loss moved to
   the serialisation boundary. `_mp.mpf` accepts strings, so callers can pass
   exact grid points — a Python float literal is f64-quantised before the
   function ever sees it (`1.05` -> 1.05000000000000004440892098...).
   The scalar LP remains f64; that boundary is now marked at the call site
   rather than being invisible, since excising it means replacing the solver.

3. **`hadron_knot_table` computed its Markov z in float64 while the exact mpf
   value sat unused fifteen lines below.** `_z = Q**3 / (Q**2 + 1)` over the
   float `Q` fed `delta_xchan = _Z2 * cross_sum * M_E_MEV` and the witness,
   while `_z_q0 = _Q0**3 / (_Q0**2 + 1)` — same formula, mpf — was defined and
   read by nothing. Also `w.add_parameter("q", Q)` put an f64 q INTO the
   witness. Both now use `_Q0`. The float import of `Q, Q_INV, HA,
   HBAR_Q_SQ` is gone entirely; the last three were dead. (The deleted line's
   comment described z as `1/(q^{1/2}+q^{-1/2})`, convention C — excised by
   owner ruling — while the code was already convention D. Both fixed.)

`source_float64_import_audit`: **2 files drained, 463 -> 458** imported names,
0 regressed, 0 new. Baseline re-written.

That 458 is the remaining corpus-wide debt under this directive:
Q=313, HA=56, Q_INV=49, HBAR_Q=12, E_CROSS=9, S_SKEIN=5, HBAR_Q_SQ=5, LN_Q=4,
TWO_Q=4, TANH_LN_Q=1.

Full suite 183 passed; braid audit exit 0.
