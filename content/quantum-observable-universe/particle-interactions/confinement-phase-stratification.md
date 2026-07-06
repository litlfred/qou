**Proposition.** Let $P$ be a [confined particle](#def:confined-particle). Let $\mathcal{G} \subset \mathbb{R}_{>1}$ be the generic locus of the substrate parameter $q$. The **confinement locus** of $P$ is

$$
  \Omega(P) \;:=\; \{\, q \in \mathcal{G} : \mathrm{confined}(P, q) \,\},
$$

where $\mathrm{confined}(P, q)$ is the strict feasibility predicate of the [confinement SDP](#prop:confinement-sdp). Then:

1. **Openness.** $\Omega(P)$ is open in $\mathcal{G}$.
2. **Stratification.** The complement $\mathcal{G} \setminus \Omega(P)$ decomposes into a real-algebraic stratification. The strata have codimension $\ge 1$ and form the **phase boundaries** of $P$. Each stratum is the zero locus of a principal minor of the SDP Gram matrix.
3. **Local constancy.** Let $\Omega_\alpha \subset \Omega(P)$ be a connected component (a **confinement phase**). On $\Omega_\alpha$:
   - the active support $\mathcal{S}^*(P, q)$ is constant;
   - the binding multiplicity $\mu(P, q) = |\mathcal{S}^*(P, q)|$ is constant;
   - the Frobenius stability index $\sigma_F(P, q) = n_{\mathrm{target}} \cdot u_0^*(P, q)$ is real-analytic.
4. **Scope.** The statements of [prop:level-sufficiency](#prop:level-sufficiency) and [prop:shell-closure-stability](#prop:shell-closure-stability), and the Markov-trace preservation of the [confinement category](#def:confinement-category) functor, hold pointwise in each $\Omega_\alpha$ and fail on $\partial\Omega(P)$.
5. **Phase transitions.** If a continuous deformation $q: [0, 1] \to \mathcal{G}$ crosses a phase boundary at $q_0 \in \partial\Omega(P)$, then at $q_0$ one of the following holds:
   - **Deconfinement.** $P$ is not realisable as a closed-braid bound state at $q_0$ (cf. [deconfinement threshold](#rem:deconfinement-golden-threshold)).
   - **Regime switch.** $\mu$ jumps discretely across $q_0$; the active support gains or loses a Wedderburn block; $\sigma_F$ has a non-smooth point (cf. [parity regime selection](#thm:parity-regime-selection)).
   - **Both.**

**Archimedean specialisation (§7c).** This block invokes real- or complex-analytic constructs (observables, bounds, numerical evaluation). Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here.
