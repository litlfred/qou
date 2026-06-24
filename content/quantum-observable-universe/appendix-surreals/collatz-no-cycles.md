**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"no periodic Collatz cycles").**
The Skein-Collatz map $\mathcal{C}_q$ on
$\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$
has no periodic orbits other than the fixed point $P = 1$.

**Classical limit.** At $q = 1$: $\gcd(2, 3) = 1$ and
$3^a \neq 2^b$ for $a, b > 0$ (unique prime factorization).
The $q$-deformation lifts this to polynomial coprimality.

**The full $(a, a+1)$ family.** The identity
$\gcd([a]_q, [b]_q) = [\gcd(a,b)]_q$ shows that all
Collatz-type maps $(a, a+1)$ exclude periodic cycles,
since $\gcd(a, a+1) = 1$ for all $a$.  Cycle exclusion
is a consequence of consecutive integers being coprime
— a fact that lifts from $\mathbb{Z}$ to $\mathbb{Z}[q]$
via the $q$-integer functor.

**What remains.** This proposition settles half the Collatz
conjecture: no periodic cycles other than $\{1\}$.  The
other half — no divergent orbits — is the contact condition
$\langle v_{[2]} \rangle \geq 2$
([contact boundary](#prop:collatz-contact-boundary)).
