#!/usr/bin/env python3
"""The colored Lawrence–Rozansky modulus identification on Σ(2,3,5) — the W_λ keystone's
last open piece (1ppQ front 2, `2026-07-17-three-front-attack-specs.md` §2).

TARGET (conjectured shape, per the s5-so3 ledger / #3703 refocus):

    |S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ),      d_q(λ) = [mark(λ)]_q  (McKay 2I↔Ê₈, EXACT per #3685)

for the 9 affine-Ê₈ McKay nodes (marks 1,2,3,4,5,6,4,2,3 = dims of the 2I irreps; Σ mark² = 120 = |2I|).

WHAT THIS PROBE ESTABLISHES (tiered; no fit, no constant wired):

  (F)  EXACT CHARACTER FOLD.  The color-α insertion on the order-5 exceptional fibre produces the
       Hikami odd character χ^{(1,1,α)}_{60} (eq. 3.1 of math-ph/0405028, machine-validated in-repo
       by `probes/keystone_valuemap_genuine_smatrix_s013.py`).  Computed exactly (integer tables,
       zero floats): the map α ↦ χ^{(1,1,α)} factors through the r = 5 affine-Weyl fold with the
       SAME kernel and signs as the quantum integer α ↦ [α]_ζ at the fibre root ζ = e^{iπ/5}:

           χ^{(1,1,4)} = +χ^{(1,1,1)}   ↔   [4]_ζ = +[1]_ζ = 1
           χ^{(1,1,3)} = +χ^{(1,1,2)}   ↔   [3]_ζ = +[2]_ζ = φ (golden ratio)
           χ^{(1,1,5)} ≡ 0              ↔   [5]_ζ = 0
           χ^{(1,1,6)} = −χ^{(1,1,1)}   ↔   [6]_ζ = −[1]_ζ = −1

       This answers the pre-registered "D = 2 collapse" kill criterion: the McKay-labelled coloring
       does NOT escape the collapse — it factors through it exactly as the value map does.  The
       collapse is structural (D(2,3,5) = 2: Σ(2,3,5) has exactly two irreducible SU(2) flat
       connections), so a 9-independent-moduli reading at one ζ is (b)-excluded by that invariant.

  (A)  COLORED GAUSS SUM + ANCHOR.  τ_N(α) = the LR/Hikami Gauss sum with the order-5 fibre factor
       sin(nπ/5N) → sin(αnπ/5N) (the standard character insertion; same convention as the in-repo
       colored family `probes/keystone_colored_sigma235_wrt.py`).  α = 1 reproduces the bare τ_N to
       machine zero, and the bare Theorem-10 identity re-validates the whole transcription chain.

  (L)  FOLD LINEARITY AT THE FLAT LEVEL.  The colored Gauss sum is NOT a functional of the fold
       class alone — but the deviations are ELEMENTARY (trivial-connection-type) terms, exact to
       machine zero at every checked N (discovered, then verified at fresh N):

           τ_N(4) − τ_N(1) = 1 + 2cos(2π/N)      τ_N(3) − τ_N(2) = e^{−6πi/(5N)}

       and τ_N(6) + τ_N(1) is O(1) after Cor-12 normalization (no √N flat growth).  So the
       flat-connection amplitudes — the only input to the modulus identification — obey the fold
       exactly: A(4) = A(1), A(3) = A(2) (up to a vanishing phase), A(6) = −A(1).  τ_N(5)
       carries NO flat part (χ ≡ 0): |pref·τ_N(5)| stays bounded while |pref·τ_N(α≠5)| ~ √N.

  (M)  MODULUS IDENTIFICATION (the corrected identity).  Flat-connection amplitudes extracted
       parameter-free (2×2 linear inversion at two large N, cross-checked at a third) match

           A_m(α) = ±(2/√5)·sin(αmπ/5),     m = 1,2  (flat connections; CS = −1/120, −49/120)

       and the EXACT ℚ(√5) algebra then gives, for every node λ and both flat connections m:

           |A_m(mark λ)| · D_{Ê₈}(ζ^m) = 2 · |[mark λ]_{ζ^m}|        (EXACT, ℚ(√5) arithmetic)

       with D_{Ê₈}(ζ^m)² = Σ_{9 nodes} [mark]_{ζ^m}² = 10 ± 2√5 and the core exact identity
       (10−2√5)(10+2√5) = 80.  Equivalently |S_{0λ}^{(m)}| = 2·d_{ζ^m}(λ)/D_{Ê₈}(ζ^m)
       = √2·d(λ)/D_MTC(ζ^m), since D_{Ê₈}² = 2·D_MTC² exactly (the Ê₈ node set folds 2:1 onto
       the r=5 alcove {1,2,3,4}, node 5 → 0).

VERDICT: **corrected exact identity** — the conjectured shape holds with three corrections:
  (1) ζ is the FIBRE root e^{mπi/5} (order 2p₃ = 10, the order-5-fibre holonomy scale), Galois-
      indexed by the flat connection m — NOT the level root ζ_N (amplitudes are N-independent)
      and NOT e^{2πi/30};
  (2) a global factor 2 (Ê₈-node normalizer) resp. √2 (folded-MTC normalizer) — the 2:1 fold
      multiplicity, exact;
  (3) the identity lives at the FOLDED (D = 2) level: the 4 generic-q Hecke classes collapse at the
      fibre root ([5]_ζ = 0 kills the (3,2) muon-class numerator; electron [5]_ζ+1 = 1 = |[6]_ζ|,
      moduli consistent across the S₅-block and 2I-node dictionaries).  The generic-q /
      archimedean-q₀ separation of the 4 classes remains the standing open continuation problem
      (#3652/#3681) — unchanged, and NOT claimed here.

No fit: every constant is forced (McKay marks, Hikami S-matrix, fold signs); unknowns extracted by
exact linear inversion are cross-checked at fresh N (anti-fabrication anchor discipline).

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (math-ph/0405028: eqs. 2.11, 2.12,
#      3.1, 3.8, 5.5; in-repo transcription machine-validated by keystone_valuemap_genuine_smatrix_s013)
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
# Ref: [fintushelstern1990] https://doi.org/10.1112/plms/s3-61.1.109  (flat-connection count)
"""
from __future__ import annotations

