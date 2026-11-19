The construction of $H_2$ proceeds in three stages.

### Stage 1: Build two hydrogen atoms

Each hydrogen atom is an [atomic braid](#def:atomic-braid) in $H_2(q)$: one proton $\mathfrak{p}$ and one electron $e$, with the $\mathcal{B}_3$-dressed $\mathfrak{p}e$ crossing.

Atom 1: $\mathcal{A}_1 = [\mathfrak{p}_1, e_1]$ with dressed eigenvalues $(q^5, -q^{-5})$.

Atom 2: $\mathcal{A}_2 = [\mathfrak{p}_2, e_2]$ with dressed eigenvalues $(q^5, -q^{-5})$.

### Stage 2: Embed in $H_4(q)$ and apply inter-atomic crossings

The molecular braid lives in $H_4(q)$ with strand ordering $[\mathfrak{p}_1, e_1, \mathfrak{p}_2, e_2]$. The six pairwise crossings are:

See [Table](#tbl:h2-molecular-braid-table-data).

The **covalent channel** is the $e_1\mathfrak{p}_2$ crossing ($\sigma_1$). Electron 1 from atom 1 is attracted to proton 2 of atom 2. By symmetry, $e_2$ is also attracted to $\mathfrak{p}_1$ via the $\mathfrak{p}_1 e_2$ crossing. This produces the shared-electron bond.

### Stage 3: Transfer matrix chain

The four-strand transfer matrix product is:

$$
  \hat{V}^{H_2} = T_{\mathfrak{p}_1 e_1}^{\mathrm{dressed}}
  \cdot T_{e_1 \mathfrak{p}_2}
  \cdot T_{\mathfrak{p}_2 e_2}^{\mathrm{dressed}}
$$

where:

$$
  T_{\mathfrak{p}e}^{\mathrm{dressed}} =
  \begin{pmatrix}
    q^{-5} + d & q^{-5} - q^5 \\
    1 & q^5 + d
  \end{pmatrix},
  \qquad
  T_{e_1\mathfrak{p}_2} =
  \begin{pmatrix}
    q^{-1} + d & q^{-1} - q \\
    1 & q + d
  \end{pmatrix}
$$

with $d = -(q - q^{-1})$. At $q_0 \approx 1.110$:

- $T_{\mathfrak{p}e}^{\mathrm{dressed}}$: eigenvalues $q^5 \approx 1.680$ and $-q^{-5} \approx -0.595$
- $T_{e_1\mathfrak{p}_2}$ (covalent): eigenvalues $q \approx 1.110$ and $-q^{-1} \approx -0.901$
