"""jqjx: does the nucleon LP instability survive the corrected trace weight?

Three conventions on ONE construction (the retired script's typed nucleon):
  OLD  = retired script: z = 1/(sqrt q + 1/sqrt q), tr_M(e-) = z^3
  HALF = the bean's scratch: OLD's z and Gram, tr_M(e-) = h z^2 + z   <- trace only
  D    = live pyhecke.gram: z = q^3/(q^2+1),      tr_M(e-) = h z^2 + z

## On float64 in this file

This probe is deliberately binary64 throughout, and `probe-float64-guard`'s
default advice (redo it in exact arithmetic) would destroy what it measures.
The question Part 2 asks is *how singular the Gram matrix is under D* — the
answer, lambda_min ~ 3e-16, is a statement about the float64 noise floor, and
every margin below is reported as a ratio against that floor. Recomputing the
spectrum exactly would return an exact zero and answer a different question:
that the radical exists, which the closed form `(-1/q)^len(w)` already gives
analytically on line 115. The numerical run is the cross-check on that closed
form, so it has to stay numerical. Individual lines carry `# float64-ok:`.
"""
# This probe measures a float64 noise floor, so numpy's binary64 spectrum is
# the instrument, not an approximation of one. See the module docstring.
import sys, numpy as np  # float64-ok: see above
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))
from q_parameter import Q as q0, Q_INV as qi0, HA as h

NAMES = ['g', 's0', 's1', 'L+', 'L-', 'e-']
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]

def hm(nf, c, d, gen):
    r = [0.0] * 6
    if gen == 0:
        tables = [(0,[(1,c),(0,d)]), (1,[(1,c*h),(0,c),(1,d)]), (2,[(3,c),(2,d)]),
                  (3,[(3,c*h),(2,c),(3,d)]), (4,[(5,c),(4,d)]), (5,[(5,c*h),(4,c),(5,d)])]
    else:
        tables = [(0,[(2,c),(0,d)]), (1,[(4,c),(1,d)]), (2,[(2,c*h),(0,c),(2,d)]),
                  (3,[(5,c),(3,d)]), (4,[(4,c*h),(1,c),(4,d)]), (5,[(5,c*h),(3,c),(5,d)])]
    for si, tgts in tables:
        if abs(nf[si]) < 1e-15: continue
        for ti, co in tgts: r[ti] += nf[si] * co
    return r

def hm_dict(t1, t2):
    """Product of two NF-dicts, as a word-keyed dict, then reduced."""
    out = [0.0] * 6
    for w1, c1 in t1.items():
        base = [0.0] * 6
        base[NF_BASIS.index(w1)] = c1
        cur = base
        for g in w2_iter(t2):
            cur = hm(cur, 1.0, 0.0, g)
        for k in range(6): out[k] += cur[k]
    return out

def w2_iter(t2):
    assert len(t2) == 1
    return list(t2.keys())[0]

def build_gram(trm):
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            cur = [0.0] * 6; cur[i] = 1.0
            for g in NF_BASIS[j]:
                cur = hm(cur, 1.0, 0.0, g)
            G[i, j] = sum(cur[k] * trm[k] for k in range(6))
    return G

def typed(z, trm, G):
    nf_b3 = [1, 0, 0, 0, 0, 0]
    for _ in range(3):
        nf_b3 = hm(nf_b3, 1, 0, 0)
        nf_b3 = hm(nf_b3, 1, -h, 1)
    def mk(g_ud1, g_ud0):
        x = hm(nf_b3[:], 1, 0, 0)      # uu
        x = hm(x, 1, -h/2, g_ud1)      # ud gen 1
        x = hm(x, 1, -h/2, g_ud0)      # ud gen 0
        return x
    p9 = mk(1, 0)
    # Neutron (udd): B3 x ud(s0 mixed) x dd(s1^-1) x ud(s0 mixed) -- the
    # retired script's own construction, lines 164-168.
    n9 = hm(hm(hm(nf_b3[:], 1, -h/2, 0), 1, -h, 1), 1, -h/2, 0)
    tr = lambda nf: sum(nf[i] * trm[i] for i in range(6))
    st = lambda nf: bool(np.all(G @ np.array(nf) >= -1e-10))
    return p9, n9, tr, st

z_old = 1.0 / (q0**0.5 + qi0**0.5)
z_D   = q0**3 / (q0**2 + 1)