import sys
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

# affine Ê₈ McKay nodes: (label, mark = dim of the 2I irrep)
MCKAY_NODES = [
    ("triv", 1), ("2s", 2), ("3", 3), ("4s", 4), ("5", 5),
    ("6", 6), ("4", 4), ("2s'", 2), ("3'", 3),
]

# S₅ conjugation-class view (#3685 dictionary: bwS0 class ↔ A₅-factoring McKay mark)
S5_CLASSES = [("{(5),(1^5)}", 1), ("{(4,1),(2,1,1,1)}", 4),
              ("{(3,2),(2,2,1)}", 5), ("{(3,1,1)} (electron, split)", 6)]


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
        return f"({self.a}+{self.b}√5)"


PHI = Q5(Fraction(1, 2), Fraction(1, 2))          # golden ratio (1+√5)/2; φ² = φ+1
SIN2_PI5 = Q5(Fraction(10, 16), Fraction(-2, 16))   # sin²(π/5)  = (10−2√5)/16
SIN2_2PI5 = Q5(Fraction(10, 16), Fraction(2, 16))   # sin²(2π/5) = (10+2√5)/16


def qint_fold(m, two_cos):
    """[m]_ζ via the Chebyshev recurrence [m+1] = 2cos(θ)[m] − [m−1], exact in ℚ(√5)."""
    a, b = Q5(0), Q5(1)  # [0], [1]
    for _ in range(m - 1):
        a, b = b, two_cos * b - a
    return b


def sin2_exact(k):
    """sin²(kπ/5) as an exact Q5 element (k any integer)."""
    k = k % 5
    if k == 0:
        return Q5(0)
    return SIN2_PI5 if k in (1, 4) else SIN2_2PI5


