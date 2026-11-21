**Normal form.** After Gröbner--Shirshov reduction, each nucleon reduces to exactly six terms, one for each basis element of $H_3(R, q)$:

$$
  \mathfrak{N}
  = 
  c_\gamma\mathbf{1}
  + c_{\sigma_0}\sigma_0
  + c_{\sigma_1}\sigma_1
  + c_{L_+}\sigma_0\sigma_1
  + c_{L_-}\sigma_1\sigma_0
  + c_{e^-}\sigma_0\sigma_1\sigma_0
$$

The coefficients $c_\bullet \in \mathbb{Z}[q, q^{-1}]$ encode the particle content of the nucleon: the photon channel $\gamma$ ($\mathbf{1}$), virtual crossings $\sigma_0, \sigma_1$, Hopf links $L_+, L_-$ ($\sigma_0\sigma_1, \sigma_1\sigma_0$), and the electron word $e^-$ ($\sigma_0\sigma_1\sigma_0$, whose closure is the Hopf link).

The **net** of the nucleon is:

$$
  \mathrm{net}(\mathfrak{N})
  = 
  \sum_{\text{basis } w} c_w(q_0)
$$

evaluated at the substrate parameter $q_0$.
