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
(|chain − exact| ≈ 1e-13). The factorized q-CLT remains the
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

import codata_constants as _codata  # noqa: E402 — registry (CODATA-2022 u→MeV); bean me3r

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

NUCLEAR_SPINS = {
    "p": 0.5, "n": 0.5, "2H": 1.0, "3H": 0.5, "3He": 0.5, "4He": 0.0,
    "6Li": 1.0, "7Li": 1.5, "9Be": 1.5, "12C": 0.0, "16O": 0.0,
    "24Mg": 0.0, "40Ca": 0.0, "56Fe": 0.0
}




def q_int_float(q, n):
    return (q**n - q**(-n)) / (q - 1.0/q)

def q_fact_float(q, n):
    res = 1.0
    for i in range(1, n + 1):
        res *= q_int_float(q, i)
    return res

def hook_lengths(lam):
    hooks = []
    lam_conj = []
    for j in range(lam[0]):
        lam_conj.append(sum(1 for row in lam if row > j))
    for i, row in enumerate(lam):
        for j in range(row):
            h = (row - 1 - j) + (lam_conj[j] - 1 - i) + 1
            hooks.append(h)
    return hooks

def W_lambda_float(q, lam):
    n = sum(lam)
    hooks = hook_lengths(lam)
    prod_hooks_sq = 1.0
    for h in hooks:
        prod_hooks_sq *= (q_int_float(q, h))**2
    return q_fact_float(q, n) / prod_hooks_sq

def get_ground_state_partition(Z, N, S):
    Nu = 2*Z + N
    Nd = Z + 2*N
    if Nu == 0 and Nd == 0:
        return None
    valid_partitions = []
    for u_up in range(Nu + 1):
        u_down = Nu - u_up
        for d_up in range(Nd + 1):
            d_down = Nd - d_up
            if abs((u_up + d_up) - (u_down + d_down)) == 2 * S:
                part = tuple(sorted([u_up, u_down, d_up, d_down], reverse=True))
                part = tuple(x for x in part if x > 0)
                if part not in valid_partitions:
                    valid_partitions.append(part)
    if not valid_partitions:
        return None
    valid_partitions.sort(key=lambda p: (p[0], p))
    return valid_partitions[0]


def format_md_tables(text):
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and lines[i].endswith('|') and i+1 < len(lines) and lines[i+1].startswith('|') and '---' in lines[i+1]:
            # Found a table
            table_lines = []
            while i < len(lines) and lines[i].startswith('|') and lines[i].endswith('|'):
                table_lines.append(lines[i])
                i += 1
            # Parse table
            rows = []
            max_cols = 0
            for line in table_lines:
                cells = [cell.strip() for cell in line[1:-1].split('|')]
                max_cols = max(max_cols, len(cells))
                rows.append(cells)
            
            # Compute max widths
            widths = [0] * max_cols
            for r_idx, row in enumerate(rows):
                for c_idx, cell in enumerate(row):
                    w = len(cell)
                    if r_idx == 1: # separator
                        if cell.startswith(':') and cell.endswith(':'): w = max(3, w)
                        elif cell.startswith(':') or cell.endswith(':'): w = max(2, w)
                        else: w = max(1, w)
                    widths[c_idx] = max(widths[c_idx], w)
            
            # Format table
            for r_idx, row in enumerate(rows):
                parts = []
                for c_idx in range(max_cols):
                    cell = row[c_idx] if c_idx < len(row) else ""
                    w = widths[c_idx]
                    if r_idx == 1:
                        # Separator
                        if cell.endswith(':'):
                            if cell.startswith(':'): parts.append(':' + '-'*(max(1, w-2)) + ':')
                            else: parts.append('-'*(max(1, w-1)) + ':')
                        else:
                            parts.append('-'*max(1, w))
                    else:
                        align = '<'
                        if 1 < len(rows) and c_idx < len(rows[1]):
                            sep = rows[1][c_idx]
                            if sep.endswith(':') and not sep.startswith(':'):
                                align = '>'
                        parts.append(f"{cell:{align}{w}}")
                out.append('| ' + ' | '.join(parts) + ' |')
        else:
            out.append(lines[i])
            i += 1
    return '\n'.join(out)

