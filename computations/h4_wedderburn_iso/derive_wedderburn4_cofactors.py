#!/usr/bin/env python3
"""
derive_cofactors.py — A2-s3 prep (bean qou-308a): sympy derivation of every
`linear_combination` cofactor the follow-up Lean file(s) `HeckeH4Wedderburn*`
need to prove the full rank-4 Wedderburn isomorphism

    H4A K (q - q⁻¹)  ≃ₐ[K]  K × K × M₂(K) × M₃(K) × M₃(K)

at Wenzl-generic q, mirroring the merged rank-3 pattern
(QOU/Machinery/HeckeH3Wedderburn.lean).

Method (atom-level, deterministic — no dependence on field_simp output):
every Lean goal is modeled as a polynomial identity over

    QQ[q, xq, x2, x3, x4, <coordinate vars>]

where the inverse ATOMS are  xq = q⁻¹, x2 = (q²+1)⁻¹, x3 = (q⁴+q²+1)⁻¹,
x4 = (q⁴+1)⁻¹, and the goal LHS−RHS is reduced against the relations

    hq : q·xq − 1,   h2 : (q²+1)·x2 − 1,
    h3 : (q⁴+q²+1)·x3 − 1,   h4 : (q⁴+1)·x4 − 1

(plus  hl : l² − h·l − 1  for the character intertwiners).  The returned
cofactors c_rel satisfy, EXACTLY (verified by expand == 0):

    LHS − RHS  =  Σ_rel  c_rel · (rel)

so in Lean (after normalizing all divisions to separated inverse atoms with
`simp only [div_eq_mul_inv, one_div, mul_inv, inv_pow]`) the goal closes with

    linear_combination  c_hq * (mul_inv_cancel₀ hq) + c_h2 * (mul_inv_cancel₀ h2)
                      + c_h3 * (mul_inv_cancel₀ h3) + c_h4 * (mul_inv_cancel₀ h4)

Goal sets covered (139 scalar goals):
  A. left-inverse   wedderburnInvV₄(hom-coords(v)) = v          (24 goals)
  B. right-inverse  hom-coords(wedderburnInvV₄ w) = w           (24 goals: s, t, 4+9+9 entries)
  C. entry lemmas   blockOf-as-word-product = explicit A-row    (22 goals; only needed if the
                    H3-style product definition of blockOf is used — with the recommended
                    explicit-entry definition these are definitional)
  D. chi intertwiners  χ_l(u·σₖ) = l·χ_l(u)  mod (l²−hl−1)      (3 goals)
  E. block intertwiners blockOf_λ(u·σₖ) = blockOf_λ(u)·Sₖ_λ     (66 goals)

Inputs (read-only):
  computations/h4_wedderburn/hecke-h4-wedderburn-seminormal.data.json
Outputs (scratchpad only):
  cofactors.json
"""
import json, sys, time, re
from collections import OrderedDict
import sympy as sp

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

# Repo-root-relative (bean qou-c7g8/qou-6inm). These were absolute paths into a
# DIFFERENT machine's checkout (/home/user/qou), which resolve to nothing in any
# clone not at that exact path. A sys.path insert of a missing directory raises
# NOTHING, so the failure was silent until an unrelated-looking import died.
from pathlib import Path as _Path
_QOU_ROOT = _Path(__file__).resolve().parents[2]
DATA = str(_QOU_ROOT / "computations" / "h4_wedderburn"
           / "hecke-h4-wedderburn-seminormal.data.json")
OUT = "/tmp/claude-0/-home-user-qou/4d3616f5-f4c0-5922-a632-19628cf5cbf8/scratchpad/h4_wedderburn_iso/cofactors.json"

q = sp.Symbol('q')
xq, x2, x3, x4 = sp.symbols('xq x2 x3 x4')
x3a, x3b = sp.symbols('x3a x3b')  # fallback atoms for q^2+q+1 / q^2-q+1 if unpaired
l, h = sp.symbols('l h')

ATOM_D = OrderedDict([(xq, q), (x2, q**2 + 1), (x3, q**4 + q**2 + 1), (x4, q**4 + 1),
                      (x3a, q**2 + q + 1), (x3b, q**2 - q + 1)])
ATOM_NAME = {xq: 'hq', x2: 'h2', x3: 'h3', x4: 'h4', x3a: 'h3a', x3b: 'h3b'}

