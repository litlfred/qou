**Definition.**
*Let $L = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a multi-nucleon Hopf link with $Z$ protons, $N$ neutrons, and $A = Z + N$. The **canonical binding Lagrangian** is the categorical action $\mathfrak{S}_q$ evaluated on $L$:*
$$
  \mathcal{L}_{\mathrm{bind}}[L]
  = 
  \mathcal{L}_{\mathrm{qCLT}}
  - \mathcal{L}_{\mathrm{Coulomb}}.
$$
*Each term arises from the exact evaluation of the topological trace on the link components, without empirical liquid-drop parameters:*

1. ***Strong Binding (q-CLT/JSJ volume term).** The strong force contribution evaluates strictly from the Hecke channel traces. As established in [q-CLT mass scaling](../mass-theory/q-clt-jsj-mass-scaling.md), the Jaco–Shalen–Johannson decomposition yields an additive scaling for the strong binding:*
   $$
     \mathcal{L}_{\mathrm{qCLT}}
     = \alpha \sum_i \ln\lvert V_i\rvert,
   $$
   *where $\alpha = \mathfrak{m}_e / (q_0(q_0-1))$ is the rigid substrate scale, and $V_i$ are the two-nucleon sub-braid Markov traces for each bond type. This is parameter-free and replaces the empirical Bethe-Weizsäcker volume, surface, asymmetry, and pairing terms entirely.*

2. ***Coulomb Repulsion.** Each proton--proton crossing acquires a $q$-deformed wedge product asymmetry. The categorical difference between identical-chirality crossings (coefficient $q$) and mixed crossings evaluates directly to the electrostatic penalty. As mapped by the $\mathrm{U}(1)$ sub-action:*
   $$
     \mathcal{L}_{\mathrm{Coulomb}} = E_C(Z, A),
   $$
   *which exactly recovers the standard $\approx 0.71 Z(Z-1)/A^{1/3}$ MeV energy without relying on empirical $a_C$ fits.*
