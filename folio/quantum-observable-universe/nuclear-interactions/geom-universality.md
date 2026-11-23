**Conjecture (universality of $\mathrm{Geom}(K)$, conditional on hyperbolic volume transcendence).**
*The categorical volume form, evaluated on the knot complement $S^3 \setminus K$ through the fibre functor $\tau$, yields $\mathrm{Vol}(K)$ for hyperbolic knots and $\mathrm{CS}(K)$ for torus knots. This identification is universal: it provides the unique evaluation compatible with the Frobenius--Hopf structure.*

*Specifically, $\mathrm{Geom}(K)$ is the unique functional on knot complements satisfying:*

1. *Additivity: $\mathrm{Geom}(K_1 \# K_2) = \mathrm{Geom}(K_1) + \mathrm{Geom}(K_2)$.*
2. *Functoriality: $\mathrm{Geom}(K) = \tau(\mathrm{tr}_M(\rho(\mathcal{B}_K)))$ for some fibre functor $\tau$.*
3. *Normalization: $\mathrm{Geom}(\bigcirc) = 0$ (vacuum) and $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$ (fixes $q_0$).*

**Proof sketch.**
The supporting argument has three steps; it is a sketch, not a complete proof.

**Step 1: Existence (Neumann--Zagier, τ-image side).**
On the τ-image side, the Neumann--Zagier theorem establishes that for a hyperbolic knot $K$, $\mathrm{Vol}(K)$ and $\mathrm{CS}(K)$ are related by the Bloch--Wigner dilogarithm. This is a function of the $\mathrm{SL}(2,\mathbb{C})$ representation variety. In the categorical framework, the Frobenius--Hopf algebra $A$ at parameter $q$ has a representation variety isomorphic to $\mathrm{Spec}$ of the coordinate ring $\mathcal{O}_q(\mathrm{SL}_2)$. The fibre functor $\tau$ evaluates the volume form $\omega$ on this variety. By Neumann--Zagier, the real part of this evaluation is $\mathrm{Vol}(K)$.

**Step 2: Uniqueness (Yekutieli rigidity).**
The rigid dualizing complex $\omega_A^\bullet$ provides a non-degenerate Frobenius pairing $\langle -, - \rangle_{\mathrm{Frob}}$. Yekutieli's rigidity theorem shows that this pairing is unique up to a scalar. The scalar is fixed by the normalizations $\mathrm{Geom}(\bigcirc) = 0$ and $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$. Therefore any functional satisfying properties 1--3 must equal $\mathrm{Geom}$.

**Step 3: The CS/Vol duality.**
For torus knots, $\mathrm{Vol} = 0$ and the representation variety consists of a single abelian flat connection. The evaluation of $\omega_A^\bullet$ on this connection yields the Chern--Simons functional. The duality $\mathrm{Vol}/\hbar_q^2 \leftrightarrow \mathrm{CS} \cdot \hbar_q^2$ follows from the self-duality of the rigid dualizing complex. Additivity follows from the fact that connected sum corresponds to tensor product in the Frobenius--Hopf category, and the volume form is a trace.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
