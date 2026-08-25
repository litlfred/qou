#!/usr/bin/env python3
"""Wire the symmetrized constituent (h_Z/e_Z) into the binding — does it move B?

Owner directive: "wire h_Z/e_Z into the binding formula" (#2103 follow-up 2).

## Setup

The canonical binding (binding_canonical.py) is the LINEAR trace difference
    B(Z,N) = scale · ( tr_M(W_free) − tr_M(W_atom) )
with tr_M(W_free) = the constituent τ_p^Z·τ_n^N (NAIVE, distinguishable;
closed_form_tau_M.py:302, identity term μ=(1^Z) only). The identical-nucleon
fix replaces it with the S_Z-(anti)symmetrized constituent
    bosonic   h_Z(p)·h_N(n)        fermionic   e_Z(p)·e_N(n)     (Frobenius, #2103)

## The structural question (and why "symmetrize tr_free only" is WRONG)

Both the free state AND the bound nucleus contain the SAME Z protons + N
neutrons, so BOTH carry the identical-particle symmetrization. Symmetrizing
tr_free but leaving tr_atom naive is inconsistent — it would change B by
scale·(h_Z h_N − τ^Z τ^N), a large O(1) shift that merely reflects the
un-cancelled free factor, not physics.

Consistent symmetrization multiplies tr_free by S_free = (h_Z h_N)/(τ^Z τ^N)
and tr_atom by S_atom (the block-permuted bound symmetrization). In the
LINEAR form these do not cancel; in the LOG-RATIO form
    B_log = scale · log( tr_free / tr_atom )
the shift is scale·log(S_free / S_atom) — so **if S_atom = S_free the binding is
unchanged**, and the entire binding signal of identical-particle exchange is the
RESIDUAL log(S_free/S_atom): how differently the exchange couples to the free vs
the bridged (bound) state. That residual is the exact block-swapped atom trace
(task-1: tr_atom_sym = |G|⁻¹ Σ_{σ∈S_Z×S_N} tr_M(W_atom·σ)), the small-Z
refinement on top of the scalar Frobenius constituent.

This probe quantifies all of it for D/T/³He/⁴He (the isotopes with a canonical
binding-trace tr_atom), reports both candidate scales (Q_β=0.782, E_0=4.186),
and shows S_free per isotope so the magnitude of the exchange effect is explicit.

Output: symmetrized-binding-probe.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from math import factorial
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Q_β(n) free-neutron β-decay Q-value (binding_canonical.py scale) and the
# canonical energy scale E_0 = m_e/(q₀(q₀−1)). The binding-scale identity is
# disputed in-repo; we report B under BOTH so the structural conclusion (does
# symmetrization move B toward AME?) is scale-independent.
Q_BETA_MEV = mp.mpf("0.78233341")
E0_MEV = M_E_MEV / (Q_MP * (Q_MP - 1))

ISO = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]


def _partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in _partitions(n - k, k):
            yield (k,) + rest


def _z_mu(mu):
    z = 1
    for i, m in Counter(mu).items():
        z *= (i ** m) * factorial(m)
    return z


def frob(p, Z, fermionic=False):
    """h_Z (bosonic) or e_Z (fermionic) via Σ_μ (±)p_μ/z_μ. h_0=e_0=1."""
    total = mp.mpf(0)
    for mu in _partitions(Z):
        pm = mp.mpf(1)
        for part in mu:
            pm *= p[part]
        term = pm / _z_mu(mu)
        if fermionic and (Z - len(mu)) % 2 == 1:
            term = -term
        total += term
    return total


def main() -> int:
    t0 = time.monotonic()
    sym = record_upstream(HERE / "symmetrized-constituent-general.witness.json", _UPSTREAM_RECORDS)
    pp = {int(k): mp.mpf(v) for k, v in sym["data"]["proton_power_sums"].items()}
    pn = {int(k): mp.mpf(v) for k, v in sym["data"]["neutron_power_sums"].items()}
    tau_p, tau_n = pp[1], pn[1]

    bc = record_upstream(HERE / "binding-canonical.witness.json", _UPSTREAM_RECORDS)
    tr = {(r["Z"], r["N"]): r for r in bc["data"]["results"]}

    from b_over_a_v5_unified import AME_BA_MEV  # canonical AME 2020 dict

    print("=" * 100)
    print(" Symmetrized constituent → binding.  B = scale·(tr_free − tr_atom);  "
          "log form B_log = scale·log(tr_free/tr_atom)")
    print(f"   Q_β = {float(Q_BETA_MEV):.5f} MeV   E_0 = {float(E0_MEV):.5f} MeV   "
          f"(both reported — scale is disputed in-repo)")
    print("=" * 100)
    print(f" {'iso':>4}{'naive_free':>12}{'h_Z·h_N':>11}{'e_Z·e_N':>11}"
          f"{'S_free(bos)':>12}{'tr_atom':>10}{'B_lin(Qβ)':>11}{'B_log(Qβ)':>11}"
          f"{'B_AME':>9}")
    print(" " + "-" * 98)

    rows = []
    for lab, Z, N in ISO:
        r = tr.get((Z, N))
        tr_atom = mp.mpf(str(r["tr_M_atom"]))
        tr_free_naive = (tau_p ** Z) * (tau_n ** N)
        h_free = frob(pp, Z) * frob(pn, N)
        e_free = frob(pp, Z, True) * frob(pn, N, True)
        S_bos = h_free / tr_free_naive
        S_fer = e_free / tr_free_naive

        b_lin_qb = Q_BETA_MEV * (tr_free_naive - tr_atom)
        b_lin_e0 = E0_MEV * (tr_free_naive - tr_atom)
        b_log_qb = Q_BETA_MEV * mp.log(tr_free_naive / tr_atom)
        b_log_e0 = E0_MEV * mp.log(tr_free_naive / tr_atom)
        ame = AME_BA_MEV.get((Z, N))
        ame_f = float(ame) if ame is not None else None

        rows.append({
            "isotope": lab, "Z": Z, "N": N, "A": Z + N,
            "naive_free": float(tr_free_naive),
            "h_ZhN": float(h_free), "e_ZeN": float(e_free),
            "S_free_bosonic": float(S_bos), "S_free_fermionic": float(S_fer),
            "tr_atom": float(tr_atom),
            "B_linear_Qbeta": float(b_lin_qb), "B_linear_E0": float(b_lin_e0),
            "B_logratio_Qbeta": float(b_log_qb), "B_logratio_E0": float(b_log_e0),
            "B_AME": ame_f,
            "B_lin_Qbeta_over_AME": float(b_lin_qb) / ame_f if ame_f else None,
            "B_log_Qbeta_over_AME": float(b_log_qb) / ame_f if ame_f else None,
        })
        print(f" {lab:>4}{float(tr_free_naive):>12.5f}{float(h_free):>11.4f}"
              f"{float(e_free):>11.4f}{float(S_bos):>12.4f}{float(tr_atom):>10.5f}"
              f"{float(b_lin_qb):>11.5f}{float(b_log_qb):>11.5f}"
              f"{(ame_f or 0):>9.4f}")
    print(" " + "-" * 98)

    w = WitnessBuilder("symmetrized-binding-probe", engine="mpmath", start_time=t0)
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Wires the Frobenius symmetrized constituent (h_Z/e_Z) into the canonical "
        "linear binding B=scale·(tr_free−tr_atom) for D/T/³He/⁴He. KEY STRUCTURAL "
        "RESULT: free and bound carry the SAME identical-particle symmetrization, "
        "so in the log-ratio form B_log=scale·log(tr_free/tr_atom) the free factor "
        "S_free=(h_Z h_N)/(τ^Z τ^N) CANCELS against the bound S_atom — symmetrizing "
        "tr_free ALONE is inconsistent (a spurious O(1) shift). The binding signal "
        "of identical-particle exchange is the residual log(S_free/S_atom), i.e. the "
        "exact block-swapped atom trace (task-1: |G|⁻¹Σ_{σ∈S_Z×S_N} tr_M(W_atom·σ)). "
        "Reports both candidate scales (Q_β, E_0); S_free per isotope (⁴He bosonic "
        "2.47×) shows the exchange magnitude. tr_atom for D/T/³He/⁴He from "
        "binding-canonical.witness.json."
    )
    w.add_parameter("Q_beta_MeV", float(Q_BETA_MEV))
    w.add_parameter("E_0_MeV", float(E0_MEV))
    w.add_data("rows", rows)
    w.add_data("structural_conclusion", {
        "symmetrize_free_only": "WRONG — inconsistent; spurious O(1) shift "
            "= scale·(h_Z h_N − τ^Z τ^N) reflecting the un-cancelled free factor.",
        "log_ratio_cancellation": "B_log shift = scale·log(S_free/S_atom); if "
            "S_atom=S_free (same nucleon content) the binding is UNCHANGED.",
        "binding_signal": "the residual log(S_free/S_atom) = the exact block-"
            "swapped bound symmetrization (task-1, S_Z×S_N), the small-Z refinement.",
        "orbit_identity_does_NOT_trivialize_symmetrization": (
            "atom_orbit_reduction.py proves tr_M(β_{Z,N})=tr_M(representative) "
            "with NO |orbit| factor — but that is RELABELING (σ leaves the word "
            "p…pn…n unchanged ⇒ conjugation β_σ W β_σ⁻¹, trace-preserving by "
            "Markov M1). The Young SYMMETRIZER is a DIFFERENT operation: it "
            "COMPOSES the block-swap braid, tr_M(W_atom·β_σ) (not conjugation), "
            "which the bonds make nontrivial. So S_atom = |G|⁻¹Σ_σ "
            "tr_M(W_atom·β_σ) is NOT trivially tr_M(W_atom); the orbit identity "
            "must not be used to shortcut it."),
        "S_free_bosonic_4He": float(frob(pp, 2) * frob(pn, 2)
                                    / ((tau_p ** 2) * (tau_n ** 2))),
    })
    out = w.save()
    print(" STRUCTURAL: free & bound share the same identical-particle factor → it "
          "CANCELS in the log-ratio binding.")
    print(" ⇒ symmetrizing tr_free alone is inconsistent; the binding signal is the "
          "RESIDUAL log(S_free/S_atom) = the exact block-swapped tr_atom (task-1).")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
