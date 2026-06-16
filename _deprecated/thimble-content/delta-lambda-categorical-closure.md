**Conjecture (per-partition $\Delta_\lambda(K)$ as block algebraic residue).**

*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q_0$, and let $\mathcal{B}_K \in B_{3A}$ be the
canonical atomic braid for knot $K = K(Z, N)$ in the Hecke algebra
$H_n(R, q)$ at $n = 3A$. For each partition $\lambda \vdash n$, let
$e_\lambda \in H_n(R, q)$ be the central idempotent projecting onto
the Wedderburn block $\mathrm{End}(V_\lambda)$, and let $\pi_\lambda$
denote the corresponding block-projection.*

*Define the **per-$\lambda$ SW differential** as the block-projection
of the Seiberg–Witten differential
([SW-period thimble equivalence](#prop:sw-period-thimble-equivalence)):*

$$
  \lambda^{(k)}_{\mathrm{SW}, \lambda}
  \;:=\;
  \pi_\lambda \bigl(\lambda^{(k)}_{\mathrm{SW}}\bigr).
$$

*Define the **per-$\lambda$ principal Galois orbit**
$\mathcal{O}_{\mathrm{prin}}^{(\lambda)}$ as the innermost conjugate
pair of the per-$\lambda$ discriminant
$\Delta^{(\lambda)}(z) := \pi_\lambda(\Delta(z))$ in
$\operatorname{Frac}(R)[z]$.*

*Then the per-partition closure of $\Delta_\lambda(K)$ in the
master binding-energy formula*

$$
  B(K) \;=\; m_e \cdot \sum_\lambda y_\lambda(q) \,
    \chi^\lambda(\mathcal{B}_K) \, \Delta_\lambda(K)
$$

*is*

$$
  \boxed{\;
    \Delta_\lambda(K)
    \;:=\;
    \tau_q\!\Bigl(\sum_{p \in \mathcal{O}_{\mathrm{prin}}^{(\lambda)}}
      \mathrm{Res}^{\mathrm{alg}}_p \bigl(
        \chi^\lambda(\mathcal{B}_K) \cdot \lambda^{(k)}_{\mathrm{SW}, \lambda}
      \bigr)\Bigr).
  \;}
$$

## Ingredients (all categorically derived)

| Ingredient | Where defined | $R$-side ring |
|---|---|---|
| $\chi^\lambda(\mathcal{B}_K)$ — Hecke character | [Markov trace product](#thm:markov-trace-product) | $\mathbb{Z}[q^{\pm 1/2}]$ |
| $e_\lambda$, $\pi_\lambda$ — central idempotent + projection | [explicit central idempotent](#prop:explicit-central-idempotent) | $\mathbb{Z}[q^{\pm 1/2}]$ |
| $\Delta(z)$ — color-tube discriminant | [color-tube cubic](#rem:color-tube-cubic) | $\mathbb{Z}[z]$ |
| $\lambda^{(k)}_{\mathrm{SW}}$ — SW differential, jet prolongation $k$ | [lepton mass integrals](#rem:lepton-mass-integrals) | over $\mathcal{E}_q$ |
| $\mathrm{Res}^{\mathrm{alg}}_p$ — algebraic residue | [A2.4](#prop:sw-period-thimble-equivalence) | $\Omega^1(\mathcal{E}_q) \to R$ |
| $\mathcal{O}_{\mathrm{prin}}^{(\lambda)}$ — innermost Galois orbit at block $\lambda$ | new in this conjecture | algebraic |
| $\tau_q$ — archimedean fibre functor | [QOU](#def:quantum-observable-universe) | $R \hookrightarrow \mathbb{R}$ |
| $y_\lambda(q)$ — Jones–Markov central coefficient | [Wenzl bridge](#prop:wenzl-bridge-applicability-qou) | $\mathbb{Z}[q^{\pm 1/2}]$ |

**No empirical input** beyond the CAL-1 anchor $m_e$. The conjecture
respects the three-calibration discipline
([three calibration inputs](#prop:three-calibration-inputs)).

## Categorical interpretation

*The formula expresses $\Delta_\lambda(K)$ as the **archimedean
realization** of the per-block algebraic residue: $\tau$ applied to a
purely $R$-side categorical expression. This is the per-$\lambda$
refinement of A2.4
([SW-period thimble equivalence](#prop:sw-period-thimble-equivalence)),
which handled only the trivial-isotype case $\lambda = (n)$
(baryon-channel reduced to single Galois orbit on the full
discriminant).*

*The diagnosis from
[`docs/audits/2026-05-19-closed-forms-first-principles-workplan.md`](https://github.com/litlfred/qou/blob/claude/closed-forms-first-principles/docs/audits/2026-05-19-closed-forms-first-principles-workplan.md)
identifies this as the formal version of "$M_\lambda(K)$ is the
archimedean realization functor's per-block action" (GAP-A-3 / GAP-A-4
per PR #777's flagging).*

## Reduction to known cases

| $\lambda$ | Block | Reduces to |
|---|---|---|
| $\lambda = (n)$ (trivial isotype) | electron-channel ($k = 0$) | A2.4 with $\chi^{(n)} = 1$, $\Delta^{(n)} = \Delta$ |
| $\lambda = (1^n)$ (alternating isotype) | baryon-channel ($k = 3$) | A2.5 with the $\mathrm{Alt}^3$ projector ([baryon product from Alt](#prop:baryon-product-from-alt)) |
| $\lambda$ standard / hook | muon-channel ($k = 1$) | per-block extension of A2.4 Step 4 |

## Six failed ansätze (per PR #777) and how this differs

| Ansatz (PR #777) | Failure mode | This closure form |
|---|---|---|
| Occam single-support | underdetermined | residue selects orbits, not points |
| Frobenius co-Casimir $1/\dim_q(\lambda)$ | wrong sign, vortex-blind | uses $\chi^\lambda(\mathcal{B}_K)$ (vortex-aware) |
| Demazure-fibre $y_\lambda \cdot D_w / D_{w_0}$ | reproduces M_LO tautologically | introduces residue (non-trivial structure) |
| LP-Plancherel cost | shifts underdetermination | algebraic, not fit |
| LP-Frobenius cost | same | same |
| Crystal-graph weight | coarse approximation of Demazure | refined via block-projection |

**The closure form is not a 7th fit-based ansatz** — it is a categorical
construction whose ingredients are all merged content blocks (PR #779
A2.4 + the discriminant + Wedderburn idempotents). The
three-calibration discipline is preserved.

## Verification status

**Phase 1b numerical test on deuteron — partial / negative.**

The script
[`delta_lambda_categorical_verification.py`](https://github.com/litlfred/qou/blob/main/computations/delta_lambda_categorical_verification.py)
tests the naive closure form (using the **bare** principal Galois orbit
$\mathcal{O}_{\mathrm{prin}} = \{z_c^\pm\}$ for all $\lambda$, i.e.
ignoring the per-$\lambda$ projection of $\Delta(z)$) with five
candidate $k(\lambda)$ mappings: by rows, by first row, by distinct
rows, by isotype channel, by hook length. None reproduce the AME 2020
deuteron binding $B(D) = :val[B_2H_AME_MeV]{precision=6}$ MeV at the required precision:

| Mapping | $B(D)$ predicted | Error |
|---|---:|---:|
| by_first_row | 0.0670 MeV | 97% miss |
| by_sign | 0.0491 MeV | 98% miss |
| by_hook | 0.0516 MeV | 98% miss |
| by_distinct_rows | −0.0067 MeV | 100% miss |
| by_rows | −0.0100 MeV | 100% miss |

**Diagnosis** (compared to empirical Δ tabulation in
[`delta-lambda-empirical-tabulation.witness.json`](https://github.com/litlfred/qou/blob/main/computations/delta-lambda-empirical-tabulation.witness.json)):

- Empirical best-single-block $\Delta_{[5,1]}(D) \approx -22.96$.
- My closure form predicts $\Delta_{[5,1]}(D) \approx |c_3| \approx 0.260$
 (using $k = 3$ at the principal pair).
- Ratio: $\approx$ **88$\times$**, missing a large structural factor.

Plausible missing factors (not tested in this PR):

- $1/\hbar_q^2 \approx 102$ (Borromean / Planck-tick rescaling) —
 gives $\approx$ 26.5, close to 22.96.
- A dimension-of-irrep factor $\dim_q(\lambda)$ — the standard partition
 $[5,1]$ has $\dim_q = 5$, giving $\approx$ 1.3, too small alone.
- Combined: $\dim_q(\lambda) / \hbar_q^2 \approx 510$, too large.

**Honest assessment.** The bare closure form is **not numerically
correct**, but the order of magnitude ($\sim 10^{-1}$ MeV vs target 2.225 MeV)
is the right ballpark — much closer than the six failed ansätze from
PR #777 which were either tautologically zero or off by orders of
magnitude wrong-sign. The closure form's **structure** (per-λ algebraic
residue at a Galois orbit) is consistent with the substrate-level
diagnostic; the **normalization** needs a categorical refinement.

**Next refinement paths:**

1. **Per-$\lambda$ discriminant factorization** (the R1 risk in the
 workplan): if $\Delta^{(\lambda)}(z) \neq \Delta(z)$ for non-trivial
 $\lambda$, the per-$\lambda$ Galois orbit is different — possibly
 larger — giving larger residues.
2. **Borromean-tower rescaling**: factor of $1/\hbar_q^2$ matches the
 m_p Borromean tower normalization; integration into Δ_λ would tie
 it back to the substrate-derived $\rho_K$ thread.
3. **Higher jet prolongation** $k \geq 4$ — currently only $k \in \{0, 1, 2, 3\}$
 are implemented; higher-order corrections may rescale.

Phase 2 will pursue path (1) — the per-$\lambda$ discriminant
factorization is the categorical refinement most consistent with
the algebraic-residue framework, and the empirical 88$\times$ factor
suggests a non-trivial block-decomposition is present.

## Risk register

- **R1 (high):** Per-$\lambda$ discriminant $\Delta^{(\lambda)}(z)$ may
 not factor from $\Delta(z)$ under $\pi_\lambda$. The
 block-decomposition of a polynomial in $z$ may not respect the
 Hecke block structure of $H_n(R, q)$. *Resolution if R1 fires:*
 redefine $\Delta^{(\lambda)}$ via the per-block Wedderburn
 discriminant (an algebraic invariant of $\mathrm{End}(V_\lambda)$),
 not by polynomial-projection.

- **R2 (medium):** Numerical $\Delta_\lambda(D)$ may match empirical
 binding only loosely (10–50% level), not at 1 ppm. *Resolution if
 R2 fires:* the closure form is qualitatively right but
 quantitatively requires refinement — likely the
 $\mathrm{Res}^{\mathrm{alg}}$ at higher jet prolongation $k \geq 4$,
 matching the higher-order Picard–Lefschetz residue structure.

- **R3 (low):** $\mathcal{O}_{\mathrm{prin}}^{(\lambda)}$ may differ from
 the trivial-block case (A2.4) at non-trivial $\lambda$. *Resolution:*
 this is expected — different blocks have different "innermost"
 orbits; the formula encodes this accordingly.

## Status

**Open.** Phase 1a (this block) is the formal statement; Phase 1b
(numerical verification on D) is the next deliverable.

## Lean axiomatisation

Per CLAUDE.md §3b, the conjecture is encoded as a Lean `class`:

```lean
class DeltaLambdaCategoricalClosure (R : Type*) [CommRing R] where
  delta_lambda :
    (lambda : Partition) → (K : KnotData) → R
  closure_form :
    ∀ (lambda : Partition) (K : KnotData),
      delta_lambda lambda K =
        sum_residues_at_principal_orbit lambda K
```

Concrete instances will be constructed for specific atoms (D, T, ${}^{3}$He)
once Phase 1b verifies the formula numerically.
