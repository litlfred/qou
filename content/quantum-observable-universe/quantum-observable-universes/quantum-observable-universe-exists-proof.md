*Proof.*
We exhibit the triple $(\mathbf{C}, A, \tau)$ and verify the four
axioms of
[quantum observable universe](#def:quantum-observable-universe) in
turn.

### Construction

*(a) The rigid monoidal category.*  For $q \in \mathbb{C}^{\times}$ not
a non-trivial root of unity, the Drinfeld--Jimbo quantum group
$U_{q}(\mathfrak{g})$ \cite{chari1994, kassel1995} is a Hopf algebra
deforming $U(\mathfrak{g})$.  Its category of finite-dimensional type-I
representations $\mathbf{Rep}(U_{q}(\mathfrak{g}))$ is a rigid ribbon
braided monoidal category; rigidity supplies evaluation and
coevaluation morphisms for every object.  Take
$\mathbf{C} := \mathbf{Rep}(U_{q}(\mathfrak{g}))$.

*(b) The Frobenius--Hopf algebra.*  Let
$A := \mathcal{O}_{q}(G)$ be the restricted dual Hopf algebra --- the
algebra of matrix coefficients of type-I representations
\cite{woronowicz1988, chari1994}.  By \cite{woronowicz1987},
$\mathcal{O}_{q}(G)$ carries a unique faithful invariant state $h$,
the Haar state.  Set $\int_{A} := h$.

*(c) The fibre functor.*  Take $\tau \colon \mathbf{C} \to
\mathrm{Vect}_{\mathbb{C}}$ to be the forgetful functor; it is
faithful by construction.

### Verification of axioms

**Axiom 1 (non-degenerate Frobenius pairing).**
The Haar state $h = \int_{A}$ is faithful: for any non-zero $a \in A$
there exists $b \in A$ with $h(ab) \neq 0$.  This is the content of
Woronowicz's reconstruction theorem \cite{woronowicz1987}.
Faithfulness is equivalent to non-degeneracy of
$(a, b) \mapsto h(ab)$, which yields the isomorphism $A \xrightarrow{\sim}
A^{\vee}$ required by axiom (1). $\checkmark$

**Axiom 2 (observability).**
We show $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
By the Peter--Weyl decomposition for compact quantum groups
\cite{woronowicz1988},

$$
  \mathcal{O}_{q}(G)
  \;\cong\;
  \bigoplus_{\lambda \in \widehat{G}} V_{\lambda}^{*} \otimes V_{\lambda},
$$

and the adjoint action decomposes each summand as
$V_{\lambda}^{*} \otimes V_{\lambda} \cong \mathrm{End}(V_{\lambda})$.
The invariant subspace
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{End}(V_{\lambda}))$
consists only of scalar multiples of $\mathrm{id}_{V_{\lambda}}$, so
the only invariant morphisms $\mathbf{1} \to \mathrm{Ad}(A)$ factor
through the unit $\eta \colon \mathbf{1} \to A$, which is excluded by
axiom (2).  Semisimplicity of $G$ and generic $q$ ensure no further
fixed vectors appear. $\checkmark$

**Axiom 3 (measurability / Chern classes).**
Categorical Chern classes are defined via $\tau$:
$c_{i}(X) := c_{i}(\tau(X))$.  For $X = \mathrm{Ad}(A)$ with
archimedean realisation $\tau(\mathrm{Ad}(A)) = \mathrm{Ad}(P)$, these
are the Chern classes of the adjoint bundle of $P$, and the
proposition's hypothesis
$c_{1}(\mathrm{Ad}(P)) = c_{2}(\mathrm{Ad}(P)) = 0$ is exactly axiom
(3).

For $c_{2}(\mathrm{Ad}(P)) \neq 0$ one replaces $\mathbf{C}$ by the
modular tensor category $\mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$ at
level $k = \langle c_{2}, [M] \rangle$, obtained by quotienting the
tilting modules of $U_{q}(\mathfrak{g})$ at $q = e^{\pi i/(k +
h^{\vee})}$ by the negligible ideal \cite{reshetikhin1991}.  The
Chern--Simons level is then absorbed into the ribbon twist, and the
axiom is replaced by compatibility with the CS level.  Under the
present hypothesis $c_{2} = 0$ reduces to $k = 0$, and generic $q$
suffices. $\checkmark$

**Axiom 4 (categorical volume constraint).**
Let $V \in \mathbf{C}$ be the standard representation (dimension
$n = \dim V_{\mathrm{std}}$).  The top exterior power $\Lambda^{n} V$
is the 1-dimensional trivial module, $\Lambda^{n} V \cong \mathbf{1}$,
with isomorphism $\epsilon \colon \Lambda^{n} V \to \mathbf{1}$ given
by the $q$-deformed determinant (the quantum volume form)
\cite{kassel1995}.  By $G$-invariance of the determinant,

$$
  \epsilon \circ \Lambda^{n}(g_{V})
  \;=\;
  g_{\mathbf{1}} \circ \epsilon
  \;=\; \epsilon
  \quad \text{for all } g \in \mathrm{Aut}^{\otimes}(\tau),
$$

which is axiom (4). $\checkmark$

### Conclusion

All four axioms hold for
$(\mathbf{Rep}(U_{q}(\mathfrak{g})), \mathcal{O}_{q}(G), \mathrm{forget})$
under the Chern-class hypothesis, establishing existence.  The triple
specialises to the archimedean realisation
([$\mathbb{C}$-QOU](#ex:c-quantum-observable-universe)) upon choosing a
fibre functor landing in a module category over a contact CR manifold.

**Non-uniqueness.**  Any $(\mathbf{C}', A', \tau')$ with $\mathbf{C}'$
Morita-equivalent to $\mathbf{Rep}(U_{q}(\mathfrak{g}))$ and $A'$
Hopf-equivalent to $\mathcal{O}_{q}(G)$ gives another QOU.
Uniqueness up to such equivalences is Tannaka--Krein reconstruction
\cite{woronowicz1988}, taken here as background and not re-proved.
$\square$
