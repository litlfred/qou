#!/usr/bin/env python3
"""Mass-binding dashboard — B_AME vs the standard-part binding forms + masses.

Powers the `/dashboard-low` and `/dashboard-sweep` commands. Every binding form
is evaluated from the ONE canonical Jones–Markov transfer trace (`tr_m_atom_zn`,
the fine-Bratteli path); B_AME comes from the vendored AME2020 table
(`data/ame2020.json`). This is the multi-isotope view of the single-pipeline
probe `binding_single_pipeline_comparison.py` (PR #2320); see the appendix
`standard-part-functor.md` for the form definitions.

Feasibility: `B_sym` is the EXACT log-ratio binding, but it no longer needs the
full per-knot trace `tr_M(W_atom)` (whose partition sum p(3A) explodes — ¹²C
5.5 min, ¹⁶O hours; the wall is intrinsically O(p(3A)), commit 61abcca9). The
atom word is a monotone braid with one inter-nucleon crossing per distinct
generator, so the log-binding factorizes over the (A−1) adjacency bonds:
`B_sym = α[(Z−1)L_pp + L_pn + (N−1)L_nn]` (audit 2026-06-16-b-sym-linear-chain-
closed-form.md), built from the same three 2-nucleon `Lbond` constants the
q-CLT already uses. So `B_sym` (and `m_sym_atom`) are now computed for EVERY
isotope from a closed form; the exact p(3A) trace is still run when
`n = 3A ≤ --max-strands` (default 21, A ≤ 7) purely to VALIDATE the chain
(|chain − exact| ≈ 1e-13). The factorized q-CLT and ⁴He magic volume remain the
cruder A→∞ extrapolations shown alongside for comparison.

EXPLORATORY presentation tool — no production rewire, no fit, no witness emitted
(the canonical witness is the probe's). α = E₀ throughout.

Usage:
    python3 mass_binding_dashboard.py --group low      # /dashboard-low
    python3 mass_binding_dashboard.py --group sweep    # /dashboard-sweep
    python3 mass_binding_dashboard.py 6Li 12C 56Fe     # explicit isotopes
    python3 mass_binding_dashboard.py --group sweep --max-strands 27   # more trace rows
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

# (name, Z, N) grouped by mass band. The sweep is a curated spread low→high so
# the trend (and the breakdown past the light nuclei) is visible in one view.
GROUPS = {
    "low":     [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
                ("6Li", 3, 3), ("7Li", 3, 4)],
    "low-mid": [("9Be", 4, 5), ("12C", 6, 6)],
    "mid":     [("16O", 8, 8), ("24Mg", 12, 12), ("40Ca", 20, 20)],
    "high":    [("56Fe", 26, 30)],
}
SWEEP = [("2H", 1, 1), ("4He", 2, 2),
         ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6),
         ("16O", 8, 8), ("24Mg", 12, 12), ("40Ca", 20, 20),
         ("56Fe", 26, 30)]


def _ame_table():
    """(Z, A) → (total binding energy MeV, experimental 1σ MeV) from the
    vendored AME2020 table. σ_B = binding_energy_per_A_unc_keV × A (the
    per-nucleon uncertainty scales with A for the total)."""
    d = json.loads((HERE / "data" / "ame2020.json").read_text())
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    out = {}
    for r in rows:
        b = r.get("binding_energy_total_keV")
        if b is not None:
            unc_perA = r.get("binding_energy_per_A_unc_keV") or 0.0
            sigma = unc_perA * r["A"] / 1000.0          # total σ_B in MeV
            out[(r["Z"], r["A"])] = (b / 1000.0, sigma)
    return out


def _constants():
    from q_parameter import Q as q0
    from knot_volumes import VOL_BORROMEAN
    from codata_constants import M_E_MEV as me
    me, q0, g8 = float(me), float(q0), float(VOL_BORROMEAN)
    return me, q0, me / (q0 * (q0 - 1.0)), g8        # me, q0, E0, 8G


def _bond_type_L():
    """Per-bond-type 2-nucleon sub-braid log-suppression: p-p (2,0), p-n (1,1),
    n-n (0,2). The V_i of the factorized q-CLT, computed once."""
    from tr_m_atom_via_transfer import tr_m_atom_zn
    out = {}
    for key, (Z, N) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
        ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
        out[key] = math.log(float(tf) / float(ta))
    return out


def _nucleon_msym(alpha):
    """Per-nucleon Kashaev mass m_sym(W) = −α·ln tr_M(W) for the free proton and
    neutron (A=1 sub-braids; cheap). The free atom word factorizes
    tr_free = tr_p^Z·tr_n^N, so m_sym(free components) = Z·msp + N·msn for ANY A
    with no bound-knot trace — the un-gateable half of the B_sym decomposition.

    NB: this is the LOG-TRACE internal mass (sub-MeV; tr_M(nucleon) ≈ 1.065), the
    quantity differenced to give B_sym = m_sym_atom − m_sym_free. It is NOT the
    physical nucleon rest mass — for that see `_nucleon_mass_canonical`."""
    from tr_m_atom_via_transfer import tr_m_atom_zn
    tp = float(tr_m_atom_zn(1, 0, dps=50)[1])   # A=1 → no interfaces → atom==free
    tn = float(tr_m_atom_zn(0, 1, dps=50)[1])
    return -alpha * math.log(tp), -alpha * math.log(tn)


def _nucleon_mass_canonical(me, q0):
    """Framework-DERIVED physical nucleon rest masses (m_p, m_n) in MeV — the
    GeV-scale categorical prediction, used for the pure-canonical constituent sum.

    m_p = m_e·Vol(𝓑₃)·ρ_global(q₀)/ℏ_q²  (the production global-scalar reading of
    the canonical mass formula m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²; ≈ 966.05 MeV, +2.96%
    vs CODATA — the known m_p gap). m_n then follows the canonical 3-input chain
    m_n = m_p + Q_β,derived + m_e with the q₀-derived β-decay scale
    Q_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³). No measured nucleon mass enters: every
    term scales off the CAL-1 unit m_e. (The per-block H₃ trace reading gives
    m_p ≈ 406 MeV (−57%) and is NOT production — see mass_vol_density.py:129.)"""
    import mpmath as _mp
    from mass_vol_density import mass_vol_density
    from knot_volumes import VOL_BORROMEAN
    from derived_masses import q_beta_predicted_mev
    me_mp, q_mp = _mp.mpf(str(me)), _mp.mpf(str(q0))
    m_p = float(mass_vol_density(me_mp, _mp.mpf(str(VOL_BORROMEAN)), q_mp))
    m_n = m_p + float(q_beta_predicted_mev()) + float(me)
    return m_p, m_n


def _row(name, Z, N, alpha, me, g8, Lbond, nucleon_msym, ame, max_strands):
    A = Z + N
    n = 3 * A
    bame_t = ame.get((Z, A))
    bame = bame_t[0] if bame_t else None
    sigma_ame = bame_t[1] if bame_t else None
    # ---- cheap forms (any A): factorized q-CLT + ⁴He magic volume -----------
    n_pp, n_pn, n_nn = comb(Z, 2), Z * N, comb(N, 2)
    sigma_L = n_pp * Lbond["pp"] + n_pn * Lbond["pn"] + n_nn * Lbond["nn"]
    Lbar = sigma_L / comb(A, 2) if A >= 2 else 0.0
    B_fac = alpha * (A - 1) * Lbar
    # ---- B_magic GENERALIZED (owner request 2026-06-23): the doubly-magic ⁴He
    #   magic-volume binding 2·m_e·A·8G is linear in A and exact-at-⁴He by
    #   construction. Ungated to ALL A as the *linear magic-volume reference*
    #   (8G = Vol(Borromean) carried per nucleon). It over-binds light nuclei
    #   and under-binds heavy ones — it is the linear-in-A line, the complement
    #   of the SATURATING B_lin below. Not a per-nucleus categorical derivation
    #   beyond ⁴He; flagged as a reference extrapolation in the legend.
    #   A=1 (lone nucleon) has no binding → None.
    B_magic = 2.0 * me * A * g8 if A >= 2 else None
    # ---- colour-weighting decomposition of the factorized q-CLT ------------
    #   B_qCLT_fac = isospin-symmetric baseline (every bond = the deuteron p-n
    #   bond) + the p↔n chirality correction. The baseline IS the uniform
    #   B_qCLT — pure combinatorics on a cached constant, so it (and the
    #   free-component mass below) are available for ALL A.
    B_base = alpha * (A - 1) * Lbond["pn"]
    B_qCLT = B_base                                  # uniform per-bond (un-gated)
    B_chir = B_fac - B_base
    # free-component Kashaev mass: tr_free = tr_p^Z·tr_n^N factorizes over GB
    # components, so m_sym(free) = Z·msp + N·msn for ANY A (no bound-knot trace).
    msp, msn = nucleon_msym
    m_sym_free = Z * msp + N * msn
    # ---- B_sym closed form: the EXACT linear chain (all A, no p(3A) sweep) --
    #   The atom word ['p']·Z+['n']·N places exactly ONE inter-nucleon crossing
    #   per DISTINCT generator (monotone word), so the log-binding factorizes
    #   over the (A−1) adjacency bonds — (Z−1) p-p, 1 p-n interface, (N−1) n-n:
    #       B_sym = α[(Z−1)L_pp + L_pn + (N−1)L_nn]
    #   with L_X the single-bond log-suppression already in Lbond. Verified ≡
    #   the exact p(3A) trace to the 50-dps floor through ¹²C (audit
    #   2026-06-16-b-sym-linear-chain-closed-form.md). So B_sym — and
    #   m_sym_atom = B_sym + m_sym_free — are available for EVERY isotope:
    #   ¹⁶O/⁴⁰Ca/⁵⁶Fe instant, with NO exact-trace wall (which 61abcca9 showed
    #   is intrinsically O(p(3A)): ¹²C 5.5 min, ¹⁶O hours).
    b_pp, b_pn, b_nn = (alpha * Lbond["pp"], alpha * Lbond["pn"],
                        alpha * Lbond["nn"])
    pn_term = b_pn if (Z >= 1 and N >= 1) else 0.0
    # max(·,0): a single-nucleon / zero-count species has no same-species bonds
    # (Z−1 or N−1 would otherwise go negative and fabricate a spurious bond).
    B_sym = max(Z - 1, 0) * b_pp + pn_term + max(N - 1, 0) * b_nn
    m_sym_atom = B_sym + m_sym_free               # B_sym = m_sym_atom − m_sym_free
    # ---- B_lin = α·s, the LINEAR/SATURATING leading term of B_sym. The bond
    #   suppression s = 1 − tr_atom/tr_free and B_sym = α·L = −α·ln(1−s), so
    #   s = 1 − e^{−L} with L = B_sym/α — recoverable from the closed-form chain
    #   (no exact trace needed). B_lin = α·s = α(1 − e^{−B_sym/α}) saturates at α
    #   (s < 1), so it under-binds increasingly with A. Leading term: B_lin ≈ B_sym
    #   for small L (B_sym = α(s + s²/2 + …)).
    B_lin = alpha * (1.0 - math.exp(-B_sym / alpha)) if alpha else 0.0
    # ---- exact p(3A) trace (capped) — VALIDATOR of the chain + the bar-
    #   involution entanglement split. Computed only when n=3A ≤ max_strands;
    #   |chain − exact| ≈ 1e-13.
    B_sym_exact = chain_resid = None
    E_retained = E_emitted = E_multilink = B_sym_ent = None
    if n <= max_strands:
        from tr_m_atom_via_transfer import tr_m_atom_zn
        import mpmath as _mp
        from q_parameter import Q as _Q0
        ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
        ta, tf = float(ta), float(tf)
        B_sym_exact = alpha * math.log(tf / ta)
        chain_resid = abs(B_sym - B_sym_exact)
        # entanglement (sibling d5f247b40d/23a0019e7f): bar-involution (q↦q⁻¹)
        # split — bar-even (cosh) = RETAINED binding/volume; bar-odd (sinh) =
        # EMITTED/radiated (Chern–Simons / γγ̄). E_multilink = bar-odd of the
        # inter-nucleon binding defect (tr_free−tr_atom); B_sym_ent augments the
        # chain binding with the radiated inter-nucleon energy.
        ta_i, tf_i, _, _ = tr_m_atom_zn(Z, N, q=_mp.mpf(1) / _mp.mpf(str(_Q0)), dps=50)
        ta_i, tf_i = float(ta_i), float(tf_i)
        E_retained = alpha * (ta + ta_i) / 2.0
        E_emitted = alpha * abs(ta - ta_i) / 2.0
        defect0, defecti = tf - ta, tf_i - ta_i
        E_multilink = alpha * abs((defect0 - defecti) / 2.0)
        B_sym_ent = B_sym + E_multilink
    return {"name": name, "Z": Z, "N": N, "A": A, "n": n, "B_AME": bame,
            "sigma_AME": sigma_ame,
            "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
            "B_lin": B_lin,
            "B_sym": B_sym, "B_sym_exact": B_sym_exact, "chain_resid": chain_resid,
            "B_qCLT": B_qCLT,
            "B_qCLT_fac": B_fac, "B_base": B_base, "B_chir": B_chir,
            "B_magic": B_magic, "E_retained": E_retained, "E_emitted": E_emitted,
            "E_multilink": E_multilink, "B_sym_ent": B_sym_ent,
            "m_sym_atom": m_sym_atom, "m_sym_free": m_sym_free}


def _fmt(v, w=8, p=2):
    return f"{v:>{w}.{p}f}" if v is not None else f"{'—':>{w}}"


def _sci(v, w=11, p=2):
    """Scientific-notation cell — for sub-keV σ_exp values that round to
    0.000000 in fixed-point and read as a misleading empty column."""
    return f"{v:>{w}.{p}e}" if v is not None else f"{'—':>{w}}"


def _err(bame, b):
    return (bame / b) if (bame is not None and b is not None and b > 0) else None


def _print_legend() -> None:
    """Explain every column header used across the dashboard's tables, so the
    output is self-documenting when pasted into a PR / issue. Grouped by table;
    every header that appears below is defined here."""
    print("#### Column legend (every header, by table)")
    print("""
