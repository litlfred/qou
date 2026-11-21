#!/usr/bin/env python3
"""Every number in the `t7qv` binding-gap arc was measured in float64. Re-run at
200 bits: the conclusions survive, most of the **evidence** offered for them did
not exist.

WHAT THIS CORRECTS — AND IT CORRECTS ME
---------------------------------------
`docs/precision-goals.md` forbids float64 in the hot path of anything that feeds
a witnessed quantity, and `.claude/agent-memory/compute-precision-auditor/`
rule 4 forbids calling a float64 agreement "exact". The mass/binding arc broke
both, in **two** places at once:

1. **The matrices.** Every trace ran through
   `hecke_characters.build_seminormal_matrices` -> `numpy.ndarray(dtype=float)`
   -> `scipy.sparse.csr_matrix(dtype=float)`. The exact twin
   `build_seminormal_matrices_mp` sits three hundred lines below it in the same
   file, with a docstring that says in as many words why it exists. It was not
   used.

2. **The substrate parameter itself — the worse of the two.** Every probe in the
   arc opened with `q = mp.mpf(str(Q0))`, which *looks* like arbitrary
   precision. `Q0` is `qou_substrate.constants.Q`, a Python `float`. `str()` of
   it is 17 digits. So the mpmath q carried **float64 information and nothing
   more**, and h inherited it:

       float64 h, as the arc used it   0.20906029879563937
       200-bit h                       0.2090602987956393154308462131296749

   -- agreeing to 16 significant figures and no further. Two losses stack: the
   truncated q costs 1.4e-17 by itself, and doing the subtraction in float64 on
   top of that costs another ~4e-17. `Q_50_DIGIT_STR` was available the whole
   time and is what this probe uses.

Then, having built the whole arc on that, I read ~1e-15 residuals as evidence of
exact identities and said so — repeatedly, and in the last case I *concluded*
exactness from a float64 measurement. That is the failure mode rule 4 names:
1e-15 IS the float64 floor, so those residuals are what you see whether the
identity holds or fails at 1e-14. The claims were unsupported as stated.

WHAT THIS PROBE DOES
--------------------
Rebuilds the trace engine with no float64 anywhere -- q from `Q_50_DIGIT_STR`,
seminormal matrices from the same a / a' / b formulas as the corpus's exact
`build_seminormal_matrices_mp`, sparse rows of MPFR (or mpmath) scalars -- and
re-measures every identity the arc asserted at A = 2, 3, 4.

RESULT: THE IDENTITIES ARE REAL. THE EVIDENCE WAS NOT.
------------------------------------------------------
Residuals drop from the float64 floor to the 200-bit floor, ~45 orders down:

    identity                              200-bit (A=3, A=4)
    exchangeability, nnn,  |S|=2          7.47e-60
    exchangeability, nnnn, |S|=2          1.18e-59
    exchangeability, nnnn, |S|=3          1.74e-59
    size-only recursion vs full Mobius    2.49e-60  (A=3)   4.98e-60  (A=4)
    additivity on disjoint parts          4.98e-60
    cumulant reconstruction = L_full      0.00e+00  (A=3)   2.49e-60  (A=4)

against which the arc's float64 figures -- 3.33e-15, 5.77e-15 and 6.22e-15 for
the |S| = 2, 3, 4 spreads, 7.55e-15 for size-only vs Mobius, and a printed
`0.000e+00` for additivity and for the reconstruction -- were all measured at
A = 5, which is the one place spreads were taken. So the columns are NOT the
same system, and this probe does not claim they are; the matching A = 5 exact
run is separate. What the two columns do share is the only thing at issue: an
identity that holds at the working floor at A = 3 and A = 4 is being asserted
of a family, and at A = 5 the float64 floor is where the assertion was read.

Every identity holds. Nothing in the arc's *conclusions* is retracted by this
probe. What is retracted is the arithmetic warrant: a residual at the working
floor is a statement about the floor, and the arc quoted six of them as though
they were statements about the algebra.

HOW WRONG WAS THE FLOAT64, ACTUALLY
-----------------------------------
Not very -- and knowing that is the point, because the arc never established it:

    L_pp   0.48989938425513485140655016749462194823043396786058
    L_pn   0.67682159238634338966311878404365178434961219856897
    L_nn   0.90726226553321290067017528738691153644541109117659

against the float64 values the arc quoted, the deltas are +1.35e-13, +3.43e-13,
+2.13e-13. So the arc's *magnitudes* were good to ~13 digits, not the ~15 it
implicitly claimed, and the 13 is set by the truncated q, not by the matrix
arithmetic. `Q_ERR = 9.21e-13` puts the physical ceiling in the same place:
q0 is itself a solved constant with a stated uncertainty, so no quantity in this
arc means anything below ~1e-12 as physics, whatever the precision of the run.
The high-precision run is for testing **algebraic identities**, which hold for
every q and so can be probed as far down as the arithmetic goes.

A BONUS THE EXACT RUN MADE VISIBLE: L IS n-INDEPENDENT
-------------------------------------------------------
L_nn is bit-identical (to the last retained digit) computed at n = 6, at n = 9
inside a 3-body system, and at n = 12 inside a 4-body one. That is the Markov
split-link factorisation -- an unbonded nucleon is a separate component and
contributes the same factor to numerator and denominator -- and it is the same
fact as the additivity result, read at a different angle.

It is not decoration. It means the k-body cumulant input `L_k` is computable in
its **own** minimal system, n = 3k, rather than inside the ambient n = 3A. The
float64 A=6 run this replaces was spending five n=18 traces to re-derive what
n = 6, 9, 12, 15 already fix; the exact A=6 run needs two.

A = 5, LANDED SEPARATELY (200-bit, 2026-09-03, ~29 min per ordering)
--------------------------------------------------------------------
Out of this probe's CI budget, so run by the same engine as a detached job.
The raw 60-digit subset traces `L_S` are committed alongside as
`*.a5_exact.{pnpnn,nnnnn}.json`, and section 7 below RE-DERIVES everything
from them -- cumulants, reconstruction, exchangeability, size-only recursion
-- rather than copying a log. Both orderings the arc used, all 26 subsets:

    5He (pnpnn)     c_2 +7.272615735   c_3 -3.786046394   c_4 -1.230795704
                    c_5 +1.604498983   |c_5/c_4| = 1.303627   signs + - - +
    nnnnn           c_2 +9.072622655   c_3 -5.081967559   c_4 -1.148549425
                    c_5 +1.955406398   |c_5/c_4| = 1.702501   signs + - - +

    reconstruction residual        0 at 200 bits, both orderings
    exchangeability (nnnnn)        |S|=2: 1.74e-59  |S|=3: 2.49e-59  |S|=4: 1.74e-59
    size-only vs full Mobius       4.23e-59  (re-derived here from the stored
                                   60-digit strings; the run itself printed
                                   3.73e-59 -- both are the working floor)

Every A=5 figure the arc quoted in float64 is reproduced to all nine printed
digits, and the same-system comparison the table above could not make is now
made: the arc's `3.33e-15 / 5.77e-15 / 6.22e-15` spreads and `7.55e-15`
recursion agreement are `1.74e-59 / 2.49e-59 / 1.74e-59` and `~4e-59`. The
`c_5` sign, the A=5 hierarchy, and the ratio straddling `1` across orderings
are established, not measured.

A = 6, LANDED SEPARATELY (128-bit, minimal-n route, 2026-09-03)
---------------------------------------------------------------
The homonuclear all-pairs A=6 hierarchy is exact at 128 bits: L_2..L_5 in
their own minimal systems, L_6 from two n=18 traces, written up and re-derived
from its committed sidecar by `the_size_only_recursion_reaches_order_six_probe`
(cross-checked against the 200-bit A=5 ambient run at ~1e-37). Its numbers are
there, not here.

WHAT IS NOT RE-ESTABLISHED HERE
-------------------------------
The MIXED A=6 figures the arc quoted (6Li, from the chain and all-pairs
constructions in float64) are not re-run: the full lattice at n=18 is 57 exact
traces, out of reach. They remain float64 measurements -- sign and magnitude
claims with margins ~1e13 above the float64 floor, not exact, not to be quoted
as exact. The float64 12-ordering sweep at A=5 is not re-run either: its sign
claim is covered by the two exact orderings, its ratio range is not.
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from math import comb
from pathlib import Path

COMP = Path(__file__).resolve().parent.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from hecke_characters import (  # noqa: E402
    standard_young_tableaux,
    build_seminormal_matrices,
    build_seminormal_matrices_mp,
)
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP, Q as Q_F64, Q_ERR  # noqa: E402
from pyhecke.constants import pn_interface_offset  # noqa: E402

BITS = 200  # ~60 decimal digits

# ── backend: MPFR when available (fast), mpmath otherwise (correct, slower) ──
try:
    import gmpy2

    gmpy2.get_context().precision = BITS
    MPF, SQRT, LOG, BACKEND = gmpy2.mpfr, gmpy2.sqrt, gmpy2.log, "gmpy2/MPFR"
except ImportError:  # pragma: no cover - CI without gmpy2
    mp.mp.prec = BITS
    MPF, SQRT, LOG, BACKEND = mp.mpf, mp.sqrt, mp.log, "mpmath"

mp.mp.dps = 60
Q = MPF(Q_50_DIGIT_STR)
H = Q - 1 / Q
ONE, ZERO = MPF(1), MPF(0)
# D_PN built from the closed form rather than round-tripped through a string:
# delta = (q-1)^2 (1 - q^-4)/3 and d_pn = -h(1 - delta/2)/2, exactly
# `pyhecke.constants.pn_interface_offset` under the canonical
# `bring_color_weighted` convention. Checked against it below.
DELTA = (Q - 1) ** 2 * (1 - Q ** -4) / 3
D_PN = -(H * (1 - DELTA / 2) / 2)

# ── the float64 figures the arc quoted, verbatim, for the delta table ──
F64_BONDS = {"pp": 0.489899384255, "pn": 0.676821592386, "nn": 0.907262265533}
# The arc only ever took spreads at A=5, so these are A=5 figures. They are
# quoted to show WHERE the arc read its evidence, not as a same-system control.
F64_RESID_A5 = {
    "exchangeability nnnnn |S|=2": 3.33e-15,
    "exchangeability nnnnn |S|=3": 5.77e-15,
    "exchangeability nnnnn |S|=4": 6.22e-15,
    "size-only vs Mobius": 7.55e-15,
    "additivity / reconstruction": 0.0,
}


# ══════════════════════════════════════════════════════════════════
# §1  Exact seminormal engine — sparse rows, no float64
# ══════════════════════════════════════════════════════════════════
def qint(m):
    """[m]_q in the exponent convention the arc's float engine used."""
    return sum(Q ** (m - 1 - 2 * i) for i in range(m))


