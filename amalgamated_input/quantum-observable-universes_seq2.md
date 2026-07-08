<!-- FILE_START: frobenius-su2.md -->
Let $A = \mathcal{O}(\mathrm{SU}(2))$ equipped with pointwise multiplication $\mu(f \otimes g) = fg$. We define the Frobenius form as the Haar integral $\int_A = \int_G$. The dual comultiplication is given by $\Delta_\mu(f)(g,h) = \int_G f(xg)\overline{h(x)}dx$. The Frobenius relation precisely encodes the associativity of convolution: integrating $f(xy)g(y)$ over $y$ yields the same result whether convolved first with $f$ or first with $g$.
<!-- FILE_END: frobenius-su2.md -->

<!-- FILE_START: dagger-su2.md -->
The representation category $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ inherits a canonical dagger structure from the antipode. For any equivariant map $f \colon V_j \to V_k$, its dagger $f^{\dagger}$ is the standard Hilbert-space adjoint, satisfying $\langle f^{\dagger}(w), v \rangle_j = \langle w, f(v) \rangle_k$. This adjoint remains equivariant because the inner product on each irreducible representation $V_j$ is $\mathrm{SU}(2)$-invariant. On the algebra $A = \mathcal{O}(\mathrm{SU}(2))$, the dagger corresponds to complex conjugation composed with inversion: $f^{\dagger}(g) = \overline{f(g^{-1})}$. Unitarity manifests categorically as the positivity of the composite $f^{\dagger} \circ f = \lVert f(1) \rVert^2 > 0$ for any non-zero state $f \colon \mathbb{C} \to V_j$.
<!-- FILE_END: dagger-su2.md -->

<!-- FILE_START: volume-from-rigidity.md -->
Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal category, and let $V$ be a simple object that is symplectically self-dual: there exists an isomorphism $\phi \colon V \xrightarrow{\sim} V^{\vee}$ satisfying $\phi^{\vee} = -\phi$. This alternating condition forces $\mathrm{rank}(V) = 2$. Specifically, the evaluation map $\mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ factors through $\Lambda^2 V$, producing an epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$. For $\epsilon$ to be non-degenerate, we must have $\mathrm{rank}(\Lambda^2 V) = 1$. The volume form factorization is:

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

This construction intrinsically satisfies the volume form requirement of the QOU axioms.
<!-- FILE_END: volume-from-rigidity.md -->

<!-- FILE_START: su2-volume-from-rigidity.md -->
In the case of $\mathrm{SU}(2)$, let $V = V_{1/2} \cong \mathbb{C}^2$. The symplectic form $\phi = \begin{smallmatrix} 0 & 1 \\ -1 & 0 \end{smallmatrix}$ identifies $V \cong V^{\vee}$ with $\phi^{\vee} = -\phi$. Applying the volume form factorization, the evaluation pairing becomes the determinant $B(v, w) = v_1 w_2 - v_2 w_1$. Because $B$ is alternating, it factors through the wedge product, yielding the isomorphism $\epsilon(v \wedge w) = \det(v, w)$ from $\Lambda^2 \mathbb{C}^2$ to $\mathbb{C}$. Any tensor automorphism $g \in G$ scales the volume form by its determinant: $\Lambda^2 g = \det(g) \cdot \mathrm{id}$. The categorical requirement that $\epsilon$ is preserved forces $\det(g) = 1$, restricting the gauge group from $\mathrm{GL}(2, \mathbb{C})$ to at least $\mathrm{SL}(2, \mathbb{C})$.
<!-- FILE_END: su2-volume-from-rigidity.md -->

<!-- FILE_START: su2-emergence.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The gauge group of tensor automorphisms $G = \mathrm{Aut}^{\otimes}(\tau)$ is forced to be $\mathrm{SU}(2)$ (or its split real form $\mathrm{SL}(2, \mathbb{R})$, depending on the signature of the Frobenius pairing).
<!-- FILE_END: su2-emergence.md -->

<!-- FILE_START: su2-emergence-volume-determinant.md -->
Every tensor automorphism $g \in G$ of the fibre functor $\tau$ satisfies the volume constraint $\det(g_V) = 1$. Consequently, $G \subseteq \mathrm{SL}(2, \mathbb{C})$.
<!-- FILE_END: su2-emergence-volume-determinant.md -->

<!-- FILE_START: su2-emergence-dagger-unitarity.md -->
Every tensor automorphism $g \in G$ preserves the Frobenius dagger structure on $\tau(V)$. Consequently, $G \subseteq \mathrm{U}(2)$.
<!-- FILE_END: su2-emergence-dagger-unitarity.md -->

