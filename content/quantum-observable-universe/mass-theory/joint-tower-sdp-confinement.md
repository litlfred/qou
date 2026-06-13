**Statement (design specification).** Let $\mathcal{U}$ be a quantum
observable universe at substrate parameter $q_0$. The **joint
mass-tower confinement SDP** at $q_0$ is the semidefinite program

$$
\boxed{\quad
\begin{aligned}
& \text{find} && \big( c_{\mathfrak{H}, w}(q_0) \big)_{\mathfrak{H} \in \mathcal{R}, \, w \in S_{n_0(\mathfrak{H})}} \in \mathbb{Q}, \\
& \text{such that} && \forall \, \mathfrak{H} \in \mathcal{R}: \\
& && \quad T_w(\mathfrak{H}) := \sum_{w \in S_{n_0(\mathfrak{H})}} c_{\mathfrak{H}, w}(q_0) \cdot T_w \;\in\; H_{n_0(\mathfrak{H})}(q_0) \\
& && \quad \rho_\lambda(T_w(\mathfrak{H})) \succeq 0 \text{ for all Wedderburn blocks } \lambda \vdash n_0(\mathfrak{H}) \\
& && \quad \text{(GB-filtration grading: } c_{\mathfrak{H}, w} \neq 0 \Rightarrow \ell(w) \in \mathrm{Filt}(\mathfrak{H})\text{)} \\
& && \quad \text{(jet-order ordering: SDP variable indexing respects jet order)} \\
& \text{cross-level constraints:} && \forall \, \mathfrak{H} \to \mathfrak{H}' \text{ in tower:} \\
& && \quad \pi_{\mathfrak{H} \to \mathfrak{H}'} \big( T_w(\mathfrak{H}) \big) \;=\; T_w(\mathfrak{H}')
\end{aligned}
\quad}
$$

