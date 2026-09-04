
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
