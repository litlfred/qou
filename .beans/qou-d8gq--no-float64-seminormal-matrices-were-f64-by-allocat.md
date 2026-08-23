---
# qou-d8gq
title: 'NO-FLOAT64: seminormal matrices were f64 BY ALLOCATION — np.zeros() truncated every mpf entry'
status: completed
type: bug
priority: normal
created_at: 2026-08-16T13:45:22Z
updated_at: 2026-08-23T23:16:09Z
---

## The defect

`pyhecke/syt_prefix_cache.py::build_seminormal_matrices_cached` allocated

    M = np.zeros((dim, dim))        # float64

and then filled it with `M[r, c] = v`. When `v` is an `mpf`, numpy **silently
truncates it to 53 bits**. So the Hoefsmit seminormal representation came back
float64 *no matter what `q_val` was handed in* — a caller passing
`q_parameter.Q_MP` got bit-identical output to one passing the f64 `Q`.

Measured before the fix:

    q as f64 : build 0.01s  dim=162  dtype=float64  entry type=float64
    q as mpf : build 0.01s  dim=162  dtype=float64  entry type=float64   <-- destroyed

## Why it is worse than a plain precision loss

`mass_at_3A_proper.per_generator_V_hat_3A` multiplies these matrices against an
**mpf braid word** (19 of 35 steps carry an mpf since `efcaf79ed`):

    M = M @ (c * sigmas[i] + d * I_lam)

`c * float64_array + mpf` promotes the RESULT to `dtype=object`, so the matmul
leaves BLAS for Python-level mpmath. Measured at dim=162:

    3 matmuls:  as-is 18.928s   forced float64 0.0295s   ratio 642x

That is bean **qou-5qwb**'s failure mode. The computation was paying full
mpmath cost while carrying only float64 information — laundered precision AND
the slow path. It is why `per_generator_V_hat_3A` cannot reach 3A = 9
(qou-2tuv) while 3A = 6 takes 0.6 s.

## The fix, and the direction it deliberately does NOT take

The tempting fix — cast the braid word down to f64 at the matrix boundary —
would remove the leak and give a 642x speedup. **It is the forbidden
direction** (NO FLOAT64) and it was my first recommendation; the owner
rejected it, correctly. The matrices being f64 is the bug, not the mpf meeting
them.

Fixed at the allocation:

    M = np.zeros((dim, dim), dtype=_value_dtype(vals))

`_value_dtype` returns `float` when every entry is a plain float/int and
`object` otherwise, so the decision follows the values rather than a new flag.

    q as f64 : dtype=float64  entry type=float64   (unchanged, BLAS kept)
    q as mpf : dtype=object   entry type=mpf       (precision preserved)

**Existing f64 callers are bit-identical and no slower** — verified: the full
deuteron comparison table reproduces to the last digit after the change.

## What this does and does not buy

It removes the *silent destruction*: high precision is now possible when
requested. It does NOT by itself make `mass_at_3A_proper` correct, because that
module still seeds its cache from the f64 `Q0`
(`_cached_seminormal` -> `stem_name = f"n{n}_q{Q0:.10f}_..."`), so it still gets
float64 matrices and still leaks when the mpf braid word arrives.

Switching it to `Q_MP` is now MEANINGFUL where before it was a no-op — but it
will be slow, because honest mpf matmul at dim 162-216 is what the 642x
measures. That trade (correct and slow vs fast and forbidden) is the real
decision, and it is the owner's.

## Gate gap

`numpy_mpmath_dtype_leak_audit.py` is blocking and reported **0 candidates**
throughout, including with the leak live. Its scope is `d_for_ctype` consumers
and `hoefsmit_numpy.py`; it does not look for `np.zeros(...)` allocations that
later receive mpf. `computations/f64_into_mpmath_audit.py` DOES name this shape
in prose — "`BlockCache(float(Q0), float(HA_VAL))` seeds a cache with doubles"
— but it is **not wired into `scripts/precision-gates.sh`**, so nothing ran it.
Two separate gaps, both worth their own item.


---

## A category the scan misses entirely, not a sampling gap — measured at ~10⁴×

This bean records that the regexes UNDERCOUNT by ~30% against an AST reference,
chiefly multi-line allocations. Found 2026-08-23: there is also a shape the
scan cannot see **at all**, and it is the most expensive instance yet measured.

    computations/mass_at_3A_proper.py:551
        for (c, d, g) in word:
            M = c * sigmas[g] + d * I        # c, d are mpf; sigmas[g] is f64
            product = product @ M            # -> object dtype, no longer BLAS

Two independent reasons it is invisible to the main scan:

1. **`mp_vars` requires a LOCAL ASSIGNMENT from an mpmath expression.** `c` and
   `d` arrive by TUPLE UNPACKING FROM A FUNCTION PARAMETER (`word`), so they
   are never assigned from an mpmath call and never enter `mp_vars`. The
   ADVISORY param-fill section covers a parameter reaching a SUBSCRIPT fill
   (`M[i, i] = q0`); this is a parameter reaching a MULTIPLICATION.
2. With `c`/`d` untracked, the `np_tok`/`mp_tok` co-occurrence test has nothing
   to match on, so the line never reaches the arithmetic check.

### What it cost

`chi_lambda_of_word` is float64 end to end — `sigmas` are f64 ndarrays or
scipy CSR, `product`/`I` are `np.eye`, and every return is
`float(np.trace(...))`. The mpf bought nothing and cost:

    3He  shape (5,1,1,1,1)  dim=70   18,859.58 ms  ->  332.45 ms   57x
    chi identical to the last bit (|delta| = 0.000e+00)

