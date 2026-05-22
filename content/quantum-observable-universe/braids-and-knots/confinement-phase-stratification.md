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

*Proof.*
*Claim (1) — Openness.
Slater-strict feasibility of an SDP is preserved under small
perturbations of the defining data (Boyd–Vandenberghe Lemma 5.4.1):
if $\Phi_0 \succ 0$ is strictly feasible at $q_0$, then for every
$q$ in a neighbourhood of $q_0$ the same $\Phi_0$ remains strictly
feasible (continuity of the SDP constraint matrices in $q$).
Hence $\Omega(P)$ is a union of open neighbourhoods, i.e. open.*

*Claim (2) — Stratification.
The complement $\mathcal{G} \setminus \Omega(P)$ is defined by the
vanishing of a finite product of principal-minor determinants of
the Gram matrix $\mathrm{G}(q)$ — each such determinant is a polynomial in
$q$ with finitely many real zeros in $\mathcal{G}$.  The union of
these zero sets forms a real-algebraic stratification; generic
strata have codimension 1 (single-minor vanishing), with lower
strata appearing at simultaneous vanishings.*

*Claim (3) — Local constancy.
On each component $\Omega_\alpha$, the active support
$\mathcal{S}^*(P, q)$ is determined by the sign pattern of
complementary-slackness dual variables $u_\lambda^*(q)$.  By
continuity of the SDP optimiser in $q$ (generic uniqueness from
Slater strictness, [Boyd–Vandenberghe §5.5.3](https://doi.org/10.1017/CBO9780511804441))
and by integer-valuedness of $|\mathcal{S}^*|$, the set
$\mathcal{S}^*(P, q)$ cannot change within $\Omega_\alpha$: any
change requires some $u_\lambda^*$ to pass through zero, which is
precisely the phase-boundary condition.  Continuity of $\sigma_F$
follows from continuity of the SDP optimal value under Slater
regularity.*

*Claim (4) — Scope.
The proofs of [prop:level-sufficiency](#prop:level-sufficiency)
(Markov-inclusion + active-support preservation) and
[prop:shell-closure-stability](#prop:shell-closure-stability)
(SDP-relaxation monotonicity + multi-block tightness) each assume
the active support is well-defined and locally constant, i.e.
assume $q \in \Omega_\alpha$.  Any one of claims (3)'s three
properties failing on $\partial\Omega(P)$ is sufficient to
invalidate the corresponding proof, so the scope is confined to
the open stratum.*

*Claim (5) — Phase transitions.
A boundary crossing at $q_0$ is by definition either a Slater-loss
event (primal strict PSD feasibility breaks $\to$ deconfinement) or an
active-support transition (some $u_\lambda^*$ passes through zero
$\to$ regime switch with $\mu$-jump).  Both correspond to the
discrete-regime-switch phenomenology already logged in
[prop:parity-regime-selection](#thm:parity-regime-selection) and
the [deconfinement golden threshold](#rem:deconfinement-golden-threshold).
$\square$*

**Corollary (phase-scoped applicability).**
*Any theorem, proposition, or definition in the confinement
framework that references
[def:confined-particle](#def:confined-particle),
[def:confinement-category](#def:confinement-category),
[prop:confinement-sdp](#prop:confinement-sdp),
[prop:level-sufficiency](#prop:level-sufficiency),
[def:electron-shell](#def:electron-shell),
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
