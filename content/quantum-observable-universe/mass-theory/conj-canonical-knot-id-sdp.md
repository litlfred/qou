The canonical Hecke elements $T_w$ for the light nuclei
$^2\mathrm{H}$ (deuterium), $^3\mathrm{H}$ (tritium), and
$^3\mathrm{He}$ (helium-3) were historically identified by matching
their hyperbolic volumes to AME binding energies.  This conjecture
states that the joint mass-tower confinement SDP
([prop:confinement-sdp](#prop:confinement-sdp)) uniquely selects
the same Hecke elements from first principles.

## Statement

**Conjecture.**
*Let $\mathfrak{E}_0$ be the hadronic energy scale fixed by $Q_\beta$
and let $q = q_0$ be the substrate parameter fixed by $m_\mu/m_e$.
For each light nucleus $\mathfrak{H} \in \{{}^2\mathrm{H}, {}^3\mathrm{H}, {}^3\mathrm{He}\}$,
the joint mass-tower confinement SDP*

$$
  \min_{T_w \in H_{n_0}(q_0)^{\mathrm{GB\text{-}NF}},\,\rho \in \mathbb{Z}_{>0}}
  \Bigl\|
    \rho \cdot \bigl[\mathrm{tr}_M(T_w) + \mathrm{tower}(T_w)
    + \mathrm{tr}_M(C_{\dim_q})\bigr] \cdot \mathfrak{E}_0
    \;-\; B_{\mathrm{AME}}(\mathfrak{H})
  \Bigr\|^2
$$

*subject to: $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$
([prop:delta-max-uniform-bound](#prop:delta-max-uniform-bound)),*

*has a unique global minimizer $T_w^*$, achieved at:*

| Nucleus | Knot type | $n_0 = 3 \cdot A$ | $\rho$ | $B_\mathrm{AME}$ (MeV) |
|---------|-----------|-------------------|--------|------------------------|
| $^2\mathrm{H}$ | $6_2$ (Miller's knot) | $6$ ($A=2$) | $1$ | $2.2246$ |
| $^3\mathrm{H}$ | $8_{11}$ | $9$ ($A=3$) | $2$ | $8.4820$ |
| $^3\mathrm{He}$ | $L_{6a4}$ | $9$ ($A=3$) | $2$ | $7.7181$ |

(Earlier drafts of this table listed $n_0 = 6$ for ${}^{3}$H/${}^{3}$He.  Reconciled
with the joint-tower SDP convention $n_0 = 3 \cdot A$ used in
[`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement)
and in
[`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/joint-tower-sdp-h6-h9.witness.json)
— `atomic_n_0 = 9` for ${}^{3}$H/${}^{3}$He.  See "Structural decomposition" below
for the binding-K factorisation that motivates the $n_0 = 3 \cdot A$
convention.)

*with residual $< 0.5\%$ of $B_{\mathrm{AME}}(\mathfrak{H})$.*

## Historical evidence (volume matching)

The knot assignments above were originally found by matching
hyperbolic volumes to AME binding energies:

| Nucleus | Knot/link | Vol (SnapPy) | $\rho \cdot m_e \cdot \mathrm{Vol}$ (MeV) | vs $B_{\mathrm{AME}}$ |
|---------|-----------|-------------|-------------------------------------------|------------------------|
| $^2$H | $6_2$ | $4.40083$ | $\approx 2.2488$ | $+1.09\%$ |
| $^3$H | $8_{11}$ | $8.28632$ | $\approx 8.4686$ | $-0.16\%$ |
| $^3$He | $L_{6a4}$ | $7.32772$ | $\approx 7.4889$ | $-2.97\%$ |

Here $\rho \in \{1, 2, 2\}$ is the multiplicity from the table above and
$m_e$ is the electron mass (CAL-1); the matching law
$B_{\mathrm{AME}}(\mathfrak{H}) \approx \rho \cdot m_e \cdot \mathrm{Vol}(K)$
carries no free parameter.

(Earlier revisions of this table printed the volumes $3.16396$, $3.42721$,
$5.33349$ — the census volumes of $6_1$, $8_1$, $6^3_1$, subscript-neighbours
of the named knots, surviving from a superseded draft normalised by
$\mathfrak{E}_0 \approx 4.150$ MeV.  Live-census verification and the
two-knot-set adjudication confirm the named assignment: the named set
reproduces the match pattern above, while the orphan volume set misses by
$27$–$59\%$ under the same law — see
[`docs/audits/2026-06-12-knot-id-volume-match-adjudication.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-12-knot-id-volume-match-adjudication.md)
and the witnesses `snappy-census-volume-verification.witness.json`,
`knot-id-volume-match-adjudication.witness.json`.)

The volume-matching identification is empirically strong, but it does not
constitute a categorical derivation.  The conjecture asserts that the SDP
ground truth agrees with the historical assignment.

## SDP witness evidence

Numerical SDP witnesses (stored in
`folio-assistant/computations/probe-sdp-canonical-paper-formula.witness.json`)
show that the multi-term mass formula reproduces the AME binding
energies of $^2$H, $^3$H, $^3$He to within the claimed error bound
when $T_w$ is set to these knot types.  The conjecture asserts that
no other $T_w$ within the $\Delta_{\max}$ ball achieves a smaller
residual.

## Partial closure

The R5-full canonical-knot SDP solver prototype
([`r5_full_canonical_knot_solver.py`](../../../folio-assistant/computations/r5_full_canonical_knot_solver.py),
witness
[`r5-full-canonical-knot-solver.witness.json`](../../../folio-assistant/computations/r5-full-canonical-knot-solver.witness.json))
gave the first **substrate-only** check of this conjecture for the
three light nuclei.  Result:

| Nucleus | Canonical $T_w$ | $\alpha^*$ | PSD-feasible at $q_0$? | Rank in 138 KLR-canonical classes |
|---------|-----------------|------------|------------------------|------------------------------------|
| $^3\mathrm{He}$ | $L_{6a4}$ | $0.000$ | **yes** ✓ | 24 (top 17 %) |
| $^2\mathrm{H}$ | $6_2$ | $0.891$ | no (single-term cost) | 62 (top 45 %) |
| $^3\mathrm{H}$ | $8_{11}$ | — | (deferred — needs $H_5$ Hoefsmit) | — |

**Status by nucleus:**

- **$^3\mathrm{He}$ — PSD-feasibility verified** at $q_0$: the
  canonical $T_w = L_{6a4}$ sits on the structural target
  ($\alpha^* = 0$) in the standard $(2,1)$ Wedderburn block.  The
  $\chi$-fingerprint of the prototype's recovered word
  $(\sigma_1 \sigma_2^{-1})^3$ matches the historical SnapPy braid
  $[-1, 2, -1, 2, -1, 2]$ up to generator-sign convention (same KLR
  canonical-basis class).  This discharges sub-deliverable 2 of
  Issue #604 for $^3\mathrm{He}$.
- **$^2\mathrm{H}$ — needs multi-term cost.** The prototype's
  single-term flagship formula $B = m_e \cdot \rho \cdot \mathrm{tr}_M(T_w)$
  does not make $6_2$ the structural winner (per the known offset
  documented in `probe-sdp-canonical-paper-formula.witness.json`).
  Wiring T2–T6 of
  [`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
  into `cost_for_candidate` is the next-priority closure step.
- **$^3\mathrm{H}$ — pipeline deferred.** Hoefsmit seminormal at
  $H_5$ needs to land first (currently a deferral to
  Rust `tools/hecke-engine`).

**Categorical uniqueness theorem (proof obligation 2)** is now
formally stated in
[`conj-canonical-knot-id-sdp.lean`](conj-canonical-knot-id-sdp.lean)
as `helium3_canonical_uniqueness_via_strict_complementarity`.  The
Lean theorem takes:

1. The R5-full numerical witness (`R5FullWitness LightNucleus.helium3`)
   recording $\alpha_{\mathrm{gap}} = 0$ + strong duality
   ($|\text{primal\_obj} - \text{dual\_obj}| \leq 10^{-6}$);
2. A strict-complementarity certificate
   (`StrictComplementarity LightNucleus.helium3`) — the categorical
   hypothesis upgrading numerical PSD-feasibility to unique-minimizer
   status per Boyd–Vandenberghe §5.5.

and concludes
`CanonicalKnotIdSDP LightNucleus.helium3` (the §3b-cond conditional
class instance for $^3\mathrm{He}$).  This is the closure path for
sub-deliverable 3 of Issue #604: under the strict-complementarity
hypothesis (a categorical claim about the geometry of the SDP's
feasible set, not a numerical certificate), the historical
$L_{6a4}$ assignment for $^3\mathrm{He}$ is *the* unique R5-full
canonical $T_w$.

The genuine *uniqueness* leg — Boyd–Vandenberghe §5.5
strict-complementarity $\Rightarrow$ unique primal optimum — is closed
for $^3\mathrm{He}$ **without any axiom**.  The R5-full witness places
$^3\mathrm{He}$ in the interior regime (all three Wedderburn-block
minimum eigenvalues strictly positive: trivial $1.87$, standard $0.53$,
sign $0.53$, so the active set is empty), where the §5.5 argument is
fully constructive.  The closure is
`nucleus_uniqueness_closed_via_active_empty` at the $^3\mathrm{He}$
strand count $n_0 = 9$ (specialised as
`helium3_uniqueness_closed_via_active_empty` in
[`AppliedHelium3Uniqueness.lean`](../lean/QOU/BraidKnot/AppliedHelium3Uniqueness.lean)),
discharged through
`real_strict_complementarity_unique_of_active_empty_and_cost_posDef`
([`SDPRealUniqueness.lean`](../lean/QOU/MathlibExt/SDPRealUniqueness.lean))
with no dependency on the general SDP rank-deficiency axiom.

The general (non-empty active set) case — needed at the degenerate /
metallic-coincidence loci where strict complementarity fails — remains
gated on the `SDPRankUniqueness` Mathlib gap (SDP optimal-face
rank-deficiency).  See
[`docs/audits/2026-06-13-strict-complementarity-sdp-uniqueness-attempt.md`](../../../docs/audits/2026-06-13-strict-complementarity-sdp-uniqueness-attempt.md)
for the closeable/irreducible split and the
[`r5-full-canonical-knot-solver.witness.json`](../../../folio-assistant/computations/r5-full-canonical-knot-solver.witness.json)
active-set data.

## Proof obligations

1. **Finitude of candidate set.**  The Plancherel-weight boundedness
   ([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
   gives a finite bound on the number of GB-normal-form elements of
   $H_6(q_0)$ with $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$.
   Make this bound explicit and computable.

2. **Exhaustive or branch-and-bound search.**  Over the finite
   candidate set (or via a certified branch-and-bound), confirm that
   no $T_w \neq T_{6_2}$ (resp.\ $T_{8_{11}}$, $T_{L_{6a4}}$) achieves
   a smaller residual.

3. **Uniqueness of $\rho$.**  Show that $\rho = 1$ for $^2$H and
   $\rho = 2$ for $^3$H/$^3$He are the unique positive-integer
   multiplicities in the feasible SDP region.

## Structural decomposition (issue #604, deliverables 3 + 4)

The numerical evidence from
[`folio-assistant/computations/r5-full-canonical-knot-solver.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/r5-full-canonical-knot-solver.witness.json)
(deliverable 1) and
[`rho-prefactor-structural-verifier.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/rho-prefactor-structural-verifier.witness.json)
(deliverable 4) shows that the canonical $T_w$ at the **braid strand
count** alone does *not* uniquely identify the bound state — proton
and ${}^{3}$He have Markov-equivalent braid words in $H_3(q_0)$ (mutual
inverses), yet they are distinct bound states with distinct $\rho$.

The structural fix is to factor:

$$
T_w(\mathfrak{H})
\;=\;
K(\mathfrak{H})
\,\cdot\,
\bigotimes_{i=1}^{A} T_w(\text{nucleon}_i)
$$

where $K(\mathfrak{H}) \in H_{3 \cdot A}(q_0)$ is the **binding
operator** linking the $A$ nucleon-trefoils.  This splits the SDP
uniqueness conjecture into:

(a) **Constituent uniqueness** — each $T_w(\text{nucleon}_i)$ is the
    unique PSD-feasible canonical element at $H_3(q_0)$.  *Closed
    numerically* by the R5-minimal verifier
    ([`joint_tower_sdp_solver_v2.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/joint_tower_sdp_solver_v2.py)).

(b) **Binding-K uniqueness** — $K(\mathfrak{H}) \in H_{3 \cdot A}(q_0)$
    is the unique PSD-feasible Hecke element satisfying the joint-tower
    SDP cross-level consistency constraints (4) of
    [`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement).
    *Open* — this is the categorical uniqueness theorem still required
    to fully close GAP-A-1.

The Lean class
[`conj-canonical-knot-id-sdp.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/conj-canonical-knot-id-sdp.lean)
records (a) and (b) as **separate** sub-assertions
(`constituentUniqueness`, `bindingKUniqueness`), so a downstream
conditional theorem can use only the closed (a) part once the binding-K
SDP solver mode lands and discharges (b) per-particle.

| Nucleus | $A$ | $n_0 = 3A$ | binding $K$ | constituents | $\rho$ |
|---------|-----|-----------|-------------|--------------|--------|
| ${}^2$H | 2 | 6 | $L_H$ (Hopf) | $\{p, n\}$ | 1 |
| ${}^{3}$H | 3 | 9 | $8_{11}$-class link | $\{p, n, n\}$ | 2 |
| ${}^{3}$He | 3 | 9 | $L_{6a4}$ | $\{p, p, n\}$ | 2 |

## Relationship to GAP-A-1

This conjecture directly addresses GAP-A-1 of the
[derivation audit report](#prose:derivation-audit-report).
A proof would replace the historical volume-matching identification
with a purely categorical derivation.

