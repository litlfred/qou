#!/usr/bin/env python3
"""EXPLORATORY shape-probe — the DERIVED q-heat-kernel weight as the per-block
binding measure (de-fit of the per-depth α_k assignment).

Owner program (2026-06-13): "use heat kernel, active-set partitions to figure
out the weight; get rid of fitting." Maps to deliverable C of the binding-
method reconciliation (docs/audits/2026-06-13-binding-method-reconciliation-
and-defit-program.md).

The depth-stratified canonical default carries a FITTED per-depth α_k
*assignment rule* (canonical_status = "canonical-with-empirical-assignment").
This probe tests the already-DERIVED replacement: the q-heat-kernel eigenvalue
from prop:q-heat-kernel-peter-weyl,

    μ_λ(q) = ℏ_q² · C_λ(q),   C_λ(q) = Σ_{□∈λ} [c(□)]_q · [c(□)+1]_q ,

as the per-block weight in the measure-search harness

    B(K) = E · Σ_λ w_λ · |Δθ_λ|        (Δθ_λ = arccos(χ^λ/d_λ), atom − free) .

This is the ONE structurally-motivated weight the prior measure search
(probe_binding_measure_search.py: y_λ / dim_q / abs_content / 1/y_λ / bar-y)
never tested. ℏ_q² is a global constant ⇒ absorbed into E ⇒ the EIGENVALUE
weight C_λ is PARAMETER-FREE (zero-fit). The heat KERNEL weight e^{−C_λ·τ}
carries one "time" τ; reported separately and TIERED (a τ tuned to AME is a
1-param near-match, never "derived").

⚠ Active-set guardrail (2026-06-10-binding-active-set-compute-optimization):
the active set (few-row λ carrying ~90% of tr_M) is used here ONLY to report
which λ the weight must rank correctly — the binding sum runs the FULL p(3A)
partition set. No truncation (that breaks L1 1-ppQ).

EXPLORATORY (production-vs-exploratory-discipline): asserts the refutation
(CI-safe); a positive (the derived heat weight closes A≥3 to 5% with no τ-fit)
is surfaced for promotion + a categorical derivation. Touches no production.
Δ_λ / A≥3-absolute remains the open gate; no 7th fit is introduced.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, fabs, acos, e as MP_E

sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
q0 = mpf(str(Q0))

AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": mpf("7.7180"), "4He": AME_B_HE4_MEV_VALIDATION}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}
A_GROWTH_TARGET = float(AME_B["4He"] / AME_B["D"])  # ≈ 12.72


def q_int(m, q):
    """Balanced q-integer [m]_q = (q^m − q^{−m})/(q − q^{−1}); [0]=0, [−m]=−[m]."""
    if m == 0:
        return mpf(0)
    return (q ** m - q ** (-m)) / (q - 1 / q)


def hooks(lam):
    colh = [0] * (max(lam) if lam else 0)
    for ri in lam:
        for j in range(ri):
            colh[j] += 1
    hs = []
    for i, ri in enumerate(lam):
        for j in range(ri):
            hs.append((ri - j - 1) + (colh[j] - i - 1) + 1)
    return hs


def dim_classical(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= h
    return mp.factorial(sum(lam)) / den


def content_casimir(lam, q):
    """q-heat-kernel eigenvalue shape C_λ(q) = Σ_□ [c]_q [c+1]_q, c = col − row.
    (μ_λ = ℏ_q²·C_λ; ℏ_q² is global ⇒ absorbed into the binding scale E.)
    Sanity: C_{(2,1)} = [2]_q (contents {0,1,−1})."""
    total = mpf(0)
    for i, ri in enumerate(lam):
        for j in range(ri):
            c = j - i
            total += q_int(c, q) * q_int(c + 1, q)
    return total


def abs_content(lam):
    return mpf(sum(abs(j - i) for i, ri in enumerate(lam) for j in range(ri)))


def load_y(n):
    d = json.load(open(HERE / "y-lambda-at-q0.witness.json"))
    byn = d.get("data", d)["by_n"][str(n)]
    return {tuple(el["partition"]): mpf(el["y_at_q0_50dps"]) for el in byn}


def active_set(atom_chi, y):
    """Top-90% partitions by |y_λ · χ^λ(atom)| (the tr_M contribution).
    DIAGNOSTIC only — the binding sum below uses the FULL partition set."""
    contrib = sorted(
        ((lam, fabs(y.get(lam, mpf(0)) * atom_chi[lam])) for lam in atom_chi),
        key=lambda kv: kv[1], reverse=True,
    )
    tot = sum(c for _, c in contrib)
    acc, picked = mpf(0), []
    for lam, c in contrib:
        if tot > 0 and acc / tot >= mpf("0.90"):
            break
        acc += c
        picked.append({"partition": list(lam), "frac": float(c / tot) if tot else 0.0})
    return picked


def main() -> int:
    # τ candidates for the heat KERNEL weight e^{−C_λ·τ} (all reported tiered;
    # NONE tuned to AME — these are substrate-flavoured probe points only).
    taus = {"tau_1": mpf(1), "tau_hbar2": (q0 - 1 / q0) ** 2, "tau_inv_hbar2": 1 / (q0 - 1 / q0) ** 2}
    weights = ["heat_mu_lambda", "abs_content", "y_lambda"] + [f"heatker_{k}" for k in taus]

    S = {w: {} for w in weights}
    active = {}
    for name, fname in CHI.items():
        path = HERE / fname
        if not path.exists():
            print(f"⚠ missing chi witness {fname} — skipping {name}")
            continue
        raw = json.load(open(path))
        d = raw["data"] if "data" in raw else raw
        atom = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
                for el in d["atom"]["by_partition"]}
        free = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
                for el in d["free"]["by_partition"]}
        n = d["atom"]["n_strands"]
        y = load_y(n)
        active[name] = {"n_strands": n, "n_partitions_total": len(atom),
                        "active_90pct": active_set(atom, y)}

        acc = {w: mpf(0) for w in weights}
        for lam in atom:
            ll = list(lam)
            dl = dim_classical(ll)
            dth = acos(mp.mpc(atom[lam] / dl)) - acos(mp.mpc(free[lam] / dl))
            a = fabs(dth)
            C = content_casimir(ll, q0)
            wv = {
                "heat_mu_lambda": C,                              # DERIVED, param-free
                "abs_content": abs_content(ll),                  # classical analogue (baseline)
                "y_lambda": y.get(lam, mpf(0)),                  # anti-correlating baseline
            }
            for k, tau in taus.items():
                wv[f"heatker_{k}"] = MP_E ** (-C * tau)          # heat kernel (1-param τ)
            for w in weights:
                acc[w] += wv[w] * a
        for w in weights:
            S[w][name] = acc[w]

    isos = [k for k in CHI if k in active]
    results = {}
    for w in weights:
        if not all(k in S[w] for k in isos) or len(isos) < 2:
            continue
        num = sum(S[w][k] * AME_B[k] for k in isos)
        den = sum(S[w][k] ** 2 for k in isos)
        scale = num / den if den else mpf(0)            # 1 global scale E (least-squares)
        worst, per = mpf(0), {}
        for k in isos:
            Bp = scale * S[w][k]
            err = (Bp - AME_B[k]) / AME_B[k]
            per[k] = {"B_pred": float(Bp), "err": float(err)}
            worst = max(worst, fabs(err))
        a_growth = float(S[w]["4He"] / S[w]["D"]) if ("4He" in S[w] and "D" in S[w]
                                                       and S[w]["D"] != 0) else float("nan")
        results[w] = {"global_scale": float(scale), "worst_err": float(worst),
                      "S_4He_over_S_D": a_growth, "per_isotope": per}

    # The de-fit candidate is heat_mu_lambda (zero-fit); kernel variants are 1-param (tiered).
    cand = results.get("heat_mu_lambda")
    closes = bool(cand and cand["worst_err"] <= 0.05)
    tier = ("derived-closes" if closes
            else "derived-refuted" if cand else "no-data")

    print(f"\nq0 = {mp.nstr(q0, 8)}   A-growth target S(⁴He)/S(D) ≈ {A_GROWTH_TARGET:.2f}\n")
    print(f"{'weight':<16}{'worst|err|':>11}{'S(⁴He)/S(D)':>13}{'tier':>8}")
    for w in weights:
        if w not in results:
            continue
        r = results[w]
        kind = "ZERO-FIT" if w == "heat_mu_lambda" else (
            "1-param" if w.startswith("heatker_") else "baseline")
        print(f"  {w:<14}{r['worst_err']*100:>9.1f}%{r['S_4He_over_S_D']:>12.2f}{kind:>10}")
    print(f"\nde-fit candidate heat_mu_lambda → {tier}"
          + (f" (worst |err| {cand['worst_err']*100:.1f}%)" if cand else ""))

    wb = WitnessBuilder("binding-heat-kernel-weight-probe", engine="mpmath")
    wb.set_description(
        "EXPLORATORY de-fit probe: tests the DERIVED q-heat-kernel eigenvalue "
        "weight C_λ(q)=Σ_□[c]_q[c+1]_q (prop:q-heat-kernel-peter-weyl, μ_λ "
        "shape) as the per-block binding measure B=E·Σ_λ w_λ|Δθ_λ|, replacing "
        "the FITTED per-depth α_k assignment. C_λ is parameter-free (ℏ_q² "
        "absorbed into E); heat-kernel e^{−C_λ·τ} variants are 1-param and "
        "reported tiered (no τ tuned to AME). Active set reported for the "
        "weight-form diagnostic; binding sum is FULL p(3A) (no truncation). "
        "Asserts the refutation if no zero-fit weight closes A≥3 to 5%."
    )
    wb.add_parameter("q0_50dps", mp.nstr(q0, 40))
    wb.add_parameter("A_growth_target", A_GROWTH_TARGET)
    wb.add_data("weights", results)
    wb.add_data("active_set_per_isotope", active)
    wb.add_data("defit_candidate", "heat_mu_lambda")
    wb.add_data("defit_tier", tier)
    wb.add_assertion(
        name="derived_heat_kernel_weight_closes_or_refutes_A3plus",
        computed=str(int(not closes)),
        expected="1",
        tolerance=0,
        source=(
            f"heat_mu_lambda (DERIVED, zero-fit) worst |err| = "
            f"{cand['worst_err']*100:.1f}% over {isos} at 1 global scale; "
            f"A-growth S(⁴He)/S(D) = {cand['S_4He_over_S_D']:.2f} vs target "
            f"{A_GROWTH_TARGET:.2f}. 1=refuted (no zero-fit closure), "
            "0=closes — promote for categorical derivation."
            if cand else "no chi witnesses available"
        ),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
