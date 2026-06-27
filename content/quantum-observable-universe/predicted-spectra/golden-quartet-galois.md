*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (Golden quartet as Galois $\times$ bar orbit).**
The golden quartet

$$
  Q  :=  \bigl\{\,1/\varphi,\;-\varphi,\;\varphi,\;-1/\varphi\,\bigr\}
$$

is the **complete root set** of the quartic polynomial

$$
  P(x)  :=  x^4 - 3x^2 + 1
   =  (x^2 - x - 1)(x^2 + x - 1)
$$

over $\mathbb{Q}$. Under the Galois action of $\mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q})
= \langle \tau \rangle \cong \mathbb{Z}/2$ (where $\tau \colon
\sqrt{5} \mapsto -\sqrt{5}$), the quartet splits into **two orbits**
of size $2$:

$$
  Q_+  :=  \{\,\varphi,\;-1/\varphi\,\}
  \;=\;\mathrm{Gal\text{-orbit}\ of\ }\varphi
  \;=\;\mathrm{roots\ of\ }x^2 - x - 1,
$$

$$
  Q_-  :=  \{\,1/\varphi,\;-\varphi\,\}
  \;=\;\mathrm{Gal\text{-orbit}\ of\ }1/\varphi
  \;=\;\mathrm{roots\ of\ }x^2 + x - 1.
$$

The **bar involution** $\iota \colon x \mapsto x^{-1}$ on $\mathbb{R}^\times$
exchanges the two Galois orbits:

$$
  \iota(Q_+) = Q_-,\qquad \iota(Q_-) = Q_+.
$$

Therefore the joint group $G := \mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q}) \times
\langle\iota\rangle \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ acts on $Q$
with **a single orbit equal to $Q$**, transitively and faithfully.

*Proof.*
Direct expansion:

$$
  (x^2 - x - 1)(x^2 + x - 1)
  = x^4 + x^3 - x^2 - x^3 - x^2 + x - x^2 - x + 1
  = x^4 - 3x^2 + 1.
$$

The two quadratic factors are the minimal polynomials of $\varphi$
and $1/\varphi$ over $\mathbb{Q}$ respectively, so their roots are
$Q_+$ and $Q_-$.

For $\tau \in \mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q})$ acting by $\sqrt{5}
\mapsto -\sqrt{5}$:

$$
  \tau(\varphi) = \tau\!\left(\tfrac{1 + \sqrt{5}}{2}\right)
   =  \tfrac{1 - \sqrt{5}}{2}  =  -1/\varphi,
$$

$$
  \tau(1/\varphi) = \tau\!\left(\tfrac{-1 + \sqrt{5}}{2}\right)
   =  \tfrac{-1 - \sqrt{5}}{2}  =  -\varphi.
$$

Hence $Q_+$ and $Q_-$ are the two Galois orbits.

For the bar involution: $\iota(\varphi) = 1/\varphi \in Q_-$, so
$\iota$ does not preserve $Q_+$. It exchanges $Q_+$ and $Q_-$
because $\varphi \cdot 1/\varphi = 1$ and $-\varphi \cdot (-1/\varphi)
= 1$, so $\iota(\varphi) = 1/\varphi$, $\iota(-\varphi) = -1/\varphi$.

The product action of $G$ on $Q$ has orbit $G \cdot \varphi = Q$:

| element of $G$ | image of $\varphi$ |
|----------------|-------------------|
| $(\mathrm{id}, \mathrm{id})$ | $\varphi$ |
| $(\tau, \mathrm{id})$ | $-1/\varphi$ |
| $(\mathrm{id}, \iota)$ | $1/\varphi$ |
| $(\tau, \iota)$ | $-\varphi$ |

All four elements appear; $|G| = 4 = |Q|$, so the action is 
transitive. $\square$

**Consequence: replace $\zeta_5$ Galois arithmetic with quartet orbit.**

Several existing arguments invoke the Galois action of
$\mathrm{Gal}(\mathbb{Q}(\zeta_5)/\mathbb{Q}) \cong \mathbb{Z}/4$ to track
$S_5$-equivariance on Bring's surface coordinates. Where the action
ultimately descends to $\varphi$ and $1/\varphi$ (real values), the
relevant subgroup is the order-2 quotient
$\mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q})$, since
$\mathbb{Q}(\sqrt{5}) \subset \mathbb{Q}(\zeta_5) = \mathbb{Q}(\zeta_{10})$
is the **maximal real subfield**.

The quartet-orbit description above lets such arguments be
**rewritten without $\zeta_5$**: instead of "the $\zeta_5$-action
on the color tube coordinates fixes $\varphi$ as a real combination",
one writes "the golden quartet $Q$ is closed under $G$-action, and
$\varphi$ is a $\mathrm{Gal}$-orbit representative". This eliminates
roots-of-unity bookkeeping where it is not essential.

**Connection to Bring's surface.**

The quartic $P(x) = x^4 - 3x^2 + 1$ is the **shadow on the maximal
real subfield** of the resolvent that determines the chiral
fibration of Bring's surface. Its discriminant
$\mathrm{disc}(P) = 400 = 2^4 \cdot 5^2$
(via the depressed-quartic formula $16\,d\,(b^2 - 4d)^2$ at
$b = -3,\,d = 1$) encodes the depth of the
$\mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q})$-extension
that supports the $S_5$ symmetry restricted to $A_4 \subset S_5$.

The four golden values are therefore not "four arbitrary algebraic
numbers" — they are the **complete real Galois orbit** generated
by either $\varphi$ or $1/\varphi$ together with the bar involution,
encoding the full set of phase boundaries and Möbius fixed points
of the Descartes universe.
