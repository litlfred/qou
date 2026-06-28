#!/usr/bin/env python3
"""Δ_λ route-(i) probe — does a QUANTUM-DIMENSION reweighting of |Δ_λ| supply
the ℓ¹ shortfall the sign-only prune says is needed?

The ℓ¹-ceiling prune (`delta_lambda_l1_ceiling_sign_prune.py`) shows a
*magnitude-adding* ingredient is necessary and names three routes:
  (i)  re-derive the block magnitude |Δ_λ| ≠ dim_λ,
  (ii) re-weight y_λ,
  (iii) add a term beyond the single Σ_λ sum (T2–T6 / A=4 interface).

This probes the cheapest, route (i): replace the proven classical magnitude
|Δ_λ| = dim_λ (Wedderburn) by the **quantum dimension**
  dim_q,λ = [n]_q! / ∏_cells [h(cell)]_q ,
with the balanced q-integer [k]_q = (q^k − q^{−k})/(q − q^{−1}), evaluated at
the canonical substrate q_0, and recompute the ℓ¹ ceiling
‖c_q‖₁ = Σ_λ |y_λ χ^λ dim_q,λ|.

Result (this script): ‖c_q‖₁/|target| ∈ [0.46, 0.79] < 1 for D/T/³He/⁴He.
So **route (i) with the balanced quantum dimension does NOT, on its own,
supply the shortfall** — but it lifts the ceiling substantially for the
heavier isotopes (⁴He 0.41 → 0.79, ³He 0.59 → 0.77), i.e. the q-deformation
accounts for a large part of the missing magnitude. This is constructive
evidence for the fibre q-kernel direction (z2bn, #2899): the q-deformation
is a big piece, just not the whole closure by this single convention.

SCOPE (a) — scope-limited negative. This excludes ONLY the specific
balanced-[k]_q hook-content quantum dimension *as the sole magnitude fix*.
Other q-dimension conventions (unbalanced (1−q^k)/(1−q), the principal
specialization of the Schur function, the Markov-trace tr_M(1) weight) are
NOT tested here, and route (i) combined with (ii)/(iii) is not excluded.
This is NOT a structural (b) exclusion — no invariant forbids a different
magnitude rule.

Inputs READ from canonical pinned witnesses (no recompute, mpmath 50 dps on
the stored y_λ, χ^λ) — env-skew-immune.

Producer for: computations/delta-lambda-qdim-route-probe.witness.json
"""
from __future__ import annotations
import json, math, os, hashlib, datetime
from mpmath import mp, mpf

mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))


def dim_irrep(part):
    n = sum(part); maxc = part[0]; col = [0] * maxc
    for r in part:
        for j in range(r):
            col[j] += 1
    h = 1
    for i, r in enumerate(part):
        for j in range(r):
            h *= (r - j - 1) + (col[j] - i - 1) + 1
    return math.factorial(n) // h


def hook_lengths(part):
    maxc = part[0]; col = [0] * maxc
    for r in part:
        for j in range(r):
            col[j] += 1
    out = []
    for i, r in enumerate(part):
        for j in range(r):
            out.append((r - j - 1) + (col[j] - i - 1) + 1)
    return out


def conj(part):
    return [sum(1 for r in part if r > j) for j in range(part[0])]


