This note collects the numerical verification, the per-order $h$-expansion, the combined nucleon-mass derivation, and the sub-ppm precision frontier for [Substrate evaluation](#conj:proton-mass-substrate-identity).

The predictive content throughout is the dimensionless ratio $m_p/m_e$ (equivalently $2(m_\mu/m_e)F_{\mathrm{Bor}} - 12$): since $m_e$ (CAL-1) sets the MeV scale by fiat, the absolute proton mass in MeV is not an independent framework prediction. The MeV figures below are that ratio rendered against the $m_e$ unit — a rendering that lets the ratio be read off against CODATA, not an absolute-mass claim.

## Numerical verification

At $q_0 = 1.10997859555\ldots$ (muon pin, 12 dps):

| Quantity | Value |
|---|---|
| $|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q_0)|$ | $0.998562163\ldots$ |
| $[3]_q!$ | $6.120579305\ldots$ |
| $q_0^3$ | $1.367551884\ldots$ |
| $F_{\mathrm{Bor}}(q_0)$ | $4.469138598\ldots$ |
| $2 \cdot m_\mu \cdot F_{\mathrm{Bor}}(q_0)$ | $944.40385\,\mathrm{MeV}$ |
| $12 \cdot m_e$ | $6.13199\,\mathrm{MeV}$ |
| $m_p$ ($m_e$-scaled rendering) | $938.27186\,\mathrm{MeV}$ |
| CODATA $m_p$ | $938.27209\,\mathrm{MeV}$ |
| Residual | $0.24\,\mathrm{ppm}$ |

## Per-order $h$-expansion in MeV

At $h_0 = q_0 - q_0^{-1} \approx 0.2091$, using the exact rational
$h$-expansion of $F_{\mathrm{Bor}}$ (categorical,
[Borromean categorical observable](../braids-and-knots/f-bor-borromean-observable.md))
the per-order MeV contributions to
$m_p = 2 m_\mu F_{\mathrm{Bor}} - 12 m_e$ are:

| Order | Coefficient | $2 m_\mu \cdot c_k \cdot h_0^k$ |
|---|---|---|
| $h^0$ | $6$ | $+1267.9\,\mathrm{MeV}$ |
| $h^1$ | $-9$ | $-397.6\,\mathrm{MeV}$ |
| $h^2$ | $19/2$ | $+87.7\,\mathrm{MeV}$ |
| $h^3$ | $-57/8$ | $-13.8\,\mathrm{MeV}$ |
| $-12 m_e$ | — | $-6.1\,\mathrm{MeV}$ |
| **Sum** | | $\approx 938.1\,\mathrm{MeV}$ |

The series converges to $0.017\,\mathrm{ppm}$ accuracy at order $h^9$.

## Combined with the canonical flavor-split

[Substrate-pure derivation of the $u$--$d$ flavor split](../mass-theory/flavor-split-substrate.md)
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
  - $m_n = m_p + \mathfrak{Q}_\beta + m_e$, with $\mathfrak{Q}_\beta$ the
    parameter-free Kashiwara $b^2$ truncation (near-match)
    $\approx 939.56542\,\mathrm{MeV}$ ($\sim +1\,\mathrm{ppb}$ residual)
  - $\mathfrak{Q}_\beta := m_n - m_p - m_e$ is DERIVED, not an input
    ($+1.25\,\mathrm{ppm}$ on $\mathfrak{Q}_\beta$ itself; $\sim 1\,\mathrm{ppb}$
    once propagated to $m_n$). The flavor-split $m_n = m_p(1 + X/(1-X/2))$
    (below) is a **secondary diagnostic** ratio ($-1.76\,\mathrm{ppm}$ on
    $m_n$), not the production route.

The flavor-split $X$ is an $h^3$-leading quantity:

$$
  X = \tfrac{1}{6}h^3 - \tfrac{1}{12}h^4 + \tfrac{1}{32}h^5 - \cdots
$$

with $h^0 = h^1 = h^2 = 0$. The neutron-proton mass difference
$\Delta_{pn} = m_p \cdot X/(1 - X/2)$ is therefore a **cubic**
effect in the deformation parameter $h$, not a quadratic one.
The dominant MeV contributions are $h^3$: $+1.43\,\mathrm{MeV}$,
$h^4$: $-0.15\,\mathrm{MeV}$.

The **secondary** flavor-split diagnostic's $m_n$ residual (2.0 ppm)
separates: $0.24\,\mathrm{ppm}$ from $F_{\mathrm{Bor}}$ (proton mass) and
$1.76\,\mathrm{ppm}$ from $X$ (the flavor-split formula). Routing the
neutron through the categorical $\mathfrak{Q}_\beta$ (Kashiwara $b^2$)
instead removes the $X$ term: the production $m_n$ residual drops to
$\sim 1\,\mathrm{ppb}$ and the $\mathfrak{Q}_\beta$ residual to
$+1.25\,\mathrm{ppm}$ (on $\mathfrak{Q}_\beta$ itself).

The 3-calibration discipline reduces to **2 calibrations** $(m_e, m_\mu/m_e)$ for the baryon and $\mathfrak{Q}_\beta$ sector. This equates to $(m_e, q_0)$ via the muon-anchor identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$.

