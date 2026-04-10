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
| $\mathfrak{p}\mathfrak{n}$ | $\tfrac{1}{2}(\sigma + \sigma^{-1})$ | $2$ | $-(q - q^{-1})$ | strong mixed (doubled) |
| $\mathfrak{p}e$ | $\sigma^{-1}$ | $1$ | $-(q - q^{-1})$ | EM attraction |
| $\mathfrak{n}e$ | $\mathrm{id}$ | $0$ | $1$ | no interaction |
| $ee$ | $\sigma$ | $1$ | $0$ | EM repulsion |

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

**Proposition.**
*The mass of a neutral atom $(Z, N)$ is*

$$
  \mathcal{M}(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  + \alpha \bigl(\Phi_1 - 2[3]_q \cdot \Phi_2 + H_A^2 \cdot \Phi_3\bigr)
$$

*where the three Wedderburn invariants of the $2 \times 2$
transfer matrix chain are:*

$$
  \Phi_1 = \sum_i \ln\lvert \hat{V}_i \rvert, \qquad
  \Phi_2 = \sum_i \ln\lvert \det M_i \rvert, \qquad
  \Phi_3 = \sum_i \ln\left\lvert \frac{\lambda_i^{\mathrm{sym}}}
    {\lambda_i^{\mathrm{alt}}}\right\rvert
$$

*and:*
- *$\alpha = m_e \times 8G$ where $G \approx 0.9160$ is Catalan's
  constant and $\mathrm{Vol}(\mathcal{B}_3) = 8G$ (theorem, not
  numerical).*
- *$[3]_q = (q^3 - q^{-3})/(q - q^{-1})$ is the quantum
  3-integer (baryon degree).*
- *$H_A = q - q^{-1}$ is the Hecke parameter.*
- *$\hat{V}_i = z \cdot a_i + b_i$ is the traced volume of
  generator $i$ (standard representation trace).*
- *$\det M_i$ is the determinant of the $2 \times 2$ transfer
  matrix for generator $i$ (equal to
  $\lambda_i^{\mathrm{sym}} \cdot \lambda_i^{\mathrm{alt}}$).*
- *$\lambda_i^{\mathrm{sym}} / \lambda_i^{\mathrm{alt}}$ is the
  ratio of symmetric to alternating eigenvalues (chirality).*

*These three invariants are **complete**: the Wedderburn
decomposition of $H_n(q)$ has three blocks (symmetric, standard,
alternating), and the transfer matrix chain produces exactly three
independent scalar invariants per generator.  No higher-degree
invariants exist.*

*All quantities are derived from $q_0$ and $m_e$.  The formula has
**zero fitted parameters**.*


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