CONV = {
  "OLD  (retired: z_old, e-=z^3)":   (z_old, lambda z: [1, z, z, z**2, z**2, z**3]),
  "HALF (bean: z_old, e-=hz^2+z)":   (z_old, lambda z: [1, z, z, z**2, z**2, h*z**2+z]),
  "D    (live: z_D,   e-=hz^2+z)":   (z_D,   lambda z: [1, z, z, z**2, z**2, h*z**2+z]),
}

print(f"q0 = {q0:.15f}   h = {h:.6f}")
print(f"z_old = {z_old:.9f}   z_D = {z_D:.9f}   ratio = {z_D/z_old:.6f}\n")

for label, (z, mk_trm) in CONV.items():
    trm = mk_trm(z)
    G = build_gram(trm)
    ev = np.linalg.eigvalsh(G)
    p9, n9, tr, st = typed(z, trm, G)
    print("=" * 74)
    print(label)
    print(f"  tr_M(e-) = {trm[5]:.9f}")
    print(f"  Gram eigenvalues: {' '.join(f'{v:+.3e}' for v in ev)}")
    print(f"  det G = {np.linalg.det(G):+.4e}   lambda_min = {ev[0]:+.4e}")
    for nm, nf in (("proton", p9), ("neutron", n9)):
        gx = G @ np.array(nf)
        print(f"  {nm:8s} NF = [{' '.join(f'{v:+.4f}' for v in nf)}]")
        print(f"           tr_M = {tr(nf):+.6f}   stable = {st(nf)}   min(Gx) = {gx.min():+.6f} at {NAMES[int(gx.argmin())]}")
    print()

# ══════════════════════════════════════════════════════════════
# Part 2: under D the Gram is SINGULAR. Is the verdict robust to that?
# ══════════════════════════════════════════════════════════════
print("=" * 74)
print("PART 2 — the radical under D, and whether the verdict leans on it")
print("=" * 74)

trm_D = [1, z_D, z_D, z_D**2, z_D**2, h*z_D**2 + z_D]
G_D = build_gram(trm_D)
w, V = np.linalg.eigh(G_D)
null = V[:, 0]
# The 1e-300 is a divide-by-zero floor, not a tolerance: w[0] is the near-null
# eigenvalue and may legitimately underflow to exactly 0.0.
spectral_gap = w[1] / max(w[0], 1e-300)  # float64-ok: guarding a float64 division at the float64 noise floor
print(f"  smallest eigenvalue {w[0]:+.4e}; next {w[1]:+.4e}  -> ratio {spectral_gap:.2e}")
print(f"  measured null vector : [{' '.join(f'{v:+.5f}' for v in null)}]")
# The library's closed form: v_i = (-1/q)^len(w_i) over NF_BASIS.
closed = np.array([(-1.0/q0)**len(b) for b in NF_BASIS])
closed = closed / np.linalg.norm(closed)
if np.dot(closed, null) < 0: closed = -closed
print(f"  closed form (-1/q)^len : [{' '.join(f'{v:+.5f}' for v in closed)}]")
print(f"  agreement |v_meas - v_closed|_max = {np.abs(null - closed).max():.2e}")
print(f"  ||G_D @ v_closed||_max = {np.abs(G_D @ closed).max():.2e}   (0 => genuine radical)")
print()

p9, n9, tr_D, st_D = typed(z_D, trm_D, G_D)
for nm, nf in (("proton", p9), ("neutron", n9)):
    x = np.array(nf)
    # np.dot already returned a binary64 scalar; float() only unwraps the
    # 0-d numpy value, so it introduces no precision loss of its own.
    comp = float(np.dot(x, closed))  # float64-ok: see above
    x_q = x - comp * closed              # project OUT the radical
    gx, gx_q = G_D @ x, G_D @ x_q
    print(f"  {nm}: component along radical = {comp:+.6f}")
    print(f"     min(Gx)          = {gx.min():+.6f}")
    print(f"     min(Gx) on quot. = {gx_q.min():+.6f}   (change {abs(gx.min()-gx_q.min()):.2e})")
    # Same divide-by-zero floor as above; this ratio IS the reported quantity —
    # how far the Frobenius margin sits above the singular-Gram noise floor.
    margin_over_floor = gx.min() / max(abs(w[0]), 1e-300)  # float64-ok: the noise floor is the unit of measurement here
    print(f"     margin / noise floor = {margin_over_floor:.2e}")
