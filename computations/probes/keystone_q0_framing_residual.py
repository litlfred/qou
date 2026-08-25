#!/usr/bin/env python3
"""Keystone geometric W_λ — the q₀ residual is the framing monomial θ_λ^f = q₀^{f·c(λ)}, which
VANISHES on the self-conjugate electron block (no archimedean continuation there). No fit.

Context. #3685 derived the value map `d_q(λ) = [mark]_q` (McKay 2I↔Ê₈ ∘ A₅⊂S₅), and #3699 formalized
its two new members sorry-free. The concrete colored-WRT vacuum row is (de-opaqued gate, #3662)

    bwS0Concrete(λ)(q) = S_{0λ}(q) · θ_λ(q)^f = (d_q(λ)/D(q)) · q^{f·c(λ)},

with θ_λ = q^{c(λ)} the ribbon twist (KeystoneModularTwist), c(λ) the content sum, f the Seifert
framing forced by Σ(2,3,5). The framework's Verlinde/Plancherel value is the framing-STRIPPED
bwS0(λ) = d_q(λ)/D.

Key structural point (this probe). The numerator d_q(λ) = [mark]_q is a Laurent polynomial — a GLOBAL
function of q, identical at roots of unity and at q₀ (no Habiro completion needed for it). D(q) and
θ_λ^f are likewise global. So the ENTIRE fibre→observable "archimedean continuation" residual reduces
to the single framing factor

    θ_λ(q₀)^f = q₀^{f·c(λ)},

which is a PHASE (|·|=1) at a root of unity but a real factor ≠ 1 at q₀ > 1 for c(λ) ≠ 0 (the #3652
refutation). Since c(λ') = −c(λ) (proved chirality law) and c(λ) = 0 iff λ is self-conjugate, and the
ONLY self-conjugate n=5 block is the ELECTRON (3,1,1) (the A₅-split mark-6 McKay node):

    → the electron block has c = 0, hence θ_λ^f = 1 for ANY framing f, hence
      bwS0Concrete((3,1,1))(q₀) = d_{q₀}((3,1,1))/D = ([5]_{q₀}+1)/D EXACTLY — NO residual, no
      continuation. The geometric q₀ value for the electron block is DERIVED outright.

    → every non-self-conjugate block carries the explicit framing residual q₀^{f·c(λ)} (the true open
      piece), a single content-sum monomial, opposite on a conjugate pair (θ_{λ'}^f = θ_λ^{-f}).

This discharges the #3681 Habiro-rigidity carrier CONCRETELY for the electron block (rigidity is
trivial there — the value is a Laurent polynomial, no root-of-unity reconstruction needed) and
quantifies the residual per block for the rest. No fit; no free constant; the framing f is the forced
Seifert datum (the c=0 electron result is f-independent, hence robust).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_MP  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# q0 comes from the pin table, never a literal. This held
# `1.1099785955541805`, the SUPERSEDED muon value -- it matches
# neither current pin, so nothing could compare it against
# anything. Owner ruling 2026-08-24, bean `qou/ftuv`.
Q0 = Q_MP

PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
# McKay marks of the A₅-factoring node for each conjugation class (from #3685).
MARK = {(5,): 1, (1, 1, 1, 1, 1): 1, (4, 1): 4, (2, 1, 1, 1): 4,
        (3, 2): 5, (2, 2, 1): 5, (3, 1, 1): 6}


def qint(m, q=Q0):
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def q_factorial(m, q=Q0):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k, q)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def d_q(lam, q=Q0):
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h, q)
    return q_factorial(sum(lam), q) / den


def content_sum(lam):
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def conj(lam):
    m = lam[0]
    return tuple(sum(1 for r in lam if r > j) for j in range(m))


def run():
    D2 = mp.fsum(d_q(l) ** 2 for l in PARTS5)
    D = mp.sqrt(D2)
    rows = []
    for l in PARTS5:
        c = content_sum(l)
        rows.append({
            "lambda": list(l), "mark": MARK[l], "content_sum": c,
            "self_conjugate": conj(l) == l,
            "d_q": float(d_q(l)), "bwS0": float(d_q(l) / D),
            # framing residual vs f: q0^{f*c}. Report exponent base and the f-independent c=0 fact.
            "framing_residual_exponent_c": c,
            "framing_trivial_any_f": c == 0,
        })
    # electron = the unique self-conjugate block: c=0 => residual 1 for any f.
    electron = next(r for r in rows if tuple(r["lambda"]) == (3, 1, 1))
    self_conj = [r for r in rows if r["self_conjugate"]]
    electron_no_residual = electron["content_sum"] == 0 and len(self_conj) == 1
    # chirality: c(lambda') = -c(lambda) on every pair.
    chirality_ok = all(content_sum(conj(l)) == -content_sum(l) for l in PARTS5)
    return {"q0": float(Q0), "D2": float(D2), "rows": rows,
            "electron_zero_framing_residual_any_f": electron_no_residual,
            "chirality_c_conj_eq_neg_c": chirality_ok,
            "electron_q0_value_bwS0": electron["bwS0"]}


def report(res):
    print("# Keystone geometric W_λ — the q₀ residual is θ_λ^f = q₀^{f·c(λ)} (no fit)\n")
    print(f"q₀ = {res['q0']:.10f}   D² = Σd_q² = {res['D2']:.6f}\n")
    print("The whole fibre→observable residual is the framing monomial `θ_λ^f = q₀^{f·c(λ)}` "
          "(d_q(λ)=[mark]_q is already a global Laurent polynomial; D and θ^f are global too).\n")
    print("| λ | mark | c(λ) | self-conj | d_q(λ) | bwS0=d_q/D | framing residual q₀^{f·c} |")
    print("|---|--:|--:|:-:|--:|--:|---|")
    for r in res["rows"]:
        lam = "(" + ",".join(map(str, r["lambda"])) + ")"
        resid = "1  (any f)" if r["content_sum"] == 0 else f"q₀^({r['content_sum']}·f)"
        print(f"| {lam} | {r['mark']} | {r['content_sum']:+d} | {r['self_conjugate']} | "
              f"{r['d_q']:.5f} | {r['bwS0']:.5f} | {resid} |")
    print(f"\n- **Electron block (3,1,1) — the unique self-conjugate n=5 block (A₅-split mark-6 node) — "
          f"has c=0, so θ_λ^f = 1 for ANY framing f: {res['electron_zero_framing_residual_any_f']}.** "
          f"Hence bwS0Concrete((3,1,1))(q₀) = d_{{q₀}}((3,1,1))/D = ([5]_q₀+1)/D = "
          f"{res['electron_q0_value_bwS0']:.6f} EXACTLY — no archimedean continuation, no Habiro "
          f"reconstruction. The geometric q₀ value is derived outright for this block.")
    print(f"- **Chirality c(λ')=−c(λ) on every conjugate pair: {res['chirality_c_conj_eq_neg_c']}** "
          f"(the proved twist law θ_{{λ'}}=θ_λ⁻¹). Non-self-conjugate blocks carry the explicit "
          f"residual q₀^{{f·c(λ)}} (opposite on a pair) — the true open piece, per-block quantified.\n")
    print("## What this resolves\n")
    print("- The #3681 Habiro-rigidity carrier is DISCHARGED concretely for the electron block: its")
    print("  value is a Laurent polynomial ([5]_q+1)/D with c=0, so there is nothing to continue —")
    print("  rigidity is trivial (no root-of-unity reconstruction). The geometric derivation of the")
    print("  electron block's q₀ value is complete, no fit.")
    print("- The residual for every other block is a single content-sum framing monomial q₀^{f·c(λ)}")
    print("  (the standing open object), now written explicitly per block. f is the forced Σ(2,3,5)")
    print("  Seifert datum; the c=0 electron result is f-independent (robust). No fit.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("keystone-q0-framing-residual", engine="mpmath")
    w.set_description(
        "Geometric W_lambda: the fibre->observable q0 residual reduces to the framing monomial "
        "theta_lambda^f = q0^{f*c(lambda)} (d_q(lambda)=[mark]_q is a global Laurent polynomial; no "
        "Habiro completion needed for it). The content sum c(lambda) satisfies c(lambda')=-c(lambda) "
        "and c=0 iff lambda self-conjugate; the ONLY self-conjugate n=5 block is the electron (3,1,1) "
        "(A5-split mark-6 McKay node), so it has c=0 => theta^f=1 for ANY framing f => "
        "bwS0Concrete((3,1,1))(q0)=([5]_q0+1)/D EXACTLY, no archimedean continuation. Discharges the "
        "#3681 Habiro-rigidity carrier concretely for the electron block; every other block carries "
        "the explicit residual q0^{f*c(lambda)} (per-block quantified open piece). No fit; the c=0 "
        "electron result is f-independent."
    )
    w.add_data("q0", res["q0"])
    w.add_data("D2", res["D2"])
    w.add_data("rows", res["rows"])
    w.add_data("electron_q0_value_bwS0", res["electron_q0_value_bwS0"])
    w.add_assertion(
        "electron_block_zero_framing_residual_any_f",
        computed=1 if res["electron_zero_framing_residual_any_f"] else 0, expected=1, tolerance=0,
        source="The electron block (3,1,1) is the unique self-conjugate n=5 partition (content sum "
               "c=0), so its framing residual theta_lambda^f = q0^{f*c} = 1 for any Seifert framing f. "
               "Hence the geometric colored-WRT vacuum row equals the Verlinde value d_q/D at q0 "
               "exactly for this block -- no archimedean continuation, discharging the #3681 "
               "Habiro-rigidity carrier concretely. No fit; f-independent.",
    )
    w.add_assertion(
        "content_sum_chirality_c_conj_eq_neg_c",
        computed=1 if res["chirality_c_conj_eq_neg_c"] else 0, expected=1, tolerance=0,
        source="c(lambda')=-c(lambda) on every conjugate pair (the proved twist chirality law "
               "theta_{lambda'}=theta_lambda^{-1}); the residual q0^{f*c} is opposite on a pair and "
               "vanishes exactly on the self-conjugate electron block.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
