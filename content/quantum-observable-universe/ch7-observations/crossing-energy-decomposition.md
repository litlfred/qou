The [crossing energy](#def:crossing-energy) assigns asymmetric
weights to positive and negative crossings: $+q$ for $L_+$ and
$-q^{-1}$ for $L_-$, with $q > 1$.  This asymmetry is not an
artefact — it is the origin of electromagnetism.  Writing
$q = e^\lambda$ with $\lambda = \ln q > 0$, the crossing weights
decompose into symmetric and antisymmetric channels:

$$
  q \;=\; \cosh\lambda + \sinh\lambda, \qquad
  q^{-1} \;=\; \cosh\lambda - \sinh\lambda.
$$

**The two channels.**

| Channel | Weight per crossing | Mirror behaviour | Physical force |
|---------|-------------------|-----------------|----------------|
| Symmetric | $\cosh(\ln q)$ | Invariant under $\sigma$ | **Strong binding** |
| Antisymmetric | $\sinh(\ln q)$ | Reverses under $\sigma$ | **Coulomb (electromagnetic)** |

The symmetric part $\cosh(\ln q)$ is the same for a crossing and
its mirror image — it contributes equally to particle and antiparticle.
This is the **strong force**: it binds regardless of charge.

The antisymmetric part $\sinh(\ln q)$ flips sign under crossing
reversal $\sigma$ — it has opposite effect on particle and antiparticle.
This is the **electromagnetic force**: like charges repel, unlike
charges attract.

**Pair creation: why the pair flies apart.**

When an $e^- e^+$ pair is created at the
[exceptional divisor](#def:exceptional-divisor), the electron
contributes $E_{\mathrm{cross}}(e^-) = 3q$ (three positive crossings)
and the positron contributes $E_{\mathrm{cross}}(e^+) = -3q^{-1}$
(three negative crossings).  Their combined crossing energy is:

$$
  E_{\mathrm{cross}}(e^-) + E_{\mathrm{cross}}(e^+)
  \;=\; 3q - 3q^{-1}
  \;=\; 6\sinh(\ln q)
  \;\approx\; 0.630 \quad (\text{Skein units}).
$$

The symmetric (strong) contributions **cancel** in the pair — the
electron's $3\cosh\lambda$ and the positron's $-3\cosh\lambda$
(from the sign convention on negative crossings) sum to zero.  What
remains is pure antisymmetric (Coulomb) repulsion: $6\sinh\lambda > 0$.
This net positive energy is what drives the pair apart after creation.

**Individual particle: both forces present.**

For a single particle, both channels contribute.  The electron's
crossing energy $3q = 3(\cosh\lambda + \sinh\lambda)$ contains
strong binding (symmetric) and Coulomb (antisymmetric) in the ratio:

$$
  \frac{\text{Coulomb}}{\text{strong}}
  \;=\;
  \frac{\sinh(\ln q)}{\cosh(\ln q)}
  \;=\; \tanh(\ln q).
$$

At the paper's substrate parameter $q = 1.10997$:

$$
  \tanh(\ln 1.10997)
  \;\approx\; 0.104.
$$

Electromagnetism is approximately **10\%** of the strong force at the
constituent (Skein) scale.  This is the ratio measured at hadronic
energy scales — before QCD running brings the strong coupling down
at higher energies, and before QED running brings the electromagnetic
coupling up.

**The full crossing energy table.**

For a particle with $n_c$ crossings (all positive in the minimal
diagram):

| Quantity | Formula | $T_{2,3}$ ($n_c = 3$) | Value |
|----------|---------|----------------------|-------|
| Total crossing energy | $n_c\,q$ | $3q$ | $3.330$ |
| Strong component | $n_c\,\cosh(\ln q)$ | $3\cosh(\ln q)$ | $3.015$ |
| Coulomb component | $n_c\,\sinh(\ln q)$ | $3\sinh(\ln q)$ | $0.315$ |
| Pair net energy | $n_c(q - q^{-1})$ | $3(q - q^{-1})$ | $0.630$ |
| EM/strong ratio | $\tanh(\ln q)$ | $\tanh(\ln q)$ | $0.104$ |

The decomposition extends to composite hadrons.  For the proton
$\mathfrak{p} = [u,u,d]_c \bowtie \mathcal{L}_H$, the total
crossing energy includes contributions from all inter-quark crossings
in the Borromean braid word.  The symmetric part gives the strong
binding energy (which is negative, holding the proton together);
the antisymmetric part gives the net Coulomb charge $Q(\mathfrak{p}) = +1$.
The [Hopf stability](#prop:torus-hopf-stability) result —
$E_{\mathrm{cross}}(\mathfrak{p}) < 0$ — says the strong binding
dominates the Coulomb repulsion, ensuring the proton is stable.
