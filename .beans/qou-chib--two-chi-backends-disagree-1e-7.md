---
# qou-chib
title: 'Two averaged-chi backends disagree at 1e-7 — cause not established'
status: todo
type: task
priority: normal
created_at: 2026-08-19T18:00:00Z
updated_at: 2026-08-19T18:00:00Z
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
