**Remark (QOU as the categorical resolution of canonical
quantum-gravity programmes).**
The contact-geometric machinery of the QOU framework
— [categorical Reeb derivation](#thm:categorical-reeb-exists),
[contact affine chart](#def:contact-affine-chart),
[categorical Dirac operator](#def:categorical-dirac-operator)
$\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \, \iota_\xi \nabla$,
and [categorical instanton](#def:categorical-instanton) condition
$\star_q F_\nabla = F_\nabla$ — is in close structural alignment
with the canonical quantum-gravity programmes (ADM, Ashtekar,
Smolin–Rovelli loop quantum gravity). The substantive differences
are not which structures appear but where they live: QOU treats them
as native categorical data, while canonical LQG bolts them onto a
continuous background and recovers algebraic data as a
regularisation patch.

## Dictionary

| Canonical programme | QOU realisation |
|---|---|
| **ADM 3+1 foliation** with lapse $N$ and shift $N^i$ \cite{ashtekar1986} | [contact affine chart](#def:contact-affine-chart) $H = \ker \varTheta_A$ as the spatial slice; [Reeb flow](#thm:categorical-reeb-exists) $\phi_t = \exp(t\xi)$ as the canonical lapse-and-shift |
| **Wheeler–DeWitt** $\hat H \Psi = 0$ | Variational minimum $\delta \mathfrak{S}_q / \delta \nabla = 0 \Rightarrow \star_q F_\nabla = F_\nabla$ ([categorical instanton](#def:categorical-instanton)) on adelic states |
| **Ashtekar connection** $A = \Gamma + \gamma K$ | [Categorical Dirac](#def:categorical-dirac-operator) $\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \iota_\xi \nabla$; the role of $\gamma K$ is played by $\hbar_q \iota_\xi \nabla$ |
| **Barbero–Immirzi parameter** $\gamma$ (fitted to $\approx 0.274$ to match $S_{BH} = A/4$ \cite{rovelli1995}) | Substrate parameter $q_0 \approx 1.11$, **derived** from the substrate Reeb flow; not a free fit |
| **Horizon (Bekenstein–Hawking) entropy** $S_{BH} = A/4\ell_p^2$ \cite{rovelli1995} | The archimedean ($\mathrm{std}$) statistical limit of the $q$-dimension (Markov-trace) partition function — the log-count of trace-closed ($\sum_p m_p = 0$, i.e. landing in $\mathcal{O}(\mathbb{P}(V)) = A^{\mathrm{co}T}$, [projective line object](#def:projective-line-object)) boundary states; horizon area = the non-abelian-Stokes surface measure |
| **Horizon Hilbert subspaces** (per-puncture $U(1)$ labels — *scalar* abelian reps) | **Wedderburn blocks** $M_{d_\lambda}(\mathbb{Q}(q))$, $\lambda \vdash n$ ([Wedderburn decomposition](#prop:three-parameters-wedderburn)); QOU carries *more* — each block is a $d_\lambda \times d_\lambda$ matrix algebra (full non-abelian intertwiner data), of which the LQG $U(1)$/scalar treatment retains only the $T_q$-weight (Cartan) projection. The $U(1)$-vs-$\mathrm{SU}(2)$ count distinction is precisely scalar-projection vs full-block |
| **Densitised triad** $E^i_a$ | Bring-curve coordinates under the $S_5$ action ([categorical Reeb on Bring](#ex:categorical-reeb-brings)); area discretisation is innate to the algebraic slices |
| **Spin networks** of arbitrary $\mathrm{SU}(2)$ representations | Knot operators as Reeb-$U(1)$ Wilson loops ([chart-swap–Reeb identification](#prop:reeb-u1-chart-swap)); torus knots $T_{m,n}$ are $(m,n)$-cables of Reeb fibres, with framings = integer ambiguity in the $U(1)$ lift |
| **Spin foams** as 2-complex path integrals \cite{rovelli2004} | Frobenius-pairing cobordism amplitudes via $\mathrm{tr}_M(\mathcal{B}_K)$ — categorical state sum, not a regularised foam triangulation |
| **Kodama state** $\Psi_K[A] = \exp\!\bigl( i \mathrm{CS}[A] \bigr)$ | $S_0$ saddle of the Faddeev WKB of $\Phi_q$ in [`conj:phi-q-wkb-greens-function`](#conj:phi-q-wkb-greens-function), evaluated at the flat-$\mathrm{SU}(2)$ critical point of a force-carrier torus knot |
| **Reality conditions** of complex Ashtekar | [Adelic product](#def:adelic-substrate) selects the unique real archimedean realisation; the original $\gamma = \pm i$ self-dual Ashtekar formulation is recovered without the reality-condition obstruction |
| **Relational QM** (Rovelli) \cite{rovelli2004} | Adelic product formula $\prod_v \lVert \psi \rVert_v = 1$ — states are well-defined only relative to the global algebraic-archimedean balance |
| **Area operator / spectrum** $\hat A = 8\pi\gamma\ell_p^2 \sum_i \sqrt{j_i(j_i+1)}$ | $\mathrm{std}$ of the $\mathrm{SU}_q(2)$ Casimir on each boundary rep (per-puncture area $=$ the $q\to1$ Casimir eigenvalue) |
| **Volume operator** | hyperbolic $\mathrm{Vol}(K)$ / vol-density — the *bulk period* (Seiberg–Witten residue) face of the non-abelian Stokes ([SW period residue sum](#prop:sw-period-residue-sum)) |
| **Holonomy–flux algebra** ($h_e$, $E_S$) | non-abelian-Stokes (Yekutieli multiplicative-integral) holonomy + Frobenius/Markov flux ([Yekutieli–Stokes](#rem:yekutieli-stokes)) — the basic categorical variables |
| **Diffeomorphism constraint** | built in: $\mathrm{tr}_M(\mathcal{B}_K)$ is an ambient-isotopy (knot) invariant by construction — no separate constraint to impose |
| **Hamiltonian constraint** (Thiemann's *rigorous* operator) | the concrete [categorical Dirac](#def:categorical-dirac-operator) / Reeb generator $\mathfrak{D}_\nabla$ — the **sharp** operator realising the *formal* Wheeler–DeWitt row above; QOU sidesteps the constraint-algebra-closure / problem-of-time issue (the Reeb flow *is* time, §1) |
| **Coherent / semiclassical states** | the archimedean ($\mathrm{std}$, $q\to1$) limit of the categorical state |
| **LQC big bounce** & **Penrose CCC aeons** (singularity-free cosmology) | **One mechanism in QOU**: cosmic time $=$ the $q$-flow, with both as *endpoints of a single surreal trajectory* — Big Bang $= q\to1^+$ ($c_q\to\infty$; the $1+\varepsilon^\omega$ end), heat death $= q\to\infty=\omega$ ($\hbar_q\to1$). LQC's bounce and CCC's conformal rescaling are the two *ends*, not two mechanisms (*highly speculative*: the named-surreal evaluation is clean, the cosmological reading is bracketed) |
| **Quantum-geometry discreteness** (discrete area/volume spectra) | algebraic discreteness — finite Wedderburn blocks $\bigoplus_\lambda M_{d_\lambda}$ + finite GS-filtration slices ([GB spectral sequence](#prop:gb-spectral-sequence)); discreteness is *innate to the algebra*, not a quantisation output |

## Three structural advantages

The dictionary tightens around three points where QOU avoids
well-known obstructions of the canonical programmes:

1. **No "problem of time".** ADM presupposes a continuous time
   coordinate to define the lapse $N$; quantising the Hamiltonian
   constraint $\hat H \Psi = 0$ then freezes the state. QOU has no
   inbuilt time: what emerges as macroscopic time is the
   [Reeb flow](#thm:categorical-reeb-exists), driven by the
   $q$-anomaly $d_q^2 \neq 0$ in the categorical action. The
   variational constraint $\delta \mathfrak{S}_q / \delta \nabla = 0$ is
   solved categorically without needing an external clock; transition
   amplitudes between algebraic states are the
   [Frobenius pairings](#def:frobenius-hopf-substrate), not
   Wheeler–DeWitt evolution operators.

2. **No Barbero–Immirzi fudge factor.** The continuous Ashtekar
   connection $A = \Gamma + \gamma K$ has $\gamma$ as a free
   parameter, conventionally tuned to make $S_{LQG} = A / 4 \ell_p^2$
   match black-hole entropy ($\gamma \approx 0.2740$ for the full
   $\mathrm{SU}(2)$ horizon count, $\gamma \approx 0.2375$ for the
   $U(1)$ reduction). The corresponding parameter in QOU is the
   substrate $q_0$, derived from the categorical Reeb flow and locked
   by the algebraic structure of Bring's surface ($\chi = -6$). The
   quantisation scale is fixed by the substrate, not back-solved from
   thermodynamics.

3. **Native self-duality, no reality conditions.** Ashtekar's
   original $\gamma = \pm i$ formulation made the Hamiltonian
   constraint polynomial via complex self-duality, but the resulting
   complex metric required intractable "reality conditions". QOU
   recovers exact self-duality $\star_q F_\nabla = F_\nabla$
   ([categorical instanton](#def:categorical-instanton)) as the
   $\delta \mathfrak{S}_q / \delta \nabla = 0$ output, and the
   [adelic product](#def:adelic-substrate) plus continuous
   $\mathbb{Z}_2 \to U(1)_{\xi}$ deformation (chart-swap–Reeb
   identification, [`prop:reeb-u1-chart-swap`](#prop:reeb-u1-chart-swap))
   produces the real Lorentzian archimedean projection without
   imposing reality conditions by hand.

## What QOU does not claim

The dictionary does not claim that QOU *derives* LQG from first
principles; canonical loop quantum gravity is a self-contained
research programme with its own quantisation scheme. The claim is
narrower: every structural ingredient that the LQG / ADM / Ashtekar
programmes have to introduce as a separate assumption (a foliation, a
free $\gamma$, a Kodama wave function, reality conditions, a foam
triangulation) appears in QOU as a *derived* output of the
categorical substrate plus Bring-curve constraint. The relevant
QOU-side outputs (the Wightman portion of the mass-gap statement, in
particular) are still conditional on the
[OS reflection-positivity conjecture](#conj:os-reflection-positivity-from-reeb)
and the
[surreal mass-gap bound](#rem:yang-mills-surreal-bound) — granting
both, the comparison sharpens to a structural equivalence at the
level of the Hamiltonian-constraint reduction.
