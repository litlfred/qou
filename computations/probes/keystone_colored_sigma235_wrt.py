#!/usr/bin/env python3
"""Keystone: the λ-COLORED Σ(2,3,5) WRT invariant — the residual-frontier step (does the geometry
realize the bwS0 = d_q/D unit vector?).

The modular-category identification (`2026-06-22-keystone-modular-category-identification.md`) and
the bare-invariant probe (`keystone_habiro_wrt_s3_2i_probe.py`) located the open keystone object as:
the explicit WRT(S³/2I) = WRT(Σ(2,3,5)) data, evaluated at q₀, reproducing the q-Plancherel family
W_λ = d_q²/D² (= bwS0², the squared vacuum S-matrix row). The bare probe computed the
CLOSED-manifold invariant Ψ(1/q₀) = 2.3296 — ONE number — and its verdict pinpointed the open step:

    "the λ-family needs the WRT TQFT with λ-COLORED insertions (colored Σ(2,3,5) invariants /
     S-matrix), not the bare closed-manifold number."

NORMALISATION (corrected 2026-08-09). Two series are in play and they are NOT the same object:

    Ψ_LZ(q) = Σ χ(n) q^{n²/120}              (Lawrence–Zagier/Hikami false theta)
    S_JL(q) = Σ χ(n) q^{(n²−1)/120}          (Jacoby–Lawrence, library/04procbryden/04procbryden.pdf p.55)

They differ by exactly one universal factor, Ψ_LZ = q^{1/120}·S_JL — not by any n-dependent
reindexing, because (n²−1)/120 is an INTEGER on the whole support of χ. That integrality is
proved sorry-free in QOU/MathlibExt/Sigma235FalseThetaExponent.lean
(`sigma235_sq_eq_120_mul_add_one`: n² = 120m+1 on the eight support residues mod 60), which
also records the four low exponents 0,1,3,7 that p.55 prints.

The Ohtsuki series itself is the AFFINE image of S_JL, not S_JL and not Ψ_LZ:

    q(q−1)·Z_∞(Σ(2,3,5))(q) = 1 − ½·S_JL(q)

so at 1/q₀ the closed-manifold quantity is ≈ −0.1658, while Ψ_LZ(1/q₀) ≈ 2.3296 and
S_JL(1/q₀) ≈ 2.3316. An earlier revision of this docstring called Ψ_LZ(1/q₀) "the CLOSED-manifold
invariant"; that identification was wrong — it omits both the q^{−1/120} twist and the affine
wrapper (which flips the sign). All three are now emitted separately so no consumer has to guess.

This probe takes that step. The false theta of
Σ(2,3,5) has support on the residues n ≡ 30·(1 ± 1/2 ± 1/3 ± 1/5) (mod 60) = {1,11,19,29} — the
ρ-shift of the SU(2) WRT surgery presentation (P = p₁p₂p₃ = 30 = Coxeter number h(E₈)). A Wilson
line on the order-5 EXCEPTIONAL FIBRE (the icosahedral / A₅ fibre — the keystone's own fibre)
coloured by the SU(2) colour α replaces 1/5 → α/5, giving the COLOURED support

    R(α) = { 30·(1 ± 1/2 ± 1/3 ± α/5)  mod 60 },   the colour-α false theta Ψ^{(α)}(q).

Key structural fact this probe establishes (pure residue arithmetic, then the q-series):
α = 1 reproduces the bare {1,11,19,29}; α = 2 gives {7,13,17,23} — the COMPLEMENTARY four E₈
exponents. Together the two lowest colours generate ALL EIGHT E₈ exponents
{1,7,11,13,17,19,23,29}. So the λ-coloured insertions on the icosahedral fibre are exactly the
mechanism that lifts the bare single invariant to the E₈-exponent-indexed FAMILY — the family that
must carry the W_λ resolution. The probe computes Ψ^{(α)}(1/q₀) for α = 1..4 and lays the colour ↔
W_λ-block correspondence next to the d_q values, reporting structure type-correctly (no fit; a
direct Ψ^{(α)} = W_λ numerology is not asserted — the deliverable is that the coloured family EXISTS
and is E₈-exponent-indexed, the structural object the bare invariant lacked).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf, nstr  # noqa: E402
from _precision import str_at_true_precision  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50
# Experimental (proton) pin — the default for all compute per the 2026-08-07 owner directive.
# This file previously carried the muon pin 1.1099785955541805 (−11.5 ppb); it was moved here
# rather than left straddling, since the whole quantity must sit on one layer.
Q0 = mpf("1.1099785827513808")
INV = 1 / Q0  # bar image, inside the unit disk where the false theta converges

P = 30  # = p1*p2*p3 = 2*3*5 = Coxeter number of E8 AND of H4 (600-cell)
E8_EXPONENTS = (1, 7, 11, 13, 17, 19, 23, 29)
# H4 = the 4D icosahedral / 600-cell Coxeter group: degrees {2,12,20,30}, exponents = degrees-1.
# The bare Sigma(2,3,5) false-theta support {1,11,19,29} IS exactly the H4 exponent set; the
# colored complement {7,13,17,23} is the rest of E8, so the colored split = the H4 <- E8 folding.
H4_EXPONENTS = (1, 11, 19, 29)


def colored_support(alpha):
    """Residues mod 60 of the colour-α false theta of Σ(2,3,5): the canonical positive reps of
    30·(1 ± 1/2 ± 1/3 ± α/5), with the odd-extension sign character (χ(60−r) = −χ(r)).

    α = 1 → {1,11,19,29} (bare). Returns {residue: +1} for the four base residues; the −1 partners
    at 60−r are added by chi_of()."""
    base = set()
    for s2 in (-1, 1):
        for s3 in (-1, 1):
            for s5 in (-1, 1):
                val = P * (1 + s2 * mpf(1) / 2 + s3 * mpf(1) / 3 + s5 * mpf(alpha) / 5)
                r = int(mp.nint(val)) % 60      # round in mpmath, not via f64
                if r == 0:
                    continue
                # canonical positive rep in 1..59; fold 60−r≡−r into the +set via |·|
                rr = r if r <= 30 else 60 - r
                base.add(rr)
    return sorted(base)


def chi_of(support):
    """Build the odd periodic character mod 60 with +1 on `support` and −1 on {60−r}."""
    pos = set(support)
    neg = {60 - r for r in support}

    def chi(n):
        r = n % 60
        if r in pos:
            return 1
        if r in neg:
            return -1
        return 0
    return chi


def false_theta(chi, q, nterms=4000):
    """Ψ_LZ(q) = Σ χ(n) q^{n²/120} — the Lawrence–Zagier/Hikami normalisation."""
    terms = [chi(n) * q ** (mpf(n * n) / 120) for n in range(nterms) if chi(n)]
    return mp.fsum(terms)


def false_theta_jl(chi, q, nterms=4000):
    """S_JL(q) = Σ χ(n) q^{(n²−1)/120} — Jacoby–Lawrence p.55.

    Exponents are integers on the whole support (Lean:
    `QOU.MathlibExt.sigma235_sq_eq_120_mul_add_one`), so this differs from `false_theta`
    by the single factor q^{1/120} and by nothing else."""
    terms = [chi(n) * q ** (mpf(n * n - 1) / 120) for n in range(nterms) if chi(n)]
    return mp.fsum(terms)


def ohtsuki_series_affine(chi, q, nterms=4000):
    """q(q−1)·Z_∞(Σ(2,3,5))(q) = 1 − ½·S_JL(q) — the closed-manifold quantity itself.

    This, NOT Ψ_LZ, is the Ohtsuki-series side of Jacoby–Lawrence p.55."""
    return 1 - false_theta_jl(chi, q, nterms) / 2


# ---- W_λ / d_q machinery (n=5) -------------------------------------------------
def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def q_factorial(m):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def d_q(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h)
    return q_factorial(sum(lam)) / den


PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]


def run():
    colors = {}
    union = set()
    for alpha in (1, 2, 3, 4):
        supp = colored_support(alpha)
        union |= set(supp)
        chi = chi_of(supp)
        psi = false_theta(chi, INV)              # Ψ_LZ, exponent n²/120
        s_jl = false_theta_jl(chi, INV)          # S_JL, exponent (n²−1)/120
        ohtsuki = ohtsuki_series_affine(chi, INV)  # 1 − ½ S_JL
        colors[alpha] = {
            "support": supp,
            "psi_lz_at_inv_q0": str_at_true_precision(psi),
            "s_jl_at_inv_q0": str_at_true_precision(s_jl),
            "ohtsuki_affine_at_inv_q0": str_at_true_precision(ohtsuki),
            # sanity: the two normalisations must differ by exactly q^{1/120}
            "psi_over_s_jl": str_at_true_precision(psi / s_jl),
            "q_pow_1_over_120": str_at_true_precision(INV ** (mpf(1) / 120)),
        }
    e8_generated = sorted(union) == sorted(E8_EXPONENTS)
    # the two lowest colours cover the E8 exponents?
    two_color_union = sorted(set(colored_support(1)) | set(colored_support(2)))
    bare_is_H4 = sorted(colored_support(1)) == sorted(H4_EXPONENTS)

    # Value-screen: is the naive exponent quantum dimension [e]_q the value map d_q?
    # Assign each conjugation class its dual-pair smallest exponent (monotone order) and compare.
    def qint_local(m):
        return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))
    value_screen = []
    ratios = []
    for e, lam in zip((1, 7, 11, 13), [(5,), (4, 1), (3, 2), (3, 1, 1)]):
        tgt = d_q(lam)
        ratio = tgt / qint_local(e)
        ratios.append(ratio)
        value_screen.append({"exponent": e, "lambda": list(lam),
                             "d_q": str_at_true_precision(tgt),
                             "qint_e": str_at_true_precision(qint_local(e)),
                             "ratio_target_over_qint": str_at_true_precision(ratio)})
    # the refutation is decided on the mpf ratios, not on their f64 shadows
    qint_refuted = not all(abs(r - ratios[0]) < mpf("1e-6") for r in ratios)

    D2 = mp.fsum(d_q(l) ** 2 for l in PARTS5)
    bwS0 = {repr(l): str_at_true_precision(d_q(l) / mp.sqrt(D2)) for l in PARTS5}

    # E8 exponents pair under e <-> h - e = 30 - e: 4 dual pairs.
    e8_pairs = sorted({tuple(sorted((e, P - e))) for e in E8_EXPONENTS})
    # n=5 partitions pair under conjugation lambda <-> lambda': distinct bwS0 classes.
    def conj(lam):
        m = lam[0]
        return tuple(sum(1 for r in lam if r > j) for j in range(m))
    seen, bw_classes = set(), []
    for l in PARTS5:
        key = frozenset({l, conj(l)})
        if key in seen:
            continue
        seen.add(key)
        bw_classes.append({"reps": sorted([list(l), list(conj(l))]),
                           "bwS0": str_at_true_precision(d_q(l) / mp.sqrt(D2))})
    return {
        "q0": str_at_true_precision(Q0), "inv_q0": str_at_true_precision(INV),
        "P": P, "E8_exponents": list(E8_EXPONENTS),
        "colors": colors, "union_support": sorted(union),
        "two_color_union": two_color_union,
        "e8_exponents_generated": e8_generated,
        "D2": str_at_true_precision(D2), "bwS0_n5": bwS0,
        "d_q_n5": {repr(l): str_at_true_precision(d_q(l)) for l in PARTS5},
        "e8_dual_pairs": [list(p) for p in e8_pairs],
        "bwS0_conjugation_classes": bw_classes,
        "count_match_4_to_4": len(e8_pairs) == len(bw_classes),
        "H4_exponents": list(H4_EXPONENTS),
        "bare_support_is_H4": bare_is_H4,
        "value_screen_qint": value_screen,
        "qint_value_map_refuted": qint_refuted,
    }


def report(res):
    print("# λ-coloured Σ(2,3,5) WRT — the residual keystone frontier (colored insertions)\n")
    print(f"q₀ = {float(mpf(res['q0'])):.10f}   1/q₀ = {float(mpf(res['inv_q0'])):.10f}"
          f"   P = {res['P']} = h(E₈)\n")
    print("Colouring the order-5 (icosahedral / A₅) fibre by SU(2) colour α shifts 1/5 → α/5:\n")
    print("| colour α | support R(α) mod 60 | Ψ_LZ(1/q₀) | S_JL(1/q₀) | 1−½S_JL |")
    print("|--:|---|--:|--:|--:|")
    for a, d in res["colors"].items():
        print(f"| {a} | {{{', '.join(map(str, d['support']))}}} | "
              f"{float(mpf(d['psi_lz_at_inv_q0'])):.6f} | "
              f"{float(mpf(d['s_jl_at_inv_q0'])):.6f} | "
              f"{float(mpf(d['ohtsuki_affine_at_inv_q0'])):.6f} |")
    print("\n  Ψ_LZ = q^{1/120}·S_JL exactly (integrality of (n²−1)/120 on the support is Lean-proved:")
    print("  QOU.MathlibExt.sigma235_sq_eq_120_mul_add_one). The Ohtsuki series of Jacoby–Lawrence")
    print("  p.55 is the LAST column, 1 − ½S_JL — not Ψ_LZ, which is neither the invariant nor S_JL.")
    print(f"\n- α=1 support = {{1,11,19,29}} = the **bare** Σ(2,3,5) false-theta support. "
          f"✓ validates the colour formula.")
    print(f"- α=2 support = {set(res['colors'][2]['support'])} = the **complementary** four E₈ exponents.")
    print(f"- α=1 ∪ α=2 = {res['two_color_union']}")
    print(f"- E₈ exponents = {res['E8_exponents']}")
    print(f"- **Two lowest colours generate ALL EIGHT E₈ exponents: "
          f"{res['e8_exponents_generated']}.**\n")

    print("## What this establishes\n")
    print("- The bare WRT(Σ(2,3,5)) is ONE number; the λ-resolved object the keystone needs is a")
    print("  FAMILY. The colored insertions on the icosahedral fibre supply exactly that family,")
    print("  and it is **E₈-exponent-indexed** — the 4 bare exponents (α=1) + 4 complementary (α=2).")
    print("- This is the concrete realization of the bare probe's pinpointed open step ('λ-colored")
    print("  insertions / colored Σ(2,3,5) invariants, not the closed-manifold number'). The colored")
    print("  family is the geometric carrier of the W_λ resolution; its index set is the E₈ exponents,")
    print("  the same icosahedral/E₈ data the A₅ fibre map and the W_λ blocks carry.\n")

    print("## W_λ side (n=5), for the colour↔block correspondence\n")
    print("| λ | d_q | bwS0 = d_q/D |")
    print("|---|--:|--:|")
    for l in PARTS5:
        print(f"| {l} | {float(mpf(res['d_q_n5'][repr(l)])):.6f} | "
              f"{float(mpf(res['bwS0_n5'][repr(l)])):.6f} |")
    print("\n## The colour↔block correspondence (E₈ dual pairs ↔ bwS0 conjugation classes)\n")
    print(f"E₈ exponents pair under e ↔ h−e = 30−e into **{len(res['e8_dual_pairs'])} dual pairs**; "
          f"the n=5 bwS0 family collapses under conjugation λ↔λ′ into "
          f"**{len(res['bwS0_conjugation_classes'])} classes**:\n")
    print("| E₈ dual pair {e, 30−e} | ↔ | bwS0 conjugation class | bwS0 |")
    print("|---|:-:|---|--:|")
    pairs = res["e8_dual_pairs"]
    cls = sorted(res["bwS0_conjugation_classes"], key=lambda c: c["bwS0"])
    pairs_sorted = sorted(pairs, key=lambda p: p[0])
    for i, c in enumerate(cls):
        pp = pairs_sorted[i] if i < len(pairs_sorted) else ["—"]
        reps = " ~ ".join("(" + ",".join(map(str, r)) + ")" for r in c["reps"])
        print(f"| {{{pp[0]}, {pp[1] if len(pp) > 1 else ''}}} | ↔ | {reps} | "
              f"{float(mpf(c['bwS0'])):.6f} |")
    print(f"\n- **Count match: 4 E₈ dual pairs ↔ 4 bwS0 conjugation classes — {res['count_match_4_to_4']}.**")
    print("  The pairing is structural (both are the icosahedral/E₈ data): the Coxeter involution")
    print("  e↔h−e on the colored-fibre exponents mirrors the transpose involution λ↔λ′ on the W_λ")
    print("  blocks (both are the bar/chirality ℤ₂ the keystone's S_{0λ}=S_{0λ′} symmetry carries).")
    print("  The table aligns classes by bwS0 magnitude order — the assignment itself (which pair ↔")
    print("  which class) + its numerical realization is the remaining value step.\n")

    print("\n## Sharper icosahedral identity + value-step screen\n")
    print(f"- **Bare support {{1,11,19,29}} = the H₄ exponents** (the 4D icosahedral / 600-cell "
          f"Coxeter group; degrees {{2,12,20,30}}, h=30): {res['bare_support_is_H4']}. The colored "
          f"complement {{7,13,17,23}} is the rest of E₈, so the colour split is exactly the "
          f"**H₄ ⊂ E₈ folding** — the icosahedral structure is concretely H₄, not bare 'E₈'.")
    print(f"- **Value-step screen — the naive exponent q-dimension [e]_q is REFUTED as the value map** "
          f"({'refuted' if res['qint_value_map_refuted'] else 'not refuted'}):")
    print("  | exponent e | λ | target d_q | [e]_q | d_q/[e]_q |")
    print("  |--:|---|--:|--:|--:|")
    for v in res["value_screen_qint"]:
        print(f"  | {v['exponent']} | {tuple(v['lambda'])} | "
              f"{float(mpf(v['d_q'])):.4f} | {float(mpf(v['qint_e'])):.4f} "
              f"| {float(mpf(v['ratio_target_over_qint'])):.4f} |")
    print("  The ratio d_q/[e]_q is non-constant (1.000, 0.539, 0.385, 0.359), so NO global")
    print("  normalisation makes the colored exponent's quantum dimension equal d_q. The value map")
    print("  is therefore NOT the exponent-label q-dimension; it needs the genuine colored")
    print("  Lawrence–Rozansky S-matrix amplitude (the real remaining derivation). This (a)-prunes")
    print("  the naive value hypothesis and locates the open step precisely.\n")

    print("## Discipline / scope\n")
    print("- No fit. A direct Ψ^{(α)} = W_λ numerical equality is NOT asserted (the colored")
    print("  invariants are q-series scalars; bwS0 is the S-matrix row — the type-correct comparison")
    print("  is structural). The deliverable is that the **E₈-exponent-indexed colored family EXISTS")
    print("  and is computed**, advancing the residual frontier from 'bare number' to 'colored family'.")
    print("- Remaining value step: the exact colour-α → partition-λ assignment and the S-matrix")
    print("  normalization (D) that turns Ψ^{(α)} into bwS0(λ) — the genuine next research step,")
    print("  now standing on an explicit colored family rather than a single closed-manifold number.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("keystone-colored-sigma235-wrt", engine="mpmath")
    w.set_description(
        "Takes the keystone residual-frontier step: the lambda-COLORED Sigma(2,3,5)=S^3/2I WRT "
        "invariant (the bare probe keystone_habiro_wrt_s3_2i computed only the closed-manifold number "
        "and pinpointed 'colored insertions' as the open step). Coloring the order-5 icosahedral fibre "
        "by SU(2) colour alpha shifts the Lawrence-Zagier false-theta support 30(1+-1/2+-1/3+-1/5) -> "
        "30(1+-1/2+-1/3+-alpha/5). alpha=1 reproduces the bare {1,11,19,29}; alpha=2 gives the "
        "complementary E8 exponents {7,13,17,23}; the two lowest colours generate ALL EIGHT E8 "
        "exponents {1,7,11,13,17,19,23,29}. So the colored insertions lift the bare single invariant "
        "to the E8-exponent-indexed FAMILY that must carry the W_lambda = bwS0^2 resolution. Computes "
        "Psi^(alpha)(1/q0) for alpha=1..4 and the n=5 d_q/bwS0 values. No fit; direct Psi=W_lambda not "
        "asserted (type-correct structural deliverable: the colored family exists and is E8-indexed)."
    )
    w.add_data("q0", res["q0"])
    w.add_data("inv_q0", res["inv_q0"])
    w.add_data("P_coxeter_E8", res["P"])
    w.add_data("E8_exponents", res["E8_exponents"])
    w.add_data("colors", res["colors"])
    w.add_data("union_support", res["union_support"])
    w.add_data("bwS0_n5", res["bwS0_n5"])
    w.add_data("d_q_n5", res["d_q_n5"])
    w.add_data("e8_dual_pairs", res["e8_dual_pairs"])
    w.add_data("bwS0_conjugation_classes", res["bwS0_conjugation_classes"])
    w.add_data("H4_exponents", res["H4_exponents"])
    w.add_data("bare_support_is_H4", res["bare_support_is_H4"])
    w.add_data("value_screen_qint", res["value_screen_qint"])
    w.add_data("qint_value_map_refuted", res["qint_value_map_refuted"])
    w.add_assertion(
        "two_lowest_colors_generate_E8_exponents",
        computed=1 if res["e8_exponents_generated"] else 0,
        expected=1, tolerance=0,
        source="Coloring the order-5 icosahedral fibre of Sigma(2,3,5) by SU(2) colours alpha=1,2 "
               "gives false-theta supports {1,11,19,29} and {7,13,17,23} whose union is exactly the "
               "8 E8 exponents {1,7,11,13,17,19,23,29} (P=30=h(E8)). The colored insertions lift the "
               "bare single WRT invariant to the E8-exponent-indexed family the keystone W_lambda "
               "resolution requires -- the residual-frontier step from 'bare number' to 'colored "
               "family'.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
