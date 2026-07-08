<!-- FILE_START: instanton-intro.md -->
The gauge term of the canonical action takes its extremal value when the curvature is $\star_q$-self-dual. We define the categorical instanton and read off its consequences for the categorical Lagrangian on-shell.
<!-- FILE_END: instanton-intro.md -->

<!-- FILE_START: categorical-instanton.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with connection $\nabla$ and $q$-Hodge star $\star_q$. The connection $\nabla$ is an **instanton** if its curvature $F_\nabla \in \Omega^2(A)$ is $\star_q$-self-dual: $\star_q F_\nabla =  F_\nabla$. Equivalently, the curvature factors through the self-dual projection.
<!-- FILE_END: categorical-instanton.md -->

<!-- FILE_START: categorical-instanton-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $q$-Hodge star $\star_q$. There exists a categorical connection $\nabla$ whose curvature $F_\nabla$ is $\star_q$-self-dual.
<!-- FILE_END: categorical-instanton-exists.md -->

<!-- FILE_START: categorical-instanton-unique.md -->
Two categorical instantons $\nabla_1$ and $\nabla_2$ of the same topological charge $c_2(\nabla_i) = k \in H^4$ coincide up to a categorical gauge transformation $g \in \mathrm{Aut}^\otimes(\tau)$:

$$
  \nabla_2 \;=\; g \cdot \nabla_1 \cdot g^{-1} + g\,dg^{-1}.
$$

The categorical instanton moduli space $\mathcal{M}^{\mathrm{inst}}_k$ is parameterised by $H^4$.
<!-- FILE_END: categorical-instanton-unique.md -->

<!-- FILE_START: instanton-on-shell.md -->
On an instanton background, the curvature is $\star_q$-self-dual. The Bogomolny decomposition yields

$$
  \lVert F_\nabla \rVert^2 = c_2(A) + 2\lVert F_\nabla^- \rVert^2.
$$

The instanton condition forces $F_\nabla^- = 0$, reducing the gauge sector to the topological term $\mathcal{D}_\nabla^{2} = c_2(A)$. The categorical Lagrangian simplifies on-shell to

$$
  \mathcal{L}_q\big|_{\text{instanton}} = c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi.
$$

There are no dynamical gauge degrees of freedom beyond topology. All physics lies in the matter equation $\mathcal{D}_\nabla\psi = 0$. The wavefront is determined by the background topology, dictating the Green's function of $\mathcal{D}_\nabla$.
<!-- FILE_END: instanton-on-shell.md -->

<!-- FILE_START: categorical-irreducible.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Any categorical instanton $\nabla$ is irreducible: $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1},\mathrm{Ad}(A)) = 0$.
<!-- FILE_END: categorical-irreducible.md -->

<!-- FILE_START: categorical-self-duality.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Every connection $\nabla$ that is a critical point of the categorical Yang--Mills functional

$$
  S[\nabla] =  \int_A\!\bigl(\star_q(F_\nabla) \cdot F_\nabla\bigr)
$$

is an instanton.
<!-- FILE_END: categorical-self-duality.md -->

<!-- FILE_START: self-dual-ses.md -->
The $q$-Hodge star $\star_q$ is an involution on $\Omega^2(A)$. Its eigenspaces provide the splitting $\Omega^2(A) = \Omega^+(A) \oplus \Omega^-(A)$ and the short exact sequence

$$
  0 \to \Omega^-(A) \to \Omega^2(A) \to \Omega^+(A) \to 0,
$$

where $\Omega^{\pm}(A) = \ker(\mathrm{id} \mp \star_q)$. The instanton condition is exactly $F_\nabla^- = 0$. In the archimedean realisation, this specialises to $0 \to \Gamma(\Lambda^-\!H^* \otimes \mathrm{Ad}(P)) \to \Gamma(\Lambda^2 H^* \otimes \mathrm{Ad}(P)) \to \Gamma(\Lambda^+\!H^* \otimes \mathrm{Ad}(P)) \to 0$.
<!-- FILE_END: self-dual-ses.md -->

<!-- FILE_START: hopf-non-cocommutativity.md -->
The Hopf comultiplication $\Delta \colon A \to A \otimes A$ of the Frobenius--Hopf object is coassociative but not cocommutative when $q \neq 1$. The failure is controlled by the universal $R$-matrix: $\sigma \circ \Delta = \mathrm{Ad}_{R_q} \circ \Delta$. This non-cocommutativity provides the algebraic origin of quantum uncertainty, preventing independent observations from commuting.
<!-- FILE_END: hopf-non-cocommutativity.md -->

