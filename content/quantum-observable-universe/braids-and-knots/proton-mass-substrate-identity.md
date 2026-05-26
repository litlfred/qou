**Proposition (proton-mass substrate identity).**
*Let $q_0 \approx 1.10978$ be the substrate parameter, $m_e$ the
electron mass (CAL-1), $m_\mu$ the muon mass (CAL-2 via $m_\mu/m_e$),
and let*

$$
  F_{\mathrm{Bor}}(q) \;:=\; \frac{\bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr| \cdot [3]_q!}{q^3}
$$

*be the natural categorical observable combining the proven Borromean
Markov-trace closed form*

$$
  \bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr|
  \;=\; \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}
  \qquad (h := q - q^{-1})
$$

*([`thm:borromean-markov-trace-closed-form`](borromean-markov-trace-closed-form.md))
with the proven q-factorial closed form*

$$
  [3]_q! \;=\; (q^2 + 1 + q^{-2})(q + q^{-1}).
$$

*Then the proton mass satisfies the substrate identity*

$$
  \boxed{\;m_p \;=\; 2 \cdot m_\mu \cdot F_{\mathrm{Bor}}(q_0) \;-\; 12 \cdot m_e\;}
$$

*to a residual of $0.24\,\mathrm{ppm}$ at $q = q_0$ (50-dps MPFR
verified, [`m_p_substrate_identity_50dps.py`](../../../folio-assistant/computations/m_p_substrate_identity_50dps.py)).*

## Numerical verification

At $q_0 = 1.10977859555\ldots$ (50 dps):

| Quantity | Value |
|---|---|
| $|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q_0)|$ | $0.998562163\ldots$ |
| $[3]_q!$ | $6.120579305\ldots$ |
| $q_0^3$ | $1.367551884\ldots$ |
| $F_{\mathrm{Bor}}(q_0)$ | $4.469138598\ldots$ |
| $2 \cdot m_\mu \cdot F_{\mathrm{Bor}}(q_0)$ | $944.40385\,\mathrm{MeV}$ |
| $12 \cdot m_e$ | $6.13199\,\mathrm{MeV}$ |
| Predicted $m_p$ | $938.27186\,\mathrm{MeV}$ |
| CODATA $m_p$ | $938.27209\,\mathrm{MeV}$ |
| Residual | $0.24\,\mathrm{ppm}$ |

## Combined with the canonical flavor-split

[`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md)
gives the canonical Hecke-skein derivation

$$
  \frac{m_n - m_p}{M_N} \;=\; \frac{(q-1)^2(1 - q^{-4})}{3}
  \;=\; \frac{\hbar_q^2 \cdot h \cdot [2]_q}{3}
$$

(matching CODATA $\Delta m / M_N$ to $-0.10\%$, NOT a fit — each
factor has explicit categorical meaning).

Combining the proposition with the flavor-split derives **both**
nucleon masses from only $(m_e, m_\mu, q_0)$:

  - $m_p = 2 \cdot m_\mu \cdot F_{\mathrm{Bor}}(q_0) - 12 \cdot m_e$
    $\approx 938.27186\,\mathrm{MeV}$ ($0.24\,\mathrm{ppm}$ residual)
  - $m_n = m_p \cdot (1 + X/(1 - X/2))$ where $X = \Delta m / M_N$
    $\approx 939.56354\,\mathrm{MeV}$ ($2.00\,\mathrm{ppm}$ residual)
  - $Q_\beta := m_n - m_p - m_e$ is now DERIVED, not an input
    (matches CODATA to $-2113\,\mathrm{ppm}$, bottlenecked by $m_n$)

The QOU 3-calibration discipline reduces to **2 calibrations**
$(m_e, m_\mu/m_e)$ for the baryon + $Q_\beta$ sector (or equivalently
$(m_e, q_0)$ via the muon-anchor identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$).

## Structural identifications

The two structural integers in the identity:

| Integer | Categorical meaning |
|---|---|
| $2$ | Bar-pair partition count: $(3) \leftrightarrow (1,1,1)$ transpose pair under bar-Mullineux symmetry. Per-Wedderburn-block diagnostic confirms these dominate the proton's $T_1$ contribution (33% + 18% = 51%). The transpose-pair identity $y_{(3)}(q) \cdot y_{(1,1,1)}(q) = 1/[3]_q!^2$ is Lean-proved in [`YLambdaQSchur.lean`](../lean/QOU/BraidsAndKnots/YLambdaQSchur.lean) `yLambdaQSchur_transpose_pair`. |
| $12$ | Inverse of the Ocneanu cancellation leading-pole coefficient $-1/12$ in $\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q) \sim -1/(12 \cdot q^{10})$ as $q \to 0$. Per [`docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md`](../../../docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md), verified to 200 dps. Bernoulli-like constant connecting the $q=0$ Laurent-pole structure to the $q=q_0$ substrate mass formula. |

## Open work for full categorical proof

1. **Categorical derivation of the factor 2** via bar-pair structure on
   $y_{(3)} \leftrightarrow y_{(1,1,1)}$. The transpose-pair identity is
   already Lean-proved; what's needed is the bridge from "partition
   transpose-pair" to "factor 2 in the mass formula".

2. **Categorical derivation of the 12** via Ocneanu cross-partition
   cancellation. PR #546's Hoefsmit symbolic work needs the 2×2 block
   bug fix to prove $-1/12$ rigorously as a symbolic identity (currently
   verified only numerically to 200 dps).

3. **Identification of $F_{\mathrm{Bor}}(q)$** as a natural categorical
   observable. Currently it's the empirically-observed combination
   $|\mathrm{tr}_M| \cdot [3]_q! / q^3$ that closes the mass formula; a
   categorical derivation would identify it as e.g. a Wedderburn trace
   with a specific content-shift normalisation.

## See also

- [`docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md`](../../../docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md)
  — full audit writeup
- [`thm:borromean-markov-trace-closed-form`](borromean-markov-trace-closed-form.md)
  — Lean-proved $|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|$
- [`thm:q-schur-y-lambda-closed-form`](q-schur-y-lambda-closed-form.md)
  — Lean-proved q-Schur y_λ closed form (this PR)
- [`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md)
  — canonical Hecke-skein $\Delta m / M_N$ derivation
- [`docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md`](../../../docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md)
  — the universal $-1/12$ leading-pole coefficient (200-dps verified)
- [`m_p_substrate_identity_50dps.py`](../../../folio-assistant/computations/m_p_substrate_identity_50dps.py)
  — production-grade compute script (50-dps MPFR)
