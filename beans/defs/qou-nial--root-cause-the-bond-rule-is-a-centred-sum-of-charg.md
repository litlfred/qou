---
# qou-nial
title: 'ROOT CAUSE: the bond rule is a centred SUM of charges where Coulomb needs a PRODUCT — one substitution explains the whole arc'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T13:00:13Z
updated_at: 2026-10-04T15:24:13Z
parent: qou-v2om
---

## The finding

Owner, 2026-08-30: *"go ahead on the p->sigma, n->sigma^-1 identification"*.

**The identification is not wrong about protons and neutrons. It is wrong about
how two charges COMBINE.** One substitution explains every failure on this arc.

Producer: `computations/probes/level3_bond_charge_rule_probe.py`, 6/6.
Lean: `QOU/MassTheory/BondChargeRule.lean`, sorry-free, generic CommRing.

## What the corpus assigns

`torus-hopf-stability-proof`: **Q(proton) = +1, Q(neutron) = 0.**
`prop:skein-crossing-asymmetry`: the per-crossing correction is
`delta = q - (q + 1/q)/2 = h/2`, applied *"between composites of the same charge
relative to a mixed-charge baseline"* -- **two-valued**.

## What the implementation computes

`closed_form_tau_M.interface_factor`, relative to the mixed-charge baseline
`f_pn`, measured at the canonical proton pin:

    pair   Qi+Qj  Qi*Qj   implementation            centred SUM               PRODUCT
    pp      2.0    1.0    +0.10453014939781965772   +0.10453014939781965772   +0.10453...
    pn      1.0    0.0     0.0                       0.0                       0.0
    nn      0.0    0.0    -0.10453014939781965772   -0.10453014939781965772    0.0

**The implementation is EXACTLY `(Q_i + Q_j - 1) * h/2`** -- the CENTRED SUM --
to the last digit. Coulomb is `Q_i * Q_j * h/2`. The two **agree on pp and pn**
and **differ ONLY on nn**: the sum rule charges two neutral objects `-h/2`, the
product rule charges them `0`. Two neutrals have no Coulomb interaction, so `0`
is the physical value.

**One bond. That is the entire defect.**

## Why it explains the whole arc

Summed over the complete graph:

    sum rule      SUM_{i<j} (Q_i + Q_j) = (A-1) * Z     LINEAR in Z
    product rule  SUM_{i<j} Q_i * Q_j   = Z(Z-1)/2      QUADRATIC

- **qou-1pig** `f_pp - f_nn = h`: `sumRule_like_pairs_differ` gives `2c = h`.
  Under the product rule `nn` sits ON the `pn` baseline
  (`prodRule_like_pairs_are_strong_baseline`), so the STRONG channel becomes
  charge-symmetric and the only charge dependence left is on `pp` -- which is
  exactly what an electromagnetic term should be.
- **qou-dhsn** the A-only Coulomb channel and the `2Z` strong channel: the
  crossing counts are linear in Z **because the bond rule is a sum**.
- **CrossingCountAffine**'s degree gap: same fact, and this is its source.
- **qou-vudb** the A^0 mirror scaling.

`no_scaling_of_sumRule_is_prodRule` proves no multiple of the sum-rule total is
the product-rule total, quantifying over the coefficient FIRST.

## 🛑 What it does NOT fix — and the numbers say so

Measured mirror exponents over 20 odd-A pairs, A = 3..41:

    sum rule      (A-1)(Z-N)          p = 1.1137411
    product rule  [Z(Z-1)-N(N-1)]/2   p = 1.1137411     <-- IDENTICAL
    Coulomb shape (A-1)/A^(1/3)       p = 0.78040779

**For mirror pairs specifically the two rules have the SAME A-scaling**, because
at `Z - N = 1` both totals are proportional to `A - 1`. So the product rule is
**not** a fix to the mirror exponent. Its gain is structural -- `nn` on the
baseline, charge symmetry of the strong channel, and a `Z(Z-1)` multiplicity
that exists at all -- not numerical.

The remaining gap is the `1/R` of a Coulomb energy with `R ~ A^(1/3)`, a
GEOMETRIC input the bond picture does not carry. **Necessary, not sufficient**,
and do not report the product rule as closing the mirror splitting.

## Scope

