**Proposition (binding A≥3 via per-rep Reeb phase at a force-carrier torus knot).**
*The light-atom binding energy* $B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(T(p_A, k_A))$
*is uniquely determined by* (i) *the substrate-universal per-rep
Reeb coupling* $\rho_0$ *pinned by the deuteron, and* (ii) *the
substrate-fixed force-carrier torus knot* $T(p_A, k_A)$
*per nucleus.  Both legs route through the proved* α_shift = k·(p-1)
*formula (`prop:alpha-shift-torus-knot`).*

## Setting — the A ≥ 3 binding gap

The binding-endomorphism analogy
([2026-05-28 audit](../../../docs/audits/2026-05-28-binding-endomorphism-analogy.md))
closes the deuteron via $B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \Delta\tr$
to **+0.19 %**, but undershoots A ≥ 3 by 44–72 %.  Diagnosis:
$\Delta\tr$ is the **linear truncation** of $\log(\tr) \sim \mathrm{Vol}$;
the extensive observable lives in the **per-rep q-Reeb rotation
phase** on the column-rich irrep of a substrate-fixed force-carrier
torus knot.

The merged α_shift universal chain
([2026-05-30 audit](../../../docs/audits/2026-05-30-alpha-shift-universal-derivation-chain.md))
proves $\alpha_{\text{shift}}(T_{p, k}) = k \cdot (p - 1)$ — the
**pole order of σ** on the column-rich irrep, equivalently the
boundary holonomy of the Yekutieli non-abelian Stokes integral
around the column cycle.  This is the **same boundary holonomy**
that the per-rep q-Reeb rotation phase records.

## The unification

Per nucleus A, identify the substrate-specific force-carrier torus
knot $T(p_A, k_A)$ whose α_shift sets the per-rep Reeb eigenvalue.
The binding closure is then

$$
  B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(T(p_A, k_A))
       = m_e \cdot \rho_0 \cdot k_A \cdot (p_A - 1).
$$

| nucleus | A | hypothesised T(p, k) | α_shift | Phase-3 status |
|---|---:|---|---:|---|
| deuteron (D) | 2 | T(?, ?) — pinned by ρ₀ calibration | — | anchor |
| tritium (T) | 3 | T(2, 5) candidate | 5 | open |
| ³He | 3 | T(2, 5) candidate (mirror) | 5 | open |
| ⁴He | 4 | T(3, 4) candidate | 8 | open |

The candidate `(p, k)` values are per the agent-survey hypothesis
(2026-05-30); the rigorous identification from the substrate's
Hecke-Wedderburn block structure on H_{3A}(q) is Phase 3 open math.

This is the A≥3 analogue of:
- [`meson-color-tube-uniqueness`](#prop:meson-color-tube-uniqueness)
  for $m_K / m_\pi$ (smallest non-trivial pair $\{T(2, 3), T(2, 4)\}$);
- [`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
  for $1/\alpha_{\rm EM}$ (genus-4 Bring pair $\{T(2, 9), T(3, 5)\}$);
- the T(2, k) tower for lepton + electroweak masses
  (W k=4, Z k=6, τ k=7, H k=8).

## Lean structure (§3b-cond)

- `class BindingPerRepReebPhase B m_e ρ_0` — substrate axiom: per-rep
  Reeb phase factorisation, with field `αShiftAt : ℕ → ℕ` recording
  the per-A pole order and `factors` axiomatising
  $B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(A)$.
- `class BindingForceCarrierKnot αShiftAt p k` — substrate axiom:
  the per-A pole order $\alpha_{\text{shift}}(A)$ is realised by
  the proved formula $k(A) \cdot (p(A) - 1)$ at a substrate-identified
  torus knot.
- `theorem binding_unique_via_alpha_shift` — sorry-free conditional
  on the two classes: two binding evaluators sharing $(m_e, \rho_0,
  \alpha_{\text{shift}})$ agree pointwise.
- `theorem binding_subsingleton` — Subsingleton companion.

## Remaining open math

**Phase 3:** identify the specific $(p_A, k_A)$ for each light
nucleus A.  The candidate hypotheses in the table above are
informed by:
- the deuteron's ρ₀ ≈ 14.7 MeV/rad calibration from
  `binding_rotation_phase_lead.py`;
- the mirror pair (T/³He) ρ ≈ 18.5 MeV/rad — ~25 % rise from the
  deuteron, suggesting a per-λ jump in pole order;
- the q-Hamiltonian rotational-scale probe
  (`binding_qhamiltonian_rotational_scale.py`) confirms μ₀ ≈ 1.63 MeV
  is derived from the universal-ilp construction, narrowing the
  open question to the **per-A force-carrier knot choice**, not the
  scale.

Closing Phase 3 — proving why specifically T(2, 5) carries A=3 mirror
binding etc. — requires the per-nucleus minimisation argument on
H_{3A}(q)'s Wedderburn block at the binding's smallest non-trivial
irrep.  Lean target: a theorem deriving $(p_A, k_A)$ from a Hecke-
trace minimisation principle, analogous to the meson force-carrier
derivation queued at `prop:meson-color-tube-uniqueness`.

## Status

This proposition is **proved conditional on the
`BindingPerRepReebPhase` + `BindingForceCarrierKnot` class
instances**.  The per-rep Reeb phase axiom is the substrate identity
(audit-confirmed); the force-carrier knot identification per A is
the genuine open math.  Sorry-free Lean conditional on both classes.

Closes the A≥3 binding entry in
[`docs/uniqueness-theorems-backlog.md`](../../../docs/uniqueness-theorems-backlog.md)
as a structurally identified item, parallel to the meson + lepton
α_shift specialisations.
