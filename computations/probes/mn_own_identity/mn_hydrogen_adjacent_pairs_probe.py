"""Pre-registered PREREGISTRATION-hydrogen-adjacent-pairs.md (b83c44f1773).
Hydrogen from gamma-gamma production with each created pair's two strands adjacent (layouts L1, L2, L3;
layout F of section 50 as control). Gathering braid G_T (all letters positive / negative), the section-46
element Y in the gathered frame, disposal by closing the disposed strands on side S:
  E_{8->4}(G_S Z G_S^-1) with Z = G_S^-1 Y G_T, i.e. Y . R_TS,  R_TS = E(G_T G_S^-1).
Bond reading A (sigma_i sigma_{i+1}^-1) and B (sigma_i^-1 sigma_{i+1}) for vertices off positions 0,1.
Reading 3 (two-row characters >= 0, convention D) on the WHOLE H_8 element; enumeration of freely reduced
gamma-gamma words; sigma0 sigma1 sigma0 (Hopf) electron arm on H_6 / H_9.
Engines: the C^2 tensor n R-matrix engine of mn_hydrogen_full_strand_probe.py (copied), and an Iwahori-basis
Hecke engine over the exact field Q(q) (sympy frac_field) for residues in a faithful basis.
Exact: Q(q), fractions.Fraction at q = 3 and at the exact rational proton pin; mpmath (80 dps) at q0 for the
character sweeps, signs certified against a 1e-45 band. No float64.
Gluon stays OPEN (owner 2026-11-22): every candidate below is a measurement, not a selection."""
import json, itertools, time
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mpm
from qou_substrate import constants as C

mpm.mp.dps = 80
Q0F = Fr(C.Q_50_DIGIT_STR)
Q0M = mpm.mpf(C.Q_50_DIGIT_STR)
BAND = mpm.mpf('1e-45')
T0 = time.time()
checks = []
def check(name, ok, detail=""):
    checks.append({"name": name, "pass": bool(ok), "detail": detail}); print("[%s] %s %s" % ("PASS" if ok else "FAIL", name, detail), flush=True)
def log(*a): print("[%6.1fs]" % (time.time() - T0), *a, flush=True)

# ======================================================== C^2 tensor n engine (from section 50)
def mats(q):
    h = q - 1/q
    R = {(0,0): [((0,0), q)], (0,1): [((1,0), 1)], (1,0): [((0,1), 1), ((1,0), h)], (1,1): [((1,1), q)]}
    Ri = {(0,0): [((0,0), 1/q)], (0,1): [((0,1), -h), ((1,0), 1)], (1,0): [((0,1), 1)], (1,1): [((1,1), 1/q)]}
    return R, Ri
def apply_word(word, vec, q, M=None):
    R, Ri = M or mats(q)
    for (i, inv) in reversed(word):          # rightmost letter acts first
        T = Ri if inv else R; out = {}
        for s, c in vec.items():
            for (a, b), v in T[(s[i], s[i+1])]:
                t = s[:i] + (a, b) + s[i+2:]; out[t] = out.get(t, 0) + c*v
        vec = {k: v for k, v in out.items() if v != 0}
    return vec
def kw(q): return {0: q**2/(q**2 + 1), 1: 1/(q**2 + 1)}
def wstr(w): return " ".join(f"s{i}{'^-1' if b else ''}" for i, b in w) or "1"
inv = lambda w: [(i, not b) for (i, b) in reversed(w)]
P = lambda ws: [(i, False) for i in ws]

def columns(word, n, q):
    M = mats(q); return {s: apply_word(word, {s: 1}, q, M) for s in itertools.product([0, 1], repeat=n)}
def chars_from_cols(cols, n, q, w=None):
    """two-row characters chi[m2] (m2 = lambda1 - lambda2) and tr_M (conv. D) of X.w, X given by its columns."""
    M = mats(q); k = kw(q); trm = {}; trM = 0
    for s in cols:
        if w is None: v = cols[s].get(s, 0)
        else:
            v = 0
            for t, c in apply_word(w, {s: 1}, q, M).items(): v += c*cols[t].get(s, 0)
        m2 = s.count(0) - s.count(1); trm[m2] = trm.get(m2, 0) + v
        wg = 1
        for x in s: wg *= k[x]
        trM += wg*v
    chi = {m2: trm.get(m2, 0) - trm.get(m2 + 2, 0) for m2 in range(n, -1, -2)}
    return chi, trM
