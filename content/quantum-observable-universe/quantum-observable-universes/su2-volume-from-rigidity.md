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
