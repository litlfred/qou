A photon decomposes into identity and color components. The photon color content model  writes a photon as:

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1,
  \qquad \varphi_0, \varphi_1, \varphi_{01} \in R.
$$

Here $\mathbf{1}$ is the degree-$0$ photon identity, $\sigma_0, \sigma_1$ are the Hecke generators, and $\sigma_0\sigma_1$ is the Hopf link dressing . Each generator maps to a polarization mode on the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$. The generator $\sigma_0$ provides horizontal polarization; $\sigma_1$ provides vertical.

## Decomposition by jet degree

The four summands distribute across jet degrees.

| Summand | Jet degree | Role | Survives horizon? |
|:---:|:---:|:---|:---:|
| $\mathbf{1}$ | $0$ | Photon identity (fibre value) | **No** |
| $\varphi_0\sigma_0$ | $1$ | Horizontal polarization (linear transport) | **Yes** |
| $\varphi_1\sigma_1$ | $1$ | Vertical polarization (linear transport) | **Yes** |
| $\varphi_{01}\sigma_0\sigma_1$ | $2$ | Hopf link dressing (quadratic transport) | **Yes** |

At a jet horizon $\mathcal{H}$ , the degree-$0$ ideal $\mathfrak{h}$ annihilates $A_0$, removing the photon identity $\mathbf{1}$. Because the higher-degree quotients $A_1/A_0$ and $A_2/A_1$ are unconstrained, the color content $(\varphi_0, \varphi_1, \varphi_{01})$ survives the horizon.

## Surviving color content

The CMB boundary datum  at a big bang state $\mathcal{S}_0$ collects the degree $\geq 1$ jet data surviving the horizon. As a collection of photons $\{\gamma_k\}$ approaches the boundary, their degree-$0$ identities $\mathbf{1}_k$ vanish. Their color weights $(\varphi_{0,k}, \varphi_{1,k})$ persist as sections of $A_1/A_0$.

The CMB aggregates the color content of the boundary photons:

$$
  \mathrm{CMB}(\mathcal{S}_0)\big|_{\text{degree }1}
   \sim 
  \sum_k
  \bigl(\varphi_{0,k}\sigma_0 + \varphi_{1,k}\sigma_1\bigr).
$$

The components $\sigma_0$ and $\sigma_1$ determine the independent polarization modes of the CMB.

| CMB observable | Photon color content | Jet data |
|:---|:---|:---|
| Temperature anisotropy | $\varphi_{0,k} + \varphi_{1,k}$ (total color weight) | Trace of $A_1/A_0$ |
| $E$-mode polarization | $\varphi_{0,k} - \varphi_{1,k}$ (polarization asymmetry) | Difference of $\sigma_0, \sigma_1$ modes |
| $B$-mode polarization | Cross-terms $\varphi_{0,k}\varphi_{1,j}$ ($k \neq j$) | Degree-$2$ Hopf-link contributions ($L_{\pm}$) |

The degree-$2$ data ($A_2/A_0$) detects linking between photons. It isolates the Hopf-link terms $L_{\pm} = \sigma_0\sigma_1$ and $\sigma_1\sigma_0$ from the product formula . These pairwise correlations generate the CMB power spectrum.

## Condensation

The initial Planck step condenses the CMB back into particles. When the Reeb flow $f_q$ acts on the boundary datum , the degree-$1$ color content $(\varphi_0, \varphi_1)$ reconstitutes degree-$0$ identities via the Hecke relation:

$$
  \sigma_i^2
  = 
  (q - q^{-1})\sigma_i + \mathbf{1}.
$$

Each color mode iterates to generate a photon identity $\mathbf{1}$ (the constant term) alongside a residual color mode $\sigma_i$ (the linear term). The Hecke self-energy algebraically converts surviving polarization data into particle states.