print()

# ══════════════════════════════════════════════════════════════
# Part 3: re-run the gluon LP under D
# ══════════════════════════════════════════════════════════════
print("=" * 74)
print("PART 3 — the gluon LP under D (min |tr_M|, stable at every step)")
print("=" * 74)
from itertools import product as cartprod
ops = [("s0", lambda nf: hm(nf, 1, 0, 0)),
       ("s1", lambda nf: hm(nf, 1, 0, 1)),
       ("L+", lambda nf: hm(hm(nf, 1, 0, 0), 1, 0, 1)),
       ("L-", lambda nf: hm(hm(nf, 1, 0, 1), 1, 0, 0))]

def lp(base, tr, st, max_depth=3):
    res = []
    if st(base): res.append((0, [], base[:], tr(base)))
    for depth in range(1, max_depth + 1):
        for combo in cartprod(range(4), repeat=depth):
            nf, names, ncross, ok = base[:], [], 0, True
            for oi in combo:
                nf = ops[oi][1](nf); names.append(ops[oi][0])
                ncross += 2 if ops[oi][0] in ("L+", "L-") else 1
                if not st(nf): ok = False; break
            if ok: res.append((ncross, names, nf[:], tr(nf)))
    seen, uniq = set(), []
    for r in res:
        k = tuple(f"{v:.6f}" for v in r[2])
        if k not in seen: seen.add(k); uniq.append(r)
    uniq.sort(key=lambda r: abs(r[3]))
    return uniq

for nm, nf in (("proton", p9), ("neutron", n9)):
    r = lp(nf, tr_D, st_D)
    print(f"  {nm}: {len(r)} feasible")
    for i, (nc, names, _, t) in enumerate(r[:4]):
        tag = "  <- BARE (0 gluons)" if nc == 0 else ""
        print(f"    {i+1}. {nc} crossings  {'.'.join(names) or '(none)':16s} |tr_M| = {abs(t):.6f}{tag}")
    mincr = min(x[0] for x in r)
    print(f"    min-crossing-first optimum: {mincr} crossings")

# ══════════════════════════════════════════════════════════════
# Part 4: the specific corpus sentences, tested one by one
# ══════════════════════════════════════════════════════════════
print()
print("=" * 74)
print("PART 4 — the corpus's individual claims under D")
print("=" * 74)

def steps_D(label, seq):
    """Walk the typed build, reporting stability at every intermediate step."""
    nf = [1, 0, 0, 0, 0, 0]
    for _ in range(3):
        nf = hm(nf, 1, 0, 0); nf = hm(nf, 1, -h, 1)
    print(f"  {label}: B3  tr_M = {tr_D(nf):+.6f}  stable = {st_D(nf)}")
    for name, c, d, g in seq:
        nf = hm(nf, c, d, g)
        print(f"    after {name:22s} tr_M = {tr_D(nf):+.6f}  stable = {st_D(nf)}"
              f"  min(Gx) = {(G_D @ np.array(nf)).min():+.6f}")
    return nf

steps_D("proton  (uud)", [("uu  (s0)", 1, 0, 0), ("ud  (s1, -h/2)", 1, -h/2, 1), ("ud  (s0, -h/2)", 1, -h/2, 0)])
print()
steps_D("neutron (udd)", [("ud  (s0, -h/2)", 1, -h/2, 0), ("dd  (s1, -h)", 1, -h, 1), ("ud  (s0, -h/2)", 1, -h/2, 0)])
print()

print("  Where the corpus's quoted optima land under D:")
for nm, base, want in (("proton", p9, ["s0", "s0"]), ("neutron", n9, ["L+", "L-"])):
    r = lp(base, tr_D, st_D)
    for rank, (nc, names, _, t) in enumerate(r, 1):
        if names == want:
            print(f"    {nm:8s} {'.'.join(want):8s} -> rank {rank}/{len(r)}, "
                  f"{nc} crossings, |tr_M| = {abs(t):.6f}")
            break
    else:
        print(f"    {nm:8s} {'.'.join(want):8s} -> NOT FEASIBLE under D")
    bare = [x for x in r if x[0] == 0]
    print(f"             bare (0 gluons) -> {'feasible, |tr_M| = %.6f' % abs(bare[0][3]) if bare else 'NOT feasible'}")
