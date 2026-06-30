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
