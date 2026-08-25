#!/usr/bin/env python3
"""x050_50a_hecke_gate_probe.py — the X₀(50)/50a integer Hecke gate (idea A4).

Consumer of uploaded-papers audit idea A4 (docs/audits/
2026-07-18-uploaded-papers-binding-mass-gap-ideas.md §A4), composing with the
committed W8 validator (tau_dictionary_hauptmodul_validator.py, the t₅ = −10
class gate) and the W8b cusp/spin results
(docs/audits/2026-07-24-tau-dictionary-fricke-cusp-spin.md) as the FIFTH
discrete filter of the dictionary gauntlet: integer Hecke eigenvalues.

THE GATE. BDH22 (library/arxiv-2208.13692v1/2208.13692v1.pdf) Prop 4.5 ([Ser08] Ex 8.3.2(b)):
the ℚ-isogeny class of the Jacobian of the P⁴-model of Bring's curve is
(50a)⁴ (Cremona labels; their §4.3 note: "the Q-isogeny class of B/A4 is 50a",
computed in Sage). BDH22 eq (10): C₁ = B/⟨(12)(34)⟩ : B² = A⁶+4A⁵+10A³+4A+1
is a model of the modular curve X₀(50) (Igusa–Clebsch match against LMFDB +
direct Shimura-method model). Hence a modular W-plane family E(q) (lever-1,
post-SL₂(ℝ) re-scope per the 2026-07-18 correction of
2026-06-24-lever1-trB-geometric-target.md) can be level-50 modular ONLY if it
reproduces the conductor-50 newform's INTEGER Hecke data a_p — a discrete,
parameter-free pass/fail with no precision ladder.

THIS PROBE (pure integer arithmetic; no floats anywhere):

  1. Takes the task curve E: y² = x³ − 675x − 79650 (RR92 §4 / Serre's curve;
     j = −25/2 = j(5τ₀), the BDH22 eq (6)/(12) j-invariant), derives its
     GLOBAL MINIMAL MODEL offline by Laska–Kraus–Connell reduction:
     y² + xy + y = x³ − x − 2, Δ_min = −1250 = −2·5⁴, conductor N = 50
     (multiplicative at 2 with f₂ = 1, additive Kodaira IV at 5 with f₅ = 2 —
     tame since p = 5 ≥ 5). Every step is verified by exact assertions.
  2. Computes a_p for every prime p ≤ 50, p ∤ 50, by exact point-counting
     over F_p on the minimal model (p = 3 needs the minimal model: the short
     model is non-minimal at 3, Δ_short = −2¹³·3¹²·5⁴). Hasse bound asserted
     per prime. a₂ = −1 (non-split multiplicative: −c₆ = −1475 ≡ 5 mod 8 is
     a ℚ₂-non-square) and a₅ = 0 (additive) from local data, each verified by
     counting non-singular points of the reduction (p − a_p, resp. p).
  3. Cross-checks (falsifier-grade, all asserted):
     (a) short model vs minimal model point counts agree (p ∤ 30);
     (b) BOTH of BDH22's printed E₂ charts (y² = 100−25x−10x²−x³ from §4.3's
         semi-invariant chart, and eq (12) (B″)² = 1−5C−40C²−80C³) are the
         (−1)-quadratic twist of E — same j = −25/2, but conductor ≠ 50
         (additive at 2). Finding: the paper's printed chart equations are
         twist-sloppy (identified only via j over ℂ); no printed BDH22
         equation carries the label-pinning class.
     (c) the (−1)-twist of BDH22's printed E₁ chart (eq (11), j = j(τ₀) =
         −5·29³/2⁵ = −121945/32) has minimal model y² + xy + y = x³+x²−3x+1,
         Δ = −800, conductor 50, a₂ = +1 (split) — this is a representative F
         of the OTHER conductor-50 class, and a_p(F) = χ₅(p)·a_p(E) for all
         good p ≤ 50 (the two level-50 classes are √5-twist partners: BDH22
         "50a and 50b merge over ℚ(√5)").
     (d) THE X₀(50) TRACE IDENTITY: on BDH22's own genus-2 model C₁,
         t_p := p + 1 − #C₁(F_p) equals a_p(E)·(1 + χ₅(p)) = a_p(E) + a_p(F)
         for ALL 13 good primes p ≤ 50 — i.e. Frobenius on Jac(X₀(50)) has
         exactly the traces of the pair {E-class, F-class} (Eichler–Shimura).
         This certifies offline that {class(E), class(F)} = {50a, 50b}.
  4. CREMONA-LABEL DISAMBIGUATION (honest): the paper never prints the
     equation of B/A₄ (the curve its Sage run labels 50a), and neither RR92
     nor [Ser08] is available offline, so WHICH of the two signatures carries
     the label "50a" cannot be settled from the paper + offline arithmetic.
     BOTH candidate signatures are recorded (they differ by χ₅(p), and at
     a₂: −1 vs +1). The single online lookup that settles it:
     https://www.lmfdb.org/EllipticCurve/Q/50/a/ (equivalently Cremona table
     entry 50a1) — compare its minimal equation / a_p against signature I.
     NOT guessed here.

Scope-(a), audit-only, NO FIT: the a_p are exact integers forced by the
curve; nothing is tuned; nothing is wired to production; a future family
failing the gate is refuted-as-stated only.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from fractions import Fraction  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

# ── primes of the gate ─────────────────────────────────────────────────────
GOOD_PRIMES = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]  # p ≤ 50, p ∤ 50
BAD_PRIMES = [2, 5]  # 50 = 2·5²


# ── exact elementary number theory ─────────────────────────────────────────
def legendre(a: int, p: int) -> int:
    """Legendre symbol (a|p) for odd prime p; 0 when p | a."""
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def valuation(n: int, p: int) -> int:
    assert n != 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def is_square_qp(n: int, p: int) -> bool:
    """Is n a square in ℚ_p* (n ≠ 0)?"""
    v = valuation(n, p)
    m = n // p**v
    if v % 2:
        return False
    if p == 2:
        return m % 8 == 1
    return legendre(m, p) == 1


def chi5(p: int) -> int:
    """Quadratic character of ℚ(√5) (conductor 5): (p|5)."""
    return legendre(p, 5)


def chi_minus1(p: int) -> int:
    """(−1|p) for odd p."""
    return 1 if p % 4 == 1 else -1


# ── Weierstrass invariants (exact) ─────────────────────────────────────────
def invariants(a1, a2, a3, a4, a6):
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2**3 + 36 * b2 * b4 - 216 * b6
    disc = -b2 * b2 * b8 - 8 * b4**3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    assert 1728 * disc == c4**3 - c6 * c6
    return c4, c6, disc


def kraus_model(c4: int, c6: int):
    """Construct an integral Weierstrass model with invariants (c4, c6), or
    return None if none exists (Kraus obstruction at 2 or 3). Scans b2 over
    a full residue system; b2 of an integral model satisfies b2 = a1² + 4a2
    with a1 ∈ {0,1} — the scan checks all divisibility conditions directly
    and round-trips the invariants. Scanning smallest |b2| first returns the
    standard reduced representative (a2 ∈ {-1,0,1}) when one exists."""
    for b2 in sorted(range(-96, 97), key=abs):
        if (b2 * b2 - c4) % 24:
            continue
        b4 = (b2 * b2 - c4) // 24
        num = -b2**3 + 36 * b2 * b4 - c6
        if num % 216:
            continue
        b6 = num // 216
        a1 = b2 % 2
        if (b2 - a1) % 4:
            continue
        a2 = (b2 - a1) // 4
        a3 = b6 % 2
        if (b6 - a3) % 4:
            continue
        a6_ = (b6 - a3) // 4
        if (b4 - a1 * a3) % 2:
            continue
        a4_ = (b4 - a1 * a3) // 2
        model = (a1, a2, a3, a4_, a6_)
        cc4, cc6, _ = invariants(*model)
        if (cc4, cc6) == (c4, c6):
            return model
    return None


def minimize(c4: int, c6: int):
    """Laska–Kraus–Connell: return (c4_min, c6_min, minimal model). Divides
    out u⁴|c4, u⁶|c6 as far as an integral model still exists (ℚ has class
    number 1, so the global minimal model exists and this procedure finds
    it)."""
    u_tot = 1
    for p in (2, 3, 5, 7):
        m = min(valuation(c4, p) // 4 if c4 % p == 0 else 0,
                valuation(c6, p) // 6 if c6 % p == 0 else 0)
        u_tot *= p**m
    divisors = sorted({d for d in range(1, u_tot + 1) if u_tot % d == 0},
                      reverse=True)
    for u in divisors:
        if c4 % u**4 == 0 and c6 % u**6 == 0:
            model = kraus_model(c4 // u**4, c6 // u**6)
            if model is not None:
                return c4 // u**4, c6 // u**6, model
    raise AssertionError("no integral model found — impossible over Q")


# ── exact point counting ───────────────────────────────────────────────────
def count_weierstrass(model, p: int) -> int:
    """#E(F_p) on a smooth Weierstrass model, odd p (completing the square)."""
    a1, a2, a3, a4, a6 = model
    n = 1  # point at infinity
    for x in range(p):
        d = ((a1 * x + a3) ** 2 + 4 * (x**3 + a2 * x * x + a4 * x + a6)) % p
        n += 1 + legendre(d, p)
    return n