**Shared** — `iso` = isotope label · `A` = mass number A = Z+N (Z protons, N neutrons).

**Table 1 — Binding B (MeV)**

| Header | Meaning |
|---|---|
| `B_AME` | Total nuclear binding energy from AME2020 (MeV) — the experimental target |
| `σ_exp (MeV)` | AME2020 experimental 1σ on the total binding (scientific notation; sub-keV for light nuclei) |
| `σ_exp (ppm)` | The same 1σ as a relative figure (σ_exp / B_AME × 10⁶) |
| `B_lin` | LINEAR/saturating binding α·s, s = 1−e^(−B_sym/α) (leading term of B_sym; bounded by α, under-binds with A) |
| `B_sym` | EXACT log-ratio binding α·ln(tr_free/tr_atom) = α[(Z−1)L_pp + L_pn + (N−1)L_nn] — the archimedean realization |
| `B_qCLT` | Uniform per-bond q-CLT α·(A−1)·ℓ̄(D) — no p↔n colour weighting |
| `B_qCLT_fac` | p↔n colour-weighted q-CLT α·(A−1)·⟨bond-type L⟩ |
| `B_magic` | Magic-volume binding 2·m_e·A·8G (GENERALIZED to all A; exact-at-⁴He by construction, linear-in-A reference elsewhere — over-binds light, under-binds heavy) |

