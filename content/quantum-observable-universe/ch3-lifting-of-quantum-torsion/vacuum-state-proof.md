
The algebra $\mathcal{A}_\infty$ is the direct limit
$\varinjlim \mathrm{End}_{\mathcal{C}}(A_n)$
([direct limit algebra](#def:direct-limit-algebra)), and the quantum gauge
group $G_q = \mathrm{Aut}^{\otimes}(\omega)$
([quantum gauge group](#def:quantum-gauge-group)) acts on it by conjugation.

*Existence.*
The fibre functor $\omega \colon \mathcal{C} \to \mathrm{Vect}_R$ is
$R$-linear and exact.  It sends the unit $\mathbf{1} \in \mathcal{C}$ to
$R$ and the Frobenius pairing on $A$ to a non-degenerate $R$-bilinear
form on $\omega(A)$.  At each finite level, $\omega$ maps
$\mathrm{End}_{\mathcal{C}}(A_n)$ to a finite-dimensional $R$-algebra
$\mathrm{End}_R(\omega(A_n))$.  The Frobenius trace
$\mathrm{tr}_n \colon \mathrm{End}_{\mathcal{C}}(A_n) \to R$ defined by
$$
  \mathrm{tr}_n(\alpha)
  \;=\;
  (\varepsilon \circ \alpha \circ \eta)(\mathbf{1}),
$$
where $\eta \colon \mathbf{1} \to A_n$ and $\varepsilon \colon A_n \to
\mathbf{1}$ are the Frobenius unit and counit, is $G_q$-invariant:
for any $g \in G_q$, $\mathrm{tr}_n(g \cdot \alpha) =
\mathrm{tr}_n(\alpha)$ by the naturality of $\eta$ and $\varepsilon$
(they are morphisms in $\mathcal{C}$, hence invariant under monoidal
automorphisms of the fibre functor).

The descent homomorphisms $\mathfrak{d}_n$ ([descent](#lem:descent)) are
equivariant and satisfy $\mathrm{tr}_n \circ \mathfrak{d}_{n+1} =
\mathrm{tr}_{n+1}$ (compatibility of the Frobenius trace with descent).
By the universal property of the direct limit, the system
$\{\mathrm{tr}_n\}$ determines a $G_q$-invariant $R$-linear functional
$\varphi \colon \mathcal{A}_\infty \to R$.

*Uniqueness.*
The vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
of the quantum observable universe axioms implies, via Schur's lemma
applied in $\mathcal{C}$, that $\mathrm{End}_{G_q}(\mathbf{1}) \cong R$.
More precisely: a $G_q$-invariant functional
$\psi \colon \mathcal{A}_\infty \to R$ must factor through the
$G_q$-fixed subalgebra $\mathcal{A}_\infty^{G_q}$.  The vanishing
condition forces this fixed subalgebra to be one-dimensional (generated
by the identity), since any non-scalar $G_q$-invariant endomorphism
would yield a non-zero element of
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$.  Therefore $\psi$ is
determined up to scalar by its value on the identity, and normalising
$\psi(\mathrm{id}) = 1$ gives $\psi = \varphi$.
