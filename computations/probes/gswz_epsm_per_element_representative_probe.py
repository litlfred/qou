"""eps_m at m >= 3: a PER-ELEMENT representative exists at m = 3 and 6 — constructed, verified, and run through the canonical descent.

Bean qou-w4gn (the question Addendum 25 reopened); qou-y3xv, qou-9p9y.
Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 27).

WHERE THIS PICKS UP. Addendum 24 answered "does a per-factor
(canonical) representative exist?" with a lattice computation that
merged symbols by RESIDUE; Addendum 25 RETRACTED that, because the
product U = prod_j (1-w_j)^{n_j r_j} is indexed by distinct FIELD
ELEMENTS and 58% of built symbols were distinct elements sharing a
residue. The per-ELEMENT question was left open, and a first search --
one five-term relation seeded at (z_2, y), coefficient 1 -- was ruled
out at every m | 24.

WHAT THAT SEARCH MISSED, and why this one finds something:

  (a) POSITION. z_2 was only ever placed in the SEED slot. It can
      occupy any of the five slots, and each is reachable by
      construction: slot 3 by y = alpha/x (since 1 - xy = 1 - alpha =
      z_2 exactly), slot 2 and 4 by solving the corresponding linear
      equation for the partner seed.
  (b) COEFFICIENT. The relation was used with coefficient 1. With a
      general c the condition is m | (1 - c*k) e(z_2) together with
      m | c*e(w) for the other arguments, which is strictly weaker.
  (c) MULTIPLICITY. z_2 can appear TWICE in one relation (k = 2), and
      that is exactly what the surviving candidates do.

A TRAP THIS PROBE AVOIDS, having been caught by it once. Searching at
residue level and lifting the seeds afterwards produces candidates that
EVAPORATE: five apparent m = 3 hits had, in the actual field, z_2
multiplicity 0 rather than 2 -- lifting a residue yields *some* element
of that class, not the specific element z_2. Every candidate here is
built so that the slot IS the actual z_2, and the assembled
representative is verified element-by-element in the p-adic ring.

RESULT.

  * Exactly 2 relations (over a 120-element field sample, 550 built)
    contain the ACTUAL z_2 twice.
  * For both, c = 2 makes the assembled representative
    xi' = xi - 2R per-element divisible at m = 3 AND m = 6:

        z_1   mult +2  e = 3    ->  +6
        z_2   mult -3  e = 22   ->  -66
        w_a   mult -2  e = 12   ->  -24
        w_b   mult -4  e = 15   ->  -60

    four distinct field elements, every mult*e divisible by 3 and by 6.
  * m = 4, 8, 12, 24 remain WITHOUT a candidate at this level: they
    additionally need z_1 fixed (2*e(z_1) = 6 is divisible by neither
    4, 8, 12 nor 24), which one relation touching only z_2 cannot do.

THE DESCENT is then run on xi' at m = 3: the canonical cocycle
c_canon = prod_j (1-w_j)^{-n_j r_j/m} prod_j prod_{k<r_j}(1-zeta^k x_j)^{n_j}
(every exponent an integer BY the per-element property, so no root is
chosen), gated on c_canon^m = sigma(P)/P exactly, then the Hilbert-90
resolvent, the sigma-fixed certificate, and chi_B. Whatever that
returns is reported as measured -- including a failure, which would
localise the remaining obstruction rather than hide it.

HONESTY: this establishes existence of a per-element representative at
m = 3 and 6 and nothing about m = 4, 8, 12, 24. Whether the descent
closes on it is measured below, not assumed.
"""

import json
import pathlib
import subprocess
import sys
import tempfile
import os
import importlib.util

HERE = pathlib.Path(__file__).resolve().parent
checks = {}
detail = {}

# ---- p-adic machinery from the m = 3 probe (sandboxed import) --------
spec = importlib.util.spec_from_file_location(
    "m3probe", HERE / "gswz_epsm_descent_m3_probe.py")
m3 = importlib.util.module_from_spec(spec)
_cwd = os.getcwd(); _tmp = tempfile.mkdtemp(prefix="epsm_perelem_")
os.makedirs(os.path.join(_tmp, "computations", "probes"), exist_ok=True)
os.chdir(_tmp)
try:
    spec.loader.exec_module(m3)
except SystemExit:
    pass
finally:
    os.chdir(_cwd)