**Table 2 — Error (B_AME / B_model; 1.00 = perfect, >1 under-binds)**

| Header | Meaning |
|---|---|
| `lin` / `sym` / `qCLT` / `qCLT_fac` / `magic` | B_AME / B_model for that binding form |
| `σ_exp (ppm)` | (as Table 1) experimental 1σ relative to B_AME |
| `best dev / σ_exp` | Best form's \\|B_model − B_AME\\| measured in experimental σ (the L2-100× gap) |

**Table 3 — Mass M = (constituents) − B (MeV)**

| Header | Meaning |
|---|---|
| `m_unbnd,can` | Framework-DERIVED unbound sum Z·m_p,can + N·m_n,can (m_p,can = m_e·Vol·ρ/ℏ_q² ≈ 966 MeV +2.96%; m_n,can = m_p,can + Q_β,derived + m_e) |
| `m_unbnd` | MEASURED unbound sum Z·m_p + N·m_n (CODATA m_p=938.272, m_n=939.565) |
| `M_AME` | Measured atomic mass = m_unbnd − B_AME |
| `m_lin` / `m_sym` / `m_qCLT` / `m_qCLT_fac` / `m_magic` | PURE-CANONICAL bound mass = m_unbnd,can − B_X (framework constituents; carries the +2.96%·A m_p gap) for X in {lin, sym, qCLT, qCLT_fac, magic} |
| `m_lin,rel` / `m_sym,rel` / `m_qCLT,rel` / `m_qCLT_fac,rel` / `m_magic,rel` | Measured-relative bound mass = m_unbnd − B_X (same canonical binding B_X, measured baseline) |

