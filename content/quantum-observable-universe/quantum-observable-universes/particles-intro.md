The transport equation $\mathcal{D}_\nabla \psi = 0$
selects on-shell solutions, but does not yet say what a particle
is. We define a particle as a $q$-harmonic form, then read off
the fermion--boson decomposition from the weight splitting,
and finally treat observation as a structural operation that
acts on these solutions.

**Categorical $q$-deformed exterior derivative** (def) extends
the substrate-deformation construction from the previous section
to all of $\Omega^\bullet(A)$, giving $d_q = q^{-1}d + (1 -
q^{-1})\pi_V \circ d$ and its dagger-adjoint $\delta_q$.
**Existence of the categorical $q$-exterior derivative** (prop)
and **uniqueness of the categorical $q$-exterior derivative**
(prop), with their proofs, fix $d_q$ once the QOU data is
chosen. **$q$-harmonic form (particle)** (def) defines a
particle as $\alpha \in \Omega^k(A)$ in the kernel of the
$q$-Laplacian $\Delta_q = d_q \delta_q + \delta_q d_q$.
**Fermion--Boson decomposition** (def) restricts the weight
decomposition to $\mathcal{H}_q^k = \ker\Delta_q$, giving the
short exact sequence $0 \to \mathcal{H}_{q,H}^k \to
\mathcal{H}_q^k \to \mathcal{H}_{q,V}^k \to 0$: a boson is
purely horizontal, a fermion has non-trivial vertical part.

**Categorical point** (def) and **Explication of the
categorical point** (rem) introduce a point of $A$ as a
morphism $p \colon \mathbf{1} \to A$, the categorical
replacement for "evaluation at a spacetime point" with no
ambient topology on $A$. **Observation** (def) defines an
observation on $U$ as a pair $(\mathfrak{O}, \epsilon)$ where
$\mathfrak{O}$ is a section of $\mathrm{Ad}(J^1 \mathcal{S})$
satisfying Frobenius compatibility and an adjoint backreaction
that shifts the substrate parameter via the Hopf coaction;
$\epsilon \in \{+1, -1\}$ selects the braiding orientation
under $\prec_c$. **The two physical roles of an observation
($J^1$ versus $\mathrm{Ad}$)** (rem) and **Observation as a
backreacting Hecke generator** (prop), with its proof, expand
the structural content.

**Two-observer parallelogram** (rem) computes the commutator
$[\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p) =
[q_1'(p), q_2'(p)] \cdot (\alpha_V)_p$ at a point and shows that
it vanishes exactly on bosons; on fermions, the non-cocommutativity
of the Hopf structure forces independent observations to disagree.
The closing block **The observer acts directly on fermions via
the colour fibre** (rem) reads this through the Hecke eigenspace
decomposition $V \otimes V = \mathrm{Sym}^2 \oplus \bigwedge^2$:
the $\mathrm{Ad}$ component preserves the bosonic eigenspace and
rotates the fermionic one, depositing $q + q^{-1}$ per crossing
in the colour fibre. The next section, **Geometric
interpretations**, takes the operators of this section and reads
them through the classical vector-calculus dictionary.

_(draft.)_
