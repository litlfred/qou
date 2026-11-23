---
id: qou-8fw2
title: "SM/Eightfold Worker Pkg 2 (Q-Gap-8): W_3*-Framed Hypercharge Y, Ordered Content-to-Braid Map, Lambda-Sigma Split & 2nd-Order GMO"
status: todo
type: feature
priority: high
parent: qou-sm8w
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-23T20:06:00Z
---

## Scope & Linked Legacy Beans (`qou-20sx`, `qou-3oi0`, `qou-wyy9`, `qou-yw3v`, `qou-ywsk`, `qou-c9uj`)

1. **Sync & Formalize Full `N=3` Eightfold Multiplet Infrastructure (`QOU/EightfoldWay/RankThreeMultiplets.lean`):** Sync `eightfold-open-problems.md` with `app:standard-model`'s proved `W_3 = pi_* L` (`z_3 = q^3/[3]_q`) bundle, formalize `dim Sym^3(W_3) = 10` (`qou-3oi0`) and `3 otimes 3 otimes 3 = 10 + 8 + 8 + 1` unconditionally on `W_3`, and complete the `eightfold-way.ts` `TODO` blocks (`hexagonal-weight-lattice`, `weyl-group-symmetry`).
2. **Per-Braid Framed Hypercharge `Y` & Ordered Content-to-Braid Map:** Lift bare single-fibre quark braids (`tbl:knot-particle-dictionary-table4-data`) to `(V_2, W_3^*)`-decorated framed braids so anti-up (`-2/3`) and down (`-1/3`) are separated categorically, and construct the parameter-free map from ordered flavour pairs (`bar{D}^0 = (-5,+3) != K^0 = (+3,-5)`) to `B_3` (`sm-gating-objects.md:71-91`).
3. **Diquark Spin-Isospin Split (`Lambda` vs `Sigma^0` 77 MeV), 2nd-Order GMO (6%), & `eta-eta'` Witten-Veneziano:** Evaluate the Hecke diquark projector difference (`I=0` antisymmetric `[2,1]` vs `I=1` symmetric `[3]`) in `H_3(q_0)` to break the weight-only `m_Lambda = m_{Sigma^0}` degeneracy without fitting, and compute the `O((q_0 - q_0^{-1})^2)` 2nd-order octet Casimir correction to GMO (`qou-c9uj`).
