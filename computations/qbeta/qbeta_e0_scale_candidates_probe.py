#!/usr/bin/env python3
"""The binding scale E_0 and the factor 2.656: enumerate every derived candidate,
and separate what a scale CAN explain from what only the bond factors can.

Bean `qou-v8ct` (parent `qou-vyvt`); decision frame
`docs/audits/2026-09-04-binding-law-options-decision-frame.md` §5 avenue 1 / §7.1;
arc synthesis `docs/audits/2026-09-05-binding-law-arc-synthesis.md` §4-§6.
Lean: `QOU/Hecke/BindingScaleCandidates.lean` (sorry-free, generic field where
possible).

*** THE QUESTION ***

The adopted additive law (Option B, owner ruling 2026-09-04) is

    B(Z,N) = E_0 . S(Z,N),   S = log(tr_M(free)/tr_M(atom))
                              = (Z-1)(-ln b_pp) + (-ln b_pn) + (N-1)(-ln b_nn)

with E_0 = m_e/(q0(q0-1)) = 4.186 MeV derived (`rem:energy-scale-planck`), and
E_0^full = E_0/(1-hbar_q^2) = 4.227 MeV ruled 2026-09-05. The best SINGLE scale
over the 2548 measured AME2020 nuclides is 11.119 MeV, 2.656x E_0. Is that a
SCALE defect (the volume->energy conversion is wrong) or does it belong to the
BOND FACTORS (the dimensionless S is wrong)?

*** WHAT THIS PROBE DOES, AND DOES NOT ***

1. Enumerates every candidate for the conversion the corpus DERIVES, states what
   each derives from (block / Lean / witness / registry), and evaluates it at the
   proton pin at 70 dps. The column "ratio to 11.119" is a DIAGNOSTIC and is
   never used to rank, select, or assert anything. No candidate is adopted.

2. Measures the separation. The Lean proves (§3) that the fitted "best scale" is
   exactly `E_0 . exp(mean ln r_i)` with `r_i = B_i/(E_0 S_i)` the per-nuclide
   residual, and (§4) that rescaling cannot change any RATIO r_i/r_j. So the
   residual splits, exactly and without a model, into

       ln r_i  =  mu  +  eps_i,      mu = mean ln r  (the only part a scale can touch)
                                      eps_i          (untouchable by any E)

   and the probe reports the size of each, the range of the single-nuclide best
   scale (0.32x (6H) .. 3.26x (4He) E_0), the drift of mu across mass bands (the target is
   SAMPLE-DEPENDENT), and the variation of r along isotope chains at FIXED Z,
   which is bond-factor content by construction.

3. Prunes the candidate class structurally: [2]_q, z_D and 1/(q^2+1) are the
   bond factors themselves (b_pp = q^2/[2]_q, b_nn = q^-2/[2]_q, Lean §2), so a
   scale carrying any of them double-counts. The dimensionful part is one anchor
   (m_e) times a function of the Planck-unit constants (c_q, hbar_q), and the
   ratio of any two candidates is m_e-free (Lean §1, §4).

*** WHAT IT FINDS (measured 2026-09-08 at the proton pin, 70 dps) ***

- Exactly two candidates carry a corpus derivation that assigns them to the
  BINDING scale: E_0 (rem:energy-scale-planck) and E_0^full (owner ruling). The
  ratio between them is q^2/(2q-1) = 1.00991, m_e-free. Everything else is
  either (i) bond content already inside S, (ii) a rung of the hbar_q ladder
  with no block assigning it to binding, or (iii) a recorded negative (LP dual).
  Both carriers sit > 2x from 11.119, so the 2.656 is not a truncation-order
  question.
- The log-residual ln r_i = mu + eps_i over 2548 measured nuclides splits as
  n mu^2 = 2431.7 against sum eps^2 = 34.4: a CONSTANT factor accounts for
  98.6 % of the squared log-residual, and the shape is 1.4 % (RMS eps = 0.116,
  i.e. +-12 %). So in FORM the defect is overwhelmingly uniform.
- But a uniform factor is exactly what cannot be assigned: E.(c S) = (c E).S, so
  a scale defect and a uniform rescaling of all three bond energies are the
  SAME observable. What a measurement CAN assign is the non-uniform 12 %: the
  single-nuclide best scale runs 0.32 (6H) .. 3.26 (4He) x E_0, the band means
  drift 2.37 (A<40) .. 2.86 (40<=A<100) .. 2.41 (A>=240) -- the target is
  sample-dependent -- and along isotope chains at fixed Z the residual moves
  4.2 % (Pb) .. 17 % (Ca) .. 108 % (O), against a derived scale freedom of
  0.99 %. Every one of those is bond-factor content (Lean §4).
- Verdict, scope (a): the 2.656 is a constant to 1.4 % of the squared
  log-residual, and a constant is indistinguishable between "scale" and
  "uniform bond-factor deficit" at fixed law. It can only be assigned by a
  DERIVATION of a uniform factor, and the corpus holds none with a carrier:
  the tower gives 1.0099, the strand count 3 has no realisable mechanism
  (qou-0c19), and no other enumerated candidate has a block behind it. The
  fitted 11.119 is exp(mean ln r_i) . E_0 -- a sample statistic that moves
  with the sample -- so no derived constant can be "checked against" it
  without first fixing the shape, which #7165 shows no pair-additive bond
  count can do. The bean stays open.

Anti-fit (AGENTS.md §NO FITTING): nothing here is tuned, no candidate is
selected by proximity, and the 11.119 is reproduced only to check the
geometric-mean identity the Lean states. NO-FLOAT64: AME values are parsed with
`parse_float=str`; every arithmetic step is mpmath at COMPUTE_DPS.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(ROOT / "computations"))

from _witness_q0_stamp import stamp_q0  # noqa: E402
from qou_substrate import constants as C  # noqa: E402
from qou_substrate.codata import value_str  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS, OUTPUT_DPS, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = COMPUTE_DPS

Q0 = mp.mpf(C.Q_50_DIGIT_STR)                       # proton pin, 50 digits
M_E = mp.mpf(value_str("electron mass energy equivalent in MeV"))
MU_E = mp.mpf(C.MASS_RATIO_MU_E_STR)                # CODATA 2022, diagnostic only
VOL41 = 2 * mp.clsin(2, mp.pi / 3)                  # Vol(4_1) = 2 Cl_2(pi/3)
BEST_SINGLE_SCALE_RECORDED = mp.mpf("11.119")       # decision frame §2B (diagnostic)

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"
LP_DUAL_WITNESS = ROOT / "computations/e-0-lp-dual-h3.witness.json"

# --- substrate constants (rem:energy-scale-planck) ----------------------------
C_Q = 1 / (Q0 - 1)
HBAR_Q = (Q0 - 1) / Q0
TWO_Q = Q0 + 1 / Q0
THREE_Q = Q0**2 + 1 + Q0**-2
Z_D = Q0**3 / (Q0**2 + 1)
H_SKEIN = Q0 - 1 / Q0

# --- the closed-form bond factors (qbeta_bond_factors_derived_probe.py) --------
B_PP = Q0**3 / (Q0**2 + 1)
B_NN = 1 / (Q0**3 + Q0)
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1) / (12*Q0**5*(Q0**2 + 1)))
L_PP, L_PN, L_NN = -mp.log(B_PP), -mp.log(B_PN), -mp.log(B_NN)

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
E0_FULL = E0 / (1 - HBAR_Q**2)


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def bond_sum(Z: int, N: int):
    """`S = log(tr_free/tr_atom)` for Z, N >= 1 -- the dimensionless bond sum."""
    return (Z - 1) * L_PP + L_PN + (N - 1) * L_NN


def _geo(vals):
    return mp.exp(sum(mp.log(v) for v in vals) / len(vals))


def _pct(vals, num: int, den: int = 100):
    v = sorted(vals)
    return v[min(len(v) - 1, len(v) * num // den)]


def candidates():
    """Every DERIVED conversion candidate in the corpus. `carrier` says whether a
    block/ruling assigns the quantity to the BINDING scale; `where` is the
    citation; `class` sorts it into scale / bond-content / ladder-rung / negative.
    """
    y0 = None
    if LP_DUAL_WITNESS.exists():
        w = json.loads(LP_DUAL_WITNESS.read_text(), parse_float=str)
        try:
            y0 = mp.mpf(w["data"]["results_per_target_cone"]["proton_net"]["y_0_star_str"])
        except KeyError:
            y0 = None
    q = Q0
    rows = [
        # ---- scale candidates with a binding carrier -------------------------
        dict(key="E0_N0", formula="m_e/(q(q-1)) = m_e c_q^2 hbar_q", value=E0,
             cls="scale", carrier=True,
             where="rem:energy-scale-planck (nuclear-interactions/energy-scale-planck.md); "
                   "Lean BindingScaleCandidates.E0_eq_planck; binding_log_free_energy.py"),
        dict(key="E0_full", formula="E0/(1-hbar_q^2) = m_e q/((q-1)(2q-1))", value=E0_FULL,
             cls="scale", carrier=True,
             where="owner ruling 2026-09-05 (qou-qkbp); Lean E0full_closed, E0full_eq_E0_mul_tsum"),
        # ---- bond content: already inside S (Lean §2) -------------------------
        dict(key="E0_abs_ln_zD", formula="E0 |ln z_D|  (per p-p bond, Markov weight)",
             value=E0 * abs(mp.log(Z_D)), cls="bond-content", carrier=False,
             where="decision frame §7.1; b_pp = z_D is a derived identity, so this is "
                   "E0 . L_pp -- the p-p term of S, not a scale"),
        dict(key="E0_ln_two_q", formula="E0 ln[2]_q  (per strand, pinned loop value)",
             value=E0 * mp.log(TWO_Q), cls="bond-content", carrier=False,
             where="qou-xf14; Lean neg_log_fPP_add_neg_log_fNN: (L_pp+L_nn)/2 = ln[2]_q"),
        dict(key="three_E0_ln_two_q", formula="3 E0 ln[2]_q  (per nucleon, 3 strands)",
             value=3 * E0 * mp.log(TWO_Q), cls="bond-content", carrier=False,
             where="qou-qkbp; the 3 is put in by hand and its colour-tube mechanism is "
                   "unrealisable (qou-0c19, QOU/Hecke/LayoutConflict.lean)"),
        dict(key="three_E0full_ln_two_q", formula="3 E0_full ln[2]_q",
             value=3 * E0_FULL * mp.log(TWO_Q), cls="bond-content", carrier=False,
             where="qou-qkbp (same caveat)"),
        dict(key="E0_over_q2p1", formula="E0/(q^2+1)  (crossing weight)",
             value=E0 / (q**2 + 1), cls="bond-content", carrier=False,
             where="1/(q^2+1) is the denominator of z_D and of b_pp -- inside S"),
        dict(key="E0_two_q", formula="E0 [2]_q",
             value=E0 * TWO_Q, cls="bond-content", carrier=False,
             where="[2]_q is the loop value inside b_pp, b_nn (Lean fPP_eq_sq_div_quantumTwo)"),
        dict(key="E0_FBor_dressing", formula="E0 [3]_q!/q^3  (F_Bor dressing)",
             value=E0 * TWO_Q * THREE_Q / q**3, cls="ladder-rung", carrier=False,
             where="[3]_q!/q^3 dresses the MUON anchor in the proton-mass chain "
                   "(constants.py::q_at); no block assigns it to binding"),
        # ---- hbar_q ladder rungs: dimensional combinations, no binding carrier -
        dict(key="m_e", formula="m_e  (bare CAL-1)", value=M_E, cls="ladder-rung",
             carrier=False, where="used by three qou-59j5 probes; NOT in E_0_CONVENTIONS "
                                  "(derivation_chain.py) -- no operator class"),
        dict(key="m_e_over_hbar", formula="m_e/hbar_q = m_e q/(q-1)", value=M_E / HBAR_Q,
             cls="ladder-rung", carrier=False, where="hbar_q^-1 rung; no carrier"),
        dict(key="m_e_over_hbar_sq", formula="m_e/hbar_q^2 = m_e c_q^2 (q/(q-1))^2 -- mass prefactor",
             value=M_E / HBAR_Q**2, cls="ladder-rung", carrier=False,
             where="prefactor of m = m_e Vol rho/hbar_q^2; DEPRECATED for absolute mass "
                   "(AGENTS.md 2026-06-24), valid for ratios where it CANCELS"),
        dict(key="E0_over_hbar", formula="E0/hbar_q = m_e c_q^2", value=E0 / HBAR_Q,
             cls="ladder-rung", carrier=False, where="hbar_q^0 rung of the E0 ladder; "
                                                       "registry convention B is hbar_q^0 but is Q_beta, not this"),
        dict(key="m_mu", formula="m_e Vol(4_1)/hbar_q^2  (muon anchor)",
             value=M_E * VOL41 / HBAR_Q**2, cls="ladder-rung", carrier=False,
             where="CAL-2 proxy in the MASS chain (constants.py::q_muon_at); not binding"),
        dict(key="m_mu_hbar", formula="m_mu hbar_q = m_e Vol(4_1)/hbar_q",
             value=M_E * VOL41 / HBAR_Q, cls="ladder-rung", carrier=False,
             where="dimensional combination only -- NO block, Lean or witness assigns it "
                   "to anything. Listed so its diagnostic ratio is on record as "
                   "numerology, not as a lead"),
        # ---- registry conventions --------------------------------------------
        dict(key="Q_beta_closed", formula="m_e |q^2-2q-1|(q+1)/(2q^3)  (registry B, hbar_q^0)",
             value=M_E * abs(q**2 - 2*q - 1) * (q + 1) / (2 * q**3), cls="registry",
             carrier=False,
             where="derivation_chain.py E_0_CONVENTIONS['B']: scale of B = E0.|Delta tr| -- "
                   "the REFUTED multiplicative law; functional also scoped inadmissible "
                   "under convention D (AGENTS.md scoping note 2026-09-05)"),
        dict(key="LP_dual_y0_me", formula="y_0^* . m_e  (registry D, operator-selection LP dual)",
             value=(y0 * M_E) if y0 is not None else None, cls="negative", carrier=False,
             where="computations/e-0-lp-dual-h3.witness.json: y_0^* dimensionless; "
                   "recorded NEGATIVE ('does NOT derive E_0 in MeV')"),
    ]
    for r in rows:
        v = r["value"]
        r["ratio_to_E0"] = (v / E0) if v is not None else None
        r["ratio_to_11_119_DIAGNOSTIC"] = (v / BEST_SINGLE_SCALE_RECORDED) if v is not None else None
    return rows


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), "note": note})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    tol = mp.mpf(10) ** (-(OUTPUT_DPS - 5))

    print("=" * 78)
    print(f"0. IDENTITIES AT THE PROTON PIN (dps={COMPUTE_DPS})")
    print("=" * 78)
    print(f"  q0      = {fmt(Q0)}")
    print(f"  m_e     = {fmt(M_E)} MeV")
    print(f"  E_0     = {fmt(E0)} MeV")
    print(f"  E_0full = {fmt(E0_FULL)} MeV")
    ok &= chk("E0_equals_me_cq2_hbar", abs(E0 - M_E * C_Q**2 * HBAR_Q) < tol, True,
              "Lean E0_eq_planck")
    ok &= chk("E0full_closed_form", abs(E0_FULL - M_E * Q0 / ((Q0 - 1) * (2*Q0 - 1))) < tol, True,
              "Lean E0full_closed")
    ok &= chk("E0full_over_E0_is_q2_over_2qm1",
              abs(E0_FULL / E0 - Q0**2 / (2*Q0 - 1)) < tol, True,
              f"= {fmt(Q0**2/(2*Q0-1), 15)}; m_e-free (Lean E0full_div_E0)")
    ok &= chk("bpp_bnn_equals_inv_two_q_sq", abs(B_PP * B_NN - 1 / TWO_Q**2) < tol, True,
              "Lean fPP_mul_fNN")
    ok &= chk("bond_level_factor_is_inside_S",
              abs(L_PP + L_NN - 2 * mp.log(TWO_Q)) < tol, True,
              "L_pp + L_nn = 2 ln[2]_q: [2]_q is bond content, not a scale (Lean "
              "neg_log_fPP_add_neg_log_fNN)")
    ok &= chk("bnn_equals_zD_minus_h", abs(B_NN - (Z_D - H_SKEIN)) < tol, True,
              "Lean fNN_eq_markovZ_sub_heckeH")

    print("\n" + "=" * 78)
    print("1. THE CANDIDATE TABLE (ratio to 11.119 is DIAGNOSTIC ONLY)")
    print("=" * 78)
    rows = candidates()
    print(f"  {'key':24s} {'class':13s} {'carrier':7s} {'MeV':>16s} {'/E0':>10s} {'/11.119':>10s}")
    for r in rows:
        v = r["value"]
        print(f"  {r['key']:24s} {r['cls']:13s} {str(r['carrier']):7s} "
              f"{(mp.nstr(v, 12) if v is not None else 'n/a'):>16s} "
              f"{(mp.nstr(r['ratio_to_E0'], 8) if v is not None else 'n/a'):>10s} "
              f"{(mp.nstr(r['ratio_to_11_119_DIAGNOSTIC'], 8) if v is not None else 'n/a'):>10s}")
    n_carrier = sum(1 for r in rows if r["carrier"])
    ok &= chk("exactly_two_candidates_carry_a_binding_derivation", n_carrier, 2,
              "E0 (rem:energy-scale-planck) and E0_full (ruling 2026-09-05); all "
              "others are bond content, ladder rungs or recorded negatives")
    ok &= chk("no_carrier_candidate_lands_on_the_fitted_scale",
              all(abs(mp.log(r["ratio_to_11_119_DIAGNOSTIC"])) > mp.log(2)
                  for r in rows if r["carrier"]), True,
              "both derived scales are > 2x from 11.119: the 2.656 is not a "
              "truncation-order (1 %) question")

    print("\n" + "=" * 78)
    print("2. THE SEPARATION: what a scale can touch, and what it cannot")
    print("=" * 78)
    meas = []
    for e in json.loads(AME.read_text(), parse_float=str)["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        if Z < 1 or N < 1:
            continue
        bpa = e.get("binding_energy_per_A_keV")
        if not bpa or e.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(bpa) * A / 1000
        if B <= 0:
            continue
        meas.append((A, Z, N, B, bond_sum(Z, N), e.get("element")))
    n = len(meas)
    lnr = [mp.log(B / (E0 * S)) for (_, _, _, B, S, _) in meas]
    mu = sum(lnr) / n
    best = E0 * mp.exp(mu)
    ss_total = sum(x**2 for x in lnr)
    ss_const = n * mu**2
    ss_shape = sum((x - mu)**2 for x in lnr)
    print(f"  measured nuclides            n = {n}")
    print(f"  best single scale (geo mean) = {fmt(best, 15)} MeV = {fmt(mp.exp(mu), 10)} x E_0")
    print(f"  ln r decomposition: n mu^2 = {fmt(ss_const, 8)}   sum eps^2 = {fmt(ss_shape, 8)}"
          f"   shape share = {fmt(ss_shape/ss_total, 6)}")
    ok &= chk("best_scale_reproduces_recorded_11_119",
              abs(best / BEST_SINGLE_SCALE_RECORDED - 1) < mp.mpf("1e-3"), True,
              f"{fmt(best, 12)} MeV at 70 dps vs 11.119 recorded at 30 dps")
    ok &= chk("best_scale_is_E0_times_geomean_of_residuals",
              abs(best - E0 * _geo([B / (E0 * S) for (_, _, _, B, S, _) in meas])) < tol, True,
              "the identity Lean bestLogScale_eq_mean states; the fitted target IS a "
              "sample statistic of the residual")

    rs = [mp.exp(x) for x in lnr]
    rmin, rmax = min(rs), max(rs)
    imin, imax = rs.index(rmin), rs.index(rmax)
    print(f"  single-nuclide best scale ranges {fmt(rmin, 6)} x E_0 "
          f"({meas[imin][5]}-{meas[imin][0]}) .. {fmt(rmax, 6)} x E_0 ({meas[imax][5]}-{meas[imax][0]})")
    print(f"  scale-invariant spread: full {fmt(rmax/rmin, 6)} x, p5-p95 "
          f"{fmt(_pct(rs, 95)/_pct(rs, 5), 6)} x -- unchanged by ANY E (Lean §4)")
    ok &= chk("residual_is_not_constant_full_range_exceeds_2x", rmax / rmin > 2, True,
              "a pure scale defect would make r constant; it spans > 2x")

    bands = [("A<40", lambda A: A < 40), ("40<=A<100", lambda A: 40 <= A < 100),
             ("100<=A<240", lambda A: 100 <= A < 240), ("A>=240", lambda A: A >= 240)]
    band_mu = {}
    for name, pred in bands:
        sel = [x for (A, _, _, _, _, _), x in zip(meas, lnr) if pred(A)]
        band_mu[name] = (len(sel), mp.exp(sum(sel) / len(sel)))
        print(f"  band {name:11s} n={len(sel):4d}  best scale / E_0 = {fmt(band_mu[name][1], 6)}")
    nz = [x for (A, Z, N, _, _, _), x in zip(meas, lnr) if Z == N]
    band_mu["N=Z"] = (len(nz), mp.exp(sum(nz) / len(nz)))
    print(f"  band {'N=Z':11s} n={len(nz):4d}  best scale / E_0 = {fmt(band_mu['N=Z'][1], 6)}")
    bvals = [v for (_, v) in band_mu.values()]
    drift = max(bvals) / min(bvals)
    ok &= chk("fitted_target_is_sample_dependent_band_drift_exceeds_5pct",
              drift > mp.mpf("1.05"), True,
              f"band best-scales differ by {fmt(drift, 5)} x: the 11.119 depends on which "
              "nuclides are averaged, so it is a shape statistic")

    chains = {}
    for Zc in (8, 20, 28, 50, 82):
        ch = sorted([(N, mp.exp(x), A) for (A, Z, N, _, _, _), x in zip(meas, lnr) if Z == Zc])
        if len(ch) < 3:
            continue
        vals = [v for (_, v, _) in ch]
        chains[Zc] = {"n": len(ch), "N_range": [ch[0][0], ch[-1][0]],
                      "r_at_Nmin": ch[0][1], "r_at_Nmax": ch[-1][1],
                      "r_max_over_min": max(vals) / min(vals)}
        print(f"  Z={Zc:2d} chain: N {ch[0][0]}..{ch[-1][0]}  r = {fmt(ch[0][1], 5)} .. "
              f"{fmt(ch[-1][1], 5)}   max/min {fmt(max(vals)/min(vals), 5)}")
    scale_freedom = E0_FULL / E0     # the ENTIRE remaining derived scale freedom, 1.0099
    ok &= chk("chain_variation_at_fixed_Z_exceeds_the_derived_scale_freedom_on_every_chain",
              all(c["r_max_over_min"] > scale_freedom for c in chains.values()), True,
              f"at fixed Z only the n-n bond count changes; r moves 4-108 % along the "
              f"chains against a derived scale freedom of {fmt(scale_freedom, 6)} x -- "
              "bond-factor content, unreachable by a scale (Lean §4). The threshold is "
              "a DERIVED quantity (E0_full/E0), not a tolerance sized to the miss")

    # the ruled scale with the hand-inserted strand count, as a cross-check of qou-qkbp
    over = [(m[5], m[0], mp.exp(x) * E0 / (3 * E0_FULL)) for m, x in zip(meas, lnr)
            if mp.exp(x) * E0 / (3 * E0_FULL) > 1]
    print(f"  under 3.E0_full: {len(over)} of {n} nuclides exceed the bound "
          f"({', '.join(f'{el}-{A} {fmt(v, 5)}' for el, A, v in over)})")
    ok &= chk("ruled_scale_times_three_bounds_all_but_one", len(over), 1,
              "reproduces qou-qkbp (4He alone); the 3 is the strand count, not derived")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    print("\n  Verdict (scope (a), not (b)): at fixed law the residual has a constant part\n"
          "  mu that a scale COULD absorb and a varying part it CANNOT; but mu is the\n"
          "  sample mean of the shape defect, so no derived constant can be checked\n"
          "  against it until the shape is removed. Nothing here selects a candidate.")

    def _r(r):
        return {k: (fmt(v) if isinstance(v, mp.mpf) else v) for k, v in r.items()}

    witness = {
        "computation": "qbeta-e0-scale-candidates",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": fmt(Q0), "q0_anchor": "proton (Q_50_DIGIT_STR)",
                       "compute_dps": COMPUTE_DPS, "output_dps": OUTPUT_DPS,
                       "m_e_MeV": fmt(M_E), "m_mu_over_m_e_diagnostic_only": fmt(MU_E),
                       "Vol_4_1": fmt(VOL41),
                       "recorded_best_single_scale_MeV_DIAGNOSTIC": str(BEST_SINGLE_SCALE_RECORDED),
                       "ame_source": "qou-mass/src/qou_mass/data/ame2020.json (measured only)"},
        "data": {
            "E_0_N0_MeV": fmt(E0), "E_0_full_MeV": fmt(E0_FULL),
            "E_0_full_over_E_0": fmt(E0_FULL / E0),
            "bond_energies": {"L_pp": fmt(L_PP), "L_pn": fmt(L_PN), "L_nn": fmt(L_NN)},
            "candidates": [_r(r) for r in rows],
            "separation": {
                "n_measured": n,
                "best_single_scale_MeV": fmt(best),
                "best_over_E0": fmt(mp.exp(mu)),
                "ln_r_mean": fmt(mu),
                "ss_const_n_mu_sq": fmt(ss_const), "ss_shape": fmt(ss_shape),
                "shape_share_of_ss": fmt(ss_shape / ss_total),
                "r_min": fmt(rmin), "r_min_nuclide": f"{meas[imin][5]}-{meas[imin][0]}",
                "r_max": fmt(rmax), "r_max_nuclide": f"{meas[imax][5]}-{meas[imax][0]}",
                "spread_full": fmt(rmax / rmin),
                "spread_p5_p95": fmt(_pct(rs, 95) / _pct(rs, 5)),
                "band_best_over_E0": {k: {"n": v[0], "value": fmt(v[1])} for k, v in band_mu.items()},
                "band_drift": fmt(drift),
                "isotope_chains": {str(k): _r(v) for k, v in chains.items()},
                "over_bound_at_3_E0_full": [[el, A, fmt(v)] for el, A, v in over],
            },
        },
        "verdict": ("scope (a): the residual's varying part is bond-factor content by the "
                    "Lean scale-invariance; its constant part is a sample mean of the shape "
                    "defect and is not a derivation target at fixed law. No candidate selected."),
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_e0_scale_candidates_probe.py",
                       "lean": "folio/quantum-observable-universe/lean/QOU/Hecke/BindingScaleCandidates.lean",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    # Provenance + anchor stamps: this producer writes its witness directly, so
    # q0Anchor/q0Value (payload-evidence-first) and scriptFile/engine/commitSha
    # are stamped here, as the other hand-rolled qbeta probes do.
    witness["q0Anchor"] = "proton"
    witness["q0Value"] = C.Q_50_DIGIT_STR
    stamp_q0(witness, __file__)
    witness.setdefault("scriptFile", Path(__file__).name)
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="mpmath", q0_anchor=False)
    out = HERE / "qbeta-e0-scale-candidates.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
