#!/usr/bin/env python3
"""Electron braid word: Gröbner-Shirshov / normal-form interaction measurements.

Measures, for each candidate e⁻ word, the criteria C1-C6 fixed IN ADVANCE in
docs/audits/2026-11-21-electron-word-gs-interactions.md §1 (committed before
this probe was written). Measure only: nothing here ranks candidates against
experiment, and no consumer of the corpus's e⁻ word is changed.

Conventions (AGENTS.md):
  Hecke   σᵢ² = h σᵢ + 1, h = q − q⁻¹ (eigenvalues q, −q⁻¹);  σᵢ⁻¹ = σᵢ − h.
  Photon  γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹   (owner ruling 2026-11-20).
  Trace   convention D, z = q³/(q²+1).
Arithmetic: sympy over ℚ(q) throughout. mpmath is used only for the cross-check
against the corpus's own reducer (photon_operator_table.reduce_nf), evaluated at
the proton q₀ (q_parameter.Q_MP).

No witness (probe). Run:
    python3 -u computations/probes/electron_word_gs_interactions_probe.py 2>&1 | tee /tmp/elw.log

# Ref: [kassel2008] Kassel & Turaev, Braid Groups, §4 (Iwahori–Hecke algebra,
#      standard basis T_w, Ocneanu trace); [kauffman1987] state-sum bracket.
"""
from __future__ import annotations

import ast
import itertools
import sys
from pathlib import Path

import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
z = q**3 / (q**2 + 1)

# ── exact H₃(q): standard basis T_w, w ∈ S₃ ───────────────────────────────
# A permutation is the tuple of images of (0,1,2). σᵢ ↦ the transposition sᵢ.
ID = (0, 1, 2)
S = {0: (1, 0, 2), 1: (0, 2, 1)}


def comp(a, b):  # (a∘b)(x) = a(b(x))
    return tuple(a[b[x]] for x in range(3))


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


# canonical reduced words: the corpus basis order
BASIS_WORDS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NAMES = ["1", "σ₀", "σ₁", "σ₀σ₁(L₊)", "σ₁σ₀(L₋)", "σ₀σ₁σ₀(e⁻)"]


def perm_of(word):
    p = ID
    for i in word:
        p = comp(p, S[i])
    return p


PERMS = [perm_of(w) for w in BASIS_WORDS]
IDX = {p: k for k, p in enumerate(PERMS)}
assert len(IDX) == 6


def right_gen(vec, i):
    """vec · T_{s_i}."""
    out = [sp.Integer(0)] * 6
    for k, c in enumerate(vec):
        if c == 0:
            continue
        w = PERMS[k]
        ws = comp(w, S[i])
        if length(ws) > length(w):
            out[IDX[ws]] += c
        else:
            out[k] += c * h
            out[IDX[ws]] += c
    return [sp.simplify(x) for x in out]


def unit():
    v = [sp.Integer(0)] * 6
    v[0] = sp.Integer(1)
    return v


def elem_of_word(word):
    """Signed word: letters +1 -> σ₀, +2 -> σ₁, -1 -> σ₀⁻¹, -2 -> σ₁⁻¹."""
    v = unit()
    for L in word:
        i = abs(L) - 1
        vs = right_gen(v, i)
        if L > 0:
            v = vs
        else:  # v·σ⁻¹ = v·σ − h v
            v = [sp.simplify(a - h * b) for a, b in zip(vs, v)]
    return v


def mul(a, b):
    """a·b for general elements: expand b in the basis words."""
    out = [sp.Integer(0)] * 6
    for k, c in enumerate(b):
        if c == 0:
            continue
        t = a
        for i in BASIS_WORDS[k]:
            t = right_gen(t, i)
        out = [o + c * x for o, x in zip(out, t)]
    return [sp.factor(sp.simplify(x)) for x in out]


def add(a, b, s=1):
    return [sp.simplify(x + s * y) for x, y in zip(a, b)]


def is_zero(v):
    return all(sp.simplify(x) == 0 for x in v)


def support(v):
    return [NAMES[k] for k, x in enumerate(v) if sp.simplify(x) != 0]


TR = [sp.Integer(1), z, z, z**2, z**2, h * z**2 + z]  # Ocneanu weights (corpus)


def trace(v):
    return sp.factor(sp.simplify(sum(a * t for a, t in zip(v, TR))))


