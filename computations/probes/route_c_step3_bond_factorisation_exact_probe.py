#!/usr/bin/env python3
"""Route C step 3 (bean qou-8uxw, candidate S3 of
docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md §A): EXACT-in-q bond
factorisation of the canonical NON-monotone nucleon word at n = 9 (A = 3).

THE QUESTION (one, exact). Let β_free be three nucleon blocks on disjoint strand
triples with NO interface, β_12 / β_23 exactly ONE interface switched on, β_123
both, all built by the canonical constructor
`canonical_braid_crossings.atom_canonical_crossings(Z, N, m_pp, m_pn, m_nn,
ordering)` → `mass_at_3A_proper.atom_braid_word_3A` (intra word
`pyhecke.atom.nucleon_word_letters`, default `intra_order="borromean"`, per-nucleon
generator sequence `[0,1,0,1,0,1,0,0,1,0,0]`, interface at generator 3k+2,
`pn_convention="bring_color_weighted"` — the canonical p/n convention, AGENTS.md
R3).  With

    C(w) := q^{l(w)} · [2]_q^n · tr_D(w),      tr_D(X) = tr(K^{⊗n} X) / [2]_q^n,
    K = diag(q⁻¹ [bit 0], q [bit 1]),   R = swap + diag(q−1 on |00⟩,|11⟩; h on |10⟩),

exactly the spin-½ convention-D trace of `c2_diagonal_insertion_expansion_probe`
(the ε² probe) and of `route_c_step2_pivotal_vs_count_probe` (up to the global
bit-flip symmetry), does

    C(β_123) · C(β_free)  =  C(β_12) · C(β_23)

hold IDENTICALLY as Laurent polynomials in q?  Equivalently
tr_D(β_123)·tr_D(β_free) = tr_D(β_12)·tr_D(β_23), since l(β_123)+l(β_free) =
l(β_12)+l(β_23) and the [2]^n factors cancel.

METHOD (no floats anywhere).  Every letter is the Hecke element σ_g + d·1 with
d ∈ {0, −h, −h/2, −h(1/2 − δ/4)}, h = q − q⁻¹, δ = (q−1)²(1−q⁻⁴)/3
(`_li_2_q_util.flavor_split_leading`, exact in q).  Multiply each letter by
12·q⁵ so that ℓ_i := 12q⁵(σ + d_i) has INTEGER polynomial entries; then

    P(w)(q) := tr( q⁹ K^{⊗9} · ∏ ℓ_i ) = 12^{l(w)} q^{4 l(w) + 9} C(w)(q)  ∈ ℤ[q].

P is evaluated at integer q on weight-sector sparse vectors (R preserves the
number of 1-bits; sector dims ≤ C(9,4) = 126) with Python big integers, divided
by its provable minimum power q^{4·l_reg} (l_reg = number of non-pn letters; the
pn letter's ℓ has minimum degree 0), Newton-interpolated over `Fraction` from
span+3 points, and the interpolant is verified at THREE further prime-power q
values not used in the fit.  Δ := C(β_123)C(β_free) − C(β_12)C(β_23) is then an
exact Laurent polynomial; its (q−1)-adic order is read off by the exact
substitution q = 1 + ε.

Compositions: ppn, pnn, ppp, nnn — the construction distinguishes all four
(pp interface σ, nn interface σ⁻¹, pn colour-weighted average), so all four are
run.  The ε²-truncation of the exact result is cross-checked against the FIVE
recorded input series of `atom_bond_product_closed_form_probe.py` (nucleon
p: ½(1, 3/2, 23/4), n: ½(1, −1, 3); bond pp ½(1, 2, 1/2), pn ½(1, 0, 3/2),
nn ½(1, −2, 5/2)).

NO FITTING: no word, ordering, letter or cutoff is chosen for its number — every
object is the canonical constructor's output with interfaces toggled by the
`m_pp/m_pn/m_nn` multiplicities exactly as the ε² probe toggles them.  q₀ is an
INPUT only (forever-gate), read for the diagnostic line alone; the identity is
q-formal.  Scope: (b) at n = 9 on the canonical word if Δ ≡ 0, with the identity
itself as the invariant; the general-A Lean statement (MarkovBondFactor.lean,
general case) stays open either way.

Run:  PYTHONPATH=computations python3 -u \\
        computations/probes/route_c_step3_bond_factorisation_exact_probe.py \\
        2>&1 | tee /tmp/routec-a1-run.log
"""
from __future__ import annotations

