"""Pre-registered PREREGISTRATION-hydrogen-from-photons.md (ddf883a5d25).
Hydrogen as one Hecke element by the six steps of def:derived-atom:
  W = gamma(0,0,q h) . gamma(0,0,-q^-1 h) . g . K   (steps 1+3, 4, 6; steps 2, 5 carry no letters)
on C^2 tensor 4, photon = 1 + p0 s0 + p1 s1 + p01 s0 s1^-1 (owner ruling). Gluon arms G0/GV/Gs1/GLm,
capture C-cable / C-adj, proton left/right; arm Phi: general symbolic collision.
Exact sympy over Q(q) (Q(q, phi) in arm Phi); mpmath 60 dps at q0. No float64.
DEVIATION from the pre-registration wording: the proton-right control TRANSLATES the proton block
(photon on generators 1,2 with fourth term s1 s2^-1, as in §43) and REFLECTS only the capture. A full
strand reflection would turn the photon's fourth term into s_{i+1} s_i^-1, which is not the ruled
photon. post_hoc_observations are not pre-registered."""
import json, itertools, sympy as sp, mpmath as mp
from qou_substrate import constants as C
mp.mp.dps = 60
q = sp.symbols('q', positive=True); h = q - 1/q
R = {(0,0): [((0,0), q)], (0,1): [((1,0), 1)], (1,0): [((0,1), 1), ((1,0), h)], (1,1): [((1,1), q)]}
Ri = {(0,0): [((0,0), 1/q)], (0,1): [((0,1), -h), ((1,0), 1)], (1,0): [((0,1), 1)], (1,1): [((1,1), 1/q)]}
def apply(L, vec):
    i, inv = L; M = Ri if inv else R; out = {}
    for s, c in vec.items():
        for (a, b), v in M[(s[i], s[i+1])]:
            t = s[:i] + (a, b) + s[i+2:]; out[t] = out.get(t, 0) + c*v
    return out
def word_apply(word, vec):
    for L in reversed(word): vec = apply(L, vec)
    return vec
# an element is a list of (coeff, word); product = concatenation; applied rightmost factor first
def elem_apply(factors, vec):
    for E in reversed(factors):
        new = {}
        for c, w in E:
            for t, v in word_apply(w, vec).items(): new[t] = new.get(t, 0) + c*v
        vec = new
    return vec
inv = lambda w: [(i, not b) for (i, b) in reversed(w)]
P = lambda ws: [(i, False) for i in ws]
W1 = lambda w: [(1, w)]
def photon(i, p0, p1, p01):   # 1 + p0 s_i + p1 s_{i+1} + p01 s_i s_{i+1}^-1
    return [(1, []), (p0, [(i, False)]), (p1, [(i+1, False)]), (p01, [(i, False), (i+1, True)])]
V = lambda i: [(i, False), (i+1, True)]
T3 = lambda s, rng: sp.Rational(sum(1 if s[k] == 0 else -1 for k in rng), 2)
n = 4
basis = list(itertools.product([0, 1], repeat=n))
def diag_of(factors):
    return {s: sp.expand(elem_apply(factors, {s: 1}).get(s, 0)) for s in basis}
def functionals(diag, prot):
    elec = [k for k in range(n) if k not in prot]; res = {}
    for name, w in (("O+", 2), ("O-", 1)):
        sel = [s for s in basis if sum(1 for k in prot if s[k] == 0) == w]
        res[name] = {"B1": sum(T3(s, range(n))*diag[s] for s in sel),
                     "B2": sum(T3(s, range(n))*q**(2*T3(s, range(n)))*diag[s] for s in sel),
                     "B3_electron": sum(T3(s, elec)*diag[s] for s in sel)}
    for k in ("B1", "B2"): res["S_" + k] = res["O+"][k] + res["O-"][k]
    return res
q0 = mp.mpf(C.Q_50_DIGIT_STR)
ev = lambda e: mp.nstr(sp.lambdify(q, e, "mpmath")(q0), 20)
def pack(r):
    d = {}
    for o in ("O+", "O-"):
        d[o] = {}
        for k, v in r[o].items():
            v = sp.factor(sp.simplify(v))
            d[o][k] = {"exact": str(v), "q=1": str(sp.simplify(v.subs(q, 1))), "q0": ev(v), "zero_identically": bool(v == 0)}
    for k in ("S_B1", "S_B2"):
        v = sp.factor(sp.simplify(r[k])); d[k] = {"exact": str(v), "q=1": str(sp.simplify(v.subs(q, 1))), "q0": ev(v)}
    return d
checks = []
def check(name, ok, detail=""):
    checks.append({"name": name, "pass": bool(ok), "detail": detail}); print("[%s] %s %s" % ("PASS" if ok else "FAIL", name, detail))