# ── cross-check against the corpus reducer at the proton q₀ ───────────────
def corpus_reducer():
    import mpmath as mp
    mp.mp.dps = 70
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import _path_bridge  # noqa: F401 — substrate modules live under computations/substrate
    from q_parameter import Q_MP
    q0 = mp.mpf(Q_MP)
    src = (Path(__file__).resolve().parents[1] / "photon_operator_table.py").read_text()
    tree = ast.parse(src)
    keep = [n for n in tree.body if isinstance(n, ast.FunctionDef)
            and n.name in ("hecke_mul", "reduce_nf")]
    ns = {"HA": q0 - 1 / q0, "_ZERO": mp.mpf(0), "_EPS": mp.mpf(10) ** -50}
    exec(compile(ast.Module(body=keep, type_ignores=[]), "corpus", "exec"), ns)
    return ns["reduce_nf"], q0, mp


def word_unsigned(word):
    return tuple(abs(L) - 1 for L in word)


# ── C1: closure components, writhe, Jones (Kauffman bracket) ──────────────
A = sp.symbols("A")
d = -A**2 - A**-2


def components(word, n=3):
    p = ID[:n]
    for L in word:
        i = abs(L) - 1
        p = comp(p, S[i])
    seen, c = set(), 0
    for x in range(n):
        if x in seen:
            continue
        c += 1
        y = x
        while y not in seen:
            seen.add(y)
            y = p[y]
    return c


def bracket(word, n=3):
    m = len(word)
    tot = sp.Integer(0)
    for states in itertools.product((0, 1), repeat=m):  # 0 = A-smoothing
        parent = {}

        def f(x):
            while parent.setdefault(x, x) != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def u(a, b):
            parent[f(a)] = f(b)

        for k, L in enumerate(word):
            i = abs(L) - 1
            for j in range(n):
                if j not in (i, i + 1):
                    u((k, j), (k + 1, j))
            # positive crossing: A-smoothing = vertical; negative: swapped
            vertical = (states[k] == 0) == (L > 0)
            if vertical:
                u((k, i), (k + 1, i))
                u((k, i + 1), (k + 1, i + 1))
            else:
                u((k, i), (k, i + 1))
                u((k + 1, i), (k + 1, i + 1))
        for j in range(n):
            u((m, j), (0, j))
        loops = len({f((k, j)) for k in range(m + 1) for j in range(n)})
        a = states.count(0)
        b = m - a
        tot += A ** (a - b) * d ** (loops - 1)
    return sp.expand(tot)


t = sp.symbols("t", positive=True)


def jones(word, n=3):
    w = sum(1 if L > 0 else -1 for L in word)
    V = sp.expand((-A**3) ** (-w) * bracket(word, n))
    return sp.expand(V.subs(A, t ** sp.Rational(-1, 4)))


# ── candidates (doc §1) and the corpus conjugation C: σᵢ ↦ σᵢ⁻¹ ────────────
CANDIDATES = {
    "X1 σ₀σ₁σ₀": (1, 2, 1),
    "X2 σ₀²σ₁": (1, 1, 2),
    "X3 σ₀³": (1, 1, 1),
    "X4 σ₁³": (2, 2, 2),
    "X5 σ₀³σ₁ (ref, 4 crossings)": (1, 1, 1, 2),
    "X6 (σ₀σ₁)² (ref, 4 crossings)": (1, 2, 1, 2),
}


def C(word):
    return tuple(-L for L in word)


def inv(word):
    return tuple(-L for L in reversed(word))


def crossing_energy(word):
    return sp.simplify(sum(q if L > 0 else -1 / q for L in word))


# ── photons ───────────────────────────────────────────────────────────────
f0, f1, f01, p0, p1, p01, c, uu = sp.symbols("f0 f1 f01 p0 p1 p01 c u")
V = elem_of_word((1, -2))  # σ₀σ₁⁻¹


def photon(a, b, e):
    v = unit()
    v = add(v, [a * x for x in elem_of_word((1,))])
    v = add(v, [b * x for x in elem_of_word((2,))])
    v = add(v, [e * x for x in V])
    return v


P_SPAN = {0, 1, 2, 3}  # span{1,σ₀,σ₁,σ₀σ₁} = span{1,σ₀,σ₁,σ₀σ₁⁻¹}


def in_P(v):
    return all(sp.simplify(v[k]) == 0 for k in (4, 5))


