**Proposition (operator-valued mass-endomorphism tower).**
*Let $\mathcal{B}_K = \beta_{\mathrm{disjoint}} \cdot \beta_{\mathrm{interface}} \in
H_n(R, q)$ be the canonical atomic braid of an atom $K = (Z, N)$ with
$n = 3(Z+N)$, factored into disjoint constituent braids
$\beta_{\mathrm{disjoint}} = \beta_1 \otimes \cdots \otimes \beta_{Z+N}$
(each $\beta_i \in H_3(R, q)$) and an interface braid
$I := \beta_{\mathrm{interface}} \in H_n(R, q)$ supported on the
between-nucleon strands
([`def:canonical-braid-interface-composition`](#def:canonical-braid-interface-composition)).
Then the per-$\lambda$ Wedderburn-block contribution to the mass tower
admits the **operator-valued** form*

$$
  \boxed{\;
    \chi^\lambda(\mathcal{B}_K)
    \;=\;
    \sum_{(\mu_1, \ldots, \mu_{Z+N})} \;
    \operatorname{Tr}_{V_{\mu_1} \otimes \cdots \otimes V_{\mu_{Z+N}}}\!\Biggl(
       A^\lambda_{\mu_1, \ldots, \mu_{Z+N}}(I)
       \;\cdot\;
       \bigotimes_{i=1}^{Z+N} \rho_{\mu_i}(\beta_i)
    \Biggr),
  \;}
$$

*where $A^\lambda_{\mu_1, \ldots, \mu_{Z+N}}(I) \in
\mathrm{End}(\bigotimes_i V_{\mu_i})$ is the iterated diagonal-summed
$(\mu_1, \ldots, \mu_{Z+N})$-block of $\rho_\lambda(I)$ in the
iterated LR basis, generalising the two-factor decomposition of
[`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)
to the $(Z+N)$-factor parabolic chain
$H_3^{\otimes(Z+N)} \hookrightarrow H_n$. Under the
[`prop:lr-tensor-character-bridge`](lr-tensor-character-bridge.md)
specialisation $I = \mathbf{1}$, the operator collapses to the identity
and the boxed identity reduces to the LR coefficient
$c^\lambda_{\mu_1, \ldots, \mu_{Z+N}}$ times the scalar character
product
$\prod_i \chi^{\mu_i}(\beta_i)$; the interface contribution
$I \neq \mathbf{1}$ is precisely the operator-valued residual
$A^\lambda_{\mu_1, \ldots, \mu_{Z+N}}(I) - c^\lambda \cdot \mathbf{1}$.*

### Mass-endomorphism tower in operator-valued form

*Per the SUPERSEDED banner in [`prop:mass-endomorphism-tower`](mass-endomorphism-tower.md),
the scalar Wedderburn-volume tower
$\mathfrak{m} = |\!\prod \hat V_i| + \sum_i F(|\hat V_i|) +
z^2 \sum_{i<j} F(|\hat V_i \hat V_j|)$ (with $F \in \{\Phi_q, -\mathrm{Li}_2^q(-\cdot)\}$)
is **structurally wrong**: it is braid-class-independent at the
$\rho_q = 1/\hbar_q^2$ ansatz level, but the empirical categorical
density $\rho_K$ varies $\sim 30\times$ across $A = 1\ldots 3$
([`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md)).
The correct dimensional factor is the operator
$A^\lambda_{\mu_1, \ldots, \mu_{Z+N}}(I)$ above, which depends on
the interface braid $I$ through its LR-block matrix entries (Hoefsmit
seminormal action of the boundary generators).*

*The operator-valued mass formula is then*

$$
  \mathcal{M}(K) \;=\; m_e \cdot \sum_{\lambda \vdash n} \tilde w_\lambda \cdot
    \log\Bigl|
      \sum_{\vec\mu}
      \operatorname{Tr}_{\bigotimes V_{\mu_i}}\!\bigl(
        A^\lambda_{\vec\mu}(I)
        \cdot \textstyle\bigotimes_i \rho_{\mu_i}(\beta_i)
      \bigr)
    \cdot \dim_q V_\lambda
    \Bigr|,
$$

*where the per-block magnitude inside the logarithm is the operator
trace from the boxed identity above (replacing the scalar
$|\chi^\lambda(\mathcal{B}_K) \cdot \dim_q V_\lambda|$ of the
depth-stratified formula
[`prop:plancherel-term-7-formulation`](plancherel-term-7-formulation.md))
and $\tilde w_\lambda = \dim_q^2 V_\lambda / [n]_q!$ is the q-deformed
Wedderburn weight.*

### Reduction to scalar limits

*The scalar Wedderburn-volume formula of the original
[`prop:mass-endomorphism-tower`](mass-endomorphism-tower.md) is
recovered in two specialisations:*

1. **$I = \mathbf{1}$ (disjoint product, no interface).** *Single
   nucleons ($A = 1$, $Z = 1, N = 0$ or $Z = 0, N = 1$): there is no
   interface, so $A^\lambda_\mu(\mathbf{1}) = \mathrm{id}_{V_\mu}$, and the
   per-block trace factors as $\dim V_\mu \cdot \chi^\mu(\beta_1)$. The
   operator-valued formula reduces to the scalar
   $\hat V_i$ formula at $A = 1$, where the substrate-only ansatz
   $\rho_q$ happens to be braid-class-correct (no interface variation).*

2. **Scalar $(\mu, \nu)$-block subset.** *For partitions $\lambda$
   where the LR decomposition gives only 1-dim $V_\mu \otimes V_\nu$
   blocks (e.g. $\lambda \in \{(n), (1^n)\}$), the operator is a scalar
   multiple of the identity, and the trace becomes
   $A^\lambda_{\mu, \nu}(I) \cdot \chi^\mu(\beta_1) \cdot \chi^\nu(\beta_2)$.
   Per
   [`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)
   Step 5, of the $30$ $(\mu, \nu)$-blocks across the $11$ partitions
   $\lambda \vdash 6$, $12$ are scalar and $18$ are genuinely
   operator-valued.*

### Why this is the Stage-1 unblock

*Per the bar-symmetrization identity
[`prop:li2q-phiq-bar-symmetrization`](li2q-phiq-bar-symmetrization.md)
and the broader three-layer synthesis
[`prop:bar-symmetric-three-layer-synthesis`](bar-symmetric-three-layer-synthesis.md),
the substitution $\Phi_q \leftrightarrow \mathrm{Li}_2^q$ is **not** a
function swap but a context-split: $\Phi_q$ is the post-$\tau$
archimedean form (carries dimensional mass scale), $\mathrm{Li}_2^q$ is
the pre-$\tau$ R-side bar-symmetric form (mass-scale cancels). Neither
substitution recovers the empirical $m_p/m_e \approx 1836$ from the
scalar $\hat V_i$ formula because the dimensional-scale carrier is
**not in the scalar volumes** — it is in the operator $A^\lambda_{\vec\mu}(I)$,
specifically in its non-scalar (off-diagonal) action on the boundary
strands. The interface contribution to the canonical-atom Markov
trace is pinned at $\tau_M(\mathcal{B}_K) / \tau_M(\mathcal{B}_K^{\mathrm{vac}}) = z$
per Z-step (derivation-grade, on `main` via the PR #819 Phase 5c.1
family — `prop:interface-knot-markov-z`); the complementary
constit-side ratio $\rho_Z^{\mathrm{constit}}(q)$ should factorize
through the operator-valued $A^\lambda_{\vec\mu}(\mathbf{1})$ blocks
(trivial-interface case) of the iterated formula, providing a
candidate categorical derivation path now that the $(2q-1)$ closed
form has been falsified globally by
[PR #842 Phase 5k.2](https://github.com/litlfred/qou/pull/842).*

*The operator-valued formula above resolves this:*

- *the **product** $|\!\prod \hat V_i^{\mathrm{full}}|$ becomes the
  diagonal block-trace
  $\sum_{\vec\mu} \prod_i \mathrm{diag}_T A^\lambda_{\vec\mu}(I)_{TT} \cdot
  \chi^{\mu_i}(\beta_i)$ — the SAME scalar-leading contribution;*
- *the **single-gen sum** $\sum_i F(|\hat V_i|)$ is recovered as the
  trace of the diagonal piece of $A^\lambda$ acting on a single boundary
  strand — the $\rho_K^{\text{single-gen}}$ piece of
  [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md);*
- *the **pair-gen sum** $\sum_{i<j} z^2 F(|\hat V_i \hat V_j|)$ is the
  open piece — it is the **off-diagonal residual** of $A^\lambda_{\vec\mu}(I)$
  acting on TWO boundary strands simultaneously (i.e., the operator's
  $T \neq T'$ matrix elements via the Hoefsmit off-diagonal entries
  $\sqrt{1 - h_q(d_T)^2}$, per
  [`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)
  Step 3).*

