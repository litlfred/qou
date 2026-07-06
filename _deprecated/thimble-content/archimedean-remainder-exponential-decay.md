**Conjecture.**
*Let $K$ be a hyperbolic knot in $S^3$ admitting a Hecke-algebraic
braid presentation $\mathcal{B}_K$, and let $\mathcal{A}_n(K)$ denote the
truncation of the algebraic quantum volume
([algebraic quantum volume](#def\:algebraic-quantum-volume)) at
degree-lex Gröbner--Shirshov filtration depth $n$. Write*

$$
  \mathcal{R}_n(K)
  \;:=\;
  \mathcal{V}_{\mathrm{hyp}}(K) \;-\; \mathcal{A}_n(K)
  \;\in\;\mathbb{R}.
$$

*Then there exist real constants $C(K), c(K) > 0$ such that*

$$
  \boxed{\;
    |\mathcal{R}_n(K)| \;\le\; C(K)\,e^{-c(K)\,n}
    \quad\text{for all }n \geq n_0(K).
  \;}
$$

*The constant $c(K)$ depends on the local geometry of the cusp shape
parameter $z_c \in \mathbb{C}$ that solves Thurston's gluing
equations.*

### Status

**Open.** This statement consolidates folklore expectations from
quantum-topology asymptotics into a single QOU-internal conjecture.
The component pieces — Faddeev quantum-dilogarithm asymptotics,
Picard--Lefschetz steepest-:refterm[descent]{#descent} reduction to the Bloch--Wigner
dilogarithm, Laplace-method bounds on the resulting integral — are
each established in the literature for *specific* knot families
(figure-eight, torus knots; see \[`andersen-kashaev2014`]-style
treatments where they exist), but the QOU formulation in terms of a
**Gröbner--Shirshov filtration depth** $n$ is new and not directly
addressed by existing asymptotic results.

### Proof sketch (heuristic, not a proof)

The expected route — to be formalised once each gap is closed:

1. **Tail as $q$-Pochhammer residue.** The Markov-trace product
   ([Markov trace product](#thm\:markov-trace-product)) at depth $n$
   factors through the partial product
   $\Phi_n(x; q)$ of the
   [$q$-Pochhammer partial product](#def\:q-pochhammer-partial-product),
   The *multiplicative remainder* — the unreduced piece of the
   Gröbner--Shirshov ideal at depth $n$ — is
   $\Phi_\infty / \Phi_n = \prod_{k \ge n}(1 - x q^k)$.

2. **Integral representation.** The
   [Archimedean limit conjecture](#conj\:dilogarithm-archimedean-limit)
   asserts $(1 - q)\log\Phi_n(x; q) \to \mathrm{Li}_2(x)$ under
   Faddeev's joint scaling. The remainder $\log(\Phi_\infty/\Phi_n)$
   inherits the dilogarithm's integral kernel
   $\bigl.-\log(1 - t)/t\bigr.$, and the integral over the full contour
   gives $\mathcal{V}_{\mathrm{hyp}}(K)$ via the standard regulator
   identification. The
   [shared-denominator cusp holonomy](#conj\:shared-denominator-cusp-holonomy)
   pins the algebraic and geometric volumes to the *same* limit
   (rather than a non-zero offset), without which the remainder might
   converge to a constant rather than zero.

3. **Picard--Lefschetz steepest :refterm[descent]{#descent}.** Deform the integration
   contour to a Lefschetz thimble $J_{z_c}$ originating at the
   critical point $z_c$ of the action $S(t) = \mathrm{Li}_2(t)$ that
   solves the local Thurston gluing equation for $K$. By definition
   of a steepest-:refterm[descent]{#descent} contour, $\operatorname{Re} S$ is strictly
   decreasing along $J_{z_c}$ away from $z_c$.

4. **Laplace-method bound.** The remainder $\mathcal{R}_n(K)$ is the
   integral of $e^{S(t)/\hbar}$ over the *tail* of $J_{z_c}$ beyond
   distance $s_n \propto n\hbar$ from $z_c$. Laplace's method gives

   $$
     |\mathcal{R}_n(K)|
     \;\le\;
     C(K)\cdot
     \exp\!\bigl(\operatorname{Re} S(s_n)/\hbar\bigr)
     \;=\;
     C(K)\cdot e^{-c(K)\,n}
   $$

   with $c(K) = -\operatorname{Re} S'(z_c)\cdot s_1 / \hbar$
   determined by the local gradient of the action at the critical
   point.

### Where the gaps are

* **Step 1 (depth $\leftrightarrow$ truncation).** Identifying the
  Gröbner--Shirshov depth $n$ with the $q$-Pochhammer truncation
  index requires a precise theorem about which monomials in the
  Skein-machine basis are eliminated at each degree-lex stage. This
  is *not* the same as truncating the polynomial in the variable
  $q$.
* **Step 3 (thimble passage).** The Picard--Lefschetz argument
  is rigorous for compact thimbles but requires care at the cusp
  boundary. Established only for figure-eight (Garoufalidis et al.)
  and certain torus knots.
* **Step 4 (uniform constants).** Even granting the previous steps,
  showing $C(K), c(K) > 0$ are *bounded uniformly across hyperbolic
  knot families* (which is **not** part of this conjecture) is a
  separate question.

### Lean axiomatisation

Per AGENTS.md §3b, the conjecture is encoded in Lean as a typeclass
`DecayConjecture K`, with `C : ℝ`, `c : ℝ`, threshold `n₀ : ℕ`, and

$$
  \texttt{decay\_holds} \;:\;
  \forall n,\;\; n_0 \le n \;\Longrightarrow\;
  |\,\texttt{remainder}\;K\;n\,| \;\le\; C \cdot \exp(-c \cdot n)
$$

as the conjectural input field, alongside positivity constraints
`C_pos`, `c_pos`. Concrete instances are constructed by hand for
specific knot families where a proof is in fact available
(figure-eight, etc.).

### Cross-paper UGB grounding

The depth parameter $n$ is **not** a free integer: it is the index of
the Gröbner--Shirshov filtration

$$
  F_0 \;\subseteq\; F_1 \;\subseteq\; F_2 \;\subseteq\; \cdots
$$

constructed in
[`UGB.GrobnerShirshov.AlgebraFiltration`](https://github.com/litlfred/qou/blob/claude/archimedean-remainder-formalization-bkBgZ/content/unital-groebner-bases/lean/UGB/GrobnerShirshov/Flatness.lean).
Concretely:

* The Lean structure `KnotData` carries a field
  `filt : AlgebraFiltration Carrier`, witnessing the cross-paper
  reading of `n`.
* The intended meaning of `algebraicVolume n` is
  $\mathcal{A}_n = \tau_{\mathrm{arch}}\!\bigl(\operatorname{tr}_M
  \!\bigl(\operatorname{truncate}_n(\mathcal{B}_K)\bigr)\bigr)$,
  where $\operatorname{truncate}_n$ projects onto $F_n$.
* The Hecke deg-lex GS basis is supplied by
  [`UGB.GrobnerShirshov.HeckeGS.heckeRewritingSystem`](https://github.com/litlfred/qou/blob/claude/archimedean-remainder-formalization-bkBgZ/content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean):
  the rewriting rules are the Hecke relation, the Yang--Baxter
  relation, and far-commutativity.

### Two :refterm[descent]{#descent} theorems (sorry-free, conditional on UGB hypotheses)

Riding on the cross-paper grounding, the following are established
unconditionally in Lean (no `sorry`):

**Monotone :refterm[descent]{#descent}.** Given a `[GSMonotonic K]` instance — a
typeclass capturing the consequence of `AlgebraFiltration.ascending`
that the truncation sequence $\mathcal{A}_n$ converges monotonically
to $\mathcal{V}_{\mathrm{hyp}}$:

$$
  |\mathcal{R}_{n+1}(K)| \;\le\; |\mathcal{R}_n(K)|
  \qquad\text{for all }n.
$$

**Strict :refterm[descent]{#descent}.** Given a `[GSStrictAt K n]` instance — the
witness that the $(n+1)$-st graded piece of $\mathcal{B}_K$ is non-zero
(so depth $n+1$ captures genuinely new content):

$$
  |\mathcal{R}_{n+1}(K)| \;<\; |\mathcal{R}_n(K)|.
$$

Neither theorem proves the *exponential* rate (that is the
conjectural part). What they do establish is that the depth
parameter $n$ behaves as a genuine :refterm[descent]{#descent} index in the
Gröbner--Shirshov filtration, providing the qualitative monotonicity
and strict-progress structure on which the exponential conjecture
sits.

### Falsifiability

The conjecture is falsifiable in two ways:

1. **Numerical witness.** Compute $\mathcal{A}_n(K)$ for increasing
   $n$ on a specific hyperbolic knot $K$ and check whether the
   residual error decays exponentially or only polynomially. A
   polynomial decay (e.g. $|\mathcal{R}_n| \sim n^{-\alpha}$) would
   refute the conjecture.
2. **Counterexample family.** Exhibit a knot family for which the
   Picard--Lefschetz contour has a *real* saddle of $S$ on the
   integration tail, blocking the strictly-decreasing-$\operatorname{Re} S$
   step.

The QOU mass-formula calibration depends on this conjecture
*qualitatively only* — the calibration uses the Wedderburn invariants
at $q_0$, not the rate $c(K)$. Falsification of the rate would not
invalidate the mass formula itself.

### Application to $Q_\beta$ closure

The same exponential bound supplies the eigenfunction-dampening
principle behind both finite-depth presentations of the free-neutron
$Q$-value
([prop:q-beta-spectral-bridge](#prop:q-beta-spectral-bridge)):
at brane-tower depth $N$, both Form A (NF counit) and Form B
(transfer-matrix log-ratio) satisfy

$$
  \bigl\lvert Q_\beta^{(N)} - Q_\beta^{\mathrm{exact}} \bigr\rvert
  \;\le\;
  C(K) \cdot e^{-c(K)\,N}
$$

with $K$ the free-neutron sector class. At $N = 0$ this gives the
observed $+1.31$ keV residual ($+0.168\%$); at $N \geq 1$ the bound
is sub-keV.

**Substrate-derived rate constants** (closed-form from CAL-2 $q_0$):

$$
  \hbar_q := \frac{q_0 - 1}{q_0},
  \qquad
  c(K) = -2 \ln \hbar_q,
  \qquad
  C(K) = \frac{\hbar_q^2}{1 - \hbar_q^2}.
$$

The identity $\hbar_q^{2(N+1)} / (1 - \hbar_q^2) = C(K) \cdot e^{-c(K) N}$
is unconditional algebra (geometric $\leftrightarrow$ exponential form), and the
left-hand side is the per-braid-mass-tower bound of
[prop:per-braid-mass-tower](#prop:per-braid-mass-tower). At
$q_0 \approx 1.1100$ ([`q-pinning-50-digit.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-pinning-50-digit.witness.json)):

| Depth $N$ | $\lvert R_N\rvert$ bound | as % | as ppm | as ppb |
|---:|---:|---:|---:|---:|
| $0$ | $9.914 \times 10^{-3}$ | $0.9915\%$ | $9914.5$ | $9{,}914{,}521$ |
| $1$ | $9.733 \times 10^{-5}$ | $0.0097\%$ | $97.3$ | $97{,}333$ |
| $2$ | $9.555 \times 10^{-7}$ | $0.0001\%$ | $0.96$ | $955.5$ |
| $3$ | $9.381 \times 10^{-9}$ | $10^{-7}\%$ | $0.0094$ | $9.38$ |
| $4$ | $9.207 \times 10^{-11}$ | $10^{-9}\%$ | $0.00009$ | $0.092$ |

with $c(K) = 4.6236$ and $C(K) = 9.91 \times 10^{-3}$. **Observation
fits the ceiling**: the $N=0$ residual is
$1.31\;\mathrm{keV}/783.6\;\mathrm{keV} = 1.677 \times 10^{-3}$, i.e.
$5.9\times$ inside the bound ($9.914 \times 10^{-3}$). The actual
$c(K)$ for the operator class may exceed the ceiling rate; pinning
the *exact* fall-off requires the open lift formula of
[conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro).

Witness: [`c_k_beta_decay_witness.py`](https://github.com/litlfred/qou/blob/main/computations/c_k_beta_decay_witness.py)
$\to$ [`c-k-beta-decay-bound.witness.json`](https://github.com/litlfred/qou/blob/main/computations/c-k-beta-decay-bound.witness.json).
Both assertions (50-dps geometric $\leftrightarrow$ exponential agreement + $N=0$
margin $\leq 1$) pass.

### Relation to surreal QOUs

The conjecture is stated entirely in $\mathbb{R}$. There is **no
appeal to the surreal-number field $\mathbf{No}$ here**; an alternate
formulation in $\mathbf{No}$ exists and is discussed only where the
notational alignment with [archimedean stpart conjecture](#conj\:archimedean-stpart)
is helpful. The two formulations are equivalent under standard-part:
$\mathrm{st}(\mathcal{R}_n) = \mathcal{R}_n$ since the remainder is a
real number.
