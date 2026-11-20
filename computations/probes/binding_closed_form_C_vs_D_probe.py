#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q = q_0, not symbolic.
"""binding_closed_form_C_vs_D_probe.py — the production closed-form binding
chain under convention C vs convention D, A = 2..7.

MEASUREMENT ONLY.  Nothing is tuned; no production value is changed.  AME2020
is an output comparison target, never an input.

WHAT PRODUCTION ACTUALLY RUNS
-----------------------------
`binding_canonical(Z, N, use_closed_form=True)` does NOT sum p(3A) partitions.
It uses the Phase-5q closed form (closed_form_tau_M.py):

    tr_M(B_K)   = tau_p^Z * tau_n^N * prod_{i in interfaces} f_i(q)
    tr_M(B_free) = tau_p^Z * tau_n^N
    delta_tr    = tr_M(B_free) - tr_M(B_K)
                = tau_p^Z * tau_n^N * (1 - prod_i f_i(q))
    B           = E_0 * delta_tr,   E_0 = Q_NEUTRON_MEV

The trace convention enters in TWO places, and both are convention C today:

  1. the H_3 nucleon blocks tau_p, tau_n = sum_{lambda |- 3} y_lambda chi^lambda,
     with y_lambda from y_lambda_wenzl_bridge (z_C hard-coded at :122,:140);
  2. the per-interface factors, which are literally built from the Ocneanu
     parameter z (closed_form_tau_M.interface_factor):
         positive  f = z
         negative  f = z - h
         averaged  f = z - h/2        (h = q - q^-1)
     via closed_form_tau_M.markov_z(q) = 1/(q^1/2 + q^-1/2)  <- convention C.

So the convention question reaches production through the interface factors
directly, not only through the weights.  This probe swaps BOTH to convention
D (z_D = q^3/(q^2+1), the N = 2 / SU(2)-TL parameter) and reports the delta.

The Markov axiom that generates those factors -- tr(alpha sigma_g) = z tr(alpha),
plus the Hecke skein sigma^-1 = sigma - h -- is convention-INDEPENDENT; it is
Lean-proved sorry-free as
QOU.BraidKnot.interface_knot_markov_z_bar_symmetric.  What the axiom does not
fix is the NUMBER z.  That number is what the fibre dimension pins
(z*[N]_q = q^N, ocneanu_param_eq_of_fibre_qdim), and it is what changes here.
The proved identity therefore remains valid under D: only its parameter moves.

PIN: EXPERIMENTAL / proton, q_parameter.Q_50_DIGIT_STR (owner directive
2026-08-07).  tau_p / tau_n are recomputed live from the Hoefsmit characters
and the closed-form y_lambda at each z -- never from y_lambda_at() or any
committed muon-pin witness.

Ref: computations/binding_canonical.py:200-215 (the closed-form production path)
Ref: computations/closed_form_tau_M.py:132,152 (markov_z, interface_factor)
Ref: QOU.BraidKnot.interface_knot_markov_z_bar_symmetric (Lean: the axiom, not z)
Ref: docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV as E_0  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    classical_dim, partitions_of, schur_principal,
)
from closed_form_tau_M import canonical_interface_kinds  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from tr_m_wenzl_bridge_mpfr import (  # noqa: E402
    _build_seminormal_matrices_mpf, _chi_lambda_of_word_mpf,
)

T0 = time.time()

# AME2020 -- OUTPUT COMPARISON TARGETS ONLY.
AME = {(1, 1): ("2H", "2.224566"), (1, 2): ("3H", "8.481821"),
       (2, 1): ("3He", "7.718043"), (2, 2): ("4He", "28.295673"),
       (3, 3): ("6Li", "31.994566"), (3, 4): ("7Li", "39.244538"),
       (4, 3): ("7Be", "37.600411")}


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def z_C(q):
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def z_D(q):
    return q ** 3 / (q ** 2 + 1)


def hecke_h(q):
    return q - 1 / q


def y_vector_at_z(n, q, z):
    Q = q ** 2
    X = q * z / (1 - Q + q * z)
    parts = [tuple(p) for p in partitions_of(n)]
    s = {p: schur_principal(list(p), X, Q) for p in parts}
    norm = sum(classical_dim(list(p)) * s[p] for p in parts)
    return {p: s[p] / norm for p in parts}


def interface_factor(kind, q, z):
    """closed_form_tau_M.interface_factor, with z as a parameter.

    Handles BOTH members of the averaged family. "averaged" is the
    colour-BLIND z - h/2; "averaged_weighted" is the canonical colour-tube
    factor z - h(1/2 - δ/4) that `closed_form_ratio` applies under
    `bring_color_weighted`.

    Keeping only "averaged" was a live defect here, not a hypothetical one:
    the caller below requests `canonical_interface_kinds(Z, N)`, which
    defaults to the canonical convention but deliberately labels the p-n
    interface "averaged" — the label vocabulary cannot carry δ. So every
    p-n interface was priced colour-blind while the run was labelled
    canonical, and no equality test against "averaged_weighted" could see it,
    because that label was never emitted. The caller now opts into
    `weighted_labels=True` so the weighting is either applied or raised on.
    """
    h = hecke_h(q)
    if kind == "positive":
        return z
    if kind == "negative":
        return z - h
    if kind == "averaged":
        return z - h / 2
    if kind == "averaged_weighted":
        return z - h * (mp.mpf(1) / 2 - flavor_split_leading(q) / 4)
    raise ValueError(kind)


def nucleon_h3_traces(q):
    """chi^lambda(B_p), chi^lambda(B_n) for lambda |- 3 -- convention-free."""
    out = {}
    for name, (Z, N) in (("p", (1, 0)), ("n", (0, 1))):
        word = atom_braid_word_3A(Z, N)
        chis = {}
        for lam in [tuple(p) for p in partitions_of(3)]:
            sig, dim = _build_seminormal_matrices_mpf(lam, q)
            chis[lam] = (mp.mpf(0) if dim == 0
                         else _chi_lambda_of_word_mpf(sig, dim, word, q=q))
        out[name] = chis
    return out


def main() -> int:
    set_compute_dps()
    q = Q_MP
    log(f"proton pin q_0 = {Q_50_DIGIT_STR}  (dps={mp.mp.dps})")
    zc, zd = z_C(q), z_D(q)
    log(f"z_C = {mp.nstr(zc, 20)}   z_D = {mp.nstr(zd, 20)}   "
        f"h = {mp.nstr(hecke_h(q), 20)}")

    chis = nucleon_h3_traces(q)
    parts3 = [tuple(p) for p in partitions_of(3)]
    e0 = mp.mpf(str(E_0))

    tau = {}
    for tag, z in (("C", zc), ("D", zd)):
        y = y_vector_at_z(3, q, z)
        tau[tag] = {nk: sum(y[l] * chis[nk][l] for l in parts3)
                    for nk in ("p", "n")}
        log(f"  {tag}: tau_p = {mp.nstr(tau[tag]['p'], 20)}   "
            f"tau_n = {mp.nstr(tau[tag]['n'], 20)}")
        for lab, kind in (("positive", "positive"), ("negative", "negative"),
                          ("averaged", "averaged"),
                          ("avg_wtd", "averaged_weighted")):
            log(f"     f_{lab:9s} = "
                f"{mp.nstr(interface_factor(kind, q, z), 20)}")

    rows = []
    for (Z, N), (name, ame_s) in AME.items():
        kinds = canonical_interface_kinds(Z, N, weighted_labels=True)
        ame = mp.mpf(ame_s)
        row = {"atom": name, "Z": Z, "N": N, "A": Z + N,
               "n_strands": 3 * (Z + N),
               "interface_kinds": list(kinds),
               "B_AME2020_MeV": ame_s}
        for tag, z in (("C", zc), ("D", zd)):
            prod = mp.mpf(1)
            for k in kinds:
                prod *= interface_factor(k, q, z)
            tr_free = tau[tag]["p"] ** Z * tau[tag]["n"] ** N
            tr_atom = tr_free * prod
            dtr = tr_free - tr_atom
            B = e0 * dtr
            row[f"prod_f_{tag}"] = mp.nstr(prod, 20)
            row[f"tr_M_free_{tag}"] = mp.nstr(tr_free, 20)
            row[f"tr_M_atom_{tag}"] = mp.nstr(tr_atom, 20)
            row[f"delta_tr_{tag}"] = mp.nstr(dtr, 20)
            row[f"B_MeV_{tag}"] = mp.nstr(B, 15)
            row[f"rel_err_{tag}"] = mp.nstr((B - ame) / ame, 10)
            row[f"_B_{tag}"] = B
        row["B_D_over_B_C"] = mp.nstr(row["_B_D"] / row["_B_C"], 12)
        log(f"  {name:4s} A={Z+N} ifaces={len(kinds)}  "
            f"B_C={mp.nstr(row['_B_C'],10)}  B_D={mp.nstr(row['_B_D'],10)}  "
            f"AME={ame_s}  D/C={row['B_D_over_B_C']}")
        del row["_B_C"], row["_B_D"]
        rows.append(row)

    wb = WitnessBuilder("binding-closed-form-c-vs-d", engine="mpmath")
    wb.add_parameter("q_0", Q_50_DIGIT_STR)
    wb.add_parameter("q_0_pin", "experimental/proton "
                                "(q_parameter.Q_50_DIGIT_STR)")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_parameter("uses_experimental_target_values_as_input", False)
    wb.add_parameter("E_0_MeV", str(E_0))
    wb.add_parameter("z_C", mp.nstr(zc, 30))
    wb.add_parameter("z_D", mp.nstr(zd, 30))
    wb.add_parameter("pn_convention", "bring_color_weighted (production "
                                      "default; interface LABELS only)")
    wb.add_data("tau_H3_C", {k: mp.nstr(v, 25) for k, v in tau["C"].items()})
    wb.add_data("tau_H3_D", {k: mp.nstr(v, 25) for k, v in tau["D"].items()})
    wb.add_data("interface_factors_C", {
        k: mp.nstr(interface_factor(k, q, zc), 25)
        for k in ("positive", "negative", "averaged")})
    wb.add_data("interface_factors_D", {
        k: mp.nstr(interface_factor(k, q, zd), 25)
        for k in ("positive", "negative", "averaged")})
    wb.add_data("per_isotope", rows)
    wb.add_assertion(
        "closed_form_binding_moves_under_D",
        1 if all(abs(mp.mpf(r["B_D_over_B_C"]) - 1) > mp.mpf("1e-6")
                 for r in rows) else 0, 1,
        source="the production closed-form binding changes for every isotope "
               "under D: z enters the per-interface factors directly, so the "
               "convention is not a common scale that cancels in delta_tr",
    )
    wb.set_description(
        "Production closed-form binding chain (binding_canonical "
        "use_closed_form path: delta_tr = tau_p^Z tau_n^N (1 - prod_i f_i), "
        "B = E_0 delta_tr) under the binding channel's current convention C "
        "vs the mass channel's settled convention D, A = 2..7, at the "
        "EXPERIMENTAL (proton) q_0. Both convention entry points are swapped: "
        "the H_3 nucleon weights AND the per-interface Markov factors, which "
        "are built literally from z. Measurement only."
    )
    wb.set_content_block("prop:interface-knot-markov-z")
    log(f"witness -> {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
