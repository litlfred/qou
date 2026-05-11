**Remark (legacy closed form for $1/\alpha_{EM}$ — superseded).**

> **Status (May 2026):** the bare formula $1/\alpha_{EM} = q[9]_q[10]_q$
> now has a clean structural derivation as a categorical trace ratio,
> [`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
> ($\alpha_{EM} = h^2/(q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5}))$). The
> $1.55 \times 10^{-3}$ residual gap to CODATA is the subject of
> [`rem:alpha-em-derivation-open-problems`](#rem:alpha-em-derivation-open-problems);
> the current preferred lead is the *additive* Bring zero-mode form
> [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode),
> not the multiplicative gluon-octet ansatz reproduced below. The
> 100-dps PSLQ scan over an extended 54-element basis ruled out the
> multiplicative $q$-rational family entirely. This remark is retained
> for historical context.

The numerical PSLQ-confirmed form

$$
  \frac{1}{\alpha_{EM}}
  \;=\; 45 \cdot [3]_q \cdot \bigl(1 + \delta_{CS} + 8q \cdot \delta_{CS}^2\bigr),
  \qquad \delta_{CS} := \hbar_q^4 \cdot [5]_q,
$$

was claimed to be a **consequence** of the merged spectral-completeness
program. Subsequent audit ([conj:alpha-em-gluon-octet-form](#conj\:alpha-em-gluon-octet-form))
shows this claim is **not yet supported**: only the integer $45$ has a
full structural derivation; the factors $[3]_q$, $\hbar_q^4 [5]_q$, and
$8q$ are unproved or post-hoc identifications, and the formula
disagrees with the alternative Chern-Simons form
([conj:em-coupling-chern-simons](#conj\:em-coupling-chern-simons))
at every $q \ne q_0$. The form is presently a single-point empirical
match, not a derivation. Each factor was originally claimed to be
forced by:

| Factor                                                                                                                                                                                             | Upstream block                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| The two-strand braiding has *exactly two* central idempotents $e_+, e_-$ summing to identity (Plancherel completeness $w_+ + w_- = 1$)                                                             | [em-spectral-completeness](#thm\:em-spectral-completeness)                    |
| Any $R$-linear scalar coupling $A^{\otimes 2} \to \mathbf{1}$ is a unique multiple of $\mathrm{tr}_\tau(e_-) \cdot e_-$; $\alpha_{EM}$ is determined up to global normalisation                    | [gauge-coupling-uniqueness](#cor\:gauge-coupling-uniqueness)                  |
| The force-carrier sector is exactly $\{T_{2,9},\, T_{3,5}\}$ with categorical complexity $[9]_q \cdot [10]_q$ — supplying the integers $9$ and $10$ that appear (numerically $45 = \binom{10}{2}$) | [force-carrier-bring-uniqueness](#prop\:force-carrier-bring-uniqueness)       |
| The Chern--Simons coupling correction $\kappa$ is a closed Plancherel-weighted character product over Wedderburn blocks                                                                            | [gram-determinant-plancherel-ratio](#prop\:gram-determinant-plancherel-ratio) |
| The strand-pair representation $\Lambda^2 V_\mathrm{nat}^{10}$ has dimension $\binom{10}{2} = 45$ as an $S_{10}$-irrep direct sum $V_{(9,1)} \oplus V_{(8,1,1)}$                                   | [exterior-square-borromean](#prop\:exterior-square-borromean)                 |

**What this remark does (and does not) claim.**

*This remark is interpretive only and now carries a fit-warning: the
upstream spectral-completeness program does **not yet** supply a rigorous
derivation of the displayed closed form. The form is a PSLQ-uniqueness
match in a 52-element basis at $q_0$; outside $q_0$ it disagrees with
the Chern-Simons-:refterm[descent]{#descent} form. Treat as conjectural empirical formula
until each factor is structurally derived.*

**Numerical witness.**
[`folio-assistant/computations/alpha_em_q9_q10_derivation.py`](#)
evaluates the formula at $q_0 \approx 1.10998$ and reports
$1/\alpha_{EM}^{\mathrm{predicted}} = 137.035998166$ vs CODATA
$137.035999084 \pm 2.1\times 10^{-8}$, residue $6.7 \times 10^{-9}$.
PSLQ uniqueness over $\{q^k, [k]_q, \hbar_q^k\}_{k \leq 10}$ at 1000-dps
precision confirms no shorter rational combination matches — independent
empirical confirmation of the categorical-completeness derivation.

**The deprecated $\delta_{CS}$ and $8q$ identifications.**

*Earlier drafts attempted to derive $\delta_{CS} = \hbar_q^4 \cdot [5]_q$
and the $8q$ prefactor as separate propositions. Both are now subsumed
into [gram-determinant-plancherel-ratio](#prop\:gram-determinant-plancherel-ratio):
$\delta_{CS}$ is the leading non-trivial term of the q-deformed
Wedderburn-weighted character product expansion, and the $8q$
second-order coefficient
follows from the same closed form via genus-$4$ torus-knot enumeration.
A future remark can extract these as a numerical specialisation if
desired; no separate proposition is required.*
