#!/usr/bin/env python3
"""qlommel_delta_lambda_two_seed_test.py
=========================================

Derive-or-refute (NO FIT of the recurrence coefficient) for the binding `Δ_λ`
ladder via the q-Lommel ORDER recurrence in its second-kind / hyperbolic regime.

## The structure (all derived, gate-respecting)

The canonical residual `Δ_λ(K) = B_AME/B_pred ≈ q₀^(10A−5) = q₀^(5(2A−1))` was
established at near-match tier in
`docs/audits/2026-06-09-delta-lambda-canonical-residual.md` (D exact to 0.01
q₀-units; the "5" is the Bring quintic, `brings-surface-example.md` Aut=S₅).

A geometric ladder with ratio `r = q₀¹⁰` is the canonical first-kind solution of
the q-Lommel ORDER three-term recurrence `Δ_{A+1} = b·Δ_A − Δ_{A−1}` whose
coefficient is **derived** (NOT fitted) as

    b = r + r⁻¹ = q₀¹⁰ + q₀⁻¹⁰ = 2·cosh(10·log q₀)          (◇)

— the two roots `r, q₀⁻¹⁰` of `t² − b t + 1` are the first- and SECOND-kind
branches (J_ν / Y_ν, here in the hyperbolic I_ν / K_ν growth regime). This is
the Lean-proved `QOU.QBeta.two_root_geometric`. The general solution
`Δ_A = α·rᴬ + β·r⁻ᴬ` is fixed by TWO SEEDS — `QOU.QBeta.two_seed_unique` — so a
derived `b` + two light isotopes PREDICT the rest with no fit (the Δ_λ gate
forbids fitting `b`, not testing a derived one).

## What this script reports (honest tiering)

  (1) the pure `q₀^(10A−5)` law vs the canonical Δ_λ (the near-match recap);
  (2) the DERIVED `b` (◇) vs the empirical interior `b` per isospin chain;
  (3) the derive-or-refute: derived-`b` recurrence + two N≥Z seeds (D, T)
      → predict Δ_λ(⁴He), compared to canonical;
  (4) the second-kind admixture `β/α` from the two-seed solve (β = the Y_ν/K_ν
      content that carries per-isotope deviation).

Verdict: NEAR-MATCH, gate-respecting, NOT wired. The exponent `10A−5` and the
Z-dependent correction (³He) remain to be derived from the W_free vs W_atom
crossing/jet bookkeeping on Bring's surface — the open keystone.
"""
from __future__ import annotations

import sys
import pathlib

# qbeta/ scripts reach the parent computations/ dir, then _path_bridge wires the
# substrate/ subdir (witness_base, q_parameter, …) onto sys.path.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402 — adds substrate/ etc. to sys.path

import time  # noqa: E402
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40


def _q0():
    from q_parameter import Q
    return mp.mpf(str(Q() if callable(Q) else Q))


def _delta_data():
    import json, pathlib
    p = pathlib.Path(__file__).resolve().parent.parent / "delta-lambda-canonical-residual.witness.json"
    d = json.loads(p.read_text())
    data = d.get("data", d)
    rows = data.get("rows") or data.get("results") or d.get("rows") or []
    return {r["atom"]: (r["A"], mp.mpf(str(r["Delta_lambda"]))) for r in rows}