import os
import sys
import time
from fractions import Fraction as F
from multiprocessing import Pool

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
except Exception:  # pragma: no cover
    Q_50_DIGIT_STR = None
try:
    from qou_substrate import constants as _c  # noqa: E402
    M_E_MEV_STR = str(_c._E_MEV.value_str)  # the CODATA string itself
except Exception:  # pragma: no cover
    M_E_MEV_STR = None

mp.mp.dps = 50
T0 = time.monotonic()
N_STRANDS = 9
B3_TARGET_MEV = F(2852445, 2000000)      # QOU/MassTheory/AmeBindingNotPairwise.lean:24 (quoted)
MU3_TARGET_MEV_QUOTED = "0.4708"         # BorromeanThreeBodyCluster.lean docstring (quoted)

# Recorded ε²-series inputs of atom_bond_product_closed_form_probe.py (measured there at
# n = 3 and at A = 3 with ONE interface on).  Format: a·(1, r, q) as [a, a r, a q].
REC_NUC = {"p": [F(1, 2), F(3, 4), F(23, 8)], "n": [F(1, 2), F(-1, 2), F(3, 2)]}
REC_BOND = {"pp": [F(1, 2), F(1), F(1, 4)], "pn": [F(1, 2), F(0), F(3, 4)],
            "nn": [F(1, 2), F(-1), F(5, 4)]}


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:6.1f}s] {msg}", flush=True)


# ─────────────────────────────────────────────────────────────────────────────
#  exact integer evaluation of P(w)(q)
# ─────────────────────────────────────────────────────────────────────────────
def _letter_ints(kind: str, q: int) -> tuple[int, int, int, int]:
    """Integer data of ℓ = 12q⁵(σ + d) at integer q: (diag_equal, swap, diag_10, d).
    σ: q on |00⟩,|11⟩; 1 on the swap; h on |10⟩ (site g = 1, site g+1 = 0); 0 on |01⟩."""
    a = 12 * q ** 6                    # 12q⁵ · q
    s = 12 * q ** 5                    # 12q⁵ · 1
    hh = 12 * q ** 4 * (q * q - 1)     # 12q⁵ · h
    if kind == "sigma":
        d = 0
    elif kind == "sigma_inv":
        d = -hh
    elif kind == "averaged":
        d = -6 * q ** 4 * (q * q - 1)  # 12q⁵ · (−h/2)
    elif kind == "averaged_weighted":
        # 12q⁵·(−h(1/2 − δ/4)) = −6q⁴(q²−1) + 3q⁵ h δ,  3q⁵hδ = (q²−1)(q−1)²(q⁴−1)
        d = -6 * q ** 4 * (q * q - 1) + (q * q - 1) * (q - 1) ** 2 * (q ** 4 - 1)
    else:
        raise ValueError(kind)
    return a, s, hh, d


