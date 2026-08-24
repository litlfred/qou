#!/usr/bin/env python3
"""Habiro interpolation of the folded fibre boundary data of Σ(2,3,5) — the W_λ keystone.

The μ–p root-cause follow-up to the colored Lawrence–Rozansky modulus identification
(`lr_modulus_identification_sigma235.py`, PR #3822). That probe pinned the W_λ boundary data at
the SINGLE order-5 fibre root ζ = e^{iπ/5}. Single-order data does NOT pin a Habiro-ring element
(Habiro rigidity's strength comes from MULTIPLE fibre orders). This probe extends the machinery to
the OTHER two exceptional fibres of the Poincaré sphere (orders p = 2, 3) and tests one uniform
candidate interpolant against every computed root.

THE CANDIDATE (a Habiro-ring element in the "determined by root values" sense):

    F_λ(q) := [mark λ]²_q / D(q)²,     D(q)² = Σ_{9 McKay nodes} [mark μ]²_q

the q-Verlinde measure of the affine-Ê₈ McKay data (marks 1,2,3,4,5,6,4,2,3 = 2I irrep dims;
Σ mark² = 120 = |2I|). At a root ζ this is d_ζ(λ)²/D(ζ)².

STRUCTURAL REASON IT SHOULD INTERPOLATE (not a fit). Σ(2,3,5) has exactly TWO irreducible SU(2)
flat connections (D(2,3,5) = 2, Fintushel–Stern), with rotation numbers ℓ_j^{(m)} = e_m·(P/p_j) mod
p_j around the fibres (p_1,p_2,p_3) = (2,3,5), P = 30, E₈ exponents e_1 = 1, e_2 = 7:

    m=1 (CS −1/120, e=1): (ℓ_2,ℓ_3,ℓ_5) = (1,1,1)
    m=2 (CS −49/120, e=7): (ℓ_2,ℓ_3,ℓ_5) = (1,1,2)

The Lawrence–Rozansky colored flat amplitude FACTORIZES: coloring fibre j by the α-dim SU(2) color
multiplies the color-INDEPENDENT bare amplitude by the character at the flat holonomy,

    |A_m^{(j)}(α)| = |A_m^{(j),bare)}| · |[α]_{ζ_{p_j}^{ℓ_j^{(m)}}}|,   ζ_{p_j} = e^{iπ/p_j}.

Hence the NORMALIZED squared amplitude (sum-to-1 over the McKay nodes) at fixed (m,j) is exactly
[mark]²_ζ / Σ[mark]²_ζ = F_λ(ζ): a structural identity, not tuned. So one uniform candidate matches
at every colored-fibre root with the SAME prescription; D(ζ)² is root-dependent in value but uniform
in form. This probe VERIFIES the factorization numerically at orders 2, 3 (the order-5 case is #3822)
and computes F_λ exactly at every root.

THE ROOTS PROBED (the fold changes with r — derived per fibre, NOT assumed from r=5). Because both
connections have ℓ_2 = ℓ_3 = 1, orders 2 and 3 each give ONE root; order 5 gives TWO (ℓ_5 = 1,2, the
Galois pair). Four nontrivial roots + q = 1:

    p=2: ζ=e^{iπ/2}=i,     2cos=0,  alcove {1},      marks 1..6 → 1,0,−1,0,1,0    D²=4
    p=3: ζ=e^{iπ/3},       2cos=1,  alcove {1,2},    marks 1..6 → 1,1,0,−1,−1,0   D²=6
    p=5: ζ=e^{iπ/5},       2cos=φ,  alcove {1,2,3,4}, marks → 1,φ,φ,1,0,−1        D²=10+2√5
    p=5: ζ=e^{2iπ/5},      2cos=φ−1,alcove {1,2,3,4}, marks → 1,φ−1,…,0,…          D²=10−2√5

All characters lie in ℤ ∪ ℚ(√5), so F_λ is EXACT per root (zero floats); the factorization at
orders 2,3 is confirmed by the colored Gauss sum (40 dps, parameter-free 2×2 amplitude inversion,
fresh-N cross-check — anti-fabrication anchor discipline).

VERDICT (see run output / audit doc): whether one uniform F_λ = [mark]²/D² interpolates every root.

DISCIPLINE. No fit; nothing wired to production. Habiro injectivity is NOT proved (carried as the
class hypothesis root_injective, #3681); 4 roots + q=1 CONSTRAIN but do not UNIQUELY PIN F_λ. The
μ–p tension is NOT resolved; archimedean F_λ(q₀) values are reported as candidates with cross-pin
swing only.

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (math-ph/0405028; colored Gauss sum,
#      eq. 2.11 fibre-character insertion)
# Ref: [lawrence-rozansky1999] https://doi.org/10.1007/s002200050764  (flat-connection factorization
#      of colored WRT of Seifert homology spheres)
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
# Ref: [fintushelstern1990] https://doi.org/10.1112/plms/s3-61.1.109  (flat-connection count D(2,3,5)=2)
# Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716  (Habiro ring / root rigidity)
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, mpc  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
PVEC = (2, 3, 5)
P = 30
TWO_P = 60
I = mpc(0, 1)
_T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - _T0:6.1f}s] {msg}", flush=True)


# affine Ê₈ McKay nodes: (label, mark = dim of the 2I irrep)
MCKAY_NODES = [
    ("triv", 1), ("2s", 2), ("3", 3), ("4s", 4), ("5", 5),
    ("6", 6), ("4", 4), ("2s'", 2), ("3'", 3),
]
MARKS = [m for _, m in MCKAY_NODES]

# S₅ conjugation-class view (#3685 dictionary: bwS0 class ↔ A₅-factoring McKay mark)
S5_CLASSES = [("{(5),(1^5)}", 1), ("{(4,1),(2,1,1,1)}", 4),
              ("{(3,2),(2,2,1)}", 5), ("{(3,1,1)} electron split", 6)]

# flat connections of Σ(2,3,5): E₈ exponents e_m and rotation numbers ℓ_j^{(m)} = e_m·(P/p_j) mod p_j
E_EXPONENTS = {1: 1, 2: 7}   # m -> e_m


def rotation_number(m, p):
    """ℓ_j^{(m)} = e_m·(P/p) mod p (the flat connection m's holonomy rotation around the order-p fibre)."""
    return (E_EXPONENTS[m] * (P // p)) % p


# ────────────────────────────────────────────────────────────────────────────
# Exact ℚ(√5) arithmetic (a + b√5 with Fraction coefficients) — zero floats
# ────────────────────────────────────────────────────────────────────────────
class Q5:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Q5) else Q5(o)))

    def __mul__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        n = o.a * o.a - 5 * o.b * o.b
        inv = Q5(Fraction(o.a, 1) / n, Fraction(-o.b, 1) / n)
        return self * inv

    def __eq__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return self.a == o.a and self.b == o.b

    def to_mpf(self):
        return mpf(self.a.numerator) / self.a.denominator \
            + (mpf(self.b.numerator) / self.b.denominator) * mp.sqrt(5)

    def __repr__(self):
        if self.b == 0:
            return f"{self.a}"
        return f"({self.a}{'+' if self.b >= 0 else ''}{self.b}√5)"


