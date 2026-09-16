#!/usr/bin/env python3
"""branching_pushforward_entangled_support_probe.py — the free composite is the LR pushforward of the
nucleon block data, its trace factorises because the convention-D weights are LR-multiplicative, and
the bound nuclei D / T / ³He / ⁴He differ from it on a small, measurable entangled support.

Bean `qou-7dal` (session `qou-qt8b`, owner 2026-09-16: "Do SDP analysis"; the substrate-phase /
light-cone recursion). Companion to `QOU/MassTheory/BranchingPushforwardMultiplicativity.lean`, whose
two hypotheses are checked here on COMMITTED DATA ONLY:

  (H1) branching   χ_λ(p ⊗ n) = Σ_{μ,ν ⊢ 3} c^λ_{μν} χ_μ(p) χ_ν(n)          (λ ⊢ 6)
  (H2) weights     Σ_{λ ⊢ 6} y_λ c^λ_{μν} = y_μ y_ν                       (μ, ν ⊢ 3)

with `c^λ_{μν}` the Littlewood–Richardson coefficients for S_6 ⊃ S_3 × S_3 (tabulated below and
self-checked by the dimension identity f^μ f^ν C(6,3) = Σ_λ c^λ_{μν} f^λ), `y_λ` the convention-D
Markov weights at the proton pin (`y-lambda-at-q0.witness.json`, n = 3, 6, 9, 12), and the
characters from `chi-proton-h3-at-q0-50dps`, `chi-neutron-h3-at-q0-50dps` and
`atom-chi-rust-{d,t,3he,4he}` (free = `include_inter=False`, the disjoint constituent product;
atom = with the inter-nucleon letters).

Then, per nucleus: Σ_λ y_λ f^λ = 1; the y-weighted entangled support {λ : y_λ ≠ 0, χ_λ(atom) ≠ χ_λ(free)};
the weighted deviation Σ_λ y_λ δ_λ = tr_M(atom) − tr_M(free) (Lean: `trM_eq_tensor_add_weighted_deviation`);
and the factorisation tr_M(free) = tr_M(p)^Z tr_M(n)^N (Lean: `trM_tensor`, iterated).

Two further measurements the SDP analysis needs, both on the same committed data:

  (R3) the owner-ruled confinement-SDP READING 3 (Frobenius positivity, whole word: χ_λ(w) ≥ 0 on every
       block with y_λ > 0) evaluated on the production bound word AND on its free product, per nucleus;
  (BF) the corpus's bond model, `tr_M(atom)/tr_M(free) = ∏_{interfaces} (z_D + d_kind)` with
       pp → σ (d = 0), pn → averaged_weighted (d = −h(1 − δ/2)/2, `pyhecke.constants.pn_interface_offset`,
       `bring_color_weighted`), nn → σ⁻¹ (d = −h), already established to ~1e-60 by
       `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe` (connected-sum multiplicativity);
       re-measured here as corroboration, not as a new claim. In the picture's words: the "categorical
       trace of the common light cone" that is passed to the knot convolution IS the interface letter's
       Markov trace, and the y-weighted deviation Σ y δ = tr(free)·(∏(z + d) − 1) is fixed by it.

Not shown: anything about selection, K, or a binding number. No fit; no q₀ arithmetic (q₀ enters only
through the committed strings); mpmath 60 dps; LR/dimension arithmetic exact in ℤ.

-- Ref: [manuscript] prop:frobenius-pairing; def:markov-axioms-primitive; bean qou-hlbx
"""
from __future__ import annotations

import json
import sys
from math import comb, factorial
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(REPO / "computations"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
C = REPO / "computations"

# Littlewood–Richardson coefficients c^λ_{μν} for μ, ν ⊢ 3 (Pieri for (3) = h₃ and (1³) = e₃;
# the (2,1)×(2,1) product is the standard LR expansion). Keys: (μ, ν) -> {λ: c}.
P3, P21, P111 = (3,), (2, 1), (1, 1, 1)
LR = {
    (P3, P3):     {(6,): 1, (5, 1): 1, (4, 2): 1, (3, 3): 1},
    (P3, P21):    {(5, 1): 1, (4, 2): 1, (4, 1, 1): 1, (3, 2, 1): 1},
    (P3, P111):   {(4, 1, 1): 1, (3, 1, 1, 1): 1},
    (P21, P21):   {(4, 2): 1, (4, 1, 1): 1, (3, 3): 1, (3, 2, 1): 2, (3, 1, 1, 1): 1, (2, 2, 2): 1, (2, 2, 1, 1): 1},
    (P21, P111):  {(3, 2, 1): 1, (3, 1, 1, 1): 1, (2, 2, 1, 1): 1, (2, 1, 1, 1, 1): 1},
    (P111, P111): {(2, 2, 2): 1, (2, 2, 1, 1): 1, (2, 1, 1, 1, 1): 1, (1, 1, 1, 1, 1, 1): 1},
}
for (mu, nu), tab in list(LR.items()):
    LR.setdefault((nu, mu), tab)  # c^λ_{μν} = c^λ_{νμ}


def hook_dim(lam: tuple[int, ...]) -> int:
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j - 1) + (conj[j] - i - 1) + 1
    assert factorial(n) % prod == 0
    return factorial(n) // prod


