# Result: electron placement in the γγ hydrogen capture (pre-registered ab4a8c43cc2)

Lean: `QOU/BraidsAndKnots/CapturePlacement.lean`, generic `Field`, lean-direct exit 0, no `sorry`,
axioms `propext, Classical.choice, Quot.sound` only. Probe: `placement_probe.py` (exact over ℚ(q)),
all pre-registered checks true: P1, P2, P3, P4, and capR = flip(capL) per orientation.

## Answer

No structural invariant among I1–I7 fixes the side of the proton the electron sits on. One exact
symmetry covers all of them: `Π = X^{⊗n} ∘ P_rev` (bit flip after strand reversal).

- `Π` commutes with the Jimbo `Ř` (`PiTwo_mul_Rch`), so it maps `σ_i ↦ σ_{n−2−i}`, keeping every
  crossing sign. On the two weight spaces of `HydrogenCaptureWeightSpace` it is the identity matrix
  (`gA_eq_gB_rev`).
- For every word, `F_R(O₊)(flip w) = −F_L(O₋)(w)`, `F_R(O₋)(flip w) = −F_L(O₊)(w)` and
  `S_R(flip w) = −S_L(w)` (`FplusR_flip`, `FminusR_flip`, `SR_flip`). This is the §46 mirror
  identity, now proved for all words, so for every photon weight and gluon arm. The corpus right
  capture `capR` has the same S as `flip capL` (`SR_flip_capL_eq_SR_capR`); the probe shows they
  agree per orientation as well, weighted and unweighted.
- `Π` keeps the inverse flags (`writhe_flip`), so the negative Hopf orientation of the capture
  cannot pick a side (I3).
- `Π` does **not** keep `T³` (sign flips), the weight `K = diag(q, q⁻¹)` (`PiTwo_mul_Kdiag`: it
  becomes `diag(q⁻¹, q)`), or the closing side. The right peel is Markov with `diag(q, q⁻¹)`
  (`OverStrandWeight.ptr_markov`). The left peel is Markov with `diag(q⁻¹, q)` (`ptrL_markov`, the
  same `q²`, so the same `z_D`) and not Markov with `diag(q, q⁻¹)` (`ptrL_other_not_scalar`). So for
  the fixed `Ř`, the Markov end and `K` form a pair, `u = K = q vector` (#7971) goes with it, and
  `Π` exchanges the two pairs. Weighted mirror identity: `S2R_K(flip w) = −S2L_{K⁻¹}(w)` (`S2R_flip`).

What this means. Within the class {letters, photon form, Hopf orientation, charge conservation,
Breit–Wheeler pair creation, `K`-weighted traces including the two-term Lagrangian trace}, the
absolute left/right placement is the same convention as the Markov end. The one binary that `Π`
does not erase is **relative**: is the electron at the Markov end of the tower, or at the far end?

- I4, charge conservation: the kept set {p, e⁻} is neutral in either order, so it gives no side.
- I5, Breit–Wheeler: pair creation places no letters (#8804 §50 P1). A cup-nesting argument
  would need the creation order of the e-pair relative to the quark pairs, and the corpus gives none.
- I6, tower end: in the corpus γγ atom (`GammaGammaAtom`), the nucleus is strand 0 and electron `k`
  is strand `k`. So new strands enter at the top, which is where the convention-D Markov property
  and conditional expectation act (sign-conventions table §1, fact 3). This puts the electron at
  the Markov end: `capL`, `S_B1 = −h²[3]_q/q²`. **This is chosen, not derived.** It is the corpus's
  tower convention, and the sign-conventions audit itself calls the tower step "a reading, not a
  theorem". No γγ letter, trace or conservation law forces it.

Scope: (b) for the class above. The invariant is `Π` with `K`, `T³` and the closing side carried
along (Lean, all words). Scope (a) beyond it: an ingredient outside that class (for example an
orientation on cups, or a non-reflection-covariant insertion) was not searched.

## Does it fix the n − p sign?

No. Two separate reasons.

1. Placement relative to the Markov end is fixed only by the tower convention (I6), not derived.
2. Measured, not pre-registered as a sign: with the corpus's own weight `K` inserted (as in t₁, t₂),
   the two placements are **not** opposite. `S2L + S2R(flip) = (q² − q⁻²)(F₊ − F₋)`
   (`S2L_add_S2R_flip`). At the proton pin:
   - `S_B2` is +0.7416 (capL) against +0.9623 (flip), the same sign.
   - With gluon σ₁: +0.2757 against +0.5207, the same sign.
   - With gluon V: −0.1349 against +0.0858, opposite signs.
   So "placement flips the sign" holds for the unweighted `B1` only. Under `K` the sign depends on
   the word, and no rule is read off.

None of these functionals is a mass. The map from `S` to "which nucleon is heavier" is not
established in the corpus, so no nucleon is declared heavier. Separately, #8804 §40-bis says the
p/n bit is already fixed by `def:down-quark` with #7971 (u = the K = q vector). The B1 mirrors of
§42–§46 used the swap that this convention excludes, and `Π` is that swap combined with strand
reversal.

## Open

- Whether "new strands enter at the Markov end" can be derived from the conditional expectation,
  for example "the nucleus is E(hydrogen)". Both peels are Markov with their own weight
  (`ptrL_markov`), so the peel alone does not decide.
- The ruled three-strand electron σ₀σ₁σ₀ and cup orientations were not tested.
- Corpus-grep: the corpus_search CLI is unavailable (platform not mounted), and beans are not
  mounted, so path 6 was not searched. Paths 1–4 were grepped for placement and Markov end.
  Hits: the sign-conventions table §1 (tower reading) and a homonym ("lepton placement" in
  `2026-11-21-qbeta-energy-map-spectator.md`, a factor placement in Q_β).
