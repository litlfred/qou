---
# 754x
title: 'Charge-symmetry tension: B_sym bond assignment (p-p=σ / n-n=σ⁻¹) over-breaks strong charge symmetry ~78%, drives spurious 3× ³H/³He split; real split is Coulomb (unwired)'
status: todo
type: task
created_at: 2026-06-30T17:28:17Z
updated_at: 2026-06-30T17:28:17Z
---


## Finding (2026-06-30, surfaced by ³H/³He critical-distance review)

The framework's p/n CHIRALITY/MASS assignment is **derived and fine**:
`flavor-split-substrate.md` gives `(m_n−m_p)/M_N = (q−1)²(1−q⁻⁴)/3 ≈ 1.293 MeV`
to 0.10%, no u–d input — a tiny **0.14%** p↔n asymmetry.

But the **inter-nucleon BOND** assignment flips the crossing SIGN
(`all_nuclides_wedderburn_spectral_v2.crossing_sequence`):
`p-p → (0,"pos")` (σ), `n-n → (0,"inv")` (σ⁻¹), `mixed → (0,"mix")`.
The crossing-sign flip is a **leading-order** Hecke effect, giving (dashboard
`_bond_type_L`, `α=E₀=4.186`):

    L_pp = 0.694    L_pn = 0.929    L_nn = 1.237    →   L_nn/L_pp = 1.78  (~78%)

So the strong core is **78% charge-asymmetric** — ~500× larger than the derived
0.14% p/n mass split, and it **contradicts experimental nuclear charge
symmetry** (V_nn ≈ V_pp to ~1%; the equality is *why* the real ³H/³He split is
Coulomb). Consequence:

    ΔB_sym(³H−³He) = α(L_nn − L_pp) = +2.27 MeV    vs    ΔB_AME = +0.76 MeV

B_sym gets the SIGN right but **3× too big** and via the **wrong mechanism**
(strong asymmetry, not Coulomb). The real ≈0.76 MeV is the textbook Coulomb
energy of ³He's two protons (`E_C ≈ (3/5)Z(Z−1)e²/4πε₀R ≈ 0.8 MeV`), and that
Coulomb term is **NOT wired** into the binding. Early work
(`binding_color_vs_charge_tn3he.py`) already concluded "split is CHARGE
(Coulomb), color ~2 orders too small" — consistent.

**Scope (a, not a declared bug):** the chirality/mass derivation stands; the
*bond-crossing-sign* assignment over-breaks strong charge symmetry. Either it is
a mis-calibrated past choice, or the model genuinely predicts a large strong
n-n/p-p asymmetry that experiment forbids — the ³H/³He case exposes it.

## How to work it (plan)

1. **Confirm + quantify (probe, no fit).** `binding_perblock_bond_type_a3.py` /
   a new probe: tabulate `L_pp, L_pn, L_nn` and the per-pair Markov-trace
   eigenvalues (σ vs σ⁻¹) at q₀; show the 78% gap is the σ/σ⁻¹ sign flip, and
   compute the implied strong charge-asymmetry vs the experimental ~1% bound and
   vs the 0.14% mass split. Witness it.
2. **Trace the assignment to its source.** Is `p-p→σ, n-n→σ⁻¹` a *derived* rule
   (from the p/n chirality knots) or an arbitrary convention? Grep
   `crossing_sequence` / `INTRA` provenance + any audit. Decide canonical vs
   artifact (corpus-grep checklist before declaring).
3. **Test the charge-symmetric-core hypothesis.** Recompute binding with a
   charge-symmetric strong core (e.g. `L_nn := L_pp`, or the magnitude-averaged
   `|σ|`-bond) and see if the residual mirror split collapses toward 0 — i.e.
   whether the strong asymmetry is spurious. Across ³H/³He, plus other mirror
   pairs (⁷Li/⁷Be, ¹³C/¹³N) if traces feasible.
4. **Wire the Coulomb term.** Add the EM-sector Coulomb energy
   `E_C(Z) = (3/5)·Z(Z−1)·α_EM·ℏc/R` (or the framework's α_EM `[2]_q(1−h²α)`
   realization) as an explicit charge term; check it supplies the ≈0.76 MeV
   ³H/³He split with a charge-symmetric strong core. Compare `B_sym` (current
   spurious-strong) vs `B_sym_cs + Coulomb` against AME on the mirror set.
5. **Disposition.** If (3)+(4) confirm: re-scope `B_sym`'s bond model
   (charge-symmetric core + wired Coulomb); audit doc + content note. If the
   strong asymmetry is genuinely derived: record it as a falsifiable model
   PREDICTION (large strong charge-symmetry breaking) that experiment
   constrains — and flag the ³H/³He tension explicitly. Either way: kill-switch
   = the mirror-pair residual after charge-symmetrising + Coulomb.

Owner-gated where it touches canonical compute (re-scoping B_sym bond types is a
production change). Exploratory probe steps (1–4) first; production rewire only
after owner sign-off.

## Progress — 2026-06-30 (steps 1, 3, 4 done; PR follow-up)

