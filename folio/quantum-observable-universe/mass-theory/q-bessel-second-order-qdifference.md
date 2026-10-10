**Proof.** Throughout, $q$ and the order $\nu$ are formal parameters in a field; the argument is purely $q$-difference-algebraic. Write $(x;q)_k = \prod_{j=0}^{k-1}\bigl(1 - x q^{j}\bigr)$ for the $q$-Pochhammer symbol, and let

$$
g(w) \;=\; \sum_{k \ge 0} c_k\, w^{k},
\qquad
c_k \;=\; \frac{(-1)^k\, q^{k(k-1)/2}}{(q;q)_k\,\bigl(q^{\nu+1};q\bigr)_k},
$$

be the generating function of the Hahn–Exton $q$-Bessel coefficients of order $\nu$. By the [contiguity recurrence](#prf:q-bessel-c-k-recurrence-cfinite), the coefficients satisfy the first-order relation

$$
c_k\,\bigl(1 - q^{k}\bigr)\bigl(1 - q^{\nu+k}\bigr) \;=\; -\,q^{k-1}\, c_{k-1},
\qquad k \ge 1. \qquad (\star)
$$

**Step 1 — assemble the three $q$-shifts.** The $q$-shifted series are $g(qw) = \sum_{k} c_k\, q^{k} w^{k}$ and $g(q^2 w) = \sum_{k} c_k\, q^{2k} w^{k}$. Hence

$$
q^{\nu}\, g(q^2 w) - \bigl(1 + q^{\nu}\bigr)\, g(q w) + g(w)
\;=\; \sum_{k \ge 0} c_k \Bigl( q^{\nu+2k} - \bigl(1 + q^{\nu}\bigr) q^{k} + 1 \Bigr) w^{k},
$$

and the bracket factors,

$$
q^{\nu+2k} - \bigl(1 + q^{\nu}\bigr) q^{k} + 1
\;=\; \bigl(1 - q^{k}\bigr)\bigl(1 - q^{\nu+k}\bigr),
$$

as one checks by expanding the right-hand side. This factorisation into the $(\star)$ denominator is the reason the second-order operator collapses onto the first-order recurrence.

**Step 2 — the source term.** Re-indexing a single $q$-shift multiplied by $w$,

$$
w\, g(q w) \;=\; \sum_{k \ge 0} c_k\, q^{k} w^{k+1} \;=\; \sum_{k \ge 1} c_{k-1}\, q^{k-1} w^{k}.
$$

**Step 3 — coefficient comparison.** Combining Steps 1 and 2, the $w^{k}$ coefficient of

$$
q^{\nu}\, g(q^2 w) - \bigl(1 + q^{\nu} - w\bigr)\, g(q w) + g(w)
$$

is $c_0 \bigl(1 - q^{0}\bigr)\bigl(1 - q^{\nu}\bigr) = 0$ for $k = 0$, and

$$
c_k\,\bigl(1 - q^{k}\bigr)\bigl(1 - q^{\nu+k}\bigr) + q^{k-1}\, c_{k-1}
$$

for $k \ge 1$. By $(\star)$ every coefficient vanishes, so the generating function satisfies the second-order $q$-difference equation

$$
q^{\nu}\, g(q^2 w) \;-\; \bigl(1 + q^{\nu} - w\bigr)\, g(q w) \;+\; g(w) \;=\; 0.
\qquad (\star\star)
$$

Writing $\eta$ for the $q$-shift operator $(\eta f)(w) = f(qw)$, equation $(\star\star)$ reads $\bigl[\,q^{\nu}\eta^{2} - \bigl(1 + q^{\nu} - w\bigr)\eta + 1\,\bigr] g = 0$: a genuine second-order (three-point: $w$, $qw$, $q^2 w$) $q$-difference operator, whose linear term $+w$ in the middle coefficient is the source making the coefficient ladder descend.

**Step 4 — equivalence of $(\star\star)$ and $(\star)$.** The computation in Steps 1–3 is reversible: $(\star\star)$ holds if and only if every $w^{k}$ coefficient vanishes, and for $k \ge 1$ that vanishing is exactly $(\star)$. The "second order" refers to the $q$-difference order (three $q$-shifted arguments); on the coefficients the equation collapses to a two-term relation between consecutive $c_k$, precisely because the middle coefficient factors through the $(\star)$ denominator as in Step 1. Equivalently, shifting the index to $k+1$, the coefficient relation is

$$
\Bigl( q^{\nu+2k+2} - q^{k+1} - q^{\nu+k+1} + 1 \Bigr) c_{k+1} + q^{k}\, c_k = 0,
\qquad
q^{\nu+2k+2} - q^{k+1} - q^{\nu+k+1} + 1 = \bigl(1 - q^{k+1}\bigr)\bigl(1 - q^{\nu+k+1}\bigr).
$$

**Step 5 — classical contraction.** In the limit $q \to 1^{-}$ the rescaled operator contracts to the ordinary Bessel operator $w\, g'' + (\nu + 1)\, g' + g$ acting on $g(w)$: the denominators degenerate as $1 - q^{k} \sim k\,(1-q)$ and $1 - q^{\nu+k} \sim (\nu+k)(1-q)$, so the rescaled coefficient ratio satisfies $\lim_{q \to 1^{-}} (1-q)^{2}\, c_k / c_{k-1} = -1/\bigl(k(\nu+k)\bigr)$, the coefficient recurrence of the classical Bessel series $\sum_{k} (-1)^k z^k / \bigl(k!\, (\nu+1)_k\bigr)$ in a formal variable $z$, where $(\nu+1)_k$ is the ordinary Pochhammer symbol. $\blacksquare$

This is a fibre-level structural result: $q$ and $\nu$ are formal parameters, and no substrate evaluation is involved.
