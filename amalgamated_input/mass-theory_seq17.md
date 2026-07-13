<!-- FILE_START: exceptional-divisor-reeb-intro.md -->
The Lagrange resolvents diagonalise the $C_5$-action on the genus-$4$ base surface, but do not provide an operator algebra acting along the resolvent eigenlines. We blow up a brane point $p$ and construct the operators on the resulting exceptional divisor. The blow-up replaces $p$ with a $\mathbb{CP}^1$ supporting a Reeb circle bundle. Vertex operators on this bundle establish the state–operator correspondence.

We fix the static geometry: the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$, the Reeb bundle $\mathcal{R}_p \cong S^3 \xrightarrow{\pi_H} \mathcal{S}_p$, the Reeb vector field, and the vertex operator dictionary that pins vertex-algebra data to the categorical structure.

We introduce dynamics on the color coordinates. The $q$-Reeb flow provides the equation $\dot\psi = q$ on each active sector. Two-strand localisation applies when a flow targets adjacent strands.

We define six canonical knot operators. Threading the flow with each $S_3$ braid word produces the identity, two adjacent transpositions $\sigma_1, \sigma_2$, the Garside element $\sigma_1\sigma_2\sigma_1$, and the two 3-cycles. We supply explicit trajectory ODEs and boundary permutations.

At the boundaries $\phi \in \{0, \pi\}$, the three colour tubes fuse into a triply-ramified disc. The ramified-disc fusion proposition identifies the monodromy as the $S_3$ Galois action on Lagrange resolvents, linking the Reeb trajectory directly to the boundary observable.

Removing tubular neighbourhoods of the trajectories from $\mathcal{R}_p$ leaves a knot complement. The Reeb-bundle complement encodes the Markov-trace observable as the JSJ-graded sum $\sum \rho_F(P_i) V_{\mathrm{hyp}}(P_i)$. Pure rotational 3-cycles trace torus knots, yielding a Seifert-fibered complement with $V_{\mathrm{hyp}} = 0$. Garside and Borromean trajectories cross Heegaard tori, producing a hyperbolic complement with strictly positive volume.
<!-- FILE_END: exceptional-divisor-reeb-intro.md -->

<!-- FILE_START: reeb-bundle.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU. Let $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a brane point $p$. The **Reeb bundle** at $p$ is the principal $U(1)$-bundle

$$
  \mathcal{R}_p = \bigl(S^3 \xrightarrow{\pi_H} \mathcal{S}_p \cong S^2, \xi_q\bigr),
$$

where $\pi_H$ is the Hopf fibration and $\xi_q$ is the $q$-Reeb vector field generating the $U(1)$ fibre action. The total space $S^3$ carries the contact structure $\ker\varTheta|_{S^3}$. The substrate parameter $q$ determines the connection $1$-form: the holonomy around a generator of $\pi_1(S^1)$ is $e^{2\pi i / [2]_q}$, where $[2]_q = q + q^{-1}$ is the quantum integer.

The Reeb bundle provides three structures. The base $\mathcal{S}_p \cong S^2$ parametrises the internal colour space. The fibre $U(1)$ aligns with the Reeb direction $\xi_q$, acting as the axis where observations commute. The total space $S^3$ forms the arena where braid words in $B_n$ are evaluated via the Iwahori--Hecke algebra $H_n(R, q)$.
<!-- FILE_END: reeb-bundle.md -->

<!-- FILE_START: reeb-exceptional-divisor.md -->
The Reeb vector field $\xi_q$ provides the dynamical complement to the static topology of Bring's surface. The surface supplies the genus-$4$ handles. The Reeb vector supplies the flow through them. The substrate parameter $q$ sets the flow's pitch.

In the classical limit $q\to 1$, the torsion coupling vanishes. The phase rotation $w_k\mapsto\zeta^kw_k$ loses its temporal component. The chiral tubes freeze in the configuration defined by the power-sum equations. This yields a conical metric limit: curvature concentrates at the blow-up points without a circulating torsion field to smooth it. The Reeb field $\xi_q$ becomes the classical Reeb field $\xi_1$. The Heisenberg commutator $[\hat{X},\hat{P}]_q\to 0$. The Bring variety collapses to a non-rotating algebraic surface.