def eval_P(args):
    """P(w)(q) = Σ_b q^{2·popcount(b)} ⟨b| ℓ_0 ℓ_1 … ℓ_{L−1} |b⟩ as an exact integer.
    The rightmost letter acts first (state passes letters L−1, …, 0), mirroring
    `c2_diagonal_insertion_expansion_probe.trace_expansion`."""
    word, q = args
    n = N_STRANDS
    lets = [(g, _letter_ints(kind, q)) for g, kind in word]
    order = list(range(len(lets) - 1, -1, -1))
    total = 0
    for b in range(1 << n):
        vec = {b: 1}
        for idx in order:
            g, (a, s, hh, d) = lets[idx]
            mg, mg1 = 1 << g, 1 << (g + 1)
            new = {}
            for st, c in vec.items():
                bg, bg1 = (st >> g) & 1, (st >> (g + 1)) & 1
                if bg == bg1:
                    new[st] = new.get(st, 0) + c * (a + d)
                else:
                    sw = st ^ (mg | mg1)
                    new[sw] = new.get(sw, 0) + c * s
                    diag = (hh + d) if (bg == 1 and bg1 == 0) else d
                    if diag:
                        new[st] = new.get(st, 0) + c * diag
            vec = new
        c = vec.get(b, 0)
        if c:
            total += c * q ** (2 * bin(b).count("1"))
    return q, total


def degree_bounds(word):
    """(min, max) degree of P(w) in q: ℓ has degree [4, 6] for non-pn letters and
    [0, 8] for the colour-weighted pn letter; the weight q^{2·popcount} adds [0, 18]."""
    lo = hi = 0
    for _, kind in word:
        if kind == "averaged_weighted":
            hi += 8
        else:
            lo += 4
            hi += 6
    return lo, hi + 2 * N_STRANDS


def newton_interpolate(xs: list[int], ys: list[F]) -> list[F]:
    """Coefficients c_0..c_m (ascending) of the unique polynomial of degree ≤ m through
    (xs, ys), exact over Fraction (Newton divided differences, then expansion)."""
    m = len(xs)
    dd = [F(y) for y in ys]
    coef_newton = [dd[0]]
    for k in range(1, m):
        dd = [(dd[i + 1] - dd[i]) / (xs[i + k] - xs[i]) for i in range(m - k)]
        coef_newton.append(dd[0])
    poly = [F(0)] * m
    # Horner-style expansion of Σ c_k ∏_{j<k}(x − x_j)
    for k in range(m - 1, -1, -1):
        # poly ← poly·(x − x_k) + c_k
        new = [F(0)] * m
        for i in range(m - 1):
            if poly[i]:
                new[i + 1] += poly[i]
                new[i] -= poly[i] * xs[k]
        new[0] += coef_newton[k]
        poly = new
    return poly


def poly_eval(coefs: list[F], x) -> F:
    acc = F(0)
    for c in reversed(coefs):
        acc = acc * x + c
    return acc


def laurent_C(word, pool, extra_points=(121, 125, 128)) -> tuple[dict, dict]:
    """Exact Laurent polynomial C(w) = Σ c_k q^k as {k: Fraction}, plus a check record."""
    L = len(word)
    lo, hi = degree_bounds(word)
    span = hi - lo
    npts = span + 3
    xs = list(range(2, 2 + npts))
    t = time.monotonic()
    vals = dict(pool.map(eval_P, [(word, x) for x in xs + list(extra_points)], chunksize=1))
    dt = time.monotonic() - t
    # divide out the provable minimum power q^lo (exact integer division)
    ys = []
    for x in xs:
        v, rem = divmod(vals[x], x ** lo)
        assert rem == 0, f"P not divisible by q^{lo} at q={x}"
        ys.append(F(v))
    coefs = newton_interpolate(xs, ys)
    # verification at points NOT used in the interpolation
    verified = all(poly_eval(coefs, x) * x ** lo == vals[x] for x in extra_points)
    top_zero = all(c == 0 for c in coefs[span + 1:])   # degree bound respected
    # C = P / (12^L q^{4L+9})
    scale = F(1, 12 ** L)
    # P used q^9 K^{⊗9} = q^{2·popcount} and ∏ℓ = 12^L q^{5L} w, so C = P / (12^L q^{4L + 9}).
    shift = lo - 4 * L - N_STRANDS
    C = {k + shift: c * scale for k, c in enumerate(coefs) if c != 0}
    rec = {"length": L, "n_pn_letters": sum(1 for _, k in word if k == "averaged_weighted"),
           "degree_bounds_P": [lo, hi], "sample_points": [xs[0], xs[-1]], "n_samples": npts,
           "verification_points": list(extra_points), "verified_at_extra_points": verified,
           "degree_bound_respected": top_zero, "eval_seconds": f"{dt:.1f}",
           "laurent_degree_range": [min(C), max(C)]}
    return C, rec