def a_p(model, p: int) -> int:
    return p + 1 - count_weierstrass(model, p)


def count_cubic_chart(coeffs, p: int) -> int:
    """#{y² = f(x)} + 1 point at infinity, f cubic (any leading coeff ∤ p)."""
    d, c, b, a = coeffs  # f = a x³ + b x² + c x + d
    assert a % p != 0
    n = 1
    for x in range(p):
        v = (a * x**3 + b * x * x + c * x + d) % p
        n += 1 + legendre(v, p)
    return n


def count_genus2_sextic(fcoeffs, p: int) -> int:
    """#C(F_p) on the smooth model of y² = f(x), deg f = 6, monic (lc = 1 is
    a square mod every odd p, so there are exactly 2 points at infinity)."""
    n = 2
    for x in range(p):
        v = sum(c * pow(x, i, p) for i, c in enumerate(fcoeffs)) % p
        n += 1 + legendre(v, p)
    return n


def nonsingular_count(model, p: int) -> int:
    """#E^ns(F_p) on a (possibly singular) reduction: all points minus
    singular ones, plus the (always smooth) point at infinity."""
    a1, a2, a3, a4, a6 = [c % p for c in model]
    n = 1
    for x in range(p):
        for y in range(p):
            f = (y * y + a1 * x * y + a3 * y
                 - (x**3 + a2 * x * x + a4 * x + a6)) % p
            if f:
                continue
            fx = (a1 * y - (3 * x * x + 2 * a2 * x + a4)) % p
            fy = (2 * y + a1 * x + a3) % p
            if fx == 0 and fy == 0:
                continue  # singular point — excluded
            n += 1
    return n


