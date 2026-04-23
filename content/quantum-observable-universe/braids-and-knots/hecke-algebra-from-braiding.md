The Iwahori--Hecke algebra in which all subsequent Gröbner--Shirshov normal-form
computations take place is *not* an algebra with a free parameter.
It is the quotient of the braid-group algebra by the minimal
polynomial of the categorical braiding.

Concretely, the braiding eigenvalue extraction
([eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
shows that $c_{V,V}$ has eigenvalues $(q, -q^{-1})$ on the
decomposition $V \otimes V = S^2 V \oplus \Lambda^2 V$.
Applying the fibre functor $\tau$ gives the endomorphism
$T = \tau(c_{V,V})$ satisfying the Hecke relation

$$
  (T - q)(T + q^{-1}) =  0,
$$

where $q \in \mathrm{End}(\mathbf{1}) \cong k^{\times}$ is the
braiding eigenvalue — the same $q$ that parametrises the substrate
family $d_q$ ([substrate parameter](#def:substrate-parameter)).

The Iwahori--Hecke algebra on $n$ strands is therefore

$$
  H_n(q) =  k[B_n] \big/
  \bigl\langle (T_i - q)(T_i + q^{-1})  \big| 
  i = 1, \ldots, n{-}1 \bigr\rangle,
$$

and the parameter $q$ is a **categorical datum** — determined by
the braiding of $(\mathbf{C}, A, \tau)$, not chosen freely.
Every Laurent polynomial $c_w \in \mathbb{Z}[q, q^{-1}]$ appearing
in a Gröbner--Shirshov normal form
([nuclear normal form](#prop:nuclear-groebner-reduction)) inherits
its $q$ from this categorical source.

### Crossing energy is not bolted on

A common misreading takes the crossing energy
([crossing energy](#def:crossing-energy))
$\mathbf{E}_{\times}(q) \propto q - q^{-1}$, which assigns a
quantum $q$ to each $L_+$ crossing and $-q^{-1}$ to each $L_-$
crossing, to be an **external physical postulate** --- an
energetic penalty bolted onto a topological framework.  It is
not.  Inside a rigid monoidal category, the two eigenvalues of
$T$ are forced by the structure itself:

1. *Rigidity fixes $\det$.*  The dualisability of $V$ in a rigid
   monoidal category --- equivalently, the existence of the
   Frobenius pairing $\int_A$ --- forces the braiding
   $c_{V,V} \colon V \otimes V \to V \otimes V$ to be an element of
   $\mathrm{SL}(V \otimes V)$: its **categorical volume**
   $\det(c_{V,V})$ must equal $1$ for the evaluation and
   coevaluation morphisms to compose to the identity.
2. *Determinant 1 picks the eigenvalue pair.*  The
   symmetric/antisymmetric decomposition
   $V \otimes V = S^{2} V \oplus \Lambda^{2} V$
   ([eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
   forces $c_{V,V}$ to act as a single scalar on each summand,
   with eigenvalues $(\lambda_{+}, \lambda_{-})$.  The
   determinant constraint reads
   $\lambda_{+} \cdot \lambda_{-} = 1$.  Together with the
   normalisation $\lambda_{+} = q$ selected by the substrate
   parameter, this forces $\lambda_{-} = -q^{-1}$ (the sign comes
   from $\Lambda^{2}$ carrying the sign of the transposition).
3. *The Hecke relation is the minimal polynomial.*  Given the
   eigenvalue pair $(q, -q^{-1})$, the Cayley--Hamilton minimal
   polynomial of $T$ is exactly $(T - q)(T + q^{-1}) = 0$.  No
   additional data is introduced; the Hecke relation is a
   consequence of categorical volume, not an axiom layered on top
   of one.
4. *The crossing energy is the eigenvalue gap.*  The quantum
   $\mathbf{E}_{\times}(q) = \tfrac{1}{2}(q - q^{-1})$ deposited
   per crossing is one half of the **spectral gap**
   $\lambda_{+} - \lambda_{-} = q - (-q^{-1}) = q + q^{-1}$ of $T$
   in the signed convention, equivalently the gap between the
   symmetric and antisymmetric channels of $V \otimes V$.  Any
   attempt to sort an unsorted tensor state into its
   $S^{2} V$ and $\Lambda^{2} V$ components pays this gap; it is
   the categorical cost of resolving identity-typed ambiguity into
   eigentyped clarity, not a separately posited interaction
   energy.

In short: once one assumes a rigid monoidal category with a
fibre functor, the Hecke relation, its two eigenvalues, and the
crossing energy are **forced together**.  Removing any one would
violate the determinant constraint and break duality.  The
apparent "physical" penalty is just the eigenvalue structure of a
volume-preserving braiding, read through the Frobenius pairing.
