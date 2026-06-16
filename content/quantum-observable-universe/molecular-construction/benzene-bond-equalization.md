*The $D_6$ symmetry of the threading link $T(2, 6)$ ensures
that all six C--C bonds are identical. Each bond has:*

- *1 $\sigma$ pair (from step 1--4 of the construction)*
- *$\frac{1}{2}$ $\pi$ pair (from the threading link — each
 $\pi$ electron is shared between 2 adjacent carbons)*

*Total bond order per C--C bond: $1 + \frac{1}{2} = \frac{3}{2}$.*

*This is the braid-theoretic derivation of the experimentally
observed bond order 1.5 in benzene, with equal bond lengths
of $:val[bond_len_benzene_ang]{precision=3, witness=computations/molecular-experimental-refs.witness.json}\;\text{\AA}$ (between the C--C single bond length
$:val[bond_len_cc_single_ang]{precision=3, witness=computations/molecular-experimental-refs.witness.json}\;\text{\AA}$ and double bond length $:val[bond_len_cc_double_ang]{precision=3, witness=computations/molecular-experimental-refs.witness.json}\;\text{\AA}$).*

*The construction proves that bond equalization is not an axiom
of molecular orbital theory but a **theorem** of the LP dual:
the threading link's $D_6$ symmetry is the unique $\Phi_1$
minimum for 6 $\pi$ electrons on a 6-membered ring.*

*Extension to larger aromatics (naphthalene $C_{10}H_8$,
anthracene $C_{14}H_{10}$) proceeds by the same construction:
build the $\sigma$ framework iteratively, then apply the LP
dual to select the optimal $\pi$ configuration. The threading
link $T(2, N)$ generalises accordingly to $N$-membered rings,
with Alexander polynomial
$\Delta_{T(2,N)}(q) = (q^{N/2} - q^{-N/2})/(q - q^{-1})$
for even $N$.*
