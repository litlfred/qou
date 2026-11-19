<!-- Theorem (conditional on:
       def:delta-q-decoration,
       prop:force-carrier-intertwining-correspondence). -->

**Proposition (torus-knot $\alpha_{\mathrm{shift}}$).**
*Let $p \geq 1$, $k \geq 1$ with $\gcd(p, k) = 1$, and let
$T_{p,k}$ be the $(p, k)$-torus knot, presented as the closure
of the braid $\beta_{p,k} = (\sigma_1 \sigma_2 \cdots
\sigma_{p-1})^k \in B_p$. Define the **shift exponent***

$$
  \alpha_{\mathrm{shift}}(T_{p,k})
  \;:=\;
  \max_{\lambda \,\vdash\, p}\;
  \mathrm{ord}_{q=0}^{(-)}\; \chi_\lambda(\beta_{p,k})
$$

*where $\chi_\lambda$ is the seminormal Hecke character on
$V_\lambda$ ([delta q decoration definition](#def:delta-q-decoration))
and $\mathrm{ord}_{q=0}^{(-)}$ denotes the pole order at $q = 0$
(i.e. the negative of the Laurent valuation). Then:*

1. *The maximizer is the all-anti-symmetric channel $V_{(1^p)}$.*
2. *$\alpha_{\mathrm{shift}}(T_{p,k}) = k(p - 1)$.*
### Witness summary

The canonical evidence
([`alpha-shift-torus.witness.json`](../../../computations/alpha/alpha-shift-torus.witness.json))
records the full per-irrep symbolic $\chi_\lambda \in \mathbb{Q}(q)$
together with the pole order at $q = 0$ for every test pair, summarised
in
[Table: $\alpha_{\mathrm{shift}}(T_{p,k})$ for 6 test pairs](#tbl:alpha-shift-torus-knot-table-data).
All $14$ assertions in the witness pass.

### Cross-link

The two values $\alpha_{\mathrm{shift}}(T_{2,9}) = 9$ and
$\alpha_{\mathrm{shift}}(T_{3,5}) = 10$ are precisely the
$q$-integer indices appearing in
[electromagnetic coupling projection proposition](#prop:em-coupling-projection)'s
formula

$$
  \alpha_{EM}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q.
$$

[alpha electromagnetic shift multiplicative chain proposition](#prop:alpha-em-shift-multiplicative-chain)
combines the two identities into the **shift-exponent form**

$$
  \alpha_{EM}^{-1}
  \;=\;
  q \cdot
  \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q \cdot
  \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q,
$$

recasting the $\delta_q$-trace identity in the same combinatorial
terms as the atomic-shift formula.
