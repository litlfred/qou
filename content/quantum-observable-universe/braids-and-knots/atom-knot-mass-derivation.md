**Statement (categorical, pre-Archimedean form).**  Let
$\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum
observable universe at substrate parameter $q_0$
([def:quantum-observable-universe](#def:quantum-observable-universe)),
let $\mathfrak{H}$ be a confined particle/atom of confinement level
$\ell$ and strand count $n_0$ with canonical Hecke element
$T_w \in H_{n_0}(q_0)$ in Gröbner–Shirshov normal form
([def:confined-particle](#def:confined-particle)).  The
**categorical mass invariant** of $\mathfrak{H}$ is the finite-sum
element of $\mathbb{Q}(q)$

$$
M(\mathfrak{H}) \;:=\; \rho \cdot m(\mathfrak{H}) \;=\; \rho \cdot \bigl[\,|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})\,\bigr],
$$

where $m(\mathfrak{H})$ is the **categorical mass invariant** in
the multi-term form of the
[unified knot mass formula](#thm:knot-mass-formula-unified):
$|\mathrm{tr}_M(T_w)|$ is the descended Markov trace
$\sum_\lambda y_\lambda(q)\,\chi_\lambda(T_w)$
(Wenzl-bridge coefficients $y_\lambda$,
$q$-Murnaghan–Nakayama character $\chi_\lambda$),
$\mathrm{tower}(T_w) = \sum_i \Phi_q(|\hat{V}_i|) + z^2 \sum_{i<j} \Phi_q(|\hat{V}_i \hat{V}_j|)$
is the brane tower built from per-generator additive-Wedderburn
volumes $\hat{V}_i$
([mass endomorphism tower](#prop:mass-endomorphism-tower)),
and $\mathrm{tr}_M(C_{\dim_q}) = \sum_{\lambda \vdash n_0} 1/\dim_q(\lambda)$
is the Frobenius co-Casimir trace
([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)).
The scalar $\rho \in \mathbb{Z}_{>0}$ is the multiplicity of
$T_w$'s SDP solution in the Wedderburn decomposition (see
algorithm step below).  This expression is **finite, exact, and
entirely pre-Archimedean** — every quantity on the right-hand side
lives in $\mathbb{Q}(q)$.

**Important historical note.**  An earlier wording wrote
$M(\mathfrak{H}) = \rho \cdot \mathrm{tr}_M(T_w)$ (single term).
That single-term form is **shorthand** for the multi-term sum
above; on its own it is structurally inadequate (verified
empirically in
[`probe-sdp-canonical-paper-formula.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe-sdp-canonical-paper-formula.witness.json):
single-term fails by 87--100% on $D$, $T$, ${}^3\mathrm{He}$
under both Plancherel and Wenzl-Schur conventions; multi-term
without the brane tower reduces error to 36--63%; the brane tower
remains technically open at $|\hat{V}|\approx 1$).

**Mass identity.**  After applying the Archimedean realization functor
([archimedean realization functor](#def:archimedean-realization-functor)),
the binding energy of $\mathfrak{H}$ is

$$
\boxed{ \quad B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0} \;=\; m_e \cdot \rho \cdot \mathrm{tr}_M(T_w) \big|_{q = q_0} \quad }
$$

— a single finite-categorical pipeline, no analytic asymptotic
content.  The volume conjecture is *not* used in the derivation; it
appears only as a post-functor naming convention (see "Post-Archimedean
interpretation" below).

## Architecture (single categorical pipeline; Yekutieli at finite slices)

The derivation is a **single categorical pipeline** that lives entirely
pre-Archimedean.  Yekutieli's non-abelian Stokes theorem (multiplicative
integration on surfaces) at finite slice depth gives the following
correspondence between 2-categorical / surface-integration data and
the Iwahori–Hecke structure on $H_{n_0}(q_0)$:

| 2-categorical | finite-slice avatar in $H_{n_0}(q)$ |
|---|---|
| 1-cells (paths) | braid generators $\sigma_i$ |
| 2-cells (squares) | Hecke quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ |
| multiplicative line integral | finite product $\prod_k \rho(\sigma_{i_k})$ |
| multiplicative trace on closed surface | Markov trace $\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda(q) \chi_\lambda(T_w)$ |
| slicing depth | GB filtration grade $\ell(w)$ (Coxeter length) |
| slice traversal order | jet order |
| non-abelian Stokes identity at adjacent slices | braid relations + Hecke quadratic |
| associated graded $\mathrm{gr}_\bullet H_{n_0}(q)$ | $E_1$-page of the GB spectral sequence |
| differentials $d_r$ vanishing past $E_\infty$ | **collapse** at $E_2$ for semisimple $H_n(q)$ at generic $q$ |
| $E_\infty$-page identification | $\bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q))$ (Wedderburn) |

**Collapsing spectral sequence.**  The GB filtration on $H_{n_0}(q)$
gives rise to a multiplicative spectral sequence
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence),
[prop:spectral-sequence-h3-explicit](#prop:spectral-sequence-h3-explicit))
whose $E_1$-page is the associated graded $\bigoplus_k \mathrm{gr}_k H_{n_0}(q)$.
By [prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse)
the spectral sequence **collapses at $E_2$ for semisimple $H_n(q)$ at
generic $q$** (the $d_2$-differential captures the Hecke quadratic
relation; higher differentials vanish because $H_n(q)$ has no further
relations beyond braid + Hecke).  The $E_\infty$-page identifications
([prop:e-infinity-page-identifications](#prop:e-infinity-page-identifications))
recover the Wedderburn decomposition $\bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q))$.

Collapse is **the reason finite-slice computation suffices**: at finite
slice depth (= filtration grade $\leq$ some $k$), the surviving
$E_\infty$-classes already account for all of $\mathrm{tr}_M(T_w)$
because $d_r = 0$ for $r \geq 3$.  No higher slices contribute.  The
GB-filtration tracker's certificate
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json))
records exactly the data the $E_2 \Rightarrow E_\infty$ collapse needs:
filtration-graded coefficients per term, in jet order.

The *finite slice* is essential: at every finite resolution Yekutieli's
multiplicative integral is a finite product / finite sum in $\mathbb{Q}(q)$,
exact, with no asymptotic limit.  This is exactly the categorical
content captured by the GB-filtration + jet-order certificate
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json)).

### Pipeline

```tex
\begin{tikzcd}[row sep=large, column sep=large]
\textbf{Categorical action of } \mathbf{C} \text{ on } \mathcal{S} \arrow[d, "\text{Yekutieli, finite slice}"]
\\
\textbf{Joint-tower confinement SDP at } q_0 \arrow[d, "\text{GB filtration} + \text{jet order}"]
\\
T_w \in H_{n_0}(q_0) \text{ (canonical, GB-NF)} \arrow[d, "\text{Wedderburn}"]
\\
H_{n_0}(q) \cong \bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q)) \arrow[d, "{y_\lambda \text{ (Wenzl)}, \chi_\lambda \text{ (q-MN)}}"]
\\
\mathrm{tr}_M(T_w) \;=\; \sum_\lambda y_\lambda(q) \chi_\lambda(T_w) \;\in\; \mathbb{Q}(q) \arrow[d, "\rho \cdot (-)"]
\\
M(\mathfrak{H}) \;=\; \rho \cdot \mathrm{tr}_M(T_w) \;\in\; \mathbb{Q}(q)
\\
{} \arrow[d, "\text{\textbf{Archimedean realization functor}}"]
\\
B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0} \;\in\; \mathbb{R} \text{ (MeV)}
\end{tikzcd}
```

Everything above the Archimedean functor lives in $\mathbb{Q}(q)$;
$\mathbb{R}$ enters exactly once, at the substitution $q := q_0$
together with the multiplication by $m_e$.  No analytic limit, no
volume conjecture, no Reeb-density construction is invoked.

### Post-Archimedean interpretation (borrowed, optional)

If $K = \widehat{T_w}$ is hyperbolic, the post-Archimedean number
$\mathrm{tr}_M(T_w)|_{q = q_0}$ admits a conventional 3-manifold-theory
naming via the **volume conjecture** (Kashaev 1997, Murakami–Murakami
2001): the asymptotic of $|J_K(\zeta_N)|^{1/N}$ at roots of unity
$\zeta_N = e^{2\pi i / N}$ as $N \to \infty$ equals
$\exp(\mathrm{Vol}_{\mathrm{hyp}}(K)/2\pi)$.  This is a **borrowed
theorem about post-Archimedean analytic continuation**, allowing
$B(\mathfrak{H})/m_e\rho$ to be *named* as a hyperbolic volume in
conventional language.  The QOU mass identity does **not** depend on
the conjecture — it depends only on the finite-categorical
$\mathrm{tr}_M(T_w)$.

In particular the geometric construction (Reeb-vortex density →
Mostow → Gromov), available on the post-Archimedean side as
*another* way to write the same number, is **not part of the QOU
derivation** and need not be derived internally.

## Algorithm

```tex
\begin{algorithm}
\caption{\textsc{AtomKnotMass}: end-to-end categorical mass derivation
from $\mathfrak{H}$ to $B(\mathfrak{H})$.  Single categorical pipeline,
finite-slice (Yekutieli), no asymptotic content.}
\textbf{Input.}  Confined particle $\mathfrak{H}$ with confinement
level $\ell$, strand count $n_0$, registry entry in
\texttt{def:confined-particle}.  Substrate parameter $q_0$.
\\
\textbf{Output.}  $B(\mathfrak{H}) \in \mathbb{R}_{\geq 0}$ in MeV,
with methodology tag and high-precision certificate.
\\
\hrulefill
\\
\textbf{Pre-Archimedean (in $\mathbb{Q}(q)$, exact, finite):}
\begin{enumerate}
  \item Run the joint mass-tower confinement SDP on all
        $\ell' \leq \ell$ atoms simultaneously.  Output: a
        \emph{structured certificate} per atom recording
        \begin{enumerate}
          \item the canonical Hecke element $T_w \in H_{n_0}(q_0)$ in GB-NF,
          \item the Gröbner--Shirshov filtration grade per term
                (= Yekutieli slicing depth at finite slice),
          \item the jet-order of reductions
                (= temporal slice-traversal order).
        \end{enumerate}
  \item Compute the Markov trace symbolically in $q$ via the
        Wedderburn decomposition + Wenzl bridge:
        $\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda(q) \chi_\lambda(T_w)$
        (\texttt{prop:alpha-k-derivation-procedure}, $y_\lambda$ from
        Wenzl-bridge witness, $\chi_\lambda$ from $q$-Murnaghan--Nakayama).
        Yekutieli at finite slice ⇒ this is exactly the multiplicative
        trace on the closed surface obtained by Markov closure of
        $T_w$; the Hecke quadratic relation is the curvature 2-form
        at adjacent slices.
  \item Read $\rho \in \mathbb{Z}_{>0}$ from the structural prefactor
        rule on $(Z, N)$ (= the multiplicity of $T_w$'s SDP solution
        in the Wedderburn decomposition).  Currently OPEN in
        general; confirmed values from the joint-tower SDP witness
        are $\rho_D = 1$, $\rho_T = 2$, $\rho_{{}^3\mathrm{He}} = 2$.
        The earlier statement "$\rho = 1$ for $\ell \leq 1$" was
        too narrow — it holds for $D$ but is contradicted by the
        SDP witness for $T$ and ${}^3\mathrm{He}$ (each carrying
        $\rho = 2$ from the multiplicity of the trefoil-like
        constituent in the $H_5$ / $H_3$ Wedderburn decomposition).
  \item Form the categorical mass invariant
        $M(\mathfrak{H}) := \rho \cdot \mathrm{tr}_M(T_w) \in \mathbb{Q}(q)$.
\end{enumerate}
\textbf{Archimedean realization (functor $\mathbf{C} \to \text{Top}$, $\mathbb{Q}(q) \to \mathbb{R}$):}
\begin{enumerate}
  \setcounter{enumi}{4}
  \item Apply the Archimedean realization functor at $q = q_0$ and
        multiply by $m_e$:
        $B(\mathfrak{H}) := m_e \cdot M(\mathfrak{H}) \big|_{q = q_0}
        = m_e \cdot \rho \cdot \mathrm{tr}_M(T_w)\big|_{q = q_0}$,
        evaluated to $\geq 50$ decimal digits via MPFR.
  \item Compare to AME 2020 binding: residual
        $\Delta = B - B_{\mathrm{AME}}$ in MeV and ppb.
  \item Tag the result with one of:
        \texttt{principled-derivation} (categorical pipeline complete
        end-to-end), \texttt{principled-gb-nf} (trivial-NF entries
        only), \texttt{manual-historical-volume-match} (knot ID by
        earlier work, GB-NF derivation pending),
        \texttt{magic-A-formula} (algebraic shell-closure rule),
        \texttt{recursive-on-${}^{4}$He} (cluster recursion).
        Quarantine separately if \texttt{deprecated-volume-match}.
\end{enumerate}
\textbf{Optional post-Archimedean naming (borrowed, not in derivation):}
\begin{enumerate}
  \setcounter{enumi}{7}
  \item For hyperbolic $K = \widehat{T_w}$, the volume conjecture
        identifies $M(\mathfrak{H})/(m_e \rho)\big|_{q_0}$ with
        $\mathrm{Vol}_{\mathrm{hyp}}(K)$ in conventional 3-manifold
        terminology.  Used only as a name for the post-Archimedean
        number; \emph{not} part of the derivation.
\end{enumerate}
\end{algorithm}
```

## Pipeline status

The categorical pipeline is now implemented in two parallel
implementations:

- **Python prototypes** ([`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb_filtration_jet_tracker.py),
  [`joint_tower_sdp_solver.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/joint_tower_sdp_solver.py),
  [`joint_tower_sdp_solver_v2.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/joint_tower_sdp_solver_v2.py)) — design-spec
  reference, exact in $q$ via SymPy + cvxpy SDP feasibility for $H_3$.
- **Rust production scaling** ([`tools/hecke-engine/src/{gb_nf_reducer,joint_tower_sdp_certificate,wedderburn_psd,cross_level_embedding,sdp_verifier}.rs`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/src/),
  binary [`joint-tower-sdp`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/src/bin/joint_tower_sdp.rs)) — bit-for-bit
  match with Python on small cases; **3,400× speedup** (47.5 s → 14 ms
  for the 7-atom registry); scales to $H_5+$ where Python defers.
  See [RUST_INTEGRATION.md](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/RUST_INTEGRATION.md)
  for the implementation plan.

| Step | Implementation | Status |
|---|---|---|
| 1a (canonical $T_w$ — joint-tower SDP for *unknown* $T_w$) | R5-full pending — research-grade | ✗ |
| 1b (GB-filtration certificate) | Python `gb_filtration_jet_tracker.py` (PoC) + Rust `gb_nf_reducer.rs` (R2; 6 unit tests; bit-for-bit match) | ✓ |
| 1c (jet-order log) | same modules | ✓ |
| 1d (Wedderburn-block PSD evaluator) | Python cvxpy at $H_3$ + Rust `wedderburn_psd.rs` (R3; 2 unit tests; scales to $H_5+$) | ✓ |
| 1e (cross-level embedding LR) | Rust `cross_level_embedding.rs` (R4; multi-LR; 2 unit tests including 77-partition $H_{12}$ identity) | ✓ |
| 1f (PSD-cone $\alpha^*$ verifier) | Rust `sdp_verifier.rs` (R5-minimal; bisection equivalent to SDP value function; 2 unit tests) | ✓ |
| 2 (Markov trace symbolic) | [`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/y_lambda_wenzl_bridge_extended.py) + [`q_mn_recursive_memoized.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/q_mn_recursive_memoized.py) | ✓ for $n \leq 12$ |
| 3 ($\rho(Z, N)$ rule from Wedderburn multiplicity) | downstream of 1a — read off SDP solution multiplicity | ✗ |
| 4 ($M(\mathfrak{H}) = \rho \cdot \mathrm{tr}_M(T_w) \in \mathbb{Q}(q)$) | algebraically trivial once 2 + 3 are in | partial |
| 5 (Archimedean realization at $q_0$ + $m_e$) | MPFR via SymPy/mpmath | ✓ |
| 6 (AME comparison) | mass-table-ppb witness + [`recursive_atom_knot_atlas_render.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/recursive_atom_knot_atlas_render.py) | ✓ |
| 7 (methodology tag) | [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/methodology-deprecation.witness.json) | ✓ |
| 8 (post-Archimedean naming via volume conjecture) | borrowed; not in QOU derivation | ✓ as theorem |

### PSD-cone $\alpha^*$ ranking (Rust R5-minimal, $q_0 = 1.1097$)

For each historical entry the verifier emits
$\alpha^*(\mathfrak{H}) := \max\{\alpha \in [0,1] :
\alpha \cdot \rho_\lambda(T_w) + (1-\alpha) \cdot I \succeq 0
\text{ for all } \lambda\}$.  $\alpha^* = 1$ ⇒ all blocks PSD;
$\alpha^* < 1$ quantifies the gap.

| atom | knot ID | $\alpha^*$ | gap $1-\alpha^*$ | diagnostic |
|---|---|---|---|---|
| proton | $\mathcal{B}_3$ Borromean | **1.000** | 0 | all 3 blocks PSD ✓ |
| neutron | $\mathcal{B}_3$ Borromean | **1.000** | 0 | all 3 blocks PSD ✓ |
| $^3\mathrm{He}$ | $L_{6a4}$ | **1.000** | 0 | all 3 blocks PSD ✓ |
| electron | $\sigma_1^3 = T_{2,3}$ | 0.577 | 0.423 | sign block $\rho_{(1,1)} = -q^{-3}$ negative (algebraic, expected for fermionic odd permutations) |
| $^2\mathrm{H}$ | $6_2$ | 0.546 | 0.454 | standard $(2,1)$ block NOT PSD |
| $^3\mathrm{H}$ | $8_{11}$ | **0.424** | 0.576 | 5 of 7 blocks NOT PSD — *largest gap* in registry |

Steps 5–8 currently substitute $\mathrm{Vol}_{\mathrm{hyp}}(K)$ from
SnapPy for $\mathrm{tr}_M(T_w)|_{q=q_0}$ on entries flagged
\texttt{manual-historical-volume-match} (²H, ³H, ³He) — i.e.\ the
post-Archimedean naming convention is used in place of the
pre-Archimedean Markov-trace evaluation.  This is acceptable for
existing established knot identifications because the volume
conjecture commits both quantities to the same number, but the
*principled* path (Step 1a → Step 5) does not depend on this
substitution.

The quarantined provisional ⁶Li, ⁷Li entries
([prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas)
§"⚠ Provisional / deprecated methodology") run *backwards* from Step
6 to a candidate knot, bypassing Step 1a entirely.  Such shortcuts
are forbidden by this proposition.

## Where the gaps actually are

After the pre-Archimedean / post-Archimedean simplification (Yekutieli
at finite slices replaces the geometric leg with finite-categorical
Markov-trace computation) and the production-scale Rust port
(R1–R4 + R5-minimal landed), the remaining open structural item is:

1. **Joint mass-tower confinement SDP — solver mode (R5-full).**
   The current Rust binary verifies that *given* candidate $T_w$
   inputs (electron $\sigma_1^3$, proton/neutron Borromean, ²H/³H/³He
   historical IDs) the certificate format is well-formed and quantifies
   the PSD-cone gap $\alpha^*$.  The remaining work is to invert this:
   for ⁶Li ($H_{18}$), ⁷Li ($H_{21}$), and α-cluster atoms ($H_{24}$
   to $H_{120}$) where canonical $T_w$ is *unknown*, formulate and
   solve the SDP

   $$
   \min_{c_{w}(q_0) \in \mathbb{R}} \, \|\,c\,\|_1 \quad\text{s.t.}\quad
   \rho_\lambda(T_w) \succeq 0 \,\forall \lambda,\ \pi_{\mathfrak{H}\to\mathfrak{H}'}(T_w(\mathfrak{H})) = T_w(\mathfrak{H}')
   $$

   via Clarabel.rs + system BLAS.  Slots cleanly into the existing
   `JointTowerSdpCertificate` schema.  Once R5-full lands, the
   deprecated `li-atom-knot-search` is fully retirable.

A second item — the structural prefactor rule $\rho(Z, N)$ — is a
downstream consequence: once the SDP-solver returns canonical $T_w$
per atom, $\rho$ is read off as the multiplicity of $T_w$'s solution
in the Wedderburn decomposition.  No separate derivation is needed.

The geometric "leg" (Reeb density → Mostow → Gromov → Vol) and the
volume conjecture are *not* part of the QOU derivation.  They appear
post-Archimedean as borrowed theorems that name the same number in
conventional 3-manifold-theory language.

## Refs

- Volume conjecture: Kashaev (1995), H.\ Murakami--J.\ Murakami (2001).
- Mostow rigidity: Mostow (1968), Prasad (1973).
- Gromov norm: Gromov (1982), Thurston (1979).
- Wenzl bridge $y_\lambda = s_{\lambda, r}(Q)/Z$: Wenzl (1988), Jones (1989).
- Iwahori--Hecke algebra + GB-NF: Kassel--Turaev (2008).
- Confinement SDP: [prop:confinement-sdp](#prop:confinement-sdp).
- AME 2020: Wang et al.\ (2021).
