#!/usr/bin/env python3
"""c1_is_stale_on_the_reordered_atom_word_probe.py — qou-pdg9's six c₁ are the OLD word. (qou-pdg9)

THE FINDING. Bean `qou-pdg9` is **completed**. It derived `c₁`, the ℏ_q¹ coefficient of
`tr_M(W_free) − tr_M(W_atom)`, two independent ways, recorded six exact dyadic rationals

    pp 19/8    pn 37/16    nn 9/4    T 163/64    ³He 85/32    ⁴He 259/128

and carried them into `QOU/MassTheory/PairwiseChainLeadingOrder.lean` as `def`s plus a closed form
`c₁(Z,N) = (21Z + 16N)·(2^(−A−1) − 2^(−2A)) − 4·(I_pp − I_nn)·2^(−2A)`. It completed **2026-09-03**.

**The atom word changed on 2026-09-05.** Owner ruling `qou-hu1f`: each nucleon's confinement core
moved from grouped `σ₀³σ₁⁻³` to the alternating `(σ₀σ₁⁻¹)³` its own source comment always named,
because `σ₀` and `σ₁` do not commute and only the alternating word is `β_Bor`. That reordering moved
absolute traces by `3.785×` (²H) to `14.325×` (⁴He). `atom_braid_word_3A(intra_order=...)` now
defaults to `"borromean"`; `"grouped"` reproduces the pre-ruling word.

Measured here: **all six recorded values are the `grouped` word's.** Under the canonical `borromean`
ordering `c₁` is

    pp 1/8     pn 1/16     nn 0      T 1/64      ³He 1/8      ⁴He 7/128

— different in every case, and `37/16 → 1/16` is a factor of **37**.

WHY NOTHING FLAGGED IT, and this is the part worth internalising. The sibling result in the same
arc **did** survive: `c₀(A) = 2^(−A) − 2^(1−2A)` is a pure cycle count, and cycle counts are blind
to letter order — measured invariant under `intra_order` and under `pn_convention`
(`classical_floor_is_interface_parity_probe.py`). So the floor, the Lean `ClassicalTraceFloor`, and
every downstream statement about the ℏ_q⁰ term are untouched by the reordering. `c₁` is the *first*
order that can see letter order at all, and it sits one bean over, already marked completed.
**A reordering that provably cannot move the leading term is not evidence about the next one.**

HOW THE CLAIM IS ESTABLISHED — two independent routes, neither trusting the other.

  1. **`[★]`, `qou-pdg9`'s own Part-B formula**, reimplemented here:

         d tr_M/dε|₀ = 2^(−n) · Σ_ℓ w_ℓ · 2^(c(word with letter ℓ deleted))

     with `w_ℓ = 1 + d′_ℓ(0) ∈ {+1, −1, 0, 0}` for `σ` / `σ⁻¹` / averaged / colour-weighted. Its
     **self-test is that it reproduces all six recorded rationals exactly under `grouped`** — six
     independent dyadic values, which a wrong implementation does not hit by accident. Run on the
     canonical word it returns the second row above.

  2. **The live trace machinery**, `tr_m_atom_via_transfer.tr_m_atom_zn`, swept along `q = exp(η)`
     with no reference to `[★]` at all. For the deuteron `(Δtr − c₀)/ℏ_q` runs

         η = 1e-3 → 0.063287    1e-4 → 0.0625782    1e-5 → 0.0625078    1e-6 → 0.06250078

     converging on `1/16 = 0.0625` with `O(η)` error, not on `37/16 = 2.3125`.

WHAT ELSE IS STALE BY THE SAME CAUSE. `qou-zrx2` quotes the ℏ_q⁰ floor as **22.46 %** of the
deuteron trace difference and **4.88 %** of ⁴He's, computed from `Δtr(D) = 0.556544660404` — a
`grouped` value (`binding_canonical`'s difference route moved by the same `3.785×`). Those
percentages are recomputed below on the canonical word. The floor itself does not move; the fraction
does, because its denominator did.

WHAT THIS DOES NOT CLAIM. Not that the derivation in `qou-pdg9` is wrong — the method is sound and
this probe is built on it. The *inputs* changed under it. And nothing here proposes a new closed
form in `A`: the six canonical values are recorded exactly and left as data. Finding the closed form
is the reopened bean's work, not this probe's, and guessing one from six points is how this arc has
been burned before.

SCOPE — (a) scope-limited. Exact `Fraction`/integer arithmetic for `[★]`; the cross-check is `mpf`
at 60 dps end to end (`mp.exp(η)` is a genuine 60-dps value, so `reject_float64_q` is satisfied
rather than bypassed). No witness, nothing wired, no Lean touched.
"""
from __future__ import annotations

