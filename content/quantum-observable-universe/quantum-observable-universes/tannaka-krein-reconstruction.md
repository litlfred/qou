Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$.
Then the coend

$$
  H =  \mathrm{End}^{\otimes}(\tau)
  =  \int^{X \in \mathbf{C}}
  \tau(X)^{\vee} \otimes_R \tau(X)
$$

carries a canonical Hopf algebra structure
$(\mu, \eta, \Delta, \varepsilon, S)$ such that:

1. **Reconstruction.** There is a monoidal equivalence
   $\mathbf{C} \simeq \mathrm{Rep}(H)$ under which $\tau$
   corresponds to the forgetful functor
   $U \colon \mathrm{Rep}(H) \to R\text{-}\mathrm{Mod}$.

2. **Universal property.** $H$ is the *universal* Hopf algebra
   through which $\tau$ factors: for every Hopf algebra $H'$ and
   monoidal natural transformation
   $\alpha \colon \tau \Rightarrow U \circ F$ (where
   $F \colon \mathbf{C} \to \mathrm{Rep}(H')$), there exists
   a unique Hopf map $\phi \colon H \to H'$ with
   $\alpha = U(\phi) \circ \mathrm{can}$.

3. **Naturality in $\tau$.** The group of monoidal natural
   automorphisms of $\tau$ is
   $\mathrm{Aut}^{\otimes}(\tau) \cong G(H)$, the group-like
   elements (characters) of $H$.

In the classical case ($\mathbf{C}$ symmetric), this is Tannaka's
theorem \cite{tannaka1939} as algebraised by Deligne \cite{deligne1990}:
The sheaf $H = \mathcal{O}(G)$ is the coordinate ring of a compact group $G$,
and $\mathrm{Aut}^{\otimes}(\tau) \cong G$.

In the quantum case ($\mathbf{C}$ braided but not symmetric), the
reconstruction is due to Woronowicz \cite{woronowicz1988}: $H$ is
a compact quantum group algebra $\mathcal{O}_q(G)$, and the braiding
$c_{V,W}$ on $\mathbf{C}$ encodes the universal $R$-matrix of $H$.
The deformation parameter $q$ is *not* an external input — it is
determined by the braiding, as shown in
([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction)).
