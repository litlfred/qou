*Two independent photons multiplied in the Iwahori--Hecke algebra $H_3(q)$ reach every operator of the six-element basis $\{\mathbf{1}, \sigma_0, \sigma_1, L_+, L_-, e^-\}$. The photon and the elementary crossings generate the whole particle catalogue through pair production.*

Write two colored photons with independent color weights:

$$
  \gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
             + \varphi_{01}\sigma_0\sigma_1^{-1},
  \qquad
  \gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1
             + \psi_{01}\sigma_0\sigma_1^{-1}.
$$

Reduce $\gamma_1\cdot\gamma_2$ with the Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + \mathbf{1}$. This places five of the six basis operators in the three-term product (where $\varphi_{01}=\psi_{01}=0$):

$$
\begin{aligned}
  \mathrm{NF}(\gamma_1\gamma_2)
  \;=\;& \underbrace{(1+\varphi_0\psi_0+\varphi_1\psi_1)}_{\mathbf{1}}
  + \underbrace{(\varphi_0+\psi_0+\varphi_0\psi_0\,h)}_{\sigma_0}\sigma_0
  + \underbrace{(\varphi_1+\psi_1+\varphi_1\psi_1\,h)}_{\sigma_1}\sigma_1
  \\[2pt]
  &+ \underbrace{\varphi_0\psi_1}_{L_+}\sigma_0\sigma_1
  + \underbrace{\varphi_1\psi_0}_{L_-}\sigma_1\sigma_0 ,
  \qquad h = q-q^{-1}.
\end{aligned}
$$

The two chiral operators are generated independently. The $L_+$ coefficient is the cross-color product $\varphi_0\psi_1$. The $L_-$ coefficient is $\varphi_1\psi_0$. For any target pair $(a,b)$, the weights $(\varphi_0,\varphi_1,\psi_0,\psi_1)=(a,b,1,1)$ realise $L_+=a$ and $L_-=b$. The operator $L_-=\sigma_1\sigma_0$ is absent from any single photon. Since $\sigma_1^{-1} = \sigma_1 - h\mathbf{1}$, the fourth term is $\sigma_0\sigma_1^{-1} = \sigma_0\sigma_1 - h\sigma_0$, so the normal-form support of a single photon is contained in $\{\mathbf{1},\sigma_0,\sigma_1,\sigma_0\sigma_1\}$. The two-photon cross term produces $L_-$. Restoring the vertex weights $\varphi_{01}, \psi_{01}$ opens the remaining basis operator $e^-=\sigma_0\sigma_1\sigma_0$, with coefficient $\varphi_{01}\psi_0 + \varphi_1\psi_{01}$. This completes the basis. The full four-term product, with all six coefficients, is [Table 5](#tbl:trivial-knot-photon-interpretation-table5-data); its coefficients are polynomials of degree $3$ in $h$.

The span of the two-photon products is all of $H_3(q)$.
