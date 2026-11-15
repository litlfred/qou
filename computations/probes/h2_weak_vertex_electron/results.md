# Results: γγ electron dressed by the weak vertex (fallback b)

Pre-registration: `preregistration.md` (commit b5b044aa3ac). Witness: `h2-weak-vertex-electron.witness.json`.
Checks: K1 (χ_(2)(W) = q⁻¹ = 0.9009) PASS, and P1 (level-6 sign from the closed form, all 84 atoms) PASS.

## Outcome (i), and it changes nothing

- **T1:** 36 of 84 electrons pass, namely every dressing (all j, both W and W′) of V³ and V⁶ and none of
  V, V², V⁴, V⁵. That is the same set as the undressed γγ electron (`h2_gg_atom`).
- **Atoms:** all 36 pass levels 1–6.
- **H₂:** for all 36 electrons and both orientations, exactly three cells pass every level: the bare
  molecule, V³ at s = 4 and V³ at s = 5. V and V² never pass. That is the same pattern as the undressed γγ
  electron and the T_w0 electron.

## Why the dressing cannot matter: an identity found during the run

With σ⁻¹ = σ − h (the Hecke relation):

  W = q⁻¹(2σ − h)/[2] = (σ + σ⁻¹)/(q[2]),   W′ = σP_L + σ⁻¹P_R = q²·W.

Both identities were checked symbolically (the sympy difference is 0). So:

1. **W is mirror-symmetric.** It is the average of a crossing and its mirror. The pre-registered
   "chirality report" (`chirality_W_vs_Wp_differs` in the witness) says the characters differ, but they
   differ only by the factor q² = 1.2321. That is visible directly: χ_(3) 0.8117 → 1.0 and 1.0 → 1.2321.
   **This is a rescaling, not chirality.** An earlier chat message called it chiral; that was wrong and
   has been corrected there. The claim was not written anywhere else.
2. **A positive rescaling cannot change any reading-3 sign**, so W and W′ must pass and fail together,
   and they do.
3. The dressed electron is still a different element from the nucleon: χ_(2,1) = 1.809 instead of 1.994
   for V³, because σ + σ⁻¹ ≠ σ.

## Consequence

In this form, the weak vertex gives no new electron and no handedness. The fallback the owner named, (a),
is in `../h2_torus_electron/`. There, right-handed torus words σ₀^m σ₁ with m = 7 and m = 9 pass and every
mirror fails.
