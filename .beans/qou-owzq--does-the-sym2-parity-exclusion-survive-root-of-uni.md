---
# qou-owzq
title: Does the Sym2 parity exclusion survive root-of-unity truncation?
status: todo
type: task
priority: normal
created_at: 2026-08-25T16:45:18Z
updated_at: 2026-08-25T16:45:54Z
parent: qou-8lxd
---

Spun off from qou-60o2 (PR #5764), which proved: any object of the SINGLE-FIBRE
tensor category passing the Sym^2 gate has EVEN dimension, so no dim-3 object
passes, reducible or not. That result is stated for the CLASSICAL fusion data,
which Drinfeld-Jimbo preserves at GENERIC q (same fusion rules, same
orthogonal/symplectic type).

At a ROOT OF UNITY the category is truncated to the tilting/negligible quotient
and is a DIFFERENT category. Whether the parity argument survives there is NOT
settled by that file, and I did not attempt it.

WHY THIS MATTERS RATHER THAN BEING A PEDANTIC CAVEAT: root-of-unity truncation
is the eightfold chapter's OWN candidate mechanism — §8 item 5, 'Truncation
mechanism' (T4). So this is a live escape route from the exclusion, sitting
exactly where the chapter already suspects the answer might be. Naming it is the
difference between a scope-(b) exclusion honestly bounded and one quietly
over-stated.

WHAT WOULD SETTLE IT (not yet done, do not cite the following as evidence):
- In C(sl2, l) the simples V_0..V_{l-2} are still self-dual with FS type
  (-1)^{2j}, and V_j still has VECTOR-SPACE dimension 2j+1. If both survive
  truncation, the multiplicity count and hence the parity argument should carry
  over verbatim, and the exclusion extends. PLAUSIBLE, UNVERIFIED.
- The genuine subtlety is WHICH dimension the downstream arguments use. The
  Schur-Weyl row cap l(lambda) <= dim V uses the honest vector-space dimension;
  the Ocneanu relation dim_q V = [N]_q => z.[N]_q = q^N uses the QUANTUM
  dimension, and at a root of unity those come apart (quantum dimensions can
  vanish or go negative). An argument that silently swaps one for the other is
  exactly the arity/type conflation the da-arity-conflation criterion exists to
  catch.
- A NEGATIVE is equally valuable: if truncation genuinely admits a 3-dimensional
  gate-passing object, that is a live N=3 route and reopens the chapter's
  principal problem from a direction currently written off.

Scope discipline: nothing above is a result. It is a statement of what evidence
would look like.
