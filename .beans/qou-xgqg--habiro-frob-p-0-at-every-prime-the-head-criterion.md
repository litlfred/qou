---
# qou-xgqg
title: 'Habiro Frob_p != 0 at every prime: the head criterion reduces to a divisibility of P; A closed form proved'
status: completed
type: task
priority: normal
created_at: 2026-08-28T19:33:34Z
updated_at: 2026-08-28T19:49:24Z
---

## RESULT — both scope limits of PR #5884 closed

#5884 landed `Frob_p != 0 at every prime` for the five on-disk atoms, with two
caveats: the `A` closed form was verified (mass 6) rather than proved, and the
p=3 closure read `a_2`, so it covered only atoms with Habiro data on disk.
Both are gone.

### 1. The head criterion was the long way round

`habiroEval_sub_head` gives `(z;z)_j | head_N - head_j` for `N >= j`, and past
the truncation `head_N` IS `P(zeta)`. So for every j

    (z;z)_j | head_j   <=>   (z;z)_j | P(zeta)

verified on 158 (atom, prime, j) cells, 0 disagreements. The criterion never
needed the Habiro coefficients — it is a statement about P. It is also
STRICTLY WEAKER than the question it is used to answer: it fires only when the
Pochhammer fails to divide P(zeta), while a nonzero value may divide perfectly
well. It earns its keep only when P is unknown; here P is a known polynomial.

### 2. So decide directly, and finitely

    P(zeta_2p) = 0  <=>  Phi_2p | P,   deg Phi_2p = p-1

so once `p-1 > deg P` it is impossible, and below that bound finitely many
primes settle EVERY prime by exact polynomial remainder. The same argument on
`denom` rules out a pole (undefined, not zero — a different failure that would
break the claim equally).

Measured: 65 cells, all (Z,N) with Z+N <= 10, degrees to 440, up to 79 primes
per cell. **Phi_2p divides P at NO prime in ANY cell.** No criterion, no a_2,
no truncation-depth caveat, and it reaches atoms with no Habiro data at all.

### 3. The A closed form is now PROVED

    A = n_p(-1)^Z * n_n(-1)^N * PROD_k n_k(-1) / G(-1)

with n_p(-1)=8, n_n(-1)=2 and per-kind 1 / 1 / 2 / 12 — six exact symbolic
constants. The census is READ FROM SOURCE: `canonical_interface_kinds` builds
`['p']*Z + ['n']*N` and walks adjacent pairs, so exactly one p->n transition
iff Z>=1 and N>=1. positive and negative contribute 1, so the product collapses
to 8^Z * 2^N * 12^[mixed].

`G(-1) = 1` is derived, in three exact steps:

  A. every denominator is const * u^i * (u^4+1)^j  (six, factored);
  B. every numerator is coprime to u^4+1  (6/6);
  C. everything lies in Z[u^2], since tr_M is a rational function of q = u^2
     (6/6) — so every exponent is even.

A and B force G to be a monomial u^k; C forces k even; a monomial of even
degree is +1 at u = -1. Hence G(-1) = 1 and

    A(Z,N) = 2^(3Z+N) * 12^[Z>=1 and N>=1]

is proved, resting only on exact evaluation of fixed expressions and a
combinatorial fact about adjacent pairs. The 65-cell grid is a consistency
check on the proof, not the evidence for it.

### 4. The 3 is convention-specific, not a property of the trace

`averaged` contributes n_k(-1) = 2, not 12. Under `strict_averaged` there
would be NO factor of 3 anywhere and the j=2 criterion would fire at every odd
prime without exception. The 3 is a fingerprint of the canonical
`bring_color_weighted` convention (owner ruling R3) reaching A through delta's
denominator.

### Slips caught in my own scratch work

A throwaway script printed a canned conclusion, "deg G = 0 everywhere => no
cancellation at all", which the table directly above it contradicted:
deg G in {0, 6, 12, 18}. G is a monomial, not a constant. Never committed, but
worth recording — the pre-written conclusion was the failure mode, not the
data. Separately the probe's section 4 kept a line calling G(-1)=1 "the ONE
step not proved" after section 5 derived it; fixed before commit.


## The mass bound is gone too — the whole question is SIX polynomials

I closed the previous entry saying the remaining gap was uniformity in mass:
each (Z,N) proved individually by exhaustive finite check, but "no Phi_2p ever
divides P at any mass" verified to 10 rather than proved. That gap closes
completely, and the argument is short:

  - P = NUM / G with G a monomial u^k (proved above);
  - NUM = n_p^Z * n_n^N * PROD_k n_k — powers of SIX FIXED polynomials,
    independent of (Z,N);
  - Phi_2p is IRREDUCIBLE over Q, and Phi_2p(0) != 0, so it cannot divide u^k;
  - Q[u] is a UFD, so Phi_2p | NUM iff Phi_2p divides one of the six.

So a single finite check on six fixed polynomials settles EVERY atom at EVERY
prime. Measured — none of the six is divisible by any Phi_2p, and the check is
finite by degree:

    tau_p              deg 44   p <= 45   14 primes   none
    tau_n              deg 36   p <= 37   12 primes   none
    positive           deg  6   p <=  7    4 primes   none
    negative           deg  0   p <=  1    0 primes   none
    averaged           deg  8   p <=  9    4 primes   none
    averaged_weighted  deg 20   p <= 21    8 primes   none

Largest degree 44, so p > 45 is impossible by degree.

    Frob_p != 0 for every (Z,N), at every prime, with NO mass bound.

**The 65-cell grid was overkill and I should say so.** The answer never
depended on mass — it was always six polynomials. The grid is kept because it
also exercises the closed form, but it is corroboration, not the evidence for
uniform non-vanishing. Three escalating sweeps (27, 44, 65 cells, the last
~6 min) were spent on a question a degree-44 factorisation answers outright;
the reduction was available from the start and I did not look for it until the
sweep had already succeeded.
