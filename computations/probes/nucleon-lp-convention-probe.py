#!/usr/bin/env python3
"""jqjx / qou-v4iw (TN-9): nucleon LP convention probe at 80-dps mpmath.

Three conventions on ONE construction (the retired script's typed nucleon):
  OLD  = retired script: z = 1/(sqrt q + 1/sqrt q), tr_M(e-) = z^3
  HALF = the bean's scratch: OLD's z and Gram, tr_M(e-) = h z^2 + z   <- trace only
  D    = live pyhecke.gram: z = q^3/(q^2+1),      tr_M(e-) = h z^2 + z

TN-9 remediation (bean qou-v4iw):
  1. Pure 80-dps ``mpmath`` throughout (zero ``numpy``, zero ``float64``).
  2. Separates the two Gram pairings on ``H_3(q)``:
     - **Bilinear (no-star) Gram** ``G_{ij} = tr_M(b_i · b_j)`` (matching
       ``pyhecke.gram.G``; built by right-multiplying ``b_i`` by ``b_j``, i.e.
       ``reversed(NF_BASIS[j])`` through left-multiplication ``hm``): signature
       ``(4+, 1-, 1 zero)`` under D, with lowest eigenvalue
       ``w[0] = -0.7527021132519655...`` on ``(L_+ - L_-)/sqrt(2)`` and radical
       at ``idx_null = argmin(|w|) = 1`` (``|w[1]| ~ 10^-80`` at 80 dps).
     - **Hecke *-Gram** ``S_{ij} = tr_M(b_i · b_j^*)`` (``T_w^* = T_{w^-1}``,
       built when ``NF_BASIS[j]`` is fed unreversed into left-multiplication
       ``hm``): swaps ``L_+ <-> L_-`` diagonal and off-diagonal entries, turning
       ``-0.75270211...`` into ``+0.75270211...`` for PSD signature
       ``(5+, 0-, 1 zero)`` with radical at ``idx_null = argmin(|w|) = 0``.
  3. Fixes radical extraction in Part 2 from ``V[:, 0]`` / ``w[0]`` (which on
     the bilinear ``G_D`` grabbed the negative ghost mode ``(L_+ - L_-)/sqrt(2)``
     with ``w[0] = -0.75270211...``!) to ``idx_null = argmin(|w|)``.
"""
from __future__ import annotations

import sys
from itertools import product as cartprod
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _bridge

from mpmath import mp  # noqa: E402
from qou_substrate import q_at, set_compute_dps  # noqa: E402

WORK_DPS = 80
set_compute_dps(WORK_DPS)
mp.dps = WORK_DPS

ZERO = mp.mpf(0)
ONE = mp.mpf(1)
TWO = mp.mpf(2)
HALF_MP = ONE / TWO
TINY_PRUNE = mp.mpf("1e-75")
STAB_TOL = -mp.mpf("1e-35")
FLOOR_GUARD = mp.mpf("1e-300")

q0 = q_at(WORK_DPS)
qi0 = ONE / q0
h = q0 - qi0

NAMES = ["g", "s0", "s1", "L+", "L-", "e-"]
NF_BASIS: list[tuple[int, ...]] = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]