where $\mathcal{R}$ is the registry of confined particles
([def:confined-particle](#def:confined-particle)), $\rho_\lambda$ is
the Wedderburn block $\lambda$-projection, and
$\pi_{\mathfrak{H} \to \mathfrak{H}'}$ is the canonical embedding
$H_{n_0(\mathfrak{H}')} \hookrightarrow H_{n_0(\mathfrak{H})}$
induced by the recursive structure of $\mathcal{R}$ (e.g.\ ${}^2$H = ${}^4$He
embeds via the strand-augmentation $H_{12} \hookrightarrow H_{18}$).

A solution $(c_{\mathfrak{H}, w}(q_0))$ is a **structured certificate**
of the canonical Hecke elements $\{T_w(\mathfrak{H})\}_{\mathfrak{H} \in \mathcal{R}}$
together with the **GB-filtration certificate** and **jet-order log**
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json))
on each. Existence is asserted by [prop:confinement-sdp](#prop:confinement-sdp);
this proposition refines that with the joint-tower / GB-filtration /
jet-order structure required by the categorical mass derivation
([prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation)).

## SDP variables

For each particle $\mathfrak{H} \in \mathcal{R}$ with strand count
$n_0 = n_0(\mathfrak{H})$, the variables are
$c_{\mathfrak{H}, w}(q_0) \in \mathbb{Q}$ for every $w \in S_{n_0}$.
These index the basis $\{T_w\}_{w \in S_{n_0}}$ of $H_{n_0}(q_0)$ in
GB-NF. Total variable count is $\sum_{\mathfrak{H}} |S_{n_0(\mathfrak{H})}|
= \sum_{\mathfrak{H}} n_0(\mathfrak{H})!$, which for $\mathcal{R}$
covering up to ${}^{40}$Ca ($n_0 = 120$) is astronomically large. In practice
the **filtration cuts the problem down**: only $w$ with $\ell(w) \leq L$
for some cutoff $L = O(n_0)$ contribute non-by definition (most $T_w$ are
zero for atomic braids of finite GB-NF length), so the effective
variable count is $\sum_{\mathfrak{H}} \binom{n_0}{L}$ which is
polynomial in $n_0$ for fixed $L$.

## SDP constraints

### (1) Per-particle Wedderburn positivity

For each $\mathfrak{H}$ and each Wedderburn block $\lambda \vdash n_0$,
the block image
$\rho_\lambda(T_w(\mathfrak{H})) \in M_{d_\lambda}(\mathbb{Q})$
must be positive semidefinite. This is the standard confinement SDP
constraint ([prop:confinement-sdp](#prop:confinement-sdp)), expressed
per Wedderburn block via the explicit Hoefsmit seminormal form
([prop:hoefsmit-seminormal-form](#prop:hoefsmit-seminormal-form)).

### (2) GB-filtration grading

The certificate variables $c_{\mathfrak{H}, w}(q_0)$ must support a
filtration: there is a graded structure $\mathrm{Filt}(\mathfrak{H}) =
\{\ell_0(\mathfrak{H}), \ell_1(\mathfrak{H}), \ldots\} \subseteq \mathbb{Z}_{\geq 0}$
such that $c_{\mathfrak{H}, w} = 0$ for $\ell(w) \notin \mathrm{Filt}(\mathfrak{H})$.
This is encoded as a **structural sparsity pattern** on the SDP
variables: the support of the certificate per Wedderburn block lives
in a fixed Coxeter-length-graded subspace. The GB spectral sequence
collapse at $E_2$
([prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse))
implies the filtration is *finite* (at most polynomial-degree cutoff
in $n_0$); the SDP need not enumerate all of $S_{n_0}$.

### (3) Jet-order ordering (variable indexing)

The SDP variables are indexed by *jet order* — i.e.\ the temporal
sequence of GB reductions. Concretely: at each Wedderburn block
$\lambda$, the variables $\{c_{\mathfrak{H}, w}\}_{\ell(w) \leq L}$
are ordered by an admissible jet sequence as in
[gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json).
Two effects:

- The SDP is decomposed into a **chain of sub-problems** along the
 jet order, each refining the previous. Solutions extend accordingly
 one jet step at a time.
- The jet-order log emitted with the certificate makes the SDP
 output reproducible: re-running with the same jet ordering yields
 the same coefficients $c_{\mathfrak{H}, w}(q_0)$.

### (4) Cross-level consistency

For each tower-edge $\mathfrak{H} \to \mathfrak{H}'$ where
$\mathfrak{H}'$ is a constituent of $\mathfrak{H}$ (e.g.\ ${}^{4}$He is a
constituent of ${}^{8}$Be in the α-cluster decomposition), the canonical
embedding
$\pi_{\mathfrak{H} \to \mathfrak{H}'} : H_{n_0(\mathfrak{H}')}(q_0) \hookrightarrow H_{n_0(\mathfrak{H})}(q_0)$
must send $T_w(\mathfrak{H}')$ to $T_w(\mathfrak{H})$ inside the
relevant cosets. This is the constraint that **per-atom SDPs alone
cannot enforce**: only the joint formulation guarantees the
filtration grading and jet ordering are consistent across confinement
levels.

The set of tower edges is determined by the recursive structure of
$\mathcal{R}$ ([def:confined-particle](#def:confined-particle)). At
$\ell \leq 2$ the explicit edges are:

See [Table 1](#tbl:joint-tower-sdp-confinement-table1-data).

For ${}^{6}$Li, ${}^{7}$Li the embedding is open: $\mathfrak{H} \to \{\alpha, p, n\}$
or $\mathfrak{H} \to \{\alpha, p, 2n\}$ respectively, with explicit
embeddings $H_{18} \hookleftarrow H_{12} \otimes H_3 \otimes H_3$ and
$H_{21} \hookleftarrow H_{12} \otimes H_3 \otimes H_3 \otimes H_3$.

## Existence

By [prop:confinement-sdp](#prop:confinement-sdp), the per-atom SDP is
feasible at $q_0$ for every $\mathfrak{H} \in \mathcal{R}$. The joint
SDP is feasible iff the cross-level constraints (4) are simultaneously
satisfiable, which holds because the embeddings $\pi_{\mathfrak{H} \to \mathfrak{H}'}$
preserve Wedderburn-block positivity (the canonical embedding of
$H_m(q_0) \hookrightarrow H_n(q_0)$ for $m \leq n$ sends each Wedderburn
block of $H_m$ into a sum of compatible blocks of $H_n$). Combined
with the GB filtration sparsity (2) and jet-order indexing (3), the
SDP is well-posed and admits at least one structured solution.

## Output

A solution to the joint-tower SDP is a structured certificate

$$
\Phi(q_0) \;:=\; \big\{ \big( T_w(\mathfrak{H}), \mathrm{Filt}(\mathfrak{H}), \mathrm{JetLog}(\mathfrak{H}) \big) \big\}_{\mathfrak{H} \in \mathcal{R}}
$$

— one canonical Hecke element per atom, with its filtration grading
and jet-order log. Combined with the structural prefactor
$\rho(\mathfrak{H}) \in \mathbb{Z}_{>0}$ read off from the Wedderburn
multiplicity of $T_w(\mathfrak{H})$, this gives the categorical mass
invariant
$M(\mathfrak{H}) = \rho(\mathfrak{H}) \cdot \mathrm{tr}_M(T_w(\mathfrak{H}))$
for the atom-knot mass derivation
([prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation)).
## Refs

- Confinement SDP: [prop:confinement-sdp](#prop:confinement-sdp).
- GB filtration / jet-order certificate format:
 [gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json) +
 [`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb_filtration_jet_tracker.py).
- GB spectral-sequence collapse:
 [prop:gb-spectral-sequence](#prop:gb-spectral-sequence),
 [prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse).
- Wedderburn block decomposition:
 [prop:wedderburn-trace-identity](#prop:wedderburn-trace-identity).
- Hoefsmit seminormal form for explicit block matrices:
 [prop:hoefsmit-seminormal-form](#prop:hoefsmit-seminormal-form).
- Mass identity that consumes this output:
 [prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation).