def lam(n, m2): return f"({(n + m2)//2},{(n - m2)//2})"
def sgn_cert(x):
    if abs(x) < BAND: return 0
    return 1 if x > 0 else -1
def disposal(word, n, nk, q):
    """E_{n->nk}: close positions nk..n-1 with convention-D weights; returns dict (row,col) on C^2^nk."""
    k = kw(q); M = mats(q); res = {}
    for b in itertools.product([0, 1], repeat=nk):
        for c in itertools.product([0, 1], repeat=n - nk):
            wc = 1
            for x in c: wc *= k[x]
            for t, v in apply_word(word, {b + c: 1}, q, M).items():
                if t[nk:] == c: res[(t[:nk], b)] = res.get((t[:nk], b), 0) + wc*v
    return {kk: v for kk, v in res.items() if v != 0}
def matC2(word, n, q):
    M = mats(q); res = {}
    for b in itertools.product([0, 1], repeat=n):
        for t, v in apply_word(word, {b: 1}, q, M).items(): res[(t, b)] = res.get((t, b), 0) + v
    return {kk: v for kk, v in res.items() if v != 0}

# ======================================================== Iwahori-basis Hecke engine over Q(q)
qs = sp.symbols('q')
KF = sp.QQ.frac_field(qs)
Kq = KF.convert(qs); Kh = Kq - 1/Kq; Kz = Kq**3/(Kq**2 + 1); K1 = KF.one
def ilen(w): return sum(1 for a in range(len(w)) for b in range(a + 1, len(w)) if w[a] > w[b])
def rmul_gen(T, i, invb=False):
    """right-multiply element T (dict perm->coeff) by sigma_i (or sigma_i^-1 = sigma_i - h)."""
    out = {}
    for w, c in T.items():
        ws = list(w); ws[i], ws[i+1] = ws[i+1], ws[i]; ws = tuple(ws)
        if w[i] < w[i+1]: out[ws] = out.get(ws, KF.zero) + c
        else:
            out[ws] = out.get(ws, KF.zero) + c; out[w] = out.get(w, KF.zero) + Kh*c
        if invb: out[w] = out.get(w, KF.zero) - Kh*c
    return {k: v for k, v in out.items() if v != 0}
def from_word(word, n):
    T = {tuple(range(n)): K1}
    for i, b in word: T = rmul_gen(T, i, b)
    return T
def red_word(v):
    w = list(v); seq = []
    changed = True
    while changed:
        changed = False
        for i in range(len(w) - 1):
            if w[i] > w[i+1]: w[i], w[i+1] = w[i+1], w[i]; seq.append(i); changed = True
    return list(reversed(seq))
def mul(A, B, n):
    out = {}
    for v, cb in B.items():
        T = dict(A)
        for i in red_word(v): T = rmul_gen(T, i)
        for w, c in T.items(): out[w] = out.get(w, KF.zero) + c*cb
    return {k: v for k, v in out.items() if v != 0}
def add(A, B, a=K1, b=K1):
    out = {k: a*v for k, v in A.items()}
    for k, v in B.items(): out[k] = out.get(k, KF.zero) + b*v
    return {k: v for k, v in out.items() if v != 0}
_dcache = {}
def coset_reps(n):
    if n in _dcache: return _dcache[n]
    reps = []
    for k in range(n - 1, -1, -1):
        word = list(range(n - 2, k - 1, -1))     # [n-2, ..., k] (empty for k = n-1)
        d = list(range(n))
        for i in word: d[i], d[i+1] = d[i+1], d[i]
        reps.append((tuple(d), word))
    _dcache[n] = reps; return reps
def E_step(T, n):
    """Ocneanu/Jones conditional expectation H_n -> H_{n-1}, convention D: E(a sigma_{n-2} b) = z a b."""
    out = {}
    for v, c in T.items():
        done = False
        for d, word in coset_reps(n):
            dinv = [0]*n
            for x in range(n): dinv[d[x]] = x
            u = tuple(v[dinv[x]] for x in range(n))
            if u[n-1] == n - 1 and ilen(u) + ilen(d) == ilen(v):
                if not word: res = {u[:n-1]: c}
                else:
                    X = {u: c*Kz}
                    for i in word[1:]: X = rmul_gen(X, i)
                    res = {w[:n-1]: cc for w, cc in X.items()}
                for w, cc in res.items(): out[w] = out.get(w, KF.zero) + cc
                done = True; break
        assert done, v
    return {k: v for k, v in out.items() if v != 0}
