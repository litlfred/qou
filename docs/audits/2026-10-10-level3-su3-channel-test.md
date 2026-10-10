# The level-3 (SU(3)) Hecke channel — pre-registered test (bean `qou-lxh5`)

Status: **PRE-REGISTRATION** (this section is committed before any
`l(lambda) = 3` quantity listed below is computed). Results are appended in a
later section of this file; this section is not edited after the commit that
introduces it.

## 0. What the test is

Bean `qou-lxh5` and `docs/audits/2026-08-16-wenzl-level-family.md` §4: build
the level-3 channel (Markov trace at the forced parameter
`z_3 = q^5/(q^4+q^2+1) = q^3/[3]_q`, weights proportional to
`s_lambda(1, Q, Q^2)` at `Q = q^2`, quotient `H_n / <E^(4)>`) and ask whether
the three-row blocks it keeps — exactly the ones `r = 2` annihilates — give a
colour quantity at the existing three calibrations (CAL-1/2/3), with nothing
tuned. PASS = yes; FAIL = it needs a fourth input.

## 1. Prior art found (corpus-grep, 2026-10-10)

- `computations/probes/level_three_colour_channel_probe.py` (bean `qou-ezhi`,
  status `completed`, 2026-09-01/02) already **built** the level family
  `z_r = q^(2r-1)(q^2-1)/(q^(2r)-1)` and the `U_q(gl_r)` quantum-dimension
  weights, and ran a colour test: the QCD one-gluon-exchange ratio
  `|C(3bar)/C(6)| = 2`, which the substrate misses by exactly 2 (ratio 1, from
  `|det T| = 1`). **That observable lives at `n = 2`, on the blocks `(2)` and
  `(1,1)`, which `r = 2` does NOT annihilate, and its value does not depend on
  `z_r` at all** (the block eigenvalues `q`, `-1/q` are level-independent). So
  it is a real result, but it is not the test `qou-lxh5` names, which is about
  the `l(lambda) = 3` sector. `qou-lxh5`'s own body ("What is missing is any
  measurement") and the 2026-10-10 pre-read ("no live producer found") both
  missed this probe.
