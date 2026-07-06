The [atomic crossing table](#def:atomic-braid) governs intra-atomic interactions. Inter-atomic crossings isolate electromagnetic interactions. The strong force remains confined to individual nuclei. 

See [Table](#tbl:molecular-crossing-table-table-data) for the inter-atomic crossing coefficients.

Subscripts $i, j$ denote distinct atoms. We observe three differences from the intra-atomic table:

- **Purely electromagnetic proton-proton repulsion.** The crossing $\mathfrak{p}_i\mathfrak{p}_j$ yields $\sigma$. The strong force coupling vanishes across atoms.
- **Neutral decoupling.** The crossings $\mathfrak{n}_i\mathfrak{n}_j$ and $\mathfrak{p}_i\mathfrak{n}_j$ yield the identity. Neutrons between distinct atoms do not interact.
- **Covalent attraction.** The crossing $\mathfrak{p}_ie_j$ retains EM attraction. An electron from atom $j$ interacting with proton $i$ forms a shared-electron Hopf link.

The transfer matrix for an inter-atomic crossing $\sigma_g$ between strands $s$ (atom $i$) and $t$ (atom $j$) evaluates to:

$$
  T_{st}^{\mathrm{inter}} =
  \begin{pmatrix}
    c_{st} q + d_{st} & c_{st}(q - q^{-1}) \\
    c_{st} & c_{st} q^{-1} + d_{st}
  \end{pmatrix}.
$$

For identity crossings ($c = 0, d = 1$), $T_{st}^{\mathrm{inter}}$ reduces to the identity matrix. The strand passes through without introducing a Hecke generator.
