The **Breit--Wheeler process** is the categorical pair production
$\gamma\gamma \to e^- e^+$: two photons fuse into an
electron--positron pair.  In the Iwahori--Hecke algebra $H_3(q)$,
the process is the identity

$$
  \gamma_1 \cdot \gamma_2
  = 
  \mathrm{NF}(e^-) + \mathrm{NF}(e^+)
  +  \text{binding energy}
$$

where the photon, electron, and positron are the braid words

$$
  \gamma = \sigma_0, \qquad
  e^- = \sigma_0\sigma_1\sigma_0  \text{(trefoil)}, \qquad
  e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}  \text{(mirror trefoil)}.
$$

**Bare photon pair.**
Two identical photons give $\gamma\gamma = \sigma_0^2$.
Applying the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$:

$$
  \mathrm{NF}(\gamma\gamma)
  =  (q - q^{-1})H^0 + \gamma
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
$$

where $\varphi_0, \varphi_1 \in \mathbb{R}$ are independent
**color weights**.  The generator $\sigma_0$ acts on the
$(\sigma, r)$ crossing plane and $\sigma_1$ on the $(r, g)$
crossing plane — two orthogonal polarization modes.

**Step-by-step derivation of the pair NF.**
Given two colored photons
$\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$
and
$\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$,
expand $\gamma_1 \cdot \gamma_2$ into nine terms and reduce
each using the Hecke relation
$\sigma_i^2 = h\sigma_i + \mathbf{1}$
where $h = q - q^{-1}$:

| Term | Product | Hecke reduction |
|:---|:---|:---|
| $\mathbf{1} \cdot \mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ |
| $\mathbf{1} \cdot \psi_0\sigma_0$ | $\psi_0\sigma_0$ | $\psi_0\sigma_0$ |
| $\mathbf{1} \cdot \psi_1\sigma_1$ | $\psi_1\sigma_1$ | $\psi_1\sigma_1$ |
| $\varphi_0\sigma_0 \cdot \mathbf{1}$ | $\varphi_0\sigma_0$ | $\varphi_0\sigma_0$ |
| $\varphi_0\sigma_0 \cdot \psi_0\sigma_0$ | $\varphi_0\psi_0\sigma_0^2$ | $\varphi_0\psi_0h\sigma_0 + \varphi_0\psi_0\mathbf{1}$ |
| $\varphi_0\sigma_0 \cdot \psi_1\sigma_1$ | $\varphi_0\psi_1\sigma_0\sigma_1$ | $\varphi_0\psi_1L_+$ |
| $\varphi_1\sigma_1 \cdot \mathbf{1}$ | $\varphi_1\sigma_1$ | $\varphi_1\sigma_1$ |
| $\varphi_1\sigma_1 \cdot \psi_0\sigma_0$ | $\varphi_1\psi_0\sigma_1\sigma_0$ | $\varphi_1\psi_0L_-$ |
| $\varphi_1\sigma_1 \cdot \psi_1\sigma_1$ | $\varphi_1\psi_1\sigma_1^2$ | $\varphi_1\psi_1h\sigma_1 + \varphi_1\psi_1\mathbf{1}$ |

Collecting by basis element:

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  \underbrace{(1 + \varphi_0\psi_0 + \varphi_1\psi_1)}_{\gamma}
  \mathbf{1}
  + 
  \underbrace{(\varphi_0 + \psi_0 + \varphi_0\psi_0h)}_{H^0}
  \sigma_0
  + 
  \underbrace{(\varphi_1 + \psi_1 + \varphi_1\psi_1h)}_{H^1}
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
- $H^0$: $\phi + \phi + \phi^2 h = 2\phi + \phi^2 h$
- $H^1$: $\phi + \phi + \phi^2 h = 2\phi + \phi^2 h$
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
- $H^0$: $s + 0 + 0 = s$
- $H^1$: $0 + s + 0 = s$
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

**Witness**: `breit-wheeler-nucleon-nf.witness.json`.
