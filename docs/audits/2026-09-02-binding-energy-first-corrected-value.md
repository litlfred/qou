# The first `binding_energy` value the corrected framework has ever produced

**Measured 2026-09-02.** Completes the `qou-sv7h` arc: the Rust LP-accumulator
kernel is wired into both loops, and `binding_energy` runs end to end for the
first time.

## The result

```
atom        Z   N       B_pred (MeV)      secs
deuterium   1   1       -7.271102125      942.3
```

against AME2020 (`ame_binding_mev(Z, A)`, signature confirmed empirically
against three known values — deuteron 2.224566, triton 8.481796, ⁴He 28.295662):

| | value |
|---|---|
| **predicted** `B(²H)` | **−7.271102125 MeV** |
| **AME2020** `B(²H)` | **+2.224566 MeV** |
| sign | **WRONG** |
| \|ratio\| | 3.27× |

Term decomposition, same run: `unified_iterative_correction = −9.1477362310`,
`sdp_cross_channel_contribution = 0.0`, so `binding_from_frobenius_pairing =
+1.8766`. The negative sign is carried by term 1.

## The sign was already negative before the correction

Important, and it constrains what the correction can be blamed for. The
accumulator was negative on the **old** (braid-violating) matrices too —
measured `−0.0319` (k=4) through `−2.1955` (k=8) — and is negative on the
corrected family — `−0.0896` through `−2.0200`. **The correction changed the
magnitude by 71–221 %; it did not introduce the sign.**

So this is not "the fix broke the physics". It is: the framework's binding
accumulator has produced a wrong-signed result all along, and until now nobody
could see it, because the function could not complete.

## What is established

- `binding_energy` **runs**, for the first time, in 942 s for A = 2.
- Its deuteron value has the **wrong sign** against AME2020 and is 3.27× the
  magnitude.
- Both checked-in gates pass on this tree:
  `lp_accumulator_kernel_gate.py` → **7.092e-48**, exit 0.

## What is NOT established

- **One atom.** A = 3 was still running at 28 min when this was written (cost
  grows as A²). A single point is not a pattern, and the sign could plausibly
  differ across the light isotopes. Do not generalise from deuterium.
- **No witness regenerated.** `hadron-knot-table.witness.json` is untouched.
- **Nothing about *why* the sign is wrong.** That is a physics question this
  measurement opens and does not answer.

## `ysn_braid_relation_audit.py` still exits 1 — that is CORRECT

`_build_ysn_matrices` is deliberately **unchanged**. The kernel bypasses it by
building the correct family in Rust; it does not repair the Python one. So the
braid audit continues to flag a real defect in a function that is **no longer on
the binding path**. Do not read its exit 1 as the wiring having failed, and do
not "fix" it by weakening the audit — other callers
(`sdp_cross_channel.py`) still use that builder and are still affected.

## What changed in the code

`unified_iterative_correction`: each partition's whole trajectory is precomputed
in Rust before Pass 1, and the step loop reads `(trace, log_norm)` from it.
**Every line of the accumulation — `raw_delta`, `cumul_partition`,
`final_tr_sign` — and the whole of Pass 2's complementary-slackness gate are
untouched.** That distinction is the point: a reimplementation that drops Pass 2
is wrong by ~4.6× (measured), which is why the kernel is wired *in* rather than
*around*.

`atom_character_raw`: same kernel, taking the final step's trace and log-norm,
which is all that function returns.

Both fall back to the original Python path when `pyhecke_native` is absent — a
bare container has no extension module, and this module must still import there.
