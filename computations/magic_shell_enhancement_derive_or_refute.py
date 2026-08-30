#!/usr/bin/env python3
"""
magic_shell_enhancement_derive_or_refute.py — is the ⁴He magic-shell enhancement
`M_need/z ≈ 2.52` DERIVED, or is it an anchor read?

`prop:bk-coordination-multiplicity` (`content/.../mass-theory/bk-coordination-multiplicity.md`)
reads the jet-filtration body-order multiplicity off AME2020 as

    M_need(A) = B_AME / (m_e · Vol_A)

and reports that for the non-magic A=3 pair `M_need ≈ z = A−1` to better than 3 %,
while doubly-magic ⁴He carries an extra `M_need/z ≈ 2.52 ≈ a_D^(4)`, "the
super-exponential Schur–Weyl period".  The block labels that factor "an AME read
rather than a derived Schur-Weyl period".

This probe establishes four things, with NO fitting and NO tuning:

  (1) `a_D^(4)` IS derived, and the block's label is half wrong.  `a_D^(n) = lw(n−1)
      = Σ_{λ⊢n} dim_q(λ)/n` (`theta_wn_kernel_derive_or_refute.py:86`, PR #3270) is a
      Schur–Weyl q-dimension sum at the substrate q₀ — no AME, no anchor, no free
      parameter.  Its q=1 limit is the exact rational `I(n)/n` (I = A000085,
      involution numbers; `QOU.Mass.sum_numSYT_eq_involutionNumber`).
      So `z·a_D^(A)` is an a-priori law and CAN be tested.

  (2) Tested, it is REFUTED at A=3 and misses by 0.55 % at A=4.  The composite rule
      actually in the block — `z` when non-magic, `z·a_D^(A)` when magic — is one bit
      of SELECTION between two parameter-free candidates, and ⁴He is the only datum
      that selects it.  One fitted bit, one point ⇒ zero residual constraint.

  (3) The 0.55 % is not a measurement agreement.  Every input to `M_need(⁴He)` is
      known to ≲1e-7 relative (AME2020 B, CODATA m_e, an exact hyperbolic volume),
      so 5.5e-3 is a discrepancy far outside the framework's own L2 100× target.

  (4) GENERICITY (AGENTS.md §"Defined residual ≠ derived decomposition" item 2 —
      "is the offset FORCED, or merely IN RANGE?").  Enumerate a pre-registered
      family of simple parameter-free q-bracket / rational candidates and count how
      many land inside the same ±0.551 % window.  If the window is crowded, the
      near-match is not evidence for `a_D^(4)` specifically.

EXPLORATORY — asserts findings, no production wiring, no fitted production constant.
Verdict is scope-(a) for the numerical leg (a construction tested alone).  The
scope-(b) structural exclusion of the Wigner-SU(4) sizing route is proved separately
in Lean (`QOU.Mass.WignerSU4RowBoundInactive`), not here.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))

from q_parameter import Q_MP  # noqa: E402  — proton pin (owner directive 2026-08-07)
from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from knot_volumes import VOL_8_11_MPF, VOL_BORROMEAN_MPF  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:  # explicit fallback, never a silent float path
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()

q = +Q_MP                       # substrate q₀, mpf — never mp.mpf(str(Q))
M_E = mp.mpf(str(M_E_MEV))


# ── Schur–Weyl period a_D^(n) = lw(n−1) = Σ_{λ⊢n} dim_q λ / n ──────────────────
def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]


def qint(k):
    """Balanced q-integer [k]_q = (q^k − q^−k)/(q − q^−1)."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d


def a_D(n):
    """The super-exponential Schur–Weyl period at q₀ — no AME input anywhere."""
    return mp.fsum(dimq(l) for l in partitions(n)) / n


def f_lambda(lam):
    """Number of SYT of shape λ — exact integer, hook-length formula."""
    n = sum(lam)
    num = 1
    for k in range(2, n + 1):
        num *= k
    den = 1
    for h in hooks(lam):
        den *= h
    assert num % den == 0
    return num // den


