#!/usr/bin/env python3
"""Chirality × topology binding probe (EXPLORATORY).

Crosses the two structural axes that the prior probes left separate:

  • CHANNEL / chirality (from hecke_channel_binding_probe.py, PR #2461/#2467):
    each inter-nucleon crossing carries Hecke channels sym(+q) / std / alt(−q⁻¹).
    The **alternating (Pauli)** channel correctly makes pp & nn UNBOUND
    (no diproton / dineutron); the **std** channel is the genuine Jones–Markov
    tr_M (PR #2481) and is what the production kernel uses.

  • TOPOLOGY (from merged PR #2343): production B_sym is EXACTLY the LINEAR
    CHAIN  B_sym = α·[(Z−1)L_pp + L_pn + (N−1)L_nn]  (adjacent bonds only),
    NOT the complete graph the chirality probe tabulated.

The prior chirality probe applied ONE channel UNIFORMLY on the COMPLETE GRAPH.
This probe fills the missing cells: {chain, complete} × {std-uniform, Pauli-mixed},
where the **Pauli-mixed** assignment is the physically-forced one —
  pp → alt (identical p's, antisymmetric ⇒ unbound),
  nn → alt (identical n's ⇒ unbound),
  pn → std (the bound Jones–Markov channel).

ZERO free parameters: per-bond channel values are derived at q₀ (reused from
hecke_channel_binding_probe.channels); only the combinatorial bond COUNT
(topology) and the forced Pauli channel ASSIGNMENT vary. Derive-or-refute,
no fit (the deuteron f_pn=0.588 magnitude is owner-gated to the s5-so3
keystone and is NOT chased here), no production rewire.

Because it is pure closed-form arithmetic (no per-knot trace), it runs for ALL
isotopes with no p(3A) partition wall.

Output: chirality-topology-binding.witness.json
"""
from __future__ import annotations

import json
import sys
from math import comb, sqrt
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Reuse the canonical channel construction (no duplication) — PR #2461/#2481.
from hecke_channel_binding_probe import channels, BONDS, E0, Q0  # noqa: E402

mp.mp.dps = 50

# Low isotopes (closed form ⇒ no feasibility wall; extend freely).
NUC = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
       "6Li": (3, 3), "7Li": (3, 4)}
AME_B = {"D": mp.mpf("2.224566"), "T": mp.mpf("8.481798"),
         "3He": mp.mpf("7.718043"), "4He": mp.mpf("28.295673"),
         "6Li": mp.mpf("31.99464"), "7Li": mp.mpf("39.24454")}

# Per-bond channel values f_bond^channel at q₀ (derived; reused).
CHVALS = {b: channels(c, d) for b, (c, d) in BONDS.items()}

# Pauli-forced per-bond channel assignment: identical-nucleon pairs are
# antisymmetric (alt = Pauli = unbound); the p-n pair takes the bound std channel.
PAULI = {"pp": "alt", "nn": "alt", "pn": "std"}
PAULI_SYM = {"pp": "alt", "nn": "alt", "pn": "sym"}


def _bond_E(channel, bond):
    """Per-bond binding in `channel`: E₀·ln(1/f) iff BOUND (0 < f < 1), else 0.

    Bound requires a positive sub-unity suppression 0 < f < 1. A negative channel
    value (the alt eigenvalue −q⁻¹ < 0) is the antisymmetric/Pauli channel and is
    UNBOUND — which is the whole physical point (no diproton/dineutron). NB this is
    stricter than hecke_channel_binding_probe's `|f| for f<0` magnitude rule, which
    spuriously binds pp in alt (|−0.901|<1); the strict form here matches that
    audit's own *prose* ("f_pp<0 antibound") and is the correct Pauli treatment.
    """
    f = CHVALS[bond][channel]
    return E0 * mp.log(1 / f) if 0 < f < 1 else mp.mpf(0)


def _counts(Z, N, topology):
    if topology == "chain":         # production: adjacent bonds only (A−1 total)
        return {"pp": max(Z - 1, 0), "pn": 1 if (Z and N) else 0, "nn": max(N - 1, 0)}
    return {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)}   # complete graph


