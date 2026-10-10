---
# qou-w8zz
title: 'D1(b): move pyhecke gram.py to convention D, invert G on the quotient H3/rad'
status: completed
type: task
priority: normal
created_at: 2026-08-11T11:21:04Z
updated_at: 2026-08-15T22:22:29Z
---

## Update 2026-08-14 — both blocking uncertainties measured (PR #5025)

`computations/probes/gram_radical_exact_probe.py`. The banner's decision rested
on two factual claims; neither survives contact.

**1. The degeneracy is EXACT.** The banner had to quote `det = 3.998e-17`,
`cond 4.9e+16`, and noted that even mpmath at 60 dps "bottoms out at f64 noise,
not a resolved eigenvalue". That is the NF path's float64 limitation, not the
question's. `z_D = q³/(q²+1)` and `h = q − 1/q` are **rational** in q, so at
rational q the Gram is exactly rational:

| q | det(G) under D | rank D | nullspace dim | rank C |
|---|---|---|---|---|
| 11/10 | **0 exactly** | 5 | 1 | 6 |
| 7/5 | **0 exactly** | 5 | 1 | 6 |
| 13/7 | **0 exactly** | 5 | 1 | 6 |

**2. The null direction has a closed form** — and it is the q-antisymmetriser:

```
v = Σ_w (−1/q)^ℓ(w) T_w
  = γ − q⁻¹(σ₀ + σ₁) + q⁻²(L₊ + L₋) − q⁻³ e⁻
```

`G @ v == 0` exactly at all three q. This is an **independent confirmation of
`qou-u2jg` from the Gram side**, and it gives the repair an explicit projector
rather than a numerically-extracted null vector.

**3. `G_INV` has ZERO arithmetic consumers.** The banner says it is "exported at
import into constants.py, atom.py, molecular.py, sdp.py and nine corpus
consumers" and that "every consumer expects a 6×6 inverse". Surveyed over `.py`
sources: `constants.py` 0, `molecular.py` 0, `sdp.py` 0, `atom.py` 1 (a
**comment** recording the M2b move), `__init__.py` export list only. Nothing
multiplies by it — no `@`, no `.dot`, no indexing.
`computations/gram-matrix-dual.py` inverts a Gram but builds its **own**
(line 179) and imports only `z`/`NF_BASIS`/`NF_NAMES`/`TR_M` — a second instance
of the hazard, not a consumer of this one.

### What this changes

The blocker is **narrower than recorded**. A convention-D switch breaks exactly
one thing: a test asserting `G @ G_INV ≈ I`, an identity convention D makes
FALSE. That is the test reporting the mathematics correctly, not a regression.

### What is still gated

Switching `gram.py` itself, because `z`, `TR_M` and `G` **do** have consumers and
moving them moves numbers. That is untouched by this survey and remains the
owner's call. The probe removed the two factual uncertainties the decision was
resting on; it did not make the decision.


## Update 2026-08-15 — flip ATTEMPTED, and the scope is THREE sites (PR #5055, draft)

Owner approved the flip. The library core is done and verified; the branch is a
**draft** because running the tests found a coupled site this bean, and the
`gram.py` banner, both missed.

### Done and verified

| | before (C) | after (D) |
|---|---|---|
| `z` | 0.4993203341836945 | **0.6126880371464652** (+22.70 %) |
| `TR_M[5]` | 0.5514434143184560 | **0.6911664783584446** |

```
RADICAL          (1, −1/q, −1/q, 1/q², 1/q², −1/q³)
‖G @ RADICAL‖     2.6e-16     numerically zero, as the exact result requires
G·G⁺·G = G        2.6e-15     pseudoinverse property holds
‖G⁺ @ RADICAL‖    1.4e-15     G⁺ kills the radical — it IS the quotient inverse
```

`RADICAL` comes from the **closed form proved in PR #5025**, not a numerical
extraction — at this module's float64 precision a numerical null vector is
indistinguishable from noise, which is why the old banner had to quote
`|λ_min| = 3.9e-17`.

`G_INV` is **removed, not rebound**. `gram_inverse()` raises and names `G_PINV`.
Repointing a trusted name at a different object is how a wrong number keeps
circulating; the two differ exactly on the radical, which is the content of the
convention change.

### Correction to this bean's own survey

"Zero arithmetic consumers" held — nothing *multiplies* by `G_INV`. But it was
too narrow: two shims **re-export** it (`computations/hecke_core_legacy.py`,
`computations/substrate/hecke_core.py`). Both updated to `G_PINV` + `RADICAL`.
Re-export is not arithmetic, but it still breaks an import.

### 🛑 The blocker — `trace_formal.py` is a SECOND convention-C site

```python
trace_formal.py:48    z_formal = 1 / (s + 1 / s)        with s = sqrt(q)
```