def two_photon_solvable(X, qval):
    """C2c: ∃ φ, ψ, c≠0 with γ(φ)γ(ψ) = c·X at q = qval (over ℚ̄)."""
    G = mul(photon(f0, f1, f01), photon(p0, p1, p01))
    eqs = [sp.together((g - c * x).subs(q, qval)) for g, x in zip(G, X)]
    eqs = [sp.numer(e) for e in eqs] + [c * uu - 1]
    gb = sp.groebner(eqs, f0, f1, f01, p0, p1, p01, c, uu, order="grevlex")
    return not (len(gb.exprs) == 1 and gb.exprs[0] == 1)


def main():
    print("Electron-word GS interaction probe (exact over ℚ(q))\n")

    # sanity: Hecke and braid relations in the exact model
    s0, s1 = elem_of_word((1,)), elem_of_word((2,))
    assert is_zero(add(mul(s0, s0), add([h * x for x in s0], unit()), -1))
    assert is_zero(add(elem_of_word((1, 2, 1)), elem_of_word((2, 1, 2)), -1))
    assert is_zero(add(mul(s0, elem_of_word((-1,))), unit(), -1))
    print("sanity: σ²=hσ+1, braid relation, σσ⁻¹=1  OK")

    # Borromean factorisation check (owner-ruled photon)
    lhs = mul(photon(0, 0, q * h), photon(0, 0, -h / q))
    rhs = elem_of_word((1, -2, 1, -2, 1, -2))
    assert is_zero(add(lhs, rhs, -1))
    print("sanity: γ(0,0,qh)·γ(0,0,−q⁻¹h) = (σ₀σ₁⁻¹)³  OK")

    # cross-check vs corpus reducer on several positive words
    red, q0, mp = corpus_reducer()
    for w in [(0, 1, 0), (0, 0, 0), (1, 1, 1), (0, 0, 1), (0, 1, 0, 1), (0, 0, 0, 1),
              (1, 0, 1, 0, 1), (0, 1, 1, 0, 0, 1)]:
        corp = red({w: mp.mpf(1)})
        mine = elem_of_word(tuple(i + 1 for i in w))
        for k, bw in enumerate(BASIS_WORDS):
            cv = corp.get(bw, mp.mpf(0))
            mv = mp.mpf(str(sp.N(mine[k].subs(q, sp.Rational(str(q0))), 75)))
            assert abs(cv - mv) < mp.mpf(10) ** -55, (w, bw, cv, mv)
    print("cross-check vs photon_operator_table.reduce_nf at proton q₀: 8 words × 6 coeffs agree to 1e-55\n")

    # calibrate Jones convention against commit 70340a13f9 values
    assert sp.simplify(jones((), 1) - 1) == 0
    Vhopf = jones((1, 1), 2)
    Vtref = jones((1, 1, 1), 2)
    print(f"calibration: V(σ₀² ∈ B₂) = {Vhopf};  V(σ₀³ ∈ B₂) = {Vtref}")
    assert sp.simplify(Vhopf - (-t ** sp.Rational(5, 2) - t ** sp.Rational(1, 2))) == 0
    assert sp.simplify(Vtref - (-t**4 + t**3 + t)) == 0
    print()

    # general two-photon NF (C2a)
    G = mul(photon(f0, f1, f01), photon(p0, p1, p01))
    print("NF γ(φ)·γ(ψ):")
    for k in range(6):
        print(f"   {NAMES[k]:14s} {sp.factor(sp.expand(G[k]))}")
    print()

    rows = {}
    for name, w in CANDIDATES.items():
        X = elem_of_word(w)
        Cw = C(w)
        Xc = elem_of_word(Cw)
        r = {}
        r["components"] = components(w)
        r["writhe"] = sum(1 if L > 0 else -1 for L in w)
        r["jones"] = sp.factor(jones(w))
        r["NF"] = [sp.factor(x) for x in X]
        r["support"] = support(X)
        nz = [k for k in range(6) if sp.simplify(X[k]) != 0]
        r["C2a_single_basis_word"] = len(nz) == 1
        r["C2a_channel_coeff"] = sp.factor(sp.expand(G[nz[0]])) if len(nz) == 1 else None
        r["C2b_in_P"] = in_P(X)
        r["C2b_scaled_photon"] = in_P(X) and sp.simplify(X[0]) != 0
        if r["C2b_scaled_photon"]:
            c0 = X[0]
            r["C2b_photon_weights"] = tuple(sp.factor(sp.simplify(x / c0)) for x in
                                            (X[1] + h * X[3], X[2], X[3]))
            # check: X/c0 = γ(φ0, φ1, φ01) with σ₀σ₁⁻¹ = σ₀σ₁ − hσ₀
            ph = photon(*r["C2b_photon_weights"])
            assert is_zero(add([x / c0 for x in X], ph, -1))
        r["C2c_two_photon_q=2"] = two_photon_solvable(X, sp.Integer(2))
        r["C2c_two_photon_q=3"] = two_photon_solvable(X, sp.Integer(3))
        # C3
        r["C3_eC(e)"] = support(mul(X, Xc))
        r["C3_eC(e)_is_1"] = is_zero(add(mul(X, Xc), unit(), -1))
        r["C3_C(e)e_is_1"] = is_zero(add(mul(Xc, X), unit(), -1))
        r["C3_eC(e)_in_P"] = in_P(mul(X, Xc))
        pair = add(X, Xc)
        r["C3_sum_support"] = support(pair)
        r["C3_sum_in_P"] = in_P(pair)
        # C4
        r["C4_C(word)"] = Cw
        r["C4_palindromic"] = tuple(reversed(w)) == w
        r["C4_C=inverse_in_H3"] = is_zero(add(Xc, elem_of_word(inv(w)), -1))
        r["C4_C(X)≠X"] = not is_zero(add(Xc, X, -1))
        r["C4_C(X)_support"] = support(Xc)
        r["C4_C(X)_single_basis_word"] = len(support(Xc)) == 1
        # C5
        Ew, ECw = crossing_energy(w), crossing_energy(Cw)
        r["C5_E"] = Ew
        r["C5_E(C)"] = ECw
        r["C5_rule_E(C)=-E|q->1/q"] = sp.simplify(ECw + Ew.subs(q, 1 / q)) == 0
        r["trace_D"] = trace(X)
        rows[name] = r
        print(f"=== {name}   word {w}")
        for k, v in r.items():
            print(f"   {k:28s} {v}")
        print()

    # C2c sweep at more specialisations for the two words that fail it at q = 2, 3
    _, q0, _mp = corpus_reducer()
    qvals = [sp.Rational(5, 2), sp.Integer(7), sp.Rational(111, 100), sp.Rational(str(q0)),
             sp.Integer(-3), sp.Rational(1, 2)]
    for name in ("X1 σ₀σ₁σ₀", "X6 (σ₀σ₁)² (ref, 4 crossings)"):
        X = elem_of_word(CANDIDATES[name])
        res = [two_photon_solvable(X, qv) for qv in qvals]
        print(f"C2c sweep {name}: solvable at q in [5/2, 7, 111/100, q0 (exact rational of Q_MP), -3, 1/2]: {res}")
    print()

    # corpus e⁺ check
    assert CANDIDATES["X1 σ₀σ₁σ₀"] == (1, 2, 1) and C((1, 2, 1)) == (-1, -2, -1)
    print("C4: C(X1) = σ₀⁻¹σ₁⁻¹σ₀⁻¹ = the corpus e⁺ (def:breit-wheeler-pair-production)")

    # parity fact (C1): every odd-length word in B₃ closes to 2 components
    odd_ok = all(components(w) == 2 for L in (1, 3, 5)
                 for w in itertools.product((1, 2, -1, -2), repeat=L))
    print(f"C1 parity: all odd-length words (len 1,3,5) in B₃ close to exactly 2 components: {odd_ok}")
    even_counts = sorted({components(w) for L in (2, 4)
                          for w in itertools.product((1, 2), repeat=L)})
    print(f"C1 parity: positive even words (len 2,4) close to component counts {even_counts}")

    print("\nDISCRIMINATION SUMMARY (does the criterion separate the 3-crossing candidates X1-X4?)")
    keys = ["components", "C2a_single_basis_word", "C2b_in_P", "C2b_scaled_photon",
            "C2c_two_photon_q=2", "C2c_two_photon_q=3", "C3_eC(e)_is_1", "C3_sum_in_P",
            "C4_C=inverse_in_H3", "C4_C(X)≠X", "C4_C(X)_single_basis_word", "C5_E"]
    three = [n for n in CANDIDATES if n[:2] in ("X1", "X2", "X3", "X4")]
    for k in keys:
        vals = [str(rows[n][k]) for n in three]
        print(f"   {k:28s} {'SEPARATES' if len(set(vals)) > 1 else 'same'}   {vals}")


if __name__ == "__main__":
    sys.exit(main())
