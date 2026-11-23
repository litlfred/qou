#!/usr/bin/env python3
"""six_strand_pair_probe — the γγ lepton pair e⁻ ⊔ ν̄ ⊔ loop on six strands.

Closed family and reporting rules: PREREGISTRATION.md (committed first).
Exact arithmetic only (fractions.Fraction, sympy rationals). Nothing is selected or scored.
Photon: γᵢ(a,b,c) = 1 + aσᵢ + bσᵢ₊₁ + cσᵢσᵢ₊₁⁻¹ (larger letter inverted at every i).
"""
from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "computations/probes/qbeta_gg_lepton_pair"):
    sys.path.insert(0, str(_ROOT / _p))

from qbeta_gg_lepton_pair_probe import (apply_crossing, gg_word, inv,  # noqa: E402
                                         strand_data)

N = 6
QS = (Fr(2), Fr(3))
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def sector_trace(word, n, q, ones):
    """Tr of rho(w) restricted to the K-weight sector with `ones` down-spins (no K)."""
    tot = Fr(0)
    for b in range(2 ** n):
        if bin(b).count("1") != ones:
            continue
        v = {b: Fr(1)}
        for (i, s) in reversed(word):
            v = apply_crossing(v, n, i, s, q)
        tot += v.get(b, 0)
    return tot


def part1():
    ref = {q: inv([(0, 1), (1, 1), (0, 1)], 5, q) for q in QS}
    refm = {q: inv([(0, -1), (1, -1), (0, -1)], 5, q) for q in QS}
    rows, parity_bad, neutral_hits = [], 0, 0
    for m in range(1, 7):
        for vs in itertools.product(range(4), repeat=m):
            w = gg_word(vs)
            k, lk2, selfc = strand_data(w, N)
            if (N + k) % 2:
                parity_bad += 1
            if k != 4:
                continue
            lks = sorted(abs(lk2[a][b]) // 2 for a in range(4) for b in range(a + 1, 4))
            if lks != [0, 0, 0, 0, 0, 1]:
                continue
            vals = {q: inv(w, N, q) for q in QS}
            match = ("e- + nu-bar + loop" if vals == ref else
                     "mirror" if vals == refm else "other link")
            neutral = all(lk2[a][b] == 0 for a in range(4) for b in range(4) if a != b)
            neutral_hits += neutral
            rows.append({"word": "".join(f"V{i}" for i in vs), "verts": list(vs),
                         "vertices": m, "self_crossings": selfc, "match": match})
    return rows, parity_bad, neutral_hits, ref



# ---------------------------------------------------------------- Part 2 helpers
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

XS = sp.symbols("x0:9")
MU, TT = sp.symbols("mu t")


def _act(vec, word, q, n):
    for (i, s) in reversed(word):
        vec = apply_crossing(vec, n, i, s, q)
    return vec


def _add(o, v, c):
    for k, x in v.items():
        o[k] = o.get(k, 0) + c * x


def _photon(vec, i, w, q, n):
    a, b, c = w
    o = dict(vec)
    _add(o, _act(vec, [(i, 1)], q, n), a)
    _add(o, _act(vec, [(i + 1, 1)], q, n), b)
    _add(o, _act(vec, [(i, 1), (i + 1, -1)], q, n), c)
    return o


def tl_test(word, pos, q, n):
    """Groebner basis of  gamma_pos[0] ... gamma_pos[-1] = mu * rho(word)  in the Jimbo rep."""
    ws = [XS[3 * k:3 * k + 3] for k in range(len(pos))]
    eqs = set()
    for bb in range(2 ** n):
        v = {bb: sp.Integer(1)}
        for k in reversed(range(len(pos))):
            v = _photon(v, pos[k], ws[k], q, n)
        rhs = _act({bb: sp.Integer(1)}, word, q, n)
        for kk in set(v) | set(rhs):
            e = sp.expand(v.get(kk, 0) - MU * rhs.get(kk, 0))
            if e != 0:
                eqs.add(e)
    vs = [x for w in ws for x in w] + [MU, TT]
    return sp.groebner(list(eqs) + [MU * TT - 1], *vs, order="grevlex")


# full Hecke algebra, standard basis T_pi, sigma^2 = h sigma + 1
QS_ = sp.Symbol("q")


def _len(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])


