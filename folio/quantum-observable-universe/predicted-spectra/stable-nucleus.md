A **stable nucleus** is a multi-nucleon Hopf link that extremizes the Skein binding Lagrangian ([Skein binding Lagrangian](#def:skein-binding-lagrangian)).

Let $\mathfrak{p}$ and $\mathfrak{n}$ be the categorical proton and neutron ([categorical proton](#def:categorical-proton), [categorical neutron](#def:categorical-neutron)). A **nucleus** with $Z$ protons and $N$ neutrons is the iterated Hopf link. (Here $Z$ is the **atomic number**, the standard nuclear physics notation for the proton count, freeing $p$ for use as a brane point.)

$$
  \mathcal{N}(Z, N)
  = 
  \underbrace{\mathfrak{p} \oplus \cdots \oplus \mathfrak{p}}_{Z}
   \oplus 
  \underbrace{\mathfrak{n} \oplus \cdots \oplus \mathfrak{n}}_{N}.
$$

The nucleus $\mathcal{N}(Z, N)$ is **stable** if $(Z, N)$ is a critical point of the Skein binding Lagrangian $\mathcal{L}_{\mathrm{bind}}$ ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) under beta variation (exchange of $\mathfrak{p} \leftrightarrow \mathfrak{n}$ at fixed $A = Z + N$):

$$
  \frac{\partial \mathcal{L}_{\mathrm{bind}}}{\partial Z}
  \bigg|_{A}
  = 0
  \qquad \Longleftrightarrow \qquad
  Z = \frac{A}{2 + a_C  A^{2/3} / (2a_A)},
$$

where $a_C = (q - q^{-1}) \cdot \lambda_C$ and $a_A$ is the Pauli coefficient ([beta-stability](#prop:beta-stability)).

A **stable atom** appends $Z$ electrons:

$$
  \mathcal{A}(Z, N)
  = 
  \mathcal{N}(Z, N)  \oplus  Z \cdot T_{2,3}.
$$

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. This block invokes real- and complex-analytic constructs, including real-valued physical observables, real-analytic bounds, transcendental constants, and numerical evaluation at the substrate parameter $q_0$. Any generic categorical or $q$-deformation identities drawn upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