def sgn_w0_young(part):
    s = 1
    for m in part:
        if (m * (m - 1) // 2) % 2 == 1:
            s = -s
    return s


def qint(k, q):
    return (q**k - q**(-k)) / (q - q**(-1))


def dim_q(part, q):
    n = sum(part)
    num = mpf(1)
    for k in range(1, n + 1):
        num *= qint(k, q)
    den = mpf(1)
    for h in hook_lengths(part):
        den *= qint(h, q)
    return num / den


M_E_MEV = mpf("0.51099895069")
ISOTOPES = {
    "D":   ("atom-chi-rust-d.witness.json",   "6",  2.224566),
    "T":   ("atom-chi-rust-t.witness.json",   "9",  8.481798),
    "3He": ("atom-chi-rust-3he.witness.json", "9",  7.718043),
    "4He": ("atom-chi-rust-4he.witness.json", "12", 28.295673),
}


def main():
    ywit = os.path.join(HERE, "y-lambda-at-q0.witness.json")
    ydat = json.load(open(ywit))["data"]["by_n"]
    q0 = mpf(json.load(open(ywit))["parameters"]["q_0"])

    rows = []
    all_below = True
    for name, (chif, nkey, B) in ISOTOPES.items():
        chi = json.load(open(os.path.join(HERE, chif)))["data"]["atom"]["by_partition"]
        yl = {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in ydat[nkey]}
        l1_classic = mpf(0)
        l1_qdim = mpf(0)
        for e in chi:
            p = tuple(e["partition"])
            y = yl[p]; c = mpf(e["chi_lambda"])
            l1_classic += abs(y * c * dim_irrep(list(p)))
            l1_qdim += abs(y * c * dim_q(list(p), q0))
        target = mpf(B) / M_E_MEV
        ratio = l1_qdim / abs(target)
        if ratio >= 1:
            all_below = False
        rows.append({
            "atom": name, "B_AME_MeV": B,
            "target_units_m_e": float(target),
            "l1_classic": float(l1_classic),
            "l1_qdim": float(l1_qdim),
            "qdim_over_classic": float(l1_qdim / l1_classic),
            "qdim_ceiling_over_target": float(ratio),
        })

    witness = {
        "engine": "mpmath",
        "engineVersion": "mpmath 50dps on canonical witnesses",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "delta-lambda-qdim-route-probe",
        "scriptFile": "delta_lambda_qdim_route_probe.py",
        "scriptHash": hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12],
        "description": (
            "Route-(i) probe: replace |Δ_λ|=dim_λ by the balanced quantum "
            "dimension dim_q,λ=[n]_q!/∏[hook]_q at q_0 and recompute the ℓ¹ "
            "ceiling. ‖c_q‖₁/|target| ∈ [0.46,0.79] < 1 for D/T/³He/⁴He ⟹ "
            "balanced-q-dim reweighting alone does NOT supply the shortfall, "
            "but lifts the heavy-isotope ceiling a lot (⁴He 0.41→0.79) — "
            "constructive evidence for the fibre q-kernel (z2bn #2899). "
            "SCOPE (a) scope-limited negative: this convention as SOLE fix "
            "only; other q-dim conventions and route (i)+(ii)/(iii) NOT "
            "excluded; no invariant ⟹ not a (b) exclusion."
        ),
        "scope": "(a) scope-limited-negative — balanced-[k]_q quantum dimension as the sole magnitude fix",
        "qdim_convention": "balanced [k]_q=(q^k-q^-k)/(q-q^-1); dim_q,λ=[n]_q!/∏_cells[hook]_q",
        "parameters": {"q_0": float(q0), "m_e_MeV": float(M_E_MEV)},
        "data": {"rows": rows, "all_qdim_ceilings_below_target": all_below},
        "allPassed": all_below,
    }
    out = os.path.join(HERE, "delta-lambda-qdim-route-probe.witness.json")
    json.dump(witness, open(out, "w"), indent=1)

    print(f"{'iso':>4}{'‖c‖₁ classic':>14}{'‖c‖₁ dim_q':>13}{'ratio':>8}"
          f"{'|target|':>10}{'dimq/tgt':>10}")
    for r in rows:
        print(f"{r['atom']:>4}{r['l1_classic']:>14.4f}{r['l1_qdim']:>13.4f}"
              f"{r['qdim_over_classic']:>8.4f}{r['target_units_m_e']:>10.4f}"
              f"{r['qdim_ceiling_over_target']:>10.4f}")
    print(f"\nall q-dim ceilings below target: {all_below}  (route (i) alone insufficient, scope (a))")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