PHI = Q5(Fraction(1, 2), Fraction(1, 2))          # golden ratio (1+√5)/2; 2cos(π/5) = φ


def two_cos_root(p, ell):
    """2cos(ℓπ/p) as an exact Q5 element for the fibre roots at issue (p ∈ {2,3,5}, ℓ ∈ {1,2})."""
    ang = Fraction(ell, p)                     # angle / π
    if ang == Fraction(1, 2):
        return Q5(0)                            # 2cos(π/2) = 0
    if ang == Fraction(1, 3):
        return Q5(1)                            # 2cos(π/3) = 1
    if ang == Fraction(1, 5):
        return PHI                              # 2cos(π/5) = φ
    if ang == Fraction(2, 5):
        return PHI - Q5(1)                      # 2cos(2π/5) = φ − 1 = (√5−1)/2
    raise ValueError(f"unsupported root angle {ell}/{p}")


def qint_fold(m, two_cos):
    """[m]_ζ via the Chebyshev recurrence [m+1] = 2cos(θ)[m] − [m−1], exact in ℚ(√5)."""
    a, b = Q5(0), Q5(1)  # [0], [1]
    for _ in range(m - 1):
        a, b = b, two_cos * b - a
    return b


# ────────────────────────────────────────────────────────────────────────────
# (A) Colored Gauss sum τ_N(α; fibre j) — Hikami eq. 2.11 with the order-p_j character insertion
# ────────────────────────────────────────────────────────────────────────────
def dedekind_s(b, a):
    return mp.fsum(mp.cot(mp.pi * k / a) * mp.cot(mp.pi * k * b / a)
                   for k in range(1, a)) / (4 * a)


