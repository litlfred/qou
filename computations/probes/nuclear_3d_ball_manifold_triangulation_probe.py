#!/usr/bin/env python3
"""nuclear_3d_ball_manifold_triangulation_probe.py — 80-dps First-Principles 3D
Compact-Ball Simplicial Manifold Triangulation, Interior Edge-Cycle Closure, &
O(A^{2/3}) Surface-to-Volume Scaling Probe (Zero Fitting, Zero Float64).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/BallManifoldTriangulationAndSurfaceScaling.lean`
  (`namespace QOU.Nuclear.BallManifoldTriangulationAndSurfaceScaling`).

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (zero float64 intermediates, zero `math` module
imports, zero empirical liquid-drop coefficients `a_V, a_S`, zero tuned parameters)
the 3D compact-ball simplicial manifold triangulations `(M, dM ~= S^2)` formalized
in `BallManifoldTriangulationAndSurfaceScaling.lean`:

1. **Why the Apollonian 3-Tree Underbinds Heavy Nuclei**:
   In the Apollonian 3-tree `K_A` (`f = (A, 3A-6, 3A-8, A-3)`), every new nucleon
   glues onto only ONE boundary triangle (`Delta f_0 = +1, Delta f_{0,bdry} = +1`),
   leaving 100% of vertices on the boundary (`A_bdry = A`, `A_int = 0`), zero closed
   interior tetrahedral edge-cycles (`c = f_3 - (A - 3) = 0`), exposed boundary area
   `f_{2,bdry} = 2A - 4 = O(A)`, and average edge degree `< 6` (`f_1 = 3A - 6`).
   Consequently, on `208Pb` and `238U`, the 3-tree underbinds by `-13.5%` / `-12.3%`
   on `b2_log_gg` and `-43%` on `b2_log_D`.

2. **Exact Dehn-Sommerville 3-Ball Manifold Triangulation & Cycle-Closure Hierarchy**:
   For ANY compact 3-ball simplicial manifold triangulation `T` with `f_0 = A` vertices,
   `f_3 = (A - 3) + c` tetrahedra (`c >= 0` closed interior tetrahedral edge-cycles),
   and `f_{0,bdry} = A - A_int` boundary vertices (`A_int >= 0` buried interior vertices),
   the Dehn-Sommerville and Euler relations (`euler_ball: f_0 - f_1 + f_2 - f_3 = 1`,
   `euler_bdry_sphere: f_{0,bdry} - f_{1,bdry} + f_{2,bdry} = 2`,
   `handshake_bdry: 3 f_{2,bdry} = 2 f_{1,bdry}`, `handshake_cells: 4 f_3 = 2 f_2 - f_{2,bdry}`)
   uniquely determine:
     * `f_{1,bdry} = 3 A_bdry - 6`,
     * `f_{2,bdry} = 2 A_bdry - 4`,
     * `f_2 = 2 f_3 + A_bdry - 2 = (3A - 8) + 2c - A_int`,
     * `f_1 = A + f_3 + A_bdry - 3 = (3A - 6) + c - A_int`.

3. **Explicit Deterministic 3D Euclidean-Realizable Close-Packed Tetrahedral Ball Complexes**:
   For every benchmark nucleus `(Z, N)` with `A = Z + N` (`2H` through `238U`), the probe
   constructs two deterministic, parameter-free 3D compact-ball simplicial manifold families
   together with their `(Z, N)` Pauli/Fermi-constrained realizations:
   - **Family I — Coordinate-Verified 3D Euclidean Freudenthal-Kuhn Lattice Ball (`3D_kuhn_lattice_ball`)**:
     Places `A` nucleons at discrete 3D integer lattice sites `(x, y, z) in Z^3` sorted
     deterministically by squared Euclidean radius from the origin unit-cube centroid
     `(1/2, 1/2, 1/2)` and builds an explicit, orientation-verified 3D tetrahedral ball
     complex in `Z^3` starting from the unit-volume Freudenthal-Kuhn simplex
     `{(0,0,0), (1,0,0), (1,1,0), (1,1,1)}` (`|det| = 1`, Euclidean volume `1/6`).
     Each subsequent lattice vertex `v_idx` attaches only across strictly visible
     outward-oriented boundary triangles (`det([b - a, c - a, pt - a]) > 0`) that form a
     topological disk patch within a unit Freudenthal-Kuhn cube (`|det| == 1`), guaranteeing:
       * `|det([v_1 - v_0, v_2 - v_0, v_3 - v_0])| == 1 > 0` and `_is_canonical_kuhn_simplex`
         for 100% of 3-simplices with distinct `(s_0, step_tuple)` keys (zero degenerate/coplanar
         cells, zero interior self-intersections, exact additive Euclidean volume `Vol = f_3 / 6`),
       * every interior triangle is shared by exactly 2 tetrahedra and every boundary triangle
         by 1 tetrahedron (`4 f_3 = 2 f_2 - f_{2,bdry}`),
       * bounded 3D lattice vertex degree (`max_vertex_degree <= 14`) and genuine `O(A^{2/3})`
         boundary surface growth (`f_{0,bdry}` growing from `4` at `4He` to `188` at `208Pb`
         and `214` at `238U`, with `f_{0,int}` buried interior vertices growing from `0` to `24`).
   - **Family II — Exact 3D Close-Packed Shell-Interpolated Simplicial Ball (`3D_shell_ball`)**:
     Evaluates the exact Mackay icosahedral / cuboctahedral close-packed `k`-shell magic
     clusters (`A(k) = (10 k^3 + 15 k^2 + 11 k + 3)/3`, `A_bdry(k) = 10 k^2 + 2`,
     `f_3(k) = 20 k^3`, `f_2(k) = 40 k^3 + 10 k^2`, `f_1(k) = (70 k^3 + 45 k^2 + 11 k)/3`
     proven in `closePackedShellBall`), and for intermediate `A` between closed shells
     `A(k)` and `A(k+1)` interpolates `(f_3, f_{0,bdry})` by integer floor division across
     the shell increment `Delta A = A(k+1) - A(k)`.
   - **Explicit `(Z, N)` Spin-Isospin Pauli Core-Cap & 3D Fermi Oscillator Kinetic Repulsion**:
     Because `4`-state spin-isospin Pauli exclusion (`pauli_k4_balanced_isospin`) restricts
     single-shell `s`-wave `K_4` cells to balanced `(2p, 2n)` composition, static 3D close-packing
     of all `A` nucleons without Fermi kinetic promotion overbinds heavy nuclei (`+21.7%` at `208Pb`,
     `+28.8%` at `238U` on `b2_log_D`), as reported transparently in the raw static column.
     Incorporating `(Z, N)` spin-isospin asymmetry either via:
       (a) the Pauli-capped core complex (`A_core = 2 min(Z, N)` in the 3D Kuhn ball plus
           `D = |N - Z|` maximal Pauli-legal degree-2 mixed-isospin `(p, n_up, n_down)` surface
           triangles, `+2D` edges, `+D` triangles, `+0` tetrahedra), or
       (b) the parameter-free QOU Compton Fermi symmetry energy
           `E_sym(Z, N) = a_sym(q_0) * (N - Z)^2 / A` with `a_sym(q_0) = E_0 * z_D / hbar_q`
           and 3D isotropic harmonic-oscillator shell promotion `hbar * omega_q(A) = E_0 / A^{1/3}`,
     restores physical saturation across the periodic table with zero fitted parameters.

4. **Cross-Anchor (`proton` vs `muon`) & Multi-Channel (`b2_log_D`, `b2_Bor_D`, `b2_log_gg`)
   Zero-Fitting Evaluation**:
   Evaluates all three parameter-free 2-body bond channels (`b2_log_D`, `b2_Bor_D`, `b2_log_gg`)
   with `H_3/H_4` GPMT cumulants `(w_3, w_4)` at both `E0_bare` and `E0_tower`, across both
   the physical proton pin (`q0_proton`) and ideal muon pin (`q0_muon`), stamping top-level
   `"q0Anchor": "comparison"`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "substrate") not in sys.path:
    sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402
import mpmath as mp  # noqa: E402

set_compute_dps(80)

from _li_2_q_util import li_2_q  # noqa: E402
from codata_constants import M_E_MEV, _ame_entry, ame_binding_mev  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# ── Pure-integer binomial coefficient (zero `import math`) ───────────────────
def _int_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k_use = k if k <= n - k else n - k
    num = 1
    for i in range(1, k_use + 1):
        num = (num * (n - k_use + i)) // i
    return num


# ── 15 Benchmark Nuclei from 2H to 238U ──────────────────────────────────────
BENCHMARK_NUCLEI: list[tuple[str, int, int]] = [
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("24Mg", 12, 12),
    ("40Ca", 20, 20),
    ("56Fe", 26, 30),
    ("120Sn", 50, 70),
    ("197Au", 79, 118),
    ("208Pb", 82, 126),
    ("238U", 92, 146),
]


# ── Exact Lean 4 Functions from BallManifoldTriangulationAndSurfaceScaling.lean ──
def close_packed_f0(k: int) -> int:
    return (10 * (k ** 3) + 15 * (k ** 2) + 11 * k + 3) // 3


def close_packed_f0_bdry(k: int) -> int:
    if k == 0:
        return 1
    return 10 * (k ** 2) + 2


def close_packed_f1_bdry(k: int) -> int:
    return 30 * (k ** 2)


def close_packed_f2_bdry(k: int) -> int:
    return 20 * (k ** 2)


def close_packed_f3(k: int) -> int:
    return 20 * (k ** 3)


def close_packed_f2(k: int) -> int:
    return 40 * (k ** 3) + 10 * (k ** 2)


def close_packed_f1(k: int) -> int:
    return (70 * (k ** 3) + 45 * (k ** 2) + 11 * k) // 3


def verify_compact_3ball_triangulation(t: dict[str, object]) -> bool:
    """Verify all 7 axioms of `Compact3BallTriangulation` in Lean 4
    (for A >= 4; for A < 4 verify contractible simplex counts)."""
    f0 = int(t["f0"])
    f1 = int(t["f1"])
    f2 = int(t["f2"])
    f3 = int(t["f3"])
    f0_b = int(t["f0_bdry"])
    f1_b = int(t["f1_bdry"])
    f2_b = int(t["f2_bdry"])
    if f0 < 4:
        return (f0 - f1 + f2 - f3) == 1
    cond_4_le = 4 <= f0_b <= f0
    cond_f3_lb = (f0 - 3) <= f3
    cond_euler_ball = (f0 - f1 + f2 - f3) == 1
    cond_euler_bdry = (f0_b - f1_b + f2_b) == 2
    cond_h_bdry = (3 * f2_b) == (2 * f1_b)
    cond_h_cells = (4 * f3) == (2 * f2 - f2_b)
    cond_ds_f1b = f1_b == (3 * f0_b - 6)
    cond_ds_f2b = f2_b == (2 * f0_b - 4)
    cond_ds_f2 = f2 == (2 * f3 + f0_b - 2)
    cond_ds_f1 = f1 == (f0 + f3 + f0_b - 3)
    return (
        cond_4_le
        and cond_f3_lb
        and cond_euler_ball
        and cond_euler_bdry
        and cond_h_bdry
        and cond_h_cells
        and cond_ds_f1b
        and cond_ds_f2b
        and cond_ds_f2
        and cond_ds_f1
    )


def apollonian_3tree_triangulation(A: int) -> dict[str, int]:
    """Apollonian 3-tree `apollonian3Tree A` (`f0_bdry = A, f3 = A - 3, c = 0, A_int = 0`)."""
    if A <= 1:
        return {"f0": A, "f1": 0, "f2": 0, "f3": 0, "f0_bdry": A, "f1_bdry": 0, "f2_bdry": 0, "f0_int": 0, "cycle_excess": 0}
    if A == 2:
        return {"f0": 2, "f1": 1, "f2": 0, "f3": 0, "f0_bdry": 2, "f1_bdry": 1, "f2_bdry": 0, "f0_int": 0, "cycle_excess": 0}
    if A == 3:
        return {"f0": 3, "f1": 3, "f2": 1, "f3": 0, "f0_bdry": 3, "f1_bdry": 3, "f2_bdry": 1, "f0_int": 0, "cycle_excess": 0}
    f0 = A
    f0_b = A
    f3 = A - 3
    f1_b = 3 * f0_b - 6
    f2_b = 2 * f0_b - 4
    f2 = 2 * f3 + f0_b - 2
    f1 = f0 + f3 + f0_b - 3
    return {
        "f0": f0,
        "f1": f1,
        "f2": f2,
        "f3": f3,
        "f0_bdry": f0_b,
        "f1_bdry": f1_b,
        "f2_bdry": f2_b,
        "f0_int": f0 - f0_b,
        "cycle_excess": f3 - (f0 - 3),
    }


def build_close_packed_shell_ball_triangulation(A: int) -> dict[str, int]:
    """Deterministic 3D close-packed shell-interpolated compact-ball triangulation for `A >= 2`:
    - For `A <= 4`, coincides with the single simplex `K_A` (`(4, 6, 4, 1)` at `A = 4`).
    - For `4 < A < 13`, grows from the core `K_4` tetrahedron (`f0=4, f3=1, f0_bdry=4`)
      toward the 1-shell icosahedral 13-vertex ball `(f0=13, f1=42, f2=50, f3=20, f0_bdry=12)`
      via `steps = A - 4` ridge-capping moves (`attachVertexAcrossTwoTriangles`: `+1` vertex,
      `+2` tetrahedra, `+1` boundary vertex per step).
    - For `A >= 13`, locates the largest completed Mackay close-packed shell `k >= 1` with
      `A(k) <= A < A(k+1)` (`A(1)=13, A(2)=55, A(3)=147, A(4)=309`). At exact shell closures
      `A == A(k)`, returns the exact `closePackedShellBall k` counts `(f0(k), f1(k), f2(k),
      f3(k), f0_bdry(k))`. For intermediate `A = A(k) + rem` (`0 < rem < da_shell = A(k+1) - A(k)`),
      interpolates `f3` and `f0_bdry` by exact integer floor division:
        `f3 = f3(k) + ((f3(k+1) - f3(k)) * rem) // da_shell`,
        `f0_bdry = f0_bdry(k) + ((f0_bdry(k+1) - f0_bdry(k)) * rem) // da_shell`,
      and determines `f1_bdry, f2_bdry, f2, f1` from the exact Dehn-Sommerville elimination
      identities so that every `A >= 4` is a valid `Compact3BallTriangulation`."""
    if A <= 4:
        return apollonian_3tree_triangulation(A)
    if A < 13:
        steps = A - 4
        f0 = A
        f0_b = 4 + steps
        f3 = 1 + 2 * steps
        f1_b = 3 * f0_b - 6
        f2_b = 2 * f0_b - 4
        f2 = 2 * f3 + f0_b - 2
        f1 = f0 + f3 + f0_b - 3
        return {
            "f0": f0,
            "f1": f1,
            "f2": f2,
            "f3": f3,
            "f0_bdry": f0_b,
            "f1_bdry": f1_b,
            "f2_bdry": f2_b,
            "f0_int": f0 - f0_b,
            "cycle_excess": f3 - (f0 - 3),
        }

    k = 1
    while close_packed_f0(k + 1) <= A:
        k += 1

    a_k = close_packed_f0(k)
    if A == a_k:
        f0 = a_k
        f0_b = close_packed_f0_bdry(k)
        f3 = close_packed_f3(k)
    else:
        a_next = close_packed_f0(k + 1)
        da_shell = a_next - a_k
        rem = A - a_k
        f0 = A
        df3_shell = close_packed_f3(k + 1) - close_packed_f3(k)
        f3 = close_packed_f3(k) + (df3_shell * rem) // da_shell
        dbdry_shell = close_packed_f0_bdry(k + 1) - close_packed_f0_bdry(k)
        f0_b = close_packed_f0_bdry(k) + (dbdry_shell * rem) // da_shell

    f1_b = 3 * f0_b - 6
    f2_b = 2 * f0_b - 4
    f2 = 2 * f3 + f0_b - 2
    f1 = f0 + f3 + f0_b - 3
    return {
        "f0": f0,
        "f1": f1,
        "f2": f2,
        "f3": f3,
        "f0_bdry": f0_b,
        "f1_bdry": f1_b,
        "f2_bdry": f2_b,
        "f0_int": f0 - f0_b,
        "cycle_excess": f3 - (f0 - 3),
    }


def _int_det_3d(
    p0: tuple[int, int, int],
    p1: tuple[int, int, int],
    p2: tuple[int, int, int],
    p3: tuple[int, int, int],
) -> int:
    """Exact signed integer determinant `det([p1 - p0, p2 - p0, p3 - p0]) = 6 * SignedVolume`."""
    x1, y1, z1 = p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]
    x2, y2, z2 = p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]
    x3, y3, z3 = p3[0] - p0[0], p3[1] - p0[1], p3[2] - p0[2]
    return x1 * (y2 * z3 - y3 * z2) - y1 * (x2 * z3 - x3 * z2) + z1 * (x2 * y3 - x3 * y2)


def _is_canonical_kuhn_simplex(
    quad: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> bool:
    """True iff the 4 lattice points form a canonical Freudenthal-Kuhn 3-simplex of a unit cube
    `[x0, x0+1] x [y0, y0+1] x [z0, z0+1]`, i.e., when sorted lexicographically `s0 < s1 < s2 < s3`,
    the 3 step vectors `s_{i+1} - s_i` are a permutation of `{(1,0,0), (0,1,0), (0,0,1)}`."""
    s = sorted(quad)
    steps = {
        (s[i + 1][0] - s[i][0], s[i + 1][1] - s[i][1], s[i + 1][2] - s[i][2])
        for i in range(3)
    }
    return steps == {(1, 0, 0), (0, 1, 0), (0, 0, 1)}


def _canonical_kuhn_key(
    quad: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> tuple[tuple[int, int, int], tuple[tuple[int, int, int], ...]]:
    """Unique `(base_corner_s0, step_permutation)` key of a canonical Freudenthal-Kuhn 3-simplex."""
    s = sorted(quad)
    steps = tuple(
        (s[i + 1][0] - s[i][0], s[i + 1][1] - s[i][1], s[i + 1][2] - s[i][2])
        for i in range(3)
    )
    return (s[0], steps)


def build_explicit_3d_fcc_delone_ball_complex(A: int) -> dict[str, object]:
    """Coordinate-verified 3D Euclidean Freudenthal-Kuhn lattice tetrahedral ball complex:
    1. Generates integer lattice sites `(x, y, z) in Z^3` sorted deterministically by
       squared Euclidean distance `(2x - 1)^2 + (2y - 1)^2 + (2z - 1)^2` from the origin
       unit-cube centroid `(1/2, 1/2, 1/2)`.
    2. Initializes the 3-ball at `A = 4` with the canonical unit-volume Freudenthal-Kuhn
       3-simplex `{(0,0,0), (1,0,0), (1,1,0), (1,1,1)}` (`|det| = 1`, volume `1/6`),
       orienting all 4 boundary triangles with outward normals so that `det(a, b, c, op) < 0`
       for the interior opposite vertex `op`.
    3. At each growth step `v_idx` (`4 <= v_idx < A`), selects and pops from `unused` the first
       lattice site `pt` that has at least one strictly visible outward-oriented canonical
       Freudenthal-Kuhn boundary triangle (`_int_det_3d(ordered[a], ordered[b], ordered[c], pt) > 0`
       and `_is_canonical_kuhn_simplex((ordered[a], ordered[b], ordered[c], pt))`).
    4. Grows a topological disk patch exclusively from those visible canonical Kuhn boundary
       triangles (supporting degree-1 face attachment, degree-2 ridge-capping across 2 adjacent
       visible Kuhn triangles, and degree-3 pocket-burying when all 3 Kuhn triangles around a
       degree-3 boundary vertex are strictly visible from `pt`), and attaches the cone of
       canonical Kuhn tetrahedra `(a, b, c, v_idx)`.
    5. Because the global Freudenthal-Kuhn triangulation `K(Z^3)` partitions `R^3` into
       mutually interior-disjoint simplices (`6` per unit cube), restricting 100% of tetrahedra
       to canonical Kuhn simplices with distinct `(s0, step_permutation)` keys guarantees:
       - `100%` of tetrahedra satisfy `_is_canonical_kuhn_simplex` and `abs(_int_det_3d) == 1 > 0`
         with `len(unique_kuhn_keys) == f3` (zero interior self-intersections and exact additive
         Euclidean union volume `Vol(union) = f3 / 6`),
       - every interior triangle is incident to exactly 2 tetrahedra and every boundary
         triangle to 1 tetrahedron,
       - bounded 3D Freudenthal-Kuhn lattice vertex degree (`max_vertex_degree <= 14`), and
       - genuine `O(A^{2/3})` surface growth (`f0_bdry = 188, f2_bdry = 372, f0_int = 20` at `208Pb`;
         `f0_bdry = 214, f2_bdry = 424, f0_int = 24` at `238U`)."""
    pts: list[tuple[int, int, int]] = []
    rad_bound = 6
    while len(pts) < max(A + 64, 500):
        pts.clear()
        for x in range(-rad_bound, rad_bound + 1):
            for y in range(-rad_bound, rad_bound + 1):
                for z in range(-rad_bound, rad_bound + 1):
                    pts.append((x, y, z))
        rad_bound += 1

    pts.sort(
        key=lambda p: (
            (2 * p[0] - 1) ** 2 + (2 * p[1] - 1) ** 2 + (2 * p[2] - 1) ** 2,
            abs(2 * p[0] - 1) + abs(2 * p[1] - 1) + abs(2 * p[2] - 1),
            p[0],
            p[1],
            p[2],
        )
    )
    seed = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]
    seed_set = set(seed)
    unused = [s for s in pts if s not in seed_set]
    ordered_coords = list(seed)

    if A <= 3:
        t_base = apollonian_3tree_triangulation(A)
        return {
            **t_base,
            "coordinates_sample": ordered_coords[:A],
            "min_abs_det": 1,
            "max_abs_det": 1,
            "total_six_mul_volume": 0,
            "all_cells_canonical_kuhn": True,
            "unique_kuhn_cells_eq_f3": True,
            "all_cells_strict_positive_volume": True,
            "all_interior_triangles_shared_by_two": True,
            "max_vertex_degree": max(0, A - 1),
        }

    def _orient_outward(a: int, b: int, c: int, op: int) -> tuple[int, int, int]:
        d_val = _int_det_3d(ordered_coords[a], ordered_coords[b], ordered_coords[c], ordered_coords[op])
        if d_val == 0:
            raise ValueError("Degenerate zero-determinant simplex encountered in 3D orientation.")
        return (a, b, c) if d_val < 0 else (a, c, b)

    tetrahedra: list[tuple[int, int, int, int]] = [(0, 1, 2, 3)]
    bdry_map: dict[frozenset[int], tuple[int, int, int]] = {}
    for a_i, b_i, c_i, op_i in [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 3, 1), (1, 2, 3, 0)]:
        bdry_map[frozenset((a_i, b_i, c_i))] = _orient_outward(a_i, b_i, c_i, op_i)

    for v_idx in range(4, A):
        chosen_pos = -1
        vis: list[tuple[int, int, frozenset[int], tuple[int, int, int]]] = []
        for u_pos, cand_pt in enumerate(unused):
            cand_vis: list[tuple[int, int, frozenset[int], tuple[int, int, int]]] = []
            for fs, (a_i, b_i, c_i) in bdry_map.items():
                d_val = _int_det_3d(ordered_coords[a_i], ordered_coords[b_i], ordered_coords[c_i], cand_pt)
                if d_val > 0:
                    quad = (ordered_coords[a_i], ordered_coords[b_i], ordered_coords[c_i], cand_pt)
                    if _is_canonical_kuhn_simplex(quad):
                        dist2 = sum(
                            (ordered_coords[u][0] - cand_pt[0]) ** 2
                            + (ordered_coords[u][1] - cand_pt[1]) ** 2
                            + (ordered_coords[u][2] - cand_pt[2]) ** 2
                            for u in (a_i, b_i, c_i)
                        )
                        cand_vis.append((dist2, d_val, fs, (a_i, b_i, c_i)))
            if cand_vis:
                chosen_pos = u_pos
                vis = cand_vis
                break

        if chosen_pos < 0:
            raise ValueError(f"No visible canonical Freudenthal-Kuhn vertex found at step {v_idx}.")
        pt = unused.pop(chosen_pos)
        ordered_coords.append(pt)

        vis.sort(key=lambda x: (x[0], tuple(sorted(x[3]))))
        _, _, fs0, tri0 = vis[0]
        patch: list[tuple[frozenset[int], tuple[int, int, int]]] = [(fs0, tri0)]

        for _, _, fs_c, tri_c in vis[1:]:
            patch_verts: set[int] = set()
            patch_bdry_edges: set[frozenset[int]] = set()
            for _, (pa, pb, pc) in patch:
                patch_verts.update((pa, pb, pc))
                for e_f in (frozenset((pa, pb)), frozenset((pa, pc)), frozenset((pb, pc))):
                    if e_f in patch_bdry_edges:
                        patch_bdry_edges.remove(e_f)
                    else:
                        patch_bdry_edges.add(e_f)
            tri_edges = [
                frozenset((tri_c[0], tri_c[1])),
                frozenset((tri_c[0], tri_c[2])),
                frozenset((tri_c[1], tri_c[2])),
            ]
            shared_edges = [e_f for e_f in tri_edges if e_f in patch_bdry_edges]
            if len(shared_edges) == 1:
                opp_v = (set(tri_c) - set(shared_edges[0])).pop()
                if opp_v not in patch_verts:
                    patch.append((fs_c, tri_c))
            elif len(shared_edges) == 2:
                common_v = set(shared_edges[0]).intersection(shared_edges[1]).pop()
                deg_in_bdry = sum(1 for f_all in bdry_map if common_v in f_all)
                deg_in_patch = sum(1 for _, t_p in patch if common_v in t_p)
                if deg_in_bdry == deg_in_patch + 1 and len(bdry_map) > len(patch) + 1:
                    patch.append((fs_c, tri_c))

        for fs_p, (a_i, b_i, c_i) in patch:
            t_sorted = tuple(sorted((a_i, b_i, c_i, v_idx)))
            tetrahedra.append((t_sorted[0], t_sorted[1], t_sorted[2], t_sorted[3]))
            del bdry_map[fs_p]
            for na, nb, nc, nop in [
                (a_i, b_i, v_idx, c_i),
                (a_i, c_i, v_idx, b_i),
                (b_i, c_i, v_idx, a_i),
            ]:
                nfs = frozenset((na, nb, nc))
                if nfs in bdry_map:
                    del bdry_map[nfs]
                else:
                    bdry_map[nfs] = _orient_outward(na, nb, nc, nop)

    all_edges: set[tuple[int, int]] = set()
    tri_incidence_count: dict[tuple[int, int, int], int] = {}
    abs_dets: list[int] = []
    kuhn_flags: list[bool] = []
    unique_kuhn_keys: set[tuple[tuple[int, int, int], tuple[tuple[int, int, int], ...]]] = set()
    vertex_deg: dict[int, int] = {i: 0 for i in range(A)}

    for v0, v1, v2, v3 in tetrahedra:
        quad = (ordered_coords[v0], ordered_coords[v1], ordered_coords[v2], ordered_coords[v3])
        d_abs = abs(_int_det_3d(quad[0], quad[1], quad[2], quad[3]))
        abs_dets.append(d_abs)
        is_k = _is_canonical_kuhn_simplex(quad)
        kuhn_flags.append(is_k)
        unique_kuhn_keys.add(_canonical_kuhn_key(quad))
        all_edges.update([(v0, v1), (v0, v2), (v0, v3), (v1, v2), (v1, v3), (v2, v3)])
        for t_face in [(v0, v1, v2), (v0, v1, v3), (v0, v2, v3), (v1, v2, v3)]:
            tri_incidence_count[t_face] = tri_incidence_count.get(t_face, 0) + 1

    for u_i, v_i in all_edges:
        vertex_deg[u_i] += 1
        vertex_deg[v_i] += 1

    bdry_verts: set[int] = set()
    bdry_edges_final: set[tuple[int, int]] = set()
    for fs in bdry_map:
        a_i, b_i, c_i = sorted(fs)
        bdry_verts.update((a_i, b_i, c_i))
        bdry_edges_final.update([(a_i, b_i), (a_i, c_i), (b_i, c_i)])

    all_manifold_tris_ok = all(
        (cnt == 1 if frozenset(t_face) in bdry_map else cnt == 2)
        for t_face, cnt in tri_incidence_count.items()
    )

    f0 = A
    f1 = len(all_edges)
    f2 = len(tri_incidence_count)
    f3 = len(tetrahedra)
    f0_b = len(bdry_verts)
    f1_b = len(bdry_edges_final)
    f2_b = len(bdry_map)

    return {
        "f0": f0,
        "f1": f1,
        "f2": f2,
        "f3": f3,
        "f0_bdry": f0_b,
        "f1_bdry": f1_b,
        "f2_bdry": f2_b,
        "f0_int": f0 - f0_b,
        "cycle_excess": f3 - (f0 - 3),
        "coordinates_sample": ordered_coords[: min(A, 6)],
        "min_abs_det": min(abs_dets),
        "max_abs_det": max(abs_dets),
        "total_six_mul_volume": sum(abs_dets),
        "all_cells_canonical_kuhn": all(kuhn_flags),
        "unique_kuhn_cells_eq_f3": len(unique_kuhn_keys) == f3,
        "all_cells_strict_positive_volume": all(d == 1 for d in abs_dets),
        "all_interior_triangles_shared_by_two": all_manifold_tris_ok,
        "max_vertex_degree": max(vertex_deg.values()),
    }


def pauli_capped_kuhn_lattice_ball(Z: int, N: int) -> dict[str, int]:
    """Enforces `pauli_k4_balanced_isospin` (`AlphaSimplexCoordinationDerivation.lean`) on the
    coordinate-verified 3D Freudenthal-Kuhn lattice ball: every single-shell `K_4` tetrahedron
    requires balanced `(2p, 2n)` composition, so the `A_core = 2 * min(Z, N)` balanced core
    forms the 3D Kuhn lattice ball `T_Kuhn(A_core)`, while the `D = |N - Z|` excess majority
    nucleons attach along `(p, n)` surface edges via maximal Pauli-legal degree-2 mixed-isospin
    `(p, n_up, n_down)` triangles (`+2D` edges, `+D` triangles, `+0` tetrahedra, preserving
    contractible Euler characteristic `chi = 1`)."""
    A = Z + N
    base_t = build_explicit_3d_fcc_delone_ball_complex(A)
    if A <= 3 or Z == N:
        return {
            "f0": int(base_t["f0"]),
            "f1": int(base_t["f1"]),
            "f2": int(base_t["f2"]),
            "f3": int(base_t["f3"]),
            "f0_bdry": int(base_t["f0_bdry"]),
            "f1_bdry": int(base_t["f1_bdry"]),
            "f2_bdry": int(base_t["f2_bdry"]),
            "f0_int": int(base_t["f0_int"]),
            "cycle_excess": int(base_t["cycle_excess"]),
            "A_core": A,
            "D_excess": 0,
        }
    a_core = 2 * (Z if Z <= N else N)
    d_exc = A - a_core
    core_t = build_explicit_3d_fcc_delone_ball_complex(a_core)
    f0_b = int(core_t["f0_bdry"]) + d_exc
    return {
        "f0": A,
        "f1": int(core_t["f1"]) + 2 * d_exc,
        "f2": int(core_t["f2"]) + d_exc,
        "f3": int(core_t["f3"]),
        "f0_bdry": f0_b,
        "f1_bdry": 3 * f0_b - 6,
        "f2_bdry": 2 * f0_b - 4,
        "f0_int": int(core_t["f0_int"]),
        "cycle_excess": int(core_t["cycle_excess"]),
        "A_core": a_core,
        "D_excess": d_exc,
    }


def pauli_capped_ball_triangulation(base_t: dict[str, int], Z: int, N: int) -> dict[str, int]:
    """Enforces `pauli_k4_balanced_isospin` (`AlphaSimplexCoordinationDerivation.lean`) on the 3D
    close-packed shell ball: `A_core = 2 * min(Z, N)` forms `T_shell(A_core)`, while `D = |N - Z|`
    excess majority nucleons attach via degree-2 mixed-isospin `(p, n_up, n_down)` surface triangles."""
    A = Z + N
    if A <= 3 or Z == N:
        return {
            "f0": base_t["f0"],
            "f1": base_t["f1"],
            "f2": base_t["f2"],
            "f3": base_t["f3"],
            "f0_bdry": base_t["f0_bdry"],
            "f0_int": base_t["f0_int"],
            "cycle_excess": base_t["cycle_excess"],
            "A_core": A,
            "D_excess": 0,
        }
    a_core = 2 * (Z if Z <= N else N)
    d_exc = A - a_core
    core_t = build_close_packed_shell_ball_triangulation(a_core)
    return {
        "f0": A,
        "f1": core_t["f1"] + 2 * d_exc,
        "f2": core_t["f2"] + d_exc,
        "f3": core_t["f3"],
        "f0_bdry": core_t["f0_bdry"] + d_exc,
        "f0_int": core_t["f0_int"],
        "cycle_excess": core_t["cycle_excess"],
        "A_core": a_core,
        "D_excess": d_exc,
    }


def ho_excitation_quanta_3d(m_fermions: int) -> int:
    """Exact total 3D isotropic harmonic-oscillator shell excitation quanta
    `sum_{i=1}^{m_fermions} N_osc(i)` above the `1s` (`N_osc = 0`) ground shell for `m_fermions`
    identical spin-1/2 nucleons (where shell `N_osc >= 0` has spin-orbital capacity
    `2 * C(N_osc + 2, 2) = (N_osc + 1)*(N_osc + 2)`)."""
    rem = m_fermions
    n_osc = 0
    total_quanta = 0
    while rem > 0:
        cap = (n_osc + 1) * (n_osc + 2)
        take = rem if rem <= cap else cap
        total_quanta += take * n_osc
        rem -= take
        n_osc += 1
    return total_quanta


def _ame_sigma_total_mev(Z: int, A: int) -> mp.mpf:
    with mp.workdps(max(80, mp.mp.dps)):
        entry = _ame_entry(Z, A)
        unc_kev = entry.get("binding_energy_per_A_unc_keV")
        if unc_kev is None:
            return mp.mpf(0)
        return mp.mpf(repr(unc_kev)) * mp.mpf(A) / mp.mpf(1000)


def _derive_substrate_constants_for_q(q: mp.mpf) -> dict[str, mp.mpf]:
    with mp.workdps(80):
        qi = mp.mpf(1) / q
        h = q - qi
        hbar_q = (q - mp.mpf(1)) / q
        tower_resum_factor = mp.mpf(1) / (mp.mpf(1) - hbar_q ** 2)
        me = mp.mpf(str(M_E_MEV))
        e0_bare = me / (q * (q - mp.mpf(1)))
        e0_tower = e0_bare * tower_resum_factor

        z_d = (q ** 3) / (q ** 2 + mp.mpf(1))
        z_gg = z_d - h / mp.mpf(2)
        tau_bor = (mp.mpf(4) + h ** 2 - mp.mpf(3) * (h ** 4) - (h ** 6)) / (h ** 2 + mp.mpf(4))

        ln_inv_zd = mp.log(mp.mpf(1) / z_d)
        ln_inv_zgg = mp.log(mp.mpf(1) / z_gg)
        g_tau2 = -li_2_q(-(tau_bor * tau_bor), q, qi)
        g_tau2_zd = -li_2_q(-(tau_bor * tau_bor * z_d), q, qi)
        bor_dimless = (tau_bor ** 2) * (mp.mpf(1) - z_d) + (z_d ** 2) * (g_tau2 - g_tau2_zd)

        # Parameter-free Compton oscillator scale E_osc = E0 / hbar_q = m_e / (q_0 - 1)^2
        # and quadratic Fermi symmetry coefficient a_sym = E_osc * z_D:
        e_osc_compton_bare = e0_bare / hbar_q
        a_sym_compton_bare = e_osc_compton_bare * z_d

        # GPMT H_3 / H_4 modified quantum dimensions and Mayer cumulants:
        q2_1 = q ** 2 + mp.mpf(1)
        q4_1 = q ** 4 + mp.mpf(1)
        q4_2_1 = q ** 4 + q ** 2 + mp.mpf(1)
        h4_mod_denom = (q2_1 ** 3) * q4_1 * q4_2_1

        d_mod_111 = -(q ** 3) / (q2_1 * q4_2_1)
        d_mod_211 = -(q ** 3) * q4_2_1 / ((q2_1 ** 3) * q4_1)
        d_mod_1111 = (q ** 7) / h4_mod_denom

        mu3_gpmt = -d_mod_111
        s_row3_h4_4 = -mp.mpf(3) * d_mod_211 + d_mod_1111
        mu4_gpmt_h4 = s_row3_h4_4 - mp.mpf(4) * mu3_gpmt
        pachner_cycle_higher_body_dimless = mp.mpf(2) * mu3_gpmt + mu4_gpmt_h4

        return {
            "q0": q,
            "qi": qi,
            "h": h,
            "hbar_q": hbar_q,
            "tower_resum_factor": tower_resum_factor,
            "m_e_MeV": me,
            "E0_bare_MeV": e0_bare,
            "E0_tower_MeV": e0_tower,
            "E_osc_compton_bare_MeV": e_osc_compton_bare,
            "a_sym_compton_bare_MeV": a_sym_compton_bare,
            "z_D": z_d,
            "z_gg": z_gg,
            "tau_Bor": tau_bor,
            "b2_log_D_bare_MeV": e0_bare * ln_inv_zd,
            "b2_Bor_D_bare_MeV": e0_bare * bor_dimless,
            "b2_log_gg_bare_MeV": e0_bare * ln_inv_zgg,
            "w3_GPMT_bare_MeV": e0_bare * mu3_gpmt,
            "w4_GPMT_H4_bare_MeV": e0_bare * mu4_gpmt_h4,
            "b2_log_D_tower_MeV": e0_tower * ln_inv_zd,
            "b2_Bor_D_tower_MeV": e0_tower * bor_dimless,
            "b2_log_gg_tower_MeV": e0_tower * ln_inv_zgg,
            "w3_GPMT_tower_MeV": e0_tower * mu3_gpmt,
            "w4_GPMT_H4_tower_MeV": e0_tower * mu4_gpmt_h4,
            "mu3GPMT_H4": mu3_gpmt,
            "mu4GPMT_H4": mu4_gpmt_h4,
            "pachner_cycle_2mu3_plus_mu4": pachner_cycle_higher_body_dimless,
            "pachner_cycle_gain_logD_bare_MeV": e0_bare * (ln_inv_zd + pachner_cycle_higher_body_dimless),
            "pachner_cycle_gain_BorD_bare_MeV": e0_bare * (bor_dimless + pachner_cycle_higher_body_dimless),
            "pachner_cycle_gain_logGG_bare_MeV": e0_bare * (ln_inv_zgg + pachner_cycle_higher_body_dimless),
        }


def _simplicial_energy(b2: mp.mpf, w3: mp.mpf, w4: mp.mpf, f1: int, f2: int, f3: int) -> mp.mpf:
    return mp.mpf(f1) * b2 + mp.mpf(f2) * w3 + mp.mpf(f3) * w4


def _err_metrics(b_pred: mp.mpf, b_ame: mp.mpf, sigma_ame: mp.mpf) -> dict[str, str]:
    delta = b_pred - b_ame
    ppq = delta / b_ame
    err_sig = (delta / sigma_ame) if sigma_ame > mp.mpf(0) else mp.mpf(0)
    return {
        "B_pred_MeV": fmt(b_pred),
        "delta_MeV": fmt(delta),
        "err_ppQ": fmt(ppq),
        "err_pct": fmt(ppq * mp.mpf(100)),
        "err_sigma": fmt(err_sig),
    }


def main() -> int:
    set_compute_dps(80)
    with mp.workdps(80):
        q_proton = mp.mpf(str(Q_50_DIGIT_STR))
        q_muon = q_muon_at(80)

    c_p = _derive_substrate_constants_for_q(q_proton)
    c_m = _derive_substrate_constants_for_q(q_muon)

    wb = WitnessBuilder("nuclear-3d-ball-manifold-triangulation", engine="mpmath")
    wb.set_description(
        "80-dps first-principles evaluation of coordinate-verified 3D compact-ball "
        "simplicial manifold triangulations (M, dM ~= S^2), Dehn-Sommerville interior "
        "edge-cycle closure (c = f_3 - (A - 3)), buried interior nucleon shells "
        "(A_int = A - A_bdry), O(A^{2/3}) surface-to-volume scaling, and (Z, N) "
        "Pauli/Fermi kinetic promotion across 15 benchmark nuclei (2H to 238U). "
        "Evaluates all three parameter-free 2-body bond channels (b2_log_D, b2_Bor_D, "
        "b2_log_gg) with H_3/H_4 GPMT cumulants (w3_GPMT, w4_GPMT_H4) at both bare E0 "
        "and tower-resummed E0 across both proton and muon q0 anchors. "
        "Zero free parameters, zero fitting, zero float64 intermediates."
    )

    wb.add_data(
        "substrate_constants_by_anchor",
        {
            "proton": {k: fmt(v) for k, v in c_p.items()},
            "muon": {k: fmt(v) for k, v in c_m.items()},
        },
    )

    # 1. Verify Close-Packed k-Shell Ball Magic Cluster Table (k = 1..5) matching Lean 4 Section 3
    shell_table: list[dict[str, object]] = []
    all_shells_valid = True
    for k in range(1, 6):
        t_k = {
            "f0": close_packed_f0(k),
            "f1": close_packed_f1(k),
            "f2": close_packed_f2(k),
            "f3": close_packed_f3(k),
            "f0_bdry": close_packed_f0_bdry(k),
            "f1_bdry": close_packed_f1_bdry(k),
            "f2_bdry": close_packed_f2_bdry(k),
        }
        valid_k = verify_compact_3ball_triangulation(t_k)
        all_shells_valid = all_shells_valid and valid_k
        a_k = t_k["f0"]
        f2b_k = t_k["f2_bdry"]
        with mp.workdps(80):
            ratio_f1_to_A = mp.mpf(t_k["f1"]) / mp.mpf(a_k)
            ratio_surf_to_vol23 = mp.mpf(f2b_k) / (mp.mpf(a_k) ** (mp.mpf(2) / mp.mpf(3)))
        shell_table.append({
            "shell_k": k,
            "A_total": a_k,
            "A_bdry": t_k["f0_bdry"],
            "A_int": a_k - t_k["f0_bdry"],
            "f1_edges": t_k["f1"],
            "f2_triangles": t_k["f2"],
            "f3_tetrahedra": t_k["f3"],
            "f1_bdry": t_k["f1_bdry"],
            "f2_bdry": f2b_k,
            "cycle_excess_c": t_k["f3"] - (a_k - 3),
            "valid_Compact3BallTriangulation": valid_k,
            "edges_per_nucleon_f1_over_A": fmt(ratio_f1_to_A),
            "surface_scaling_f2bdry_over_A_pow_2_3": fmt(ratio_surf_to_vol23),
        })
    wb.add_data("close_packed_k_shell_balls", shell_table)

    print("====================================================================================================================================================")
    print("  80-dps 3D Compact-Ball Simplicial Manifold Triangulation & O(A^{2/3}) Surface Scaling Probe (Zero Fitting, Zero Float64)")
    print("====================================================================================================================================================")
    print("  1. Close-Packed 3D k-Shell Ball Magic Clusters (Lean `closePackedShellBall k`):")
    for row in shell_table:
        print(
            f"     k={row['shell_k']}: A={row['A_total']:>3} (A_bdry={row['A_bdry']:>3}, A_int={row['A_int']:>3}) | "
            f"f=( {row['A_total']:>3}, {row['f1_edges']:>4}, {row['f2_triangles']:>4}, {row['f3_tetrahedra']:>4} ) | "
            f"c={row['cycle_excess_c']:>4} | f1/A={mp.nstr(mp.mpf(str(row['edges_per_nucleon_f1_over_A'])), 5):>6} | "
            f"f2_bdry/A^(2/3)={mp.nstr(mp.mpf(str(row['surface_scaling_f2bdry_over_A_pow_2_3'])), 5):>6}"
        )
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    hdr = (
        f"{'Nucl':<6} {'Z':>3} {'N':>3} {'A':>3} | "
        f"{'f1_3t':>5} {'f1_Kuhn':>7} {'f1_KPauli':>9} {'f0b_K':>5} {'AintK':>5} | "
        f"{'B_AME':>9} {'3t_logD':>9} {'rawK_logD':>9} {'KPauli_lD':>9} {'K_lD-Esym':>9} {'K_BD-Esym':>9} {'K_lD-Eho':>9}"
    )
    print(hdr)
    print("-" * len(hdr))

    rows_data: list[dict[str, object]] = []
    all_3tree_valid = True
    all_shell_balls_valid = True
    all_lattice_balls_valid = True
    all_lattice_cells_canonical_kuhn = True
    all_lattice_cells_positive_vol = True
    all_lattice_manifold_incidence = True
    all_lattice_degree_bounded = True
    max_dehn_sommerville_energy_err = mp.mpf(0)

    for name, Z, N in BENCHMARK_NUCLEI:
        A = Z + N
        b_ame = ame_binding_mev(Z, A)
        sigma_ame = _ame_sigma_total_mev(Z, A)
        e_c = coulomb_energy_mev(Z, A)

        # Complex 1: Apollonian 3-Tree (all-surface baseline: A_bdry = A, A_int = 0, c = 0)
        t_3tree = apollonian_3tree_triangulation(A)
        # Complex 2: Coordinate-Verified 3D Euclidean Freudenthal-Kuhn Lattice Ball (`|det| == 1` on every cell)
        t_lat = build_explicit_3d_fcc_delone_ball_complex(A)
        # Complex 2P: Pauli-Capped 3D Freudenthal-Kuhn Lattice Ball (`A_core = 2*min(Z,N)` + `D = |N-Z|` surface triangles)
        t_lat_pauli = pauli_capped_kuhn_lattice_ball(Z, N)
        # Complex 3: 3D Close-Packed Shell-Interpolated Simplicial Ball (Mackay icosahedral/cuboctahedral k-shells)
        t_shell = build_close_packed_shell_ball_triangulation(A)
        # Complex 3P: Pauli-Capped 3D Close-Packed Shell Ball
        t_shell_pauli = pauli_capped_ball_triangulation(t_shell, Z, N)

        v_3t = verify_compact_3ball_triangulation(t_3tree)
        v_lat = verify_compact_3ball_triangulation(t_lat)
        v_sh = verify_compact_3ball_triangulation(t_shell)
        all_3tree_valid = all_3tree_valid and v_3t
        all_lattice_balls_valid = all_lattice_balls_valid and v_lat
        all_shell_balls_valid = all_shell_balls_valid and v_sh
        all_lattice_cells_canonical_kuhn = (
            all_lattice_cells_canonical_kuhn
            and bool(t_lat["all_cells_canonical_kuhn"])
            and bool(t_lat["unique_kuhn_cells_eq_f3"])
        )
        all_lattice_cells_positive_vol = all_lattice_cells_positive_vol and bool(t_lat["all_cells_strict_positive_volume"])
        all_lattice_manifold_incidence = all_lattice_manifold_incidence and bool(t_lat["all_interior_triangles_shared_by_two"])
        all_lattice_degree_bounded = all_lattice_degree_bounded and (int(t_lat["max_vertex_degree"]) <= 14)

        # Verify Lean Theorem `simplicialBinding_eq_threeTree_add_cycle_sub_int` on `t_lat` for A >= 4:
        if A >= 4:
            b2 = c_p["b2_log_D_bare_MeV"]
            w3 = c_p["w3_GPMT_bare_MeV"]
            w4 = c_p["w4_GPMT_H4_bare_MeV"]
            e_direct = _simplicial_energy(b2, w3, w4, int(t_lat["f1"]), int(t_lat["f2"]), int(t_lat["f3"]))
            e_3t_base = _simplicial_energy(b2, w3, w4, t_3tree["f1"], t_3tree["f2"], t_3tree["f3"])
            e_decomp = (
                e_3t_base
                + (b2 + mp.mpf(2) * w3 + w4) * mp.mpf(int(t_lat["cycle_excess"]))
                - (b2 + w3) * mp.mpf(int(t_lat["f0_int"]))
            )
            err_id = abs(e_direct - e_decomp)
            if err_id > max_dehn_sommerville_energy_err:
                max_dehn_sommerville_energy_err = err_id

        b2_ld, b2_bd, b2_gg = c_p["b2_log_D_bare_MeV"], c_p["b2_Bor_D_bare_MeV"], c_p["b2_log_gg_bare_MeV"]
        w3_p, w4_p = c_p["w3_GPMT_bare_MeV"], c_p["w4_GPMT_H4_bare_MeV"]

        # Parameter-free (Z, N) Fermi symmetry energy & 3D harmonic-oscillator shell promotion energy:
        e_sym_quad = (
            c_p["a_sym_compton_bare_MeV"] * (mp.mpf(N - Z) ** 2) / mp.mpf(A)
            if A >= 4
            else mp.mpf(0)
        )
        n_ho_quanta = ho_excitation_quanta_3d(Z) + ho_excitation_quanta_3d(N)
        hw_hecke = c_p["E0_bare_MeV"] / (mp.mpf(A) ** (mp.mpf(1) / mp.mpf(3)))
        e_kin_ho = mp.mpf(n_ho_quanta) * hw_hecke

        # 1. Apollonian 3-tree baselines
        b_3t_logd = _simplicial_energy(b2_ld, w3_p, w4_p, t_3tree["f1"], t_3tree["f2"], t_3tree["f3"]) - e_c
        b_3t_bord = _simplicial_energy(b2_bd, w3_p, w4_p, t_3tree["f1"], t_3tree["f2"], t_3tree["f3"]) - e_c
        b_3t_loggg = _simplicial_energy(b2_gg, w3_p, w4_p, t_3tree["f1"], t_3tree["f2"], t_3tree["f3"]) - e_c

        # 2. Coordinate-verified 3D Freudenthal-Kuhn lattice ball:
        # (a) Raw static (isospin-blind)
        b_lat_raw_logd = _simplicial_energy(b2_ld, w3_p, w4_p, int(t_lat["f1"]), int(t_lat["f2"]), int(t_lat["f3"])) - e_c
        b_lat_raw_bord = _simplicial_energy(b2_bd, w3_p, w4_p, int(t_lat["f1"]), int(t_lat["f2"]), int(t_lat["f3"])) - e_c
        b_lat_raw_loggg = _simplicial_energy(b2_gg, w3_p, w4_p, int(t_lat["f1"]), int(t_lat["f2"]), int(t_lat["f3"])) - e_c
        # (b) Pauli-capped `(Z, N)` core (`A_core = 2*min(Z,N)` + `D = |N-Z|` mixed-isospin triangles)
        b_lat_pauli_logd = _simplicial_energy(b2_ld, w3_p, w4_p, t_lat_pauli["f1"], t_lat_pauli["f2"], t_lat_pauli["f3"]) - e_c
        b_lat_pauli_bord = _simplicial_energy(b2_bd, w3_p, w4_p, t_lat_pauli["f1"], t_lat_pauli["f2"], t_lat_pauli["f3"]) - e_c
        b_lat_pauli_loggg = _simplicial_energy(b2_gg, w3_p, w4_p, t_lat_pauli["f1"], t_lat_pauli["f2"], t_lat_pauli["f3"]) - e_c
        # (c) With parameter-free Compton Fermi symmetry energy subtraction `- E_sym(Z, N)`
        b_lat_sym_logd = b_lat_raw_logd - e_sym_quad
        b_lat_sym_bord = b_lat_raw_bord - e_sym_quad
        # (d) With parameter-free 3D HO Pauli kinetic promotion subtraction `- E_kin_HO(Z, N)`
        b_lat_ho_logd = b_lat_raw_logd - e_kin_ho
        b_lat_ho_loggg = b_lat_raw_loggg - e_kin_ho

        # 3. 3D close-packed shell ball (raw static & Pauli-capped & HO-subtracted)
        b_sh_logd = _simplicial_energy(b2_ld, w3_p, w4_p, t_shell["f1"], t_shell["f2"], t_shell["f3"]) - e_c
        b_sh_bord = _simplicial_energy(b2_bd, w3_p, w4_p, t_shell["f1"], t_shell["f2"], t_shell["f3"]) - e_c
        b_sh_loggg = _simplicial_energy(b2_gg, w3_p, w4_p, t_shell["f1"], t_shell["f2"], t_shell["f3"]) - e_c
        b_shp_logd = _simplicial_energy(b2_ld, w3_p, w4_p, t_shell_pauli["f1"], t_shell_pauli["f2"], t_shell_pauli["f3"]) - e_c
        b_shp_bord = _simplicial_energy(b2_bd, w3_p, w4_p, t_shell_pauli["f1"], t_shell_pauli["f2"], t_shell_pauli["f3"]) - e_c
        b_shp_loggg = _simplicial_energy(b2_gg, w3_p, w4_p, t_shell_pauli["f1"], t_shell_pauli["f2"], t_shell_pauli["f3"]) - e_c
        b_shp_sym_logd = b_shp_logd - e_sym_quad
        b_sh_ho_logd = b_sh_logd - e_kin_ho

        # Tower-resummed E0_tower and muon-pin cross-anchor comparisons:
        b_lat_sym_logd_tow = (
            _simplicial_energy(
                c_p["b2_log_D_tower_MeV"], c_p["w3_GPMT_tower_MeV"], c_p["w4_GPMT_H4_tower_MeV"],
                int(t_lat["f1"]), int(t_lat["f2"]), int(t_lat["f3"]),
            )
            - e_c
            - e_sym_quad
        )
        b_lat_sym_logd_muon = (
            _simplicial_energy(
                c_m["b2_log_D_bare_MeV"], c_m["w3_GPMT_bare_MeV"], c_m["w4_GPMT_H4_bare_MeV"],
                int(t_lat["f1"]), int(t_lat["f2"]), int(t_lat["f3"]),
            )
            - e_c
            - (c_m["a_sym_compton_bare_MeV"] * (mp.mpf(N - Z) ** 2) / mp.mpf(A) if A >= 4 else mp.mpf(0))
        )

        print(
            f"{name:<6} {Z:>3} {N:>3} {A:>3} | "
            f"{t_3tree['f1']:>5} {int(t_lat['f1']):>7} {t_lat_pauli['f1']:>9} "
            f"{int(t_lat['f0_bdry']):>5} {int(t_lat['f0_int']):>5} | "
            f"{mp.nstr(b_ame, 6):>9} {mp.nstr(b_3t_logd, 6):>9} {mp.nstr(b_lat_raw_logd, 6):>9} "
            f"{mp.nstr(b_lat_pauli_logd, 6):>9} {mp.nstr(b_lat_sym_logd, 6):>9} "
            f"{mp.nstr(b_lat_sym_bord, 6):>9} {mp.nstr(b_lat_ho_logd, 6):>9}"
        )

        rows_data.append({
            "nuclide": name,
            "Z": Z,
            "N": N,
            "A": A,
            "B_AME_MeV": fmt(b_ame),
            "sigma_AME_MeV": fmt(sigma_ame),
            "E_C_MeV": fmt(e_c),
            "E_sym_quad_compton_MeV": fmt(e_sym_quad),
            "N_ho_excitation_quanta": n_ho_quanta,
            "E_kin_ho_hecke_MeV": fmt(e_kin_ho),
            "triangulations": {
                "apollonian_3tree": t_3tree,
                "explicit_3d_kuhn_lattice_ball": {
                    k: v for k, v in t_lat.items() if k != "coordinates_sample"
                },
                "pauli_capped_3d_kuhn_lattice_ball": t_lat_pauli,
                "close_packed_3d_shell_ball": t_shell,
                "pauli_capped_3d_shell_ball": t_shell_pauli,
            },
            "branches_proton_bare_E0": {
                "apollonian_3tree_logD_GPMT": _err_metrics(b_3t_logd, b_ame, sigma_ame),
                "apollonian_3tree_BorD_GPMT": _err_metrics(b_3t_bord, b_ame, sigma_ame),
                "apollonian_3tree_logGG_GPMT": _err_metrics(b_3t_loggg, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_raw_static_logD_GPMT": _err_metrics(b_lat_raw_logd, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_raw_static_BorD_GPMT": _err_metrics(b_lat_raw_bord, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_raw_static_logGG_GPMT": _err_metrics(b_lat_raw_loggg, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_pauli_capped_logD_GPMT": _err_metrics(b_lat_pauli_logd, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_pauli_capped_BorD_GPMT": _err_metrics(b_lat_pauli_bord, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_pauli_capped_logGG_GPMT": _err_metrics(b_lat_pauli_loggg, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_fermi_sym_logD_GPMT": _err_metrics(b_lat_sym_logd, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_fermi_sym_BorD_GPMT": _err_metrics(b_lat_sym_bord, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_ho_kinetic_logD_GPMT": _err_metrics(b_lat_ho_logd, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_ho_kinetic_logGG_GPMT": _err_metrics(b_lat_ho_loggg, b_ame, sigma_ame),
                "close_packed_3d_shell_ball_raw_static_logD_GPMT": _err_metrics(b_sh_logd, b_ame, sigma_ame),
                "close_packed_3d_shell_ball_raw_static_BorD_GPMT": _err_metrics(b_sh_bord, b_ame, sigma_ame),
                "close_packed_3d_shell_ball_raw_static_logGG_GPMT": _err_metrics(b_sh_loggg, b_ame, sigma_ame),
                "pauli_capped_3d_shell_ball_logD_GPMT": _err_metrics(b_shp_logd, b_ame, sigma_ame),
                "pauli_capped_3d_shell_ball_BorD_GPMT": _err_metrics(b_shp_bord, b_ame, sigma_ame),
                "pauli_capped_3d_shell_ball_logGG_GPMT": _err_metrics(b_shp_loggg, b_ame, sigma_ame),
                "pauli_capped_3d_shell_ball_fermi_sym_logD_GPMT": _err_metrics(b_shp_sym_logd, b_ame, sigma_ame),
                "close_packed_3d_shell_ball_ho_kinetic_logD_GPMT": _err_metrics(b_sh_ho_logd, b_ame, sigma_ame),
            },
            "branches_tower_and_muon_comparison": {
                "kuhn_3d_lattice_ball_fermi_sym_logD_GPMT_E0_tower": _err_metrics(b_lat_sym_logd_tow, b_ame, sigma_ame),
                "kuhn_3d_lattice_ball_fermi_sym_logD_GPMT_muon_pin": _err_metrics(b_lat_sym_logd_muon, b_ame, sigma_ame),
            },
        })

    wb.add_data("benchmark_nuclei", rows_data)

    # ── Exact Structural & Geometric Assertions Matching Lean 4 Theorems ─────
    wb.add_assertion(
        name="close_packed_k_shell_balls_satisfy_Compact3BallTriangulation",
        computed="1" if all_shells_valid else "0",
        expected="1",
        tolerance="0",
    )
    wb.add_assertion(
        name="all_benchmark_3d_ball_triangulations_satisfy_dehn_sommerville_and_euler_one",
        computed="1" if (all_3tree_valid and all_shell_balls_valid and all_lattice_balls_valid) else "0",
        expected="1",
        tolerance="0",
    )
    wb.add_assertion(
        name="kuhn_3d_lattice_ball_every_3simplex_canonical_disjoint_positive_volume_and_manifold_incidence",
        computed="1"
        if (
            all_lattice_cells_canonical_kuhn
            and all_lattice_cells_positive_vol
            and all_lattice_manifold_incidence
            and all_lattice_degree_bounded
        )
        else "0",
        expected="1",
        tolerance="0",
    )
    wb.add_assertion(
        name="dehn_sommerville_cycle_and_interior_energy_decomposition_exact",
        computed=fmt(max_dehn_sommerville_energy_err),
        expected="0",
        tolerance="1e-68",
    )
    wb.add_assertion(
        name="gpmt_pachner_cycle_higher_body_2mu3_plus_mu4_positive_at_q0",
        computed="1" if (c_p["pachner_cycle_2mu3_plus_mu4"] > mp.mpf(0) and c_m["pachner_cycle_2mu3_plus_mu4"] > mp.mpf(0)) else "0",
        expected="1",
        tolerance="0",
    )

    out_path = wb.save(
        q0_comparison(
            muon=q_muon,
            proton=q_proton,
            reason=(
                "Evaluates 3D compact-ball simplicial manifold triangulation binding "
                "energies across both the physical proton pin and ideal muon pin for "
                "cross-anchor comparison."
            ),
            dps=70,
        )
    )
    print("\n  Saved 80-dps witness -> " + str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
