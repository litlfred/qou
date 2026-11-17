---
# qou-5zl1
title: 'Lean: trace factorisation tr_z(W_atom) = prod_bonds (z+d_k) * P_p(z)^Z * P_n(z)^N on a concrete braided Hecke tower'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:00:00Z
updated_at: 2026-11-15T13:30:00Z
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

## 2026-10-12: step 3 DONE

`QOU/MathlibExt/BraidedBlockShiftTrace.lean`, sorry-free, on any braided-tower Markov trace:
- `tr_blockProd`: blocks with `blk k ∈ H(3k+2) ∩ shifted(3k)` ⇒ `tr(blk 0⋯blk n) = ∏ tr(blk k)`
  (one application of `disjointBlock_of_braided` per block).
- `cyc_mul_g`: `c = g_s⋯g_{s+m-1}` satisfies `c g_t = g_{t+1} c` for `s ≤ t`, `t+1 < s+m`
  (braid + far commutation only). Hence `tr_wordVal_shift`: a word of affine letters
  `a•1 + b•g_{off+i}` has trace independent of `off`.
- `tr_blockProd_pn`: proton/neutron blocks ⇒ `P_p^Z · P_n^N`.
Inverse generators are affine letters (`ginv_letter`, from the quadratic relation).

## 2026-10-12: step 4 DONE — the factorisation is a theorem (for the production LAYOUT)

`QOU/Mass/AtomTraceFactorisation.lean`, sorry-free. `atomWord S isP wp wn d n` (A = n+2
nucleons; block k = proton/neutron word on strands 3k..3k+2; bond letters g_{3k+2} + d_k):

    tr_atomWord : tr(W_atom) = ∏_{k≤n} (z + d_k) · P_p^Z · P_n^N

on every braided-tower Markov trace; `tr_atomWord_colimit` on the Hecke colimit for any family;
`tr_atomWord_of_z_eq_zero` gives ∏ d_k (the τ form). Proof = `tr_productionChain_braided`
(main) + `freeWord_chainFrom` + `tr_blockProd_pn`. Axioms clean.

**Still NOT derived (stays open, so this bean stays in-progress per §13a until reviewed):**
- bond coefficient on g is 1; the d_k and the nucleon words are inputs (qou-qqm4);
- no Lean model checks that `atom_braid_word_3A` emits exactly these letters;
- existence of a Markov trace at arbitrary z on the Hecke tower is open (only D and Wenzl r);
- no binding energy / c_k.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Round 70 Formalization Progress (PR #8297)
- Formalized `QOU.Mass.AtomTraceFactorisation.tr_atomWord_const_bond` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/tl_uniqueness_threerow_factorisation_shadow_gluon_probe.py`, `scriptHash: 3ae4cba85e90`, Commit 1 `1f88e71305a6e71d41389edf2285daae1528f7d8`, Commit 2 / Witness `cfb7f3d64020483db10298c3ccdd51ae1d1bd7d8`, PR `litlfred/qou#8297`).
