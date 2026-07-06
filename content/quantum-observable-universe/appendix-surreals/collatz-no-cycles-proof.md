*Proof.* A periodic orbit of length $k$ with $k_{\mathrm{odd}}$ odd steps and $k_{\mathrm{even}}$ even steps satisfies $\mathcal{C}_q^k(P) = P$. The odd steps multiply by $[3]_q / [2]_q$ and the even steps multiply by $1/[2]_q$. The return condition requires:

$$
  \frac{[3]_q^{k_{\mathrm{odd}}}}{[2]_q^{k_{\mathrm{odd}} + k_{\mathrm{even}}}}
  =  1,
  \qquad\text{i.e.,}\qquad
  [3]_q^{k_{\mathrm{odd}}} =  [2]_q^k
  \quad (k = k_{\mathrm{odd}} + k_{\mathrm{even}}).
$$

But $[2]_q$ and $[3]_q$ are coprime in $\mathbb{Z}[q]$. The Skein divisibility identity establishes this in one line:

$$
  [3]_q - q[2]_q = 1.
$$

By Bézout's identity, $\gcd([2]_q, [3]_q) = 1$. Since $[3]_q$ is a unit modulo $[2]_q$:

$$
  [3]_q^{k_{\mathrm{odd}}}
  \equiv 1^{k_{\mathrm{odd}}}
  \equiv 1
  \pmod{[2]_q}.
$$

Conversely, $[2]_q^k \equiv 0 \pmod{[2]_q}$ for $k \geq 1$. These are never equal for $k_{\mathrm{odd}} \geq 1$. A cycle with $k_{\mathrm{odd}} = 0$ (all even steps) forces $P \mapsto P / [2]_q^k = P$, which requires $P = 0$. Therefore, the only periodic orbit is $P = 1$ (the unknot). $\qquad\blacksquare$

### Classical Limit

At $q = 1$, we have $\gcd(2, 3) = 1$ and $3^a \neq 2^b$ for $a, b > 0$ by unique prime factorization. The $q$-deformation lifts this integer coprimality directly to polynomial coprimality.

### The Full $(a, a+1)$ Family

The identity $\gcd([a]_q, [b]_q) = [\gcd(a,b)]_q$ implies that all Collatz-type maps $(a, a+1)$ exclude periodic cycles, because $\gcd(a, a+1) = 1$ for all $a$. Cycle exclusion is a consequence of consecutive integers being coprime. This fact lifts from $\mathbb{Z}$ to $\mathbb{Z}[q]$ via the $q$-integer functor.

### Remainder of the Collatz Conjecture

This proposition settles half of the Collatz conjecture: there are no periodic cycles other than $\{1\}$. The remaining half—the absence of divergent orbits—is exactly the contact condition $\langle v_{[2]} \rangle \geq 2$ ([contact boundary](#prop:collatz-contact-boundary)).