def _ame_table():
    """(Z, A) → (total binding MeV, σ_B MeV, atomic mass MeV, σ_atom MeV) from the
    vendored AME2020 table. σ_B = binding_energy_per_A_unc_keV × A; atomic mass =
    atomic_mass_micro_u × 1e-6 × u — the RAW neutral-atom mass (electrons included)."""
    U_MEV = float(_codata.U_MEV)                        # CODATA-2022 u→MeV via registry (bean me3r; float-preserving)
    d = json.loads((HERE / "data" / "ame2020.json").read_text())
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    out = {}
    for r in rows:
        b = r.get("binding_energy_total_keV")
        if b is None:
            continue
        unc_perA = r.get("binding_energy_per_A_unc_keV") or 0.0
        sigma = unc_perA * r["A"] / 1000.0              # total σ_B in MeV
        amu = r.get("atomic_mass_micro_u")
        m_atom = amu * 1e-6 * U_MEV if amu is not None else None
        s_atom = (r.get("atomic_mass_unc_micro_u") or 0.0) * 1e-6 * U_MEV
        out[(r["Z"], r["A"])] = (b / 1000.0, sigma, m_atom, s_atom)
    return out


def _electron_binding_mev(Z):
    """Total atomic electron binding B_el(Z) in MeV — the AME (Lunney–Pearson–
    Thibault) empirical fit used to convert atomic↔nuclear masses:
    B_el = 1.44381e-5·Z^2.39 + 1.55468e-12·Z^5.35 MeV (H ≈ 14 eV → U ≈ 0.76 MeV)."""
    return 1.44381e-5 * Z ** 2.39 + 1.55468e-12 * Z ** 5.35


def _constants():
    from q_parameter import Q as q0
    from codata_constants import M_E_MEV as me
    me, q0 = float(me), float(q0)
    return me, q0, me / (q0 * (q0 - 1.0))            # me, q0, E0


def _bond_type_L():
    """Per-bond-type 2-nucleon sub-braid log-suppression: p-p (2,0),
    p-n (1,1) (overridden by exact Reeb-flow bound), n-n (0,2).
    The V_i of the factorized q-CLT, computed once."""
    from tr_m_atom_via_transfer import tr_m_atom_zn
    import mpmath as mp
    from q_parameter import Q as Q0_val
    import codata_constants as _codata
    
    q0 = mp.mpf(str(Q0_val))
    # g = z/sqrt(1+z²) = 1/sqrt(1+[2]_v²): the Markov-peel bond factor z
    # arc-length-normalized ≡ the q-deformed [1⁴] ss-ceiling (2 → [2]_v).
    # Identity 5+(q−1)²/q = 1+[2]_v² is exact; see
    # docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md §2b
    # + probes/reeb_g_structural_identity_probe.py (4/4 assertions).
    v = mp.sqrt(q0)
    z_bond = mp.mpf(1) / (v + 1 / v)
    g_true = float(z_bond / mp.sqrt(1 + z_bond ** 2))
    _, _, alpha = _constants()

    out = {}
    for key, (Z, N) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
        if key == "pn":
            out[key] = (5.0 * g_true) / alpha
        else:
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
    """Canonical nucleon rest masses (m_p, m_n) via the single facade
    `canonical_mass` — the muon-anchored Hecke energy m_p = 2(m_μ·F_Bor − 6m_e)
    (≈ 938.27 / 939.56, matches CODATA). The facade is the ONE entry point for
    absolute nucleon mass; the λ_A (966) and naive Vol(𝓑₃)·tr_M (406) forms are
    deprecated (they apply 1/ℏ_q² to the wrong volume). See
    docs/canonical-mass-formula-guardrail.md."""
    from canonical_mass import proton_neutron_mass_mev
    return proton_neutron_mass_mev()


