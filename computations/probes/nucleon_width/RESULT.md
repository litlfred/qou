# Result: nucleon width as Im of the complex volume (bean qou-zslg)

Computed 2026-11-22 after the preregistration in `PREREGISTRATION.md`. Tool: SnapPy 3.3.2 with
high-precision geometry (about 64 digits), not float64. Script `cs_borromean_probe.py`, output
`result.txt`.

| manifold | cusps | Vol | CS |
|---|---|---|---|
| Borromean complement L6a4 | 3 | 7.3277247534177521… | −1.5 × 10⁻⁶⁵ |
| proton braid closure + axis (L12n2208) | 4 | — | −4.0 × 10⁻⁶⁵ |
| neutron (mirror) closure + axis | 4 | — | −3.7 × 10⁻⁶⁵ |

The proton and neutron manifolds are isometric (SnapPy `is_isometric_to`: True).

**Claims against the preregistration.**
1. **Confirmed.** The proton and neutron closures give the same CS. They are isometric, and the
   Borromean rings are amphichiral, so CS(p) = CS(n) ∈ {0, ½} mod 1.
2. **The value is 0.** Amphichirality restricts CS to the discrete set {0, ½}, and the computed value
   is 10⁻⁶⁵ away from 0 and ½ away from ½. So the choice is 0, and this does not rest on the last
   digits.
3. **Verdict, scope (a).** Under the reading width = Im Vol_ℂ = CS, the closure gives width 0 for
   both nucleons. That derives proton stability, but it also predicts a stable neutron, which is
   false (τ_n ≈ 879 s). So a closure-only reading cannot be the nucleon width. A width difference
   would have to come from decorations of the braid, the same conclusion issue #9002 reached for
   the mass.
4. No CS-to-width unit map is derived, so no lifetime is quoted.

**Not covered.** Claim 1 rests on standard 3-manifold topology (orientation reversal negates CS;
amphichirality) and on SnapPy's isometry check. It is not proved in Lean.

**Caveat.** SnapPy's `Braid:` manifold includes the braid axis (4 cusps), so the braid-word rows are
for the closure together with the axis. The bare closure is L6a4.