**Table 4 — Entanglement (bar-involution q↦q⁻¹ split of the atom trace)**

| Header | Meaning |
|---|---|
| `retained E` | E₀·bar-even (cosh) channel — retained binding/volume (MeV) |
| `emitted E` | E₀·\\|bar-odd\\| (sinh) channel — emitted/radiated γγ̄ (MeV) |
| `multi-link emit` | bar-odd of the inter-nucleon binding defect (tr_free−tr_atom) — radiated inter-nucleon energy (MeV) |
| `emitted/retained` | ratio emitted E / retained E |

**Table 5 — Entanglement-augmented binding**

| Header | Meaning |
|---|---|
| `B_sym` | (as Table 1) the log-ratio binding |
| `err sym` | B_AME / B_sym |
| `B_sym+ent` | B_sym + multi-link emitted energy |
| `err sym+ent` | B_AME / B_sym+ent |

**Table 6 — Colour-weighting (B_qCLT_fac = baseline + p↔n chirality)**

| Header | Meaning |
|---|---|
| `bonds pp/pn/nn` | bond counts: pp = C(Z,2), pn = Z·N, nn = C(N,2) |
| `sym baseline` | isospin-symmetric baseline α·(A−1)·L_pn (every bond = the deuteron p-n bond) |
| `+ chirality` | the p↔n colour correction B_qCLT_fac − baseline |
| `= B_qCLT_fac` | their sum (the colour-weighted q-CLT binding) |