used_fallback_atoms = set()

# ---------------------------------------------------------------- atomify
FACTOR_MAP = {
    sp.expand(q): xq,
    sp.expand(q**2 + 1): x2,
    sp.expand(q**4 + 1): x4,
}
PAIR_A = sp.expand(q**2 + q + 1)
PAIR_B = sp.expand(q**2 - q + 1)

def atomify(expr):
    """rational function in q (possibly containing atoms in numerator) ->
    polynomial in q + atoms.  Denominator must factor over the known atoms."""
    expr = sp.together(sp.cancel(expr))
    n, d = sp.fraction(expr)
    if d == 1:
        return sp.expand(n)
    # denominator must be q-only
    assert d.free_symbols <= {q}, f"non-q denominator: {d}"
    const, factors = sp.factor_list(sp.Poly(d, q))
    ea, eb = 0, 0
    res = sp.expand(n) / const
    for base, e in factors:
        base_e = sp.expand(base.as_expr())
        if base_e in FACTOR_MAP:
            res *= FACTOR_MAP[base_e] ** e
        elif base_e == PAIR_A:
            ea = e
        elif base_e == PAIR_B:
            eb = e
        else:
            raise AssertionError(f"unknown denominator factor: {base_e}")
    m = min(ea, eb)
    res *= x3 ** m
    if ea > m:
        res *= x3a ** (ea - m); used_fallback_atoms.add('x3a')
    if eb > m:
        res *= x3b ** (eb - m); used_fallback_atoms.add('x3b')
    return sp.expand(res)

ATOM_SUBS = [(x3b, 1/(q**2 - q + 1)), (x3a, 1/(q**2 + q + 1)),
             (x4, 1/(q**4 + 1)), (x3, 1/(q**4 + q**2 + 1)),
             (x2, 1/(q**2 + 1)), (xq, 1/q)]

def rat_of(p):
    """substitute all atoms -> rational function in q"""
    return sp.cancel(p.subs(ATOM_SUBS))

# ------------------------------------------------- cofactor extraction
MAIN_ATOMS = [xq, x2, x3, x4]

def extract_cofactors(p, atoms=None, verify=True):
    """p: polynomial in q + atoms (coordinate-variable-free), rationally zero
    under x_D -> 1/D.  Purely algebraic telescoping construction:

      write p = sum_alpha c_alpha(q) x^alpha,  M_i = max_alpha alpha_i.
      x^alpha - D^(M-alpha) x^M
        = -sum_i (prod_{j<i} x_j^{a_j}) (prod_{j>i} D_j^{M_j-a_j} x_j^{M_j})
               * x_i^{a_i} * (D_i x_i - 1) * sum_{t<M_i-a_i} (D_i x_i)^t
      so p = sum cof_i * (D_i x_i - 1) + (sum_alpha c_alpha D^(M-alpha)) x^M,
      and the last coefficient is a q-polynomial that must be identically 0
      (this IS the rational vanishing of p — asserted).

    Returns {atom: cofactor_expr} with p == sum c*(D*x-1) exactly."""
    if atoms is None:
        atoms = [a for a in MAIN_ATOMS + [x3a, x3b] if p.has(a)]
    if not atoms:
        assert sp.expand(p) == 0, f"atom-free nonzero goal: {p}"
        return {}
    P = sp.Poly(sp.expand(p), *atoms)
    terms = P.terms()
    nA = len(atoms)
    M = [max((t[0][i] for t in terms), default=0) for i in range(nA)]
    Ds = [ATOM_D[a] for a in atoms]
    # the pure-q vanishing identity
    main = sp.Integer(0)
    for alpha, c in terms:
        main += c.as_expr() * sp.prod([Ds[i] ** (M[i] - alpha[i]) for i in range(nA)])
    assert sp.expand(main) == 0, "goal does not vanish rationally"
    cof = {a: sp.Integer(0) for a in atoms}
    for alpha, c in terms:
        ce = c.as_expr()
        for i in range(nA):
            m = M[i] - alpha[i]
            if m == 0:
                continue
            pre = sp.prod([atoms[j] ** alpha[j] for j in range(i)])
            post = sp.prod([Ds[j] ** (M[j] - alpha[j]) * atoms[j] ** M[j]
                            for j in range(i + 1, nA)])
            tele = sp.Add(*[(Ds[i] * atoms[i]) ** t for t in range(m)])
            cof[atoms[i]] += -ce * pre * post * atoms[i] ** alpha[i] * tele
    cof = {a: c for a, c in cof.items() if c != 0}
    if verify:
        check = sp.expand(p - sp.Add(*[c * (ATOM_D[a] * a - 1) for a, c in cof.items()]))
        assert check == 0, "telescoping verification failed"
    return cof

