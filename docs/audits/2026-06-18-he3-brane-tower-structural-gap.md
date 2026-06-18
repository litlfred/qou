# ³He structural gap of the per-generator brane-tower — diagnosis

**Date:** 2026-06-18
**Branch:** `claude/great-babbage-4vngb1`
**Thread:** the surviving empirical branch of `conj:brane-tower-z-habiro`
("the ³He gap is a structural deficit of the brane-tower formula at the
`A=3 / n₀=9` regime, not an operator-volume choice"). The six n⋆ families
are refuted; this doc isolates *why* ³He specifically overshoots.

## Finding (one sentence)

The per-generator brane-tower sum `Σ_i −Li₂^q(−|V̂_i^full|)` is **monotone
increasing in proton near-pole count**, so it predicts ³He *more* bound than
tritium — but ³He is the *less*-bound mirror member. The tower's Z-ordering is
**inverted** relative to the empirical binding.

## Evidence

Probe [`computations/probes/he3_brane_tower_structural_gap.py`] (mpmath 50 dps,
witness `he3-brane-tower-structural-gap.witness.json`), using the **production
bounded** `−Li₂^q(−z)` form (not Φ_q) and the exact production per-generator
`|V̂_i^full|` (`terms-2-3-atom-per-gen-mpfr-50dps.witness.json`):

| atom | Z,N | #near-pole gens (\|V̂\|>0.9) | tower Σ−Li₂^q | B_AME (MeV) |
|---|---|---|---|---|
| deuteron | 1,1 | 3 | 3.393 | 2.225 |
| tritium | 1,2 | 4 | 5.072 | 8.482 |
| ³He | 2,1 | 5 | 5.350 | 7.718 |

- **tower(³He) = 5.350 > tower(T) = 5.072** (Δ = +0.278), yet
- **B_AME(³He) = 7.718 < B_AME(T) = 8.482** (³He less bound by 0.764 MeV).
- `tower_ordering_opposes_binding: true`.

## Mechanism

The per-generator volume lists (production `full` channel) expose it directly.
Each proton contributes a near-pole pair `(|V̂|≈0.989, 0.971)`; each
`−Li₂^q(−0.989) ≈ 0.815`. The mirror pair differs only in proton/neutron count:

| atom | proton near-pole pairs | neutron near-pole entries |
|---|---|---|
| tritium (1p,2n) | **1** (gens 0,1) | 2 (the 0.976 entries) |
| ³He (2p,1n) | **2** (gens 0,1 **and** 3,4) | 1 |

³He carries the proton near-pole pair **doubled**. Because the tower is a *sum*
of per-generator terms that are individually large for near-pole (proton)
generators, it grows with proton count. Empirically the proton-rich member is
*less* bound (more Coulomb repulsion, fewer `nn`/`pn` attractive pairs at fixed
A) — so a binding contribution that increases with proton count has the wrong
sign of Z-dependence at A=3.

This is **structural and dilog-independent**: shown here in the bounded
`−Li₂^q` form, so it is not the Φ_q blow-up pathology
([`2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md`](2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md));
it is a defect of the **per-generator additive form** itself at A=3.

## Where the fix must live (direction, not a closure)

The defect is the *additive per-generator* treatment of the duplicated proton
near-pole structure. The two surviving structural findings of the conjecture
point the way — and notably do **not** add a seventh n⋆ fit:

1. **Pair-knot composite at closed shells** (`brane-tower-z-habiro.md`
   §"pair-knot operators are selected at closed shells"; Lean
   `lpDualActiveSetIncludesPairKnotAtMagicShells`). The operator-selection LP
   dual already selects a *composite* `σ_pp` / `σ_nn` knot at magic shells
   instead of summing separate per-generator terms. Treating the ³He proton
   pair as one composite knot operator — rather than two additive near-pole
   generators — is the structurally-motivated route to removing the
   double-count.
2. **Z↔N isospin symmetry is exact at the Markov-trace level**
   (`tr_M(σ_pp) = tr_M(σ_nn) = 0.0622`). So the residual T/³He asymmetry must
   come from a Z-dependent term *outside* the symmetric tower — physically the
   two-proton Coulomb energy, which is exactly what makes ³He the less-bound
   member. The per-generator tower has no such term.

**Open question for the branch.** Does replacing the duplicated proton
per-generator pair with the LP-dual-selected pair-knot composite (finding 1),
plus an explicit Z(Z−1) Coulomb term (finding 2's complement), restore the
correct T/³He ordering without per-atom retuning? That is the falsifiable next
probe; it is *not* an n⋆ level-selection ansatz (those are refuted), but a
change to the *operator content* of the tower at A≥3.

## Cross-references

- `computations/probes/he3_brane_tower_structural_gap.py` + `he3-brane-tower-structural-gap.witness.json`
- `content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md`
  (§"Structural conclusion", §"pair-knot operators … at closed shells",
  §"Z ↔ N isospin symmetry")
- `docs/audits/2026-06-17-refuted-ansatz-lemmas.md` (six refuted n⋆ families)
- `computations/terms-2-3-atom-per-gen-mpfr-50dps.witness.json` (exact |V̂_i^full|)
- AME2020 binding energies
