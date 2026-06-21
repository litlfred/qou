Throughout this paper, particles **are** their knots.  We write

$$
  \mathfrak{K}_x^{\pm}
$$

where $x$ is the traditional physics symbol for the particle and
$\pm$ is the chirality (orientation) of the knot.  The
superscript distinguishes particle from antiparticle: mirror
image = charge conjugation.

**Fundamental particles.**

See [Table 1](#tbl:knot-notation-convention-table1-data).

The sign convention: $\mathfrak{K}_e^- = T_{2,3}$ (left trefoil =
electron), $\mathfrak{K}_e^+ = T_{2,3}^{\sigma}$ (right trefoil =
positron).  For amphichiral knots ($\mathfrak{K}_\mu$,
$\mathfrak{K}_\gamma$), the sign is trivial: $K \cong K^{\sigma}$.

The unknot $\mathfrak{K}_\nu$ is amphichiral as an unoriented knot,
but the neutrino $\nu$ and antineutrino $\nu^{\sigma}$ are
distinguished by **framing** (a choice of normal vector along the
knot), not by knot type.  This is the geometric origin of the
neutrino's chirality: left-handed $\nu_L$ and right-handed
$\nu_R^{\sigma}$ are the same unknot with opposite framings.

**Torus knots.**
When the torus parameters are relevant, write $T_{m,n}$ for the
$(m, n)$-torus knot.  The mirror image is $T_{m,n}^{\sigma} =
T_{m,-n}$.

**Links.**

See [Table 2](#tbl:knot-notation-convention-table2-data).

**Composites.**
The connected sum of knots is $\mathfrak{K}_1 \mathbin{\#} \mathfrak{K}_2$.  A hadron ([hadron](#def:hadron)) is written
$[\mathfrak{K}_1, \mathfrak{K}_2, \mathfrak{K}_3]_p \oplus \mathcal{L}_H$, where the subscript $c$ indicates colour-tube
coupling and $\oplus$ denotes the linking operation.  The proton:

$$
  \mathfrak{p} = [\mathfrak{K}_u, \mathfrak{K}_u, \mathfrak{K}_d]_p
  \oplus \mathcal{L}_H
$$

**Hecke / Skein conventions for worked examples.**
Per [AGENTS.md §7a Hecke-Skein
convention](https://github.com/litlfred/qou/blob/main/AGENTS.md), the
Hecke generator is **$\sigma_i$** (the same symbol serves both as
braid generator in $B_n$ and its image in $H_n(R, q)$; context
disambiguates), satisfying the Hecke relation
$\sigma_i^{2} = (q - q^{-1})\sigma_i + 1$ and the Skein relation
$\sigma_i - \sigma_i^{-1} = q - q^{-1}$.  The two eigenchannels on
$V \otimes V$ are symmetric (eigenvalue $q$, projector $e_+$) and
antisymmetric (eigenvalue $-q^{-1}$, projector $e_-$); see
[Hecke–Markov interpretation](#rem:hecke-markov-interpretation)
for the full eigenprojector decomposition.  The Jones polynomial
is **$J_K(q)$** throughout (never $V_K(t)$ or the bracket variable
$A$).  When a worked example evaluates a knot's mass, it uses the
topological mass formula
$\mathfrak{m}(K) = \mathrm{Vol}(K) / \hbar_q^{2}$
([prop:topological-mass-formula](#prop:topological-mass-formula))
with $\hbar_q = 1 - q^{-1}$ the quantum Planck constant.
