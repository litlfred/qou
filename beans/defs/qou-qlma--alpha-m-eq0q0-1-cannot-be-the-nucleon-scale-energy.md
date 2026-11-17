---
# qou-qlma
title: 'alpha = m_e/(q0(q0-1)) cannot be the nucleon-scale energy: derived bound alpha <= B_AME(2H)/ln2 = 3.2094 MeV, actual 4.1860 (+30.43%)'
status: in-progress
pr: 8260
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:05:33Z
updated_at: 2026-10-10T07:01:43Z
parent: qou-v2om
---


Branch: claude/anchor-followups-2026-08-08. Grew out of the 2H cornering in
docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md
(section 10b), which eliminated the functional, the interface, coordination and
the anchor as routes. This is what was left, and it now has a number.

## The bound, derived in three steps

1. **z <= 1/2 for EVERY q.** The production Markov parameter is
   `z_m = 1/(q^1/2 + q^-1/2)`. For any real x > 0, AM-GM gives x + 1/x >= 2
   (equivalently x + 1/x - 2 = (x-1)^2/x >= 0), so with x = sqrt(q0),
   z_m <= 1/2 unconditionally. Wenzl positivity (q^1/2 + q^-1/2 > 2, which the
   corpus already requires) makes it strict. Measured:
   q^1/2 + q^-1/2 = 2.002722363860533, z_m = 0.4993203341836945.

2. **mu <= 1/2.** The admissible interface offset is d in [-h, 0] (sigma to
   sigma^-1), Lean-recorded as `mu_mem_Icc`, so mu = z + d <= z <= 1/2.

3. **Therefore B_bond = -alpha*ln(mu) >= alpha*ln 2**, for ANY q, ANY crossing
   convention, ANY crossing multiplicity, and ANY N in an SU(N) choice of z.

       alpha*ln 2  =  2.90150117984 MeV
       B_AME(2H)   =  2.224566      MeV      -- 30.43% BELOW the floor

   Rearranged, the deuteron is reachable at all only if

       alpha  <=  B_AME(2H)/ln 2  =  3.2093703363302 MeV
       alpha  as derived           =  4.1859813632945 MeV   (+30.43%)

This supersedes the earlier floor theorem (`mu_unreachable`), which was stated
at the actual z. The new one holds across the whole z family and is therefore a
statement about **alpha**, not about the interface.

## Why alpha is suspect on its own terms

alpha = E_0 = m_e/(q0(q0-1)). CAL-1 pins m_e; q0 is pinned by m_p/m_e. So alpha
is an ELECTRON-scale quantity built from a proton-derived q0 — calibrated for
the lepton tower and the nucleon mass, then applied UNCHANGED to nuclear
binding. Of the three uses, only the first two are calibrated. Nothing in the
chain licenses the third.

For scale, what one alpha is being asked to serve:

    SEMF volume    a_V  15.8 MeV     alpha/a_V = 0.265
    SEMF surface   a_S  18.3 MeV     alpha/a_S = 0.229
    SEMF asymmetry a_A  23.2 MeV     alpha/a_A = 0.180
    B/A plateau         8.5  MeV     alpha/    = 0.492
    deuteron B          2.2246 MeV   alpha/    = 1.882

UNVERIFIED OBSERVATION, recorded so it is not re-noticed as a discovery: 2*alpha
= 8.372 against the ~8.5 MeV B/A plateau is 1.5% off. Suggestive of a factor-2
site-vs-bond convention (cf. bean qou-9lew, "derive the site vs bond factor 2").
NOT pursued, NOT claimed — a 1.5% coincidence on a soft number is weak evidence.

## Also settled this round: the z derivation (the other half of the ask)

`markov-z-reconciliation.md` documents TWO Markov parameters and the corpus uses
the non-invariant one:

    z_J = (q-1)/(q^1/2+q^-1/2)^2  = 0.0274199478  -- Jones; makes tr a LINK INVARIANT
    z_m = 1/(q^1/2+q^-1/2)        = 0.4993203342  -- ALL mass/binding computations

