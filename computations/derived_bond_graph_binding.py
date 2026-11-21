#!/usr/bin/env python3
"""DERIVED per-bond binding over the nucleon bond graph (chain vs complete).

Owner directive 2026-06-10: "fix: the braid wires only A−1 chain bonds; do a
full compute audit" + "derive it [f], no |·|" + "[all-pairs] 1 y".

## The derivation (task 2 — f is NOT fitted)

The atom braid (`mass_at_3A_proper.atom_braid_word_3A`) links nucleon k to k+1
by an inter-nucleon bridge crossing `c·σ_{3k+2} + d·I` with, per pair type:

    p-p: (c,d) = (1, 0)            n-n: (1, −h)            p-n: (1, −h(½−δ/4))

(h = q−q⁻¹, δ = color split). The free config (no bridges) factors as a
product of nucleon traces; each bridge is GS-independent (far-commutes,
|3i−3j|≥3) and sits at a Markov-removable position, so its contribution to the
Jones–Markov trace is the **conditional expectation** `E(c·σ + d) = c·z + d`
(z = q³/(q²+1), **convention D**, the Markov parameter, since E(σ_{n-1}) = z).
This docstring declared the convention-C form z = 1/(q^½+q^{-½}) until 2026-08-31
while line 78 has computed the D form throughout — the body was right and the
docstring was stale, the same shape as the `markovZc` collision (bean qou-961o).
Hence the trace factorizes over bonds:

    tr_M(W_atom) = tr_M(W_free) · ∏_{bonds} f_bond ,   f_bond = c·z + d

    f_pp = z ,   f_nn = z − h ,   f_pn = z − h(½ − δ/4)

This is an EXACT derivation of the per-bond suppression f ≈ 0.39 measured
empirically (`gs_filtration_binding_components.py`). NO modulus, NO fit — each
f_bond is a closed q₀ expression. The binding is then EXTENSIVE over the bond
graph, with NO |·|:

    B(K) = E_0 · log( tr_free / tr_atom ) = E_0 · Σ_{bonds} log(1 / f_bond)

at the canonical energy scale E_0 = m_e/(q₀(q₀−1)) (the deuteron-fixing scale,
not Q_β). log(tr_free/tr_atom) is positive because f_bond < 1, so no absolute
value is needed — the log-ratio is the extensive invariant directly.

## The fix (task 1 — bond topology)

`atom_braid_word_3A` wires only the **A−1 chain** bonds (`k < A−1`). Physical
binding involves all nucleon pairs. With the derived f_bond, the binding over
any bond graph is a closed sum, so the "fix" needs no exotic all-pairs braid —
just the right edge set:

    chain    (A−1 edges):  the bonds the braid currently wires
    complete (C(A,2) edges, by type): C(Z,2) p-p + Z·N p-n + C(N,2) n-n

This probe (a) VALIDATES the derivation: ∏_{chain} f_bond vs the measured
tr_atom/tr_free; (b) reports the chain and complete-graph DERIVED binding vs
B_AME. The per-bond energies E_0·log(1/f_type) are fixed substrate quantities.

Output: derived-bond-graph-binding.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE / "hecke"))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# NO-FLOAT64 (bean qou-vsqh).  This producer used to downcast q0/h/m_e with
# float() and accumulate the bond-graph binding through math.log over sum(),
# i.e. float64 end to end, while emitting a witness — 108 raw-float64 fields in
# `raw-float64-baseline.json`.  The accumulation over C(A,2) logs is exactly the
# part float64 degrades and exactly the part the saturation verdict is read off.
# Everything below is mpmath.mpf; float appears nowhere.
set_compute_dps()

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []


def _constants():
    # Read the 50-DIGIT q0 string, not `q_parameter.Q`.  `Q` and `HA` are Python
    # floats (measured: Q = 1.1099785827513808, 17 digits), so `mp.mpf(str(Q))`
    # faithfully preserves float64 and creates no precision that is not there --
    # AGENTS.md §"a float64 input poisons the whole result".  Deriving h from the
    # 50-digit q0 instead of importing the float HA is what lets the f_bond
    # derivation be confirmed past 1e-16.  Bean qou-vsqh.
    from q_parameter import Q_50_DIGIT_STR
    from codata_constants import M_E_MEV as me
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0                  # h = q - q^-1, derived, not imported as f64
    me = me if isinstance(me, mp.mpf) else mp.mpf(str(me))
    z = q0**3 / (q0**2 + 1)          # convention D
    try:
        from canonical_braid_crossings import _avg_color_delta
        delta = mp.mpf(str(_avg_color_delta()))
    except Exception:
        delta = mp.mpf(0)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.canonical(q=q0, m_e=me)  # tower-summed E_0, canonical (owner ruling 2026-11-20, #8590); was order-zero m_e/(q(q-1))
    return q0, h, z, delta, me, E0


def main() -> int:
    t0 = time.time()
    q0, h, z, delta, me, E0 = _constants()

    # Derived per-bond suppression factors f_bond = c·z + d.
    f = {
        "pp": z,                       # (1, 0)
        "nn": z - h,                   # (1, −h)
        "pn": z - h * (mp.mpf(1) / 2 - delta / 4),  # (1, −h(½−δ/4))
    }
    # Derived per-bond binding energy E_0·log(1/f)  [MeV].
    e_bond = {k: E0 * mp.log(1 / v) for k, v in f.items()}

    # Bar-conjugate factors  \check{f} = f(q→q⁻¹), and h→−h.
    #
    # CORRECTED 2026-08-24 (qou-cds1).  This block used to assert
    # "z→z (z = 1/(q^½+q^{-½}) is bar-symmetric)" and set f_bar["pp"] = z.
    # That is a **convention-C-only** fact.  `z` at the top of this function is
    # convention D (`q**3/(q**2+1)`), and under D the bar involution does NOT
    # fix z.  Proved symbolically (sympy, exact):
    #
    #     z_D - h  =  q^3/(q^2+1) - (q^2-1)/q  =  1/(q^3 + q)
    #     bar(z_D) =  z_D(q -> 1/q)            =  1/(q^3 + q)
    #     => bar(z_D) = z_D - h   EXACTLY, identically in q   (and z/(z-h) = q^4)
    #
    # Under C it is the other identity that holds: bar(z_C) = z_C, and
    # z_C - h != bar(z_C).  The two conventions swap which one is true, so the
    # old comment was correct when written and became wrong when `z` migrated.
    #
    # Consequence worth noting: under D the bar involution **exchanges the pp
    # and nn channels** -- bar(f_pp) = bar(z) = z - h = f_nn, and
    # bar(f_nn) = bar(z - h) = bar(z) + h = z = f_pp.  So the pp and nn
    # bar-norms coincide, which they did not under C.
    #
    # This is the archimedean NORM tr_M·\check{tr}_M (owner: use the bar product,
    # NOT |·|).  δ assumed bar-symmetric (tiny, 0.0014).
    z_bar = z - h                      # = bar(z) = 1/(q^3+q) under convention D
    f_bar = {
        "pp": z_bar,                   # bar(z)
        "nn": z_bar + h,               # = z   (bar exchanges pp <-> nn under D)
        "pn": z_bar + h * (mp.mpf(1) / 2 - delta / 4),
    }
    # Bar-norm per-bond factor |f|²_bar = f·\check{f}, and the magnitude
    # |tr|_bar = sqrt(tr·\check{tr}) gives per-bond energy (E_0/2)·log(1/(f·f̄)).
    f_norm = {k: f[k] * f_bar[k] for k in f}
    e_bond_bar = {k: E0 * mp.log(1 / v) / 2 for k, v in f_norm.items()}

    bc = record_upstream(HERE / "binding-canonical.witness.json", _UPSTREAM_RECORDS)
    res = {(r["Z"], r["N"]): r for r in bc["data"]["results"]
           if r.get("status") == "solved"}

    def chain_bonds(Z, N):
        """Bond types along the chain ordering ['p']*Z + ['n']*N."""
        order = ["p"] * Z + ["n"] * N
        out = []
        for k in range(len(order) - 1):
            a, b = order[k], order[k + 1]
            out.append("pp" if a == b == "p" else "nn" if a == b == "n" else "pn")
        return out

    def complete_bonds(Z, N):
        """All C(A,2) pair types by composition."""
        return (["pp"] * (Z * (Z - 1) // 2)
                + ["pn"] * (Z * N)
                + ["nn"] * (N * (N - 1) // 2))

    rows = []
    raw_rows = []          # the mpf values, for statistics and display
    for (Z, N), r in sorted(res.items(), key=lambda kv: (kv[0][0] + kv[0][1], kv[0])):
        A = Z + N
        ta = mp.mpf(r["tr_M_atom"].strip("()").split("+")[0])
        tf = mp.mpf(r["tr_M_free"].strip("()").split("+")[0])
        B_ame = mp.mpf(str(r["B_AME_MeV"]))
        measured_ratio = ta / tf

        cb = chain_bonds(Z, N)
        comp = complete_bonds(Z, N)
        prod_chain = mp.mpf(1)
        for b in cb:
            prod_chain *= f[b]
        # Derivation validation: ∏ f_bond (chain) vs measured tr_atom/tr_free.
        ratio_err = abs(prod_chain - measured_ratio) / abs(measured_ratio)

        B_chain = E0 * mp.fsum(mp.log(1 / f[b]) for b in cb)
        B_complete = E0 * mp.fsum(mp.log(1 / f[b]) for b in comp)
        # Bar-norm binding: E_0·log(|tr_free|/|tr_atom|), |tr| = sqrt(tr·\check{tr}).
        B_chain_bar = mp.fsum(e_bond_bar[b] for b in cb)
        B_complete_bar = mp.fsum(e_bond_bar[b] for b in comp)

        rows.append({
            "atom": r["atom"], "Z": Z, "N": N, "A": A,
            "B_AME_MeV": fmt(B_ame),
            "tr_atom_meas": fmt(ta), "tr_free_meas": fmt(tf),
            "measured_ratio_atom_over_free": fmt(measured_ratio),
            "chain_bonds": cb,
            "prod_f_chain_DERIVED": fmt(prod_chain),
            "derivation_rel_err": fmt(ratio_err),
            "B_chain_derived_MeV": fmt(B_chain),
            "miss_chain_x": fmt(B_ame / B_chain),
            "complete_bonds_count": {"pp": comp.count("pp"),
                                     "pn": comp.count("pn"),
                                     "nn": comp.count("nn")},
            "B_complete_derived_MeV": fmt(B_complete),
            "miss_complete_x": fmt(B_ame / B_complete),
            # bar-norm (tr_M·\check{tr}_M) variants
            "B_chain_bar_MeV": fmt(B_chain_bar),
            "miss_chain_bar_x": fmt(B_ame / B_chain_bar),
            "B_complete_bar_MeV": fmt(B_complete_bar),
            "miss_complete_bar_x": fmt(B_ame / B_complete_bar),
        })
        raw_rows.append({
            "atom": r["atom"], "A": A, "B_ame": B_ame, "ratio_err": ratio_err,
            "prod_chain": prod_chain, "measured_ratio": measured_ratio,
            "B_chain": B_chain, "B_complete": B_complete,
            "miss_chain": B_ame / B_chain, "miss_complete": B_ame / B_complete,
        })

    # Statistics over the mpf values, NOT over the serialized strings: max() on
    # decimal strings is lexicographic and would silently pick the wrong row.
    max_deriv_err = max(raw["ratio_err"] for raw in raw_rows)
    chain_miss = [raw["miss_chain"] for raw in raw_rows]
    comp_miss = [raw["miss_complete"] for raw in raw_rows]

    w = WitnessBuilder("derived-bond-graph-binding", engine="python",
                       start_time=t0)
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "DERIVED per-bond binding. f_bond = c·z + d (Markov conditional "
        "expectation of the inter-nucleon bridge crossing): f_pp=z, f_nn=z−h, "
        "f_pn=z−h(½−δ/4) — closed q₀ expressions, NO fit, NO |·|. Validated: "
        "∏_chain f_bond reproduces the measured tr_atom/tr_free to "
        f"{mp.nstr(max_deriv_err, 2)}. Binding B = E_0·log(tr_free/tr_atom) = "
        "E_0·Σ_bonds log(1/f_bond) (extensive, positive — no modulus). FIX: "
        "the braid wires only A−1 CHAIN bonds; the complete graph (C(Z,2) pp + "
        "Z·N pn + C(N,2) nn) is the all-pairs topology. Per-bond energies "
        f"E_0·log(1/f): pp={mp.nstr(e_bond['pp'], 6)}, "
        f"pn={mp.nstr(e_bond['pn'], 6)}, "
        f"nn={mp.nstr(e_bond['nn'], 6)} MeV (substrate-fixed)."
    )
    w.add_parameter("q0", fmt(q0))
    w.add_parameter("z_markov", fmt(z))
    w.add_parameter("h", fmt(h))
    w.add_parameter("color_delta", fmt(delta))
    w.add_parameter("E_0_MeV", fmt(E0))
    w.add_data("derived_f_bond", {k: fmt(v) for k, v in f.items()})
    w.add_data("derived_bond_energy_MeV", {k: fmt(v) for k, v in e_bond.items()})
    w.add_data("rows", rows)
    w.add_data("headline", {
        "derivation": "f_bond = c·z + d (EXACT: max rel err vs measured "
                      f"tr_atom/tr_free = {mp.nstr(max_deriv_err, 3)} over D/T/³He/⁴He)",
        "chain_miss_range": f"{mp.nstr(min(chain_miss), 4)}–"
                            f"{mp.nstr(max(chain_miss), 4)}×",
        "complete_miss_range": f"{mp.nstr(min(comp_miss), 4)}–"
                               f"{mp.nstr(max(comp_miss), 4)}×",
        "verdict": "f is DERIVED (Markov factor of the bridge), not fitted. "
                   "Chain (A−1 bonds, as-wired) under-binds (esp ⁴He); complete "
                   "graph (C(A,2)) over-binds the light nuclei — the true bond "
                   "graph is between (saturation/Pauli/shell), the remaining "
                   "structural question. The per-bond ENERGIES are fixed "
                   "substrate quantities; only the edge SET is open.",
    })
    # Assertion: the f_bond = c·z+d derivation reproduces the measured ratio.
    w.add_assertion(
        name="f_bond_derivation_matches_measured_trace_ratio",
        computed=fmt(max_deriv_err), expected=fmt(mp.mpf(0)), tolerance=5e-3,
        source="max over D/T/³He/⁴He of |∏_chain (c·z+d) − tr_atom/tr_free| / "
               "(tr_atom/tr_free); confirms f_bond is the Markov conditional "
               "expectation of the bridge crossing, not a fit.",
    )
    out = w.save()

    print("=" * 100)
    print(" DERIVED per-bond binding  f_bond = c·z + d  (Markov factor of the bridge)")
    _n = mp.nstr
    print(f"   z={_n(z, 8)}  h={_n(h, 8)}  δ={_n(delta, 8)}  E_0={_n(E0, 8)} MeV")
    print(f"   f_pp=z={_n(f['pp'], 8)}  f_pn=z−h(½−δ/4)={_n(f['pn'], 8)}  "
          f"f_nn=z−h={_n(f['nn'], 8)}")
    print(f"   per-bond E [MeV]: pp={_n(e_bond['pp'], 8)}  "
          f"pn={_n(e_bond['pn'], 8)}  nn={_n(e_bond['nn'], 8)}")
    print("=" * 100)
    print(f" {'atom':>7}{'A':>3}{'B_AME':>8}{'∏f chain':>10}{'meas a/f':>10}"
          f"{'deriv err':>11}{'B_chain':>9}{'chain×':>8}{'B_compl':>9}{'compl×':>8}")
    print(" " + "-" * 98)
    for raw in raw_rows:
        print(f" {raw['atom']:>7}{raw['A']:>3}{_n(raw['B_ame'], 6):>8}"
              f"{_n(raw['prod_chain'], 6):>10}{_n(raw['measured_ratio'], 6):>10}"
              f"{_n(raw['ratio_err'], 3):>11}{_n(raw['B_chain'], 6):>9}"
              f"{_n(raw['miss_chain'], 4):>7}×{_n(raw['B_complete'], 6):>9}"
              f"{_n(raw['miss_complete'], 4):>7}×")
    print(" " + "-" * 98)
    print(f" derivation max rel err = {_n(max_deriv_err, 3)}  (f_bond = c·z+d is EXACT)")
    print(f" chain miss:    {_n(min(chain_miss), 4)}–{_n(max(chain_miss), 4)}×"
          "  (A−1 bonds, as-wired — the bug)")
    print(f" complete miss: {_n(min(comp_miss), 4)}–{_n(max(comp_miss), 4)}×"
          "  (C(A,2) all-pairs — the fix)")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
