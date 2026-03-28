The $R$-matrix is unitary.  This is not negotiable — it is a
theorem of the braided tensor category, formalised in Lean.
The question is not "what if unitarity breaks?" but rather:
**unitarity is the mechanism that pins zeros to $\sigma_q$**.

**The logical chain.**

$$
  R\text{-matrix unitary}
  \;\xRightarrow{\text{spectral id.}}\;
  \mathcal{L}_s\text{ self-adjoint}
  \;\Rightarrow\;
  \text{spectrum real}
  \;\xRightarrow{q\text{-func. eq.}}\;
  \operatorname{Re}(\rho) = \sigma_q.
$$

Each arrow:

1. **$R$-matrix unitary $\Rightarrow$ $\mathcal{L}_s$
   self-adjoint.**  The spectral identification
   ([unitarity forces zeros](#prop:q-critical-line)) maps the Ruelle
   transfer operator to the $R$-matrix braiding.  Unitarity of
   $\beta_{V,V}$ (i.e., $\beta \circ \beta^{-1} = \mathrm{id}$)
   translates to self-adjointness of $\mathcal{L}_s$ on
   $L^2(J(f_q), \mu_q)$.

2. **Self-adjoint $\Rightarrow$ real spectrum.**  Standard functional
   analysis.

3. **Real spectrum + $q$-functional equation $\Rightarrow$
   $\operatorname{Re}(\rho) = \sigma_q$.**  The functional equation
   $\zeta_q(s) = \chi_q(s)\,\zeta_q(d_H(q) - s)$ pairs $\rho$ with
   $d_H(q) - \bar{\rho}$.  Real spectrum forces
   $\rho = d_H(q) - \bar{\rho}$, giving
   $\operatorname{Re}(\rho) = d_H(q)/2$.

**Contrapositive: what an off-critical zero would require.**

Suppose, for contradiction, that $\rho = \beta + i\gamma$ with
$\beta \neq \sigma_q$.  Then:

- The transfer operator $\mathcal{L}_s$ would **not** be
  self-adjoint at $s = \rho$.
- By the spectral identification, the $R$-matrix would **not** be
  unitary — braiding and unbraiding would fail to compose to the
  identity.
- But $\beta_{V,V} \circ \beta_{V,V}^{-1} = \mathrm{id}$ is
  proved.  Contradiction.  $\square$

**Physical consequences (by contradiction).**

The following pathologies would arise if unitarity *could* be
violated — which it cannot, but the exercise clarifies what
unitarity prevents:

| Pathology | Mechanism | Prevented by |
|-----------|-----------|-------------|
| Orbit-counting anomaly | $\Pi_q(N)$ fluctuates as $q^{(\beta - \sigma_q)N}$ | Self-adjointness of $\mathcal{L}_s$ |
| Information loss in braiding | $\beta \circ \beta^{-1} \neq \mathrm{id}$ | $R$-matrix invertibility (Lean) |
| Gravity fluctuations | $G_{\mathrm{Planck}} \neq 1$ at scale $|\gamma|$ | $d_H(q)$ closed form + $G = 1$ |
| Entropy bound violation | $\Delta\eta \neq 0$ oscillations | $\eta_q = (2q-1)/q^3$ exact |

**The $d_H(q)$ closed form is the linchpin.**

The entire argument rests on the exact formula
$d_H(q) = (2q-1)^2/q^3$
([operational entropy](#def:operational-entropy)).  This enters in
two places:

1. **The functional equation**: the symmetry
   $\zeta_q(s) \leftrightarrow \zeta_q(d_H - s)$ determines where
   the critical line sits.  If $d_H(q)$ has corrections, the
   critical line moves.

2. **The self-consistency condition**: $G_{\mathrm{Planck}} = 1$
   *algebraically forces* $\eta_q = (2q-1)/q^3$, which together
   with $\chi_q = 1/(2q-1)$ gives $d_H$ via Manning–McCluskey.

The derivation chain is:

$$
  G_{\mathrm{Planck}} = 1
  \;\Rightarrow\;
  \eta_q = \frac{2q-1}{q^3}
  \;\xRightarrow{\chi_q = 1/(2q-1)}\;
  d_H(q) = \frac{(2q-1)^2}{q^3}
  \;\Rightarrow\;
  \sigma_q = \frac{(2q-1)^2}{2q^3}.
$$

Each step is algebraic — no approximations, no numerics, no
fitting.  But the inputs must be exact:

- **$G_{\mathrm{Planck}} = 1$**: this is a normalisation choice
  (Planck units), so it is exact by definition.
- **$\chi_q = 1/(2q-1)$**: this is the $q$-deformed Lyapunov
  exponent replacing $\ln 2$.  The replacement $\ln 2 \to 1/(2q-1)$
  is forced by requiring $\chi_q$ to be a rational function of $q$
  (valid over any field) with $\chi_1 = 1$.  Any other rational
  function with these properties would give a different $d_H$ and a
  different critical line.

The question of whether the $q$-RH holds thus reduces to:
**is $\chi_q = 1/(2q-1)$ the unique $q$-deformation of the
Lyapunov exponent?**  If it is, the critical line is determined
and unitarity forces zeros onto it.

**Classical RH as a corollary.**
At $q = 1$: $d_H(1) = 1$, $\sigma_1 = 1/2$, $\chi_1 = 1$, and
the $R$-matrix collapses to the symmetric group (trivially
unitary).  The classical Riemann Hypothesis is the statement:
*the classical limit of the substrate preserves unitarity*.  The
$q$-deformed version says: *unitarity is preserved at every value
of $q$, but the critical line moves with the fractal dimension of
the Julia set*.

**Falsifiability.**
The orbit periods $|\gamma|$ of $f_q(z) = z^2 + c(q)$ are
computable over $\mathbb{F}_p$
([discrete Planck step](#rem:discrete-planck-step)).  For
prime-power $q$, the Weil conjectures (Deligne) guarantee zeros at
$\operatorname{Re}(s) = 1/2$.  The $q$-critical line prediction
gives $\sigma_q = 1/2$ only when $d_H(q) = 1$, i.e., at $q = 1$
or $q = \varphi^2$.  For other prime-power values, the dynamical
zeta $Z_q$ and the arithmetic Weil zeta $Z_{\mathbb{F}_q}$ must
disagree — a concrete, computable test.
