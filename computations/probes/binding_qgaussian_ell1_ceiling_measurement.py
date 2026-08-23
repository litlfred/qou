#!/usr/bin/env python3
"""z2bn binding q-Gaussian ℓ¹-ceiling measurement — does the q-deformed
magnitude breach the sign-only ceiling?

Context
-------
The per-block binding closure (Track D / Option-E) is

    B(K)/m_e  =  Σ_λ  y_λ(q_0) · χ^λ(β_K) · Δ_λ(K).

`delta_lambda_l1_ceiling_sign_prune.py` proved a (b) STRUCTURAL exclusion:
with the **classical integer** magnitude |Δ_λ| = dim_λ held fixed, *no*
sign/chirality-only re-derivation can close the deficit — the ℓ¹ ceiling
‖c_cl‖₁ = Σ_λ |y_λ χ^λ dim_λ| is only 36–59 % of the binding target, so a
41–64 % *magnitude-adding* ingredient is required.

The z2bn fibre-kernel lever proposes exactly such a magnitude: the binding
q-Gaussian replaces the classical Wedderburn dimension dim_λ by the
**symmetric quantum dimension** dim_q(λ) = [n]_q! / ∏_c [h_c]_q evaluated at
the substrate anchor q_0 (the q-deformation underlying
`BindingQGaussianHabiro.lean`, S(m) = Σ_{λ⊢m} dim_q(λ)). Since q_0 ≈ 1.110 >
1, every q-integer [k]_q > k, so dim_q(λ) ≥ dim_λ with equality only for the
single-row/single-column λ.

The measurement (this script)
-----------------------------
Hold {y_λ, χ^λ} at their canonical pinned values (same witnesses the sign
prune reads) and replace dim_λ → dim_q(λ) at q_0. Report per isotope the
q-deformed ℓ¹ ceiling

    ‖c_q‖₁ = Σ_λ |y_λ χ^λ dim_q(λ)|     and     ‖c_q‖₁ / |target|,

the inflation factor ‖c_q‖₁/‖c_cl‖₁, and the sign-twisted signed net
Σ_λ y_λ χ^λ sgn(w_0^{S_{λ'}}) dim_q(λ). The decision question: does the
q-Gaussian magnitude breach the 0.36–0.59 classical ceiling (ratio ≥ 1 ⟹
the q-deformation alone could in principle supply the missing magnitude;
ratio < 1 ⟹ the prune extends to the q-Gaussian-magnitude-only sub-class).

This is a *measurement*, not a closure: the q-inflation factor is read off,
nothing is fitted (anti-flip-flop discipline). Evaluated at BOTH the proton
anchor q_0 and the muon anchor for anchor-stability of the inflation factor.

Inputs are READ from canonical pinned witnesses (y-lambda-at-q0,
atom-chi-rust-*) — no q_0 re-solve, no tr_M recompute, no pyhecke; dim_q is
pure q-combinatorics (hook lengths + q-integers) at 50 dps. Env-skew-immune.

Producer for: computations/binding-qgaussian-ell1-ceiling-measurement.witness.json
"""
from __future__ import annotations

# Path bridge (probes/ subdirectory → flat compute namespace).
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401,E402
del _sys, _Path, _bridge

import json
import os
import sys
from pathlib import Path

from mpmath import mp, mpf  # noqa: E402

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

M_E_MEV = 0.51099895069  # CODATA 2022 CAL-1 (matches the sign-prune script)

# name : (chi witness, n=3A key, B_AME MeV, Z, N, A)  — identical to the prune
ISOTOPES = {
    "D":   ("atom-chi-rust-d.witness.json",   "6",  2.224566, 1, 1, 2),
    "T":   ("atom-chi-rust-t.witness.json",   "9",  8.481798, 1, 2, 3),
    "3He": ("atom-chi-rust-3he.witness.json", "9",  7.718043, 2, 1, 3),
    "4He": ("atom-chi-rust-4he.witness.json", "12", 28.295673, 2, 2, 4),
}


# ---- partition / hook combinatorics ----
def _cols(part):
    maxc = part[0]
    col = [0] * maxc
    for r in part:
        for j in range(r):
            col[j] += 1
    return col


def hooks(part):
    """All hook lengths of the Young diagram of `part`."""
    col = _cols(part)
    hs = []
    for i, r in enumerate(part):
        for j in range(r):
            hs.append((r - j - 1) + (col[j] - i - 1) + 1)
    return hs


