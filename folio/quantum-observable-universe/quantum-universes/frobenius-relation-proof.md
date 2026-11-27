The Frobenius form $\int_A$ and the multiplication $\mu$ together
define a non-degenerate pairing
$\langle a, b \rangle = \int_A(\mu(a \otimes b))$
([Frobenius pairing](#def:frobenius-pairing)). Non-degeneracy gives a
copairing $\gamma = \sum_i \gamma_i' \otimes \gamma_i'' \in A \otimes A$, the
unique element satisfying the snake identity
$\sum_i \langle a, \gamma_i' \rangle\, \gamma_i'' = a$ for all $a \in A$.
The comultiplication dual to $\mu$ under the pairing is

$$
  \Delta_\mu = (\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \gamma),
  \qquad
  \Delta_\mu(b) = \sum_i \mu(b \otimes \gamma_i') \otimes \gamma_i'' .
$$

That this map is the transpose of $\mu$ under the pairing is the standard
equivalence of the two descriptions of the comultiplication of a Frobenius
algebra (\cite{kock2004}, §2.3); it uses only the snake identity.

With this form the relation is associativity. For $a, b \in A$,

$$
  (\mu \otimes \mathrm{id})\bigl(a \otimes \Delta_\mu(b)\bigr)
  = \sum_i \mu\bigl(a \otimes \mu(b \otimes \gamma_i')\bigr) \otimes \gamma_i''
  = \sum_i \mu\bigl(\mu(a \otimes b) \otimes \gamma_i'\bigr) \otimes \gamma_i''
  = \Delta_\mu\bigl(\mu(a \otimes b)\bigr).
$$

Hence $(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu) = \Delta_\mu \circ \mu$. $\square$
