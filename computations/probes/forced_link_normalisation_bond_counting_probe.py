#!/usr/bin/env python3
"""
Probe — the forced link-invariant normalisation of the convention-D Ocneanu
trace, and what it does to the additive binding law of #6611.

FORMALIZE-FIRST CONTEXT (QOU/MathlibExt/ForcedLinkNormalisation.lean, sorry-free):

  Markov-move invariance of X = mu^(n-1) nu^e tr on each sigma^{±1} branch is
  two equations, mu nu z = 1 and mu nu^-1 z' = 1, with the unique solution
      nu^2 = z'/z,   mu = 1/(nu z).                         (nu_sq_forced, mu_forced)
  Then nu z = nu^-1 z' — the normalised weight of a crossing does NOT depend
  on its sign (normalised_weights_equal) — so any branch mixture c+ sigma +
  c- sigma^-1 with c+ + c- = 1 has the same normalised weight (normalised_mixture).
  At convention D (z = q^3/(q^2+1), z' = z - h = 1/(q^3+q)):
      nu = q^-2,  mu = (q^2+1)/q = [2]_q,  common weight = q/(q^2+1).   (convD_*)

CONSEQUENCE FOR THE BINDING LAW. Under #6611's surviving law
B = E_0 ln(tr_free/tr_atom), the monotone factorization makes B a sum over
the bond letters alone. Normalised: mu^(n-1) cancels (both words have 3A
strands), and every single-letter bond — pp = sigma, nn = sigma^-1, pn = the
colour-weighted branch mixture — has the SAME normalised weight q/(q^2+1). So

    B_norm = (A - 1) · E_0 · ln((q^2+1)/q) = (A - 1) · E_0 · ln [2]_q,

pure bond counting with one derived bond energy. The un-normalised bond
energies -ln b_pp != -ln b_pn != -ln b_nn — and the (N-Z) asymmetry #6611
measured to have the WRONG sign against the data (kappa_derived = +0.22 vs
data optimum ~ -0.15) — are exactly the writhe factor nu^e the un-normalised
trace leaves in. #6611 also measured, empirically, that "bond COUNT only
(layout-free)" beats every isospin-resolved variant on the p5-p95 spread; the
forced normalisation PREDICTS that shape.

WHAT THIS PROBE MEASURES (all exact/mpmath 50 dps, no fit):
  1. the three production bond-letter traces b_pp, b_pn, b_nn from the
     production word, matching #6611's closed forms;
  2. their normalised weights: all three equal q/(q^2+1) to 50 dps;
  3. B_norm for 2H/3H/3He/4He against AME, and the residual SCALE
     (a target, never a criterion);
  4. the same scale-free spread metric as #6611's roast probe over the
     measured AME nuclides (same selection, same percentile function):
     p5-p95 of B_exp/B_pred for the un-normalised law at E_0 vs B_norm.
     Since the metric is scale-free, B_norm's spread equals #6611's "bond
     COUNT only" spread by construction — the check is that the derived
     law lands on the empirically best shape, not that it fits.

Nothing wired, nothing fitted. The scale (E_0 vs the data) is untouched.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

import cyclic_triple_bond_cross_term_probe as ct  # noqa: E402  (affine-letter algebra, same dir)
from binding_log_free_energy import M_E_MEV  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402

mp.mp.dps = 50
Q, H, Z_D, TOL = ct.Q, ct.H, ct.Z_D, ct.TOL
Z_INV = Z_D - H                                  # MarkovTrace.markovParam_inv_eq_sub
M_E = mp.mpf(str(M_E_MEV))
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
NU = 1 / Q ** 2
MU = (Q ** 2 + 1) / Q
W_NORM = Q / (Q ** 2 + 1)
EPS_BOND = E0 * mp.log((Q ** 2 + 1) / Q)         # the derived bond energy
ROOT = Path(__file__).resolve().parents[2]
AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _pct(vals, num, den=100):
    v = sorted(vals)
    return v[min(len(v) - 1, len(v) * num // den)]


def bond_letters(word, A):
    """the (a, b) affine form of each bond letter, in chain order."""
    return [ct.letter(word[i][0], word[i][1]) for i in ct.bond_positions(word, A)]


def branch_weights(L):
    """c σ + d·1 = (c + d/h) σ − (d/h) σ⁻¹  (branch form; c₊ + c₋ = c)."""
    a, b = L                       # a = d, b = c
    return (b + a / H, -a / H)


def main() -> int:
    checks: list[tuple[str, bool]] = []
    print(f"  q0 = {mp.nstr(Q, 20)}   z = {mp.nstr(Z_D, 15)}   z' = z − h = {mp.nstr(Z_INV, 15)}"
          f"   1/(q³+q) = {mp.nstr(1 / (Q ** 3 + Q), 15)}")
    checks.append(("z' = z − h = 1/(q³+q) (convD_zinv)", abs(Z_INV - 1 / (Q ** 3 + Q)) < TOL))
    checks.append(("ν = q⁻² satisfies ν² = z'/z (nu_sq_forced / convD_nu)", abs(NU ** 2 - Z_INV / Z_D) < TOL))
    checks.append(("μ = [2]_q satisfies μ ν z = 1 (mu_forced / convD_mu)", abs(MU * NU * Z_D - 1) < TOL))
    checks.append(("μ ν⁻¹ z' = 1 (the second Markov move)", abs(MU / NU * Z_INV - 1) < TOL))
    checks.append(("ν z = ν⁻¹ z' = q/(q²+1) (normalised_weights_equal / convD_weight)",
                   abs(NU * Z_D - W_NORM) < TOL and abs(Z_INV / NU - W_NORM) < TOL))
    print(f"  forced: ν = q⁻² = {mp.nstr(NU, 15)}   μ = [2]_q = {mp.nstr(MU, 15)}   "
          f"common crossing weight q/(q²+1) = {mp.nstr(W_NORM, 15)}")
    print(f"  E_0 = {mp.nstr(E0, 12)} MeV   derived bond energy ε = E_0·ln[2]_q = {mp.nstr(EPS_BOND, 12)} MeV\n")

    # ---- 1–2: production bond letters, raw and normalised ------------------
    seen = {}
    for name, Z, N in ct.NUCLEI:
        A = Z + N
        W = atom_braid_word_3A(Z, N)
        sp = ["p"] * Z + ["n"] * N
        for k, L in enumerate(bond_letters(W, A)):
            key = f"{sp[k]}{sp[k + 1]}"
            raw = ct.aff_tr(L)
            cp, cm = branch_weights(L)
            norm = cp * NU * Z_D + cm * Z_INV / NU
            checks.append((f"{name} bond {k} ({key}): branch form reproduces the raw trace c₊z + c₋z'",
                           abs(cp * Z_D + cm * Z_INV - raw) < TOL))
            checks.append((f"{name} bond {k} ({key}): c₊ + c₋ = 1", abs(cp + cm - 1) < TOL))
            checks.append((f"{name} bond {k} ({key}): normalised weight = q/(q²+1)", abs(norm - W_NORM) < TOL))
            seen.setdefault(key, (raw, cp, cm, norm))
    print("  bond letter   c₊        c₋        raw trace b      −ln b      normalised   −ln(norm)")
    for key, (raw, cp, cm, norm) in seen.items():
        print(f"    {key:>3}     {mp.nstr(cp, 8):>9} {mp.nstr(cm, 8):>9}   {mp.nstr(raw, 12):>14}"
              f"  {mp.nstr(-mp.log(raw), 8):>9}   {mp.nstr(norm, 12):>12}  {mp.nstr(-mp.log(norm), 8)}")
    checks.append(("raw b_pp = z, b_nn = z' (#6611's closed forms)",
                   abs(seen["pp"][0] - Z_D) < TOL and abs(seen["nn"][0] - Z_INV) < TOL))
    print()

    # ---- 3: 2H–4He under the un-normalised and the normalised law ----------
    print("  nucleus   B_log(un-normalised)   B_norm = (A−1)·ε   B_AME     AME/B_norm")
    ratios_light = []
    for name, Z, N in ct.NUCLEI:
        A = Z + N
        ta, tf, _, _ = tr_m_atom_zn(Z, N)
        B_log = E0 * mp.log(tf / ta)
        B_norm = (A - 1) * EPS_BOND
        B_ame = ame_binding_mev(Z, A)
        ratios_light.append(B_ame / B_norm)
        print(f"    {name:>4}   {mp.nstr(B_log, 8):>12}          {mp.nstr(B_norm, 8):>10}      "
              f"{mp.nstr(B_ame, 8):>8}   {mp.nstr(B_ame / B_norm, 6)}")
    print()

    # ---- 4: the full AME scan with #6611's metric ---------------------------
    rows = []
    for ent in json.loads(AME.read_text())["entries"]:
        Z, N, A = ent["Z"], ent["N"], ent["A"]
        bpa = ent.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not bpa or ent.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B > 0:
            rows.append((A, Z, N, B))
    b_pp, b_pn, b_nn = seen["pp"][0], seen["pn"][0], seen["nn"][0]

    def B_unnorm(A, Z, N):      # #6611's segregated chain: (Z−1) pp, 1 pn, (N−1) nn
        return E0 * ((Z - 1) * -mp.log(b_pp) + -mp.log(b_pn) + (N - 1) * -mp.log(b_nn))

    def B_norm_law(A, Z, N):
        return (A - 1) * EPS_BOND

    def spread(pred):
        v = [B / pred(A, Z, N) for (A, Z, N, B) in rows]
        return (_pct(v, 50), _pct(v, 75) / _pct(v, 25), _pct(v, 95) / _pct(v, 5), max(v) / min(v))

    print(f"  {len(rows)} measured AME nuclides (#6611's selection and percentile function)")
    print(f"    {'law':<40}{'median AME/pred':>16}{'p25-p75':>10}{'p5-p95':>10}{'full':>10}")
    res = {}
    for nm, f in (("un-normalised segregated chain (#6611)", B_unnorm),
                  ("normalised = bond counting, ε derived", B_norm_law)):
        med, iqr, p595, full = spread(f)
        res[nm] = (med, iqr, p595, full)
        print(f"    {nm:<40}{mp.nstr(med, 7):>16}{mp.nstr(iqr, 6):>10}{mp.nstr(p595, 6):>10}{mp.nstr(full, 6):>10}")
    un, no = res["un-normalised segregated chain (#6611)"], res["normalised = bond counting, ε derived"]
    checks.append(("normalised law has a tighter p5–p95 spread than the un-normalised segregated chain",
                   no[2] < un[2]))
    checks.append(("normalised law has a tighter p25–p75 spread too", no[1] < un[1]))
    checks.append(("the (N−Z) asymmetry vanishes identically under normalisation (all three bond energies equal)",
                   all(abs(seen[k][3] - W_NORM) < TOL for k in ("pp", "pn", "nn"))))
    print(f"\n  residual SCALE under the normalised law: median AME/B_norm = {mp.nstr(no[0], 8)}"
          f"   (ε would need to be {mp.nstr(no[0] * EPS_BOND, 8)} MeV; #6611's factor on E_0 was 2.656)")
    print("  — a target for a future derivation to be checked against, not a criterion to search on.")

    ok = 0
    print()
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
