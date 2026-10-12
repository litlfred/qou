---
# qou-5zl1
title: 'Lean: trace factorisation tr_z(W_atom) = prod_bonds (z+d_k) * P_p(z)^Z * P_n(z)^N on a concrete braided Hecke tower'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:00:00Z
updated_at: 2026-10-12T19:00:00Z
parent: qou-0fmb
---
Stream 4 of the 2026-10-12 stalled-session split (coordinator session_01M5GA1LmsEf8tSMxFjMkmnn,
issue #7735, PR #7736). Work lands on PR #7612's branch
`claude/tau-bond-letter-vanishing-2026-10-10` so that #7612 and this land together.

Bean file created here because no `qou-5zl1` file existed on main, on #7612, or on #7736.
The coordinator ledger names the id; the relaunched agent's uncommitted draft was not found
on any remote branch.

## Plan (4 steps, commit after each)

1. Concrete braided-tower instance from the SchurWeyl `heckeIncl` colimit, at a general `z`.
2. Bond-letter law (`MarkovBondLetter.tr_bond_letter`) on that instance; check z = 0.
3. Trace multiplicative over disjoint strand blocks; block trace independent of offset.
4. Factorisation for the production atom words (combine with
   `ProductionChainBondProduct.tr_productionChain_braided`, on main).

## 2026-10-12: step 1 DONE

`QOU/SchurWeyl/HeckeColimitFamilyTrace.lean`, sorry-free. `ocneanuMarkovTraceAt U hqi`
turns ANY `HeckeCoset.MarkovTraceFamily K q qi z` (generic `[CommRing K]`, `q * qi = 1`)
into an `OcneanuTrace.MarkovTrace` on `HeckeLim`; `braidedTower_ocneanuMarkovTraceAt`,
`towerSpan_…`, `disjointBlock_…`. `zinv = z - (q - qi)` derived. Generalises
`HeckeColimitMarkovTrace` (which is ℝ, convention D only).
lean -DautoImplicit=false -s 65536 exit 0; #print axioms [propext, Classical.choice, Quot.sound].

**Not an existence theorem at arbitrary z.** It packages a family; the families proved to
exist are convention D (`ocneanuMarkovTrace`) and Wenzl level r (`wenzlMarkovTrace`). The
general-z Markov property of `ocneanuWeight q z` is open (`OcneanuWeight` says so).

## 2026-10-12: step 2 DONE

`QOU/Hecke/MarkovBondLetterColimit.lean`, sorry-free. `tr_bond_letter_colimit` (any family,
any z): `tr(a (c g_i + d) b) = (c z + d) tr(ab)`. z = 0 check: `…_of_z_eq_zero` gives factor
`d`, and `tr_bare_bond_colimit_of_z_eq_zero` gives 0 — the same scalars as
`TauBondLetter.tau_bond_letter` / `tau_bare_bond_eq_zero`. That agreement is in FORM only: τ
lives on `QOU.Hecke.IwahoriHecke`, the colimit on `QOU.SchurWeyl.Hecke`, and no z = 0 family is
built on the SchurWeyl tower. Convention D corollary `tr_bond_letter_conventionD`
(factor `c·q³/(q²+1) + d`, generic field). Axioms clean.
