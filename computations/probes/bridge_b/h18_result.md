# H18 result: a model in which the wall weight is forced (2026-11-21)

Pre-registration: `h18_preregistration.md`. Script: `h18_forced_wall_weight_probe.py`; output: `h18_forced_wall_weight_probe.out.txt`. All arithmetic is exact over ℚ at v = 2.

## Outcome: passes at even n; inconclusive at odd n, so the weight-3 wall is not yet tested

The set-up check passes at every n = 4..7: J = F·P satisfies J² = 1 and J ρ(T̃_i) J = ρ(T̃_{n−i}).

**Even n (4, 6): the weight is forced.** For each orbit, the twisted power sums p_k = tr(J A_I^k) obey the weight-L recurrence for exactly one candidate pair, and only at the right L:

| orbit | ambient length | passing pair (a, b) |
|---|---|---|
| fixed middle root s_{n/2} | 1 | (v, −v⁻¹) only: Lusztig's sign |
| swapped pair s_i s_{n−i} | 2 | (v², +v⁻²) only |

Every wrong L fails. So in this model a folded generator's weight is read off the ambient operator, not chosen. That is the property H17's two-strand model lacked.

Under criterion 2, the swapped pairs pass with the sign +v⁻², not Lusztig's −v⁻² (§16.7(b)). This is the sign normalisation the pre-registration named: Lusztig's φ_x is normalised (§16.4), and plain J does not carry that normalisation. It is a sign convention, not a failure of the weight, and it is recorded as open.

**Odd n (5, 7): inconclusive.** At odd n every twisted power sum is exactly zero: p_k = 0 for all k and every orbit, and tr J = 0. Identically zero sums satisfy every recurrence, so the pre-registered criterion fails because the test is degenerate, not because the weight is wrong. The reason is structural. F reverses the total weight, and at odd n the total weight of (C²)^{⊗n} is never zero. So J maps every weight space to a different one, and the twisted trace of anything weight-preserving vanishes. This module has zero twisted character at odd n and cannot see the middle orbit.

So **the weight-3 wall is not tested by H18**, and it is not refuted either.

## What would test it

A module whose twisted character at odd n is not zero. The simplest is spin 1, (C³)^{⊗n}, where weight 0 occurs at every n. Another is a different realisation of ι that does not flip the spin. Either one needs its own pre-registration.

## Scope

Exact checks at the single value v = 2. Nothing here is a mass or is compared with experiment.
