**Proof.**
The QOU non-degeneracy axiom ensures the Frobenius form
$\int_A \colon A \to \mathbf{1}$ is non-degenerate, inducing the
Frobenius self-duality $A \cong A^{\vee}$
(the fibre-adjoint involution, constructed later in this chapter). Define a dagger on
morphisms by $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$, where
$S$ is the antipode. Non-degeneracy of $\int_A$ and faithfulness
of $\tau$ imply $f^{\dagger} \circ f = 0 \Rightarrow f = 0$, so this
is a positive-definite dagger structure
([positive definite dagger](#prop:positive-definite-dagger)).

It remains to show that every tensor automorphism $g \in G$ preserves this
dagger, forcing unitarity on $\tau(V)$. By naturality, $g$ commutes
with every morphism in $\mathbf{C}$; in particular with the antipode
$S$ and the Frobenius form $\int_A$:

$$
  \tau(S) \circ g_A = g_A \circ \tau(S),
  \qquad
  \tau({\textstyle\int_A}) \circ g_A = \tau({\textstyle\int_A}).
$$

Applying $\tau$ to the defining formula
$f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$ shows that
conjugation by $g_V$ preserves the induced Hermitian pairing
$\langle f_1, f_2 \rangle
   := \tau(\int_A) \circ \tau(\mu)(\tau(S)(f_1) \otimes f_2)$
on $\mathrm{End}(\tau(V))$. Restricting to $\mathrm{Hom}(\mathbf{1},
\tau(V)) \cong \tau(V)$, this gives
$\langle g_V v, g_V w \rangle = \langle v, w \rangle$ for all
$v, w \in \tau(V)$, which is equivalent to
$g_V^{\dagger} g_V = \mathrm{id}_{\tau(V)}$, i.e.
$g_V^{-1} = g_V^{\dagger}$. Hence $G \subseteq \mathrm{U}(2)$. $\square$