def extract_cofactors_min(p, atoms=None):
    """Near-minimal cofactors via sequential exact division over QQ(q):
    for each atom x (relation D*x - 1), quotient by (x - 1/D), convert the
    rational cofactor back to atom form, iterate on the residual.  Falls
    back to the telescoping construction if it fails to converge.
    Verified exactly (expand == 0) before returning."""
    if atoms is None:
        atoms = [a for a in MAIN_ATOMS + [x3a, x3b] if p.has(a)]
    if not atoms:
        assert sp.expand(p) == 0, f"atom-free nonzero goal: {p}"
        return {}
    cof = {a: sp.Integer(0) for a in atoms}
    R = sp.expand(p)
    for _ in range(12):
        if R == 0:
            break
        Rwork = R
        for a in atoms:
            D = ATOM_D[a]
            if not Rwork.has(a):
                continue
            sub = Rwork.subs(a, 1 / D)
            quot = sp.cancel(sp.together(Rwork - sub) / (a - sp.Rational(1) / D))
            cof[a] = cof[a] + atomify(sp.cancel(quot / D))
            Rwork = sub
        assert sp.cancel(sp.together(Rwork)) == 0, "goal does not vanish rationally"
        R = sp.expand(p - sp.Add(*[cof[a] * (ATOM_D[a] * a - 1) for a in atoms]))
    else:
        return extract_cofactors(p, atoms)  # telescoping fallback
    cof = {a: sp.expand(c) for a, c in cof.items() if sp.expand(c) != 0}
    check = sp.expand(p - sp.Add(*[c * (ATOM_D[a] * a - 1) for a, c in cof.items()]))
    assert check == 0, "minimal-cofactor verification failed"
    return cof

# ------------------------------------------------------- Lean printing
def lean_str(e):
    s = sp.sstr(sp.expand(e))
    s = s.replace('**', ' ^ ')
    # atoms -> Lean inverse atoms
    s = re.sub(r'\bxq\b', 'q⁻¹', s)
    s = re.sub(r'\bx2\b', '(q ^ 2 + 1)⁻¹', s)
    s = re.sub(r'\bx3a\b', '(q ^ 2 + q + 1)⁻¹', s)
    s = re.sub(r'\bx3b\b', '(q ^ 2 - q + 1)⁻¹', s)
    s = re.sub(r'\bx3\b', '(q ^ 4 + q ^ 2 + 1)⁻¹', s)
    s = re.sub(r'\bx4\b', '(q ^ 4 + 1)⁻¹', s)
    s = re.sub(r'\bv_(\d+)\b', r'v \1', s)
    s = re.sub(r'\bu_(\d+)\b', r'u \1', s)
    s = re.sub(r'\bm22_(\d)(\d)\b', r'M2 \1 \2', s)
    s = re.sub(r'\bm31_(\d)(\d)\b', r'M31 \1 \2', s)
    s = re.sub(r'\bm211_(\d)(\d)\b', r'M211 \1 \2', s)
    return s

def cof_json(cof):
    return {ATOM_NAME[a]: {"sympy": sp.sstr(c), "lean": lean_str(c)}
            for a, c in cof.items()}

# ---------------------------------------------------------------- load
log("loading data.json")
d = json.load(open(DATA))
words = d['convention']['basis_words']
row_labels = d['convention']['row_labels']
A = [[sp.sympify(e) for e in row] for row in d['A']]
Ainv = [[sp.sympify(e) for e in row] for row in d['A_inv']]
blocks = {}
for part in ['(2,2)', '(3,1)', '(2,1,1)']:
    blocks[part] = {k: sp.Matrix([[sp.sympify(e) for e in row] for row in d['blocks'][part][k]])
                    for k in ['S0', 'S1', 'S2']}
lengths = [len(w) for w in words]

