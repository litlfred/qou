**Proposition.**
*Fix a [confined particle](#def:confined-particle) $P$ and let
$\mathcal{G} \subset \mathbb{R}_{>1}$ be the generic locus of the
substrate parameter $q$.  Define the **confinement locus** of $P$:*

$$
  \Omega(P) \;:=\; \{\, q \in \mathcal{G} : \mathrm{confined}(P, q) \,\},
$$

*where $\mathrm{confined}(P, q)$ is the Slater-strict feasibility
predicate of the [confinement SDP](#prop:confinement-sdp)
(there exists $\Phi \succ 0$ satisfying every primal constraint
with strict PSD margin).  Then:*

1. ***Openness.** $\Omega(P)$ is an open subset of $\mathcal{G}$.*

2. ***Stratification.** $\mathcal{G} \setminus \Omega(P) =
   \partial\Omega(P) \cup \Omega(P)^c$ decomposes as a
   real-algebraic stratification in finitely many strata of
   codimension $\ge 1$ — the **phase boundaries** of $P$.  Each
   stratum is the zero locus of a determinant polynomial
   $\det\bigl(\text{principal minor of }\mathrm{G}(q)\bigr) = 0$ for some
   principal minor of the SDP Gram matrix.*

3. ***Local constancy on components.** Let $\Omega_\alpha \subseteq
   \Omega(P)$ be any connected component (a **confinement phase**).
   Then on $\Omega_\alpha$:*
   - *the active support $\mathcal{S}^*(P, q)$ is constant as a
     finite set of Wedderburn labels;*
   - *the binding multiplicity
     $\mu(P, q) = |\mathcal{S}^*(P, q)|$ is constant;*
   - *the Frobenius stability index $\sigma_F(P, q) =
     n_{\mathrm{target}} \cdot u_0^*(P, q)$ is continuous
     (real-analytic in $q$ on the interior).*

4. ***Scope of confinement statements.**  Every statement of
   [prop:level-sufficiency](#prop:level-sufficiency),
   [prop:shell-closure-stability](#prop:shell-closure-stability),
   and their corollaries, as well as the Markov-trace preservation
   of the [confinement category](#def:confinement-category) functor
   $\mathrm{tr}_M: \mathbf{Conf} \to \mathbb{C}(q)$, holds
   **pointwise in each $\Omega_\alpha$** and in general **fails on
   $\partial\Omega(P)$**.*

5. ***Boundary crossings = phase transitions.** If a continuous
   deformation $q: [0, 1] \to \mathcal{G}$ crosses a phase boundary
   at $q_0 \in \partial\Omega(P)$, then at $q_0$ one of the
   following holds:*
   - ***Deconfinement.** $\mathrm{confined}(P, q_0)$ fails;
     $P$ is not realisable as a closed-braid bound state at $q_0$
     (cf. [deconfinement threshold](#rem:deconfinement-golden-threshold)).*
   - ***Regime switch.** $\mu$ jumps discretely across $q_0$;
     the active support gains or loses a Wedderburn block;
     $\sigma_F$ has a non-smooth point
     (cf. [parity regime selection](#thm:parity-regime-selection)).*
   - ***Both.***

*

**Corollary (phase-scoped applicability).**
*Any theorem, proposition, or definition in the confinement
framework that references
[def:confined-particle](#def:confined-particle),
[def:confinement-category](#def:confinement-category),
[prop:confinement-sdp](#prop:confinement-sdp),
[prop:level-sufficiency](#prop:level-sufficiency),
def:electron-shell,
[def:dressed-particle](#def:dressed-particle), or
[prop:shell-closure-stability](#prop:shell-closure-stability) is
to be read with the implicit scope "for all
$q \in \Omega_\alpha(P)$, some fixed confinement phase of $P$".
Statements that must hold across phase boundaries (e.g. phase-
transition signatures, critical exponents, scaling laws) require
explicit boundary analysis and are not covered by the
within-phase theorems.*

**Remark (topology of $\Omega(P)$).**
*For simple particles (quark, free nucleon) $\Omega(P)$ is a
single connected interval of $\mathcal{G}$ containing $q_0$.
For composite particles with multi-block binding
($\mu \ge 2$, e.g. noble-gas dressed atoms), $\Omega(P)$ can be
disconnected — each component corresponds to a distinct
configuration of the active support.  Transitions between
components are physically realised as chemical or nuclear
rearrangements (e.g. $\mathrm{sp}^3 \leftrightarrow \mathrm{sp}^2$
hybridisation of carbon), and show up computationally as
regime switches in the witness files
`sdp_cross_channel.py` and `parity-regime-selection`.*
