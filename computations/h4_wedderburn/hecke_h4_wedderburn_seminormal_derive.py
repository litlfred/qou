#!/usr/bin/env python3
"""derive.py — complete symbolic data for the rank-4 Hecke Wedderburn decomposition

    H4(q) ≅ K × K × M2(K) × M3(K) × M3(K)

Bean qou-yidw.  Conventions match the rank-3 Lean chain
(QOU/Machinery/{MarkovTraceOnHecke, HeckeH3Characters, HeckeH3BlockRep,
HeckeH3Wedderburn}.lean) and the rank-4 NF tables in
QOU/Machinery/HeckeH4StabilizationRung.lean:

  * Hecke quadratic  x^2 = h x + 1,  h = q − q⁻¹;  eigenvalues ℓ₊ = q,
    ℓ₋ = −q⁻¹.
  * 24-word S4 GB-NF basis, H3 Lean basis [γ,σ₀,σ₁,L₊,L₋,e⁻] as prefix,
    remaining 18 words sorted by (length, canonical word).  Word tuple
    (i₀,i₁,…) denotes the product σ_{i₀}σ_{i₁}⋯ ; right multiplication
    u·b_j applies mulσ_{i₀} first (anti-homomorphism of right actions).
  * Block map on NF coordinates: ρ(v) = Σ_j v_j · ρ(word_j) with
    ρ(word) = S_{i₀}·S_{i₁}·⋯ (product in word order) — same as H3
    blockOf, giving a plain (not anti-) algebra homomorphism.
  * 2×2 mixing blocks normalized with the b-entry (upper off-diagonal,
    earlier-tableau row) = 1, exactly like H3BlockRep's S1.

Everything is verified symbolically over ℚ(q) (sympy, exact); the
determinant / inverse of the 24×24 coordinate matrix are computed over the
fraction field QQ(q) via DomainMatrix.

Outputs (next to this script): data.json, summary.md.
Self-contained (sympy).
"""
import itertools
import json
import os
import random

import sympy as sp
from sympy.polys.matrices import DomainMatrix
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

q = sp.Symbol('q')
h_expr = q - 1/q
hs = sp.Symbol('h')  # formal h for the NF tables

HERE = os.path.dirname(os.path.abspath(__file__))

report = {"checks": []}


def check(name, ok, detail=""):
    report["checks"].append({"name": name, "passed": bool(ok), "detail": detail})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok:
        raise SystemExit(f"CHECK FAILED: {name}")


# ---------------------------------------------------------------- basis words
def apply_s(p, i):
    p = list(p)
    p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def length(p):
    return sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b])


def canonical_word(p):
    w, p = [], tuple(p)
    while length(p) > 0:
        for i in range(3):
            if p[i] > p[i + 1]:
                w.append(i)
                p = apply_s(p, i)
                break
    return tuple(reversed(w))


def word_to_perm(w):
    p = (0, 1, 2, 3)
    for i in w:
        p = apply_s(p, i)
    return p


perms = list(itertools.permutations(range(4)))
s3_words = [(), (0,), (1,), (1, 0), (0, 1), (0, 1, 0)]
s3_perms = [word_to_perm(w) for w in s3_words]
rest = sorted((p for p in perms if p not in s3_perms),
              key=lambda p: (length(p), canonical_word(p)))
BASIS = s3_perms + rest
WORDS = s3_words + [canonical_word(p) for p in rest]
IDX = {p: k for k, p in enumerate(BASIS)}

WITNESS_WORDS = [[], [0], [1], [1, 0], [0, 1], [0, 1, 0], [2], [1, 2], [2, 0],
                 [2, 1], [0, 1, 2], [1, 2, 0], [1, 2, 1], [2, 0, 1], [2, 1, 0],
                 [0, 1, 2, 0], [0, 1, 2, 1], [1, 2, 0, 1], [1, 2, 1, 0],
                 [2, 0, 1, 0], [0, 1, 2, 0, 1], [0, 1, 2, 1, 0],
                 [1, 2, 0, 1, 0], [0, 1, 2, 0, 1, 0]]
check("basis_words_match_preflight_witness",
      [list(w) for w in WORDS] == WITNESS_WORDS,
      "24 canonical words, H3 Lean prefix")