def conj(part):
    return [sum(1 for r in part if r > j) for j in range(part[0])]


def sgn_w0_young(part):
    """Sign of the longest element of S_part = ∏ S_{part_i}: (-1)^{Σ m(m-1)/2}."""
    s = 1
    for m in part:
        if (m * (m - 1) // 2) % 2 == 1:
            s = -s
    return s


def dim_classical(part):
    """Hook-length formula: |S_n irrep λ| = n! / ∏ hooks."""
    import math
    h = 1
    for x in hooks(part):
        h *= x
    return math.factorial(sum(part)) // h


def _qint(k, q):
    """Symmetric q-integer [k]_q = (q^k − q^−k)/(q − q^−1)."""
    return (q**k - q**(-k)) / (q - 1 / q)


def dim_q(part, q):
    """Symmetric quantum dimension dim_q(λ) = [n]_q! / ∏_c [h_c]_q."""
    n = sum(part)
    num = mpf(1)
    for k in range(1, n + 1):
        num *= _qint(k, q)
    den = mpf(1)
    for hlen in hooks(part):
        den *= _qint(hlen, q)
    return num / den


def _muon_q0():
    """The documented muon anchor, imported — never retyped.

    The fallback here was ``mpf("1.1099785955541810")``, a hand-typed copy of
    what ``q_muon_at()`` derived *at the time it was typed*. That copy is now
    the CODATA-2018 value while ``q_muon_at()`` reads the live NIST ratio, so
    the two branches of this function returned different numbers — silently,
    and only when the import failed. Raising beats guessing: if the substrate
    is not importable this probe cannot know the anchor, and saying so is more
    useful than quietly answering with a pin that was retired.

    Same fix, same reason, as ``flavor_split_alpha_dilog_expansion_probe``
    (bean qou-khac).
    """
    try:
        from qou_substrate.constants import q_muon_at
        return mpf(str(q_muon_at()))
    except Exception as exc:  # noqa: BLE001 — re-raised with the reason
        raise RuntimeError(
            "muon q0 unavailable: qou_substrate.constants.q_muon_at could not "
            "be imported, and this probe will not substitute a hand-typed pin "
            "(qou-khac). Put tools/qou-substrate/python on PYTHONPATH."
        ) from exc


def _provenance(path):
    d = json.load(open(path))
    return {"file": os.path.basename(path), "scriptHash": d.get("scriptHash"),
            "scriptCommitSha": d.get("scriptCommitSha"),
            "computedAt": d.get("computedAt")}


def measure(q, label, ydat, sources):
    rows = []
    any_breach = False
    for name, (chif, nkey, B, Z, N, A) in ISOTOPES.items():
        chipath = os.path.join(COMP, chif)
        chi = json.load(open(chipath))["data"]["atom"]["by_partition"]
        if label == "proton_q0":
            sources[f"chi_{name}"] = _provenance(chipath)
        yl = {tuple(e["partition"]): mpf(str(e["y_at_q0_50dps"])) for e in ydat[nkey]}

        l1_cl = mpf(0)
        l1_q = mpf(0)
        net_q = mpf(0)
        for e in chi:
            p = tuple(e["partition"])
            w = yl[p] * mpf(str(e["chi_lambda"]))
            dcl = dim_classical(list(p))
            dq = dim_q(list(p), q)
            l1_cl += abs(w * dcl)
            l1_q += abs(w * dq)
            net_q += w * sgn_w0_young(conj(list(p))) * dq
        target = mpf(-B) / mpf(M_E_MEV)  # binding = negative energy contribution
        ceil_cl = l1_cl / abs(target)
        ceil_q = l1_q / abs(target)
        breach = ceil_q >= 1
        any_breach = any_breach or breach
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME_MeV": B,
            "target_units_m_e": str(target),
            "l1_ceiling_classical": str(l1_cl),
            "l1_ceiling_qgauss": str(l1_q),
            "q_inflation_factor": str(l1_q / l1_cl),
            "classical_ceiling_over_target": str(ceil_cl),
            "qgauss_ceiling_over_target": str(ceil_q),
            "qgauss_signed_net_over_target": str(net_q / target),
            "breaches_target": bool(breach),
        })
    return {"anchor": label, "q0": str(q), "rows": rows,
            "any_isotope_breaches_target": any_breach}