# ────────────────────────────────────────────────────────────────────────────
# (F) Exact characters χ^{(1,1,α)} with accumulation (α = 5 cancels identically)
# ────────────────────────────────────────────────────────────────────────────
def chi_table(alpha):
    """χ^{(1,1,α)}_{60}: accumulate ± over the 8 sign choices (Hikami eq. 3.1);
    entries that cancel are dropped.  Exact integer arithmetic."""
    out = {}
    for e1 in (-1, 1):
        for e2 in (-1, 1):
            for e3 in (-1, 1):
                val = Fraction(P) * (1 + Fraction(e1, 2) + Fraction(e2, 3)
                                     + Fraction(e3 * alpha, 5))
                assert val.denominator == 1
                r = int(val) % TWO_P
                out[r] = out.get(r, 0) + (1 if e1 * e2 * e3 == -1 else -1)
    return {r: v for r, v in out.items() if v != 0}


def fold_of(alpha):
    """(base, sign) with χ^{(1,1,α)} = sign·χ^{(1,1,base)}, or (None, 0) if χ ≡ 0.
    Exact table comparison — no numerics."""
    t = chi_table(alpha)
    if not t:
        return None, 0
    for base in (1, 2):
        tb = chi_table(base)
        if t == tb:
            return base, 1
        if t == {r: -v for r, v in tb.items()}:
            return base, -1
    return "other", 0


# ────────────────────────────────────────────────────────────────────────────
# (A) Colored Gauss sum τ_N(α)  (Hikami eq. 2.11 with the order-5 fibre character insertion)
# ────────────────────────────────────────────────────────────────────────────
def dedekind_s(b, a):
    return mp.fsum(mp.cot(mp.pi * k / a) * mp.cot(mp.pi * k * b / a)
                   for k in range(1, a)) / (4 * a)


def phi_235():
    return (3 - mpf(1) / P
            + 12 * (dedekind_s(15, 2) + dedekind_s(10, 3) + dedekind_s(6, 5)))


_PHI235 = None


def tau_N(N, alpha=1):
    """τ_N(Σ(2,3,5); order-5 fibre colored by the α-dim SU(2) color).
    α = 1 is Hikami eq. (2.11) verbatim (validated: Theorem-10 anchor)."""
    global _PHI235
    if _PHI235 is None:
        _PHI235 = phi_235()
    pref_lhs = mp.e ** (2 * mp.pi * I / N * (_PHI235 / 4 - mpf(1) / 2)) \
        * (mp.e ** (2 * mp.pi * I / N) - 1)
    total = mpc(0)
    for n in range(2 * P * N):
        if n % N == 0:
            continue
        num = ((mp.e ** (n * mp.pi * I / (N * 2)) - mp.e ** (-n * mp.pi * I / (N * 2)))
               * (mp.e ** (n * mp.pi * I / (N * 3)) - mp.e ** (-n * mp.pi * I / (N * 3)))
               * (mp.e ** (alpha * n * mp.pi * I / (N * 5))
                  - mp.e ** (-alpha * n * mp.pi * I / (N * 5))))
        den = mp.e ** (n * mp.pi * I / N) - mp.e ** (-n * mp.pi * I / N)
        total += mp.e ** (-n * n * mp.pi * I / (2 * P * N)) * num / den
    rhs = mp.e ** (mp.pi * I / 4) / (2 * mp.sqrt(mpf(2 * P * N))) * total
    return rhs / pref_lhs


def theorem10_residual(N):
    """Bare anchor (Hikami Thm 10, eq. 5.5) — re-validates the transcription chain."""
    chi = chi_table(1)
    lhs = (mp.e ** (2 * mp.pi * I / N)
           * (mp.e ** (2 * mp.pi * I / N) - 1) * tau_N(N, 1))
    eich = mp.fsum(chi[n % TWO_P] * (1 - mpf(n) / (P * N))
                   * mp.e ** (n * n * mp.pi * I / (2 * P * N))
                   for n in range(P * N + 1) if (n % TWO_P) in chi)
    rhs = 1 + mp.e ** (-mp.pi * I / (60 * N)) * eich / 2
    return abs(lhs - rhs)


# ────────────────────────────────────────────────────────────────────────────
# (M) Flat-connection amplitude extraction — parameter-free 2×2 inversion
# ────────────────────────────────────────────────────────────────────────────
def pref_c12(N):
    """Corollary-12 LHS prefactor: e^{2πi(121/120)/N}(e^{2πi/N}−1)."""
    return mp.e ** (2 * mp.pi * I / N * mpf(121) / 120) * (mp.e ** (2 * mp.pi * I / N) - 1)


