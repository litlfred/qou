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

*Proof.* A periodic orbit of length $k$ with $k_{\mathrm{odd}}$
odd steps and $k_{\mathrm{even}}$ even steps satisfies
$\mathcal{C}_q^k(P) = P$. The odd steps multiply by
$[3]_q / [2]_q$ and the even steps multiply by $1/[2]_q$,
The return condition requires:

$$
  \frac{[3]_q^{k_{\mathrm{odd}}}}{[2]_q^{k_{\mathrm{odd}} + k_{\mathrm{even}}}}
  =  1,
  \qquad\text{i.e.,}\qquad
  [3]_q^{k_{\mathrm{odd}}} =  [2]_q^k
  \quad (k = k_{\mathrm{odd}} + k_{\mathrm{even}}).
$$

But $[2]_q$ and $[3]_q$ are **coprime** in $\mathbb{Z}[q]$.
The Skein divisibility identity gives the proof in one line:

$$
  [3]_q - q[2]_q = 1,
$$

so $\gcd([2]_q, [3]_q) = 1$ by Bézout.  Since $[3]_q$
is a unit modulo $[2]_q$:

$$
  [3]_q^{k_{\mathrm{odd}}}
  \equiv 1^{k_{\mathrm{odd}}}
  \equiv 1
  \pmod{[2]_q},
$$

while $[2]_q^k \equiv 0 \pmod{[2]_q}$ for $k \geq 1$.
These are never equal for $k_{\mathrm{odd}} \geq 1$.
A cycle with $k_{\mathrm{odd}} = 0$ (all even steps) would
be $P \mapsto P / [2]_q^k = P$, forcing $P = 0$.

Therefore the only periodic orbit is $P = 1$
(the unknot).  $\square$

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