def E_down(T, n, nk):
    for m in range(n, nk, -1): T = E_step(T, m)
    return T
def kval2(x, qq):
    e = sp.together(KF.to_sympy(x)); n_, d_ = sp.fraction(e)
    P1 = sp.Poly(n_, qs); P2 = sp.Poly(d_, qs)
    f = lambda Pp: sum(Fr(int(c.p), int(c.q))*qq**int(m[0]) for m, c in zip(Pp.monoms(), Pp.coeffs()))
    return f(P1)/f(P2)
def iw_to_C2(T, n, qq):
    res = {}
    for w, c in T.items():
        cv = kval2(c, qq)
        for kk, v in matC2(P(red_word(w)), n, qq).items(): res[kk] = res.get(kk, 0) + cv*v
    return {kk: v for kk, v in res.items() if v != 0}
def gen_support(T, n):
    """generators s_i occurring in the reduced words of the support (s_i occurs iff w does not preserve {0..i})."""
    g = set()
    for w in T:
        for i in range(n - 1):
            if set(w[:i+1]) != set(range(i + 1)): g.add(i)
    return sorted(g)
def iw_str(T, n):
    return {wstr(P(red_word(w))): str(sp.factor(KF.to_sympy(c))) for w, c in sorted(T.items(), key=lambda kv: (ilen(kv[0]), kv[0]))}

# ======================================================== layouts, labels, gathering
def kind(lab):
    if lab.startswith("qb"): return "antiquark"
    if lab.startswith("q"): return "quark"
    if lab == "e+": return "positron"
    return "electron"
def pair_of(lab):
    if lab.startswith("e"): return 0
    return int(lab[-1])
def classify(a, b):
    ka, kb = kind(a), kind(b)
    if pair_of(a) == pair_of(b) and not (ka == "electron" and kb == "electron"): return "intra-pair"
    if ka == kb == "electron": return "electron-electron (same particle)"
    s = tuple(sorted((ka, kb)))
    return {("quark", "quark"): "cross-pair quark-quark", ("antiquark", "antiquark"): "cross-pair antiquark-antiquark",
            ("antiquark", "quark"): "quark-antiquark of another pair"}.get(s, "-".join(s))
KEPT = lambda lab: kind(lab) in ("quark", "electron")
def gathering(layout):
    """time-ordered swaps of the minimal shuffle moving kept strands left (relative orders preserved)."""
    lab = list(layout); seq = []
    changed = True
    while changed:
        changed = False
        for i in range(len(lab) - 1):
            if not KEPT(lab[i]) and KEPT(lab[i+1]):
                lab[i], lab[i+1] = lab[i+1], lab[i]; seq.append(i); changed = True
    return seq, lab
def G_word(seq, sign):   # element word (rightmost acts first) of the gathering braid with all letters of one sign
    return [(i, sign == "-") for i in reversed(seq)]
def track(elem_word, labels0):
    perm = list(labels0); rec = []
    for (i, invb) in reversed(elem_word):
        a, b = perm[i], perm[i+1]
        rec.append({"letter": f"s{i}{'^-1' if invb else ''}", "strands": [a, b], "class": classify(a, b)})
        perm[i], perm[i+1] = b, a
    return rec, perm

LAYOUTS = {"L1": ["q1", "qb1", "q2", "qb2", "q3", "qb3", "e-", "e+"],
           "L2": ["qb1", "q1", "qb2", "q2", "qb3", "q3", "e+", "e-"],
           "L3": ["e-", "e+", "q1", "qb1", "q2", "qb2", "q3", "qb3"],
           "F":  ["q1", "q2", "q3", "e-", "e+", "qb1", "qb2", "qb3"]}
def Vv(i, reading):
    if i == 0 or reading == "A": return [(i, False), (i + 1, True)]
    return [(i, True), (i + 1, False)]
def Y_elem(layout_name, g_name, reading):
    if layout_name == "L3":   # e- at 0, quarks 1..3
        core = Vv(1, reading)*3; K = inv(P([0, 1, 2, 2, 1, 0]))
        gl = {"G0": [], "GV": Vv(1, reading), "Gs": P([2]), "GLm": P([2, 1])}
    else:
        core = Vv(0, reading)*3; K = inv(P([2, 1, 0, 0, 1, 2]))
        gl = {"G0": [], "GV": Vv(0, reading), "Gs": P([1]), "GLm": P([1, 0])}
    return core + gl[g_name] + K