def flat_basis(N):
    """The two flat-connection basis terms √N e^{−πi/4} e^{2πiN·CS_m}, CS = −1/120, −49/120."""
    c = mp.sqrt(mpf(N)) * mp.e ** (-mp.pi * I / 4)
    return (c * mp.e ** (-mp.pi * I * N / 60), c * mp.e ** (-49 * mp.pi * I * N / 60))


def extract_amplitudes(alpha, N1, N2):
    """Solve the 2×2 linear system  Σ_m basis_m(N_i)·A_m = pref(N_i)·τ_{N_i}(α)  for (A₁, A₂).
    Parameter-free (linear inversion, no fit); tail contributes O(1/√N) error."""
    rows, rhs = [], []
    for N in (N1, N2):
        b = flat_basis(N)
        rows.append(b)
        rhs.append(pref_c12(N) * tau_N(N, alpha))
    det = rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
    a1 = (rhs[0] * rows[1][1] - rhs[1] * rows[0][1]) / det
    a2 = (rows[0][0] * rhs[1] - rows[1][0] * rhs[0]) / det
    return a1, a2


def predicted_amp(alpha, m):
    """|A_m(α)| predicted = (2/√5)|sin(αmπ/5)|  (exact-Q5 squared value available)."""
    return 2 / mp.sqrt(mpf(5)) * abs(mp.sin(alpha * m * mp.pi / 5))


