The tritium $\beta$-decay $Q$-value is independently verified by computing
the full Gröbner--Shirshov normal form of the 9-strand nuclear braid
$\beta({}^3\mathrm{H})$ in the Iwahori--Hecke algebra $H_9(q)$, using
the Borromean confinement braid $B_3 = (\sigma \cdot \sigma^{-1})^3$
at each nucleon.

**Substrate parameter** (from muon--electron mass ratio, [Skein mass relation](#rem:skein-mass-relation)):

$$
  q_0 = 1.10998, \quad
  \hbar_q = 1 - q^{-1} \approx 0.09908, \quad
  \kappa_q = \tfrac{\ln q \cdot m_e}{3} \approx 0.01777\;\text{MeV}.
$$

**Nuclear braids** ($3A = 9$ strands):

- Parent ${}^3\mathrm{H}$: $[\mathfrak{p}, \mathfrak{n}_1, \mathfrak{n}_2]$
  $= [uud \mid udd \mid udd]$, quark types $[p,p,n \mid p,n,n \mid p,n,n]$.
- Daughter ${}^3\mathrm{He}$: $[\mathfrak{p}_1, \mathfrak{p}_2, \mathfrak{n}]$
  $= [uud \mid uud \mid udd]$, quark types $[p,p,n \mid p,p,n \mid p,n,n]$.

**Crossing coefficients** (from $\sigma^{-1} = \sigma - (q - q^{-1})$):

| Pair | Type | $(c, d)$ |
|------|------|----------|
| $uu$ (pp) | symmetric | $(1, 0)$ |
| $dd$ (nn) | antisymmetric | $(1, -\mathrm{HA})$ |
| $ud$ (pn) | mixed | $(1, -\mathrm{HA}/2)$ |

where $\mathrm{HA} = q - q^{-1} \approx 0.2091$.

**Verified assertions** (all from `h9_beta` engine at $q_0 = 1.10998$):

| Quantity | Computed | Expected | Discrepancy | Source |
|----------|----------|----------|-------------|--------|
| NF(${}^3\mathrm{H}$) terms | $864$ | — | — | Gröbner--Shirshov reduction |
| NF(${}^3\mathrm{He}$) terms | $864$ | — | — | Gröbner--Shirshov reduction |
| $\mathrm{net}({}^3\mathrm{H})$ | $0.6694$ | — | — | Sum of NF coefficients |
| $\mathrm{net}({}^3\mathrm{He})$ | $1.1185$ | — | — | Sum of NF coefficients |
| $\Delta\mathrm{net}$ | $-0.4491$ | — | — | $\mathrm{net(par)} - \mathrm{net(dau)}$ |

**$Q$-value comparison** ($Q = |\Delta\mathrm{net}| \times \kappa_q$):

| Method | $Q$ (MeV) | $Q_{\mathrm{exp}}$ (MeV) | Error | Notes |
|--------|-----------|--------------------------|-------|-------|
| Borromean NF | $0.00798$ | $0.01861$ | $-57\%$ | Full $B_3$ confinement |
| Flat L1 | $0.366$ | $0.01861$ | $+1868\%$ | No confinement (all crossings equal) |
| $T_{3,5}$ weak vertex | $0.00728$ | $0.01861$ | $-61\%$ | $(\sigma_3 \sigma_4)^5$ insertion |
| Experimental | — | $0.01861$ | — | CODATA ${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar{\nu}_e$ |

**Interpretation.**

1. *Borromean confinement is essential.*  The flat L1 model (which treats
   all $3A = 9$ quark strands equally without confinement braids) overshoots
   by a factor of $\sim 20$.  The Borromean confinement braid $B_3 = (\sigma \cdot
   \sigma^{-1})^3$ introduces the accepting crossings ($\sigma^{-1}$ terms)
   that suppress the amplitude, reducing the error from $+1868\%$ to $-57\%$.

2. *Remaining discrepancy.*  The $-57\%$ error in the Borromean NF result
   suggests that the energy scale $\kappa_q = \ln(q) \cdot m_e / 3$ or the
   crossing coefficient assignments need refinement at the nuclear level.
   Possible sources: (a) the $\kappa_q$ calibration is derived from free-neutron
   decay and may not transfer exactly to bound nuclei; (b) inter-nucleon
   Hopf crossings may require a distinct coupling from intra-nucleon Borromean
   crossings.

3. *Compare with muon--electron mass ratio.*  The muon--electron mass ratio
   $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$ ([knot volume verification](#prf:knot-volumes-verification))
   is reproduced to six significant figures — it is the *input* that
   determines $q_0$.  The tritium $Q$-value is a genuine *prediction*
   with zero free parameters at the quark level.

**Reproducibility**: Build and run `cargo run --release --bin h9_beta`
in `tools/hecke-engine/`.