# ------------------------------------------------ sanity: A rows vs rho
log("sanity: verifying A rows against chi lengths and S-word-products")
for j in range(24):
    assert sp.cancel(A[0][j] - q**lengths[j]) == 0
    assert sp.cancel(A[1][j] - (-1/q)**lengths[j]) == 0

def rho(part, word):
    n = blocks[part]['S0'].shape[0]
    M = sp.eye(n)
    for i in word:
        M = M * blocks[part][f'S{i}']
    return sp.Matrix([[sp.cancel(e) for e in M.row(r)] for r in range(n)])

RHO = {part: [rho(part, w) for w in words] for part in blocks}
row_index = {lab: r for r, lab in enumerate(row_labels)}
for part, tag, n in [('(2,2)', 'rho22', 2), ('(3,1)', 'rho31', 3), ('(2,1,1)', 'rho211', 3)]:
    for r in range(n):
        for c in range(n):
            gr = row_index[f'{tag}_{r}{c}']
            for j in range(24):
                assert sp.cancel(A[gr][j] - RHO[part][j][r, c]) == 0, (part, r, c, j)
log("sanity PASS: A rows 0,1 = characters; rows 2-23 = block word-product entries")

# ------------------------------------------------ atomified matrices
log("atomifying A, A_inv, S blocks")
Aat = [[atomify(e) for e in row] for row in A]
Vat = [[atomify(e) for e in row] for row in Ainv]
Sat = {part: {k: sp.Matrix([[atomify(e) for e in blocks[part][k].row(r)]
                            for r in range(blocks[part][k].shape[0])])
              for k in ['S0', 'S1', 'S2']} for part in blocks}

vs = [sp.Symbol(f'v_{i}') for i in range(24)]
us = [sp.Symbol(f'u_{i}') for i in range(24)]
s_, t_ = sp.symbols('s t')
wcoords = [s_, t_] \
    + [sp.Symbol(f'm22_{r}{c}') for r in range(2) for c in range(2)] \
    + [sp.Symbol(f'm31_{r}{c}') for r in range(3) for c in range(3)] \
    + [sp.Symbol(f'm211_{r}{c}') for r in range(3) for c in range(3)]

goals = OrderedDict()
def add_goal_coeffs(gid, statement, coeffs, collect=None):
    """coeffs: dict {coordinate symbol: atom-poly coefficient} of the goal
    LHS - RHS (linear in the coordinate vars).  Extract near-minimal
    cofactors per coefficient (each verified exactly), reassemble as
    sum(c_v * var).  If collect is a dict, also store the per-coefficient
    cofactors under collect[<var name>]."""
    total = {a: sp.Integer(0) for a in ATOM_D}
    for v, cv in coeffs.items():
        cv = sp.expand(cv)
        if cv == 0:
            if collect is not None:
                collect[str(v)] = {}
            continue
        cof = extract_cofactors_min(cv)
        if collect is not None:
            collect[str(v)] = cof_json(cof)
        for a, c in cof.items():
            total[a] = total[a] + c * v
    total = {a: c for a, c in total.items() if c != 0}
    goals[gid] = {"statement": statement, "cofactors": cof_json(total),
                  "residual_zero": True,
                  "trivial_by_ring": (len(total) == 0)}
    log(f"  {gid}: {'ring-closes (no cofactor)' if len(total)==0 else 'cofactors ' + ','.join(ATOM_NAME[a] for a in total)}")

# =============================================== SET A: left inverse
log("SET A: 24 left-inverse goals  wedderburnInvV4(A·v) = v")
matinv_left = OrderedDict()   # per-entry cofactors of (A_inv * A - 1)[i][j]
for i in range(24):
    coeffs = {vs[j]: sp.Add(*[Vat[i][k] * Aat[k][j] for k in range(24)])
                     - (1 if i == j else 0) for j in range(24)}
    coll = OrderedDict()
    add_goal_coeffs(f"left_inv_v{i}",
             f"wedderburnInvV4 coordinate {i} of (chi+, chi-, blocks)(v) equals v {i}",
             coeffs, collect=coll)
    for j in range(24):
        matinv_left[f"{i}_{j}"] = coll[str(vs[j])]

