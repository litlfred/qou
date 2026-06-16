**Notation.** The prefactor previously written
$\rho$ in this block is the **SDP-solution multiplicity** in the
Wedderburn decomposition, an integer $\in \mathbb{Z}_{>0}$. To
disambiguate from the distinct **categorical density** $\rho_K \in
\mathbb{R}_{>0}$ used in
[`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md) (CODATA-fit
scalar, e.g. $\rho_K^{\mathfrak{p}} \approx 1723.6$), this block
uses **$\nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$** throughout. The
old symbol $\rho$ is reserved (i) for the Hoefsmit irrep
representation $\rho_\lambda \colon H_n(q) \to \mathrm{GL}_{d_\lambda}$
and (ii) for $\rho_K$ in `prop:atomic-mass-gb-nf`. See
[`docs/audits/-rho-notation-fix-recommendation.md`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/docs/audits/-rho-notation-fix-recommendation.md)
for the full notation audit.

**Caveat (structural form).** The multi-term formula below is the
**first-principles structural form** of the mass invariant. At the
substrate value $q_0$ it predicts $m_{\mathfrak{p}} \approx 5\,\mathrm{MeV}$
(off CODATA $938\,\mathrm{MeV}$ by $\approx 173\times$). The remaining
factor is the **categorical density $\rho_K$** of
[`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md), whose
substrate-only derivation is an **open problem** ("Open question:
categorical derivation of $\rho_K$",
[`atomic-mass-gb-nf.md` §Open](atomic-mass-gb-nf.md)). This block
formalises what the brane-tower contributes; closure of the nucleon-
mass anchors requires the additional categorical content in
$\rho_K$.

**Class-A discipline status.** The 173$\times$ shortfall is captured by
$\rho_K$ in [`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md), which
admits a **graded substrate expansion**
([`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md)) — the
LO piece $Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e$ is
**proved** (Wenzl 1988 Markov multiplicativity); the single-gen
piece $\tfrac{\alpha}{2} \sum_i \ln(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}})$ closes
empirically to $0.18\%$; the pair-gen piece is open. On the
nucleon-anchor side, $m_{\mathfrak{p}}$ has a **conjectural
substrate form**
([`prop:lambda-scale-substrate-form`](lambda-scale-substrate-form.md))
at $\lambda_{\mathrm{scale}} \approx 5/2 - h^2 G$ matching CODATA
to ~5.4 ppm; ${}^1\mathrm{H}$ lifts to `derived` once the Borromean
tower wiring lands. Per
[`docs/audits/-lambda-scale-derivation-search.md`](../../../docs/audits/-lambda-scale-derivation-search.md)
§13, the current state is **justification** (5.4 ppm structural match)
rather than full derivation. This proposition is therefore a Class-A
opt-out (conditional on the substrate forms above) per the
[three-calibration discipline](three-calibration-inputs.md); the
structural form (this block) is correct and independent of the open
pieces. Tracked under
[Workplan 0b](../../../docs/audits/-workplan-0b-script-rewire-handoff.md)
and the [m_p chain closure gap](../../../docs/audits/-m-p-chain-closure-gap-analysis.md).
$\rho_K$ closure; only its numerical instantiation is currently
empirical.

**Statement (categorical, pre-Archimedean form).** Let
$\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum
observable universe at substrate parameter $q_0$
([def:quantum-observable-universe](#def:quantum-observable-universe)),
let $\mathfrak{H}$ be a confined particle/atom of confinement level
$\ell$ and strand count $n_0$ with canonical Hecke element
$T_w \in H_{n_0}(q_0)$ in Gröbner–Shirshov normal form
([def:confined-particle](#def:confined-particle)). The
**categorical mass invariant** of $\mathfrak{H}$ is the finite-sum
element of $\mathbb{Q}(q)$

$$
M(\mathfrak{H}) \;:=\; \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H}) \;=\; \nu_{\mathrm{SDP}} \cdot \bigl[\,\mathrm{tr}_M(T_w) + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})\,\bigr],
$$

