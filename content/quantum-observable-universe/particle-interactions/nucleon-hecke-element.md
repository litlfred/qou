Let $\mathfrak{N} = [\mathfrak{q}_1, \mathfrak{q}_2, \mathfrak{q}_3]$ denote a Borromean baryon with quark flavors $f_1, f_2, f_3 \in \{\mathfrak{u}, \mathfrak{d}\}$. The **nucleon Hecke element** evaluates in $H_3(R, q)$ as:

$$
  \mathfrak{N}(f_1, f_2, f_3)
  = 
  \mathcal{B}_3
   \cdot 
  C(f_1, f_2; \sigma_0)
   \cdot 
  C(f_1, f_3; \sigma_0)
   \cdot 
  C(f_2, f_3; \sigma_1)
$$

where:

- $\mathcal{B}_3 = (\sigma_0 \sigma_1^{-1})^3 \in H_3(R, q)$ is the Borromean link element.
- $C(f_i, f_j; \sigma_k)$ is the typed crossing operator for the quark pair at positions $i, j$.
- The three pairwise crossings $(1,2)$, $(1,3)$, $(2,3)$ map to generators $\sigma_0, \sigma_0, \sigma_1$, respectively.

**Proton.** For $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]$:

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{u}; \sigma_0)}_{\sigma_0}
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_0)}_{\sigma_0 - \tfrac{1}{2}h_{\mathrm{A}}\cdot\mathbf{1}}
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_1)}_{\sigma_1 - \tfrac{1}{2}h_{\mathrm{A}}\cdot\mathbf{1}}
$$

where $h_{\mathrm{A}} = q - q^{-1}$.

**Neutron.** For $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$:

$$
  \mathfrak{n}
  = 
  \mathcal{B}_3
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_0)}_{\sigma_0 - \tfrac{1}{2}h_{\mathrm{A}}\cdot\mathbf{1}}
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_0)}_{\sigma_0 - \tfrac{1}{2}h_{\mathrm{A}}\cdot\mathbf{1}}
   \cdot 
  \underbrace{C(\mathfrak{d}, \mathfrak{d}; \sigma_1)}_{\sigma_1 - h_{\mathrm{A}}\cdot\mathbf{1}}
$$

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

The coefficients $c_\bullet \in \mathbb{Z}[q, q^{-1}]$ encode the particle content of the nucleon: the photon channel $\gamma$ ($\mathbf{1}$), virtual crossings $\sigma_0, \sigma_1$, Hopf links $L_+, L_-$ ($\sigma_0\sigma_1, \sigma_1\sigma_0$), and the trefoil (electron) $e^-$ ($\sigma_0\sigma_1\sigma_0$).

The **net** of the nucleon is:

$$
  \mathrm{net}(\mathfrak{N})
  = 
  \sum_{\text{basis } w} c_w(q_0)
$$

evaluated at the substrate parameter $q_0$.

**Witness**: `breit-wheeler-nucleon-nf.witness.json`.