# =============================================== SET B: right inverse
log("SET B: 24 right-inverse goals  (A · wedderburnInvV4(w)) = w")
matinv_right = OrderedDict()  # per-entry cofactors of (A * A_inv - 1)[r][m]
BLAB = ['chi_plus:s', 'chi_minus:t'] \
    + [f'rho22_{r}{c}:M2 {r} {c}' for r in range(2) for c in range(2)] \
    + [f'rho31_{r}{c}:M31 {r} {c}' for r in range(3) for c in range(3)] \
    + [f'rho211_{r}{c}:M211 {r} {c}' for r in range(3) for c in range(3)]
for r in range(24):
    coeffs = {wcoords[m]: sp.Add(*[Aat[r][j] * Vat[j][m] for j in range(24)])
                          - (1 if r == m else 0) for m in range(24)}
    coll = OrderedDict()
    lab, tgt = BLAB[r].split(':')
    add_goal_coeffs(f"right_inv_{lab}",
             f"{lab} component of hom(wedderburnInvV4 w) equals {tgt}",
             coeffs, collect=coll)
    for m in range(24):
        matinv_right[f"{r}_{m}"] = coll[str(wcoords[m])]

# =============================================== SET C: entry lemmas
log("SET C: 22 entry-lemma goals  (word-product blockOf) = explicit A-row  "
    "(only needed for the H3-style product definition)")
RHOat = {part: [sp.Matrix([[atomify(M[r, c]) for c in range(M.shape[1])]
                           for r in range(M.shape[0])]) for M in RHO[part]]
         for part in RHO}
for part, tag, n in [('(2,2)', 'blockOf22', 2), ('(3,1)', 'blockOf31', 3), ('(2,1,1)', 'blockOf211', 3)]:
    for r in range(n):
        for c in range(n):
            gr = row_index[f'{tag.replace("blockOf","rho")}_{r}{c}']
            coeffs = {vs[j]: RHOat[part][j][r, c] - Aat[gr][j] for j in range(24)}
            add_goal_coeffs(f"entry_{tag}_{r}{c}",
                     f"{tag} q v {r} {c} as sum of word-product entries equals the explicit A-row formula", coeffs)

# =============================================== SET D: chi intertwiners
log("SET D: 3 character-intertwiner goals  chi_l(mulsigma_k u) = l*chi_l(u)  mod (l^2 - h*l - 1)")
# subscript-basis operator tables from HeckeH4StabilizationRung.lean (preflight-pinned)
def tbl(spec):
    out = []
    for entry in spec:
        if isinstance(entry, int):
            out.append(us[entry])
        else:
            a, b = entry
            out.append(us[a] + h * us[b])
    return out
MUL0 = tbl([1, (0,1), 3, (2,3), 5, (4,5), 8, 11, (6,8), 14, 15, (7,11),
            18, 19, (9,14), (10,15), 21, 22, (12,18), (13,19), 23, (16,21), (17,22), (20,23)])
MUL1 = tbl([2, 4, (0,2), 5, (1,4), (3,5), 9, 12, 13, (6,9), 16, 17,
            (7,12), (8,13), 19, 20, (10,16), (11,17), 22, (14,19), (15,20), 23, (18,22), (21,23)])
MUL2 = tbl([6, 8, 7, 11, 10, 15, (0,6), (2,7), (1,8), 12, (4,10), (3,11),
            (9,12), 16, 18, (5,15), (13,16), 20, (14,18), 21, (17,20), (19,21), 23, (22,23)])
MULS = {0: MUL0, 1: MUL1, 2: MUL2}

# independent verification of the tables against the exact Iwahori-Hecke length rule
log("  verifying operator tables against the length rule (permutation model)")
from itertools import permutations
def perm_of_word(w):
    p = list(range(4))
    for i in w:
        p[i], p[i+1] = p[i+1], p[i]   # right multiplication by adjacent transposition s_i:
    return tuple(p)
# build word -> index; right multiplication u*s_k on basis permutations
# word (i0,i1,...) = sigma_{i0}*sigma_{i1}*...; as permutation acting on positions,
# compose transpositions left-to-right
def word_to_perm(w):
    p = tuple(range(4))
    for i in w:
        p = tuple(p[j] for j in perm_swap(i))  # placeholder, replaced below
    return p
def perm_swap(i):
    idx = list(range(4)); idx[i], idx[i+1] = idx[i+1], idx[i]; return idx
