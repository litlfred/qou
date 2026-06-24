**Proposition (explicit $\alpha_k$ at $H_3(R, q)$).**
*Let $z = 1/(q^{1/2} + q^{-1/2})$ be the Markov parameter and
$h = q - q^{-1}$ the Hecke amplitude. The structural prefactors of
the unified curvature-rank mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
at the single-nucleon Hecke algebra $H_3(R, q)$ are*

$$
  \boxed{\;
    \alpha_0 \,=\, 1, \qquad
    \alpha_1 \,=\, 0, \qquad
    \alpha_2 \,=\, z^2, \qquad
    \alpha_3 \,=\, h\,z^2 + z \,=\, z\,\bigl(1 + q^{1/2} - q^{-1/2}\bigr).
  \;}
$$

*All four are explicit q-algebraic — no transcendental constants, no
fitting.*

## Alternative derivation via Wenzl-bridge

By [Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q)$ at $H_3$ admits the closed form
$y_\lambda = s_{\lambda, r}(Q) / \sum_\mu d_\mu s_{\mu, r}(Q)$ with
$Q = q^2$ and $X = Q^r = q^{3/2}/(1 + q - q^2 - q^3 + q^{3/2})$. The
Markov pairings $\alpha_k = \langle \mathrm{tr}_M, r_k \rangle$ on the
four $E_\infty$ classes inherit this $q$-rational structure
automatically; the per-class derivations below can be replaced by a
uniform application of the bridge formula (see also
[recipe](#prop:y-lambda-recipe-from-partition)).

## Alternative derivation via Wenzl-bridge

By [Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q)$ at $H_3$ admits the closed form
$y_\lambda = s_{\lambda, r}(Q) / \sum_\mu d_\mu s_{\mu, r}(Q)$ with
$Q = q^2$ and $X = Q^r = q^{3/2}/(1 + q - q^2 - q^3 + q^{3/2})$. The
Markov pairings $\alpha_k = \langle \mathrm{tr}_M, r_k \rangle$ on the
four $E_\infty$ classes inherit this $q$-rational structure
automatically; the per-class derivations below can be replaced by a
uniform application of the bridge formula (see also
[recipe](#prop:y-lambda-recipe-from-partition)).

## Significance

This proposition closes the H_3 stratum-prefactor derivation that the
[unified mass formula](#prop:unified-curvature-rank-mass-formula) and
[plancherel-term-7-formulation](#prop:plancherel-term-7-formulation)
left implicit ("stratum-dependent prefactors $\alpha_k$"). All four
$\alpha_k$ are now explicit q-algebraic functions — no transcendental
constants, no per-isotope fitting.

For $\alpha_{k \geq 4}$, the universal prefactor
$m_e \cdot 8 G$ ([gravity spectral prefactor](#prop:gravity-spectral-prefactor))
is the Newton's-constant identification at the deep-tower stratum.

## Open

- **$\alpha_1$ disambiguation.** Two distinct objects share the
 symbol "$\alpha_1$":

 *(i) Spectral-sequence $\alpha_1$* (this proposition): the Markov
 pairing of $\mathrm{tr}_M$ with the alternating-pair representative
 $[\sigma_1 - \sigma_2]$. This vanishes by cyclicity of the Markov
 trace ($\alpha_1 = 0$ exactly). At generic $q$,
 $\mathrm{HH}^k(H_n(R, q)) = 0$ for $k \geq 1$
 ([spectral sequence collapse](#prop:spectral-sequence-collapse)),
 The Gerstenhaber bracket has empty target on the surviving
 $\mathrm{HH}^0$ — the spectral-sequence $\alpha_1$ is
 **structurally forced to zero**, not only an artifact of
 representative choice.

 *(ii) Plancherel-mass depth-1 contribution* (in the unified mass
 formula): the depth-1 stratum $\Lambda_1 = \{(n - 1, 1)\}$ has
 Plancherel-mass weight $y_{(n-1, 1)} \neq 0$
 ([procedure](#prop:alpha-k-derivation-procedure)). At $H_3$:
 $y_{(2, 1)} \approx 0.281$ — non-zero and structurally extracted
 from the witness, contributing
 $0.281 \cdot \chi_{(2, 1)}(\beta) \cdot \log|\chi_{(2, 1)}(\beta)|$
 to the unified mass formula at every nucleon.

 The unified mass formula uses sense (ii); the spectral-sequence
 vanishing in sense (i) does **not** imply the depth-1 stratum is
 empty.

- **$\alpha_k$ at $H_n$ for $n \geq 6$.** The analogous derivation
 for multi-nucleon Hecke algebras requires explicit $E_\infty^{p, *}$
 pages at higher $H_n$, generalising
 [$H_3$ explicit pages](#prop:spectral-sequence-h3-explicit).

## Witness

[`computations/alpha/alpha_k_jones_markov_h3.py`](#)
implements the Jones-Markov linear system and the explicit Markov
pairings. Produces witness `alpha-k-jones-markov-h3.witness.json`
with $\alpha_2 = z^2$ verified to $10^{-17}$ and $\alpha_3 = h z^2 + z$
verified to numerical precision.