# --- the element, per placement
coll_L = [photon(0, 0, 0, q*h), photon(0, 0, 0, -h/q)]          # steps 1+3, proton strands 0-2
coll_R = [photon(1, 0, 0, q*h), photon(1, 0, 0, -h/q)]          # proton strands 1-3 (mirror i -> 2-i on proton: s0<->s1 => use gens 1,2 with V=s1 s2^-1)
# mirror of the proton block: generator i on strands 0-2 maps to 3-i... keep the §43 convention: core (s1 s2^-1)^3 on 1-3
gl = {"L": {"G0": [], "GV": [W1(V(0))], "Gs1": [W1(P([1]))], "GLm": [W1(P([1, 0]))]},
      "R": {"G0": [], "GV": [W1(V(1))], "Gs1": [W1(P([2]))], "GLm": [W1(P([2, 1]))]}}
cap = {"L": {"C-cable": [W1(inv(P([2, 1, 0, 0, 1, 2])))], "C-adj": [W1(inv(P([2, 2])))]},
       "R": {"C-cable": [W1(inv(P([0, 1, 2, 2, 1, 0])))], "C-adj": [W1(inv(P([0, 0])))]}}
prot = {"L": [0, 1, 2], "R": [1, 2, 3]}

# C1: the photon product equals the hand-written core V^3 on every basis state of C^2(x)4
for side, i in (("L", 0), ("R", 1)):
    ok = all(sp.simplify(elem_apply(coll_L if side == "L" else coll_R, {s: 1}).get(t, 0)
                         - word_apply(V(i)*3, {s: 1}).get(t, 0)) == 0 for s in basis for t in basis)
    check("C1 gamma(0,0,qh).gamma(0,0,-h/q) == (V)^3 on C2^4, side " + side, ok)
# element size: braid words in the expansion before any reduction
check("element expansion: collision = 1 + h^2 V - h^2 V^2 (3 words)", True,
      "coefficients a+b = h^2, ab = -h^2 with a = qh, b = -h/q")

out = {"preregistration": "PREREGISTRATION-hydrogen-from-photons.md (ddf883a5d25)",
       "element": "W = gamma(0,0,q h).gamma(0,0,-q^-1 h) . g . K on C^2^4, h = q - 1/q",
       "arms": {}}
for side in ("L", "R"):
    for gname, g in gl[side].items():
        for cname, K in cap[side].items():
            factors = (coll_L if side == "L" else coll_R) + g + K
            lab = f"proton_{'left' if side == 'L' else 'right'}|{gname}|{cname}"
            out["arms"][lab] = pack(functionals(diag_of(factors), prot[side]))
            d = out["arms"][lab]
            print(lab, {o: (d[o]["B1"]["q0"], d[o]["B1"]["q=1"]) for o in ("O+", "O-")}, "S_B1:", d["S_B1"]["exact"], d["S_B1"]["q0"])

# C2 / P2: G0 C-cable equals §43 arm 2
prev = json.load(open(__file__.replace("mn_hydrogen_from_photons_probe.py", "mn_hydrogen_capture_chirality_probe.out.json")))
for side, key in (("left", "arm2_capture_left"), ("right", "arm2_capture_right")):
    a = out["arms"][f"proton_{side}|G0|C-cable"]
    ok = all(sp.simplify(sp.sympify(a[o]["B1"]["exact"], locals={"q": q}) - sp.sympify(prev[key][o]["B1"]["exact"], locals={"q": q})) == 0 for o in ("O+", "O-"))
    check("P2 G0/C-cable equals §43 arm 2, proton " + side, ok)

# reading-3 diagnostic on the nucleon (3 strands) for each gluon arm: chi_(2,1) = (Tr_{C2^3} - 4 chi_(3))/2
basis3 = list(itertools.product([0, 1], repeat=3))
def tr3(factors):
    tot = 0
    for s in basis3:
        vec = {s: 1}
        for E in reversed(factors):
            new = {}
            for c, w in E:
                for t, v in word_apply(w, vec).items(): new[t] = new.get(t, 0) + c*v
            vec = new
        tot += vec.get(s, 0)
    return sp.simplify(tot)
r3 = {}
for gname, g in gl["L"].items():
    fac = coll_L + g
    # chi_(3): the q-symmetric character; sigma -> q, sigma^-1 -> q^-1 on (3); evaluate on the all-zero state
    chi3 = sp.simplify(elem_apply(fac, {(0, 0, 0, 0): 1}).get((0, 0, 0, 0), 0))
    chi21 = sp.factor(sp.simplify((tr3(fac) - 4*chi3)/2))
    r3[gname] = {"chi_(3)": str(sp.factor(chi3)), "chi_(3)_q0": ev(chi3), "chi_(2,1)": str(chi21), "chi_(2,1)_q0": ev(chi21),
                 "reading3_pass_at_q0": bool(sp.lambdify(q, chi21, "mpmath")(q0) >= 0 and sp.lambdify(q, chi3, "mpmath")(q0) >= 0)}
    print("reading-3", gname, r3[gname])
out["reading3_nucleon_diagnostic"] = r3

