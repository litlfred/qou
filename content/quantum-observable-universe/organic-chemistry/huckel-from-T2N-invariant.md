**Conjecture.**
A neutral planar $N$-membered cyclopolyene is **aromatic** in the
Hückel sense if and only if the threading link $T(2, N)$ satisfies
both:

1. **Two-component condition** ([component count of $T(2,N)$](#lem:T2N-components)):
   $\gcd(2, N) = 2$, i.e. $N$ is even.
2. **Odd-weight condition**:
   $\Delta_{T(2,N)}(1) = N/2$ is odd.

Equivalently, $N \equiv 2 \pmod{4}$, recovering the standard
Hückel **$4n+2$** rule.

**Empirical agreement.**
For $N \in \{2, 3, 4, \ldots, 14\}$ this conjectural rule agrees
with the standard Hückel classification in **13 of 13** cases, as
verified in the witness `huckel-bridge.witness.json`:

- Aromatic ($N = 2, 6, 10, 14$): both rules agree (✓ benzene,
  ✓ naphthalene-class, ✓ anthracene-class).
- Non-aromatic ($N = 3, 5, 7, 9, 11, 13$): topological rule fails
  on the two-component condition; Hückel rule fails on $4n+2$.
- Anti-aromatic ($N = 4, 8, 12$): topological rule fails on the
  odd-weight condition; Hückel rule fails on $4n+2$.

**Caveat.**
The conjectural rule does **not** distinguish *non-aromatic* from
*anti-aromatic* (cyclobutadiene vs. cyclopentadiene), since both
fail aromaticity by different topological mechanisms.  An extension
of the conjecture that captures the destabilising character of
anti-aromatics likely involves the **signature** of $T(2,N)$ rather
than just the component count, and is left for future work.

**Strategy for proof.**
A first-principles derivation would proceed in two steps:

1. Show that the Hückel secular determinant for the $\pi$-MO system
   of a planar $N$-membered ring is the characteristic polynomial of
   the cyclic graph adjacency matrix $C_{N}$, whose spectrum is
   $\{\,2\cos(2\pi k / N) : k = 0, 1, \ldots, N-1\,\}$.
2. Show that the parity condition for $4n+2$ aromaticity coincides
   with the **two-component, odd-weight** condition on
   $\Delta_{T(2,N)}(1)$ via the substitution
   $q = e^{i\pi/N}$ in the Alexander polynomial.

Both steps are accessible to existing Hopf-algebraic techniques but
require a careful choice of basis on the symmetric tensor space.
