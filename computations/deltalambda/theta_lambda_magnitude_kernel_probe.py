#!/usr/bin/env python3
"""
theta_lambda_magnitude_kernel_probe.py — derive-or-refute the A≥3 per-rep
θ_λ magnitude (the cheat-sheet 🔴 open gate) via the formalize-first
invariant, then one pre-named kernel probe.  NO fit, NO tuning.

# Ref: docs/audits/2026-07-13-theta-lambda-magnitude-derive-or-refute.md
# Ref: docs/audits/2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md
# Ref: docs/coordination/binding-scale-is-hyperbolic-volume.md
# Ref: docs/audits/2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md

HYPOTHESIS CLASS (stated per compute-author §3.3 step 1).  The binding
carrier is B = m_e · Σ_λ w_λ · 𝒜 · f(θ_λ) with f linear at leading order
(f(θ) = θ + O(θ³)), w_λ a fixed Markov weighting (w = y_λ or y_λ·dim_λ),
and 𝒜 the OPEN magnitude — either a single derived dimensionless
amplification (the "scalar-𝒜 sub-class") or a per-block 𝒜_λ (the
"kernel sub-class").  Known anchors (all corpus, no fit):
  • scalar-trace collapse:  B_D = m_e·Vol(𝓑₃)·Δtr        → +0.19 %
  • highest-weight j=n/2:   B_D = μ₀·ℏ_q·J_q²(3)          → −9 %
  • bare per-λ mirror:      m_e·Σ y_λ Δθ (³H−³He)  undershoots the
    0.7638 MeV split by a LARGE factor (audit quotes ~270×; shown below
    to be convention-dependent, 13×–662×).

INVARIANT I1 (formalize-first step 2 — cross-observable rigidity).
For the scalar-𝒜 sub-class, ONE derived number must satisfy ALL of
    𝒜 = B_AME(K) / (m_e · S_w(K))            for K ∈ {D, T, ³He, ⁴He}
    𝒜 = split_AME / (m_e · (S_w(³H) − S_w(³He)))   (mirror)
simultaneously, within the ±9 % inter-scheme truncation band (the gap
between the two proved collapse schemes — the honest error budget of the
linear-order carrier).  This is finite arithmetic on cached canonical
witnesses: if the required 𝒜's disperse beyond the band, the ENTIRE
scalar-𝒜 sub-class is refuted at once — including every "large derived
constant near 270" (1/ℏ_q², e^{Vol}/2π, [n]_q!, q₀-powers, F_Bor, …) —
without fitting or scanning.  (Scope-(a): as the sole magnitude for the
linear carrier; it constrains combinations, not ingredients.)

INVARIANT I2 (evaluation-level).  The Kashaev/volume-conjecture growth
e^{Vol·N/(2π)} is the |q| = 1 root-of-unity asymptotic of the colored
Jones (fibre level); the binding observable is evaluated at REAL q₀
(archimedean level).  Per the AGENTS.md Im(q) two-level rule these must
not be conflated: at real q₀ the large-rep growth is the q₀^{±writhe}
growth channel (already present in the arccosh channel of the Reeb
decomposition), and Vol enters only through the full-contraction
semiclassics (the +0.19 % route).  A per-λ kernel 𝒜_λ = e^{Vol·N_λ/(2π)}
therefore has NO structural warrant at q₀; the numeric probe below
documents the expected failure (cheap + decisive on cached data).

KERNEL PROBE (ONE candidate, pre-named, parameter-free).
  𝒜_λ = exp(Vol(K_bind) · N_λ / (2π)),   N_λ = λ₁ − λ₂ + 1
(the sl₂ color of the two-row quotient — the colored-Jones color the
volume conjecture actually quantifies; single-row λ = (n) has N = n+1).
Tested on BOTH the deuteron (must stay inside the +0.19 %/−9 % band)
and the A=3 mirror split.  No second shape is tried (no shape-probing).

ANTI-FIT (STRICT).  Numerically-close constants without a structural
tie to θ_λ are reported as GUARDED DATA (e.g. κ_D(y·dim) ≈ [3]_q! to
+1.3 %), never wired.  An AME/CODATA-inverted scale is a fit and is not
proposed.

Inputs: cached canonical witnesses only —
  binding-reeb-phase-decomposition.witness.json          (θ_λ vectors)
  chi-{deuteron,tritium,helium-3,helium-4}-h*-at-q0-50dps.witness.json (y_λ)
Emits: theta-lambda-magnitude-kernel-probe.witness.json
EXPLORATORY — audit-only witness; no production wiring.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate", _COMP / "hecke", _COMP / "habiro"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

q0 = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf(str(M_E_MEV))
HBAR_Q = 1 - 1 / q0
MU_0 = M_E / (3 * (q0 - 1 / q0) / 2)

B_AME = {
    "D":   mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
    "T":   mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
    "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
    "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION)),
}
SPLIT_AME = B_AME["T"] - B_AME["3He"]            # 0.7638 MeV mirror split

# Binding-link volumes (same registry + fallback as
# binding_a3plus_full_theta_assembly.py; D uses the 𝓑₃ substitution of the
# proved endomorphism route — the Hopf sub-link itself has Vol = 0).
try:
    from substrate.knot_volumes import VOL_BORROMEAN_MPF, VOL_8_11_MPF
    VOL_K = {"D": VOL_BORROMEAN_MPF, "T": VOL_8_11_MPF,
             "3He": VOL_BORROMEAN_MPF, "4He": 2 * VOL_BORROMEAN_MPF}
except ImportError:
    VOL_K = {"D": mp.mpf("7.3277248"), "T": mp.mpf("8.2863168"),
             "3He": mp.mpf("7.3277248"), "4He": mp.mpf("14.6554497")}

# The honest error budget of the linear-order carrier: the gap between the
# two PROVED collapse schemes of the same θ_λ (+0.19 % vs −9 %).
INTER_SCHEME_BAND = mp.mpf("0.09")

CHI_WITNESS = {
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def _load(name: str) -> dict:
    return json.loads((_COMP / name).read_text())


def _key(part) -> str:
    return "_".join(str(p) for p in part)


def load_atom(atom: str, reeb_per_atom: dict) -> list[dict]:
    """Merge θ_λ rows with y_λ; hard-error on any mismatch (no silent 0)."""
    chi = _load(CHI_WITNESS[atom])
    if chi.get("partial", False):
        raise RuntimeError(f"chi witness for {atom} is partial — regenerate")
    y_map = {_key(e["partition"]): mp.mpf(e["y_lambda"])
             for e in chi["by_partition"]}
    rows = []
    for r in reeb_per_atom[atom]["by_partition"]:
        k = _key(r["partition"])
        if k not in y_map:
            raise KeyError(f"{atom}: y_λ missing for partition {k}")
        th_a = mp.mpf(r["theta_atom_rad"])
        th_f = mp.mpf(r["theta_free_rad"])
        rows.append({
            "key": k,
            "partition": list(r["partition"]),
            "dim": int(r["dim"]),
            "y": y_map[k],
            "theta_atom": th_a,
            "theta_free": th_f,
            "abs_dtheta": abs(th_a - th_f),
        })
    return rows


def sum_w(rows: list[dict], weighting: str) -> mp.mpf:
    """Bare linear carrier Σ w_λ |Δθ_λ| under a fixed weighting."""
    if weighting == "y":
        return sum(r["y"] * r["abs_dtheta"] for r in rows)
    if weighting == "y_dim":
        return sum(r["y"] * r["dim"] * r["abs_dtheta"] for r in rows)
    raise ValueError(weighting)


def color_N(part: list[int]) -> int:
    """Pre-named sl₂ color of the two-row quotient: N = λ₁ − λ₂ + 1
    (single-row (n) → N = n + 1)."""
    lam1 = part[0]
    lam2 = part[1] if len(part) > 1 else 0
    return lam1 - lam2 + 1


def main() -> int:
    reeb = _load("binding-reeb-phase-decomposition.witness.json")["data"]["per_atom"]
    atoms = ["D", "T", "3He", "4He"]
    rows = {a: load_atom(a, reeb) for a in atoms}

    print("=" * 74)
    print(" θ_λ magnitude — derive-or-refute (formalize-first invariant + kernel)")
    print("=" * 74)
    print(f"  q₀ = {float(q0):.8f}   ℏ_q = {float(HBAR_Q):.8f}   "
          f"m_e = {float(M_E):.6f} MeV   μ₀ = {float(MU_0):.6f} MeV")

    # ── 1. Required amplifications κ per observable, per weighting ──────
    required: dict[str, dict[str, str]] = {}
    kappas: dict[str, dict[str, mp.mpf]] = {}
    for w in ("y", "y_dim"):
        S = {a: sum_w(rows[a], w) for a in atoms}
        kap = {a: B_AME[a] / (M_E * S[a]) for a in atoms}
        dS_mirror = S["T"] - S["3He"]
        kap["mirror"] = SPLIT_AME / (M_E * dS_mirror)
        kappas[w] = kap
        required[w] = {k: mp.nstr(v, 10) for k, v in kap.items()}
        required[w]["_S_bare"] = {a: mp.nstr(S[a], 10) for a in atoms}
        required[w]["_dS_mirror"] = mp.nstr(dS_mirror, 10)
        print(f"\n  required 𝒜 (weighting w = {w}):")
        for k in ["D", "T", "3He", "4He", "mirror"]:
            print(f"    {k:>7s}  𝒜_req = {float(kap[k]):>10.3f}")

    # ── 1b. The "~270×" convention family (mirror only, documentation) ──
    yT = {r["key"]: r for r in rows["T"]}
    yH = {r["key"]: r for r in rows["3He"]}
    fam = {}
    me = M_E
    v = sum(yT[k]["y"] * (yT[k]["theta_atom"] - yH[k]["theta_atom"]) for k in yT)
    fam["y*(theta_atom diff)"] = v
    v = sum(yT[k]["y"] * ((yT[k]["theta_atom"] - yT[k]["theta_free"])
                          - (yH[k]["theta_atom"] - yH[k]["theta_free"])) for k in yT)
    fam["y*(dtheta diff)"] = v
    v = sum(yT[k]["y"] * abs(yT[k]["theta_atom"] - yH[k]["theta_atom"]) for k in yT)
    fam["y*|theta_atom diff|"] = v
    v = sum(yT[k]["y"] * yT[k]["dim"] * (yT[k]["abs_dtheta"] - yH[k]["abs_dtheta"])
            for k in yT)
    fam["y*dim*(|dtheta| diff)"] = v
    mirror_family = {}
    print("\n  mirror bare-sum convention family (the '~270×' is one member):")
    for name, s in fam.items():
        amp = SPLIT_AME / abs(me * s)
        mirror_family[name] = {"m_e_S_MeV": mp.nstr(me * s, 8),
                               "amplification_needed": mp.nstr(amp, 8)}
        print(f"    {name:<26s} m_e·S = {float(me*s):+.6f} MeV   needs ×{float(amp):.1f}")

    # ── 2. INVARIANT I1 — uniform-𝒜 prune (cross-observable rigidity) ───
    prune = {}
    print("\n  I1 cross-observable rigidity (uniform derived 𝒜 must fit ALL):")
    for w in ("y", "y_dim"):
        vals = [kappas[w][k] for k in ["D", "T", "3He", "4He", "mirror"]]
        disp = max(vals) / min(vals)
        prune[w] = {"dispersion_max_over_min": mp.nstr(disp, 8),
                    "band_allowed": mp.nstr(1 + 2 * INTER_SCHEME_BAND, 4),
                    "uniform_class_refuted": bool(disp > 1 + 2 * INTER_SCHEME_BAND)}
        print(f"    w = {w:<6s}: dispersion max/min = {float(disp):8.2f}   "
              f"(band allows ≤ {float(1 + 2*INTER_SCHEME_BAND):.2f})  "
              f"→ {'REFUTED (scope-(a))' if prune[w]['uniform_class_refuted'] else 'compatible'}")

    # ── 3. Candidate table — derived constants vs required 𝒜's ─────────
    def qint(n: int) -> mp.mpf:
        return (q0 ** n - q0 ** (-n)) / (q0 - 1 / q0)

    def qfact(n: int) -> mp.mpf:
        out = mp.mpf(1)
        for i in range(2, n + 1):
            out *= qint(i)
        return out

    try:
        from m_p_substrate_identity_50dps import F_Bor
        f_bor = F_Bor(q0)
    except ImportError:
        f_bor = mp.mpf("4.4691387357675225")

    candidates = {
        "1/hbar_q":            (1 / HBAR_Q, "substrate q-Planck"),
        "1/hbar_q^2":          (1 / HBAR_Q ** 2, "muon-anchor c_q² (guardrail: belongs to Vol(4₁), not binding)"),
        "1/hbar_q^3":          (1 / HBAR_Q ** 3, "no tie to θ_λ"),
        "[3]_q!":              (qfact(3), "per-nucleon H₃ Poincaré factor (F_Bor normaliser)"),
        "[5]_q!":              (qfact(5), "no tie to θ_λ at H₉"),
        "mu_0/m_e":            (MU_0 / M_E, "per-crossing scale (derived)"),
        "F_Bor":               (f_bor, "Borromean Hecke factor (mass chain)"),
        "Vol(B3)":             (VOL_K["3He"], "hyperbolic volume (semiclassical contraction)"),
        "Vol(B3)/hbar_q":      (VOL_K["3He"] / HBAR_Q, "composite; no single-object tie"),
        "exp(Vol(B3))/2pi":    (mp.e ** VOL_K["3He"] / (2 * mp.pi), "Kashaev-like at NON-integer color (I2: no theorem at real q₀)"),
        "exp(Vol(8_11))/2pi":  (mp.e ** VOL_K["T"] / (2 * mp.pi), "same objection (I2)"),
        "exp(Vol(B3)/2pi)":    (mp.e ** (VOL_K["3He"] / (2 * mp.pi)), "per-color Kashaev growth rate (fibre level)"),
    }
    cand_table = {}
    n_match_all = 0
    print("\n  candidate table (match = within ±9 % of a required 𝒜, w = y_dim):")
    print(f"    {'candidate':<20s} {'value':>10s}   matches")
    targets = {k: kappas["y_dim"][k] for k in ["D", "T", "3He", "4He", "mirror"]}
    targets_y = {f"{k}(y)": kappas["y"][k] for k in ["D", "mirror"]}
    for name, (val, tie) in candidates.items():
        matches = [k for k, t in {**targets, **targets_y}.items()
                   if abs(val / t - 1) <= INTER_SCHEME_BAND]
        matches_all = all(abs(val / t - 1) <= INTER_SCHEME_BAND
                          for t in targets.values())
        n_match_all += int(matches_all)
        cand_table[name] = {"value": mp.nstr(val, 10), "structural_tie": tie,
                            "matches": matches, "matches_all_observables": matches_all}
        print(f"    {name:<20s} {float(val):>10.3f}   {matches if matches else '—'}")

    # Guarded datum (anti-fit): κ_D(y·dim) vs [3]_q!
    guard = abs(kappas["y_dim"]["D"] / qfact(3) - 1)
    print(f"\n  GUARDED DATUM: 𝒜_req(D, y·dim) = {float(kappas['y_dim']['D']):.4f} "
          f"vs [3]_q! = {float(qfact(3)):.4f}  (rel diff {float(guard)*100:.2f} %) — "
          f"single-observable near-match, breaks at A≥3; datum only, NOT a closure.")

    # ── 3b. GUARDED PATTERN — the required 𝒜 is GEOMETRIC in A ─────────
    # Derived directly from the κ table (no new inputs): per-added-nucleon
    # amplification ratios.  This is a genuine CONSTRAINT any derivation
    # must reproduce (𝒜 grows ~×3.2 per nucleon — exponential extensivity,
    # the same direction as the jet-filtration mechanism), but the
    # IDENTIFICATION of the ratio constant is degenerate at 4 data points
    # (π, [3]_q, μ₀/m_e, e^{Vol(𝓑₃)/2π} all sit inside the scatter) —
    # post-hoc shape selection, NUMEROLOGY-GUARDED, not a derivation.
    kd = kappas["y_dim"]
    A_of = {"D": 2, "T": 3, "3He": 3, "4He": 4}
    steps = {
        "T/D": kd["T"] / kd["D"],
        "3He/D": kd["3He"] / kd["D"],
        "4He/T": kd["4He"] / kd["T"],
        "4He/3He": kd["4He"] / kd["3He"],
    }
    ratio_candidates = {
        "pi": mp.pi,
        "[3]_q": qint(3),
        "mu_0/m_e": MU_0 / M_E,
        "exp(Vol(B3)/2pi)": mp.e ** (VOL_K["3He"] / (2 * mp.pi)),
    }
    print("\n  GUARDED PATTERN — per-added-nucleon amplification ratio (w = y·dim):")
    for k, v in steps.items():
        print(f"    𝒜({k}) = {float(v):.4f}")
    print("    degenerate identification candidates (all inside the ±3 % scatter):")
    for k, v in ratio_candidates.items():
        print(f"      {k:<18s} = {float(v):.4f}")
    # Composite guarded formula (post-hoc selection — DATUM ONLY):
    #   𝒜(A) = [3]_q! · (e^{Vol(𝓑₃)/2π})^{A−2}
    r_kash = mp.e ** (VOL_K["3He"] / (2 * mp.pi))
    composite = {}
    print("    composite GUARDED formula 𝒜(A) = [3]_q!·(e^{Vol(𝓑₃)/2π})^{A−2} "
          "(post-hoc selected — datum, NOT derived):")
    for a in atoms:
        pred = qfact(3) * r_kash ** (A_of[a] - 2)
        rel = pred / kd[a] - 1
        composite[a] = {"A": A_of[a], "pred": mp.nstr(pred, 8),
                        "required": mp.nstr(kd[a], 8), "rel_diff": mp.nstr(rel, 6)}
        print(f"      {a:>4s}  pred = {float(pred):>8.3f}   req = {float(kd[a]):>8.3f}"
              f"   ({float(rel)*100:+.2f} %)")
    # its mirror check (differences amplify the absolute residuals):
    split_comp = (qfact(3) * r_kash) * M_E * (sum_w(rows["T"], "y_dim")
                                              - sum_w(rows["3He"], "y_dim"))
    print(f"      mirror split pred = {float(split_comp):.4f} MeV vs "
          f"{float(SPLIT_AME):.4f}  ({float(split_comp/SPLIT_AME-1)*100:+.1f} %) — "
          f"the difference does NOT close; absolutes-only pattern.")
    composite["mirror"] = {"split_pred_MeV": mp.nstr(split_comp, 8),
                           "split_AME_MeV": mp.nstr(SPLIT_AME, 8),
                           "rel_diff": mp.nstr(split_comp / SPLIT_AME - 1, 6)}

    # ── 4. Kernel probe — Kashaev color kernel (pre-named, one shape) ───
    kernel_res = {}
    print("\n  kernel probe 𝒜_λ = exp(Vol·N_λ/2π), N_λ = λ₁−λ₂+1  (w = y·dim):")
    for a in atoms:
        V = VOL_K[a]
        Sk = sum(r["y"] * r["dim"] * mp.e ** (V * color_N(r["partition"]) / (2 * mp.pi))
                 * r["abs_dtheta"] for r in rows[a])
        B_pred = M_E * Sk
        rel = (B_pred - B_AME[a]) / B_AME[a]
        kernel_res[a] = {"B_pred_MeV": mp.nstr(B_pred, 10),
                         "B_AME_MeV": mp.nstr(B_AME[a], 10),
                         "rel_err": mp.nstr(rel, 8)}
        print(f"    {a:>4s}  B_pred = {float(B_pred):>14.3f} MeV   "
              f"B_AME = {float(B_AME[a]):>8.3f}   rel = {float(rel)*100:+.1f} %")
    # mirror under the kernel
    SkT = sum(r["y"] * r["dim"] * mp.e ** (VOL_K['T'] * color_N(r["partition"]) / (2 * mp.pi))
              * r["abs_dtheta"] for r in rows["T"])
    SkH = sum(r["y"] * r["dim"] * mp.e ** (VOL_K['3He'] * color_N(r["partition"]) / (2 * mp.pi))
              * r["abs_dtheta"] for r in rows["3He"])
    mir_pred = M_E * (SkT - SkH)
    kernel_res["mirror"] = {"split_pred_MeV": mp.nstr(mir_pred, 10),
                            "split_AME_MeV": mp.nstr(SPLIT_AME, 10),
                            "rel_err": mp.nstr((mir_pred - SPLIT_AME) / SPLIT_AME, 8)}
    print(f"    mirror  split_pred = {float(mir_pred):>10.3f} MeV   "
          f"AME = {float(SPLIT_AME):.4f}   rel = {float((mir_pred-SPLIT_AME)/SPLIT_AME)*100:+.1f} %")
    d_rel = abs(mp.mpf(kernel_res["D"]["rel_err"]))
    kernel_refuted = bool(d_rel > INTER_SCHEME_BAND)
    print(f"    → deuteron consistency band ±9 %: "
          f"{'VIOLATED — kernel refuted (scope-(a))' if kernel_refuted else 'inside band'}")

    # ── witness ─────────────────────────────────────────────────────────
    wb = WitnessBuilder("theta-lambda-magnitude-kernel-probe", engine="mpmath")
    wb.set_description(
        "Derive-or-refute the A≥3 per-rep θ_λ magnitude (cheat-sheet 🔴 gate). "
        "Formalize-first: (I1) cross-observable rigidity — the required "
        "dimensionless amplification 𝒜 = B/(m_e·Σ w_λ|Δθ_λ|) is computed for "
        "D/T/³He/⁴He + the ³H−³He mirror under two fixed Markov weightings; "
        "its dispersion (~10×) refutes the ENTIRE scalar-𝒜 sub-class (any "
        "single derived constant: 1/ℏ_q², e^{Vol}/2π, [n]_q!, F_Bor, …) at "
        "once, scope-(a). The '~270×' mirror undershoot is shown to be "
        "convention-dependent (13×–662×), so 'find a derived 270' is "
        "ill-posed. (I2) evaluation-level: the Kashaev growth e^{Vol·N/2π} "
        "is a |q|=1 fibre asymptotic, not a real-q₀ observable growth; the "
        "pre-named per-color kernel 𝒜_λ = e^{Vol·N_λ/2π} (N_λ = λ₁−λ₂+1) is "
        "probed anyway on cached data and fails the deuteron ±9 % "
        "inter-scheme band. Guarded datum: 𝒜_req(D, y·dim) ≈ [3]_q! (+1.3 %), "
        "single-point, not a closure. NO fit; no production wiring."
    )
    wb.add_data("substrate", {"q_0": mp.nstr(q0, 30), "hbar_q": mp.nstr(HBAR_Q, 30),
                              "m_e_MeV": mp.nstr(M_E, 15), "mu_0_MeV": mp.nstr(MU_0, 15),
                              "inter_scheme_band": "0.09 (the +0.19%/−9% collapse gap)"})
    wb.add_data("required_amplifications", required)
    wb.add_data("mirror_convention_family", mirror_family)
    wb.add_data("invariant_I1_uniform_scale_prune", prune)
    wb.add_data("candidate_table", cand_table)
    wb.add_data("guarded_datum_kappaD_vs_q3fact",
                {"kappa_D_y_dim": mp.nstr(kappas["y_dim"]["D"], 10),
                 "q3_factorial": mp.nstr(qfact(3), 10),
                 "rel_diff": mp.nstr(guard, 6),
                 "status": "datum only — single observable, breaks at A≥3"})
    wb.add_data("kashaev_color_kernel_probe", kernel_res)
    wb.add_data("volumes", {k: mp.nstr(v, 15) for k, v in VOL_K.items()})
    wb.add_data("guarded_pattern_geometric_in_A", {
        "per_step_ratios": {k: mp.nstr(v, 8) for k, v in steps.items()},
        "ratio_identification_candidates":
            {k: mp.nstr(v, 8) for k, v in ratio_candidates.items()},
        "composite_guarded_formula_q3fact_times_kashaev_rate_pow_Aminus2": composite,
        "status": ("GUARDED DATUM — post-hoc shape selection at 4 points with "
                   "degenerate ratio identification; a constraint on any future "
                   "derivation (𝒜 grows geometrically in A, ratio ≈ 3.2), NOT "
                   "a closure; the mirror difference does not close; "
                   "falsifiable next at A=6 (𝒜(⁶Li) ≈ 650 predicted)"),
    })

    wb.add_assertion(
        "deuteron_bare_kappa_reproduced",
        computed=float(kappas["y_dim"]["D"]),
        expected=6.0426, tolerance=0.01,
        source="B_D/(m_e·Σ y·dim·|Δθ|) from cached canonical witnesses "
               "(matches binding-a3plus-full-theta-assembly rho_need/m_e)")
    wb.add_assertion(
        "I1_uniform_scale_dispersion_y_dim",
        computed=float(mp.mpf(prune["y_dim"]["dispersion_max_over_min"])),
        expected=10.4, tolerance=1.0,
        source="max/min of required 𝒜 across {D,T,³He,⁴He,mirror}, w=y·dim — "
               "≫ 1.18 band ⇒ scalar-𝒜 sub-class refuted (scope-(a))")
    wb.add_assertion(
        "no_candidate_matches_all_observables",
        computed=n_match_all, expected=0, tolerance=0,
        source="none of the 12 enumerated derived constants sits within ±9 % "
               "of all five required 𝒜's (corollary of I1)")
    wb.add_assertion(
        "geometric_in_A_pattern_ratio_scatter",
        computed=float(max(steps.values()) / min(steps.values())),
        expected=1.06, tolerance=0.05,
        source="per-added-nucleon 𝒜 ratios (3.14–3.32) agree within ~6 % — "
               "the geometric-extensivity CONSTRAINT (guarded; identification "
               "of the ratio constant is degenerate)")
    wb.add_assertion(
        "kashaev_color_kernel_refuted_on_deuteron",
        computed=int(kernel_refuted), expected=1, tolerance=0,
        source="pre-named kernel e^{Vol·N_λ/2π} violates the deuteron "
               "+0.19%/−9% inter-scheme band (I2 predicted this: fibre-level "
               "growth applied at the real-q₀ observable level)")
    out = wb.save()
    print(f"\n  witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
