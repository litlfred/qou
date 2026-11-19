## Proof

**Step 1: maximal crossings.** A perfect matching of $[2n]$ has at most
$\binom{n}{2}$ crossings, attained by
$M^\star = \{(i,\, n+i) : 1 \le i \le n\}$. For $i < j \le n$ the arcs
interleave, $i < j < n+i < n+j$, so all $\binom{n}{2}$ arc-pairs cross; and no
matching can exceed $\binom{n}{2}$ because that is the total number of arc-pairs.
(Confirmed by exhaustive enumeration for $n \le 6$: $\max_\pi \mathrm{cr}(\pi) =
\binom{n}{2}$, achieved by $M^\star$.)

**Step 2: super-exponential lower bound.** Each summand $q_0^{\mathrm{cr}(\pi)}$
is positive, so retaining only the $M^\star$ term,
$$
  T_n(q_0) \;\ge\; q_0^{\binom{n}{2}}
  \;=\; \exp\!\Big( \tfrac{n(n-1)}{2}\,\ln q_0 \Big)
  \;=\; \exp\!\big(\Theta(n^2)\big),
$$
since $\ln q_0 > 0$. The exponent is **quadratic** in $n$, so $T_n(q_0)$
outgrows $c^{\,n}$ for every constant $c$, giving super-exponential divergence. (The
exact values $T_n(q_0) = 3.11,\,16.7,\,131,\,1365,\,1.81\!\times\!10^4,\,
2.96\!\times\!10^5$ for $n=2,\dots,7$ confirm a ratio $T_n/T_{n-1}$ that *grows*
with $n$ rather than saturating, the signature of $\exp(\Theta(n^2))$.)

**Step 3: no $q$-Fock realisation.** By Bożejko–Speicher, the $q$-deformed
commutation relations $a_i a_j^{\dagger} - q\, a_j^{\dagger} a_i = \delta_{ij}$
admit a positive (Fock-space) representation **iff** $-1 \le q \le 1$. At
$q_0 > 1$ the associated Gram form fails to be positive semi-definite, so no
$q$-Gaussian state on the $q$-Fock space exists.

**Step 4: a measure still exists.** The moments $T_n$ are those of the
three-term recurrence $x\,p_k = p_{k+1} + [k]_{q}\, p_{k-1}$ with
$[k]_q = 1 + q + \cdots + q^{k-1}$ (the Touchard–Riordan expansion of the
$q$-Hermite moments). For $q_0 > 1$ every coefficient $[k]_{q_0}$ is positive, so
the Hankel determinants equal $\prod_{k=1}^{n-1}[k]_{q_0}^{\,n-k} > 0$ and, by
Favard's theorem, probability measures with moments $T_n(q_0)$ exist (for
example $\det H_3 = 1 + q_0 \approx 2.11$ and $\det H_4 \approx 14.88$). By
Step 2 none of them has a finite moment-generating function. The obstruction
is therefore to the Fock-space construction, not to the existence of a
measure. $\square$