def main() -> int:
    ywit = os.path.join(COMP, "y-lambda-at-q0.witness.json")
    ydat = json.load(open(ywit))["data"]["by_n"]
    sources = {"y_lambda": _provenance(ywit)}

    rp = measure(mpf(Q_50_DIGIT_STR), "proton_q0", ydat, sources)
    rm = measure(_muon_q0(), "muon_q0", ydat, sources)

    print("z2bn binding q-Gaussian ℓ¹-ceiling measurement")
    print("=" * 64)
    for r in (rp, rm):
        print(f"\n[{r['anchor']}]  q0={mp.nstr(mpf(r['q0']),9)}")
        print(f"  {'iso':>4}{'cl/tgt':>8}{'q/tgt':>8}{'infl':>8}{'qnet/tgt':>10}"
              f"{'breach':>8}")
        for d in r["rows"]:
            print(f"  {d['atom']:>4}"
                  f"{float(d['classical_ceiling_over_target']):>8.3f}"
                  f"{float(d['qgauss_ceiling_over_target']):>8.3f}"
                  f"{float(d['q_inflation_factor']):>8.4f}"
                  f"{float(d['qgauss_signed_net_over_target']):>10.3f}"
                  f"{('YES' if d['breaches_target'] else 'no'):>8}")

    # anchor-stability of the inflation factor (per isotope)
    infl_drift = max(
        abs(mpf(a["q_inflation_factor"]) - mpf(b["q_inflation_factor"]))
        for a, b in zip(rp["rows"], rm["rows"])
    )
    infl_max = max(float(d["q_inflation_factor"]) for d in rp["rows"])
    print(f"\n  max q-inflation (proton anchor): {infl_max:.4f}×")
    print(f"  inflation anchor drift: {mp.nstr(infl_drift,4)}")
    verdict_breach = rp["any_isotope_breaches_target"]
    print(f"  any isotope q-ceiling ≥ target: {verdict_breach}")
    if not verdict_breach:
        print("  VERDICT: q-Gaussian magnitude does NOT breach the ceiling —")
        print("  the sign-prune (b) exclusion EXTENDS to the q-deformed magnitude;")
        print("  the missing 41–64% needs many-body terms, not dim_q inflation alone.")
    else:
        print("  VERDICT: q-Gaussian magnitude BREACHES the ceiling for ≥1 isotope —")
        print("  dim_q inflation is a viable magnitude-supplier candidate (motivates")
        print("  the owner-gated SW-period keystone of the z2bn fibre kernel).")

    w = WitnessBuilder("binding-qgaussian-ell1-ceiling-measurement", engine="mpmath")
    w.set_description(
        "z2bn binding q-Gaussian ℓ¹-ceiling measurement. Holds canonical "
        "{y_λ, χ^λ} fixed and replaces the classical Wedderburn dim_λ by the "
        "symmetric quantum dimension dim_q(λ)=[n]_q!/∏[h_c]_q at the substrate "
        "anchor q_0 (the BindingQGaussianHabiro magnitude). Measures whether the "
        "q-deformed ℓ¹ ceiling ‖c_q‖₁/|target| breaches the 0.36–0.59 classical "
        "ceiling that the sign-only prune (delta-lambda-l1-ceiling-sign-prune) "
        "proved insufficient. Reports per-isotope q-inflation factor + signed net "
        "at both proton and muon anchors. Measurement, not a fit (anti-flip-flop). "
        "Pure q-combinatorics on canonical y_λ+χ^λ witnesses — env-skew-immune."
    )
    w.add_data("m_e_MeV", str(M_E_MEV))
    w.add_data("proton_anchor", rp)
    w.add_data("muon_anchor", rm)
    w.add_data("max_q_inflation_proton", str(infl_max))
    w.add_data("inflation_anchor_drift", str(infl_drift))
    w.add_assertion(
        name="qgauss_inflation_anchor_stable",
        computed=1 if infl_drift < mpf("1e-3") else 0,
        expected=1,
        source="the q-inflation factor of the ℓ¹ ceiling is stable (<1e-3) "
               "between the proton and muon anchors",
    )
    w.save()
    print("\n  Witness: binding-qgaussian-ell1-ceiling-measurement.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