Lean identities exact over a generic CommRing, for ANY charges; `Q(p)=1,
Q(n)=0` enter only in the specialised corollaries. Probe scope-(a).

**Nothing refuted.** `prop:skein-crossing-asymmetry`'s own wording is
two-valued and is what the PRODUCT rule realises; it is the three-valued ladder
in the implementation that does not follow from it. Nothing wired -- changing
`interface_factor` moves `tr_M` for every atom with an nn interface, i.e. the
whole binding table, and Phase 5q's 1e-49 closed-form validation is against the
current convention.

Parents: qou-1pig, qou-dhsn, qou-vudb.



---

## 🛑 MEASURED (owner: "go") — the product rule LOSES on the dashboard. Do NOT switch.

Producer: `computations/probes/bond_rule_dashboard_comparison_probe.py`, 5/5.
Both rules through the Sec.10a log form on the chain assembly, 12 nuclei
2H-56Fe, against AME2020.

### 1. The product rule is WORSE on absolute binding

    mean |ln(model/AME)| over 12:   SUM 0.808072    PROD 0.939762

Moving `f_nn` onto the `pn` baseline **removes** binding from every nucleus
with an nn bond, and the model is already short. That is a measurable
regression, not a wash.

### 2. Its A=3 mirror agreement is a coincidence — the same trap as qou-vudb

    pair      A   observed        SUM (ratio)          PROD (ratio)
    3He/3H    3   -0.76375488   -1.7470732 (2.29x)   -0.78294409 (1.025x)
    7Be/7Li   7   -1.6442398    -1.7470732 (1.06x)   -0.78294409 (0.476x)

Under the chain the product rule's mirror difference is
`(Z-N)(B_pp - B_baseline)` — a **CONSTANT** for odd-A mirrors, flat in A,
exactly like the sum rule. It is **identical at A=3 and A=7** while the observed
splitting has doubled. **Do not quote the 1.025x as a win**: a flat line
crossing a rising curve.

### 3. Both rules are ~3x short on absolute binding for A >= 4

Ratios 0.28-0.35 from 4He to 56Fe under either rule. That is the extensivity
problem (`qou-brng`) — the chain carries only A-1 bonds — and **no bond-rule
change can reach it.**

## Recommendation

**Do not switch `interface_factor`.** It would trade a measured regression in
absolute binding for a structural improvement whose numerical benefit does not
survive past A=3, while leaving the 3x shortfall untouched.

The structural finding **stands**: the sum-vs-product substitution is a correct
and complete diagnosis of why the arc's four failures all look alike. It is a
**diagnosis, not a repair** — the assembly is short by 3x independently, and
that is the thing to attack next.

Scope-(a): a measurement under ONE assembly (the chain). It does not refute the
product rule structurally; it prices it.


---

## 🛑 MEASURED (owner: "go") — the product rule LOSES on the dashboard. Do NOT switch.

Producer: `computations/probes/bond_rule_dashboard_comparison_probe.py`, 5/5.
Both rules through the Sec.10a log form on the chain assembly, 12 nuclei
2H-56Fe, against AME2020.

### 1. The product rule is WORSE on absolute binding

    mean |ln(model/AME)| over 12:   SUM 0.808072    PROD 0.939762

Moving `f_nn` onto the `pn` baseline REMOVES binding from every nucleus with an
nn bond, and the model is already short. A measurable regression, not a wash.

### 2. Its A=3 mirror agreement is a coincidence — the same trap as qou-vudb

    pair      A   observed        SUM (ratio)          PROD (ratio)
    3He/3H    3   -0.76375488   -1.7470732 (2.29x)   -0.78294409 (1.025x)
    7Be/7Li   7   -1.6442398    -1.7470732 (1.06x)   -0.78294409 (0.476x)

Under the chain the product rule's mirror difference is
`(Z-N)(B_pp - B_baseline)` — a CONSTANT for odd-A mirrors, flat in A, exactly
like the sum rule. IDENTICAL at A=3 and A=7 while the observed splitting has
doubled. Do not quote the 1.025x as a win: a flat line crossing a rising curve.

### 3. Both rules are ~3x short on absolute binding for A >= 4

