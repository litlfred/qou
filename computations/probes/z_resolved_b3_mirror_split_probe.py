#!/usr/bin/env python3
"""The Z-resolved b_3: the framework's per-(Z,N) construction reproduces the
A=3 mirror SPLIT to 0.20 % from q_0 alone -- and nothing else. Both b_3
magnitudes come out negative against a positive target, and the same split
formula is 2.15x and 3.93x short at A=7 and A=13.

Bean `qou-tbk7`, takeover of PR #7005.

## What #7005 measured, and what it left as inference

`binding_resolution_loss_is_self_inflicted_probe.py` (#7005) measured that AME
knows b_3 = B(3) - 3*B(2) to ~6 digits per mirror partner, and that the A-only
body-order construction averages 3H (1808.10 keV) and 3He (1044.34 keV) into a
53.6 % band -- 0.271 digits.  5.81 digits lost to the convention, none to
experiment.  It INFERRED, and flagged as inference, that a Z-resolved
construction would have ~6.1 digits to work with, and explicitly did NOT claim
that such a construction would find anything.

This probe builds that construction from the machinery the corpus already has
and measures both halves: the resolution (exactly, no `math.hypot`), and what
the framework's Z-resolved b_3 actually is.

## The construction -- nothing new is introduced

The per-(Z,N) canonical word `atom_braid_word_3A(Z, N)` is distinct for tritium
(1,2) and helium-3 (2,1) (`per_atom_braid_closure_probe`, #6942).  The corpus
evaluates two binding forms on it, both at the proton q_0 under convention D
(`z = q^3/(q^2+1)`), both mpmath at the 50-dps transfer floor:

  * the EXACT Markov trace of the word, via the fine-Bratteli transfer engine
    `tr_m_atom_via_transfer.tr_m_atom_zn` (validated against the full Hoefsmit
    character sum to the 50-dps floor):
        B_sym^exact = alpha * ln(tr_free / tr_atom)          (POSITED: alpha*ln)
        B_can0      = alpha * (tr_free - tr_atom)            (brane tower, level 0)
  * the PRODUCTION closed-form chain `mass_binding_dashboard._bond_type_L`:
        B_sym^chain = (Z-1)*b_pp + b_pn + (N-1)*b_nn,
        b_XY = alpha * [ -ln(z + d_XY) - (de_XY/2) * ln(1-h) ]
    with d_pp = 0, d_pn = -h(1/2 - delta/4), d_nn = -h (the sigma / colour-
    weighted / sigma^-1 interfaces), delta = flavor_split_leading(q_0), and the
    writhe normalisation (1-h)^(de/2) that `WritheNormalisation.lean` proves is
    forced by Markov invariance up to sign.

Every input is a function of q_0 (proton pin, `Q_50_DIGIT_STR`) and the CAL-1
unit m_e through alpha = E_0 = m_e / (q_0 (q_0 - 1)).  No per-case constant, no
fitted weight, no census knot.  The Z-resolved b_3 is then simply

        b_3(Z, N) := B(Z, N) - 3 * B(1, 1)

evaluated on each form -- the SAME definition #7005 applied to AME, so the
comparison is like against like.

## Findings

1. RESOLUTION (exact `Fraction` propagation, sigma_3^2 + 9 sigma_2^2):
       b_3(3H)  = 1808.0976 keV   sigma 0.001500 keV   6.081 digits
       b_3(3He) = 1044.3427 keV   sigma 0.001282 keV   5.911 digits
       split    =  763.7549 keV   sigma 0.001006 keV   5.880 digits
   #7005's ~6.1 inference is confirmed as a measurement; the float `math.hypot`
   step it used moves nothing at this level.

2. MAGNITUDE: NEGATIVE on every form, against a POSITIVE target.
       form            b_3(3H) MeV   b_3(3He) MeV      AME   +1.808   +1.044
       chain (prod.)      -2.359        -3.124
       exact trace        -1.869        -3.616
       B_can0             -1.374        -1.304
   That is not a near miss; it is the pairwise wall in Z-resolved form.  Every
   one of these is pairwise-additive over bonds, so its "b_3" is not a connected
   3-body cumulant at all -- it is the bond-heterogeneity term
   b_XX - 2 b_pn (chain) with the deuteron bond counted three times.  The
   connected 3-body part of every corpus assembly is 0 or negative
   (`PairwiseCumulantVanishing`, `MayerThreeBodySign`, bean `qou-edt7`), and
   resolving Z does not change that.

3. THE SPLIT, from q_0 alone.  On the chain the deuteron term cancels and
       b_3(3H) - b_3(3He) = B(1,2) - B(2,1) = b_nn - b_pp
                          = alpha * ln( q_0^3 (1 + q_0 - q_0^2) )
   (closed form verified here to the 60-dps floor; it uses z - h = 1/(q(q^2+1))
   and z(1-h) = q^2(1+q-q^2)/(q^2+1)).  Numerically

       framework  0.7653202 MeV      AME  0.7637549 MeV      +0.205 %,  +1.565 keV

   Direction right (3H more bound), magnitude 0.2 % out.  The writhe factor is
   load-bearing: without it the exact-trace split is 1.7470 MeV (2.29x), which
   is the "3x overshoot" recorded under convention C in
   `2026-07-11-mirror-split-coulomb-diagnosis.md` (2.27 MeV then).

4. AND IT IS A COINCIDENCE AT A=3, not a mechanism.  The chain split is
   b_nn - b_pp for EVERY mirror pair (Z, Z+1)/(Z+1, Z) -- it does not depend on
   Z at all -- while the measured split is the Coulomb displacement energy and
   grows with Z:
       pair        framework   AME      ratio
       3H/3He        0.7653    0.7638   1.002
       7Li/7Be       0.7653    1.6442   0.465
       13C/13N       0.7653    3.0028   0.255
   The exact trace at A=7 (un-normalised) gives 1.7470 MeV against 1.6442, 6 %
   out -- but that is the same Z-independent constant that is 2.29x out at A=3,
   so it cannot be right at both.  `coulomb_mirror_killswitch_probe` already
   recorded the 0.002 MeV hit at A=3 beside 0.65 and 1.59 MeV misses at A=7 and
   A=13, and read it the same way.  `mirror_penalty_decomposition_probe` and
   `c1_mirror_asymmetry_sign_probe` found the trace-only forms sign-BACKWARDS
   on the split; B_can0 reproduces that here (-0.070 MeV).

## Verdict -- scope (a)

The Z-resolved construction exists, is cheap (0.1 s per A=3 word), and has the
~6 digits #7005 said it would.  It reproduces NEITHER b_3 magnitude (wrong sign,
both nuclides, all forms) and reproduces the A=3 split by a coincidence that
fails at the next two mirror pairs by 2.15x and 3.93x.  What it does establish
is structural: the A-only b_3 of the corpus conflates two things -- the
bond-heterogeneity difference b_nn - b_pp, which the framework predicts and the
data locate in Coulomb, and the connected 3-body cumulant, which the framework
puts at <= 0 and the data at > 0.  Resolving Z separates them and shows the
second is the open one.  Nothing here refutes an ingredient; the 31 %
`tanh(ln q_0) * B_pp` Coulomb derivation on `main`
(`a3_mirror_residual_reconciliation`) and the EM-linking gate are untouched.

## Precision

mpmath end to end (dps 60 for the closed forms; the transfer engine's own 50-dps
floor for the traces); AME as exact `Fraction` from the vendored table, the
uncertainties from `binding_energy_per_A_unc_keV * A`.  Uncertainties combined in
quadrature as `Fraction`s and square-rooted in mpmath.  `float()` nowhere; every
printed number goes through `mp.nstr`.  Proton pin (`Q_50_DIGIT_STR`),
convention D throughout; one witness stamped `q0Anchor: proton`.

-- Ref: [manuscript] computations/probes/binding_resolution_loss_is_self_inflicted_probe.py (#7005)
-- Ref: [manuscript] docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md
-- Ref: [manuscript] docs/audits/2026-07-11-mirror-split-coulomb-diagnosis.md
-- Ref: [manuscript] computations/probes/coulomb_mirror_killswitch_probe.py
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
_ROOT = _COMP.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

import mass_binding_dashboard as mbd  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60

AME_PATH = _ROOT / "qou-mass/src/qou_mass/data/ame2020.json"
NUCLIDES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
MIRROR_PAIRS = [("3H/3He", (1, 2), (2, 1)), ("7Li/7Be", (3, 4), (4, 3)),
                ("13C/13N", (6, 7), (7, 6))]

CHECKS: list[bool] = []


def fmt(x, n=30):
    if isinstance(x, F):
        x = mpf_of_frac(x)
    return mp.nstr(mp.mpf(x), n)


def mpf_of_frac(f: F) -> mp.mpf:
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def check(name, ok, note=""):
    CHECKS.append(bool(ok))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}" + (f"  ({note})" if note else ""))
    return ok


def load_ame():
    d = json.load(open(AME_PATH))
    E = {(e["Z"], e["A"]): e for e in d["entries"]}

    def B_keV(Z, N):
        return F(str(E[(Z, Z + N)]["binding_energy_total_keV"]))

    def U_keV(Z, N):
        return F(str(E[(Z, Z + N)]["binding_energy_per_A_unc_keV"])) * (Z + N)

    return B_keV, U_keV


def main() -> int:
    wb = WitnessBuilder("z-resolved-b3-mirror-split-probe", engine="mpmath")
    wb.set_description(
        "The Z-resolved b_3 = B(Z,N) - 3 B(1,1), built from the per-(Z,N) "
        "canonical word at the proton q_0 under convention D. Resolution "
        "measured exactly: 6.08 digits (3H), 5.91 (3He), 5.88 on the split. "
        "The framework's Z-resolved b_3 is NEGATIVE on every form (chain, "
        "exact trace, B_can0) against a positive AME target -- the pairwise "
        "wall in Z-resolved form. The A=3 mirror split alone is reproduced "
        "from q_0: b_nn - b_pp = alpha*ln(q_0^3(1+q_0-q_0^2)) = 0.76532 MeV vs "
        "AME 0.76375 (+0.205 %), but that constant is Z-independent while the "
        "Coulomb displacement energy grows with Z, so it is 2.15x short at "
        "7Li/7Be and 3.93x at 13C/13N: a coincidence, not a mechanism. "
        "Scope (a); no ingredient excluded; no fit; no per-case constant.")

    B_keV, U_keV = load_ame()
    me, q0, alpha = mbd._constants()
    Lb = mbd._bond_type_L()
    b = {k: alpha * v for k, v in Lb.items()}

    print("=" * 78)
    print("Z-resolved b_3 and the mirror split -- proton q_0, convention D")
    print("=" * 78)
    print(f"  q_0 = {fmt(q0, 25)}   alpha = E_0 = {fmt(alpha, 20)} MeV")
    print(f"  per-bond chain bindings (writhe-normalised): "
          f"b_pp {fmt(b['pp'], 12)}  b_pn {fmt(b['pn'], 12)}  b_nn {fmt(b['nn'], 12)} MeV")

    # ---------------------------------------------------------------- 1. resolution
    print("\n1. Resolution of the Z-resolved b_3 -- exact Fraction propagation")
    b3_ame, sig_ame, dig_ame = {}, {}, {}
    B2, U2 = B_keV(1, 1), U_keV(1, 1)
    for lbl, Z, N in (("3H", 1, 2), ("3He", 2, 1)):
        b3 = B_keV(Z, N) - 3 * B2
        var = U_keV(Z, N) ** 2 + 9 * U2 ** 2
        sig = mp.sqrt(mpf_of_frac(var))
        dig = mp.log10(mpf_of_frac(b3) / sig)
        b3_ame[lbl], sig_ame[lbl], dig_ame[lbl] = b3, sig, dig
        print(f"     {lbl:<4} b_3 = {fmt(b3, 10)} keV   sigma = {fmt(sig, 6)} keV"
              f"   {fmt(dig, 4)} digits")
    split_ame = B_keV(1, 2) - B_keV(2, 1)                    # == b3(3H) - b3(3He)
    var_split = U_keV(1, 2) ** 2 + U_keV(2, 1) ** 2
    sig_split = mp.sqrt(mpf_of_frac(var_split))
    dig_split = mp.log10(mpf_of_frac(split_ame) / sig_split)
    print(f"     split b_3(3H)-b_3(3He) = {fmt(split_ame, 10)} keV   sigma = "
          f"{fmt(sig_split, 6)} keV   {fmt(dig_split, 4)} digits")
    check("b_3(3H) resolved to > 6 digits", dig_ame["3H"] > 6, fmt(dig_ame["3H"], 4))
    check("b_3(3He) resolved to > 5.9 digits", dig_ame["3He"] > mp.mpf("5.9"),
          fmt(dig_ame["3He"], 4))
    check("the split is resolved to > 5.8 digits", dig_split > mp.mpf("5.8"),
          fmt(dig_split, 4))
    wb.add_data("resolution_exact", {
        "b3_3H_keV": str(b3_ame["3H"]), "sigma_3H_keV": fmt(sig_ame["3H"]),
        "digits_3H": fmt(dig_ame["3H"]),
        "b3_3He_keV": str(b3_ame["3He"]), "sigma_3He_keV": fmt(sig_ame["3He"]),
        "digits_3He": fmt(dig_ame["3He"]),
        "split_keV": str(split_ame), "sigma_split_keV": fmt(sig_split),
        "digits_split": fmt(dig_split),
        "method": "b3 = B(Z,N) - 3 B(1,1) as exact Fraction; var = u3^2 + 9 u2^2 "
                  "as Fraction; sqrt and log10 in mpmath at 60 dps"})
    wb.add_assertion(
        name="z_resolved_b3_has_six_digits", computed=fmt(dig_ame["3H"]),
        expected="6.081", tolerance="0.005", unit="significant digits (3H)",
        source="#7005 inferred ~6.1 from float hypot; measured here exactly")
    check("matches #7005's inferred ~6.08", abs(dig_ame["3H"] - mp.mpf("6.081")) < mp.mpf("0.005"))

    # ---------------------------------------------------------- 2. framework forms
    print("\n2. Framework Z-resolved bindings on the per-(Z,N) word (MeV)")
    forms = {"chain": {}, "exact": {}, "can0": {}}
    traces = {}
    for lbl, Z, N in NUCLIDES:
        t0 = time.time()
        ta, tf, _chi, _wall = tr_m_atom_zn(Z, N, dps=50)
        traces[lbl] = (ta, tf)
        forms["exact"][lbl] = alpha * mp.log(tf / ta)
        forms["can0"][lbl] = alpha * (tf - ta)
        forms["chain"][lbl] = (max(Z - 1, 0) * b["pp"] + b["pn"] + max(N - 1, 0) * b["nn"])
        shift = mbd._chain_writhe_shift(Z, N, alpha)
        resid = forms["exact"][lbl] + shift - forms["chain"][lbl]
        print(f"     {lbl:<4} tr_atom {fmt(ta, 18)}  tr_free {fmt(tf, 18)}   "
              f"B_sym^exact {fmt(forms['exact'][lbl], 12)}  +writhe {fmt(shift, 10)}  "
              f"B_sym^chain {fmt(forms['chain'][lbl], 12)}  |diff| {fmt(abs(resid), 3)}   "
              f"B_can0 {fmt(forms['can0'][lbl], 10)}   [{time.time() - t0:.1f}s]")
        check(f"chain == exact trace + writhe shift at {lbl}", abs(resid) < mp.mpf("1e-30"),
              fmt(abs(resid), 3))
    wb.add_data("traces_proton_q0_convention_D", {
        lbl: {"tr_atom": fmt(ta, 50), "tr_free": fmt(tf, 50)} for lbl, (ta, tf) in traces.items()})
    wb.add_data("bindings_MeV", {
        form: {lbl: fmt(v) for lbl, v in d.items()} for form, d in forms.items()})

    print("\n   Z-resolved b_3 = B(Z,N) - 3 B(1,1), per form (MeV):")
    print(f"     {'form':<8} {'b3(3H)':>12} {'b3(3He)':>12} {'split':>12}   "
          f"AME  b3(3H) {fmt(mpf_of_frac(b3_ame['3H']) / 1000, 8)}  "
          f"b3(3He) {fmt(mpf_of_frac(b3_ame['3He']) / 1000, 8)}  "
          f"split {fmt(mpf_of_frac(split_ame) / 1000, 8)}")
    b3_fw = {}
    for form, d in forms.items():
        t3h = d["3H"] - 3 * d["2H"]
        t3he = d["3He"] - 3 * d["2H"]
        b3_fw[form] = (t3h, t3he, t3h - t3he)
        print(f"     {form:<8} {fmt(t3h, 10):>12} {fmt(t3he, 10):>12} {fmt(t3h - t3he, 10):>12}")
    wb.add_data("z_resolved_b3_MeV", {
        form: {"3H": fmt(v[0]), "3He": fmt(v[1]), "split": fmt(v[2]),
               "residual_3H_MeV": fmt(v[0] - mpf_of_frac(b3_ame["3H"]) / 1000),
               "residual_3He_MeV": fmt(v[1] - mpf_of_frac(b3_ame["3He"]) / 1000)}
        for form, v in b3_fw.items()})
    all_neg = all(v[0] < 0 and v[1] < 0 for v in b3_fw.values())
    check("framework b_3 is NEGATIVE on every form for both nuclides (AME: positive)",
          all_neg)
    wb.add_assertion(
        name="framework_z_resolved_b3_negative_on_every_form", computed=str(int(all_neg)),
        expected="1", tolerance="0", unit="boolean",
        source="chain, exact trace and B_can0 all give b_3 < 0 at 3H and 3He; "
               "AME gives +1.808 and +1.044 MeV. The pairwise wall in Z-resolved form.")

    # ------------------------------------------------------------- 3. the split
    print("\n3. The mirror split -- deuteron term cancels; chain gives b_nn - b_pp")
    split_chain = b["nn"] - b["pp"]
    closed = alpha * mp.log(q0 ** 3 * (1 + q0 - q0 ** 2))
    h = q0 - 1 / q0
    z = q0 ** 3 / (q0 ** 2 + 1)
    check("identity z - h == 1/(q(q^2+1))", abs((z - h) - 1 / (q0 * (q0 ** 2 + 1))) < mp.mpf("1e-55"))
    check("chain split == alpha*ln(q_0^3 (1+q_0-q_0^2)) (closed form, 60 dps)",
          abs(split_chain - closed) < mp.mpf("1e-45"), fmt(abs(split_chain - closed), 3))
    split_ame_mev = mpf_of_frac(split_ame) / 1000
    sig_split_mev = sig_split / 1000
    rel = split_chain / split_ame_mev - 1
    nsig = (split_chain - split_ame_mev) / sig_split_mev
    print(f"     chain / closed form   {fmt(split_chain, 12)} MeV")
    print(f"     AME                   {fmt(split_ame_mev, 12)} MeV  (sigma {fmt(sig_split_mev, 4)})")
    print(f"     residual              {fmt(split_chain - split_ame_mev, 6)} MeV = "
          f"{fmt(rel * 100, 4)} %  =  {fmt(nsig, 5)} sigma_exp")
    print(f"     exact trace, un-normalised: {fmt(b3_fw['exact'][2], 10)} MeV "
          f"({fmt(b3_fw['exact'][2] / split_ame_mev, 4)}x);  "
          f"writhe factor alpha*ln(1-h) = {fmt(alpha * mp.log(1 - h), 8)} MeV")
    print(f"     B_can0:                     {fmt(b3_fw['can0'][2], 10)} MeV  (wrong sign)")
    wb.add_data("mirror_split_A3", {
        "chain_MeV": fmt(split_chain), "closed_form_MeV": fmt(closed),
        "closed_form": "alpha * ln(q0^3 * (1 + q0 - q0^2)), alpha = m_e/(q0(q0-1))",
        "AME_MeV": fmt(split_ame_mev), "AME_sigma_MeV": fmt(sig_split_mev),
        "residual_MeV": fmt(split_chain - split_ame_mev), "residual_rel": fmt(rel),
        "residual_sigma_exp": fmt(nsig),
        "exact_trace_unnormalised_MeV": fmt(b3_fw["exact"][2]),
        "writhe_factor_MeV": fmt(alpha * mp.log(1 - h)),
        "B_can0_MeV": fmt(b3_fw["can0"][2])})
    wb.add_assertion(
        name="chain_split_matches_AME_to_0_2_percent", computed=fmt(rel),
        expected="0.00205", tolerance="0.0001", unit="relative",
        source="b_nn - b_pp = 0.7653202 vs AME 0.7637549 MeV; +1.565 keV; the "
               "writhe factor supplies -0.982 MeV of it, without which it is 2.29x")
    check("split residual is +0.20 %", abs(rel - mp.mpf("0.00205")) < mp.mpf("0.0001"), fmt(rel, 5))
    check("and it is > 1000 sigma_exp -- not an L2 match", nsig > 1000, fmt(nsig, 5))
    check("B_can0 split has the WRONG sign (3He more bound)", b3_fw["can0"][2] < 0,
          fmt(b3_fw["can0"][2], 6))

    # ------------------------------------------------------ 4. the split beyond A=3
    print("\n4. The same split at the next mirror pairs -- the chain is Z-independent")
    rows = {}
    for lbl, (Z1, N1), (Z2, N2) in MIRROR_PAIRS:
        chain = ((max(Z1 - 1, 0) - max(Z2 - 1, 0)) * b["pp"]
                 + (max(N1 - 1, 0) - max(N2 - 1, 0)) * b["nn"])
        ame = mpf_of_frac(B_keV(Z1, N1) - B_keV(Z2, N2)) / 1000
        rows[lbl] = (chain, ame, chain / ame)
        extra = ""
        if Z1 + N1 == 7:
            ta1, tf1, _, _ = tr_m_atom_zn(Z1, N1, dps=50)
            ta2, tf2, _, _ = tr_m_atom_zn(Z2, N2, dps=50)
            ex = alpha * (mp.log(tf1 / ta1) - mp.log(tf2 / ta2))
            rows[lbl] = (chain, ame, chain / ame, ex)
            extra = f"   exact trace (un-normalised) {fmt(ex, 8)} MeV"
        print(f"     {lbl:<8} chain {fmt(chain, 10)}   AME {fmt(ame, 10)}   "
              f"ratio {fmt(chain / ame, 5)}{extra}")
    check("chain split is the SAME constant at all three pairs",
          all(abs(r[0] - split_chain) < mp.mpf("1e-40") for r in rows.values()))
    check("AME split grows: 7Li/7Be > 2x and 13C/13N > 3.9x the A=3 value",
          rows["7Li/7Be"][1] / rows["3H/3He"][1] > 2 and rows["13C/13N"][1] / rows["3H/3He"][1] > mp.mpf("3.9"),
          f"{fmt(rows['7Li/7Be'][1] / rows['3H/3He'][1], 4)}x, {fmt(rows['13C/13N'][1] / rows['3H/3He'][1], 4)}x")
    wb.add_data("mirror_split_by_pair_MeV", {
        lbl: {"chain": fmt(r[0]), "AME": fmt(r[1]), "ratio": fmt(r[2]),
              **({"exact_trace_unnormalised": fmt(r[3])} if len(r) > 3 else {})}
        for lbl, r in rows.items()})
    wb.add_assertion(
        name="chain_split_is_z_independent_and_short_at_A7_A13",
        computed=fmt(rows["13C/13N"][2]), expected="0.2549", tolerance="0.001",
        unit="framework/AME at 13C/13N",
        source="b_nn - b_pp for every (Z,Z+1)/(Z+1,Z) pair; AME 0.764 / 1.644 / 3.003 MeV")
    check("13C/13N ratio is 0.255", abs(rows["13C/13N"][2] - mp.mpf("0.2549")) < mp.mpf("0.001"),
          fmt(rows["13C/13N"][2], 5))

    # ------------------------------------------------------------------ verdict
    ok = all(CHECKS)
    print("\n" + "=" * 78)
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks pass")
    print("=" * 78)
    print("""
