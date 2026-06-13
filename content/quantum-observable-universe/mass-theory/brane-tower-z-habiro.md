The [mass-endomorphism conjecture](#conj:mass-endomorphism) states that
the Hecke mass element $\Phi_{\mathrm{mass}}$ admits a closed-form NF
decomposition. Its **transient (brane-tower) component** is the sum

$$
  \Phi_{\mathrm{mass}}^{\mathrm{trans}}(\beta)
  \;=\;
  \sum_{i=1}^{N} \Phi_q(z_i),
$$

where $z_i = |\hat{V}_i|$ are the per-generator algebraic-volume
magnitudes from
[algebraic quantum volume](#def:algebraic-quantum-volume) and
$\Phi_q$ is the [quantum dilogarithm](#cor:quantum-dilogarithm).

For low isotopes $\{D, T, {}^3\mathrm{He}\}$, the per-generator
volumes satisfy $z_i \in [0.85, 1.0]$ — just below the first pole of
$\Phi_q$ at $z = q_0 \approx 1.11$. Numerically
$\Phi_q(0.989) \approx 6.7 \times 10^5$ and $\Phi_q(1) \approx 9 \times 10^5$,
so each summand is enormous and the analytic brane tower dominates the
mass formula by orders of magnitude beyond the empirical AME binding.

Two regularizations have been documented but neither uniformly closes
the gap (see [mass-endomorphism conjecture §"Two distinct convergence problems"](#conj:mass-endomorphism)):

1. **Yekutieli truncation** at GB filtration depth $k_{\max}$ — works
   for $D$ ($k_{\max}=2$, error $\sim 22\%$), grossly fails for $T$
   ($k_{\max}=9$, error $\sim 17000\%$). Empirical, not structural.
2. **$q$-Habiro completion** (the
   [Habiro ring](#def:habiro-ring) at $((q;q)_n)$) — regularizes in
   the variable $q$, not $z$. Does not change the analytic value of
   $\Phi_q$ at fixed $z$. The $q$-side termination
   ([atomic Habiro expansion](#cor:habiro-expansion-atomic), proved:
   $m_{\max} \leq \lceil\sqrt{2 \deg p}\rceil$) is the q-analog of
   the parallel claim conjectured for $z$ below.

## Statement

**Conjecture (brane tower in $z$-Habiro).**

*Let $\mathfrak{H}$ be a confined particle/atom with per-generator
volumes $\{\hat{V}_i(q)\}_{i=1}^{N}$ in
$\mathbb{Z}[q^{\pm 1/2}]$. The brane-tower partial sums*

$$
  \widetilde{\Phi}^{(N)}(\beta)
  \;:=\;
  \sum_{i=1}^{N}
    \mathrm{Trunc}_{<n}\!\bigl[\Phi_q(\hat{V}_i)\bigr]
  \;\in\;
  \mathbb{Z}[q^{\pm 1}][z] / (P_n(q, z))
$$

*(where $\mathrm{Trunc}_{<n}$ takes the unique representative of
degree $< n$ in $z$ in the cyclotomic-in-$z$ quotient)
form a Cauchy sequence in the* $z$*-Habiro topology
([$z$-Habiro ring](#def:z-habiro-ring)) **as $N$ varies**. Their limit*

$$
  \widetilde{\Phi}_q^{\mathrm{tower}}(\beta)
  \;\in\;
  \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z
$$

*exists as an algebraic element — well-defined purely algebraically,
with no analytic regularization required.*

*Furthermore, there exists a **canonical level-selection rule***

$$
  n_\star \;:\; \{\text{confined particles}\} \;\longrightarrow\;
  \mathbb{N}_{\geq 1},
  \qquad
  \mathfrak{H} \;\longmapsto\; n_\star(\mathfrak{H}),
$$

*derivable from QOU substrate data alone (e.g. confinement level
$\ell$, strand count $n_0$, GB filtration on $H_{n_0}(q)$,
or analogous structural invariants), such that the cyclotomic
projection*

$$
  \pi_{n_\star(\mathfrak{H})}^{(z)}\!\bigl(\widetilde{\Phi}_q^{\mathrm{tower}}(\beta_\mathfrak{H})\bigr)
$$

*evaluated at $q = q_0$ and $z = z_i$ recovers the empirical brane-tower
contribution to the binding $B(\mathfrak{H})$ uniformly across atoms,
not just for the single atom whose GB filtration depth happens to
match.*

## What this conjecture would buy

If true, the conjecture:

1. **Replaces the analytic infinite product** $\Phi_q(z)$ — which has
   no algebraic home and blows up at $|z| \to q$ — with an algebraic
   element of $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$.
2. **Promotes Yekutieli truncation** from an ad-hoc cutoff at GB depth
   to a **structural cyclotomic projection** at a canonical level.
3. **Predicts the level-selection rule** $n_\star$ structurally — the
   single open computation reduces from "find the right Φ_q
   regularization" to "identify $n_\star$ from substrate data".

## The open part: $n_\star$

The level-selection rule $n_\star$ is **the open part**. Candidate
structural inputs:

See [Table 1](#tbl:brane-tower-z-habiro-table1-data).

A correct $n_\star$ must (i) be a structural invariant of
$\mathfrak{H}$, (ii) reproduce the empirical $B(\mathfrak{H})$ across
atoms when fed into $\pi_{n_\star}^{(z)}$, and (iii) be derivable from
the QOU substrate without external calibration.

**Empirical observation (uniform-$k$ sweep).** A
uniform-depth probe
([`probe_phiq_uniform_k.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/folio-assistant/computations/probe_phiq_uniform_k.py))
sweeping $k \in \{1, 2, 3, 4, 5, 6, 8, 10\}$ uniformly across
$\{D, T, {}^3\mathrm{He}\}$ shows:

1. **The absolute formula** $B = m_e \cdot \rho \cdot (\mathrm{tr}_M(T_w) + \mathrm{tower}^{(k)} + \sigma_{3A})$
   overshoots at every uniform $k$ — errors grow monotonically with
   $k$ ($+775\%$ at $k=1$, $+1.27 \times 10^6\,\%$ at $k=10$). No
   uniform absolute-form $k$ closes the gap.

2. **The subtractive form** $B = E_0 \cdot (\mathrm{tower}_{\mathrm{free}}^{(k)} - \mathrm{tower}_{\mathrm{atom}}^{(k)})$
   has a **sign-flip at $k = 2$**: for all three atoms,
   $\Delta\mathrm{tower}^{(k=1)} < 0$ but $\Delta\mathrm{tower}^{(k \geq 2)} > 0$.
   At $k = 2$:
   $B(D) \approx +1.74\,\mathrm{MeV}$ (err $-22\%$),
   $B(T) \approx +5.18\,\mathrm{MeV}$ (err $-39\%$),
   $B({}^3\mathrm{He}) \approx +18.05\,\mathrm{MeV}$ (err $+134\%$).

3. **${}^3\mathrm{He}$ overshoots at every $k \geq 2$ in subtractive
   form**, suggesting the per-generator volume list for ${}^3\mathrm{He}$
   carries a doubled $|\hat{V}| \approx 0.989$ contribution that the
   subtractive cancellation does not absorb. This is consistent with
   ${}^3\mathrm{He}$'s 8-generator list having two near-pole entries
   (positions 0 and 3), versus $D$'s single near-pole entry.

The sign-flip at $k = 2$ is structurally interesting: it is the
smallest depth that includes the **Hecke quadratic relation slice**
($\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, two factors of $\Phi_q$).
This may indicate that the correct $n_\star$ rule depends not only on
filtration depth but also on how the per-generator volume list
**multiplicities** interact with the cyclotomic projection — a refined
form of the conjecture would need to fold per-generator-volume
multiplicity into $n_\star$.

## Relation to the $q$-Habiro picture

The two completions are **independent**:

See [Table 2](#tbl:brane-tower-z-habiro-table2-data).

The full picture would be a **bicompletion**
$\widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}$ at the bigraded ideal
generated by both $(q;q)_n$ and $P_n(q,z)$, in which the colored Jones
data and the brane-tower data coexist as a single algebraic object.
Construction of the bicompletion is open.

## Falsifiability

The conjecture is **falsifiable** by computation:

1. Pick a candidate $n_\star$ rule (one of the rows above, or a
   combination).
2. Compute $\pi_{n_\star(\mathfrak{H})}^{(z)}(\widetilde{\Phi}^{(N)})$
   at $q_0$ for each isotope in the AME light-isotope sample
   $\{D, T, {}^3\mathrm{He}\}$.
3. Form $B(\mathfrak{H}) = m_e \cdot \rho \cdot (\mathrm{tr}_M(T_w) + \mathrm{tower}(\mathfrak{H}) + \sigma_{3A})|_{q_0}$.
4. Compare with the AME values $\{2.224566, 8.481798, 7.71806\}$ MeV.

A candidate $n_\star$ rule that closes all three to within $\sim 5\%$
**without per-atom retuning** is the empirical signature that
$n_\star$ has been correctly identified. A rule that requires
per-atom retuning is structurally equivalent to Yekutieli's $k_{\max}$
and does not constitute progress.

## Closure: scalar-eigenvalue form of $n_\star$ is refuted

**Scope of this section.** "Scalar-eigenvalue" means **both** that
the candidate $n_\star$ is a function of scalar substrate invariants
of a single confined particle, **and** that the truncated quantum
dilogarithm $\Phi_q^{[\leq n_\star]}$ is evaluated on a **scalar
argument** (the per-generator algebraic volume $|\hat{V}_i|$). These
two assumptions together collapse the Wedderburn decomposition of
$H_{3A}(q_0)$ onto its 1-D eigenvalues; higher partitions $\lambda$
contribute only through scalar reductions. The strictly-stronger
**operator-valued** (Wedderburn-block, convolution-aware via
$\chi^\lambda_q(\beta)$) form is probed separately in the next
section.

The level-selection part of this conjecture asserted the existence of
an $n_\star$ derivable **from QOU substrate data alone** — a function
of scalar substrate invariants of a single confined particle, without
per-atom retuning. Every scalar candidate in the table above has now
been probed against the AME light-isotope sample, and **all fail by
the conjecture's own falsifiability criterion**:

See [Table 3](#tbl:brane-tower-z-habiro-table3-data).

These three witnesses together cover every scalar invariant in the
candidate table (GB max grade, confinement level $\ell$, strand count
$n_0 = 3A$, Coxeter length $\ell(w)$, and the leading additive
combination $\ell n_0 + k$).

**Theorem (scalar-eigenvalue $n_\star$ refutation).** *Let
$n_\star : \mathfrak{H} \mapsto \mathbb{N}_{\geq 1}$ be any rule
constructed from the candidate scalar substrate invariants
$(\ell, n_0, k, \ell(w))$, and let $\Phi_q^{[\leq n_\star]}$ be
evaluated on the scalar per-generator volumes $|\hat{V}_i|$ — without
per-atom retuning. Then the cyclotomic projection
$\pi_{n_\star(\mathfrak{H})}^{(z)}\!\bigl(\widetilde{\Phi}_q^{\mathrm{tower}}(\beta_\mathfrak{H})\bigr)$,
evaluated at $(q_0, z_i)$ into the binding formula
$B(\mathfrak{H}) = m_e \cdot \rho \cdot (\mathrm{tr}_M(T_w) + \mathrm{tower}(\mathfrak{H}) + \sigma_{3A})$,
produces an error exceeding $100\%$ on at least one of
$\{D, T, {}^3\mathrm{He}\}$.*

*Proof.* Direct numerical evaluation, recorded in the three witnesses
above. The uniform-$k$ sweep covers every scalar invariant up to
monotone reparameterization (the empirical error grows monotonically
with $k$ outside the narrow $k = 2$ window); the per-atom probe rules
out the additive combination $\ell n_0 + k$. All three exceed $100\%$
error on at least one isotope, far outside the $\sim 5\%$
empirical-confirmation threshold. $\square$

By the conjecture's own criterion, the **scalar-eigenvalue form** of
the $n_\star$ existence claim is therefore **refuted**.

## Operator-valued probe: per-eigenvalue form also refuted

A natural objection to the closure above is: **the scalar form
collapses $\Phi_q$ onto 1-D eigenvalues**. Hecke irreps $V_\lambda$
for $\lambda \vdash 3A$ are mostly higher-dimensional, and the
braid operator $\rho(\beta_\mathfrak{H}) \in H_{3A}(q)$ acts on each
irrep via R-matrix **convolution**, not a per-generator scalar
product. The conjecture's $n_\star$ existence claim might survive
when $\Phi_q$ is promoted to the canonical operator-valued form.

This section reports the **canonical operator-valued probe** —
$\Phi_q$ applied **per eigenvalue** of $\rho_\lambda(\beta)$ in
each Hecke irrep $V_\lambda$, summed via the operator trace, then
Wedderburn-weighted by signed $y_\lambda$:

$$
  \mathrm{tower}_{\mathrm{op}}^{(k)}(\beta_\mathfrak{H})
  \;:=\;
  \Biggl|\,
  \sum_{\lambda \vdash 3A} \;
    y_\lambda(q_0) \cdot
    \mathrm{tr}_\lambda\!\Bigl(
      \Phi_q^{[\leq k]}\bigl(\rho_\lambda(\beta_\mathfrak{H})\bigr)
    \Bigr)
  \,\Biggr|
  \;=\;
  \Biggl|\,
  \sum_\lambda y_\lambda(q_0) \cdot
    \sum_{a=1}^{\dim V_\lambda}
      \Phi_q^{[\leq k]}\!\bigl(\mu_a^{(\lambda)}\bigr)
  \,\Biggr|,
$$

where $\mu_a^{(\lambda)}$ are the eigenvalues of $\rho_\lambda(\beta)$
(complex, in general) and $\Phi_q^{[\leq k]}$ extends to a complex
argument as the finite product $\prod_{j=1}^{k}(1 - q^{-j}\mu)^{-1}$.
The implementation is
[`probe_phiq_operator_valued.py`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe_phiq_operator_valued.py)
([witness](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe-phiq-operator-valued.witness.json));
it builds $\rho_\lambda(\beta)$ numerically from Hoefsmit seminormal
matrices at $q_0$, computes eigenvalues via `numpy.linalg.eigvals`,
applies $\Phi_q$ per eigenvalue, sums as the operator trace, and
Wedderburn-weights with signed $y_\lambda(q_0)$ from the canonical
Jones-Markov machinery
([`wedderburn_jones_markov.y_lambda_at`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/wedderburn_jones_markov.py)).

**Three normalization properties handled correctly** (vs the earlier
[`_avg_chi_over_classical_dim`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe_phiq_avg_chi_over_classical_dim.py)
variant, which used approximations on all three):

1. **No per-irrep dimension denominator.** Replaced by the operator
   trace $\mathrm{tr}_\lambda$ — classical-vs-quantum-dim question
   resolved structurally.
2. **Signed character throughout.** Complex Φ_q evaluation; final
   $|\cdot|$ only at the binding-formula level.
3. **Per-eigenvalue $\Phi_q$.** Applied to each $\mu_a^{(\lambda)}$
   separately rather than to the per-irrep mean.

### Result — per-eigenvalue operator form is also refuted

See [Table 4](#tbl:brane-tower-z-habiro-table4-data).

**Notable structural finding.** Two of three atoms find their
*own* near-AME uniform $k$ under the per-eigenvalue form —
**deuteron at $k = 1$ lands at $-6.87\%$** and **tritium at $k = 2$
lands at $-8.00\%$**, both within $10\%$ of the AME value. But
${}^3\mathrm{He}$ never gets within $50\%$ at any uniform $k$ in
$\{1, \ldots, 10\}$ — and the (D, T) sweet spots are at *different*
$k$ values, so **no single uniform $k$ closes all three**.

**Theorem (per-eigenvalue operator $n_\star$ refutation).** *Under
the canonical operator-valued promotion above, for every
$k \in \{1, 2, 3, 4, 5, 6, 8, 10\}$, the tower
$\mathrm{tower}_{\mathrm{op}}^{(k)}$ substituted into the binding
formula produces an error exceeding the falsifiability threshold on
at least one of $\{D, T, {}^3\mathrm{He}\}$.* The Lean form is
[`witness_refutes_per_eigenvalue_operator_form`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.lean)
in the sibling `.lean`.

By the conjecture's own criterion (no per-atom retuning), the
**operator-valued form** of the $n_\star$ existence claim is
therefore also **refuted**.

### Reading of the (D, T) per-atom sweet spots

The fact that $D$ and $T$ each find their own near-AME uniform $k$
($k = 1$ for $D$, $k = 2$ for $T$) under the canonical
operator-valued form is structurally informative but **does not
support the conjecture**: per-atom $k$ values are exactly what
`conj:brane-level-selection` tried
to predict via $n_\star = \ell \cdot n_0 + k$, and the conjecture
explicitly rules out per-atom retuning as the empirical signature
of correctness. The result is consistent with the refuted
$\ell n_0 + k$ formula being approximately right for $D$ and $T$
but missing a doubled-near-pole correction for ${}^3\mathrm{He}$ —
the same multiplicity signature flagged in the scalar-form closure
above.

### What survives the closure

The conjecture has two independent claims:

1. **Algebraic Cauchy-limit claim** —
   $\widetilde{\Phi}_q^{\mathrm{tower}}(\beta)$ exists as a Cauchy
   limit in the $z$-Habiro topology. **Untouched by any of the
   witnesses and remains open.** A direct algebraic proof would
   proceed via the cyclotomic projections $\pi_n^{(z)}$ on the
   $z$-Habiro ring ([$z$-Habiro ring](#def:z-habiro-ring)) and does
   not depend on $n_\star$.

2. **$n_\star$ existence claim** — refuted across every empirically
   probed form:
   - Scalar-eigenvalue family (§"Closure"): **refuted**.
   - Operator-valued per-eigenvalue family (§"Operator-valued
     probe"): **refuted**. The canonical convolution-aware
     promotion fails the falsifiability criterion at every uniform
     $k$, even though $D$ and $T$ individually find near-AME values
     at different $k$ (per-atom retuning is excluded).
   - Multiplicity-refined scalar family: **open** (this section's
     final §).

A historical Wedderburn-block-average variant
([`probe_phiq_avg_chi_over_classical_dim.py`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe_phiq_avg_chi_over_classical_dim.py))
that used three approximations — classical $\dim V_\lambda$,
$|\chi^\lambda|$ (abs), mean-of-eigenvalues — is preserved for
audit purposes but superseded by the per-eigenvalue probe; its
witness is
[`probe-phiq-avg-chi-over-classical-dim.witness.json`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe-phiq-avg-chi-over-classical-dim.witness.json).

### Multiplicity / Type-B-fold probe: also refuted

The (D, T) per-atom sweet spots under the operator-valued form
($k = 1$ for D, $k = 2$ for T) and the ${}^3\mathrm{He}$ holdout at
every $k$ pointed at the **multiplicity-refined** form as the
surviving open thread. That probe is now done.

**Probe.**
[`probe_phiq_multiplicity_refined.py`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe_phiq_multiplicity_refined.py)
([witness](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe-phiq-multiplicity-refined.witness.json))
tests four substrate-derived per-atom rules built from the
per-generator near-pole multiplicity $m_{\max}(\mathfrak{H})$ and the
Type-B-folded-crystal structure of $H_{3A}(q_0)$ (CLAUDE.md §7b):

See [Table 5](#tbl:brane-tower-z-habiro-table5-data).

with $\lambda_\star^D = (3,2,1)$, $\lambda_\star^T = \lambda_\star^{{}^3\mathrm{He}} = (3,3,3)$;
near-pole multiplicities (band $\varepsilon = 0.15$) $m_{\max}^D = 3$,
$m_{\max}^T = 4$, $m_{\max}^{{}^3\mathrm{He}} = 5$.

Each rule was evaluated in both the scalar tower and the
per-eigenvalue operator-valued tower (using the spectra persisted in
[`probe-phiq-operator-valued.witness.json`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe-phiq-operator-valued.witness.json)).

### Result — refuted, but with structural finding worth recording

See [Table 6](#tbl:brane-tower-z-habiro-table6-data).

**No rule closes uniformly** — the conjecture's $n_\star$ existence
claim is refuted across every probed family.

**Structural finding worth recording.** The R2 rule
$n_\star = \max(1, \lfloor k_{\mathrm{Hecke}} / m_{\max} \rfloor)$,
under the per-eigenvalue operator-valued form, **correctly identifies
the per-atom optimal truncation depth from substrate data alone for
$D$ and $T$**:

- $D$: substrate gives $n_\star^D = \lfloor 2/3 \rfloor \to \max(1,0) = 1$;
  operator-valued $\Phi_q^{[\leq 1]}$ tower closes $D$ to $-6.87\%$.
- $T$: substrate gives $n_\star^T = \lfloor 9/4 \rfloor = 2$;
  operator-valued $\Phi_q^{[\leq 2]}$ tower closes $T$ to $-8.00\%$.
- ${}^3\mathrm{He}$: substrate gives $n_\star^{{}^3\mathrm{He}} = \lfloor 2/5 \rfloor \to \max(1,0) = 1$;
  $-55.97\%$ residual.

So **the structural blocker is the ${}^3\mathrm{He}$ gap itself, not
the choice of $n_\star$**. No per-atom truncation depth — substrate-
derived or otherwise — closes the ${}^3\mathrm{He}$ binding. The
remaining open question shifts away from $n_\star$:

> *What additional structural contribution to the ${}^3\mathrm{He}$
> mass formula is missing? Two natural candidates:*
> - *Markov-trace error: is $\mathrm{tr}_M(\beta_{{}^3\mathrm{He}})$
>   itself under- or over-counted by ~7 MeV against the empirical
>   value? (cross-check via mass-table audits and the ρ_K assembly
>   path in [#564](https://github.com/litlfred/qou/pull/564)).*
> - *Substrate-parameter inconsistency: is $q_0 \approx 1.110$
>   calibrated against observables for which ${}^3\mathrm{He}$
>   sits at a special locus (e.g. 3-strand $A = 3$ braid structure
>   coinciding with the cyclotomic $q^9 = 1$ branch cut)?*

The Lean form
[`witness_refutes_multiplicity_and_type_b_forms`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.lean)
records the refutation at the falsifiability threshold using the
best-rule max error ($56.0\%$ on R2-op).

## Pair-knot magic-shell probe: partial closure with LP dual confirmation

The (D, T) per-atom sweet spots and ${}^{3}$He holdout under the
operator-valued form (§"Operator-valued probe") plus the refuted
multiplicity / Type-B-fold candidates above point at a deeper
structural reformulation: **for magic-shell nuclei the brane-tower's
per-generator decomposition is too fine — the closed shell should
contribute as a single composite knot operator** (the Hopf-linked
sub-knot of the magic nucleon pair), not as a sum of 4 separate
$\Phi_q(|\hat V_i|)$ contributions.

The per-generator magnitudes make the structure visible:

See [Table 7](#tbl:brane-tower-z-habiro-table7-data).

${}^{3}$He has Z=2 magic $\to$ **duplicated intra-p block** at positions
{0,1} and {3,4}; ${}^{4}$He is doubly magic (Z=N=2) $\to$ both intra-p and
intra-n blocks duplicated.

### Pair-knot composite operator + LP-dual confirmation

[`probe_phiq_pair_knot_magic_shell.py`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe_phiq_pair_knot_magic_shell.py)
([witness](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe-phiq-pair-knot-magic-shell.witness.json))
replaces each magic-shell intra-block by a single composite term
$\Phi_q(|\hat V_{\text{shell}}|)$ with
$|\hat V_{\text{shell}}| = \prod_{i \in \text{shell}} |\hat V_i|$
(Hopf-link convention), and **confirms the pair-knot operator
structurally via the operator-selection LP dual** per
[`prop:operator-selection-lp`](#prop:operator-selection-lp) and
CLAUDE.md "LP / SDP duals — first-class infra":

- Operator basis $\{\sigma_i \;(\text{per-generator}),\;\sigma_{pp},\;\sigma_{nn}\}$
  built per atom, cost vector $t_i = |\hat V_i|$, diagonal Frobenius
  Gram $G_{ij} = \delta_{ij} |\hat V_i|^2$ as a tractable
  approximation (full $\mathrm{tr}_M(\sigma_i \sigma_j)$ from
  Hoefsmit seminormal is a refinement).
- Operator-selection LP solved via
  [`lp_dual_solver.solve_operator_selection_lp`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/lp_dual_solver.py).
- **Strong duality verified** (gap = 0 to numerical precision) for
  all four atoms.

### LP-dual structural result: pair-knot operators ARE selected at closed shells

See [Table 8](#tbl:brane-tower-z-habiro-table8-data).

The LP dual confirms the pair-knot composites $\sigma_{pp}, \sigma_{nn}$
are **structurally distinguishable from per-generator operators at
exactly the magic configurations** — and absent from D's active set,
which has no magic shell. This is the operator-level signature of
$Z=2$ / $N=2$ shell closure showing up in the substrate algebra.

### Empirical closure result: partial — pair-knot collapse alone doesn't suffice

See [Table 9](#tbl:brane-tower-z-habiro-table9-data).

${}^{4}$He at $-19.4\%$ is the closest any probed form has come to a uniform
closure (any atom, any rule). But pair-knot collapse alone does not
close the AME light-isotope sample uniformly.

### Magic-shell correction calibration: $Z{=}2$ / $N{=}2$ symmetry fails

Calibrating $\Delta_{\text{shell}}$ from the residuals under
paired tower:

- $\Delta_{\text{shell}}(Z{=}2) = B_{\text{AME}}(^3\mathrm{He}) - B_{\text{paired}}(^3\mathrm{He}) = -16.88$ MeV
- $\Delta_{\text{shell}}(N{=}2) = B_{\text{AME}}(^4\mathrm{He}) - B_{\text{paired}}(^4\mathrm{He}) - \Delta_{\text{shell}}(Z{=}2) = +22.38$ MeV

The $Z{=}2$ / $N{=}2$ symmetry fails: the two extracted
corrections have **opposite signs** and differ in magnitude by a
factor of $1.326\times$. A doubly-magic-symmetry assumption
$\Delta_{\text{shell}}(N{=}2) = \Delta_{\text{shell}}(Z{=}2)$
gives the wrong sign on ${}^{4}$He (predicted $-11$ MeV vs AME $+28.3$
MeV, $-139\%$ error).

### Pair-knot magic-shell probe

The pair-knot magic-shell probe **partially supports the structural
diagnosis but does not close the conjecture**:

- **Pair-knot operators ARE structurally privileged at closed
  shells** (LP-dual confirmed via strong duality with non-trivial
  shadow prices on $\sigma_{pp}, \sigma_{nn}$ at magic atoms).
- **Pair-knot collapse alone does not close the gap uniformly**;
  ${}^{3}$He still at $+219\%$, ${}^{4}$He at $-19.4\%$.
- **Magic-shell correction does not respect $Z{=}2$ / $N{=}2$
  symmetry** under the simple product-volume convention.

This refutes the simple pair-knot-product-volume conjecture as
formulated but identifies a real structural feature (the LP-dual
active-set distinction between magic and non-magic atoms) that
points at the right direction for a refined formulation — pursued
in the next section.

The Lean form
[`witness_refutes_pair_knot_product_volume_form`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.lean)
records the refutation of this specific (simplest) pair-knot
convention; the structural finding (LP-dual selection of pair-knot
operators) is recorded as `def lpDualActiveSetIncludesPairKnotAtMagicShells` for downstream use.

## Pair-knot Markov-trace refinement: also refuted, $Z\leftrightarrow N$ symmetry restored

The LP-dual evidence from the product-volume probe pointed at the
canonical refinement: replace
$|\hat V_{\text{shell}}| = \prod_{i} |\hat V_i|$ by the actual
Markov trace $\mathrm{tr}_M(\sigma_{i_1} \cdots \sigma_{i_k})$ of the
shell sub-braid as a single Hecke-algebra element via Hoefsmit
seminormal at $q_0$, AND use the full Frobenius Gram
$G_{ij} = \mathrm{tr}_M(\sigma_i \sigma_j)$ in the LP, AND confirm
via the SDP lift (cvxpy / SCS) per CLAUDE.md "LP / SDP duals —
first-class infra".

The refined probe
[`probe_phiq_pair_knot_markov_trace.py`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe_phiq_pair_knot_markov_trace.py)
([witness](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/folio-assistant/computations/probe-phiq-pair-knot-markov-trace.witness.json))
implements all three.  Scope: $D, T, {}^3\mathrm{He}$ (${}^{4}$He n=12
seminormal compute ~10 min, deferred).

### Result — refined pair-knot Markov-trace form also refuted

See [Table 10](#tbl:brane-tower-z-habiro-table10-data).

LP+SDP both confirm strong duality (LP gap $< 10^{-15}$, SDP gap
$< 10^{-6}$ via cvxpy/SCS) at the full Frobenius Gram.  Refined
pair-knot Markov-trace tower **does not close** the AME light-isotope
sample.

### Positive structural finding — $Z \leftrightarrow N$ isospin symmetry restored

$$
  \mathrm{tr}_M(\sigma_{pp}) \;=\; \mathrm{tr}_M(\sigma_{nn})
  \;=\; 0.0622 \quad (\text{exactly})
$$

The two magic-shell sub-braids are **isomorphic Hecke elements**
(four intra-strand generators each with identical Hecke quadratic
structure), so the Markov-trace gives the same value for both.  The
$1.326\times$ ratio in family 5's $\Delta_{\text{shell}}$
calibration ($Z{=}2$ vs $N{=}2$) was a **product-volume artifact**,
not a real symmetry breaking.  At the canonical Markov-trace
operator-volume level, $Z \leftrightarrow N$ isospin symmetry
holds exactly.

### Structural conclusion (closes the level-selection question)

The brane-tower formula's $\Phi_q$-truncated tower at **any**
operator-volume convention probed (product, geometric mean, OR
canonical Markov trace) overshoots at the AME light-isotope scale.
The ${}^{3}$He gap is **not** an operator-volume choice issue — it is a
structural deficit of the brane-tower formula itself at the
$A{=}3$ / $n_0{=}9$ regime.

This closes the level-selection question for `conj:brane-tower-z-habiro`:
no `n_⋆` choice and no operator-volume refinement we have probed
recovers the AME light-isotope binding uniformly.  The surviving
open paths are recorded in §"What survives the closure" above (the
algebraic Cauchy-limit half, and the ${}^{3}$He structural-gap branch).

The Lean form
[`witness_refutes_pair_knot_markov_trace_form`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.lean)
records this refutation; the combined `nStar_all_probed_forms_refuted`
now covers **six** probed families:

1. Scalar uniform-$k$
2. Scalar $\ell \cdot n_0 + k$
3. Per-eigenvalue operator-valued
4. Multiplicity / Type-B-folded-crystal
5. Pair-knot product-volume
6. Pair-knot Markov-trace + full Gram + SDP

Full consolidation in
[`docs/audits/-brane-tower-n_star-closure-audit.md`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/docs/audits/-brane-tower-n_star-closure-audit.md).

## Multiplicity / Type-B-fold probe: also refuted

The empirical support for promoting $\mathbf{m}$ to a first-class
input comes from two converging signals:

- **Scalar-form $k = 2$ subtractive** gives $\{-22\%, -39\%, +134\%\}$
  for $\{D, T, {}^3\mathrm{He}\}$ — ${}^3\mathrm{He}$ overshoots
  because its 8-generator list carries **two** near-pole entries
  ($|\hat{V}| \approx 0.989$ at positions $0$ and $3$) versus
  $D/T$'s **single** near-pole entry.
- **Per-eigenvalue operator form** gives $D$ closure at $k = 1$
  ($-6.87\%$), $T$ closure at $k = 2$ ($-8.00\%$), but
  ${}^3\mathrm{He}$ failure at every $k$ — same underlying
  multiplicity asymmetry showing up as a *uniform-$k$-non-closability*
  rather than as overshoot.

Both witnesses point to per-generator near-pole multiplicity as the
missing structural input.

The block kind remains `conjecture` because the algebraic and the
multiplicity-refined parts are still open. The sibling
[`brane-tower-z-habiro.lean`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.lean)
records all three refutations as explicit theorems driven by the
witness data (`witness_refutes_scalar_uniform_k_form`,
`witness_refutes_scalar_ell_n0_k_form`,
`witness_refutes_per_eigenvalue_operator_form`, combined as
`nStar_all_probed_forms_refuted`); the conditional class
`BraneTowerZHabiro` is kept for downstream conditional results that
ride on the surviving algebraic claim.

## Per-partition $k_\lambda$ refinement (sibling )

['s `per-partition-k-lambda-rule.md`](https://github.com/litlfred/qou/pull/639)
sharpens the closure direction beyond the multiplicity-refined
scalar form: the failure of uniform-$k$ in the per-eigenvalue
operator form is dominated by **one specific partition per atom**:

See [Table 11](#tbl:brane-tower-z-habiro-table11-data).

Re-assigning $k_\lambda = 1$ for the dominant partition while
keeping $k_\lambda = 2$ elsewhere collapses each atom's tower
magnitude below 2.  The surviving sharpened open form is
**per-partition** $k_\lambda$: there should exist a substrate-
derivable map $k_\lambda : \{\text{partitions of } 3A\} \to \mathbb{N}_{\geq 1}$
producing AME closure under non-uniform Wedderburn-block
truncation.

This is consistent with the magic-shell pair-knot finding of this
PR: $\sigma_{pp}, \sigma_{nn}$ activate distinct partitions (the
Type-B-fixed locus) under the LP-dual, which is the natural home
of a per-partition $k_\lambda$ rule.  The two refinements
(per-partition $k_\lambda$ from #639 + magic-shell $\Delta_{\text{shell}}$
from `conj:magic-shell-stabilization`)
target different layers: per-partition $k_\lambda$ regulates the
$\Phi_q$ tower; magic-shell $\Delta_{\text{shell}}$ is the
non-tower structural term.  Both are open.
