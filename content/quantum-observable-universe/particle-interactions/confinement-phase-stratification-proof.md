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
