#!/usr/bin/env python3
"""
Holomorphic-tie probe (bean 1jrh) — do the binding (bar-even) and Q_β
(bar-odd) ladders satisfy ONE three-term recurrence with a bar-even
multiplier, as `QOU.Knot.SelfDuality.recurrence_descent` (sorry-free)
says they must if they are the two parities of a single complex-volume
ladder 𝔙 (conj:binding-qbeta-complex-volume)?

Formalize-first status: the STRUCTURAL claim is already Lean-proved —
a recurrence V₊ = c·Vₖ − V₋ with σ-fixed c descends to BOTH parity
ladders with the SAME c. What is NOT known is whether the empirical
trace ladders actually satisfy such a recurrence. This probe is the
narrowed numerical test that theorem licenses (compute-author §3.3).

Ladder: neutron-number chains at fixed Z (the prior probe
`binding_bar_even_odd_probe.py` found the bar-odd part and the
bar-ratio exponent are neutron-organized). For V_N ∈ {defect
D = tr_free − tr_atom, log-form L = ln(tr_free/tr_atom)} evaluated at
q₀ AND q₀⁻¹:

    c_N(q)      = (V_{N+1}(q) + V_{N-1}(q)) / V_N(q)   implied multiplier
    E_N, O_N    = ½[V_N(q₀) ± V_N(q₀⁻¹)]               bar-even / bar-odd
    c_N^even    = (E_{N+1} + E_{N-1}) / E_N            binding-face ladder
    c_N^odd     = (O_{N+1} + O_{N-1}) / O_N            Q_β-face ladder

Tests (all must hold for the holomorphic tie):
  (1) constancy: c_N(q₀) independent of N (a genuine 3-term recurrence)
  (2) bar-evenness: c_N(q₀) = c_N(q₀⁻¹)  (σ-fixed multiplier)
  (3) parity tie: c_N^even = c_N^odd     (the recurrence_descent signature —
      the binding and Q_β ladders share ONE multiplier)
If (1)-(3) hold on the Z=1 chain, back-extrapolate V₀ = c·V₁ − V₂ (the
bare-proton self-defect) and compare its bar-even face to the μ–p
tension residual ≈ 242 ppb of m_p (the tnjb substance; see
docs/audits/2026-05-28-mu-p-tension-substrate-floor.md).

Audit-only; no production wiring. E₀ = m_e/(q₀(q₀−1)) (CAL-1 + CAL-2).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

import mpmath as mp

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV as _ME, M_P_MEV_VALIDATION  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# Neutron chains: (Z, [N ...]); A = Z+N kept ≤ 6 (transfer path, ~0.2 s each)
CHAINS = [(1, [1, 2, 3, 4]), (2, [1, 2, 3, 4])]

# μ–p tension residual for the back-extrapolation comparison (context only,
# not a fit target): −242 ppb on m_p per the substrate-floor audit.
MU_P_RESIDUAL_PPB = 242.0
M_P_MEV_CODATA = float(M_P_MEV_VALIDATION)  # from codata_constants registry (validation target)


def ladder_values(Z: int, N: int, qi):
    """(D(q0), D(qi), L(q0), L(qi)) for one (Z, N).

    The q₀ leg deliberately uses `tr_m_atom_zn`'s DEFAULT q — the canonical
    substrate q₀ at full 50-digit precision (Q_50_DIGIT_STR internally);
    passing an explicit q would re-lift the word instead. Only the q₀⁻¹
    leg needs the explicit `q=` argument.
    """
    ta0, tf0, _, _ = tr_m_atom_zn(Z, N, dps=50)
    tai, tfi, _, _ = tr_m_atom_zn(Z, N, q=qi, dps=50)
    ta0, tf0, tai, tfi = (mp.mpf(str(x)) for x in (ta0, tf0, tai, tfi))
    return (tf0 - ta0, tfi - tai, mp.log(tf0 / ta0), mp.log(tfi / tai))


def implied_c(seq):
    """Implied 3-term multipliers c_N = (V_{N+1}+V_{N-1})/V_N for interior N."""
    out = []
    for i in range(1, len(seq) - 1):
        out.append((seq[i + 1] + seq[i - 1]) / seq[i] if seq[i] != 0 else mp.mpf("nan"))
    return out


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate q₀
    qi = mp.mpf(1) / q0
    E0 = mp.mpf(str(_ME)) / (q0 * (q0 - 1))

    print("\n  HOLOMORPHIC-TIE PROBE (bean 1jrh): one 3-term recurrence, two parity ladders?")
    print(f"  q₀ = {float(q0):.10f}   E₀ = {float(E0):.4f} MeV   forms: D = tr_free−tr_atom, L = ln(tr_free/tr_atom)\n")

    witness_chains = {}
    for Z, Ns in CHAINS:
        rows = {"D0": [], "Di": [], "L0": [], "Li": []}
        for N in Ns:
            d0, di, l0, li = ladder_values(Z, N, qi)
            rows["D0"].append(d0)
            rows["Di"].append(di)
            rows["L0"].append(l0)
            rows["Li"].append(li)
        # parity parts
        even = {f: [(rows[f0][k] + rows[fi][k]) / 2 for k in range(len(Ns))]
                for f, f0, fi in (("D", "D0", "Di"), ("L", "L0", "Li"))}
        odd = {f: [(rows[f0][k] - rows[fi][k]) / 2 for k in range(len(Ns))]
               for f, f0, fi in (("D", "D0", "Di"), ("L", "L0", "Li"))}

        print(f"  chain Z={Z}, N={Ns}")
        chain_w = {"N": Ns}
        for form in ("D", "L"):
            c_q0 = implied_c(rows[f"{form}0"])
            c_qi = implied_c(rows[f"{form}i"])
            c_ev = implied_c(even[form])
            c_od = implied_c(odd[form])
            print(f"    form {form}:")
            print(f"      V(q₀)      = {[f'{float(v):.6e}' for v in rows[form + '0']]}")
            print(f"      c(q₀)      = {[f'{float(c):.6f}' for c in c_q0]}   (test 1: constant?)")
            print(f"      c(q₀⁻¹)    = {[f'{float(c):.6f}' for c in c_qi]}   (test 2: = c(q₀)?)")
            print(f"      c^even     = {[f'{float(c):.6f}' for c in c_ev]}   (binding face)")
            print(f"      c^odd      = {[f'{float(c):.6f}' for c in c_od]}   (Q_β face; test 3: = c^even?)")
            chain_w[form] = {
                "V_q0": [str(v) for v in rows[form + "0"]],
                "V_qinv": [str(v) for v in rows[form + "i"]],
                "V_even": [str(v) for v in even[form]],
                "V_odd": [str(v) for v in odd[form]],
                "c_q0": [str(c) for c in c_q0],
                "c_qinv": [str(c) for c in c_qi],
                "c_even": [str(c) for c in c_ev],
                "c_odd": [str(c) for c in c_od],
            }
            # back-extrapolate the N=0 rung (bare nucleus, Z protons only)
            # V0 = c·V1 − V2 using the first interior multiplier
            if len(c_ev) >= 1:
                v0_even = c_ev[0] * even[form][0] - even[form][1]
                chain_w[form]["V0_even_backextrap"] = str(v0_even)
                if Z == 1:
                    # V₀ is dimensionless (trace units) in both forms; E₀
                    # (MeV, CAL-1 + CAL-2) converts to MeV — same convention
                    # as binding_bar_even_odd_probe.py.
                    v0_mev = E0 * v0_even
                    resid_mev = mp.mpf(MU_P_RESIDUAL_PPB) * 1e-9 * mp.mpf(M_P_MEV_CODATA)
                    print(f"      V₀^even backextrap (bare p defect, {form}) = {float(v0_even):.6e}"
                          f"  → E₀·V₀ = {float(v0_mev):.6e} MeV  vs μ–p residual {float(resid_mev):.3e} MeV")
                    chain_w[form]["E0_V0_even_MeV"] = str(v0_mev)
                    chain_w[form]["mu_p_residual_MeV"] = str(resid_mev)
        witness_chains[f"Z{Z}"] = chain_w
        print()

    # verdict summary (scope-limited phrasing per the refuted-discipline (a))
    def spread(vals):
        vals = [v for v in vals if mp.isfinite(v)]
        if not vals:
            return None
        m = mp.fsum(vals) / len(vals)
        return float(max(abs(v - m) for v in vals) / abs(m)) if m != 0 else None

    verdict = {}
    for zkey, cw in witness_chains.items():
        for form in ("D", "L"):
            c_ev = [mp.mpf(c) for c in cw[form]["c_even"]]
            c_od = [mp.mpf(c) for c in cw[form]["c_odd"]]
            c_q0 = [mp.mpf(c) for c in cw[form]["c_q0"]]
            c_qi = [mp.mpf(c) for c in cw[form]["c_qinv"]]
            verdict[f"{zkey}_{form}"] = {
                "test1_constancy_rel_spread_q0": spread(c_q0),
                "test2_bar_even_rel_gap": (
                    float(abs(c_q0[0] - c_qi[0]) / abs(c_q0[0])) if c_q0 and c_q0[0] != 0 else None),
                "test3_parity_tie_rel_gap": (
                    float(abs(c_ev[0] - c_od[0]) / abs(c_ev[0])) if c_ev and c_ev[0] != 0 else None),
            }
    print("  verdict (rel gaps; ≪1 everywhere = holomorphic tie holds in that form/chain):")
    for k, v in verdict.items():
        print(f"    {k}: {v}")

    wb = WitnessBuilder("binding-qbeta-recurrence-tie-probe", engine="mpmath")
    wb.set_description(
        "Holomorphic-tie probe (bean 1jrh): do the binding (bar-even) and "
        "Q_beta (bar-odd) trace ladders over neutron chains satisfy ONE "
        "3-term recurrence with a bar-even multiplier "
        "(QOU.Knot.SelfDuality.recurrence_descent)?")
    wb.set_audit_only("docs/audits/2026-07-02-binding-qbeta-recurrence-tie-probe.md")
    wb.add_parameter("precision_dps", 50)
    wb.add_parameter("q_0", str(q0))
    wb.add_parameter("q_inv", str(qi))
    wb.add_parameter("E0_MeV", str(E0))
    wb.add_data("chains", witness_chains)
    wb.add_data("verdict_gaps", verdict)
    wb.add_data("context", {
        "tests": "conj:binding-qbeta-complex-volume via the proved recurrence_descent",
        "prior_probe": "binding_bar_even_odd_probe.py (parity projection refuted as binding fix)",
        "tnjb_link": "if the tie holds, Re-face m_p correction is determined by the Q_beta face — the mu-p tension becomes computable",
    })
    wb.add_caveat(
        "Scope-limited: tests the (Z,N) neutron-chain trace ladder in the "
        "linear-defect and log forms only; a failure here does not exclude "
        "the tie in a different ladder variable (e.g. the u = b*hbar_q^2 "
        "c_k rungs).")
    out = wb.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
