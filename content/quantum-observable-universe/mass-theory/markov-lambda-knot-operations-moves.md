The [Wedderburn $\lambda$-block decomposition of the Markov
chain](#rem:markov-lambda-knot-operations) splits the chain into
independent $\lambda$-sectors. The knot-theoretic operations on a
closed braid then sort cleanly into those that **fix** $\lambda$ and
the single one that **changes** it.

The operations are **Reidemeister moves** and the equivalent
**Markov moves** on braids.  Each has a determinate action on
$\lambda$:

| Operation | Algebraic form | Effect on $\lambda$ | Effect on the chain |
|:----------|:---------------|:-------------------|:--------------------|
| Braid relation (Reidemeister III) | $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ | **fixes** $\lambda$ | Yang--Baxter inside one $\rho^\lambda_q$ block |
| Hecke quadratic (Reidemeister II) | $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ | **fixes** $\lambda$ | Two-channel skein: symmetric $q$ / antisymmetric $-q^{-1}$ eigenspace in $V_\lambda$ |
| Markov I --- conjugation | $\beta \mapsto \alpha \beta \alpha^{-1}$, $\alpha,\beta \in B_n$ | **fixes** every $\chi^\lambda_q$ | Class-function property of the trace; trajectory distribution unchanged |
| **Markov II** --- stabilization | $\beta \in B_n \mapsto \beta \sigma_n^{\pm 1} \in B_{n+1}$ | $\lambda \vdash n \;\to\; \mu \vdash n{+}1,\ \mu = \lambda + \square$ | **Young-graph edge**; trace weight rescales by $z^{\pm 1}$ |
| Reidemeister I (framing) | $\beta \mapsto \beta \sigma_n^{\pm 1}$ with framing compensation | $\lambda \nearrow \mu$ same as Markov II | Absorbed into stabilization with framing factor |

The point is the sharp dichotomy: **only Markov II crosses
$\lambda$-sectors**, and it does so exactly along **box-addition
edges of the Young graph**

$$
  \lambda \nearrow \mu
  \quad\Longleftrightarrow\quad
  \mu \setminus \lambda = \{\square\}.
$$

All other knot operations act inside a single irrep block.

### Markov II as a transition on the Young lattice

Stabilization therefore is **not** a step of the
within-$\lambda$ SYT chain; it is a step of a **second,
coarser Markov chain on partitions**:

$$
  \cdots \;\longrightarrow\;
  \lambda \vdash n
  \;\xrightarrow{\;z^{\pm 1}\;}\;
  \mu \vdash n{+}1
  \;\longrightarrow\; \cdots,
  \qquad
  \mu \supset \lambda,\ |\mu| = |\lambda| + 1.
$$

The transition rate along edge $\lambda \nearrow \mu$ is
proportional to the Ocneanu trace weight ratio
$w_\mu(q)/w_\lambda(q)$; at generic $q$ this is the
**$q$-Plancherel measure** on the Young lattice, matching the
growth process familiar from the Robinson--Schensted--Knuth
correspondence and the asymmetric simple exclusion process
\cite{diaconis-ram2000}.
