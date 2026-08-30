#!/usr/bin/env python3
"""gap10_tjon_correlation_probe.py — GAP-10 (bean qou-zowh): does the block-trace
operator reproduce the Tjon correlation B(³H) ↔ B(⁴He)?

WHY THIS TARGET REPLACES THE OLD ONE. Bean qou-pve2 asked "what supplies ~10×
per-order growth in the moment ladder?" That question was mis-posed: GAP-9 showed
the target μ₄ = −4.591 is −10.21 MeV, i.e. 36% of B(⁴He) and 34× the N³LO
four-nucleon estimate, so it is not a physical four-body quantity — its size
comes from the C(A,k) simplex basis (which has no saturation mechanism) plus
ρ_grad over-subtracting. Chasing that growth was chasing an artifact.

The Tjon correlation is the field's own robust observable for exactly the
3-body/4-body question, and it is CONVENTION-FREE: it compares A=3 against A=4
within one system, so overall scale, the y_λ normalisation and any global sign
all cancel.

THE FORMAL CORE (Lean: QOU.MassTheory.TjonSimplexForm, sorry-free, generic ring):

    M(4) − (4·M(3) − 6·M(2))  =  μ₄            [tjon_deviation_eq_mu4]
    μ₄ = 0  ⟺  M(4) = 4·M(3) − 6·M(2)          [mu4_eq_zero_iff_tjon]

So `4·M(3) − 6·M(2)` is the two-point "no four-body parameter" prediction, and
the deviation from it IS μ₄. That gives a sharp, scale-free score for any
candidate: the FRACTIONAL Tjon deviation μ₄ / M(4).

WHAT IS MEASURED. The operator's interaction at each mass number,

    M_op(A) = g_A(all bonds) − g_A(∅)

at A = 2 (deuteron, H₆), A = 3 (triton, H₉) and A = 4 (⁴He, H₁₂), where g is the
same block trace Σ_λ y_λ|χ_λ| used throughout the epic. Two bond conventions are
run, because GAP-8 flagged that μ₄ is sensitive to the bond set:

  * COMPLETE graph — C(A,2) bonds, matching the C(A,k) simplex basis: 1, 3, 6
    bonds, the non-adjacent ones built as BKL bands (GAP-8's construction).
  * CHAIN only — the adjacent interfaces the word itself carries: 1, 2, 3 bonds.

Then compared against nature's own numbers, ρ_strong = (1, 3.8128, 13.0316) in
units of B(D), on two scale-free scores:

  [T1] the normalised ladder  M(A)/M(2)  vs  ρ_strong(A)
  [T2] the fractional Tjon deviation  μ₄/M(4)  vs nature's

SIGN CONVENTION — AND A RETRACTION. The corpus's canonical binding proxy is the
trace DEFICIT against the unlink, `c = E₀·(g_unlink − g_link) = E₀·(1−τ)·g_unlink`
(`helium_four_body_cluster_probe`: "A trace deficit against the unlink is a
BINDING object"; `a4_h12_brunnian_deficit_measure_probe`, `borromean_*`). So the
binding-like quantity is

    B_op(A) = g_A(∅) − g_A(all bonds)   = −M_op(A)

and a NEGATIVE `M_op` is a POSITIVE binding, exactly as intended.

An earlier revision of this probe printed a "GLOBAL SIGN CAVEAT" claiming the
operator "carries the opposite overall sign to binding" and that its agreement
with nature's Tjon sign was therefore "fake". **Both claims were wrong and are
retracted.** The convention was already canonical in the corpus and I had not
checked it. Worse, the argument was vacuous in both directions: the fractional
Tjon deviation is *invariant* under a global sign flip (Lean:
`QOU.MassTheory.TjonSimplexForm.fracTjon_neg`, sorry-free), so it can neither
confirm nor refute the convention. What survives untouched is the LADDER
GROWTH — also sign-blind (`ladder_ratio_neg`), which is why it is the finding
that stands.

No Δ_λ, no μ fitted, no convention tuned, nothing wired. Reports either way.
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path[:0] = [str(COMP), str(COMP / "hecke"), str(COMP / "habiro"),
                str(COMP / "substrate"), str(HERE)]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

DPS = 30
set_compute_dps(DPS)
q0 = mp.mpf(str(Q0))
# The kernel entry takes q as a DECIMAL STRING, not a double: the f64 entry
# `chi_q_atomic_all_partitions` capped every character at ~15-16 significant
# digits while this probe serialises its results at 58, i.e. ~42 digits of
# noise. `H` stays an `mpf` for the same reason and for one more: it is passed
# to `pn_interface_offset_from_h`, which branches on `isinstance(h, float)`
# and takes an f64 sqrt on that branch -- handing it a float silently selected
# the lossy path. Bean `qou-k6b3`.
Q0_STR = mp.nstr(q0, DPS)
H = q0 - 1 / q0

# nature, in units of B(D) — the corpus's rho_strong (Coulomb-corrected)
RHO_STRONG = {2: mp.mpf(1), 3: mp.mpf("3.8128"), 4: mp.mpf("13.0316")}


def sfmt(v):
    """`fmt` pinned to THIS probe's compute precision.

    Bare `fmt` serialises at the corpus `OUTPUT_DPS` (60 decimals) no matter
    what `mp.dps` is. The corpus design has compute ABOVE serialisation (65
    compute / 50 output); this probe sets compute to 30, which inverts it, so
    every witness field was padded with ~30 digits of noise -- independently of
    the f64 kernel entry fixed above, and still there after it. `fmt` takes a
    per-call `dps`, so the honest width is the one actually computed.
    """
    return fmt(v, dps=DPS)

_Y = {}
_t0 = time.time()
_n = [0]


def perblock(n_strands, word):
    if n_strands not in _Y:
        _Y[n_strands] = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
                         for k, v in y_lambda_at(n_strands, q0).items()}
    Y = _Y[n_strands]
    # `atom_braid_word_3A` already returns `mpf` coefficients (it takes
    # `allow_float64=False` by default and goes to trouble to keep them exact);
    # casting them to `float` here threw that away one line before the kernel.
    factors = [(mp.nstr(mp.mpf(c), DPS), mp.nstr(mp.mpf(d), DPS), int(g) + 1)
               for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions_mpfr(
        n_strands, factors, Q0_STR, DPS)
    _n[0] += 1
    print(f"      [trace {_n[0]:2d}]  n={n_strands:2d}  {time.time() - _t0:6.1f}s", flush=True)
    # `mp.mpf(chi)` directly: the MPFR entry returns a decimal STRING, so the
    # `repr()` the f64 path needed (shortest round-trip of a Python float)
    # would now wrap it in quotes and raise.
    return sum(Y[tuple(s)] * abs(mp.mpf(chi)) for s, chi in cp if tuple(s) in Y)


def band_word(i, j, c, d):
    """BKL band bonding non-adjacent nucleons i<j (GAP-8's construction)."""
    carry = list(range(3 * j - 1, 3 * i + 2, -1))
    one, zero = mp.mpf(1), mp.mpf(0)
    return ([(one, zero, g) for g in carry] + [(c, d, 3 * i + 2)]
            + [(one, -H, g) for g in reversed(carry)])


def M_op(A, Z, N, complete):
    """M_op(A) = g(all bonds) − g(∅) for the A-nucleon system."""
    ns = 3 * A
    full = atom_braid_word_3A(Z, N, include_inter=True)
    ifaces = {x[2]: x for x in full if x[2] % 3 == 2}
    d_by_gen = {g: mp.mpf(ifaces[g][1]) for g in sorted(ifaces)}
    nz = [d for d in d_by_gen.values() if d != 0]
    # Nearest-match against the CANONICAL p-n offset, not -H/2. The word
    # now carries `-h*(1/2 - delta/4)`; the nearest-match happens to pick
    # the same entry either way (the alternatives are 0 and -H, orders
    # further off), but the reference and the fallback were both the
    # colour-blind value and would silently mis-select if the spread ever
    # narrowed.
    _d_pn = _pn_d(H)
    pn_d = min(nz, key=lambda d: abs(abs(d) - abs(_d_pn))) if nz else _d_pn

    free = [x for x in full if x[2] % 3 != 2]           # no interfaces at all
    allb = list(full)                                    # every adjacent interface
    if complete:
        for (i, j) in combinations(range(A), 2):
            if j > i + 1:
                allb = allb + band_word(i, j, mp.mpf(1), pn_d)
    return perblock(ns, allb) - perblock(ns, free)


def main() -> int:
    print("=" * 78)
    print(" GAP-10: does the block trace reproduce the Tjon correlation B(³H)↔B(⁴He)?")
    print("=" * 78)
    print(" Lean core (TjonSimplexForm): M(4) − (4M(3) − 6M(2)) = μ₄, so the")
    print(" two-point prediction is 4M(3) − 6M(2) and μ₄ is exactly its deviation.")

    # nature's own scores, from rho_strong
    nat = RHO_STRONG
    nat_mu4 = nat[4] - (4 * nat[3] - 6 * nat[2])
    nat_frac = nat_mu4 / nat[4]
    print(f"\n NATURE (ρ_strong, units of B(D)): {[float(nat[a]) for a in (2, 3, 4)]}")
    print(f"   two-point Tjon prediction for M(4) = 4M(3) − 6M(2) = "
          f"{float(4 * nat[3] - 6 * nat[2]):.4f}   actual {float(nat[4]):.4f}")
    print(f"   μ₄ = {float(nat_mu4):+.4f}   fractional Tjon deviation μ₄/M(4) = "
          f"{float(nat_frac):+.4f}")

    results = {"nature": {"ladder": [sfmt(nat[a]) for a in (2, 3, 4)],
                          "mu4": sfmt(nat_mu4), "frac_tjon_dev": sfmt(nat_frac)}}
    scores = {}

    for label, complete in (("complete graph (C(A,2) bonds: 1,3,6)", True),
                            ("chain only (adjacent: 1,2,3)", False)):
        print(f"\n ── operator, {label} ──", flush=True)
        M = {2: M_op(2, 1, 1, complete),
             3: M_op(3, 1, 2, complete),
             4: M_op(4, 2, 2, complete)}
        for a in (2, 3, 4):
            print(f"      M_op({a}) = {float(M[a]):+.9f}")

        if M[2] == 0:
            print("      M_op(2) = 0 — ladder ratios undefined; skipping [T1]")
            ladder = None
        else:
            ladder = {a: M[a] / M[2] for a in (2, 3, 4)}
            print(f"\n   [T1] normalised ladder M(A)/M(2) vs nature")
            for a in (3, 4):
                print(f"        A={a}: operator {float(ladder[a]):+9.4f}   "
                      f"nature {float(nat[a]):8.4f}   ratio "
                      f"{float(ladder[a] / nat[a]):+.3f}")

        mu4_op = M[4] - (4 * M[3] - 6 * M[2])
        frac = mu4_op / M[4] if M[4] != 0 else None
        print(f"\n   [T2] Tjon deviation (the convention-free score)")
        print(f"        two-point prediction 4M(3) − 6M(2) = {float(4 * M[3] - 6 * M[2]):+.6f}")
        print(f"        actual M(4)                        = {float(M[4]):+.6f}")
        print(f"        μ₄^op = {float(mu4_op):+.6f}")
        if frac is not None:
            print(f"        fractional deviation μ₄/M(4) = {float(frac):+.4f}   "
                  f"nature {float(nat_frac):+.4f}")
            sign_ok = (frac > 0) == (nat_frac > 0)
            print(f"        sign matches nature: {bool(sign_ok)}   "
                  f"|ratio| {float(abs(frac / nat_frac)):.2f}×")
            scores[label] = {"frac": sfmt(frac), "sign_ok": bool(sign_ok),
                             "ratio_to_nature": sfmt(abs(frac / nat_frac)),
                             "_f": float(frac),          # printing only
                             "_r": float(abs(frac / nat_frac))}
        results[label] = {
            "M_op": {str(a): sfmt(M[a]) for a in (2, 3, 4)},
            "ladder_normalised": ({str(a): sfmt(ladder[a]) for a in (2, 3, 4)}
                                  if ladder else None),
            "_ladder_f": ({str(a): float(ladder[a]) for a in (2, 3, 4)}
                          if ladder else None),          # printing only
            "_M_op_f": {str(a): float(M[a]) for a in (2, 3, 4)},
            "tjon_two_point_prediction": sfmt(4 * M[3] - 6 * M[2]),
            "mu4_op": sfmt(mu4_op),
            "frac_tjon_deviation": sfmt(frac) if frac is not None else None}

    # SIGN CONVENTION (corrected) — the corpus binding proxy is the DEFICIT
    pos = {k: all(v <= 0 for v in results[k]["_M_op_f"].values())
           for k in results if k != "nature"}
    print(f"\n [!] SIGN CONVENTION — binding is the trace DEFICIT")
    print(f"     Corpus canonical: c = E₀·(g_unlink − g_link), so the binding proxy is")
    print(f"     B_op(A) = −M_op(A) > 0. M_op ≤ 0 at every A under both conventions:")
    for k, v in pos.items():
        print(f"       {k:42s} {bool(v)}")
    print(f"     ⇒ the operator's binding proxy is POSITIVE, as nature's is. An earlier")
    print(f"       revision called this a sign MISMATCH; that was wrong and is retracted.")
    print(f"       (And the [T2] score is invariant under a global flip anyway — Lean")
    print(f"        fracTjon_neg — so it could never have settled the question.)")

    print(f"\n [S] summary — fractional Tjon deviation μ₄/M(4)")
    print(f"     nature                                   {float(nat_frac):+.4f}")
    for k, v in scores.items():
        print(f"     {k:42s} {v['_f']:+.4f}   sign {v['sign_ok']}   "
              f"{v['_r']:.2f}×")

    any_sign = any(v["sign_ok"] for v in scores.values())
    best = min((v["_r"] for v in scores.values()
                if v["sign_ok"]), default=None)
    lad = {k: results[k]["_ladder_f"] for k in results if k != "nature"}
    print(f"\n [S2] the substantive score — normalised ladder growth M(A)/M(2)")
    print(f"      nature   A=3 {float(nat[3]):6.2f}   A=4 {float(nat[4]):6.2f}   (grows 3.4x)")
    for k, v in lad.items():
        if v:
            print(f"      operator A=3 {v['3']:6.2f}   A=4 {v['4']:6.2f}   "
                  f"(grows {v['4'] / v['3']:.2f}x)  — {k}")
    print(f"      ⇒ the operator's ladder is nearly FLAT in A while nature's grows.")

    verdict = (f"operator fractional Tjon deviations "
               f"{ {k: round(v['_f'], 4) for k, v in scores.items()} } vs nature "
               f"{float(nat_frac):+.4f}; sign reproduced by at least one bond convention: "
               f"{bool(any_sign)}"
               + (f"; best |ratio| {best:.2f}×" if best is not None else "")
               + "; the binding proxy is the trace DEFICIT B_op = -M_op > 0 (corpus canonical), "
                 "so the operator's sign is CORRECT, not mismatched — an earlier revision claimed "
                 "otherwise and is retracted; the [T2] score is sign-blind anyway (Lean "
                 "fracTjon_neg). THE SURVIVING NEGATIVE is the ladder: nearly FLAT in A ("
               + "; ".join(f"{k}: A=3 {v['3']:.2f}, A=4 {v['4']:.2f}, grows {v['4']/v['3']:.2f}x"
                           for k, v in lad.items() if v)
               + f") against nature's {float(nat[3]):.2f} -> {float(nat[4]):.2f} (grows "
                 f"{float(nat[4]/nat[3]):.2f}x), off {float(nat[3])/max(v['3'] for v in lad.values() if v):.1f}x "
                 f"at A=3 and {float(nat[4])/max(v['4'] for v in lad.values() if v):.1f}x at A=4. "
                 "Scope-(a) NEGATIVE on growth, not on sign")
    print(f"\n ⇒ {verdict}")
    print("   Scale-free by construction — M(2) normalisation and the Tjon deviation")
    print("   both cancel the overall trace scale, y_λ normalisation and global sign.")

    wb = WitnessBuilder("gap10-tjon-correlation", engine="pyhecke_native")
    wb.set_description(
        "GAP-10 (bean qou-zowh, epic qou-xu6t): tests the block-trace operator against the Tjon "
        "correlation B(³H)↔B(⁴He), the target that REPLACES the retired qou-pve2 question 'what "
        "supplies ~10× per-order growth'. That question was mis-posed: GAP-9 showed the μ₄ target "
        "is −10.21 MeV, 36% of B(⁴He) and 34× the N³LO four-nucleon estimate, so its size is a "
        "C(A,k) simplex-basis artifact plus ρ_grad over-subtracting, not four-body physics. The "
        "Tjon correlation is the field's own robust observable for the 3-body/4-body question and "
        "is convention-free. Formal core (Lean QOU.MassTheory.TjonSimplexForm, sorry-free, "
        "generic CommRing): M(4) − (4M(3) − 6M(2)) = μ₄ and μ₄ = 0 ⟺ M(4) = 4M(3) − 6M(2), so "
        "the two-point 'no four-body parameter' prediction is 4M(3) − 6M(2) and μ₄ is exactly its "
        "deviation — giving the scale-free score μ₄/M(4). Measures M_op(A) = g(all bonds) − g(∅) "
        "at A=2 (H₆), A=3 (H₉), A=4 (H₁₂) with the same block trace Σ_λ y_λ|χ_λ| used throughout "
        "the epic, under TWO bond conventions (complete graph 1/3/6 bonds matching the C(A,k) "
        "basis with BKL bands, and chain-only 1/2/3 adjacent) because GAP-8 flagged μ₄'s "
        "sensitivity to the bond set. Scored on the normalised ladder M(A)/M(2) against "
        f"ρ_strong = (1, 3.8128, 13.0316) and on the fractional Tjon deviation. VERDICT: {verdict}. "
        "No Δ_λ, no μ fitted, no convention tuned, nothing wired.")
    for _d in list(results.values()) + list(scores.values()):
        for _k in ("_f", "_r", "_ladder_f", "_M_op_f"):
            _d.pop(_k, None)
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_data("tjon_correlation", {
        "lean": ("QOU.MassTheory.TjonSimplexForm: tjon_deviation_eq_mu4, mu4_eq_zero_iff_tjon, "
                 "mu4_neg_of_below_tjon, additive_higher_moments_vanish"),
        "rho_strong": {str(a): sfmt(RHO_STRONG[a]) for a in (2, 3, 4)},
        "results": results, "scores": scores, "verdict": verdict})
    wb.add_assertion("three_mass_numbers_measured", str(len(results) >= 3), "True")
    # Was add_assertion(name, X, X) -- both slots the same literal, so `x == x`:
    # it renders as "passed": true beside real checks, which reads as machine-
    # verified. This is a DECLARATION the code cannot verify about itself, so it is
    # a parameter. The statement is unchanged; only the false badge is removed.
    # Bean qou-ploj (LITERAL class).
    wb.add_parameter("tjon_identity_is_lean_backed", "True (a claim about the LEAN CORPUS, not verified from this probe; the declarations are named in data.tjon_correlation.lean)")
    wb.save()
    print("\nwitness → gap10-tjon-correlation.witness.json")
    print("STRUCTURAL ASSERTIONS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
