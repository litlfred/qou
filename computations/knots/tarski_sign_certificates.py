#!/usr/bin/env python3
"""Generate Lean sign certificates for the figure-eight Kashaev value at level N.

Bean qou-rc4t (Tarski route for finite-N comparisons), epic qou-dk7p.

For each N this script, in exact rational arithmetic (sympy ``Rational``; no
float enters any decision):

1. computes Psi_N, the minimal polynomial of c = zeta_N + zeta_N^{-1};
2. reduces the Kashaev sum <4_1>_N = sum_{k<N} prod_{j<=k} (2 - C_j(c)) modulo
   Psi_N, keeping the quotient for a ``linear_combination`` proof;
3. picks the embedding zeta_N = e^{2 pi i/N}, i.e. the largest real root of
   Psi_N. sympy isolates the real roots exactly (``Poly.real_roots`` returns
   ``CRootOf`` objects whose comparisons with rationals are decided by
   rational interval refinement);
4. follows c through Conway's sign-expansion recipe (``GonshorState.step`` in
   ``QOU/Observations/SignSequence.lean``). The embedding depth d is the first
   window holding no other root of Psi_N; that window is the embedding
   hypothesis of the Lean theorem;
5. after depth d, each further sign is one exclusion certificate: Psi_N has
   constant sign on the half-window that does not contain c, proved by a
   Bernstein (bounded) or Taylor-shift (half-line) form with nonnegative
   coefficients, degree-elevated until they are;
6. stops at the first depth k at which floor(<4_1>_N) = n is certified:
   Bernstein forms of f - n and n + 1 - f on the window are positive.

It writes ``QOU/Core/TarskiSignKashaevGen.lean`` (sorry-free, any ordered
field) and prints a table of N, deg Psi_N, d, k, n. The table is also written
as a witness JSON next to this script.

Usage:  python3 -u computations/knots/tarski_sign_certificates.py [N ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

x = sp.symbols("x")
R = sp.Rational

REPO = Path(__file__).resolve().parents[2]
LEAN_OUT = REPO / "folio/quantum-observable-universe/lean/QOU/Core/TarskiSignKashaevGen.lean"
WITNESS = Path(__file__).with_suffix(".witness.json")

MAX_ELEVATION = 60


# --------------------------------------------------------------------------
# exact algebra
# --------------------------------------------------------------------------

def psi(N: int) -> sp.Poly:
    """Minimal polynomial of zeta_N + zeta_N^{-1}, from the cyclotomic Phi_N.

    Phi_N(z) = z^{phi/2} Psi_N(z + 1/z) for N >= 3; Psi_1 = x - 2, Psi_2 = x + 2.
    """
    if N == 1:
        return sp.Poly(x - 2, x)
    if N == 2:
        return sp.Poly(x + 2, x)
    z = sp.symbols("z")
    phi = sp.Poly(sp.cyclotomic_poly(N, z), z)
    m = phi.degree() // 2
    # Solve for Psi by matching: build Psi coefficient by coefficient.
    target = sp.expand(phi.as_expr() / z**m)
    p = 0
    rem = target
    for k in range(m, -1, -1):
        # leading coefficient of z^k in rem
        coeff = sp.Poly(sp.expand(rem * z**m), z).coeff_monomial(z**(m + k))
        p += coeff * x**k
        rem = sp.expand(rem - coeff * sp.expand((z + 1 / z) ** k))
    assert sp.simplify(rem) == 0, (N, rem)
    return sp.Poly(p, x)


def dickson(N: int) -> list:
    C = [sp.Integer(2), x]
    for _ in range(2, N + 1):
        C.append(sp.expand(x * C[-1] - C[-2]))
    return C


def kashaev_poly(N: int) -> sp.Expr:
    C = dickson(N)
    tot = sp.Integer(0)
    prod = sp.Integer(1)
    for k in range(N):
        if k > 0:
            prod = sp.expand(prod * (2 - C[k]))
        tot += prod
    return sp.expand(tot)


# --------------------------------------------------------------------------
# certificates
# --------------------------------------------------------------------------

def bernstein_coeffs(f: sp.Expr, a, b, n: int):
    """Coefficients c_i with f = sum c_i (x-a)^i (b-x)^(n-i), exact.

    With x = a + (b - a) u and f = sum g_j u^j, the Bernstein coefficients are
    beta_i = sum_{j<=i} C(i,j)/C(n,j) g_j, and c_i = beta_i C(n,i)/(b-a)^n.
    """
    a, b = sp.Rational(a), sp.Rational(b)
    u = sp.symbols("u")
    g = sp.Poly(sp.expand(f.subs(x, a + (b - a) * u)), u).all_coeffs()[::-1]
    g = [sp.Rational(c) for c in g] + [sp.Integer(0)] * (n + 1 - len(g))
    out = []
    for i in range(n + 1):
        beta = sum(sp.binomial(i, j) / sp.binomial(n, j) * g[j] for j in range(i + 1))
        out.append(sp.Rational(beta * sp.binomial(n, i) / (b - a) ** n))
    return out


def bernstein_cert(f: sp.Expr, a, b):
    """Least elevation degree with a valid certificate for f > 0 on [a, b]."""
    d0 = max(sp.Poly(f, x).degree(), 1)
    for n in range(d0, d0 + MAX_ELEVATION):
        cs = bernstein_coeffs(f, a, b, n)
        if all(c >= 0 for c in cs) and cs[0] > 0 and cs[-1] > 0:
            return n, cs
    return None


def taylor_cert(f: sp.Expr, m, up: bool):
    """f = sum c_i (x - m)^i (up) or sum c_i (m - x)^i (down), all c_i >= 0."""
    t = sp.symbols("t")
    g = sp.expand(f.subs(x, m + t if up else m - t))
    cs = sp.Poly(g, t).all_coeffs()[::-1]
    if all(c >= 0 for c in cs) and cs[0] > 0:
        return len(cs) - 1, cs
    return None


# --------------------------------------------------------------------------
# Gonshor walk (mirrors GonshorState.step)
# --------------------------------------------------------------------------

class State:
    def __init__(self, value, lo, hi, hasLo, hasHi):
        self.value, self.lo, self.hi, self.hasLo, self.hasHi = value, lo, hi, hasLo, hasHi

    def step(self, plus: bool) -> "State":
        v = self.value
        if plus:
            if self.hasHi:
                return State((v + self.hi) / 2, v, self.hi, True, True)
            return State(v + 1, v, R(0), True, False)
        if self.hasLo:
            return State((self.lo + v) / 2, self.lo, v, True, True)
        return State(v - 1, R(0), v, False, True)


def in_window(st: State, r) -> bool:
    return (not st.hasLo or st.lo < r) and (not st.hasHi or r <= st.hi)


# --------------------------------------------------------------------------
# Lean emission
# --------------------------------------------------------------------------

def lean_q(q) -> str:
    q = sp.Rational(q)
    if q.q == 1:
        return f"({q.p} : K)" if q.p < 0 else f"{q.p}"
    return f"({q.p} / {q.q} : K)"


def lean_qK(q) -> str:
    q = sp.Rational(q)
    if q.q == 1:
        return f"({q.p} : K)"
    return f"({q.p} / {q.q} : K)"


def lean_poly(f: sp.Expr, var: str = "x") -> str:
    p = sp.Poly(f, x)
    terms = []
    for (k,), c in sorted(p.terms(), key=lambda t: -t[0][0]):
        c = sp.Rational(c)
        mag = abs(c)
        mono = "" if k == 0 else (var if k == 1 else f"{var} ^ {k}")
        if mag == 1 and k > 0:
            body = mono
        else:
            cs = str(mag.p) if mag.q == 1 else f"({mag.p} / {mag.q})"
            body = cs if k == 0 else f"{cs} * {mono}"
        terms.append(("-" if c < 0 else "+", body))
    out = ("-" if terms[0][0] == "-" else "") + terms[0][1]
    for s, b in terms[1:]:
        out += f" {s} {b}"
    return out


def lean_list(cs) -> str:
    items = []
    for c in cs:
        c = sp.Rational(c)
        items.append(str(c.p) if c.q == 1 else f"{c.p} / {c.q}")
    return "[" + ", ".join(items) + "]"


def exclusion_block(name, P, s, kind, a, b, cert, hyp_lo, hyp_hi, conclude_lt):
    """Lean `have` deciding one sign by excluding [a, b] (or a half-line)."""
    n, cs = cert
    sgn = "" if s > 0 else "-"
    pexpr = lean_poly(P)
    rhs = f"{sgn}({pexpr})" if s < 0 else pexpr
    lines = []
    if conclude_lt:  # c < m, excluded [m, hi] or [m, inf)
        m = a
        if kind == "bern":
            lines.append(f"  have {name} : c < {lean_qK(m)} := lt_of_excluded (p := fun x => {pexpr}) (b := {lean_qK(b)}) hc {hyp_hi}.le (fun x hx0 hx1 => by")
            lines.append(f"    have h := bernstein_pos (a := {lean_qK(a)}) (b := {lean_qK(b)}) (n := {n}) (c := coeffs {lean_list(cs)}) (by norm_num) hx0 hx1 (by intro i hi; interval_cases i <;> norm_num [coeffs]) (by norm_num [coeffs]) (by norm_num [coeffs])")
            lines.append(f"    have e : bernstein {lean_qK(a)} {lean_qK(b)} {n} (coeffs {lean_list(cs)}) x = {rhs} := by simp [bernstein, coeffs, sum_range_succ]; ring")
        else:
            lines.append(f"  have {name} : c < {lean_qK(m)} := lt_of_excluded_up (p := fun x => {pexpr}) hc (fun x hx0 => by")
            lines.append(f"    have h := taylorUp_pos (m := {lean_qK(m)}) (n := {n}) (c := coeffs {lean_list(cs)}) hx0 (by intro i hi; interval_cases i <;> norm_num [coeffs]) (by norm_num [coeffs])")
            lines.append(f"    have e : taylorUp {lean_qK(m)} {n} (coeffs {lean_list(cs)}) x = {rhs} := by simp [taylorUp, coeffs, sum_range_succ]; ring")
    else:  # m < c, excluded [lo, m] or (-inf, m]
        m = b
        if kind == "bern":
            lines.append(f"  have {name} : {lean_qK(m)} < c := lt_of_excluded' (p := fun x => {pexpr}) (a := {lean_qK(a)}) hc {hyp_lo}.le (fun x hx0 hx1 => by")
            lines.append(f"    have h := bernstein_pos (a := {lean_qK(a)}) (b := {lean_qK(b)}) (n := {n}) (c := coeffs {lean_list(cs)}) (by norm_num) hx0 hx1 (by intro i hi; interval_cases i <;> norm_num [coeffs]) (by norm_num [coeffs]) (by norm_num [coeffs])")
            lines.append(f"    have e : bernstein {lean_qK(a)} {lean_qK(b)} {n} (coeffs {lean_list(cs)}) x = {rhs} := by simp [bernstein, coeffs, sum_range_succ]; ring")
        else:
            lines.append(f"  have {name} : {lean_qK(m)} < c := lt_of_excluded_down (p := fun x => {pexpr}) hc (fun x hx0 => by")
            lines.append(f"    have h := taylorDown_pos (m := {lean_qK(m)}) (n := {n}) (c := coeffs {lean_list(cs)}) hx0 (by intro i hi; interval_cases i <;> norm_num [coeffs]) (by norm_num [coeffs])")
            lines.append(f"    have e : taylorDown {lean_qK(m)} {n} (coeffs {lean_list(cs)}) x = {rhs} := by simp [taylorDown, coeffs, sum_range_succ]; ring")
    lines.append("    intro h'; simp only at h'; rw [e] at h; linarith)")
    return lines


def sign_theorem(tag, k, psi_lean, lo, hi, concl, blk):
    """Wrap one exclusion `have` as a standalone lemma (bounded heartbeats)."""
    lower_used = concl.endswith("< c")
    lo_name = "hlo" if lower_used else "_hlo"
    hi_name = "_hhi" if lower_used else "hhi"
    first = blk[0]
    i = first.index(":= ")
    body = ["  exact " + first[i + 3:]] + blk[1:]
    head = [f"/-- Sign {k} after the embedding window: `{concl}`, given `{lo} < c < {hi}`. -/",
            f"theorem kashaev_{tag}_sign{k} {{K : Type*}} [Field K] [LinearOrder K] [IsStrictOrderedRing K]",
            f"    {{c : K}} (hc : {psi_lean} = 0) ({lo_name} : {lean_qK(lo)} < c) ({hi_name} : c < {lean_qK(hi)}) :",
            f"    {concl} := by"]
    return head + body + [""]


def process(N: int) -> dict:
    t0 = time.time()
    P = psi(N)
    deg = P.degree()
    Pexpr = P.as_expr()
    K = kashaev_poly(N)
    Q, r = sp.div(sp.Poly(K, x), P)
    f = r.as_expr()
    info = {"N": N, "deg_psi": deg, "psi": str(Pexpr), "reduced": str(f)}

    roots = P.real_roots()
    assert len(roots) == deg, "Psi_N is totally real"
    c = roots[-1]  # largest real root = 2cos(2 pi/N)

    lean = []
    tag = f"N{N}"
    psi_lean = lean_poly(Pexpr, "c")
    val_name = f"kashaev_{tag}_value"
    lean.append(f"/-- `⟨4₁⟩_{N}` modulo `Ψ_{N} = {psi_lean}`. -/")
    lean.append(f"theorem {val_name} {{R : Type*}} [CommRing R] (c : R) (hc : {psi_lean} = 0) :")
    lean.append(f"    kashaevFigureEight c {N} = {lean_poly(f, 'c')} := by")
    lean.append("  simp only [kashaevFigureEight, sum_range_succ, prod_range_succ, sum_range_zero,")
    lean.append("    prod_range_zero, dicksonC_add_two, dicksonC_one, dicksonC_zero, zero_add]")
    lean.append(f"  linear_combination ({lean_poly(Q.as_expr(), 'c')}) * hc")
    lean.append("")

    if deg == 1:
        val = sp.Rational(f.subs(x, c))
        info.update({"embedding_depth": 0, "decision_depth": 0, "value": str(val), "floor": int(sp.floor(val))})
        info["lean_lo"] = info["lean_hi"] = str(val)
        info["seconds"] = str(round(time.time() - t0, 2))
        return info, lean

    # Gonshor walk
    st = State(R(0), R(0), R(0), False, False)
    signs = []
    others = roots[:-1]
    depth = 0
    while any(in_window(st, rr) for rr in others) or not (st.hasLo and st.hasHi):
        plus = st.value < c
        signs.append("+" if plus else "-")
        st = st.step(plus)
        depth += 1
    d = depth
    emb_lo, emb_hi = st.lo, st.hi
    info["embedding_depth"] = d
    info["embedding_window"] = [str(emb_lo), str(emb_hi)]

    n_floor = int(sp.floor(f.subs(x, c)))
    info["floor"] = n_floor
    steps = []
    sign_thms = []
    hyp_lo, hyp_hi = "hlo", "hhi"
    cur_lo, cur_hi = emb_lo, emb_hi
    k = 0
    while True:
        lo_c = bernstein_cert(sp.expand(f - n_floor), cur_lo, cur_hi)
        hi_c = bernstein_cert(sp.expand(n_floor + 1 - f), cur_lo, cur_hi)
        if lo_c and hi_c:
            break
        plus = st.value < c
        v = st.value
        signs.append("+" if plus else "-")
        k += 1
        name = f"s{k}"
        if plus:  # v < c: exclude [cur_lo, v]
            s = 1 if P.eval(v) > 0 else -1
            cert = bernstein_cert(sp.expand(s * Pexpr), cur_lo, v)
            assert cert, (N, "exclusion", cur_lo, v)
            blk = exclusion_block(name, Pexpr, s, "bern", cur_lo, v, cert, "hlo", "hhi", False)
            sign_thms += sign_theorem(tag, k, psi_lean, cur_lo, cur_hi, f"{lean_qK(v)} < c", blk)
            steps.append(f"  have {name} := kashaev_{tag}_sign{k} hc {hyp_lo} {hyp_hi}")
            hyp_lo, cur_lo = name, v
        else:  # c < v (c irrational): exclude [v, cur_hi]
            s = 1 if P.eval(v) > 0 else -1
            cert = bernstein_cert(sp.expand(s * Pexpr), v, cur_hi)
            assert cert, (N, "exclusion", v, cur_hi)
            blk = exclusion_block(name, Pexpr, s, "bern", v, cur_hi, cert, "hlo", "hhi", True)
            sign_thms += sign_theorem(tag, k, psi_lean, cur_lo, cur_hi, f"c < {lean_qK(v)}", blk)
            steps.append(f"  have {name} := kashaev_{tag}_sign{k} hc {hyp_lo} {hyp_hi}")
            hyp_hi, cur_hi = name, v
        st = st.step(plus)
        if k > 200:
            raise RuntimeError("no decision by depth 200")
    info["decision_depth"] = d + k
    info["signs"] = "".join(signs)
    info["decision_window"] = [str(cur_lo), str(cur_hi)]

    lean += sign_thms
    fl = lean_poly(f, 'c')
    lean.append(f"/-- On the decision window `{cur_lo} < c < {cur_hi}`, `{n_floor} < r_{N}(c) < {n_floor + 1}`. -/")
    lean.append(f"theorem kashaev_{tag}_window {{K : Type*}} [Field K] [LinearOrder K] [IsStrictOrderedRing K]")
    lean.append(f"    {{c : K}} (hlo : {lean_qK(cur_lo)} < c) (hhi : c < {lean_qK(cur_hi)}) :")
    lean.append(f"    ({n_floor} : K) < {fl} ∧ {fl} < {n_floor + 1} := by")
    for which, cert, rhs in (("lo", lo_c, f"{fl} - {n_floor}"),
                             ("hi", hi_c, f"{n_floor + 1} - ({fl})")):
        n, cs = cert
        lean.append(f"  have b{which} := bernstein_pos (a := {lean_qK(cur_lo)}) (b := {lean_qK(cur_hi)}) (n := {n}) (c := coeffs {lean_list(cs)}) (x := c) (by norm_num) hlo.le hhi.le (by intro i hi; interval_cases i <;> norm_num [coeffs]) (by norm_num [coeffs]) (by norm_num [coeffs])")
        lean.append(f"  have e{which} : bernstein {lean_qK(cur_lo)} {lean_qK(cur_hi)} {n} (coeffs {lean_list(cs)}) c = {rhs} := by simp [bernstein, coeffs, sum_range_succ]; ring")
        lean.append(f"  rw [e{which}] at b{which}")
    lean.append("  constructor <;> linarith")
    lean.append("")
    lean.append(f"/-- **`{n_floor} < ⟨4₁⟩_{N} < {n_floor + 1}`.** Embedding: the Gonshor window after")
    lean.append(f"{d} signs, `{emb_lo} < c < {emb_hi}`, which holds only the largest root of `Ψ_{N}`.")
    lean.append(f"Decided after {k} more sign(s) (decision depth {d + k}); signs `{''.join(signs)}`. -/")
    lean.append(f"theorem kashaev_{tag}_floor {{K : Type*}} [Field K] [LinearOrder K] [IsStrictOrderedRing K]")
    lean.append(f"    {{c : K}} (hc : {psi_lean} = 0) (hlo : {lean_qK(emb_lo)} < c) (hhi : c < {lean_qK(emb_hi)}) :")
    lean.append(f"    ({n_floor} : K) < kashaevFigureEight c {N} ∧ kashaevFigureEight c {N} < {n_floor + 1} := by")
    lean += steps
    lean.append(f"  rw [{val_name} c hc]")
    lean.append(f"  exact kashaev_{tag}_window {hyp_lo} {hyp_hi}")
    lean.append("")
    info["seconds"] = str(round(time.time() - t0, 2))
    return info, lean


HEADER = '''import QOU.Core.TarskiSignKashaev

/-!
# QOU.Core.TarskiSignKashaevGen — `⌊⟨4₁⟩_N⌋` decided by certificates (generated)

**Generated by `computations/knots/tarski_sign_certificates.py`; do not edit by
hand.** Bean `qou-rc4t`. Every certificate below was produced in exact rational
arithmetic and is re-checked here by Lean.

For each `N` listed: `kashaev_N*_value` reduces `⟨4₁⟩_N` modulo the minimal
polynomial `Ψ_N` of `c = ζ_N + ζ_N⁻¹` (any commutative ring), and
`kashaev_N*_floor` decides `n < ⟨4₁⟩_N < n + 1` over any ordered field.

The embedding `ζ_N = e^{2πi/N}` enters only as the hypothesis that `c` lies in
the first Gonshor window holding no other root of `Ψ_N` (the *embedding
depth*). Every later sign is one exclusion certificate (`lt_of_excluded`,
`lt_of_excluded'` with `bernstein_pos`), and the floor is two Bernstein
certificates on the final window (the *decision depth*). No cosine, no `π`, no
`Coev`. The kashaev_chain theorem compares consecutive levels, which live in
different fields, through their integer floors.

No empirical value enters this file.
-/

namespace QOU.Core.TarskiSignKashaev.Gen

open Finset QOU.Core.TarskiSign QOU.Core.TarskiSignKashaev

'''


def main(argv):
    Ns = [int(a) for a in argv] or [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    infos, body = [], []
    for N in Ns:
        info, lean = process(N)
        print(json.dumps(info), flush=True)
        infos.append(info)
        body += lean
    # monotone chain between consecutive generated levels with distinct floors
    body.append("/-! ### The levels increase -/")
    body.append("")
    for a, b in zip(infos, infos[1:]):
        if a["floor"] + 1 > b["floor"]:
            continue
        def hyps(i, v):
            if i["deg_psi"] == 1:
                return f"(h{v} : {lean_poly(sp.sympify(i['psi']), 'c' + v)} = 0)"
            lo, hi = i["embedding_window"]
            return (f"(h{v} : {lean_poly(sp.sympify(i['psi']), 'c' + v)} = 0) "
                    f"(h{v}lo : {lean_qK(sp.Rational(lo))} < c{v}) (h{v}hi : c{v} < {lean_qK(sp.Rational(hi))})")
        def upper(i, v):
            if i["deg_psi"] == 1:
                return f"by norm_num [kashaev_N{i['N']}_value c{v} h{v}]"
            return f"(kashaev_N{i['N']}_floor h{v} h{v}lo h{v}hi).2"
        def lower(i, v):
            if i["deg_psi"] == 1:
                return f"by norm_num [kashaev_N{i['N']}_value c{v} h{v}]"
            return f"(kashaev_N{i['N']}_floor h{v} h{v}lo h{v}hi).1.le"
        Na, Nb = a["N"], b["N"]
        body.append(f"/-- `⟨4₁⟩_{Na} < ⟨4₁⟩_{Nb}`, through the integer separator `{a['floor'] + 1}`. -/")
        body.append(f"theorem kashaev_chain_{Na}_{Nb} {{K : Type*}} [Field K] [LinearOrder K] [IsStrictOrderedRing K]")
        body.append(f"    {{ca cb : K}} {hyps(a, 'a')} {hyps(b, 'b')} :")
        body.append(f"    kashaevFigureEight ca {Na} < kashaevFigureEight cb {Nb} := by")
        body.append(f"  have u : kashaevFigureEight ca {Na} < {a['floor'] + 1} := {upper(a, 'a')}")
        body.append(f"  have l : ({b['floor']} : K) ≤ kashaevFigureEight cb {Nb} := {lower(b, 'b')}")
        body.append(f"  have : ({a['floor'] + 1} : K) ≤ {b['floor']} := by norm_num")
        body.append("  linarith")
        body.append("")
    LEAN_OUT.write_text(HEADER + "\n".join(body) + "\nend QOU.Core.TarskiSignKashaev.Gen\n")
    from qou_substrate.witness import WitnessBuilder
    payload = {"producer": "computations/knots/tarski_sign_certificates.py",
               "bean": "qou-rc4t", "arithmetic": "exact (sympy Rational)",
               "levels": [{k: v for k, v in i.items() if k != "seconds"} for i in infos]}
    WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="sympy", engine_version=sp.__version__,
        q0_anchor=False,
        q0_anchor_reason="exact arithmetic in Q(zeta_N)+ at roots of unity; no q0 enters")
    WITNESS.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {LEAN_OUT.relative_to(REPO)} and {WITNESS.relative_to(REPO)}")


if __name__ == "__main__":
    main(sys.argv[1:])
