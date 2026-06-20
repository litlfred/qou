#!/usr/bin/env python3
"""binding_sym_vs_lin_two_models.py
====================================

ONE pipeline, TWO models — distinguish the *exact* log-trace binding from its
*linear* truncation, both calibrated on the SAME object (canonical Markov trace
`markov_trace_canonical`, read from `binding-canonical.witness.json`) and both
pinned on the **deuteron**, so T / ³He / ⁴He are parameter-free tests of *which
functional form* the binding takes.

  Model A — B_sym (exact, log-trace):  B(K) = α · ln| τ_free(K) / τ_atom(K) |
  Model B — B_lin (linear truncation): B(K) = E₀ · ( τ_free(K) − τ_atom(K) )

ln x ≈ x − 1 near x = 1 ⇒ B_lin is the linearization of B_sym. With both scales
fixed on D, the only question left is the FORM. The implied per-isotope scale
(α(K), E₀(K)) is reported too: a form whose scale stays flat is "derived"; a
scale that drifts is absorbing a missing A-dependence.

Symbolic-α check: α is pinned on D; we then test whether that single number is
structural (vs m_e, E₀, Q_β, 2π·m_e) and whether it stays constant across the
four isotopes (it does NOT — see witness; the drift is the qCLT/additive term
B_qCLT = −α Σ ln|V_i|, the A→∞ form not modelled by a single knot trace).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import pathlib
import time

import mpmath as mp  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 30
HERE = pathlib.Path(__file__).resolve().parent


def main() -> int:
    t0 = time.monotonic()
    from q_parameter import Q
    from codata_constants import M_E_MEV as m_e  # registry (no inline literal)
    q0 = mp.mpf(str(Q() if callable(Q) else Q))

    d = json.loads((HERE / "binding-canonical.witness.json").read_text())
    res = {r["atom"]: r for r in d.get("witness", d).get("data", {}).get("results", [])}
    order = ["D", "T", "3He", "4He"]

    def ta(K): return mp.mpf(str(res[K]["tr_M_atom"]))
    def tf(K): return mp.mpf(str(res[K]["tr_M_free"]))
    def bame(K): return mp.mpf(str(res[K]["B_AME_MeV"]))

    # log-trace ratio and linear difference per isotope
    L = {K: mp.log(abs(tf(K) / ta(K))) for K in order}          # exact (log)
    D = {K: tf(K) - ta(K) for K in order}                        # linear (diff)

    # pin both scales on the deuteron
    alpha = bame("D") / L["D"]      # Model A scale (MeV)
    E0 = bame("D") / D["D"]         # Model B scale (MeV)

    print(f"  q0={mp.nstr(q0,8)}   α(pinned on D)={mp.nstr(alpha,8)} MeV   "
          f"E₀(pinned on D)={mp.nstr(E0,8)} MeV\n")
    print(f"{'iso':>4} {'B_AME':>8} | {'B_sym':>8} {'err%':>7} {'α_impl':>7} "
          f"| {'B_lin':>8} {'err%':>7} {'E0_impl':>7}")
    rows = []
    for K in order:
        bs = alpha * L[K]; es = (bs - bame(K)) / bame(K) * 100
        bl = E0 * D[K]; el = (bl - bame(K)) / bame(K) * 100
        a_impl = bame(K) / L[K]      # α that would fit THIS isotope
        e_impl = bame(K) / D[K]      # E₀ that would fit THIS isotope
        rows.append({"atom": K, "A": res[K]["A"], "Z": res[K]["Z"], "N": res[K]["N"],
                     "B_AME_MeV": mp.nstr(bame(K), 6),
                     "B_sym_MeV": mp.nstr(bs, 6), "err_sym_pct": mp.nstr(es, 4),
                     "B_lin_MeV": mp.nstr(bl, 6), "err_lin_pct": mp.nstr(el, 4),
                     "alpha_implied_MeV": mp.nstr(a_impl, 6),
                     "E0_implied_MeV": mp.nstr(e_impl, 6),
                     "log_ratio": mp.nstr(L[K], 6), "lin_diff": mp.nstr(D[K], 6)})
        print(f"{K:>4} {float(bame(K)):8.3f} | {float(bs):8.3f} {float(es):+7.1f} "
              f"{float(a_impl):7.3f} | {float(bl):8.3f} {float(el):+7.1f} {float(e_impl):7.3f}")

    # which form tracks better (mean |err| over the 3 predicted isotopes)?
    pred = order[1:]
    mae_sym = sum(abs(mp.mpf(r["err_sym_pct"])) for r in rows if r["atom"] in pred) / 3
    mae_lin = sum(abs(mp.mpf(r["err_lin_pct"])) for r in rows if r["atom"] in pred) / 3
    winner = "B_sym (exact log)" if mae_sym < mae_lin else "B_lin (linear)"
    print(f"\n  mean|err| over T/³He/⁴He (parameter-free):  B_sym={float(mae_sym):.1f}%  "
          f"B_lin={float(mae_lin):.1f}%  →  {winner} tracks better")

    # symbolic-α candidates vs the D-pinned α
    cand = {"m_e": m_e, "E0(linear)": E0, "Q_beta_n": mp.mpf(str(res["D"]["Q_beta_n_MeV"])),
            "2*pi*m_e": 2 * mp.pi * m_e, "m_e/(q0-1)": m_e / (q0 - 1)}
    print("\n  α symbolic check (α_D = %.4f MeV):" % float(alpha))
    sym = {}
    for name, v in cand.items():
        sym[name] = mp.nstr(alpha / v, 6)
        print(f"    α / {name:<12} = {float(alpha / v):8.4f}")

    b = WitnessBuilder("binding-sym-vs-lin-two-models", engine="python+mpmath", start_time=t0)
    (b.set_description(
        "Two binding models on ONE canonical-tr_M pipeline, both pinned on the "
        "deuteron: B_sym = α·ln|τ_free/τ_atom| (exact log-trace) vs "
        "B_lin = E₀·(τ_free−τ_atom) (linear truncation). Parameter-free test on "
        "T/³He/⁴He distinguishes the FORM: B_sym mean|err|={:.1f}% beats B_lin "
        "{:.1f}%. Implied scale drifts with A (single knot trace misses the "
        "qCLT/additive A-term); α not matched by m_e/E₀/Q_β/2π·m_e. No fit "
        "beyond the one D pin; NOT wired.".format(float(mae_sym), float(mae_lin)))
     .add_parameter("q0", mp.nstr(q0, 12))
     .add_parameter("alpha_pinned_D_MeV", mp.nstr(alpha, 10))
     .add_parameter("E0_pinned_D_MeV", mp.nstr(E0, 10))
     .add_data("rows", rows)
     .add_data("mae_sym_pct", mp.nstr(mae_sym, 5))
     .add_data("mae_lin_pct", mp.nstr(mae_lin, 5))
     .add_data("winner", winner)
     .add_data("alpha_symbolic_ratios", sym))
    b.add_assertion("B_sym_beats_B_lin_parameter_free",
                    computed=bool(mae_sym < mae_lin), expected=True,
                    source="exact log-trace form tracks AME better than linear truncation")
    out = b.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
