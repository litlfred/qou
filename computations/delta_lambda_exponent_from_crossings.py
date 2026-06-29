#!/usr/bin/env python3
"""delta_lambda_exponent_from_crossings.py
==========================================

Derive-or-refute: where does the Δ_λ q₀-exponent **10A−5 = 5(2A−1)** come from?
(`docs/audits/2026-06-09-delta-lambda-canonical-residual.md` named the admissible
non-fit next step: "categorical derivation of 10A−5 from crossing/jet bookkeeping
of W_free vs W_atom".)

## CLOSED-FORM crossing counts of `atom_braid_word_3A(Z,N)` (derived, verified)

The construction is: per nucleon, intra-𝓑₃ crossings (proton 6σ/2avg/3σ⁻¹,
neutron 5σ/2avg/4σ⁻¹ — both **9 non-averaged**), then one typed interface per
adjacent pair in the ordering `[p×Z, n×N]`: **p-p → σ (Z−1 of them), n-n → σ⁻¹
(N−1), p-n → color-averaged (1)**. Hence, exactly:

    σ        = (6Z+5N) + (Z−1)  = 7Z + 5N − 1
    σ⁻¹      = (3Z+4N) + (N−1)  = 3Z + 5N − 1
    averaged = (2Z+2N) + 1      = 2A + 1            (bar-symmetric d=−h/2)
    ─────────────────────────────────────────
    σ + σ⁻¹  = 10A − 2     ← Z,N CANCEL ⇒ A-only ⇒ the exponent is A-only
    writhe   = σ − σ⁻¹ = 4Z                         (proton-number only)

The color-averaged crossings carry `d = −h/2 = (σ+σ⁻¹)/2`, **bar-symmetric
(q↔q⁻¹) ⇒ 0 net q-power**, so only `σ+σ⁻¹` enters the q₀-exponent:

    10A − 5 = (σ + σ⁻¹) − 3,            A ≥ 2.

So the **exponent SLOPE 10 = 9 (intra-𝓑₃ non-averaged) + 1 (interface),
derived not fitted**; and it is A-only precisely because the Z,N dependence
cancels in `σ+σ⁻¹`. (T and ³He share `σ+σ⁻¹ = 28` ⇒ identical leading exponent
25, as `q₀^(10A−5)` demands.)

## The proton-excess Z-correction — SOURCE derived

`Z − N = (p-p interfaces) − (n-n interfaces) = (Z−1) − (N−1)`. p-p interfaces are
**σ** (positive, d=0), n-n are **σ⁻¹** (negative, d=−h), so a proton excess makes
the interface chirality net-σ (writhe = 4Z). The deviation from the integer law
tracks this proton excess (Z−N): D=0, T=−1, ³He=+1 (the −1.40 outlier), ⁴He=0.
Open: the coefficient and the p/n asymmetry (proton excess is penalised, neutron
excess is not) require the intra p≠n split (proton 6σ/3σ⁻¹ vs neutron 5σ/4σ⁻¹).

## Testable prediction — RAN, and the 10A−5 law is REFUTED at A≥5 (scope-(a))

The crossing closed form predicted the Δ_λ q₀-exponent ⁶Li → 55, ⁸Be → 75 (i.e.
`Δ_λ ≈ q₀^(10A−5)` continues). **That decisive test has now RUN**
(`delta_lambda_z_coefficient_and_slope.py`, ⁶Li/⁷Li/⁷Be added to
`binding_canonical.py`) and the prediction is **FALSIFIED**: ⁶Li gives
`log_{q₀}Δ_λ = 36.1`, not 55. The slope is ≈10/nucleon only for A≤4 and
collapses to ≈0.4/nucleon at the ⁴He shell. This is a SCOPE-LIMITED negative
(AGENTS.md "refuted" discipline (a)): the crossing-SUM closed forms below remain
exact arithmetic, but their reading as a *global* binding-exponent law does NOT
continue past A=4 — `B_pred` saturates while `B_AME` grows ~linearly, so
`log Δ_λ` is logarithmic, not linear. The crossing counts are not excluded; only
the global 10A−5 extrapolation is.

## The −3 offset dissolves under the chain-SITE reading

The exponent is more naturally `5·(2A−1)`, and **`2A−1 = A nucleons + (A−1)
inter-nucleon bonds = the chain "sites"`**. So `exponent = 5 × (sites)` with NO
offset — the awkward `−3` was an artifact of comparing to the crossing count
`10A−2` rather than the natural site count. The per-site q-power is **5 = the
Bring quintic** (Bring's surface is the quintic `𝒳₅`, Aut = S₅, `g²=5`). The
crossing count `σ+σ⁻¹ = 10A−2` is then a separate fact, exactly 3 above the
site-quintic law `10A−5`.

## Honest status

Slope DERIVED; the offset reframed as **5 (Bring quintic) per chain-site**
(`exponent = 5·(A nucleons + A−1 bonds)`, no `−3`). Remaining open: *why* 5 =
the Bring quintic per site, the Z-correction **coefficient**, and the
per-nucleon **9 = intra-𝓑₃** count. NOT wired (near-match tier).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import time
from collections import Counter

from qou_substrate.witness import WitnessBuilder  # noqa: E402


def crossing_counts(Z, N):
    from mass_at_3A_proper import atom_braid_word_3A
    c = Counter()
    for (_, d, _) in atom_braid_word_3A(Z, N):
        d = round(float(d), 4)
        if abs(d) < 1e-9:
            c["sig"] += 1
        elif abs(d + 0.1045) < 1e-3:
            c["avg"] += 1
        elif abs(d + 0.2091) < 1e-3:
            c["inv"] += 1
    return c["sig"], c["avg"], c["inv"]


def closed_form(Z, N):
    return (7 * Z + 5 * N - 1, 3 * Z + 5 * N - 1, 2 * (Z + N) + 1)  # σ, σ⁻¹, avg


# Per-nucleon intra-𝓑₃ writhe seeds (the p≠n asymmetry source): a proton walk
# is 6σ−3σ⁻¹=+3, a neutron 5σ−4σ⁻¹=+1 (both 9 non-averaged). 3≠1 ⇒ proton excess
# accumulates net writhe faster than neutron excess (³He penalised, mirror T not).
PROTON_INTRA_WRITHE = 3
NEUTRON_INTRA_WRITHE = 1


def writhe_decomposition(Z, N):
    """writhe = 4Z = intra (3Z+N) + interface (Z−N), bar-ODD ⇒ Z-only.

    intra    = proton(+3)·Z + neutron(+1)·N           = 3Z + N
    interface= (Z−1) p-p σ(+1) − (N−1) n-n σ⁻¹(−1)     = Z − N   (mirror splitter)
    """
    intra = PROTON_INTRA_WRITHE * Z + NEUTRON_INTRA_WRITHE * N
    interface = (Z - 1) - (N - 1)
    return intra, interface  # intra + interface == 4Z


def main() -> int:
    t0 = time.monotonic()
    dev = {"D": -0.011, "T": -0.066, "3He": -1.404, "4He": 0.272}
    znd = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}

    rows, cf_ok = [], True
    for name, (Z, N) in znd.items():
        A = Z + N
        sig, avg, inv = crossing_counts(Z, N)
        ps, pi, pa = closed_form(Z, N)
        intra_w, iface_w = writhe_decomposition(Z, N)
        decomp_ok = (intra_w + iface_w == sig - inv == 4 * Z) and (iface_w == Z - N)
        match = ((sig, inv, avg) == (ps, pi, pa) and (sig + inv == 10 * A - 2)
                 and (sig - inv == 4 * Z) and decomp_ok)
        cf_ok = cf_ok and match
        rows.append({"atom": name, "Z": Z, "N": N, "A": A,
                     "sigma": sig, "averaged": avg, "sigma_inv": inv,
                     "non_averaged": sig + inv, "writhe": sig - inv,
                     "intra_writhe_3Z_N": intra_w, "interface_writhe_Z_N": iface_w,
                     "closed_form_sigma_7Z5N_1": ps, "closed_form_inv_3Z5N_1": pi,
                     "exponent_10A_5": 10 * A - 5, "nonavg_minus_3": sig + inv - 3,
                     "Z_minus_N": Z - N, "q0_exp_dev": dev[name]})
        print(f"  {name:>4} Z{Z}N{N}: σ={sig}(=7Z+5N-1={ps}) σ⁻¹={inv}(=3Z+5N-1={pi}) avg={avg}(=2A+1={pa}) "
              f"| σ+σ⁻¹={sig+inv}=10A-2 | writhe={sig-inv}=4Z=intra({intra_w}=3Z+N)+iface({iface_w}=Z-N) "
              f"| (σ+σ⁻¹)-3={sig+inv-3}=10A-5 | Z-N={Z-N} dev={dev[name]:+.3f}  {'OK' if match else 'X'}")

    # NOTE: these crossing-SUM values are exact arithmetic, but their reading as
    # the binding q₀-exponent (10A−5) is REFUTED at A≥5 — see
    # delta_lambda_z_coefficient_and_slope.py (⁶Li measured 36.1, not 55).
    preds = {n: (10 * (Z + N) - 5) for n, (Z, N) in
             {"6Li": (3, 3), "7Li": (3, 4), "8Be": (4, 4)}.items()}
    print(f"\n  closed forms verified (A≤4): {'DERIVED' if cf_ok else 'FAILED'}")
    print(f"  crossing-sum 10A-5 values: {preds}  "
          f"[REFUTED as a binding law at A≥5: ⁶Li measured 36.1 ≠ 55]")

    b = WitnessBuilder("delta-lambda-exponent-from-crossings", engine="python+combinatorial", start_time=t0)
    (b.set_description(
        "Closed-form crossing-bookkeeping derivation of the Δ_λ q₀-exponent. "
        "atom_braid_word_3A: σ=7Z+5N-1, σ⁻¹=3Z+5N-1, avg=2A+1 (bar-symmetric, "
        "0 q-power). σ+σ⁻¹=10A-2 (Z,N cancel ⇒ A-only) ⇒ 10A-5=(σ+σ⁻¹)-3: the "
        "exponent SLOPE 10 = 9 intra-𝓑₃ + 1 interface per nucleon, DERIVED not "
        "fit. writhe=4Z; Z-N=(p-p ifaces)-(n-n ifaces) sources the proton-excess "
        "correction (³He -1.40). Predicts ⁶Li exp 55, ⁸Be 75. Open: -3 offset, "
        "Z-coefficient, the 9=intra count. NOT wired.")
     .add_data("rows", rows)
     .add_data("closed_forms", {"sigma": "7Z+5N-1", "sigma_inv": "3Z+5N-1",
                                "averaged": "2A+1", "non_averaged_sum": "10A-2",
                                "writhe": "4Z", "Z_minus_N": "(p-p ifaces)-(n-n ifaces)",
                                "exponent": "10A-5 = (σ+σ⁻¹) - 3  [A≥2]"})
     .add_data("bar_parity", {
         "sum_sigma_plus_inv": "bar-EVEN (q↔q⁻¹ invariant) ⇒ A-only ⇒ leading exponent 10A-5",
         "writhe_sigma_minus_inv": "bar-ODD ⇒ Z-only (4Z) ⇒ source of the proton-excess correction",
         "reading": "leading bar-even q₀^(10A-5) + first bar-odd Z-correction; "
                    "a symmetric sum cannot carry Z-dependence, so ³He/T asymmetry is forced into the writhe"})
     .add_data("writhe_decomposition", {
         "identity": "writhe = 4Z = intra(3Z+N) + interface(Z-N)",
         "per_nucleon_intra_writhe": {"proton": "6σ-3σ⁻¹ = +3", "neutron": "5σ-4σ⁻¹ = +1"},
         "p_ne_n_seed": "3 ≠ 1 ⇒ proton walk more positive-chirality ⇒ proton excess "
                        "penalised faster than neutron excess (³He -1.40 vs mirror T -0.07)",
         "interface_writhe": "(Z-1) p-p σ minus (N-1) n-n σ⁻¹ = Z-N (mirror-pair splitter; "
                             "T & ³He share σ+σ⁻¹=28 ⇒ identical leading exp 25, differ only here)"})
     .add_data("per_nucleon_10", "9 (intra-𝓑₃ non-averaged) + 1 (interface, amortized)")
     .add_data("predictions_exponent_REFUTED", {
         "values_10A_5": preds,
         "status": "REFUTED at A≥5 (scope-(a)): ⁶Li measured log_q0 Δ_λ=36.1, "
                   "not 55; slope collapses ~10→0.4 at the ⁴He shell. See "
                   "delta_lambda_z_coefficient_and_slope.py. Crossing-sum "
                   "arithmetic stands; the global binding-law reading does not."})
     .add_data("site_reading", {
         "exponent": "5·(2A-1) = 5 × (A nucleons + A-1 bonds) = 5 per chain-site",
         "per_site_q_power": "5 = Bring quintic (𝒳₅; Aut=S₅; g²=5)",
         "offset_minus_3_resolved": "artifact of crossing-count vs site-count; "
                                    "σ+σ⁻¹=10A-2 = site-law 10A-5 + 3 (separate counts)"})
     .add_data("open", {"why_5_is_bring_quintic": "the per-site quintic q-power, not derived",
                        "Z_coefficient": "~-1.4/excess-proton; p≠n asymmetry open",
                        "per_nucleon_9": "intra-𝓑₃ count from Borromean/Bring, not derived"})
     .add_data("discipline", "closed-form combinatorial; derive-or-refute; "
                             "slope DERIVED; offset+Z-coeff open; NOT wired"))
    b.add_assertion("closed_forms_sigma_inv_avg_exact",
                    computed=bool(cf_ok), expected=True,
                    source="σ=7Z+5N-1, σ⁻¹=3Z+5N-1, avg=2A+1, σ+σ⁻¹=10A-2, writhe=4Z for D,T,³He,⁴He")
    b.add_assertion("nonavg_sum_is_A_only_ZN_cancel",
                    computed=bool(all(r["non_averaged"] == 10 * r["A"] - 2 for r in rows)),
                    expected=True, source="σ+σ⁻¹=10(Z+N)-2 ⇒ exponent slope is A-only")
    b.add_assertion("writhe_is_Z_only_and_decomposes",
                    computed=bool(all(r["writhe"] == 4 * r["Z"]
                                      and r["intra_writhe_3Z_N"] + r["interface_writhe_Z_N"] == r["writhe"]
                                      and r["interface_writhe_Z_N"] == r["Z"] - r["N"] for r in rows)),
                    expected=True,
                    source="writhe σ-σ⁻¹=4Z (bar-odd, Z-only) = intra(3Z+N)+interface(Z-N); "
                           "p≠n seed proton+3≠neutron+1 sources the proton-excess correction")
    out = b.save()
    print(f"  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
