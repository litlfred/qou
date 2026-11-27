---
# qou-pc7n
title: 'Constructive: per-N positivity certificates for the volume conjecture in Q(zeta_N)+'
status: in-progress
type: task
priority: normal
tags:
    - constructive
    - volume-conjecture
created_at: 2026-11-27T17:40:00Z
updated_at: 2026-11-27T18:45:00Z
parent: qou-dk7p
---
Owner choice 2026-11-27 ("Both, quantale cut + certificates").

Goal: for each N, a lower bound on the Kashaev / colored-Jones value at
zeta = e^{2 pi i/N} from a Hermitian-square (sum-of-squares) certificate in
Q(zeta_N)+ on H_n(q) modulo the trace radical. Each certificate is finite
algebra; no analysis per N. Only the N -> infinity limit (the volume
conjecture proper) is a coev claim, stated on [Coev E] from
QOU/Core/LawvereCut.lean (PR #9487).

Caveats to carry:
- Jones unitarity holds only at zeta = e^{+-2 pi i/N}, not at Galois
  conjugates, so a certificate must be stated at that embedding (it is not
  Galois-invariant).
- 3_1 and 4_1 are both alternating (Khovanov-thin) and two-bridge
  (HOMFLY-thin), so thinness cannot separate them. A categorical
  (cone-tower / Isbell) cut stage must use something finer.

Later stage: the categorical Dedekind cut (Isbell/Lawvere profunctors,
Cone towers in D^b) once Mathlib support allows. Handed to the knot-volume
thread.

This bean tracks an open conjecture and must not be closed until the
mathematics closes.

## 2026-11-27 stage 1 (knot-volume thread, PR #9547)
4_1 done for every N: QOU/Core/KashaevHermitianCertificate.lean writes
<4_1>_N = sum_k star((q;q)_k)(q;q)_k (sum of norms Q(zeta_N) -> Q(zeta_N)^+),
gives each term as a nonnegative certificate in any star-ordered field, and
<4_1>_N >= 1 + N^2 at every primitive N-th root in C (total positivity).
No unitarity is used, so the embedding caveat does not bite for 4_1.
Open: sharper per-N bounds from the middle terms k ~ 5N/6; knots whose
state sum is not a sum of norms (8_18: c_1 < 0 at the Kashaev point, PR #9456);
the N -> infinity limit on [Coev E]. Bean stays open.

## 2026-11-27 stage 2 (knot-volume thread, PR #9568)

Reflection identity (q;q)_k * star((q;q)_{N-1-k}) = N at every primitive N-th
root with star q = q^-1 (algebraic form of sum_log_two_sin_reflect). Each pair of
Hermitian-square terms is 2N + a further Hermitian square, giving
<4_1>_N >= N^2 + (N-1)^2 in any star-ordered field of char 0 and at every
primitive root in C (QOU/Core/KashaevReflection.lean, sorry-free). Still
polynomial; exponential growth and the N -> infinity limit stay open, the latter
on [Coev E]. Non-norm knots (8_18) also open. Bean stays open.
