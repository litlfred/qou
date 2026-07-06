The paper's unified six-term mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) covers
Hecke-algebraic content — descended trace, brane towers,
Frobenius co-Casimir, chirality, and higher-stratum residues —
but under-predicts isotope masses for $A \geq 5$ by $\sim 10\%$.
A diagnostic analysis
([higher-A shell diagnostic](#rem:strutinsky-from-graded-trace))
identifies a structured residual whose best single-feature
predictor is the GB-filtration level $\ell = 5$ (partitions of
height $6$).  This motivates a **seventh term** capturing
nuclear shell structure.

**Conjecture (Term 7 in shadow-price form).**
*There exists a height-$h_*$ such that the extended mass formula*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{\sum_{p=0}^{\infty}
    \bigl\langle \mathrm{tr}_M,\; E_\infty^{p,*}(T_w) \bigr\rangle}_{\text{Terms 1–3, 6}}
  \;+\;
  \underbrace{a_K \cdot \mathcal{C}_K}_{\text{Term 5}}
  \;+\;
  \underbrace{m_e \cdot \tau(C_{\dim_q})}_{\text{Term 4}}
  \;+\;
  \underbrace{m_e \cdot \!\!\!\!\sum_{\substack{\lambda \,\vdash\, 3A \\ \mathrm{height}(\lambda) = h_*}}
    \!\!\!\!  C_\lambda(q) \cdot S_\lambda(Z, N, A)}_{\text{\textbf{Term 7}}}
$$

*agrees with experimental CODATA masses to sub-percent accuracy
for $A \geq 5$, where:*

1. *$C_\lambda(q) = w_\lambda(q) \cdot \tau_\lambda(\sigma_g)$ is the
   **shadow-price coefficient** of partition $\lambda$
   ([BW shadow price](#prop:mass-coefficient-shadow-price)),
   with $w_\lambda = \dim_q(\lambda)^2 / [3A]_q!$ and
   $\tau_\lambda = \mathrm{tr}(\sigma_g^{(\lambda)})/\dim(\lambda)$
   the per-generator-trace per-dim;*

2. *$S_\lambda(Z, N, A)$ is the **scaling function** determined by the
   content sum $c(\lambda) = \sum_{(i,j) \in \lambda}(j - i)$
   ([content scaling](#prop:content-scaling-correspondence));*

3. *$h_* = 6$ identifies the level-5 GB-filtration channel (matching
   the empirical residual fit at A = 1–4).*

**Specialisation at A = 2 (k = 6).**

*The only height-6 partition of $k = 6$ is $\lambda = (3,2,1)$ (the
self-conjugate "staircase" partition).  Term 7 specialises to
a single shadow price:*

$$
  \mathrm{Term~7}(Z, N, A{=}2)
  \;=\;
  m_e \cdot C_{[3,2,1]}(q) \cdot S_{[3,2,1]}(Z, N, 2)
$$

*By [Wigner-2 coefficient](#prop:wigner-2-coefficient), the
self-conjugate-partition trace identity gives
$\tau_{[3,2,1]} = h/2$ and the closed form*

$$
  C_{[3,2,1]}(q)
  \;=\;
  \frac{[2]_q\,[4]_q\,[6]_q \cdot h}{2\,[3]_q^3\,[5]_q}.
$$

*At $q_0 \approx 1.110$ this evaluates to
$C_{[3,2,1]}(q_0) \approx 0.0375$ (witness:
`shadow-price-c-321-q0.witness.json`).  The scaling function
$S_{[3,2,1]}(Z, N, 2) = (Z-N)(A-1)/A^{4/3}$ vanishes for the
deuteron ($Z = N = 1$), consistent with the **pn-invisibility**
of $(3,2,1)$ noted in
[Wigner-2](#prop:wigner-2-coefficient).

## Motivation

### Empirical signal

Fitting residuals
$\Delta_{\mathrm{iso}} = M_{\mathrm{CODATA}} - M_{\text{6-term}}$
at $A = 1, 2, 3, 4$ to the per-GB-level contributions
$(\mathrm{tr}_M, E_\infty^{\ell,*})$ of the atomic braid, the
single-feature fit $\Delta \sim \alpha_\ell \cdot \chi_\ell(T_w)$
produces the smallest RMSE for $\ell = 5$
(witness: `higher-a-shell-diagnostic.witness.json`):

| $\ell$ | $\alpha_\ell$ (MeV, signed) | RMSE (MeV) | isotopes |
|:------:|:---:|:---:|:---:|
| 0 | $+1.2 \times 10^{3}$ | 411 | 6 |
| 1 | $+4.6 \times 10^{2}$ | 413 | 6 |
| 2 | $-2.5 \times 10^{3}$ | 381 | 6 |
| 3 | $+5.8 \times 10^{3}$ | 454 | 4 |
| 4 | $+1.7 \times 10^{4}$ | 438 | 4 |
| $\mathbf{5}$ | $\mathbf{-4.2 \times 10^{5}}$ | $\mathbf{342}$ | $\mathbf{4}$ |
| 6 | $+1.1 \times 10^{6}$ | 452 | 3 |

Level $5$ wins — the residual is best explained as a linear
combination of level-$5$ character values.

### Algebraic interpretation

GB-filtration level $\ell = 5$ corresponds to partitions
$\lambda \vdash n$ with $\mathrm{height}(\lambda) = 6$
([confinement level](#def:confinement-level)).  For $n = 3A$
(atomic braid in $H_{3A}(q)$), height-$6$ partitions only exist
when $3A \geq 6$, i.e., $A \geq 2$; they become numerous at
$A \geq 4$ where they carry significant tower weight
([three-parameters Wedderburn](#prop:three-parameters-wedderburn)).

Physically, height-$6$ partitions correspond to **six-nucleon
coherent superpositions** — the minimal shell-closure quorum
for the lightest closed shell (He-like, $Z + N = 4$–$6$).
Empirical nuclear shell models (Mayer, Jensen, \cite{mayer1949})
identify the first shell closure at $A = 4$ ($^4$He), which
aligns with the onset of height-$6$ partition support in
$H_{3A}(q)$.

### Structural form of $\chi_5$

The level-$5$ character projector is:

$$
  \chi_5(T_w) \;:=\; \sum_{\substack{\lambda \vdash 3A \\ \mathrm{height}(\lambda) = 6}}
    w_\lambda(q) \cdot \chi^\lambda(T_w),
$$

with Wedderburn weights $w_\lambda = \dim_q(\lambda)^2 / [3A]_q!$
([Schur–Weyl](#prop:schur-weyl-mass-decomposition)) and
Hoefsmit-seminormal $q$-characters $\chi^\lambda$
([Hecke characters](#prop:hoefsmit-seminormal-form)).  This is a
structural functional — no new mathematical machinery beyond
the existing Wedderburn decomposition — and its action on an
atomic braid $T_w(Z, N)$ is computable via the same
numerical-Hoefsmit pipeline used for the other terms.

## Evidence and falsifiability

**Supporting (structural).**

1. *Level-$5$ partitions first appear at $A \geq 2$ and become
   dense at $A \geq 4$ — aligning with empirical onset of
   shell-closure effects.*

2. *The $\alpha_5 < 0$ sign is consistent with shell closure
   being **binding-enhancing** — the correction lowers the mass
   prediction, matching the empirical stronger-than-6-term
   binding at $A = 4$ ($^4$He is doubly magic with $+7.07$ MeV/A
   binding vs. $+4.2$ MeV/A for neighbours).*

3. *The level-$5$ signal does not reduce to linear-in-$A$,
   asymmetry $(N-Z)^2/A$, or pairing $(\pm)/\sqrt{A}$ single-
   feature fits (all give RMSE 380–490 MeV vs. $342$ MeV for
   $\chi_5$), ruling out the BW empirical components as the
   source.*

**Falsifiable predictions.**

1. *At $A = 5$ ($^5$Li, $^5$He): Term 7 contribution should be
   monotonically larger in magnitude than at $A = 4$ (more
   level-$5$ partitions available).*

2. *At $A = 8$ ($^8$Be, $^8$B): Term 7 should predict the
   $^8$Be instability (weakly unbound with respect to
   $2 \cdot {}^4$He) as a sign-change in the level-$5$
   contribution.*

3. *At $A = 16$ ($^{16}$O, another doubly-magic): Term 7
   should again be binding-enhancing, scaling by the same
   $\alpha_5$ with an amplitude determined by level-$5$
   character values on the ${}^{16}$O atomic braid.*

**Refuting scenarios.**

- *If the A = 5–7 isotope residuals do not linearly correlate
  with $\chi_5$ computed from atomic-braid characters, Term 7
  as stated is falsified.*

- *If a cleaner single-level fit emerges at $\ell = 6$ or $\ell = 7$
  with $A = 5$–$7$ data added, the conjecture needs relabelling
  but the structural form stands.*

## Status

*This is a **conjecture** — the empirical signal supports the
functional form and level choice.  As of the 2026-05-09 crystal-
basis derivation, the **structural side** has been closed: the
factor $\chi_5$ admits the closed form*

$$
  S_\mathrm{crystal}(A) \;:=\; \sum_{\substack{\lambda \,\vdash\, 3A \\ \mathrm{height}(\lambda) \,\leq\, 6}}
    w_\lambda(q = 1) \cdot \chi_\lambda^\mathrm{crystal}(\beta_A),
$$

*The bound $\mathrm{height}(\lambda) \leq 6$ matches the implemented
enumeration in `term7_alpha5_crystal_derivation.py` (cumulative GS-
filtration sum through level $5$); it refines the per-stratum
$\chi_5$ projector defined earlier in this document by including
contributions from the lower strata $\ell = 0, \ldots, 4$.  For
$A = 1$ the sum reduces to those lower strata only, since no
partition of $3$ can have exactly six parts.*

*evaluated at the crystal limit $q \to 0$ (witness:
[`term7-alpha5-crystal-derivation.witness.json`](../../../computations/term7-alpha5-crystal-derivation.witness.json),
chain:
[`term7-s-crystal-4he.derivation.json`](../../../computations/term7-s-crystal-4he.derivation.json)).
$\chi_\lambda^\mathrm{crystal}(\beta_A)$ is the trace of the
crystal-limit signed-permutation action on $\mathrm{SYT}(\lambda)$,
conditional on
[crystal-graph realisation](#conj:crystal-graph-realization).
For $A = 4$ (${}^4\mathrm{He}$, doubly magic),
$S_\mathrm{crystal}({}^4\mathrm{He}) \approx -0.991241$ — no free
parameter.*

*Term $7$ then takes the form*

$$
  \mathrm{Term~7}(A) \;=\; \alpha_5 \cdot S_\mathrm{crystal}(A),
$$

*with $\alpha_5$ the **AME-calibrated** proportionality constant
(empirical fit $\alpha_5 \approx -4.2 \times 10^5\;\mathrm{MeV}$).
Atom-independence of $\alpha_5$ across $A = 1$–$4$ is a
flat-transport check on the $q \to 0 \rightsquigarrow q_0$
connection — passing this check upgrades Term $7$ from
phenomenological extension to a derived prediction; failing it
diagnoses curvature in the connection map at the level-$5$ stratum.*

*A purely-algebraic derivation of $\alpha_5$ itself (without AME
calibration) would require either (a) closure of the $q$-FSC $\leftrightarrow$ $q_0$
identification, or (b) a substrate-level identification of the
crystal-limit signed-permutation trace with a closed-form $q_0$-
algebraic functional.*

## Computational support

Witness: `higher-a-shell-diagnostic.witness.json` (A = 1–4 data,
best-fit level identified).  Extension to A = 5–7 requires
`atom_level_wedderburn_tower.py` with the `ATOM_LEVEL_WITH_A5PLUS=1`
flag enabled (partition counts: 176 for A=5, 297 for A=6, 490
for A=7).
