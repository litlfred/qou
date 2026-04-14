*The [atomic crossing table](#def:atomic-braid) governs
intra-atomic interactions (strong + EM).  For inter-atomic
crossings, only electromagnetic interactions remain — the strong
force is confined within each nucleus.  The inter-atomic crossing
coefficients are:*

| Pair | Crossing | $c$ | $d$ | Origin |
|:-----|:---------|:----|:----|:-------|
| $\mathfrak{p}_i\mathfrak{p}_j$ | $\sigma$ | $1$ | $0$ | EM repulsion (proton--proton) |
| $\mathfrak{n}_i\mathfrak{n}_j$ | $\mathrm{id}$ | $0$ | $1$ | no EM interaction |
| $\mathfrak{p}_i\mathfrak{n}_j$ | $\mathrm{id}$ | $0$ | $1$ | no EM interaction |
| $\mathfrak{p}_ie_j$ | $\sigma^{-1}$ | $1$ | $-(q-q^{-1})$ | EM attraction |
| $\mathfrak{n}_ie_j$ | $\mathrm{id}$ | $0$ | $1$ | no interaction |
| $e_ie_j$ | $\sigma$ | $1$ | $0$ | EM repulsion |

*where subscripts $i, j$ denote atoms, not strands.  Key
differences from the intra-atomic table:*

- *$\mathfrak{p}_i\mathfrak{p}_j$ is purely electromagnetic
  ($\sigma$, repulsive) — the strong $\mathfrak{p}\mathfrak{p}$
  crossing only operates within the same nucleus.*
- *$\mathfrak{n}_i\mathfrak{n}_j$ and $\mathfrak{p}_i\mathfrak{n}_j$
  are identity — neutrons from different atoms do not interact
  electromagnetically.*
- *$\mathfrak{p}_ie_j$ retains the EM attraction — this is the
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
reduces to the $2 \times 2$ identity matrix — the strand passes
through without generating a Hecke generator.*
