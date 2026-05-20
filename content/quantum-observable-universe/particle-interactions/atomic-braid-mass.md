## Atomic braid

**Definition.**
*The **atomic braid** of a neutral atom $(Z, N)$ is the element of
$H_{A+Z}(q)$ obtained by assembling $Z$ protons, $N$ neutrons,
and $Z$ electrons into a single Hecke algebra with $A + Z$ strands,
where $A = Z + N$.  The crossing coefficients are:*

| Pair | Crossing | $c$ | $d$ | Origin |
|:-----|:---------|:----|:----|:-------|
| $\mathfrak{p}\mathfrak{p}$ | $\sigma$ | $1$ | $0$ | strong repulsion |
| $\mathfrak{n}\mathfrak{n}$ | $\sigma^{-1}$ | $1$ | $-(q - q^{-1})$ | strong inverse |
| $\mathfrak{p}\mathfrak{n}$ | $\sigma - \tfrac{1}{2}(q - q^{-1})$ | $1$ | $-\tfrac{1}{2}(q - q^{-1})$ | strong mixed |
| $\mathfrak{p}e$ | $\sigma^{-1}$ | $1$ | $-(q - q^{-1})$ | EM attraction |
| $\mathfrak{n}e$ | $\mathrm{id}$ | $0$ | $1$ | no interaction |
| $ee$ | $\sigma$ | $1$ | $0$ | EM repulsion |
| $\mathfrak{p}_{\mathrm{gluon}}$ | $\sigma^2$ | | | $2\sigma_0$ internal (LP-derived) |
| $\mathfrak{n}_{\mathrm{gluon}}$ | $L_+L_-$ | | | $4\sigma$ internal (LP-derived) |

