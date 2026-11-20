#!/usr/bin/env python3
"""
mirror_pair_em_isolation_probe — the 3H/3He mirror pair isolates the EM channel,
and the framework gets it to 0.3% while missing the absolute (strong) binding by
38-44%. So the low-isotope binding error is NOT in the electromagnetic sector.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Answers, with a measurement
rather than an argument, "which of EM / strong / weak does the discrepancy live
in?"

## Why the mirror pair is the right instrument

`3H` (Z=1,N=2) and `3He` (Z=2,N=1) are mirror nuclei: identical under p<->n
exchange. The strong interaction is isospin-symmetric to a good approximation, so
it very nearly CANCELS in the difference

    Delta_exp := B(3H) - B(3He)

and what survives is dominated by the Coulomb repulsion of the two protons in
`3He` plus a small isospin-breaking remainder. This is standard nuclear
phenomenology and is why mirror pairs are the classical Coulomb-energy probe.

The framework's chain law is
    B_sym = alpha * [ (Z-1) L_pp + L_pn + (N-1) L_nn ]
so for the mirror pair the `L_pn` terms cancel identically and

    Delta_model = alpha * (L_nn - L_pp)

with (closed form, `mass_binding_dashboard._bond_type_L`, bean qou-c6gx)

    L_XY = -ln(z + d_XY) - (e_XY/2) ln(1 - h),   z = q0^3/(q0^2+1)  [conv. D]
    d_pp = 0        (sigma,     writhe exponent e = +1)
    d_nn = -h       (sigma^-1,  writhe exponent e = -1)

**There is no electromagnetic input anywhere in that expression.** It is a
function of `q0` alone, times the CAL-1 scale `alpha = m_e/(q0(q0-1))`. So
comparing `Delta_model` to `Delta_exp` is a parameter-free test of whether the
framework's p/n asymmetry reproduces the nuclear Coulomb splitting.

## What is measured

Three things, in order of how much they constrain:

  1. **The mirror splitting** -- `Delta_model` vs `Delta_exp`, and the same
     comparison for the rival colour-weighted form `B_qCLT_fac`, which gives a
     different and much worse answer. That difference makes the test a
     DISCRIMINATOR between the two live log-forms, not merely a check.
  2. **The writhe normalisation's role.** Dropping it changes the prediction by
     2.3x. Since it is Lean-proved sorry-free
     (`QOU.QBeta.writhe_factor_unique_up_to_sign`) with no freedom to tune, the
     agreement is not available by adjusting it.
  3. **Where the error actually is** -- the per-isotope absolute deficit, showing
     that the residual is a single strong-channel shortfall that grows with the
     number of bonds, not an EM effect.

## Scope

Scope **(a)** throughout: a measurement and a discriminator. Nothing is wired,
no closure is proposed, and AME is used ONLY as the comparison target -- never
inverted into any weight. The bond constants are read from the production
dashboard's own closed form, not re-derived here, so this cannot silently use
different inputs than the table it is checking.

NO FLOAT64: mpmath `mpf` at 50 dps end to end, 50-digit proton pin, exact decimal
AME strings. `float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import json  # noqa: E402

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50


def constants():
    """Exactly the dashboard's closed form (`_bond_type_L`, bean qou-c6gx)."""
    from codata_constants import M_E_MEV as _me
    q0 = Q_MP
    h = q0 - 1 / q0
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    alpha = me / (q0 * (q0 - 1))
    z = q0**3 / (q0**2 + 1)                       # convention D
    delta = flavor_split_leading(q0)
    d = {"pp": mp.mpf(0),                          # sigma
         "pn": -h * (mp.mpf(1) / 2 - delta / 4),   # colour-weighted
         "nn": -h}                                 # sigma^-1
    e = {"pp": mp.mpf(1), "pn": mp.mpf(0), "nn": mp.mpf(-1)}   # writhe exponents
    wr = mp.log(1 - h)
    L = {k: -mp.log(z + d[k]) - (e[k] / 2) * wr for k in d}
    L_nowr = {k: -mp.log(z + d[k]) for k in d}
    return q0, h, alpha, z, delta, d, e, L, L_nowr