def _rmul(el, i, h):
    out = {}
    for w, c in el.items():
        ws = list(w); ws[i], ws[i + 1] = ws[i + 1], ws[i]; ws = tuple(ws)
        out[ws] = out.get(ws, 0) + c
        if _len(ws) < _len(w):
            out[w] = out.get(w, 0) + h * c
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def h_word(word, n, q):
    h = q - 1 / q
    el = {tuple(range(n)): sp.Integer(1)}
    for (i, s) in word:
        new = _rmul(el, i, h)
        if s < 0:
            for k, v in el.items():
                new[k] = sp.expand(new.get(k, 0) - h * v)
            new = {k: v for k, v in new.items() if v != 0}
        el = new
    return el


def _red_word(p):
    p = list(p); word = []
    while True:
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]; word.append(i); break
        else:
            break
    return word[::-1]


def h_mul(e1, e2, q):
    h = q - 1 / q
    out = {}
    for w, c in e2.items():
        el = dict(e1)
        for i in _red_word(w):
            el = _rmul(el, i, h)
        for k, v in el.items():
            out[k] = sp.expand(out.get(k, 0) + c * v)
    return out


def h_photon(i, w, n, q):
    a, b, c = w
    out = {tuple(range(n)): sp.Integer(1)}
    for coef, wd in ((a, [(i, 1)]), (b, [(i + 1, 1)]), (c, [(i, 1), (i + 1, -1)])):
        for k, v in h_word(wd, n, q).items():
            out[k] = sp.expand(out.get(k, 0) + coef * v)
    return out


def h_test(word, pos, n, q):
    target = h_word(word, n, q)
    P = h_photon(pos[0], XS[0:3], n, q)
    for k in range(1, len(pos)):
        P = h_mul(P, h_photon(pos[k], XS[3 * k:3 * k + 3], n, q), q)
    eqs = [sp.expand(P.get(k, 0) - MU * target.get(k, 0)) for k in set(P) | set(target)]
    eqs = [e for e in eqs if e != 0]
    vs = list(XS[:3 * len(pos)]) + [MU, TT]
    return sp.groebner(eqs + [MU * TT - 1], *vs, order="grevlex")


def reduced_real_search(qv, trials=400, want=3, seed=1):
    """Real solutions of gamma(a,b,c) gamma(A,B,C) = lam * V0^2 s1 (z s1 - 1/h)^-1 in H3(q)."""
    import random
    q = sp.Rational(qv)
    h = q - 1 / q
    a, b, c, A, B, C, lam, z = sp.symbols("a b c A B C lam z")
    S0 = sp.Matrix([[q, 0], [1, -1 / q]]); S1 = sp.Matrix([[-1 / q, 1], [0, q]])
    blocks = [(sp.Matrix([[q]]), sp.Matrix([[q]])),
              (sp.Matrix([[-1 / q]]), sp.Matrix([[-1 / q]])), (S0, S1)]
    eqs = []
    for s0, s1 in blocks:
        Id = sp.eye(s0.shape[0])
        g = lambda x, y, w: Id + x * s0 + y * s1 + w * s0 * s1.inv()  # noqa: E731
        V = s0 * s1.inv()
        E = V * V * s1 * (z * s1 - Id / h).inv()
        eqs += [sp.numer(sp.together(e)) for e in (g(a, b, c) * g(A, B, C) - lam * E)]
    v6 = [a, b, c, B, C, lam]
    random.seed(seed)
    mp.mp.dps = 40
    found = []
    for _ in range(trials):
        zv = sp.Rational(random.randint(-30, 30), 10)
        Av = sp.Rational(random.randint(-30, 30), 10)
        es = [e.subs({z: zv, A: Av}) for e in eqs]
        f = sp.lambdify(v6, es, "mpmath")
        x0 = [mp.mpf(random.uniform(-3, 3)) for _ in range(6)]
        try:
            r = mp.findroot(lambda *x: f(*x), x0, tol=mp.mpf(10) ** -32, maxsteps=80)
        except Exception:  # noqa: BLE001  (non-convergence is a miss, not a result)
            continue
        r = [r[i] for i in range(6)]
        if any(abs(mp.im(v)) > mp.mpf(10) ** -25 for v in r) or abs(r[5]) < mp.mpf(10) ** -6:
            continue
        r = [mp.re(v) for v in r]
        res = max(abs(e) for e in f(*r))
        if res < mp.mpf(10) ** -30:
            found.append({"z": str(zv), "A": str(Av), "residual": mp.nstr(res, 3),
                          **{str(k): mp.nstr(v, 15) for k, v in zip(v6, r)}})
            if len(found) >= want:
                break
    return found