Relation z_J = (q-1) z_m^2 verified to the arithmetic floor. The doc states
plainly that z_m "arises when we evaluate the trace on a single generator
sigma_i WITHOUT the writhe prefactor", and that the (q-1) in z_J is exactly what
"absorbs the writhe correction and makes J_L(q) independent of the braid
representative".

CONSEQUENCE, and it unifies a separate finding: **with z_m, tr_M is not a link
invariant — it depends on the braid REPRESENTATIVE.** That is the same defect as
the measured nucleon-ordering dependence (B varies by up to 2.88 MeV over
permutations of ['p']*Z+['n']*N, bean qou-c6gx). Two symptoms, one cause.

z_m is also specifically the Temperley-Lieb / SU(2) value, z = 1/[2]_{sqrt q}
with TL loop delta = q^1/2 + q^-1/2. Nucleons are 3-quark SU(3) objects, so
1/[N] at N=3 is the natural rival — but it goes the WRONG WAY:

    z_m = 1/[2]_{sqrt q}   0.499320   B_pp = 2.907195
    1/[2]_q                0.497287   B_pp = 2.924255
    1/[3]_{sqrt q}         0.332126   B_pp = 4.614624
    1/[3]_q  (SU(3))       0.328547   B_pp = 4.659315
    z_J (invariant)        0.027420   B_pp = 15.054817

Larger N -> smaller z -> MORE binding, and 2H needs less. No N helps, which is
step 3 of the bound above.

## Work

- [ ] Decide whether z_m or z_J is the licensed convention for MASS (not for the
      Jones polynomial). If z_J, every binding number changes by a lot and the
      braid-representative defect disappears; if z_m, the framework owes an
      argument for using a non-invariant quantity as a physical observable.
- [ ] Derive the nucleon-scale energy instead of reusing E_0. Acceptance: it is
      <= 3.2094 MeV and derived, not fitted to it.
- [ ] Check whether the same alpha is load-bearing in the lepton tower and the
      nucleon-mass path at a precision that would EXCLUDE a different nuclear
      alpha — i.e. is one-alpha actually a claim of the framework, or an
      unexamined default?
- [ ] Lean: strengthen `QOU.QBeta.InterfaceScalar` with the universal floor
      (z <= 1/2 by AM-GM => B >= alpha ln 2), superseding `mu_unreachable`.

## Item 3 RESOLVED: one-alpha is an unexamined default, not a claim

The question was whether alpha is pinned tightly enough elsewhere that a
different nuclear alpha would break something. Checked, and it is not.

**The nucleon mass does not use alpha.** `canonical_mass.proton_neutron_mass_mev`
returns the muon-anchored F_Bor identity from a witness, with — its own words —
"deliberately NO formula fallback (owner directive 2026-07-19)". The dashboard's
+1.351 ppb / +2.389 ppb agreement for m_p/m_n is therefore NOT evidence for
alpha; it is evidence for F_Bor. Changing the nuclear alpha cannot disturb it.

**The meson path does use alpha, and it fails.** `meson_mass_from_hecke.py`
builds `E_0 = m_e/(q0*(q0-1))`. Its witness records err_ppm of
143220, 431487, 586718, 630059, 651679, 671777, 954572, 886388, 988878, 998158
(i.e. 14% to 99.8%), with a single 1677 ppm (0.17%) outlier. That is not a
success pinning alpha either.

So nothing calibrated constrains alpha = 4.186 MeV. Its use as the
nucleon-nucleon interface scale is a default that was never examined.

## AND: the corpus already has TWO E_0 values in the same slot

    E_0 = m_e/(q0(q0-1))        = 4.185981 MeV   DERIVED from q0
    E_0_CALIBRATION_MEV = Q_b(n)= 0.782333 MeV   EXPERIMENTAL (CODATA 2022)
    ratio                       = 5.350636