def binding(Z, N, topology, assignment):
    """assignment is either a channel name (uniform) or a per-bond dict (mixed)."""
    cnt = _counts(Z, N, topology)
    if isinstance(assignment, str):
        chan = {b: assignment for b in cnt}
    else:
        chan = assignment
    return sum(cnt[b] * _bond_E(chan[b], b) for b in cnt)


def _rms(model):
    es = [float(model[nm] - AME_B[nm]) for nm in NUC]
    return sqrt(sum(e * e for e in es) / len(es))


def main() -> int:
    print(f"\n  CHIRALITY × TOPOLOGY binding probe   α = E₀ = {float(E0):.6f} MeV   "
          f"q₀ = {float(Q0):.10f}")
    print("  per-bond channel f at q₀:  " + "  ".join(
        f"{b}[std={float(CHVALS[b]['std']):.3f} alt={float(CHVALS[b]['alt']):.3f}]"
        for b in ("pp", "pn", "nn")))
    print("  Pauli assignment = {pp→alt(unbound), nn→alt(unbound), pn→std(bound)}; "
          "no fit, no rewire.\n")

    # the four (topology × assignment) cells + the two reference uniform-std cells
    models = {
        "std·chain  (=merged B_sym)": ("chain", "std"),
        "std·complete (all-pairs)":   ("complete", "std"),
        "Pauli·chain":                ("chain", PAULI),
        "Pauli·complete":             ("complete", PAULI),
        "Pauli-sym·complete":         ("complete", PAULI_SYM),
    }

    print("### Binding B (MeV) by (assignment · topology)  vs AME")
    hdr = "| nuc | A | AME_B | " + " | ".join(models) + " |"
    print(hdr)
    print("|" + "---|" * (3 + len(models)))
    computed = {k: {} for k in models}
    for nm, (Z, N) in NUC.items():
        row = [f"| {nm} | {Z+N} | {float(AME_B[nm]):.2f} "]
        for k, (topo, asg) in models.items():
            b = binding(Z, N, topo, asg)
            computed[k][nm] = b
            row.append(f"| {float(b):.2f} ")
        print("".join(row) + "|")

    print("\n### Accuracy ratio AME_B / B_model  (1.00 = perfect; >1 under-binds)")
    print("| nuc | " + " | ".join(models) + " |")
    print("|" + "---|" * (1 + len(models)))
    for nm in NUC:
        row = [f"| {nm} "]
        for k in models:
            b = computed[k][nm]
            row.append(f"| {float(AME_B[nm]/b):.2f} " if b > 0 else "| ∞ ")
        print("".join(row) + "|")

    print("\n### RMS error vs AME (MeV, lower = better)")
    for k in models:
        print(f"  {k:<28} RMS = {_rms(computed[k]):6.2f}")

    # ⁴He residual under the best physical model = the α-cluster 4-body term
    best = "Pauli·complete"
    he4_resid = float(AME_B["4He"] - computed[best]["4He"])
    print(f"\n  ⁴He residual under {best}: {he4_resid:+.2f} MeV "
          f"(= the irreducible 4-body α-cluster term, cf. PR #2343 §α-unit)")

    witness = {
        "computation": "chirality-topology-binding",
        "description": "Chirality (Hecke channel) × bond-count topology binding probe. "
                       "Crosses the Pauli-channel assignment (pp/nn→alt unbound, pn→std) "
                       "with chain vs complete-graph topology. Exploratory, no fit, no rewire.",
        "engine": "mpmath", "dps": 50,
        "q0": str(Q0), "E0_MeV": str(E0),
        "channel_values_at_q0": {b: {c: str(v) for c, v in CHVALS[b].items()} for b in CHVALS},
        "pauli_assignment": PAULI,
        "models": {k: {nm: str(computed[k][nm]) for nm in NUC} for k in models},
        "ame_B_MeV": {nm: str(AME_B[nm]) for nm in NUC},
        "rms_MeV": {k: _rms(computed[k]) for k in models},
        "he4_alpha_cluster_residual_MeV": he4_resid,
        "discipline": "EXPLORATORY — derive-or-refute, zero free parameters, no production rewire.",
    }
    out = HERE.parent / "chirality-topology-binding.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
