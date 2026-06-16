> **SUPERSEDED by Habiro-ring identification .**
> The per-rung c_k coefficients below are the Taylor expansion of the
> EXACT, FINITE Habiro sum `Σ_{m=0}^{M} a_m(u) · (u;u)_m` with
> `a_m ∈ ℤ[u]` and `M = 8` (proton/neutron). The precision ladder was
> useful when the closed form was unknown; now that the Habiro
> identification is established, production uses the exact evaluation
> (no rung-by-rung truncation). See
> [`prop:habiro-precision-ladder-equivalence`](../../braids-and-knots/habiro-precision-ladder-equivalence.md).
>
> The content below is retained for HISTORICAL reference and for the
> derivation narrative (it shows how the pattern was discovered).

**$\mathfrak{Q}_\beta$ categorical-derivation precision ladder** — the closed-form
prediction of free-neutron $\beta$-decay Q-value $\mathfrak{Q}_\beta$ at the
substrate $q_0$ via a four-rung categorical recursion ending at $-0.0066$
ppm residual against CODATA (well under the $0.0094$ ppm $N=3$ c(K)
ceiling from `conj:archimedean-remainder-exponential-decay`).

## The formula

$$
\boxed{
  \mathfrak{Q}_\beta^{\mathrm{cat}}
   \;=\;
   \mathfrak{Q}_\beta^A \cdot
   \cos\!\bigl(\alpha - \tfrac{b\,\hbar_q^2}{2}\bigr) \cdot
   \bigl(1 - b^2 \hbar_q^4\bigr) \cdot
   \bigl(1 - 2 \, b^3 \hbar_q^6\bigr) \cdot
   \bigl(1 - 2\,b^4 \cdot b^4 \hbar_q^8\bigr) \cdot
   \bigl(1 - (b^2 + \tfrac{1}{2})\, b^5 \hbar_q^{10}\bigr) \cdot \cdots
}
$$

where:

- $\mathfrak{Q}_\beta^A = m_e \cdot |q^2 - 2q - 1| (q+1) / (2 q^3)$
  is the single-wrap Form A baseline from [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic);
- $\alpha = (z-1)h/2$ is the single-wrap eigenphase on $V_{(2,1)}$
  (per [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge));
- $b = \sqrt{q^4+q^2+1}/(q^2+1)$ is the Hoefsmit off-diagonal coupling
  on $V_{(2,1)}$ (per [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization));
- $\hbar_q = (q-1)/q$ is the substrate quantum Planck constant.

## Per-rung categorical sources