# ------------------------------------------- right-mult matrices (length rule)
def right_mult_matrix(i):
    M = sp.zeros(24, 24)
    for j, p in enumerate(BASIS):
        ps = apply_s(p, i)
        if length(ps) > length(p):
            M[j, IDX[ps]] += 1
        else:
            M[j, j] += hs
            M[j, IDX[ps]] += 1
    return M


MS = [right_mult_matrix(i) for i in range(3)]

# ------------------------- Lean tables (HeckeH4StabilizationRung.lean), by hand
# entry k of mulσᵢ(v) is v[a] (+ h·v[k] when has_h): encoded (a, has_h)
LEAN_TABLES = {
    0: [(1, 0), (0, 1), (3, 0), (2, 1), (5, 0), (4, 1), (8, 0), (11, 0),
        (6, 1), (14, 0), (15, 0), (7, 1), (18, 0), (19, 0), (9, 1), (10, 1),
        (21, 0), (22, 0), (12, 1), (13, 1), (23, 0), (16, 1), (17, 1), (20, 1)],
    1: [(2, 0), (4, 0), (0, 1), (5, 0), (1, 1), (3, 1), (9, 0), (12, 0),
        (13, 0), (6, 1), (16, 0), (17, 0), (7, 1), (8, 1), (19, 0), (20, 0),
        (10, 1), (11, 1), (22, 0), (14, 1), (15, 1), (23, 0), (18, 1), (21, 1)],
    2: [(6, 0), (8, 0), (7, 0), (11, 0), (10, 0), (15, 0), (0, 1), (2, 1),
        (1, 1), (12, 0), (4, 1), (3, 1), (9, 1), (16, 0), (18, 0), (5, 1),
        (13, 1), (20, 0), (14, 1), (21, 0), (17, 1), (19, 1), (23, 0), (22, 1)],
}
lean_ok = True
for i in range(3):
    for k in range(24):
        a, hh = LEAN_TABLES[i][k]
        expr = sp.Symbol(f'v{a}') + (hs * sp.Symbol(f'v{k}') if hh else 0)
        mat = sum(MS[i][j, k] * sp.Symbol(f'v{j}') for j in range(24))
        if sp.expand(expr - mat) != 0:
            lean_ok = False
check("lean_operator_tables_match_length_rule", lean_ok,
      "mulσ₀/mulσ₁/mulσ₂ entries of HeckeH4StabilizationRung.lean == exact "
      "Iwahori–Hecke length-rule matrices, entry-for-entry")


# --------------------------------------------------------- seminormal blocks
def mix2(a, upper=True):
    """2x2 mixing block [[a,1],[c,h-a]] with det = -1 (c = a(h-a)+1)."""
    hq = h_expr
    return sp.Matrix([[a, 1], [a * (hq - a) + 1, hq - a]])


