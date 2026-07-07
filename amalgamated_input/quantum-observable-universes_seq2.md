<!-- FILE_START: frobenius-su2.md -->
Continuing [QOU on $\mathrm{SU}(2)$](#ex:qou-su2), set
$A = \mathcal{O}(\mathrm{SU}(2))$ with multiplication
$\mu(f \otimes g) = fg$ (pointwise product) and Frobenius form
$\int_A = \int_G$ (Haar integral). The dual comultiplication is
$\Delta_\mu(f)(g,h) = \int_G f(xg)\overline{h(x)}dx$, and the
Frobenius relation expresses the associativity of convolution:
$\int_G f(xy)g(y)dy$ can be evaluated by convolving first with $f$
or first with $g$.
<!-- FILE_END: frobenius-su2.md -->

<!-- FILE_START: dagger-su2.md -->
Continuing [Frobenius $\mathrm{SU}(2)$](#ex:frobenius-su2), the category
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ carries a canonical
involutive structure built from the antipode:

- *What it does.* For a morphism $f \colon V_j \to V_k$
  (an equivariant linear map between representations),
  $f^{\dagger}$ is the *Hilbert-space adjoint*: the unique
  map $f^{\dagger} \colon V_k \to V_j$ satisfying
  $\langle f^{\dagger}(w), v \rangle_j = \langle w, f(v) \rangle_k$
  for all $v \in V_j$, $w \in V_k$.
- *Why it exists.* Each irreducible representation $V_j$
  carries a unique (up to scalar) $\mathrm{SU}(2)$-invariant
  inner product. The adjoint $f^{\dagger}$ with respect to
  these inner products is automatically equivariant, so
  $f^{\dagger}$ is again a morphism in $\mathbf{C}$.
- *On the algebra.* On $A = \mathcal{O}(\mathrm{SU}(2))$,
  $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$, where
  $S(f)(g) = f(g^{-1})$ is the antipode. The involution
  $f \mapsto f^{\dagger}$ is complex conjugation composed with
  pullback by inversion: $f^{\dagger}(g) = \overline{f(g^{-1})}$.
- *Positive-definiteness.* For a non-zero state
  $f \colon \mathbb{C} \to V_j$, the composite
  $f^{\dagger} \circ f = \lVert f(1) \rVert^2 > 0$.
  This is the statement that the inner product on each $V_j$ is
  positive-definite --- the categorical encoding of unitarity.
<!-- FILE_END: dagger-su2.md -->

<!-- FILE_START: volume-from-rigidity.md -->
Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal
category, and let $V$ be a simple object that is
*symplectically self-dual*: there exists an isomorphism
$\phi \colon V \xrightarrow{ \sim } V^{\vee}$ satisfying
$\phi^{\vee} = -\phi$ (alternating). The alternating condition forces
$\mathrm{rank}(V) = 2$: the composite
$\mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ factors through
$\Lambda^2 V$, and for the resulting morphism
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$ to be a non-degenerate
epimorphism one needs $\mathrm{rank}(\Lambda^2 V) = 1$, i.e.,
$\mathrm{rank}(V) = 2$. The factorisation is (the
*volume form factorisation*):

```tex
\begin{equation}\label{eq:volume-form-factorisation}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  V \otimes V
    \ar[r, "\mathrm{id} \otimes \phi"]
    \ar[d, "\pi"', two heads]
  & V \otimes V^{\vee}
    \ar[d, "\mathrm{ev}_V"]
  \\
  \Lambda^2 V
    \ar[r, "\epsilon"', dashed]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

and $\epsilon$ is non-degenerate; that is,
condition (iii) of
[quantum observable universe](#def:quantum-observable-universe) holds.

<!-- FILE_END: volume-from-rigidity.md -->

<!-- FILE_START: su2-volume-from-rigidity.md -->
Continuing [QOU on $\mathrm{SU}(2)$](#ex:qou-su2), take $V = V_{1/2} \cong \mathbb{C}^2$.
The symplectic form is
$\phi = \begin{smallmatrix} 0 & 1 \\ -1 & 0 \end{smallmatrix}$,
identifying $V \cong V^{\vee}$ with $\phi^{\vee} = -\phi$ (alternating).
[volume from rigidity](#lem:volume-from-rigidity) then gives:

- The evaluation pairing becomes
  $B(v, w) = v_1 w_2 - v_2 w_1$ (the determinant).
- $B$ is alternating, so it factors through $\Lambda^2 V$:
  the map $\epsilon \colon \Lambda^2 V \to \mathbb{C}$ is
  $\epsilon(v \wedge w) = \det(v, w)$.
- Non-degeneracy: $\epsilon$ is an isomorphism
  $\Lambda^2 \mathbb{C}^2 \cong \mathbb{C}$.
- For $g \in G$, $\Lambda^2 g = \det(g) \cdot \mathrm{id}$, so
  $\epsilon$-preservation forces $\det(g) = 1$: this is why the
  gauge group is $\mathrm{SU}(2)$ rather than
  $\mathrm{GL}(2, \mathbb{C})$ or $\mathrm{U}(2)$.
<!-- FILE_END: su2-volume-from-rigidity.md -->

<!-- FILE_START: su2-emergence.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)). Then
$G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$
(or $\mathrm{SL}(2, R)$ depending on the signature of the Frobenius
pairing).

<!-- FILE_END: su2-emergence.md -->

<!-- FILE_START: su2-emergence-volume-determinant.md -->
**Lemma.**
*Under the QOU hypotheses of [emergence of the gauge group](#thm:su2-emergence),
every tensor automorphism $g \in G$ of the fibre functor $\tau$
satisfies $\det(g_V) = 1$; equivalently, $G \subseteq \mathrm{SL}(2)$.*
<!-- FILE_END: su2-emergence-volume-determinant.md -->

<!-- FILE_START: su2-emergence-dagger-unitarity.md -->
**Lemma.**
*Under the QOU hypotheses of [emergence of the gauge group](#thm:su2-emergence),
every tensor automorphism $g \in G$ preserves the Frobenius dagger
on $\tau(V)$; equivalently, $G \subseteq \mathrm{U}(2)$.*
<!-- FILE_END: su2-emergence-dagger-unitarity.md -->