and above the dim-500 sparse threshold it was not slow but FATAL —
`ValueError: scipy.sparse does not support dtype object`. The 4He partition
(8,3,1) dim=891 that raised it now returns in 0.03 s. A separate 420 s
profiling run of the same path segfaulted.

Blast radius: this is why `paper_six_term_isotope_sweep` could not complete. A
2900 s run exited 124 still inside 4He mode 1 of 8, with 100% of sampled stack
time on that one line. Extrapolated, 4He alone (77 partitions, max dim 7700,
sum dim^3 = 2.11e12) was ~16 YEARS.

Fixed at the numpy boundary in `03569d001`, which is what efcaf79ed's own
comment prescribes: *"Consumers needing f64 (the numpy validation paths) cast
at their own boundary."*

### Candidate extension, not implemented

A THIRD advisory section, in the same spirit as the existing param-fill one and
carrying the same "NOT a defect list" caveat: **a scalar of unknown provenance
multiplying a tracked numpy array.** It cannot distinguish an mpf parameter
from a plain float parameter, so it must be advisory — but the param-fill
section already accepts exactly that trade, and the shape it would catch is
worth four orders of magnitude.

Cheaper and possibly better alternative worth weighing first: a RUNTIME assert.
Any function whose return is `float(...)` could check `product.dtype != object`
once per call, which is exact rather than approximate, costs nothing, and needs
no regex at all.


---

## NEGATIVE RESULT: the consumption side cannot be hooked from Python

Recorded because it saves the next person the attempt, and because it changes
which detector is worth building.

A runtime probe patching `np.matmul` to report object-dtype operands was built
and validated in BOTH directions:

    np.matmul(prod, M)   module-level patch  ->  FIRES  (dtypes ('object','float64'))
    prod @ M             same patch          ->  SILENT

`ndarray.__matmul__` dispatches in C and never reaches the module-level name.
**`@` is exactly the form in `chi_lambda_of_word`**, so the obvious
interception point would have passed silently on its own motivating case — the
failure mode this whole area keeps producing. It was correctly NOT registered
as a gate.

A static AST proxy — a function parameter reaching `*` or `@` in a module that
handles both mpf and numpy — returns **116 sites**, mostly integer parameters
(`n`, `k`, `Z`, `i`) in ordinary arithmetic. It does not discriminate and was
correctly not offered as a finding.

## What DOES work, and it is cheaper than either

Check the RESULT rather than intercepting the operation. Landed in `6ed921b93`:

    if getattr(product, "dtype", None) == object:
        raise TypeError(...)

one attribute read per call, immediately before the trace. Exact rather than
approximate, needs no interception, and cannot pass silently on the shape it
was written for. It RAISES rather than casting: a float64 kernel that has
acquired object dtype has lost the guarantee its `-> float` signature makes,
and quietly repairing it would hide the regression the way the original
promotion did.

Verified in both directions, not just the passing one:

    current code, mpf word            ->  no raise, chi = 5.478692360634873
    same function with the cast removed ->  TypeError, guard fires

The generalisable rule: **every float64 kernel that ends in `float(...)` and
does a numpy matmul should carry this one-line dtype assert.**
`chi_lambda_of_word` is the first; a sweep for that signature would find the
rest, and it is a far better use of effort than another approximate scan.


---

## MEASURED: no second instance in the tree. Do NOT do the 19-kernel migration.

A sweep for the rule this bean proposes — *a function that returns `float(...)`
and does a numpy matmul* — found **27 such kernels, 19 unguarded**, and the
signature validates against its own motivating case (it finds
`chi_lambda_of_word` and correctly shows it as guarded).

The obvious next step was to add the one-line assert to all 19. **I measured
first, and the measurement says don't.**

### How

19 unguarded narrowed to **12** by asking which modules can even reach an
object scalar (import `mpmath` or `sympy`); the other 7 are pure-float64
modules where the promotion cannot arise. The 12 have a strikingly uniform
shape — `return float(np.trace(X))` — so a temporary PRINTING probe on `X`'s
dtype was inserted mechanically before each return, the producers were run,
and the probes were reverted (`git checkout --`, tree verified clean).

### Result

    total observations                  1388
    distinct dtypes observed            ['float64']
    object dtype                        0

    meson_character_shortcut_l1              float64   1003
    probes/markov_reduction_h3_to_h4_verify  float64    167
    ocneanu_weights                          float64     87
    alpha/alpha_k_jones_markov_h3            float64     39
    alpha/alpha_k_jones_markov_h4            float64     39
    phase5/phase1a_symbolic_trace_dominant   float64     35
    meson_symmetry_and_bar_involution        float64     12
    phase5/phase1b_two_row_closed_form       float64      6

**Adding a raising guard to those 8 would be dead weight** — it would defend
against something measured not to occur, in code nobody has studied, with a
non-zero chance of breaking a producer that legitimately does something else.
The guard belongs where the bug was found, and it is there (`6ed921b93`).

### The honest limit of this measurement

Two of the ten probed files ran rc=0 but **never reached the probed return**,
so they are **UNMEASURED, not clean**:

    computations/from_scratch/hoefsmit_general.py    chi_lambda_braid_numeric
    computations/hecke/hecke_characters.py           nuclear_braid_character

`nuclear_braid_character` is the more interesting of the two: it is the only
kernel in the 27 whose return is `np.trace(product)` with **no `float(...)`
wrapper**, so unlike the rest it can hand an object scalar straight to its
caller. If anyone extends this, those two are where to start — driven by a
caller that actually exercises them.

### What the sweep was actually worth

Not a migration — a **negative result**, obtained in about ten minutes, that
prevents one. The rule stays correct and worth applying to any NEW float64
kernel; it just has no backlog behind it today.