def main() -> int:
    from witness_base import WitnessBuilder
    rows, pb, nh, ref = part1()
    hits = [r for r in rows if r["match"] != "other link"]
    for r in hits:
        used = set()
        for i in r["verts"]:
            used |= {i, i + 1, i + 2}
        r["idle_strands"] = N - len(used)
    first = {}
    for r in hits:
        first.setdefault(r["match"], r["vertices"])
    m3 = [r for r in hits if r["vertices"] == 3]
    no_idle = [r for r in hits if r["idle_strands"] == 0]
    m_no_idle = min(r["vertices"] for r in no_idle)
    m5 = [r for r in no_idle if r["vertices"] == m_no_idle]
    check("P1_parity", pb == 0, "n + #components even for every word (Lean gammaGamma_components_parity).")
    check("P1_smallest_match", first == {"e- + nu-bar + loop": 3, "mirror": 3},
          f"{len(hits)} words (<= 6 vertices, i = 0..3) match e- + nu-bar + loop or its mirror at "
          f"q = 2, 3; smallest vertex count 3, with {len(m3)} words "
          f"({sum(r['match'] != 'mirror' for r in m3)} + {sum(r['match'] == 'mirror' for r in m3)} mirror).")
    check("P1_minimal_words_leave_two_idle_strands", all(r["idle_strands"] == 2 for r in m3),
          "every 3-vertex match moves only 4 strands; two components are untouched strands.")
    check("P1_smallest_with_no_idle_strand", m_no_idle == 5,
          f"with every strand inside some vertex footprint, the smallest vertex count is {m_no_idle}: {len(m5)} words "
          f"({sum(r['match'] != 'mirror' for r in m5)} + {sum(r['match'] == 'mirror' for r in m5)} mirror).")
    check("P1_no_match_is_linking_neutral", nh == 0,
          "no candidate is whole-word linking-neutral: the Hopf pair has lk = 1 by definition.")
    sect = {}
    for r in m3:
        if r["match"] != "mirror":
            sect[r["word"]] = {str(q): str(sector_trace(gg_word(r["verts"]), N, q, 3)) for q in QS}
    vals = {json.dumps(v, sort_keys=True) for v in sect.values()}
    check("P1_zero_charge_sector_trace_reported", True,
          f"trace on the zero-charge K-sector (3 up, 3 down) for the 9 minimal e- words takes "
          f"{len(vals)} distinct value pair(s) at q = 2, 3: {sorted(vals)}.")

    # Part 2a: two photons, TL quotient, every ordered pair of positions
    two = {}
    for qv in (sp.Integer(2), sp.Integer(3)):
        for r in m3:
            for i in range(4):
                for j in range(4):
                    G = tl_test(gg_word(r["verts"]), (i, j), qv, N)
                    if list(G) != [1]:
                        two.setdefault("m3", []).append((r["word"], i, j, str(qv)))
    for r in m5:
        for i in range(4):
            for j in range(4):
                G = tl_test(gg_word(r["verts"]), (i, j), sp.Integer(2), N)
                if list(G) != [1]:
                    two.setdefault("m5", []).append((r["word"], i, j))
    found_words = sorted({x[0] for v in two.values() for x in v})
    check("P2_two_photon_factorisations_reported", True,
          f"two-photon TL factorisations exist for {len(found_words)} words: "
          f"3-vertex {sorted({(x[0], x[1], x[2]) for x in two.get('m3', [])})}, "
          f"5-vertex {sorted({(x[0], x[1], x[2]) for x in two.get('m5', [])})}. "
          "Every other (word, i, j) gives Groebner basis 1 (no solution over C).")

    # Part 2a': exact identities behind them, full Hecke algebra, generic q
    qs = sp.Symbol("q")
    hq = qs - 1 / qs

    def same(e1, e2):
        return all(sp.simplify(e1.get(k, 0) - e2.get(k, 0)) == 0 for k in set(e1) | set(e2))

    lhs = h_word(gg_word([0, 1, 2, 0, 3]), 6, qs)
    red = h_word([(0, 1), (0, 1), (1, -1), (4, -1)], 6, qs)
    g0 = h_photon(0, (0, -1 / hq, -1), 6, qs)
    g3 = h_photon(3, (0, -1 / hq, 0), 6, qs)
    prod = {k: sp.expand(hq ** 2 * v) for k, v in h_mul(g0, g3, qs).items()}
    hopf = {k: sp.expand(-v / hq) for k, v in h_word([(0, 1), (0, 1), (1, -1)], 3, qs).items()}
    check("P2_exact_pair_word_identity_fullH",
          same(lhs, red) and same(lhs, prod) and same(h_photon(0, (0, -1 / hq, -1), 3, qs), hopf),
          "generic q, full Hecke algebra: V0V1V2V0V3 = s0^2 s1^-1 s4^-1 = "
          "h^2 gamma_0(0,-1/h,-1) gamma_3(0,-1/h,0), and gamma(0,-1/h,-1) = -h^-1 s0^2 s1^-1 "
          "(whose closure on 3 strands is the Hopf link). After the braid reduction strand 3 "
          "is untouched, so 'no idle strand' in P1 is a property of the vertex footprint, "
          "not of the braid. Lean: QOU/MassTheory/PhotonCrossingMonomials.lean.")

    # Part 2b: three photons for V0V0V1 on four strands, q = 2
    w = gg_word([0, 0, 1])
    tl3, h3 = {}, {}
    for pos in itertools.product((0, 1), repeat=3):
        tl3[str(pos)] = list(tl_test(w, pos, sp.Integer(2), 4)) != [1]
    for pos in ((0, 0, 1), (1, 0, 1)):
        h3[str(pos)] = list(h_test(w, pos, 4, sp.Integer(2))) != [1]
    check("P2_three_photons_TL", [k for k, v in tl3.items() if v] == ["(0, 0, 1)", "(1, 0, 1)"],
          f"V0V0V1 = mu^-1 gamma_i gamma_j gamma_k over C, q = 2, TL quotient: solvable exactly at "
          f"{[k for k, v in tl3.items() if v]} of the 8 placements in {{0,1}}^3.")
    check("P2_three_photons_full_H", h3 == {"(0, 0, 1)": True, "(1, 0, 1)": False},
          f"in the full Hecke algebra H4(q) at q = 2: {h3}. Only (0,0,1) survives.")

    # Part 2c: real weights via the coset reduction
    real = {str(qv): reduced_real_search(qv) for qv in ("2", "11/10")}
    check("P2_real_three_photon_family", all(len(v) >= 3 for v in real.values()),
          "gamma_0 gamma_0 gamma_1(0, -1/h, z) = mu^-1 V0V0V1 has real solutions at q = 2 and "
          "q = 11/10 for several (z, A); residual < 1e-30 at 40 digits. The weights are not "
          "fixed: a two-parameter real family.")

    # Part 2d (addendum 2): two photons at generic q, Groebner basis over Q(q)
    qg = sp.Symbol("q")

    def eqs_generic(word, pos, n):
        ws = [XS[3 * k:3 * k + 3] for k in range(len(pos))]
        eqs = set()
        for bb in range(2 ** n):
            v = {bb: sp.Integer(1)}
            for k in reversed(range(len(pos))):
                v = _photon(v, pos[k], ws[k], qg, n)
            rhs = _act({bb: sp.Integer(1)}, word, qg, n)
            for kk in set(v) | set(rhs):
                e = sp.expand(sp.numer(sp.together(sp.expand(v.get(kk, 0) - MU * rhs.get(kk, 0)))))
                if e != 0:
                    eqs.add(e)
        return list(eqs)

    gen_pos, gen_sol = [], {}
    targets = [r for r in m3 + m5]
    for idx, r in enumerate(targets):
        for i in range(4):
            for j in range(4):
                G = sp.groebner(eqs_generic(gg_word(r["verts"]), (i, j), N) + [MU * TT - 1],
                                *XS[:6], MU, TT, order="grevlex", domain=sp.QQ.frac_field(qg))
                if list(G) != [1]:
                    gen_pos.append((r["word"], i, j))
                    gen_sol[f"{r['word']}@{i},{j}"] = [str(g) for g in G]
        print(f"    generic q: {idx + 1}/{len(targets)} words done", flush=True)
    same_as_rational = sorted(gen_pos) == sorted(
        {(x[0], x[1], x[2]) for v in two.values() for x in v})
    check("P2_generic_q_two_photon", same_as_rational,
          f"over Q(q) the two-photon factorisations are exactly the ones found at q = 2, 3: "
          f"{sorted(gen_pos)}; every other (word, i, j) has Groebner basis [1], so no solution "
          "for generic q (finitely many special q not excluded).")

    # Part 3 (addendum 2): convention-D Markov trace, comparison only
    import qbeta_e0  # noqa: E402
    from qou_substrate.constants import q_at  # noqa: E402

    def trD(word, n):
        two_q = qg + 1 / qg
        tot = 0
        for bb in range(2 ** n):
            v = _act({bb: sp.Integer(1)}, word, qg, n)
            d = v.get(bb, 0)
            if d != 0:
                tot += qg ** (n - 2 * bin(bb).count("1")) * d
        return sp.factor(sp.simplify(tot / two_q ** n))

    pair = [(0, 1), (0, 1), (1, -1), (4, -1)]
    trs = {"pair_word_s0^2 s1^-1 s4^-1 (6 strands)": trD(pair, 6),
           "hopf_photon_s0^2 s1^-1 (3 strands)": trD(pair[:3], 3),
           "crossing_photon_s^-1 (2 strands)": trD([(0, -1)], 2),
           "electron_s0 s1 s0 (3 strands)": trD([(0, 1), (1, 1), (0, 1)], 3)}
    zD = qg ** 3 / (qg ** 2 + 1)
    mult = sp.simplify(trs["pair_word_s0^2 s1^-1 s4^-1 (6 strands)"]
                       - trs["hopf_photon_s0^2 s1^-1 (3 strands)"]
                       * trs["crossing_photon_s^-1 (2 strands)"]) == 0
    zcheck = sp.simplify(trD([(0, 1)], 2) - zD) == 0
    mp.mp.dps = 70
    q0 = q_at(70)
    E0 = qbeta_e0.canonical(q=q0)
    mev = {k: mp.nstr(abs(mp.mpf(str(sp.N(v.subs(qg, sp.Float(str(q0), 70)), 70)))) * E0, 15)
           for k, v in trs.items()}
    check("P3_zD_trace_comparison", mult and zcheck,
          f"Jimbo quantum trace / [2]^n is the convention-D Markov trace (tr(s) = z_D, checked); "
          f"exact traces { {k: str(v) for k, v in trs.items()} }; tr(pair) = tr(Hopf photon) * "
          f"tr(crossing photon) (Markov factorisation, checked). |tr| x E0 (canonical, proton q0), "
          f"COMPARISON ONLY, not proposed as Q_beta: {mev} MeV. CODATA Q_beta = 0.78233 MeV.")
    # same trace for every matching gamma-gamma word? (all have writhe 0)
    qf = mp.mpf(q0)
    by = {}
    for r in hits:
        w = gg_word(r["verts"])
        tot = mp.mpf(0)
        for bb in range(2 ** N):
            d = _act({bb: mp.mpf(1)}, w, qf, N).get(bb, 0)
            tot += qf ** (N - 2 * bin(bb).count("1")) * d
        by.setdefault(r["match"], set()).add(mp.nstr(abs(tot / (qf + 1 / qf) ** N) * E0, 30))
    check("P3_trace_same_for_every_match", all(len(v) == 1 for v in by.values()),
          f"every one of the {len(hits)} matching gamma-gamma words gives the same |tr_D| x E0 "
          f"per orientation (gamma-gamma words have writhe 0, so the Markov trace is a link "
          f"invariant on them): { {k: sorted(v) for k, v in by.items()} } MeV. COMPARISON ONLY.")
    zd_record = {"traces": {k: str(v) for k, v in trs.items()}, "abs_tr_times_E0_MeV": mev,
                 "E0": "qbeta_e0.canonical (tower-summed, by ruling)",
                 "status": "comparison only; the pair word is not the beta-decay element",
                 "per_orientation_all_matches_MeV": {k: sorted(v) for k, v in by.items()}}

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("six-strand-photon-pair", engine="fractions+sympy+mpmath", output_dir=_HERE)
    for nm, o, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "q0Anchor": "proton",
        "q0Value": str(q0),
        "q0AnchorReason": "Parts 1-2 are exact over Q(q) and at rational q = 2, 3, 11/10; "
                          "Part 3 evaluates the comparison trace |tr_D| * E0 at the proton pin q_at(70)",
        "description": "Gamma-gamma lepton pair e- + nu-bar + loop on six strands with the "
                       "sliding photon (owner card 2026-11-22): which vertex words close to it, "
                       "and how many photons each needs.",
        "photon": "gamma_i(a,b,c) = 1 + a s_i + b s_{i+1} + c s_i s_{i+1}^-1, i = 0..3",
        "matches_smallest": [{k: r[k] for k in ("word", "match", "idle_strands")} for r in m3],
        "matches_no_idle_smallest": [{k: r[k] for k in ("word", "match")} for r in m5],
        "zero_charge_sector_trace": sect,
        "two_photon_solutions": two,
        "three_photon_V0V0V1": {"TL_q2": tl3, "fullH_q2": h3},
        "real_three_photon_samples": real,
        "generic_q_two_photon": {"positions": sorted(gen_pos), "solutions": gen_sol},
        "zD_comparison": zd_record,
        "scope": "(a): six strands, <= 6 vertices; invariant at two rational q; Groebner at "
                 "q = 2 (and 3 for the two-photon m3 test); real search at q = 2, 11/10.",
        "lean": "QOU/QBeta/GammaGammaLeptonPair.lean (parity)",
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