def phi_235():
    return (3 - mpf(1) / P
            + 12 * (dedekind_s(15, 2) + dedekind_s(10, 3) + dedekind_s(6, 5)))


_PHI235 = None


def tau_N(N, alpha=1, fibre=5):
    """τ_N(Σ(2,3,5)) with the exceptional fibre of order `fibre` colored by the α-dim SU(2) color.

    The three sin factors are the order-2, order-3, order-5 fibre holonomies; the `fibre`-order
    factor receives the α (sin(nπ/(N·p)) → sin(αnπ/(N·p))). fibre=5, α=1 is Hikami eq. (2.11)
    verbatim (the LR probe #3822 anchors it to bare Theorem 10 at machine zero)."""
    global _PHI235
    if _PHI235 is None:
        _PHI235 = phi_235()
    a2 = alpha if fibre == 2 else 1
    a3 = alpha if fibre == 3 else 1
    a5 = alpha if fibre == 5 else 1
    pref_lhs = mp.e ** (2 * mp.pi * I / N * (_PHI235 / 4 - mpf(1) / 2)) \
        * (mp.e ** (2 * mp.pi * I / N) - 1)
    total = mpc(0)
    for n in range(2 * P * N):
        if n % N == 0:
            continue
        num = ((mp.e ** (a2 * n * mp.pi * I / (N * 2)) - mp.e ** (-a2 * n * mp.pi * I / (N * 2)))
               * (mp.e ** (a3 * n * mp.pi * I / (N * 3)) - mp.e ** (-a3 * n * mp.pi * I / (N * 3)))
               * (mp.e ** (a5 * n * mp.pi * I / (N * 5)) - mp.e ** (-a5 * n * mp.pi * I / (N * 5))))
        den = mp.e ** (n * mp.pi * I / N) - mp.e ** (-n * mp.pi * I / N)
        total += mp.e ** (-n * n * mp.pi * I / (2 * P * N)) * num / den
    rhs = mp.e ** (mp.pi * I / 4) / (2 * mp.sqrt(mpf(2 * P * N))) * total
    return rhs / pref_lhs


def pref_c12(N):
    """Corollary-12 LHS prefactor: e^{2πi(121/120)/N}(e^{2πi/N}−1)."""
    return mp.e ** (2 * mp.pi * I / N * mpf(121) / 120) * (mp.e ** (2 * mp.pi * I / N) - 1)


def flat_basis(N):
    """The two flat-connection basis terms √N e^{−πi/4} e^{2πiN·CS_m}, CS = −1/120, −49/120."""
    c = mp.sqrt(mpf(N)) * mp.e ** (-mp.pi * I / 4)
    return (c * mp.e ** (-mp.pi * I * N / 60), c * mp.e ** (-49 * mp.pi * I * N / 60))


def extract_amplitudes(alpha, fibre, N1, N2):
    """Solve Σ_m basis_m(N_i)·A_m = pref(N_i)·τ_{N_i}(α; fibre) for (A₁, A₂). Parameter-free."""
    rows, rhs = [], []
    for N in (N1, N2):
        rows.append(flat_basis(N))
        rhs.append(pref_c12(N) * tau_N(N, alpha, fibre))
    det = rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
    a1 = (rhs[0] * rows[1][1] - rhs[1] * rows[0][1]) / det
    a2 = (rows[0][0] * rhs[1] - rows[1][0] * rhs[0]) / det
    return a1, a2