Both are called "the E_0 calibration" and they are consumed by DISJOINT script
families:

    4.186  binding_canonical, derived_masses, meson_mass_from_hecke,
           bar_pairing_binding_observable, deltalambda/{borromean_3body,
           b4_nonsaturating, b4_multiplicative_cumulant, mu4_rhoF_cluster,
           s5so3_geometric_wlambda_a4}, probes/{hecke_channel_binding,
           binding_additive_linked_cluster, binding_triangle_3body}
    0.782  pyhecke/constants.py (the package default!), qou-mass/hecke_characters,
           canonical_tower, binding_block_multiplicative,
           phase5/phase3_triton_binding_convention_b

`mass_at_3A_proper`'s own CLI defaults to the 0.782 one
(`--E0 default=E_0_CALIBRATION_MEV`, help text "β-decay Q = 0.78233341") while
the binding path it feeds uses 4.186. That is a live inconsistency, not a
historical one.

EPISTEMIC NOTE, and it is the sharper half: 0.782333 is CODATA — an
EXPERIMENTAL input. Adopting it as E_0 converts a derivation into a third
calibration, which cuts against the framework's parameter-free claim. The fork
is therefore not just numerical.

## Where that leaves the deuteron

    required E_0 for B(2H) = AME   =  2.394018 MeV
    derived alpha  4.185981  ->  B = 3.889692   (+74.9%)
    CODATA  Q_beta 0.782333  ->  B = 0.726959   (-67.3%)

**Neither works, and the required value sits between them.** The bound from
`bond_energy_floor` (alpha <= 3.209370) excludes the derived alpha and admits
Q_beta, but Q_beta then undershoots by a factor of 3. So this is not a matter of
picking the other existing constant — a nucleon-scale energy still has to be
DERIVED, and its acceptance test is now two-sided:

    2.394018 MeV to reproduce 2H exactly, and <= 3.209370 MeV to be admissible
    at all.

- [x] item 3 — is one-alpha a claim? No: unexamined default, nothing pins it
- [ ] resolve the two-E_0 fork explicitly (which is THE E_0, and say so once)
- [ ] `mass_at_3A_proper --E0` default disagrees with the path it feeds — fix

## DECISIVE (2026-08-09): the title of this bean is too weak — NO alpha works

Asked why alpha exists at all and what the right object is. Both have sharp
answers, and together they redirect the whole investigation.

### Why alpha exists: forced, not chosen

Everything upstream of the Archimedean step is dimensionless — q0 is a mass
RATIO, and so are h, delta, z, chi^lambda, y_lambda and tr_M. Exactly one
dimensionful input exists in the whole framework (CAL-1, m_e). So the map to MeV
**must** have the form `m_e x f(q0)`. Its existence is not a modelling choice;
only the dimensionless factor f is.

    alpha = m_e * 1/(q0(q0-1)) = m_e * 8.19176117219 = 4.18598136329 MeV
    identity: q0(q0-1) = q0^2 * hbar_q,  hbar_q = 1 - 1/q0   (residual 7.2e-42)

so equivalently `alpha = m_e/(q0^2 * hbar_q)` — "the electron rest energy per
Planck tick" (`beta-decay-energy-scale.md`).

### Why NO choice of alpha can close 2H

Take a ratio of two quantities the framework predicts with the SAME alpha.
Alpha cancels exactly:

    framework   B(2H)/Q_beta = 0.929218723 / 0.188291 = 4.935014012
    nature      B(2H)/Q_beta = 2.224566   / 0.782333  = 2.843501463
    ratio of ratios                                   = 1.735541225   (+73.55%)

**That number is alpha-free.** It cannot be moved by any f(q0) whatsoever, so
replacing alpha with "the right object" cannot work — there is no right object.
Equivalently:

    alpha needed for 2H binding   = 2.39401762 MeV
    alpha needed for beta decay   = 4.15491628 MeV
    ratio                         = 1.735541225x

One alpha cannot serve both, and the derived alpha (4.18598) is within **0.75%**
of the beta-decay requirement. So alpha is essentially RIGHT where it is
validated, and the derivation in `beta-decay-energy-scale.md` is not the defect.

### What the right object actually is

Not alpha — the **dimensionless binding multiplier**. The framework computes

    ln(tr_free/tr_atom) = 0.929218723