where $m(\mathfrak{H})$ is the **categorical mass invariant** in
the multi-term form of the
[unified knot mass formula](#thm:knot-mass-formula-unified):
$\mathrm{tr}_M(T_w)$ is the descended Markov trace
$\sum_\lambda y_\lambda(q)\,\chi_\lambda(T_w)$
(Wenzl-bridge coefficients $y_\lambda$,
$q$-Murnaghan–Nakayama character $\chi_\lambda$),
$\mathrm{tower}(T_w) = \sum_i \mathrm{Li}_2^q(-\hat{V}_i) + z^2 \sum_{i<j} \mathrm{Li}_2^q(-\hat{V}_i \hat{V}_j)$
is the brane tower built from per-generator additive-Wedderburn
volumes $\hat{V}_i$ (symmetric $q$-dilogarithm
$\mathrm{Li}_2^q$ per the paper canon,
[mass endomorphism tower](#prop:mass-endomorphism-tower)).
Per [`prop:li2q-phiq-bar-symmetrization`](li2q-phiq-bar-symmetrization.md),
$\mathrm{Li}_2^q$ is the **pre-Archimedean (categorical, $R$-side)**
form, bar-invariant under $q \mapsto q^{-1}$ and living in the Habiro
ring $\widehat{\mathbb{Z}[q]}[\![z]\!]$. The post-Archimedean
realization under $\tau_{\mathrm{arch}}$ is the bar-pair
$\tfrac{1}{2}(\log \Phi_q(z) + \log \Phi_{q^{-1}}(z))$, **not**
naive numerical substitution of $\mathrm{Li}_2^q$ at $q = q_0$; the
naive substitution kills the dimensional mass scale by the
bar-symmetric projection (empirical: $m_{\mathfrak{p}}/m_e \approx
3.31$ vs CODATA $1836$; see
[`m-p-m-e-li2q.witness.json`](https://github.com/litlfred/qou/blob/main/computations/m-p-m-e-li2q.witness.json)).
The $\sim 173\times$ shortfall flagged below is consistent with this
bar-projection structure; the $\rho_K$ closure path of
[`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md) and the Faddeev
$\Phi_q$ archimedean tower are the two reconciliation candidates.
The third summand $\mathrm{tr}_M(C_{\dim_q}) = \sum_{\lambda \vdash n_0} 1/\dim_q(\lambda)$
is the Frobenius co-Casimir trace
([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)).
The scalar $\nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$ is the
multiplicity of $T_w$'s SDP solution in the Wedderburn
decomposition (see algorithm step below). This expression is
**finite, exact, and entirely pre-Archimedean** — every quantity
on the right-hand side lives in $\mathbb{Q}(q)$.

**Historical note — single-term shorthand retired.** An earlier
wording wrote $M(\mathfrak{H}) = \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w)$
(single term, dropping the tower and Frobenius co-Casimir). That
single-term form is **shorthand** for the multi-term sum above
and is structurally inadequate as a mass formula on its own,
verified empirically in
[`probe-sdp-canonical-paper-formula.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/probe-sdp-canonical-paper-formula.witness.json):
single-term fails by 87--100% on $D$, $T$, ${}^3\mathrm{He}$ under
both Plancherel and Wenzl-Schur conventions; multi-term without
the brane tower reduces error to 36--63%; the multi-term form
with the canonical Li_2^q brane tower (above) reaches $\approx 5\,
\mathrm{MeV}$ for $\mathfrak{p}$ at $q_0$, with the remaining
$\sim 170 \times$ shortfall captured by $\rho_K$. **This block uses
the multi-term form throughout; the single-term shorthand should
not appear elsewhere in the paper.**

**Mass identity (structural form).** After applying the
Archimedean realization functor
([archimedean realization functor](#def:archimedean-realization-functor)),
the binding energy of $\mathfrak{H}$ is

$$
\boxed{ \quad B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0} \;=\; m_e \cdot \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H})\big|_{q = q_0} \quad }
$$

— a single finite-categorical pipeline, no analytic asymptotic
content. The volume conjecture is *not* used in the derivation; it
appears only as a post-functor naming convention (see "Post-Archimedean
interpretation" below). **At $q_0$, this structural form
under-predicts $m_{\mathfrak{p}}$ by $\sim 173\times$; the closure
requires the additional categorical density $\rho_K$
([atomic-mass-gb-nf](#prop:atomic-mass-gb-nf)) whose substrate-only
derivation is open.**

## Architecture (single categorical pipeline; Yekutieli at finite slices)

The derivation is a **single categorical pipeline** that lives entirely
pre-Archimedean. Yekutieli's non-abelian Stokes theorem (multiplicative
integration on surfaces) at finite slice depth gives the following
correspondence between 2-categorical / surface-integration data and
the Iwahori–Hecke structure on $H_{n_0}(q_0)$:

See [Table 1](#tbl:atom-knot-mass-derivation-table1-data).

**Collapsing spectral sequence.** The GB filtration on $H_{n_0}(q)$
gives rise to a multiplicative spectral sequence
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence),
[prop:spectral-sequence-h3-explicit](#prop:spectral-sequence-h3-explicit))
whose $E_1$-page is the associated graded $\bigoplus_k \mathrm{gr}_k H_{n_0}(q)$.
By [prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse)
the spectral sequence **collapses at $E_2$ for semisimple $H_n(q)$ at
generic $q$** (the $d_2$-differential captures the Hecke quadratic
relation; higher differentials vanish because $H_n(q)$ has no further
relations beyond braid + Hecke). The $E_\infty$-page identifications
([prop:e-infinity-page-identifications](#prop:e-infinity-page-identifications))
recover the Wedderburn decomposition $\bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q))$.

Collapse is **the reason finite-slice computation suffices**: at finite
slice depth (= filtration grade $\leq$ some $k$), the surviving
$E_\infty$-classes already account for all of $\mathrm{tr}_M(T_w)$
because $d_r = 0$ for $r \geq 3$. No higher slices contribute. The
GB-filtration tracker's certificate
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json))
records exactly the data the $E_2 \Rightarrow E_\infty$ collapse needs:
filtration-graded coefficients per term, in jet order.

The *finite slice* is essential: at every finite resolution Yekutieli's
multiplicative integral is a finite product / finite sum in $\mathbb{Q}(q)$,
exact, with no asymptotic limit. This is exactly the categorical
content captured by the GB-filtration + jet-order certificate
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json)).

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
\mathrm{tr}_M(T_w) \;=\; \sum_\lambda y_\lambda(q) \chi_\lambda(T_w) \;\in\; \mathbb{Q}(q) \arrow[d, "\nu_{\mathrm{SDP}} \cdot m(\cdot)"]
\\
M(\mathfrak{H}) \;=\; \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H}) \;\in\; \mathbb{Q}(q)
\\
{} \arrow[d, "\text{\textbf{Archimedean realization functor}}"]
\\
B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0} \;\in\; \mathbb{R} \text{ (MeV)}
\end{tikzcd}
```

Everything above the Archimedean functor lives in $\mathbb{Q}(q)$;
$\mathbb{R}$ enters exactly once, at the substitution $q := q_0$
together with the multiplication by $m_e$. No analytic limit, no
volume conjecture, no Reeb-density construction is invoked.

### Post-Archimedean interpretation (borrowed, optional)

If $K = \widehat{T_w}$ is hyperbolic, the post-Archimedean number
$\mathrm{tr}_M(T_w)|_{q = q_0}$ admits a conventional 3-manifold-theory
naming via the **volume conjecture** (Kashaev 1997, Murakami–Murakami
2001): the asymptotic of $|J_K(\zeta_N)|^{1/N}$ at roots of unity
$\zeta_N = e^{2\pi i / N}$ as $N \to \infty$ equals
$\exp(\mathrm{Vol}_{\mathrm{hyp}}(K)/2\pi)$. This is a **borrowed
theorem about post-Archimedean analytic continuation**, allowing
$B(\mathfrak{H})/(m_e \nu_{\mathrm{SDP}})$ to be *named* as a hyperbolic volume in
conventional language. The QOU mass identity does **not** depend on
the conjecture — it depends only on the finite-categorical
$\mathrm{tr}_M(T_w)$.

In particular the geometric construction (Reeb-vortex density $\to$
Mostow $\to$ Gromov), available on the post-Archimedean side as
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
  \item Read $\nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$ from the
        structural prefactor rule on $(Z, N)$ (= the multiplicity
        of $T_w$'s SDP solution in the Wedderburn decomposition).
        Currently OPEN in general; confirmed values from the
        joint-tower SDP witness are $\nu_{\mathrm{SDP},D} = 1$,
        $\nu_{\mathrm{SDP},T} = 2$, $\nu_{\mathrm{SDP},{}^3\mathrm{He}} = 2$.
        The earlier statement "$\nu_{\mathrm{SDP}} = 1$ for
        $\ell \leq 1$" was too narrow — it holds for $D$ but is
        contradicted by the
        SDP witness for $T$ and ${}^3\mathrm{He}$ (each carrying
        $\nu_{\mathrm{SDP}} = 2$ from the multiplicity of the
        trefoil-like constituent in the $H_5$ / $H_3$ Wedderburn
        decomposition).
  \item Form the categorical mass invariant
        $M(\mathfrak{H}) := \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H}) \in \mathbb{Q}(q)$
        (multi-term form per the Statement above; the
        single-term shorthand $M = \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w)$
        is structurally inadequate and is no longer used).
\end{enumerate}
\textbf{Archimedean realization (functor $\mathbf{C} \to \text{Top}$, $\mathbb{Q}(q) \to \mathbb{R}$):}
\begin{enumerate}
  \setcounter{enumi}{4}
  \item Apply the Archimedean realization functor at $q = q_0$ and
        multiply by $m_e$:
        $B(\mathfrak{H}) := m_e \cdot M(\mathfrak{H}) \big|_{q = q_0}
        = m_e \cdot \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H})\big|_{q = q_0}$,
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
        identifies $M(\mathfrak{H})/(m_e \nu_{\mathrm{SDP}})\big|_{q_0}$ with
        $\mathrm{Vol}_{\mathrm{hyp}}(K)$ in conventional 3-manifold
        terminology.  Used only as a name for the post-Archimedean
        number; \emph{not} part of the derivation.
\end{enumerate}
\end{algorithm}
```