import argparse
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "substrate"))

import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

# The six values `qou-pdg9` recorded and carried into PairwiseChainLeadingOrder.lean as defs.
RECORDED = {"pp": Fraction(19, 8), "pn": Fraction(37, 16), "nn": Fraction(9, 4),
            "T": Fraction(163, 64), "³He": Fraction(85, 32), "⁴He": Fraction(259, 128)}
CASES = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2), "T": (1, 2), "³He": (2, 1), "⁴He": (2, 2)}
# c₀(A) = 2^(−A) − 2^(1−2A), derived in ClassicalTraceFloor.lean and INVARIANT under intra_order.
C0 = {"pp": Fraction(1, 8), "pn": Fraction(1, 8), "nn": Fraction(1, 8),
      "T": Fraction(3, 32), "³He": Fraction(3, 32), "⁴He": Fraction(7, 128)}


def cycles(p):
    n = len(p)
    seen = [False] * n
    c = 0
    for i in range(n):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c


def perm_of(gens, n):
    p = list(range(n))
    for g in gens:
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


def star(Z, N, *, include_inter, intra_order):
    """`[★]` — d tr_M/dε|₀ = 2^(−n)·Σ_ℓ w_ℓ·2^(c(word minus ℓ)).

    `w_ℓ = 1 + d′_ℓ(0)`. With `h = q − 1/q` and `h′(1) = 2`, the four letter classes give:
    `σ` (`d = 0`) → `+1`; `σ⁻¹` (`d = −h`) → `1 − 2 = −1`; averaged (`d = −h/2`) → `1 − 1 = 0`;
    colour-weighted (`d = −h(1/2 − δ/4)`) → `0` as well, since `δ = O(ε³)` is invisible at this
    order. Zero-weight letters contribute nothing, so their (expensive) deletion cycle count is
    skipped.

    Classification is by exact comparison against the word's own templates rather than by a
    tolerance: `d = 0` and `d = −h` are the two extremes of the four values present, and every
    letter is built from the same `h` inside one `workdps` block, so equality is exact.
    """
    n = 3 * (Z + N)
    word = atom_braid_word_3A(Z, N, include_inter=include_inter, intra_order=intra_order)
    ds = [mp.mpf(t[1]) for t in word]
    h_neg = min(ds)                      # −h, the σ⁻¹ template
    gens = [int(t[2]) for t in word]
    total = Fraction(0)
    for i, d in enumerate(ds):
        if d == 0:
            w = 1
        elif d == h_neg:
            w = -1
        else:
            continue                     # both averaged forms carry weight 0
        total += w * Fraction(2) ** cycles(perm_of(gens[:i] + gens[i + 1:], n))
    return total * Fraction(1, 2) ** n