and to reproduce AME at the derived alpha it must be

    B_AME/alpha = 0.531432419        i.e. a factor 1.748517 too large.

So the target for replacement is that number, and by the chain walk
(`docs/audits/2026-08-09-canonical-chain-walk-gaps-marked.md`) it is built from
exactly two things that are neither calibrated nor derived:

  * **GAP 1** — `z_m = 1/(q^1/2+q^-1/2)`, chosen over the link-invariant `z_J`
    with no derivation, and known (per `markov-z-reconciliation.md`) to be the
    convention WITHOUT the writhe prefactor, hence not a link invariant;
  * **GAP 2** — the interface templates `sigma`/`sigma^-1` assigned by electric
    charge, plus a hardcoded nucleon ordering.

### Consequences for this bean's earlier sections

- The "two E_0s" fork (4.185981 derived vs 0.782333 CODATA) is still a real
  inconsistency and the owner ruling stands (keep only derived) — but it is now
  a HYGIENE item, not a route to closing 2H. Neither value can close it.
- The two-sided acceptance test recorded earlier ("2.394018 to hit 2H,
  <= 3.209370 to be admissible") is **withdrawn as a target**: hitting 2.394018
  would break beta decay by the same 1.7355x. Retained only as a diagnostic.
- The Lean bound `alpha <= 3.209370` remains valid and remains a genuine
  contradiction with the derived 4.18598 — but its resolution is to fix the
  dimensionless number so the floor is not binding, not to lower alpha.

- [x] why does alpha exist — dimensionally forced, m_e x f(q0)
- [x] what is the right object — NOT alpha; alpha cancels. It is the
      dimensionless multiplier, target 0.531432 vs current 0.929219
- [ ] retarget onto GAP 1 (z_m) — the one factor that is neither calibrated nor
      derived and that moves the multiplier

## CORRECTION 2026-08-09: "z_m is the Temperley-Lieb / SU(2) value" is FALSE

Stated twice above and in the 2026-06-29 colour-weighting audit. Wrong, and
`docs/coordination/trace-convention-registry.md` says so explicitly — a
registry that exists precisely because convention-silent trace values kept being
compared. I did not read it before asserting.

    C  full-Hecke Ocneanu / Wenzl z-trace   z = 1/(q^1/2+q^-1/2) = 0.49932033418369445
       y_lambda at n=3 = (0.4153958, 0.2809296, 0.0227449)   <- PRODUCTION
    D  SU(2) / Temperley-Lieb (Jones)       z = q^3/(q^2+1)     = 0.61268803714646524
       y_lambda at n=3 = (0.5054042, 0.2472979, 0)

`D != C` is **Lean-proved**
(`QOU.BraidsAndKnots.BorromeanTraceConventionSplit.conventionD_ne_conventionC`);
they differ by 195.8 ppm on beta_Bor. So the framework's z is convention C and
the TL/SU(2) value is a DIFFERENT trace, not the same one.

The consequence is bigger than the misnaming. **Convention C has
y_(1^3) = 0.0227449 != 0**, whereas D has it exactly 0. That zero IS the row cap
`dim V_(1^3) = C(N,3) = 0 <=> N < 3` which `RowCapObstruction.lean` proves
sorry-free. So:

  * the mass trace does NOT carry the N=2 row cap;
  * the eightfold ledger's "framework supplies dim V = 2" is about the
    single-fibre tower, NOT about the trace the masses are computed with.

Also wrong above: the guess that the SU(N) family is `z = 1/[N]`. It is not —
the SU(N) weights are quantum dimensions (hook-content), and `1/[3]_q = 0.3285`
was a made-up rival, not SU(3).

## AND: convention C is not SU(N) for ANY integer N

New module `computations/y_lambda_su_n.py` (33/33 self-tests) implements the
real SU(N) weights,

    s_lambda  ∝  PROD_{(i,j)}  [N + j - i]_q / [h(i,j)]_q ,   normalised Σ y_λ f^λ = 1

validated by reproducing registry convention D EXACTLY at N = 2, including
y_(1^3) = 0 on the nose and the implied z = q^3/(q^2+1). At n = 3:

    N=2   0.5054042   0.2472979   0.0            == convention D
    N=3   0.3783707   0.2930825   0.0354643
    N=4   0.3226034   0.3090941   0.0592084
    C     0.4153958   0.2809296   0.0227449      <- production, between N=2 and N=3

Solving for the real N reproducing C's y_(1^3)/y_(3):

    N = 2.5995155

NON-INTEGER. The mass channel is not an SU(N) quantum-group trace at all; it
sits between SU(2) and SU(3). That reframes the eightfold "N = 3 problem": the
mass trace is not at N = 2 either, so the flavour channel is not being asked to
move from 2 to 3 — it is being asked to move from a non-SU(N) point to 3.

Nothing wired. The module is the weight function the flavour channel would need,
plus the measurement of where C actually sits.

## What happens under convention D — the impossibility is C-SPECIFIC

Asked directly, and it changes the headline. Registry channels:

    mass     definitional C, production D  -> DISPUTED (bean qou-3qrv, OWNER decision,
                                              agents explicitly forbidden from switching)
    binding  C / C                         -> agreed   <- where all of the above lives

So C is "out" for MASS but is current for BINDING. Recomputed the binding
channel under D (actual D weights on the 6-strand word, not just the closed
form; 7 of 11 blocks vanish under D, normalisation still exactly 1, and the
closed form tr_atom = tr_free*(z+d) still holds to 2.56e-42):

    convention   z            admissible B band       AME 2.224566
    C            0.4993203    [2.9071952, 5.1779672]  OUTSIDE, 30.4% below floor
    D            0.6126880    [2.0507097, 3.7977829]  INSIDE

**Under D the deuteron is reachable.** Required d = -0.0249256 = -0.1192*h,
comfortably inside [-h, 0]. The reason is exact: z_C = 1/(x+1/x) <= 1/2 by
AM-GM, which is what `markov_param_le_half` and `bond_energy_floor` rest on;
z_D = q^3/(q^2+1) = 0.6127 > 1/2, so the theorem simply does not apply.

CORRECTED IN THE LEAN AS A RESULT. The `bond_energy_floor` docstring claimed the
floor holds "for every N in an SU(N) choice of z (larger N shrinks z and
increases the floor)". FALSE — that assumed the family is z = 1/[N]. SU(2) IS
convention D at z = 0.6127 > 1/2. The theorems are unaffected; the scope claim
was wrong and is now marked. The impossibility is specific to convention C.