Convention C — and **not one line**. `s = √q` is the base symbol the whole
module is parameterized on. Under D, `z = q³/(q²+1)` is rational in `q` and does
not need `s` at all, so converting it is a **change of symbol basis**, not a
substitution.

Flipping `gram.py` alone desynchronises the symbolic and float trace paths by
22.7 %, with only a test to say so. Three of the 11 failing pyhecke tests are
`test_trace_formal` reporting exactly that; the other 8 pin C's `z` and the
`G @ G_INV ≈ I` identity, i.e. the tests reporting the mathematics correctly.

### The real scope

| site | state |
|---|---|
| `pyhecke/gram.py` | ✅ done, verified |
| `pyhecke/trace_formal.py` | ❌ symbol-basis change (√q → q) |
| `hecke-engine/src/gram.rs` | ❌ `TR_M[5]` + quotient together — `qou-m7py` |

The banner named only the third. **Awaiting owner direction** on whether to
extend to all three, do the two Python sites, or park it — the approved
decision was "flip `gram.py`", and the honest scope is larger.

## 2026-08-15 — DONE on the Python side (PR #5055, out of draft)

`gram.py` and `trace_formal.py` are both convention D. Two claims I made
mid-work were wrong and are corrected in the PR body and in the code:

* **"trace_formal needs a symbol-basis rewrite"** — false. `z = q³/(q²+1)
  = s⁶/(s⁴+1)` is still rational in `s`, and `s = √q` is required anyway by
  `quantum_int` (balanced `[n]_q`). One-line substitution; the `s` basis is
  kept so the root-of-unity API is untouched. I blocked the PR on a
  non-blocker.
* **"the Rust is still on convention C"** — false. `markov_z` is already
  `q³/(q²+1)`. See qou-m7py for the crate's actual divergences (`z³` trace
  rule + muon anchor).

### Two results worth carrying forward

1. **The exact ℚ path is now genuinely exact.** `_Z_FRAC` was
   `4993/10000` — a 4-digit truncation injected into a path labelled
   "exact", forced by C's irrational `z`. Under D it is
   `1367631/2232100` exactly. Consequence: the exact-ℚ path is the ONLY
   one that can *prove* the Gram degenerate (det `0` exactly, rank 5);
   float64's `3.998e-17` and mpmath's smaller epsilon cannot distinguish
   singular from tiny. Pinned by
   `test_gram_determinant_is_exactly_zero_over_Q`.

2. **The trace pole moved N=2 → N=4.** C: `z = s/(s²+1)` → pole at
   `q = −1`. D: `z = q³/(q²+1)` → pole at `q = ±i`. Verified analytically
   at N=1..4. **ζ₂ is now an accessible evaluation point; ζ₄ is not.**
   → *Actionable for anyone on the Habiro / Q_β c₃ residue front:* any
   analysis that assumed N=2 was the excluded root of unity needs
   re-checking. This is the kind of change that silently invalidates a
   downstream conclusion without failing any test.

### Guard added (and its cost)

`build_atom_nf` / `atom_per_generator_volumes` now REFUSE to dispatch to
`pyhecke_native`, because with Python on D and the crate diverging,
installing the wheel would silently change results per-machine. Costs the
~100× speedup until qou-m7py lands. `QOU_ALLOW_NATIVE_DIVERGENCE=1`
overrides.

### Not done

- qou-m7py (Rust) — guarded against, not fixed.
- qou-aze5 — pre-existing LP-dual test/impl contradiction found while
  draining the suite; not folded in.

### 2026-08-15 check-in — a third G_INV consumer, missed twice

My "zero arithmetic consumers" survey was wrong in scope **twice**:

1. (already corrected) it missed the two re-export shims,
   `hecke_core_legacy.py` and `substrate/hecke_core.py`;
2. (this pass) it never walked `computations/_deprecated/`.
   `hecke_startup_cache.py` **imports and serializes** `G_INV`
   (L105, L157) — removing the symbol would have shipped a hard
   `ImportError`.

**Method lesson worth keeping:** the survey grepped for *arithmetic* use
(`@`, `.dot`, indexing) and for live trees. Neither filter catches a
re-export or a `.tolist()` serialization, and `_deprecated/` is still
importable Python. When removing an exported symbol, grep for the NAME
across every tree and classify each hit, rather than grepping for the
uses you expect. Also: `mergeable_state: clean` is no evidence here —
there is no textual conflict when a symbol merely stops existing.

Fixed by DROPPING the `gram_matrix_inv` cache key rather than repointing
it at `G_PINV` (same reasoning as `G_INV` itself: don't hand readers a
different object under a trusted name; a JSON key is worse than a Python
symbol because it carries no type to trip over). New keys:
`gram_matrix_quotient_inv`, `gram_radical`. Zero consumers of the old key
anywhere outside the producer, verified.
