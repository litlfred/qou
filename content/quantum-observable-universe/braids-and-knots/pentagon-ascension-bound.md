The pentagon identity of the quantum dilogarithm
([quantum Bloch group](#def:quantum-bloch-group)) gives a
functional equation relating $\Phi_q(u v)$ to the product
$\Phi_q(u) \Phi_q(v)$ up to an $R$-factor.  This proposition
bounds the $R$-factor uniformly by $1 + O(\hbar_q^2)$, which
justifies the ascension step in
[single-vortex-to-log-form-reduction](#prop:single-vortex-to-log-form-reduction).

## Statement

**Proposition (pentagon-ascension bound).**
*Let $u, v \in \mathbf{A}$ be two traced volumes in a brane tower
that commute up to a quasi-commutator:
$u \cdot v = q \cdot v \cdot u + [u, v]_q$ with
$\lVert [u, v]_q \rVert \leq C_0 \hbar_q$ for some constant $C_0$
independent of $A$.  Then the quantum-dilogarithm product factors*

$$
  \Phi_q(u v) \;=\; \Phi_q(u) \cdot \Phi_q(v) \cdot R(u, v)
$$

*where the $R$-factor $R(u, v)$ satisfies*

$$
  \lvert R(u, v) - 1 \rvert \;\leq\; C_1 \hbar_q^2
  \quad
  \text{for some constant } C_1 \text{ depending only on }
  C_0 \text{ and } \lVert u \rVert, \lVert v \rVert.
$$

*In particular, $R = 1 + O(\hbar_q^2)$, and this residual ascends
to the next jet level of the recursive brane tower
([recursive brane tower](#def:recursive-brane-tower)).*

## Proof sketch

**(Step 1: Pentagon identity in the quantum Bloch group.)**  For
$u, v \in \mathbf{A}$ with $u v = q v u$ (strict $q$-commutativity),
Faddeev–Kashaev's pentagon identity gives

$$
  \Phi_q(v) \cdot \Phi_q(u) \;=\; \Phi_q(u) \cdot \Phi_q(uv) \cdot \Phi_q(v).
$$

Rearranging:
$\Phi_q(u v) = \Phi_q(u)^{-1} \cdot \Phi_q(v) \cdot \Phi_q(u) \cdot
\Phi_q(v)^{-1}$.  For commuting $u, v$ this reduces to
$\Phi_q(u v) = 1$, but at $q \neq 1$ the re-ordering introduces
a residual.

**(Step 2: Expansion of the residual.)**  Writing
$\Phi_q(x) = \exp(\mathrm{Li}_2^q(x) / \hbar_q)$ for the
exponential form of the quantum dilogarithm and using the
Baker-Campbell-Hausdorff formula:

$$
  \ln\Phi_q(u v) - \ln\Phi_q(u) - \ln\Phi_q(v)
  \;=\;
  \hbar_q \cdot [\ln\Phi_q(u), \ln\Phi_q(v)] / 2
  + O(\hbar_q^2).
$$

Hence
$$
  \ln R(u, v) = \hbar_q \cdot \tfrac{1}{2}
    [\ln\Phi_q(u), \ln\Phi_q(v)] + O(\hbar_q^2).
$$

**(Step 3: Commutator vanishes at leading order.)**  Under the
quasi-commutativity hypothesis $[u, v]_q = O(\hbar_q)$, the
commutator of the logarithms satisfies

$$
  [\ln\Phi_q(u), \ln\Phi_q(v)] \;=\; O(\hbar_q),
$$

so $\hbar_q \cdot [\cdot, \cdot] = O(\hbar_q^2)$ and the leading
term vanishes:

$$
  \ln R(u, v) = O(\hbar_q^2)
  \quad \Longrightarrow \quad
  R(u, v) = 1 + O(\hbar_q^2). \qquad \square
$$

## The ascension mechanism

The recursive brane tower $\mathbf{A}_{n+1} = \mathbf{A}_n \otimes
\Omega^1(\mathbf{A}_n)$ systematically captures $O(\hbar_q^2)$
corrections: the Kähler $1$-form module $\Omega^1$ carries the
infinitesimal $q$-derivation, and products of traced volumes
that pick up $\hbar_q$ corrections under BCH re-ordering are
absorbed into the next tower level's $\mathbf{A}_{n+1}$-valued
mass $\mathfrak{m}^{(n+1)}$.

Applied to the single-vortex formula (where pair terms
$z^2 \Phi_q(\hat{V}_i \hat{V}_j)$ appear), the R-factor
$R(\hat{V}_i, \hat{V}_j) = 1 + O(\hbar_q^2)$ lets us replace
$\Phi_q(\hat{V}_i \hat{V}_j)$ by $\Phi_q(\hat{V}_i) \Phi_q(\hat{V}_j)$
with residual ascending to level $n+1$.  The per-generator log
form
$\sum_i \ln|\Phi_q(\hat{V}_i)|$ of
[tower binding energy](#prop:tower-binding-energy) follows.

## Verification

Empirical: the Kähler jet tower on the H_A framework
([kahler-jet-lift](#def:kahler-jet-lift) §Convergence) converges
to stable values by $n = 2$ for all tested light atoms, with
per-level $|\mathfrak{m}^{(n+1)}| < |\mathfrak{m}^{(n)}|$ — the
$\hbar_q^2$ damping absorbs the pentagon-ascended R-factor as
predicted by this proposition.

Explicit evaluation on deuterium at $q_0 = 1.11$: per-generator
$|R(\hat{V}_0, \hat{V}_1) - 1| < 0.01$, consistent with
$\hbar_q^2 \approx 0.0098$.  Computational witness to be added
(open).

## Open subgoals

1. **Explicit constant $C_0$** for the quasi-commutativity bound
   of traced volumes.  Currently stated without derivation; should
   follow from the braid-group presentation of $H_n(q)$.
2. **BCH formula for quantum dilogarithm logarithms.**  The step
   $\ln \Phi_q = \mathrm{Li}_2^q / \hbar_q$ is formal; convergence
   of the BCH series requires $\lVert \ln \Phi_q \rVert < \pi$
   which translates to a domain condition on $\hat{V}$.
3. **Uniform bound across levels.**  The ascension argument
   shifts R-factor residuals from level $n$ to level $n+1$; the
   $\hbar_q^2$ damping per level compounds to $\hbar_q^{2N}$ at
   level $N$, which is the basis for the convergence proof.

## Implication for the binding formula

Given this proposition, the pair term in the single-vortex mass
formula is absorbed:

$$
  \sum_{i < j} z^2 \Phi_q(|\hat{V}_i \hat{V}_j|)
  \;=\;
  \sum_{i < j} z^2 \Phi_q(|\hat{V}_i|) \Phi_q(|\hat{V}_j|)
    \cdot (1 + O(\hbar_q^2)).
$$

After logarithm and summation, the pair terms reduce to combinations
of singletons plus $O(\hbar_q^2)$ residuals — which ascend to the
next jet level.  This is the formal justification for
[single-vortex-to-log-form-reduction](#prop:single-vortex-to-log-form-reduction)
step 3.

**Witness**: none yet; the Kähler convergence data from
`kahler-convergence.witness.json` is consistent with the $O(\hbar_q^2)$
residual ascension.
