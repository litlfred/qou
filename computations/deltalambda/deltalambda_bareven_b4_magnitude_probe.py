#!/usr/bin/env python3
"""Vector-3 forward test: does BAR-EVEN symmetrization of the b_A cumulant crack
the isospin-EVEN STRONG binding magnitude?  (Honest-negative probe, no fit.)

CONTEXT (read first, in order):
  * docs/audits/2026-07-18-deltalambda-attack-vector-map.md  (Vector 3, §4 row 3)
  * b4_slater_antisymmetrizer_exchange_sign.py (#3924) -- the det(I+mG) machinery:
        WRITHE K_A exchange S (pp=+1,nn=-1,pn=+1), spectrum {+-sqrt5,+-1} at A=4,
        det(I+mS)=(1-5m^2)(1-m^2), ceiling m<1/sqrt5, cumulant b_A=-ln det(I+mS).
  * QOU/MassTheory/IsospinMirrorInvariance.lean (#3986) -- the ISOSPIN-product
        exchange (off-diag mag*s_i*s_j) is p<->n mirror invariant => strong 3H/3He
        split EXACTLY 0.  det=(1+(A-1)m)(1-m)^(A-1), a function of A only (strong).
  * docs/audits/2026-07-18-deltalambda-coulomb-mirror-split.md (#3990, PARTIAL) --
        the 3H/3He split is pure-EM Coulomb; used here to ISOSPIN-CORRECT rho targets.
  * docs/audits/2026-06-25-he4-magic-factor-bar-even-pruning.md -- prior scope-(b):
        4He is self-mirror (N=Z=2) => its binding must be BAR-EVEN.  That audit PRUNED
        bar-odd candidates; it did NOT apply bar-even to the b_A cumulant.  This probe
        does (the new synthesis) -- and finds the construction is ALREADY bar-even.
  * rem-ohtsuki-tower-bar-parity.md + OhtsukiTowerBarParity.lean -- the c3 precedent:
        bar involution q->q^{-1} splits an object into bar-even (mass) / bar-odd (decay).

HYPOTHESIS (Vector 3).  The cumulant b_A = -ln det(I+m G_A) mixes bar-even (mass)
and bar-odd (decay) parts when G carries the q-deformation.  Symmetrize under the
bar involution q->q^{-1} BEFORE evaluating -- b_A^{even} = 1/2(b_A(q)+b_A(q^{-1}))
-- isolating the bar-even (mass/binding) part.  Test whether the bar-even cumulant
ratio b_A^{even}/b_2^{even} reproduces the isospin-corrected strong rho ratios
{~3.81, ~13.03} at a SINGLE parameter-free m (or q0), simultaneously for A=3, A=4.

STRICT anti-fit: m/q0 is fixed parameter-free (g_reeb / z_naive) BEFORE comparison;
NEVER solved from the rho ratios.  We ALSO run a coherence scan over a hypothetical
FREE m purely to show the hypothesis fails independent of the pin -- that scan is a
falsification test, not a fit (nothing from it is promoted or wired).

FINDING (honest negative, scope-(a) with a scope-(b) sub-result):
  1. The corpus's DERIVED parameter-free bond magnitude g_reeb = 1/sqrt(5+(q0-1)^2/q0)
     and the naive z = 1/[2]_v are BOTH BAR-EVEN (m(q^{-1}) = m(q)).  Hence
     b_A(q) = b_A(q^{-1}) IDENTICALLY for every A, so bar-even symmetrization is a
     STRUCTURAL NO-OP on the actual construction.  There is no bar-odd part to remove;
     the overshoot (#3952: 4He 2.6-10.6x) is a genuine bar-EVEN magnitude problem, not
     a bar-parity contamination.  This is consistent with (not a re-derivation of) the
     2026-06-25 scope-(b) pruning: binding lives entirely in the bar-even sector.
  2. STEELMAN (grant a hypothetical FREE bar-odd m, m(q^{-1}) = -m(q)).  Even then:
     - A=4 WRITHE det (1-5m^2)(1-m^2) is a function of m^2 (symmetric spectrum) => b_4
       is bar-even ANYWAY => symmetrization is STILL a no-op at the DOMINANT A=4 wall
       (Lean scope-(b): B4CumulantBarEven.lean, det(I+mS)=det(I-mS)).
     - No single m in the physical window lands BOTH strong targets:
         * WRITHE rho4=13.03 forces m=0.42687, where rho3=2.4661 (-35.3%).
         * WRITHE rho3=3.81 has NO root: rho3_writhe decreases monotonically from
           2.907 (m=0.05) to 2.450 (at the m<1/sqrt5 ceiling) and never reaches
           3.813, so there is no m to force rho4 from.
         * ISO raw rho4 is range-capped in (~3.05, ~6.03) and cannot reach 13 at all.
         * ISO bar-even rho4 DOES reach 13.03, at m=0.31900, with det_iso(A,-m) > 0
           for A=2,3,4 -- i.e. still physical.  It is excluded not on physicality
           but because rho3_even there is 3.4350 vs the 3.8128 target (-9.9%).
       (Numbers corrected 2026-08-30 while draining the tautological
        `single_m_lands_both_targets` assertion, bean qou-26f2: the previous
        text's 6.02/+58%, 6.79/-48% and "det<0 before 13.03" did not match this
        script's own output, and the branch that was supposed to produce 6.79
        never executed.  The scope-(a) negative itself is unchanged.)
  => BAR-EVEN SYMMETRIZATION DOES NOT CRACK THE STRONG MAGNITUDE.  Nothing wired, no fit.

EXPLORATORY -- audit + witness only; no production wiring, no fit, no AME inversion.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)
mp.mp.dps = 60

# muon-canonical q0 (the computations/ layer convention; AGENTS.md q0-convention)
# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was the literal
# "1.10997859555733471" -- the RETIRED self-certified muon pin A, superseded
# 2026-08-22 (fca08de7d2) by the live CODATA-2022 lepton-ratio derivation.
# A frozen literal cannot follow the anchor when it moves, and this producer
# was UNSTAMPED, so the anchor audit filed it Q0_ANCHOR_MISSING rather than
# Q0_FLIP -- invisible to the corpus-wide drain, which keys on stamps.
# It resolves the PROTON pin per the owner directive of 2026-08-15, sharpened
# 2026-08-30: proton unless the producer is (E1) an explicit mu-vs-p
# comparison or (E2) the ideal CAL-1/2/3 mathematical layer. This is neither
# -- it is a sole-anchor probe that happened to be muon-named.
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0_STR = _Q0_RESOLVED

# ---------------------------------------------------------------------------
# Exchange matrices and cumulants
# ---------------------------------------------------------------------------
# WRITHE matrix (#3924): diag 1, off-diag sgn(type_i,type_j)*m with pp=+1,nn=-1,pn=+1.
_WSGN = {("p", "p"): 1, ("n", "n"): -1, ("p", "n"): 1, ("n", "p"): 1}
# A -> nucleon type word (Z protons first).  A=2 deuteron pn; A=3 He3 ppn; A=4 He4 ppnn.
_WORD = {2: ["p", "n"], 3: ["p", "p", "n"], 4: ["p", "p", "n", "n"]}


def det_writhe(word, m):
    n = len(word)
    M = mp.eye(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i, j] = _WSGN[(word[i], word[j])] * m
    return mp.det(M)


def det_writhe_closed(A, m):
    """Closed form for the standard A words: A=2 -> 1-m^2 ; A=3 -> 1-3m^2+2m^3 ;
    A=4 -> (1-5m^2)(1-m^2).  Used only for the algebraic preflight vs mp.det."""
    if A == 2:
        return 1 - m ** 2
    if A == 3:
        return 1 - 3 * m ** 2 + 2 * m ** 3
    if A == 4:
        return (1 - 5 * m ** 2) * (1 - m ** 2)
    raise ValueError(A)


def det_iso(A, m):
    """ISOSPIN-product exchange (#3986): off-diag m*s_i*s_j, s=+-1 => M=(1-m)I+m ss^T,
    det = (1+(A-1)m)(1-m)^(A-1).  A-only (strong, isospin-blind)."""
    return (1 + (A - 1) * m) * (1 - m) ** (A - 1)


def b_writhe(A, m):
    return -mp.log(det_writhe(_WORD[A], m))


def b_iso(A, m):
    return -mp.log(det_iso(A, m))


def bar_even(bfun, A, m):
    """Bar-even symmetrization for a hypothetical bar-ODD magnitude (q->q^{-1} sends
    m->-m): 1/2(b(A,m)+b(A,-m)).  Returned as mpc if det<0 in either branch."""
    return (bfun(A, m) + bfun(A, -m)) / 2


# ---------------------------------------------------------------------------
def main() -> int:
    q0 = mp.mpf(Q0_STR)
    v = mp.sqrt(q0)
    # CONVENTION C, DELIBERATE AND BLOCKED -- do not substitute z_D here.
    # z_naive (below) and its bar image z_bar are convention C, z = sqrt(q)/(q+1).
    # This probe's SUBJECT is bar-evenness, and only z_C has it: measured
    # symbolically, bar(z_C) - z_C = 0, while bar(z_D) = 1/(q^3+q) and
    # bar(z_D) - z_D = 1/q - q = -h, so z_D is bar-NEITHER. Swapping in z_D
    # therefore flips this file's own assertion rather than re-coordinatising
    # it. Registered in docs/coordination/trace-convention-registry.json under
    # blocked_on_rederivation (both z_naive and z_bar), blocked on bean
    # qou-pmkh: what replaces this under D is a D-frame bar decomposition
    # built on bar(z_D) = z_D - h, which is real work, not a swap.
    z_naive = 1 / (v + 1 / v)                       # 1/[2]_v
    g_reeb = 1 / mp.sqrt(5 + (q0 - 1) ** 2 / q0)    # derived reeb magnitude
    ceiling = 1 / mp.sqrt(mp.mpf(5))

    # ---- 0. bar-parity of the parameter-free magnitudes ----------------------
    g_bar = 1 / mp.sqrt(5 + (1 / q0 - 1) ** 2 * q0)
    # MANIFEST, not measured (labelled 2026-08-30, qou-t9r1). z(v) = 1/(v + 1/v)
    # is symmetric under the bar v -> 1/v BY INSPECTION -- this line differs from
    # z_naive only by commuting the addition, so `z_bar_even` below is exactly 0
    # and CANNOT FAIL. No formulation of it can: the symmetry is syntactic.
    # Kept because the claim is TRUE and worth recording, but it is not evidence
    # in the way `g_bar_even` is -- that one compares (q-1)**2/q against
    # (1/q-1)**2*q, a genuine algebraic identity that a sign slip would break.
    # Read the two assertions differently when citing this witness.
    z_bar = 1 / (1 / v + v)
    g_bar_even = abs(g_reeb - g_bar) < mp.mpf(10) ** -40
    z_bar_even = abs(z_naive - z_bar) < mp.mpf(10) ** -40

    # ---- 1. algebraic preflight: mp.det vs closed form -----------------------
    preflight = all(
        abs(det_writhe(_WORD[A], m) - det_writhe_closed(A, m)) < mp.mpf(10) ** -45
        for A in (2, 3, 4)
        for m in (mp.mpf("0.31"), g_reeb)
    )
    # A=4 writhe det is even in m (symmetric spectrum {+-sqrt5,+-1}); A=3 iso is not.
    a4_writhe_even = abs(det_writhe(_WORD[4], g_reeb) - det_writhe(_WORD[4], -g_reeb)) < mp.mpf(10) ** -40
    a4_iso_even = abs(det_iso(4, g_reeb) - det_iso(4, -g_reeb)) < mp.mpf(10) ** -40  # False

    # ---- 2. isospin-corrected STRONG rho targets (from #3990 E_C) -------------
    # AME2020 binding energies (MeV) and the deuteron reference.
    BD = mp.mpf("2.224566")
    B3H = mp.mpf("8.481821")
    B3He = mp.mpf("7.718058")
    B4 = mp.mpf("28.295673")
    rho3H, rho3He, rho4 = B3H / BD, B3He / BD, B4 / BD
    # Lean #3986: strong 3H/3He split = 0 exactly => the entire 3H-3He difference is EM.
    # 3H (Z=1) has NO proton pair => E_C(3H)=0 => strong(A=3) = B(3H) exactly.
    EC3He = B3H - B3He                                   # = the AME split, all Coulomb
    # 4He (Z=2) has one pp pair; same coef & Z(Z-1)=2, radius ~ A^{1/3} (#3990):
    EC4 = EC3He * (mp.mpf(3) / 4) ** (mp.mpf(1) / 3)
    rho_strong_3 = B3H / BD                              # = rho3He + EC3He/BD (consistent)
    rho_strong_4 = (B4 + EC4) / BD                       # add pp-Coulomb back to strong
    naive_avg_3 = (rho3H + rho3He) / 2                   # the task-hint 3.6 (PHYS-INCORRECT)

    T3, T4 = rho_strong_3, rho_strong_4

    # ---- 3. forward test at PARAMETER-FREE magnitudes (no fit) ----------------
    def rho_row(bfun, A_den, m, use_bar_even=False):
        fn = (lambda A, mm: bar_even(bfun, A, mm)) if use_bar_even else bfun
        b2, b3, b4 = fn(A_den, m), fn(3, m), fn(4, m)
        return b2, b3, b4

    forward = {}
    for name, m in (("g_reeb", g_reeb), ("z_naive", z_naive)):
        entry = {"m": mp.nstr(m, 18), "below_ceiling": bool(m < ceiling)}
        # WRITHE requires m<ceiling for A=4 physicality
        if m < ceiling:
            b2, b3, b4 = rho_row(b_writhe, 2, m)
            entry["writhe"] = {
                "rho3": mp.nstr(b3 / b2, 6), "rho4": mp.nstr(b4 / b2, 6),
                "rho3_err_pct": mp.nstr((b3 / b2 / T3 - 1) * 100, 4),
                "rho4_err_pct": mp.nstr((b4 / b2 / T4 - 1) * 100, 4),
                # bar-even is identical (m bar-even => b(q)=b(q^-1)):
                "bar_even_is_noop": True,
            }
        else:
            entry["writhe"] = {"excluded": "m >= 1/sqrt5 => det(I+mS)<0 (unphysical) at A=4"}
        b2i, b3i, b4i = rho_row(b_iso, 2, m)
        entry["iso"] = {
            "rho3": mp.nstr(b3i / b2i, 6), "rho4": mp.nstr(b4i / b2i, 6),
            "rho3_err_pct": mp.nstr((b3i / b2i / T3 - 1) * 100, 4),
            "rho4_err_pct": mp.nstr((b4i / b2i / T4 - 1) * 100, 4),
            "bar_even_is_noop": True,   # m bar-even => b(q)=b(q^-1) identically
        }
        forward[name] = entry

    # ---- 4. STEELMAN coherence scan: hypothetical FREE m (falsification only) --
    def bisect(f, a, b):
        fa, fb = f(mp.mpf(a)), f(mp.mpf(b))
        if fa * fb > 0:
            return None
        return mp.findroot(f, (mp.mpf(a), mp.mpf(b)), solver="bisect", tol=mp.mpf(10) ** -30)

    steelman = {}
    # WRITHE: fix rho4=T4, read rho3 (and vice versa).  det even in m => bar-even == raw.
    mw = bisect(lambda m: b_writhe(4, m) / b_writhe(2, m) - T4, "0.30", "0.4472")
    if mw is not None:
        r3 = b_writhe(3, mw) / b_writhe(2, mw)
        steelman["writhe_fix_rho4"] = {
            "m": mp.nstr(mw, 8), "rho3_forced": mp.nstr(r3, 6),
            "rho3_target": mp.nstr(T3, 6), "rho3_err_pct": mp.nstr((r3 / T3 - 1) * 100, 4)}
    mw3 = bisect(lambda m: b_writhe(3, m) / b_writhe(2, m) - T3, "0.05", "0.4472")
    if mw3 is not None:
        r4 = b_writhe(4, mw3) / b_writhe(2, mw3)
        steelman["writhe_fix_rho3"] = {
            "m": mp.nstr(mw3, 8), "rho4_forced": mp.nstr(r4, 6),
            "rho4_target": mp.nstr(T4, 6), "rho4_err_pct": mp.nstr((r4 / T4 - 1) * 100, 4)}
    else:
        # NO ROOT — and this branch has always been the one taken.  It used to
        # leave nothing at all in the witness, so the docstring's "WRITHE
        # rho3=3.81 forces rho4=6.79 (-48%)" read as a measured result when in
        # fact the bisection never bracketed a sign change.  rho3_writhe is
        # DECREASING in m (2.907 at m=0.05 down to 2.450 at the ceiling), so it
        # never reaches 3.813 anywhere in the physical window.  That is a
        # STRONGER negative than the docstring claimed, so it is recorded, not
        # dropped.
        steelman["writhe_fix_rho3"] = {
            "root_exists": False,
            "rho3_at_bracket_lo": mp.nstr(b_writhe(3, mp.mpf("0.05")) / b_writhe(2, mp.mpf("0.05")), 6),
            "rho3_at_bracket_hi": mp.nstr(b_writhe(3, mp.mpf("0.4472")) / b_writhe(2, mp.mpf("0.4472")), 6),
            "rho3_target": mp.nstr(T3, 6),
            "note": "rho3_writhe is monotone DECREASING in m and capped below the "
                    "target over the whole physical window m < 1/sqrt5 -- no m "
                    "lands rho3=T3 at all, so there is nothing to force rho4 to."}
    # ISO raw: rho4 range (asymptotic limits m->0 and m->1).
    iso_rho4_at_0 = b_iso(4, mp.mpf("1e-6")) / b_iso(2, mp.mpf("1e-6"))
    iso_rho4_at_1 = b_iso(4, mp.mpf("0.999999")) / b_iso(2, mp.mpf("0.999999"))
    steelman["iso_raw_rho4_range"] = {
        "m->0": mp.nstr(iso_rho4_at_0, 5), "m->1": mp.nstr(iso_rho4_at_1, 5),
        # COMPUTED, not the literal False it used to be: rho4_iso is monotone
        # between the two endpoints, so the target is reachable iff it lies
        # between them.
        "reaches_target_13": bool(min(iso_rho4_at_0, iso_rho4_at_1) <= T4
                                  <= max(iso_rho4_at_0, iso_rho4_at_1)),
        "note": "rho4 monotone in (~3,~6); cannot reach strong target 13.03"}
    # ISO bar-even: where det(I-mS) first turns negative (unphysical) and rho4 there.
    m_neg = bisect(lambda m: det_iso(4, -m), "0.01", "0.9")  # 1-3m=0 -> m=1/3
    steelman["iso_bareven_unphysical_at"] = {
        "m_det_neg": (mp.nstr(m_neg, 6) if m_neg else "n/a"),
        "rho4_even_just_below": mp.nstr(
            mp.re(bar_even(b_iso, 4, mp.mpf("0.32")) / bar_even(b_iso, 2, mp.mpf("0.32"))), 5),
        "rho3_even_just_below": mp.nstr(
            mp.re(bar_even(b_iso, 3, mp.mpf("0.32")) / bar_even(b_iso, 2, mp.mpf("0.32"))), 5),
        "note": "rho3_even stalls near 3.4 against the 3.813 target.  (The old "
                "note here also claimed det(I-mS) turns negative BEFORE rho4_even "
                "reaches 13.03.  It does not -- see iso_bareven_fix_rho4: the "
                "target is reached at m=0.31900 with every det still positive.)"}
    # ISO bar-even, the branch the old note asserted was unreachable.  Solve it
    # instead of assuming it: rho4_even DOES reach T4 inside the physical window.
    r4_even = lambda m: mp.re(bar_even(b_iso, 4, m) / bar_even(b_iso, 2, m))   # noqa: E731
    r3_even = lambda m: mp.re(bar_even(b_iso, 3, m) / bar_even(b_iso, 2, m))   # noqa: E731
    m_even = bisect(lambda m: r4_even(m) - T4, "0.01", "0.32")
    if m_even is not None:
        steelman["iso_bareven_fix_rho4"] = {
            "m": mp.nstr(m_even, 8),
            "rho4_even_forced": mp.nstr(r4_even(m_even), 6),
            "rho4_target": mp.nstr(T4, 6),
            "rho3_even_forced": mp.nstr(r3_even(m_even), 6),
            "rho3_target": mp.nstr(T3, 6),
            "rho3_err_pct": mp.nstr((r3_even(m_even) / T3 - 1) * 100, 4),
            "physical": bool(det_iso(2, -m_even) > 0 and det_iso(3, -m_even) > 0
                             and det_iso(4, -m_even) > 0),
            "note": "rho4_even hits the strong A=4 target while all three dets "
                    "stay positive, so this branch is NOT excluded on "
                    "physicality -- it is excluded because rho3_even misses."}
    else:
        steelman["iso_bareven_fix_rho4"] = {"root_exists": False}

    # ---- 4b. THE COHERENCE VERDICT, counted rather than asserted -------------
    # `single_m_lands_both` used to be the literal False, and the assertion built
    # on it was computed="False"/expected="False" -- true by construction, and
    # green at exactly the value that would refute the probe (qou-26f2).  Count
    # instead.  Each candidate below is an m that lands ONE target EXACTLY (by
    # construction of the bisection that produced it); since each rho is monotone
    # in m on its branch, these are the ONLY m that land that target, so checking
    # the other rho at each one decides the claim for the whole window.  A branch
    # with no root cannot land both and contributes no candidate.
    COHERENCE_TOL = mp.mpf("0.05")          # same 5% gate as writhe_forced_rho3_*
    coherence_candidates = []
    if mw is not None:                      # WRITHE, lands rho4=T4
        coherence_candidates.append(
            ("writhe_fix_rho4", b_writhe(3, mw) / b_writhe(2, mw),
             b_writhe(4, mw) / b_writhe(2, mw)))
    if mw3 is not None:                     # WRITHE, lands rho3=T3  (no root here)
        coherence_candidates.append(
            ("writhe_fix_rho3", b_writhe(3, mw3) / b_writhe(2, mw3),
             b_writhe(4, mw3) / b_writhe(2, mw3)))
    if m_even is not None:                  # ISO bar-even, lands rho4=T4
        coherence_candidates.append(
            ("iso_bareven_fix_rho4", r3_even(m_even), r4_even(m_even)))
    n_lands_both = sum(
        1 for _, r3c, r4c in coherence_candidates
        if abs(r3c / T3 - 1) <= COHERENCE_TOL and abs(r4c / T4 - 1) <= COHERENCE_TOL)
    steelman["coherence_candidates_examined"] = [c[0] for c in coherence_candidates]
    steelman["single_m_lands_both_count"] = n_lands_both
    steelman["single_m_lands_both"] = bool(n_lands_both)

    # ---- assemble result ------------------------------------------------------
    result = {
        "bar_parity_of_parameter_free_magnitude": {
            "g_reeb": mp.nstr(g_reeb, 18), "g_reeb_bar_even": bool(g_bar_even),
            "z_naive": mp.nstr(z_naive, 18), "z_naive_bar_even": bool(z_bar_even),
            "consequence": "m(q^-1)=m(q) => b_A(q)=b_A(q^-1) for every A => bar-even "
                           "symmetrization is a STRUCTURAL NO-OP on the actual construction.",
        },
        "algebraic_preflight": {
            "writhe_det_matches_closed_form": bool(preflight),
            "A4_writhe_det_even_in_m": bool(a4_writhe_even),
            "A4_iso_det_even_in_m": bool(a4_iso_even),
            "reading": "A=4 writhe det=(1-5m^2)(1-m^2) is even in m (symmetric spectrum "
                       "{+-sqrt5,+-1}) => b_4 bar-even regardless of magnitude parity; the "
                       "iso det carries odd-in-m terms (A>=3).",
        },
        "isospin_corrected_strong_targets": {
            "rho3H": mp.nstr(rho3H, 6), "rho3He": mp.nstr(rho3He, 6), "rho4_raw": mp.nstr(rho4, 6),
            "EC3He_MeV": mp.nstr(EC3He, 6), "EC4He_MeV": mp.nstr(EC4, 6),
            "rho_strong_3": mp.nstr(rho_strong_3, 6),
            "rho_strong_4": mp.nstr(rho_strong_4, 6),
            "naive_avg_3_task_hint": mp.nstr(naive_avg_3, 6),
            "method": "Lean #3986: strong 3H/3He split=0 => 3H(Z=1,no pp pair) IS the strong "
                      "A=3 value => rho_strong(3)=B(3H)/BD=3.813 (the task's 3.6 is the naive "
                      "symmetric average, which is physically incorrect since only 3He carries "
                      "Coulomb). 4He: add pp-Coulomb E_C4=E_C3He*(3/4)^{1/3} back => 13.03.",
        },
        "forward_test_parameter_free": forward,
        "steelman_coherence_scan_free_m": steelman,
        "verdict": {
            "classification": "HONEST NEGATIVE (scope-(a)) with a scope-(b) sub-result.",
            "scope_b_subresult": "The parameter-free bond magnitude is bar-even (proved here) "
                                 "AND the A=4 writhe cumulant det is even in m (Lean "
                                 "B4CumulantBarEven.lean) => bar-even symmetrization is a "
                                 "structural no-op at the dominant A=4 magnitude wall.",
            "scope_a_negative": "No single parameter-free (or even free) m reproduces BOTH "
                                "isospin-corrected strong ratios {3.81, 13.03}: WRITHE rho4=13.03 "
                                "forces rho3=2.466 (-35.3%); WRITHE rho3=3.81 has no root at all "
                                "(rho3_writhe caps at 2.91 < 3.81 over the whole window); ISO raw "
                                "rho4 caps at ~6; ISO bar-even DOES reach rho4=13.03 at m=0.31900 "
                                "while still physical (all dets > 0), but rho3_even there is 3.435 "
                                "(-9.9%). Bar-even symmetrization does NOT tame "
                                "the overshoot (#3952) because the construction is already in "
                                "the bar-even sector -- there is no bar-odd part to isolate.",
            "consistency": "Consistent with (not a re-derivation of) the 2026-06-25 scope-(b) "
                           "pruning that 4He binding must be bar-even; here the b_A cumulant is "
                           "shown to be ALREADY bar-even, so the overshoot is a genuine bar-even "
                           "magnitude problem. Nothing wired, no fit, no AME inversion.",
        },
    }

    payload = {
        "computation": "deltalambda-bareven-b4-magnitude",
        "description": ("Vector-3 forward test: bar-even symmetrization of the b_A=-ln det(I+mG) "
                        "cumulant does NOT crack the isospin-even strong binding magnitude. The "
                        "parameter-free magnitude (g_reeb, z_naive) is bar-even => symmetrization "
                        "is a structural no-op; steelmanned with a free bar-odd m no single m "
                        "lands both isospin-corrected strong targets {3.81, 13.03}. Honest "
                        "negative, scope-(a) + scope-(b) sub-result. No fit, audit-only."),
        "tier": "structural (exact det closed forms + bar-parity argument; no fit, no AME inversion)",
        "result": result,
        "context": {
            "axis": "Delta_lambda magnitude wall -- Vector 3 (bar-even symmetrized b_A cumulant)",
            "attack_vector_map": "docs/audits/2026-07-18-deltalambda-attack-vector-map.md",
            "q0_convention": "experimental/proton pin, read by name from q_parameter.Q_50_DIGIT_STR (bean qou-9ugp)",
            "q0": Q0_STR,   # record the pin used, so a reader need not infer it
            "no_fit": True,
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "deltalambda-bareven-b4-magnitude", payload,
        script_path=__file__, engine="mpmath", output_dir=os.path.join(COMP, "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("g_reeb_bar_even", computed=str(bool(g_bar_even)), expected="True")
    wb.add_assertion("z_naive_bar_even", computed=str(bool(z_bar_even)), expected="True")
    wb.add_assertion("writhe_det_matches_closed_form", computed=str(bool(preflight)), expected="True")
    wb.add_assertion("A4_writhe_det_even_in_m", computed=str(bool(a4_writhe_even)), expected="True")
    wb.add_assertion("rho_strong_3_is_3p81", computed=rho_strong_3, expected=3.8128, tolerance=1e-3)
    wb.add_assertion("rho_strong_4_is_13p03", computed=rho_strong_4, expected=13.032, tolerance=2e-2)
    # The coherence gate FAILS: forcing WRITHE rho4=13.03 leaves rho3 >5% off target.
    _r3f = mp.mpf(steelman.get("writhe_fix_rho4", {}).get("rho3_forced", "0"))
    wb.add_assertion(
        "writhe_forced_rho3_misses_target_gt5pct",
        computed=str(bool(abs(_r3f / T3 - 1) > mp.mpf("0.05"))), expected="True")
    wb.add_assertion("iso_raw_rho4_cannot_reach_13", computed=str(float(iso_rho4_at_0) < 13.0), expected="True")
    # Was computed="False"/expected="False" -- passes by construction, and would
    # have stayed green at the value that refutes the probe (qou-26f2).  Now the
    # COUNT of m values that land both isospin-corrected strong targets within
    # the same 5% gate the sibling assertion uses, over every branch that has a
    # root.  Expected 0 is the honest-negative claim; one coherent m turns it red.
    wb.add_assertion(
        "single_m_lands_both_targets",
        computed=n_lands_both, expected=0, tolerance=0, unit="m values",
        source=("Coherence count over the branches examined "
                f"({', '.join(steelman['coherence_candidates_examined'])}). Each "
                "candidate m lands ONE target exactly by construction of the "
                "bisection that produced it, and each rho is monotone in m on its "
                "branch, so these are the only m that can land both. WRITHE at "
                "rho4=T4 gives rho3 off -35.3%; ISO bar-even at rho4=T4 (m=0.31900, "
                "all dets positive, so NOT excluded on physicality as the old note "
                "claimed) gives rho3_even off -9.9%; WRITHE rho3=T3 has no root at "
                "all in the physical window. Gate: 5%, matching "
                "writhe_forced_rho3_misses_target_gt5pct."))
    out = wb.save(extra={"auditOnly": True})

    # ---- console report -------------------------------------------------------
    print("=== Vector-3: bar-even-symmetrized b_A cumulant vs strong magnitude ===")
    print("parameter-free magnitude bar-parity:")
    print(f"   g_reeb  = {mp.nstr(g_reeb,10)}  bar-even={bool(g_bar_even)}")
    print(f"   z_naive = {mp.nstr(z_naive,10)}  bar-even={bool(z_bar_even)}")
    print("   => b_A(q)=b_A(q^-1) identically => bar-even symmetrization is a NO-OP.")
    print(f"algebraic preflight (mp.det vs closed form): {preflight};  A4 writhe det even in m: {a4_writhe_even}")
    print("isospin-corrected STRONG targets (from #3990 E_C):")
    print(f"   rho_strong(3) = {mp.nstr(rho_strong_3,6)}  (=B(3H)/BD; 3H Coulomb-free)")
    print(f"   rho_strong(4) = {mp.nstr(rho_strong_4,6)}  (=(B4+E_C4)/BD)")
    print(f"   [task hint 3.6 = naive avg {mp.nstr(naive_avg_3,5)} -- physically incorrect]")
    for name, e in forward.items():
        print(f"forward @ m={name}:")
        print(f"   WRITHE {e['writhe']}")
        print(f"   ISO    {e['iso']}")
    print("steelman coherence scan (free m, falsification only):")
    for k, val in steelman.items():
        print(f"   {k}: {val}")
    print("VERDICT: HONEST NEGATIVE (scope-(a)) + scope-(b) no-op sub-result. Not wired, no fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