GL_NAMES = ["G0", "GV", "Gs", "GLm"]
out = {"preregistration": "PREREGISTRATION-hydrogen-adjacent-pairs.md (b83c44f1773)", "layouts": LAYOUTS,
       "gluon_arms": {"L1/L2/F": {"G0": "1", "GV": "V0", "Gs": "s1", "GLm": "s1 s0"},
                      "L3": {"G0": "1", "GV": "V1 (reading)", "Gs": "s2", "GLm": "s2 s1"}},
       "readings": {"A": "V_i = s_i s_{i+1}^-1 (invert the larger letter; production)", "B": "V_i = s_i^-1 s_{i+1} (reflected letter)",
                    "note": "V_0 = s0 s1^-1 is the ruled vertex in both readings",
                    "owner_ruling_2026-11-22": "reading A plus right-hand closure is canonical (owner-rulings.md, PR #9019; sign-conventions-table section 6). Reading B is RETIRED: every B result below is moved to the section 'non_canonical_comparison (reading B retired 2026-11-22)' and is not a live alternative."}}

# ---------------- checks on the Iwahori expectation
for n in (2, 3, 4):
    Ez = E_step(from_word([(n - 2, False)], n), n)
    check(f"C1 Iwahori E_{n}->{n-1}(sigma_top) = z_D", Ez == {tuple(range(n - 1)): Kz})
check("C1 Iwahori E(1) = 1", E_step({tuple(range(3)): K1}, 3) == {(0, 1): K1})
# bimodule: E(s0 s2 s0^-1 s1) vs s0 E(s2) ... check E(a s_top b) = z a b for random a, b in H_3 at n=4
a = from_word([(0, False), (1, True)], 4); b = from_word([(1, False), (0, False)], 4)
lhs = E_step(mul(mul(a, from_word([(2, False)], 4), 4), b, 4), 4)
rhs = {w[:3]: Kz*c for w, c in mul(a, b, 4).items()}
check("C1 Iwahori E(a s_top b) = z a b (a = s0 s1^-1, b = s1 s0)", lhs == rhs)
# Iwahori expectation vs C^2 partial trace on a nontrivial word (8 -> 4 at q = 3)
wtest = [(4, False), (3, False), (5, True), (2, False), (6, False), (4, True), (3, False)]
Ti = E_down(from_word(wtest, 8), 8, 4)
check("C1 Iwahori E_{8->4} = C^2 partial-trace disposal at q = 3 (test word)", iw_to_C2(Ti, 4, Fr(3)) == disposal(wtest, 8, 4, Fr(3)))
log("checks on E done")

