Two mass formulas coexist in the QOU framework:

- The **single-vortex formula**
  ([mass endomorphism tower](#prop:mass-endomorphism-tower))
  applies to one vortex $\varrho$ with $n$ strands:
  $$
    \mathfrak{m}(\varrho) = \Bigl\lvert\prod_{i=0}^{n-2}\hat{V}_i
    \Bigr\rvert + \sum_{i} \Phi_q(\lvert\hat{V}_i\rvert)
    + \sum_{i<j} z^2 \Phi_q(\lvert\hat{V}_i \hat{V}_j\rvert).
  $$
- The **3-channel log-form**
  ([tower binding energy](#prop:tower-binding-energy)) applies to
  a multi-nucleon atom:
  $$
    B(Z,N) = \sum_{\lambda \in \{\mathrm{sym},\mathrm{std},\mathrm{alt}\}}
    w_\lambda \cdot m_e \cdot \sum_{i=0}^{A-2}
    \ln\lvert\Phi_q(\hat{V}_i^\lambda)\rvert.
  $$

Their surface shapes differ: the first is a sum of $\Phi_q$-values,
the second a sum of $\ln|\Phi_q|$.  This proposition bridges them.

## Statement

**Proposition.**
*Under the Wedderburn projection of $H_n(q)$ onto the three
irreps $\mathrm{sym}, \mathrm{std}, \mathrm{alt}$ of $H_3(q)$ and
the log-separation approximation where higher-order products
$\hat{V}_i \hat{V}_j \hat{V}_k\ldots$ ascend to the next jet
level, the single-vortex mass formula reduces channel-by-channel
to the 3-channel log-form:*

$$
  \mathfrak{m}(\varrho) \big|_{\lambda}
  \;\asymp\;
  m_e \cdot \sum_{i=0}^{A-2}
  \ln\bigl\lvert\Phi_q(\hat{V}_i^\lambda)\bigr\rvert
  \quad \text{(up to jet-level corrections)}.
$$

*Summing over channels with Wedderburn weights $w_\lambda =
d_q(\lambda)^2 / [3]_q!$ yields the binding formula of
[tower binding energy](#prop:tower-binding-energy).*

## Proof sketch

**(1) Log of single-vortex formula.** Taking the logarithm of
the single-vortex mass:

$$
  \ln\mathfrak{m}
  \;=\;
  \ln\Bigl\lvert\prod_i \hat{V}_i\Bigr\rvert
    + \sum_i \ln\bigl\lvert 1 + \Phi_q(\hat{V}_i)
           / \lvert\prod \hat{V}\rvert \bigr\rvert + \ldots
$$

The descended term $\ln|\prod \hat{V}_i| = \sum_i \ln|\hat{V}_i|$
is already a sum over generators, linear in the per-generator
volumes.  In the $q \to 1$ limit each $\hat{V}_i \to 1$ and this
term vanishes.

**(2) Quantum dilogarithm in log form.** The Fadeev
$\Phi_q(v) = \prod_{k \geq 1} (1 - q^{-k} v)^{-1}$ has the
analytic-continuation identity
([quantum dilogarithm as localised torsion volume](#cor:quantum-dilogarithm)):

$$
  \ln\lvert\Phi_q(v)\rvert
  \;=\;
  -\sum_{k \geq 1} \ln\bigl\lvert 1 - q^{-k} v\bigr\rvert
  \;=\;
  \int_0^{\lvert v\rvert} \frac{\ln_q(1+t)}{t}\,dt.
$$

Under the Wedderburn projection of $\hat{V}_i$ onto irrep $\lambda$,
$\hat{V}_i^\lambda$ is a well-defined $q$-rational scalar
($\lambda \in \{\mathrm{sym}, \mathrm{std}, \mathrm{alt}\}$),
so $\ln|\Phi_q(\hat{V}_i^\lambda)|$ is finite for $|\hat{V}_i^\lambda|
< q$.

**(3) Pair terms ascend.** The single-vortex pair contribution
$z^2 \Phi_q(\hat{V}_i \hat{V}_j)$ has argument
$\hat{V}_i \hat{V}_j$, which under the channel projection becomes
$\hat{V}_i^\lambda \hat{V}_j^\lambda$ (per-channel product).  By the
pentagon identity of the quantum Bloch group
([quantum Bloch group](#def:quantum-bloch-group)), products of
traced volumes factorise modulo $\hbar_q$-corrections:

$$
  \Phi_q(\hat{V}_i \hat{V}_j)
  \;=\;
  \Phi_q(\hat{V}_i) \cdot \Phi_q(\hat{V}_j)
  \cdot R_{ij}(\hbar_q),
$$

where the **R-factor** $R_{ij}$ is $1 + O(\hbar_q^2)$ (leading
braid commutator term).  Taking logs:

$$
  z^2 \Phi_q(\hat{V}_i \hat{V}_j)
  \;\asymp\;
  z^2 [\Phi_q(\hat{V}_i) + \Phi_q(\hat{V}_j)]
  \cdot (1 + O(\hbar_q^2)).
$$

The $O(\hbar_q^2)$ residuals **ascend to the next jet level** via
the brane tower structure
([recursive brane tower](#def:recursive-brane-tower)), where the
$\hbar_q^{2n}$ damping absorbs them.  Hence at level $n$ the
explicit pair term does not contribute at that level's
$\ln|\Phi_q|$ sum.

**(4) Channel decomposition.** With pair terms ascended, the
per-level mass simplifies to
$\sum_i \ln|\Phi_q(\hat{V}_i)|$.  Decomposing $\hat{V}_i$ into
the three Wedderburn channels:

$$
  \hat{V}_i = w_{\mathrm{sym}} \hat{V}_i^{\mathrm{sym}}
            + w_{\mathrm{std}} \hat{V}_i^{\mathrm{std}}
            + w_{\mathrm{alt}} \hat{V}_i^{\mathrm{alt}},
$$

and noting $\ln|\Phi_q(a + b + c)| \asymp w_{\mathrm{sym}}
\ln|\Phi_q(a/w_{\mathrm{sym}})|$ etc. under the $R$-factorisation
(above), gives the per-channel form

$$
  \ln|\Phi_q(\hat{V}_i)|
  \;\asymp\;
  \sum_\lambda w_\lambda \cdot \ln|\Phi_q(\hat{V}_i^\lambda)|.
$$

Summing over $i$ and multiplying by the energy scale $m_e$
recovers the 3-channel log-form of
[tower binding energy](#prop:tower-binding-energy).  $\square$

## Caveats

- The pentagon-ascension step (3) is stated but not rigorously
  proved; it requires an explicit computation of the $R$-factor
  as an $\hbar_q^2$-bounded element of $\mathbf{A}$.
- The channel decomposition in (4) treats the Wedderburn weights
  as probability weights (summing to 1); this is correct at
  $q = 1$ and corrected at $q \neq 1$ by the $R$-factorisation.
- The reduction is **asymptotic** (denoted $\asymp$) not exact:
  the two formulas agree to leading order in $\hbar_q$ and
  differ by jet-level corrections bounded via
  [Kähler jet lift](#def:kahler-jet-lift).

## Numerical consistency

Empirical verification: full-tower-mass.py (which implements the
3-channel log-form) gives mean err $0.071\%$ across Z=1..20.
The single-vortex formula applied to a multi-nucleon atom
(via canonical_plus_multibrane.py, now deprecated) diverges due
to the $A-1$-wide $\prod \hat{V}$ term growing super-linearly
with $A$, as expected from the above reduction (the "ascend to
next jet level" step is required — naive direct evaluation
over-counts).

**Witness**: `full-tower-mass.witness.json` (3-channel log-form),
`canonical-plus-multibrane.witness.json` (single-vortex, with
brane-scaling fix).
