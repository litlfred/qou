<!-- FILE_START: lepton-meson-parallel-intro.md -->
The torus-knot dictionary that assigns leptons to $T(2,k)$ braids extends naturally to mesons. Both sectors share the Hecke algebra $H_3(q)$, but mesons carry a bar-involution asymmetry that distinguishes them from bar-symmetric baryons.
<!-- FILE_END: lepton-meson-parallel-intro.md -->

<!-- FILE_START: frobenius-lepton-meson-bridge.md -->
The standard representation $V_{(2,1)}$ of $H_3(q)$ restricts to $H_2(q)$ as the direct sum of the two lepton irreps:
$$
  V_{(2,1)} \big\downarrow_{H_2}
  = V_{(2)} \oplus V_{(1,1)}.
$$
The meson sector's sole mass-carrying partition is this entangled lepton spectrum.

At $H_2$, the lepton irreps $V_{(2)}$ and $V_{(1,1)}$ are separate channels. At $H_3$, they entangle inside the $2 \times 2$ Hoefsmit block of $V_{(2,1)}$. The off-diagonal element
$$
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
  \qquad
  a_\rho = \frac{h}{1 - q^{-2\rho}},
$$
is the binding amplitude that prevents the channels from decoupling. When $b = 0$, the meson reverts to two independent leptons. When $b \ne 0$, the channels mix, producing Hopf link binding.

By Frobenius reciprocity:
$$
  \langle \mathrm{Res}(V_{(2,1)}), V_{(2)} \rangle_{H_2}
  = \langle V_{(2,1)}, \mathrm{Ind}(V_{(2)}) \rangle_{H_3}
  = 1.
$$
Each lepton irrep appears exactly once in the restriction. 
1. The lepton mass ratio $m_\mu / m_\mathfrak{e}$ measures the separated $V_{(2)} \leftrightarrow V_{(1,1)}$ transition.
2. The meson mass ratio $m_K / m_\pi$ measures the same transition inside the entangled $(2,1)$ block.
3. The Hoefsmit off-diagonal $b$ is the amplitude at which the lepton pair-channel becomes the meson binding channel.

This branching explains why charge conjugation $C$ aligns with the bar involution at $H_2$ (separate 1-dim irreps) but diverges at $H_3$ (entangled 2-dim irrep with off-diagonal $b$).
<!-- FILE_END: frobenius-lepton-meson-bridge.md -->

<!-- FILE_START: frobenius-lepton-meson-bridge-interpretation.md -->
The underlying branching rule $V_{(2,1)} \downarrow V_{(2)} \oplus V_{(1,1)}$ is standard representation theory. The mathematical novelty lies in applying it topologically: mapping the physical entanglement of lepton channels directly to the mass-carrying partition of the meson sector.
<!-- FILE_END: frobenius-lepton-meson-bridge-interpretation.md -->

<!-- FILE_START: hoefsmit-binding-amplitude.md -->
The off-diagonal element $b$ of the Hoefsmit seminormal matrix for the standard representation $(2,1)$ of $H_3(q)$ satisfies:
$$
  b^2 = \frac{[3]_q}{[2]_q^2},
  \qquad
  1 - b^2 = \frac{1}{[2]_q^2}.
$$
**Mathematical Novelty:** Reinterpreting the rational relation $1-b^2 = 1/[2]_q^2$ as a discrete geometric de-entanglement fraction for the pion mass.

The pion decay $\pi \to \mu + \nu$ de-entangles the meson into $V_{(2)} \oplus V_{(1,1)}$. It releases a fraction $1 - b^2 = 1/[2]_q^2$ of the pion's rest energy:
$$
  E_{\mathrm{bind}} = \frac{m_\pi}{[2]_q^2}.
$$
The residual energy $m_\pi \cdot b^2$ flows into the de-entangled lepton channel $V_{(2)}$. These identities are exact in $q$, independent of the substrate parameter.
<!-- FILE_END: hoefsmit-binding-amplitude.md -->

<!-- FILE_START: hoefsmit-toroidal-ladder-locus.md -->
*Let $R$ be a field of characteristic zero and let $\alpha, \beta \in R$ be
constants. If the associated-Legendre order-ladder factor at degree
$n = d + \alpha$ and order $\mu = \beta$ reproduces the squared Hoefsmit
channel-mixing numerator identically in the axial distance $d$,*