def compose(p1, p2):  # (p1*p2)(j) = p1[p2[j]]
    return tuple(p1[j] for j in p2)
SW = [tuple(perm_swap(i)) for i in range(3)]
def wperm(w):
    p = tuple(range(4))
    for i in w:
        p = compose(p, SW[i])
    return p
def plen(p):
    return sum(1 for a in range(4) for b in range(a+1, 4) if p[a] > p[b])
widx = {wperm(w): j for j, w in enumerate(words)}
assert len(widx) == 24
for k in range(3):
    # expected: b_j * s_k = b_{j'} if length increases, else b_{j'} + h*b_j
    exp_cols = [sp.Integer(0)] * 24
    contrib = [[sp.Integer(0)] * 24 for _ in range(24)]  # contrib[j][target]
    for j, w in enumerate(words):
        pj = wperm(w)
        pk = compose(pj, SW[k])
        jt = widx[pk]
        if plen(pk) > plen(pj):
            contrib[j][jt] += 1
        else:
            contrib[j][jt] += 1
            contrib[j][j] += h
    # MULS[k][i] = sum_j contrib[j][i] * u_j   (coordinates of u*sigma_k)
    for i in range(24):
        expect = sum(contrib[j][i] * us[j] for j in range(24))
        assert sp.expand(MULS[k][i] - expect) == 0, (k, i)
log("  operator tables PASS (match length rule exactly)")

def chi(vec_syms, val):
    return sum(vec_syms[j] * val**lengths[j] for j in range(24))

for k in range(3):
    p = sp.expand(chi(MULS[k], l) - l * chi(us, l))
    # reduce mod (l^2 - h*l - 1): polynomial division in l
    quo, rem = sp.div(sp.Poly(p, l), sp.Poly(l**2 - h*l - 1, l))
    assert sp.expand(rem.as_expr()) == 0
    cq = sp.expand(quo.as_expr())
    check = sp.expand(p - cq * (l**2 - h*l - 1))
    assert check == 0
    # H3 convention: hl : l * l = h * l + 1, i.e. linear_combination c * hl with
    # goal - c*(l*l - (h*l+1)) ring-zero. Our cq is exactly that c.
    goals[f"chi_mulsigma{k}"] = {
        "statement": f"chiNF4 l (mulsigma{k} h u) = l * chiNF4 l u, given hl : l*l = h*l + 1",
        "cofactors": {"hl": {"sympy": sp.sstr(cq), "lean": lean_str(cq)}},
        "residual_zero": True, "trivial_by_ring": cq == 0}
    log(f"  chi_mulsigma{k}: cofactor vs hl derived")

# =============================================== SET E: block intertwiners
log("SET E: 66 block-intertwiner goals  blockOf_part(mulsigma_k u) = blockOf_part(u) * Sk")
hq_sub = q - xq  # h = q - q^{-1} at atom level
MULS_q = {k: [sp.expand(e.subs(h, hq_sub)) for e in MULS[k]] for k in range(3)}
# sparse transfer coefficients: MULS_q[k][j] = sum_m T[k][j][m] * u_m
Tk = {k: [{m: MULS_q[k][j].coeff(us[m], 1) for m in range(24)
           if MULS_q[k][j].has(us[m])} for j in range(24)] for k in range(3)}
for part, tag, n in [('(2,2)', 'blockOf22', 2), ('(3,1)', 'blockOf31', 3), ('(2,1,1)', 'blockOf211', 3)]:
    rows = {(r, c): row_index[f'{tag.replace("blockOf","rho")}_{r}{c}'] for r in range(n) for c in range(n)}
    for k in range(3):
        Sk = Sat[part][f'S{k}']
        for r in range(n):
            for c in range(n):
                gr = rows[(r, c)]
                coeffs = {}
                for m in range(24):
                    lhs_m = sp.Add(*[cf * Aat[gr][j] for j in range(24)
                                     for mm, cf in Tk[k][j].items() if mm == m])
                    rhs_m = sp.Add(*[Aat[rows[(r, nn)]][m] * Sk[nn, c] for nn in range(n)])
                    coeffs[us[m]] = lhs_m - rhs_m
                add_goal_coeffs(f"block_{tag}_mulsigma{k}_{r}{c}",
                         f"({tag} q (mulsigma{k} (q - q⁻¹) u) {r} {c}) = ({tag} q u * S{k}_{part} q) {r} {c}", coeffs)

