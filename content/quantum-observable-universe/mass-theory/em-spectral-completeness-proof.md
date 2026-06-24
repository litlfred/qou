The braiding eigenvalue extraction
([eigenvalue extraction](#prop\:braiding-eigenvalue-extraction))
shows that $c_{A,A}$ satisfies the Hecke minimal polynomial

$$
  (c_{A,A} - q^{1/2})(c_{A,A} + q^{-1/2}) \;=\; 0
$$

in $E$.  The two eigenvalues $q^{1/2}, -q^{-1/2}$ are distinct
(their difference $q^{1/2} + q^{-1/2}$ is a unit in $R$), so the
minimal polynomial splits over $R$ and Bezout produces orthogonal
idempotents

$$
  e_- \;=\; \frac{q^{1/2} \cdot \mathrm{id} - c_{A,A}}{q^{1/2} + q^{-1/2}},
  \qquad
  e_+ \;=\; \mathrm{id} - e_-.
$$

These are central in $E$ since $c_{A,A}$ generates the centraliser of
the diagonal $R$-action by Schur--Weyl-Hecke duality.  Statement (2)
follows from $H_2(R, q) \cong E$ being free of rank $2$ over $R$: $E$
has at most two simple summands, and $e_\pm$ realise them.  The
singlet identification $V_- \cong \mathbf{1}$ is the standard
Schur-functor decomposition $A \otimes A = S^2 A \oplus \Lambda^2 A$
with $\Lambda^2 A \cong \mathbf{1}$ when $A$ is the fundamental of
$\mathrm{SU}_q(2)$.  Statement (4) is the Wedderburn trace identity
([Wedderburn trace](#prop\:wedderburn-trace-identity)) at $n = 2$.
$\qquad\blacksquare$
