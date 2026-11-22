"""Pre-registered PREREGISTRATION-hydrogen-full-strand-gammagamma.md (4c6cb4ad589).
Hydrogen on its full strand count H_8 from gamma-gamma production (layout F: q1 q2 q3 e- | e+ qb1 qb2 qb3),
cross-pair letter bookkeeping, disposal by the convention-D conditional expectation (closure of the
rightmost strands), the general collision gamma(phi)gamma(psi) in H_3, and an enumeration of gamma-gamma
words (products of vertices s_i s_{i+1}^-1) up to 6 crossings on H_3, H_4, H_8 with reading 3.
Photon = 1 + p0 s0 + p1 s1 + p01 s0 s1^-1 (owner ruling). Exact: sympy over Q(q) for symbolic checks,
fractions.Fraction at the exact rational proton pin q0 (and at q = 3) for numeric work. No float64.
Gluon stays OPEN (owner 2026-11-22): every pick below is a measurement, not a selection."""
import json, itertools
from fractions import Fraction as Fr
import sympy as sp
from qou_substrate import constants as C

Q0 = Fr(C.Q_50_DIGIT_STR)
checks = []
def check(name, ok, detail=""):
    checks.append({"name": name, "pass": bool(ok), "detail": detail}); print("[%s] %s %s" % ("PASS" if ok else "FAIL", name, detail))

# ---------------- C^2 tensor n engine, generic coefficient field
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
def apply_elem(factors, vec, q, M=None):     # factors: list of [(coeff, word)], rightmost first
    for E in reversed(factors):
        new = {}
        for c, w in E:
            for t, v in apply_word(w, vec, q, M).items(): new[t] = new.get(t, 0) + c*v
        vec = {k: v for k, v in new.items() if v != 0}
    return vec
W1 = lambda w: [(1, w)]
P = lambda ws: [(i, False) for i in ws]
inv = lambda w: [(i, not b) for (i, b) in reversed(w)]
Vw = lambda i: [(i, False), (i+1, True)]
def kw(q):  # convention-D closure weights per strand state
    return {0: q**2/(q**2 + 1), 1: 1/(q**2 + 1)}

def characters(word_or_elem, n, q, elem=False):
    """two-row characters chi_j, j = n/2, n/2-1, ...; chi_j = Tr|_{T3=j} - Tr|_{T3=j+1}; plus tr_M (conv. D)."""
    M = mats(q); k = kw(q); trm = {}; trM = 0
    for s in itertools.product([0, 1], repeat=n):
        v = (apply_elem(word_or_elem, {s: 1}, q, M) if elem else apply_word(word_or_elem, {s: 1}, q, M)).get(s, 0)
        m2 = s.count(0) - s.count(1)          # 2*T3
        trm[m2] = trm.get(m2, 0) + v
        wgt = 1
        for x in s: wgt *= k[x]
        trM += wgt*v
    chi = {}
    for m2 in range(n, -1, -2):
        chi[m2] = trm.get(m2, 0) - trm.get(m2 + 2, 0)
    return chi, trM   # key m2 = lambda1 - lambda2