*This identifies the pair-gen / $A \geq 4$ structural gap in
[`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) **not** as
a missing scalar term but as the missing off-diagonal contribution of
the operator-valued residual; closing this gap reduces to summing the
Hoefsmit off-diagonal matrix entries over the SYT pairs $(T, T')$
that contribute to the operator's $\sqrt{1 - h_q^2}$ piece.*

### Scope and proof status

*The boxed identity is the iterated form of
[`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md);
its proof is the $(Z+N-1)$-fold iteration of the two-factor Wenzl 1988
branching identity, with each iteration using Hoefsmit 1974 seminormal
matrix elements for the new boundary generator. The two-factor case
is verified to $\sim 10^{-15}$ relative precision across all
$11$ partitions $\lambda \vdash 6$ for the deuteron interface
$I = \sigma_2 - \tfrac{1}{2}(q - q^{-1}) \mathbf{1}$
(`sublemma-2-1-A-operator-extract.witness.json`). The $k$-factor
extension is structurally identical: each iteration adds one boundary
generator's worth of LR multiplicities, and the same trace-formula
algebra applies.*

*The connection to the **mass-endomorphism tower** (the bridge claim of
this proposition) is **conditional** on:*

1. *the iterated $A^\lambda_{\vec\mu}(I)$ matrix entries being
   computable for $\lambda \vdash 3A$ with $A \geq 4$ (currently
   verified for $\lambda \vdash 6$, deuteron case);*