def c1(Z, N, intra_order):
    return (star(Z, N, include_inter=False, intra_order=intra_order)
            - star(Z, N, include_inter=True, intra_order=intra_order))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-live", action="store_true",
                    help="skip the tr_m_atom_zn cross-check (it is the slow half)")
    ap.add_argument("--with-he4", action="store_true",
                    help="include ⁴He in the floor-share table (slow: H_12 trace)")
    ap.add_argument("--dps", type=int, default=60)
    args = ap.parse_args()
    mp.mp.dps = args.dps

    print("[c1-stale] qou-pdg9's six c₁ values are the PRE-2026-09-05 (grouped) atom word.")
    print("[c1-stale] The owner ruling qou-hu1f reordered each nucleon's core on 2026-09-05.\n")

    # ── SELF-TEST FIRST. Without this the borromean column below is an unvalidated number, and an
    # unvalidated number disagreeing with a committed one is not a finding about the committed one.
    print("  SELF-TEST — does [★] reproduce the six RECORDED values on the word they were computed")
    print("  on (intra_order='grouped', the pre-ruling ordering)?")
    print(f"    {'case':<6}{'[★] grouped':>14}{'recorded':>14}  verdict")
    ok_self = True
    grouped = {}
    for nm, (Z, N) in CASES.items():
        v = c1(Z, N, "grouped")
        grouped[nm] = v
        good = (v == RECORDED[nm])
        ok_self = ok_self and good
        print(f"    {nm:<6}{str(v):>14}{str(RECORDED[nm]):>14}  {'ok' if good else 'FAIL'}")
    if not ok_self:
        print("    ⇒ [★] does NOT reproduce the recorded values. This probe's implementation is")
        print("      wrong, or the recorded values were computed some third way. EITHER WAY, do")
        print("      not read the canonical column below as a finding about qou-pdg9.")
        return 1
    print("    ⇒ 6/6 exact. [★] is validated on six independent dyadic rationals, so the")
    print("      canonical-word column below is a statement about the WORD, not about this code.\n")

    # ── THE FINDING ─────────────────────────────────────────────────────────────────────────────
    print("  CANONICAL WORD — intra_order='borromean' (the default since qou-hu1f)")
    print(f"    {'case':<6}{'c₁ canonical':>14}{'c₁ recorded':>14}{'ratio rec/canon':>18}  moved?")
    moved = 0
    canonical = {}
    for nm, (Z, N) in CASES.items():
        v = c1(Z, N, "borromean")
        canonical[nm] = v
        r = (RECORDED[nm] / v) if v != 0 else None
        moved += (v != RECORDED[nm])
        print(f"    {nm:<6}{str(v):>14}{str(RECORDED[nm]):>14}"
              f"{(str(r) if r is not None else '∞ (canon = 0)'):>18}"
              f"  {'MOVED' if v != RECORDED[nm] else 'same'}")
    print(f"    ⇒ {moved} of {len(CASES)} moved.")
    print("      The canonical values are recorded as DATA. No closed form in A is proposed here —")
    print("      six points do not fix one, and that guess is how this arc has been burned before.\n")

    # ── WHY NOTHING CAUGHT IT ───────────────────────────────────────────────────────────────────
    # c₀ is a cycle count and cycle counts cannot see letter order; c₁ is the first order that can.
    print("  WHY NOTHING FLAGGED IT — c₀ is invariant, so the sibling result survived")
    print(f"    {'case':<6}{'c₀ grouped':>12}{'c₀ borromean':>14}{'c₀ derived':>12}  same?")
    ok_c0 = True
    for nm, (Z, N) in CASES.items():
        A = Z + N
        n = 3 * A
        cg, cb = [], []
        for order, out in (("grouped", cg), ("borromean", cb)):
            cf = cycles(perm_of([int(t[2]) for t in atom_braid_word_3A(
                Z, N, include_inter=False, intra_order=order)], n))
            ca = cycles(perm_of([int(t[2]) for t in atom_braid_word_3A(
                Z, N, include_inter=True, intra_order=order)], n))
            out.append(Fraction(1, 2) ** (n - cf) - Fraction(1, 2) ** (n - ca))
        good = (cg[0] == cb[0] == C0[nm])
        ok_c0 = ok_c0 and good
        print(f"    {nm:<6}{str(cg[0]):>12}{str(cb[0]):>14}{str(C0[nm]):>12}"
              f"  {'YES' if good else 'NO'}")
    print(f"    ⇒ {'c₀ is unmoved by the reordering, exactly as a cycle count must be.' if ok_c0 else 'c₀ MOVED — that would contradict the cycle-count derivation; investigate.'}")
    print("      So ClassicalTraceFloor.lean, the floor closed form and every ℏ_q⁰ statement stand.")
    print("      A reordering that provably cannot move the leading term is not evidence about")
    print("      the next one — which is the whole reason this went unnoticed.\n")

    ok_live = True
    if args.skip_live:
        print("  LIVE CROSS-CHECK — skipped (--skip-live).")
    else:
        # Independent of [★] entirely: the production trace machinery on the production word.
        # q = exp(η) is a genuine 60-dps value, so reject_float64_q is satisfied, not bypassed.
        import tr_m_atom_via_transfer as TR    # noqa: E402  (slow import; only needed here)
        from q_parameter import Q_50_DIGIT_STR as _Q50    # noqa: E402
        print("  LIVE CROSS-CHECK — tr_m_atom_via_transfer.tr_m_atom_zn on the canonical word,")
        print("  with no reference to [★]. Deuteron: (Δtr − c₀)/ℏ_q along q = exp(η).")
        c0d = mp.mpf(C0["pn"].numerator) / C0["pn"].denominator
        print(f"    {'η':<8}{'Δtr':>20}{'(Δtr−c₀)/ℏ_q':>20}")
        last = None
        for e in ("1e-3", "1e-4", "1e-5", "1e-6"):
            eta = mp.mpf(e)
            q = mp.exp(eta)
            ta, tf, _chi, _w = TR.tr_m_atom_zn(1, 1, dps=args.dps, q=q)
            d = abs(tf) - abs(ta)
            last = (d - c0d) / ((q - 1) / q)
            print(f"    {e:<8}{mp.nstr(d, 14):>20}{mp.nstr(last, 12):>20}")
        want = mp.mpf(canonical["pn"].numerator) / canonical["pn"].denominator
        bad = mp.mpf(RECORDED["pn"].numerator) / RECORDED["pn"].denominator
        # 1e-4 is the Richardson error at η = 1e-6; the two candidates differ by 37×, so this
        # tolerance is nowhere near tight enough to be doing any of the discriminating.
        ok_live = abs(last - want) < mp.mpf("1e-4")
        print(f"    → {mp.nstr(last, 12)} vs [★] {canonical['pn']} = {mp.nstr(want, 10)}"
              f"  ({'agrees' if ok_live else 'DISAGREES'})")
        print(f"      and vs recorded {RECORDED['pn']} = {mp.nstr(bad, 10)}: off by"
              f" {mp.nstr(bad / want, 5)}×")

        # ── THE FLOOR SHARE, RECOMPUTED. This is the number that actually matters downstream:
        # qou-zrx2's whole complaint is sized by it, and it was sized on the superseded word.
        print("\n  FLOOR SHARE at the canonical q₀, recomputed on the canonical word")
        print(f"    {'atom':<6}{'Δtr':>20}{'c₀':>10}{'floor share':>14}{'qou-zrx2 said':>16}")
        shares = (("D", 1, 1, C0["pn"], "22.46 %"),)
        if args.with_he4:
            shares = shares + (("⁴He", 2, 2, C0["⁴He"], "4.88 %"),)
        for nm, Z, N, c0f, said in shares:
            ta, tf, _chi, _w = TR.tr_m_atom_zn(Z, N, dps=args.dps,
                                               q=mp.mpf(str(_Q50)))
            d = abs(tf) - abs(ta)
            f0 = mp.mpf(c0f.numerator) / c0f.denominator
            print(f"    {nm:<6}{mp.nstr(d, 14):>20}{str(c0f):>10}"
                  f"{mp.nstr(100 * f0 / d, 6) + ' %':>14}{said:>16}")
        print("    The floor did not move; Δtr did. On the canonical word the deuteron binding")
        print("    observable is ~85 % a q-INDEPENDENT topological term, not ~22 %. That does not")
        print("    weaken qou-zrx2's complaint — it is the same complaint, four times larger.")
        print("    (⁴He is slow; pass --with-he4 to include it.)")

    # ── DOWNSTREAM ──────────────────────────────────────────────────────────────────────────────
    print("\n  DOWNSTREAM — what else is stale by the same cause")
    print("    • QOU/MassTheory/PairwiseChainLeadingOrder.lean — six c₁ defs")
    print("    • QOU/MassTheory/LeadingOrderTraceCoefficient.lean — the Part-B derivation")
    print("    • the closed form c₁(Z,N) = (21Z+16N)·(2^(−A−1) − 2^(−2A)) − 4(I_pp − I_nn)·2^(−2A)")
    print("    • qou-zrx2's floor SHARES (22.46 % D, 4.88 % ⁴He): computed from the grouped")
    print("      Δtr(D) = 0.556544660404. The floor does not move; its denominator did.")
    print("    NOT stale: c₀, ClassicalTraceFloor.lean, and the ℏ_q⁰ conclusions.")

    ok = ok_self and ok_c0 and ok_live and (moved == len(CASES))
    # Say which evidence actually ran. With --skip-live the finding rests on [★] alone, and [★] is
    # this probe's own code — validated 6/6, but still one route. Reporting that as the same
    # verdict as the two-route run would overstate it by exactly the independence that matters.
    routes = "[★] only (live cross-check SKIPPED)" if args.skip_live else "[★] and the live sweep"
    print(f"\n  {'checks pass on ' + routes + ' — qou-pdg9 needs reopening.' if ok else 'SOME CHECKS FAILED — do not quote this probe.'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
