---
# qou-8fw2
title: 'SM/Eightfold Worker Pkg 2 (Q-Gap-8): W_3*-Framed Hypercharge Y, Ordered Content-to-Braid Map, Lambda-Sigma Split & 2nd-Order GMO'
status: in-progress
type: feature
priority: high
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-23T21:46:57Z
parent: qou-sm8w
---

## Scope & Linked Legacy Beans (`qou-20sx`, `qou-3oi0`, `qou-wyy9`, `qou-yw3v`, `qou-ywsk`, `qou-c9uj`)

1. **Sync & Formalize Full `N=3` Eightfold Multiplet Infrastructure (`QOU/EightfoldWay/RankThreeMultiplets.lean`):** Sync `eightfold-open-problems.md` with `app:standard-model`'s proved `W_3 = pi_* L` (`z_3 = q^3/[3]_q`) bundle, formalize `dim Sym^3(W_3) = 10` (`qou-3oi0`) and `3 otimes 3 otimes 3 = 10 + 8 + 8 + 1` unconditionally on `W_3`, and complete the `eightfold-way.ts` `TODO` blocks (`hexagonal-weight-lattice`, `weyl-group-symmetry`).
2. **Per-Braid Framed Hypercharge `Y` & Ordered Content-to-Braid Map:** Lift bare single-fibre quark braids (`tbl:knot-particle-dictionary-table4-data`) to `(V_2, W_3^*)`-decorated framed braids so anti-up (`-2/3`) and down (`-1/3`) are separated categorically, and construct the parameter-free map from ordered flavour pairs (`bar{D}^0 = (-5,+3) != K^0 = (+3,-5)`) to `B_3` (`sm-gating-objects.md:71-91`).
3. **Diquark Spin-Isospin Split (`Lambda` vs `Sigma^0` 77 MeV), 2nd-Order GMO (6%), & `eta-eta'` Witten-Veneziano:** Evaluate the Hecke diquark projector difference (`I=0` antisymmetric `[2,1]` vs `I=1` symmetric `[3]`) in `H_3(q_0)` to break the weight-only `m_Lambda = m_{Sigma^0}` degeneracy without fitting, and compute the `O((q_0 - q_0^{-1})^2)` 2nd-order octet Casimir correction to GMO (`qou-c9uj`).

## Additional Lean Targets from Analyst 10 Audit
- Wire the **51 existing sorry-free `lean/QOU/Eightfold/*.lean` modules** (`GellMannOkuboIdentity`, `DecupletEqualSpacing`, `ColemanGlashowIdentity`, `OctetWeightDegeneracy`, `NonetMixingUnconstrained`, `FlavourColourDiscriminator`, `Sym2GateMultiplicity`, `FibreFunctorDimensionNotCategorical`) to `eightfold-way/*.ts` (`qou-8fl1`).
- Test the **3-strand hyperbolic meson clasp** (`(n_1, n_2) in {3,5,7}^2` + gluon clasp `sigma_0 sigma_1^{-1}`, `qou-3ttt`, `qou-qpj9`, bypassing `Vol=0` 2-strand torus knots while separating `K^0=(+3,-5)` from `bar{D}^0=(-5,+3)`).
- Resolve the `Lambda-Sigma^0` 77 MeV degeneracy via `I=0` vs `I=1` sub-projector inside `S^{(2,1)}` (`qou-pwz4`) and vector vs pseudoscalar nonet mixing (`NonetMixingUnconstrained.lean`).

## 2026-11-23 — Worker 20 (qou-8fw2) claimed on branch claude/sm8w-eightfold-wire-clasp-lambda-sigma-20261123: Starting Eightfold Way & SM Package 2 (Lean wiring, F = V_2 + W_3* sync, HyperbolicMesonClaspAndDiquarkSplit.lean, 80-dps pre-registered probe).