2. *the operator-valued mass formula reproducing the $0.18\%$
   accuracy of the scalar single-gen piece at $A = 1\ldots 3$ where
   the scalar formula is empirically validated;*
3. *the operator's off-diagonal residual closing the
   $\rho_K^{\text{pair-gen}}$ open piece without introducing new
   calibration constants.*

*All three are **falsifiable** at the witness level — see the
follow-up sweep below.*

### Falsification path

*Reproduce the per-atom $m_p / m_e \approx 1836$ prediction (currently
$1869$ from scalar Faddeev $\Phi_q$, or $3.31$ from naive scalar Li_2^q)
under the operator-valued formula above on the proton's
$\mathcal{B}_3 \times \mathfrak{u}\mathfrak{u}\mathfrak{d}$ canonical
braid:*

1. *Compute $A^\lambda_{\mu}(I)$ matrix entries for all $11$ partitions
   $\lambda \vdash 3 = (Z+N) = 1$ (trivial — $I = \mathbf{1}$, so
   $A = \mathrm{id}$);*
2. *Sum the per-block traces with their $\tilde w_\lambda$ weights and
   $\dim_q V_\lambda$ multipliers;*
3. *Take the magnitude and apply the post-$\tau$ archimedean
   evaluation at $q_0 = 1.109978595554181\ldots$ (50 dps);*
4. *Compare to CODATA $m_p / m_e = 1836.152$.*

*If the operator-valued formula gives $m_p / m_e \in [1830, 1845]$
(< 0.5% error, matching the current scalar Faddeev's $1.84\%$
or better), the operator-valued framework is **validated** as the
correct Stage-1 unblock and $\Phi_q$ can be retired in favour of the
operator trace. If it gives $m_p / m_e$ far from $1836$, additional
structural content beyond the boundary-generator operator is required
(the next candidate would be off-shell propagator contributions per
[`conj:depth-stratified-frobenius-reciprocity`](depth-stratified-frobenius-reciprocity.md)).*

### Status

**Proven (boxed identity)** at the two-factor case via
[`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md);
forward-validated on the canonical deuteron at all 11 partitions
$\lambda \vdash 6$ to ~$10^{-15}$ relative residual
(`mass-tower-operator-valued.witness.json`, all assertions passed).

**Proven at the three-factor (A=3) case** via the SYT-branching-basis
approach of `sublemma_2_1_h9_branching_basis.py`
(witness `sublemma-2-1-h9-tritium-branching-verify.witness.json`,
assertion `all_lambda_path_a_eq_path_b_machine_eps` passes across all
30 $\lambda \vdash 9$): direct $\chi^\lambda(\beta_T)$ at H_9 equals
the iterated Path-B trace
$\sum_{(\xi, \nu)} \mathrm{Tr}(P_{(\xi,\nu)} \cdot \rho_\lambda(\beta_T))$
to machine $\varepsilon$ for every $\lambda \vdash 9$, where
$(\xi, \nu)$ ranges over the iterated $H_6 \times H_3$ Wedderburn
blocks. This validates the iterated boxed identity at $k = Z+N = 3$
for tritium (Z=1, N=2). The corresponding ${}^3$He (Z=2, N=1) case
follows by the same algorithm with a different nucleon braid.

**Open** for $k \geq 4$ (the ${}^4$He case at H_12): the iterated
branching basis approach scales to H_12 in principle
(`sublemma_2_1_h12_he4_branching.py` is in place) but is memory- and
time-bounded; closure pending.

**Open** for the bridge claim from the boxed identity to a CONCRETE
mass prediction under the operator-valued tower — the operator-trace
formula gives the same numerical $\chi^\lambda$ as direct evaluation
(since both compute the same character), so the structural mass
prediction only differs from the scalar case if a NEW formula
(e.g. taking the LOG of the operator trace separately per (μ, ν)
block, rather than per λ) is wired in. That formula change is the
remaining Stage-1 unblock, tracked under
[`docs/coordination/1ppb-categorical-chain.md`](https://github.com/litlfred/qou/blob/main/docs/coordination/1ppb-categorical-chain.md)
"Stage-1 blocker entry".

### Lean formalisation

The Lean file
[`qou:QOU.BraidKnot.MassTowerOperatorValued`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/mass-tower-operator-valued.lean)
axiomatises the operator $A^\lambda_{\vec\mu}(I)$ as a class with the
Wenzl-branching field and the LR-collapse field. The boxed identity
is a conditional theorem (AGENTS.md §3b-cond pattern) taking the class
as an explicit `[Instance]` hypothesis; the conditional statement is
fully verified by Lean modulo the class instance.