def load_y(n: int) -> dict:
    Y = json.loads((C / "y-lambda-at-q0.witness.json").read_text(encoding="utf-8"))
    assert Y["q0Anchor"] == "proton"
    return {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"]) for e in Y["data"]["by_n"][str(n)]}


def load_nucleon(name: str) -> dict:
    w = json.loads((C / f"chi-{name}-h3-at-q0-50dps.witness.json").read_text(encoding="utf-8"))
    assert w["q0Anchor"] == "proton"
    return {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["by_partition"]}


def load_atom(tag: str) -> tuple[dict, dict, dict]:
    w = json.loads((C / f"atom-chi-rust-{tag}.witness.json").read_text(encoding="utf-8"))
    atom = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["data"]["atom"]["by_partition"]}
    free = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["data"]["free"]["by_partition"]}
    return atom, free, {"computedAt": w["computedAt"], "commitSha": w["commitSha"][:12], "description": w["description"][:120]}


def main() -> int:
    checks: list[tuple[str, bool, str]] = []
    def check(name, ok, src):
        checks.append((name, bool(ok), src)); print(f"  [{'ok' if ok else 'FAIL'}] {name}")

    # ── 0. LR table self-check by dimension counting ─────────────────────────────────────────
    dim_ok = True
    for (mu, nu), tab in LR.items():
        lhs = hook_dim(mu) * hook_dim(nu) * comb(6, 3)
        rhs = sum(c * hook_dim(lam) for lam, c in tab.items())
        dim_ok &= (lhs == rhs)
    print("LR table dimension identity f^μ f^ν C(6,3) = Σ c f^λ for all 9 pairs:", dim_ok)
    check("lr_table_dimension_identity", dim_ok, "hook-length dims, exact in ℤ")

    # ── 1. (H2) weight identity at (3,3) -> 6 ────────────────────────────────────────────────
    y3, y6 = load_y(3), load_y(6)
    worst = mp.mpf(0)
    rows_h2 = []
    for (mu, nu), tab in LR.items():
        lhs = sum(y6[lam] * c for lam, c in tab.items())
        rhs = y3[mu] * y3[nu]
        dev = abs(lhs - rhs); worst = max(worst, dev)
        rows_h2.append({"mu": list(mu), "nu": list(nu), "sum_y6_c": mp.nstr(lhs, 50), "y3_mu_y3_nu": mp.nstr(rhs, 50), "abs_dev": mp.nstr(dev, 5)})
        print(f"  Σ_λ y_λ c^λ_{{{mu},{nu}}} = {mp.nstr(lhs, 20)}   y_μ y_ν = {mp.nstr(rhs, 20)}   |dev| = {mp.nstr(dev, 3)}")
    check("weight_identity_sum_y6_c_eq_y3_y3_to_1e-48", worst < mp.mpf("1e-48"), "convention-D y at n=3,6 from y-lambda-at-q0")

    # ── 2. (H1) branching on the committed characters, deuteron free = p ⊗ n ─────────────────
    chi_p, chi_n = load_nucleon("proton"), load_nucleon("neutron")
    atomD, freeD, metaD = load_atom("d")
    worst_b = mp.mpf(0)
    rows_h1 = []
    for lam in freeD:
        pred = sum((LR[(mu, nu)].get(lam, 0)) * chi_p[mu] * chi_n[nu] for mu in y3 for nu in y3)
        dev = abs(pred - freeD[lam]); worst_b = max(worst_b, dev)
        rows_h1.append({"lambda": list(lam), "chi_free_witness": mp.nstr(freeD[lam], 50), "lr_pushforward": mp.nstr(pred, 50), "abs_dev": mp.nstr(dev, 5)})
    print("branching rule on χ(free_D) vs Σ c χ_μ(p) χ_ν(n): worst |dev| =", mp.nstr(worst_b, 5))
    check("branching_rule_free_deuteron_matches_lr_pushforward_to_1e-40", worst_b < mp.mpf("1e-40"),
          "atom-chi-rust-d free vs chi-proton/neutron-h3 through the LR table")

    # ── 3. per-nucleus block measure, entangled support, deviation, factorisation ─────────────
    tr_p = sum(y3[m] * chi_p[m] for m in y3)
    tr_n = sum(y3[m] * chi_n[m] for m in y3)
    print(f"tr_M(p) = {mp.nstr(tr_p, 20)}   tr_M(n) = {mp.nstr(tr_n, 20)}")
    # bond factors at the pin (q0 from the y witness's own recorded string; convention D; R3 colour weighting)
    Yw = json.loads((C / "y-lambda-at-q0.witness.json").read_text(encoding="utf-8"))
    q0 = mp.mpf(Yw["q0Value"])
    h = q0 - 1 / q0
    zD = q0 ** 3 / (q0 ** 2 + 1)
    delta = (q0 - 1) ** 2 * (1 - q0 ** -4) / 3                      # flavor_split_leading
    d_pn = -(h * (1 - delta / 2) / 2)                                 # pn_interface_offset, bring_color_weighted
    bond = {"pp": zD, "pn": zD + d_pn, "nn": zD - h}
    print("bond factors z_D + d_kind at q0:", {k: mp.nstr(v, 20) for k, v in bond.items()})
    chain_kinds = {"d": ["pn"], "t": ["pn", "nn"], "3he": ["pp", "pn"], "4he": ["pp", "pn", "nn"]}  # protons first
    per = {}
    for tag, (Z, N, n) in {"d": (1, 1, 6), "t": (1, 2, 9), "3he": (2, 1, 9), "4he": (2, 2, 12)}.items():
        atom, free, meta = load_atom(tag)
        y = load_y(n)
        assert set(y) == set(atom) == set(free), tag
        total = sum(y[l] * hook_dim(l) for l in y)
        tr_a = sum(y[l] * atom[l] for l in y)
        tr_f = sum(y[l] * free[l] for l in y)
        supp = [l for l in y if y[l] != 0 and atom[l] != free[l]]
        dev = {l: y[l] * (atom[l] - free[l]) for l in y}
        top = sorted(supp, key=lambda l: -abs(dev[l]))[:4]
        prod = tr_p ** Z * tr_n ** N
        bond_prod = mp.mpf(1)
        for k in chain_kinds[tag]:
            bond_prod *= bond[k]
        ratio = tr_a / tr_f
        r3_atom_viol = [l for l in y if y[l] != 0 and atom[l] < 0]
        r3_free_viol = [l for l in y if y[l] != 0 and free[l] < 0]
        per[tag] = {
            "reading3_violations_atom": [list(l) for l in r3_atom_viol],
            "reading3_violations_free": [list(l) for l in r3_free_viol],
            "ratio_tr_atom_over_tr_free": mp.nstr(ratio, 50),
            "bond_product_z_plus_d": mp.nstr(bond_prod, 50),
            "bond_chain_kinds": chain_kinds[tag],
            "bond_product_abs_dev": mp.nstr(abs(ratio - bond_prod), 5),
            "Z": Z, "N": N, "n_strands": n, "blocks": len(y),
            "sum_P": mp.nstr(total, 50),
            "two_row_blocks": sum(1 for l in y if len(l) <= 2),
            "y_weighted_entangled_support_size": len(supp),
            "raw_chi_differs": sum(1 for l in y if atom[l] != free[l]),
            "top_deviation_blocks": [{"lambda": list(l), "y_delta": mp.nstr(dev[l], 30)} for l in top],
            "tr_M_atom": mp.nstr(tr_a, 50), "tr_M_free": mp.nstr(tr_f, 50),
            "weighted_deviation_sum": mp.nstr(tr_a - tr_f, 50),
            "tr_p_pow_Z_tr_n_pow_N": mp.nstr(prod, 50),
            "factorisation_abs_dev": mp.nstr(abs(tr_f - prod), 5),
            "chi_witness": meta,
        }
        print(f"{tag:>4}: n={n} blocks={len(y)} ΣP={mp.nstr(total, 25)} |supp_y|={len(supp)} (two-row {per[tag]['two_row_blocks']})"
              f" tr(atom)={mp.nstr(tr_a, 12)} tr(free)={mp.nstr(tr_f, 12)} p^Z n^N={mp.nstr(prod, 12)} Δ={mp.nstr(tr_a - tr_f, 10)}")
        print(f"        ratio tr(atom)/tr(free) = {mp.nstr(ratio, 20)}   ∏(z+d) over {chain_kinds[tag]} = {mp.nstr(bond_prod, 20)}   |dev| = {mp.nstr(abs(ratio - bond_prod), 3)}")
        print(f"        reading-3 violations (y>0, χ<0): atom {[list(l) for l in r3_atom_viol]}   free {[list(l) for l in r3_free_viol]}")
        for l in top:
            print(f"        {str(l):<18} y·δ = {mp.nstr(dev[l], 10)}")
    check("block_measure_sums_to_one_at_n_6_9_12", all(abs(mp.mpf(per[t]["sum_P"]) - 1) < mp.mpf("1e-48") for t in per), "Σ y_λ f^λ per nucleus")
    check("entangled_support_is_the_two_row_support_for_all_four", all(per[t]["y_weighted_entangled_support_size"] == per[t]["two_row_blocks"] for t in per), "y≠0 ⇔ ≤2 rows (convention D) and χ differs on every such block")
    check("free_trace_factorises_as_tr_p_Z_tr_n_N_to_1e-40", all(mp.mpf(per[t]["factorisation_abs_dev"]) < mp.mpf("1e-40") for t in per), "Lean trM_tensor iterated; committed traces")
    dT = {tuple(r["lambda"]): mp.mpf(r["y_delta"]) for r in per["t"]["top_deviation_blocks"]}
    dH = {tuple(r["lambda"]): mp.mpf(r["y_delta"]) for r in per["3he"]["top_deviation_blocks"]}
    check("ratio_equals_bond_product_z_plus_d_to_1e-40_all_four", all(mp.mpf(per[t]["bond_product_abs_dev"]) < mp.mpf("1e-40") for t in per),
          "corroborates the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe (connected-sum multiplicativity)")
    check("free_product_satisfies_reading3_on_all_four", all(len(per[t]["reading3_violations_free"]) == 0 for t in per),
          "χ_λ(free) ≥ 0 on every y>0 block")
    check("bound_word_violates_reading3_on_all_four", all(len(per[t]["reading3_violations_atom"]) > 0 for t in per),
          "the production bound word has χ_λ < 0 on some y>0 block — the owner-ruled whole-word reading 3 FAILS")
    check("tritium_and_he3_deviation_vectors_differ", per["t"]["weighted_deviation_sum"] != per["3he"]["weighted_deviation_sum"] or dT != dH,
          "the two A=3 mirror nuclei have different y-weighted deviations on the two-row support")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("branching-pushforward-entangled-support", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0_anchor_reason": "all inputs are proton-pinned committed witnesses; no q0 arithmetic here",
        "description": ("PROBE (bean qou-7dal): on committed data the convention-D Markov weights satisfy the LR weight identity "
                        "Σ_λ y_λ c^λ_{μν} = y_μ y_ν (S_6 ⊃ S_3×S_3, 9 pairs, to 1e-48); the deuteron's free product characters ARE "
                        "the LR pushforward of the nucleon characters; hence tr_M(free) = tr_M(p)^Z tr_M(n)^N for D/T/3He/4He; "
                        "Σ y f = 1 at n=6,9,12; the y-weighted entangled support is exactly the two-row support; T and 3He deviate "
                        "differently. Nothing selected, nothing fitted, nothing wired."),
        "weight_family": "markov_y_lambda_convention_D",
        "lr_table_partitions_of_3": {f"{mu}x{nu}": {str(l): c for l, c in tab.items()} for (mu, nu), tab in LR.items()},
        "weight_identity_rows": rows_h2, "weight_identity_worst_abs_dev": mp.nstr(worst, 5),
        "branching_rows_deuteron": rows_h1, "branching_worst_abs_dev": mp.nstr(worst_b, 5),
        "tr_M_proton": mp.nstr(tr_p, 50), "tr_M_neutron": mp.nstr(tr_n, 50),
        "q0_from_y_witness": mp.nstr(q0, 50), "z_D": mp.nstr(zD, 50), "h": mp.nstr(h, 50),
        "bond_factors_z_plus_d": {k: mp.nstr(v, 50) for k, v in bond.items()},
        "pn_convention": "bring_color_weighted",
        "per_nucleus": per,
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
