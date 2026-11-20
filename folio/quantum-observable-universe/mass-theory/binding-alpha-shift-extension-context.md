## Setting — the $A \ge 3$ binding gap

The binding-endomorphism analogy closes the deuteron via
$B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \Delta\mathrm{tr}$
to **+0.19 %**, but undershoots $A \ge 3$ by 44–72 %.  Diagnosis:
$\Delta\mathrm{tr}$ is the **linear truncation** of $\log(\mathrm{tr}) \sim \mathrm{Vol}$;
the extensive observable lives in the **per-rep q-Reeb rotation
phase** on the column-rich irrep of a substrate-fixed force-carrier
torus knot.

The α_shift universal chain proves
$\alpha_{\text{shift}}(T_{p, k}) = k \cdot (p - 1)$ — the
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

| nucleus | A | hypothesised T(p, k) | α_shift | status |
|---|---:|---|---:|---|
| deuteron (D) | 2 | T(2, 3) candidate | 3 | open |
| tritium (T) | 3 | T(2, 5) candidate | 5 | open |
| $^3$He | 3 | T(2, 5) candidate (mirror) | 5 | open |
| $^4$He | 4 | T(3, 4) candidate | 8 | open |

The candidate `(p, k)` values are hypothesised; the rigorous
identification from the substrate's
Hecke-Wedderburn block structure on $H_{3A}(q)$ is open.

The deuteron candidate $T(2, 3)$ is motivated by the following rationale:

1. *Smallest non-trivial torus knot.*  $T(2, 3)$ is the trefoil —
   the minimum-pole-order column-rich irrep, matching the deuteron's
   role as the lightest $A \ge 2$ nucleus.
2. *$\mathcal{B}_3$-braid-closure consistency.*  The
   binding-endomorphism analogy closes the deuteron via
   $B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \Delta\mathrm{tr}$
   to $+0.19\,\%$.  $T(2, 3)$ is the canonical boundary torus knot
   of $\mathcal{B}_3$ (the trefoil is the $(2, 3)$-cable of the
   core circle in $\mathcal{B}_3$'s Seifert fibre structure).
3. *Calibration consistency.*  The
   deuteron's full
   Markov-weighted q-Reeb phase aggregation gives
   $\rho_{\mathrm{full}}(D) = 14.6673$ MeV/rad.  With
   $\alpha_{\mathrm{shift}} = 3$ and $m_e \approx 0.511$ MeV, the
   abstract substrate coupling $\rho_0$ of the binding factorisation
   reads $\rho_0 = B(D) / (m_e \cdot 3) \approx 1.451$ — a
   dimensionless ratio (its $\mathrm{rad}^{-1}$ unit arises only
   when the result is re-multiplied by the $14.6673$ MeV/rad
   phase-scale measurement to recover $B(D)$).  Note that
   $\rho_0$ (the *substrate coupling*) and $\rho_{\mathrm{full}}(D)$
   (the *measured aggregation*) are **distinct quantities** — one is
   the substrate-universal coupling, the other the per-deuteron
   phase-weighted aggregation — bridged by the $\alpha_{\mathrm{shift}} = 3$
   normalisation.

This is the $A\ge3$ analogue of:
- [`meson-color-tube-uniqueness`](#prop:meson-color-tube-uniqueness)
  for $m_K / m_\pi$ (smallest non-trivial pair $\{T(2, 3), T(2, 4)\}$);
- [`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
  for $1/\alpha_{\rm EM}$ (genus-4 Bring pair $\{T(2, 9), T(3, 5)\}$);
- the T(2, k) tower for lepton + electroweak masses
  (W k=4, Z k=6, τ k=7, H k=8).

## Structure of the statement

- **Hypothesis 1 (per-rep Reeb phase factorisation).**
  $B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(A)$, where
  $\alpha_{\text{shift}}(A) \in \mathbb{N}$ is the per-A pole order.
- **Hypothesis 2 (force-carrier knot).** The per-A pole order
  $\alpha_{\text{shift}}(A)$ is realised by the proved formula
  $k(A) \cdot (p(A) - 1)$ at a substrate-identified torus knot.
- **Uniqueness (conditional on both hypotheses).** Two binding
  evaluators sharing $(m_e, \rho_0, \alpha_{\text{shift}})$ agree
  pointwise.

### Light-nuclei candidate assignment

The candidate table above is a single assignment covering the light
nuclei $A \in \{2, 3, 4\}$: $D \mapsto T(2, 3)$,
$T / {}^{3}\mathrm{He} \mapsto T(2, 5)$,
${}^{4}\mathrm{He} \mapsto T(3, 4)$. With
$\alpha_{\text{shift}}(A) = k(A) \cdot (p(A) - 1)$ it gives
$\alpha_{\mathrm{shift}} = 3$ (deuteron), $\alpha_{\mathrm{shift}} = 5$
(A=3 mirror) and $\alpha_{\mathrm{shift}} = 8$ ($^4$He), and it satisfies
Hypothesis 2 by construction. The identification pattern is stated once
for all light nuclei; identifying $(p_A, k_A)$ from first principles is
the open question below.

## Remaining open math

What is open is to identify the specific $(p_A, k_A)$ for each light
nucleus A.  The candidate hypotheses in the table above are
informed by:
- the deuteron's $\rho_0 \approx 14.7$ MeV/rad calibration from
  the formal derivation;
- the mirror pair (T/$^3$He) $\rho \approx 18.5$ MeV/rad — ~25 % rise from the
  deuteron, suggesting a per-λ jump in pole order;
- the q-Hamiltonian rotational-scale canonical evaluation
  (the formal derivation) confirms $\mu_0 \approx 1.63$ MeV
  is derived from the universal-ilp construction, narrowing the
  open question to the **per-A force-carrier knot choice**, not the
  scale.

Closing it — proving why specifically T(2, 5) carries A=3 mirror
binding etc. — requires the per-nucleus minimisation argument on
H_{3A}(q)'s Wedderburn block at the binding's smallest non-trivial
irrep.  The target is a theorem deriving $(p_A, k_A)$ from a Hecke-
trace minimisation principle, analogous to the still-open meson
force-carrier derivation in
[Meson m_K/m_π ratio uniqueness via the α_shift universal chain](#prop:meson-color-tube-uniqueness).
