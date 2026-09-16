#!/usr/bin/env python3
"""lr_a3_three_factor_branching_probe.py — the A = 3 Littlewood–Richardson branching, built and checked
on COMMITTED DATA ONLY at H_9. Bean `qou-672t` (milestone `qou-cgsn`; owner 2026-09-16: "Build the
A = 3 Littlewood–Richardson branching"). Companion to the `Iterated` section of
`QOU/MassTheory/BranchingPushforwardMultiplicativity.lean` (`c₃`, `branching₃`, `weight_branching₃`,
`trM_tensor₃`), whose hypotheses and conclusions are measured here:

  (H1₃) three-factor restriction rule   χ_λ(x₁ ⊗ x₂ ⊗ x₃) = Σ_{μ,ν,ρ ⊢ 3} c^λ_{μνρ} χ_μ(x₁) χ_ν(x₂) χ_ρ(x₃)
        with c^λ_{μνρ} = Σ_{κ ⊢ 6} c^κ_{μν} c^λ_{κρ}   (λ ⊢ 9; `c₃` in the Lean), checked against the
        committed FREE products of T = (p, n, n) and ³He = (p, p, n) (`atom-chi-rust-{t,3he}`, `free`
        = `include_inter=False`, Rust + MPFR 50 dps) on all 30 blocks;
  (H2)  the (6, 3) → 9 weight identity   Σ_{λ ⊢ 9} y_λ c^λ_{κρ} = y_κ y_ρ   (κ ⊢ 6, ρ ⊢ 3; 33 pairs),
        new at this level — the previous probe measured (3, 3) → 6;
  (H2₃) the iterated weight identity     Σ_{λ ⊢ 9} y_λ c^λ_{μνρ} = y_μ y_ν y_ρ   (27 triples;
        `weight_branching₃`);
  (M₃)  tr_M(free) = tr_M(p)^Z tr_M(n)^N at H_9 through the three-factor rule (`trM_tensor₃`);
  (Δ)   the block-resolved deviation δ_λ = χ_λ(atom) − χ_λ(free) of T and ³He on the two-row support
        (the y-weighted entangled support), with its weighted total against the bond product
        tr_M(free)(∏(z_D + d) − 1) (`weighted_deviation_eq_of_trM_eq_mul`), and the direction
        (unit vector on the two-row support) that distinguishes the mirror pair.

Inputs: `y-lambda-at-q0.witness.json` (n = 3, 6, 9; convention D, proton pin), `chi-{proton,neutron}-h3-at-q0-50dps`,
`atom-chi-rust-{t,3he}`. LR coefficients from `computations/substrate/lr_coefficients.py` (skew-tableau
enumeration, exact in ℤ), self-checked by the dimension identity f^μ f^ν f^ρ · 9!/(3!)³ = Σ_λ c^λ_{μνρ} f^λ.
No fit, no selection, no q₀ arithmetic beyond the committed strings; mpmath 60 dps.

What this does NOT show: which interface letter produces the measured deviation (the composition program,
bean `qou-8r6b`), or any binding number. The deviation *direction* is reported as data, not as a claim.
-- Ref: [manuscript] prop:frobenius-pairing; def:markov-axioms-primitive; bean qou-672t
"""
from __future__ import annotations
import json
import sys
from math import factorial  # float64-ok: exact arbitrary-precision ints (hook-length count f^λ, multinomial); only //, %, == below, never a float
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
C = REPO / "computations"
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(C / "substrate"))
sys.path.insert(0, str(C))
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402

