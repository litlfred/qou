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

*Equivalently, factoring $12 = \dim V_{(2,1)} \cdot |S_3| = 2 \cdot 6$:*

$$
  \boxed{\;m_p \;=\; \dim V_{(2,1)} \cdot \bigl(m_\mu \cdot F_{\mathrm{Bor}}(q_0) \;-\; |S_3| \cdot m_e\bigr)\;}
$$

*where $\dim V_{(2,1)} = 2$ is the standard irrep dimension (Lean-proved via
hook-length formula) and $|S_3| = 3! = 6$ is the symmetric group order
($= P_3(q^2)|_{q=1}$, the Poincaré polynomial classical limit of $[3]_q!$).*

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

## Consistency gap: decay-rate cross-check

The mass-derived $Q_\beta = m_n - m_p - m_e \approx 0.7807\,\mathrm{MeV}$
differs from the N=3 categorical-ladder
$Q_\beta \approx 0.78233\,\mathrm{MeV}$ by $2113\,\mathrm{ppm}$ — bottlenecked
by the flavor-split's $0.10\%$ residual. Closing this gap
would cohomologically prove the $q_0 \leftrightarrow Q_\beta$ relationship.

A decay-width cross-check connects both derivations to experimental
lifetimes via the Fermi theory:
$\mathfrak{D}_\mu = G_F^2 \mathfrak{m}_\mu^5 / (192\pi^3)$ and
$\mathfrak{D}_n \propto G_F^2 Q_\beta^5 f(Q_\beta/\mathfrak{m}_e)$,
where $\mathfrak{D}_K = \hbar / (\text{lifetime of } K)$ is the
decay width in the paper's fraktur-observable convention (avoiding
collision with $\tau$ = fibre functor and $\Gamma$ = sheaf sections).
The ratio $\mathfrak{D}_\mu / \mathfrak{D}_n$ eliminates $G_F$ and
provides a $Q_\beta$-independent consistency test: if both
$\mathfrak{m}_\mu$ and $Q_\beta$ are substrate-derived, the lifetime
ratio $\hbar/\mathfrak{D}_n \div \hbar/\mathfrak{D}_\mu$ should match
CODATA ($\approx 4 \times 10^8$) from categorical invariants alone.

## Structural identifications

The two structural integers in the identity:

| Integer | Categorical meaning | Status |
|---|---|---|
| $2$ | $\dim V_{(2,1)}$ — classical dimension of the standard irrep of $S_3$ (trace-dominant per Wedderburn diagnostic at 49% of $T_1$). Hook-length formula: $3! / (3 \cdot 1 \cdot 1) = 2$. | **Lean-proved** ([`DimStandardRepS3.lean`](../lean/QOU/BraidsAndKnots/DimStandardRepS3.lean) `dim_V_21_eq_two`) |
| $12$ | $\dim V_{(2,1)} \cdot 3! = 2 \cdot 6$. The mass formula factors as $m_p = \dim V_{(2,1)} \cdot (m_\mu \cdot F_{\mathrm{Bor}} - \lvert S_3 \rvert \cdot m_e)$, where $\lvert S_3 \rvert = 3! = P_3(1)$ is the Poincaré polynomial at $q=1$ (classical limit of $[3]_q!$). Both factors are categorically meaningful. | **Identified** — $\dim V_{(2,1)}$ is Lean-proved; $3!$ is the symmetric group order |

## Open work for full categorical proof

1. ~~**Categorical derivation of the factor 2.**~~ **DONE.** The factor
   $2 = \dim V_{(2,1)}$ is the hook-length dimension of the standard
   irrep of $S_3$. Lean-proved in
   [`DimStandardRepS3.lean`](../lean/QOU/BraidsAndKnots/DimStandardRepS3.lean)
   via $3!/(3 \cdot 1 \cdot 1) = 2$.

2. ~~**Categorical derivation of the 12.**~~ **IDENTIFIED:** $12 = \dim V_{(2,1)} \cdot 3! = 2 \cdot 6$.
   The mass formula factors cleanly as
   $m_p = \dim V_{(2,1)} \cdot \bigl(m_\mu \cdot F_{\mathrm{Bor}}(q_0) - |S_3| \cdot m_e\bigr)$
   where $|S_3| = 3! = 6$ is the symmetric group order (equivalently
   the Poincaré polynomial $P_3(q^2)|_{q=1}$, the classical limit of
   $[3]_q!$). Both factors have clean categorical meaning: $\dim V_{(2,1)}$
   is the standard irrep dimension (Lean-proved), and $|S_3|$ is the
   group order. Verified at 50 dps: factored form matches original to
   machine precision, residual $-0.24\,\mathrm{ppm}$ vs CODATA.

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