# ────────────────────────────────────────────────────────────────────────────
# main
# ────────────────────────────────────────────────────────────────────────────
def run():
    out = {}

    # (F) exact fold table, both sides
    fold = {}
    fold_matches_qint = True
    two_cos = PHI  # 2cos(π/5) = φ exactly
    qint_vals = {m: qint_fold(m, two_cos) for m in range(1, 7)}
    # ℚ(√5) fold facts: [4] = [1] = 1, [3] = [2] = φ, [5] = 0, [6] = −1
    qfold_exact = (qint_vals[4] == Q5(1) and qint_vals[3] == qint_vals[2]
                   and qint_vals[2] == PHI and qint_vals[5] == Q5(0)
                   and qint_vals[6] == Q5(-1))
    for alpha in range(1, 7):
        base, sign = fold_of(alpha)
        fold[alpha] = {"base": base, "sign": sign}
        # the quantum-integer side of the fold: [α]_ζ = sign·[base]_ζ, base ∈ {1,2}
        if alpha == 5:
            ok = qint_vals[5] == Q5(0) and base is None
        else:
            ok = base in (1, 2) and qint_vals[alpha] == (Q5(sign) * qint_vals[base])
        fold_matches_qint = fold_matches_qint and ok
    out["fold_table"] = {str(k): v for k, v in fold.items()}
    out["qint_fold_values"] = {str(m): repr(qint_vals[m]) for m in range(1, 7)}
    out["chi_115_identically_zero"] = not chi_table(5)
    out["qfold_exact"] = bool(qfold_exact)
    out["fold_matches_qint_signs"] = bool(fold_matches_qint)

    # (A) anchors
    t10 = {str(N): float(theorem10_residual(N)) for N in (3, 5, 7)}
    out["theorem10_residuals"] = t10
    out["theorem10_exact"] = all(v < 1e-28 for v in t10.values())

    # (L) fold linearity at the FLAT-CONNECTION level.  The colored Gauss sum is NOT a
    # functional of the fold class alone — but the deviations are ELEMENTARY (trivial-
    # connection-type) terms, discovered and then verified machine-zero at fresh N
    # (anti-fabrication anchor discipline; finitely many candidates vs ~1e-38 residuals):
    #
    #     τ_N(4) − τ_N(1) = 1 + 2cos(2π/N)          (exact)
    #     τ_N(3) − τ_N(2) = e^{−6πi/(5N)}           (exact, unit modulus)
    #     τ_N(6) + τ_N(1) = O(1) after Cor-12 normalization (bounded; no √N flat growth)
    #
    # Hence the flat-connection amplitudes — the only input to the modulus identification —
    # obey the fold exactly: A(4) = A(1), A(3) = A(2) up to a vanishing phase, A(6) = −A(1).
    lin = {}
    d4 = {str(N): float(abs(tau_N(N, 4) - tau_N(N, 1)
                            - (1 + 2 * mp.cos(2 * mp.pi / N))))
          for N in (7, 11, 13, 25)}
    d32 = {str(N): float(abs(tau_N(N, 3) - tau_N(N, 2)
                             - mp.e ** (-6 * mp.pi * I / (5 * N))))
           for N in (7, 11, 13, 25)}
    d6 = {str(N): float(abs(pref_c12(N) * (tau_N(N, 6) + tau_N(N, 1))))
          for N in (7, 11, 13, 25, 51, 101)}
    lin["delta4_eq_1_plus_2cos"] = d4
    lin["delta32_eq_exp_m6pi_over_5N"] = d32
    lin["delta6_normalized_abs"] = d6
    out["chi_linearity"] = lin
    out["delta4_exact"] = all(v < 1e-28 for v in d4.values())
    out["delta32_exact"] = all(v < 1e-28 for v in d32.values())
    out["delta6_flat_free"] = max(d6.values()) < 4.0  # bounded, vs √N·|A|·|pref-scale| growth
    out["fold_holds_at_flat_level"] = bool(
        out["delta4_exact"] and out["delta32_exact"] and out["delta6_flat_free"])

    # (L) α = 5: no flat part — the Cor-12-normalized |pref·τ_N(5)| stays O(1)
    # while |pref·τ_N(1)| grows ~ √N (flat-connection contribution present).
    a5 = {str(N): float(abs(pref_c12(N) * tau_N(N, 5))) for N in (25, 51, 101, 201)}
    a1 = {str(N): float(abs(pref_c12(N) * tau_N(N, 1))) for N in (25, 51, 101, 201)}
    out["alpha5_normalized_abs"] = a5
    out["alpha1_normalized_abs"] = a1
    out["alpha5_bounded"] = a5["201"] < 3 * max(a5["25"], 1e-9) and a5["201"] < a1["201"] / 3

    # (M) amplitude extraction for ALL colors α = 1,2,3,4,6 (α = 5 is flat-free, above);
    # extraction is parameter-free (2×2 linear inversion), cross-checked at a fresh N pair.
    amp = {}
    amp_ok = True
    for alpha in (1, 2, 3, 4, 6):
        e1 = extract_amplitudes(alpha, 101, 149)
        e2 = extract_amplitudes(alpha, 151, 199)   # fresh pair — anti-fabrication cross-check
        rows = {}
        for m in (1, 2):
            got1, got2 = abs(e1[m - 1]), abs(e2[m - 1])
            pred = predicted_amp(alpha, m)
            rows[str(m)] = {"extracted_pair1": float(got1),
                            "extracted_pair2": float(got2),
                            "predicted": float(pred),
                            "rel_err": float(abs(got2 - pred) / (abs(pred) + mpf("1e-30")))}
            amp_ok = amp_ok and abs(got2 - pred) < mpf("0.05") * (1 + pred)
        amp[str(alpha)] = rows
    out["amplitudes"] = amp
    out["amplitudes_match_predicted"] = bool(amp_ok)

    # (M) the EXACT ℚ(√5) modulus identification, per node and flat connection:
    #     A_m(mark)² · D_{Ê₈}(ζ^m)² = 4 · [mark]²_{ζ^m}    (all in ℚ(√5), zero floats)
    #     with A_m(α)² = (4/5)·sin²(αmπ/5) and D² = Σ_{9 nodes} [mark]²_{ζ^m}.
    d2 = {}
    core_ok = True
    for m in (1, 2):
        two_cos_m = PHI if m == 1 else (PHI - Q5(1))  # 2cos(2π/5) = φ − 1 = (√5−1)/2 exactly
        vals = {mm: qint_fold(mm, two_cos_m) for mm in range(1, 7)}
        D2 = Q5(0)
        for _, mark in MCKAY_NODES:
            D2 = D2 + vals[mark] * vals[mark]
        d2[str(m)] = repr(D2)
        # D² = 10 + 2√5 (m=1), 10 − 2√5 (m=2)
        expect = Q5(10, 2) if m == 1 else Q5(10, -2)
        core_ok = core_ok and D2 == expect
        for _, mark in MCKAY_NODES:
            lhs = Q5(Fraction(4, 5)) * sin2_exact(mark * m) * D2
            rhs = Q5(4) * vals[mark] * vals[mark]
            core_ok = core_ok and lhs == rhs
    out["D2_E8"] = d2
    out["core_identity_10m2s5_times_10p2s5_eq_80"] = bool(
        (Q5(10, -2) * Q5(10, 2)) == Q5(80))
    # fold multiplicity: D_{Ê₈}² = 2·D_MTC² (alcove {1,2,3,4})
    two_cos_1 = PHI
    vals1 = {mm: qint_fold(mm, two_cos_1) for mm in range(1, 5)}
    Dmtc2 = Q5(0)
    for mm in range(1, 5):
        Dmtc2 = Dmtc2 + vals1[mm] * vals1[mm]
    out["D2_MTC"] = repr(Dmtc2)
    out["fold_multiplicity_exact"] = bool(Q5(10, 2) == Q5(2) * Dmtc2)
    out["modulus_identity_exact_all_nodes"] = bool(core_ok)

    # numeric cross-check of the exact leg (50 dps)
    with mp.workdps(50):
        num_ok = True
        for m in (1, 2):
            th = mp.pi * m / 5
            D2n = mp.fsum((mp.sin(mark * th) / mp.sin(th)) ** 2 for _, mark in MCKAY_NODES)
            for _, mark in MCKAY_NODES:
                lhs = (mpf(4) / 5) * mp.sin(mark * m * mp.pi / 5) ** 2 * D2n
                rhs = 4 * (mp.sin(mark * th) / mp.sin(th)) ** 2
                num_ok = num_ok and abs(lhs - rhs) < mpf("1e-45")
    out["numeric_crosscheck_50dps"] = bool(num_ok)

    # per-node table (floats for display; exact identity is the ℚ(√5) leg above)
    table = []
    for name, mark in MCKAY_NODES:
        row = {"node": name, "mark": mark}
        for m in (1, 2):
            th = mp.pi * m / 5
            lhsA = predicted_amp(mark, m)
            dq = mp.sin(mark * th) / mp.sin(th)
            D = mp.sqrt(mp.fsum((mp.sin(mk * th) / mp.sin(th)) ** 2
                                for _, mk in MCKAY_NODES))
            row[f"absA_m{m}"] = float(lhsA)
            row[f"dq_over_D_m{m}"] = float(abs(dq) / D)
            row[f"ratio_m{m}"] = float(lhsA / (abs(dq) / D)) if abs(dq) > 0 else None
        table.append(row)
    out["per_node_table"] = table

    # S₅-class view at the fibre root (moduli agree with the 2I-node view, incl. split node)
    s5 = []
    for name, mark in S5_CLASSES:
        # d_q at ζ: class value; electron (3,1,1) has d = [5]_ζ + 1 = 1 = |[6]_ζ|
        if mark == 6:
            dval = qint_vals[5] + Q5(1)
            note = "[5]_z+1 = 1; |[6]_z| = 1 — moduli agree, sign differs"
        else:
            dval = qint_vals[mark]
            note = ""
        s5.append({"s5_class": name, "mark": mark, "d_at_zeta": repr(dval), "note": note})
    out["s5_class_view"] = s5
    out["split_node_moduli_agree"] = bool((qint_vals[5] + Q5(1)) == Q5(1)
                                          and qint_vals[6] == Q5(-1))
    # group-side q → 1 anchor: Σ mark² = 120 = |2I|
    out["sum_mark_sq_eq_120"] = sum(mk * mk for _, mk in MCKAY_NODES) == 120
    return out


