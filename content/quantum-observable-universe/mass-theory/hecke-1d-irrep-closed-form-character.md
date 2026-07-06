**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — 1-dimensional Hecke irrep character, universal closed form).**

For any $n \geq 2$ and any typed braid $\beta \in B_n$ encoded as a
sequence of crossings of three types
$\{\sigma_i,\, \sigma_i^{-1},\, \sigma_i - h/2\cdot\mathbf{1}\}$
(the `operator-valued interface`
with $h = q - q^{-1}$), the $q$-character on each 1-dimensional
irreducible representation of $H_n(q)$ is given by the **universal
closed form**

$$
\boxed{
  \chi^{(n)}_q(\beta)
   \;=\;
   q^{w(\beta)} \cdot \bigl(\tfrac{[2]_q}{2}\bigr)^{m(\beta)}
  \qquad\text{and}\qquad
  \chi^{(1^n)}_q(\beta)
   \;=\;
   \bigl(-q^{-1}\bigr)^{w(\beta)} \cdot \bigl(-\tfrac{[2]_q}{2}\bigr)^{m(\beta)},
}
$$

where:

- $w(\beta) = \#(\sigma_i) - \#(\sigma_i^{-1})$ is the **writhe**
  (signed crossing count of the typed braid),
- $m(\beta)$ is the number of **averaged** (operator-valued
  $\sigma_i - h/2$) crossings,
- $[2]_q = q + q^{-1}$ is the standard quantum integer (so
  $[2]_q / 2 = (q + q^{-1})/2$ is the q-half-integer).

**The closed form is independent of $n$.** Only the choice of which
1-d irrep ($V_{(n)}$ trivial or $V_{(1^n)}$ sign) toggles the
sign of the eigenvalue $\lambda_\sigma \in \{+q,\, -q^{-1}\}$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
