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

## 5. Results

*Appended after the pre-registration commit `ce171d625e`; sections 0-4 above
are unchanged.* Producer:
[`computations/eightfold/level3_su3_channel_probe.py`](../../computations/eightfold/level3_su3_channel_probe.py),
witness `computations/eightfold/level3-su3-channel.witness.json`
(`q0Anchor: comparison`, both pins recorded). Exact arithmetic in sympy over
`Q(q)`; numerics in mpmath at `mp.dps = 70`; no float arithmetic. Wall time
~23 s.

### 5.1 Construction checks (all pass)

- Seminormal matrices satisfy the braid and Hecke relations on every irrep of
  `H_2, H_3, H_4` over `Q(q)`, and on every irrep of `H_5` at `q = 7/5` (17
  irreps).
- Weights: hook-content `s_lambda(1, Q, Q^2)` equals the bialternant for all
  `l(lambda) <= 3`, `n <= 4`.
- `tr^(2)(sigma_1) = q^3/(q^2+1)` and `tr^(3)(sigma_1) = q^5/(q^4+q^2+1) = q^3/[3]_q`.
- Markov property `tr(x sigma_n) = z_3 tr(x)` holds for every basis element
  `T_w`, `w in S_n`: `n = 3` over `Q(q)`; `n = 4` at `q = 7/5` and `q = 3/2`
  (exact rationals).
- **Control: `r = 2` reproduces `(4+h^2-3h^4-h^6)/(h^2+4)` exactly**
  (difference simplifies to 0).

### 5.2 Level-3 quantities (exact)

Level-3 weights at `n = 3`, `Phi_3 = q^2+q+1`, `Phi_6 = q^2-q+1`:
`y_(3) = (q^4+1)Phi_5 Phi_10 / (Phi_3 Phi_6)^3`,
`y_(2,1) = q^2 (q^2+1)^2 (q^4+1) / (Phi_3 Phi_6)^3`,
`y_(1,1,1) = q^6 / (Phi_3 Phi_6)^3`.

```
tr^(3)(beta_Bor) = -(q^16 - 2q^14 - q^12 - 5q^8 - q^4 - 2q^2 + 1)
                   / (q^4 Phi_6^2 Phi_3^2)

tr^(3) - tr^(2)  = -(q-1)^4 (q+1)^4 Phi_10 Phi_5
                   / (q^2 (q^2+1)^2 Phi_6^2 Phi_3^2)          = O(h^4)
```

### 5.3 Primary test (section 3), at `q_0` from CAL-2 alone

`q_0 = 1.10997859564273904668179512938...` (`q_muon_at`, CODATA 2022
`m_mu/m_e = 206.7682827(46)`). Target: CODATA 2022
`m_p/m_e = 1836.152673426(32)`. `sigma_pred` = `|dR/d(m_mu/m_e)| * sigma(m_mu/m_e)`
(mpmath derivative through the `q_0` solve) in quadrature with
`sigma(m_p/m_e)`.

| | `abs tr(beta)` | `F_Bor` | `R_r` | residual | `sigma_pred` | residual / `sigma_pred` | rel. residual | verdict (rule verbatim) |
|---|---|---|---|---|---|---|---|---|
| `r = 2` (baseline) | 0.998562163193 | 4.469138596907 | 1836.152225661420 | -4.4776e-4 | 4.7165e-5 | **9.494** | 2.4386e-7 | NEAR-MATCH |
| `r = 3` (test) | 0.998295962844 | 4.467947197613 | **1835.659538489631** | **-0.49313** | 4.7175e-5 | **10453.2** | **2.6857e-4** | **NEAR-MATCH** |

Secondary (proton pin `q_0 = 1.10997858275138...`): `R_2 = 1836.152673426`
(zero residual by construction, -1.3e-70), `R_3 = 1835.659986355657`
(rel. residual -2.683e-4).

