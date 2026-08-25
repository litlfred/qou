---
# qou-owzq
title: Does the Sym2 parity exclusion survive root-of-unity truncation?
status: todo
type: task
priority: normal
created_at: 2026-08-25T16:45:18Z
updated_at: 2026-08-25T17:58:15Z
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

## Corpus check 2026-08-25 — the existing three-row results do NOT answer this

Relevant finding surfaced in the PR #5762 thread (the >=3-row stratum audit), and it
sharpens rather than closes this bean.

I had assumed the corpus's '>=3-row stratum is a structural zero under convention D'
result might already be the root-of-unity story, in which case this bean would be
partly answered. IT IS NOT. Quoting the measured finding there:

  wenzlWeight_eq_zero_iff carries hQ : forall k : Z, k != 0 -> Q^k != 1 — i.e. Q is
  explicitly GENERIC, NOT a root of unity. What vanishes is a Schur polynomial in r
  variables when l(lambda) > r, since schurPrincipal r Q mu = s_mu(1, Q, ..., Q^{r-1})
  has only r of them. So at q_0 nothing is truncated away: H_n(q) is semisimple, every
  lambda |- n is a block of it, each with NONZERO dim_q.

Two consequences for this bean:

1. The corpus's three-row vanishing is a GENERIC-q weight vanishing, in the same
   regime my Sym^2 parity result is stated for. So it is not evidence about the
   truncated category either way, and this bean cannot be closed by citing it.
2. It is a live worked example of the exact trap I flagged as the likely failure mode
   here: 'y_lambda = 0' (weight) and 'dim_q = 0' (quantum dimension) are DIFFERENT
   functions, and the sibling measured seven blocks at n = 6 with y_lambda = 0 and
   min dim_q = 1.0 — none zero. Conflating them changed a downstream sum by more
   than 2x (Sigma 1/dim_q = 3.202 over all eleven blocks vs 1.479 over the <=2-row
   ones). Anyone attacking this bean will meet the same vector-space-vs-quantum
   dimension distinction, and that measurement is the concrete warning.

So: still open, still generic-q-only, and now with a corpus-verified reason that the
nearby three-row results are not a substitute for doing it.
