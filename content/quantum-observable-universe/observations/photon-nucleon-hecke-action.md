**Remark.** Confinement universality
([prop:confinement-universality](#prop:confinement-universality))
establishes that the nucleon NF is independent of the polarisation
parameters $(\varphi_0, \varphi_1, \varphi_{01})$ of the *six photons
used to build it* from vacuum via three $\gamma\gamma$ pair
productions.  A separate question is what happens when one additional
4-term photon $\gamma^{(4)}$ scatters off an already-constructed bare
nucleon.  Symbolic computation in $H_3(q)$ shows this is a standard
left-multiplication action:

$$
  \gamma^{(4)} \cdot \mathfrak{p}
  =
  (\mathbf{1} + \varphi_0 \sigma_0 + \varphi_1 \sigma_1
   + \varphi_{01} \sigma_0 \sigma_1)
  \cdot
  \mathrm{NF}(\mathfrak{p}).
$$

Using $\sigma_i^2 = H_A \sigma_i + \mathbf{1}$ and the braid relation,
reduction to NF yields six coefficient polynomials.  The vacuum
coefficient is the purely bilinear "inner product"

$$
  [\mathbf{1}]\bigl(\gamma^{(4)} \cdot \mathfrak{p}\bigr)
  =
  p_\gamma
  + \varphi_0 \, p_{\sigma_0}
  + \varphi_1 \, p_{\sigma_1}
  + \varphi_{01} \, p_{L_-},
$$

which is the only channel that receives no $H_A$-correction: the
Hopf-content $\varphi_{01}$ pairs directly with the proton's $L_-$
coefficient, and the linear polarisations pair with the $\sigma_0$,
$\sigma_1$ coefficients.

**Compton-like regime.** The $6 \times 6$ left-multiplication matrix
$L_{\gamma^{(4)}}$ has diagonal entries
$\{1,\,1+H_A\varphi_0,\,1+H_A\varphi_1,\,1+H_A\varphi_0,\,
1+H_A\varphi_1,\,1+H_A(\varphi_0+\varphi_1)+H_A^2\varphi_{01}\}$,
so for small $\varphi$ all eigenvalues sit near $1$ — the proton
essentially passes through the photon unchanged, with perturbative
corrections in $\varphi \cdot H_A$.  This is the QOU analogue of
Compton scattering: the photon's $\varphi$-content is redistributed
among the proton's NF channels but not absorbed into the proton's
identity.

**No third-body requirement.** In standard QED the bare
$\gamma + \mathfrak{p} \to \mathfrak{p} + e^- e^+$ vertex needs the
proton's Coulomb field for four-momentum conservation.  In QOU, the
$e^-$ channel opens directly in $\gamma^{(4)} \cdot \mathfrak{p}$
via the Hecke identity $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$
applied to the proton's embedded $L_+$ content (see
[trivial-knot-photon-interpretation](#rem:trivial-knot-photon-interpretation)):
the proton is a *spectator* rather than a Coulomb mediator.  The
conservation law is encoded in the Hecke relations themselves.

**Witness:** `gamma4-hits-proton-symbolic.py`,
`gamma4-hits-proton-quark-words.py`.