def report(res):
    print("# Colored Lawrence–Rozansky modulus identification on Σ(2,3,5)\n")
    print("## (F) Exact character fold  (kill criterion: the D=2 collapse)\n")
    for a, d in res["fold_table"].items():
        print(f"  α={a}: χ^(1,1,{a}) = {d['sign']:+d}·χ^(1,1,{d['base']})"
              if d["sign"] else f"  α={a}: χ ≡ 0")
    print(f"  χ^(1,1,5) ≡ 0: **{res['chi_115_identically_zero']}**")
    print(f"  fold signs/kernel == [α]_ζ fold (ζ=e^{{iπ/5}}, exact ℚ(√5)): "
          f"**{res['fold_matches_qint_signs']}**\n")
    print("## (A) Anchors\n")
    print(f"  Theorem-10 residuals: {res['theorem10_residuals']}  exact: "
          f"**{res['theorem10_exact']}**\n")
    print("## (L) Fold linearity at the flat-connection level + α=5 flat-free\n")
    print(f"  τ_N(4) − τ_N(1) − (1+2cos(2π/N)):   {res['chi_linearity']['delta4_eq_1_plus_2cos']}")
    print(f"  τ_N(3) − τ_N(2) − e^(−6πi/5N):      {res['chi_linearity']['delta32_eq_exp_m6pi_over_5N']}")
    print(f"  |pref·(τ_N(6) + τ_N(1))| (bounded): {res['chi_linearity']['delta6_normalized_abs']}")
    print(f"  Δ₄ exact: **{res['delta4_exact']}**  Δ₃₂ exact: **{res['delta32_exact']}**  "
          f"Δ₆ flat-free: **{res['delta6_flat_free']}**  → fold holds at flat level: "
          f"**{res['fold_holds_at_flat_level']}**")
    print(f"  |pref·τ_N(5)| bounded: {res['alpha5_normalized_abs']} vs "
          f"|pref·τ_N(1)| {res['alpha1_normalized_abs']}  → **{res['alpha5_bounded']}**\n")
    print("## (M) Amplitudes and the corrected exact identity\n")
    for a, rows in res["amplitudes"].items():
        for m, r in rows.items():
            print(f"  α={a} m={m}: extracted {r['extracted_pair2']:.4f} "
                  f"(pair1 {r['extracted_pair1']:.4f}) vs predicted {r['predicted']:.4f} "
                  f"(rel err {r['rel_err']:.1e})")
    print(f"  amplitudes match: **{res['amplitudes_match_predicted']}**")
    print(f"  D²_E8 = {res['D2_E8']}   D²_MTC = {res['D2_MTC']}  "
          f"(fold multiplicity D²_E8 = 2·D²_MTC: **{res['fold_multiplicity_exact']}**)")
    print(f"  core exact identity (10−2√5)(10+2√5) = 80: "
          f"**{res['core_identity_10m2s5_times_10p2s5_eq_80']}**")
    print(f"  EXACT modulus identity |A_m(mark)|·D_E8(ζ^m) = 2·|[mark]_ζ^m| at ALL 9 nodes, "
          f"both m: **{res['modulus_identity_exact_all_nodes']}** "
          f"(50-dps numeric cross-check: **{res['numeric_crosscheck_50dps']}**)\n")
    print("## Per-node table (m = 1, 2 flat connections; ratio = 2 everywhere)\n")
    print("  node  mark  |A_1|    d/D(ζ)   ratio   |A_2|    d/D(ζ²)  ratio")
    for r in res["per_node_table"]:
        print(f"  {r['node']:>4} {r['mark']:>4}  {r['absA_m1']:.4f}  "
              f"{r['dq_over_D_m1']:.4f}  {str(r['ratio_m1'])[:5]:>5}  "
              f"{r['absA_m2']:.4f}  {r['dq_over_D_m2']:.4f}  {str(r['ratio_m2'])[:5]:>5}")
    print("\n## S₅-class view at the fibre root\n")
    for r in res["s5_class_view"]:
        print(f"  {r['s5_class']:>28}: mark {r['mark']}, d(ζ) = {r['d_at_zeta']} {r['note']}")
    print("\nVERDICT: corrected exact identity — |S_0λ^(m)(ζ)| = 2·|[mark λ]_{ζ^m}|/D_E8(ζ^m)")
    print("= √2·d(λ)/D_MTC at the FIBRE roots ζ^m = e^{mπi/5} (Galois-indexed by the flat")
    print("connection), NOT at the level root ζ_N and NOT at e^{2πi/30}. The identity holds")
    print("THROUGH the D=2 fold (it does not escape it); the generic-q 4-class separation")
    print("remains the archimedean-continuation open object (#3652/#3681). No fit.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("lr-modulus-identification-sigma235", engine="mpmath+exact-Q5")
    w.set_description(
        "The colored Lawrence-Rozansky modulus identification on Sigma(2,3,5) -- the W_lambda "
        "keystone's last open piece. VERDICT: CORRECTED EXACT IDENTITY. The color-alpha "
        "insertion on the order-5 fibre produces the Hikami odd character chi^(1,1,alpha); "
        "computed exactly, the map alpha -> chi factors through the r=5 affine-Weyl fold with "
        "the SAME kernel and signs as alpha -> [alpha]_zeta at the fibre root zeta = e^{i pi/5} "
        "(chi^(114)=+chi^(111) ~ [4]=+[1]; chi^(113)=+chi^(112) ~ [3]=+[2]; chi^(115)=0 ~ "
        "[5]=0; chi^(116)=-chi^(111) ~ [6]=-[1]). The colored Gauss sum tau_N(alpha) (alpha=1 "
        "anchors to bare Theorem 10 machine-zero) obeys the fold AT THE FLAT-CONNECTION LEVEL: "
        "the class deviations are ELEMENTARY exact identities -- tau_N(4)-tau_N(1) = "
        "1+2cos(2pi/N) and tau_N(3)-tau_N(2) = e^{-6pi i/(5N)} (machine zero at N=7,11,13,25), "
        "tau_N(6)+tau_N(1) bounded after Cor-12 normalization, tau_N(5) has NO flat part. "
        "Flat-connection amplitudes extracted parameter-free match A_m(alpha) = "
        "(2/sqrt5)sin(alpha m pi/5), and the EXACT Q(sqrt5) algebra gives, for every affine-E8 "
        "McKay node lambda (marks 1,2,3,4,5,6,4,2,3 = 2I irrep dims) and both flat connections "
        "m: |A_m(mark)| * D_E8(zeta^m) = 2*|[mark]_{zeta^m}| with D_E8(zeta^m)^2 = 10 +- 2sqrt5 "
        "and core identity (10-2sqrt5)(10+2sqrt5)=80. So |S_0lambda^(m)| = "
        "2*d_{zeta^m}(lambda)/D_E8 = sqrt2*d/D_MTC (D_E8^2 = 2*D_MTC^2, the 2:1 fold of the "
        "affine-E8 node set onto the r=5 alcove). Corrections to the conjectured shape: (1) "
        "zeta is the FIBRE root e^{m pi i/5} Galois-indexed by the flat connection, not the "
        "level root and not e^{2 pi i/30}; (2) global factor 2 (resp. sqrt2); (3) the identity "
        "lives at the FOLDED D=2 level -- the 4 generic-q Hecke classes collapse at the fibre "
        "root ((3,2) muon class -> [5]=0; electron [5]+1 = 1 = |[6]|, moduli consistent); the "
        "9-independent-moduli reading at a single zeta is (b)-excluded by D(2,3,5)=2 (two "
        "irreducible SU(2) flat connections, Fintushel-Stern; machine-validated in-repo). The "
        "generic-q/archimedean separation remains the standing open continuation (#3652/#3681). "
        "No fit; nothing wired to production."
    )
    for k, v in res.items():
        w.add_data(k, v)
    w.add_assertion(
        "corrected_modulus_identity_established",
        computed=1 if (res["theorem10_exact"] and res["fold_holds_at_flat_level"]
                       and res["fold_matches_qint_signs"] and res["alpha5_bounded"]
                       and res["amplitudes_match_predicted"]
                       and res["modulus_identity_exact_all_nodes"]
                       and res["fold_multiplicity_exact"]
                       and res["numeric_crosscheck_50dps"]) else 0,
        expected=1, tolerance=0,
        source="Exact character fold == quantum-integer fold (integer tables + Q(sqrt5)); "
               "colored Gauss sum chi-linear to machine zero; amplitudes parameter-free-"
               "extracted match (2/sqrt5)sin(alpha m pi/5); exact Q(sqrt5) modulus identity "
               "|A_m|*D_E8 = 2*|[mark]| at all 9 nodes, both flat connections.",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
