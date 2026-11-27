---
# qou-pc7n
title: 'Constructive: per-N positivity certificates for the volume conjecture in Q(zeta_N)+'
status: todo
type: task
priority: normal
tags:
    - constructive
    - volume-conjecture
created_at: 2026-11-27T17:40:00Z
updated_at: 2026-11-27T17:40:00Z
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