- `computations/probes/wenzl_level_family.py` W6 (PR #5229) — the quotient
  dimensions `sum_{l(lambda)<=r} (f^lambda)^2`; reused as a cross-check.
- `computations/probes/wenzl_level_tower_verify.py` — `z_r = q^r/[r]_q`
  symbolic identity.
- `computations/m_p_substrate_identity_50dps.py::trM_borromean` — the corpus
  proton identity `m_p/m_e = 2 (Vol(4_1)/hbar_q^2) F_Bor - 12`,
  `F_Bor = |tr_M(beta_Bor)| [3]_q! / q^3`, with `tr_M` the convention-D
  (= level-2) Markov trace, closed form `(4+h^2-3h^4-h^6)/(h^2+4)`. Its own
  docstring records that *"the mass channel sees `y_3 + y_(1^3)`"* and that D
  was substituted so that `y_(1^3) = 0` is baked in.
  **Control already run (an `r = 2` quantity, not `l = 3`):** the level-2
  normalised Markov trace built here from seminormal matrices reproduces that
  closed form exactly over `Q(q)` (difference simplifies to 0), and satisfies
  `tr(sigma_1) = z_2`. So replacing level 2 by level 3 in this identity is a
  well-defined substitution, not a re-modelling.

**Disclosure (blinding).** Before writing this list I had read `qou-ezhi`'s
printed `n = 3` level-3 weights (`y(3) = 0.378370691`, `y(2,1) = 0.293082487`,
`y(1,1,1) = 0.035464334`) and its colour-factor verdict. I had **not** seen any
level-3 value of the Borromean trace, of `F_Bor`, or of `m_p/m_e`.

## 2. Candidate colour observables in the corpus (look-elsewhere count = 9)

| # | observable | corpus home | tested here? | why / why not |
|---|---|---|---|---|
| 1 | `m_p/m_e` via the corpus proton identity with the level-3 trace | `m_p_substrate_identity_50dps.py`, `canonical_mass.py` | **YES — PRIMARY** | the only corpus formula that is (i) dimensionless, (ii) a colour-singlet baryon observable, (iii) a 3-strand Markov trace in which the `(1^3)` block enters with nonzero character (`chi_(1^3)(beta_Bor) = 1`), so the `l = 3` sector the bean is about actually contributes. No new map has to be invented. |
| 2 | `alpha_s(M_Z) = 0.1180(9)` | bean `qou-5iaz` | no — recorded as untestable | the corpus has **no** map from any Markov-trace quantity to `alpha_s`; `qou-5iaz` option 1 names `T(2,9)` with an unspecified normalisation. Supplying one would be the fourth input. `T(2,9)` is a 2-strand braid, so it has no `l = 3` block in any case (computed as a control only). |
| 3 | QCD colour-factor ratio `|C(3bar)/C(6)| = 2` | `qou-ezhi` | no — already run | FAIL by exactly 2 at `n = 2`; not the `l = 3` sector (see §1). |
| 4 | colour Casimirs `C_F = 4/3`, `C_A = 3` | grep: 2 files | no | pure group theory, no corpus formula reading them off a Markov trace. |
| 5 | singlet fraction of `3^(x)3` = 1/27, and the three-row state fractions of `3^(x)n` | — | consistency check only | at `q = 1` these are reproduced by construction (Schur–Weyl / Jimbo); not evidence for anything. Reported with the `q_0` deformation. |
| 6 | `Delta(1232)–N` splitting | 5 files, none a formula | no | no corpus formula. |
| 7 | string tension | 7 files, dimensionful | no | needs a scale and a map; none in corpus. |
| 8 | `theta_QCD` | bean `tqcp` | no | not formulated (pre-read). |
| 9 | `R(e+e- -> hadrons)` / `N_c` | — | no | needs quark charges (flavour sector), not a level-3 trace. |

## 3. The primary test, fixed in advance

**Quantity.** `R_3 := m_p/m_e` computed from the corpus identity
`2 (Vol(4_1)/hbar_q^2) F_Bor^(r) - 12` with
`F_Bor^(r) = |tr^(r)(beta_Bor)| [3]_q! / q^3`, `beta_Bor = (sigma_1 sigma_2^-1)^3`,
`tr^(r)` the normalised level-`r` Markov trace (weights `s_lambda(1,Q,Q^2)`
normalised by `sum_lambda y_lambda f^lambda = 1`), for `r = 3`. Baseline: the
same expression at `r = 2`.

**Where it is evaluated.** At `q_0` pinned by **CAL-2 alone**
(`m_mu/m_e = Vol(4_1)/hbar_q^2`, CODATA 2022 — `qou_substrate.constants.q_muon_at`).
Reason: the proton pin is itself solved from this identity at `r = 2`, so at
the proton pin the `r = 2` residual is zero by construction and `m_p/m_e` is a
calibration, not a test. Under the hypothesis "the proton channel is level 3"
the honest test is to predict `m_p/m_e` from CAL-1/2 only — exactly this.
This is the E1-type explicit comparison AGENTS.md allows for the muon pin. The
proton-pin value is reported as secondary information only.

**Target.** CODATA 2022 `m_p/m_e` (`MASS_RATIO_P_E_STR`).

**Verdict rule (fixed now).** Let `sigma_pred` be the uncertainty of the
prediction propagated from `sigma(m_mu/m_e)` through the `q_0` solve (computed
by mpmath derivative), combined in quadrature with `sigma(m_p/m_e)`.
- **PASS**: `|R_3 - R_codata| <= 3 sigma_pred`.
- **NEAR-MATCH**: not PASS, but `|R_3 - R_codata| / R_codata <= 1e-2`. Labelled
  near-match, wired to nothing.
- **FAIL**: otherwise. Phrased scope (a) unless a proved invariant is named.
The `r = 2` baseline is judged by the same rule and reported alongside (it is
expected to fail PASS at ~9.5 sigma — the known mu–p tension — which is why the
rule is stated relative to the experimental error and not to the baseline).

**Nothing is tuned.** No coefficient, no level, no word, no normalisation is
adjusted after this commit. Number of comparisons against a measured target:
**one** (primary), plus the secondary proton-pin readout of the same quantity.

## 4. Quantities computed but compared to nothing (fixed in advance)

- `z_3` recomputed (exact and at `q_0`), and the Markov property
  `tr(x sigma_n) = z tr(x)` checked on seminormal matrices for `n = 3, 4`.
- Quotient dimensions `sum_{l<=3} (f^lambda)^2`, `n = 1..8`, against W6.
- The `l(lambda) = 3` Markov shares `sum_{l(lambda)=3} y_lambda f^lambda` for
  `n = 3..8`, exact over `Q(q)` and at `q_0`, and the same at `q = 1` against
  the SU(3) state fractions (consistency).
- `T(2,9) = sigma_1^9` Markov trace at levels 2 and 3 (control: no `l = 3`
  block on 2 strands).
- Whether constructing the channel needed a flavour/colour object `W` with
  `Lambda^3 W != 0` (the audit's "A collapses into C" risk).