# ─────────────────────────────────────────────────────────────────────────────
#  exact Laurent-polynomial arithmetic over Fraction
# ─────────────────────────────────────────────────────────────────────────────
def lmul(a: dict, b: dict) -> dict:
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, 0) + x * y
    return {k: v for k, v in out.items() if v != 0}


def lsub(a: dict, b: dict) -> dict:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v != 0}


def to_sympy(a: dict, q):
    return sp.Add(*[sp.Rational(v.numerator, v.denominator) * q ** k for k, v in a.items()]) if a else sp.Integer(0)


def eps_series(a: dict, K: int) -> list[F]:
    """Exact [ε^j], j ≤ K, of Σ c_k (1+ε)^k (generalised binomial for negative k)."""
    out = [F(0)] * (K + 1)
    for k, c in a.items():
        binom = F(1)
        for j in range(K + 1):
            if j:
                binom = binom * (k - j + 1) / j
            out[j] += c * binom
    return out


def ser_mul(a, b, K):
    out = [F(0)] * (K + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= K:
                out[i + j] += x * y
    return out


def ser_div(a, b, K):
    out = []
    for j in range(K + 1):
        s = a[j] - sum(out[i] * b[j - i] for i in range(j))
        out.append(s / b[0])
    return out


def trD_series(C: dict, L: int, K: int = 2) -> list[F]:
    """tr_D = C / (q^L [2]^n) to order ε^K, exactly."""
    two = {1: F(1), -1: F(1)}
    den = {L: F(1)}
    for _ in range(N_STRANDS):
        den = lmul(den, two)
    return ser_div(eps_series(C, K), eps_series(den, K), K)


def q_adic_order(a: dict, max_order: int = 400):
    """(q−1)-adic order of a Laurent polynomial: smallest j with [ε^j] ≠ 0 (None if a ≡ 0)."""
    if not a:
        return None, None
    K = max(abs(k) for k in a) + 2
    s = eps_series(a, min(K, max_order))
    for j, v in enumerate(s):
        if v != 0:
            return j, v
    return None, None


# ─────────────────────────────────────────────────────────────────────────────
def main() -> int:
    print("=" * 84)
    print(" route C step 3: EXACT-in-q bond factorisation of the canonical nucleon word, n = 9")
    print("=" * 84)
    q = sp.symbols("q", positive=True)
    checks: list[tuple[str, bool]] = []
    comps = {"ppn": ("pp", "pn"), "pnn": ("pn", "nn"), "ppp": ("pp", "pp"), "nnn": ("nn", "nn")}
    results = {}

    with Pool(min(4, os.cpu_count() or 1)) as pool:
        for comp, (b1, b2) in comps.items():
            ordering = list(comp)
            Z, N = comp.count("p"), comp.count("n")

            # interface k (k = 0, 1) sits at generator 3k+2 between nucleons k and k+1; its
            # multiplicity is selected by the BOND TYPE, exactly as the ε² probe's
            # `_series(..., m_pp=, m_pn=, m_nn=)` toggles it.
            free = atom_canonical_crossings(Z, N, include_inter=False, ordering=ordering)
            if b1 != b2:
                mk12 = {"m_pp": 0, "m_pn": 0, "m_nn": 0}; mk12["m_" + b1] = 1
                mk23 = {"m_pp": 0, "m_pn": 0, "m_nn": 0}; mk23["m_" + b2] = 1
                w12 = atom_canonical_crossings(Z, N, include_inter=True, ordering=ordering, **mk12)
                w23 = atom_canonical_crossings(Z, N, include_inter=True, ordering=ordering, **mk23)
                w123 = atom_canonical_crossings(Z, N, include_inter=True, ordering=ordering,
                                                m_pp=1, m_pn=1, m_nn=1)
            else:
                # Same bond type twice: the constructor's multiplicity toggles both together, so
                # β_12 / β_23 are obtained by DELETING the other interface letter from β_123
                # (the letter at generator 5 / generator 2 respectively).  The letters are the
                # constructor's own; nothing is re-typed.
                w123 = atom_canonical_crossings(Z, N, include_inter=True, ordering=ordering,
                                                m_pp=1, m_pn=1, m_nn=1)
                inter_idx = [i for i, (g, k) in enumerate(w123) if g in (2, 5)]
                assert len(inter_idx) == 2 and [w123[i][0] for i in inter_idx] == [2, 5]
                w12 = [x for i, x in enumerate(w123) if i != inter_idx[1]]
                w23 = [x for i, x in enumerate(w123) if i != inter_idx[0]]
            # structural sanity: interfaces are exactly the letters at generators 2 and 5
            n_int = {nm: sum(1 for g, _ in w if g in (2, 5)) for nm, w in
                     (("free", free), ("12", w12), ("23", w23), ("123", w123))}
            checks.append((f"{comp}: interface counts free/12/23/123 = 0/1/1/2",
                           n_int == {"free": 0, "12": 1, "23": 1, "123": 2}))
            checks.append((f"{comp}: l(123)+l(free) = l(12)+l(23)",
                           len(w123) + len(free) == len(w12) + len(w23)))
            per_nuc = [g for g, _ in free[:11]]
            checks.append((f"{comp}: first nucleon block is the canonical non-monotone word [0,1,0,1,0,1,0,0,1,0,0]",
                           per_nuc == [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]))
            log(f"{comp}: words built, lengths free {len(free)} / 12 {len(w12)} / 23 {len(w23)} / 123 {len(w123)}; "
                f"interface letters 12: {[k for g, k in w12 if g in (2, 5)]}, 23: {[k for g, k in w23 if g in (2, 5)]}")

            Cs, recs = {}, {}
            for nm, w in (("free", free), ("12", w12), ("23", w23), ("123", w123)):
                Cs[nm], recs[nm] = laurent_C(w, pool)
                checks.append((f"{comp}: C({nm}) interpolant verified at 3 unused prime-power q values",
                               recs[nm]["verified_at_extra_points"]))
                checks.append((f"{comp}: C({nm}) degree bound respected", recs[nm]["degree_bound_respected"]))
                log(f"{comp}: C({nm}) done — {recs[nm]['n_samples']} samples in {recs[nm]['eval_seconds']}s, "
                    f"Laurent degrees {recs[nm]['laurent_degree_range']}, verified {recs[nm]['verified_at_extra_points']}")

            lhs = lmul(Cs["123"], Cs["free"])
            rhs = lmul(Cs["12"], Cs["23"])
            delta = lsub(lhs, rhs)
            holds = not delta
            order, lead = q_adic_order(delta)
            checks.append((f"{comp}: C(123)·C(free) − C(12)·C(23) ≡ 0 as a Laurent polynomial", holds))
            log(f"{comp}: Δ ≡ 0: {holds}" + ("" if holds else f"; (q−1)-adic order {order}, leading coefficient {lead}"))

            # ε²-cross-check against the recorded series of atom_bond_product_closed_form_probe
            K = 2
            s_free = trD_series(Cs["free"], len(free), K)
            s_12 = trD_series(Cs["12"], len(w12), K)
            s_23 = trD_series(Cs["23"], len(w23), K)
            s_123 = trD_series(Cs["123"], len(w123), K)
            pred_free = [F(1), F(0), F(0)]
            for nuc in ordering:
                pred_free = ser_mul(pred_free, REC_NUC[nuc], K)
            bond1 = ser_div(s_12, s_free, K)
            bond2 = ser_div(s_23, s_free, K)
            bond1_in_123 = ser_div(s_123, s_23, K)
            bond2_in_123 = ser_div(s_123, s_12, K)
            checks.append((f"{comp}: tr_D(free) to ε² = product of the recorded nucleon series", s_free == pred_free))
            checks.append((f"{comp}: bond {b1} (from β_12/β_free) to ε² = recorded ½(1,ρ,τ)", bond1 == REC_BOND[b1]))
            checks.append((f"{comp}: bond {b2} (from β_23/β_free) to ε² = recorded ½(1,ρ,τ)", bond2 == REC_BOND[b2]))
            checks.append((f"{comp}: bond {b1} extracted with the other interface ON equals the recorded one to ε²",
                           bond1_in_123 == REC_BOND[b1]))
            log(f"{comp}: ε² cross-check — free {[str(x) for x in s_free]} vs recorded product {[str(x) for x in pred_free]}; "
                f"bond {b1} {[str(x) for x in bond1]}, bond {b2} {[str(x) for x in bond2]}")

            # exact bond factors as rational functions, and the STRONGER fact they turn out to obey:
            # C(one)/C(free) = q·(z_D + d_bond) with z_D = q³/(q²+1) and d_bond the interface letter's
            # own Hecke shift — the Markov scalar of the interface letter, which is the
            # gap-multiplicativity mechanism bean qou-g8i1 names (there as a mechanism, not a proof).
            f1 = sp.factor(to_sympy(Cs["12"], q) / to_sympy(Cs["free"], q))
            f2 = sp.factor(to_sympy(Cs["23"], q) / to_sympy(Cs["free"], q))
            f1_alt = sp.factor(to_sympy(Cs["123"], q) / to_sympy(Cs["23"], q))
            f2_alt = sp.factor(to_sympy(Cs["123"], q) / to_sympy(Cs["12"], q))
            hq = q - 1 / q
            dlt = (q - 1) ** 2 * (1 - q ** -4) / 3
            d_of = {"pp": sp.Integer(0), "nn": -hq, "pn": -hq * (sp.Rational(1, 2) - dlt / 4)}
            z_D = q ** 3 / (q ** 2 + 1)
            markov1 = sp.simplify(f1 - q * (z_D + d_of[b1])) == 0
            markov2 = sp.simplify(f2 - q * (z_D + d_of[b2])) == 0
            checks.append((f"{comp}: C(12)/C(free) = q·(z_D + d_{b1}) exactly (Markov scalar of the interface letter)", markov1))
            checks.append((f"{comp}: C(23)/C(free) = q·(z_D + d_{b2}) exactly (Markov scalar of the interface letter)", markov2))
            checks.append((f"{comp}: C(123)/C(23) = C(12)/C(free) and C(123)/C(12) = C(23)/C(free) exactly",
                           sp.simplify(f1_alt - f1) == 0 and sp.simplify(f2_alt - f2) == 0))
            results[comp] = {
                "ordering": ordering, "bonds": [b1, b2],
                "word_lengths": {"free": len(free), "12": len(w12), "23": len(w23), "123": len(w123)},
                "interface_letter_kinds": {"12": [k for g, k in w12 if g in (2, 5)], "23": [k for g, k in w23 if g in (2, 5)]},
                "interpolation": recs,
                "C_laurent": {nm: {str(k): str(v) for k, v in sorted(Cs[nm].items())} for nm in Cs},
                "C_factored": {nm: str(sp.factor(to_sympy(Cs[nm], q))) for nm in Cs},
                "Delta_identically_zero": holds,
                "Delta_laurent": {str(k): str(v) for k, v in sorted(delta.items())},
                "Delta_factored": str(sp.factor(to_sympy(delta, q))) if delta else "0",
                "Delta_q_minus_1_adic_order": order, "Delta_leading_coefficient": str(lead) if lead is not None else None,
                "bond_factor_12_over_free": str(f1), "bond_factor_23_over_free": str(f2),
                "bond_factor_123_over_23": str(f1_alt), "bond_factor_123_over_12": str(f2_alt),
                "bond_factor_equals_q_times_zD_plus_d": {b1 + "_12": markov1, b2 + "_23": markov2},
                "z_D": str(z_D), "d_" + b1: str(sp.factor(d_of[b1])), "d_" + b2: str(sp.factor(d_of[b2])),
                "eps2_cross_check": {"trD_free": [str(x) for x in s_free], "recorded_product": [str(x) for x in pred_free],
                                     "bond_" + b1: [str(x) for x in bond1], "bond_" + b2: [str(x) for x in bond2],
                                     "bond_" + b1 + "_with_other_on": [str(x) for x in bond1_in_123],
                                     "bond_" + b2 + "_with_other_on": [str(x) for x in bond2_in_123],
                                     "recorded_" + b1: [str(x) for x in REC_BOND[b1]], "recorded_" + b2: [str(x) for x in REC_BOND[b2]]},
            }
            log(f"{comp}: bond factors  {b1}: {f1}   {b2}: {f2}")

    # ── diagnostic at the proton pin (comparison boundary; nothing adjusted) ──
    anchor = {}
    if Q_50_DIGIT_STR is not None:
        q0 = Q_MP
        anchor = {"q0": Q_50_DIGIT_STR, "h0": mp.nstr(q0 - 1 / q0, 30), "eps0": mp.nstr(q0 - 1, 30)}
        if M_E_MEV_STR is not None:
            me = mp.mpf(M_E_MEV_STR)
            import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
            E0 = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
            anchor.update({"m_e_MeV": M_E_MEV_STR, "E0_MeV": mp.nstr(E0, 30),
                           "b3_target_MeV_quoted": str(B3_TARGET_MEV), "mu3_target_MeV_quoted": MU3_TARGET_MEV_QUOTED})
            for comp, r in results.items():
                if r["Delta_identically_zero"]:
                    anchor[f"{comp}_Delta_at_pin"] = "0 (identity holds exactly; no many-body term to evaluate)"
                else:
                    m, c = r["Delta_q_minus_1_adic_order"], F(r["Delta_leading_coefficient"])
                    cm = mp.mpf(c.numerator) / c.denominator
                    hm = (q0 - 1 / q0) ** m
                    anchor[f"{comp}_Delta_leading_E0_h^m_coeff_MeV"] = mp.nstr(E0 * hm * cm, 20)
                    anchor[f"{comp}_Delta_order"] = m
    else:
        log("q_parameter not importable — pin diagnostic skipped")

    ok = 0
    print()
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")
    all_hold = all(r["Delta_identically_zero"] for r in results.values())
    verdict = (
        "bond factorisation holds EXACTLY at n = 9 on the canonical word: for every composition "
        "(ppn, pnn, ppp, nnn) C(β_123)·C(β_free) = C(β_12)·C(β_23) identically as Laurent polynomials "
        "in q, i.e. the two-bond word's convention-D trace is the free word's trace times the two "
        "one-bond factors, each extracted with the other interface OFF or ON — and each one-bond factor "
        "is EXACTLY q·(z_D + d_bond), the Markov scalar of the interface letter (z_D = q³/(q²+1); "
        "pp: q⁴/(q²+1), nn: 1/(q²+1), pn: q·(z_D − h(1/2 − δ/4))), which is the gap-multiplicativity "
        "mechanism of bean qou-g8i1 made exact at A = 3 and the ∏(z + dᵢ) law that "
        "mass_at_3A_proper.atom_braid_word_3A's docstring records to ~1e-60. Scope (b) at n = 9, "
        "invariant = the identity itself (exact, interpolated from span+3 integer q and verified at 3 "
        "unused prime powers). No many-body term of ANY q-adic order exists on the production word at "
        "A = 3; a route-C b₃ must come from a non-chain word class or from outside the trace. The "
        "general-A Lean statement (MarkovBondFactor.lean general case, bean qou-g8i1) stays OPEN."
        if all_hold else
        "bond factorisation FAILS at n = 9 on the canonical word for at least one composition; see "
        "Delta_q_minus_1_adic_order / Delta_leading_coefficient per composition and the pin diagnostic.")
    print("\n  VERDICT: " + verdict)

    wb = WitnessBuilder("route-c-step3-bond-factorisation-exact", engine="fraction", _script_path=__file__)
    wb.set_description(
        "Route C step 3 / candidate S3 (bean qou-8uxw): exact-in-q test of block-and-bond "
        "factorisation for the canonical NON-monotone nucleon word at n = 9 (A = 3). C(w) := "
        "q^{l(w)}[2]_q^9 tr_D(w) is computed as an exact Laurent polynomial (integer big-int "
        "evaluation on weight sectors of V^{⊗9}, Newton interpolation over Fraction, verified at "
        "unused prime powers) for β_free, β_12, β_23, β_123 in the compositions ppn, pnn, ppp, nnn, "
        "using the canonical constructor (atom_canonical_crossings → atom_braid_word_3A, "
        "bring_color_weighted, intra_order=borromean) with interfaces toggled by multiplicity exactly "
        "as atom_bond_product_closed_form_probe does. Δ = C(123)C(free) − C(12)C(23) is reported "
        "exactly with its (q−1)-adic order; the ε² truncation is cross-checked against that probe's "
        "five recorded input series. NO FITTING; q₀ read only for a diagnostic line; the identity is "
        "q-formal. " + verdict)
    wb.set_content_block("prop:markov-trace-axiomatic-closed-form")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0",
                         expected="1", tolerance="0.5", source="exact (Fraction / big-int / sympy factor)")
    wb.add_parameter("n_strands", N_STRANDS)
    wb.add_parameter("rep", "spin-1/2 V^{⊗9}: σ = swap + diag(q−1 on |00⟩,|11⟩; h on |10⟩), K = diag(q⁻¹, q), "
                            "tr_D = tr(K^{⊗n}·)/[2]^n; letters σ_g + d, d ∈ {0, −h, −h/2, −h(1/2−δ/4)}, "
                            "δ = (q−1)²(1−q⁻⁴)/3")
    wb.add_parameter("constructor", "canonical_braid_crossings.atom_canonical_crossings(Z, N, include_inter, "
                                    "m_pp, m_pn, m_nn, ordering) → mass_at_3A_proper.atom_braid_word_3A "
                                    "(pn_convention=bring_color_weighted, intra_order=borromean) → "
                                    "pyhecke.atom.nucleon_word_letters")
    wb.add_parameter("recorded_eps2_inputs", {"nucleon": {k: [str(x) for x in v] for k, v in REC_NUC.items()},
                                              "bond": {k: [str(x) for x in v] for k, v in REC_BOND.items()},
                                              "source": "computations/probes/atom_bond_product_closed_form_probe.py"})
    if Q_50_DIGIT_STR is not None:
        wb.add_parameter("q0", Q_50_DIGIT_STR)
    for comp, r in results.items():
        wb.add_data(f"composition_{comp}", r)
    wb.add_data("anchor_evaluation", anchor)
    wb.add_data("verdict", verdict)
    wb.add_caveat("Scope: n = 9 (A = 3), the four compositions listed, the canonical word with each "
                  "interface toggled. Scope (b) at n = 9 with the identity as the invariant if Δ ≡ 0; "
                  "the general-A disjoint-block Lean statement (MarkovBondFactor.lean general case) is NOT "
                  "established here.")
    wb.add_caveat("b₃ = 2852445/2000000 MeV and μ₃ = 0.4708 MeV are QUOTED targets for comparison only; "
                  "nothing is adjusted toward them.")
    wb.add_caveat("For ppp/nnn the constructor's multiplicity toggles both like-type interfaces together, "
                  "so β_12/β_23 are the constructor's β_123 with the OTHER interface letter deleted "
                  "(letters at generators 2 and 5); no letter is re-typed.")
    out = wb.save()
    print(f"  witness -> {os.path.relpath(out, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