# ======================================================== M1 / M2
M1, M2 = {}, {}
RES = {}
for L, layout in LAYOUTS.items():
    seq, Fp = gathering(layout)
    out.setdefault("gathered_frame", {})[L] = {"frame_F_prime": Fp, "gathering_letters_time_order": seq, "n_letters": len(seq)}
    readings = ["A", "B"] if L == "L3" else ["A"]
    for TS in (("+", "+"), ("-", "-"), ("+", "-"), ("-", "+")):
        T_, S_ = TS
        GT, GS = G_word(seq, T_), G_word(seq, S_)
        # M1 bookkeeping of the whole element Z = G_S^-1 Y G_T (g = G0 and GV for the letter list)
        for rd in readings:
            for gname in ("G0", "GV"):
                Z = inv(GS) + Y_elem(L, gname, rd) + GT
                rec, perm = track(Z, layout)
                cls = {}
                for r in rec: cls[r["class"]] = cls.get(r["class"], 0) + 1
                M1[f"{L}|T{T_}S{S_}|{rd}|{gname}"] = {"element_word": wstr(Z), "class_counts": cls, "final_permutation": perm,
                                                      "letters_time_order": rec if (gname == "G0") else None}
        # M2 residue R = E(G_T G_S^-1)
        if L == "F": continue
        Rw = GT + inv(GS)
        Ti = E_down(from_word(Rw, 8), 8, 4)
        RES[(L, TS)] = Ti
        c2ok = all(iw_to_C2(Ti, 4, qq) == disposal(Rw, 8, 4, qq) for qq in (Fr(3),))
        scalar = set(Ti) <= {(0, 1, 2, 3)}
        gs = gen_support(Ti, 4)
        cen = all(mul(Ti, from_word([(i, False)], 4), 4) == mul(from_word([(i, False)], 4), Ti, 4) for i in range(3))
        rec_k = {0: f"{Fp[0]}-{Fp[1]}", 1: f"{Fp[1]}-{Fp[2]}", 2: f"{Fp[2]}-{Fp[3]}"}
        # span{1, V, V^2} test at q = 3 (exact): V of the kept quark window
        span = {}
        for rd in readings:
            V = from_word(Vv(1, rd) if L == "L3" else Vv(0, rd), 4)
            basis = [{tuple(range(4)): K1}, V, mul(V, V, 4)]
            keys = sorted(set(Ti) | set().union(*[set(x) for x in basis]))
            Mx = sp.Matrix([[sp.Rational(*(lambda f: (f.numerator, f.denominator))(kval2(bb.get(k_, KF.zero), Fr(3)))) for bb in basis] +
                            [sp.Rational(*(lambda f: (f.numerator, f.denominator))(kval2(Ti.get(k_, KF.zero), Fr(3))))] for k_ in keys])
            span[rd] = Mx[:, :3].rank() == Mx.rank()
        M2[f"{L}|T{T_}S{S_}"] = {"R_TS_iwahori": iw_str(Ti, 4), "n_terms": len(Ti), "scalar": scalar,
                                 "generator_support": [f"s{i} ({rec_k[i]})" for i in gs], "central_in_H4": cen,
                                 "in_span_1_V_V2_at_q3": span, "C2_partial_trace_check_q3": c2ok}
        log(L, TS, "R terms", len(Ti), "support", gs, "central", cen, "span", span, "C2", c2ok)
check("P2 T = S: R = 1 exactly in L1, L2, L3", all(M2[f"{L}|T{t}S{t}"]["R_TS_iwahori"] == {"1": "1"} for L in ("L1", "L2", "L3") for t in "+-"))
check("M2 Iwahori residues agree with C^2 partial-trace disposal (q = 3), all layouts and arms", all(v["C2_partial_trace_check_q3"] for v in M2.values()))
check("P3 T != S: R non-scalar in every adjacent layout", all(not M2[f"{L}|T{t}S{s}"]["scalar"] for L in ("L1", "L2", "L3") for t, s in (("+", "-"), ("-", "+"))))
check("P3 L1: R lies in <s1, s2> and contains s1 (q2-q3)", all([x.split()[0] for x in M2[f"L1|T{t}S{s}"]["generator_support"]] == ["s1", "s2"] for t, s in (("+", "-"), ("-", "+"))),
      str(M2["L1|T+S-"]["generator_support"]))
check("P3 L1: R not in span{1, V, V^2}", all(not M2[f"L1|T{t}S{s}"]["in_span_1_V_V2_at_q3"]["A"] for t, s in (("+", "-"), ("-", "+"))))
check("P3 L2: R involves s0, s1, s2", all(len(M2[f"L2|T{t}S{s}"]["generator_support"]) == 3 for t, s in (("+", "-"), ("-", "+"))))
# P1 bookkeeping
def cc(key): return M1[key]["class_counts"]
check("P1 L1: 6 gathering letters, none intra-pair; cross-pair quark-quark = 6 core letters",
      out["gathered_frame"]["L1"]["n_letters"] == 6 and cc("L1|T+S+|A|G0").get("intra-pair", 0) == 0 and cc("L1|T+S+|A|G0").get("cross-pair quark-quark") == 6,
      json.dumps(cc("L1|T+S+|A|G0")))
check("P1 L2: 10 gathering letters, 3 q_k-qb_k and 1 e- e+ (intra-pair 4 per pass, 8 in Z)",
      out["gathered_frame"]["L2"]["n_letters"] == 10 and cc("L2|T+S+|A|G0").get("intra-pair", 0) == 8 and cc("L2|T+S+|A|G0").get("cross-pair quark-quark") == 6,
      json.dumps(cc("L2|T+S+|A|G0")))
check("P1 L3: 6 gathering letters, none intra-pair; cross-pair quark-quark = 6 core letters",
      out["gathered_frame"]["L3"]["n_letters"] == 6 and cc("L3|T+S+|A|G0").get("intra-pair", 0) == 0 and cc("L3|T+S+|A|G0").get("cross-pair quark-quark") == 6,
      json.dumps(cc("L3|T+S+|A|G0")))