Blowing up a spacetime defect $z_c$ where chiral sheets merge replaces the singularity with an exceptional divisor $\mathcal{S}_c\cong\mathbb{P}^1(\mathbb{C})\cong S^2$. This sphere bounds the macroscopic coordinates $(x_0,x_1)$ from the internal chiral modes $(w_1,w_2,w_3)$. It resolves the self-intersections of the chiral fibres. The $C_5$ phase rotation now circulates around the exceptional divisor.

On the blown-up surface, $\xi_q$ generates the $U(1)$ action rotating the chiral fibre. The total space of this $U(1)$ fibration is the Reeb bundle $\mathcal{R}_c$. The $q$-deformed Reeb flow $\phi_t^q$ on $\mathcal{S}_c$ generates the Hopf fibration, with $q$ controlling the rotation's pitch. The vector field $\xi_q$ establishes the time-like direction, driving the spectral modes to execute the phase rotation $w_k\mapsto\zeta^kw_k$. All braiding occurs within this Reeb bundle.

As $q\to\infty$, the spinning maximizes and $[\hat{X},\hat{P}]_q\to J$. As $q\to 1$, the spinning stops, the Reeb field trivialises, and the topology reduces to a static cone.
<!-- FILE_END: reeb-exceptional-divisor.md -->

<!-- FILE_START: vertex-operator.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU, let $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a brane point $p$, and let $\mathcal{R}_p$ be the Reeb bundle over $\mathcal{S}_p$.

In the QOU, the formal variable $z$ of the vertex operator algebra is the affine coordinate $z = v_1/v_2$ on the projective line $\mathcal{S}_p$. This matches the contact affine coordinate $Z = \alpha_H / \iota_\xi\alpha$ restricted to the fibre $\mathcal{S}_p$. On the affine chart $v_2 \neq 0$, $z$ generates $\mathbb{C}[z]$.

The **vertex operator algebra** at $p$ is the triple $(V, Y, |0\rangle)$. The $\mathbb{Z}_{\geq 0}$-graded state space is the brane tower:

$$
  V = \bigoplus_{n \geq 0} V_n, \qquad V_n = A_n = J^n(A_0),
$$

where $A_0 = \mathcal{O}(\mathrm{SU}_q(2))$ and $J^n$ is the $n$-th jet prolongation. The grading $n$ is the conformal weight, defined as the eigenvalue of the zero-mode Reeb charge operator $L_0 = \xi_q^{(0)}$.

The map $Y \colon V \longrightarrow (\mathrm{End}V)[\![z, z^{-1}]\!]$ assigns to each state $a \in V_n$ the **vertex operator**:

$$
  Y(a, z) = \sum_{m \in \mathbb{Z}} a_m z^{-m-1},
$$

where the modes $a_m \in \mathrm{End}V$ derive from the $R$-matrix insertion:

$$
  a_m = \oint_{|z| = 1} Y(a, z) z^m \frac{dz}{2\pi i} = \mathrm{tr}_M\!\bigl(\check{R}_{(a)} z^m\bigr).
$$

Here $\check{R}_{(a)} = P \circ \mathcal{R}$ applies the braid operator to the state $a$, and $\mathrm{tr}_M$ is the Markov trace. The contour integral traces a fibre of the Reeb bundle $\mathcal{R}_p$.

The vacuum is the unknot $|0\rangle = 1 \in A_0$. The translation operator $T = L_{-1} = j \colon A_n \to A_{n+1}$ advances one level in the brane tower.

When insertion points $z$ and $w$ collide on $\mathcal{S}_p$, the operator product expansion

$$
  Y(a, z) Y(b, w) \sim \sum_{n \geq 0} \frac{Y(c_n, w)}{(z - w)^{n+1}}
$$

has its leading singularity governed by the Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. This corresponds to the Skein relation $L_+ - L_- = (q - q^{-1}) L_0$. The collision represents two strands meeting on $\mathcal{S}_p$. The resolution into $L_+$, $L_-$, $L_0$ forms the OPE decomposition. The eigenvalues $q$ and $-q^{-1}$ of $\sigma_i$ correspond to the symmetric and antisymmetric OPE channels.
<!-- FILE_END: vertex-operator.md -->

<!-- FILE_START: vertex-operator-dictionary.md -->
The vertex operator definition establishes the dictionary between the standard VOA formalism and QOU structures. The classical connection relies on the KZ equation for the WZW model, where monodromy corresponds to the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$. The QOU makes this correspondence geometric.