### But D is NOT better, and must not be adopted on this basis

    atom     B_C     errC %      B_D     errD %     B_AME
    2H     3.8897    +74.85    2.8332    +27.36    2.224566
    3H     9.0677     +6.91    6.6309    -21.82    8.481798
    3He    6.7969    -11.94    4.8839    -36.72    7.718043
    4He   11.9749    -57.68    8.6817    -69.32   28.295673
    6Li   20.0600    -37.30   14.5301    -54.59   31.994564
    7Li   25.2380    -35.69   18.3279    -53.30   39.244524

    mean |err|   C 37.39 %   D 43.85 %      mirror split: C 2.2708, D 1.7471 (nature 0.7638)

D fixes 2H's REACHABILITY and improves the mirror split, but under-binds
everywhere else and is worse on average. The registry's own rule applies with
full force here: "D is the value that lands on CODATA, which is precisely why
deciding by match is forbidden." The same forbids adopting D for binding because
it flatters 2H.

WHAT IS ACTUALLY LEARNED: the 2H impossibility I proved is a property of
convention C, not of the framework. That converts the headline from "no Markov
trace can bind the deuteron" to "**the production binding trace cannot, and a
neighbouring one can**" — which makes the convention choice load-bearing physics
rather than bookkeeping, and puts it in the same owner-decision class as the
already-disputed mass channel.

- [ ] does the binding channel's C assignment have a forcing argument, or is it
      inherited from the definitional doc the way the mass channel's was?


## 2026-10-10 — pointer

Tracked under carrier M8 (qou-n1dj) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.