VERDICT (scope (a) -- nothing refuted, no ingredient excluded):

  The Z-resolved construction exists in the corpus already, costs 0.1 s per
  A=3 word, and has the ~6 digits #7005 inferred (measured: 6.08 / 5.91 on the
  two b_3, 5.88 on their difference).

  What it finds: the framework's Z-resolved b_3 is NEGATIVE on every form,
  against +1.808 / +1.044 MeV.  Resolving Z does not touch the pairwise wall --
  each form is pairwise-additive, so its "b_3" is the bond-heterogeneity term
  b_XX - 2 b_pn, not a connected 3-body cumulant.

  The one thing that lands is the A=3 SPLIT: b_nn - b_pp =
  alpha*ln(q_0^3 (1+q_0-q_0^2)) = 0.7653 vs 0.7638 MeV (+0.20 %), from q_0 and
  m_e alone.  But that constant is the same at every mirror pair and the data
  are not: 2.15x short at 7Li/7Be, 3.93x at 13C/13N.  A coincidence at one
  pair, already noted in `coulomb_mirror_killswitch_probe`, not a mechanism.

  What the Z-resolution buys is a separation: the A-only b_3 mixes the mirror
  bond difference (framework: predicted; data: Coulomb) with the connected
  3-body term (framework: <= 0; data: > 0).  The second is the open object,
  and it is now visible on its own.
""")
    wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR,
             "q0AnchorReason": "every trace and bond constant is evaluated at "
                               "q_parameter.Q_50_DIGIT_STR (proton pin, owner "
                               "directive 2026-08-07); no muon value is read"})
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