The CFT worldsheet is the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$. The target space is the Reeb bundle $\mathcal{R}_p \to \mathcal{S}_p$. The time direction is the Reeb flow $\xi_q$. The state space at fixed time is the brane tower $\bigoplus A_n$. The Reeb bundle serves as the arena for braiding and as the total space of the string whose quantisation yields the VOA. The substrate parameter $q = e^{2\pi i/(k+2)}$ links algebraic deformation to the geometric pitch of the Reeb connection.
<!-- FILE_END: vertex-operator-dictionary.md -->

<!-- FILE_START: q-reeb-flow-on-color-coords.md -->
Let $\mathfrak{r}(\phi,\psi), \mathfrak{g}(\phi,\psi), \mathfrak{b}(\phi,\psi)$ be the color-sector parametrisation on the Reeb bundle $\mathcal{R}_p$. The $q$-Reeb flow $\phi^q_t$ acts on the red sector by

$$
  \phi^q_t \cdot \mathfrak{r}(\phi,\psi) \;=\; \mathfrak{r}(\phi,\,\psi + k^{(r)}\,q\,t).
$$

The green and blue sectors follow analogous equations with rate multipliers $k^{(g)}, k^{(b)} \in \mathbb{Z}$. The braid generator determines the signed rate multiplier $k^{(s)}$. A spectator sector has $k^{(s)} = 0$. In a two-strand subsystem, the active leading strand has $k^{(s)} = +1$, and the partner strand counter-rotates with $k^{(s)} = -1$ to preserve the centre-of-mass. The flow parameter $t \in [0,\pi]$ tracks the latitude, from $t=0$ at the south foundry to $t=\pi$ at the north foundry.

The flow accumulates the color-twist factor $q t$ linearly. A strand at $\psi = 0$ on the south foundry arrives at $\psi = q\pi$ on the north foundry. Sequential flows compose additively: $\phi^q_{t_1} \circ \phi^q_{t_2} = \phi^q_{t_1 + t_2}$. A braid word acts as a concatenation of partial flows. This realizes the Heisenberg commutator $[\hat X,\hat P]_q = J\hbar_q$.

Uniform-vortex 3-cycle generators apply $k = +1$ or $k = -1$ to all sectors simultaneously. The signed-rate machine links the algebraic Hecke generator $\sigma_i$ to the explicit ODE on color-sector coordinates.
<!-- FILE_END: q-reeb-flow-on-color-coords.md -->