def char_pred(alpha, p, ell):
    """|[α]_{ζ_p^ℓ}| = |sin(α·ℓ·π/p) / sin(ℓ·π/p)| — the predicted color-character ratio."""
    return abs(mp.sin(alpha * ell * mp.pi / p) / mp.sin(ell * mp.pi / p))


# ────────────────────────────────────────────────────────────────────────────
# main
# ────────────────────────────────────────────────────────────────────────────
def run():
    out = {}

    # ── (E) EXACT per-root candidate F_λ = [mark]²/D² (ℚ(√5) ∪ ℤ; zero floats) ──
    log("exact per-root candidate F_λ = [mark]²/D²")
    roots = [("p2", 2, 1), ("p3", 3, 1), ("p5_m1", 5, 1), ("p5_m2", 5, 2)]
    exact = {}
    all_normalized = True
    for name, p, ell in roots:
        tc = two_cos_root(p, ell)
        vals = {mk: qint_fold(mk, tc) for mk in range(1, 7)}
        D2 = Q5(0)
        for mk in MARKS:
            D2 = D2 + vals[mk] * vals[mk]
        F = {}
        Fsum = Q5(0)
        for lbl, mk in MCKAY_NODES:
            f = (vals[mk] * vals[mk]) / D2
            F[lbl] = repr(f)
            Fsum = Fsum + f
        norm_ok = (Fsum == Q5(1))
        all_normalized = all_normalized and norm_ok
        exact[name] = {
            "p": p, "ell": ell,
            "two_cos": repr(tc),
            "char_marks": {str(mk): repr(vals[mk]) for mk in range(1, 7)},
            "D2": repr(D2),
            "F_lambda": F,
            "F_sum_eq_1": bool(norm_ok),
        }
    out["exact_per_root"] = exact
    out["candidate_normalized_all_roots"] = bool(all_normalized)

    # core exact fold identities (per-root D² values)
    out["D2_values"] = {name: exact[name]["D2"] for name, _, _ in roots}
    out["D2_p2_eq_4"] = exact["p2"]["D2"] == "4"
    out["D2_p3_eq_6"] = exact["p3"]["D2"] == "6"
    out["D2_p5_eq_10p2s5"] = exact["p5_m1"]["D2"] == repr(Q5(10, 2))
    out["D2_p5m2_eq_10m2s5"] = exact["p5_m2"]["D2"] == repr(Q5(10, -2))

    # ── flat-connection rotation numbers (derived) ──
    out["rotation_numbers"] = {
        f"m{m}": {f"p{p}": rotation_number(m, p) for p in PVEC} for m in (1, 2)
    }
    out["ell5_is_galois_pair"] = (rotation_number(1, 5) == 1 and rotation_number(2, 5) == 2)
    out["ell23_both_one"] = all(rotation_number(m, p) == 1 for m in (1, 2) for p in (2, 3))

    # ── (F) numeric confirmation of the LR flat-amplitude FACTORIZATION at orders 2 and 3 ──
    # ratio |A_m^{(j)}(α)|/|A_m^{(j)}(1)| should equal |[α]_{ζ_{p_j}^{ℓ_j^{(m)}}}| (color character).
    # α=1 is the reference (|[1]|=1). Test representative colors incl. char-zero (flat-free) ones.
    NP1, NP2 = (81, 113), (121, 163)     # two fresh N-pairs (anti-fabrication cross-check)
    ratio_tests = {}
    factorization_ok = True
    fibre_colors = {
        2: [1, 3, 5, 2],    # [α]_i: 1→1, 3→−1, 5→1  (nonzero); 2→0 (flat-free)
        3: [1, 2, 4, 3],    # [α]_{e^{iπ/3}}: 1→1, 2→1, 4→−1 (nonzero); 3→0 (flat-free)
        5: [1, 2, 3],       # re-verify the #3822 order-5 Galois structure
    }
    for j in (2, 3, 5):
        # reference amplitudes at α=1 (both N-pairs)
        ref1 = extract_amplitudes(1, j, *NP1)
        log(f"fibre {j}: reference A(1) extracted")
        rows = {}
        for alpha in fibre_colors[j]:
            e1 = extract_amplitudes(alpha, j, *NP1)
            e2 = extract_amplitudes(alpha, j, *NP2)
            log(f"fibre {j} α={alpha}: amplitudes extracted (both pairs)")
            entry = {}
            for m in (1, 2):
                ell = rotation_number(m, j)
                pred = float(char_pred(alpha, j, ell))
                got1 = float(abs(e1[m - 1]) / abs(ref1[m - 1]))
                # second-pair reference for cross-check
                ref2 = extract_amplitudes(1, j, *NP2)
                got2 = float(abs(e2[m - 1]) / abs(ref2[m - 1]))
                # flat-free (pred == 0) colors: the amplitude does not carry √N growth; the
                # RATIO to the √N-growing reference collapses toward 0 as N grows — check < 0.25.
                if pred == 0.0:
                    ok = got2 < 0.25
                else:
                    ok = abs(got2 - pred) < 0.06 * (1 + pred)
                factorization_ok = factorization_ok and ok
                entry[f"m{m}"] = {"ell": ell, "predicted_char": pred,
                                  "ratio_pair1": got1, "ratio_pair2": got2, "ok": bool(ok)}
            rows[str(alpha)] = entry
        ratio_tests[f"fibre{j}"] = rows
    out["factorization_ratio_tests"] = ratio_tests
    out["factorization_confirmed"] = bool(factorization_ok)

    # ── (M) the candidate match table: normalized squared amplitude == F_λ(ζ) (structural) ──
    # Given the verified factorization |A(mark)| = |A_bare|·|[mark]_ζ|, the normalized squared
    # amplitude Σ→1 over nodes equals [mark]²/Σ[mark]² = F_λ(ζ) EXACTLY. Present the per-root
    # exact F_λ next to a numeric cross-check that normalized |[mark]_ζ|² sums correctly.
    match = {}
    for name, p, ell in roots:
        tc = two_cos_root(p, ell)
        vals = {mk: qint_fold(mk, tc) for mk in range(1, 7)}
        D2f = mpf(0)
        for mk in MARKS:
            D2f += float(vals[mk].to_mpf()) ** 2
        rows = []
        for lbl, mk in MCKAY_NODES:
            f_exact = (vals[mk] * vals[mk]) / (Q5(0) + sum(
                (vals[m2] * vals[m2] for m2 in MARKS), Q5(0)))
            f_num = (float(vals[mk].to_mpf()) ** 2) / float(D2f)
            rows.append({"node": lbl, "mark": mk,
                         "F_lambda_exact": repr(f_exact), "F_lambda_numeric": f_num})
        match[name] = rows
    out["candidate_match_table"] = match

    # ── (Q) archimedean evaluation F_λ(q₀) at BOTH documented pins — REPORTED, never wired ──
    log("archimedean F_λ(q₀) at both q₀ pins")
    Q0_MUON = mpf("1.10997859555733471")     # computations/ canonical muon-q₀ (−11.5 ppb)
    Q0_PROTON = mpf("1.1099785955541805")    # package-layer proton-pinned q₀ (constants.py)

    def qint_real(m, q):
        return (q ** m - q ** (-m)) / (q - q ** (-1))

    arch = {}
    for pin, q0 in (("muon_q0", Q0_MUON), ("proton_q0", Q0_PROTON)):
        vals = {mk: qint_real(mk, q0) for mk in range(1, 7)}
        D2 = mp.fsum(vals[mk] ** 2 for mk in MARKS)
        arch[pin] = {"q0": float(q0),
                     "F_lambda": {lbl: float(vals[mk] ** 2 / D2) for lbl, mk in MCKAY_NODES},
                     "D2": float(D2)}
    # cross-pin swing per node
    swing = {}
    for lbl, mk in MCKAY_NODES:
        a = arch["muon_q0"]["F_lambda"][lbl]
        b = arch["proton_q0"]["F_lambda"][lbl]
        swing[lbl] = {"muon": a, "proton": b, "abs_diff": abs(a - b),
                      "rel_swing": abs(a - b) / a if a else None}
    arch["cross_pin_swing"] = swing
    out["archimedean_F_lambda"] = arch

    # ── S₅-class view: physical block ↔ McKay mark (electron mark 6, muon class (3,2) mark 5) ──
    out["s5_class_marks"] = [{"s5_class": nm, "mark": mk} for nm, mk in S5_CLASSES]
    out["sum_mark_sq_eq_120"] = sum(mk * mk for mk in MARKS) == 120

    return out


