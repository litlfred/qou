---
# qou-qlma
title: 'alpha = m_e/(q0(q0-1)) cannot be the nucleon-scale energy: derived bound alpha <= B_AME(2H)/ln2 = 3.2094 MeV, actual 4.1860 (+30.43%)'
status: todo
type: task
created_at: 2026-08-09T00:05:33Z
updated_at: 2026-08-09T00:05:33Z
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