**Verdict: NEAR-MATCH under the pre-registered rule, and that label must be
read with its scope.** The rule is applied verbatim: `r = 3` is not PASS
(10453 sigma) and its relative residual 2.69e-4 is inside the 1e-2 near-match
band. Labelled near-match, wired to nothing. Three things the label does not
say:

1. **Level 3 is ~1100x worse than level 2** on the same quantity (2.69e-4 vs
   2.44e-7 relative; 10453 sigma vs 9.49 sigma). The `r = 2` baseline
   reproduces the known mu-p tension (9.49 sigma on the ratio — the
   AGENTS.md figure), which is a consistency check on the whole pipeline.
2. **The 1e-2 band is uninformative for this substitution.** `tr^(3) - tr^(2)`
   is `O(h^4)` with `h^4 ~ 1.9e-3` at `q_0`, so *any* level substitution of
   this form lands within ~1e-3 of the level-2 value and therefore inside the
   band. The near-match is a statement about how close the two traces are, not
   evidence that the three-row block carries colour content.
3. Scope (a): this construction — the level-3 trace substituted into the
   unchanged corpus proton identity, with the constants `2`, `12` and the
   normalisation `[3]_q!/q^3` carried over from level 2 — does not reproduce
   `m_p/m_e` from CAL-1/2. It is not a structural exclusion of the
   `l(lambda) = 3` sector from any closure: no invariant is named.

### 5.4 Section-4 quantities (compared to nothing)

- `z_3 = q^5/(q^4+q^2+1)`; at `q_0` (muon pin): `z_3 = 0.449304823303`, against
  `z_2 = 0.612688050638`.
- Quotient dimensions `sum_{l<=3} (f^lambda)^2`, `n = 1..8`:
  `1, 2, 6, 23, 103, 513, 2761, 15767` — **match W6** (`wenzl-level-family.json`).
- `l(lambda) = 3` Markov shares `sum_{l=3} y_lambda f^lambda` at `q_0`:
  n=3 0.035464334, n=4 0.106393001, n=5 0.201134308, n=6 0.306778842,
  n=7 0.412987597, n=8 0.512818417. At `q = 1` they equal the SU(3) state
  fractions of `3^(x)n` in three-row irreps exactly
  (1/27, 1/9, 17/81, 233/729, 313/729, 1163/2187) — consistency by
  construction, not evidence.
- `T(2,9) = sigma_1^9`: level 2 `(q^18+q^14-q^12+q^10-q^8+q^6-q^4+q^2-1)/(q^7(q^2+1))`
  = 1.828414019 at `q_0`; level 3 `(q^20+q^16-1)/(q^7 Phi_3 Phi_6)` = 1.588844579.
  Two strands: no `l = 3` block; the level enters only through `z_r`.
- **Was a flavour/colour object `W` with `Lambda^3 W != 0` needed?** No separate
  object was introduced — the only input is the integer `r = 3`. But by
  Jimbo–Schur–Weyl the level-3 trace *is* the normalised trace on `V^(x)n` for
  a 3-dimensional `U_q(gl_3)`-module `V` with `Lambda^3 V != 0` (the `(1,1,1)`
  weight `q^6/(Phi_3 Phi_6)^3` is the q-determinant line) and
  `Lambda^4 V = 0`. So the channel is equivalent to choosing such a 3-dim
  object: **the colour object is assumed via `r`, not derived** — the "A
  collapses into C" risk is realised in that sense.

### 5.5 Caveats

- Level 3 contradicts the premise of `FibreDimensionForcesTL.lean` (the mass
  fibre is 2-dimensional, forcing level 2). This probe tests the substitution;
  it does not touch that theorem.
- The `n = 4` Markov check is at two exact rational `q`, not over `Q(q)`.
- `sigma_pred` is dominated by `sigma(m_mu/m_e)` (22 ppb); `sigma(m_p/m_e)` is
  negligible in quadrature.
