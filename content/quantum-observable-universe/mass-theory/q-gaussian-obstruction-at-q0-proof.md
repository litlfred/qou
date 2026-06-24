**Step 1 — maximal crossings.** A perfect matching of $[2n]$ has at most
$\binom{n}{2}$ crossings, attained by
$M^\star = \{(i,\, n+i) : 1 \le i \le n\}$. For $i < j \le n$ the arcs
interleave, $i < j < n+i < n+j$, so all $\binom{n}{2}$ arc-pairs cross; and no
matching can exceed $\binom{n}{2}$ because that is the total number of arc-pairs.
(Confirmed by exhaustive enumeration for $n \le 6$: $\max_\pi \mathrm{cr}(\pi) =
\binom{n}{2}$, achieved by $M^\star$.)

**Step 2 — super-exponential lower bound.** Each summand $q_0^{\mathrm{cr}(\pi)}$
is positive, so retaining only the $M^\star$ term,
$$
  T_n(q_0) \;\ge\; q_0^{\binom{n}{2}}
  \;=\; \exp\!\Big( \tfrac{n(n-1)}{2}\,\ln q_0 \Big)
  \;=\; \exp\!\big(\Theta(n^2)\big),
$$
since $\ln q_0 > 0$. The exponent is **quadratic** in $n$, so $T_n(q_0)$
outgrows $c^{\,n}$ for every constant $c$ — super-exponential divergence. (The
exact values $T_n(q_0) = 3.11,\,16.7,\,131,\,1365,\,1.81\!\times\!10^4,\,
2.96\!\times\!10^5$ for $n=2,\dots,7$ confirm a ratio $T_n/T_{n-1}$ that *grows*
with $n$ rather than saturating, the signature of $\exp(\Theta(n^2))$.)

**Step 3 — no probability measure.** By Bożejko–Speicher, the $q$-deformed
commutation relations $a_i a_j^{\dagger} - q\, a_j^{\dagger} a_i = \delta_{ij}$
admit a positive (Fock-space) representation **iff** $-1 \le q \le 1$. At
$q_0 > 1$ the associated Gram form fails to be positive semi-definite, so no
$q$-Gaussian state — hence no representing probability measure — exists; the
moment blow-up of Step 2 is the concrete witness ($T_n$ outgrows the moment
sequence of any measure with a finite analytic moment-generating function). $\square$
