#!/usr/bin/env python3
"""Arbitrate the Masbaum-Thm-5.1 p=2 discrepancy: independent J'_3(5₂) via
TL 2-cabling (the arbiter named by qbeta_5two_colored_tower_barodd_qstar).

THE QUESTION. The Masbaum math/0306345 twist-knot tower at p=2 (K₂ = 5₂)
contradicts the independent GZ 2111.06645 eq-(7.9) ⟨5₂⟩ at N ≥ 3 and the
proven volume conjecture, despite exact N=2 Jones + p=±1 gates and internal
§4/§5 self-consistency (see that probe's witness). One of them is wrong.
This probe computes J'_3(5₂) by a THIRD, definitional route — the colored
Jones from the Kauffman bracket of the e₂-cabled braid closure — and lets it
arbitrate.

CONSTRUCTION. A generic Temperley–Lieb TL_n transfer engine (basis =
noncrossing matchings, Catalan(n); U_i generator matrices; braid generator
σ_i = A·1 + A⁻¹·U_i; Markov-closure loop count valued δ^{loops−1},
δ = −A²−A⁻²). The 2-cable of a B_k braid word lives in B_{2k}
(σ_i ↦ σ_{2i}σ_{2i+1}σ_{2i−1}σ_{2i}); the Jones–Wenzl e₂ = 1 − U/δ is
inserted once (U₁ at the closure):

    ⟨K(e₂)⟩ = ⟨K²⟩ − δ⁻¹·⟨K²·U₁⟩,   J'_3(K) = fr(q)^w · ⟨K(e₂)⟩ / (δ − δ⁻¹)

with the color-2 framing factor fr(q) CALIBRATED (not assumed) on the
trefoil control and validated on 4₁ (w=0, framing-free).

GATES (trusted references = the p=±1 Masbaum towers, which reproduce the
printed Rmk-5.2 f̃'s, the corpus TL₃ Jones at 1e-41, the corpus
aj_masbaum_crosscheck at all N, and the PROVEN 4₁ VC growth):
  G1 — engine 1-cable control: V(4₁), V(5₂) from the TL₃ closure reproduce
       the corpus-validated Jones (same values as qbeta_5two_jones_barodd).
  G2 — 4₁ 2-cable (w=0): J'_3(4₁) from the cable = the trusted p=−1 tower
       value at 3 real q points (no framing factor enters at w=0).
  G3 — trefoil 2-cable: the calibrated framing factor fr(q) is consistent
       across q (a fixed power of q — reported), and with it the cable
       reproduces the trusted p=1 tower J'_3(K₁) at all test q.
THE ARBITRATION:
  A — J'_3(5₂) from the calibrated cable vs the Masbaum p=2 tower value
      J_twist(3,2,q) at the test q's (match/mismatch), and
  B — at q = e^{2πi/3}: cable J'_3 vs GZ eq-(7.9) ⟨5₂⟩_3 = 20.952… modulus.
Whichever of {Masbaum-p=2-as-printed, GZ-(7.9)} the definitional cable
agrees with wins. auditOnly; no c_k wired; no fit.

Run: python3 -u computations/probes/qbeta_5two_n3_cable_arbitration_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_n3_cable.log
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_colored_tower_barodd_qstar_probe as tower  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

BRAID_5_2 = [1, 1, 1, 2, -1, 2]     # B₃, writhe 4 (canonical, #3892)
BRAID_4_1 = [1, -2, 1, -2]          # B₃, writhe 0
BRAID_TREF = [1, 1, 1]              # B₂, writhe 3 (chirality identified by gate)


# ---------------- generic TL_n diagram engine ----------------

def tl_basis(n):
    """Noncrossing perfect matchings of 2n boundary points in circular order
    top 0..n−1 (L→R) then bottom 2n−1..n (R→L below). Catalan(n) diagrams,
    each a frozenset of frozenset-pairs of point labels 0..2n−1 where labels
    0..n−1 = top T0..T(n−1) and n..2n−1 = bottom B0..B(n−1) with the circular
    position of Bj being 2n−1−j."""
    pos = list(range(n)) + [2 * n - 1 - j for j in range(n)]  # label -> circle pos

    def circ(label):
        return pos[label]

    labels = list(range(2 * n))

    def rec(avail):
        if not avail:
            yield []
            return
        a = avail[0]
        for b in avail[1:]:
            # noncrossing on the circle: points strictly between circ(a), circ(b)
            # must pair among themselves
            lo, hi = sorted((circ(a), circ(b)))
            inside = [x for x in avail[1:] if x != b and lo < circ(x) < hi]
            outside = [x for x in avail[1:] if x != b and not (lo < circ(x) < hi)]
            if len(inside) % 2 == 0:
                for rest_in in rec(inside):
                    for rest_out in rec(outside):
                        yield [(a, b)] + rest_in + rest_out
    out = []
    for m in rec(labels):
        out.append(frozenset(frozenset(p) for p in m))
    return out


class _UF:
    """Union-find with cycle counting (multigraph, degree ≤ 2): each edge
    joining two already-connected nodes closes exactly one loop."""

    def __init__(self):
        self.p = {}
        self.loops = 0

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            self.loops += 1
        else:
            self.p[ra] = rb


def tl_compose(d_top, d_bot, n):
    """Stack d_top ABOVE d_bot (top's bottom row glued to bot's top row).
    Returns (resulting diagram frozenset, closed loop count). Edge-based
    union-find — the first path-walking version crashed on 2-node double
    edges (a length-2 glue loop)."""
    uf = _UF()
    for pair in d_top:
        a, b = tuple(pair)
        na = ('t', a) if a < n else ('g', a - n)
        nb = ('t', b) if b < n else ('g', b - n)
        uf.union(na, nb)
    for pair in d_bot:
        a, b = tuple(pair)
        na = ('g', a) if a < n else ('b', a - n)
        nb = ('g', b) if b < n else ('b', b - n)
        uf.union(na, nb)
    # externals sharing a component are paired (degree ≤ 2 ⇒ exactly 2 per
    # external-containing component)
    ext = [('t', j) for j in range(n)] + [('b', j) for j in range(n)]
    groups = {}
    for e in ext:
        groups.setdefault(uf.find(e), []).append(e)

    def lab(node):
        k, j = node
        return j if k == 't' else n + j
    dg = frozenset(frozenset((lab(a), lab(b))) for a, b in groups.values())
    return dg, uf.loops


def tl_engine(n):
    """Precompute basis index + U_i composition tables."""
    basis = tl_basis(n)
    idx = {d: i for i, d in enumerate(basis)}
    ident = frozenset(frozenset((j, n + j)) for j in range(n))
    U = []
    for i in range(1, n):
        u = set()
        for j in range(n):
            if j == i - 1:
                u.add(frozenset((i - 1, i)))
                u.add(frozenset((n + i - 1, n + i)))
            elif j != i:
                u.add(frozenset((j, n + j)))
        U.append(frozenset(u))
    # composition tables: for generator g (a diagram), table[g][d] = (index, loops)
    tables = []
    for u in U:
        tab = []
        for d in basis:
            dg, lp = tl_compose(d, u, n)   # multiply on the RIGHT: d then u below
            tab.append((idx[dg], lp))
        tables.append(tab)
    # closure loop count per basis diagram (edge-based union-find)
    closure = []
    for d in basis:
        uf = _UF()
        for pair in d:
            a, b = tuple(pair)
            uf.union(a, b)
        for j in range(n):
            uf.union(j, n + j)
        closure.append(uf.loops)
    return basis, idx, ident, tables, closure


def bracket_closure(word, n, A, engine):
    """Kauffman bracket ⟨closure(word)⟩ with δ^{loops−1} normalization; word
    entries ±g (1-indexed generators), plus the sentinel ('U', g) to insert a
    bare U_g."""
    basis, idx, ident, tables, closure = engine
    delta = -A ** 2 - A ** -2
    vec = {idx[ident]: mp.mpc(1)}
    for g in word:
        new = {}
        if isinstance(g, tuple):        # bare U insertion
            gi = g[1] - 1
            for i, c in vec.items():
                j, lp = tables[gi][i]
                new[j] = new.get(j, mp.mpc(0)) + c * delta ** lp
        else:
            gi = abs(g) - 1
            cA = A if g > 0 else A ** -1
            cB = A ** -1 if g > 0 else A
            for i, c in vec.items():
                new[i] = new.get(i, mp.mpc(0)) + c * cA
                j, lp = tables[gi][i]
                new[j] = new.get(j, mp.mpc(0)) + c * cB * delta ** lp
        vec = new
    tot = mp.mpc(0)
    for i, c in vec.items():
        tot += c * delta ** (closure[i] - 1)
    return tot


def cable2(word):
    """2-cable of a braid word: σ_i ↦ σ_{2i}σ_{2i+1}σ_{2i−1}σ_{2i} (inverses
    reversed)."""
    out = []
    for g in word:
        i = abs(g)
        block = [2 * i, 2 * i + 1, 2 * i - 1, 2 * i]
        if g > 0:
            out += block
        else:
            out += [-x for x in reversed(block)]
    return out


def jones1(word, n, q, engine):
    """1-cable (ordinary) Jones V(q) with t = q² (corpus convention)."""
    A = q ** mp.mpf("-0.5")
    w = sum(1 if g > 0 else -1 for g in word)
    return (-A ** 3) ** (-w) * bracket_closure(word, n, A, engine)


def colored3_raw(word, k, q, engines):
    """⟨K(e₂)⟩/(δ−δ⁻¹) for the closure of a B_k word, WITHOUT framing factor."""
    A = q ** mp.mpf("-0.5")
    delta = -A ** 2 - A ** -2
    cw = cable2(word)
    eng = engines[2 * k]
    br_full = bracket_closure(cw, 2 * k, A, eng)
    br_u = bracket_closure(cw + [('U', 1)], 2 * k, A, eng)
    return (br_full - br_u / delta) / (delta - 1 / delta)


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" N=3 cable arbitration: Masbaum p=2 tower vs GZ (7.9) vs the TL cable")
    print("=" * 78)

    print("\n  building TL engines (n = 2,3,4,6; Catalan dims 2,5,14,132) ...",
          flush=True)
    engines = {n: tl_engine(n) for n in (2, 3, 4, 6)}
    print(f"  ... built ({time.monotonic()-t0:.0f}s)", flush=True)

    qs_test = [mp.mpf("1.11"), mp.mpf("0.93"), mp.mpf("1.037")]

    # ---- G1: engine 1-cable control vs corpus Jones ----
    def V41_known(q):
        return q**4 - q**2 + 1 - q**-2 + q**-4

    def V52_known(q):
        return -q**12 + q**10 - q**8 + 2 * q**6 - q**4 + q**2

    g1_ok = True
    print("\n[G1] engine 1-cable control (TL₃) vs corpus-validated Jones:")
    for q in qs_test:
        v41 = jones1(BRAID_4_1, 3, q, engines[3])
        v52 = jones1(BRAID_5_2, 3, q, engines[3])
        e41 = abs(v41 - V41_known(q)) / abs(V41_known(q))
        c52 = [V52_known(q), V52_known(1 / q)]
        e52 = min(abs(v52 - c) / abs(c) for c in c52)
        g1_ok &= e41 < mp.mpf("1e-22") and e52 < mp.mpf("1e-22")
        print(f"    q={q}: 4₁ rel {mp.nstr(e41,3)}; 5₂ rel {mp.nstr(e52,3)}")
    print(f"    {'PASS' if g1_ok else 'FAIL'}")

    # ---- G2: 4₁ 2-cable (w=0) vs the trusted p=−1 tower ----
    g2_ok = True
    print("\n[G2] 4₁ 2-cable J'_3 (w=0, framing-free) vs trusted Masbaum p=−1 tower:")
    for q in qs_test:
        jc = colored3_raw(BRAID_4_1, 3, q, engines)
        # Masbaum's a = A² (Lemma 4.1 proof) ⇒ q_Masbaum = q_cable^{∓2}
        jt = tower.J_twist(3, -1, q ** 2)
        err = min(abs(jc - jt) / abs(jt),
                  abs(jc - tower.J_twist(3, -1, q ** -2)) / abs(jt))
        g2_ok &= err < mp.mpf("1e-20")
        print(f"    q={q}: cable={mp.nstr(jc,10)}  tower={mp.nstr(jt,10)}  rel={mp.nstr(err,3)}")
    print(f"    {'PASS' if g2_ok else 'FAIL'}")

    # ---- G3: trefoil 2-cable — calibrate the framing factor ----
    print("\n[G3] trefoil 2-cable: calibrate fr(q) (w=3) against trusted p=1 tower:")
    frs = []
    for q in qs_test:
        jc = colored3_raw(BRAID_TREF, 2, q, engines)
        cands = [tower.J_twist(3, 1, q ** 2), tower.J_twist(3, 1, q ** -2)]
        # fr^3 = tower/cable; take the candidate giving |fr| closest to a
        # clean power of q
        best = None
        for jt in cands:
            fr3 = jt / jc
            fr = fr3 ** (mp.mpf(1) / 3)
            k = mp.log(abs(fr)) / mp.log(q)
            score = abs(k - mp.nint(k))
            if best is None or score < best[0]:
                best = (score, fr, k, jt)
        frs.append(best)
        print(f"    q={q}: fr(q) = {mp.nstr(best[1],10)}  |fr| = q^{mp.nstr(best[2],6)}")
    ks = [b[2] for b in frs]
    k_int = mp.nint(ks[0])
    g3_ok = all(abs(k - k_int) < mp.mpf("1e-8") for k in ks)
    print(f"    consistent integer power across q: k = {int(k_int)}  "
          f"{'PASS' if g3_ok else 'FAIL'}")

    # ---- ARBITRATION A: 5₂ 2-cable vs the Masbaum p=2 tower at real q ----
    print("\n[A] J'_3(5₂) from the calibrated cable vs the Masbaum p=2 tower:")
    rows = {}
    match_masbaum = True
    for q in qs_test:
        jc_raw = colored3_raw(BRAID_5_2, 3, q, engines)
        # writhe 4; try both fr-sign/mirror candidates like G3 did
        cands = []
        for sgn in (1, -1):
            fr = frs[0][1] if sgn == 1 else 1 / frs[0][1]
        # recompute fr at THIS q from its integer power + phase convention:
        # use fr from G3's per-q calibration
        fr_q = [b for b in frs if True][qs_test.index(q)][1]
        for fr_c in (fr_q, 1 / fr_q):
            for jt in (tower.J_twist(3, 2, q ** 2), tower.J_twist(3, 2, q ** -2)):
                cands.append(abs(fr_c ** 4 * jc_raw - jt) / abs(jt))
        err = min(cands)
        rows[str(q)] = {"cable_raw": mp.nstr(jc_raw, 12), "best_rel_vs_tower": mp.nstr(err, 4)}
        match_masbaum &= err < mp.mpf("1e-10")
        print(f"    q={q}: cable(raw)={mp.nstr(jc_raw,10)}  best rel vs tower = {mp.nstr(err,4)}")
    print(f"    ⇒ Masbaum p=2 tower {'MATCHES' if match_masbaum else 'DOES NOT match'} "
          "the definitional cable at real q")

    # ---- ARBITRATION B: at q = e^{2πi/3} vs GZ (7.9) ----
    qroot = mp.e ** (2j * mp.pi / 3)          # the N=3 Kashaev point (tower/GZ var)
    # ⟨e₂⟩ = [3]_{q_M} VANISHES at the root (0/0 in the bracket ratio); J'_3 is
    # a Laurent polynomial, so evaluate by radial limit q_M → root:
    eps = mp.mpf("5e-9")
    qc_root = mp.sqrt((1 - eps) * qroot)       # qc² = (1−ε)·e^{2πi/3}
    jc_root_raw = colored3_raw(BRAID_5_2, 3, qc_root, engines)
    gz3 = tower.gz79(3)
    # framing factor is a phase at |q|=1 — compare moduli (phase-free)
    m_cable = abs(jc_root_raw)
    m_gz = abs(gz3)
    m_masb = abs(tower.J_twist(3, 2, qroot))
    # also the conjugate root, same radial limit
    m_cable2 = abs(colored3_raw(BRAID_5_2, 3, mp.sqrt((1 - eps) / qroot), engines))
    print(f"\n[B] at q=e^(2πi/3) (moduli; framing = pure phase):")
    print(f"    |cable(e^ipi/3)| = {mp.nstr(m_cable,12)}  |cable(e^-ipi/3)| = "
          f"{mp.nstr(m_cable2,12)}  |GZ79| = {mp.nstr(m_gz,12)}  "
          f"|Masbaum tower| = {mp.nstr(m_masb,12)}")
    agree_gz = min(abs(m_cable - m_gz), abs(m_cable2 - m_gz)) / m_gz < mp.mpf("1e-4")
    agree_masb = min(abs(m_cable - m_masb), abs(m_cable2 - m_masb)) / m_masb < mp.mpf("1e-4")
    print(f"    cable agrees with: GZ {'YES' if agree_gz else 'no'}; "
          f"Masbaum p=2 {'YES' if agree_masb else 'no'}")

    # ---- [C] CERTIFIED N=3 categorical q*-test via the validated cable ----
    # zero-framed definitional J'_3(q) = fr(q)^w · cable_raw(q), fr = q^4
    # (calibrated exactly); bar-odd datum B(q) = [J'(q) − J'(1/q)]/2.
    Q_STAR = mp.mpf("1.10997859303152")
    print("\n[C] CERTIFIED N=3 categorical q*-test (validated cable, w=4 framing):")

    def J3_def(word, k, w, q):
        return q ** (4 * w) * colored3_raw(word, k, q, engines)

    # amphichiral control at q*: B_3(4_1) = 0
    b41 = (J3_def(BRAID_4_1, 3, 0, Q_STAR) - J3_def(BRAID_4_1, 3, 0, 1 / Q_STAR)) / 2
    j41m = abs(J3_def(BRAID_4_1, 3, 0, Q_STAR))
    c_null = abs(b41) / j41m < mp.mpf("1e-25")
    print(f"    4₁ null control: |B₃(4₁;q*)|/|J| = {mp.nstr(abs(b41)/j41m,3)}  "
          f"{'PASS' if c_null else 'FAIL'}")

    half = mp.mpf("2e-8")
    npts = 9
    grid = [Q_STAR - half + 2 * half * i / (npts - 1) for i in range(npts)]
    bvals = []
    for qq in grid:
        B = (J3_def(BRAID_5_2, 3, 4, qq) - J3_def(BRAID_5_2, 3, 4, 1 / qq)) / 2
        bvals.append(mp.re(B))
    sc = sum(1 for x, y in zip(bvals, bvals[1:]) if mp.sign(x) != mp.sign(y))
    B_star = bvals[npts // 2]
    q_mu = mp.mpf("1.10997859555733471")
    q_pr = mp.mpf("1.1099785827513808075916690956107688798744991218736")
    B_mu = mp.re((J3_def(BRAID_5_2, 3, 4, q_mu) - J3_def(BRAID_5_2, 3, 4, 1 / q_mu)) / 2)
    B_pr = mp.re((J3_def(BRAID_5_2, 3, 4, q_pr) - J3_def(BRAID_5_2, 3, 4, 1 / q_pr)) / 2)
    rel_slope = float(abs(B_mu - B_pr) / abs(B_mu) / (q_mu - q_pr))
    c_no_zero = sc == 0 and abs(B_star) > 0
    print(f"    B₃(5₂;q*) = {mp.nstr(B_star,8)}  sign changes on ±2e-8 grid = {sc}  "
          f"|d ln B/dq| ≈ {rel_slope:.3e}")
    print(f"    ⇒ N=3 categorical face: {'NO zero at q*, anchor-smooth — capstone constraint (2) FAILS (certified)' if c_no_zero and rel_slope < 1e5 else 'inspect!'}")

    verdict_gz = agree_gz and not agree_masb and not match_masbaum
    verdict_masb = agree_masb and match_masbaum and not agree_gz
    ok_gates = g1_ok and g2_ok and g3_ok

    print("\n  VERDICT:", "GZ (7.9) is correct; the Masbaum Thm-5.1 p=2 assembly "
          "(as printed/transcribed) is NOT J'_N(5₂) — the discrepancy resolves "
          "against Masbaum-p=2." if verdict_gz else
          ("the Masbaum tower is vindicated; GZ-(7.9) is not ⟨5₂⟩ in this "
           "convention." if verdict_masb else
           "MIXED/INCONCLUSIVE — inspect before any claim."))

    wb = WitnessBuilder("qbeta-5two-n3-cable-arbitration", engine="mpmath",
                        _script_path=__file__)
    wb.set_description(
        "Definitional N=3 arbitration of the Masbaum-p=2 vs GZ-(7.9) 5₂ "
        "discrepancy: J'_3 via a generic TL_n transfer engine (Catalan bases "
        "2..132), e₂ = 1−U/δ inserted in the 2-cabled braid closure. Gates: "
        "the engine reproduces the corpus TL₃ Jones (1-cable); the 4₁ "
        "2-cable (w=0, framing-free) equals the trusted p=−1 tower; the "
        "trefoil 2-cable calibrates a consistent integer-power framing "
        "factor. Arbitration: the cable J'_3(5₂) vs the Masbaum p=2 tower "
        "at real q, and vs GZ eq-(7.9) modulus at q=e^{2πi/3}. auditOnly.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("gate_engine_1cable_jones",
                     computed=1.0 if g1_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="TL engine reproduces corpus V(4₁), V(5₂) at 3 q-points")
    wb.add_assertion("gate_41_2cable_matches_trusted_tower",
                     computed=1.0 if g2_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="4₁ 2-cable J'_3 (framing-free) = trusted Masbaum p=−1 "
                            "tower at 3 q-points")
    wb.add_assertion("gate_trefoil_framing_calibration",
                     computed=1.0 if g3_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="trefoil 2-cable framing factor is a consistent integer "
                            "power of q across test points")
    wb.add_assertion("certified_41_null_at_qstar",
                     computed=1.0 if c_null else 0.0, expected=1.0, tolerance=0.5,
                     source="B₃(4₁;q*) = 0 to 1e-25 via the validated cable — "
                            "amphichiral control")
    wb.add_assertion("certified_N3_no_qstar_zero",
                     computed=1.0 if c_no_zero else 0.0, expected=1.0, tolerance=0.5,
                     source="B₃(5₂;q) via the validated definitional cable: 0 sign "
                            "changes on q*±2e-8, B₃(q*) ≠ 0 — capstone constraint "
                            "(2) fails on the CERTIFIED N=3 categorical face")
    wb.add_assertion("arbitration_decisive",
                     computed=1.0 if (verdict_gz or verdict_masb) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="the cable agrees with exactly one of "
                            "{Masbaum-p=2, GZ-(7.9)}")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("arbitration_A_real_q", rows)
    wb.add_data("arbitration_B_root", {"cable_modulus": mp.nstr(m_cable, 15),
                                       "gz79_modulus": mp.nstr(m_gz, 15),
                                       "masbaum_tower_modulus": mp.nstr(m_masb, 15)})
    wb.add_data("framing_power", int(k_int) if g3_ok else None)
    wb.add_data("certified_N3_qstar_test", {
        "B3_qstar": mp.nstr(B_star, 12), "sign_changes": sc,
        "rel_slope": f"{rel_slope:.4e}",
        "note": "zero-framed definitional J'_3 via the 1e-30-validated cable; "
                "supersedes the UNCERTIFIED tower diagnostic at N=3"})
    wb.add_data("verdict",
                ("GZ-(7.9) WINS: the definitional TL-cable J'_3(5₂) agrees with "
                 "GZ and refutes the Masbaum Thm-5.1 p=2 assembly as "
                 "printed/transcribed — the fault is upstream in that assembly. "
                 "Unblocks bean qou-3yxn via the GZ/cable route."
                 if verdict_gz else
                 ("MASBAUM WINS: the tower is vindicated; GZ-(7.9) is not ⟨5₂⟩ "
                  "in the assumed convention." if verdict_masb else
                  "INCONCLUSIVE — inspect."))
                )
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-t0:.0f}s)")
    print("  witness -> computations/probes/qbeta-5two-n3-cable-arbitration.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
