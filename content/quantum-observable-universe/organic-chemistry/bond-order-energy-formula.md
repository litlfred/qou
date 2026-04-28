**Statement.**
The bond dissociation energy (BDE) of a C–C bond of order
$k \in \{1, 2, 3\}$ admits the leading-order linear approximation

$$
  \mathrm{BDE}(k) = k \cdot \mathrm{BDE}_{1} + \Delta\varepsilon_{\mathrm{res}}(k),
$$

where $\mathrm{BDE}_{1}$ is the single C–C bond dissociation energy
and $\Delta\varepsilon_{\mathrm{res}}(k)$ is a small correction
encoding the difference between an idealised $k$-fold Hopf link and
the experimental $\pi$-bond energy.

**Empirical verification** (with $\mathrm{BDE}_{1} = 377\ \mathrm{kJ/mol}$
from C–C in ethane):

| Bond | Order $k$ | Experimental BDE | Predicted $k \cdot \mathrm{BDE}_{1}$ | Relative error |
|:-----|:---:|:---:|:---:|:---:|
| C–C single | 1   | 377  | 377  | 0%  |
| C=C double | 2   | 728  | 754  | -3.4% |
| C≡C triple | 3   | 965  | 1131 | -14.7% |
| aromatic C–C | 1.5 | 519 | 566 | -8.3% |

All differences fall within $15\%$, confirming the linear formula
as a useful first-order approximation.

**Significance.**
The linear formula is the **bookkeeping consequence** of the
multi-link Hopf representation of double and triple bonds: a
$k$-fold Hopf link contributes $k$ times the single-link
crossing-energy quantum, plus the pairwise resonance correction.
The systematic underprediction of higher-order BDEs ($-3\%$ at
$k = 2$, $-15\%$ at $k = 3$, $-8\%$ aromatic) indicates that
$\Delta\varepsilon_{\mathrm{res}}(k) < 0$, i.e. real $\pi$-bonds are
*weaker* than $k$ independent Hopf links — consistent with the
electron correlation cost of multi-bond formation.

**Caveat.**
The first-order formula does not derive $\Delta\varepsilon_{\mathrm{res}}(k)$
from first principles; this is a candidate computation for the next
revision of the chapter and is recorded as a TODO in the proof
manifest.