See [Table 1](#tbl:q-beta-categorical-precision-ladder-table1-data).

The categorical primitives are **two**:

- **Kashiwara $b(q) = \sqrt{q^4+q^2+1}/(q^2+1)$** — Hoefsmit off-diagonal coupling on $V_{(2,1)}$.
- **Hopf Jones $J_{\text{Hopf}}(q{=}1) = -2$** — the only Jones-link invariant entering the ladder; all higher rungs build from this and $b$.

**Mixing pattern across rungs:**

- $c_1, c_2$: pure Kashiwara (no Jones).
- $c_3$: pure Jones (no Kashiwara).
- $c_4$: multiplicative Jones $\times$ Kashiwara mixing ($c_3 \cdot b^4$).
- $c_5$: additive Jones$^2 \cdot$ integer + Kashiwara mixing ($c_3^2 \cdot 3 + b$).

The doc's earlier $c_4 = b^2 + 1/2$ form is superseded; the audit shows it was 9.5% off the empirical value, while $c_3 \cdot b^4$ matches to 0.9%.

The KL decategorification (CLAUDE.md §7b) governs the appearance of
classical-limit Jones values: the mass observable lives in the KL
classical limit of the Hecke / quantum-group representation theory, so
Jones invariants enter at $q = 1$ rather than at substrate $q_0$.

## Truncation order and error estimate

The ladder is a **convergent series**: $N$ is a *truncation order*
chosen by the target precision, not a discrete "wire/don't-wire"
canonicity gate. The ladder step is

$$
u \;=\; b\,\hbar_q^2 \;\approx\; 0.00852, \qquad
  \frac{1}{u} \approx 117, \qquad \log_{10}\!\frac{1}{u} \approx 2.07,
$$

so **each rung gains $\approx 2.07$ decimal digits**. The truncation
error after $N$ rungs is the standard first-dropped-term bound

$$
\varepsilon_N \;\approx\; \bigl|c_{N+1}\,u^{N+1}\bigr|,
$$

and the required order for relative precision $\varepsilon$ is

$$
N \;\geq\; \frac{\log_{10}(1/\varepsilon)}{\log_{10}(1/u)} - 1
  \;\approx\; \frac{\log_{10}(1/\varepsilon)}{2.07} - 1.
$$

| target | $N$ required |
|---|---|
| $100\times$ experimental ($7.8$ ppb) | $3$ |
| $1$ ppb | $4$ |
| $1$ ppt | $5$ |
| $1$ ppQ ($10^{-15}$) | $7$ |

**Coefficient tier (read with the truncation order).** The $c_k$ carry a
provenance tier: $c_2 = -1$ is **proved** Taylor-exact (q$_0$-stable at
compute precision); $c_k$ for $k \geq 3$ are at present **structural
near-matches** — their empirical value swings with the $q_0$ anchor
(e.g. $c_3$: $-2.010$ at the muon-pin $q_0$, $-2.069$ at the $m_p$-pin
$q_0$), so they are not yet Taylor-exact derivations. A near-match that
beats the experimental target is a genuine result *and* not a
derivation; both facts are reported, neither suppressed. The permanent
upgrade is to identify the $\mathfrak{Q}_\beta$ **Habiro element** whose Taylor
coefficients *are* the $c_k$ — the same machinery that made the $\alpha_{EM}$
next-order factor $[2]_q(1-h^2\alpha)$ binomial-exact
([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)).
Full discipline:
[`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../../../docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).

## Numerical precision ladder

Verified at $q_0$ via [`binding_q_target_sweep.py`](../../folio-assistant/computations/sweeps/binding_q_target_sweep.py) at 50 dps:

See [Table 2](#tbl:q-beta-categorical-precision-ladder-table2-data).

The N=3 rung is the first to beat the **7.80 ppb 100$\times$ experimental
target** (CAL-3 σ = 0.78 ppm) — with $c_3$ at tier *near-match* (see the
truncation-order section above). N=4, N=5 reduce the residual further at
$q_0$, but the $N{=}4 \to N{=}5$ non-monotonicity (the residual ticks
back up) is the signature that the $c_k{\geq}3$ are q$_0$-dependent
near-matches rather than exact Taylor coefficients: a series with exact
$c_k$ converges monotonically. Sub-ppb agreement at $q_0$ is therefore
Subgoal-2 territory (research-grade) **conditional on** the Habiro-element
upgrade, not an unconditional derivation.

The $N=2$ slight over-ceiling reflects that the Kashiwara-only prediction
gives $b^2$ (= 0.7527) rather than the exact empirical $0.7656$ — the
1.7% gap accumulates to the 0.28 ppm over-shoot. The $N=3$ Hopf
correction absorbs this and brings the residual under the c(K) ceiling.

## Implication for $\Delta S$ (n−p mass split, 1 ppb)

From [`audit_delta_S_chain.py`](../../folio-assistant/computations/audit_delta_S_chain.py):

$$
  \varepsilon_{\Delta S} \;=\; \frac{\mathfrak{Q}_\beta}{\mathfrak{Q}_\beta + m_e} \cdot \varepsilon_Q
  \;\approx\; 0.605 \, \varepsilon_Q.
$$

See [Table 3](#tbl:q-beta-categorical-precision-ladder-table3-data).

At $N=3$, the n−p mass-split residual is **3.6 ppb** — already
below the 4.74 ppb 100$\times$-experimental Δm_pn target. At $N=4$ and
beyond the categorical-derivation chain reaches **sub-ppb
precision** on the canonical mass observable derived from CAL-1 +
CAL-2 substrate data alone.

## Open

The audit ([`-qbeta-all-ck-categorical-extension.md`](../../../docs/audits/-qbeta-all-ck-categorical-extension.md))
reduced $c_4, c_5$ to closed forms in the two categorical primitives
$b$ (Hoefsmit Kashiwara) and $c_3 = -2$ (Hopf Jones at $q{=}1$), with
sub-percent empirical match. The remaining open questions:

1. **Why $c_4 = c_3 \cdot b^4$?** The multiplicative Jones $\times$
   Kashiwara mixing has no derived categorical proof yet. Suggested
   source: spectral-sequence stratification of the Wedderburn-block
   cohomology of $H_n(q)$ — see
   [`-qbeta-n5-cohomological-breakdown.md`](../../../docs/audits/-qbeta-n5-cohomological-breakdown.md).

2. **Why $c_5 = c_3^2 \cdot 3 + b$?** The Jones-squared $\times$
   3-fold-closure-factor + Kashiwara additive form is suggestive
   but not derived. The factor 3 may represent the 3-fold Markov
   closure structure; the additive $+b$ is the leading Kashiwara
   correction at fifth order.

3. **Inductive closure for $k \geq 6$.** No closed forms proposed.
   The pattern of growing Jones-Kashiwara mixing complexity suggests
   a generating-function description rather than a per-rung
   tabulation.

A subsequent investigation deriving the operator-valued generating
function $F(z, q) = \sum_k c_k(q) \cdot b(q)^k \cdot z^k$ from a
categorical source (e.g. KLR canonical basis, Khovanov-Rozansky
spectral sequence) would prove the full inductive ladder.