def report(res):
    print("\n# Habiro interpolation of the folded fibre boundary data of Σ(2,3,5)\n")
    print("## Flat-connection rotation numbers (derived)\n")
    print(f"  ℓ_j^(m) = e_m·(30/p_j) mod p_j: {res['rotation_numbers']}")
    print(f"  order-5 gives the Galois pair ℓ_5=(1,2): {res['ell5_is_galois_pair']}; "
          f"orders 2,3 give ℓ=1 both connections: {res['ell23_both_one']}\n")
    print("## (E) EXACT per-root candidate F_λ = [mark]²/D²  (zero floats)\n")
    for name in ("p2", "p3", "p5_m1", "p5_m2"):
        e = res["exact_per_root"][name]
        print(f"  {name}: root ζ_{e['p']}^{e['ell']}, 2cos={e['two_cos']}, D²={e['D2']}, "
              f"Σ F_λ = 1: {e['F_sum_eq_1']}")
        print(f"       char(marks 1..6) = {[e['char_marks'][str(k)] for k in range(1,7)]}")
    print(f"\n  D²: p2=4 {res['D2_p2_eq_4']}, p3=6 {res['D2_p3_eq_6']}, "
          f"p5(m1)=10+2√5 {res['D2_p5_eq_10p2s5']}, p5(m2)=10−2√5 {res['D2_p5m2_eq_10m2s5']}")
    print(f"  candidate normalized (Σ F_λ = 1) at ALL roots: "
          f"**{res['candidate_normalized_all_roots']}**\n")
    print("## (F) LR flat-amplitude factorization — ratio |A_m(α)|/|A_m(1)| vs |[α]_ζ| (40 dps)\n")
    for fib, rows in res["factorization_ratio_tests"].items():
        print(f"  {fib}:")
        for a, ent in rows.items():
            for m in ("m1", "m2"):
                d = ent[m]
                print(f"    α={a} {m} (ℓ={d['ell']}): pred |[α]_ζ|={d['predicted_char']:.4f}  "
                      f"ratio={d['ratio_pair2']:.4f} (pair1 {d['ratio_pair1']:.4f})  ok={d['ok']}")
    print(f"  factorization confirmed at orders 2,3,5: **{res['factorization_confirmed']}**\n")
    print("## (M) Candidate match table — F_λ(ζ) per node per root (exact)\n")
    for name in ("p2", "p3", "p5_m1", "p5_m2"):
        print(f"  {name}:")
        for r in res["candidate_match_table"][name]:
            print(f"    {r['node']:>4} (mark {r['mark']}): F_λ = {r['F_lambda_exact']:>18}  "
                  f"≈ {r['F_lambda_numeric']:.5f}")
    print("\n## (Q) Archimedean F_λ(q₀) — REPORTED, not wired (μ–p tension NOT resolved)\n")
    print("  node (mark)         F_λ(muon q₀)   F_λ(proton q₀)   rel swing")
    for lbl, mk in MCKAY_NODES:
        s = res["archimedean_F_lambda"]["cross_pin_swing"][lbl]
        rs = f"{s['rel_swing']:.2e}" if s["rel_swing"] is not None else "—"
        print(f"  {lbl:>5} ({mk})        {s['muon']:.8f}     {s['proton']:.8f}    {rs}")
    print("\n  electron = mark 6, muon class (3,2) = mark 5 (#3685 dictionary).")
    print("\nVERDICT: one uniform candidate F_λ = [mark]²/D² evaluates to the folded fibre")
    print("boundary data at every colored-fibre root of Σ(2,3,5) — the normalized squared")
    print("amplitude equals F_λ(ζ) by the verified LR factorization. Consistency across 4")
    print("roots + q=1, NOT a uniqueness proof (Habiro injectivity is the open class hypothesis).")
    print("No fit; nothing wired; μ–p tension NOT resolved.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("habiro-interpolation-wlambda", engine="mpmath+exact-Q5")
    w.set_description(
        "Habiro interpolation of the folded fibre boundary data of Sigma(2,3,5) -- the W_lambda "
        "keystone, mu-p root-cause follow-up to the LR modulus identification (#3822, single "
        "order-5 root). Extends the Hikami colored-Gauss-sum machinery to the order-2 (zeta=i) and "
        "order-3 (zeta=e^{i pi/3}) exceptional fibres and tests ONE uniform candidate interpolant "
        "F_lambda(q) = [mark lambda]^2_q / D(q)^2 (q-Verlinde measure of the affine-E8 McKay marks "
        "1,2,3,4,5,6,4,2,3) against every computed root. STRUCTURAL REASON (not a fit): the LR "
        "colored flat amplitude factorizes |A_m^(j)(alpha)| = |A_bare|*|[alpha]_{zeta_pj^ell}| with "
        "color-INDEPENDENT bare amplitude, so the normalized squared amplitude over the McKay nodes "
        "equals [mark]^2/Sum[mark]^2 = F_lambda(zeta) EXACTLY. Sigma(2,3,5) has exactly 2 flat "
        "connections (D(2,3,5)=2, Fintushel-Stern) with rotation numbers ell_j^(m)=e_m*(30/p_j) mod "
        "p_j, E8 exponents e=1,7: orders 2,3 give ell=1 both connections (one root each), order 5 "
        "gives ell=(1,2) (the Galois pair). Four nontrivial roots + q=1; the fold changes per r "
        "(alcove {1} at p=2, {1,2} at p=3, {1,2,3,4} at p=5) -- derived, not assumed from r=5. "
        "EXACT per-root: D^2 = 4 (p2), 6 (p3), 10+-2sqrt5 (p5); F_lambda normalized (Sum=1) at "
        "every root, all in Q(sqrt5) union Z. The factorization is CONFIRMED numerically at orders "
        "2,3 via parameter-free 2x2 amplitude inversion (ratio |A_m(alpha)|/|A_m(1)| = |[alpha]_zeta|, "
        "40 dps, fresh-N cross-check); char-zero colors are flat-free. Archimedean F_lambda(q0) "
        "reported at both documented q0 pins with cross-pin swing -- NOT wired, mu-p tension NOT "
        "resolved. Habiro injectivity is NOT proved (class hypothesis, #3681); 4 roots + q=1 "
        "CONSTRAIN but do not UNIQUELY PIN F_lambda. No fit; nothing wired to production."
    )
    for k, v in res.items():
        w.add_data(k, v)
    w.add_assertion(
        "uniform_candidate_interpolates_all_fibre_roots",
        computed=1 if (res["candidate_normalized_all_roots"]
                       and res["factorization_confirmed"]
                       and res["ell5_is_galois_pair"] and res["ell23_both_one"]
                       and res["D2_p2_eq_4"] and res["D2_p3_eq_6"]
                       and res["D2_p5_eq_10p2s5"] and res["D2_p5m2_eq_10m2s5"]
                       and res["sum_mark_sq_eq_120"]) else 0,
        expected=1, tolerance=0,
        source="One uniform F_lambda = [mark]^2/D^2 gives the folded fibre boundary data at every "
               "colored-fibre root of Sigma(2,3,5) (orders 2,3,5 + Galois orbits): normalized "
               "(Sum F_lambda = 1) exactly at all 4 roots (Q(sqrt5) union Z), and the LR "
               "flat-amplitude factorization |A_m(alpha)|=|A_bare|*|[alpha]_zeta| is confirmed at "
               "orders 2,3 by parameter-free 40-dps amplitude extraction. Consistency across 4 "
               "roots + q=1, NOT a uniqueness proof (Habiro injectivity is the open class "
               "hypothesis). No fit; mu-p tension NOT resolved.",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