# ── main ───────────────────────────────────────────────────────────────────
def main():
    wb = WitnessBuilder("x050-50a-hecke-gate-probe", engine="python")

    # ══ 1. The task curve and its exact reduction data ════════════════════
    # E: y² = x³ − 675x − 79650  (RR92 §4 / Serre's curve; j = −25/2)
    short_model = (0, 0, 0, -675, -79650)
    c4_s, c6_s, disc_s = invariants(*short_model)
    assert (c4_s, c6_s) == (32400, 68817600)
    assert disc_s == -(2**13) * 3**12 * 5**4, disc_s
    j_task = Fraction(c4_s**3, disc_s)
    assert j_task == Fraction(-25, 2), j_task  # = j(5τ₀), BDH22 eq (12)

    c4_m, c6_m, min_model = minimize(c4_s, c6_s)
    assert (c4_m, c6_m) == (25, 1475), (c4_m, c6_m)
    assert min_model == (1, 0, 1, -1, -2), min_model  # y²+xy+y = x³−x−2
    _, _, disc_min = invariants(*min_model)
    assert disc_min == -1250 == -2 * 5**4, disc_min

    # local data at 2: v2(c4)=0, v2(Δ)=1 → multiplicative, f₂ = 1, Kodaira I₁
    assert c4_m % 2 == 1 and valuation(disc_min, 2) == 1
    # split iff −c6 ∈ (ℚ₂*)²; −1475 ≡ 5 (mod 8) → non-split → a₂ = −1
    assert not is_square_qp(-c6_m, 2)
    a2_E = -1
    w2_E = -a2_E  # Atkin–Lehner λ_p = −a_p for p ‖ N (Atkin–Lehner 1970)
    # verified by counting: #E^ns(F₂) = 2 − a₂ = 3
    assert nonsingular_count(min_model, 2) == 2 - a2_E
    # local data at 5: (v(c4), v(c6), v(Δ)) = (2, 2, 4) → additive, Kodaira
    # IV, tame (p = 5 ≥ 5) → f₅ = 2, a₅ = 0
    assert (valuation(c4_m, 5), valuation(c6_m, 5),
            valuation(disc_min, 5)) == (2, 2, 4)
    a5_E = 0
    assert nonsingular_count(min_model, 5) == 5  # additive: p ns-points
    conductor = 2**1 * 5**2
    assert conductor == 50

    print("E (task): y² = x³ − 675x − 79650,  j = −25/2 = j(5τ₀)")
    print("  minimal model  y² + xy + y = x³ − x − 2   (derived offline, LKC)")
    print(f"  (c4, c6, Δ)_min = ({c4_m}, {c6_m}, {disc_min})")
    print("  p=2: multiplicative I₁, NON-split (−c₆ ≡ 5 mod 8) → a₂ = −1, w₂ = +1")
    print("  p=5: additive Kodaira IV, tame → a₅ = 0, f₅ = 2")
    print(f"  conductor N = {conductor}")

    # ══ 2. a_p by exact point counting; Hasse bound per prime ═════════════
    ap_E = {p: a_p(min_model, p) for p in GOOD_PRIMES}
    for p, ap in ap_E.items():
        assert ap * ap <= 4 * p, f"Hasse bound violated at {p}"  # |a_p| ≤ 2√p

    # cross-check (a): short model agrees wherever it has good reduction
    for p in GOOD_PRIMES:
        if p == 3:
            continue  # short model non-minimal at 3 (Δ_short has 3¹²)
        assert a_p(short_model, p) == ap_E[p], f"short-model mismatch at {p}"

    # ══ 3. BDH22's printed charts: the twist bookkeeping ══════════════════
    # E₂ chart #1 (§4.3 in-text): y² = 100 − 25x − 10x² − x³; x ↦ −x gives
    # the monic model y² = x³ − 10x² + 25x + 100 (same point sets over F_p).
    e2_chart1 = (0, -10, 0, 25, 100)
    c4_e2, c6_e2, disc_e2 = invariants(*e2_chart1)
    assert (c4_e2, c6_e2) == (400, -94400)
    assert disc_e2 == -(2**13) * 5**4
    assert Fraction(c4_e2**3, disc_e2) == Fraction(-25, 2)  # same j as E
    # (25, −1475) admits NO integral model (c₆ ≡ 1 mod 4 forces b₂ ≡ 3 mod 4,
    # impossible for b₂ = a₁² + 4a₂) → minimal invariants stay (400, −94400)
    assert kraus_model(25, -1475) is None
    # → additive at 2 (v₂(c₄) = 4 > 0): conductor ≠ 50. The chart is the
    # (−1)-twist of E: (c₄, c₆) = (25·(−1)², 1475·(−1)³) = (25, −1475). ✓
    for p in GOOD_PRIMES:
        assert a_p(e2_chart1, p) == chi_minus1(p) * ap_E[p], f"E₂ chart1 @ {p}"

    # E₂ chart #2 (eq (12)): (B″)² = 1 − 5C − 40C² − 80C³ — count directly.
    for p in GOOD_PRIMES:
        ap_chart2 = p + 1 - count_cubic_chart((1, -5, -40, -80), p)
        assert ap_chart2 == chi_minus1(p) * ap_E[p], f"E₂ chart2 @ {p}"

    # E₁ chart (eq (11)): y² = x³ − 5x² − 40x − 80, j = j(τ₀) = −5·29³/2⁵.
    e1_chart = (0, -5, 0, -40, -80)
    c4_e1, c6_e1, disc_e1 = invariants(*e1_chart)
    assert (c4_e1, c6_e1) == (2320, 134720)
    assert Fraction(c4_e1**3, disc_e1) == Fraction(-121945, 32)  # −5·29³/2⁵
    assert kraus_model(145, 2105) is None  # E₁ chart also NOT conductor 50

    # Its (−1)-twist F: (145, −2105) → minimal model y²+xy+y = x³+x²−3x+1,
    # Δ = −800 = −2⁵·5², multiplicative split at 2, additive II at 5 → N = 50.
    F_model = kraus_model(145, -2105)
    assert F_model == (1, 1, 1, -3, 1), F_model
    _, _, disc_F = invariants(*F_model)
    assert disc_F == -800 == -(2**5) * 5**2
    assert is_square_qp(2105, 2)  # −c₆(F) = 2105 ≡ 1 mod 8 → split → a₂ = +1
    a2_F = +1
    assert nonsingular_count(F_model, 2) == 2 - a2_F
    assert (valuation(145, 5), valuation(-2105, 5),
            valuation(disc_F, 5)) == (1, 1, 2)  # Kodaira II, f₅ = 2 → N = 50
    assert nonsingular_count(F_model, 5) == 5  # additive → a₅(F) = 0

    # cross-check (c): the two conductor-50 classes are √5-twist partners
    ap_F = {p: a_p(F_model, p) for p in GOOD_PRIMES}
    for p in GOOD_PRIMES:
        assert ap_F[p] == chi5(p) * ap_E[p], f"√5-twist relation fails @ {p}"
        assert a_p(e1_chart, p) == chi_minus1(p) * ap_F[p], f"E₁ chart @ {p}"
    assert a2_F == chi5(2) * a2_E  # χ₅(2) = −1: consistent at p = 2 too

    # ══ 4. THE X₀(50) TRACE IDENTITY on BDH22 eq (10) ═════════════════════
    # C₁ : B² = A⁶ + 4A⁵ + 10A³ + 4A + 1  (genus 2, = X₀(50) per BDH22 §4.3)
    sextic = (1, 4, 0, 10, 0, 4, 1)  # coefficients of A⁰..A⁶
    t_C1 = {}
    for p in GOOD_PRIMES:
        t_C1[p] = p + 1 - count_genus2_sextic(sextic, p)
        assert t_C1[p] == ap_E[p] + ap_F[p] == ap_E[p] * (1 + chi5(p)), \
            f"X₀(50) trace identity fails @ {p}"

    # ══ 5. The two candidate label signatures (NOT disambiguated) ═════════
    sig_I = {2: a2_E, 5: a5_E, **ap_E}    # class of E  (j(5τ₀) member shown)
    sig_II = {2: a2_F, 5: 0, **ap_F}      # twin class  (j(τ₀) member shown)

    hdr = "  p  : " + "  ".join(f"{p:3d}" for p in sorted(sig_I))
    print("\nInteger Hecke data (exact; the FIVE-filter gauntlet's filter 5):")
    print(hdr)
    print("  I  : " + "  ".join(f"{sig_I[p]:3d}" for p in sorted(sig_I))
          + "   [class of E: y²+xy+y = x³−x−2, Δ=−1250, w₂ = +1]")
    print("  II : " + "  ".join(f"{sig_II[p]:3d}" for p in sorted(sig_II))
          + "   [twin class: y²+xy+y = x³+x²−3x+1, Δ=−800, w₂ = −1]")
    print("  χ₅ : " + "  ".join(f"{chi5(p):3d}" for p in sorted(sig_I)))
    print("\nX₀(50) trace identity (Jac(X₀(50)) ~ the two classes, Eichler–"
          "Shimura):")
    print("  t_p(C₁) = a_p·(1+χ₅(p)) verified for all 13 good primes ✓")
    print("\nLabel disambiguation (50a vs 50b): NOT settleable offline — the "
          "paper never\nprints the equation of B/A₄ (its Sage-labelled 50a) "
          "and its printed E₁/E₂ charts\nare (−1)-twists with conductor ≠ 50. "
          "Single settling lookup:\n  https://www.lmfdb.org/EllipticCurve/Q/50/a/"
          "  (Cremona 50a1 minimal equation + a_p)")

    # ══ 6. Witness ════════════════════════════════════════════════════════
    wb.set_description(
        "X0(50)/50a integer Hecke gate (uploaded-papers idea A4; filter 5 of "
        "the tau-dictionary gauntlet, composing with the W8 t5=-10 validator "
        "and the W8b Fricke/sign filters). From the task curve y^2 = x^3 - "
        "675x - 79650 (j = -25/2 = j(5tau0)) the global minimal model y^2 + "
        "xy + y = x^3 - x - 2 (Delta = -1250, conductor 50: non-split "
        "multiplicative at 2 so a_2 = -1 and w_2 = +1; additive Kodaira IV at "
        "5 so a_5 = 0) is derived offline by Laska-Kraus-Connell, and a_p for "
        "all p <= 50, p not dividing 50, are computed by exact point-counting "
        "(Hasse bound asserted per prime). Cross-checks: BDH22's printed "
        "E1/E2 charts are (-1)-twists with conductor != 50 (chart twist-"
        "sloppiness finding); the (-1)-twist of the E1 chart is the twin "
        "conductor-50 class (y^2+xy+y = x^3+x^2-3x+1, Delta = -800, split at "
        "2) with a_p = chi5(p) a_p(E) (the Q(sqrt5) merge of BDH22); and on "
        "BDH22's own genus-2 X0(50) model (eq 10) the Frobenius trace "
        "identity t_p = a_p (1 + chi5(p)) holds at all 13 good primes "
        "(Eichler-Shimura), certifying {class(E), twin} = {50a, 50b}. WHICH "
        "of the two signatures is Cremona 50a is NOT decidable from the "
        "paper + offline arithmetic (the paper prints no equation for B/A4); "
        "both signatures are recorded and the single settling lookup is "
        "named (LMFDB EllipticCurve/Q/50/a). Audit-only; no fit; scope-(a)."
    )
    wb.set_audit_only("docs/audits/2026-07-25-x050-50a-hecke-gate.md")
    wb.add_parameter("good_primes", GOOD_PRIMES)
    wb.add_parameter("bad_primes", BAD_PRIMES)
    wb.add_parameter("task_curve", "y^2 = x^3 - 675x - 79650")
    wb.add_data("task_curve", {
        "short_model_a_invariants": [0, 0, 0, -675, -79650],
        "short_c4_c6_disc": [c4_s, c6_s, disc_s],
        "j_exact": "-25/2  (= j(5tau0), BDH22 eq (12); RR92/BN12 corrected)",
        "minimal_model": "y^2 + x y + y = x^3 - x - 2",
        "minimal_a_invariants": list(min_model),
        "minimal_c4_c6_disc": [c4_m, c6_m, disc_min],
        "conductor": conductor,
        "local_at_2": "multiplicative I1, non-split (-c6 = -1475 == 5 mod 8 "
                      "not in (Q_2*)^2) => a_2 = -1, Atkin-Lehner w_2 = +1",
        "local_at_5": "additive Kodaira IV (v(c4),v(c6),v(D)) = (2,2,4), "
                      "tame => f_5 = 2, a_5 = 0",
    })
    wb.add_data("hecke_signature_I_class_of_E", sig_I)
    wb.add_data("hecke_signature_II_twin_class", sig_II)
    wb.add_data("twin_class", {
        "minimal_model": "y^2 + x y + y = x^3 + x^2 - 3x + 1",
        "minimal_a_invariants": list(F_model),
        "minimal_c4_c6_disc": [145, -2105, disc_F],
        "j_exact": "-121945/32  (= j(tau0) = -5*29^3/2^5)",
        "conductor": 50,
        "local_at_2": "multiplicative I5, split => a_2 = +1, w_2 = -1",
        "relation": "a_p(twin) = chi5(p) * a_p(E) for all good p "
                    "(BDH22: 50a/50b merge over Q(sqrt5))",
    })
    wb.add_data("x050_trace_identity", {
        "genus2_model": "C1: B^2 = A^6 + 4A^5 + 10A^3 + 4A + 1 (BDH22 eq 10)",
        "t_p": t_C1,
        "identity": "t_p = a_p(E) * (1 + chi5(p)) for all 13 good primes",
    })
    wb.add_data("bdh22_exact_claims", {
        "prop_4_5": "The Q-isogeny class of the Jacobian of the P4-model of "
                    "Bring's curve is (50a)^4  [attributed to Ser08 Ex "
                    "8.3.2(b); proof note: 'the Q-isogeny class of B/A4 is "
                    "50a using the Cremona labels', computed in Sage]",
        "sec_4_3_x050": "C1 = B/<(12)(34)>: B^2 = A^6+4A^5+10A^3+4A+1 'is a "
                        "model for the modular curve X0(50)' (Igusa-Clebsch "
                        "vs LMFDB + direct Shimura-method model)",
        "sec_4_3_50b": "The Q-isogeny class of the elliptic curve "
                       "B/<(12)(34),(13)(24)> calculated via the HC-model is "
                       "50b ... 50b and 50a merge over Q[sqrt5]; 450b and 50a "
                       "merge over Q[rho]; 450b and 50b merge over "
                       "Q[sqrt(-15)]",
        "sec_2_2": "j(3tau0) = 5*211^3/2^15, j(15tau0) = -5^2*241^3/2^3; the "
                   "j(3tau0) curve is 50H and the j(5tau0) curve is 50E in "
                   "BK75 naming, 15-isogenous over Q; complete Q-isogeny "
                   "class of order four with periods tau0, 3tau0, 5tau0, "
                   "15tau0 [BK75]",
        "not_in_paper": "no equation for B/A4 is printed; no a_p table; the "
                        "printed E1/E2 chart equations are (-1)-twists with "
                        "conductor != 50 (identified in the paper via j over "
                        "C only)",
    })
    wb.add_data("label_disambiguation", {
        "status": "OPEN offline — recorded, not guessed",
        "settling_lookup": "https://www.lmfdb.org/EllipticCurve/Q/50/a/ "
                           "(Cremona 50a1): compare minimal equation / a_p "
                           "against signature I",
        "discriminating_primes": "any p with chi5(p) = -1 and a_p != 0, e.g. "
                                 "p = 2 (a_2 = -1 vs +1) or p = 3",
    })
    wb.add_caveat(
        "Point counts and reduction data are exact and unconditional. The "
        "identification {class(E), twin} = {50a, 50b} additionally uses "
        "Eichler-Shimura (Jac(X0(50)) ~ product of the two level-50 newform "
        "classes) + BDH22's identification of C1 with X0(50); the 13-prime "
        "trace identity is the falsifier for that composite claim and it "
        "passes. Which class carries the Cremona LABEL 50a is a table "
        "convention not derivable from arithmetic; it requires the named "
        "lookup. Gate usage: a candidate W-plane family must reproduce ONE "
        "of the two recorded signatures exactly (integers, no tolerance); "
        "failing both = refuted-as-stated, scope-(a)."
    )
    wb.add_assertion(
        "j_invariant_exact",
        computed=str(j_task), expected="-25/2", tolerance=None,
        source="j = c4^3/Delta of y^2 = x^3-675x-79650, exact Fraction; "
               "matches BDH22 eq (12) j(5tau0) = -25/2.",
    )
    wb.add_assertion(
        "minimal_model_conductor_50",
        computed=f"model={min_model}, Delta={disc_min}, N={conductor}",
        expected="model=(1, 0, 1, -1, -2), Delta=-1250, N=50", tolerance=None,
        source="Laska-Kraus-Connell offline; f_2 = 1 (mult I1), f_5 = 2 "
               "(additive IV, tame at p = 5).",
    )
    wb.add_assertion(
        "hasse_bound_all_primes",
        computed=max(ap_E[p] * ap_E[p] / (4 * p) for p in GOOD_PRIMES),
        expected=0.0, tolerance=1.0,
        source="a_p^2 <= 4p asserted per prime (exact integer check in-loop; "
               "this witness field records max a_p^2/4p < 1).",
    )
    wb.add_assertion(
        "x050_trace_identity_13_primes",
        computed=sum(abs(t_C1[p] - ap_E[p] * (1 + chi5(p)))
                     for p in GOOD_PRIMES),
        expected=0, tolerance=0,
        source="t_p(C1) = a_p(E)(1 + chi5(p)) on BDH22 eq (10), all 13 good "
               "primes p <= 50 — Eichler-Shimura certification that "
               "{class(E), twin} = {50a, 50b}.",
    )
    wb.add_assertion(
        "sqrt5_twin_relation",
        computed=sum(abs(ap_F[p] - chi5(p) * ap_E[p]) for p in GOOD_PRIMES),
        expected=0, tolerance=0,
        source="a_p(twin) = chi5(p) a_p(E) for all good p, plus a_2: -1 vs "
               "+1 with chi5(2) = -1 — BDH22's '50a/50b merge over Q(sqrt5)' "
               "realized as the quadratic twist by 5.",
    )
    charts_verdict = (
        "charts-are-minus1-twists-not-conductor-50"
        if (kraus_model(25, -1475) is None and kraus_model(145, 2105) is None)
        else "unexpected"
    )
    wb.add_assertion(
        "bdh22_charts_are_minus1_twists",
        computed=charts_verdict,
        expected="charts-are-minus1-twists-not-conductor-50", tolerance=None,
        source="Both printed E2 charts and the E1 chart satisfy a_p = "
               "chi_{-1}(p) x (their conductor-50 partner) at all good p "
               "(asserted in-loop), and kraus_model(25,-1475) = "
               "kraus_model(145,2105) = None (no integral model, so additive "
               "at 2, conductor != 50). Finding: BDH22's printed chart "
               "equations are twist-sloppy (identified via j over C only) — "
               "no printed equation pins the Cremona label offline.",
    )
    wb.save()
    print("\nwitness saved; all assertions passed.")


if __name__ == "__main__":
    main()
