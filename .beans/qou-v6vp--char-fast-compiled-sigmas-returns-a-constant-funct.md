---
# qou-v6vp
title: char_fast._compiled_sigmas returns a CONSTANT function of q; "mpmath50" is a label with no high-precision data
status: todo
type: task
priority: normal
created_at: 2026-08-22T09:43:02Z
updated_at: 2026-08-22T12:39:17Z
---

## What

`computations/substrate/char_fast.py::_compiled_sigmas` builds its rep
matrices from `mass_at_3A_proper._cached_seminormal(shape)`, which takes
ONLY a shape and returns a **float64 ndarray with q already substituted**
at the module-level `Q0` (its disk cache is keyed `q{Q0:.10f}`, which
encodes the assumption). `_compiled_sigmas` then wraps those constants in
`sp.lambdify(Q_SYM, S_sym, ...)`.

Two consequences, both measured, not argued:

**1. The returned "function of q" ignores its argument.**

    sigma, dim = _compiled_sigmas((2,1), 'mpmath50')
    sigma[0](mp.mpf('0.5'))  ->  1.1099785827513810599
    sigma[0](mp.mpf('2.0'))  ->  1.1099785827513810599
    sigma[0](mp.mpf('7.0'))  ->  1.1099785827513810599

Identical for every q. Same for shape `(3,)`, where the single entry
should simply BE q.

**2. `precision="mpmath50"` buys arithmetic, not data.** The float64
constants are widened to `mpf`; no information is added. The returned
value sits **2.27e-16** from the 50-digit `Q_50_DIGIT_STR` — i.e. at
float64 eps. `_safe_sympify` even makes this explicit: it converts every
entry via `sp.Float(float(val))`.

## Blast radius — latent, not currently wrong

Every caller found passes q0, so nothing in the corpus is currently
producing a wrong number from this:

- `chi_monotone_transfer.py:241` — passes `mp.mpf(Q_50_DIGIT_STR)`.
  Its self-test comment calls itself "an exact (50-dps) cross-check";
  that is overstated on the char_fast side, which is float64-accurate.
  The 1e-12 tolerance passes regardless.
- `a_operator/A_operator_extract_at_level.py` — `"double"`, at q0.
- `sublemma_2_1_A_operator_extract.py` — `"mpmath50"`, at q0.
- `sublemma_2_1_deuteron_branching.py` — `q_val=float(Q0)`.

**The trap:** it is silently correct only because everyone happens to use
q0. Any future q-sweep through this path will sweep a constant and
return the q0 answer with no error, no warning, and a `"mpmath50"` label
suggesting 50 significant digits.

## Why this is filed rather than fixed

Found while porting `sublemma_2_1_A_operator_extract.py` off float64
(`qou-zck8`, PR #5427). It is upstream of that file, in a different
module, and the fix is a real change to how the seminormal rep is built
(symbolic in q, or threaded q through `_cached_seminormal` + its disk
cache key) rather than a one-liner. Absorbing it would have made an
A-operator PR into a char_fast PR.

Recorded in-tree at `evaluate_word_matrix.__doc__` and in that
producer's witness under `precision.accuracy_ceiling_cause`, so the
ceiling is not re-derived from scratch by the next reader.

## Next honest step

Decide whether `_cached_seminormal` should be symbolic in q (correct,
slower, invalidates the disk cache format) or whether `_compiled_sigmas`
should stop pretending to be a function of q (honest, cheap, and forces
callers to state the q they baked). Then re-check the two "50-dps
cross-check" claims that lean on the current behaviour.


---

## Scoping (2026-08-22) — the fix is bigger than char_fast, and the class is already tracked

Two findings that change how this should be approached.

**1. The float64 substitution is not in `char_fast` at all.** It is two
layers down. `mass_at_3A_proper._cached_seminormal` builds via
`build_seminormal_matrices_cached(shape, cache=BlockCache(float(Q0),
float(HA_VAL)))`, and `pyhecke.syt_prefix_cache.BlockCache` is float64 by
signature and by storage:

    def __init__(self, q: float, h: float):
        self.q = q
        self.h = h
        self._by_rho: dict[int, tuple[float, float, float]] = {}

So the Hoefsmit block values `(a_p, a'_p, b_p)` are float64 at the point
of construction. `char_fast._compiled_sigmas` merely wraps the resulting
constants in `lambdify(Q_SYM, ...)`, which is what makes it a constant
function of q. Option (a) from the original bean — "make it symbolic in q"
— therefore means changing `BlockCache` / `build_seminormal_matrices_cached`
and their on-disk cache format, in `tools/pyhecke/`, with **17 consumer
files**. That is a package-level change, not a fix to this file.

**2. It is an instance of an already-tracked class.**
`computations/f64_into_mpmath_audit.py` classifies exactly this shape as
**NUMPY_ON_Q** — "numpy kernel in a module holding an f64 q-name and using
mpmath" — and marks that tier **"CIRCUMSTANTIAL — review, do not
bulk-edit"**, explicitly non-failing. Correctly-scoped count: 15 files /
60 ops where this is the worst tier, 257 ops corpus-wide. Related beans
already open on the family: `qou-840k`, `qou-d8gq`, `qou-jtbo`,
`qou-tj98` (completed).

## Revised recommendation

Option (b) — **stop pretending to be a function of q** — is the
proportionate fix and is safe: no caller anywhere passes a non-q0 value
(verified across all 7 consumers). Make `_compiled_sigmas` take no `q`, or
assert the passed q matches the baked one, so a future q-sweep fails loudly
instead of silently returning the q0 answer. Small, local, removes the trap.

Option (a) is the *correct* fix mathematically but is a `pyhecke` package
change with a cache-format migration, and per the audit's own guidance the
tier is review-not-sweep. It should be its own scoped piece of work with
owner sign-off, not folded into an A-operator PR.

**Not done here** — flagged for the owner's call on PR #5427.