**Step 1 (quantify) — DONE.** `computations/probes/charge_symmetry_bond_probe.py`.
`L_pp=0.6945, L_pn=0.9292, L_nn=1.2370` → `L_nn/L_pp−1 ≈ 78%`. The bonds are
the bare crossing σ (p-p, eigenvalues `{q,−q⁻¹}`) and its inverse σ⁻¹ (n-n,
`{q⁻¹,−q}`). The 78% is ~570× the derived 0.14% p/n split and ~78× the ~1%
experimental CSB bound; drives a 3–4.5× over-split of the mirror pairs.

**Step 2 (provenance) — answered.** `atom_braid_word_3A` (mass_at_3A_proper.py:271)
documents p-p↦σ, n-n↦σ⁻¹ as "isospin-distinct"; the deprecated
`integer-lp-gluon.witness.json` shows the SDP (Gram-positivity feasibility)
*derived* p-optimum = σ, n-optimum = σ₀σ₁σ₁σ₀ (σ⁻¹-like) as the per-nucleon
STABILITY optima — so the sign split is SDP-grounded but coarse. The content
block `inter-nucleon-channel-color-tube.md` labels it the **flavor-only
majority-sign projection** of the 9-channel color-tube (gg) assignment, gated
on `conj:s5-so3-fiber-action` (the s5-so3 keystone). Not arbitrary; not yet
canonical.

**Step 3 (charge-symmetric-core / gg test) — DONE.**
`computations/probes/gg_production_bond_probe.py` (owner directive "build p and
n through gg production"). Gluons are flavor-blind, so the leading gg bond is the
single color-average σ_avg for every bond type: forcing it makes
`L_pp=L_pn=L_nn=0.9294` EXACTLY → the 78% collapses to 0 and all three mirror
ΔB_sym collapse to 0. The whole gap was the σ-vs-σ⁻¹ inter-crossing sign (intra
uud/udd chains cancel in the L ratio). Documented in the paper
(inter-nucleon-channel-color-tube.md, fourth-line evidence). PR #3175 (merged).

**Step 4 (wire Coulomb / kill-switch) — DONE.**
`computations/probes/coulomb_mirror_killswitch_probe.py`. Uniform-sphere
`E_C=(3/5)Z(Z−1)·α_EM·ℏc/(r0·A^1/3)` (r0=1.2fm, α·ℏc=1.43996 MeV·fm — standard,
not fit):

| pair | ΔE_Coul | CS-core+Coulomb | ΔB_AME | prod σ/σ⁻¹ | resid CS+C | resid prod |
|---|--:|--:|--:|--:|--:|--:|
| 3H-3He | +0.998 | +0.998 | +0.764 | +2.271 | +0.235 | +1.507 (6.4×) |
| 7Li-7Be | +2.258 | +2.258 | +1.644 | +6.812 | +0.614 | +5.168 (8.4×) |
| 13C-13N | +3.674 | +3.674 | +3.003 | +13.625 | +0.672 | +10.622 (15.8×) |

CS-core+Coulomb matches ΔB_AME to 22–37% (within the known uniform-sphere /
Nolen–Schiffer over-estimate for light nuclei — Coulomb runs slightly high),
vs production's 197–354% over-split. **Kill-switch PASSES**: the mirror split is
Coulomb on a charge-symmetric core, not strong CSB.

**Step 5 (disposition) — OWNER-GATED.** The probes confirm B_sym's σ/σ⁻¹ bond
split is a (a) scope-limited flavor-only-projection artifact; the canonical fix
is (gg charge-symmetric core via the color-tube W-matrix, keystone-gated) + a
wired Coulomb term. Re-scoping production `B_sym` is a canonical-compute change
requiring owner sign-off. Recorded; not applied.

## Step 5 disposition — DONE (scope A: Coulomb wired; strong core keystone-gated)

Owner approved the re-scope (option A — Coulomb now, defer strong core).

- **Coulomb wired (additive):** new canonical `computations/coulomb_energy.py`
  (`coulomb_energy_mev`, `mirror_displacement_mev`) + an `E_C` column in the
  mass-binding dashboard. Reported alongside the strong B-forms, NOT subtracted
  (they are calibrated against Coulomb-inclusive AME ⇒ global subtraction would
  double-count); E_C is cleanly separable only in the mirror-pair difference.
  Mirror visibility now first-class: ³H `E_C=0.00` vs ³He `E_C=1.00` MeV.
  **No strong-binding number changed; no witness migration.**
- **Strong-core charge-symmetrising DEFERRED (keystone-gated).** Replacing the
  flavor-only σ/σ⁻¹ bond with the flavor-blind gg core must use the full
  9-channel color-tube weight `W_{c₁c₂}` (gated on `conj:s5-so3-fiber-action`,
  the s5-so3 keystone — reduced this session to `bwS0 = d_q/D`). The bare-σ_avg
  stopgap is rejected because it zeroes the **derived 0.14% p/n flavor split**
  the owner directed be kept; the full W preserves it. So the strong-core rewire
  rides with the keystone, done once, not as an 840-witness stopgap migration.

Bean 754x is functionally complete: the σ/σ⁻¹ over-break is diagnosed (artifact),
the mechanism is confirmed (Coulomb on a charge-symmetric core), the EM term is
wired, and the strong-core fix is correctly gated on the keystone.