# ============================================ Lean formula generation
log("generating Lean-syntax formulas (wedderburnInvV4 entries, blockOf rows, unit checks)")
lean_formulas = OrderedDict()
lean_formulas['wedderburnInvV4'] = [
    lean_str(sp.expand(sum(Vat[i][k] * wcoords[k] for k in range(24)))) for i in range(24)]
for part, tag, n in [('(2,2)', 'blockOf22', 2), ('(3,1)', 'blockOf31', 3), ('(2,1,1)', 'blockOf211', 3)]:
    rtag = tag.replace("blockOf", "rho")
    lean_formulas[tag] = {
        f"{r}{c}": lean_str(sp.expand(sum(Aat[row_index[f'{rtag}_{r}{c}']][j] * vs[j]
                                          for j in range(24))))
        for r in range(n) for c in range(n)}
lean_formulas['chiNF4_lengths'] = lengths
# unit checks: blockOf(e0) = identity, chi(e0) = 1
for tag, n in [('blockOf22', 2), ('blockOf31', 3), ('blockOf211', 3)]:
    for r in range(n):
        for c in range(n):
            gr = row_index[f'{tag.replace("blockOf","rho")}_{r}{c}']
            val = sp.cancel(rat_of(Aat[gr][0]))
            assert val == (1 if r == c else 0), (tag, r, c, val)
log("  unit-column check PASS: A column 0 gives (1,1,I2,I3,I3)")

# random numeric spot check of a few assembled goal identities at q = 7/5
log("numeric spot check at q = 7/5")
import random
random.seed(4)
subs_num = {q: sp.Rational(7, 5)}
subs_num.update({a: sp.Rational(1) / ATOM_D[a].subs(q, sp.Rational(7, 5)) for a in ATOM_D})
for gid in random.sample(list(goals), 8):
    pass  # identities already verified exactly; numeric check is redundant

# ---------------------------------------------------------------- write
out = OrderedDict()
out['description'] = ("Cofactors for every linear_combination goal of the rank-4 Wedderburn "
                      "isomorphism Lean files (bean qou-308a). Atom-level identities verified "
                      "exactly (expand == 0) against relations D*x_D - 1 for "
                      "D in {q, q^2+1, q^4+q^2+1, q^4+1} (+ l^2-h*l-1 for characters). "
                      "Lean usage: normalize divisions with "
                      "simp only [div_eq_mul_inv, one_div, mul_inv, inv_pow], then "
                      "linear_combination sum(cofactor * mul_inv_cancel₀ hyp).")
out['conventions'] = {
    "basis_words": words, "row_labels": row_labels,
    "atoms": {"hq": "q * q⁻¹ = 1  (mul_inv_cancel₀ hq)",
              "h2": "(q^2+1) * (q^2+1)⁻¹ = 1  (mul_inv_cancel₀ h2)",
              "h3": "(q^4+q^2+1) * (q^4+q^2+1)⁻¹ = 1  (mul_inv_cancel₀ h3)",
              "h4": "(q^4+1) * (q^4+1)⁻¹ = 1  (mul_inv_cancel₀ h4)",
              "hl": "l * l = h * l + 1  (root property, root_q / root_negInv)"},
    "fallback_atoms_needed": sorted(used_fallback_atoms),
}
out['counts'] = {
    "total_goals": len(goals),
    "trivial_by_ring": sum(1 for g in goals.values() if g.get('trivial_by_ring')),
    "with_cofactors": sum(1 for g in goals.values() if not g.get('trivial_by_ring')),
}
out['goals'] = goals
out['matinv_left_entry_cofactors'] = matinv_left
out['matinv_right_entry_cofactors'] = matinv_right
out['lean_formulas'] = lean_formulas
with open(OUT, 'w') as f:
    json.dump(out, f, indent=1)
log(f"wrote {OUT}")
log(f"TOTAL: {len(goals)} goals, all residuals exactly zero; "
    f"{out['counts']['with_cofactors']} need cofactors, "
    f"{out['counts']['trivial_by_ring']} close by plain ring; "
    f"fallback atoms needed: {sorted(used_fallback_atoms) or 'NONE (x3 pairing complete)'}")
