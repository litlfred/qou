# PR #751 critical re-analysis — triple-check for sneak CAL-4

**Date:** 2026-05-22
**Branch:** `claude/workplan-0b-mn-substrate` (merged via PR #751)
**Scope:** every commit in the last 10 days on this branch + the two
docs it cites (`2026-05-18-workplan-0b-m-n-substrate-derivation.md`,
`2026-05-18-workplan-0b-routes-b-c-findings.md`,
`2026-05-18-lambda-scale-derivation-search.md`,
`2026-05-18-rd4-deep-exploration.md`,
`mobius-limit-from-thimble.md`).

## TL;DR

The merged PR contains **one solid mathematical result** and
**one structural over-claim that is a CAL-4 in disguise**. The
load-bearing claim — that `A((4-q)/(4q+3))` gives a substrate-
pure mass scale at q_0 — does not survive the triple-check.

| Item | Status |
|---|---|
| `prop:sw-3root-rational-integrand` — integrand_baryon $= -P(z)/D(z)$ | **SOUND** (verified via Vieta-resultant; numerical match to machine precision) |
| Family A `(1/4) Σ dim_q V_λ = 5/2 + (3/4)·h²` | **SOUND** (already proved on PR #701; restated here) |
| V7 = Σ dim_q V_λ / [4]_q hits `5/2 − (13/16)·h²` | **SOUND identity, but 11% off the empirical −G coefficient** |
| `5/2 − h²·G` empirical λ_scale | **EMPIRICAL** (5.4 ppm to CODATA, no substrate derivation; G transcendental, so no rational/Laurent form can realise it) |
| `A((4-q)/(4q+3)) = 5/2 − h²·G` as functions of q | **FALSIFIED in this same PR** (commit `ffcf23584`: A(3/7) = 2.4637 ≠ 2.5) |
| Routes-B+C-findings claim "PR #690 implicitly computes 5/2 − h²·G" | **MISLEADING** — numerical coincidence at q_0 alone, not a structural identity |
| **(4-q)/(4q+3) "Picard-Lefschetz" derivation** | **SNEAK CAL-4** — see §3 below |

## 1. What is actually proved

### 1.1 Schur–Weyl 3-root product is an exact rational function

For the q-independent color-tube cubic
$F(z,c) = c^3 + (4z+1)c^2 + (6z^2+3z+1)c + (4z^3+3z^2+2z+1)$,

$$
  \prod_{k=1}^{3} \frac{dc_k}{dz}
  \;=\; -\frac{P(z)}{D(z)},
$$

with explicit palindromic-discriminant `D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16`
and `P(z) = 64z⁶+96z⁵+120z⁴+160z³+105z²+66z+39 = Res_c(F, F_z)`.

**Triple-check:**
- `sympy.resultant(F, F_z, c)` → P ✓
- `sympy.resultant(F, F_c, c) = -disc_c(F)` (sign: `D(0) = 16`,
  `disc_c(F)|_{z=0} = -16`) ✓
- Numerical match against production `sw_3root_product_degree1`
  at `z=0.1` is machine ε ✓

This is correct mathematics. The `.md` is right; the `.ts` and `.lean`
docstrings still say `D = disc_c(F)` without the sign correction
(Copilot already flagged this; uncommitted patches partly address
the `.md` but leave `.ts` line 15 and `.lean` lines 11/48 in the
old form).

### 1.2 Polynomial-division structure

$$
  -\frac{P(z)}{D(z)} \;=\; -4 \;+\; \frac{20z^4 + 40z^3 + 35z^2 + 30z + 25}{D(z)},
$$

so $\int_{-a}^{a}(-P/D)\,dz = -8a + (\text{remainder integral})$. The
remainder integral is sum-of-arctangents over the three irrational
w-roots of `D̃(w) = 16w³+24w²−13w+2` (discriminant $-80000$,
**not** a perfect square in $\mathbb{Q}$ — so D(z) is irreducible
over $\mathbb{Q}$, ruling out clean factorisation).

This is sound but **not** what the merged PR claims. It does **not**
give a closed-form expression for $A(a)$, just a rational
decomposition of the integrand.

## 2. Family A vs V7 — structural impasse

| Candidate | $\sum$ at $q=1$ | $h^2$ coefficient |
|---|---|---|
| V1 = Family A: $\tfrac{1}{4}\sum_\lambda \dim_q V_\lambda$ | $5/2$ | $+3/4$ (positive!) |
| V7 = $\sum_\lambda \dim_q V_\lambda / [4]_q$ | $5/2$ | $-13/16 \approx -0.8125$ |
| **Target from empirical fit** | $5/2$ | $-G \approx -0.91597$ |
| V10 = $\sum_\lambda \dim_q V_\lambda \cdot [2]_q / ([3]_q[4]_q)$ | $5/3$ | $-8/9 \approx -0.8889$ |

**V7 was advertised as a "discovery" but its $h^2$ coefficient
$-13/16$ is 11% off $-G$**, not within shouting distance. More
importantly: **no rational combination of q-integer denominators
can ever equal $-G$** (G = Catalan's constant is transcendental).
So the empirical form $5/2 - h^2 G$ is provably **not**
realisable as a Wedderburn sum of q-quantum dimensions over
$\mathbb{Q}(q)$-coefficients — PR #701's exhaustive falsification
already established this.

V7 is therefore a numerical near-miss, not a structural result.
The merged narrative does not over-claim this (the witness
description honestly notes "within 11% of empirical −G"), but
it should be classified as an empirical observation, not a
candidate derivation.

## 3. **Sneak CAL-4: the (4-q)/(4q+3) ansatz**

This is the load-bearing claim and where the PR's structural
narrative fails the triple-check.

### 3.1 What the merged narrative says

The Routes-B+C-findings doc (lines 28–41) and commit
`95e07e71c` ("BREAKTHROUGH") claim:

> PR #690's C2 inflection on $A(a)$ gives multiplicative factor
> 2.4615 ≈ `5/2 − h²·G` (0.068% match). So the substrate's actual
> prediction IS the `5/2 − h²·G` form.

Combined with `prop:mobius-limit-from-thimble`'s claim that
$a = (4-q)/(4q+3)$ is "the steepest-descent re-entry abscissa"
on the Picard-Lefschetz thimble, the chain reads:

1. $a(q) = (4-q)/(4q+3)$ derived from cubic geometry (P-L thimble).
2. $A(a(q)) \approx 5/2 - h^2 G$ at $q_0$ (numerical).
3. $m_p = (\text{Vol}(\mathcal{B}_3)/\hbar_q^2) \cdot A(a(q)) \cdot m_e$
   to ~0.0006%.

### 3.2 Where the chain breaks

I verified the following facts directly (script:
`probe_categorical_action_symbolic.py`; spot-check above).

**Fact 1.** The color-tube cubic $F(z,c)$ has **coefficients in $z$
only** — no $q$ dependence anywhere. Therefore:

- The discriminant locus $D(z) = 0$ has q-independent roots
  $z_c \in \{(-0.975 \pm 0.223i),\,(+0.106 \pm 0.937i),\,(+0.119 \pm 1.054i)\}$.
- The Hessian $H(z_c) = \partial^2 S/\partial z^2|_{z_c}$ is
  q-independent.
- The thimble directions and re-entry geometry are q-independent.

**Fact 2.** Therefore $A(a)$ depends only on $a$, not on $q$. The
$q$-dependence of $A(a(q))$ enters **exclusively** through the
choice of integration limit $a(q)$.

**Fact 3.** $A(3/7) = 2.4637$, $A(0.3884) = A_{\text{target}} = 2.4599$.
The post-hoc commit `ffcf23584` in this same PR records this
falsification: $A(3/7) \ne 5/2$, so $A(a(q))$ and $5/2 - h^2 G$
**are not the same function of $q$**; they agree numerically at
$q_0$ to ~600 ppm only.

### 3.3 The CAL-4 diagnosis

Combining Facts 1–3:

- The only thing that "moves with $q$" in the construction is
  $a(q) = (4-q)/(4q+3)$.
- The curve $a(q)$ is **the unique smooth one-parameter Möbius
  pencil that makes $A(a(q)) \approx m_p(q)/[m_e \cdot \text{Vol}(\mathcal{B}_3)/\hbar_q^2]$
  hold to ~0.001%** over the substrate q-range. This is exactly
  what "fit a curve through CODATA m_p" produces.
- `prop:mobius-limit-from-thimble` Step 4 attributes the
  coefficients 4 and 3 to the cubic's $c^2$-term and the cubic's
  degree — but those data are q-independent, so they cannot
  source any q-dependence in $a$. The "derivation" therefore
  cannot trace the q-dependence; it can at best name the matrix
  entries after the fit is in hand.

**Therefore: `(4-q)/(4q+3)` is a 4th calibration in disguise.**
It is a CODATA-m_p-fitted curve dressed up as a structural Möbius
transform. Including it as the integration limit while claiming
"substrate-pure" violates the 3-calibration discipline exactly the
way PR #701's R&D 4 audit warned (`2026-05-18-rd4-deep-exploration.md`
§Option A).

### 3.4 What PR #701 already concluded

PR #701's R&D 4 deep exploration (file
`2026-05-18-rd4-deep-exploration.md`, lines 138–151) already
delivered the honest verdict that should govern any successor PR:

> - **STRUCTURALLY FALSIFIED**: `λ_scale = 5/2 − h²·G` via Family
>   A, sign-flips, Hecke levels, transcendentals, R&D 4 Vol search
> - **EMPIRICAL STATUS**: λ_scale ≈ 2.46 matches CODATA m_p to
>   5.4 ppm but has no substrate derivation in any tested basis
> - **OPEN R&D**: substrate origin of λ_scale (paper-level decision
>   required, beyond compute scope)

The merged PR #751's "Routes-B+C-findings" `§Headline finding`
restates the SAME numerical match — `5/2 − h²·G` at 0.068% — and
re-interprets it through PR #690's C2 inflection, **without
acknowledging** PR #701's verdict that the form is empirical-only.
The "structural mechanism is the **inflection point of the SDP
categorical action**" claim (line 41 of that doc) inherits PR
#690's CAL-4 fit and does not provide an independent substrate
derivation.

## 4. What should change

1. **`prop:sw-3root-rational-integrand` stays** — it's a correct
   Vieta-resultant statement. But:
   - Fix the `.ts` docstring (line 15) and `.lean` (lines 11, 48):
     $D(z) = \mathrm{Res}_c(F, F_c) = -\mathrm{disc}_c(F)$, not
     $\mathrm{disc}_c(F)$. (Copilot already flagged; the
     uncommitted `.md` patch is correct, propagate to siblings.)
   - Drop the over-claim in "Consequences" (lines 116–131 of the
     `.md`) that this provides a "structural path forward for
     deriving the substrate $m_p$ anchor categorically" — the
     rational form helps integrate $A(a)$ at a **given** $a$, but
     does **not** derive the structural value of $a$.

2. **`prop:mobius-limit-from-thimble` should be downgraded** to
   `rem:mobius-limit-fit-not-derivation` or kept as
   `conj:mobius-limit-from-thimble` with an explicit honest banner
   that:
   - The cubic $F(z,c)$ is q-independent.
   - The thimble geometry is therefore q-independent.
   - The Möbius matrix entries $\{-1, 4, 4, 3\}$ are named after
     the fit, not derived from it.
   - Until a mechanism that genuinely sources q into the
     integration limit is identified, this is a CAL-4 anchor.

3. **`conj:lambda-scale-substrate-form` re-classification**
   (already recommended by PR #701 R&D 4, never executed): rename
   to `conj:lambda-scale-empirical-form` and mark explicitly as a
   4th calibration.

4. **`probe_workplan_0b_route_c_bring.py`** (verdict section,
   line 174 — Copilot review on the merged PR): the "verdict"
   should not describe `(4-q)/(4q+3)` as an empirical match. The
   comparable output factor is $A(a_{C2})$, not the input
   parameter $a$. The uncommitted patch attempts this but leaves
   the surrounding narrative still referencing the formula as if
   it were derived.

5. **Routes-B+C-findings.md needs a §0 honesty banner** stating
   that the document records numerical correspondences, **not**
   substrate derivations, and that PR #701's empirical-only
   verdict still holds for $\lambda_{\text{scale}}$. Without this,
   readers conclude (incorrectly) that the merged PR has
   substrate-derived $M_N$.

## 5. Net effect on Workplan-0b/M_N status

| Phase | Status before PR #751 | Status after PR #751 (honest) |
|---|---|---|
| M_N anchor CLASS-A retired | open | **still open** |
| Substrate-pure M_N derivation | open | **still open** |
| 4-CAL violation tracked | yes (`atomic_braid_mass_table.py:441`) | **PLUS new sneak CAL-4 in `(4-q)/(4q+3)`** |
| Exact integrand form known | no | **YES: $-P(z)/D(z)$ (new positive)** |
| Closed-form $A(a)$ | no | no (rational integrand, but $D̃(w)$ irreducible over $\mathbb{Q}$) |

The PR delivered **one** structural positive (the integrand's
exact rational form) and **inherits two** sneak CAL-4s (PR #690's
$(4-q)/(4q+3)$ ansatz, and the cross-PR claim that this realises
PR #701's empirical $5/2 - h^2 G$ form). Neither CAL-4 was
acknowledged in the merged narrative.

## 6. Recommended next actions

1. **Cherry-pick the `.ts` / `.lean` sign-fix patches** onto main
   (separate PR, blockers for Copilot review #751 resolution).
2. **Open a follow-up "honesty PR"** that:
   - Adds the §0 honesty banner to Routes-B+C-findings.
   - Renames `conj:lambda-scale-substrate-form` →
     `conj:lambda-scale-empirical-form`.
   - Demotes `prop:mobius-limit-from-thimble` →
     `conj:mobius-limit-from-thimble` with the q-independence
     banner.
   - Updates `prop:sw-3root-rational-integrand`'s "Consequences"
     section to drop the over-claim.
3. **Add a `derivation_uses_no_4th_calibration` audit** that
   explicitly tests for `(4-q)/(4q+3)`-style fit-curves as
   integration limits, not just for hard-coded CODATA constants.
   The existing canonical_script_input_audit catches direct
   CODATA literals but not curve-fit ansätze.
4. **Real M_N derivation route**: per PR #701 R&D 4
   recommendation §5, the open path is a derivation of $a$ (or
   equivalently $A_{\text{target}}$) from the proton's full
   9-strand braid complement volume via SnapPy, or a Bloch-group
   class. Neither was attempted in this PR.