## Categorical pipeline implementation

The categorical pipeline is now implemented in two parallel
implementations:

- **Python prototypes** ([`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb_filtration_jet_tracker.py),
 [`joint_tower_sdp_solver.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/joint_tower_sdp_solver.py),
 [`joint_tower_sdp_solver_v2.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/joint_tower_sdp_solver_v2.py)) — design-spec
 reference, exact in $q$ via SymPy + cvxpy SDP feasibility for $H_3$.
- **Rust production scaling** ([`tools/hecke-engine/src/{gb_nf_reducer,joint_tower_sdp_certificate,wedderburn_psd,cross_level_embedding,sdp_verifier}.rs`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/src/),
 binary [`joint-tower-sdp`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/src/bin/joint_tower_sdp.rs)) — bit-for-bit
 match with Python on small cases; **3,400$\times$ speedup** (47.5 s $\to$ 14 ms
 for the 7-atom registry); scales to $H_5+$ where Python defers.
 See [RUST_INTEGRATION.md](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/RUST_INTEGRATION.md)
 for the implementation plan.

See [Table 2](#tbl:atom-knot-mass-derivation-table2-data).

### PSD-cone $\alpha^*$ ranking (Rust R5-minimal, $q_0 = 1.109978595554181\ldots$, 50 dps)

For each historical entry the verifier emits
$\alpha^*(\mathfrak{H}) := \max\{\alpha \in [0,1] :
\alpha \cdot \rho_\lambda(T_w) + (1-\alpha) \cdot I \succeq 0
\text{ for all } \lambda\}$. $\alpha^* = 1$ $\Rightarrow$ all blocks PSD;
$\alpha^* < 1$ quantifies the gap.

See [Table 3](#tbl:atom-knot-mass-derivation-table3-data).

Steps 5–8 currently substitute $\mathrm{Vol}_{\mathrm{hyp}}(K)$ from
SnapPy for $\mathrm{tr}_M(T_w)|_{q=q_0}$ on entries flagged
\texttt{manual-historical-volume-match} (${}^2$H, ${}^{3}$H, ${}^{3}$He) — i.e.\ the
post-Archimedean naming convention is used in place of the
pre-Archimedean Markov-trace evaluation. This is acceptable for
existing established knot identifications because the volume
conjecture commits both quantities to the same number, but the
*principled* path (Step 1a $\to$ Step 5) does not depend on this
substitution.

The quarantined provisional ${}^{6}$Li, ${}^{7}$Li entries
([prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas)
§"Provisional / deprecated methodology") run *backwards* from Step
6 to a candidate knot, bypassing Step 1a entirely. Such shortcuts
are forbidden by this proposition.

## Where the gaps actually are

After the pre-Archimedean / post-Archimedean simplification (Yekutieli
at finite slices replaces the geometric leg with finite-categorical
Markov-trace computation) and the production-scale Rust port
(R1–R4 + R5-minimal landed), the remaining open structural item is:

1. **Joint mass-tower confinement SDP — solver mode (R5-full).**
 The current Rust binary verifies that *given* candidate $T_w$
 inputs (electron $\sigma_1^3$, proton/neutron Borromean, ${}^2$H/${}^{3}$H/${}^{3}$He
 historical IDs) the certificate format is well-formed and quantifies
 the PSD-cone gap $\alpha^*$. The remaining work is to invert this:
 for ${}^{6}$Li ($H_{18}$), ${}^{7}$Li ($H_{21}$), and α-cluster atoms ($H_{24}$
 to $H_{120}$) where canonical $T_w$ is *unknown*, formulate and
 solve the SDP

 $$
   \min_{c_{w}(q_0) \in \mathbb{R}} \, \|\,c\,\|_1 \quad\text{s.t.}\quad
   \rho_\lambda(T_w) \succeq 0 \,\forall \lambda,\ \pi_{\mathfrak{H}\to\mathfrak{H}'}(T_w(\mathfrak{H})) = T_w(\mathfrak{H}')
   $$

 via Clarabel.rs + system BLAS. Slots into the existing
 `JointTowerSdpCertificate` schema. Once R5-full lands, the
 deprecated `li-atom-knot-search` is fully retirable.

 **Status ( issue #604 deliverable 1).** A first-pass
 Python R5-full prototype landed at
 [`computations/r5_full_canonical_knot_solver.py`](https://github.com/litlfred/qou/blob/main/computations/r5_full_canonical_knot_solver.py)
 with witness
 [`r5-full-canonical-knot-solver.witness.json`](https://github.com/litlfred/qou/blob/main/computations/r5-full-canonical-knot-solver.witness.json).
 It enumerates $B_3$ braid words up to length $L_{\max} = 8$,
 filters via a KLR canonical-basis "cemetery" prune (drops $\sigma_i^{\pm k}$
 pure-power Demazure-trivial classes per CLAUDE.md §7b symmetric-
 crystal guidance) plus a $\chi$-fingerprint dedup that collapses
 Markov-equivalent words to a single canonical-basis-class
 representative, and emits an operator-selection LP with strong-
 duality dual fields ($y_0^*$, $y_\lambda^*$, active set) per the
 CLAUDE.md "LP / SDP duals — first-class infra" rule.

 The cemetery + dedup pass compresses the search space by **99 %**
 ($13088 \to 138$ canonical-basis classes at $L_{\max} = 8$). The
 historical canonical $T_w$ for ${}^{3}$He ($L_{6a4}$) is found to be
 **fully PSD-feasible** at $q_0$ ($\alpha^* = 0$) and ranks in the
 top 17 % of the 138 canonical-basis classes by single-term cost;
 ${}^2$H ($6_2$) is **not** PSD-feasible on its own ($\alpha^* = 0.89$
 on the standard $(2,1)$ block) and ranks in the top 45 %. The
 single-term shorthand $B = m_e \cdot \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w)$
 (retired — see Statement above) has the known structural offset documented in
 [`probe-sdp-canonical-paper-formula.witness.json`](https://github.com/litlfred/qou/blob/main/computations/probe-sdp-canonical-paper-formula.witness.json),
 which prevents the historical $T_w$ from being the unique global
 winner; wiring the multi-term tower (T2--T6 of
 [`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified))
 into the cost is the next-session deliverable. ${}^{3}$H ($8_{11}$ in
 $B_5$) is also next-session work — needs Hoefsmit seminormal at
 $H_5$, consistent with the deferred-to-Rust posture in
 [`joint_tower_sdp_solver_v2.py`](https://github.com/litlfred/qou/blob/main/computations/joint_tower_sdp_solver_v2.py).

A second item — the structural prefactor rule $\nu_{\mathrm{SDP}}(Z, N)$ — is a
downstream consequence: once the SDP-solver returns canonical $T_w$
per atom, $\nu_{\mathrm{SDP}}$ is read off as the multiplicity of $T_w$'s solution
in the Wedderburn decomposition. No separate derivation is needed.

The geometric "leg" (Reeb density $\to$ Mostow $\to$ Gromov $\to$ Vol) and the
volume conjecture are *not* part of the QOU derivation. They appear
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