$$
(d + \alpha - \beta)(d + \alpha + \beta + 1) \;=\; d^2 - 1
\qquad \text{for all } d \in R,
$$

*then*

$$
\alpha = -\tfrac{1}{2},
\qquad
\beta \in \bigl\{ \tfrac{1}{2},\; -\tfrac{3}{2} \bigr\},
$$

*i.e. $(n, \mu) = \bigl(d - \tfrac{1}{2}, \tfrac{1}{2}\bigr)$ up to the
Legendre reflection $\mu \mapsto -\mu - 1$. The half-integer degree shift —
the signature of the toroidal harmonic family $P^\mu_{\nu - 1/2}$ — is
forced by the Hoefsmit mixing structure, not imposed.*

## Context

The Hoefsmit seminormal block at axial distance $d$ mixes the two lepton
channels with amplitude $b$ satisfying
$b^2 = [d-1]_q [d+1]_q / [d]_q^2$
([prop:hoefsmit-binding-amplitude](#prop:hoefsmit-binding-amplitude) is the
$d = 2$ meson case $b^2 = [3]_q/[2]_q^2$). At $q \to 1$ the squared mixing
numerator is $d^2 - 1$. The associated-Legendre order-ladder factor is
$(n - \mu)(n + \mu + 1)$, and the toroidal harmonics — the separated
eigenfunctions around a vortex ring \cite{lebedev1965} — are exactly the
Legendre family at half-integer degree $\nu - \tfrac{1}{2}$
\cite{whipple1917}. The proposition says the match between the two
structures admits no freedom: the degree shift $-\tfrac{1}{2}$ and the
order $\tfrac{1}{2}$ are the unique solution.

Because the $q$-bracket identity $[d-1]_q[d+1]_q = [d]_q^2 - 1$ holds for
all $q$, the same forcing computation runs verbatim at the $q$-deformed
level (the coefficient matching gives $q^{2\alpha + 1} = 1$); the
half-integer shift survives $q$-deformation. The $q$-layer verification is
recorded in the computational witness
`computations/substrate/hoefsmit-toroidal-ladder-probe.witness.json`.

The physical reading: the two windings $(\mu, \nu)$ of a toroidal harmonic
$P^\mu_{\nu-1/2}(\cosh\eta)\, e^{i\mu\theta} e^{i\nu\varphi}$ are the two
local one-dimensional channel oscillations of a bound vortex pair, and the
forced $-\tfrac{1}{2}$ is the zero-point offset of the interpolating
channel ladder.
<!-- FILE_END: hoefsmit-toroidal-ladder-locus.md -->

<!-- FILE_START: three-strand-color-winding-rigidity.md -->
*On the $2$-dimensional $(2,1)$ Hoefsmit block of $H_3(q)$, the uniform
three-strand rotation $M = \rho_{(2,1)}(\sigma_1\sigma_2)$ has*

$$
\mathrm{tr}\,M = -1, \qquad \det M = 1, \qquad M^3 = \mathrm{Id},
$$

*for every $q$ with $q^4 \neq 1$. The eigenvalues of $M$ are the primitive
cube roots of unity, independently of $q$.*

The proof is Cayley–Hamilton: trace $-1$ and determinant $1$ give the
$\zeta_3$ quadratic $M^2 = -M - 1$, hence $M^3 = \mathrm{Id}$. The trace
identity is a rational-function identity in $q$ alone; the determinant
identity is exactly the Hoefsmit constraint
$\beta^2 = a_2 a_{-2} + 1$ on the binding amplitude
([prop:hoefsmit-binding-amplitude](hoefsmit-binding-amplitude.md)). The
Lean sibling states both over a generic field with $\beta$ carried as a
constrained variable (no square root, no $\mathbb{R}$), and derives the
cube identity from the two scalar facts.

Since the closures of $(\sigma_1\sigma_2)^k$ are the $(3,k)$ torus links,
the proposition says the compact winding of the three-strand torus-link
tower is **topological**: a $\zeta_3$ (color/triality) rotation that does
not flow with the substrate modulus, in contrast to the modulus-carrying
hyperbolic winding pair $q^{\pm 2k}$ of the $1$-dimensional channels. The
level-lattice and vortex readings — winding pair $(k,\ k \bmod 3)$ for the
three-strand (Borromean/nucleon) carrier, and the alternating-word
deformation of the same rotation — are developed in the channel-
interpolation audit and its witnesses
(`toroidal-level-selection-three-strand-probe`,
`alternating-tower-borromean-winding-probe`).
<!-- FILE_END: three-strand-color-winding-rigidity.md -->

<!-- FILE_START: self-dual-higgs-real-volume.md -->
The figure-eight knot $4_1$ (the Higgs mechanism) is amphichiral. Under the bar-involution $\sigma\colon q \mapsto q^{-1}$, its colored Jones polynomial is fixed:
$$
  J_N(4_1; q) = J_N(4_1; q^{-1}) \qquad (\forall N).
$$
Consequently, its Neumann–Zagier complex volume $\mathbb{V}(4_1) = \mathrm{Vol}(4_1) + i\,\mathrm{CS}(4_1)$ is real:
$$
  \mathrm{CS}(4_1) = 0,
  \qquad
  \mathrm{Re}\,\mathbb{V}(4_1) = \mathrm{Vol}(4_1) \approx 2.0299.
$$
The bare Higgs knot contributes only the real volume (mass) face. Its imaginary (decay) face vanishes, proving that $\mathfrak{Q}_\beta$ is not a property of the lone Higgs knot.

For the amphichiral $4_1$, both archimedean saddles (hyperbolic and torus) collapse onto the real axis. This self-duality is an algebraic identity over any commutative ring with a bar-involution and is formalized sorry-free.
<!-- FILE_END: self-dual-higgs-real-volume.md -->

<!-- FILE_START: meson-em-sinh-closed-form.md -->
Let $R$ be a field and $q \in R^\times$. Writing the substrate Planck quantum $\hbar_q = (q - 1)/q$, we have:
$$
  1 + \hbar_q - \hbar_q^2/2
  \;=\;
  1 + \frac{1 - q^{-2}}{2}
  \;=\;
  \frac{3 - q^{-2}}{2}
  \;=\;
  \frac{3 q^2 - 1}{2 q^2}.
$$
Substituting this closed form into the meson mass-squared ratio gives:
$$
  \frac{m_K^2}{m_\pi^2}
  \;=\;
  [3]_q \cdot [4]_q
  \;+\;
  \frac{\alpha_{\mathrm{em}}}{\pi}
  \cdot
  \frac{3 q^2 - 1}{2 q^2}.
$$
Both pieces are framework-derived. The strong fusion $[3]_q \cdot [4]_q$ originates from the qq̄ 2-body decomposition, and the sinh-channel EM correction from the CS-corrected $\alpha_{\mathrm{em}}$.
<!-- FILE_END: meson-em-sinh-closed-form.md -->

<!-- FILE_START: meson-qcg-fusion-identity.md -->
The q-integers satisfy the q-Clebsch–Gordan fusion identity:
$$
  [3]_q \cdot [4]_q \;=\; [2]_q + [4]_q + [6]_q.
$$
This forms the categorical foundation for the meson mass-squared ratio $m_K^2 / m_\pi^2$. Since a meson is a 2-body state, its mass-squared is a bilinear quantity evaluated on the pair.

**Mathematical Novelty:** Applying the standard q-Clebsch-Gordan fusion identity directly to the 2-body meson $m_K^2/m_\pi^2$ squared-ratio instead of relying on a 1-body character.
<!-- FILE_END: meson-qcg-fusion-identity.md -->

<!-- FILE_START: q-difference-viewpoint-method.md -->
Several framework quantities—the $\mathfrak{Q}_\beta$ element, the $\alpha_{EM}$ factor, and the Markov trace—are analysed via the $q$-difference shift $\sigma_q : q \mapsto q\zeta$ at roots of unity. 

A Habiro-type element satisfies a $q$-difference equation $(1 - \sigma_q)\,F = \delta\,(q;q)_\infty$. This shift is diagonalised by the Fourier transform over $\langle\zeta\rangle$. Because the $q$-Pochhammer vanishes at primitive roots of unity, evaluating the expansion truncates the sum to an exact, finite spectrum. When $F$ is rational, solving the equation reduces to partial-fraction decomposition.

This fibre-level viewpoint keeps $q$ formal. The operative symmetry is the bar involution $q \mapsto q^{-1}$, not a reality assumption.
<!-- FILE_END: q-difference-viewpoint-method.md -->

<!-- FILE_START: alpha-em-habiro-bar-involution.md -->
Let $H(q) = [2]_q\,(1 - h^2\alpha)$ be the $\alpha_{EM}$ Habiro element. 
1. $H$ is a fixed point of the bar involution: $H(q^{-1}) = H(q)$.
2. Its leading special values are $H(1) = 2$ and $H(-1) = -2$.

These fibre-level statements highlight that $H$ lies entirely in the charge-conjugation-symmetric sector. The lowest root-of-unity evaluation $H(\zeta_1) = 2$ supplies the classical leading term for $\alpha/(4\pi)$. The exact modular zero $H(\zeta_4) = 0$ is the structural dual of the $\mathfrak{Q}_\beta$ modular pole.
<!-- FILE_END: alpha-em-habiro-bar-involution.md -->

<!-- FILE_START: figure-eight-reeb-rotation.md -->
The figure-eight knot operator $M_{4_1} = (\sigma_1\sigma_2^{-1})^2$, acting on $V_{(2,1)}$, has eigenvalues of unit modulus:
$$
  \lambda_{4_1} = e^{\pm i\theta},
  \qquad |\lambda_{4_1}| = 1.
$$
The phase $\theta$ is the accumulated $q$-Reeb rotation angle. The $q$-Reeb flow rotates between the two lepton channels $V_{(2)}$ and $V_{(1,1)}$ that constitute $V_{(2,1)}$. The rotation angle $\theta$ is the natural invariant of this mixing. 

The muon-anchor identity $m_\mu / m_\mathfrak{e} = \mathrm{Vol}(4_1) / \hbar_q^2$ relies on the asymptotic volume, which represents the Kashaev limit of this rotation angle.
<!-- FILE_END: figure-eight-reeb-rotation.md -->

<!-- FILE_START: figure-eight-reeb-novelty-note.md -->
**Mathematical Novelty:** Reading the figure-eight eigenvalue on $V_{(2,1)}$ as a q-Reeb-rotation phase that connects to $\mathrm{Vol}(4_1)$ and the muon anchor.
<!-- FILE_END: figure-eight-reeb-novelty-note.md -->

<!-- FILE_START: pion-half-figure-eight.md -->
The pion braid $\mathfrak{M}_+ = (\sigma_1\sigma_2)^2\sigma_2\sigma_1$ and the half-figure-eight braid $\sigma_1\sigma_2^{-1}$ have identical eigenvalue phases when acting on $V_{(2,1)}$:
$$
  \mathrm{arg}\bigl(\lambda(\mathfrak{M}_+)\bigr)
  = \mathrm{arg}\bigl(\lambda(\sigma_1\sigma_2^{-1})\bigr).
$$
The figure-eight knot operator $(\sigma_1\sigma_2^{-1})^2$ is exactly the square of the pion-type rotation. 

The pion decay $\pi \to \mu + \nu$ de-entangles $V_{(2,1)}$. This decay inverts a half-Reeb-rotation: it releases the energy stored in the phase $\theta$. Two such decays would undo a full figure-eight rotation, connecting meson decay directly to the lepton mass ratio.
<!-- FILE_END: pion-half-figure-eight.md -->

<!-- FILE_START: pion-half-figure-eight-formalization-note.md -->
**Mathematical Novelty:** Formalising the relationship between meson decay energies and the lepton mass ratio (figure-eight volume) via the algebraic squaring relation $4_1 = (\sigma_1\sigma_2^{-1})^2$.
<!-- FILE_END: pion-half-figure-eight-formalization-note.md -->

<!-- FILE_START: outro-braids-and-knots.md -->
This concludes the substrate-arithmetic chapter. The categorical Hecke machinery, Wenzl bridge, and Gröbner–Shirshov formalisms developed here drive all subsequent numerical predictions, including the mass formula, binding energies, and the alpha-EM coupling. 
<!-- FILE_END: outro-braids-and-knots.md -->