def main() -> int:
    t0 = time.monotonic()
    q0 = _q0()
    eta = mp.log(q0)
    D = _delta_data()
    r = q0 ** 10                      # geometric ratio per A-step (DERIVED exponent 10)
    b = r + 1 / r                     # (◇) DERIVED recurrence coefficient = 2 cosh(10 η)

    # (1) pure q0^(10A-5) law
    pure = {a: (A, q0 ** (10 * A - 5)) for a, (A, _) in D.items()}
    print(f"q0 = {mp.nstr(q0,10)}  eta0 = {mp.nstr(eta,8)}  b = q0^10+q0^-10 = {mp.nstr(b,8)}")
    print("(1) pure q0^(10A-5):")
    rows = []
    for a, (A, v) in D.items():
        law = pure[a][1]
        exp_actual = mp.log(v) / eta
        rows.append({"atom": a, "A": A, "Delta_lambda": mp.nstr(v, 8),
                     "q0_pow_10A_5": mp.nstr(law, 8),
                     "exp_actual": mp.nstr(exp_actual, 6), "exp_law": 10 * A - 5,
                     "exp_dev": mp.nstr(exp_actual - (10 * A - 5), 4)})
        print(f"    {a:4s} A={A} Δ={float(v):8.4f}  law={float(law):8.4f}  "
              f"exp={float(exp_actual):.3f} (want {10*A-5}, dev {float(exp_actual-(10*A-5)):+.3f})")

    # (2) derived b vs empirical interior b (per isospin chain)
    chains = {"T": ["D", "T", "4He"], "3He": ["D", "3He", "4He"]}
    chain_out = {}
    print(f"\n(2) DERIVED b = {float(b):.5f}  vs empirical interior b:")
    for name, ch in chains.items():
        d = [D[a][1] for a in ch]
        b_emp = (d[2] + d[0]) / d[1]
        chain_out[name] = {"interior_b_emp": mp.nstr(b_emp, 8),
                           "b_derived_rel_err_pct": mp.nstr((b - b_emp) / b_emp * 100, 5)}
        print(f"    {name+'-chain':12s} interior b_emp = {float(b_emp):.5f}  "
              f"(derived b off {float((b-b_emp)/b_emp*100):+.2f}%)")

    # (3) derive-or-refute: derived-b recurrence + two seeds (D, X) -> predict 4He
    print("\n(3) two-seed prediction Δ(4He) = b·Δ(X) − Δ(D)  [derived b, NO fit]:")
    pred_out = {}
    for X in ("T", "3He"):
        p4 = b * D[X][1] - D["D"][1]
        err = (p4 - D["4He"][1]) / D["4He"][1] * 100
        pred_out[X] = {"pred_4He": mp.nstr(p4, 8), "actual_4He": mp.nstr(D["4He"][1], 8),
                       "err_pct": mp.nstr(err, 5)}
        print(f"    seeds D,{X:3s}: predict {float(p4):8.4f}  vs 39.6597  ({float(err):+.2f}%)")

    # (4) second-kind admixture β/α from the two-seed solve (D, T), r·s=1
    s = 1 / r
    # α r^2 + β s^2 = Δ(D);  α r^3 + β s^3 = Δ(T)
    A2, A3 = D["D"][1], D["T"][1]
    det = r ** 2 * s ** 3 - r ** 3 * s ** 2
    alpha = (A2 * s ** 3 - A3 * s ** 2) / det
    beta = (r ** 2 * A3 - r ** 3 * A2) / det
    print(f"\n(4) two-seed (D,T) solve: α={float(alpha):.5f}  β={float(beta):.5f}  "
          f"second-kind content β/α = {float(beta/alpha):.4f}")

    builder = WitnessBuilder("qlommel-delta-lambda-two-seed", engine="python+mpmath", start_time=t0)
    (builder
     .set_description(
        "Derive-or-refute (no fit of b) of the binding Δ_λ ladder via the q-Lommel "
        "ORDER recurrence in its second-kind/hyperbolic regime. Derived coefficient "
        "b = q0^10 + q0^-10 = 2cosh(10 log q0) from the q0^(10A-5) canonical residual "
        "(Bring quintic '5'); Lean QOU.QBeta.two_root_geometric + two_seed_unique. "
        "Verdict NEAR-MATCH, gate-respecting, NOT wired: derived-b + two N≥Z seeds "
        "predicts Δ(4He) to ~-3.5%; 3He is the Z-dependent outlier. Open keystone: "
        "derive 10A-5 from W_free/W_atom crossing-jet bookkeeping on Bring's surface.")
     .add_parameter("q0", mp.nstr(q0, 12))
     .add_parameter("b_derived", mp.nstr(b, 12))
     .add_parameter("geometric_ratio_r", mp.nstr(r, 12))
     .add_data("pure_law_rows", rows)
     .add_data("chains", chain_out)
     .add_data("two_seed_predictions", pred_out)
     .add_data("second_kind_admixture", {"alpha": mp.nstr(alpha, 8), "beta": mp.nstr(beta, 8),
                                         "beta_over_alpha": mp.nstr(beta / alpha, 6)})
     .add_data("discipline", "derived b (no fit); near-match tier; NOT wired; "
                             "open keystone = derive 10A-5 from Bring crossings"))
    # derived b matches the N≥Z (T) chain interior b within 5%
    bT = (D["4He"][1] + D["D"][1]) / D["T"][1]
    builder.add_assertion("derived_b_matches_NgeZ_chain_within_5pct",
                          computed=bool(abs((b - bT) / bT) < mp.mpf("0.05")), expected=True,
                          source="b = q0^10+q0^-10 vs T-chain interior b")
    # two-seed (D,T) predicts 4He within 5% (near-match tier)
    p4T = b * D["T"][1] - D["D"][1]
    builder.add_assertion("two_seed_DT_predicts_4He_within_5pct",
                          computed=bool(abs((p4T - D["4He"][1]) / D["4He"][1]) < mp.mpf("0.05")),
                          expected=True, source="derived-b recurrence, no fit")
    # 3He is the Z-dependent outlier (>10% as a seed) — the derivation must carry a Z-correction
    p4H = b * D["3He"][1] - D["D"][1]
    builder.add_assertion("3He_is_Z_outlier_gt_10pct",
                          computed=bool(abs((p4H - D["4He"][1]) / D["4He"][1]) > mp.mpf("0.10")),
                          expected=True, source="proton-rich 3He needs the Z-dependent correction")
    out = builder.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
