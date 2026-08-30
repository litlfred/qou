#!/usr/bin/env python3
"""
Probe — R is extensive at leading order, the count is DEGENERATE, and R is not one term.

Continues qou-ls86. `collective_term_sign_screen_regime_confined_probe.py`
established that on the well-bound regime (3519 nuclides, B_AME/A > 5) the missing
term `R(A) := B_AME/A - B_chain/A` is strictly positive and bounded. This probe
asks the structural question the confirmed step-7 functional poses.

Since `S = -sum log mu` is the archimedean functor (settled in qou-y0mc by
extensivity), any additive collective term must ITSELF be a sum of log
suppressions over some additional interface structure. So the target

    T(A,Z,N) := R * A / alpha        [dimensionless log-suppression budget]

should be proportional to the COUNT of whatever that structure is. That is a
shape test with exactly one free parameter (the overall scale), not a fit.

## Result 1 — extensive, and C(A,2) / surface excluded

    candidate count          mean ratio   rel. spread
    A-1   chain bonds            1.2197         9.7%
    A-2   2nd-neighbour          1.2341         9.9%
    A     nucleons               1.2062         9.8%
    3A    colour strands         0.4021         9.8%
    3A-1  braid generators       0.4035         9.8%
    floor(3A/2)+1  blocks        0.7998         9.8%
    C(A,2) all pairs             0.0271       110.1%
    A^(2/3) surface              6.0431        17.4%

`C(A,2)` is excluded at 110% — this upgrades the existing scaling screen from the
`A >= 24` band to the whole chart. Pure surface scaling is excluded at 17.4%.

## Result 2 — THE COUNT IS DEGENERATE. Do not read a winner off that table.

The six "good" rows differ by 0.2 percentage points, which is not a
discrimination: they are ONE fit expressed in different units. Rescaling each to
the `A` column at `A = 100`:

    A-1 -> 1.2075 | A-2 -> 1.2094 | A -> 1.2062
    3A  -> 1.2062 | 3A-1 -> 1.2066 | blocks -> 1.2077

All collapse to ~1.207. Any count linear in `A` fits identically, because over
this sample they differ only by a constant factor and an O(1) offset. **Reporting
"A-1 is tightest at 9.7%" as an identification would be over-reading** — the test
constrains the SCALING (extensive), not the STRUCTURE.

To discriminate among linear counts one needs an observable sensitive to the O(1)
offset — i.e. the light nuclei — and those are exactly the rows contaminated by
the two-nucleon defect. That is a real obstruction, not a gap in this probe.

## Result 3 — the 10% residual is not noise, and R is NOT one term

Subtracting the leading extensive term leaves a residual of range
`[-70.69, +15.64]` alpha with `sd 17.70`, against a leading term of `252.5` alpha
at `A = 208`. Its extremes are physically identified:

    most POSITIVE   A=90 Z=40 (N=50)      a shell closure
    most NEGATIVE   A=295 Z=118           the superheavy Coulomb limit

**Correlation does NOT identify which liquid-drop term this is**, and the numbers
say so plainly:

    -Z^2/A^(1/3)  Coulomb     r = +0.8271
    -A^(2/3)      surface     r = +0.7015
    -(N-Z)^2/A    asymmetry   r = +0.6886
    +A            volume      r = -0.7670

Every term correlates strongly because they are all monotone in `A` across the
chart and therefore mutually collinear. This is the SAME failure mode as the
count degeneracy in Result 2, and the same discipline applies: a single-term
Pearson `r` is not an identification.

## The framing conclusion

**"Find the missing collective term" is the wrong framing.** `R` is at least
three things:

1. an extensive piece, ~1.207 alpha per nucleon, scaling-identified but
   structure-degenerate;
2. shell structure (the N=50 peak);
3. a large negative piece at high `Z` consistent with Coulomb.

   > **CORRECTED 2026-08-17.** This item originally read "...consistent with
   > Coulomb — which the framework does not model **at all**." **That is false**,
   > and it was written without running the corpus-grep checklist. `def:coulomb-charge`
   > derives a Coulomb charge `Q = (1/2)(n_+ - n_-)` with `Coulomb/strong =
   > tanh(ln q0) = 0.103964`; `magic-shell-coupling-kappa`, `docs/coordination/alpha-em.md`
   > and three deprecated Coulomb/shell probes also exist.
   >
   > The corrected statement is sharper: on the framework's own words
   > `Q = 2Z + 3.4393e-04` (constant offset from the colour-weighted `pn` bond),
   > so the EM term is **linear in charge** while electrostatic energy is
   > **quadratic** — the shortfall runs 1.0x at 4He to 12.1x at 208Pb. The
   > framework has a charge; it has no charge-charge interaction energy.
   > See `coulomb_charge_is_linear_in_z_probe.py`.

Only (1) is plausibly a categorical object to derive. (2) and (3) are ordinary
nuclear physics absent from the construction, and no single derived term will
supply them. A search that treats `R` as one object is searching for something
that is not there.

## Scope

**Scope-(a) throughout.** Excluded as the LEADING scaling: all-pairs `C(A,2)`
and pure surface `A^(2/3)`. Established: the leading behaviour is extensive.
NOT established: which extensive count, which liquid-drop terms the residual
decomposes into, or that a categorical object supplies (1).

NO WITNESS: a subtraction over the committed AME2020 table plus ratio statistics;
the tables reproduce it.

Bean qou-ls86; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp
from _precision import set_compute_dps  # noqa: E402

ALPHA = "4.1859813632944758969"
WELL_BOUND = "5.0"

COUNTS = {
    "A-1   chain bonds": lambda A, Z, N: A - 1,
    "A-2   2nd-neighbour": lambda A, Z, N: max(A - 2, 0),
    "A     nucleons": lambda A, Z, N: A,
    "3A    colour strands": lambda A, Z, N: 3 * A,
    "3A-1  braid generators": lambda A, Z, N: 3 * A - 1,
    "floor(3A/2)+1  blocks": lambda A, Z, N: (3 * A) // 2 + 1,
    "C(A,2) all pairs": lambda A, Z, N: A * (A - 1) // 2,
    "A^(2/3) surface": lambda A, Z, N: A ** (2 / 3),
}
DROP = {
    "-Z^2/A^(1/3)  Coulomb": lambda A, Z, N: -Z * Z / A ** (1 / 3),
    "-A^(2/3)      surface": lambda A, Z, N: -A ** (2 / 3),
    "-(N-Z)^2/A    asymmetry": lambda A, Z, N: -((N - Z) ** 2) / A,
    "+A            volume": lambda A, Z, N: A,
}


def _mean(v):
    return mp.fsum(v) / len(v)


def _pstdev(v):
    m = _mean(v)
    return mp.sqrt(mp.fsum([(x - m) ** 2 for x in v]) / len(v))


def corr(xs, ys):
    mx, my = _mean(xs), _mean(ys)
    num = mp.fsum([(x - mx) * (y - my) for x, y in zip(xs, ys)])
    den = mp.sqrt(mp.fsum([(x - mx) ** 2 for x in xs])
                  * mp.fsum([(y - my) ** 2 for y in ys]))
    return num / den


def main() -> int:
    set_compute_dps()
    import mass_binding_dashboard as M
    L = M._bond_type_L()
    ame = M._ame_table()
    a = mp.mpf(ALPHA)
    Lpp, Lpn, Lnn = L["pp"], L["pn"], L["nn"]

    rows = []
    for (Z, A), v in ame.items():
        N = A - Z
        if A < 2 or Z < 1 or N < 1:
            continue
        B = mp.mpf(str(v[0]))
        if B <= 0 or B / A <= mp.mpf(WELL_BOUND):
            continue
        ch = a * ((Z - 1) * Lpp + Lpn + (N - 1) * Lnn)
        rows.append((A, Z, N, (B - ch) / a))

    print("R is extensive at leading order; the COUNT is degenerate; R is not one term.\n")
    print(f"  well-bound sample: {len(rows)} nuclides")
    print("  target T = R*A/alpha, the dimensionless log-suppression budget")
    print("  shape test with ONE free parameter (overall scale) — not a fit\n")

    print("## 1. Scaling\n")
    print("| candidate count        | mean ratio | rel. spread |")
    print("| ---------------------- | ---------: | ----------: |")
    for nm, f in COUNTS.items():
        r = [t / mp.mpf(f(A, Z, N)) for A, Z, N, t in rows if mp.mpf(f(A, Z, N)) > 0]
        m = _mean(r)
        print(f"| {nm:<22} | {mp.nstr(m, 8):>10} | {mp.nstr(_pstdev(r) / m * 100, 4):>9}% |")

    print("\n## 2. THE COUNT IS DEGENERATE — do not read a winner off that table\n")
    print("  rescaled to the 'A' column at A = 100:")
    line = []
    for nm, f in COUNTS.items():
        if "C(A,2)" in nm or "surface" in nm:
            continue
        m = _mean([t / mp.mpf(f(A, Z, N)) for A, Z, N, t in rows if mp.mpf(f(A, Z, N)) > 0])
        line.append(f"{nm.split()[0]} -> {mp.nstr(m * mp.mpf(f(100, 50, 50)) / 100, 6)}")
    print("    " + " | ".join(line))
    print("\n  All collapse to ~1.207: ONE fit in different units. The 0.2pp spread")
    print("  differences are not a discrimination. The test constrains the SCALING")
    print("  (extensive), not the STRUCTURE. Discriminating among linear counts needs")
    print("  the O(1) offset, i.e. the light nuclei — exactly the rows contaminated by")
    print("  the two-nucleon defect. A real obstruction, not a gap in this probe.\n")

    k = _mean([t / (A - 1) for A, Z, N, t in rows])
    resid = [(t - k * (A - 1), A, Z, N) for A, Z, N, t in rows]
    r = [v for v, _A, _Z, _N in resid]
    print("## 3. The residual is not noise, and R is NOT one term\n")
    print(f"  range [{mp.nstr(min(r), 6)}, {mp.nstr(max(r), 6)}] alpha,  sd {mp.nstr(_pstdev(r), 6)}")
    print(f"  leading term at A=208 is {mp.nstr(k * 207, 6)} alpha — the residual is a large"
          " fraction there")
    top = max(resid)
    bot = min(resid)
    print(f"  most POSITIVE  A={top[1]} Z={top[2]} (N={top[3]})   a shell closure")
    print(f"  most NEGATIVE  A={bot[1]} Z={bot[2]}          the superheavy Coulomb limit\n")
    print("| liquid-drop term           | Pearson r |")
    print("| -------------------------- | --------: |")
    for nm, f in DROP.items():
        print(f"| {nm:<26} | {mp.nstr(corr([mp.mpf(f(A, Z, N)) for _v, A, Z, N in resid], r), 6):>9} |")
    print("\n  CORRELATION DOES NOT IDENTIFY WHICH. Every term correlates strongly")
    print("  because all are monotone in A across the chart and therefore mutually")
    print("  collinear — the SAME failure mode as the count degeneracy in 2.\n")

    print("## Framing conclusion\n")
    print("  'Find the missing collective term' is the WRONG FRAMING. R is at least")
    print("  three things: (1) an extensive piece ~1.207 alpha/nucleon, scaling-")
    print("  identified but structure-degenerate; (2) shell structure (the N=50 peak);")
    print("  (3) a large negative piece at high Z consistent with Coulomb, which the")
    print("  framework does not model AT ALL. Only (1) is plausibly a categorical")
    print("  object to derive. A search treating R as one object is looking for")
    print("  something that is not there.")
    print("\n(no witness by design — subtraction over AME2020 plus ratio statistics.)")

    ratios = {nm: _pstdev([t / mp.mpf(f(A, Z, N)) for A, Z, N, t in rows if mp.mpf(f(A, Z, N)) > 0])
              / _mean([t / mp.mpf(f(A, Z, N)) for A, Z, N, t in rows if mp.mpf(f(A, Z, N)) > 0])
              for nm, f in COUNTS.items()}
    assert ratios["C(A,2) all pairs"] > 1.0, "all-pairs must be excluded"
    lin = [v for nm, v in ratios.items() if "C(A,2)" not in nm and "surface" not in nm]
    assert max(lin) - min(lin) < 0.01, "linear counts must be degenerate"
    return 0


if __name__ == "__main__":
    sys.exit(main())
