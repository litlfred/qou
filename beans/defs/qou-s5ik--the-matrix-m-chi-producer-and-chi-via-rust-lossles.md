---
# qou-s5ik
title: the matrix-m chi producer and chi_via_rust_lossless write the SAME witness filename
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T03:43:16Z
updated_at: 2026-10-04T15:24:57Z
parent: qou-5vkl
---

## Two producers, one filename

Both of these write `chi-{atom}-h{n}-at-q0-{dps}dps-matrix-m.witness.json`:

- [`chi_at_q0_via_matrix_m_mpfr.py:185`](../computations/chi_at_q0_via_matrix_m_mpfr.py)
  — `out_path = HERE / f"chi-{atom_name}-h{n}-at-q0-{dps}dps-matrix-m.witness.json"`
- [`chi_via_rust_lossless.py:75`](../computations/chi_via_rust_lossless.py)
  — `out = HERE / f"chi-{atom}-h{n}-at-q0-50dps-matrix-m.witness.json"`

So whichever ran last owns the file, and `witness.producer` / `scriptFile`
flip-flops between `matrix-m-chi-q-via-gp` and the rust-lossless producer
depending on run order. Nothing detects this: the producer-orphan audit checks
that a witness *has* a producer, not that only one producer claims it.

## How it surfaced

Found while draining the raw-float64 ratchet (PR #5163). The two producers
disagree on the *type* of `compute_time_sec` — matrix-m now writes a string
(wall clock, like `chi_at_q0_via_hoefsmit_mpfr.py`), rust-lossless writes an
`int` — and `chi_via_rust_lossless.py:89` reads the cache back with a bare
`int(cached.get("compute_time_sec", 0) or 0)`. Reading a matrix-m-written cache
there raises `ValueError: invalid literal for int() with base 10: '0.05'`.

Patched at the read site (`int(float(...))`) so it tolerates either producer,
which is the right defensive fix but not the root fix.

## How to attack

1. **Decide which producer owns the name.** They are not interchangeable —
   matrix-m is the mpfr matrix-M backend, rust-lossless goes through
   `chi_q_via_gp`. Two different computations should not share an output path.
2. **Rename one.** `-matrix-m` describes the matrix-M backend, so
   `chi_via_rust_lossless.py` is the one carrying the wrong suffix; a
   `-rust-lossless` suffix would say what it is. Check consumers before
   renaming — `li6_h18_amplification_discriminator_probe.py` names
   `chi-lithium-{5,6}-h{15,18}-at-q0-50dps-matrix-m.witness.json` explicitly,
   and there may be others.
3. **Add a guard to the orphan audit**: flag any witness filename that more
   than one producer can emit. That is the check that would have caught this
   without a type mismatch to trip over.

## Worth checking while in there

Whether the two producers actually agree numerically on a shared atom. If they
do, the collision has been harmless so far and the fix is pure hygiene. If they
do not, the corpus has been silently serving whichever ran last.
