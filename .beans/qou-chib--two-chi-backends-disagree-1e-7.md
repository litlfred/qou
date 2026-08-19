---
# qou-chib
title: 'Two averaged-chi backends disagreed at 1e-7 — RESOLVED: stale witnesses'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T18:00:00Z
updated_at: 2026-08-19T19:59:08Z
---

Two production producers compute χ^λ(β_atomic; q₀) in the **same** (averaged /
colour-weighted) convention and do not agree:

- `computations/chi_at_q0_via_hoefsmit_mpfr.py` → `chi-{atom}-h{n}-at-q0-50dps` (8 witnesses)
- `computations/compute_atom_chi_rust.py` → `atom-chi-rust-{d,t,3he,4he}` (4 witnesses)

Measured on the deuteron, per-partition relative difference:

| λ | rel diff |
|---|---|
| (6) | 6.956e-8 |
| (5,1) | 1.29e-7 |
| (4,2) | 3.762e-7 |
| **(4,1,1)** | **7.988e-7** |
| (3,3) | 7.614e-8 |
| (1,1,1,1,1,1) | 6.956e-8 |

Both claim 50 dps, so this is ~11 orders above the stated floor.

## Ruled out

- **μ–p pin tension** — 1.15e-8, wrong size, and **both take the proton pin**:
  the hoefsmit witnesses declare `q_0` inline
  (`1.1099785827513808075916690956107688798744991218736`);
  `compute_atom_chi_rust` imports `q_parameter.Q`.
- **float64 q₀ truncation** — ~2e-16 after the ~23-crossing amplification.

## The shape of the residual is the clue

The two **one-dimensional** blocks, λ=(6) and λ=(1⁶), disagree by *exactly* the
same 6.956e-8, while higher-dimensional blocks disagree by up to 11× more. A
scalar shift in `q` would move all blocks by their q-degree, not by their
dimension. That points at the **matrix products** — the seminormal path — rather
than at the input.

Next probes worth running:
1. Compare a single generator's matrix ρ^λ(σ_i) between the two backends at one
   λ of dim > 1. If they differ, it is the Hoefsmit construction, not the word.
2. Check whether the two use the same `(c, d)` colour weights and the same
   `include_inter` setting on `atom_braid_word_3A`.
3. Check the Rust kernel's internal precision on the `chi_q_atomic` path — the
   witness says mpfr 50 dps but the import alias is `Q0_F64`.

## Also

`atom-chi-rust-*` records **no q₀ at all**, contrary to the AGENTS.md rule that
a witness must say which pin it used. Fix regardless of the outcome above.

Until the cause is established, `chi-at-q0-averaged-atomic.derivation.json`
covers the Hoefsmit family **only**; the four `compute_atom_chi_rust` witnesses
are deliberately unclaimed and remain tier C. Claiming both would assert an
agreement that does not hold.

Found while draining tier C (bean `dgpc`), PR #5289.


---

## RESOLVED 2026-08-19 — no live bug, the artifacts were stale

Adjudicated against an **independent closed form**: on λ=(n) every generator
acts by the scalar `q`, so `χ^(n) = ∏_j (c_j q + d_j)` — computable straight
from the braid word without either backend.

| | deuteron λ=(6) | verdict |
|---|---|---|
| closed form | 1.559870199564151592706167 | — |
| hoefsmit (python mpmath) | matches to **8.7e-50** | **correct** |
| atom-chi-rust (as committed) | off by **6.956e-8** | **wrong** |

### The three probes, all negative

1. **`chi_cd_mpfr`'s `float()` calls** — classification only; coefficients are
   rebuilt in `mpf`. The word's `d` values match the bridge's templates to
   **1e-61**, so nothing is silently overridden. This was my leading
   hypothesis (`_TOL = 1e-9` accepting a value the bridge then replaces) and it
   is **wrong**.
2. **Same word, weights, `include_inter`, dps, pin** — both use
   `mass_at_3A_proper.atom_braid_word_3A`, both `include_inter=True`, both 50
   dps, both proton-pinned.
3. **The native kernel is exact** to ~1e-50 on every primitive: `σ`, `σ⁻¹`,
   `σ²`, `s1 s2 s1`, and the **sign-0 averaged** crossing against `(q+1/q)/2`.

### The actual cause

Re-running `chi_all_partitions_cd_mpfr` on the deuteron word **today**
reproduces the closed form to **5.9e-50**. The code is correct; the committed
witnesses were produced by an older pipeline and never regenerated.

### Outcome

D, T, 3He regenerated — each now matches the closed form to ~1e-49, and the two
**independent** backends agree across all 11 deuteron partitions to
**4.64e-50**, down from 7.988e-7. Not "one backend fixed" but two independent
implementations cross-validating at the arithmetic floor.

4He (H₁₂, 77 partitions) is a long run; lands separately.

### Residual, for a follow-up

- `compute_atom_chi_rust` emits three raw float64 fields (`compute_time_sec`
  ×2, `assertions[0].computed`). Already baselined; NEW dirty 0, REGRESSED 0
  after regeneration.
- Its witnesses still record **no q₀**, contrary to the AGENTS.md rule.
- **The general lesson:** a stale witness is indistinguishable from a wrong
  producer until you re-run. The shape of the residual (both 1-dim blocks
  disagreeing by *exactly* the same amount, higher-dim by up to 11× more) read
  as a matrix-product defect; it was a version difference.
