In the $\mathrm{SU}(2)$ realisation the notion of "adjoint" is
unambiguous: all three candidate adjoints coincide, with
$f^{\dagger} = \overline{f \circ \mathrm{inv}}$, and the
Frobenius adjoint reproduces the Hilbert-space adjoint on each
representation $V_j$
([dagger on SU(2)](#ex:dagger-su2)).  This concrete anchor fixes
the intended meaning; the three notations below only diverge once
one leaves it.

Three notations for "adjoint" coexist in the literature and in this
book.  To prevent confusion:

- $f^{\dagger}$ (dagger) denotes the **Frobenius adjoint**: the
  involution $f \mapsto \int_A \circ \mu(S(f) \otimes -)$ derived
  from the Frobenius pairing and the antipode.  This is the
  categorical structure.

- $f^{\ast}$ (star) denotes **complex conjugation** in the
  archimedean realisation ($R = \mathbb{C}$).  On functions
  $f \in \mathcal{O}(G)$, it acts as $f^{\ast}(g) = \overline{f(g)}$.

- The **physicist's adjoint** $A^{\dagger}_{\mathrm{phys}}$ of an
  operator $A$ on a Hilbert space $\mathcal{H}$ satisfies
  $\langle A^{\dagger}_{\mathrm{phys}} v, w \rangle = \langle v, A w \rangle$.

In the general categorical setting only $\dagger$ is defined;
$\ast$ requires an archimedean structure and
$A^{\dagger}_{\mathrm{phys}}$ requires a Hilbert space.
