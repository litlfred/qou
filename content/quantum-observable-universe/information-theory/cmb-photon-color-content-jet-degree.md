## Decomposition by jet degree

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

with $\mathbf{1}$ the photon identity (degree $0$),
$\sigma_0, \sigma_1$ the Hecke generators, and
$\sigma_0\sigma_1$ the Hopf link dressing.  The four
summands live at different jet degrees:

| Summand | Jet degree | Role | Survives horizon? |
|:---:|:---:|:---|:---:|
| $\mathbf{1}$ | $0$ | Photon identity (fibre value) | **No** |
| $\varphi_0\sigma_0$ | $1$ | Horizontal polarization (linear transport) | **Yes** |
| $\varphi_1\sigma_1$ | $1$ | Vertical polarization (linear transport) | **Yes** |
| $\varphi_{01}\sigma_0\sigma_1$ | $2$ | Hopf link dressing (quadratic transport) | **Yes** |

At a jet horizon $\mathcal{H}$
([jet horizon](#def:jet-horizon)), the degree-$0$
ideal $\mathfrak{h}$ annihilates $A_0$, so the photon
identity $\mathbf{1}$ vanishes.  But the degree-$1$ and degree-$2$ data
$A_1/A_0$ and $A_2/A_1$ are unconstrained: the color content
$(\varphi_0, \varphi_1, \varphi_{01})$ passes through.