out["M1_bookkeeping"] = M1; out["M2_residues"] = M2
# letters joining quarks after disposal: the kept element is Y.R; R's letters joining two quark labels
q_pairs = {}
for key, v in M2.items():
    q_pairs[key] = [x for x in v["generator_support"] if all(p.startswith("q") for p in x.split("(")[1].rstrip(")").split("-"))]
out["M2_letters_joining_quarks_in_R"] = q_pairs
log("M1/M2 done")

# ======================================================== M3 reading 3 on the whole element
def r3_row(cols, n, w=None):
    chi, trM = chars_from_cols(cols, n, Q0M, w)
    sg = {lam(n, m2): sgn_cert(v) for m2, v in chi.items()}
    return {"chi": {lam(n, m2): mpm.nstr(v, 15) for m2, v in chi.items()},
            "reading3": "pass" if all(s >= 0 for s in sg.values()) and 0 not in sg.values() else ("undecided" if 0 in sg.values() and all(s >= 0 for s in sg.values()) else "fail"),
            "trM": mpm.nstr(trM, 15), "abs_trM": abs(trM)}
Ecr = lambda w: sum(-1/Q0M if b else Q0M for _, b in w)
M3 = {}; COLS = {}
for L, layout in LAYOUTS.items():
    seq, Fp = gathering(layout)
    readings = ["A", "B"] if L == "L3" else ["A"]
    TSs = [("+", "+")] if L == "F" else [("+", "+"), ("-", "-"), ("+", "-"), ("-", "+")]
    for T_, S_ in TSs:
        for rd in readings:
            for gname in GL_NAMES:
                Z = inv(G_word(seq, S_)) + Y_elem(L, gname, rd) + G_word(seq, T_)
                cols = columns(Z, 8, Q0M)
                if gname == "G0": COLS[(L, T_ + S_, rd)] = cols
                r = r3_row(cols, 8); r.pop("abs_trM")
                r.update({"crossings": len(Z), "E": mpm.nstr(Ecr(Z), 15)})
                M3[f"{L}|T{T_}S{S_}|{rd}|{gname}"] = r
        log("M3", L, T_, S_)
# Y alone on H_4 (section 46 element) for comparison, and P4
Y4 = {}
for L, rd in (("L1", "A"), ("L3", "A"), ("L3", "B")):
    for gname in GL_NAMES:
        r = r3_row(columns(Y_elem(L, gname, rd), 4, Q0M), 4); r.pop("abs_trM"); Y4[f"{L}-frame|{rd}|{gname}"] = r
out["M3_Y_on_H4"] = Y4
check("P4 (non-canonical comparison, reading B retired 2026-11-22) L3 reading B: Y'(B,G0) has the characters and tr_M of Y(G0) (L1 frame)",
      Y4["L3-frame|B|G0"]["chi"] == Y4["L1-frame|A|G0"]["chi"] and Y4["L3-frame|B|G0"]["trM"] == Y4["L1-frame|A|G0"]["trM"],
      f'{Y4["L3-frame|B|G0"]["trM"]} vs {Y4["L1-frame|A|G0"]["trM"]}')
out["M3_whole_H8"] = M3
log("M3 done")

# ======================================================== M4 enumeration of freely reduced gamma-gamma words
def free_reduce(w):
    st = []
    for x in w:
        if st and st[-1][0] == x[0] and st[-1][1] != x[1]: st.pop()
        else: st.append(x)
    return st
def gg_reduced(rd, cap=3):
    res = []
    for Lw in range(1, cap + 1):
        for t in itertools.product(range(6), repeat=Lw):
            w = sum((Vv(i, rd) for i in t), [])
            if free_reduce(w) == w: res.append((t, w))
    return res
