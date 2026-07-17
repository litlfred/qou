#!/usr/bin/env python3
"""Δ_λ per-block magnitude-deficit profile — target profile for the levers.

Companion to `delta_lambda_l1_ceiling_sign_prune.py`. The ℓ¹-ceiling prune
shows a *magnitude-adding* ingredient is necessary; this script tells the
magnitude-side levers (z2bn fibre R(q,x), w5tg occupancy, thb7 universal-ρ,
PROBE-2 A=4 interface) **where** the missing ℓ¹ mass must go.

Two well-defined, fit-free quantities per isotope (the per-λ *attribution*
of the deficit is NOT unique — 1 equation, n unknowns — so we report only
what is basis-independent):

1. **ℓ¹ concentration.** Rank partitions by |c_λ| = |y_λ χ^λ dim_λ|; report
   the cumulative ℓ¹ fraction. Tells the levers which blocks already carry
   the mass (and thus which a multiplicative re-weighting would amplify).

2. **Irreducible magnitude shortfall.** Even at perfect sign alignment the
   reachable magnitude is ‖c‖₁; the shortfall S = |target| − ‖c‖₁ is the
   ℓ¹ mass that a magnitude-adding object MUST contribute (a lower bound,
   since real closures also lose some to residual cancellation). Report S
   both absolutely (m_e units) and as a fraction of |target|.

Inputs READ from canonical pinned witnesses (no recompute) — env-skew-immune.

Producer for: computations/delta-lambda-magnitude-deficit-profile.witness.json
"""
from __future__ import annotations
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import json, math, os, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))


def dim_irrep(part):
    n = sum(part); maxc = part[0]; col = [0] * maxc
    for r in part:
        for j in range(r):
            col[j] += 1
    hooks = 1
    for i, r in enumerate(part):
        for j in range(r):
            hooks *= (r - j - 1) + (col[j] - i - 1) + 1
    return math.factorial(n) // hooks


def conj(part):
    return [sum(1 for r in part if r > j) for j in range(part[0])]


def sgn_w0_young(part):
    s = 1
    for m in part:
        if (m * (m - 1) // 2) % 2 == 1:
            s = -s
    return s


def delta_sgndim(part):
    return sgn_w0_young(conj(part)) * dim_irrep(part)


M_E_MEV = 0.51099895069
ISOTOPES = {
    "D":   ("atom-chi-rust-d.witness.json",   "6",  2.224566, 2),
    "T":   ("atom-chi-rust-t.witness.json",   "9",  8.481798, 3),
    "3He": ("atom-chi-rust-3he.witness.json", "9",  7.718043, 3),
    "4He": ("atom-chi-rust-4he.witness.json", "12", 28.295673, 4),
}


def main():
    ywit = os.path.join(HERE, "y-lambda-at-q0.witness.json")
    ydat = json.load(open(ywit))["data"]["by_n"]
    q0 = json.load(open(ywit))["parameters"]["q_0"]

    out_rows = {}
    for name, (chif, nkey, B, A) in ISOTOPES.items():
        chi = json.load(open(os.path.join(HERE, chif)))["data"]["atom"]["by_partition"]
        yl = {tuple(e["partition"]): float(e["y_at_q0_50dps"]) for e in ydat[nkey]}
        terms = []
        for e in chi:
            p = tuple(e["partition"])
            d = delta_sgndim(list(p))
            c = yl[p] * float(e["chi_lambda"]) * d
            terms.append({"partition": list(p), "dim": dim_irrep(list(p)),
                          "sign": sgn_w0_young(conj(list(p))),
                          "contrib": c, "abs_contrib": abs(c)})
        l1 = sum(t["abs_contrib"] for t in terms)
        net = sum(t["contrib"] for t in terms)
        target = -B / M_E_MEV
        # ell1 concentration
        terms.sort(key=lambda t: t["abs_contrib"], reverse=True)
        cum = 0.0
        for t in terms:
            cum += t["abs_contrib"]
            t["cum_l1_frac"] = cum / l1
        shortfall = abs(target) - l1   # irreducible magnitude the levers must add
        out_rows[name] = {
            "A": A, "B_AME_MeV": B, "target_units_m_e": target,
            "l1_ceiling": l1, "net_sum": net,
            "irreducible_shortfall_units_m_e": shortfall,
            "irreducible_shortfall_frac_of_target": shortfall / abs(target),
            "dominant_blocks": [
                {"partition": t["partition"], "abs_contrib": t["abs_contrib"],
                 "cum_l1_frac": t["cum_l1_frac"], "sign": t["sign"]}
                for t in terms if t["cum_l1_frac"] <= 0.901 or t is terms[0]
            ][:6],
            "n_blocks_for_90pct_l1": next(
                (i + 1 for i, t in enumerate(terms) if t["cum_l1_frac"] >= 0.90), len(terms)),
        }

    witness = {
        "engine": "python",
        "engineVersion": "pure-arithmetic-on-canonical-witnesses",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "delta-lambda-magnitude-deficit-profile",
        "scriptFile": "delta_lambda_magnitude_deficit_profile.py",
        "scriptHash": hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12],
        "description": (
            "Per-block magnitude-deficit profile for the Δ_λ binding closure. "
            "Companion to the ℓ¹-ceiling prune: gives the magnitude-side levers "
            "(z2bn/w5tg/thb7/PROBE-2) the ℓ¹ concentration (which blocks carry "
            "the mass) and the irreducible magnitude shortfall S=|target|−‖c‖₁ "
            "they must supply. Per-λ deficit ATTRIBUTION is non-unique (1 eq, n "
            "unknowns) and is deliberately NOT reported. Pure arithmetic on "
            "canonical witnesses — env-skew-immune."
        ),
        "parameters": {"q_0": q0, "m_e_MeV": M_E_MEV},
        "data": out_rows,
    }
    import sys as _sys  # noqa: E402
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out = WitnessBuilder.wrap_legacy(
        "delta-lambda-magnitude-deficit-profile", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
    ).save()

    for name, r in out_rows.items():
        doms = ", ".join(f"{d['partition']}({d['sign']:+d})" for d in r["dominant_blocks"][:4])
        print(f"{name:>4}  shortfall={r['irreducible_shortfall_units_m_e']:7.3f} m_e "
              f"({r['irreducible_shortfall_frac_of_target']*100:4.1f}% of target)  "
              f"90% ℓ¹ in {r['n_blocks_for_90pct_l1']} blocks  | top: {doms}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
