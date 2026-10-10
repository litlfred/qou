#!/usr/bin/env python3
"""composition_feasibility_a2_probe.py — the composition feasibility program POSED and solved at A = 2 on the
one-parameter interface alphabet (1 − e)·σ + e·σ⁻¹. Bean `qou-8r6b` (milestone `qou-cgsn`; owner 2026-09-16:
"Pose the composition feasibility program"). Companion to `QOU/MassTheory/CompositionFeasibilityProgram.lean`
(`CompositionProgram`, `Feasible` = reading 3 on the composite) and
`QOU/MassTheory/InterfaceLetterCrossingMixture.lean` (`interfaceLetter_eq_mix`, `trace_interfaceLetter`).

THE PROGRAM (A = 2, deuteron marginals)
  data      the production proton and neutron H_3 blocks (11 letters each, `pyhecke.atom.nucleon_gen_chains`
            templates, alternating `(σ₀σ₁⁻¹)³` core per the 2026-09-05 ruling), embedded disjointly in H_6;
  variable  the interface letter on the bridge generator σ₂, from the alphabet
              L_e = σ₂ − e·h·1 = (1 − e)·σ₂ + e·σ₂⁻¹,   e ∈ ℝ   (e = 0: σ, e = 1: σ⁻¹, e = e_pn: production),
            plus the power letters σ₂^m, m = −3..3 (m = 0 is the unit letter);
  composite W_e = W_free · L_e  (right multiplication, as `atom_braid_word_3A` lays the bond after the blocks);
  feasible  reading 3, whole word (owner 2026-09-12/13): χ_λ(W_e) ≥ 0 on every block with y_λ > 0
            (convention D: the four two-row blocks (6), (5,1), (4,2), (3,3)).

WHY IT IS SOLVABLE IN CLOSED FORM
  χ_λ(W_free · L_e) = (1 − e)·χ_λ(W_free σ₂) + e·χ_λ(W_free σ₂⁻¹) is AFFINE in e, so each block's constraint
  is a half-line and the feasible set in e is an interval (possibly empty), determined exactly by the two
  endpoint character vectors A_λ = χ_λ(W_free σ₂), B_λ = χ_λ(W_free σ₂⁻¹). Likewise
  tr_M(W_e)/tr_M(W_free) = z_D − e·h along the whole family (Lean `trace_interfaceLetter`), which is measured
  here on a grid as a check of the evaluator, not assumed.

EVALUATOR AND ITS VALIDATION
  A self-contained mpmath Hoefsmit seminormal evaluator (same a / a′ / b formulas and SYT conventions as
  `computations/_exact_trace_engine.py`, which needs gmpy2 and is not importable here; no numpy anywhere).
  It is validated against COMMITTED canonical data before any program is solved: the H_3 proton/neutron
  characters (`chi-{proton,neutron}-h3-at-q0-50dps`) and the H_6 deuteron free and bound characters
  (`atom-chi-rust-d`, Rust + MPFR 50 dps). A mismatch there fails the probe; nothing downstream is trusted.

RESULT SHAPE (what the witness records)
  the feasible e-interval under reading 3; whether the three production points e ∈ {0, e_pn, 1} lie in it;
  the feasible power letters; the bond law along the family; the binding form −log(tr ratio) along the family.
  No objective is optimised. No fit, no selection: this is the feasible SET, reported. q₀ enters only through
  the committed `q0Value` string of `y-lambda-at-q0.witness.json`; mpmath 60 dps.
-- Ref: [manuscript] prop:operator-selection-lp; def:markov-axioms-primitive; bean qou-8r6b
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
C = REPO / "computations"
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Yw = json.loads((C / "y-lambda-at-q0.witness.json").read_text(encoding="utf-8"))
assert Yw["q0Anchor"] == "proton"
Q = mp.mpf(Yw["q0Value"])
H = Q - 1 / Q
Z_D = Q ** 3 / (Q ** 2 + 1)
DELTA = (Q - 1) ** 2 * (1 - Q ** -4) / 3                 # pyhecke.constants.flavor_split_leading
D_PN = -(H * (1 - DELTA / 2) / 2)                        # pn_interface_offset, bring_color_weighted
E_PN = -D_PN / H                                          # inverse-crossing weight of the pn letter
HALF = mp.mpf(1) / 2


# ── Hoefsmit seminormal form, mirroring computations/_exact_trace_engine.py ──────────────────────────
def young_cells(shape):
    return [(r, c) for r, row in enumerate(shape) for c in range(row)]


def standard_young_tableaux(shape):
    """All SYT of `shape` as dicts {entry: cell_index}; cells row-major; contents c − r."""
    n = sum(shape)
    cells = young_cells(shape)
    contents = [c - r for r, c in cells]
    out = []

    def fill(entry, filled, avail):
        if entry > n:
            out.append(dict(filled))
            return
        for ci, (r, c) in enumerate(cells):
            if not avail[ci]:
                continue
            if c > 0 and avail[cells.index((r, c - 1))]:
                continue
            if r > 0 and avail[cells.index((r - 1, c))]:
                continue
            filled[entry] = ci
            avail[ci] = False
            fill(entry + 1, filled, avail)
            del filled[entry]
            avail[ci] = True

    fill(1, {}, [True] * len(cells))
    return out, contents


_SIG: dict = {}


def sigmas(shape):
    """Dense seminormal matrices of σ_1..σ_{n-1} (1-indexed generators) on the SYT basis of `shape`."""
    key = tuple(shape)
    if key in _SIG:
        return _SIG[key]
    n = sum(shape)
    syts, contents = standard_young_tableaux(shape)
    dim = len(syts)
    idx = {tuple(sorted(t.items())): i for i, t in enumerate(syts)}
    mats = []
    for k in range(1, n):
        M = [[mp.mpf(0)] * dim for _ in range(dim)]
        for i in range(dim):
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            a = H / (1 - Q ** (-2 * rho))
            ap = H / (1 - Q ** (2 * rho))
            sw = dict(syts[i])
            sw[k], sw[k + 1] = ci1, ci
            j = idx.get(tuple(sorted(sw.items())))
            M[i][i] = a
            if j is not None and j != i:
                M[i][j] = mp.sqrt(abs(a * ap + 1))
        mats.append(M)
    _SIG[key] = (mats, dim)
    return mats, dim


def matmul(X, Y):
    n = len(X)
    return [[mp.fsum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def chi(shape, word):
    """χ_λ(∏ (c σ_g + d)) with 0-indexed generators g in `word` = [(c, d, g), ...]."""
    mats, dim = sigmas(shape)
    M = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(dim)] for i in range(dim)]
    for c, d, g in word:
        S = mats[g]
        op = [[c * S[i][j] + (d if i == j else 0) for j in range(dim)] for i in range(dim)]
        M = matmul(M, op)
    return mp.fsum(M[i][i] for i in range(dim))


def partitions_of(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        return [()]
    out = []
    for k in range(min(n, max_part), 0, -1):
        for rest in partitions_of(n - k, k):
            out.append((k,) + rest)
    return out


# ── the production words, letter for letter (computations/_exact_trace_engine.py::nucleon_word, word) ──
B_P = (mp.mpf(0), HALF, HALF)      # uud: pairs (0,1)=uu → 0, (0,2)=ud → ½, (1,2)=ud → ½
B_N = (HALF, HALF, mp.mpf(1))      # udd: (0,1)=ud → ½, (0,2)=ud → ½, (1,2)=dd → 1


def nucleon_word(b, g0, g1):
    w = []
    for _ in range(3):                         # alternating confinement core (σ₀σ₁⁻¹)³
        w += [(1, mp.mpf(0), g0), (1, -H, g1)]
    w += [(1, -b[0] * H, g0), (1, -b[1] * H, g0), (1, -b[2] * H, g1)]   # quark pairs
    return w + [(1, mp.mpf(0), g0), (1, mp.mpf(0), g0)]                  # gluon self-coupling


def load_y(n):
    return {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"]) for e in Yw["data"]["by_n"][str(n)]}


def load_nucleon(name):
    w = json.loads((C / f"chi-{name}-h3-at-q0-50dps.witness.json").read_text(encoding="utf-8"))
    assert w["q0Anchor"] == "proton"
    return {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["by_partition"]}


def load_atom(tag):
    w = json.loads((C / f"atom-chi-rust-{tag}.witness.json").read_text(encoding="utf-8"))
    atom = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["data"]["atom"]["by_partition"]}
    free = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in w["data"]["free"]["by_partition"]}
    return atom, free, {"computedAt": w["computedAt"], "commitSha": w["commitSha"][:12]}


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    TOL = mp.mpf("1e-40")
    # ── validation 1: H_3 nucleon blocks against the committed characters ──
    P3 = partitions_of(3)
    wp3, wn3 = nucleon_word(B_P, 0, 1), nucleon_word(B_N, 0, 1)
    chi_p, chi_n = load_nucleon("proton"), load_nucleon("neutron")
    dev3 = max(max(abs(chi(l, wp3) - chi_p[l]) for l in P3), max(abs(chi(l, wn3) - chi_n[l]) for l in P3))
    print("H_3 validation worst |χ_eval − χ_committed| =", mp.nstr(dev3, 5))
    check("evaluator_reproduces_committed_H3_proton_and_neutron_characters_to_1e-40", dev3 < TOL,
          "chi-{proton,neutron}-h3-at-q0-50dps; 11-letter production block, alternating core")
    # ── validation 2: H_6 deuteron free and bound words against the committed Rust characters ──
    P6 = partitions_of(6)
    y6 = load_y(6)
    w_free = nucleon_word(B_P, 0, 1) + nucleon_word(B_N, 3, 4)
    w_atom = w_free + [(1, D_PN, 2)]
    atom, free, meta = load_atom("d")
    chi_free = {l: chi(l, w_free) for l in P6}
    chi_atom = {l: chi(l, w_atom) for l in P6}
    dev6f = max(abs(chi_free[l] - free[l]) for l in P6)
    dev6a = max(abs(chi_atom[l] - atom[l]) for l in P6)
    print("H_6 validation worst |χ_eval − χ_committed|: free", mp.nstr(dev6f, 5), " atom", mp.nstr(dev6a, 5))
    check("evaluator_reproduces_committed_H6_deuteron_free_characters_to_1e-40", dev6f < TOL, "atom-chi-rust-d free (include_inter=False), 11 blocks")
    check("evaluator_reproduces_committed_H6_deuteron_bound_characters_to_1e-40", dev6a < TOL, "atom-chi-rust-d atom, bond letter (1, d_pn, gen 2)")
    tr_free = sum(y6[l] * chi_free[l] for l in P6)
    pos = [l for l in P6 if y6[l] > 0]
    print("positive-weight blocks (convention D):", pos)

    # ── the program: endpoint character vectors and the exact feasible interval in e ──
    A = {l: chi(l, w_free + [(1, mp.mpf(0), 2)]) for l in P6}     # χ_λ(W_free σ₂)
    B = {l: chi(l, w_free + [(1, -H, 2)]) for l in P6}            # χ_λ(W_free σ₂⁻¹)
    lo, hi = -mp.inf, mp.inf
    block_constraints = {}
    for l in pos:
        a, b = A[l], B[l]                                          # χ_λ(e) = (1 − e) a + e b = a + e (b − a) ≥ 0
        slope = b - a
        if slope > 0:
            lo = max(lo, -a / slope)
            kind = f"e ≥ {mp.nstr(-a / slope, 12)}"
        elif slope < 0:
            hi = min(hi, -a / slope)
            kind = f"e ≤ {mp.nstr(-a / slope, 12)}"
        else:
            kind = "constant, " + ("feasible" if a >= 0 else "infeasible")
            if a < 0:
                lo, hi = mp.inf, -mp.inf
        block_constraints[str(l)] = {"chi_free_sigma": mp.nstr(a, 30), "chi_free_sigma_inv": mp.nstr(b, 30), "constraint": kind}
        print(f"  block {str(l):<8} χ(W_free σ₂) = {mp.nstr(a, 12):>16}   χ(W_free σ₂⁻¹) = {mp.nstr(b, 12):>16}   ⇒ {kind}")
    feasible_nonempty = lo <= hi
    print(f"feasible interval in e under reading 3: [{mp.nstr(lo, 15)}, {mp.nstr(hi, 15)}]  nonempty={feasible_nonempty}")

    def feasible_at(e):
        return all((1 - e) * A[l] + e * B[l] >= 0 for l in pos)

    production_points = {"sigma (pp-type, e=0)": mp.mpf(0), "production pn (e=e_pn)": E_PN, "sigma_inv (nn-type, e=1)": mp.mpf(1)}
    prod_feas = {k: feasible_at(v) for k, v in production_points.items()}
    print("production points feasible?", prod_feas, " e_pn =", mp.nstr(E_PN, 20))
    # the composite at e_pn must reproduce the committed bound characters (affine identity), and fail reading 3 on (5,1)
    chi51_epn = (1 - E_PN) * A[(5, 1)] + E_PN * B[(5, 1)]
    check("affine_family_at_e_pn_reproduces_committed_bound_chi_51_to_1e-40", abs(chi51_epn - atom[(5, 1)]) < TOL,
          "χ_(5,1)(W_free L_e) = (1−e)χ(W_free σ) + eχ(W_free σ⁻¹) at e = e_pn vs atom-chi-rust-d")
    check("production_pn_letter_is_infeasible_under_reading3", not prod_feas["production pn (e=e_pn)"], "corroborates qou-7dal: χ_(5,1)(atom) < 0")
    check("unit_letter_free_product_is_feasible", all(chi_free[l] >= 0 for l in pos), "Lean feasible_unit_iff")

    # ── the bond law and the binding form along the family, on a grid (checks trace_interfaceLetter) ──
    grid = [mp.mpf(k) / 20 for k in range(0, 21)] + [E_PN]
    worst_bond = mp.mpf(0)
    family_rows = []
    for e in sorted(grid):
        chis = {l: (1 - e) * A[l] + e * B[l] for l in P6}
        tr = sum(y6[l] * chis[l] for l in P6)
        ratio = tr / tr_free
        pred = Z_D - e * H
        worst_bond = max(worst_bond, abs(ratio - pred))
        feas = all(chis[l] >= 0 for l in pos)
        viol = [str(l) for l in pos if chis[l] < 0]
        family_rows.append({"e": mp.nstr(e, 20), "tr_ratio": mp.nstr(ratio, 30), "z_minus_eh": mp.nstr(pred, 30),
                            "neg_log_ratio": mp.nstr(-mp.log(ratio), 20) if ratio > 0 else None,
                            "reading3_feasible": feas, "violating_blocks": viol})
    check("bond_law_tr_ratio_eq_z_minus_eh_along_family_to_1e-40", worst_bond < TOL, "Lean trace_interfaceLetter; 22 grid points")
    grid_feas = [r for r in family_rows if r["reading3_feasible"]]
    check("grid_feasibility_agrees_with_closed_form_interval",
          all(r["reading3_feasible"] == (lo <= mp.mpf(r["e"]) <= hi) for r in family_rows), "22 grid points vs [lo, hi]")

    # ── power letters σ₂^m ──
    power_rows = {}
    for m in range(-3, 4):
        letter = [(1, mp.mpf(0), 2)] * m if m >= 0 else [(1, -H, 2)] * (-m)
        chis = {l: chi(l, w_free + letter) for l in P6}
        tr = sum(y6[l] * chis[l] for l in P6)
        power_rows[str(m)] = {"tr_ratio": mp.nstr(tr / tr_free, 30), "reading3_feasible": all(chis[l] >= 0 for l in pos),
                              "violating_blocks": [str(l) for l in pos if chis[l] < 0], "chi_two_row": {str(l): mp.nstr(chis[l], 20) for l in pos}}
        print(f"  σ₂^{m:+d}: tr ratio {mp.nstr(tr / tr_free, 15)}  feasible={power_rows[str(m)]['reading3_feasible']}  viol={power_rows[str(m)]['violating_blocks']}")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("composition-feasibility-a2", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0_anchor_reason": "q0 read from the committed y-lambda-at-q0 witness string; evaluator validated against committed Rust/MPFR characters",
        "description": ("PROBE (bean qou-8r6b): the composition feasibility program at A = 2 on the alphabet (1−e)σ₂ + eσ₂⁻¹, solved in closed "
                        "form (affine in e). Evaluator validated to 1e-40 against committed H_3 and H_6 canonical characters. Reports the "
                        "feasible e-interval under reading 3, the production points' status, the bond law tr ratio = z_D − e h along the "
                        "family, and the power letters. No objective; nothing selected; nothing wired."),
        "weight_family": "markov_y_lambda_convention_D",
        "evaluator": "self-contained mpmath Hoefsmit seminormal (mirrors _exact_trace_engine.py), 60 dps",
        "committed_inputs": {"atom_chi_rust_d": meta, "chi_h3": "chi-{proton,neutron}-h3-at-q0-50dps", "y": "y-lambda-at-q0 (n=6)"},
        "validation_worst_abs_dev": {"H3": mp.nstr(dev3, 5), "H6_free": mp.nstr(dev6f, 5), "H6_atom": mp.nstr(dev6a, 5)},
        "z_D": mp.nstr(Z_D, 50), "h": mp.nstr(H, 50), "d_pn": mp.nstr(D_PN, 50), "e_pn": mp.nstr(E_PN, 50),
        "positive_weight_blocks": [str(l) for l in pos],
        "block_constraints": block_constraints,
        "feasible_interval_e": {"lo": mp.nstr(lo, 30), "hi": mp.nstr(hi, 30), "nonempty": feasible_nonempty},
        "production_points_feasible": {k: v for k, v in prod_feas.items()},
        "family_rows": family_rows,
        "bond_law_worst_abs_dev": mp.nstr(worst_bond, 5),
        "power_letters": power_rows,
        "tr_M_free": mp.nstr(tr_free, 50),
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