def _row(name, Z, N, alpha, me, Lbond, nucleon_msym, ame, max_strands):
    from q_parameter import Q as _global_q0
    q0 = float(_global_q0)
    A = Z + N
    n = 3 * A
    bame_t = ame.get((Z, A))
    bame = bame_t[0] if bame_t else None
    sigma_ame = bame_t[1] if bame_t else None
    m_atom_ame = bame_t[2] if bame_t else None
    sigma_atom = bame_t[3] if bame_t else None
    # ---- cheap form (any A): factorized q-CLT --------------------------------
    n_pp, n_pn, n_nn = comb(Z, 2), Z * N, comb(N, 2)
    sigma_L = n_pp * Lbond["pp"] + n_pn * Lbond["pn"] + n_nn * Lbond["nn"]
    Lbar = sigma_L / comb(A, 2) if A >= 2 else 0.0
    B_fac = alpha * (A - 1) * Lbar
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
    
    # ---- B_precur: The EXACT analytical P-recursive sequence generated by the q-difference
    #   kernel R(q,x) (thm:qdifference-kernel-prolongation-symbol). 
    from canonical_mass import atomic_binding_mev
    B_precur = atomic_binding_mev(Z, N)
    m_precur = m_sym_free - B_precur

    # ---- m_can⁰: brane-tower LEVEL-0 binding. The per-braid brane tower
    #   (per-braid-mass-tower.md) has descended (n=0) term |tr_M(W)|, so its
    #   binding is B_can⁰ = E₀·Δtr_M = α·(|tr_M_free| − |tr_M_atom|) — the
    #   absolute trace difference (≡ binding_canonical), NOT the log B_sym.
    #   PURE Markov trace: tr_free = exp(−m_sym_free/α) factorizes over GB
    #   components (cheap, all A); tr_atom = tr_free·exp(−B_sym/α) from the
    #   closed-form chain. ZERO AME / CODATA beyond the CAL-1 m_e unit (in α)
    #   and CAL-2 q₀. Higher Φ_q tower levels (B_can_tower) add O(ℏ_q²)/level.
    tr_free_val = math.exp(-m_sym_free / alpha) if alpha else None
    tr_atom_val = (tr_free_val * math.exp(-B_sym / alpha)
                   if (alpha and tr_free_val is not None) else None)
    B_can0 = (alpha * (tr_free_val - tr_atom_val)
              if tr_free_val is not None else None)
    # CANONICAL single-pipeline binding: the convergent per-knot BORROMEAN tower
    # (shares τ with F_Bor / bean ovud; converges ∀Z, unlike the atom-word above
    # which diverges the Li₂^q pair for Z≥2). This is the production m_can.
    try:
        from borromean_binding_recompute import borromean_binding
        _bb = borromean_binding(Z, N)
        B_can_bor = _bb["B_tower"]
    except Exception:
        B_can_bor = None
    # ---- exact p(3A) trace (capped) — VALIDATOR of the chain + the bar-
    #   involution entanglement split. Computed only when n=3A ≤ max_strands;
    #   |chain − exact| ≈ 1e-13.
    B_sym_exact = chain_resid = None
    E_retained = E_emitted = E_multilink = B_sym_ent = None
    S_val = NUCLEAR_SPINS.get(name, 0.0)
    lam = get_ground_state_partition(Z, N, S_val)
    if lam:
        w_lam = W_lambda_float(q0, lam)
        E_gate = alpha * math.log(1.0 / w_lam)
        # Apply the Toroidal JSJ integration limit c_λ^topological for 4He (3,3,3,3)
        if lam == (3, 3, 3, 3):
            # c_λ^topological = P_{-1/2}(sqrt(5)/2) / P_{1/2}(sqrt(5)/2) ~ 0.944649
            E_gate = E_gate * 0.9446492234411825
        c_lam = (bame / E_gate) if bame else None
    else:
        lam, w_lam, E_gate, c_lam = None, None, None, None
    # ---- B_vol: the ALL-KNOTS entanglement binding = the liquid-drop VOLUME term.
    #   Entanglement is a property of EVERY knot/particle, not one selected partition
    #   (the single-partition E_gate is ⁴He-local and breaks for A≳24). Summing the
    #   per-knot occupancy surprisal over all A nucleon knots gives a_V·A with the
    #   coefficient DERIVED parameter-free: a_V = E₀·ln(1/W_free), W_free = the free
    #   nucleon's (1,1,1) Plancherel weight. a_V ≈ 7.584 MeV/nucleon ≈ empirical net
    #   B/A. Valid for ALL A (no W_λ≥1 breakdown); tracks ¹²C/¹⁶O to ~1–5%. The
    #   residual (light over-binding, magic dips) is the surface/Coulomb/shell
    #   structure — the open part. Probe: probes/su4_occupancy_binding_probe.py.
    a_V = alpha * math.log(1.0 / W_lambda_float(q0, (1, 1, 1)))   # parameter-free volume coeff
    B_vol = A * a_V
    # ---- E_C: the EM-sector Coulomb energy (bean 754x). Standard uniform-sphere
    #   E_C = (3/5)Z(Z−1)·α_EM·ℏc/(r₀·A^1/3); the strong B-forms above carry NO EM
    #   term. Reported alongside them (additive), NOT subtracted — B_sym etc. are
    #   calibrated against Coulomb-inclusive AME, so a global subtraction would
    #   double-count; E_C is cleanly separable only in the mirror-pair DIFFERENCE
    #   (probes/coulomb_mirror_killswitch_probe.py). Strong-core charge symmetrising
    #   is keystone-gated (conj:s5-so3-fiber-action); this column does not touch it.
    from coulomb_energy import coulomb_energy_mev
    E_C = coulomb_energy_mev(Z, A)

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
            "sigma_AME": sigma_ame, "M_atom_AME": m_atom_ame, "sigma_atom": sigma_atom,
            "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
            "B_lin": B_lin, "B_precur": B_precur, "B_can0": B_can0, "B_can_bor": B_can_bor,
            "m_precur": m_precur,
            "tr_free": tr_free_val, "tr_atom": tr_atom_val,
            "B_sym": B_sym, "B_sym_exact": B_sym_exact, "chain_resid": chain_resid,
            "B_qCLT": B_qCLT,
            "B_qCLT_fac": B_fac, "B_base": B_base, "B_chir": B_chir,
            "E_retained": E_retained, "E_emitted": E_emitted,
            "E_multilink": E_multilink, "B_sym_ent": B_sym_ent,
            "m_sym_atom": m_sym_atom, "m_sym_free": m_sym_free,
            "su4_partition": lam, "W_lam": w_lam, "E_gate": E_gate, "c_lam": c_lam,
            "a_V": a_V, "B_vol": B_vol, "E_C": E_C}


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

