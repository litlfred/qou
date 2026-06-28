The photon color content model
([color content](#rem:knot-basis-color-content)) writes a
photon as

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1,
  \qquad \varphi_0, \varphi_1, \varphi_{01} \in R,
$$

where $\mathbf{1}$ is the photon identity (degree $0$),
$\sigma_0, \sigma_1$ are the Hecke generators, and
$\sigma_0\sigma_1$ is the Hopf link dressing
([Breit--Wheeler vertex](#rem:breit-wheeler-vertex)).  Each
generator corresponds to a polarization mode on the
exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$:
The generator $\sigma_0$ is horizontal polarization, $\sigma_1$ is vertical.

## The CMB is the surviving color content

The CMB boundary datum
([CMB boundary datum](#def:cmb-boundary-datum)) at a big
bang state $\mathcal{S}_0$ is exactly the degree $\geq 1$
jet data that survives the horizon.  For a collection of
photons $\{\gamma_k\}$ approaching the boundary, the
degree-$0$ identities $\mathbf{1}_k$ all vanish, but
their color weights $(\varphi_{0,k}, \varphi_{1,k})$
persist as sections of $A_1/A_0$.

The CMB is therefore the aggregate color content of
all photons at the boundary:

$$
  \mathrm{CMB}(\mathcal{S}_0)\big|_{\text{degree }1}
   \sim 
  \sum_k
  \bigl(\varphi_{0,k}\sigma_0 + \varphi_{1,k}\sigma_1\bigr).
$$

The two polarization components $\sigma_0$ and $\sigma_1$
manifest as the two independent polarization modes of the
CMB:

| CMB observable | Photon color content | Jet data |
|:---|:---|:---|
| Temperature anisotropy | $\varphi_{0,k} + \varphi_{1,k}$ (total color weight) | Trace of $A_1/A_0$ |
| $E$-mode polarization | $\varphi_{0,k} - \varphi_{1,k}$ (polarization asymmetry) | Difference of $\sigma_0, \sigma_1$ modes |
| $B$-mode polarization | Cross-terms $\varphi_{0,k}\varphi_{1,j}$ ($k \neq j$) | Degree-$2$ Hopf-link contributions ($L_{\pm}$) |

The degree-$2$ data ($A_2/A_0$) captures **linking** between
photons — precisely the Hopf-link terms $L_{\pm} =
\sigma_0\sigma_1$ and $\sigma_1\sigma_0$ from the product
formula ([color content](#rem:knot-basis-color-content)).
These are the pairwise correlations that produce the CMB
power spectrum.