def ame():
    """AME2020 total binding energies keyed (Z, A), in MeV as `mpf`.

    Same file and same field the production dashboard uses
    (`mass_binding_dashboard._ame_table`), so this cannot silently compare
    against a different table than the one it is checking. The dashboard divides
    by 1000.0 in float; here the keV value is routed through `str` into `mpf`
    first, so the MeV figure carries full precision rather than f64.
    """
    p = _Path(__file__).resolve().parent / "data" / "ame2020.json"
    d = json.loads(p.read_text())
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    out = {}
    for r in rows:
        b = r.get("binding_energy_total_keV")
        if b is None:
            continue
        out[(r["Z"], r["A"])] = mp.mpf(str(b)) / 1000
    return out


def b_sym(Z, N, alpha, L):
    return alpha * ((Z - 1) * L["pp"] + L["pn"] + (N - 1) * L["nn"])


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0, h, alpha, z, delta, d, e, L, L_nowr = constants()
    raw = ame()

    print("mirror_pair_em_isolation_probe")
    print("=" * 78)
    print(f"q0 = {fmt(q0, 20)}   (50-digit proton pin)")
    print(f"h  = q0 - 1/q0 = {fmt(h, 14)}")
    print(f"z  = q0^3/(q0^2+1) = {fmt(z, 14)}   [convention D]")
    print(f"alpha = m_e/(q0(q0-1)) = {fmt(alpha, 14)} MeV   [CAL-1 scale]")
    print()
    print("Bond log-suppressions  L_XY = -ln(z + d_XY) - (e_XY/2) ln(1-h):")
    print(f"{'bond':>5} {'d_XY':>16} {'e (writhe)':>11} {'L (no writhe)':>15} "
          f"{'L':>15} {'alpha*L [MeV]':>15}")
    for k in ("pp", "pn", "nn"):
        print(f"{k:>5} {fmt(d[k], 12):>16} {fmt(e[k], 3):>11} "
              f"{fmt(L_nowr[k], 11):>15} {fmt(L[k], 11):>15} "
              f"{fmt(alpha * L[k], 11):>15}")
    print()
    print("  NOTE: no electromagnetic quantity appears anywhere above.  These")
    print("  are functions of q0 alone, times the CAL-1 mass scale.")
    print()

    # ---- 1. the mirror splitting ------------------------------------------
    # Keyed (Z, A) straight from the vendored table -- no hardcoded AME values
    # anywhere in this probe, so it cannot drift from the dashboard's targets.
    ZA = {"2H": (1, 2), "3H": (1, 3), "3He": (2, 3), "4He": (2, 4),
          "6Li": (3, 6), "7Li": (3, 7)}
    missing = [k for k, za in ZA.items() if za not in raw]
    assert not missing, f"AME table is missing {missing}"
    B = {k: raw[za] for k, za in ZA.items()}
    print(f"  AME2020 read from computations/data/ame2020.json "
          f"(binding_energy_total_keV), {len(B)} isotopes, no hardcoded values")
    print()

    d_exp = B["3H"] - B["3He"]
    d_mod = alpha * (L["nn"] - L["pp"])
    d_nowr = alpha * (L_nowr["nn"] - L_nowr["pp"])

    print("1. THE MIRROR SPLITTING — the EM isolator")
    print("-" * 78)
    print("  3H (Z=1,N=2) and 3He (Z=2,N=1) are mirror nuclei.  In")
    print("  B_sym = alpha[(Z-1)L_pp + L_pn + (N-1)L_nn] the L_pn terms cancel")
    print("  identically, leaving  Delta_model = alpha (L_nn - L_pp).")
    print()
    print(f"  B_AME(3H)              = {fmt(B['3H'], 10)} MeV")
    print(f"  B_AME(3He)             = {fmt(B['3He'], 10)} MeV")
    print(f"  Delta_exp              = {fmt(d_exp, 10)} MeV   <- Coulomb-dominated")
    print(f"  Delta_model            = {fmt(d_mod, 10)} MeV   <- pure q0, no EM in")
    rel = (d_mod - d_exp) / d_exp
    print(f"  Delta_model/Delta_exp  = {fmt(d_mod / d_exp, 10)}")
    print(f"  relative error         = {fmt(rel * 100, 6)} %")
    print()
    assert abs(rel) < mp.mpf("0.02"), "mirror splitting should agree within 2%"
    print(f"  => the mirror splitting is reproduced to {fmt(abs(rel) * 100, 3)} %,")
    print("     with NO electromagnetic input of any kind.")
    print()

    # ---- 2. the writhe normalisation is load-bearing and not tunable -------
    print("2. THE WRITHE NORMALISATION IS LOAD-BEARING")
    print("-" * 78)
    print(f"  without writhe: Delta = {fmt(d_nowr, 10)} MeV "
          f"({fmt(d_nowr / d_exp, 6)}x experiment)")
    print(f"  with writhe   : Delta = {fmt(d_mod, 10)} MeV "
          f"({fmt(d_mod / d_exp, 6)}x experiment)")
    print(f"  the factor between them is {fmt(d_nowr / d_mod, 8)}")
    print()
    print("  This matters for whether the agreement is cheap.  The writhe factor")
    print("  is Lean-proved SORRY-FREE and unique up to sign")
    print("  (QOU.QBeta.writhe_factor_unique_up_to_sign: Markov invariance forces")
    print("  S_hat = S*A^(e-n) with A^2 = 1-h), so there is NO freedom to tune it")
    print("  and the 0.3% could not have been dialled in by choosing it.")
    assert abs(d_nowr / d_exp - 1) > mp.mpf("1.0"), \
        "without writhe the prediction must be badly off, else the point is empty"
    print()

    # ---- 3. the rival form gets it wrong — so this is a discriminator ------
    print("3. IT DISCRIMINATES BETWEEN THE TWO LIVE LOG-FORMS")
    print("-" * 78)
    print("  B_qCLT_fac = alpha*(A-1)*<bond-type L> uses the same bond constants")
    print("  but averages them over the bond multiset instead of using the chain.")
    print("  For the mirror pair (dashboard table): 3H 5.98, 3He 5.47.")
    q_3h, q_3he = mp.mpf("5.98"), mp.mpf("5.47")
    d_qclt = q_3h - q_3he
    print(f"  Delta_qCLT_fac  = {fmt(d_qclt, 6)} MeV   "
          f"({fmt(d_qclt / d_exp, 5)}x experiment)")
    print(f"  Delta_B_sym     = {fmt(d_mod, 6)} MeV   "
          f"({fmt(d_mod / d_exp, 6)}x experiment)")
    print()
    print("  B_sym wins decisively on a quantity neither form was built to fit.")
    print("  That is what makes this a DISCRIMINATOR and not just a check: the")
    print("  two forms agree on the isospin-symmetric part and disagree exactly")
    print("  where the p/n asymmetry enters.")
    assert abs(d_mod / d_exp - 1) < abs(d_qclt / d_exp - 1), \
        "B_sym must beat B_qCLT_fac on the mirror splitting"
    print()

    # ---- 4. where the error actually is ------------------------------------
    print("4. WHERE THE ERROR ACTUALLY IS — the strong channel, and it scales")
    print("-" * 78)
    ISO = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
           ("6Li", 3, 3), ("7Li", 3, 4)]
    print(f"{'iso':>5} {'A':>3} {'bonds':>6} {'B_AME':>10} {'B_sym':>10} "
          f"{'deficit':>10} {'deficit/bond':>13} {'B_AME/B_sym':>12}")
    rows = []
    for nm, Z, N in ISO:
        A = Z + N
        bs = b_sym(Z, N, alpha, L)
        defc = B[nm] - bs
        rows.append((nm, A, A - 1, B[nm], bs, defc, defc / (A - 1), B[nm] / bs))
        print(f"{nm:>5} {A:>3} {A-1:>6} {fmt(B[nm], 7):>10} {fmt(bs, 7):>10} "
              f"{fmt(defc, 7):>10} {fmt(defc/(A-1), 7):>13} "
              f"{fmt(B[nm]/bs, 6):>12}")
    print()
    print("  The deficit is POSITIVE for every A >= 3 and NEGATIVE at 2H -- the")
    print("  deuteron is the only over-bound case.  4He carries by far the")
    print("  largest deficit, and 6Li/7Li share an almost identical ratio, so")
    print("  past A ~ 6 the A-dependence is right and only the SCALE is wrong.")
    print()

    print("READING — which sector the discrepancy is in")
    print("-" * 78)
    print(f"  * EM: reproduced to {fmt(abs(rel)*100, 3)} % on the one observable")
    print("    that isolates it, parameter-free.  The electromagnetic sector is")
    print("    NOT where the error lives.")
    print("  * STRONG: the absolute binding misses by 27 % (2H, over) to 226 %")
    print("    (4He, under).  The whole residual sits here.")
    print("  * WEAK: not probed by binding energies at all -- the weak sector")
    print("    enters via CAL-2 (the beta-decay width) and Q_beta, not B(A,Z).")
    print("    Nothing here constrains it, and nothing here should be read as")
    print("    doing so.")
    print()
    # A numerical near-coincidence that WILL be conflated if not flagged.
    print("A CONFLATION HAZARD — flagged so nobody 'notices' it later")
    print("-" * 78)
    qbeta_model = mp.mpf("0.7836")      # np-discrepancy-resolution.md
    qbeta_codata = mp.mpf("0.7823334093099085")
    print(f"  Q_beta (model, np-discrepancy-resolution)  = {fmt(qbeta_model, 6)} MeV")
    print(f"  Q_beta (CODATA)                            = "
          f"{fmt(qbeta_codata, 8)} MeV")
    print(f"  mirror splitting Delta_exp (this probe)    = {fmt(d_exp, 8)} MeV")
    print(f"  Delta_exp / Q_beta_CODATA                  = "
          f"{fmt(d_exp / qbeta_codata, 6)}")
    print()
    print("  These agree to ~2.4 % and are DIFFERENT PHYSICS: Q_beta is the")
    print("  free-neutron beta-decay Q-value (weak sector, CAL-2), while the")
    print("  mirror splitting is the Coulomb energy of a pp pair in 3He.  The")
    print("  corpus already carries a nucleon-level 'mirror' discussion in")
    print("  np-discrepancy-resolution.md about n vs p, which is a THIRD object")
    print("  again.  Three ~0.78 MeV quantities, one of which is weak, one EM,")
    print("  one a nucleon mass asymmetry.  Do not let them merge.")
    print()

    print("WHAT THIS DOES NOT SAY")
    print("-" * 78)
    print("  * NOT that the framework 'derives the Coulomb energy'.  It")
    print("    reproduces the mirror SPLITTING; the mirror splitting is")
    print("    Coulomb-DOMINATED, not purely Coulomb (isospin breaking in the")
    print("    strong force contributes a few percent), and one observable")
    print("    agreeing to 0.3 % is one data point, not a derivation.")
    print("  * NOT that B_sym is correct.  Its absolute binding is badly wrong")
    print("    and its log-form is still POSITED (bean qou-unqc: no dynamics")
    print("    licenses alpha*ln(ratio) as an energy).")
    print("  * NOT a fit.  AME enters only as the comparison target; the bond")
    print("    constants come from q0 through the dashboard's closed form.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
