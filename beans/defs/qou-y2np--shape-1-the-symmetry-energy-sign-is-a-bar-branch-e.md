---
# qou-y2np
title: 'SHAPE-1: the symmetry-energy sign is a BAR BRANCH (exactly +/- 2 ln q), the corpus took the branch that fits nuclear binding worse, and beta-decay does NOT pin it (Q_beta uses |Delta net|)'
status: todo
pr: 8321
branch: feat/qou-ai7v-cgyn-k12x-u8ji-y2np
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T06:49:20Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

`computations/qbeta/qbeta_asymmetry_sign_is_a_bar_branch_probe.py` (6/6).

## The asymmetry is exactly `+/- 2 ln q`

From `qou-xf14`'s pinning, `b_pp = q^2/[2]_q` and `b_nn = q^-2/[2]_q`, so the
bond energies are `ln[2]_q -/+ 2 ln q` identically and

    S(Z,N) = (A-2) ln[2]_q + (-ln b_pn) + 2 ln(q) . (N - Z)

The coefficient is **exactly `2 ln q_0 = 0.2086814`**, positive for one reason:
`q_0 > 1`. (Supersedes `qou-q7ga`'s first-order `2(q_0-1) = 0.21996`.)

## Its sign is one bit — a bar branch

Under `q -> 1/q`: `[2]_q` is INVARIANT and `b_pp <-> b_nn` swap. So the two
branches are `+2 ln q` (as built, `p-p = sigma`) and `-2 ln q` (swapped), and the
bit traces to the Hecke eigenvalue assignment `u <-> +q`, `d <-> -q^-1`
(`meson-to-proton-via-borromean.md`).

## The swapped branch fits substantially better

2548 measured AME nuclides, tower-summed `E_0`, 3 strands/nucleon:

    law                            p5-p95    full    corr (N-Z)^2/A^2
    as built    p-p = sigma        1.22497  10.18       -0.804
    BAR-SWAPPED p-p = sigma^-1     1.16633   7.37       -0.493
    no asymmetry (count only)      1.18054   8.21       -0.697

It nearly halves the symmetry-energy correlation and is the **first isospin
structure in this arc to beat layout-free bond counting** — which reverses
`qou-q7ga`.

## And beta-decay does NOT pin the branch

The obvious objection is that the same letters build the nucleons, so `Q_beta`
fixes the bit. It does not, for a specific reason: `derived_masses.py` computes
`Q_beta = |Delta(net)| . E_0` with an **absolute value**, so the magnitude is
sign-blind; and the ordering is imposed separately as `m_n = m_p + Q_beta + m_e`,
not read off `Delta(net)`'s sign. Neither half constrains the bit.

## NOT adopted — and what would settle it

Choosing the branch that fits IS a fit. What is established is that the choice is
currently **free** and the evidence points away from the corpus's convention, so
something must pin it. Candidates, none evaluated here: electric charge
(`u = +2/3`, `d = -1/3` is not bar-symmetric — the most promising), the Borromean
proton construction, or the `net` values' own derivation.

**Caveat that cuts against this:** the swap is one bit out of two, so "it fits
better" is a single bit of evidence, not a derivation. And it REDUCES the symmetry
residual without supplying it — `corr = -0.493` is still the dominant residual
shape, so the term is still missing, just less badly.

Successor to the shape agenda in
`docs/audits/2026-09-05-binding-law-arc-synthesis.md` §6 item 1-2.

---

## 2026-09-05 (later) — SWAP REFUTED. The branch is selected; the REASON is not.

Instruction was to adopt the swap if the data holds. **It does not**
(`qbeta_bar_branch_refuted_probe.py`, 6/6), for two independent reasons, and the
charge test comes back weak.

### 1. The swap destroys the upper bound

The tower ruling made the law one-sided — an upper bound for 2547 of 2548 — and
that has a physical reason: every SEMF correction SUBTRACTS from the volume term,
so a law omitting all of them belongs above the data.

    branch        exceeding B <= 3.E_0.S   (measured / all)
    as built            1 / 2548              1 / 3554
    BAR-SWAPPED       845 / 2548           1018 / 3554

Band medians show why: swapped, the `A = 40-160` bands sit ABOVE 1 (1.028, 1.021,
0.994); as-built stays below throughout (0.860 -> 0.961 -> ... -> 0.796). The
swap moves the law INTO the data rather than above it — the wrong side for a law
with only negative corrections outstanding.

### 2. And it redistributes shape error rather than removing it

    branch        (N-Z)^2/A^2   A^(-1/3)   Z^2/A^(4/3)
    as built        -0.804       -0.178      -0.044
    BAR-SWAPPED     -0.493       -0.376      -0.068

It halves the ASYMMETRY correlation and more than DOUBLES the SURFACE one. The
p5-p95 gain (1.225 -> 1.166) is real but bought by moving error between channels,
not out of the law. That is what a one-bit reparameterisation does; it is not
what a missing term looks like.

### 3. The charge test — selects the corpus branch, proves little

`sigma^2 = h.sigma + 1` has eigenvalues `{+q, -1/q}` (solved). Sign-matching
`u = +2/3 -> +q`, `d = -1/3 -> -1/q` reproduces the corpus assignment. **Weak, on
two counts I state because they cut against it:** one bit agreeing with one bit
happens half the time by chance; and in `V (x) V` the eigenvalue `+q` belongs to
the SYMMETRIC part and `-q^-1` to the ANTISYMMETRIC part, so the sign encodes
pairing statistics, not charge — reading it as a charge sign is a category slip,
and the magnitudes do not corroborate (`q^2 = 1.2321` vs charge ratio `2`).

## THE OBLIGATION THIS BEAN NOW CARRIES

The branch is **selected** — by §1, a structural property of the whole table. It
is not **derived**. Nothing in the framework says why the algebra assigns
`u -> +q` rather than `d -> +q`; the corpus asserts it
(`meson-to-proton-via-borromean.md`) and every downstream number inherits it.

**This bean stays open on exactly that:** derive the flavour-to-eigenvalue
assignment, or record it explicitly as a convention with the bound as its only
current justification. Candidates unevaluated: the Borromean proton construction,
the `net` values' own derivation, colour-antisymmetry of the quark wavefunction
(the physically natural one, since the eigenvalue sign IS a statistics label).

**And the symmetry energy is still missing.** `corr = -0.804` stands, the swap is
refuted, `qou-ubsl`'s SU(4) route stays structurally forbidden. The dominant
residual shape has no source — that is unchanged by this round.

---

## 2026-09-05 (third) — COLOUR TESTED. It forbids the asymmetry rather than explaining it.

`qbeta_colour_does_not_license_the_asymmetry_probe.py` (6/6).

### The symmetry argument does not mention the flavour

In a colour-singlet baryon any quark PAIR is antisymmetric in colour (`3bar`), and
Fermi statistics then forces `space (x) spin (x) flavour` to be SYMMETRIC — at
`L = 0` with symmetric flavour, a spin triplet. **That derivation never names the
flavour**, so `uu` in the proton and `dd` in the neutron are in identical
configurations. Colour licenses NO asymmetry; whatever letter one takes, the
other takes.

### And which common letter it picks is ambiguous

  * **strand = whole quark** -> total exchange is antisym (Fermi) -> both `-q^-1`
  * **strand = colour index** -> colour antisym, rest sym -> both `+q`

The **row cap argues for the first**: `dim V = 2` (`QOU/Hecke/RowCap.lean`) and a
colour index needs three values, so a strand cannot be carrying colour. This
arc's own result points at the total-exchange reading.

### Measured — the two readings bracket the corpus's choice

    law                                     viol   median   p5-p95     corr
    as built  p-p=sigma, n-n=sigma^-1          1   0.8864   1.2250   -0.8038
    colour: BOTH symmetric  (+q)            2498   1.3231   1.1779   -0.6911
    colour: BOTH antisym    (-q^-1)            0   0.7189   1.1823   -0.6994
    both = pinned loop      (1/[2]_q)         62   0.9314   1.1805   -0.6969

  * the colour-INDEX reading is **catastrophically refuted** (2498 of 2548
    exceed the law);
  * the total-exchange reading gives a **STRICT bound** — zero violations, better
    than the corpus's one — but over-binds 39 % on the median against 11 %;
  * `2498 > 1 > 0`: the corpus's asymmetric hybrid sits BETWEEN the two symmetric
    readings and is neither of them.

### And the corpus's own justification is a declared fit

`meson-to-proton-via-borromean.md`: *"Untyped composition yields net ~ 1.506. The
CODATA proton net is ~ 0.999. **Typed crossings close this gap.**"* The split is
there because it lands on the measured proton, and the block says so. The code
asserts `uu -> sigma` / `dd -> sigma^-1` with no reason at all.

### Where that leaves this bean

**Open, one candidate shorter and sharper.** The assignment is not merely
underived — it is in **tension with the symmetry argument that would be its
natural home**. Remaining candidates: the Borromean proton construction, and the
`net` values' own derivation.

**And the symmetry energy survives all four laws** (best `-0.691` against the
corpus's `-0.804`). Removing the asymmetry is worth about a seventh of the
residual; it is not the missing term.

## 2026-09-05 — the bar branch is the ENDPOINTS of a convex family with a derived crossing

`qou-i01a`. `b_pn = w.b_pp + (1-w).b_nn` for a convex `w` (the sibling's
`pn-bond-cannot-be-extremal`), and

    delta(w) = L_pn(w) - (L_pp+L_nn)/2

runs continuously from `delta(0) = +2 log q0 = +0.20868144063904` to
`delta(1) = -2 log q0`. **Those are exactly this bean's two branches.** So the
"one bit" is the two ENDS of a continuum, and the sign flips in between at the
derived crossing `w = 1/(q^2+1) = 0.448018`, where the convex combination equals
the geometric mean `1/[2]_q`.

That reframes the open question usefully. The bar swap was refuted as a repair
(845 bound violations against 1), and it did not have to be evaluated as a
binary: the real quantity is `w`, the corpus sits at `0.500344`, and the target
is anything below `0.448018`. A derivation of `w` is the live item, not a choice
between two labels.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-10-11 — quark template tracked order by order in q (reading 3)

Probe `computations/probes/quark_template/` (pre-registered at 6b9dd5d172; exact over Q(q); 4/4 checks).

- **Flavour is invisible at order t⁰** (t = q − 1): since σ⁻¹ = σ − h, every quark letter equals σ at q = 1, all 8 template variants give the same element, and χ_(2,1) = 0 there. So reading 3 holds with equality at order zero for every template. The verdict is decided at order t¹ (where the sign bits enter), or at t³ when t¹ cancels. No verdict flips between truncation orders t¹…t⁶ or across the sub-interval of (1, ∞) containing q₀.
- **k = 0, builder placement:** the corpus template (u = σ, d = σ⁻¹, ud = average) FAILS reading 3 for both nucleons (χ_(2,1) = −0.09198 p, −0.18200 n). Its sign changes exactly at q*² + q*⁻² = 1 + 2cos(2π/7), q* = 1.27890, above q₀. Every bar-swapped template (u = σ⁻¹, d = σ) passes for both nucleons, under every pair rule. The two flavour-blind templates also pass.
- **With the gluon pair σ₀σ₀:** no template passes for both nucleons.
- **Placement varied too:** the corpus template has 4/8 admissible placements per nucleon; the builder's is not one of them. So reading 3 constrains sign map and placement jointly, not the template alone.
- **Tension, unresolved:** this bean's 2026-09-05 "swap refuted" rests on a comparison with measured binding data, which cannot select under the no-fitting rule. Reading 3, the ruled derived test, points to the swap at k = 0 and the builder placement. This is an owner decision. The bean stays open.

## 🟧 OWNER RULING 2026-10-12 — quark sign map: option 4, derive it, do not pick it

Asked in the six-part frame on PR #7718 (comment 6130340849). The four options were: 1 keep S+ (status quo); 2 adopt the swap S− (u = σ⁻¹, d = σ), which passes reading 3 at the builder placement; 3 keep S+ and move the letters to placement 011 or 100; 4 pick nothing by hand. **The owner chose 4.** The quark sign map and the letter placement must be outputs of the γγ construction plus reading 3 at every tower level (`qou-ales`), not a template choice. The template stays open and nothing is re-scored. The dashboard knowingly keeps scoring an element that reading 3 rejects until a derivation lands. The 2026-09-05 data-based "swap refuted" in `qou-y2np` is a comparison with data, so it counts as a selection neither way. This bean stays open (rule 13a). Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`FallbackTierWindowZeroingAndPerGeneratorGroupedVolume.lean`, `CanonicalBraidLinkingNonUniformityAndMirrorSlopeFlip.lean`, `SymmetryEnergyBarBranchContinuumAndBetaBlindness.lean`) and verified at 50 dps in `computations/probes/fallback_tier_grouped_volume_braid_linking_mirror_slope_symmetry_branch_probe.py` (`computations/probes/fallback-tier-grouped-volume-braid-linking-mirror-slope-symmetry-branch-probe.witness.json`, `allPassed = true`). Opened PR #8321 (`ready: cde173d67efbd687c4f51cce6847a870b6c300f4`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8321, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