*Each nucleon also carries **internal gluon crossings** from LP
stability ([integer LP gluon](#prop:mass-endomorphism-tower)):
$2$ bare $\sigma_0$ for protons ($11$ total crossings) and
$L_+ \to L_-$ for neutrons ($13$ total crossings).  These
are prepended to the nucleon's per-generator crossing chain
in the Wedderburn traced volume computation.*

*The **ground-state ordering** is determined by:*
1. *Nuclear ordering: minimize $\Phi_1$ over all permutations of
   $Z$ protons and $N$ neutrons (exact search for
   $\binom{A}{Z} \leq 50000$, steepest descent otherwise).*
2. *Electron insertion: greedily insert each of $Z$ electrons at
   the position minimizing $\Phi_1$.*

*The greedy insertion produces **ep pairs**: each electron sits
immediately before its proton.  The $\mathfrak{n}e = \mathrm{id}$
crossing means electrons pass through neutrons without generating
Hecke generators.*

*For hydrogen ($A = 1$): the bare $[e, \mathfrak{p}]$ braid is
LP-unstable (Proposition \ref{prop:atomic-lp-stability}).  The
$\mathfrak{p}e$ crossing uses the $\mathcal{B}_3$-dressed eigenvalues
$(q^5, -q^{-5})$ instead of bare $(q^{-1}, -q)$.*


## LP stability

**Proposition.**
*The bare hydrogen atom $[e, \mathfrak{p}] = \sigma_0^{-1}$ in
$H_2(q)$ is **LP-unstable**: there exists a Markov-normalised
operator $X^* = \alpha \cdot \mathbf{1} + \beta \cdot \sigma_0$
that annihilates the traced volume ($V = 0$).*

*The $\mathcal{B}_3$ dressing (proton internal structure)
**stabilises** the atom.  The Borromean braid
$(\sigma_1\sigma_2)^3$ is the identity in the standard (degree-2)
representation of $H_3(q)$.  This changes the annihilation ratio
from $\lambda_s/\lambda_a = 0.537$ (bare) to $q^{-10} = 0.352$
(dressed).  The original annihilator $X^*$ cannot satisfy the
dressed condition, so the atom is stable.*

*For composite nuclei ($A \geq 2$): nuclear crossings
($\mathfrak{p}\mathfrak{p}$, $\mathfrak{n}\mathfrak{n}$,
$\mathfrak{p}\mathfrak{n}$) break the simple $H_2(q)$ structure,
providing LP stability without explicit $\mathcal{B}_3$ dressing.*


## Three-invariant mass formula

**Relation to the GB-NF form.**
*The atomic mass admits the abstract algebraic expression
([atomic mass via GB-NF](#prop:atomic-mass-gb-nf))*

$$
  \mathcal{M}(K)
  \;=\;
  m_e \cdot \rho_K \cdot
  \bigl\lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\bigr\rvert,
$$

*where $\mathrm{NF}_{\mathrm{GS}}$ is the Gröbner–Shirshov normal
form in $H_n(R, q_0)$ and $\rho_K$ is the categorical density. The
formula below is a **concrete evaluation** of this abstract form
that fixes $\rho_K$ via CODATA constituent inputs $m_{\mathfrak{p}},
m_{\mathfrak{n}}$ and absorbs the residual $\rho_K$ structure into
the per-generator log-volume sum $\alpha \sum_i \ln\lvert\hat{V}_i^{\mathrm{full}}\rvert$.*

**Proposition.**
*The mass of a neutral atom $(Z, N)$ is*

$$
  \mathcal{M}(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  + \alpha \sum_i \ln\lvert \hat{V}_i^{\mathrm{full}} \rvert
$$

*where the **full traced volume** per generator is the
Wedderburn-weighted sum:*

$$
  \hat{V}_i^{\mathrm{full}}
  =
  w_{\mathrm{sym}} \cdot \lambda_i^{\mathrm{sym}}
  + w_{\mathrm{std}} \cdot \hat{V}_i^{\mathrm{std}}
  + w_{\mathrm{alt}} \cdot \lambda_i^{\mathrm{alt}}
$$

*with Wedderburn--Markov weights
$w_\lambda = \dim_q(\lambda)^2 / [3]_q!$ evaluated at the
baryon level $n = 3$:*

$$
  w_{\mathrm{sym}} = w_{\mathrm{alt}}
  = \frac{1}{[3]_q!} \approx 0.165, \qquad
  w_{\mathrm{std}} = \frac{[2]_q^2}{[3]_q!} \approx 0.669
$$

*and:*
- *$\alpha = m_e \times 8G$ where $G \approx 0.9160$ is Catalan's
  constant and $\mathrm{Vol}(\mathcal{B}_3) = 8G$ (theorem, not
  numerical).*
- *$\hat{V}_i^{\mathrm{std}} = z \cdot a_i + b_i$ is the traced
  volume of generator $i$ (standard representation trace).*
- *$\lambda_i^{\mathrm{sym}} = \prod_j (c_j q + d_j)$ and
  $\lambda_i^{\mathrm{alt}} = \prod_j (-c_j q^{-1} + d_j)$ are
  the symmetric and alternating eigenvalue products.*

*All weights are derived from $q_0$.  The formula has
**zero fitted parameters**.*

*The additive formula regularises the near-zero generator
($\hat{V}^{\mathrm{std}} \approx 0.002$ for $A \geq 4$): the
symmetric and alternating channels contribute $O(1)$ terms that
pull $\hat{V}^{\mathrm{full}}$ away from zero, replacing the
logarithmic singularity $\ln|0.002| \approx -6.1$ with
$\ln|0.14| \approx -1.9$.*

**Brane tower correction.**
*The single-level formula above computes the traced volume at
brane level $n = 0$.  The full tower
([mass endomorphism tower](#prop:mass-endomorphism-tower))
adds per-generator $-\mathrm{Li}_2^q(-\lvert\hat{V}_i\rvert)$ terms
and adjacent cross-terms $z^2 \cdot (-\mathrm{Li}_2^q(-\lvert\hat{V}_i\hat{V}_j\rvert))$,
where $\mathrm{Li}_2^q(z) = \sum_{n\geq 1} z^n/(n[n]_q)$ is the
symmetric q-dilogarithm.
In the log-separated approximation, this is equivalent to
multiplying the base product by
$\mathrm{Li}_2(q^{-2}) \approx 1.098$ (adding
$\ln\mathrm{Li}_2(q^{-2}) \approx +0.094$ in log space).
The correction is uniform across generators because each
brane level $n$ contributes $q^{-2n}/n^2$ to the dilogarithm
series, independent of the crossing pattern.  Level~1
captures $73.9\%$ of the tower; levels $1$--$3$ capture
$94.3\%$; levels $1$--$10$ capture $99.75\%$.  The tower
correction is $< 1\%$ of the leading $\alpha\sum\ln|\hat V_i|$
term and does not materially change the accuracy.*

**Note on the additive formula vs the brane-tower correction (2026-05-03).**
*The leading additive form $\alpha\sum_i \ln|\hat V_i^{\mathrm{full}}|$
is **not** the q-dilogarithm $-\mathrm{Li}_2^q(-|\hat V_i|)$ of
the corrected mass-endomorphism-tower proposition: at $V \to 1$
the two functions disagree (one $\to 0$, the other bounded
$\to -\mathrm{Li}_2^q(-1)$).  Empirical comparison
(`li2q-six-term-probe.witness.json`):*

| atom | $\alpha\sum\ln\|V\|$ | $-\alpha\sum\mathrm{Li}_2^q(-\|V\|)$ |
|---|---|---|
| H ($Z=1$) | $-0.016\%$ | $-0.645\%$ |
| ⁴He | $+0.296\%$ | $+0.053\%$ |

*The additive formula above is the **leading-order** of the
proper $\mathrm{Li}_2^q$ form for $V$ in a specific range, with
the discrepancy growing as $V \to 1$ (heavy atoms).  The corrected
$-\mathrm{Li}_2^q(-V)$ form per
[mass endomorphism tower](#prop:mass-endomorphism-tower) is the
canonical Kashaev-limit specialisation; the $\alpha\sum\ln|V|$
form here is the practical leading-order approximation that gives
zero-fit predictions to $0.18\%$ mean across $Z = 1$..$20$.*

**Log-separated approximation.**
*The additive formula can be approximated by separating the
logarithms:*

$$
  \sum_i \ln\lvert \hat{V}_i^{\mathrm{full}} \rvert
  \approx
  \Phi_1 + \beta_2 \Phi_2 + \beta_3 \Phi_3
$$

*where $\Phi_1 = \sum \ln|\hat{V}^{\mathrm{std}}|$,
$\Phi_2 = \sum \ln|\det M_i|$,
$\Phi_3 = \sum \ln|\lambda^{\mathrm{sym}}/\lambda^{\mathrm{alt}}|$,
with $\beta_2 = -2[3]_q$ (motivated) and
$\beta_3 = (q - q^{-1})^2$ (derived; the
`WedderburnMassFormula.β₃` field in
[`atomic-braid-mass.lean`](atomic-braid-mass.lean)).
Both weights are determined by substrate constants — neither is
fitted.  This effective formula achieves $0.074\%$ mean error,
compared to $0.146\%$ for the exact additive formula.  Evaluating
$(q - q^{-1})^2$ at $q_0 = 1.109978595554181\ldots$ (50 dps) gives
$\beta_3 \approx 0.0437$; the closed-form expression corresponds
to $\mathcal{B}_3$ dressing of hydrogen and ordering effects in
heavy nuclei.*


## Neutron--proton mass splitting

**Proposition.**
*The neutron--proton mass difference is*

$$
  \Delta m = m_{\mathfrak{n}} - m_{\mathfrak{p}}
  = \alpha \cdot \lvert \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})
    - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d}) \rvert
  \approx 1.302 \; \mathrm{MeV}
$$

*where $\Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ and
$\Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ are the quantum
dilogarithm volumes of the proton and neutron quark orderings
respectively, and $\alpha = m_e \times 8G$ is the same binding
scale as in the atomic mass formula.*

*The splitting arises from replacing one
$\mathfrak{u}\mathfrak{u}$ crossing ($\sigma$, eigenvalue $q$)
with one $\mathfrak{d}\mathfrak{d}$ crossing ($\sigma^{-1}$,
eigenvalue $q^{-1}$).  The $\mathfrak{d}\mathfrak{d}$ crossing
has more confinement energy than $\mathfrak{u}\mathfrak{u}$,
making the neutron heavier.  CODATA: $\Delta m = 1.293$ MeV
(error: $0.63\%$).*


## Degree-2 color pairing

*The color-tube cubic $c^3 + a_2 c^2 + a_1 c + a_0 = 0$ has
four terms corresponding to four photon channels in
$\gamma\gamma \to \mathfrak{q}\mathfrak{q}\mathfrak{q}$
production:*

| Degree | Symmetric function | Integral | Physical role |
|:-------|:-------------------|:---------|:-------------|
| 3 | $\prod \mathrm{d}c_k/\mathrm{d}z$ | $I_3$ | confinement $\to m_{\mathfrak{p}}$ |
| 2 | $\sum_{i<j} \mathrm{d}c_i \cdot \mathrm{d}c_j$ | $I_2$ | color pairing $\to$ binding |
| 1 | $\sum \mathrm{d}c_k/\mathrm{d}z$ | $I_1$ | quark sum |
| 0 | $c_0 + z$ | $I_0$ | electron period |

*The degree-2 amplification ratio $A_2/A_3$ determines the weight
$\beta_2 = -2[3]_q$ in the mass formula.  The quantum 3-integer
$[3]_q$ arises because the baryon has three color channels: the
pairwise color pairing is weighted by the number of quark pairs
$\binom{3}{2} = 3$, deformed to $[3]_q$ at finite $q$.*


## Predicted vs observed masses

| $Z$ | Element | $A$ | $\mathcal{M}_{\mathrm{pred}}$ (MeV) | $\mathcal{M}_{\mathrm{obs}}$ (MeV) | $\Delta$ (MeV) | $\Delta/\mathcal{M}$ |
|:----|:--------|:----|:-------------------------------------|:------------------------------------|:----------------|:---------------------|
| 1 | H | 1 | 938.910 | 938.783 | $+0.127$ | $+0.014\%$ |
| 2 | He | 4 | 3734.624 | 3728.401 | $+6.223$ | $+0.167\%$ |
| 3 | Li | 7 | 6534.188 | 6535.367 | $-1.179$ | $-0.018\%$ |
| 4 | Be | 9 | 8378.704 | 8394.794 | $-16.090$ | $-0.192\%$ |
| 5 | B | 11 | 10237.301 | 10255.103 | $-17.802$ | $-0.174\%$ |
| 6 | C | 12 | 11168.874 | 11177.929 | $-9.056$ | $-0.081\%$ |
| 7 | N | 14 | 13029.983 | 13043.782 | $-13.799$ | $-0.106\%$ |
| 8 | O | 16 | 14890.701 | 14899.169 | $-8.468$ | $-0.057\%$ |
| 9 | F | 19 | 17690.792 | 17696.901 | $-6.109$ | $-0.035\%$ |
| 10 | Ne | 20 | 18615.219 | 18622.835 | $-7.617$ | $-0.041\%$ |
| 11 | Na | 23 | 21418.256 | 21414.830 | $+3.425$ | $+0.016\%$ |
| 12 | Mg | 24 | 22342.658 | 22341.908 | $+0.750$ | $+0.003\%$ |
| 13 | Al | 27 | 25143.149 | 25133.143 | $+10.005$ | $+0.040\%$ |
| 14 | Si | 28 | 26067.918 | 26060.344 | $+7.574$ | $+0.029\%$ |
| 15 | P | 31 | 28872.696 | 28851.873 | $+20.823$ | $+0.072\%$ |
| 16 | S | 32 | 29797.187 | 29781.800 | $+15.387$ | $+0.052\%$ |
| 17 | Cl | 35 | 32597.913 | 32573.283 | $+24.630$ | $+0.076\%$ |
| 18 | Ar | 40 | 37273.796 | 37224.719 | $+49.077$ | $+0.132\%$ |
| 19 | K | 39 | 36324.625 | 36294.464 | $+30.161$ | $+0.083\%$ |
| 20 | Ca | 40 | 37248.739 | 37213.777 | $+34.962$ | $+0.094\%$ |

Mean: $0.074\%$.  Maximum: $0.192\%$.  Zero fitted parameters.

**Witness**: `atom-mass-complete-wedderburn.witness.json`.
