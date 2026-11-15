# Results: torus-knot electron σ₀^m σ₁^t (fallback a)

Pre-registration: `preregistration.md` (commit 0823f764c57). Witness: `h2-torus-electron.witness.json`.
Checks: K0 (the trefoil reproduces χ_(2,1) = −1) PASS, and P1 (level-6 sign from the closed form, all
40 atoms) PASS.

## Outcome (i)

Some H₂ cells pass reading 3 at every level 1–12. Every passing cell is listed below. Nothing is chosen
among them.

**Atoms passing levels 1–6:** only m = 7 and m = 9 with t = +1, for both nucleons V³ and V⁶. That is
exactly the hand prediction recorded in the pre-registration (negative for m = 3, 5, positive for 7, 9).

**H₂ cells passing every level** (both nucleons give the same pattern):

| electron | atom 2 | bare | V@4 | V@5 | V²@4 | V²@5 | V³@4 | V³@5 |
|---|---|---|---|---|---|---|---|---|
| m = 7, t = +1 | pe | ✓ | ✓ | – | ✓ | – | ✓ | ✓ |
| m = 7, t = +1 | ep | ✓ | – | – | – | – | ✓ | ✓ |
| m = 9, t = +1 | pe | ✓ | ✓ | – | ✓ | – | ✓ | ✓ |
| m = 9, t = +1 | ep | ✓ | ✓ | – | ✓ | – | ✓ | ✓ |

## What this does and does not show

1. **The level-6 obstruction is a threshold in m, not a ban on torus electrons.** The (3,3) bracket
   χ_(3)(e) + χ_(2,1)(p)·χ_(2,1)(e) grows like q^{m+1}, so at q₀ it turns positive between m = 5 and m = 7.
   The run stopped at m = 9 by pre-registration. The bracket's growth suggests every larger odd m with
   t = +1 also passes level 6, but that was not computed. The passing set is a tail, not a single knot.
   Naming T(2, 7) as "the" electron would be selection against the target.
2. **The rule is chiral here.** Every mirror (m < 0 with t = −1) fails, and so does every t = −1
   stabilisation. Only right-handed torus words pass. This is a real mirror asymmetry. It is unlike
   fallback (b), where W = (σ + σ⁻¹)/(q[2]) is mirror-symmetric (see `h2_weak_vertex_electron/results.md`).
3. **The threshold depends on q₀.** It sits where q^{m+1} overtakes 1.994·(q^{m−2} + q^{2−m})/[2], so a
   different pin would move it. This is a property of the rule evaluated at q₀, not a derived integer.
4. **The electron alone fails reading 3 on its own three strands** (T1, levels 2–3), for all 20 words.
   The pre-registration did not make T1 a gate for T3, and the H₂ word closes from the top, where the
   first three levels are the nucleon's strands. Whether "the electron must pass by itself" is part of the
   rule is an owner question, not something this run decides. If it is, no torus electron survives.
5. **Bonding is not forced.** The bare H₂ passes in every cell, and several bonds (V, V², V³) pass too.
   The bond picture is less sharp than with the T_w0 or γγ electron, where only V³ passed.

## Procedure note

The first run gated T3 on T1, which the pre-registration does not do. That run was discarded before any
H₂ number was looked at, the gate was removed, and the run was repeated. Stage 1 (T1, levels 1–6) is
identical between the two runs.
