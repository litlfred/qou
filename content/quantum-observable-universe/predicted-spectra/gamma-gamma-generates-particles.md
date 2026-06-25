**Proposition ($\gamma\gamma$ production generates the operator basis).**
*Two independent photons, multiplied in the Iwahori--Hecke algebra
$H_3(q)$, reach every operator of the six-element basis
$\{\mathbf{1}, \sigma_0, \sigma_1, L_+, L_-, e^-\}$.  The photon together
with the elementary crossings therefore generates the whole particle
catalogue through pair production.*

Write the two colored photons with **independent** color weights
([breit-wheeler-pair-production](#def:breit-wheeler-pair-production)),

$$
  \gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
             + \varphi_{01}\sigma_0\sigma_1,
  \qquad
  \gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1
             + \psi_{01}\sigma_0\sigma_1 .
$$

Reducing $\gamma_1\cdot\gamma_2$ with the Hecke relation
$\sigma_i^2 = (q-q^{-1})\sigma_i + \mathbf{1}$ already places **five** of
the six basis operators in the three-term product
($\varphi_{01}=\psi_{01}=0$):

$$
  \operatorname{NF}(\gamma_1\gamma_2)
  = \underbrace{(1+\varphi_0\psi_0+\varphi_1\psi_1)}_{\mathbf{1}}
  + \underbrace{(\varphi_0+\psi_0+\varphi_0\psi_0\,h)}_{\sigma_0}\sigma_0
  + \underbrace{(\varphi_1+\psi_1+\varphi_1\psi_1\,h)}_{\sigma_1}\sigma_1
  + \underbrace{\varphi_0\psi_1}_{L_+}\sigma_0\sigma_1
  + \underbrace{\varphi_1\psi_0}_{L_-}\sigma_1\sigma_0 ,
  \qquad h = q-q^{-1}.
$$

The two chiral operators are generated **independently**: the $L_+$
coefficient is the cross-color product $\varphi_0\psi_1$ and the $L_-$
coefficient is $\varphi_1\psi_0$, so for any target pair $(a,b)$ the
weights $(\varphi_0,\varphi_1,\psi_0,\psi_1)=(a,b,1,1)$ realise
$L_+=a$ and $L_-=b$.  In particular $L_-=\sigma_1\sigma_0$ — which is
**absent from every single photon**, whose support is
$\{\mathbf{1},\sigma_0,\sigma_1,\sigma_0\sigma_1\}$ — is produced only by
the two-photon cross term.  Restoring the four-term coupling
$\varphi_{01}\neq 0$ opens the remaining basis operator
$e^-=\sigma_0\sigma_1\sigma_0$, the trefoil/electron channel
([breit-wheeler-pair-production](#def:breit-wheeler-pair-production)),
completing the basis.

Thus the span of the two-photon products is all of $H_3(q)$: the photon
and the elementary crossings generate the full operator catalogue, and
$\gamma\gamma$ production is the categorical mechanism by which light
assembles matter.

## Lean structure

The generative core is formalised in the sibling Lean file over a generic
commutative ring (the cross-color coefficients are purely algebraic, with
no $q_0$ specialization).  `gamma_gamma_chirality_surjective` proves that
the chiral pair $(L_+, L_-)$ is **jointly surjective** in the photon color
weights, and `gamma_gamma_reaches_Lminus` exhibits a two-photon product
carrying the $L_-=\sigma_1\sigma_0$ operator that no single photon can
hold.  The opening of $e^-$ under $\varphi_{01}\neq 0$ is inherited from
[breit-wheeler-pair-production](#def:breit-wheeler-pair-production).