M4 = {}
for L in ("F", "L1", "L2", "L3"):
    for TSk in (["++"] if L == "F" else ["++", "+-"]):
        for rd in ("A", "B"):
            base = COLS.get((L, TSk, rd)) or COLS.get((L, TSk, "A"))
            if L == "L3": base = COLS[(L, TSk, rd)]
            words = gg_reduced(rd); rows = []
            for t, w in words:
                r = r3_row(base, 8, w)
                rows.append({"vertices": "".join(f"V{i}" for i in t), "word": wstr(w), "crossings": len(w), "reading3": r["reading3"],
                             "trM": r["trM"], "abs_trM": r["abs_trM"], "E_word": mpm.nstr(Ecr(w), 15), "chi": r["chi"]})
            adm = [r for r in rows if r["reading3"] == "pass"]
            pk = {"n_words": len(rows), "pass": len(adm), "undecided": sum(r["reading3"] == "undecided" for r in rows)}
            if adm:
                mc = min(r["crossings"] for r in adm); mt = min(r["abs_trM"] for r in adm)
                pk.update({"min_crossings": [r["vertices"] for r in adm if r["crossings"] == mc], "min_crossings_value": mc,
                           "min_abs_trM": [r["vertices"] for r in adm if r["abs_trM"] == mt], "min_abs_trM_value": mpm.nstr(mt, 15),
                           "min_E": [r["vertices"] for r in adm if r["crossings"] == mc], "note": "E(w) = crossings*h/2 on writhe-0 words, so min E = min crossings"})
            for r in rows: r.pop("abs_trM")
            M4[f"{L}|T{TSk[0]}S{TSk[1]}|{rd}"] = {"picks": pk, "passing": [r["vertices"] for r in rows if r["reading3"] == "pass"], "rows": rows}
            log("M4", L, TSk, rd, pk["pass"], "/", pk["n_words"])
import re
def vseq(v): return [int(x) for x in re.findall(r"V(\d)", v)]
check("M4 reduction rule: every kept word is freely reduced; V_i V_{i+1} absent (i >= 0 reading A, i >= 1 reading B)",
      all(free_reduce([(int(x.split("^")[0][1:]), "^-1" in x) for x in r["word"].split()]) == [(int(x.split("^")[0][1:]), "^-1" in x) for x in r["word"].split()]
          and all(not (b_ == a_ + 1 and (a_ >= 1 or k.split("|")[2] == "A")) for a_, b_ in zip(vseq(r["vertices"]), vseq(r["vertices"])[1:]))
          for k, v in M4.items() for r in v["rows"]))
def n_expected(rd):   # independent count on index sequences: forbidden adjacent (i, i+1), i >= 1 only in reading B (V0 is always s0 s1^-1)
    forb = {(i, i + 1) for i in range(5)} if rd == "A" else {(i, i + 1) for i in range(1, 5)}
    return sum(1 for Lw in (1, 2, 3) for t in itertools.product(range(6), repeat=Lw) if all((a_, b_) not in forb for a_, b_ in zip(t, t[1:])))
check("M4 reduced word count matches the index-sequence count (A: 197, B: 209)",
      all(v["picks"]["n_words"] == n_expected(k.split("|")[2]) for k, v in M4.items()), str({rd: n_expected(rd) for rd in "AB"}))
out["M4_enumeration_reduced_cap6"] = M4
log("M4 done")

# ======================================================== M5 electron sigma0 sigma1 sigma0 (Hopf) arm
def cable_capture():
    lab = ["q1", "q2", "q3", "e1", "e2", "e3"]; left = []
    changed = True
    while changed:
        changed = False
        for i in range(5):
            if lab[i].startswith("q") and lab[i+1].startswith("e"): lab[i], lab[i+1] = lab[i+1], lab[i]; left.append(i); changed = True
    right = []; changed = True
    while changed:
        changed = False
        for i in range(5):
            if lab[i].startswith("e") and lab[i+1].startswith("q"): lab[i], lab[i+1] = lab[i+1], lab[i]; right.append(i); changed = True
    loop_elem = [(i, False) for i in reversed(left + right)]
    return inv(loop_elem), lab
Kc, lab_back = cable_capture()
check("M5 cabled capture returns the bundles to q1 q2 q3 e1 e2 e3 (pure braid), 18 letters", lab_back == ["q1", "q2", "q3", "e1", "e2", "e3"] and len(Kc) == 18)
# single-strand version of the same construction reproduces K
lab = ["q1", "q2", "q3", "e"]; left = []; ch = True
while ch:
    ch = False
    for i in range(3):
        if lab[i].startswith("q") and lab[i+1] == "e": lab[i], lab[i+1] = lab[i+1], lab[i]; left.append(i); ch = True
right = []; ch = True
while ch:
    ch = False
    for i in range(3):
        if lab[i] == "e" and lab[i+1].startswith("q"): lab[i], lab[i+1] = lab[i+1], lab[i]; right.append(i); ch = True
