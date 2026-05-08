The algebra $\mathcal{A}_\infty$ is the direct limit
$\varinjlim \mathrm{End}_{\mathbf{C}}(A_n)$
([direct limit algebra](#def\:direct-limit-algebra)), and the quantum gauge
group $G_q = \mathrm{Aut}^{\otimes}(\tau)$
([quantum gauge group](#def\:quantum-gauge-group)) acts on it by conjugation.

*Existence.*
The fibre functor $\tau \colon \mathbf{C} \to \mathrm{Vect}_R$ is
$R$-linear and exact, sending $\mathbf{1}$ to $R$ and the
[Frobenius pairing](#def\:frobenius-pairing) on $A$ to a non-degenerate
$R$-bilinear form on $\tau(A)$.  At each finite level, the Frobenius trace
$\mathrm{tr}_n(\alpha) = (\varepsilon \circ \alpha \circ \eta)(\mathbf{1})$,
where $\eta$ and $\varepsilon$ are the Frobenius unit and counit, is
$G_q$-invariant by naturality (they are morphisms in $\mathbf{C}$,
hence invariant under monoidal automorphisms of $\tau$).
The :refterm[descent]{#descent} homomorphisms $\mathfrak{d}_n$ ([:refterm[descent]{#descent}](#lem\:descent)) are
equivariant and satisfy
$\mathrm{tr}_n \circ \mathfrak{d}_{n+1} = \mathrm{tr}_{n+1}$, so by the
universal property of the direct limit, the system $\{\mathrm{tr}_n\}$
determines a $G_q$-invariant $R$-linear functional
$\varphi \colon \mathcal{A}_\infty \to R$.

*Uniqueness.*
The vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
of the quantum observable universe axioms implies, via Schur's lemma,
that $\mathrm{End}_{G_q}(\mathbf{1}) \cong R$.  A $G_q$-invariant
functional $\psi \colon \mathcal{A}_\infty \to R$ must factor through
the $G_q$-fixed subalgebra $\mathcal{A}_\infty^{G_q}$, and the vanishing
condition forces this fixed subalgebra to be one-dimensional (any
non-scalar $G_q$-invariant endomorphism would yield a non-zero element
of $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$).  Hence $\psi$ is
determined up to scalar by its value on the identity, and normalising
$\psi(\mathrm{id}) = 1$ gives $\psi = \varphi$.  $\square$