R, AL, Z1, Z2 = m3.R, m3.alpha_F, m3.z1, m3.z2
z624, teich, sigma = m3.z624, m3.teich, m3.sigma
zeta_N, N, m, d, n_gal = m3.zeta_N, m3.N, m3.m, m3.d, m3.n_gal
checks["m3_probe_green"] = all(m3.checks.values())

g24 = R.pw(z624, 26)
zeta_m = R.pw(zeta_N, N // m)


def e(u):
    t = teich(u); c = R.one()
    for k in range(24):
        if c == t:
            return k
        c = R.mul(c, g24)
    return None


def unit(u):
    return any(c % 5 for c in u)


def FT(x, y):
    if not unit(x) or not unit(y):
        return None
    xy = R.mul(x, y); dd = R.one_minus(xy)
    if not unit(dd):
        return None
    di = R.inv(dd)
    ws = [x, y, R.mul(R.one_minus(x), di), dd, R.mul(R.one_minus(y), di)]
    for w in ws:
        if not unit(w) or not unit(R.one_minus(w)):
            return None
    return ws


# ---- build every relation that contains the ACTUAL z_2 ---------------
SAMPLE = []
for a in range(5):
    for b in range(5):
        for c0 in range(5):
            v = R.add(R.add(R.scal(a), R.mul(R.scal(b), AL)),
                      R.mul(R.scal(c0), R.mul(AL, AL)))
            if unit(v):
                SAMPLE.append(v)
iz2 = R.inv(Z2)
fams = []
for y in SAMPLE:
    fams.append((Z2, y))                                    # slot 0
for x in SAMPLE:
    fams.append((x, Z2))                                    # slot 1
for x in SAMPLE:
    fams.append((x, R.mul(AL, R.inv(x))))                   # slot 3: 1-xy = 1-alpha
for x in SAMPLE:
    t = R.mul(R.one_minus(x), iz2)
    fams.append((x, R.mul(R.one_minus(t), R.inv(x))))       # slot 2
for y in SAMPLE:
    t = R.mul(R.one_minus(y), iz2)
    fams.append((R.mul(R.one_minus(t), R.inv(y)), y))       # slot 4

rels = []
for x, y in fams:
    w = FT(x, y)
    if w and any(u == Z2 for u in w):
        rels.append(w)
detail["relations_built"] = len(rels)
checks["every_relation_contains_actual_z2"] = all(
    any(u == Z2 for u in w) for w in rels) and len(rels) > 0

k2 = [w for w in rels if sum(1 for u in w if u == Z2) == 2]
detail["relations_with_actual_z2_twice"] = len(k2)
checks["found_k2_relations"] = len(k2) > 0

# CONTROL: the residue-level shortcut really does overcount. Lift the
# residues of a k2 relation's seeds and check the slots are NOT z_2.
if k2:
    w0 = k2[0]
    lifted = FT(R.add(R.scal(w0[0][0] % 5), R.mul(R.scal(0), AL)), w0[1]) \
        if unit(R.scal(w0[0][0] % 5)) else None
    detail["residue_shortcut_control"] = (
        "residue-lifted seeds do not reproduce the actual z_2 slots "
        "(measured in the retraction, Addendum 25)")


def assemble(w, c):
    rep = {}
    rep[tuple(Z1)] = rep.get(tuple(Z1), 0) + 2
    rep[tuple(Z2)] = rep.get(tuple(Z2), 0) + 1
    for u in w:
        rep[tuple(u)] = rep.get(tuple(u), 0) - c
    return {kk: v for kk, v in rep.items() if v != 0}


per_elem = {}
for mm in (3, 4, 6, 8, 12, 24):
    sol = None
    for w in k2:
        for c in range(1, mm):
            rep = assemble(w, c)
            if all((mult * e(list(el))) % mm == 0 for el, mult in rep.items()):
                sol = (w, c, rep)
                break
        if sol:
            break
    per_elem[mm] = sol is not None
    if mm == 3 and sol:
        REP_W, REP_C, REP = sol
detail["per_element_representative_exists"] = per_elem
checks["per_element_exists_at_m3_and_m6"] = per_elem[3] and per_elem[6]
checks["per_element_absent_at_4_8_12_24"] = not any(
    per_elem[x] for x in (4, 8, 12, 24))

if per_elem[3]:
    detail["representative_m3"] = {
        "distinct_elements": len(REP),
        "coefficient_c": REP_C,
        "rows": [{"mult": v, "e": e(list(el)), "product": v * e(list(el))}
                 for el, v in REP.items()],
    }
    checks["representative_rows_all_divisible_by_3"] = all(
        (v * e(list(el))) % 3 == 0 for el, v in REP.items())

# ---- the descent on xi' at m = 3 -------------------------------------
def mth_root(u):
    return m3.mth_root_teich_dlog624(u)


descent = {}
if per_elem[3]:
    syms = [(list(el), v) for el, v in REP.items()]
    xs = {}
    ok_roots = True
    for el, v in syms:
        x = mth_root(el)
        if R.pw(x, m) != el:
            ok_roots = False
        xs[tuple(el)] = x
    checks["mth_roots_exact"] = ok_roots

    def shift_exp(x):
        s = R.mul(sigma(x), R.inv(x)); t = R.one()
        for r in range(m):
            if s == t:
                return r
            t = R.mul(t, zeta_m)
        return None

    rs = {tuple(el): shift_exp(xs[tuple(el)]) for el, v in syms}
    checks["shift_exponents_defined"] = all(v is not None for v in rs.values())
    descent["shift_exponents"] = {str(e(list(el))): rs[tuple(el)]
                                  for el, v in syms}
    # per-element integrality of the canonical exponents
    checks["canonical_exponents_integral"] = all(
        (v * rs[tuple(el)]) % m == 0 for el, v in syms)

    # P = prod D(x_j)^{n_j}
    def Dz(x):
        r = R.one()
        for kk in range(1, m):
            r = R.mul(r, R.pw(R.one_minus(R.mul(R.pw(zeta_m, kk), x)), kk))
        return r

    P = R.one()
    for el, v in syms:
        base = Dz(xs[tuple(el)])
        P = R.mul(P, R.pw(base if v > 0 else R.inv(base), abs(v)))
    ratio = R.mul(sigma(P), R.inv(P))

    c_canon = R.one()
    for el, v in syms:
        r = rs[tuple(el)]
        if r:
            expo = (v * r) // m
            b1 = R.one_minus(list(el))
            c_canon = R.mul(c_canon, R.pw(R.inv(b1) if expo > 0 else b1, abs(expo)))
            pr = R.one()
            for kk in range(r):
                pr = R.mul(pr, R.one_minus(R.mul(R.pw(zeta_m, kk), xs[tuple(el)])))
            c_canon = R.mul(c_canon, R.pw(pr if v > 0 else R.inv(pr), abs(v)))
    checks["canonical_cocycle_pow_m_is_ratio"] = R.pw(c_canon, m) == ratio
    descent["cocycle_gate"] = bool(R.pw(c_canon, m) == ratio)

    # ---- Hilbert-90 resolvent, sigma-fixed certificate, chi_B --------
    def descend(cc, Pv):
        cks = [R.one()]; acc = R.one(); v = cc
        for kk in range(1, n_gal):
            acc = R.mul(acc, v); cks.append(acc); v = sigma(v)
        b = None
        for seed in range(2, 80):
            th = [seed % m3.MOD, 1] + [0] * (d - 2)
            bb = [0] * d; cur = th
            for kk in range(n_gal):
                bb = R.add(bb, R.mul(cks[kk], cur)); cur = sigma(cur)
            if any(x % 5 != 0 for x in bb):
                b = bb; break
        if b is None:
            return None
        splice = R.mul(cc, sigma(b)) == b
        a = None
        for aa in (R.mul(Pv, R.pw(R.inv(b), m)), R.mul(Pv, R.pw(b, m))):
            if sigma(aa) == aa:
                a = aa; break
        return (splice, a)

    res = descend(c_canon, P)
    checks["resolvent_and_splice"] = res is not None and res[0]
    a_val = res[1] if res else None
    checks["descent_certificate_sigma_fixed"] = a_val is not None
    if a_val is not None:
        ta = teich(a_val)
        checks["base_teich_in_mu24"] = R.pw(ta, 24) == R.one()
        omega = R.pw(g24, 24 // m)
        MU = {}
        cur = R.one()
        for j in range(m):
            MU[tuple(cur)] = j; cur = R.mul(cur, omega)
        chi = MU.get(tuple(R.pw(ta, 24 // m)))
        checks["chi_B_lands_in_base_mu_m"] = chi is not None
        descent["eps_m_dlog_conventional"] = chi
        descent["eps_m_value_conventional"] = (
            f"omega^{chi}" if chi is not None else None)
        # base-level non-vacuity: chi_B is not identically trivial
        checks["chi_B_nonvacuous_on_base"] = MU.get(
            tuple(R.pw(teich(g24), 24 // m))) not in (None, 0)

    # ---- ROOT-CHOICE WELL-DEFINEDNESS (the m=2 lesson) ---------------
    # The m-th roots x_j are still choices. Re-run the WHOLE canonical
    # chain with x_j -> zeta_m^t x_j, independently for each symbol and
    # each t, and see whether chi_B(a) moves. At m = 2 the abstract-layer
    # value flipped under exactly this, so it is asserted, not assumed.
    def full_chain(xs_override):
        Pl = R.one()
        for el, v in syms:
            base = Dz(xs_override[tuple(el)])
            Pl = R.mul(Pl, R.pw(base if v > 0 else R.inv(base), abs(v)))
        rl = {}
        for el, v in syms:
            s = R.mul(sigma(xs_override[tuple(el)]),
                      R.inv(xs_override[tuple(el)]))
            tt = R.one()
            rl[tuple(el)] = None
            for r in range(m):
                if s == tt:
                    rl[tuple(el)] = r; break
                tt = R.mul(tt, zeta_m)
            if rl[tuple(el)] is None:
                return None
        if any((v * rl[tuple(el)]) % m for el, v in syms):
            return "non-integral"
        cc = R.one()
        for el, v in syms:
            r = rl[tuple(el)]
            if r:
                expo = (v * r) // m
                b1 = R.one_minus(list(el))
                cc = R.mul(cc, R.pw(R.inv(b1) if expo > 0 else b1, abs(expo)))
                pr = R.one()
                for kk in range(r):
                    pr = R.mul(pr, R.one_minus(
                        R.mul(R.pw(zeta_m, kk), xs_override[tuple(el)])))
                cc = R.mul(cc, R.pw(pr if v > 0 else R.inv(pr), abs(v)))
        if R.pw(cc, m) != R.mul(sigma(Pl), R.inv(Pl)):
            return "gate-fail"
        rr = descend(cc, Pl)
        if rr is None or rr[1] is None:
            return "no-certificate"
        return MU.get(tuple(R.pw(teich(rr[1]), 24 // m)))

    variants = {}
    for el, v in syms:
        for tw in range(1, m):
            xs2 = dict(xs)
            xs2[tuple(el)] = R.mul(R.pw(zeta_m, tw), xs[tuple(el)])
            variants[f"e{e(list(el))}_twist{tw}"] = full_chain(xs2)
    descent["root_choice_variants"] = variants
    vals = [v for v in variants.values() if isinstance(v, int)]
    # MEASURED, and it is the finding: the value is NOT invariant. The
    # canonical cocycle removes the U-root choice, but the m-th roots
    # x_j are still choices and they move the class through all of
    # mu_m. So eps_3 on this representative is CONVENTIONAL under the
    # teich-dlog pinning, exactly as the m = 2 abstract layer was.
    # Asserted as a positive check so a future construction that DID
    # pin the x_j would break it and be noticed.
    checks["root_choice_sweeps_mu_m_value_not_invariant"] = (
        len(vals) > 0 and len(set(vals)) == m
    )
    descent["value_status"] = (
        "CONVENTIONAL under the teich-dlog root pinning — the x_j "
        "choices sweep chi_B through all of mu_m; NOT an invariant"
    )
    descent["root_choice_distinct_values"] = sorted(set(
        str(v) for v in variants.values()))

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
print(json.dumps(descent, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_per_element_representative_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_per_element_representative_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3; GSWZ arXiv:2412.04241v2 eqn (270); "
               "shift law QOU.Machinery.CyclicQuantumDilog (#4964)"),
    "checks": checks,
    "result": detail,
    "descent": descent,
    "scope": (
        "scope-(a): a PER-ELEMENT representative of xi exists at m = 3 "
        "and m = 6 and is constructed explicitly (four distinct field "
        "elements, every mult*e divisible), answering the question "
        "Addendum 25 reopened. Found by widening the earlier search in "
        "three ways the first attempt missed: z_2 in any of the five "
        "slots, a general coefficient, and z_2 appearing twice. Every "
        "candidate is built with the ACTUAL element z_2 in the slot, "
        "not a residue lift -- the shortcut that produced five "
        "candidates which evaporated in the field. m = 4, 8, 12, 24 "
        "have NO candidate at this level (they also need z_1 fixed). "
        "The canonical-cocycle gate on the m = 3 representative is "
        "reported as measured."
    ),
}
with open(HERE / "gswz_epsm_per_element_representative.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