**Table 7 — Compositional B_sym (m_sym(W) = −α·ln tr_M(W))**

| Header | Meaning |
|---|---|
| `m_sym(free comps)` | LOG-TRACE internal mass of the free word Z·msp + N·msn (sub-MeV; NOT a rest mass) |
| `m_sym(atom)` | LOG-TRACE internal mass of the bound atom word (sub-MeV; NOT a rest mass) |
| `B_sym (chain)` | the closed-form chain binding = m_sym(atom) − m_sym(free comps) |
| `Δ vs exact trace` | \\|chain − exact p(3A) trace\\| where the trace is feasible (n=3A ≤ max-strands), else "— (no trace)" |
""")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Mass-binding low-isotope dashboard")
    ap.add_argument("isotopes", nargs="*", help="explicit isotopes e.g. 6Li 12C")
    ap.add_argument("--group", choices=["low", "low-mid", "mid", "high", "sweep"],
                    help="named isotope band")
    ap.add_argument("--max-strands", type=int, default=21,
                    help="trace forms (B_sym/B_qCLT) computed only when "
                         "n=3A ≤ this (default 21 = A≤7; raise for more rows, slower)")
    args = ap.parse_args(argv)

    # resolve the isotope list
    by_name = {nm: (nm, Z, N) for grp in GROUPS.values() for (nm, Z, N) in grp}
    by_name.update({nm: (nm, Z, N) for (nm, Z, N) in SWEEP})
    if args.isotopes:
        sel = []
        for nm in args.isotopes:
            if nm not in by_name:
                print(f"  unknown isotope {nm!r}; known: {', '.join(sorted(by_name))}")
                return 2
            sel.append(by_name[nm])
    elif args.group == "sweep":
        sel = SWEEP
    elif args.group:
        sel = GROUPS[args.group]
    else:
        sel = GROUPS["low"]

    # Prepend the single-nucleon reference rows (proton, neutron): A=1, no
    # binding, so they display the bare nucleon-level m_p/m_n gap (canonical
    # m_p,can ≈ 966 vs measured 938). Deduped against the selection.
    present = {(Z, N) for (_, Z, N) in sel}
    sel = [nuc for nuc in (("p", 1, 0), ("n", 0, 1))
           if (nuc[1], nuc[2]) not in present] + sel

    me, q0, E0, g8 = _constants()
    Lbond = _bond_type_L()
    nucleon_msym = _nucleon_msym(E0)         # per-nucleon free Kashaev mass (cheap)
    mp_can, mn_can = _nucleon_mass_canonical(me, q0)   # framework-derived rest masses
    ame = _ame_table()                       # parse AME2020 once, not per row
    rows = [_row(nm, Z, N, E0, me, g8, Lbond, nucleon_msym, ame, args.max_strands)
            for (nm, Z, N) in sel]

    title = (args.group or ("custom" if args.isotopes else "low")).upper()
    print(f"\n  MASS-BINDING DASHBOARD [{title}]   α = E₀ = {E0:.4f} MeV"
          f"   (bond-type L: pp={Lbond['pp']:.3f} pn={Lbond['pn']:.3f} "
          f"nn={Lbond['nn']:.3f})")
    print(f"  B_sym/m_sym_atom: EXACT closed-form linear chain → all A; the "
          f"p(3A) trace is run for n=3A ≤ {args.max_strands} (A ≤ "
          f"{args.max_strands // 3}) only to validate the chain. "
          f"qCLT/fac/magic + m_sym(free): combinatorial → all A.\n")

    _print_legend()

    # 1. MASS  M = (constituents) − B  (shown first, per owner request 2026-06-24)
    #    Two-column convention (owner-set 2026-06-22): wherever the nucleon masses
    #    enter the constituent sum we report BOTH:
    #      • a PURE-CANONICAL column — framework-DERIVED nucleon rest masses
    #        (m_p,can = m_e·Vol(𝓑₃)·ρ_global/ℏ_q² ≈ 966.05 MeV, +2.96% gap;
    #        m_n,can = m_p,can + Q_β,derived + m_e). No measured nucleon mass enters
    #        — everything scales off the CAL-1 unit m_e. m_sym = m_unbnd,can − B_sym.
    #      • a "…,rel" column — the SAME canonical binding B_X subtracted from
    #        the MEASURED constituent sum mu = Z·m_p + N·m_n (CODATA). This is the
    #        experiment-anchored reading, kept for AME comparison.
    #    The binding B_X itself is the single canonical value in both readings;
    #    only the constituent baseline differs (framework-derived vs measured). The
    #    ~2.96%·A spread between m_X and m_X,rel IS the propagated m_p gap.
    from codata_constants import M_P_MEV_VALIDATION as mp_, M_N_MEV_VALIDATION as mn_
    mp_, mn_ = float(mp_), float(mn_)
    print("### Mass  M = (constituents) − B (MeV)   "
          "[canonical = framework-derived nucleon masses; ,rel = measured CODATA mu]")
    print(f"  canonical constituents: m_p,can = {mp_can:.3f} MeV (+"
          f"{(mp_can/mp_-1)*100:.2f}%), m_n,can = {mn_can:.3f} MeV "
          f"(= m_p,can + Q_β,derived + m_e). Every binding form has BOTH a "
          f"canonical (m_X = m_unbnd,can − B_X) and a ,rel (m_X,rel = m_unbnd − B_X) mass.")
    print("| iso | A | m_unbnd,can | m_unbnd | M_AME | m_lin | m_lin,rel | m_sym | m_sym,rel "
          "| m_qCLT | m_qCLT,rel | m_qCLT_fac | m_qCLT_fac,rel | m_magic | m_magic,rel |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        mu = r["Z"] * mp_ + r["N"] * mn_                 # measured constituent sum
        mu_can = r["Z"] * mp_can + r["N"] * mn_can       # framework-derived sum
        mame = (mu - r["B_AME"]) if r["B_AME"] is not None else None
        # each form X: m_X (canonical, mu_can − B_X) and m_X,rel (measured, mu − B_X)
        def _pair(bkey):
            b = r[bkey]
            if b is None:
                return None, None
            return mu_can - b, mu - b
        m_lin_can, m_lin_rel = _pair("B_lin")
        m_sym_can, m_sym_rel = _pair("B_sym")
        m_qclt_can, m_qclt_rel = _pair("B_qCLT")
        m_fac_can, m_fac_rel = _pair("B_qCLT_fac")
        m_magic_can, m_magic_rel = _pair("B_magic")
        print(f"| {r['name']} | {r['A']} | {mu_can:>9.1f} | {mu:>9.1f} "
              f"| {_fmt(mame,9,1)} | {_fmt(m_lin_can,9,1)} | {_fmt(m_lin_rel,9,1)} "
              f"| {_fmt(m_sym_can,9,1)} | {_fmt(m_sym_rel,9,1)} "
              f"| {_fmt(m_qclt_can,9,1)} | {_fmt(m_qclt_rel,9,1)} "
              f"| {_fmt(m_fac_can,9,1)} | {_fmt(m_fac_rel,9,1)} "
              f"| {_fmt(m_magic_can,9,1)} | {_fmt(m_magic_rel,9,1)} |")

    # 2. BINDING  (B_AME ± experimental 1σ from AME2020)
    print("### Binding  B (MeV)   [σ_exp = AME2020 experimental 1σ]")
    print("| iso | A | B_AME | σ_exp (MeV) | σ_exp (ppm) | B_lin | B_sym | B_qCLT | B_qCLT_fac | B_magic |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        s = r["sigma_AME"]
        s_ppm = (s / r["B_AME"] * 1e6) if (s and r["B_AME"]) else None
        print(f"| {r['name']} | {r['A']} | {_fmt(r['B_AME'])} | {_sci(s,11,2)} "
              f"| {_fmt(s_ppm,11,3)} | {_fmt(r['B_lin'])} | {_fmt(r['B_sym'])} "
              f"| {_fmt(r['B_qCLT'])} | {_fmt(r['B_qCLT_fac'])} | {_fmt(r['B_magic'])} |")

    # 1b. chain ≡ exact-trace validation (rows where the p(3A) trace is feasible)
    val = [(r["name"], r["chain_resid"]) for r in rows
           if r["chain_resid"] is not None]
    if val:
        mx = max(v[1] for v in val)
        print(f"\n  B_sym closed-form chain ≡ exact p(3A) trace: max|Δ| = "
              f"{mx:.1e} MeV over {{{', '.join(v[0] for v in val)}}} "
              f"(n=3A ≤ {args.max_strands}; float64 dashboard noise — the chain "
              f"≡ trace to the 50-dps floor through ¹²C, audit "
              f"2026-06-16-b-sym-linear-chain-closed-form.md). Chain used for all A.")

    # 2. ERROR  B_AME / B_model, alongside the experimental precision and the
    #    best form's deviation measured in experimental σ (how far past the
    #    100× L2 target each form sits).
    print("\n### Error  (B_AME / B_model; 1.00 = perfect, >1 under-binds)")
    print("| iso | A | lin | sym | qCLT | qCLT_fac | magic | σ_exp (ppm) | best dev / σ_exp |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        e = {k: _err(r["B_AME"], r[k]) for k in
             ("B_lin", "B_sym", "B_qCLT", "B_qCLT_fac", "B_magic")}
        s = r["sigma_AME"]
        s_ppm = (s / r["B_AME"] * 1e6) if (s and r["B_AME"]) else None
        # best model = smallest |B_AME − B_model|; report its deviation in σ_exp
        cand = [r[k] for k in ("B_lin", "B_sym", "B_qCLT", "B_qCLT_fac", "B_magic") if r[k]]
        best_dev_sigma = None
        if cand and s and r["B_AME"]:
            best = min(cand, key=lambda b: abs(b - r["B_AME"]))
            best_dev_sigma = abs(best - r["B_AME"]) / s
        print(f"| {r['name']} | {r['A']} | {_fmt(e['B_lin'],6)} | {_fmt(e['B_sym'],6)} "
              f"| {_fmt(e['B_qCLT'],6)} | {_fmt(e['B_qCLT_fac'],6)} "
              f"| {_fmt(e['B_magic'],6)} | {_fmt(s_ppm,11,3)} "
              f"| {_fmt(best_dev_sigma,16,3) if best_dev_sigma else _fmt(None,16)} |")

    # 3b. ENTANGLEMENT  (bar-involution q↦q⁻¹ split of the atom trace, via the
    #     q-parameterised core): bar-even (cosh) = retained binding/volume;
    #     bar-odd (sinh) = emitted/radiated Chern–Simons / γγ̄ channel.
    print("\n### Entanglement  (E₀·bar-even = retained binding/volume, E₀·|bar-odd| = emitted γγ̄ channel)")
    print("| iso | A | retained E (MeV) | emitted E (MeV) | multi-link emit (MeV) | emitted/retained |")
    print("|---|--:|--:|--:|--:|--:|")
    for r in rows:
        er, ee, eml = r.get("E_retained"), r.get("E_emitted"), r.get("E_multilink")
        ratio = (ee / er) if (er and ee and er != 0) else None
        print(f"| {r['name']} | {r['A']} | {_fmt(er,8,3)} | {_fmt(ee,8,3)} "
              f"| {_fmt(eml,8,3)} | {_fmt(ratio,8,4)} |")

    # 3c. ENTANGLEMENT-AUGMENTED BINDING + error: does adding the inter-nucleon
    #     emitted (multi-link) energy to the log-trace binding improve the AME fit?
    print("\n### Entanglement-augmented binding  (B_sym+ent = B_sym + multi-link emit; error = B_AME/B)")
    print("| iso | A | B_AME | B_sym | err sym | B_sym+ent | err sym+ent |")
    print("|---|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        bs, bse = r.get("B_sym"), r.get("B_sym_ent")
        es = _err(r["B_AME"], bs)
        ese = _err(r["B_AME"], bse)
        print(f"| {r['name']} | {r['A']} | {_fmt(r['B_AME'])} | {_fmt(bs)} "
              f"| {_fmt(es,6)} | {_fmt(bse)} | {_fmt(ese,6)} |")

    # 4. COLOUR-WEIGHTING decomposition (B_qCLT_fac = baseline + p↔n chirality)
    print("\n### Colour-weighting  (B_qCLT_fac = isospin-symmetric baseline + p↔n chirality)")
    print("| iso | A | bonds pp/pn/nn | sym baseline | + chirality | = B_qCLT_fac |")
    print("|---|--:|:--:|--:|--:|--:|")
    for r in rows:
        print(f"| {r['name']} | {r['A']} | {r['n_pp']}/{r['n_pn']}/{r['n_nn']} "
              f"| {r['B_base']:>8.2f} | {r['B_chir']:>+8.2f} | {r['B_qCLT_fac']:>8.2f} |")

    # 5. COMPOSITIONAL B_sym (atom GB-braid mass − free GB-component masses).
    #   m_sym(free) is combinatorial (all A); m_sym(atom) needs the bound trace.
    print("\n### Compositional B_sym  (m_sym(W) = −α·ln tr_M(W); free = GB components)")
    print("| iso | A | m_sym(free comps) | m_sym(atom) | B_sym (chain) | Δ vs exact trace |")
    print("|---|--:|--:|--:|--:|--:|")
    for r in rows:
        resid = (f"{r['chain_resid']:.1e}" if r["chain_resid"] is not None
                 else "—  (no trace)")
        print(f"| {r['name']} | {r['A']} | {r['m_sym_free']:>8.3f} "
              f"| {_fmt(r['m_sym_atom'],8,3)} | {_fmt(r['B_sym'],8,3)} | {resid:>16} |")

    print("\n  Forms: B_sym=α·ln(tr_free/tr_atom)=α[(Z−1)L_pp+L_pn+(N−1)L_nn] "
          "(exact linear chain, all A) · B_qCLT=α·(A−1)·ℓ̄(D) · "
          "B_qCLT_fac=α·(A−1)·⟨bond-type L⟩ · B_magic=2·m_e·A·8G (⁴He). "
          "Defn: standard-part-functor.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