## Consistency gap: decay-rate cross-check

The production neutron directly consumes the parameter-free Kashiwara $b^2$ categorical $\mathfrak{Q}_\beta \approx 0.78233\,\mathrm{MeV}$, so the flavor-split mass-derived $\mathfrak{Q}_\beta$ and the categorical ladder agree at the production level.

A decay-width cross-check connects both derivations to experimental
lifetimes via the Fermi theory:
$\mathfrak{D}_\mu = G_F^2 \mathfrak{m}_\mu^5 / (192\pi^3)$ and
$\mathfrak{D}_n \propto G_F^2 \mathfrak{Q}_\beta^5 f(\mathfrak{Q}_\beta/\mathfrak{m}_e)$,
where $\mathfrak{D}_K = \hbar / (\text{lifetime of } K)$ is the
decay width in the paper's fraktur-observable convention (avoiding
collision with $\tau$ = fibre functor and $\Gamma$ = sheaf sections).
The ratio $\mathfrak{D}_\mu / \mathfrak{D}_n$ eliminates $G_F$ and provides a $\mathfrak{Q}_\beta$-independent consistency test. If both $\mathfrak{m}_\mu$ and $\mathfrak{Q}_\beta$ are substrate-derived, the lifetime ratio $\hbar/\mathfrak{D}_n \div \hbar/\mathfrak{D}_\mu$ matches CODATA ($\approx 4 \times 10^8$) strictly from categorical invariants.

## Open work for full categorical proof

The categorical structure of $F_{\mathrm{Bor}}$ + its rational
$h$-expansion are completed in
[Borromean categorical observable](../braids-and-knots/f-bor-borromean-observable.md).
What remains specific to this archimedean evaluation:

1. **Bridge from $\dim V_{(2,1)}$ to linear factor in mass formula.**
   The factored form
   $m_p = \dim V_{(2,1)} \cdot (m_\mu \cdot F_{\mathrm{Bor}} - |S_3| \cdot m_e)$
   is numerically exact at 50 dps but the categorical WHY — why the
   trace-dominant irrep's dimension enters linearly — remains a formal
   gap. The Wedderburn block expansion of the Markov trace provides
   the natural framework (the $(2,1)$ block carries 49% of the proton's
   $T_1$ contribution), but the formal categorical statement is pending.

## Sub-ppm precision frontier

The identity matches CODATA at $-0.24\,\mathrm{ppm}$. A near-match
candidate for closing the residual to $\sim 0.054\,\mathrm{ppm}$ is

$$
  \mathfrak{m}_\mathfrak{p}
  \;=\;
  \dim V_{(2,1)} \cdot \bigl(\mathfrak{m}_\mu \cdot F_{\mathrm{Bor}}(q_0)
  \;-\;
  \lvert S_3 \rvert \cdot \mathfrak{m}_\mathfrak{e}\bigr)
  \;+\;
  \frac{\alpha_{\mathrm{em}}}{\pi \cdot \dim H_3} \cdot \mathfrak{m}_\mathfrak{e}.
$$

The correction $(\alpha_{\mathrm{em}}/\pi) / \dim H_3 = (\alpha_{\mathrm{em}}/\pi) / 6$
appeared at 0.054 ppm (vs the bare identity's 32 ppm residual to integer
12) — a $600\times$ improvement, computed by
[`ocneanu-12-em-correction-candidate`](../../../computations/ocneanu_12_em_correction_candidate.py).
Both factors are structurally motivated: $(\alpha_{\mathrm{em}}/\pi)$
appears in m_K/m_π's Bring zero-mode closure, and
$1/\dim H_3$ is the Plancherel-mean normalization over the H_3
Wedderburn block.

A Bring zero-mode template transfer
and an enumeration of 27 alternative
knot-operator geometries both confirmed that $1/\dim H_3 = 1/6$ is
the structurally robust denominator, but no transfer of the m_K/m_π
$(3q^2-1)/(2q^2)$ shape gives a tighter form. The 54 ppb residual
after the EM correction is either (a) a non-trivial categorical
$f(q)$ factor with $f(q_0) \approx 1.00167$ not yet identified, or
(b) higher-order QED / categorical corrections at the substrate
precision floor. This correction remains a near-match candidate, not
an established categorical derivation.

The Ocneanu-weight cancellation behind the $-12\,m_e$ term carries a
universal leading-pole coefficient $-1/12$. That coefficient rests on
high-precision numerical pole detection, verified to 200 decimal
places; the symbolic Hoefsmit route to the cancellation count still
carries unrepaired convention and sign issues, so the coefficient is
numerically verified rather than symbolically derived.

## See also

- [Borromean categorical observable](../braids-and-knots/f-bor-borromean-observable.md)
  — categorical observable $F_{\mathrm{Bor}}$ (closed form, $h$-expansion, structural integers)
- [Substrate-pure derivation of the $u$--$d$ flavor split](../mass-theory/flavor-split-substrate.md)
  — canonical Hecke-skein $\Delta m / M_N$ derivation
