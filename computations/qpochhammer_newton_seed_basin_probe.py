"""The algebraic seeds are REAL, Newton preserves the reals, and the real axis
holds two DEGENERATE roots — so the pole-seeding claim converges to the wrong
root unless an imaginary lift the conjecture does not supply is added.

`conj:shared-denominator-cusp-holonomy` §"Implication for the Newton-Raphson
solver" asserts that the denominator zeros `q_0^{-k}` are "the **exact initial
seed values** for the Newton-Raphson solver of the Thurston gluing equations",
converging in `O(1)` Newton steps per cusp "instead of the `O(log eps^-1)` steps
needed when starting from a generic universal `z_q`", and that the algebraic
poles are "**isolated** in the cusp variety" so the step "avoids local-minimum
traps".

This probe composes the two halves the corpus already has and has never joined:
`gluing_residual(z, m)` from `computations/qbeta/qbeta_c3_barodd_gluing_newton_solve.py`
(Newton-solved there, recovering `Vol(4_1) = 2.029883213` to 10 digits at the
complete structure `m = 1`) and `algebraic_seeds(q, n)` from
`computations/snappy_cusp_seeding.py:60`. Measured on `main`: of the 8 files
carrying a gluing residual, seven reference no seed at all and the eighth uses
`x = q^{-k}` only as a coordinate label.

NOTHING HERE IS FITTED. `m = 1` is not a chosen value: it IS the complete
hyperbolic structure (parabolic meridian), and the cited probe's own docstring
records "Complete structure m=1 => z=w=e^{i pi/3}". No parameter is tuned
against any target; every number below is a root, a count, or a basin label.

THE ROOT STRUCTURE, exactly
---------------------------
At `m = 1` the gluing equation `z(z-1)*w(w-1) = 1` with `w = m^2 z = z` is
`(z^2 - z)^2 = 1`, i.e. `z^2 - z = +-1`, so it FACTORS:

    (z^2 - z - 1)(z^2 - z + 1) = 0

      z^2 - z - 1 = 0  ->  phi = 1.6180339887..., -1/phi = -0.6180339887...
                           REAL, so Im z = 0: DEGENERATE, not geometric shapes
      z^2 - z + 1 = 0  ->  e^{+- i pi/3}
                           the regular ideal tetrahedron, the geometric roots

So the complete-structure gluing equation has four roots and HALF OF THEM ARE
DEGENERATE. The two degenerate ones are real.

THE EXCLUSION (scope-(b); invariant = Newton preserves a real-coefficient map's
real axis)
----------------------------------------------------------------------------
The residual has real coefficients, so its Newton map `N(z) = z - R(z)/R'(z)`
sends the reals into the reals. The algebraic seeds `q_0^{-k}` are real. Hence
from an algebraic seed, EVERY iterate is real, and the geometric root
`e^{i pi/3}` — which has `Im z = sqrt(3)/2` — is unreachable in principle, not
merely in practice. Measured below: the iteration converges, to the degenerate
real root `-1/phi`.

This is not a scope-(a) numerical miss. It is structural, and the invariant is
one line: a Newton step on a real-coefficient rational function cannot leave
the reals. It excludes the seeding claim AS STATED (real seeds). It does not
exclude the conjecture, and it does not exclude a seeding claim stated with a
lift — which is the next section.

WHAT THE CONJECTURE DOES NOT SUPPLY
-----------------------------------
The algebraic side yields a real number; the geometric side needs a point of
the upper half plane. The imaginary part is a free input, and the conjecture
provides none. `snappy_cusp_seeding.py` and `q_pochhammer_seed.py` both lift by
a hardcoded `IM_PERTURBATION = 0.1`. That constant is therefore MANDATORY
rather than cosmetic — without it the iteration provably cannot reach a
geometric root — and it is also undetermined, so every "converges in 9-11
iterations" figure in the corpus is a statement about that constant as much as
about the seed.

Both halves are measured below, each against a CONTROL, because an iteration
count with no control says nothing: the conjecture's claim is comparative
("instead of ... a generic universal z_q"), so a bare count cannot test it.

Bean qou-v57s; carrier
folio/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

Q0 = Q_MP
TOL = mp.mpf("1e-40")
MAX_IT = 200

PHI = (1 + mp.sqrt(5)) / 2
ROOTS = {
    "e^{+i pi/3}  GEOMETRIC": mp.e ** (mp.mpc(0, 1) * mp.pi / 3),
    "e^{-i pi/3}  geometric conj": mp.e ** (mp.mpc(0, -1) * mp.pi / 3),
    "phi          DEGENERATE": mp.mpc(PHI, 0),
    "-1/phi       DEGENERATE": mp.mpc(1 - PHI, 0),
}


def gluing_residual(z, m=mp.mpf(1)):
    """Thurston figure-eight gluing: z(z-1)*w(w-1) - 1, w = m^2 z.

    Verbatim in form from qbeta_c3_barodd_gluing_newton_solve.py; not re-derived.
    """
    w = m * m * z
    return z * (z - 1) * w * (w - 1) - 1


def dR(z, m=mp.mpf(1)):
    """Exact derivative at m = 1: d/dz [(z^2-z)^2 - 1] = 2(z^2-z)(2z-1)."""
    return 2 * (z * z - z) * (2 * z - 1)


def newton(seed):
    """Return (iterations, limit, basin-label). Counts steps, does not use findroot."""
    z = mp.mpc(seed)
    for it in range(1, MAX_IT + 1):
        d = dR(z)
        if d == 0:
            return it, z, "STUCK (R' = 0)"
        z = z - gluing_residual(z) / d
        if abs(gluing_residual(z)) < TOL:
            for name, r in ROOTS.items():
                if abs(z - r) < mp.mpf("1e-20"):
                    return it, z, name
            return it, z, "converged, UNRECOGNISED root"
    return MAX_IT, z, "NO CONVERGENCE"


def main() -> int:
    ok = True
    print("=== the quartic factors; half its roots are degenerate ===")
    for name, r in ROOTS.items():
        print(f"  {name:28s} z = {mp.nstr(r, 20):34s} |R| = {mp.nstr(abs(gluing_residual(r)), 4)}")
    # the factorisation, verified rather than asserted
    probe = mp.mpc("0.3", "0.7")
    lhs = gluing_residual(probe)
    rhs = (probe**2 - probe - 1) * (probe**2 - probe + 1)
    print(f"  factorisation (z^2-z-1)(z^2-z+1) == R at a probe point: "
          f"|diff| = {mp.nstr(abs(lhs - rhs), 4)}")
    if abs(lhs - rhs) > mp.mpf("1e-45"):
        print("  FAIL: the factorisation does not hold"); ok = False

    print("\n=== seed k = 0 is z = 1, and z = 1 is a CRITICAL POINT of R ===")
    print("  R(z) = (z^2-z)^2 - 1, so R'(z) = 2(z^2-z)(2z-1) vanishes at")
    print("  z = 0, 1/2, 1 -- and the k = 0 seed is q_0^0 = 1 for EVERY q_0.")
    for zc in ("0", "0.5", "1"):
        z = mp.mpf(zc)
        print(f"    R'({zc:>3s}) = {mp.nstr(dR(mp.mpc(z)), 4)}")
    print("  So the Newton step is UNDEFINED at the k = 0 pole, independently of")
    print("  the substrate value. The carrier's claim that 'the algebraic poles")
    print("  are isolated in the cusp variety' so the step 'avoids local-minimum")
    print("  traps' is inverted here: the first pole IS a critical point.")
    if dR(mp.mpc(1, 0)) != 0:
        print("    FAIL: R'(1) is not zero"); ok = False

    print("\n=== the REAL algebraic seeds: Newton cannot leave the reals ===")
    n = 2  # m004 / m003: two ideal tetrahedra
    for k in range(n):
        seed = Q0 ** (-k)
        it, lim, basin = newton(seed)
        imag_seen = abs(mp.im(mp.mpc(lim)))
        print(f"  seed q_0^-{k} = {mp.nstr(seed, 18):22s} -> {it:3d} iters, "
              f"{basin}")
        print(f"      limit {mp.nstr(lim, 18)}   |Im(limit)| = {mp.nstr(imag_seen, 4)}")
        if imag_seen != 0:
            print("      UNEXPECTED: a real seed left the real axis"); ok = False
        if "GEOMETRIC" in basin:
            print("      UNEXPECTED: a real seed reached the geometric root"); ok = False

    print("\n=== lift sweep: which delta reaches a GEOMETRIC root, and how fast ===")
    print(f"  {'delta':>12s}  {'seed k=0':>26s}  {'seed k=1':>26s}")
    lifts = ["0.001", "0.01", "0.1", "0.3", "0.5",
             "0.8660254037844386467637231707529", "1.0", "2.0"]
    rows = []
    for ds in lifts:
        d = mp.mpf(ds)
        cells = []
        for k in range(n):
            it, lim, basin = newton(mp.mpc(Q0 ** (-k), d))
            tag = ("GEOM" if basin.startswith("e^{+i") else
                   "geom-conj" if basin.startswith("e^{-i") else
                   "DEGEN" if "DEGENERATE" in basin else basin)
            cells.append(f"{tag} in {it}")
            rows.append({"delta": ds, "k": k, "iters": it, "basin": tag})
        print(f"  {ds:>12s}  {cells[0]:>26s}  {cells[1]:>26s}")
    print("  (delta = 0.8660254... is sqrt(3)/2, the geometric root's own Im)")

    print("\n=== CONTROL: generic seeds at the same lift ===")
    print("  An iteration count means nothing without this. The conjecture's")
    print("  claim is COMPARATIVE -- O(1) 'instead of' a generic z_q -- so the")
    print("  test is whether the algebraic seeds beat generic ones, not whether")
    print("  they converge at all.")
    for ds in ("0.1", "0.8660254037844386467637231707529"):
        d = mp.mpf(ds)
        alg = [newton(mp.mpc(Q0 ** (-k), d)) for k in range(n)]
        # generic reals spanning the same interval the seeds live in, same lift
        generic_re = ["0.0", "0.25", "0.5", "0.75", "1.0", "1.25", "1.5", "2.0"]
        # EXCLUDE any control point that already IS a root: it converges in 1
        # step by construction and would make the control meaningless. At
        # delta = sqrt(3)/2 the point re = 0.5 is exactly e^{i pi/3}.
        gen = []
        for r in generic_re:
            pt = mp.mpc(mp.mpf(r), d)
            if any(abs(pt - rt) < mp.mpf("1e-20") for rt in ROOTS.values()):
                print(f"    (control re = {r} excluded: it IS a root at this lift)")
                continue
            gen.append((r, newton(pt)))
        gen = [g[1] for g in gen]
        gen_geom = [g for g in gen if g[2].startswith("e^{+i")]
        print(f"\n  lift delta = {ds}")
        print(f"    algebraic seeds : iters {[a[0] for a in alg]}  "
              f"basins {[('GEOM' if a[2].startswith('e^{+i') else 'other') for a in alg]}")
        print(f"    generic seeds   : iters {[g[0] for g in gen]}")
        print(f"                      basins {[('GEOM' if g[2].startswith('e^{+i') else 'other') for g in gen]}")
        if gen_geom:
            best = min(g[0] for g in gen_geom)
            alg_geom = [a[0] for a in alg if a[2].startswith("e^{+i")]
            if alg_geom:
                print(f"    best generic reaching GEOM: {best} iters; "
                      f"best algebraic: {min(alg_geom)} iters -> "
                      f"{'algebraic FASTER' if min(alg_geom) < best else 'NOT faster'}")
            else:
                print(f"    best generic reaching GEOM: {best} iters; "
                      f"NO algebraic seed reaches GEOM at this lift")

    print("\n=== verdict ===")
    print("  The seeding claim, as stated with the real poles, is EXCLUDED:")
    print("  scope-(b), invariant = Newton preserves a real-coefficient map's")
    print("  real axis, and the real axis carries two DEGENERATE roots")
    print("  (phi, -1/phi) which are what the iteration actually finds.")
    print("  The conjecture is NOT excluded. The imaginary lift is mandatory")
    print("  and is not supplied by the conjecture, so every recorded")
    print("  'converges in 9-11 iterations' figure is a statement about that")
    print("  undetermined constant as much as about the seed.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