mp.mp.dps = 60
P3 = [(3,), (2, 1), (1, 1, 1)]


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
    return atom, free, {"computedAt": w["computedAt"], "commitSha": w["commitSha"][:12], "Z": w["data"]["atom"]["Z"], "N": w["data"]["atom"]["N"]}


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    t33 = get_lr_table(3, 3)   # {(mu, nu, kappa): c}
    t63 = get_lr_table(6, 3)   # {(kappa, rho, lam): c}
    P6, P9 = partitions_of(6), partitions_of(9)
    print(f"LR tables: (3,3)→6 {len(t33)} nonzero, (6,3)→9 {len(t63)} nonzero; |P6|={len(P6)} |P9|={len(P9)}")

    # c^λ_{μνρ} = Σ_κ c^κ_{μν} c^λ_{κρ}   (exact ℤ)
    c3: dict[tuple, dict[tuple, int]] = {}
    for mu in P3:
        for nu in P3:
            for rho in P3:
                acc: dict[tuple, int] = {}
                for kappa in P6:
                    c1 = t33.get((mu, nu, kappa), 0)
                    if c1 == 0:
                        continue
                    for lam in P9:
                        c2 = t63.get((kappa, rho, lam), 0)
                        if c2:
                            acc[lam] = acc.get(lam, 0) + c1 * c2
                c3[(mu, nu, rho)] = acc
    # dimension identity: f^μ f^ν f^ρ · 9!/(3!3!3!) = Σ_λ c^λ_{μνρ} f^λ
    multinomial = factorial(9) // (factorial(3) ** 3)
    dim_ok = all(hook_dim(mu) * hook_dim(nu) * hook_dim(rho) * multinomial == sum(c * hook_dim(l) for l, c in tab.items())
                 for (mu, nu, rho), tab in c3.items())
    check("c3_dimension_identity_all_27_triples", dim_ok, "f^μ f^ν f^ρ · 1680 = Σ_λ c^λ_{μνρ} f^λ, exact in ℤ")
    n_support = {k: len(v) for k, v in c3.items()}
    print("  three-factor supports |{λ : c^λ_{μνρ} ≠ 0}|:", {f"{mu}{nu}{rho}": n for (mu, nu, rho), n in n_support.items()})

    y3, y6, y9 = load_y(3), load_y(6), load_y(9)
    assert set(y9) == set(P9) and set(y6) == set(P6)
    # (H2) at (6,3)→9
    worst_63 = mp.mpf(0)
    rows_63 = []
    for kappa in P6:
        for rho in P3:
            lhs = sum(y9[l] * t63.get((kappa, rho, l), 0) for l in P9)
            rhs = y6[kappa] * y3[rho]
            dev = abs(lhs - rhs)
            worst_63 = max(worst_63, dev)
            rows_63.append({"kappa": list(kappa), "rho": list(rho), "lhs": mp.nstr(lhs, 30), "rhs": mp.nstr(rhs, 30), "abs_dev": mp.nstr(dev, 5)})
    check("weight_identity_6x3_to_9_all_33_pairs_to_1e-45", worst_63 < mp.mpf("1e-45"), f"worst |Σ_λ y_λ c^λ_{{κρ}} − y_κ y_ρ| = {mp.nstr(worst_63, 5)}")
    # (H2₃) iterated
    worst_333 = mp.mpf(0)
    rows_333 = []
    for (mu, nu, rho), tab in c3.items():
        lhs = sum(y9[l] * c for l, c in tab.items())
        rhs = y3[mu] * y3[nu] * y3[rho]
        dev = abs(lhs - rhs)
        worst_333 = max(worst_333, dev)
        rows_333.append({"mu": list(mu), "nu": list(nu), "rho": list(rho), "lhs": mp.nstr(lhs, 30), "rhs": mp.nstr(rhs, 30), "abs_dev": mp.nstr(dev, 5)})
    check("iterated_weight_identity_3x3x3_to_9_all_27_triples_to_1e-45", worst_333 < mp.mpf("1e-45"), f"worst |Σ_λ y_λ c^λ_{{μνρ}} − y_μ y_ν y_ρ| = {mp.nstr(worst_333, 5)}")

    # nucleons and the two A = 3 nuclei
    chi_p, chi_n = load_nucleon("proton"), load_nucleon("neutron")
    tr_p = sum(y3[l] * chi_p[l] for l in y3)
    tr_n = sum(y3[l] * chi_n[l] for l in y3)
    q0 = mp.mpf(json.loads((C / "y-lambda-at-q0.witness.json").read_text(encoding="utf-8"))["q0Value"])
    h = q0 - 1 / q0
    zD = q0 ** 3 / (q0 ** 2 + 1)
    delta = (q0 - 1) ** 2 * (1 - q0 ** -4) / 3
    d_pn = -(h * (1 - delta / 2) / 2)
    bond = {"pp": zD, "pn": zD + d_pn, "nn": zD - h}
    chain_kinds = {"t": ["pn", "nn"], "3he": ["pp", "pn"]}   # protons first: T = (p, n, n), 3He = (p, p, n)
    per = {}
    worst_b = mp.mpf(0)
    for tag, order in {"t": ("p", "n", "n"), "3he": ("p", "p", "n")}.items():
        atom, free, meta = load_atom(tag)
        assert set(atom) == set(free) == set(P9), tag
        assert (meta["Z"], meta["N"]) == (order.count("p"), order.count("n")), (tag, meta)
        chis = [chi_p if s == "p" else chi_n for s in order]
        # (H1₃) three-factor rule against the committed free product
        pred = {}
        for l in P9:
            acc = mp.mpf(0)
            for (mu, nu, rho), tab in c3.items():
                c = tab.get(l, 0)
                if c:
                    acc += c * chis[0][mu] * chis[1][nu] * chis[2][rho]
            pred[l] = acc
        dev_b = max(abs(pred[l] - free[l]) for l in P9)
        worst_b = max(worst_b, dev_b)
        tr_a = sum(y9[l] * atom[l] for l in P9)
        tr_f = sum(y9[l] * free[l] for l in P9)
        prod = tr_p ** order.count("p") * tr_n ** order.count("n")
        bond_prod = mp.mpf(1)
        for k in chain_kinds[tag]:
            bond_prod *= bond[k]
        two_row = [l for l in P9 if len(l) <= 2]
        dev = {l: atom[l] - free[l] for l in two_row}
        ydev = {l: y9[l] * dev[l] for l in two_row}
        total = sum(ydev.values())
        pinned = tr_f * (bond_prod - 1)
        norm = mp.sqrt(sum(v ** 2 for v in ydev.values()))
        direction = {l: ydev[l] / norm for l in two_row}
        per[tag] = {
            "order": list(order), "chi_witness": meta,
            "three_factor_rule_worst_abs_dev_over_30_blocks": mp.nstr(dev_b, 5),
            "tr_M_atom": mp.nstr(tr_a, 50), "tr_M_free": mp.nstr(tr_f, 50), "tr_p_pow_Z_tr_n_pow_N": mp.nstr(prod, 50),
            "factorisation_abs_dev": mp.nstr(abs(tr_f - prod), 5),
            "bond_chain_kinds": chain_kinds[tag], "bond_product_z_plus_d": mp.nstr(bond_prod, 50),
            "ratio_tr_atom_over_tr_free": mp.nstr(tr_a / tr_f, 50), "bond_product_abs_dev": mp.nstr(abs(tr_a / tr_f - bond_prod), 5),
            "two_row_deviation_delta": {str(l): mp.nstr(dev[l], 30) for l in two_row},
            "two_row_y_weighted_deviation": {str(l): mp.nstr(ydev[l], 30) for l in two_row},
            "weighted_deviation_total": mp.nstr(total, 50),
            "pinned_total_tr_free_times_bond_minus_one": mp.nstr(pinned, 50),
            "pinned_abs_dev": mp.nstr(abs(total - pinned), 5),
            "deviation_direction_unit_two_row": {str(l): mp.nstr(direction[l], 20) for l in two_row},
            "chi_atom_two_row": {str(l): mp.nstr(atom[l], 30) for l in two_row},
            "chi_free_two_row": {str(l): mp.nstr(free[l], 30) for l in two_row},
            "reading3_violations_atom": [list(l) for l in P9 if y9[l] != 0 and atom[l] < 0],
        }
        print(f"{tag:>4} {order}: three-factor rule worst dev {mp.nstr(dev_b, 3)} | tr(free) {mp.nstr(tr_f, 15)} vs p^Z n^N {mp.nstr(prod, 15)} "
              f"| ratio {mp.nstr(tr_a / tr_f, 15)} vs ∏(z+d) {mp.nstr(bond_prod, 15)} | Σyδ {mp.nstr(total, 12)} vs pinned {mp.nstr(pinned, 12)}")
        for l in two_row:
            print(f"        {str(l):<8} χ_atom {mp.nstr(atom[l], 12):>16}  χ_free {mp.nstr(free[l], 12):>16}  y·δ {mp.nstr(ydev[l], 10):>14}  dir {mp.nstr(direction[l], 8)}")
    check("three_factor_rule_matches_committed_free_products_T_and_3He_to_1e-40", worst_b < mp.mpf("1e-40"),
          f"worst |Σ c³ χχχ − χ_λ(free)| over 60 blocks = {mp.nstr(worst_b, 5)} (Lean branching₃)")
    check("free_trace_factorises_at_H9_to_1e-40", all(mp.mpf(per[t]["factorisation_abs_dev"]) < mp.mpf("1e-40") for t in per), "Lean trM_tensor₃")
    check("weighted_deviation_total_is_pinned_by_bond_product_to_1e-40", all(mp.mpf(per[t]["pinned_abs_dev"]) < mp.mpf("1e-40") for t in per),
          "Σ y δ = tr(free)(∏(z_D+d) − 1); Lean weighted_deviation_eq_of_trM_eq_mul")
    dT = per["t"]["deviation_direction_unit_two_row"]
    dH = per["3he"]["deviation_direction_unit_two_row"]
    cos_dir = sum(mp.mpf(dT[k]) * mp.mpf(dH[k]) for k in dT)
    check("mirror_pair_deviation_directions_differ", any(dT[k] != dH[k] for k in dT), f"cos(angle between the two unit deviation directions) = {mp.nstr(cos_dir, 12)}")
    check("both_A3_bound_words_fail_reading3", all(len(per[t]["reading3_violations_atom"]) > 0 for t in per), "re-measured, corroborates qou-7dal")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("lr-a3-three-factor-branching", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0_anchor_reason": "all inputs are proton-pinned committed witnesses; q0 enters only through committed strings",
        "description": ("PROBE (bean qou-672t): the A = 3 Littlewood–Richardson branching on committed data. c^λ_{μνρ} = Σ_κ c^κ_{μν} c^λ_{κρ} "
                        "(exact, dimension-checked on 27 triples); the (6,3)→9 weight identity holds on all 33 pairs and the iterated one on all "
                        "27 triples; the three-factor restriction rule reproduces the committed free products of T and 3He on all 30 blocks; "
                        "tr_M(free) factorises; the y-weighted deviation total is pinned by the bond product and the mirror pair differs only "
                        "in the DIRECTION of its two-row deviation. Nothing selected, nothing fitted, nothing wired."),
        "weight_family": "markov_y_lambda_convention_D",
        "lr_6x3_to_9_nonzero_entries": len(t63), "lr_3x3_to_6_nonzero_entries": len(t33),
        "c3_support_sizes": {f"{mu}x{nu}x{rho}": n for (mu, nu, rho), n in n_support.items()},
        "weight_identity_6x3_rows": rows_63, "weight_identity_6x3_worst_abs_dev": mp.nstr(worst_63, 5),
        "iterated_weight_identity_rows": rows_333, "iterated_weight_identity_worst_abs_dev": mp.nstr(worst_333, 5),
        "tr_M_proton": mp.nstr(tr_p, 50), "tr_M_neutron": mp.nstr(tr_n, 50),
        "q0_from_y_witness": mp.nstr(q0, 50), "z_D": mp.nstr(zD, 50), "h": mp.nstr(h, 50),
        "bond_factors_z_plus_d": {k: mp.nstr(v, 50) for k, v in bond.items()}, "pn_convention": "bring_color_weighted",
        "cos_angle_between_T_and_3He_deviation_directions": mp.nstr(cos_dir, 30),
        "per_nucleus": per,
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
