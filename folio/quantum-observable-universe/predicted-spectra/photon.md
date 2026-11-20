**Definition (photon).** Let $R$ be a commutative ring and let $H_3(R,q)$ be the Iwahori--Hecke algebra with generators $\sigma_0, \sigma_1$. The :defterm[photon]{#photon} with :defterm[colour weights]{#colour-weights} $(\varphi_0, \varphi_1, \varphi_{01}) \in R^3$ is the four-term element

$$
  \gamma(\varphi) \;=\; \mathbf{1} + \varphi_0\,\sigma_0 + \varphi_1\,\sigma_1 + \varphi_{01}\,\sigma_0\sigma_1^{-1} \;\in\; H_3(R,q).
$$

A photon has three parameters and four terms. Its fourth term is the chiral pair-production vertex $V = \sigma_0\sigma_1^{-1}$, the $\gamma\bar\gamma$ vertex: one positive crossing on the strands $(0,1)$ and one negative crossing on the strands $(1,2)$. The weight $\varphi_{01}$ is the vertex weight. With $h = q - q^{-1}$ the Hecke relation gives $\sigma_1^{-1} = \sigma_1 - h\mathbf{1}$, so $V = L_+ - h\sigma_0$ with $L_+ = \sigma_0\sigma_1$, and

$$
  \gamma(\varphi_0, \varphi_1, \varphi_{01}) \;=\; \mathbf{1} + (\varphi_0 - h\varphi_{01})\,\sigma_0 + \varphi_1\,\sigma_1 + \varphi_{01}\,L_+ .
$$

In the normal-form basis of $H_3(R,q)$ the support of a photon is therefore contained in $\{\mathbf{1}, \sigma_0, \sigma_1, L_+\}$.

The :defterm[bare photon]{#bare-photon} is $\gamma(0,0,0) = \mathbf{1}$, the empty knot. It is the identity element, not the unknot $0_1$, which is a closed strand and denotes the neutrino ([notation](#prose:notation-collisions)).

Four consequences of the definition fix how the word is used elsewhere:

1. A single crossing $\sigma_i$ is not a photon. It is the $\sigma_i$-term of a photon's support.
2. The form $\mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$ is the specialisation $\varphi_{01} = 0$, not a second definition.
3. $L_- = \sigma_1\sigma_0$ and $e^- = \sigma_0\sigma_1\sigma_0$ are not in the normal-form support of one photon. They first appear in the product $\gamma(\varphi)\gamma(\psi)$ of two photons ([$\gamma\gamma$ generation](#prop:gamma-gamma-generates-particles)).
4. The Borromean braid is a product of two photons that carry only their vertex term: $(\sigma_0\sigma_1^{-1})^3 = \gamma(0,0,qh)\,\gamma(0,0,-q^{-1}h)$ ([two-photon factorisation](#prop:borromean-two-photon-factorisation)).