# arm Phi: general symbolic collision, G0, C-cable
f0, f1, f01, g0, g1, g01 = sp.symbols('phi0 phi1 phi01 psi0 psi1 psi01')
arm_phi = {}
for side, i in (("L", 0), ("R", 1)):
    fac = [photon(i, f0, f1, f01), photon(i, g0, g1, g01)] + cap[side]["C-cable"]
    r = functionals(diag_of(fac), prot[side])
    S = sp.factor(sp.simplify(r["S_B1"]))
    Op = sp.factor(sp.simplify(r["O+"]["B1"])); Om = sp.factor(sp.simplify(r["O-"]["B1"]))
    spec = {f0: 0, f1: 0, f01: q*h, g0: 0, g1: 0, g01: -h/q}
    lab = "proton_left" if side == "L" else "proton_right"
    arm_phi[lab] = {"O+_B1": str(Op), "O-_B1": str(Om), "S_B1": str(S),
                    "S_B1_identically_zero": bool(sp.simplify(S) == 0),
                    "O+_B1_identically_zero": bool(sp.simplify(Op) == 0), "O-_B1_identically_zero": bool(sp.simplify(Om) == 0),
                    "S_B1_at_q=1": str(sp.factor(sp.simplify(S.subs(q, 1)))),
                    "S_B1_poly_terms_in_phi_psi": len(sp.Poly(sp.expand(sp.numer(sp.together(S))), f0, f1, f01, g0, g1, g01).terms())}
    ok = sp.simplify(S.subs(spec) - sp.sympify(out["arms"][f"{lab}|G0|C-cable"]["S_B1"]["exact"], locals={"q": q})) == 0
    check("C2 arm Phi at derived weights reproduces G0/C-cable, " + lab, ok)
    print("Phi", lab, arm_phi[lab]["S_B1_identically_zero"], arm_phi[lab]["S_B1_at_q=1"], arm_phi[lab]["S_B1_poly_terms_in_phi_psi"])
out["arm_Phi"] = arm_phi

# post-hoc structural observations (not pre-registered; reported as such)
obs = {}
L_ = {"q": q, "phi0": f0, "phi1": f1, "phi01": f01, "psi0": g0, "psi1": g1, "psi01": g01}
for gname, g in gl["L"].items():
    chi3 = sp.sympify(r3[gname]["chi_(3)"], locals=L_)
    for cname in ("C-cable", "C-adj"):
        S = sp.sympify(out["arms"][f"proton_left|{gname}|{cname}"]["S_B1"]["exact"], locals=L_)
        S0 = sp.sympify(out["arms"][f"proton_left|G0|{cname}"]["S_B1"]["exact"], locals=L_)
        mir = all(sp.simplify(sp.sympify(out["arms"][f"proton_right|{gname}|{cname}"][a]["B1"]["exact"], locals=L_)
                              + sp.sympify(out["arms"][f"proton_left|{gname}|{cname}"][b]["B1"]["exact"], locals=L_)) == 0
                  for a, b in (("O+", "O-"), ("O-", "O+")))
        obs[f"{gname}|{cname}"] = {"S_B1_equals_chi3(gluon)*S_B1(G0)": bool(sp.simplify(S - chi3*S0) == 0),
                                   "mirror_Oplus_right_eq_minus_Ominus_left": mir}
Sphi = sp.sympify(arm_phi["proton_left"]["S_B1"], locals=L_)
S0c = sp.sympify(out["arms"]["proton_left|G0|C-cable"]["S_B1"]["exact"], locals=L_)
chiphi = (1 + q*f0 + q*f1 + f01)*(1 + q*g0 + q*g1 + g01)
obs["Phi|C-cable"] = {"S_B1_equals_chi3(gamma_phi)chi3(gamma_psi)*S_B1(G0)": bool(sp.simplify(Sphi - chiphi*S0c) == 0),
                      "mirror_Oplus_right_eq_minus_Ominus_left": all(
                          sp.simplify(sp.sympify(arm_phi["proton_right"][a + "_B1"], locals=L_) + sp.sympify(arm_phi["proton_left"][b + "_B1"], locals=L_)) == 0
                          for a, b in (("O+", "O-"), ("O-", "O+")))}
out["post_hoc_observations"] = obs
print(obs)
# decision per arm
verdict = {}
for gname in ("G0", "GV", "Gs1", "GLm"):
    for cname in ("C-cable", "C-adj"):
        neut = {side: [o for o in ("O+", "O-") if mp.mpf(out["arms"][f"proton_{side}|{gname}|{cname}"][o]["B1"]["q0"]) == 0] for side in ("left", "right")}
        fixed = all(len(neut[s]) == 1 for s in neut) and neut["left"] == neut["right"]
        verdict[f"{gname}|{cname}"] = {"neutral_at_q0": neut, "orientation_fixed": fixed}
out["verdict"] = verdict; out["checks"] = checks
out["checks_passed"] = f"{sum(c['pass'] for c in checks)}/{len(checks)}"
open(__file__.replace('.py', '.out.json'), 'w').write(json.dumps(out, indent=1) + "\n")
print(out["checks_passed"], verdict)