Ratios 0.28-0.35 from 4He to 56Fe under either rule. That is the extensivity
problem (qou-brng) — the chain carries only A-1 bonds — and NO bond-rule change
can reach it.

## Recommendation

DO NOT switch `interface_factor`. It would trade a measured regression in
absolute binding for a structural improvement whose numerical benefit does not
survive past A=3, while leaving the 3x shortfall untouched.

The structural finding STANDS: the sum-vs-product substitution is a correct and
complete diagnosis of why the arc's four failures all look alike. It is a
DIAGNOSIS, NOT A REPAIR — the assembly is short by 3x independently, and that is
what to attack next.

Scope-(a): a measurement under ONE assembly (the chain). It does not refute the
product rule structurally; it prices it.

## 2026-09-05 — confirmed, and it is combinatorial before it is algebraic

`computations/qbeta/qbeta_chain_cannot_carry_coulomb_or_surface_probe.py`
(8/8, 2548 nuclides). The sum-vs-product diagnosis is right, and it has a
shorter statement that needs no letters at all:

**A path has `Z-1` proton-proton edges. There are `Z(Z-1)/2` proton pairs.**
The chain therefore carries `2/Z` of the Coulomb interaction — 100 % at Z=2,
25 % at Z=8, 10 % at Z=20, 7.69 % at Z=26, 4 % at Z=50, **2.44 % at Z=82**.
Coulomb is quadratic in `Z`; a path's edge count is linear. No choice of bond
letters and no scale factor produces a `Z^2` term out of `Z-1` edges, so this
cannot be repaired inside the chain — the *edge set* has to change.

**The surface term is the same defect.** A path's interior degree is the
constant 2, so its endpoint deficit is `A`-independent: there is no `A^(2/3)`
in it at any `A`, for the same reason. `qou-3wvl`'s alpha-cluster ratio law
(~2 % for n<=2, drifting +13 % by 16O) is that seen from the cluster side.
So Coulomb and surface are ONE defect: a 1-D chain standing in for a
saturating 3-D packing.

**And Coulomb is bigger than this arc reported.** The marginal correlation
`-0.044` was read as "essentially absent"; fitted JOINTLY with the other two
SEMF shapes over the same nuclides the spans in `B` are asymmetry 361 %,
surface 154 %, **Coulomb 67 %** — a ranking of 3 : 1.8 : 1, not 18 : 4 : 1,
with joint `R^2 = 0.927`. Marginal correlations cannot separate collinear
shapes, and heavy nuclei have large `Z`, large `N-Z` and large `A` together.
That reading is retracted.

## 2026-09-05 (later) — generalised and CLOSED as a route: `qou-556v`

The chain result above turns only on the chain's DEGREE, so it generalises to
every edge set the corpus has: by the degree-sum formula a graph with max degree
`d` covers at most `d/(Z-1)` of the proton pairs — 2.47 % (chain), 6.17 %
(max-contact deltahedra), **14.81 % even for close packing** at Z=82, and the
bound holds for the induced proton subgraph whatever the assignment.

Proved in `QOU/Hecke/BoundedDegreeCoulomb.lean` (4 decls, axiom-clean),
instantiated in `qbeta_bounded_degree_cannot_carry_coulomb_probe.py` (7/7).

**So the sum-vs-product diagnosis in this bean is right and is not repairable
inside the bond graph.** The only remaining door is a `Z`-dependent per-bond
energy: reproducing the SEMF term needs `eps(Z) >= 2 a_C (Z-1)/(d A^(1/3))`,
which spans 21.7x from 4He to 208Pb. That is a different form of law, not a
re-tuning of the letters. Tracking there: `qou-556v`.

## Progress Update (Round 65 — PR #8267)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8267`](https://github.com/litlfred/qou/pull/8267) (branch `feat/round65-radical-branching-bond-habiro-cusp-43c1`, Commit 1 `20143712c434683951cbe6f568953fd4a98454bc`, Commit 2 / Head `1ee46ede72413597113d706dd733554a25e327d5`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/MassTheory/BondChargeRule.lean (`sumRule_sub_prodRule_and_total_deficit`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/radical_branching_bond_habiro_cusp_probe.py` (`scriptHash: 949a90321cd5`) + `test/results/witnesses/radical-branching-bond-habiro-cusp.witness.json` (`allPassed: true`).