def solve_blocks():
    """Solve every 2x2 mixing block from trace=h, det=-1, b=1 + braid/far
    relations, exactly as HeckeH3BlockRep solved S1.  Returns dict of
    partition -> (S0, S1, S2)."""
    hq = h_expr
    lp, lm = q, -1/q
    blocks = {}

    # ---- (2,2): tableaux [ [12|34], [13|24] ]
    a = sp.Symbol('a')
    S0 = sp.diag(lp, lm)
    S2 = sp.diag(lp, lm)
    S1 = sp.Matrix([[a, 1], [a * (hq - a) + 1, hq - a]])
    eqs = [sp.numer(sp.cancel(e)) for e in (S0 * S1 * S0 - S1 * S0 * S1)]
    sols = sp.solve([e for e in eqs if e != 0], a, dict=True)
    sols = [s for s in sols
            if sp.simplify(S1.subs(s) * S2 * S1.subs(s)
                           - S2 * S1.subs(s) * S2) == sp.zeros(2, 2)]
    assert len(sols) == 1, f"(2,2) solve: {sols}"
    blocks["(2,2)"] = (S0, sp.Matrix([[sp.cancel(e.subs(sols[0]))
                                       for e in S1.row(r)] for r in range(2)]), S2)

    # ---- (3,1): tableaux [ [123|4], [124|3], [134|2] ]
    a1, a2 = sp.symbols('a1 a2')
    S0 = sp.diag(lp, lp, lm)
    S1 = sp.Matrix([[lp, 0, 0],
                    [0, a1, 1],
                    [0, a1 * (hq - a1) + 1, hq - a1]])
    S2 = sp.Matrix([[a2, 1, 0],
                    [a2 * (hq - a2) + 1, hq - a2, 0],
                    [0, 0, lp]])
    eqs = []
    for E in (S0 * S1 * S0 - S1 * S0 * S1,
              S1 * S2 * S1 - S2 * S1 * S2,
              S0 * S2 - S2 * S0):
        eqs += [sp.numer(sp.cancel(e)) for e in E if sp.cancel(e) != 0]
    sols = sp.solve(eqs, [a1, a2], dict=True)
    assert len(sols) == 1, f"(3,1) solve: {sols}"
    s = sols[0]
    blocks["(3,1)"] = tuple(
        sp.Matrix([[sp.cancel(E[r, c].subs(s)) for c in range(3)]
                   for r in range(3)]) for E in (S0, S1, S2))

    # ---- (2,1,1): tableaux [ [12|3|4], [13|2|4], [14|2|3] ]
    b1, b2 = sp.symbols('b1 b2')
    S0 = sp.diag(lp, lm, lm)
    S1 = sp.Matrix([[b1, 1, 0],
                    [b1 * (hq - b1) + 1, hq - b1, 0],
                    [0, 0, lm]])
    S2 = sp.Matrix([[lm, 0, 0],
                    [0, b2, 1],
                    [0, b2 * (hq - b2) + 1, hq - b2]])
    eqs = []
    for E in (S0 * S1 * S0 - S1 * S0 * S1,
              S1 * S2 * S1 - S2 * S1 * S2,
              S0 * S2 - S2 * S0):
        eqs += [sp.numer(sp.cancel(e)) for e in E if sp.cancel(e) != 0]
    sols = sp.solve(eqs, [b1, b2], dict=True)
    assert len(sols) == 1, f"(2,1,1) solve: {sols}"
    s = sols[0]
    blocks["(2,1,1)"] = tuple(
        sp.Matrix([[sp.cancel(E[r, c].subs(s)) for c in range(3)]
                   for r in range(3)]) for E in (S0, S1, S2))
    return blocks


BLOCKS = solve_blocks()
for part, (S0, S1, S2) in BLOCKS.items():
    n = S0.shape[0]
    I = sp.eye(n)
    ok = True
    for S in (S0, S1, S2):
        ok &= sp.simplify(S * S - h_expr * S - I) == sp.zeros(n, n)
    ok &= sp.simplify(S0 * S1 * S0 - S1 * S0 * S1) == sp.zeros(n, n)
    ok &= sp.simplify(S1 * S2 * S1 - S2 * S1 * S2) == sp.zeros(n, n)
    ok &= sp.simplify(S0 * S2 - S2 * S0) == sp.zeros(n, n)
    check(f"block_{part}_relations",
          ok, "Hecke quadratic ×3, braid σ₀σ₁σ₀=σ₁σ₀σ₁, braid σ₁σ₂σ₁=σ₂σ₁σ₂, "
              "far commutation σ₀σ₂=σ₂σ₀ — exact over ℚ(q)")

