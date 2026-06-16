**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation*

$$
\mathfrak{Q}_\beta(q) \;=\; Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q))
  \cdot \prod_{k \ge 2} \bigl(1 + c_k \cdot u_{\text{ladder}}^k\bigr),
\qquad u_{\text{ladder}} = b(q) \cdot \hbar_q^2,
$$

*the $k = 2$ coefficient is*

$$
c_2 \;=\; -1
$$

*as a structural identity over any commutative ring, independent of
the substrate value $q_0$ and of CODATA.*

## Proof (algebraic identity)

The operator-valued $N{=}2$ correction to $\mathfrak{Q}_\beta$ (per the brane-tower
truncation of [`probe_q_beta_operator_valued_N3.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/probe_q_beta_operator_valued_N3.py))
is the factor $(1 - b^2 \cdot \hbar_q^4)$. With $u_{\text{ladder}} = b \cdot \hbar_q^2$,
direct expansion gives

$$
1 - b^2 \cdot \hbar_q^4
\;=\; 1 - (b \cdot \hbar_q^2)^2
\;=\; 1 - u_{\text{ladder}}^2.
$$

This is a one-line `ring` identity in any commutative ring containing
$b$ and $\hbar_q$. Comparing to the ladder ansatz
$1 + c_2 \cdot u_{\text{ladder}}^2 + O(u_{\text{ladder}}^3)$ at order $u_{\text{ladder}}^2$
forces $c_2 = -1$. $\blacksquare$

## Why this is "structural", not "fit"

The earlier numerical observation $c_2 \approx -1$ (PR
[#1602](https://github.com/litlfred/qou/pull/1602), bar-even constraint)
was treated as an *empirical near-match*: a value extracted from the
SDP and compared to the proved bar-even prediction. The present
proposition strengthens that to a **structural identity**: $c_2$ is
not extracted from data, it is the coefficient of $u_{\text{ladder}}^2$ in the
exact algebraic factorisation of the categorical $N{=}2$ ladder
correction. No fit, no CODATA-$\mathfrak{Q}_\beta$ input, no $q_0$-evaluation
required — the identity holds in any commutative ring.

The corresponding sympy verification in
[`qbeta_symbolic_chain_alpha_b.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/qbeta/qbeta_symbolic_chain_alpha_b.py)
computes `sp.simplify((1 - b²·ℏ_q⁴) - (1 - u²))` and obtains
**exactly $0$**.

## Numerical impact at $q_0$

With $c_2 = -1$ structurally locked in, the partial ladder

$$
Q_{N=2}(q) \;=\; Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot (1 - b^2 \hbar_q^4)
$$

evaluated at the substrate $q_0 \approx 1.10998$ gives

$$
Q_{N=2}(q_0) \;\approx\; 0.78233441\;\text{MeV},
$$

within $5.6\,\text{ppm}$ of $\mathfrak{Q}_\beta^{\text{CODATA}} = 0.78233\;\text{MeV}$
with **zero CODATA-$\mathfrak{Q}_\beta$ input**. The remaining $\sim 6\,\text{ppm}$
is the categorical target for $c_3, c_4$ — see
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](q-beta-c-k-recursion-from-habiro-q-difference.md)
for the recursion framework.

## Implication for $c_3$, $c_4$

The same line of attack applies at higher $N$: if the categorical
$N{=}3$ correction is exactly $(1 + a \cdot u^3)$ for some explicit
$a$, then $c_3 = a$ structurally. The candidates
$\text{cos}(b \cdot \hbar_q^2)$, $\text{exp}(-\tfrac12 \sum b^k \hbar_q^{2k})$,
$1 - b^3 \hbar_q^6$, ... each predict a *different* $c_3$ by Taylor
expansion. Testing which candidate matches the empirical $c_3 \approx -2$
discriminates between brane-tower truncation schemes; if exactly one
candidate matches structurally, $c_3$ becomes a second structural
identity.

This proposition is the $k = 2$ instance of that programme. Higher-$k$
instances are the remaining open work toward CODATA-free $\mathfrak{Q}_\beta$ at
$1\,\text{ppQ}$.
