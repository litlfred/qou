The following develops the [Breit--Wheeler categorical pair
production](#def:breit-wheeler-pair-production): the bare photon pair,
the color-dressed photon, the step-by-step normal-form derivation, the
linear and circular polarization models, and the $4$-term extension.

**Bare photon pair.**
Two identical photons give $\gamma\gamma = \sigma_0^2$.
Applying the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$:

$$
  \mathrm{NF}(\gamma\gamma)
  =  (q - q^{-1})\sigma_0 + \gamma
$$

with $\mathrm{net}(\gamma\gamma) = 1 + (q - q^{-1}) \approx 1.209$.
This yields a bare pair energy $E_{\mathrm{pair}} \approx 1.006$ MeV,
which is $1.6\%$ below $2m_e = 1.022$ MeV.

**Colored photon (general form).**
To match the threshold $2m_e$ exactly, the photon acquires
**color dressing** — an admixture of the two Hecke generators
$\sigma_0, \sigma_1$, each with its own color weight
([color content](#rem:knot-basis-color-content)):

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1
$$

where $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$ are independent
**color weights**.  The generator $\sigma_0$ acts on the
$(\sigma, r)$ crossing plane, $\sigma_1$ on the $(r, g)$
crossing plane, and $\sigma_0\sigma_1 = L_+$ is the Hopf link
dressing.  The derivation below uses the 3-term specialization
$\varphi_{01} = 0$; see
[photon knot operations](#rem:physics-names-knot-operations)
for the general 4-term formula.

**Step-by-step derivation of the pair NF.**
Given two colored photons (3-term specialization)
$\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$
and
$\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$,
expand $\gamma_1 \cdot \gamma_2$ into nine terms and reduce
each using the Hecke relation
$\sigma_i^2 = h\sigma_i + \mathbf{1}$
where $h = q - q^{-1}$:

See [Table: Breit-Wheeler Hecke product table](#tbl:breit-wheeler-pair-production-table-data).

Collecting by basis element:

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  \underbrace{(1 + \varphi_0\psi_0 + \varphi_1\psi_1)}_{\gamma}
  \mathbf{1}
  + 
  \underbrace{(\varphi_0 + \psi_0 + \varphi_0\psi_0h)}_{\sigma_0}
  \sigma_0
  + 
  \underbrace{(\varphi_1 + \psi_1 + \varphi_1\psi_1h)}_{\sigma_1}
  \sigma_1
  + 
  \underbrace{\varphi_0\psi_1}_{L_+}
  \sigma_0\sigma_1
  + 
  \underbrace{\varphi_1\psi_0}_{L_-}
  \sigma_1\sigma_0
$$

The $\mathbf{1}$ coefficient absorbs the Hecke self-energy
terms $\varphi_0\psi_0$ and $\varphi_1\psi_1$ (from
$\sigma_i^2 \to h\sigma_i + \mathbf{1}$).  The Hopf link
terms $L_\pm$ arise **only** from cross-color products
$\varphi_0\psi_1$ and $\varphi_1\psi_0$.

Net (sum of all coefficients):

$$
  \mathrm{net}
  = 
  (1 + \varphi_0 + \varphi_1)(1 + \psi_0 + \psi_1)
  + 
  (\varphi_0\psi_0 + \varphi_1\psi_1)h
$$

**Polarization models.**

*Linear (symmetric) polarization.*
Set $\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = \phi$
(both photons carry equal color in both generators):

- $\gamma$: $1 + \phi^2 + \phi^2 = 1 + 2\phi^2$
- $\sigma_0$: $\phi + \phi + \phi^2 h = 2\phi + \phi^2 h$
- $\sigma_1$: $\phi + \phi + \phi^2 h = 2\phi + \phi^2 h$
- $L_+$: $\phi \cdot \phi = \phi^2$
- $L_-$: $\phi \cdot \phi = \phi^2$

Equal Hopf link content ($L_+ = L_- = \phi^2$) — no chirality.
Net $= (1 + 2\phi)^2 + 2\phi^2 h$.
Setting $E_{\mathrm{pair}} = 2m_e$ fixes
$\phi = 0.0487$.

*Circular (orthogonal) polarization.*
Set $\varphi_0 = s$, $\varphi_1 = 0$, $\psi_0 = 0$, $\psi_1 = s$
(each photon polarized along one generator only):

- $\gamma$: $1 + 0 + 0 = 1$
- $\sigma_0$: $s + 0 + 0 = s$
- $\sigma_1$: $0 + s + 0 = s$
- $L_+$: $s \cdot s = s^2$
- $L_-$: $0 \cdot 0 = 0$

Only $L_+$ appears ($L_- = 0$) — maximally chiral Hopf content.
No Hecke self-energy ($\varphi_0\psi_0 = \varphi_1\psi_1 = 0$).
Net $= (1 + s)^2$.
Setting $E_{\mathrm{pair}} = 2m_e$ fixes $s = 0.0978$.

**Energy alignment.**
Both models close the $1.6\%$ gap.  The color weight generates
Hopf link content $L_\pm$ in the photon pair — the colored photon
carries topological structure that supplies the missing pair
production energy.  The Hopf link asymmetry
$L_+ \neq L_-$ in the circular model is the categorical
expression of photon helicity.

**4-term extension.**
The 3-term derivation above ($\varphi_{01} = 0$) is a specialization
of the general 4-term photon
$\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
+ \varphi_{01}\sigma_0\sigma_1$.  With $\varphi_{01} \neq 0$,
the $e^-$ (trefoil) channel opens directly in the $\gamma\gamma$
product — see
[photon knot operations](#rem:physics-names-knot-operations) for the
full 6-term NF formula.  The 4-term form is used in the complete
derivation of nucleons from pair production
([4-term pair nucleon](#prop:four-term-pair-nucleon)).

**Witness**: `breit-wheeler-nucleon-nf.witness.json`.