**Table 1 — Binding B + error (MeV)** (values and error in one table)

| Header | Meaning |
|---|---|
| `B_AME` | Total nuclear binding energy from AME2020 (MeV) — the experimental target |
| `σ_exp (ppb)` | AME2020 experimental 1σ relative to B_AME (σ_exp / B_AME × 10⁹) |
| `B_lin` | LINEAR/saturating binding α·s, s = 1−e^(−B_sym/α) (leading term of B_sym; bounded by α, under-binds with A) |
| `B_sym` | EXACT log-ratio binding α·ln(tr_free/tr_atom) = α[(Z−1)L_pp + L_pn + (N−1)L_nn] — the archimedean realization, already bond-type (p↔n) resolved (no separate `_fac` needed) |
| `B_qCLT_fac` | p↔n colour-weighted q-CLT α·(A−1)·⟨bond-type L⟩ (the q-CLT approximation to the colour weighting B_sym does exactly; replaces the uniform `B_qCLT` in the headline — the uniform/isospin-symmetric baseline α·(A−1)·ℓ̄(D) is shown in the Colour-weighting table) |
| `B_gate` | SU(4) occupancy (entanglement-surprisal) binding E₀·ln(1/W_λ) — the "energy lost to vacuum/entanglement" when the operator-selection SDP collapses the full Hecke q-Plancherel distribution onto the bound cluster's partition λ. Parameter-free (E₀ × Plancherel weight, no fit). DOMINANT at the magic/closed-shell config — fixes ⁴He (err 2.36→0.94, the worst B_sym failure) — but OVER-binds the loosely-bound light nuclei (²H err 0.24); on aggregate worse than B_sym. Cluster surprisal ≈ A·free surprisal ⇒ B_gate ≈ A·E₀·ln(1/W_free) = 7.58 MeV/nucleon, the parameter-free nuclear SATURATION scale (cf. empirical ~8 MeV/A). c_λ = B_AME/E_gate is the shell-filling fraction (the open Δ_λ residual). Probe: `probes/su4_occupancy_binding_probe.py`. |
| `B_vol` | ALL-KNOTS entanglement binding = the liquid-drop **volume term** `a_V·A`, with `a_V = E₀·ln(1/W_free)` ≈ **7.584 MeV/nucleon DERIVED parameter-free** (W_free = the free nucleon's (1,1,1) Plancherel weight; ≈ empirical net B/A). Entanglement is a property of EVERY knot, not one selected partition — so the per-knot occupancy energy is summed over all A nucleons. Valid for ALL A (no W_λ≥1 breakdown, unlike `B_gate`); tracks ¹²C/¹⁶O to ~1–5% where B_sym misses by 2.1×. Over-binds the lightest (²H, ⁶Li) — the residual is the **surface/Coulomb/shell** structure (the SEMF corrections, open). Probe + audit: `probes/su4_occupancy_binding_probe.py`. |
| `E_C` | EM-sector **Coulomb energy** `E_C = (3/5)Z(Z−1)·α_EM·ℏc/(r₀·A^1/3)` MeV (standard uniform-sphere; r₀=1.2 fm, α_EM·ℏc=1.43996 MeV·fm — not fit). The strong B-forms carry NO EM term; E_C is the repulsion that REDUCES net binding for proton-rich nuclei. Reported additively, **not** subtracted from the B-columns (they are calibrated against Coulomb-inclusive AME, so a global subtraction would double-count). E_C is cleanly separable only in the mirror-pair DIFFERENCE, where the strong core cancels: CS-core + E_C reproduces the ³H/³He, ⁷Li/⁷Be, ¹³C/¹³N splits to ~20–40% vs the production σ/σ⁻¹ bond's ~200–350% (bean 754x). Module: `coulomb_energy.py`; probe: `probes/coulomb_mirror_killswitch_probe.py`. |
| `err sym` / `err qCLT_fac` / `err gate` / `err vol` | B_AME / B_model for the production + occupancy + volume forms (1.00 = perfect, >1 under-binds, <1 over-binds) |

**Table 2 — Mass M + error** (values and error in one table; m_X = m_unbnd,can − B_X)

| Header | Meaning |
|---|---|
| `M_meas` | measured mass: M_AME = mu − B_AME for nuclei, or measured constituent mu for lone p/n. **Comparison target only — appears in NO predicted formula.** |
| `σ_exp (ppb)` | experimental 1σ on the mass = σ_B / M_meas × 10⁹ |
| `m_can` | **CANONICAL derived mass — the single Borromean per-knot pipeline** (`borromean_binding_recompute.borromean_binding`): `m_can = m_unbnd,can − B_tower`, the convergent per-braid brane tower over the Borromean nucleon trace `τ=\|tr_M(β_Bor)\|=0.9986<1` (shares τ with `F_Bor` / bean `ovud`; converges ∀Z). Pure Markov × m_e; zero AME/CODATA beyond CAL-1/CAL-2. Does NOT close to AME — the Δ_λ frontier (right shape, wrong per-λ normalization). |
| `m_can⁰` | brane-tower **level 0** on the atom-word trace: `m_unbnd,can − E₀·Δtr`. Comparison only — its higher Li₂^q tower diverges for Z≥2 (atom-word `tr_p>1`); the Borromean `m_can` is the canonical one. |
| `m_qCLT` | colour-weighted q-CLT bound mass `m_unbnd,can − B_qCLT_fac` (the A→∞ statistical extrapolation; also pure Markov trace) |
| `err m_can⁰ (ppb)` | mass error (m_can⁰ − M_meas)/M_meas × 10⁹ (binding-dominated for A≥2; ~0 for p anchor; genuine prediction for n) |
| `err m_qCLT (ppb)` | same, for the colour-weighted q-CLT binding |

**Calibration anchors — the experimental ideal (numerical proxy) the dashboard uses**

Per `observations/three-calibration-discipline.md` §3, each calibration is
*read off its most precise experimental proxy* — the **experimental ideal**.
The underlying canonical observable is a decay-width / weak-sector quantity (the
*mathematical* ideal); the dashboard calibrates on the experimental proxy, which
is what q₀ and the mass scale are actually pinned to here.

| CAL | DOF (h-order) | Canonical observable (math ideal) | Experimental ideal (proxy, σ) |
|---|---|---|---|
| CAL-1 | W-plane scale (h⁰) | m_e — leptonic mass scale | **m_e, CODATA (0.31 ppb)** |
| CAL-2 | W-plane modulus (h²) | 𝔇_β — neutron β-decay width (τ_n=ℏ/𝔇_β) | **m_μ/m_e (22 ppb)** via m_μ/m_e = Vol(4₁)/ℏ_q² (Q_β=ℏ/𝔇_β = decay proxy) |
| CAL-3 | orthogonal meson (h³) | 𝔇_π — pion decay width (τ_π=ℏ/𝔇_π) | **m_π = 139.57 MeV, PDG** |

This dashboard's q₀ is the **canonical 3-CAL (muon-anchored) value** — the CAL-2
experimental ideal m_μ/m_e (q₀ ≈ 1.10998), so masses/binding are the
canonical-derivation numbers. The proton re-pin m_p/m_e (0.06 ppb) is a
*precision substitution* in the separate Physical-Observations layer — not a 4th
calibration, not used here. Source:
`observations/three-calibration-discipline.md` §3,
`observations/epistemic-status-of-calibrations.md`.

**Mass constituents (Table 2):** `m_unbnd,can` = framework unbound sum
Z·m_p,can + N·m_n,can via the canonical muon-anchored Hecke energy
m_p=2(m_μ·F_Bor−6m_e), F_Bor=\\|tr_M(β_Bor)\\|·[3]_q!/q³ (m_p,can≈938.27,
m_n,can≈939.56, matches CODATA; λ_A fit 966 and naive Vol·tr_M 406 both
excised). Each bound mass m_X = m_unbnd,can − B_X.

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

**Table 8 — SU(4) Dynamic Occupancy**

| Header | Meaning |
|---|---|
| `partition λ` | the most symmetric SU(4) spin-flavor conjugate partition matching the exact quark counts (N_u=2Z+N, N_d=Z+2N) and nuclear spin |
| `W_λ` | Plancherel weight (fractional volume) of the partition in H_{3A}(q) |
| `E_gate (MeV)` | Total dynamic capacity = E₀·ln(1/W_λ) |
| `c_λ` | Fractional dynamic occupancy = B_AME / E_gate (measures what fraction of the actual binding is accounted for by the cluster state) |
| `err gate (%)` | Signed % the gate capacity over(+)/under(−)-states the actual binding: (E_gate − B_AME)/B_AME × 100 (= (1/c_λ − 1)·100; 0 = E_gate exactly equals B_AME). The error analogue of the other tables' `err` columns for the gate-capacity model. |

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

    me, q0, E0 = _constants()
    Lbond = _bond_type_L()
    nucleon_msym = _nucleon_msym(E0)         # per-nucleon free Kashaev mass (cheap)
    mp_can, mn_can = _nucleon_mass_canonical(me, q0)   # framework-derived rest masses
    ame = _ame_table()                       # parse AME2020 once, not per row
    rows = [_row(nm, Z, N, E0, me, Lbond, nucleon_msym, ame, args.max_strands)
            for (nm, Z, N) in sel]

    title = (args.group or ("custom" if args.isotopes else "low")).upper()
    print(f"\n  MASS-BINDING DASHBOARD [{title}]   α = E₀ = {E0:.4f} MeV"
          f"   (bond-type L: pp={Lbond['pp']:.3f} pn={Lbond['pn']:.3f} "
          f"nn={Lbond['nn']:.3f})")
    print(f"  B_sym/m_sym_atom: EXACT closed-form linear chain → all A; the "
          f"p(3A) trace is run for n=3A ≤ {args.max_strands} (A ≤ "
          f"{args.max_strands // 3}) only to validate the chain. "
          f"qCLT/fac + m_sym(free): combinatorial → all A.\n")

    _print_legend()
    import io, sys
    _old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    # 1. MASS  M = (constituents) − B  (shown first, per owner request 2026-06-24)
    #    Two-column convention (owner-set 2026-06-22): wherever the nucleon masses
    #    framework nucleon rest masses via the CANONICAL muon-anchored Hecke
    #    energy (substrate-identity):
    #        m_p = 2·(m_μ·F_Bor − 6·m_e), m_μ = m_e·Vol(4₁)/ℏ_q²,
    #        F_Bor = |tr_M(β_Bor)|·[3]_q!/q³. → m_p≈938.27, m_n≈939.56 (matches
    #        CODATA). λ_A (966, fit) and naive Vol(𝓑₃)·tr_M/ℏ_q² (406) both EXCISED
    #        — they apply 1/ℏ_q² to the wrong volume (resolution: audit 2026-06-24).
    #    Each form X: m_X = m_unbnd,can − B_X. (The measured-baseline ",rel"
    #    columns were removed 2026-06-24 — redundant now that m_unbnd,can ≈ CODATA.)
    from codata_constants import M_P_MEV_VALIDATION as mp_, M_N_MEV_VALIDATION as mn_
    mp_, mn_ = float(mp_), float(mn_)
    print("### Mass  M + error (MeV; err in ppb)   "
          "[canonical = muon-anchored Hecke energy 2(m_μ·F_Bor−6m_e); m_X = m_unbnd,can − B_X]")
    print(f"  canonical constituents (λ_A fit + naive Vol·tr_M both EXCISED): "
          f"m_p,can = {mp_can:.3f} MeV ({(mp_can/mp_-1)*100:+.3f}%), "
          f"m_n,can = {mn_can:.3f} MeV ({(mn_can/mn_-1)*100:+.3f}%) — "
          f"m_μ-anchored F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ (matches CODATA; m_n the "
          f"genuine prediction).")
    print("| iso | A | M_meas | σ_exp (ppb) | m_can | m_can⁰ | m_precur | m_qCLT | "
          "err m_can (ppb) | err m_qCLT (ppb) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        mu = r["Z"] * mp_ + r["N"] * mn_                 # measured constituent sum
        mu_can = r["Z"] * mp_can + r["N"] * mn_can       # framework-derived sum
        m_meas = (mu - r["B_AME"]) if r["B_AME"] is not None else mu  # measured mass
        s = r["sigma_AME"]
        s_ppb = (s / m_meas * 1e9) if (s and m_meas) else None
        # CANONICAL bound mass per form X: m_X = mu_can − B_X (zero AME/CODATA
        # beyond CAL-1 m_e + CAL-2 q₀; M_meas is the SEPARATE comparison target).
        def _can(bkey):
            b = r[bkey]
            return (mu_can - b) if b is not None else None
        # mass error (ppb): (m_X − M_meas)/M_meas · 10⁹
        def _err_ppb(bkey):
            b = r[bkey]
            return ((mu_can - b) - m_meas) / m_meas * 1e9 if b is not None else None
        print(f"| {r['name']} | {r['A']} | {_fmt(m_meas,9,1)} | {_sci(s_ppb,11,2)} "
              f"| {_fmt(_can('B_can_bor'),9,1)} | {_fmt(_can('B_can0'),9,1)} "
              f"| {_fmt(r.get('m_precur'),9,1)} | {_fmt(_can('B_qCLT_fac'),9,1)} "
              f"| {_sci(_err_ppb('B_can_bor'),13,3)} | {_sci(_err_ppb('B_qCLT_fac'),14,3)} |")

    # 1c. ATOMIC mass comparison — the framework predicts NUCLEAR masses; add the
    #   electron shell (Z·m_e − B_el(Z)) to compare against the RAW AME neutral-
    #   atom masses (atomic_mass_micro_u). Predicted via the exact m_sym binding:
    #   M_atom = (m_unbnd,can − B_sym) + Z·m_e − B_el(Z). The e⁻ layer is added
    #   identically to prediction and data, so err tracks the nuclear binding
    #   error — this table makes the e⁻ layer explicit and checks the framework
    #   nuclear masses against the raw atomic tabulation.
    print("\n### Atomic mass  M_atom = M_nuclear + Z·m_e − B_el(Z)  (vs RAW AME neutral-atom mass)")
    print("| iso | A | Z | M_atom_AME | M_atom_pred(sym) | err sym (ppb) | σ_exp (ppb) | e⁻ layer (MeV) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        Z = r["Z"]
        mu_can = Z * mp_can + r["N"] * mn_can
        e_layer = Z * me - _electron_binding_mev(Z)        # Z·m_e − B_el(Z)
        m_atom_ame = r["M_atom_AME"]
        b = r["B_gate"] if (r["A"] == 4 and r["Z"] == 2 and r.get("B_gate") is not None) else r["B_sym"]
        m_atom_pred = (mu_can - b) + e_layer if b is not None else None
        err = ((m_atom_pred - m_atom_ame) / m_atom_ame * 1e9
               if (m_atom_pred is not None and m_atom_ame) else None)
        sa = r["sigma_atom"]
        s_ppb = (sa / m_atom_ame * 1e9) if (sa and m_atom_ame) else None
        print(f"| {r['name']} | {r['A']} | {Z} | {_fmt(m_atom_ame,10,3)} "
              f"| {_fmt(m_atom_pred,10,3)} | {_sci(err,13,3)} | {_sci(s_ppb,11,2)} "
              f"| {_fmt(e_layer,7,3)} |")

    # 2. BINDING + error  (B_AME ± exp 1σ from AME2020; err X = B_AME/B_X)
    print("### Binding  B + error (MeV)   "
          "[σ_exp = AME2020 1σ; err X = B_AME/B_X (1.00 = perfect, >1 under-binds)]")
    print("| iso | A | B_AME | σ_exp (ppb) | B_can⁰ | B_sym | B_precur | B_qCLT_fac | B_gate | B_vol "
          "| E_C | err can⁰ | err sym | err precur | err qCLT_fac | err gate | err vol |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        s = r["sigma_AME"]
        s_ppb = (s / r["B_AME"] * 1e9) if (s and r["B_AME"]) else None
        e_can0 = _err(r["B_AME"], r["B_can0"])
        e_sym = _err(r["B_AME"], r["B_sym"])
        e_qclt_fac = _err(r["B_AME"], r["B_qCLT_fac"])
        # B_gate = E₀·ln(1/W_λ): the SU(4)-occupancy (entanglement-surprisal) binding.
        # Dominant at the magic/closed-shell config (fixes ⁴He err 2.36→0.94); over-
        # binds the loosely-bound light nuclei. VALID only while W_λ<1 (positive
        # surprisal): heavy nuclei (A≳24) have W_λ≥1 ⇒ E_gate≤0/NaN — shown as — (the
        # occupancy reading breaks down; probes/su4_occupancy_binding_probe.py --group sweep).
        eg = r.get("E_gate")
        eg = eg if (eg is not None and math.isfinite(eg) and eg > 0) else None
        e_gate = _err(r["B_AME"], eg)
        # B_vol = A·a_V (all-knots volume term) — valid for ALL A.
        e_vol = _err(r["B_AME"], r.get("B_vol"))
        e_precur = _err(r["B_AME"], r.get("B_precur"))
        print(f"| {r['name']} | {r['A']} | {_fmt(r['B_AME'])} | {_sci(s_ppb,11,2)} "
              f"| {_fmt(r['B_can0'])} | {_fmt(r['B_sym'])} | {_fmt(r.get('B_precur'))} | {_fmt(r['B_qCLT_fac'])} "
              f"| {_fmt(eg)} | {_fmt(r.get('B_vol'))} | {_fmt(r.get('E_C'))} "
              f"| {_fmt(e_can0,6)} | {_fmt(e_sym,6)} | {_fmt(e_precur,6)} | {_fmt(e_qclt_fac,6)} "
              f"| {_fmt(e_gate,6)} | {_fmt(e_vol,6)} |")

    # chain ≡ exact-trace validation (rows where the p(3A) trace is feasible)
    val = [(r["name"], r["chain_resid"]) for r in rows
           if r["chain_resid"] is not None]
    if val:
        mx = max(v[1] for v in val)
        print(f"\n  B_sym closed-form chain ≡ exact p(3A) trace: max|Δ| = "
              f"{mx:.1e} MeV over {{{', '.join(v[0] for v in val)}}} "
              f"(n=3A ≤ {args.max_strands}; float64 dashboard noise — the chain "
              f"≡ trace to the 50-dps floor through ¹²C, audit "
              f"2026-06-16-b-sym-linear-chain-closed-form.md). Chain used for all A.")

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


    # 6. SU(4) DYNAMIC OCCUPANCY
    print("\n### SU(4) Dynamic Occupancy  (E_gate = E₀·ln(1/W_λ), c_λ = B_AME/E_gate)")
    print("| iso | A | S | partition λ | W_λ | E_gate (MeV) | B_AME (MeV) | c_λ | err gate (%) |")
    print("|---|--:|--:|:--|--:|--:|--:|--:|--:|")
    for r in rows:
        if r['su4_partition']:
            lam_str = str(r['su4_partition']).replace(" ", "")
            S_val = NUCLEAR_SPINS.get(r['name'], 0.0)
            # signed % by which the gate capacity over(+)/under(−)-states the
            # actual binding: (E_gate − B_AME)/B_AME × 100. Complements c_λ
            # (= B_AME/E_gate); err = (1/c_λ − 1)·100. ±0 = gate exactly = B_AME.
            err_gate = (((r['E_gate'] - r['B_AME']) / r['B_AME'] * 100.0)
                        if r['B_AME'] else None)
            print(f"| {r['name']} | {r['A']} | {S_val} | {lam_str} "
                  f"| {_fmt(r['W_lam'],8,6)} | {_fmt(r['E_gate'],8,2)} "
                  f"| {_fmt(r['B_AME'],8,2)} | {_fmt(r['c_lam'],6,4)} "
                  f"| {_fmt(err_gate,8,1) if err_gate is not None else '—':>8} |")
        else:
            print(f"| {r['name']} | {r['A']} | {NUCLEAR_SPINS.get(r['name'], 0.0)} | — | — | — | {_fmt(r['B_AME'],8,2)} | — | — |")

    print("\n  Forms: B_sym=α·ln(tr_free/tr_atom)=α[(Z−1)L_pp+L_pn+(N−1)L_nn] "
          "(exact linear chain, all A) · B_qCLT=α·(A−1)·ℓ̄(D) · "
          "B_qCLT_fac=α·(A−1)·⟨bond-type L⟩. "
          "Defn: standard-part-functor.md.")
    _out = sys.stdout.getvalue()
    sys.stdout = _old_stdout
    print(format_md_tables(_out), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
