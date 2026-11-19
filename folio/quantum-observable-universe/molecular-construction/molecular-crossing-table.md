*The [atomic crossing table](#def:atomic-braid) governs
intra-atomic interactions (strong + EM).  For inter-atomic
crossings, only electromagnetic interactions remain because the strong
force is confined within each nucleus.  The inter-atomic crossing
coefficients are:*

See [Table](#tbl:molecular-crossing-table-table-data).

*where subscripts $i, j$ denote atoms rather than strands.  Key
differences from the intra-atomic table:*

- *$\mathfrak{p}_i\mathfrak{p}_j$ is purely electromagnetic
  ($\sigma$, repulsive): the strong $\mathfrak{p}\mathfrak{p}$
  crossing only operates within the same nucleus.*
- *$\mathfrak{n}_i\mathfrak{n}_j$ and $\mathfrak{p}_i\mathfrak{n}_j$
  are identity: neutrons from different atoms do not interact
  electromagnetically.*
- *$\mathfrak{p}_ie_j$ retains the EM attraction, which is the
  **covalent bond channel**.  An electron from atom $j$ attracted
  to proton $i$ creates the shared-electron Hopf link.*

*The transfer matrix for inter-atomic crossing
$\sigma_g$ between strands $s$ (atom $i$) and $t$ (atom $j$) is:*

$$
  T_{st}^{\mathrm{inter}} =
  \begin{pmatrix}
    c_{st} q + d_{st} & c_{st}(q - q^{-1}) \\
    c_{st} & c_{st} q^{-1} + d_{st}
  \end{pmatrix}
$$

*using the $(c, d)$ coefficients from the table above.  For
identity crossings ($c = 0$, $d = 1$), $T_{st}^{\mathrm{inter}}$
reduces to the $2 \times 2$ identity matrix, so the strand passes
through without generating a Hecke generator.*