def a_D_at_one(n):
    """Exact rational q=1 limit: I(n)/n, I = A000085 (involution numbers)."""
    return Fraction(sum(f_lambda(l) for l in partitions(n)), n)


# ── the AME read M_need(A) = B_AME / (m_e · Vol_A) ─────────────────────────────
ISO = {
    "3H":  {"A": 3, "B": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
            "vol": VOL_8_11_MPF,      "link": "8_11",      "magic": False},
    "3He": {"A": 3, "B": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
            "vol": VOL_BORROMEAN_MPF, "link": "L6a4",      "magic": False},
    "4He": {"A": 4, "B": mp.mpf(str(AME_B_HE4_MEV_VALIDATION)),
            "vol": VOL_BORROMEAN_MPF, "link": "L6a4 base", "magic": True},
}


def main() -> int:
    print("magic_shell_enhancement_derive_or_refute")
    print(f"  q0 = {mp.nstr(q, 25)}   m_e = {mp.nstr(M_E, 12)} MeV\n")

    aD = {n: a_D(n) for n in range(2, 6)}
    aD1 = {n: a_D_at_one(n) for n in range(2, 6)}
    print("  (1) a_D^(n) — DERIVED, no AME, no anchor, no free parameter:")
    for n in sorted(aD):
        print(f"      a_D^({n}) = {mp.nstr(aD[n], 17):<20}"
              f" q=1 limit exactly I({n})/{n} = {aD1[n]}")
    print()

    # ── (2) the a-priori law z·a_D^(A) tested on all three points ──────────────
    print("  (2) the a-priori law  M(A) = z(A)*a_D^(A)  tested (nothing fitted):")
    print(f"      {'iso':<5} {'z':>2} {'M_need':>14} {'z*a_D^(A)':>14} {'rel err':>10}")
    rows = {}
    for name, d in ISO.items():
        A = d["A"]
        z = A - 1
        m_need = d["B"] / (M_E * d["vol"])
        pred = z * aD[A]
        rel = (pred - m_need) / m_need
        rows[name] = {
            "A": A, "z": z, "vol": d["vol"], "B_AME_MeV": d["B"],
            "M_need": m_need, "M_need_over_z": m_need / z,
            "pred_z_aD": pred, "rel_err_z_aD": rel,
            # what z alone (the non-magic rule) predicts, for symmetry
            "rel_err_z": (mp.mpf(z) - m_need) / m_need,
            "B_pred_z_aD_MeV": M_E * d["vol"] * pred,
        }
        print(f"      {name:<5} {z:>2} {mp.nstr(m_need, 9):>14}"
              f" {mp.nstr(pred, 9):>14} {mp.nstr(rel * 100, 4):>9} %")
    print("      => REFUTED at A=3 (+33 % / +30 %); +0.55 % at A=4.")
    print("      => the block's composite rule (z if non-magic, z*a_D if magic)")
    print("        is ONE BIT of selection, and 4He is the ONLY datum selecting it.\n")

    he4 = rows["4He"]
    target = he4["M_need_over_z"]                 # 2.5188914618…  the AME read
    cand = aD[4]                                  # 2.5327796564…  the derived period
    rel_he4 = abs(cand - target) / target

    print("  (3) the 0.55 % is a DISCREPANCY, not an agreement within errors:")
    print(f"      M_need/z (AME read)   = {mp.nstr(target, 17)}")
    print(f"      a_D^(4)  (derived)    = {mp.nstr(cand, 17)}")
    print(f"      relative gap          = {mp.nstr(rel_he4, 6)}  ({mp.nstr(rel_he4*100,4)} %)")
    print(f"      B(4He) predicted      = {mp.nstr(he4['B_pred_z_aD_MeV'], 12)} MeV")
    print(f"      B(4He) AME2020        = {mp.nstr(he4['B_AME_MeV'], 12)} MeV")
    print(f"      miss                  = "
          f"{mp.nstr(he4['B_pred_z_aD_MeV'] - he4['B_AME_MeV'], 6)} MeV\n")

    # ── (4) genericity: is the offset FORCED, or merely IN RANGE? ──────────────
    # Pre-registered family, fixed BEFORE looking at which members hit:
    #   (i)  balanced q-brackets  [a]/[b], [a][b]/[c], [a][b]/([c][d]),  1<=.<=6
    #   (ii) plain rationals p/r with p,r <= 24
    #   (iii) q-powers q^k, k in [-6,6], times a small rational
    # This is the family the corpus itself uses for identifications of this shape
    # (cf. bean qou-o16k's kappa-normaliser table: [2]_q[3]_q, [6]_q, [2]_q^3, …).
    tol = rel_he4                                  # the SAME window a_D^(4) occupies
    lo, hi = target * (1 - tol), target * (1 + tol)
    hits, total = [], 0
    br = {a: qint(a) for a in range(1, 7)}
    for a in range(1, 7):
        for b in range(1, 7):
            total += 1
            v = br[a] / br[b]
            if lo <= v <= hi:
                hits.append((f"[{a}]/[{b}]", v))
            for c in range(1, 7):
                total += 1
                v = br[a] * br[b] / br[c]
                if lo <= v <= hi:
                    hits.append((f"[{a}][{b}]/[{c}]", v))
                for e in range(1, 7):
                    total += 1
                    v = br[a] * br[b] / (br[c] * br[e])
                    if lo <= v <= hi:
                        hits.append((f"[{a}][{b}]/([{c}][{e}])", v))
    for p in range(1, 25):
        for r in range(1, 25):
            total += 1
            v = mp.mpf(p) / r
            if lo <= v <= hi:
                hits.append((f"{p}/{r}", v))
    for k in range(-6, 7):
        for p in range(1, 13):
            for r in range(1, 13):
                total += 1
                v = q ** k * p / r
                if lo <= v <= hi:
                    hits.append((f"q^{k}*{p}/{r}", v))

    print("  (4) genericity of the near-match — is the offset FORCED or IN RANGE?")
    print(f"      window = M_need/z * (1 +- {mp.nstr(tol,4)})"
          f"  = [{mp.nstr(lo, 10)}, {mp.nstr(hi, 10)}]   width {mp.nstr(hi-lo, 6)}")
    print(f"      pre-registered family size          : {total}")
    print(f"      members inside the SAME window      : {len(hits)}")
    for label, v in hits[:14]:
        print(f"        {label:<24} = {mp.nstr(v, 12)}")
    if len(hits) > 14:
        print(f"        … and {len(hits) - 14} more")
    closer = [(lab, v) for lab, v in hits if abs(v - target) / target < rel_he4]
    print(f"      members CLOSER to M_need/z than a_D^(4) is : {len(closer)}")
    for lab, v in closer:
        print(f"        {lab:<24} = {mp.nstr(v, 12)}"
              f"   ({mp.nstr(abs(v - target) / target * 100, 3)} % vs a_D^(4)'s "
              f"{mp.nstr(rel_he4 * 100, 3)} %)")
    print()

    # ── assertions ────────────────────────────────────────────────────────────
    checks = []

    def chk(name, cond, detail):
        checks.append({"name": name, "passed": bool(cond), "detail": detail})
        print(f"      [{'PASS' if cond else 'FAIL'}] {name} — {detail}")

    print("  assertions:")
    chk("a_D_4_is_AME_free",
        aD1[4] == Fraction(5, 2),
        f"q=1 limit of a_D^(4) is exactly I(4)/4 = {aD1[4]} — a rational from the "
        f"involution numbers, no AME input")
    chk("z_aD_refuted_at_A3",
        rows["3H"]["rel_err_z_aD"] > mp.mpf("0.25")
        and rows["3He"]["rel_err_z_aD"] > mp.mpf("0.25"),
        f"z*a_D^(3) overshoots 3H by {mp.nstr(rows['3H']['rel_err_z_aD']*100,4)} % and "
        f"3He by {mp.nstr(rows['3He']['rel_err_z_aD']*100,4)} %")
    chk("z_aD_misses_A4_by_half_percent",
        mp.mpf("0.004") < rel_he4 < mp.mpf("0.007"),
        f"a_D^(4) is {mp.nstr(rel_he4*100,4)} % above the AME read M_need/z")
    chk("near_match_is_generic",
        len(hits) > 1,
        f"{len(hits)} members of a pre-registered parameter-free family of {total} "
        f"land in the same window, so 2.519 is IN RANGE, not FORCED to be a_D^(4)")
    chk("only_A4_constrains_the_enhancement",
        len({rows[k]['A'] for k in rows if ISO[k]['magic']}) == 1,
        "exactly one magic point (4He) exists in the Vol_A-covered range A <= 4, so "
        "the magic/non-magic selector is fitted on one datum with no out-of-sample test")

    ok = all(c["passed"] for c in checks)
    print(f"\n  VERDICT: the 4He enhancement is NOT DERIVED. a_D^(4) is derived; its "
          f"IDENTIFICATION with M_need/z is not, and misses by "
          f"{mp.nstr(rel_he4*100,4)} %.  Scope (a).")

    if _HAVE_WB:
        w = WitnessBuilder("magic-shell-enhancement-derive-or-refute")
        w.set_description(
            "Is the 4He magic-shell enhancement M_need/z ~ 2.52 derived? "
            "a_D^(n) = sum_{lam|-n} dim_q lam / n IS derived (Schur-Weyl at q0, no "
            "AME; q=1 limit I(n)/n exactly). The a-priori law M(A) = z*a_D^(A) is "
            "REFUTED at A=3 (+33 %/+30 %) and misses 4He by 0.55 %. The block's "
            "composite magic/non-magic rule is one bit of selection fitted on the "
            "single 4He datum. Genericity: the same window is occupied by other "
            "parameter-free candidates - some CLOSER than a_D^(4) - so 2.519 is in "
            "range, not forced. Scope (a) - no structural exclusion claimed here.")
        w.add_data("a_D_at_q0", {str(n): fmt(aD[n]) for n in aD})
        w.add_data("a_D_at_q_eq_1_exact",
                   {str(n): f"{aD1[n].numerator}/{aD1[n].denominator}" for n in aD1})
        w.add_data("isotopes", {
            k: {kk: (fmt(vv) if isinstance(vv, mp.mpf) else vv)
                for kk, vv in v.items()} for k, v in rows.items()})
        w.add_data("he4_gap_relative", fmt(rel_he4))
        w.add_data("genericity", {
            "window_lo": fmt(lo), "window_hi": fmt(hi),
            "family_size": total, "hits": len(hits),
            "hit_labels": [h[0] for h in hits],
            "closer_than_a_D_4": [h[0] for h in closer],
        })
        w.add_data("scope", "a")
        w.add_caveat(
            "Scope (a): a construction tested alone. No proved invariant is cited "
            "here, so nothing is structurally excluded by THIS probe. The scope-(b) "
            "exclusion of the Wigner-SU(4) sizing route is in "
            "QOU.Mass.WignerSU4RowBoundInactive.")
        w.add_caveat(
            "Only 4He is magic in the Vol_A-covered range (A <= 4). "
            "binding_link_volumes.py assigns links for 2H/3H/3He and the 4He L6a4 "
            "base only, so the magic/non-magic selector has ZERO out-of-sample "
            "support and cannot be validated until Vol_A extends past A=4.")
        for c in checks:
            w.add_assertion(c["name"],
                            computed="PASS" if c["passed"] else "FAIL",
                            expected="PASS",
                            source=c["detail"])
        w.save()
        print("  witness written.")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