# H3 back-check: the (2,2) mixing block must equal H3BlockRep's S1
H3_S1 = sp.Matrix([[-1 / (q * (q ** 2 + 1)), 1],
                   [(q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2,
                    q ** 3 / (q ** 2 + 1)]])
check("block_2_2_S1_equals_H3_S1",
      sp.simplify(BLOCKS["(2,2)"][1] - H3_S1) == sp.zeros(2, 2),
      "(2,2) σ₁ mixing block == HeckeH3BlockRep.S1 (same axial distance −2)")


# ---------------------------------------------------------------- characters
def chi(l, word_len):
    return l ** word_len


# ------------------------------------------------------- coordinate matrix A
def rho_word(part, word):
    S = BLOCKS[part]
    n = S[0].shape[0]
    M = sp.eye(n)
    for i in word:
        M = M * S[i]
    return sp.Matrix([[sp.cancel(M[r, c]) for c in range(n)] for r in range(n)])


ROW_LABELS = (["chi_plus", "chi_minus"]
              + [f"rho22_{r}{c}" for r in range(2) for c in range(2)]
              + [f"rho31_{r}{c}" for r in range(3) for c in range(3)]
              + [f"rho211_{r}{c}" for r in range(3) for c in range(3)])

A = sp.zeros(24, 24)
for j, w in enumerate(WORDS):
    L = len(w)
    col = [chi(q, L), chi(-1/q, L)]
    for part, n in (("(2,2)", 2), ("(3,1)", 3), ("(2,1,1)", 3)):
        R = rho_word(part, w)
        col += [R[r, c] for r in range(n) for c in range(n)]
    for r in range(24):
        A[r, j] = sp.cancel(col[r])

# ------------------------------------------------ det + inverse over QQ(q)
print("building DomainMatrix over QQ(q) ...")
dA = DomainMatrix.from_Matrix(A).to_field()
K = dA.domain
print("domain:", K)
detA = dA.det()
det_expr = sp.cancel(K.to_sympy(detA))
det_fact = sp.factor(det_expr)
print("det(A) =", det_fact)
check("det_nonzero", det_expr != 0, str(det_fact))

print("inverting (24x24 over QQ(q)) ...")
dAinv = dA.inv()
prod = dA.matmul(dAinv)
check("A_times_Ainv_is_identity",
      prod.to_Matrix() == sp.eye(24)
      and dAinv.matmul(dA).to_Matrix() == sp.eye(24),
      "A·A⁻¹ = A⁻¹·A = 1, exact over the fraction field of QQ[q]")
Ainv = dAinv.to_Matrix()
Ainv = sp.Matrix([[sp.cancel(Ainv[r, c]) for c in range(24)] for r in range(24)])


# ----------------------------------------------- mulNF (rank-4) sanity checks
def mul_sigma(i, v, q0):
    hq = q0 - 1 / q0
    return [v[a] + (hq * v[k] if hh else 0)
            for k, (a, hh) in enumerate(LEAN_TABLES[i])]


def mul_word(u, word, q0):
    for i in word:
        u = mul_sigma(i, u, q0)
    return u


def mulNF(u, v, q0):
    out = [sp.Integer(0)] * 24
    for j in range(24):
        if v[j] == 0:
            continue
        ub = mul_word(u, WORDS[j], q0)
        out = [o + v[j] * x for o, x in zip(out, ub)]
    return out


def coords(v, A0):
    return [sum(A0[r, j] * v[j] for j in range(24)) for r in range(24)]


def block_product(c1, c2):
    out = [c1[0] * c2[0], c1[1] * c2[1]]
    for off, n in ((2, 2), (6, 3), (15, 3)):
        M1 = sp.Matrix(n, n, c1[off:off + n * n])
        M2 = sp.Matrix(n, n, c2[off:off + n * n])
        P = M1 * M2
        out += [P[r, c] for r in range(n) for c in range(n)]
    return out


random.seed(20260719)
QVALS = [sp.Rational(7, 5), sp.Rational(3, 2), sp.Rational(5, 3),
         sp.Rational(9, 7), sp.Rational(11, 4)]
alg_ok = True
for t, q0 in enumerate(QVALS):
    A0 = A.subs(q, q0)
    u = [sp.Rational(random.randint(-9, 9)) for _ in range(24)]
    v = [sp.Rational(random.randint(-9, 9)) for _ in range(24)]
    lhs = coords(mulNF(u, v, q0), A0)
    rhs = block_product(coords(u, A0), coords(v, A0))
    if any(sp.nsimplify(x - y) != 0 for x, y in zip(lhs, rhs)):
        alg_ok = False
        break
    # unit check
    e0 = [sp.Integer(1)] + [sp.Integer(0)] * 23
    cu = coords(e0, A0)
    unit = [1, 1] + [sp.eye(2)[r, c] for r in range(2) for c in range(2)] \
        + [sp.eye(3)[r, c] for r in range(3) for c in range(3)] * 2
    if any(x - y != 0 for x, y in zip(cu, unit)):
        alg_ok = False
        break
check("coordinate_map_is_algebra_map_5_random_pairs", alg_ok,
      f"coords(u·v) == blockwise product at q ∈ {[str(x) for x in QVALS]}, "
      "random integer u,v; unit ↦ (1,1,I₂,I₃,I₃)")

# left/right-inverse spot check at numeric q (A⁻¹ then A returns v)
q0 = sp.Rational(7, 5)
A0 = A.subs(q, q0)
Ai0 = Ainv.subs(q, q0)
v = [sp.Rational(random.randint(-9, 9)) for _ in range(24)]
w = coords(v, A0)
v2 = [sum(Ai0[r, j] * w[j] for j in range(24)) for r in range(24)]
check("numeric_roundtrip_Ainv_A", all(sp.nsimplify(a - b) == 0
                                      for a, b in zip(v, v2)), "q = 7/5")

# ---------------------------------------------------------------- genericity
# read the ≠0 conditions off the factored determinant
num, den = sp.fraction(sp.together(det_expr))
gen_factors = {f for f, m in sp.factor_list(num)[1] if not f.is_number}
gen_factors |= {f for f, m in sp.factor_list(den)[1] if not f.is_number}
genericity = sorted((str(f) for f in gen_factors), key=lambda s: (len(s), s))

# ---------------------------------------------------------------- outputs
def mat_strs(M):
    return [[sp.sstr(sp.cancel(M[r, c])) for c in range(M.shape[1])]
            for r in range(M.shape[0])]


data = {
    "convention": {
        "quadratic": "x^2 = h*x + 1, h = q - 1/q, eigenvalues q and -1/q",
        "basis_words": [list(w) for w in WORDS],
        "word_meaning": "word (i0,i1,...) = product sigma_{i0}*sigma_{i1}*...; "
                        "right mult u*b_j applies mulsigma_{i0} first",
        "rho_of_word": "product of block matrices in word order (S_{i0}*S_{i1}*...)",
        "row_labels": ROW_LABELS,
        "tableaux_order": {
            "(2,2)": ["[12|34]", "[13|24]"],
            "(3,1)": ["[123|4]", "[124|3]", "[134|2]"],
            "(2,1,1)": ["[12|3|4]", "[13|2|4]", "[14|2|3]"],
        },
        "normalization": "each 2x2 mixing block [[a,1],[a*(h-a)+1,h-a]]: "
                         "b-entry (earlier tableau -> later tableau) = 1, "
                         "det = -1, trace = h (H3BlockRep S1 pattern)",
    },
    "blocks": {part: {name: mat_strs(S)
                      for name, S in zip(("S0", "S1", "S2"), triple)}
               for part, triple in BLOCKS.items()},
    "characters": {"chi_plus": "sigma_i -> q  (partition (4))",
                   "chi_minus": "sigma_i -> -1/q  (partition (1,1,1,1))"},
    "A": mat_strs(A),
    "det_A": sp.sstr(det_expr),
    "det_A_factored": sp.sstr(det_fact),
    "genericity_nonzero_conditions": genericity,
    "A_inv": mat_strs(Ainv),
    "checks": report["checks"],
}
# Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
# `os.replace` it into position. `open(..., "w")` TRUNCATES before the
# dump runs, so any exception in between leaves the committed witness
# empty or partial -- the shape that emptied 22 witnesses to zero bytes
# in one `producer_importability_audit` run. `os.replace` is atomic on
# POSIX within a filesystem, hence a SIBLING temp file.
_wpath_sidu = os.path.join(HERE, "data.json")
_wtmp_sidu = str(_wpath_sidu) + ".tmp"
with open(_wtmp_sidu, "w") as f:
    json.dump(data, f, indent=1)
_os_sidu.replace(_wtmp_sidu, _wpath_sidu)
print("wrote data.json")


def md_matrix(M, name):
    rows = [" & ".join(sp.latex(sp.cancel(M[r, c]))
                       for c in range(M.shape[1])) for r in range(M.shape[0])]
    return f"$$ {name} = \\begin{{pmatrix}} " + " \\\\ ".join(rows) \
        + " \\end{pmatrix} $$"


words_json = json.dumps([list(w) for w in WORDS])
det_latex = sp.latex(det_fact)
gen_lines = "\n".join('* $' + sp.latex(sp.sympify(g)) + ' \\neq 0$'
                      for g in genericity)
check_lines = "\n".join(
    '* [' + ('PASS' if c['passed'] else 'FAIL') + '] ' + c['name']
    + (' — ' + c['detail'] if c['detail'] else '')
    for c in report['checks'])
mats = {(part, i): md_matrix(BLOCKS[part][i], f"S_{i}")
        for part in BLOCKS for i in range(3)}


summary = f"""# H₄(q) Wedderburn decomposition — symbolic data (bean qou-yidw)

Conventions (verified against the Lean sources, see "convention surprises"
below): Hecke quadratic $x^2 = h\\,x + 1$, $h = q - q^{{-1}}$, eigenvalues
$\\ell_+ = q$, $\\ell_- = -q^{{-1}}$.

## Basis (from `HeckeH4StabilizationRung.lean` / preflight witness)

24 canonical S₄ words, H₃ Lean basis `[γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`
as prefix, then the remaining 18 sorted by (length, canonical word):

```
{words_json}
```

Word $(i_0, i_1, \\dots)$ is the product $\\sigma_{{i_0}}\\sigma_{{i_1}}\\cdots$;
right multiplication $u\\cdot b_j$ composes `mulσ` along the word applying
$\\sigma_{{i_0}}$ FIRST (right actions anti-compose); the representation of a
word is the plain product $S_{{i_0}} S_{{i_1}} \\cdots$ (H3 `blockOf` pattern).

## The two characters

* $\\chi_+$ (partition $(4)$): $\\sigma_i \\mapsto q$; basis word of length
  $\\ell$ contributes $q^\\ell$.
* $\\chi_-$ (partition $(1^4)$): $\\sigma_i \\mapsto -q^{{-1}}$; contributes
  $(-q^{{-1}})^\\ell$.

## Seminormal blocks (b-entry of each mixing block normalized to 1)

Tableaux orders: $(2,2)$: `[12|34], [13|24]`; $(3,1)$: `[123|4], [124|3],
[134|2]`; $(2,1,1)$: `[12|3|4], [13|2|4], [14|2|3]`.

### Partition (2,2) — 2-dimensional

{mats[("(2,2)", 0)]}

{mats[("(2,2)", 1)]}

{mats[("(2,2)", 2)]}

(The $S_1$ mixing block is *identical* to `HeckeH3BlockRep.S1` — same axial
distance $-2$.)

### Partition (3,1) — 3-dimensional

{mats[("(3,1)", 0)]}

{mats[("(3,1)", 1)]}

{mats[("(3,1)", 2)]}

### Partition (2,1,1) — 3-dimensional

{mats[("(2,1,1)", 0)]}

{mats[("(2,1,1)", 1)]}

{mats[("(2,1,1)", 2)]}

All three blocks verified symbolically: Hecke quadratic for each $S_i$, both
adjacent braid relations, far commutation $S_0 S_2 = S_2 S_0$.

Structure notes: every 2×2 mixing block has the H3BlockRep shape
$[[a, 1], [a(h-a)+1, h-a]]$ with $a = h/(1-q^{{-2d}})$ for axial distance
$d$.  The $d=-2$ block (all three partitions' $\\sigma_1$-edge) is exactly
`HeckeH3BlockRep.S1`; the $d=-3$ block (the $\\sigma_2$-edge of $(3,1)$ and
$(2,1,1)$) has $a = -1/(q(q^4+q^2+1))$, $h-a = q^5/(q^4+q^2+1)$ and
$c$-entry $(q^2+1)^2(q^4+1)/(q^4+q^2+1)^2$ — the $[4]$-type factor
$q^4+1$ enters here, matching its appearance in $\\det A$.

## Convention surprises found in the Lean file

None that contradict the task assumptions, but three facts worth pinning:

1. The 24-word basis order is NOT plain length-lex over all of S₄: the six
   H₃ words come FIRST (in the H₃ Lean order, so word 3 is $\\sigma_1
   \\sigma_0$ and word 4 is $\\sigma_0\\sigma_1$), and only the remaining 18
   words are sorted by (length, canonical word).  Canonical words come from
   the leftmost-descent factorization (see `canonical_word` above).
2. `mulσᵢ` is RIGHT multiplication; each output entry $k$ is
   $v_a + h\\,v_k$ (the $h$-coefficient always sits on the output index
   itself) — verified entry-for-entry against the exact Iwahori–Hecke
   length rule.
3. $\\rho(\\text{{word}})$ must be the product of the $S$ matrices in word
   order (NOT reversed): right actions anti-compose, which is already
   accounted for in the `mulNF` pattern `u·b_j = mulσ_{{i_0}}` first.

## Determinant of the 24×24 coordinate matrix

$$ \\det A = {det_latex} $$

## Genericity hypotheses (the ≠ 0 conditions read off det A)

{gen_lines}

## Verification summary

{check_lines}

Full matrices `A`, `A⁻¹` (entries cancelled over ℚ(q)) in `data.json`.
Reproduce with `python3 derive.py`.
"""
with open(os.path.join(HERE, "summary.md"), "w") as f:
    f.write(summary)
print("wrote summary.md")
print("ALL CHECKS PASSED" if all(c["passed"] for c in report["checks"])
      else "SOME CHECKS FAILED")
