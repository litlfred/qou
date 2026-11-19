**Proof.** Throughout, $q$ and the order $\nu$ are formal parameters in a field; no archimedean structure is used. Write $(x;q)_k = \prod_{j=0}^{k-1}\bigl(1 - x q^{j}\bigr)$ for the $q$-Pochhammer symbol, with $(x;q)_0 = 1$.

**Step 1 — the closed-form coefficients and their ratio.** The Hahn–Exton $q$-Bessel function of order $\nu$ has power-series coefficients

$$
c_k \;=\; \frac{(-1)^k\, q^{k(k-1)/2}}{(q;q)_k\,\bigl(q^{\nu+1};q\bigr)_k}, \qquad k \ge 0 .
$$

Compare consecutive coefficients. The sign contributes a factor $-1$; the Gaussian exponent contributes $q^{k(k+1)/2 - k(k-1)/2} = q^{k}$; and each $q$-Pochhammer symbol gains exactly one factor,

$$
\frac{(q;q)_{k+1}}{(q;q)_k} = 1 - q^{k+1},
\qquad
\frac{\bigl(q^{\nu+1};q\bigr)_{k+1}}{\bigl(q^{\nu+1};q\bigr)_k} = 1 - q^{\nu+k+1}.
$$

Multiplying out, the coefficients satisfy the first-order $q$-recurrence

$$
c_{k+1}\,\bigl(1 - q^{k+1}\bigr)\bigl(1 - q^{\nu+k+1}\bigr) \;=\; -\,q^{k}\, c_k
\qquad (\star)
$$

for all $k \ge 0$.

**Step 2 — first-order recurrences integrate to a product.** Conversely, $(\star)$ determines the sequence from its seed. Let $(r_k)_{k \ge 0}$ be any sequence of scalars and suppose a sequence $(c_k)$ satisfies $c_{k+1} = r_k\, c_k$ for all $k$. Then, by induction on $k$,

$$
c_k \;=\; c_0 \prod_{j=0}^{k-1} r_j ,
$$

the empty product being $1$ at $k = 0$ and the induction step reading $c_{k+1} = r_k\, c_k = c_0 \prod_{j=0}^{k} r_j$. For generic parameters the denominators $\bigl(1 - q^{k+1}\bigr)\bigl(1 - q^{\nu+k+1}\bigr)$ never vanish (vanishing requires $q$ a root of unity or $q^{\nu+1} \in q^{-\mathbb{N}}$), so $(\star)$ is of this form with ratio

$$
r_k \;=\; \frac{-\,q^{k}}{\bigl(1 - q^{k+1}\bigr)\bigl(1 - q^{\nu+k+1}\bigr)} ,
$$

and every solution of $(\star)$ is the $q$-hypergeometric product $c_k = c_0 \prod_{j=0}^{k-1} r_j$. In particular the closed form of Step 1 is the unique solution with $c_0 = 1$.

**Step 3 — $q$-holonomic, with C-finite as the degeneration.** The ratio $r_k$ depends on $k$ through $q^{k}$: the recurrence $(\star)$ is first-order linear with $q^{k}$-dependent coefficients, so the sequence $(c_k)$ is $q$-holonomic. A constant-coefficient (C-finite) recurrence arises exactly in the degenerate case of a $k$-independent ratio: if $c_{k+1} = \rho\, c_k$ for a single scalar $\rho$, the product of Step 2 collapses to the geometric sequence

$$
c_k = c_0\, \rho^{k},
$$

which is C-finite of order $1$ with characteristic root $\rho$. This degeneration occurs in the rational limit of the underlying $q$-difference kernel (in particular after the $q \to 1$ contraction, where the rescaled ratio $(1-q)^2\, c_{k+1}/c_k$ tends to $-1/\bigl((k+1)(\nu+k+1)\bigr)$, the coefficient ratio of the classical Bessel series), never for the genuine $q$-Bessel ratio $r_k$.

**Step 4 — consequence for the precision-ladder coefficients.** At the fibre level the ladder kernel is a $q$-Bessel object rather than a rational function; by Step 3 its coefficient sequence therefore admits no low-order constant-coefficient recurrence, while the dominant-root structure of the associated $q$-difference kernel survives. The canonical ladder values $c_2, \ldots, c_{10}$, expanded in the ladder variable $u \approx 0.00852$, exhibit exactly this pair of signatures: no constant-coefficient recurrence of order at most $4$ fits them, while the tail ratio approaches the reciprocal pole location, $c_{k+1}/c_k \to 1/u \approx 117.4$. $\blacksquare$

This argument supplies the fibre-level skeleton of the recursion only: the identification of the ladder with a $q$-Bessel coefficient sequence is a formal statement in $q$ and $\nu$, and the production $c_k$ ladder remains calibration-anchored.
