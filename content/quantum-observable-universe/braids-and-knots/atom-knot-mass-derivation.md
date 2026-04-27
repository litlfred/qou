**Statement.**  Let $\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$
be a quantum observable universe at substrate parameter $q_0$
([def:quantum-observable-universe](#def:quantum-observable-universe)),
let $\mathfrak{H}$ be a confined particle/atom of confinement level $\ell$
and strand count $n_0$ with canonical Hecke element
$T_w \in H_{n_0}(q_0)$ in Gröbner–Shirshov normal form
([def:confined-particle](#def:confined-particle)), and let
$K = \widehat{T_w}$ be the Markov closure of $T_w$ in $S^3$.  If
$K$ is a hyperbolic knot/link, then there exists $\rho \in
\mathbb{Z}_{>0}$, structurally determined by $\mathfrak{H}$, such that

$$
B(\mathfrak{H}) \;=\; \rho \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(K),
$$

where $B(\mathfrak{H})$ is the binding energy of $\mathfrak{H}$, $m_e$
is the electron mass, and $\mathrm{Vol}_{\mathrm{hyp}}$ is the
hyperbolic volume of $K$ in $S^3$.  Moreover the equality is
established by *two parallel derivations* — a **geometric leg** running
top-down from the categorical action, and an **algebraic leg** running
bottom-up from the confinement SDP — that meet at the volume conjecture
identity.

## Architecture (two legs meet at $\mathrm{Vol}_{\mathrm{hyp}}$)

```tex
\begin{tikzcd}[row sep=large, column sep=large]
\textbf{Categorical action of } \mathbf{C} \text{ on } \mathcal{S} \arrow[d, "\text{induce } \nabla"]
& & \textbf{Confinement SDP at } q_0 \arrow[d, "\text{joint mass tower}"]
\\
\text{Connection } \nabla \text{ on } \mathcal{S} \arrow[d, "\text{Stokes}"]
& & T_w \in H_{n_0}(q_0) \text{ (GB-NF)} \arrow[d, "\text{Wedderburn}"]
\\
\text{Frobenius pairing } \langle\,,\,\rangle = \mathrm{tr}_{\mathrm{Ad}}(- \otimes -^*) \arrow[d, "\text{push to cover}"]
& & H_{n_0}(q) \cong \bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q)) \arrow[d, "y_\lambda \text{ (Wenzl)}"]
\\
\text{Reeb-vortex density } \mu \text{ on } S^3 \setminus K \arrow[d, "\text{Mostow + Gromov}"]
& & \mathrm{tr}_M(T_w) \;=\; \sum_\lambda y_\lambda(q) \chi_\lambda(T_w) \arrow[d, "\text{R--T}"]
\\
\mathrm{Vol}_{\mathrm{hyp}}(K) \arrow[rr, leftrightarrow, "\text{volume conjecture}"]
& & J_K(q) \;=\; \mathrm{tr}_M(T_w)
\\
\textbf{geometric leg} & & \textbf{algebraic leg}
\end{tikzcd}
```

Both legs land on the same $\mathrm{Vol}_{\mathrm{hyp}}(K)$.  The
mass identity $B = \rho \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}$
is then the comparison to AME via the Archimedean realization functor
([prop:archimedean-realization-functor](#prop:archimedean-realization-functor))
which fixes the dimensional bridge.

## Algorithm

```tex
\begin{algorithm}
\caption{\textsc{AtomKnotMass}: end-to-end mass derivation from
$\mathfrak{H}$ to $B(\mathfrak{H})$.}
\textbf{Input.}  Confined particle $\mathfrak{H}$ with confinement
level $\ell$, strand count $n_0$, registry entry in
\texttt{def:confined-particle}.  Substrate parameter $q_0$.
\\
\textbf{Output.}  $B(\mathfrak{H}) \in \mathbb{R}_{\geq 0}$ in MeV,
with methodology tag and high-precision certificate.
\\
\hrulefill
\\
\textbf{Algebraic leg (bottom-up):}
\begin{enumerate}
  \item Run the joint mass-tower confinement SDP on all
        $\ell' \leq \ell$ atoms simultaneously.  Output: a
        \emph{structured certificate} per atom recording
        \begin{enumerate}
          \item the canonical Hecke element $T_w \in H_{n_0}(q_0)$ in GB-NF,
          \item the Gröbner--Shirshov filtration grade per term,
          \item the jet-order of reductions.
        \end{enumerate}
  \item Take the Markov closure $K := \widehat{T_w}$ in $S^3$.
  \item Compute the Markov trace symbolically in $q$ via the
        Wedderburn decomposition + Wenzl bridge:
        $\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda(q) \chi_\lambda(T_w)$
        (\texttt{prop:alpha-k-derivation-procedure},
        $y_\lambda$ from Wenzl-bridge witness, $\chi_\lambda$ from
        $q$-Murnaghan--Nakayama).
  \item Evaluate $J_K(q_0) = \mathrm{tr}_M(T_w)$ at substrate $q_0$
        with $\geq 50$ decimal digits via MPFR.
\end{enumerate}
\textbf{Geometric leg (top-down):}
\begin{enumerate}
  \setcounter{enumi}{4}
  \item From the categorical action of $\mathbf{C}$ on $\mathcal{S}$
        and the Frobenius pairing on $\mathrm{End}_{\mathbf{C}}(A)$,
        build the Reeb-vortex density $\mu$ on the universal cover of
        $S^3 \setminus K$.
  \item Integrate $\mu$ against the Gromov norm to obtain
        $\mathrm{Vol}_{\mathrm{hyp}}(K) = \|S^3 \setminus K\|_{\mathrm{Gr}} \cdot v_3$
        (Mostow rigidity + Gromov norm theorem).
\end{enumerate}
\textbf{Bridge:}
\begin{enumerate}
  \setcounter{enumi}{6}
  \item Verify the volume-conjecture identity at $q_0$:
        $\mathrm{Vol}_{\mathrm{hyp}}(K)$ from step 6 matches the
        asymptotic $2\pi \lim_{N \to \infty} (1/N) \log |J_K(e^{2\pi i/N})|$
        derived from step 4.
\end{enumerate}
\textbf{Mass identity:}
\begin{enumerate}
  \setcounter{enumi}{7}
  \item Read $\rho \in \mathbb{Z}_{>0}$ from the structural prefactor
        rule on $(Z, N)$ (open in general; $\rho \in \{1, 2\}$ for
        $\ell \leq 2$ light atoms, $\rho = 5$ observed for ⁶Li/⁷Li
        — derivation pending).
  \item Compute $B_\mathrm{pred} = \rho \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(K)$.
  \item Compare to $B_\mathrm{AME}$ via the Archimedean realization
        functor; emit the residual $\Delta = B_\mathrm{pred} - B_\mathrm{AME}$
        in MeV and ppb.
  \item Tag the result with one of:
        \texttt{principled-derivation} (algebraic + geometric legs both
        verified), \texttt{principled-gb-nf} (trivial-NF entries
        only), \texttt{manual-historical-volume-match} (knot ID by
        earlier work, GB-NF derivation pending),
        \texttt{magic-A-formula} (algebraic shell-closure rule),
        \texttt{recursive-on-${}^{4}$He} (cluster recursion).
        Quarantine separately if \texttt{deprecated-volume-match}.
\end{enumerate}
\end{algorithm}
```

## Pipeline status

| Step | Implementation | Status |
|---|---|---|
| 1a (canonical $T_w$) | confinement SDP solver | ✓ for $\ell \leq 1$; **gap** for $\ell = 2$ atoms |
| 1b (GB-filtration) | [`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb_filtration_jet_tracker.py) | ✓ PoC for $H_2$, $H_3$ |
| 1c (jet-order) | same module | ✓ PoC for $H_2$, $H_3$ |
| 1 (joint-tower SDP) | not built — **design pending** | ✗ |
| 2 (Markov closure) | conceptual | ✓ |
| 3 (Markov trace symbolic) | [`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/y_lambda_wenzl_bridge_extended.py) + [`q_mn_recursive_memoized.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/q_mn_recursive_memoized.py) | ✓ for $n \leq 12$ |
| 4 ($J_K(q_0)$ at $\geq 50$ dps) | MPFR via SymPy/mpmath | ✓ |
| 5 (Reeb density) | not built — **design pending** | ✗ |
| 6 (Mostow + Gromov $\Rightarrow$ Vol) | borrowed (Thurston/Mostow) | ✓ as theorem; not derived from QOU |
| 7 (volume conjecture verification) | not built — **gap** | ✗ |
| 8 ($\rho(Z, N)$ rule) | open structural question | ✗ |
| 9 ($B_\mathrm{pred}$ via mass identity) | [`recursive_atom_knot_atlas_render.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/recursive_atom_knot_atlas_render.py) using [`hp_volume.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/hp_volume.py) at $\geq 50$ dps | ✓ |
| 10 (AME comparison) | mass-table-ppb witness | ✓ |
| 11 (methodology tag) | [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/methodology-deprecation.witness.json) | ✓ |

The principled atlas
([prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas))
currently runs steps 9–11 against pre-existing knot identifications
from $\ell \leq 1$ entries (where 1–4 are done) and $\ell = 2$ entries
flagged \texttt{manual-historical} (steps 1, 5–7 pending).  The
quarantined provisional ⁶Li, ⁷Li entries are exactly those whose
pipeline shortcut runs *backwards* from step 9 to a candidate knot,
i.e.\ they reverse-engineer a $K$ that makes step 10 small without
touching steps 1, 5–7.  Such shortcuts are forbidden by this
proposition.

## Where the gaps actually are

The two genuine open derivations:

1. **Reeb-vortex density $\mu$ from the categorical Frobenius pairing.**
   This is the geometric leg's content.  Without it, the QOU framework
   *borrows* the volume conjecture rather than *deriving* it — which is
   methodologically the same shortcut the volume-match search makes,
   only at a more abstract level.  The simplest non-trivial test case
   is the Borromean rings $\mathcal{B}_3 = \widehat{(\sigma_1 \sigma_2^{-1})^3}$
   where $\mathrm{Vol}_{\mathrm{hyp}} = 7.32772\ldots = 8 G$ is known
   exactly.

2. **Joint mass-tower confinement SDP.**  The algebraic leg's first
   step.  Per-atom SDPs are insufficient because the GB filtration and
   jet-order grading must be *consistent across confinement levels* —
   only a joint SDP enforces that.  Certificate format already locked
   ([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json)).

The structural prefactor rule $\rho(Z, N)$ is a downstream consequence
once both legs are derived — it falls out of the SDP solution
multiplicities.

## Refs

- Volume conjecture: Kashaev (1995), H.\ Murakami--J.\ Murakami (2001).
- Mostow rigidity: Mostow (1968), Prasad (1973).
- Gromov norm: Gromov (1982), Thurston (1979).
- Wenzl bridge $y_\lambda = s_{\lambda, r}(Q)/Z$: Wenzl (1988), Jones (1989).
- Iwahori--Hecke algebra + GB-NF: Kassel--Turaev (2008).
- Confinement SDP: [prop:confinement-sdp](#prop:confinement-sdp).
- AME 2020: Wang et al.\ (2021).