check("M5 the cable construction with one electron strand gives K = (s2 s1 s0 s0 s1 s2)^-1", inv([(i, False) for i in reversed(left + right)]) == inv(P([2, 1, 0, 0, 1, 2])))
We = P([3, 4, 3])
def Y6(gname):
    gl = {"G0": [], "GV": Vv(0, "A"), "Gs": P([1]), "GLm": P([1, 0])}
    return Vv(0, "A")*3 + gl[gname] + Kc + We
M5 = {}
trE = chars_from_cols(columns(P([0, 1, 0]), 3, Q0M), 3, Q0M)[1]
trPos = chars_from_cols(columns(inv(P([0, 1, 0])), 3, Q0M), 3, Q0M)[1]
qM = Q0M
check("P6 tr_D(s0 s1 s0) = q^3(q^4+1)/(q^2+1)^2 at q0", abs(trE - qM**3*(qM**4 + 1)/(qM**2 + 1)**2) < BAND, mpm.nstr(trE, 15))
M5["tr_D_electron_word"] = mpm.nstr(trE, 20); M5["tr_D_positron_mirror_word"] = mpm.nstr(trPos, 20)
for gname in GL_NAMES:
    r = r3_row(columns(Y6(gname), 6, Q0M), 6); r.pop("abs_trM"); M5[f"Y6_on_H6|{gname}"] = r
# Y without capture: factorisation check (P6)
rnc = chars_from_cols(columns(Vv(0, "A")*3 + We, 6, Q0M), 6, Q0M)[1]
rcore = chars_from_cols(columns(Vv(0, "A")*3, 3, Q0M), 3, Q0M)[1]
check("P6 no capture: tr_M(V0^3 . s3 s4 s3) = tr_M(V^3) tr_D(s0 s1 s0)", abs(rnc - rcore*trE) < BAND)
L13 = ["q1", "qb1", "q2", "qb2", "q3", "qb3", "e1", "e2", "e3"]
seq3, Fp3 = gathering(L13)
M5["L1_3_layout"] = L13; M5["L1_3_gathered"] = Fp3; M5["L1_3_gathering_letters"] = len(seq3)
for TS in (("+", "+"), ("+", "-"), ("-", "+")):
    T_, S_ = TS; GT, GS = G_word(seq3, T_), G_word(seq3, S_)
    if T_ != S_:
        Rw = GT + inv(GS)
        Ti = E_down(from_word(Rw, 9), 9, 6)
        names = {i: f"{Fp3[i]}-{Fp3[i+1]}" for i in range(5)}
        M5[f"R_L1_3|T{T_}S{S_}"] = {"n_terms": len(Ti), "generator_support": [f"s{i} ({names[i]})" for i in gen_support(Ti, 6)],
                                     "scalar": set(Ti) <= {tuple(range(6))}}
        log("M5 residue", TS, len(Ti), gen_support(Ti, 6))
    for gname in ("G0", "GV"):
        Z = inv(GS) + Y6(gname) + GT
        r = r3_row(columns(Z, 9, Q0M), 9); r.pop("abs_trM"); r["crossings"] = len(Z)
        M5[f"whole_H9_L1_3|T{T_}S{S_}|{gname}"] = r
        log("M5 whole H9", TS, gname, r["reading3"])
for gname in ("G0", "GV"):
    r = r3_row(columns(Y6(gname), 9, Q0M), 9); r.pop("abs_trM"); M5[f"whole_H9_F3|{gname}"] = r
out["M5_electron_s0s1s0"] = M5
# ---- owner ruling 2026-11-22: reading A canonical; move every reading-B result to a labelled comparison section
NC = {}
for sec in ("M1_bookkeeping", "M3_whole_H8", "M3_Y_on_H4", "M4_enumeration_reduced_cap6"):
    moved = {k: v for k, v in out[sec].items() if "|B|" in k or k.endswith("|B")}
    for k in moved: del out[sec][k]
    NC[sec] = moved
NC["M2_in_span_1_V_V2_at_q3_reading_B"] = {k: v["in_span_1_V_V2_at_q3"].pop("B") for k, v in out["M2_residues"].items() if "B" in v["in_span_1_V_V2_at_q3"]}
out["non_canonical_comparison (reading B retired 2026-11-22)"] = NC
out["checks"] = checks; out["checks_passed"] = f"{sum(c['pass'] for c in checks)}/{len(checks)}"
open(__file__.replace('.py', '.out.json'), 'w').write(json.dumps(out, indent=1, default=str) + "\n")
log(out["checks_passed"])
