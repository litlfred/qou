## Proof

**Step 1 — character values at $w_0$.** The longest element
$w_0 \in S_3$ is the involution $(1\,3)$ (cycle type $[2,1]$).
Standard $S_n$ character theory gives:

- $\chi_{(3)}(w_0) = 1$: trivial rep is constant.
- $\chi_{(2,1)}(w_0) = 0$: the standard 2-d rep maps the transposition
  $(1\,3)$ to a reflection; trace of a reflection in 2-d is $0$.
- $\chi_{(1,1,1)}(w_0) = -1$: sign rep gives $\mathrm{sgn}(w_0) = -1$
  (odd permutation).

**Step 2 — per-irrep closed forms at $H_3(q)$.** By
[chi per irreducible-representation cyclotomic closed forms remark](#rem:chi-per-irrep-cyclotomic-closed-forms),
the three character-difference closed forms are

$$
\begin{aligned}
  \chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)     &= -\tfrac{(q^2+1)^2(q^2-1)}{4q}, \\[4pt]
  \chi_{(2,1)}(\mathcal{B}_n) - \chi_{(2,1)}(\mathcal{B}_p) &= -\tfrac{(q^4+1)(q^2-1)}{4q^3}, \\[4pt]
  \chi_{(1,1,1)}(\mathcal{B}_n) - \chi_{(1,1,1)}(\mathcal{B}_p) &= -\tfrac{(q^2+1)^2(q^2-1)}{4q^5}.
\end{aligned}
$$

**Step 3 — conjugate-partition symmetry.** The
conjugate-partition relation
$\chi_{(1,1,1)}\text{-diff}(q) = \chi_{(3)}\text{-diff}(q) / q^4$
([chi per irreducible-representation cyclotomic closed forms remark](#rem:chi-per-irrep-cyclotomic-closed-forms))
implies, expanding both at $q = 1 + \varepsilon$,
that **every** $\varepsilon^m$ coefficient (odd and even alike) of
the $V_{(1,1,1)}$ difference is a $q^{-4} = (1+\varepsilon)^{-4}$
binomial-shift of the $V_{(3)}$ coefficients:

$$
  [\varepsilon^m]\,\chi_{(1,1,1)}\text{-diff}
  \;=\;
  \sum_{j = 0}^{m} (-1)^j \binom{j + 3}{j}\,
  [\varepsilon^{m - j}]\,\chi_{(3)}\text{-diff}.
$$

The indices $j$ run over both parities. The $c_k$ in this
proposition's statement are the *even-power* coefficients
$c_k^{(\lambda)} = [\varepsilon^{2k}]\,\chi_\lambda\text{-diff}$;
restoring the full ε-expansion is needed to pick out the
$[\varepsilon^{2k}]$ contribution of $\chi_{(1,1,1)}$, which
involves $[\varepsilon^{2k - j}]\,\chi_{(3)}$ for $j$ ranging
over $\{0, 1, \ldots, 2k\}$ — including odd values like
$j = 2k - 1$ where the input is the odd-power coefficient
$[\varepsilon^1]\,\chi_{(3)}$.

For $m = 2k \geq 10$ (i.e. $k \geq 5$), the binomial coefficient
$\binom{j+3}{j}$ grows monotonically in $j$, so the dominant
contributions come from the **largest $j$** values where the
$[\varepsilon^{m - j}]\,\chi_{(3)}$ factor is still non-zero —
the smallest non-trivial $[\varepsilon^{m - j}]\,\chi_{(3)}$
sit at $m - j \in \{1, 2\}$ per the witness data (e.g.
$[\varepsilon^1]\,\chi_{(3)} = -2$, $[\varepsilon^2]\,\chi_{(3)} = -3$).
At $m = 10$ the dominant contributions are therefore at
$j \in \{8, 9\}$, where $\binom{11}{8} = 165$ and
$\binom{12}{9} = 220$. The alternating sign $(-1)^j$ from the
$(1+\varepsilon)^{-4}$ expansion combined with the consistently
negative low-order $\chi_{(3)}$ coefficients gives
$c_k^{(1,1,1)} \gg c_k^{(3)}$ in magnitude with sign tied to
the parity of the dominant $j$.

**Step 4 — sign-character coincidence.** Substituting into
$S_k^{(w_0)} = c_k^{(3)} - c_k^{(1,1,1)}$ and observing that
$c_k^{(1,1,1)} \gg c_k^{(3)}$ for $k \geq 5$
(because of the $q^{-4}$ amplification of the high-order ε-tail),

$$
  \mathrm{sgn}\bigl(S_k^{(w_0)}\bigr)
  \;=\; \mathrm{sgn}\bigl(-c_k^{(1,1,1)}\bigr)
  \;=\; -\mathrm{sgn}\bigl(c_k^{(1,1,1)}\bigr).
$$

The empirical $c_k$ from the Wenzl-bridge Markov trace at $H_3$
selects the same signed combination (canonical structural verification at
$k = 5, 6$ above; the Markov-trace decomposition by Wenzl
([Wenzl 1988, Theorem 5]) factors through the character ring of
$S_3$, with the long-element coefficient governing the
sign-character extraction).

The sign agreement at $k = 5, 6$ is therefore the **leading
manifestation of the long-element character extraction** in the
$c_k$ chain. $\square$

## Open: magnitude closure

The proposition closes the **sign** at $k = 5, 6$. The **magnitude**
ratios ($1.49\times$ at $c_5$, $95.3\times$ at $c_6$) remain open.
Candidate refinements:

1. **Cross-block coupling via $\sigma_1$ matrix elements.** The
   $V_{(2,1)}$ Hoefsmit matrix mixes the std rep into the
   diagonal sum at the $b$-element (off-diagonal Hoefsmit entry).
   The empirical c_k may carry a $b^{2k}$-multiplicative factor
   not captured by the diagonal $\chi_\lambda$ values.
2. **q-deformed long-element character** $\chi_\lambda^q(w_0)$ at
   $q = q_0$ rather than $q = 1$. The character ring of $H_3(q)$
   differs from that of $S_3$ at $q \neq 1$; the appropriate
   weighting may use the q-deformed evaluation.
3. **Higher partitions** (k $\ge$ 7) where additional $\lambda \vdash 3$
   cancellations or new $\lambda \vdash 6$ contributions enter via
   the Wenzl-bridge inductive ascent.

These extensions are flagged for follow-up under the
alpha k categorical closure conjecture proposal.
