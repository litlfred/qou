The Frobenius form $\int_A$ and the multiplication $\mu$ together
define a non-degenerate pairing
$\langle a, b \rangle = \int_A(\mu(a \otimes b))$
([Frobenius pairing](#def:frobenius-pairing)), giving an isomorphism
$\phi \colon A \xrightarrow{\sim} A^{\vee}$.  Define the *dual
comultiplication* $\Delta_\mu$ as the transpose of $\mu$ under $\phi$:

$$
  \Delta_\mu = (\phi^{-1} \otimes \phi^{-1}) \circ \mu^{\vee} \circ \phi.
$$

To verify the Frobenius relation, the two composites
$(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu)$
and $\Delta_\mu \circ \mu$ are maps $A \otimes A \to A \otimes A$;
by non-degeneracy it suffices to show they agree after pairing with
an arbitrary test element $c \in A$.  Writing
$\Delta_\mu(b) = b_1 \otimes b_2$ in Sweedler notation, the
left-hand side equals

$$
  \int_A \mu\bigl(\mu(a \otimes b_1) \otimes b_2\bigr) \cdot c
  = \int_A \mu\bigl(a \otimes \mu(b_1 \otimes b_2)\bigr) \cdot c
$$

by associativity of $\mu$, and the right-hand side equals
$\int_A \mu(a \otimes \mu(b_1 \otimes b_2)) \cdot c$ directly.
Both sides agree, so the Frobenius relation holds: $\Delta_\mu$ is
the transpose of $\mu$, and associativity of $\mu$ is the only
non-trivial axiom used.  $\square$