def lam(n, m2): return f"({(n + m2)//2},{(n - m2)//2})"
def nstr(x, d=14):
    if isinstance(x, Fr):
        neg = x < 0; x = abs(x); ip = x.numerator // x.denominator; fr = x - ip
        digs = "".join(str((fr*10**(k+1)).numerator // (fr*10**(k+1)).denominator % 10) for k in range(d))
        return ("-" if neg else "") + f"{ip}.{digs}"
    return str(x)

out = {"preregistration": "PREREGISTRATION-hydrogen-full-strand-gammagamma.md (4c6cb4ad589)",
       "layout_F": "positions 0,1,2 = q1,q2,q3; 3 = e-; 4 = e+; 5,6,7 = qb1,qb2,qb3", "tower": "H_8(q) on C^2 tensor 8"}

# ---------------- checks on the disposal map
qs = sp.symbols('q', positive=True)
for qq, lab in ((Q0, "q0"), (Fr(3), "q=3")):
    k = kw(qq)
    # E_{2->1}(s0): sum_c k(c) <a c| s0 |b c>
    Es = {}
    for a in (0, 1):
        for b in (0, 1):
            Es[(a, b)] = sum(k[c]*apply_word([(0, False)], {(b, c): 1}, qq).get((a, c), 0) for c in (0, 1))
    zD = qq**3/(qq**2 + 1)
    check(f"C1 E(sigma_last) = z_D * 1 at {lab}", Es[(0,0)] == zD and Es[(1,1)] == zD and Es[(0,1)] == 0 and Es[(1,0)] == 0)
    check(f"C1 E(1) = 1 at {lab}", k[0] + k[1] == 1)

# ---------------- M1 / M2: full word on H_8 and disposal
labels0 = ["q1", "q2", "q3", "e-", "e+", "qb1", "qb2", "qb3"]
pair = {"q1": 1, "qb1": 1, "q2": 2, "qb2": 2, "q3": 3, "qb3": 3, "e-": 0, "e+": 0}
def classify(a, b):
    if pair[a] == pair[b]: return "intra-pair"
    qa, qb = a.startswith("q") and not a.startswith("qb"), b.startswith("q") and not b.startswith("qb")
    ba, bb = a.startswith("qb"), b.startswith("qb")
    if qa and qb: return "cross-pair quark-quark"
    if ba and bb: return "cross-pair antiquark-antiquark"
    if (qa or qb) and (a.startswith("e") or b.startswith("e")): return "quark-lepton"
    return "other cross-pair"
def track(word_time_order):
    perm = list(labels0); rec = []
    for (i, invb) in word_time_order:
        a, b = perm[i], perm[i+1]
        rec.append({"letter": f"s{i}{'^-1' if invb else ''}", "strands": [a, b], "class": classify(a, b)})
        perm[i], perm[i+1] = b, a
    return rec, perm
core0 = Vw(0)*3; core5 = Vw(5)*3
K = inv(P([2, 1, 0, 0, 1, 2]))
gl = {"G0": [], "GV": Vw(0), "Gs1": P([1]), "GLm": P([1, 0])}
out["M1_full_word"] = {}
for aarm, anti in (("A-ann", []), ("A-bar", core5)):
    for gname, g in gl.items():
        word = core0 + anti + g + K              # element product; acts rightmost first
        rec, perm = track(list(reversed(word)))  # time order
        cls = {}
        for r in rec: cls[r["class"]] = cls.get(r["class"], 0) + 1
        out["M1_full_word"][f"{aarm}|{gname}"] = {"element_word_left_to_right": " ".join(f"s{i}{'^-1' if b else ''}" for i, b in word),
                                                  "letters_in_time_order": rec, "class_counts": cls, "final_permutation": perm}
        print(aarm, gname, cls)
check("P1 derived arm: no intra-pair letter anywhere (pair creation and BW place no letters)",
      all(v["class_counts"].get("intra-pair", 0) == 0 for v in out["M1_full_word"].values()))
check("P1 G0: cross-pair quark-quark letters = exactly the 6 core letters; the 6 capture letters are quark-lepton",
      out["M1_full_word"]["A-ann|G0"]["class_counts"] == {"quark-lepton": 6, "cross-pair quark-quark": 6}, str(out["M1_full_word"]["A-ann|G0"]["class_counts"]))

def disposal(word8, qq):
    """E_{8->4}: closes positions 4..7 with convention-D weights. Returns dict (a,b)->entry on C^2^4."""
    k = kw(qq); M = mats(qq); res = {}
    cl = list(itertools.product([0, 1], repeat=4))
    for b in itertools.product([0, 1], repeat=4):
        for c in cl:
            wc = k[c[0]]*k[c[1]]*k[c[2]]*k[c[3]]
            for t, v in apply_word(word8, {b + c: 1}, qq, M).items():
                if t[4:] == c: res[(t[:4], b)] = res.get((t[:4], b), 0) + wc*v
    return res
def mat4(word4, qq):
    M = mats(qq); res = {}
    for b in itertools.product([0, 1], repeat=4):
        for t, v in apply_word(word4, {b: 1}, qq, M).items(): res[(t, b)] = res.get((t, b), 0) + v
    return res
def proportional(A, B):
    keys = set(A) | set(B); c = None
    for kk in keys:
        a, b = A.get(kk, 0), B.get(kk, 0)
        if b == 0:
            if a != 0: return None
            continue
        r = a/b
        if c is None: c = r
        elif r != c: return None
    return c
out["M2_disposal"] = {}
for qq, lab in ((Q0, "q0"), (Fr(3), "q=3")):
    for aarm, anti in (("A-ann", []), ("A-bar", core5)):
        for gname, g in gl.items():
            red = disposal(core0 + anti + g + K, qq)
            ref = mat4(core0 + g + K, qq)
            c = proportional(red, ref)
            out["M2_disposal"][f"{lab}|{aarm}|{gname}"] = {"proportional_to_s46_element": c is not None, "c": nstr(c) if c is not None else None}
    # predicted c for A-bar: tr_M(V^3) on 3 strands
    _, trV3 = characters(Vw(0)*3, 3, qq)
    cc = out["M2_disposal"][f"{lab}|A-bar|G0"]["c"]
    check(f"P2 disposal exact: A-ann c = 1, A-bar c = tr_M(V^3 on H_3) at {lab}",
          all(v["proportional_to_s46_element"] for kk, v in out["M2_disposal"].items() if kk.startswith(lab))
          and out["M2_disposal"][f"{lab}|A-ann|G0"]["c"] == nstr(Fr(1)) and cc == nstr(trV3), f"tr_M(V^3) = {nstr(trV3)}")

# ---------------- M3: general collision in H_3, words and NF (Iwahori basis on S_3)
f0, f1, f01, g0, g1, g01 = sp.symbols('phi0 phi1 phi01 psi0 psi1 psi01'); hq = qs - 1/qs
def gam(a, b, c): return [(1, []), (a, [(0, False)]), (b, [(1, False)]), (c, [(0, False), (1, True)])]
words = {}
for c1, w1 in gam(f0, f1, f01):
    for c2, w2 in gam(g0, g1, g01):
        key = " ".join(f"s{i}{'^-1' if b else ''}" for i, b in (w1 + w2)) or "1"
        words[key] = sp.expand(sp.sympify(words.get(key, 0)) + c1*c2)
# NF via right regular action on T_w, w in S_3 as reduced words
def smul(T, i):     # right-multiply element T (dict perm->coeff) by sigma_i
    out_ = {}
    for w, c in T.items():
        ws = list(w); ws[i], ws[i+1] = ws[i+1], ws[i]; ws = tuple(ws)
        lw = sum(1 for a in range(3) for b in range(a+1, 3) if w[a] > w[b]); lws = sum(1 for a in range(3) for b in range(a+1, 3) if ws[a] > ws[b])
        if lws > lw: out_[ws] = out_.get(ws, 0) + c
        else: out_[ws] = out_.get(ws, 0) + c; out_[w] = out_.get(w, 0) + hq*c
    return out_
def nf(word):
    T = {(0, 1, 2): sp.Integer(1)}
    for i, b in word:
        if b:   # sigma^-1 = sigma - h
            A = smul(T, i); T = {w: A.get(w, 0) - hq*T.get(w, 0) for w in set(A) | set(T)}
        else: T = smul(T, i)
    return T
nm = {(0, 1, 2): "1", (1, 0, 2): "s0", (0, 2, 1): "s1", (1, 2, 0): "s0s1", (2, 0, 1): "s1s0", (2, 1, 0): "s0s1s0"}
def nf_elem(terms):
    tot = {}
    for c, w in terms:
        for p, v in nf(w).items(): tot[p] = tot.get(p, 0) + c*v
    return {nm[p]: sp.factor(sp.simplify(v)) for p, v in tot.items() if sp.simplify(v) != 0}
prodterms = [(c1*c2, w1 + w2) for c1, w1 in gam(f0, f1, f01) for c2, w2 in gam(g0, g1, g01)]
NFgen = nf_elem(prodterms)
ledger = {"s1": [(1, False)], "s0s0": [(0, False), (0, False)], "Lm=s1s0": [(1, False), (0, False)], "V=s0s1^-1": [(0, False), (1, True)]}
keymap = {"s1": "s1", "s0s0": "s0 s0", "Lm=s1s0": "s1 s0", "V=s0s1^-1": "s0 s1^-1"}
occ = {k: str(words.get(v, 0)) for k, v in keymap.items()}
out["M3_general_collision"] = {"words_with_coefficients": {k: str(v) for k, v in words.items()},
                               "ledger_candidates_as_words": occ,
                               "NF_general": {k: str(v) for k, v in NFgen.items()}}
check("P4 all four ledger words occur in gamma(phi)gamma(psi) with coefficients phi1+psi1, phi0 psi0, phi1 psi0, phi01+psi01",
      sp.simplify(words["s1"] - (f1 + g1)) == 0 and sp.simplify(words["s0 s0"] - f0*g0) == 0
      and sp.simplify(words["s1 s0"] - f1*g0) == 0 and sp.simplify(words["s0 s1^-1"] - (f01 + g01)) == 0, json.dumps(occ))
spec = {f0: 0, f1: 0, f01: qs*hq, g0: 0, g1: 0, g01: -hq/qs}
wspec = {k: sp.simplify(v.subs(spec)) for k, v in words.items()}; wspec = {k: v for k, v in wspec.items() if v != 0}
NFspec = nf_elem([(sp.sympify(c).subs(spec), w) for c, w in prodterms]); NFV3 = nf_elem([(1, Vw(0)*3)])
out["M3_general_collision"]["derived_weights_words"] = {k: str(sp.factor(v)) for k, v in wspec.items()}
out["M3_general_collision"]["derived_weights_NF"] = {k: str(v) for k, v in NFspec.items()}
check("P4 derived weights: words = {1, V, V V} only, NF equals NF(V^3)",
      set(wspec) == {"1", "s0 s1^-1", "s0 s1^-1 s0 s1^-1"} and all(sp.simplify(NFspec.get(k, 0) - NFV3.get(k, 0)) == 0 for k in set(NFspec) | set(NFV3)),
      str({k: str(sp.factor(v)) for k, v in wspec.items()}))

# ---------------- M4: writhe
writhe = lambda w: sum(-1 if b else 1 for _, b in w)
out["M4_writhe"] = {k: writhe(v) for k, v in ledger.items()}
out["M4_writhe"]["every gamma-gamma word"] = 0
check("P3 only V among the ledger candidates has writhe 0 (every gamma-gamma word has writhe 0)",
      [k for k, v in ledger.items() if writhe(v) == 0] == ["V=s0s1^-1"], json.dumps(out["M4_writhe"]))
h0 = Q0 - 1/Q0
E = lambda w, qq: sum((1/qq)*(-1) if b else qq for _, b in w)

# ---------------- M5: enumeration
def row(word, n, qq=Q0, elem=None):
    chi, trM = characters(elem if elem is not None else word, n, qq, elem=elem is not None)
    return {"word": " ".join(f"s{i}{'^-1' if b else ''}" for i, b in word) or "1", "crossings": len(word),
            "chi": {lam(n, m2): nstr(v) for m2, v in chi.items()}, "reading3_pass": all(v >= 0 for v in chi.values()),
            "trM": nstr(trM), "abs_trM": abs(trM), "E": nstr(E(word, qq))}
def picks(rows):
    adm = [r for r in rows if r["reading3_pass"] and r["crossings"] > 0]
    if not adm: return {"admissible_nonidentity": 0}
    mc = min(r["crossings"] for r in adm); mt = min(r["abs_trM"] for r in adm)
    return {"admissible_nonidentity": len(adm), "of": sum(1 for r in rows if r["crossings"] > 0),
            "min_crossings": [r["word"] for r in adm if r["crossings"] == mc], "min_crossings_value": mc,
            "min_abs_trM": [r["word"] for r in adm if r["abs_trM"] == mt], "min_abs_trM_value": nstr(mt),
            "min_E": [r["word"] for r in adm if r["crossings"] == mc], "note": "on gamma-gamma words E = crossings*h/2 (writhe 0), so min E = min crossings"}
def gg_words(nv, cap=3):
    res = [[]]
    for L in range(1, cap + 1):
        for t in itertools.product(range(nv), repeat=L): res.append(sum((Vw(i) for i in t), []))
    return res
M5 = {}
# H_3: bare gamma-gamma words, and gluon-on-core core.g
r3 = [row(w, 3) for w in gg_words(1)]
r3c = [dict(row(w, 3, elem=[W1(core0 + w)]), word=" ".join(f"s{i}{'^-1' if b else ''}" for i, b in w) or "1") for w in gg_words(1)]
M5["H3_bare"] = {"rows": r3, "picks": picks(r3)}; M5["H3_core_times_g"] = {"rows": r3c, "picks": picks(r3c)}
check("P5 H_3: core.V^k passes reading 3 for k in {0,3} only (k<=3)", [r["word"] for r in r3c if r["reading3_pass"]] == ["1", "s0 s1^-1 s0 s1^-1 s0 s1^-1"],
      str([r["word"] for r in r3c if r["reading3_pass"]]))
# ledger candidates on the bare core, H_3
lr = [dict(row(w, 3, elem=[W1(core0 + w)]), word=k, E=nstr(E(w, Q0))) for k, w in ledger.items()]
M5["H3_ledger_on_core"] = lr
print("ledger on core:", [(r["word"], r["reading3_pass"], r["trM"], r["E"]) for r in lr])
# symbolic: sign of chi for core.V^k over q > 1? report exact (2,1) characters
chis = {}
for kk in range(4):
    ch, _ = characters(core0 + Vw(0)*kk, 3, qs); chis[f"V^{3+kk}"] = {lam(3, m2): str(sp.factor(sp.simplify(v))) for m2, v in ch.items()}
M5["H3_core_times_g_exact"] = chis
# H_4: gamma-gamma words over V0, V1; bare and as hydrogen gluon arm V0^3 . g . K
r4 = [row(w, 4) for w in gg_words(2)]
r4h = [dict(row(w, 4, elem=[W1(core0 + w + K)]), word=" ".join(f"s{i}{'^-1' if b else ''}" for i, b in w) or "1",
            crossings=len(w), E=nstr(E(w, Q0)), touches_electron_strand=any(i == 2 for i, _ in w)) for w in gg_words(2)]
M5["H4_bare"] = {"rows": r4, "picks": picks(r4)}; M5["H4_hydrogen_core_g_K"] = {"rows": r4h, "picks": picks(r4h)}
# H_8 bare gamma-gamma words
r8 = []
for idx, w in enumerate(gg_words(6)):
    r8.append(row(w, 8))
    if idx % 50 == 0: print("H8", idx, "/ 259", flush=True)
M5["H8_bare"] = {"pass_count": sum(r["reading3_pass"] for r in r8 if r["crossings"] > 0), "of": len(r8) - 1,
                 "passing_words": [r["word"] for r in r8 if r["reading3_pass"] and r["crossings"] > 0], "picks": picks(r8),
                 "failing_blocks_histogram": {}}
for r in r8:
    if not r["reading3_pass"]:
        for l, v in r["chi"].items():
            if v.startswith("-"): M5["H8_bare"]["failing_blocks_histogram"][l] = M5["H8_bare"]["failing_blocks_histogram"].get(l, 0) + 1
def free_reduce(w):
    st = []
    for x in w:
        if st and st[-1][0] == x[0] and st[-1][1] != x[1]: st.pop()
        else: st.append(x)
    return st
# post-hoc (not pre-registered): which H_8 passing words are freely reducible (s_j s_j^-1 adjacent)
ph = []
for w, r in zip(gg_words(6), r8):
    if r["reading3_pass"] and r["crossings"] > 0:
        fr = free_reduce(w); ph.append({"word": r["word"], "freely_reduced": " ".join(f"s{i}{'^-1' if b else ''}" for i, b in fr), "reduced_crossings": len(fr)})
M5["H8_bare"]["post_hoc_free_reduction_of_passing_words"] = ph
M5["H8_bare"]["post_hoc_passing_words_that_are_freely_reduced_already"] = [x["word"] for x in ph if x["reduced_crossings"] == len(x["word"].split())]
print("H8 passing, already freely reduced:", M5["H8_bare"]["post_hoc_passing_words_that_are_freely_reduced_already"])
for blk in M5.values():
    for r in (blk["rows"] if isinstance(blk, dict) and "rows" in blk else (blk if isinstance(blk, list) else [])):
        r.pop("abs_trM", None)
out["M5_enumeration_cap6"] = M5
for k in ("H3_bare", "H3_core_times_g", "H4_bare", "H4_hydrogen_core_g_K", "H8_bare"):
    print(k, M5[k]["picks"])
out["checks"] = checks; out["checks_passed"] = f"{sum(c['pass'] for c in checks)}/{len(checks)}"
open(__file__.replace('.py', '.out.json'), 'w').write(json.dumps(out, indent=1, default=str) + "\n")
print(out["checks_passed"])
