Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$
([quantum observable universe](#def:quantum-observable-universe)).
Let $\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$ denote
the non-perturbative quantum dilogarithm
([quantum Bloch group](#def:quantum-bloch-group)).  Let
$\hat{V}_i^{\mathrm{full}}$ denote the additive Wedderburn traced
volume at generator $i$
([three-invariant mass formula](#prop:atomic-braid-mass)).

**Proposition.**
*The mass of a vortex $\varrho$ with braid representative
$\beta \in B_n$ and $n - 1$ generators is*

$$
  \mathfrak{m}(\varrho)
  =
  \Bigl\lvert \prod_{i=0}^{n-2} \hat{V}_i^{\mathrm{full}} \Bigr\rvert
  +
  \sum_{i=0}^{n-2}
    \Phi_q\!\bigl(\lvert\hat{V}_i^{\mathrm{full}}\rvert\bigr)
  +
  \sum_{\substack{i < j \\ |i - j| = 1}}
    z^2 \cdot \Phi_q\!\bigl(\lvert\hat{V}_i^{\mathrm{full}}
      \cdot \hat{V}_j^{\mathrm{full}}\rvert\bigr),
$$

*where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter
([Jones--Markov trace](#thm:jones-markov-trace)).*

*The three sums correspond to the three types of blow-up centre
in the brane tower
([topological decomposition](#thm:topological-mass)):*

1. *The **descended term** $\lvert\prod \hat{V}_i\rvert$ is the
   base-level Markov trace
   ([categorical mass as Markov trace](#prop:categorical-mass-markov)).*
2. *Each **single-generator blow-up** at generator $i$ contributes
   $\Phi_q(\lvert\hat{V}_i\rvert)$.  (The Markov weight
   $\mathrm{tr}_M(\sigma_i) = z$ is already absorbed into the
   traced volume $\hat{V}_i$, which is computed via the Markov
   trace of the transfer chain.)*
3. *Each **adjacent-generator blow-up** at the product $\sigma_i\sigma_j$
   ($\lvert i - j\rvert = 1$) contributes
   $z^2 \cdot \Phi_q(\lvert\hat{V}_i \hat{V}_j\rvert)$, weighted by
   $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$.*

*Products $\sigma_i\sigma_j$ with $\lvert i - j\rvert \geq 2$ commute
(far-commutativity in $H_n(q)$) and do not generate independent
blow-up centres.  The element $\sigma_i\sigma_j\sigma_i$
($\lvert i - j\rvert = 1$) reduces via the Yang--Baxter relation
to $\sigma_j\sigma_i\sigma_j$ and does not contribute an independent
centre.*

*Proof.*
The Hecke mass element $\Phi_{\mathrm{mass}}(\beta) \in H_n(q)$
([Hecke mass element](#def:hecke-mass-element)) decomposes via the
descent involution into descended and transient contributions.  The
transient trace localises to blow-up centres $p$ in the brane tower
([topological decomposition](#thm:topological-mass)), each
contributing $\Phi_q(z_p)$ where $z_p$ is the spectral coordinate at
$p$ ([Briggs--Klein chart](#def:briggs-klein-chart)).

The NF basis of $H_n(q)$ decomposes by generator content.  For $n = 3$:

| Generator content | NF elements | Markov weight | Spectral coordinate |
|:-------------------|:-----------|:-------------|:-------------------|
| $\emptyset$ | $1$ | $1$ | $0$ |
| $\{0\}$ | $\sigma_0$ | $z$ | $\hat{V}_0$ |
| $\{1\}$ | $\sigma_1$ | $z$ | $\hat{V}_1$ |
| $\{0,1\}$, adjacent | $\sigma_0\sigma_1$, $\sigma_1\sigma_0$ | $z^2$ (combined) | $\hat{V}_0\hat{V}_1$ |
| $\{0,1,0\}$, dependent | $\sigma_0\sigma_1\sigma_0$ | — | reduces via YB |

The spectral coordinate $z_p$ at a blow-up centre $p$ corresponding
to NF element $w = \sigma_{i_1}\cdots\sigma_{i_k}$ is the product
$\hat{V}_{i_1}\cdots\hat{V}_{i_k}$.  The Markov weight is
$\mathrm{tr}_M(w) = z^{\ell(w)}$ for reduced words of length $\ell$.

The elements $\sigma_0\sigma_1$ and $\sigma_1\sigma_0$ have the same
generator content $\{0,1\}$ and the same spectral coordinate
$\hat{V}_0\hat{V}_1$; their combined weight is $2z^2$.  However,
$\sigma_1\sigma_0 = \sigma_0\sigma_1$ modulo the braid relation only
when $\lvert i - j\rvert \geq 2$; for adjacent generators they are
distinct NF elements.  The topological mass formula counts
**independent blow-up centres**, not NF elements.  Adjacent products
$\sigma_i\sigma_j$ and $\sigma_j\sigma_i$ share the same blow-up
centre (same support in the brane tower), so the combined weight
is $z^2$ (not $2z^2$).

The element $\sigma_0\sigma_1\sigma_0$ is not an independent blow-up
centre: it decomposes as $\sigma_1\sigma_0\sigma_1$ via the
Yang--Baxter relation, which is a rearrangement of the same transient
support.  Its contribution is already encoded in the descended term
and the single/adjacent blow-up centres.  $\square$

## Application to the proton--electron mass ratio

For the electron (trefoil $\sigma_1^3$ on $2$ strands,
$1$ generator, additive Wedderburn
$\hat{V}_e^{\mathrm{full}} \approx 0.594$):

$$
  \mathfrak{m}_e
  =
  \lvert\hat{V}_e\rvert
  + \Phi_q(\lvert\hat{V}_e\rvert).
$$

For the proton ($\mathcal{B}_3 \times \mathfrak{u}\mathfrak{u}\mathfrak{d}$
with gluon self-coupling on $3$ strands, $2$ generators,
$\hat{V}_0^{\mathrm{full}} \approx 0.989$,
$\hat{V}_1^{\mathrm{full}} \approx 0.971$):

$$
  \mathfrak{m}_{\mathfrak{p}}
  =
  \lvert\hat{V}_0\hat{V}_1\rvert
  + \Phi_q(\lvert\hat{V}_0\rvert)
  + \Phi_q(\lvert\hat{V}_1\rvert)
  + z^2 \cdot \Phi_q(\lvert\hat{V}_0\hat{V}_1\rvert).
$$

The proton's $11$ crossings (from the $4$-channel production vertex
$\gamma\gamma \to \mathfrak{q}\bar{\mathfrak{q}}$,
[photon channel chain](#rem:photon-channel-wedderburn-chain)) produce
spectral coordinates near $1$, where $\Phi_q$ diverges.  The
electron's $3$ crossings produce $\hat{V}_e \approx 0.594$, well
below the singularity.  The mass ratio is:

$$
  \frac{\mathfrak{m}_{\mathfrak{p}}}{\mathfrak{m}_e}
  \approx 1870
  \qquad (\text{CODATA: } 1836.15, \;\text{error } 1.8\%).
$$

No parameters are fitted.  The inputs are the substrate parameter
$q_0$ and the electron mass $m_e$ (energy scale).

**Witness**: `mass-endomorphism.witness.json`.
