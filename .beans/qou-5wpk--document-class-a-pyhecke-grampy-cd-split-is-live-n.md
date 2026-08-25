---
# qou-5wpk
title: 'Document class A: pyhecke gram.py C/D split is live (native wheel is D, gram.z is C)'
status: completed
type: task
priority: normal
created_at: 2026-08-11T11:21:05Z
updated_at: 2026-08-15T22:22:29Z
---


## The split the banner predicted has already happened — measured 2026-08-11

`tools/pyhecke/python/pyhecke/gram.py:121` sets `z = 1.0/(q0**0.5 + qi**0.5)` —
convention C, float64, module-level, evaluated **at import**. Lines 44–47 carry
an explicit banner: *"TRACE CONVENTION C — and the C → D migration is BLOCKED
HERE. Do not 'finish the excision' on this line."* (bean `qou-wgta` item 11).

**Why it was blocked, and the reason is sound:** `G_INV = np.linalg.inv(G)` runs
unconditionally at import, and under convention D that Gram form is **singular**
— proved in `QOU/QBeta/GramSignature.lean`. `tests/test_gram_values.py:50` pins
`z == 0.4993203341836945`, so C is asserted there deliberately.

**What is new.** The banner warns that once the native wheel is rebuilt,
`build_atom_nf` / `atom_per_generator_volumes` return D while `z`/`TR_M`/`G`/
`G_INV` in the same module stay C. That rebuild has happened:

| layer | value at q₀ | convention |
|---|---|---|
| `pyhecke_native.markov_z` (v0.9.0, `.so` dated 2026-08-10 12:58) | `0.6126880371464652` | **D** |
| `pyhecke.gram.z` | `0.4993203341836945` | **C** |

**And the only thing detecting it is silent.**
`computations/substrate/deuteron_tower_fusion_frame_probe.py` computes exactly
this check and records

```
z_canonical_equals_pyhecke_gram_z: False
z_live_pyhecke: 0.4993203341836945
allPassed: False
```

then **exits 0**. The regeneration cascade recorded it `ok` at 25/29. (→ `qou-9d6h`)

**Coupling to the Rust bug.** The banner states the Rust mirror
`tools/hecke-engine/src/gram.rs` "survives the degeneracy only because it still
carries the pre-2026-05-19 `TR_M[5] = z^3` bug that this file fixed" (correct is
`h·z² + z`). So fixing that known bug may make the singularity bite in the
native path too — it cannot be decided independently of the gram.py convention.

**Owner ruling 2026-08-11:** take route D1(b) — move `gram.py` to D and invert on
the quotient (→ `qou-w8zz`), and make the probe exit non-zero (→ `qou-9d6h`).

## Witnesses downstream of this blocker (cannot clear until D1(b) lands)

Of the 14 witnesses still carrying the z_C fingerprint `0.49932033418369`, these
import `pyhecke`: `gram-matrix-dual`, `h2o-bond-angle-magnitude-vsepr`,
`qbeta-c3-barodd-binding-sdp-dual`, `deuteron-tower-fusion-frame-probe`.

Legitimate C references, NOT defects — they name C explicitly as a comparison:
`markov-z-fibre-rank-bar-covariance` (`.data.conventions.C.z_at_q0`),
`ocneanu-param-from-fibre-dimension` (`.checks[].z_C`).
