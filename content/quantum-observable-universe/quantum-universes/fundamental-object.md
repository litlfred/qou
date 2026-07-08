Let $\mathbf{C}$ be an $R$-linear rigid :refterm[monoidal category]{#monoidal-category}. A **fundamental object** is a simple object $V \in \mathbf{C}$ equipped with a non-degenerate volume form
$$
  \epsilon \colon \Lambda^2 V \longrightarrow \mathbf{1}.
$$
The volume constraint forces $\mathrm{rank}(V) = 2$: in $\mathrm{SU}(2)$ it singles out $V = V_{1/2} \cong \mathbb{C}^2$, and abstractly $V$ is the unique simple object of categorical dimension $2$. Every other simple object is an exterior or symmetric power of $V$, so $V$ generates $\mathbf{C}$ as a tensor category.

Equivalently, $\epsilon$ makes $V$ a *symplectic self-dual object*: paired with its adjoint coform $\eta \colon \mathbf{1} \to V \otimes V$ it satisfies the two snake identities, so $V$ is its own dual. Self-duality through an antisymmetric form is exactly what distinguishes $\mathrm{SL}_2 / \mathrm{SU}(2)$ from $\mathrm{GL}_2$ \cite{deligne1990}.