def hm(nf: list[mp.mpf], c: mp.mpf, d: mp.mpf, gen: int) -> list[mp.mpf]:
    """Left-multiply NF vector ``nf`` by ``(c * sigma_gen + d * 1)``."""
    r = [ZERO] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h), (1, d), (4, d)] if False else [(4, c * h), (1, c), (4, d)]),
            (5, [(5, c * h), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if mp.fabs(nf[si]) < TINY_PRUNE:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return r


def build_gram(trm: list[mp.mpf], *, star: bool = False) -> mp.matrix:
    """Build 6x6 Gram matrix over NF_BASIS at working mpmath precision.

    Because ``hm`` left-multiplies by ``sigma_gen``:
      - ``star=False`` iterates ``reversed(NF_BASIS[j])`` to form ``b_j * b_i``,
        whose trace ``tr_M(b_j b_i) = tr_M(b_i b_j)`` is the bilinear Gram ``G``
        of ``pyhecke.gram.G`` (signature ``(4+, 1-, 1 zero)`` under D).
      - ``star=True`` iterates ``NF_BASIS[j]`` forward to form ``b_j^* * b_i``,
        whose trace ``tr_M(b_j^* b_i) = tr_M(b_i b_j^*)`` is the Hecke *-Gram ``S``
        (signature ``(5+, 0-, 1 zero)`` under D).
    """
    G = mp.matrix(6, 6)
    for i in range(6):
        for j in range(6):
            cur = [ZERO] * 6
            cur[i] = ONE
            word = NF_BASIS[j] if star else tuple(reversed(NF_BASIS[j]))
            for g in word:
                cur = hm(cur, ONE, ZERO, g)
            G[i, j] = mp.fsum(cur[k] * trm[k] for k in range(6))
    return G


def mat_vec(G: mp.matrix, x: list[mp.mpf]) -> list[mp.mpf]:
    return [mp.fsum(G[i, j] * x[j] for j in range(6)) for i in range(6)]


def typed(z: mp.mpf, trm: list[mp.mpf], G: mp.matrix):
    nf_b3 = [ONE, ZERO, ZERO, ZERO, ZERO, ZERO]
    for _ in range(3):
        nf_b3 = hm(nf_b3, ONE, ZERO, 0)
        nf_b3 = hm(nf_b3, ONE, -h, 1)

    def mk(g_ud1: int, g_ud0: int) -> list[mp.mpf]:
        x = hm(nf_b3[:], ONE, ZERO, 0)          # uu
        x = hm(x, ONE, -h * HALF_MP, g_ud1)     # ud gen 1
        x = hm(x, ONE, -h * HALF_MP, g_ud0)     # ud gen 0
        return x

    p9 = mk(1, 0)
    n9 = hm(hm(hm(nf_b3[:], ONE, -h * HALF_MP, 0), ONE, -h, 1), ONE, -h * HALF_MP, 0)
    tr = lambda nf: mp.fsum(nf[i] * trm[i] for i in range(6))
    st = lambda nf: all(v >= STAB_TOL for v in mat_vec(G, nf))
    return p9, n9, tr, st


z_old = ONE / (mp.sqrt(q0) + mp.sqrt(qi0))
z_D = (q0 ** 3) / (q0 ** 2 + ONE)

CONV = {
    "OLD  (retired: z_old, e-=z^3)": (z_old, lambda z: [ONE, z, z, z ** 2, z ** 2, z ** 3]),
    "HALF (bean: z_old, e-=hz^2+z)": (z_old, lambda z: [ONE, z, z, z ** 2, z ** 2, h * (z ** 2) + z]),
    "D    (live: z_D,   e-=hz^2+z)": (z_D, lambda z: [ONE, z, z, z ** 2, z ** 2, h * (z ** 2) + z]),
}

print(f"q0 = {mp.nstr(q0, 20)}   h = {mp.nstr(h, 10)}   (working dps = {WORK_DPS})")
print(
    f"z_old = {mp.nstr(z_old, 12)}   z_D = {mp.nstr(z_D, 12)}   "
    f"ratio = {mp.nstr(z_D / z_old, 9)}\n"
)

for label, (z, mk_trm) in CONV.items():
    trm = mk_trm(z)
    G_bil = build_gram(trm, star=False)
    S_star = build_gram(trm, star=True)
    ev_bil = sorted(mp.eigsy(G_bil)[0])
    ev_star = sorted(mp.eigsy(S_star)[0])
    p9, n9, tr, st_bil = typed(z, trm, G_bil)
    _, _, _, st_star = typed(z, trm, S_star)
    print("=" * 78)
    print(label)
    print(f"  tr_M(e-) = {mp.nstr(trm[5], 12)}")
    print("  Bilinear G_{ij}=tr_M(b_i b_j) eigs: " + " ".join(mp.nstr(v, 5) for v in ev_bil))
    print(f"    det G_bil  = {mp.nstr(mp.det(G_bil), 6)}   min_eig = {mp.nstr(ev_bil[0], 6)}")
    print("  Hecke *-Gram S_{ij}=tr_M(b_i b_j^*) eigs: " + " ".join(mp.nstr(v, 5) for v in ev_star))
    print(f"    det S_star = {mp.nstr(mp.det(S_star), 6)}   min_eig = {mp.nstr(ev_star[0], 6)}")
    for nm, nf in (("proton", p9), ("neutron", n9)):
        gx_bil = mat_vec(G_bil, nf)
        gx_star = mat_vec(S_star, nf)
        idx_min_bil = min(range(6), key=lambda k: gx_bil[k])
        idx_min_star = min(range(6), key=lambda k: gx_star[k])
        print(f"  {nm:8s} NF = [" + " ".join(mp.nstr(v, 5) for v in nf) + "]")
        print(
            f"           tr_M = {mp.nstr(tr(nf), 7)}   "
            f"bil: stable={st_bil(nf)} min(Gx)={mp.nstr(gx_bil[idx_min_bil], 7)}@{NAMES[idx_min_bil]} | "
            f"star: stable={st_star(nf)} min(Sx)={mp.nstr(gx_star[idx_min_star], 7)}@{NAMES[idx_min_star]}"
        )
    print()

# ══════════════════════════════════════════════════════════════
# Part 2: under D the Gram is SINGULAR — argmin(|w|) vs w[0]
# ══════════════════════════════════════════════════════════════
print("=" * 78)
print("PART 2 — the radical under D: bilinear G_D vs Hecke *-Gram S_D (TN-9 fix)")
print("=" * 78)

trm_D = [ONE, z_D, z_D, z_D ** 2, z_D ** 2, h * (z_D ** 2) + z_D]
G_D = build_gram(trm_D, star=False)
S_D = build_gram(trm_D, star=True)

closed_raw = [(-qi0) ** len(b) for b in NF_BASIS]
closed_norm = mp.sqrt(mp.fsum(v * v for v in closed_raw))
closed = [v / closed_norm for v in closed_raw]

for tag, M_D in (("Bilinear G_D (no-star, pyhecke.gram.G)", G_D),
                 ("Hecke *-Gram S_D (T_w^* = T_{w^-1})", S_D)):
    w_raw, V_raw = mp.eigsy(M_D)
    order = sorted(range(6), key=lambda k: w_raw[k])
    w = [w_raw[k] for k in order]
    cols = [[V_raw[r, k] for r in range(6)] for k in order]

    # TN-9 FIX: select radical by argmin(|w|), NOT index 0!
    idx_null = min(range(6), key=lambda k: mp.fabs(w[k]))
    null = cols[idx_null][:]
    dot_c = mp.fsum(closed[r] * null[r] for r in range(6))
    closed_aligned = [-v for v in closed] if dot_c < ZERO else closed[:]
    next_abs = min(mp.fabs(w[k]) for k in range(6) if k != idx_null)
    null_floor = max(mp.fabs(w[idx_null]), FLOOR_GUARD)
    spectral_gap = next_abs / null_floor
    agree_max = max(mp.fabs(null[r] - closed_aligned[r]) for r in range(6))
    resid_max = max(mp.fabs(v) for v in mat_vec(M_D, closed_aligned))

    # Also record what the buggy index-0 choice gave for before/after transparency:
    v0 = cols[0][:]
    if mp.fsum(closed[r] * v0[r] for r in range(6)) < ZERO:
        v0 = [-v for v in v0]
    buggy_v0_err = max(mp.fabs(v0[r] - closed[r]) for r in range(6))

    print(f"  [{tag}]")
    print(f"    sorted w[0] = {mp.nstr(w[0], 10)} (index 0);  idx_null = argmin(|w|) = {idx_null}")
    print(
        f"    |w[idx_null]| = {mp.nstr(mp.fabs(w[idx_null]), 5)};  "
        f"min_{{k!=null}} |w[k]| = {mp.nstr(next_abs, 10)}  -> gap ratio {mp.nstr(spectral_gap, 4)}"
    )
    print(f"    agreement |v_null - v_closed|_max = {mp.nstr(agree_max, 4)}  (buggy v[0] err = {mp.nstr(buggy_v0_err, 4)})")
    print(f"    ||M_D @ v_closed||_max = {mp.nstr(resid_max, 4)}  (0 => genuine radical)")
    print()

p9, n9, tr_D, st_D_bil = typed(z_D, trm_D, G_D)
_, _, _, st_D_star = typed(z_D, trm_D, S_D)

w_bil_raw, _ = mp.eigsy(G_D)
rad_floor_bil = max(min(mp.fabs(ev) for ev in w_bil_raw), FLOOR_GUARD)

for nm, nf in (("proton", p9), ("neutron", n9)):
    comp = mp.fsum(nf[r] * closed[r] for r in range(6))
    x_q = [nf[r] - comp * closed[r] for r in range(6)]
    gx, gx_q = mat_vec(G_D, nf), mat_vec(G_D, x_q)
    sx, sx_q = mat_vec(S_D, nf), mat_vec(S_D, x_q)
    min_gx, min_gx_q = min(gx), min(gx_q)
    min_sx, min_sx_q = min(sx), min(sx_q)
    margin_over_floor = min_gx / rad_floor_bil
    print(f"  {nm}: component along radical = {mp.nstr(comp, 7)}")
    print(
        f"     bilinear min(G_D x) = {mp.nstr(min_gx, 7)} | on quot. = {mp.nstr(min_gx_q, 7)} "
        f"(change {mp.nstr(mp.fabs(min_gx - min_gx_q), 4)})"
    )
    print(
        f"     *-Gram   min(S_D x) = {mp.nstr(min_sx, 7)} | on quot. = {mp.nstr(min_sx_q, 7)} "
        f"(change {mp.nstr(mp.fabs(min_sx - min_sx_q), 4)})"
    )
    print(f"     margin / 80-dps radical floor = {mp.nstr(margin_over_floor, 4)}")
print()

# ══════════════════════════════════════════════════════════════
# Part 3: re-run the gluon LP under D (both bilinear G_D and *-Gram S_D)
# ══════════════════════════════════════════════════════════════
print("=" * 78)
print("PART 3 — the gluon LP under D (min |tr_M|, stable at every step)")
print("=" * 78)

ops = [
    ("s0", lambda nf: hm(nf, ONE, ZERO, 0)),
    ("s1", lambda nf: hm(nf, ONE, ZERO, 1)),
    ("L+", lambda nf: hm(hm(nf, ONE, ZERO, 0), ONE, ZERO, 1)),
    ("L-", lambda nf: hm(hm(nf, ONE, ZERO, 1), ONE, ZERO, 0)),
]


def lp(base: list[mp.mpf], tr, st, max_depth: int = 3):
    res = []
    if st(base):
        res.append((0, [], base[:], tr(base)))
    for depth in range(1, max_depth + 1):
        for combo in cartprod(range(4), repeat=depth):
            nf, names, ncross, ok = base[:], [], 0, True
            for oi in combo:
                nf = ops[oi][1](nf)
                names.append(ops[oi][0])
                ncross += 2 if ops[oi][0] in ("L+", "L-") else 1
                if not st(nf):
                    ok = False
                    break
            if ok:
                res.append((ncross, names, nf[:], tr(nf)))
    seen, uniq = set(), []
    for r in res:
        k = tuple(mp.nstr(v, 12) for v in r[2])
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    uniq.sort(key=lambda r: mp.fabs(r[3]))
    return uniq


for pairing_lbl, st_fn in (("bilinear G_D", st_D_bil), ("*-Gram S_D", st_D_star)):
    print(f"  [{pairing_lbl}]")
    for nm, nf in (("proton", p9), ("neutron", n9)):
        r = lp(nf, tr_D, st_fn)
        print(f"    {nm}: {len(r)} feasible")
        for i, (nc, names, _, t) in enumerate(r[:4]):
            tag = "  <- BARE (0 gluons)" if nc == 0 else ""
            print(
                f"      {i + 1}. {nc} crossings  {'.'.join(names) or '(none)':16s} "
                f"|tr_M| = {mp.nstr(mp.fabs(t), 7)}{tag}"
            )
        mincr = min(x[0] for x in r)
        print(f"      min-crossing-first optimum: {mincr} crossings")

# ══════════════════════════════════════════════════════════════
# Part 4: the specific corpus sentences, tested one by one
# ══════════════════════════════════════════════════════════════
print()
print("=" * 78)
print("PART 4 — the corpus's individual claims under D")
print("=" * 78)


def steps_D(label: str, seq):
    """Walk the typed build, reporting stability at every intermediate step."""
    nf = [ONE, ZERO, ZERO, ZERO, ZERO, ZERO]
    for _ in range(3):
        nf = hm(nf, ONE, ZERO, 0)
        nf = hm(nf, ONE, -h, 1)
    print(
        f"  {label}: B3  tr_M = {mp.nstr(tr_D(nf), 7)}  "
        f"bil_stable = {st_D_bil(nf)}  star_stable = {st_D_star(nf)}"
    )
    for name, c, d, g in seq:
        nf = hm(nf, c, d, g)
        min_bil = min(mat_vec(G_D, nf))
        min_star = min(mat_vec(S_D, nf))
        print(
            f"    after {name:22s} tr_M = {mp.nstr(tr_D(nf), 7)}  "
            f"min(G_D x) = {mp.nstr(min_bil, 7)}  min(S_D x) = {mp.nstr(min_star, 7)}"
        )
    return nf


steps_D(
    "proton  (uud)",
    [
        ("uu  (s0)", ONE, ZERO, 0),
        ("ud  (s1, -h/2)", ONE, -h * HALF_MP, 1),
        ("ud  (s0, -h/2)", ONE, -h * HALF_MP, 0),
    ],
)
print()
steps_D(
    "neutron (udd)",
    [
        ("ud  (s0, -h/2)", ONE, -h * HALF_MP, 0),
        ("dd  (s1, -h)", ONE, -h, 1),
        ("ud  (s0, -h/2)", ONE, -h * HALF_MP, 0),
    ],
)
print()

print("  Where the corpus's quoted optima land under D (bilinear G_D / *-Gram S_D):")
for pairing_lbl, st_fn in (("bilinear G_D", st_D_bil), ("*-Gram S_D", st_D_star)):
    print(f"    [{pairing_lbl}]")
    for nm, base, want in (("proton", p9, ["s0", "s0"]), ("neutron", n9, ["L+", "L-"])):
        r = lp(base, tr_D, st_fn)
        for rank, (nc, names, _, t) in enumerate(r, 1):
            if names == want:
                print(
                    f"      {nm:8s} {'.'.join(want):8s} -> rank {rank}/{len(r)}, "
                    f"{nc} crossings, |tr_M| = {mp.nstr(mp.fabs(t), 7)}"
                )
                break
        else:
            print(f"      {nm:8s} {'.'.join(want):8s} -> NOT FEASIBLE under D")
        bare = [x for x in r if x[0] == 0]
        bare_msg = (
            f"feasible, |tr_M| = {mp.nstr(mp.fabs(bare[0][3]), 7)}"
            if bare
            else "NOT feasible"
        )
        print(f"               bare (0 gluons) -> {bare_msg}")
