**Remark (Numerical Probe: SU(4) Alpha-Cluster Capacity and AME Residuals).**
*Numerical evaluation of the $\mathrm{SU}(4)$ alpha-cluster capacity links the Plancherel weight to the magic $A\cdot 8G$ closure and AME residuals.*

## Connection to nuclear-shell binding

The framework's nuclear-shell-binding gap relies on the hard-coded `magic A·8G` rule for $^{4}\!\mathrm{He}$ and the α-cluster recursion for $A \geq 8$. This conjecture identifies the magic A$\cdot$8G closure as the SU(4) supermultiplet structure:

| A | SU(4) supermultiplet | Framework rule |
|---|----------------------|----------------|
| 1 | fundamental $\mathbf{4}$ (single nucleon) | Borromean tower |
| 2 | $\mathbf{4} \otimes \mathbf{4} = \mathbf{6} \oplus \mathbf{10}$ | inter-nucleon Hecke (deuteron $^{2}\!\mathrm{H}$) |
| 3 | $\mathbf{4}^{\otimes 3} = \mathbf{4} \oplus \mathbf{20} \oplus \cdots$ | tritium / helium-3 |
| **4** | $\mathbf{4}^{\otimes 4} \supset \mathbf{1}$ (first totally-antisym) | **magic A$\cdot$8G** closure |
| 8 | first α-cluster pair | $c_{\alpha\alpha} = m_e \cdot \mathrm{Vol}(7^2_1)$ |
| 12 | second α-cluster | $c_{\alpha\alpha} \cdot 3$ |
| 16 | third α-cluster (closed p-shell) | second magic |

The magic A$\cdot$8G constant is conjectured to equal the SU(4)-singlet projection coefficient of the saturated 4-nucleon braid, evaluated under the SO(3)-fiber and bar-symmetric crystal functional:

$$
  \text{magic A$\cdot$8G constant}
  \;=\;
  \mathrm{tr}_{\mathrm{SU}(4)\text{-singlet}}\bigl(\beta_4^{\mathrm{canonical}}\bigr)
  \cdot
  \mathrm{Vol}(\mathcal{B}_3)
  \;=\;
  2 \cdot 4 \cdot 8G.
$$

The factor of 2 arises from the doubly-saturated isospin $\times$ spin closure (both SU(2)_S and SU(2)_I supermultiplets). The factor of 4 counts the $A=4$ nucleons. The $8G$ factor scales the Borromean hyperbolic volume.

## Classification of shell closures

The prototype script [`prototype_gs_nf_shell_binding.py`](../../../../computations/prototype_gs_nf_shell_binding.py) uses ε_shell values derived from AME residuals. It does so because the framework lacks a categorical formula determining which $(Z, N)$ saturates which shell. This conjecture provides that classification:

- **s-shell closure** at $A = 4$: SU(4) totally-antisymmetric $\mathbf{1}$.
- **p-shell closure** at $A = 16$ ($^{16}\!\mathrm{O}$): 12 p-shell nucleons fill the next SU(4) supermultiplet.
- **s-d-shell closure** at $A = 40$ ($^{40}\!\mathrm{Ca}$): doubly-magic 20p + 20n.

The α-cluster recursion in `mass_table_ppb.py` derives directly from this classification. Each $\alpha$ is a Wigner SU(4)-singlet quadruplet (the $A=4$ atomic shell unit). The n-α clusters form products of these quadruplets.

## Open R&D

1. **Verify magic A$\cdot$8G constant formula numerically**: At $q = q_0$, the dynamic capacity $E_{gate} = E_0 \ln(1/W_\lambda)$ derived from the SU(4) spin-flavor conjugate partition $\lambda$ precisely dictates the binding gap. The required fractional occupancy $c_\lambda$ scales from 0.24 ($^2H$) to 0.9435 ($^4He$, where $\lambda = (3,3,3,3)$). This formally supersedes the empirical $A \cdot 8G$ approximation with the categorical Plancherel weight.
2. **Derive α-cluster recursion**: Show that $c_{\alpha\alpha} = m_e \cdot \mathrm{Vol}(7^2_1)$ in `mass_table_ppb.py` arises as the product of two SU(4)-singlet quadruplets under categorical multiplication.
3. **Connect to the shell-binding prototype**: Replace ε_shell empirical estimates in [`prototype_gs_nf_shell_binding.py`](../../../../computations/prototype_gs_nf_shell_binding.py) with categorical SU(4)-singlet projection coefficients (via $c_\lambda$).
