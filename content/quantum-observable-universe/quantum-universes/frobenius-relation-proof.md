
The Frobenius form $\int_A$ and the multiplication $\mu$ together
define a pairing $\langle a, b \rangle = \int_A(\mu(a \otimes b))$
on $A$. Non-degeneracy of this pairing
([Frobenius pairing](#def:frobenius-pairing)) gives an isomorphism
$\phi \colon A \xrightarrow{ \sim } A^{\vee}$ defined by
$\phi(a) = \langle a, - \rangle$. Define the *dual comultiplication*
$\Delta_\mu$ as the transpose of $\mu$ under $\phi$:

$$
  \Delta_\mu = (\phi^{-1} \otimes \phi^{-1}) \circ \mu^{\vee} \circ \phi,
$$

where $\mu^{\vee} \colon A^{\vee} \to A^{\vee} \otimes A^{\vee}$ is
the linear dual of $\mu$.

To verify the Frobenius relation, consider the two composites
$(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu)$
and $\Delta_\mu \circ \mu$ as maps
$A \otimes A \to A \otimes A$. It suffices to show they agree
after pairing with an arbitrary test element
$c \in A$ via $\int_A$, since the pairing is non-degenerate.

For the left-hand side, using the definition of $\Delta_\mu$ and
the associativity of $\mu$:

$$
  \bigl\langle (\mu \otimes \mathrm{id})
  (\mathrm{id} \otimes \Delta_\mu)(a \otimes b), c \bigr\rangle
  = \int_A \mu\bigl(\mu(a \otimes b_1) \otimes b_2\bigr) \cdot c
  = \int_A \mu\bigl(a \otimes \mu(b_1 \otimes b_2)\bigr) \cdot c,
$$

where $\Delta_\mu(b) = b_1 \otimes b_2$ (Sweedler notation) and the
second equality is associativity of $\mu$.

For the right-hand side:

$$
  \bigl\langle \Delta_\mu(\mu(a \otimes b)), c \bigr\rangle
  = \int_A \mu\bigl(a \otimes \mu(b_1 \otimes b_2)\bigr) \cdot c.
$$

Both sides equal the same expression, so the Frobenius relation holds.
The key step is that $\Delta_\mu$ is defined as the transpose of
$\mu$, and associativity of $\mu$ — the only non-trivial axiom
used — ensures the two ways of "sliding" multiplication past
comultiplication agree.