<!-- FILE_START: six-canonical-knot-operators.md -->
**Proposition (conditional on [`def:q-reeb-flow-on-color-coords`](#def:q-reeb-flow-on-color-coords)).**
*Let $\mathcal{R}_p$ be the Reeb bundle over the exceptional divisor at brane point $p$. For each of the six elements $w \in S_3$, the corresponding braid word $\beta_w \in B_3$ generates a unique trajectory across $\mathcal{R}_p$. Its boundary footprint realises $w$ as a Galois permutation of the colour tubes.*

We trace the trajectories across the Reeb bundle.

1. **Identity.** All three sectors are spectators. Each strand traces a constant-meridian line from south to north. The boundary footprint is the identity.
2. **Adjacent transpositions $\sigma_1, \sigma_2$.** The generator $\sigma_1$ activates the red and green sectors with opposite rates. The centre of mass is conserved. The difference accumulates a phase of $\pi$. At the north foundry, red and green swap. The blue spectator remains unchanged. This realises the transposition $(rg)$.
3. **Garside $\sigma_1\sigma_2\sigma_1$.** The latitude interval decomposes into three sub-intervals. The green sector acts as the intermediary. Red and blue exchange via the compound flow. The boundary footprint is the non-adjacent transposition $(rb)$.
4. **3-cycles $\sigma_1\sigma_2$ and $\sigma_2\sigma_1$.** All three sectors rotate uniformly with rate $+q$ or $-q$. The trajectory traces a right-handed or left-handed helix on a Heegaard torus. The output boundary realises $(rgb)$ or $(rbg)$.

The six boundary permutations are pairwise distinct, establishing a bijection onto $S_3$. This explicitly constructs the $S_3$ holonomy of $\rho: B_3 \to \mathrm{SU}(2)$ as Reeb-bundle trajectories.

The 3-cycle trajectories lie on a Heegaard torus. Their complement is Seifert-fibered with $V_{\mathrm{hyp}} = 0$. The Garside trajectory crosses between Heegaard tori, yielding a hyperbolic piece with positive volume.
<!-- FILE_END: six-canonical-knot-operators.md -->

<!-- FILE_START: garside-as-compound-flow.md -->
The Garside element $\Delta_3 = \sigma_1\sigma_2\sigma_1$ has a three-stage compound Reeb-flow trajectory.

The word divides the latitude interval $[0,\pi]$ into three equal sub-intervals. In each sub-interval, two sectors spiral while the third spectates: $(rg)$, then $(gb)$, then $(rg)$. Threading the three yields the non-adjacent transposition $(rb)$.

The dual decomposition $\sigma_2\sigma_1\sigma_2$ implements $(gb)$, then $(rg)$, then $(gb)$. The two flow sequences trace distinct intermediate trajectories for the green sector, but produce the same boundary permutation $(rb)$. The braid relation encodes the equivalence of these two boundary-matched compound trajectories.

Unlike the 3-cycle global vortex, the Garside flow is piecewise. The angular rate switches sign at the boundaries of the sub-intervals. The solution concatenates three exact two-strand ODEs.

Because the trajectory crosses between the two Heegaard tori of $\mathcal{R}_p \cong S^3$, the knot complement does not admit a full Seifert fibration. Its JSJ decomposition contains a hyperbolic piece, yielding a positive Bloch-Wigner sum.
<!-- FILE_END: garside-as-compound-flow.md -->

<!-- FILE_START: garside-flow-explicit-closed-form.md -->
The Garside trajectory $\sigma_1\sigma_2\sigma_1$ admits a closed-form solution by direct composition. The underlying flow is piecewise-linear in the angular coordinate.

Divide the latitude $\phi \in [0, \pi]$ into three equal sub-intervals $I_1, I_2, I_3$. The Garside word applies $\sigma_1$ on $I_1$, $\sigma_2$ on $I_2$, and $\sigma_1$ on $I_3$. The rate multiplier sequences are $(+1, -1, 0)$ for $\sigma_1$ and $(0, +1, -1)$ for $\sigma_2$. 

Applying the additive composition rule tracks the angular positions $\psi^{(s)}$ from their input values $\psi^{(s)}_0$. The red sector accumulates $q\phi$ during $I_1$ and $I_3$. The green sector decreases during $I_1$ and $I_3$, and increases during $I_2$. The blue sector remains stationary during $I_1$ and $I_3$, and decreases during $I_2$. 

Evaluating at the output boundary $\phi = \pi$ yields the net color-twist accumulated by each sector:
$\Delta\psi^{(r)} = +2q\pi/3$, $\Delta\psi^{(g)} = -q\pi/3$, and $\Delta\psi^{(b)} = -q\pi/3$. The green sector acts as the displacement carrier between the red and blue swap. The three-sector centre of mass $\Delta\psi^{(r)} + \Delta\psi^{(g)} + \Delta\psi^{(b)}$ sums to zero, confirming the transposition signature.

The flow equation $\dot\psi = k\,q$ represents a piecewise-affine ODE. The formal-algebraic solution demonstrates that the Garside trajectory crosses both Heegaard tori, confirming its non-Seifert JSJ verdict and positive volume.
<!-- FILE_END: garside-flow-explicit-closed-form.md -->

<!-- FILE_START: ramified-disc-fusion.md -->
*Let $D \subset \mathcal{S}_p$ be a small open disc around a foundry boundary. Let $\widetilde{D} \subset \mathcal{R}_p$ denote the preimage $\pi_H^{-1}(D)$ together with the three colour-tube sections. Then:*

1. **Fusion.** *$\widetilde{D}$ is a single connected topological disc with degree-$3$ ramification at the centre. The three sectors coalesce at the centre.*
2. **Monodromy.** *The monodromy around $\partial D$ is the cyclic group $C_3 = \langle (rgb) \rangle$. The full Galois group of the regular closure is the symmetric group $S_3$.*
3. **Comparison with Lagrange resolvents.** *The $S_3$ monodromy agrees with the $S_3$ action on the Lagrange resolvents. The cyclic generator $(rgb)$ corresponds to the cyclic permutation $w_k \mapsto \zeta w_k$. The transpositions correspond to parity reflections.*

At the foundry boundary $\phi \to 0$ or $\pi$, the latitude factor $\sin\phi \to 0$ collapses the three sectors onto their common axis, fusing the meridian seams into a triple point. The resulting quotient topology is a ramified disc. A loop around $\partial D$ lifts to paths connecting each sector to its cyclic successor. The monodromy is $(rgb)$. Adjoining orientation reversals yields $S_3$. The resolvents $w_k$ derive from the color coordinates via a cube-root DFT. The permutation $(c_r, c_g, c_b) \mapsto (c_g, c_b, c_r)$ sends $w_k \mapsto \zeta^{-k} w_k$. This aligns the geometric monodromy with the algebraic $S_3$ action.
<!-- FILE_END: ramified-disc-fusion.md -->

<!-- FILE_START: ramified-disc-fusion-interpretation.md -->
**Remark.** The proposition links the internal Reeb flow to the boundary observable. The $S_3$ Galois action of the algebraic braid-group representation is read directly from the monodromy of the ramified-disc cover at the foundry boundary. This establishes the correspondence mapping a Reeb trajectory to its boundary Galois permutation.
<!-- FILE_END: ramified-disc-fusion-interpretation.md -->

<!-- FILE_START: reeb-bundle-complement-equals-volume.md -->
**Proposition (conditional on [`conj:mass-volume-factorization`](#conj:mass-volume-factorization)).**
*Let $\mathcal{R}_p \cong S^3$ be the Reeb bundle. Let $K_\beta$ denote the closure of the colour-tube trajectory under $\beta \in B_3$. The categorical Markov-trace observable equals the JSJ-graded sum over the hyperbolic pieces $P_i$ of the knot complement $\mathcal{R}_p \setminus \nu(K_\beta)$:*

$$
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr) \;=\; \sum_{P_i \text{ hyperbolic}} \rho_F(P_i)\,V_{\mathrm{hyp}}(P_i),
$$

*where $V_{\mathrm{hyp}}$ is the Thurston volume and $\rho_F(P_i)$ is the Frobenius packing density.*

This presents the geometric face of the mass-volume factorisation conjecture. The observable evaluates inside the Reeb bundle. Its value equals the hyperbolic volume of its complement. Pure-rotation 3-cycles trace Heegaard torus trajectories, leaving a Seifert-fibered complement where $V_{\mathrm{hyp}} = 0$. Non-torus compositions cross Heegaard tori, leaving a hyperbolic complement with positive volume.
<!-- FILE_END: reeb-bundle-complement-equals-volume.md -->

<!-- FILE_START: torus-knot-zero-volume-via-reeb.md -->
The 3-cycle braid words $\sigma_1\sigma_2$ and $\sigma_2\sigma_1$ rotate all three colour tubes uniformly with rate $\dot\psi = \pm q$. The trajectory traces a helix on a Heegaard torus $T^2 \subset S^3$. The trajectory completes a $T_{2,3}$ torus knot (trefoil). 

The complement of any torus knot admits a Seifert fibration. It supports no hyperbolic structure, meaning $V_{\mathrm{hyp}}(T_{m,n}) = 0$. The global-vortex flow maintains parallel strands, aligns with the Hopf fibre, and closes onto the Heegaard torus, guaranteeing a Seifert-fibered complement.

Consequently, the topological mass component of the Markov-trace observable vanishes for torus configurations. Torus knots yield zero hyperbolic volume, contributing only to the counting part of the trace.
<!-- FILE_END: torus-knot-zero-volume-via-reeb.md -->

<!-- FILE_START: hyperbolic-knot-positive-volume-via-reeb.md -->
The Garside element $\Delta_3$ and the Borromean braid $(\sigma_1\sigma_2^{-1})^3$ form non-torus Reeb-flow trajectories with positive hyperbolic volume.

The Garside flow swaps the red and blue tubes across three sub-intervals. It crosses between the two Heegaard tori. Its complement is not Seifert-fibered, and its JSJ decomposition contains a hyperbolic piece with a strictly positive Bloch–Wigner sum.

The Borromean braid traces a link whose complement is the Gieseking–Meyerhoff manifold. Its hyperbolic volume is $V_{\mathrm{hyp}} = 8\,G$, derived from two regular ideal octahedra.

The figure-eight knot $4_1$ sits between the trefoil and the Borromean link. It carries the minimal hyperbolic volume $2 v_3 \approx 2.0299$. Its Reeb-flow trajectory $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ crosses between Heegaard tori twice.

Only hyperbolic pieces contribute to the JSJ-graded mass factorization. Torus trajectories remain geometrically invisible because they never enter the bulk hyperbolic regime. The trajectory pattern determines the JSJ verdict.
<!-- FILE_END: hyperbolic-knot-positive-volume-via-reeb.md -->

