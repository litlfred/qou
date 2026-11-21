# H₂ order test — results

Pre-registration: `preregistration.md` (commit 428919bc80b). Producer: `h2_order_test_probe.py`.
Witness: `h2-order-test.witness.json`. 56 bare molecules: nucleon P ∈ {V¹…V⁷}, electron E ∈ {V³, torus T(2,7) stabilised},
atom-1 order ∈ {pe, ep}, atom-2 order ∈ {pe, ep}. Reading 3 at every level, convention D, proton q₀, mpmath.

## Check

- **O2 PASS.** At levels 1–3 the closure tests only the bottom 3-strand block, so these levels pass iff the bottom
  particle passes reading 3 on its own strands (tensor-product Markov factorisation).

## Outcome: (i) order-dependent

| P | E | atom-1 = pe | atom-1 = ep |
|---|---|---|---|
| V³ | V³ | pass (both atom-2 orders) | pass |
| V³ | torus m=7 | pass | **fail at levels 2–4** |
| V⁶ | V³ | pass | pass |
| V⁶ | torus m=7 | pass | **fail at levels 2–4** |
| V¹, V², V⁴, V⁵, V⁷ | either | fail | fail |

- The torus electron passes only when the proton sits on the bottom strands. Put it on the bottom and levels 2–4
  test the electron alone, which fails (it fails T1 alone, see `h2_torus_electron/results.md`).
- The V³ electron passes in all four orders, with P = V³ or V⁶.

## What the earlier probes did not show

Higher levels also test the upper particles, not only levels 1–3. For example P = V⁴, E = V³, atom-1 = ep:
the bottom particle (V³) passes alone, yet levels 6, 7, 9, 10, 11 fail. So "levels 1–3 decide" is false; the
bottom particle is decided at levels 1–3 and the others are mixed into higher levels.

## What this means (scope a)

Under the molecule-only reading (option 2), whether the torus electron is admissible depends on the strand order
of the particles, which the model does not fix. Under the per-particle reading (option 1), only electrons that
pass alone survive, and then the verdict does not depend on order for every cell measured here. This is a
measurement in favour of option 1's consistency; it does not decide it. Which option holds is the owner's call.