def weights(n):
    """Convention-D (Wenzl level r=2) block weights: only <=2-row shapes live."""
    ks = list(range(n // 2 + 1))
    ps = [((n - k, k) if k else (n,)) for k in ks]
    raw = [qint(n - 2 * k + 1) for k in ks]
    dims = [comb(n, k) - comb(n, k - 1) if k else 1 for k in ks]
    Z = sum(r * d for r, d in zip(raw, dims))
    return ps, [r / Z for r in raw]


_SIG: dict = {}


def sigmas(shape):
    """sigma_1..sigma_{n-1} as row lists [(col, val)]. <=2 non-zeros per row.

    Same a / a' / b as `build_seminormal_matrices_mp`; §2 checks entry by entry.
    """
    key = tuple(shape)
    if key in _SIG:
        return _SIG[key]
    n = sum(shape)
    syts, _cells, contents = standard_young_tableaux(list(shape))
    dim = len(syts)
    idx = {tuple(sorted(t.items())): i for i, t in enumerate(syts)}
    out = []
    for k in range(1, n):
        rows: list[list] = [[] for _ in range(dim)]
        seen: set[int] = set()
        for i in range(dim):
            if i in seen:
                continue
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            a = H / (1 - Q ** (-2 * rho))
            ap = H / (1 - Q ** (2 * rho))
            sw = dict(syts[i])
            sw[k], sw[k + 1] = ci1, ci
            j = idx.get(tuple(sorted(sw.items())))
            if j == i:
                j = None
            if j is None:
                rows[i].append((i, a))
                seen.add(i)
            else:
                # a*a' = -1/[rho]^2 exactly, so a*a'+1 >= 0 whenever the swap
                # lands on another standard tableau (|rho| >= 2 there).
                b = SQRT(abs(a * ap + 1))
                rows[i] += [(i, a), (j, b)]
                rows[j] += [(j, ap), (i, b)]
                seen.add(i)
                seen.add(j)
        out.append(rows)
    _SIG[key] = (out, dim)
    return out, dim


def _op(rows, c, d):
    """c*sigma + d*I as row lists, merged so each row still holds <=2 entries."""
    res = []
    for i, r in enumerate(rows):
        acc: dict = {}
        for j, v in r:
            acc[j] = acc.get(j, ZERO) + c * v
        if d != 0:
            acc[i] = acc.get(i, ZERO) + d
        res.append([(j, v) for j, v in acc.items() if v != 0])
    return res


def trM(n, word):
    """sum_lambda w_lambda * tr_lambda(prod (c sigma_g + d I)), exactly.

    Propagates one basis row at a time through the sparse operators: O(2*W*d^2)
    scalar products per block instead of the O(W*d^3) a dense product costs.
    """
    ps, ws = weights(n)
    tot = ZERO
    for shape, w in zip(ps, ws):
        rows, dim = sigmas(shape)
        ops = [_op(rows[g], MPF(c), d) for c, d, g in word]
        acc = ZERO
        for s in range(dim):
            v = [ZERO] * dim
            v[s] = ONE
            nz = [s]
            for op in ops:
                out = [ZERO] * dim
                seen = []
                for i in nz:
                    vi = v[i]
                    if vi == 0:
                        continue
                    for j, m in op[i]:
                        if out[j] == 0:
                            seen.append(j)
                        out[j] = out[j] + vi * m
                v, nz = out, seen
            acc += v[s]
        tot += w * acc
    return tot


# ══════════════════════════════════════════════════════════════════
# §2  Words — the production `atom_gen_chains` bond order, letter for letter
# ══════════════════════════════════════════════════════════════════
B_P = (ZERO, ONE / 2, ONE / 2)
B_N = (ONE / 2, ONE / 2, ONE)


def nucleon_word(b, g0, g1):
    w = []
    for _ in range(3):
        w += [(1, ZERO, g0), (1, -H, g1)]
    w += [(1, -b[0] * H, g0), (1, -b[1] * H, g0), (1, -b[2] * H, g1)]
    return w + [(1, ZERO, g0), (1, ZERO, g0)]


def bond_d(a, b):
    return ZERO if a == b == "p" else (-H if a == b == "n" else D_PN)


def band(i, j, d):
    """Route a bond from nucleon i to nucleon j past the spectators between."""
    a, b = 3 * i + 2, 3 * j
    ups = list(range(b - 1, a, -1))
    return ([(1, ZERO, g) for g in ups] + [(1, d, a)]
            + [(1, -H, g) for g in reversed(ups)])


def word(order, S, parts=None):
    """Nucleon chain with bonds among `S` (or confined within each of `parts`)."""
    w = []
    for k in range(len(order)):
        w += nucleon_word(B_P if order[k] == "p" else B_N, 3 * k, 3 * k + 1)
        if parts is not None:
            for part in parts:
                if k in part:
                    for prev in sorted(part):
                        if prev < k:
                            w += [(1, bond_d(order[prev], order[k]), 3 * prev + 2)]
        elif k in S:
            for prev in range(k):
                if prev in S:
                    d = bond_d(order[prev], order[k])
                    w += ([(1, d, 3 * prev + 2)] if k == prev + 1
                          else band(prev, k, d))
    return w


def L_of(order, S):
    n = 3 * len(order)
    return LOG(trM(n, word(order, set())) / trM(n, word(order, set(S))))


def fmt(x, k=50):
    return mp.nstr(mp.mpf(str(x)), k, strip_zeros=False)


# ══════════════════════════════════════════════════════════════════
# §3  Main
# ══════════════════════════════════════════════════════════════════
def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nbackend {BACKEND} at {BITS} bits (~{BITS * 0.30103:.0f} digits)")

    # ── §3.1 the q input, which is where the arc actually lost its digits ──
    print("\n" + "=" * 68)
    print("§1  THE SUBSTRATE PARAMETER: WHAT float(Q) COSTS")
    print("=" * 68)
    q_arc = MPF(str(Q_F64))            # exactly what every probe in the arc did
    h_arc = q_arc - 1 / q_arc          # ... but with the arithmetic done exactly
    h_f64 = MPF(Q_F64 - 1 / Q_F64)     # ... and as the arc actually got it
    print(f"  Q (python float)   {Q_F64!r}   type {type(Q_F64).__name__}")
    print(f"  Q_50_DIGIT_STR     {Q_50_DIGIT_STR}")
    print(f"  Q_ERR              {Q_ERR:.4e}   (q0's own stated uncertainty)")
    print(f"  h, all in float64  {fmt(h_f64, 24)}   <- what the arc used")
    print(f"  h, exact from f(Q) {fmt(h_arc, 24)}   <- truncated q alone")
    print(f"  h from 50 digits   {fmt(H, 24)}   <- correct")
    dq, dh = abs(Q - q_arc), abs(H - h_arc)
    print(f"  |dq| {float(dq):.3e}   |dh| from the truncated q alone "
          f"{float(dh):.3e}")
    print(f"                        |dh| as the arc had it        "
          f"{float(abs(H - h_f64)):.3e}")
    check("float(Q) loses q0 below ~1e-17 (the arc's real precision ceiling)",
          1e-20 < float(dq) < 1e-15)
    check("q0's own uncertainty Q_ERR ~1e-12 dominates the float64 loss",
          Q_ERR > float(dq))

    # ── §3.2 the engine is a faithful twin of the corpus's exact route ──
    print("\n" + "=" * 68)
    print("§2  FAITHFULNESS: this engine vs `build_seminormal_matrices_mp`")
    print("=" * 68)
    qmp = Q_MP
    worst_mp_all = 0.0
    for shape in [(3, 1), (4, 2), (5, 3)]:
        rows_all, dim = sigmas(shape)
        ref, _rdim, _ = build_seminormal_matrices_mp(list(shape), qmp)
        f64, _, _ = build_seminormal_matrices(list(shape))
        wmp = wf64 = 0.0
        for g, rows in enumerate(rows_all):
            for i, r in enumerate(rows):
                for j, v in r:
                    wmp = max(wmp, float(abs(mp.mpf(str(v)) - ref[g][i, j])))
                    wf64 = max(wf64, float(abs(mp.mpf(str(v)) - mp.mpf(float(f64[g][i, j])))))
        worst_mp_all = max(worst_mp_all, wmp)
        print(f"  {str(shape):8s} dim {dim:3d}   vs mpmath-exact <= {wmp:.2e}"
              f"   vs float64 <= {wf64:.2e}")
    check("engine agrees with the corpus exact builder below 1e-45",
          worst_mp_all < 1e-45)
    d_ref = pn_interface_offset(qmp)
    d_gap = float(abs(mp.mpf(str(D_PN)) - d_ref))
    print(f"  D_PN closed form vs pn_interface_offset: {d_gap:.2e}")
    check("D_PN reproduces pn_interface_offset exactly", d_gap < 1e-45)

    # ── §3.3 the bond constants, exactly ──
    print("\n" + "=" * 68)
    print("§3  THE THREE BOND CONSTANTS AT 200 BITS")
    print("=" * 68)
    bonds = {}
    for name in ("pp", "pn", "nn"):
        bonds[name] = L_of(name, (0, 1))
        d = float(mp.mpf(str(bonds[name])) - mp.mpf(F64_BONDS[name]))
        print(f"  L_{name} = {fmt(bonds[name])}")
        print(f"         arc quoted {F64_BONDS[name]:.12f}   delta {d:+.3e}")
    check("float64 bond constants were good to ~1e-13, not 1e-15",
          all(1e-15 < abs(float(mp.mpf(str(bonds[k])) - mp.mpf(F64_BONDS[k])))
              < 1e-11 for k in bonds))
    check("L_pp < L_pn < L_nn ordering unchanged",
          bonds["pp"] < bonds["pn"] < bonds["nn"])

    # ── §3.4 the identities the arc quoted at the float64 floor ──
    print("\n" + "=" * 68)
    print("§4  THE IDENTITIES, RE-MEASURED 45 ORDERS BELOW WHERE THEY WERE READ")
    print("=" * 68)
    sizes = [3] + ([4] if BACKEND.startswith("gmpy2") else [])
    if 4 not in sizes:
        print("  (A=4 skipped: no gmpy2. mpmath-only run covers A<=3.)")
    resid_top = 0.0
    for A in sizes:
        order, n = "n" * A, 3 * A
        t0 = time.time()
        tf = trM(n, word(order, set()))
        allL = {}
        print(f"\n  --- exchangeability, {order} (n={n}) ---")
        for r in range(2, A + 1):
            vals = {S: LOG(tf / trM(n, word(order, set(S))))
                    for S in combinations(range(A), r)}
            allL.update(vals)
            spread = float(abs(max(vals.values()) - min(vals.values())))
            resid_top = max(resid_top, spread)
            print(f"    |S|={r}  {len(vals):2d} subsets   L = "
                  f"{fmt(list(vals.values())[0], 22)}   spread {spread:.3e}")
        # full Mobius cumulants vs the size-only recursion
        cum = {}
        for r in range(2, A + 1):
            for S in combinations(range(A), r):
                c = allL[S]
                for m in range(2, r):
                    c -= sum(cum[T] for T in combinations(S, m))
                cum[S] = c
        cs = {}
        for k in range(2, A + 1):
            cs[k] = allL[tuple(range(k))] - sum(comb(k, j) * cs[j]
                                                for j in range(2, k))
        worst = max(float(abs(cum[tuple(range(k))] - cs[k]))
                    for k in range(2, A + 1))
        resid_top = max(resid_top, worst)
        print(f"    size-only recursion vs full Mobius: worst |diff| {worst:.3e}"
              f"    ({time.time() - t0:.0f}s)")
        for k in range(2, A + 1):
            print(f"      c_{k} = {fmt(cs[k])}")
    check("every identity holds below 1e-55 (was quoted at the 1e-15 floor)",
          resid_top < 1e-55)
    print("\n  what the arc quoted, all of it measured at A=5 in float64:")
    for k, v in F64_RESID_A5.items():
        print(f"    {k:32s} {v:.3e}")
    print(f"  200-bit worst over A=3, A=4 above:  {resid_top:.3e}")

    # ── §3.5 additivity, which the arc reported as literally zero ──
    print("\n" + "=" * 68)
    print("§5  ADDITIVITY ON DISJOINT PARTS  (the arc printed '0.000e+00')")
    print("=" * 68)
    n = 3 * len(sizes and "nnnn"[:max(sizes)] or "nnn")
    order = "pnpn" if 4 in sizes else "pnp"
    A = len(order)
    n = 3 * A
    tf = trM(n, word(order, set()))
    parts = [{0, 1}, {2, 3}] if A == 4 else [{0, 1}, {2}]
    L1 = LOG(tf / trM(n, word(order, set(), parts=[parts[0]])))
    L2 = LOG(tf / trM(n, word(order, set(), parts=[parts[1]])))
    Lu = LOG(tf / trM(n, word(order, set(), parts=parts)))
    add = float(abs(L1 + L2 - Lu))
    print(f"  L(part 1)        {fmt(L1)}")
    print(f"  L(part 2)        {fmt(L2)}")
    print(f"  sum              {fmt(L1 + L2)}")
    print(f"  L(both together) {fmt(Lu)}")
    print(f"  residual         {add:.3e}   (float64 said 0.000e+00, which is"
          " what float64 says either way)")
    check("additivity is real, at the 200-bit floor rather than the f64 one",
          add < 1e-55)

    # ── §3.6 the bonus: L is n-independent ──
    print("\n" + "=" * 68)
    print("§6  L_S DEPENDS ONLY ON |S| *AND ON NOTHING OUTSIDE S*")
    print("=" * 68)
    nn2 = {A: L_of("n" * A, (0, 1)) for A in ([2, 3] + ([4] if 4 in sizes else []))}
    for A, v in nn2.items():
        print(f"  L_nn measured inside A={A} (n={3*A}):  {fmt(v)}")
    spread_n = float(max(abs(v - nn2[2]) for v in nn2.values()))
    print(f"  spread across ambient sizes: {spread_n:.3e}")
    check("L_k is computable in its own minimal system n=3k, not the ambient n",
          spread_n < 1e-55)
    print("\n  Consequence: the k-body cumulant input L_k needs 2 traces at"
          " n=3k,\n  not one per subset at n=3A. That is what makes A=6"
          " reachable exactly.")

    # ── §3.7 A=5, re-derived from the committed 200-bit traces ──
    print("\n" + "=" * 68)
    print("§7  A=5 FROM THE COMMITTED 200-BIT TRACES (re-derived, not copied)")
    print("=" * 68)
    import json as _json
    a5: dict = {}
    for order in ("pnpnn", "nnnnn"):
        side = Path(__file__).with_name(f"{Path(__file__).stem}.a5_exact.{order}.json")
        if not side.exists():
            print(f"  ({order}: sidecar absent, skipped)")
            continue
        d = _json.load(open(side))
        Ls = {tuple(int(x) for x in k.strip("()").split(",") if x.strip()): mp.mpf(v)
              for k, v in d["L"].items()}
        A5 = 5
        cum5: dict = {}
        for r in range(2, A5 + 1):
            for S in combinations(range(A5), r):
                c = Ls[S]
                for m in range(2, r):
                    c -= sum(cum5[T] for T in combinations(S, m))
                cum5[S] = c
        tot = {r: sum(cum5[S] for S in combinations(range(A5), r)) for r in range(2, A5 + 1)}
        resid5 = abs(sum(tot.values()) - Ls[tuple(range(A5))])
        print(f"\n  {order}  ({d['bits']} bits, {len(Ls)} traces"
              f"{', PARTIAL' if d.get('partial') else ''})")
        prev = None
        for r in range(2, A5 + 1):
            rt = abs(tot[r] / prev) if prev else None
            print(f"    k={r}  c_k = {mp.nstr(tot[r], 12):>16s}   ratio "
                  f"{mp.nstr(rt, 7) if rt is not None else '-'}")
            prev = tot[r]
        print(f"    reconstruction residual {mp.nstr(resid5, 3)}")
        rec = {"c": tot, "resid": resid5, "signs": [tot[r] > 0 for r in range(2, A5 + 1)]}
        if len(set(order)) == 1:
            spreads = {}
            for r in range(2, A5):
                vals = [Ls[S] for S in combinations(range(A5), r)]
                spreads[r] = max(vals) - min(vals)
            cs5: dict = {}
            for k in range(2, A5 + 1):
                cs5[k] = Ls[tuple(range(k))] - sum(comb(k, j) * cs5[j] for j in range(2, k))
            worst5 = max(abs(cum5[tuple(range(k))] - cs5[k]) for k in range(2, A5 + 1))
            print("    exchangeability spreads: " + "  ".join(
                f"|S|={r}: {mp.nstr(v, 3)}" for r, v in spreads.items()))
            print(f"    size-only recursion vs full Mobius: {mp.nstr(worst5, 3)}")
            rec.update(spreads=spreads, sizeonly=worst5)
        a5[order] = rec
    if a5:
        check("A=5: signs + - - + and reconstruction residual < 1e-55 in every recorded ordering",
              all(r["signs"] == [True, False, False, True] and r["resid"] < mp.mpf("1e-55")
                  for r in a5.values()))
        check("A=5 (pnpnn): |c_5/c_4| = 1.3036 > 1 at 200 bits",
              "pnpnn" in a5 and abs(a5["pnpnn"]["c"][5] / a5["pnpnn"]["c"][4]) > 1)
        check("A=5 (nnnnn): exchangeability and size-only recursion hold below 1e-55",
              "nnnnn" in a5 and all(v < mp.mpf("1e-55") for v in a5["nnnnn"]["spreads"].values())
              and a5["nnnnn"]["sizeonly"] < mp.mpf("1e-55"))

    # ── witness ──
    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        for order, r in a5.items():
            for k, v in r["c"].items():
                wb.add_data(f"a5_{order}_c{k}_200bit", mp.nstr(v, 30))
            wb.add_data(f"a5_{order}_reconstruction_resid", mp.nstr(r["resid"], 3))
            if "spreads" in r:
                for kk, v in r["spreads"].items():
                    wb.add_data(f"a5_{order}_exch_spread_{kk}", mp.nstr(v, 3))
                wb.add_data(f"a5_{order}_sizeonly_vs_mobius", mp.nstr(r["sizeonly"], 3))
        wb.set_description(
            "Precision audit of the t7qv binding-gap arc. The arc ran entirely "
            "in float64 -- both the seminormal matrices (numpy/scipy dtype=float) "
            "and, worse, the substrate parameter itself (q = mp.mpf(str(Q)) off "
            "a Python float, i.e. 17 digits). Re-measured at 200 bits with q "
            "from Q_50_DIGIT_STR. Every identity the arc asserted survives, with "
            "residuals falling from the float64 floor (~1e-15) to the 200-bit "
            "floor (~1e-60); the arc's magnitudes were accurate to ~1e-13. The "
            "conclusions stand; the arithmetic warrant offered for them did not.")
        for k, v in bonds.items():
            wb.add_data(f"L_{k}_200bit", fmt(v))
        wb.add_data("h_200bit", fmt(H))
        wb.add_data("d_pn_200bit", fmt(D_PN))
        wb.add_data("q_50_digits", Q_50_DIGIT_STR)
        wb.add_data("worst_identity_residual_200bit", f"{resid_top:.6e}")
        wb.add_data("additivity_residual_200bit", f"{add:.6e}")
        wb.add_data("float64_residuals_as_quoted_at_A5", str(F64_RESID_A5))
        wb.add_data("bond_deltas_f64_minus_200bit",
                    str({k: f"{float(mp.mpf(F64_BONDS[k]) - mp.mpf(str(bonds[k]))):.3e}"
                         for k in bonds}))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "A<=4 is computed here. A=5 is RE-DERIVED here from the committed "
            "200-bit subset traces of a detached run (sidecars "
            "*.a5_exact.{pnpnn,nnnnn}.json, same engine, 2026-09-03); the probe "
            "does not recompute those traces. The homonuclear all-pairs A=6 is "
            "exact at 128 bits in the_size_only_recursion_reaches_order_six_probe; "
            "the MIXED A=6 (6Li) figures in the arc remain float64 measurements -- "
            "sign and magnitude claims with margins ~1e13 above the float64 floor, "
            "not exact, not to be quoted as exact. The float64 12-ordering sweep "
            "at A=5 is not re-run; its sign claim is covered by the two exact "
            "orderings, its ratio range is not.")
        wb.add_caveat(
            "200-bit precision tests ALGEBRAIC identities, which hold for every "
            "q. It buys nothing physical: Q_ERR = 9.2e-13 is q0's own stated "
            "uncertainty, so no quantity in this arc carries physical meaning "
            "below ~1e-12 at any working precision.")
        wb.add_caveat(
            "The float64 route is not thereby shown harmless anywhere else. It "
            "was harmless HERE because every identity tested is exact and every "
            "magnitude is O(1); a cancellation-heavy quantity would not have "
            "survived, and the arc had no way to tell the difference.")
        wb.add_caveat(
            "The seminormal off-diagonal uses b = sqrt(|a a' + 1|). The absolute "
            "value is a no-op: a a' = -1/[rho]^2 exactly, and a branching swap "
            "forces |rho| >= 2, so the radicand is non-negative. It is retained "
            "to mirror `build_seminormal_matrices_mp` letter for letter.")
        print(f"\nWitness: {wb.save(extra={'q0Anchor': 'proton', 'q0Value': Q_50_DIGIT_STR, 'q0AnchorReason': 'q is MPF(Q_50_DIGIT_STR), the proton pin'})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
