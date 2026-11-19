#!/usr/bin/env python3
"""Mass-binding dashboard — B_AME vs the standard-part binding forms + masses.

Powers the `/dashboard-low` and `/dashboard-sweep` commands. Every binding form
is evaluated from the ONE canonical Jones–Markov transfer trace (`tr_m_atom_zn`,
the fine-Bratteli path); B_AME comes from the vendored AME2020 table
(`data/ame2020.json`). This is the multi-isotope view of the single-pipeline
probe `binding_single_pipeline_comparison.py` (PR #2320); see the appendix
`algebraic-quantum-volume.md` (Vol_alg := tr_M) for the naming. NOT
`standard-part-functor.md` -- corrected 2026-08-25, that block defines the
standard-part map st: No_fin -> R and the functor St, and contains no B_ form,
no alpha and no binding.

WHAT LICENSES THE LOG, AND WHAT DOES NOT (corrected 2026-08-26, bean qou-mkm8).
This docstring, and the B_sym provenance row, cited `vol-through-tau.md` and
tagged the log-forms KVC-conditional. I put that citation here myself in
933053614f, and it is wrong twice over -- so the retraction it announced is
itself retracted. Three neighbouring objects have three different licences:

  (1) The LOG'S EXTENSIVITY is DERIVED and needs no conjecture at all. The
      interface subalgebra is 2-dimensional (sigma^2 = h*sigma + 1 gives
      span{1, sigma_2}), so tr_atom = tr_free * prod_bonds (z + d_XY) by the
      Markov property tr_M(W . sigma_2) = z * tr_M(W). A product over bonds has
      an additive logarithm. That is the whole reason a log appears, and it is
      elementary. See `_bond_type_L`.

  (2) E_0 x (trace DIFFERENCE) is licensed -- as a CONJECTURE, not a
      proposition -- by `knot-factor-frobenius-pairing.md`:
      B_bulk = E_0 (|tr_M(W_free)| - |tr_M(W_atom)|). That is the B_can0 column,
      and the code comment there already said "NOT the log B_sym".

  (3) ln|tr_M| = Vol is `vol-through-tau.md`, KVC-conditional -- and it does not
      reach this object. Its quantifier is "for every BRAID beta in B_n", while
      atom_braid_word_3A's letters are c*sigma_g + d*1, general Hecke elements
      that are not braid generators. I corrected that quantifier myself in
      1c83073b3c, 47 minutes AFTER 933053614f, and did not go back to check what
      it invalidated. Reading past the quantifier does not help either: 0 of 40
      branch closures of the atom element are hyperbolic (c64833a979, both
      controls green), so Vol = 0 while B_sym(2H) = 3.8897 MeV.

So B_sym has (1)'s extensivity and (2)'s prefactor, and NO block asserts the
combination. It is POSITED, not DERIVED*: the KVC tag was over-hedging in form
(attaching an irrelevant open conjecture) while under-stating in substance
(concealing that nothing licenses the energy identification at all).

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
import sys

from decimal import Decimal
from fractions import Fraction
import mpmath as mp
from pathlib import Path


def comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(k):
        num *= n - i
        den *= i + 1
    return num // den

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import codata_constants as _codata  # noqa: E402 — registry (CODATA-2022 u→MeV); bean me3r
from hecke_core import E_HARTREE_EV as _E_HARTREE_EV_DERIVED  # noqa: E402 — mp-backed downcast (qou-ozvb)

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
    "p": Fraction(1, 2), "n": Fraction(1, 2), "2H": Fraction(1), "3H": Fraction(1, 2),
    "3He": Fraction(1, 2), "4He": Fraction(0), "6Li": Fraction(1), "7Li": Fraction(3, 2),
    "9Be": Fraction(3, 2), "12C": Fraction(0), "16O": Fraction(0),
    "24Mg": Fraction(0), "40Ca": Fraction(0), "56Fe": Fraction(0),
    "197Au": Fraction(3, 2), "238U": Fraction(0),
}




def q_int_float(q, n):
    with mp.workdps(max(mp.mp.dps, 60)):
        qx = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
        return (qx**n - qx**(-n)) / (qx - 1 / qx)

def q_fact_float(q, n):
    with mp.workdps(max(mp.mp.dps, 60)):
        qx = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
        res = mp.mpf(1)
        for i in range(1, n + 1):
            res *= q_int_float(qx, i)
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

# ── DEPRECATED 2026-08-08: B_gate / B_vol / E_gate / c_λ ─────────────────────
#
# Deprecated: they have no basis in the derivation chain. NOTE (2026-08-22):
# they were NEVER actually removed from the code below — the columns are still
# computed and printed. Until that cleanup lands they are RETAINED FOR THE RECORD
# but flagged NON-DERIVED in the legend (see the B_vol / B_gate rows). Do not read
# them as derived. Red-team: docs/audits/2026-08-22-avol-binding-redteam.md.
#
# The chain is
#     q0 -> categorical action -> Yekutieli non-abelian Stokes -> H_n(q)
#        -> Wedderburn (lambda |- n) -> Frobenius pairing tr_M = SUM_lambda y_lambda chi_lambda
#        -> confinement SDP -> canonical T_w -> Archimedean functor -> MeV
#
# and its terminal object at that stage is tr_M. Everything downstream must be
# a function of tr_M. `B_sym = alpha*ln(tr_free/tr_atom)` is; `B_gate =
# alpha*ln(1/W_lambda)` is NOT. It takes ONE partition's Plancherel weight --
# no character, no sum -- and never touches the braid word at all, so it
# cannot distinguish two nuclei with the same (Z,N,S) and different topology.
# It is a Wedderburn-layer side-channel around the pairing. `B_vol = A*a_V`
# with `a_V = E0*ln(1/W_free)` is the same construct with one partition fixed.
#
# Measured on the way out, and worth keeping in the record:
#
#   * SUM_lambda W_lambda is NOT 1 at q0 -- it is 1.517 at n=12 and 26.28 at
#     n=21. So -ln W_lambda was never a surprisal; the construct treated an
#     unnormalised weight as a probability. The repo already knew:
#     `normalized_plancherel_weights_3A` exists and its docstring says the
#     naive weights "do NOT sum to 1" at q > 1.
#   * Normalising would have moved err gate at 7Li from 1.46 to 0.97 and at
#     6Li from 1.09 to 0.85 -- i.e. most of the heavy-end drift WAS the missing
#     normalisation. Recorded because it is evidence about the construct, not
#     a reason to keep it: fixing the normalisation would not make it licensed.
#   * B_gate and B_vol both reported 7.58 MeV of BINDING for a free nucleon,
#     where B_AME = 0 by definition, making `err gate` read 0.00 as though it
#     were a perfect score.
#
# The SU(4) ground-state partition itself is fine -- it is a genuine lambda |- 3A
# (4 parts, the spin-isospin classes) and a legitimate Wedderburn label. The
# defect is using its weight INSTEAD of the pairing, not the label.


def W_lambda_float(q, lam):
    from canonical_mass import _as_formattable_mpf
    with mp.workdps(max(mp.mp.dps, 60)):
        qx = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
        n = sum(lam)
        hooks = hook_lengths(lam)
        prod_hooks_sq = mp.mpf(1)
        for h in hooks:
            prod_hooks_sq *= (q_int_float(qx, h))**2
        return _as_formattable_mpf(q_fact_float(qx, n) / prod_hooks_sq)

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
    atomic_mass_micro_u × 10^-6 × u — the RAW neutral-atom mass (electrons included)."""
    from canonical_mass import _as_formattable_mpf
    with mp.workdps(max(mp.mp.dps, 60)):
        u_mev = mp.mpf(str(_codata.U_MEV))
        thousand = mp.mpf(1000)
        micro = mp.mpf("1e-6")
        d = json.loads((HERE / "data" / "ame2020.json").read_text())
        entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
        rows = entries.values() if isinstance(entries, dict) else entries
        out = {}
        for r in rows:
            b = r.get("binding_energy_total_keV")
            if b is None:
                continue
            b_mp = mp.mpf(str(b))
            unc_raw = r.get("binding_energy_per_A_unc_keV")
            unc_perA = mp.mpf(str(unc_raw)) if unc_raw is not None else mp.mpf(0)
            sigma = _as_formattable_mpf(unc_perA * r["A"] / thousand)
            amu = r.get("atomic_mass_micro_u")
            m_atom = (
                _as_formattable_mpf(mp.mpf(str(amu)) * micro * u_mev)
                if amu is not None
                else None
            )
            s_raw = r.get("atomic_mass_unc_micro_u")
            s_unc = mp.mpf(str(s_raw)) if s_raw is not None else mp.mpf(0)
            s_atom = _as_formattable_mpf(s_unc * micro * u_mev)
            out[(r["Z"], r["A"])] = (
                _as_formattable_mpf(b_mp / thousand),
                sigma,
                m_atom,
                s_atom,
            )
        return out


def _electron_binding_mev(Z):
    """Total atomic electron binding B_el(Z) in MeV — DERIVED (owner-ordered
    swap 2026-08-30, bean qou-g3x3): bare-Z hydrogenic shell sum at the
    canonical e-Hartree scale, Ry = E_h/2, E_h = α_EM²·m_e c² with the
    CS-corrected mp α_EM and CODATA m_e (pyhecke float64 excised, bean
    qou-ozvb). Replaces the AME Lunney-Pearson-Thibault empirical fit
    (kept as _electron_binding_mev_ame_fit for comparison). Bare-Z carries
    no inter-electron screening: exact for H (13.606 eV), over-binds He/Li
    at the eV scale and Fe by ~18 keV — all far below the MeV-scale nuclear
    residuals this table reports. mp-exact version + witness:
    computations/atom_electron_mass.py / atom-electron-mass.witness.json."""
    from canonical_mass import _as_formattable_mpf
    with mp.workdps(max(mp.mp.dps, 60)):
        ry_mev = mp.mpf(str(_E_HARTREE_EV_DERIVED)) / mp.mpf(2) / mp.mpf(1000000)
        total, n, left = mp.mpf(0), 1, Z
        while left > 0:
            k = min(2 * n * n, left)
            total += mp.mpf(k * (Z * Z)) * ry_mev / mp.mpf(n * n)
            left -= k
            n += 1
        return _as_formattable_mpf(total)


def _electron_binding_mev_ame_fit(Z):
    """AME (Lunney-Pearson-Thibault) empirical fit — COMPARISON ONLY since
    the 2026-08-30 derived swap: 1.44381e-5·Z^2.39 + 1.55468e-12·Z^5.35 MeV."""
    from canonical_mass import _as_formattable_mpf
    with mp.workdps(max(mp.mp.dps, 60)):
        z_mp = mp.mpf(Z)
        val = (
            mp.mpf("1.44381e-5") * (z_mp ** mp.mpf("2.39"))
            + mp.mpf("1.55468e-12") * (z_mp ** mp.mpf("5.35"))
        )
        return _as_formattable_mpf(val)


def _constants():
    # NO FLOAT64 (owner directive): source the 50-dps q0 and form E0 exactly.
    # `q_parameter.Q` is the f64 value; doing `me / (q0 * (q0 - 1))` in f64
    # threw away digits E0 is entitled to.
    #
    # The `float()` casts that used to sit on the return are GONE (bean
    # `qou-4ohh`). Their comment said "cast ONCE at the boundary", but the
    # boundary moved: `_disp` is the display boundary now, and its docstring
    # states the invariant this function was violating — "every computed
    # quantity stays mpf upstream and nothing that reaches a witness passes
    # through this function". Casting here formed E0 at 60 dps and then threw
    # 43 of those digits away before a single consumer saw it, which is the
    # f64 collapse `_bond_type_L`'s docstring already names as forbidden.
    import mpmath as _mp
    from q_parameter import Q_50_DIGIT_STR as _Q50
    from codata_constants import M_E_MEV as me
    with _mp.workdps(60):
        q0x = _mp.mpf(str(_Q50))
        mex = _mp.mpf(str(me))
        e0x = mex / (q0x * (q0x - 1))
    from canonical_mass import _as_formattable_mpf
    return _as_formattable_mpf(mex), _as_formattable_mpf(q0x), _as_formattable_mpf(e0x)  # me, q0, E0 — all mpf


def _bond_type_L():
    """Per-bond-type 2-nucleon sub-braid log-suppression, ALL THREE from the
    trace: p-p (2,0), p-n (1,1), n-n (0,2). The V_i of the factorized q-CLT.

    THE REEB OVERRIDE IS GONE (2026-08-08). `pn` used to be replaced by
    `5*g_reeb/alpha` with `g_reeb = 1/sqrt(5 + (q0-1)^2/q0)`, while pp and nn
    came from `ln(tr_free/tr_atom)`. Three bond constants, two derivations.

    It was removed because the linear law B = 5g is not derivable in this
    framework, not merely unproven. `g` depends only on q0, which is a mass
    RATIO and therefore dimensionless, so `5g = 2.2336` is a PURE NUMBER
    declared to be MeV. It does not scale with m_e:

        alpha = m_e/(q0(q0-1))  ->  4.185981 MeV == 4185.981 keV   consistent
        5g                      ->  2.2336 "MeV" != 2.2336 "keV"   off by 1000x

    Every energy here is alpha x dimensionless and alpha carries the CAL-1 unit
    m_e; a quantity with no m_e in it cannot be an energy. Its +0.41% agreement
    with AME was a coincidence in MeV specifically. The 2026-07-06 provenance
    audit already graded the linear law ASSERTED and "dimensionally implicit";
    this is the stronger statement that no derivation can exist for it as
    written.

    It also made the chain sum incoherent term-by-term: L_pn carried m_e (via
    the 1/alpha) while L_pp and L_nn were pure q0 functions, so alpha cancelled
    for one term of `alpha[(Z-1)L_pp + L_pn + (N-1)L_nn]` and not the others.

    WHAT THIS COSTS, stated plainly. The override was what made the deuteron
    come out exact:

        B_AME(2H)                      2.2246 MeV
        with the Reeb override         2.2336 MeV   err 0.996
        with the trace (now)           3.8897 MeV   err 0.572

    So the flagship "err sym = 1.00" was a property of the override, not of the
    Frobenius pairing. Removing it makes the deuteron over-bind by 1.75x, which
    is the theory's actual state. What is gained is that B_sym is now genuinely
    `alpha*ln(tr_free/tr_atom)` -- the docstring's claim that the chain closed
    form reproduces the exact p(3A) trace to ~1e-13 becomes TRUE, where it was
    off by a constant 1.6561 MeV for every isotope.

    Bean qou-xzda.

    CLOSED FORM (2026-08-08, bean qou-c6gx). These no longer need the transfer.
    sigma_2 -- the sole generator joining strand 2 (nucleon k's last quark) to
    strand 3 (nucleon k+1's first) -- generates a TWO-dimensional subalgebra,
    since sigma^2 = h*sigma + 1 gives span{1, sigma_2}. So every interface
    element is a*sigma_2 + b*I, and with the Markov property
    tr_M(W . sigma_2) = z * tr_M(W),

        tr_atom = tr_free * (a*z + b)        L = -ln(a*z + b)

    Each bond type is the a = 1 case at its own d, so

        L_XY = -ln(z + d_XY),   z = q0^3/(q0^2 + 1)      [convention D]

    Agrees with the transfer kernel to 4.489e-32 at all three bond types (that
    residual is the shared tr_free floor, not a per-case error). Two things are
    gained besides speed: the values are now mpmath end to end -- the old body
    did `math.log(float(tf)/float(ta))`, an f64 collapse the owner directive
    forbids -- and L_pp is exhibited as ln(1/z) EXACTLY, a derived constant of
    the framework with no freedom in it at all.

    WHAT THE CLOSED FORM ALSO EXPOSES, and it REVERSED under D. B over the
    ENTIRE admissible interface family (d from 0 at sigma to -h at sigma^-1),
    for a single bond, with E0 = 4.1859813632944758969 MeV:

        convention C (excised)   [2.907195188, 5.177967207] MeV
        convention D (production)[2.050709692, 3.797782935] MeV

    Under C, AME(2H) = 2.2245662 sat BELOW the whole band -- the minimum was
    30.69 % above it -- so no crossing sign, colour weight, or crossing
    multiplicity could reach the deuteron and the miss was not localisable in
    the interface. Under D the band CONTAINS AME(2H) (8.48 % above the
    minimum, at d = -0.1192*h). The 2H impossibility argument that this
    paragraph used to make DOES NOT SURVIVE the convention change; the
    registry records the same reversal under the `binding` channel's
    resolution. The stacking remark (m = 2 gives mu = 1.1044, B = -0.416 MeV)
    was also computed under C and has not been recomputed.

    Prose corrected 2026-08-09, bean qou-wgta item 13; the `zx` below had
    already been switched to D and this docstring had not.
    """
    import mpmath as _mp
    from q_parameter import Q_50_DIGIT_STR as _Q50
    from _li_2_q_util import flavor_split_leading

    # Built inside one guard: an mpf carries the precision of the OPERATION,
    # so forming these at the caller's ambient dps would silently re-cap them.
    with _mp.workdps(max(_mp.mp.dps, 60)):
        q0x = _mp.mpf(str(_Q50))
        hx = q0x - 1 / q0x
        # CONVENTION D (fixed 2026-08-09). This read
        # `zx = 1/(sqrt(q0)+1/sqrt(q0))` = 0.4993203 -- convention **C**, the
        # full-Hecke Ocneanu z. C was excised (73311b57, 33a6c7aa) but the
        # excision swept `wedderburn_jones_markov.y_lambda_at` and
        # `closed_form_tau_M.markov_z` and MISSED this inline literal, so the
        # binding dashboard was still reporting C bond energies afterwards.
        # D is z = q^3/(q^2+1) = 0.6126880.
        zx = q0x ** 3 / (q0x ** 2 + 1)
        dx = flavor_split_leading(q0x)
        d = {"pp": _mp.mpf(0),                                  # sigma
             "pn": -hx * (_mp.mpf(1) / 2 - dx / 4),             # colour-weighted
             "nn": -hx}                                         # sigma^-1
        # WRITHE NORMALISATION (owner directive 2026-08-09: "want all derived
        # bits in there even if negligible"). Lean-proved SORRY-FREE in
        # QOU/QBeta/WritheNormalisation.lean: Markov invariance forces
        # S_hat = S * A^(e-n) with A^2 = 1-h, i.e. the factor (1-h)^((e-n)/2),
        # unique up to sign (`writhe_factor_sq`,
        # `writhe_factor_unique_up_to_sign`) -- no freedom to tune.
        #
        # On the free/atom RATIO the strand count cancels (both n=6), so only
        # the exponent-sum difference survives:
        #     L_XY  ->  L_XY - (delta_e/2)*ln(1-h)
        # with delta_e = +1 for sigma (pp), -1 for sigma^-1 (nn), and
        # 2t-1 ~ -6.9e-4 for the p-n colour superposition at t ~ 0.4997.
        #
        # Bean qou-c6gx recorded this as "REAL but negligible ... 3.2e-4 MeV".
        # That was the 2H (p-n) case ONLY, where delta_e ~ 0. For a PURE
        # crossing delta_e = +/-1 and the shift is alpha*|ln(1-h)|/2 = 0.4909
        # MeV -- NOT negligible, and equal-and-opposite on pp vs nn.
        de = {"pp": _mp.mpf(1), "nn": _mp.mpf(-1),
              "pn": 2 * (_mp.mpf(1) / 2 - dx / 4) - 1}
        lw = _mp.log(1 - hx)
        # mpf, NOT float (bean `qou-4ohh`). The docstring above says "the values
        # are now mpmath end to end"; until this `float()` was removed that was
        # true of the BODY and false of the RETURN, so every consumer of these
        # bond constants — B_sym, and through it the chain-vs-exact residual
        # this module reports — was back at f64 one line later. The docstring
        # and the internals agreed with each other and both were wrong about
        # what came out.
        from canonical_mass import _as_formattable_mpf
        return {k: _as_formattable_mpf(-_mp.log(zx + v) - de[k] / 2 * lw) for k, v in d.items()}


def _chain_writhe_shift(Z, N, alpha):
    """Total writhe normalisation carried by the closed-form chain for (Z, N).

    `_bond_type_L` returns writhe-NORMALISED per-bond suppressions
    `L_XY - (delta_e/2)*ln(1-h)`; `tr_m_atom_zn` returns the UN-normalised trace.
    This is the difference between them, summed over the chain's bonds, so that
    the two can be compared on the same footing:

        shift = -alpha * ln(1-h)/2 * [ (Z-1)*de_pp + de_pn + (N-1)*de_nn ]

    with `de_pp = +1`, `de_nn = -1`, and `de_pn = 2t-1 ~ -6.9e-4` for the p-n
    colour superposition. The pp and nn terms cancel whenever `#pp = #nn`, i.e.
    on the `N = Z` line; off it the shift is ~0.4909 MeV per unit of `d = N-Z`.

    Returns the SIGNED amount to ADD to the un-normalised exact trace to make it
    commensurable with the normalised chain (the sign is already carried by
    `n_de`, so the caller adds it rather than choosing a direction). Sign
    convention checked against 3H/3He, where it must cancel a residual of
    -0.491214/+0.490539 exactly; getting it backwards DOUBLES the residual
    instead of clearing it, which is the diagnostic to watch for.

    Derived, not fitted -- every factor
    comes from `WritheNormalisation.lean` (`writhe_factor_sq`,
    `writhe_factor_unique_up_to_sign`), which fixes it up to sign with no freedom.
    """
    import mpmath as _mp
    from q_parameter import Q_50_DIGIT_STR as _Q50
    from _li_2_q_util import flavor_split_leading
    with _mp.workdps(max(_mp.mp.dps, 60)):
        q0x = _mp.mpf(str(_Q50))
        hx = q0x - 1 / q0x
        dx = flavor_split_leading(q0x)
        de_pn = 2 * (_mp.mpf(1) / 2 - dx / 4) - 1
        n_de = (max(Z - 1, 0) * _mp.mpf(1)
                + (de_pn if (Z >= 1 and N >= 1) else _mp.mpf(0))
                + max(N - 1, 0) * _mp.mpf(-1))
        # mpf, not float (bean `qou-4ohh`) — same defect as `_bond_type_L`'s
        # return: computed at working precision, then downcast one line later.
        # This term is ADDED to the exact-trace side of the chain-vs-exact
        # residual, so an f64 return put a floor under that residual by itself.
        return -_mp.mpf(str(alpha)) * _mp.log(1 - hx) / 2 * n_de


def _nucleon_msym(alpha):
    """Per-nucleon Kashaev mass m_sym(W) = −α·ln tr_M(W) for the free proton and
    neutron (A=1 sub-braids; cheap). The free atom word factorizes
    tr_free = tr_p^Z·tr_n^N, so m_sym(free components) = Z·msp + N·msn for ANY A
    with no bound-knot trace — the un-gateable half of the B_sym decomposition.

    NB: this is the LOG-TRACE internal mass (sub-MeV; tr_M(nucleon) ≈ 1.065), the
    quantity differenced to give B_sym = m_sym_atom − m_sym_free. It is NOT the
    physical nucleon rest mass — for that see `_nucleon_mass_canonical`."""
    from tr_m_atom_via_transfer import tr_m_atom_zn
    import mpmath as _mp
    # The traces arrive as 50-dps mpf; they used to be float()'d here and fed to
    # math.log, discarding 33 digits before the logarithm (bean `qou-4ohh`).
    tp = tr_m_atom_zn(1, 0, dps=50)[1]          # A=1 → no interfaces → atom==free
    tn = tr_m_atom_zn(0, 1, dps=50)[1]
    return -alpha * _mp.log(tp), -alpha * _mp.log(tn)


def _nucleon_mass_canonical(me, q0):
    """Canonical nucleon rest masses (m_p, m_n) via the single facade
    `canonical_mass` — the Hecke energy m_p = 2(m_μ·F_Bor − 6m_e). NB the m_μ
    here is DERIVED from q₀ (m_e·Vol(4₁)/ℏ_q²), and q₀ is on the proton pin —
    so this is not a muon anchoring, despite the historical wording.
    (≈ 938.27 / 939.56, matches CODATA). The facade is the ONE entry point for
    absolute nucleon mass; the λ_A (966) and naive Vol(𝓑₃)·tr_M (406) forms are
    deprecated (they apply 1/ℏ_q² to the wrong volume). See
    docs/canonical-mass-formula-guardrail.md."""
    from canonical_mass import proton_neutron_mass_mev
    return proton_neutron_mass_mev()


def _row(name, Z, N, alpha, me, Lbond, nucleon_msym, ame, max_strands):
    from q_parameter import Q_50_DIGIT_STR as _Q50
    from canonical_mass import _as_formattable_mpf
    with mp.workdps(max(mp.mp.dps, 60)):
        q0 = _as_formattable_mpf(mp.mpf(str(_Q50)))   # 50-dps mpf (no float64 downcast; bean qou-cqk6)
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
    Lbar = sigma_L / comb(A, 2) if A >= 2 else _as_formattable_mpf(0)
    B_fac = _as_formattable_mpf(alpha * (A - 1) * Lbar)
    # ---- colour-weighting decomposition of the factorized q-CLT ------------
    #   B_qCLT_fac = isospin-symmetric baseline (every bond = the deuteron p-n
    #   bond) + the p↔n chirality correction. The baseline IS the uniform
    #   B_qCLT — pure combinatorics on a cached constant, so it (and the
    #   free-component mass below) are available for ALL A.
    B_base = _as_formattable_mpf(alpha * (A - 1) * Lbond["pn"])
    B_qCLT = B_base                                  # uniform per-bond (un-gated)
    B_chir = _as_formattable_mpf(B_fac - B_base)
    # free-component Kashaev mass: tr_free = tr_p^Z·tr_n^N factorizes over GB
    # components, so m_sym(free) = Z·msp + N·msn for ANY A (no bound-knot trace).
    msp, msn = nucleon_msym
    m_sym_free = _as_formattable_mpf(Z * msp + N * msn)
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
    pn_term = b_pn if (Z >= 1 and N >= 1) else _as_formattable_mpf(0)
    # max(·,0): a single-nucleon / zero-count species has no same-species bonds
    # (Z−1 or N−1 would otherwise go negative and fabricate a spurious bond).
    B_sym = _as_formattable_mpf(max(Z - 1, 0) * b_pp + pn_term + max(N - 1, 0) * b_nn)
    m_sym_atom = _as_formattable_mpf(B_sym + m_sym_free)               # B_sym = m_sym_atom − m_sym_free
    # ---- B_lin = α·s, the LINEAR/SATURATING leading term of B_sym. The bond
    #   suppression s = 1 − tr_atom/tr_free and B_sym = α·L = −α·ln(1−s), so
    #   s = 1 − e^{−L} with L = B_sym/α — recoverable from the closed-form chain
    #   (no exact trace needed). B_lin = α·s = α(1 − e^{−B_sym/α}) saturates at α
    #   (s < 1), so it under-binds increasingly with A. Leading term: B_lin ≈ B_sym
    #   for small L (B_sym = α(s + s²/2 + …)).
    with mp.workdps(max(mp.mp.dps, 60)):
        B_lin = _as_formattable_mpf(alpha * (1 - mp.exp(-B_sym / alpha))) if alpha else _as_formattable_mpf(0)

        # Explicit h^4 = (q_0 - q_0^{-1})^4 modification applied to the raw trace B_lin 
        # scaled by the topological exponent (10A-5), to observe jet-order scaling.
        h4 = (q0 - 1 / q0)**4
        B_tetra = _as_formattable_mpf(B_lin * (q0 ** (10*A - 5)) * h4)
        m_tetra = _as_formattable_mpf(m_sym_free - B_tetra)

    # ---- m_can⁰: brane-tower LEVEL-0 binding. The per-braid brane tower
    #   (per-braid-mass-tower.md) has descended (n=0) term |tr_M(W)|, so its
    #   binding is B_can⁰ = E₀·Δtr_M = α·(|tr_M_free| − |tr_M_atom|) — the
    #   absolute trace difference (≡ binding_canonical), NOT the log B_sym.
    #   PURE Markov trace: tr_free = exp(−m_sym_free/α) factorizes over GB
    #   components (cheap, all A); tr_atom = tr_free·exp(−B_sym/α) from the
    #   closed-form chain. ZERO AME / CODATA beyond the CAL-1 m_e unit (in α)
    #   and CAL-2 q₀. Higher Φ_q tower levels (B_can_tower) add O(ℏ_q²)/level.
    tr_free_val = mp.exp(-m_sym_free / alpha) if alpha else None
    tr_atom_val = (tr_free_val * mp.exp(-B_sym / alpha)
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
    #   |chain − exact| ≈ 2e-49, i.e. the 50-dps serialization floor.
    #
    #   That figure read "≈ 1e-13" until 2026-09-05 and the printed value was
    #   8.9e-16 — BOTH were artifacts, not measurements (bean `qou-4ohh`). Three
    #   f64 downcasts sat on this path (`_constants`' return, `_bond_type_L`'s
    #   return, `_chain_writhe_shift`'s return, plus `float(ta), float(tf)`
    #   before the logarithm), so the residual could not be smaller than f64
    #   epsilon on quantities of order 1-30 MeV whatever the mathematics did.
    #   With them removed the residual is 2.1e-49 / 4.3e-50 / 5.3e-50 at
    #   2H/3H/3He and every other column of this dashboard is BYTE-IDENTICAL.
    #
    #   Note 3H printed exactly `0.0e+00` before. That was not agreement — it
    #   was the difference underflowing below f64 resolution, which is the
    #   failure mode AGENTS.md names: a float64 agreement reported as exact is
    #   the floor of the arithmetic, not evidence about the mathematics. The
    #   chain really does reproduce the exact p(3A) trace; that claim is now
    #   supported by a measurement instead of by noise.
    B_sym_exact = chain_resid = None
    E_retained = E_emitted = E_multilink = B_sym_ent = None
    S_val = NUCLEAR_SPINS.get(name, Fraction(1, 2) if (A % 2) else Fraction(0))
    lam = get_ground_state_partition(Z, N, S_val)
    if lam:
        with mp.workdps(max(mp.mp.dps, 60)):
            w_lam = W_lambda_float(q0, lam)
            E_gate = _as_formattable_mpf(alpha * mp.log(1 / w_lam))
            c_lam = _as_formattable_mpf(bame / E_gate) if bame else None
    else:
        lam, w_lam, E_gate, c_lam = None, None, None, None
    # ---- B_vol: the ALL-KNOTS entanglement binding = the liquid-drop VOLUME term.
    #   Entanglement is a property of EVERY knot/particle, not one selected partition
    #   (the single-partition E_gate is ⁴He-local and breaks for A≳24). Summing the
    #   per-knot occupancy surprisal over all A nucleon knots gives a_V·A with the
    #   coefficient DEPRECATED 2026-08-08 (postdiction near-match, NOT derived — no
    #   basis in the derivation chain; see banner + avol red-team):
    #   a_V = E₀·ln(1/W_free), W_free = the free
    #   nucleon's (1,1,1) Plancherel weight. a_V ≈ 7.584 MeV/nucleon ≈ empirical net
    #   B/A. Valid for ALL A (no W_λ≥1 breakdown); tracks ¹²C/¹⁶O to ~1–5%. The
    #   residual (light over-binding, magic dips) is the surface/Coulomb/shell
    #   structure — the open part. Probe: probes/su4_occupancy_binding_probe.py.
    with mp.workdps(max(mp.mp.dps, 60)):
        a_V = _as_formattable_mpf(alpha * mp.log(1 / W_lambda_float(q0, (1, 1, 1))))   # DEPRECATED postdiction coeff (not derived — see banner)
        B_vol = _as_formattable_mpf(A * a_V)
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
        ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
        # `ta, tf = float(ta), float(tf)` used to sit here (bean `qou-4ohh`).
        # It collapsed two 50-dps traces to f64 immediately before the
        # logarithm, which put a ~1e-16 floor under `chain_resid` below — the
        # residual this check exists to measure. That is the same
        # `math.log(float(tf)/float(ta))` collapse `_bond_type_L`'s docstring
        # names as forbidden by the owner directive.
        B_sym_exact = alpha * mp.log(tf / ta)
        # WRITHE-COMMENSURABILITY (fixed 2026-08-15). `_bond_type_L` applies the
        # Lean-proved writhe normalisation L_XY -> L_XY - (delta_e/2)*ln(1-h)
        # (owner directive 2026-08-09, QOU/QBeta/WritheNormalisation.lean), and
        # `tr_m_atom_zn` does NOT. Differencing them directly therefore measures
        # the writhe factor, not the factorisation: the shift is
        # alpha*|ln(1-h)|/2 = 0.4908765 MeV per PURE crossing, equal-and-opposite
        # on pp (delta_e=+1) vs nn (delta_e=-1). It cancels exactly when
        # #pp = #nn -- i.e. on the N = Z line -- and is +/-0.4909 per unit of the
        # imbalance d = N-Z otherwise. That is why 2H and 4He agreed to 3.4e-04
        # while 3H and 3He were off by -/+0.4909: not noise, and not an A-growing
        # error either. The footnote used to call this "float64 dashboard noise",
        # which is wrong by ~12 orders of magnitude and made the ONLY
        # non-circular check on the production chain unable to pass off N = Z.
        # Add the same normalisation to the trace side so the residual tests the
        # per-bond factorisation, which is what this check is for.
        _writhe = _chain_writhe_shift(Z, N, alpha)
        chain_resid = abs(B_sym - (B_sym_exact + _writhe))
        # entanglement (sibling d5f247b40d/23a0019e7f): bar-involution (q↦q⁻¹)
        # split — bar-even (cosh) = RETAINED binding/volume; bar-odd (sinh) =
        # EMITTED/radiated (Chern–Simons / γγ̄). E_multilink = bar-odd of the
        # inter-nucleon binding defect (tr_free−tr_atom); B_sym_ent augments the
        # chain binding with the radiated inter-nucleon energy.
        # q0^-1 leg, built from the 50-dps string. It used to divide into
        # `_mp.mpf(str(q_parameter.Q))` — the f64 — so the inverse-anchor leg
        # was capped at ~17 digits while the forward leg was not.
        from q_parameter import Q_50_DIGIT_STR as _Q50i
        ta_i, tf_i, _, _ = tr_m_atom_zn(
            Z, N, q=_mp.mpf(1) / _mp.mpf(str(_Q50i)), dps=50)
        # NO-FLOAT64 (AGENTS.md): these were cast via `float(...)` until
        # 2026-08-26.  Measured impact on E_multilink was 5e-22..3e-19 relative
        # (2H/3H/3He/4He), i.e. none of the displayed digits moved -- the two
        # defects differ at O(1), so the subtraction below is not in fact
        # near-cancelling at these parameters.  Removed regardless: the rule is
        # not conditional on the cancellation happening to be benign, and a
        # dashboard column becomes an argument in an audit the moment it is
        # quoted.
        E_retained = alpha * (ta + ta_i) / 2
        E_emitted = alpha * abs(ta - ta_i) / 2
        defect0, defecti = tf - ta, tf_i - ta_i
        E_multilink = alpha * abs((defect0 - defecti) / 2)
        B_sym_ent = B_sym + E_multilink
    return {"name": name, "Z": Z, "N": N, "A": A, "n": n, "B_AME": bame,
            "sigma_AME": sigma_ame, "M_atom_AME": m_atom_ame, "sigma_atom": sigma_atom,
            "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
            "B_lin": B_lin, "B_tetra": B_tetra, "B_can0": B_can0, "B_can_bor": B_can_bor,
            "m_tetra": m_tetra,
            "tr_free": tr_free_val, "tr_atom": tr_atom_val,
            "B_sym": B_sym, "B_sym_exact": B_sym_exact, "chain_resid": chain_resid,
            "B_qCLT": B_qCLT,
            "B_qCLT_fac": B_fac, "B_base": B_base, "B_chir": B_chir,
            "E_retained": E_retained, "E_emitted": E_emitted,
            "E_multilink": E_multilink, "B_sym_ent": B_sym_ent,
            "m_sym_atom": m_sym_atom, "m_sym_free": m_sym_free,
            "su4_partition": lam, "W_lam": w_lam, "E_gate": E_gate, "c_lam": c_lam,
            "a_V": a_V, "B_vol": B_vol, "E_C": E_C}


def _disp(v):
    """Coerce a value to an arbitrary-precision `Decimal` display type.

    `mpmath.mpf` implements `__format__` but rejects the fixed-point /
    scientific specs used below, so an mpf-valued cell (e.g. `E_C`, which
    `coulomb_energy_mev` returns at full working precision) raises
    `TypeError` instead of printing. Coercion happens HERE, at the display
    boundary only, using arbitrary-precision `Decimal(mp.nstr(v, 50))` (no
    binary64 `float` conversion) — every computed quantity stays mpf upstream
    and nothing that reaches a witness passes through this function.
    """
    if v is None:
        return None
    if isinstance(v, mp.mpf):
        return Decimal(mp.nstr(v, 50))
    return Decimal(str(v))


def _fmt(v, w=8, p=2):
    v = _disp(v)
    return f"{v:>{w}.{p}f}" if v is not None else f"{'—':>{w}}"


def _sci(v, w=11, p=2):
    """Scientific-notation cell — for sub-keV σ_exp values that round to
    0.000000 in fixed-point and read as a misleading empty column."""
    v = _disp(v)
    return f"{v:>{w}.{p}e}" if v is not None else f"{'—':>{w}}"


def _print_provenance() -> None:
    """What each quantity IS, epistemically. Printed, not left to prose.

    The dashboard mixes three very different kinds of number in adjacent
    columns — a CODATA input, a parameter-free substrate derivation, and an
    exploratory extrapolation — and nothing in the table said which was which.
    A reader comparing `m_can` to `M_meas` is comparing a prediction against a
    measurement; a reader comparing `B_AME` to `σ_exp` is not.
    """
    print("\n#### Provenance — what kind of number each column is")
    print("| tag | meaning |")
    print("| --- | --- |")
    print("| `MEASURED`  | experimental input/target: B_AME, M_meas, σ_exp "
          "(AME2020), m_e (CODATA). Not predicted by anything here. |")
    print("| `CAL`       | one of the three calibrations: m_e (CAL-1), q₀ via "
          "CAL-2, m_π (CAL-3). Inputs BY CONSTRUCTION — not successes. |")
    print("| `DERIVED*`  | as DERIVED, but CONDITIONAL on an open conjecture or "
          "sorry: E_C on the Witten-κ Gram-determinant sorry. |")
    print("| `POSITED`   | the functional FORM is asserted, not derived. The "
          "log-forms: their extensivity follows from the Markov property (no "
          "conjecture), but no block licenses α·ln(ratio) as an ENERGY — the "
          "nearest, conj:knot-factor-frobenius-pairing, gives E₀ × the trace "
          "DIFFERENCE. Corrected 2026-08-26 (bean qou-mkm8); these read "
          "`DERIVED*` on a KVC citation that does not reach the atom word. |")
    print("| `DERIVED`   | parameter-free from (q₀, m_e) through the Markov "
          "trace: m_can, F_Bor. No fit, no "
          "AME beyond the comparison. |")
    print("| `EXPLORATORY` | shown for comparison, NOT production-wired: "
          "B_lin, B_tetra, m_can⁰, m_tetra. |")
    print()
    print("| column | tag | note |")
    print("| --- | --- | --- |")
    for col, tag, note in (
        ("B_AME / M_meas / σ_exp", "MEASURED", "AME2020 — the target"),
        ("m_e, q₀, m_π", "CAL", "the 3 calibrations; q₀ on the PROTON pin"),
        ("B_sym", "POSITED", "exact log-ratio α·ln(tr_free/tr_atom). The log's "
         "EXTENSIVITY is derived (Markov property, no conjecture); the α× "
         "identification as an energy is asserted. NOT KVC-conditional — "
         "vol-through-tau quantifies over BRAIDS and the atom word's letters "
         "are general Hecke elements; 0/40 closures hyperbolic ⇒ Vol = 0 while "
         "B_sym(²H) = 3.89 MeV. Corrected 2026-08-26, bean qou-mkm8"),
        ("B_qCLT_fac", "POSITED", "colour-weighted q-CLT (A→∞ approximation) — "
         "same log-form licence as B_sym"),
        ("m_can", "DERIVED", "Borromean brane tower; m_n is a PREDICTION"),
        ("E_C", "DERIVED*", "uniform-sphere Coulomb at the CAL-3 length "
         "R = λ̄_π·A^(1/3), λ̄_π = ℏc/m_π = 1.41382 fm (NOT the empirical "
         "r₀ = 1.2 fm); α_EM is DERIVED, and *conditional on an open "
         "Witten-κ sorry — see the legend"),
        ("B_lin / B_tetra / m_can⁰", "EXPLORATORY", "comparison only"),
    ):
        print(f"| `{col}` | `{tag}` | {note} |")
    print("\n" + _lean_status())


def _relerr(v, w=13):
    """A RELATIVE error in whichever unit makes it readable, unit in the cell.

    One fixed unit cannot serve this table. The proton anchor agrees at ~1e-9
    relative while ⁴He's binding-dominated mass error is ~6e-3, and forcing
    both into ppb prints `1.351e+00` beside `5.878e+06` — the reader has to
    count zeroes to see that one is a part-per-billion agreement and the other
    is over half a percent.

        >= 0.1%  -> %       >= 1 ppm -> ppm
        >= 1 ppb -> ppb     else     -> ppq  (parts per 10^15)

    Thresholds are decades, so a column stays in one unit across a row group
    unless a value genuinely crosses one. Sign is kept: it distinguishes over-
    from under-binding, which the magnitude alone does not.
    """
    if v is None:
        return f"{'—':>{w}}"
    dv = _disp(v)
    a = abs(dv)
    if a == 0:
        s = "0"
    elif a >= Decimal("1e-3"):
        s = f"{dv * Decimal(100):+.3f}%"
    elif a >= Decimal("1e-6"):
        s = f"{dv * Decimal(1000000):+.3f}ppm"
    elif a >= Decimal("1e-9"):
        s = f"{dv * Decimal(1000000000):+.3f}ppb"
    else:
        s = f"{dv * Decimal(1000000000000000):+.3f}ppq"
    return f"{s:>{w}}"


def _lean_status() -> str:
    """The REAL Lean build status, read from build-logs/lean-build-status.json.

    Deliberately not a per-quantity "Lean-proved" badge. That file records one
    status per PAPER, not per formula, so a per-row green tick would be an
    assertion nothing in the repo backs. And the status it does record is not
    green: the QOU target last built with 357 errors across 89 modules plus 7
    `sorry`s. Printing "Lean-proved 100%" over that would be the same
    label-contradicts-numbers defect this dashboard was just corrected for.

    Staleness is printed too — a months-old build status read as current is its
    own way of overclaiming.
    """
    import json as _json
    from datetime import datetime, timezone
    f = ROOT / "build-logs" / "lean-build-status.json"
    if not f.exists():
        return "Lean: no build-status file — status unknown, NOT assumed green."
    try:
        d = _json.loads(f.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return "Lean: build-status file unreadable — status unknown."
    gen = str(d.get("generatedAt", "?"))
    try:
        age = (datetime.now(timezone.utc)
               - datetime.fromisoformat(gen.replace("Z", "+00:00"))).days
        age_s = f", {age}d old" if age > 7 else ""
    except Exception:  # noqa: BLE001
        age_s = ""
    parts = []
    for r in d.get("results", []):
        n_s, n_e = len(r.get("sorries") or []), len(r.get("errors") or [])
        mark = "ok" if r.get("status") == "ok" and not n_s else "FAIL"
        parts.append(f"{r.get('paper')}={mark}"
                     + (f"({n_e}err/{n_s}sorry)" if (n_e or n_s) else ""))
    return (f"Lean build [{gen}{age_s}]: " + "  ".join(parts)
            + "\n  No quantity in this dashboard carries a per-formula Lean "
              "proof. The status above is per PAPER, and the QOU target does "
              "not currently build.")


def _err(bame, b):
    return (bame / b) if (bame is not None and b is not None and b > 0) else None


def _print_legend() -> None:
    """Explain every column header used across the dashboard's tables, so the
    output is self-documenting when pasted into a PR / issue. Grouped by table;
    every header that appears below is defined here."""
    print("#### Column legend (every header, by table)")
    print(r"""
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
| `B_vol` | ALL-KNOTS entanglement binding = the liquid-drop **volume term** `a_V·A`, with `a_V = E₀·ln(1/W_free)` ≈ **7.584 MeV/nucleon — DEPRECATED 2026-08-08 postdiction near-match, NOT derived** (no basis in the derivation chain; the surprisal form was chosen because it lands near 8 and `W_free` is unnormalised so `ln(1/W)` is not a probability — red-team `docs/audits/2026-08-22-avol-binding-redteam.md`) (W_free = the free nucleon's (1,1,1) Plancherel weight; ≈ empirical net B/A). Entanglement is a property of EVERY knot, not one selected partition — so the per-knot occupancy energy is summed over all A nucleons. Valid for ALL A (no W_λ≥1 breakdown, unlike `B_gate`); tracks ¹²C/¹⁶O to ~1–5% where B_sym misses by 2.1×. Over-binds the lightest (²H, ⁶Li) — the residual is the **surface/Coulomb/shell** structure (the SEMF corrections, open). Probe + audit: `probes/su4_occupancy_binding_probe.py`. |
| `E_C` | EM-sector **Coulomb energy** `E_C = (3/5)Z(Z−1)·α_EM·ℏc/(r₀·A^1/3)` MeV (uniform sphere). **Both inputs corrected here 2026-08-25 — the legend had described a superseded configuration.** The length is the **CAL-3** radius `R = λ̄_π·A^(1/3)` with `λ̄_π = ℏc/m_π = 1.41382 fm`; `coulomb_energy.R0_FM = LAMBDA_BAR_PI_FM`, and `R0_FM_EMPIRICAL = 1.2` is retained *for comparison only, not as the default*. And `α_EM·ℏc = 1.4399652199 MeV·fm` is no longer the CODATA literal `1.43996` — it is **derived** via `meson_em_sinh_closed_form._alpha_em_inv_derived(q₀)`. So "not fit" understates it in one direction and overstates it in another: it is derived rather than fitted, but that derivation is **conditional on an open Witten-κ Gram-determinant `sorry`**, so `E_C` is tagged `DERIVED*` rather than `DERIVED`. Two weak steps remain named in the module itself: `A^(1/3)` is a saturation assumption (solving `R = λ̄_π·A^x` gives x = 0.97/0.43/0.53/0.31 at A = 2,3,3,4, not ⅓), and coefficient-exactly-1 is a selection among four mass scales, measured at 0.985 ± 0.069 (bean `qou-usft`). The strong B-forms carry NO EM term; E_C is the repulsion that REDUCES net binding for proton-rich nuclei. Reported additively, **not** subtracted from the B-columns (they are calibrated against Coulomb-inclusive AME, so a global subtraction would double-count). E_C is cleanly separable only in the mirror-pair DIFFERENCE, where the strong core cancels: CS-core + E_C reproduces the ³H/³He, ⁷Li/⁷Be, ¹³C/¹³N splits to ~20–40% vs the production σ/σ⁻¹ bond's ~200–350% (bean 754x). Module: `coulomb_energy.py`; probe: `probes/coulomb_mirror_killswitch_probe.py`. |
| `err sym` / `err qCLT_fac` / `err gate` / `err vol` | B_AME / B_model for the production + occupancy + volume forms (1.00 = perfect, >1 under-binds, <1 over-binds) |

**Table 2 — Mass M + error** (values and error in one table; m_X = m_unbnd,can − B_X)

| Header | Meaning |
|---|---|
| `M_meas` | measured mass: M_AME = mu − B_AME for nuclei, or measured constituent mu for lone p/n. **Comparison target only — appears in NO predicted formula.** |
| `σ_exp (ppb)` | experimental 1σ on the mass = σ_B / M_meas × 10⁹ |
| `m_can` | **CANONICAL derived mass — the single Borromean per-knot pipeline** (`borromean_binding_recompute.borromean_binding`): `m_can = m_unbnd,can − B_tower`, the convergent per-braid brane tower over the Borromean nucleon trace `τ=\|tr_M(β_Bor)\|=0.9986<1` (shares τ with `F_Bor` / bean `ovud`; converges ∀Z). Pure Markov × m_e; zero AME/CODATA beyond CAL-1/CAL-2. Does NOT close to AME — the Δ_λ frontier (right shape, wrong per-λ normalization). |
| `m_can⁰` | brane-tower **level 0** on the atom-word trace: `m_unbnd,can − E₀·Δtr`. Comparison only — its higher Li₂^q tower leaves the SERIES radius at Z≥2 (atom-word `tr_p>1`, so τ_p²=1.13488 > q₀=1.10998 by 2.2%); the Borromean `m_can` is the canonical one. NB this is not a divergence — the q-product continuation is finite there and `li_2_q` now returns it (bean `qou-cw27`); Borromean is preferred on magnitude, not convergence. |
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
| CAL-2 | W-plane modulus (h²) | P_skew^β — neutron β-decay width (τ_n=ℏ/P_skew^β) | **m_μ/m_e (22 ppb)** via m_μ/m_e = Vol(4₁)/ℏ_q² (Q_β=ℏ/P_skew^β = decay proxy) |
| CAL-3 | orthogonal meson (h³) | P_avg^π — pion decay width (τ_π=ℏ/P_avg^π) | **m_π = 139.57 MeV, PDG** |

This dashboard's q₀ is the **experimental (proton) pin**, m_p/m_e,
q₀ = 1.1099785827513808… — per the 2026-08-07 owner directive that all compute
defaults to it.

CORRECTED 2026-08-25 (PR #5765): this sentence previously claimed the stem was
"now declared explicitly as `physical_proton` in `q0_anchor_manifest.json` rather
than relying on the 'not listed ⇒ proton' default". **That is false, and it was
load-bearing.** Measured: `mass_binding_dashboard` does not appear in that manifest
at all — nor do `canonical_mass`, `borromean_binding_recompute` or `coulomb_energy`.
(`tr_m_atom_via_transfer` IS listed, under `physical_proton`.) So the resolution is
correct but is obtained **by exactly the default the sentence denied relying on**.
That matters because the explicit declaration is what would protect these numbers if
anyone drove `ideal_muon` differently — a protection the dashboard claimed and did
not have. Either add the four stems to the manifest or say plainly that they resolve
by default; do not claim the former while doing the latter.

CORRECTED 2026-08-08: this paragraph previously claimed the canonical 3-CAL
(muon-anchored) value and that the proton re-pin was "not used here". The code
never matched it — `q_parameter.Q` resolves by manifest stem, this script was
unlisted, and unlisted means proton. So the numbers had been experimental-layer
all along while the prose asserted the ideal layer. Nothing about the output
changed when it was listed; only the claim did.

The *ideal* CAL-2 framing still describes the derivation chain, and `m_μ`
appears in the canonical mass `m_p = 2(m_μ·F_Bor − 6m_e)` — but with q₀ on the
proton pin, `m_μ = m_e·Vol(4₁)/ℏ_q²` is a DERIVED prediction there, not an
anchoring input. Do not read the m_μ in that formula as a muon pin. Source:
`observations/three-calibration-discipline.md` §3,
`observations/epistemic-status-of-calibrations.md`.

**Mass constituents (Table 2):** `m_unbnd,can` = framework unbound sum
Z·m_p,can + N·m_n,can via the canonical Hecke energy (proton pin)
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
    from canonical_mass import _as_formattable_mpf
    with mp.workdps(max(mp.mp.dps, 60)):
        mp_ = _as_formattable_mpf(mp.mpf(str(mp_)))
        mn_ = _as_formattable_mpf(mp.mpf(str(mn_)))
        ppb_scale = mp.mpf(10) ** 9
        kev_scale = mp.mpf(1000)
    print("### Mass  M + error (MeV; err auto-scaled %/ppm/ppb/ppq)   "
          "[canonical = Hecke energy 2(m_μ·F_Bor−6m_e) at the PROTON pin; "
          "m_μ there is derived from q₀, not an anchor; m_X = m_unbnd,can − B_X]")
    print(f"  canonical constituents (λ_A fit + naive Vol·tr_M both EXCISED): "
          f"m_p,can = {mp_can:.3f} MeV ({(mp_can/mp_-1)*100:+.3f}%), "
          f"m_n,can = {mn_can:.3f} MeV ({(mn_can/mn_-1)*100:+.3f}%) — "
          f"F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ at the proton pin (matches CODATA; m_n the "
          f"genuine prediction).")
    print("| iso | A | M_meas | σ_exp (ppb) | m_can | m_can⁰ | m_tetra | m_qCLT | "
          "err m_can | err m_qCLT |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        mu = r["Z"] * mp_ + r["N"] * mn_                 # measured constituent sum
        mu_can = r["Z"] * mp_can + r["N"] * mn_can       # framework-derived sum
        m_meas = (mu - r["B_AME"]) if r["B_AME"] is not None else mu  # measured mass
        s = r["sigma_AME"]
        s_ppb = (s / m_meas * ppb_scale) if (s and m_meas) else None
        # CANONICAL bound mass per form X: m_X = mu_can − B_X (zero AME/CODATA
        # beyond CAL-1 m_e + CAL-2 q₀; M_meas is the SEPARATE comparison target).
        def _can(bkey):
            b = r[bkey]
            return (mu_can - b) if b is not None else None
        # mass error (ppb): (m_X − M_meas)/M_meas · 10⁹
        def _err_rel(bkey):
            b = r[bkey]
            return ((mu_can - b) - m_meas) / m_meas if b is not None else None
        print(f"| {r['name']} | {r['A']} | {_fmt(m_meas,9,1)} | {_sci(s_ppb,11,2)} "
              f"| {_fmt(_can('B_can_bor'),9,1)} | {_fmt(_can('B_can0'),9,1)} "
              f"| {_fmt(r.get('m_tetra'),9,1)} | {_fmt(_can('B_qCLT_fac'),9,1)} "
              f"| {_relerr(_err_rel('B_can_bor'),15)} | {_relerr(_err_rel('B_qCLT_fac'),16)} |")

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
        b = r["B_sym"]
        m_atom_pred = (mu_can - b) + e_layer if b is not None else None
        err = ((m_atom_pred - m_atom_ame) / m_atom_ame * ppb_scale
               if (m_atom_pred is not None and m_atom_ame) else None)
        sa = r["sigma_atom"]
        s_ppb = (sa / m_atom_ame * ppb_scale) if (sa and m_atom_ame) else None
        print(f"| {r['name']} | {r['A']} | {Z} | {_fmt(m_atom_ame,10,3)} "
              f"| {_fmt(m_atom_pred,10,3)} | {_sci(err,13,3)} | {_sci(s_ppb,11,2)} "
              f"| {_fmt(e_layer,7,3)} |")
    max_fit_dev_kev = _as_formattable_mpf(max(
        abs(_electron_binding_mev(r["Z"]) - _electron_binding_mev_ame_fit(r["Z"])) * kev_scale
        for r in rows if r["Z"] > 0
    ))
    print(f"\n  B_el is DERIVED (bare-Z hydrogenic @ e-Hartree, swap 2026-08-30); "
          f"max |derived − AME fit| over this group: {max_fit_dev_kev:.4f} keV "
          f"(screening open; both far below the MeV nuclear residuals)")

    # 2. BINDING + error  (B_AME ± exp 1σ from AME2020; err X = B_AME/B_X)
    print("### Binding  B + error (MeV)   "
          "[σ_exp = AME2020 1σ; err X = B_AME/B_X (1.00 = perfect, >1 under-binds)]")
    print("| iso | A | B_AME | σ_exp (ppb) | B_can⁰ | B_sym | B_tetra | B_qCLT_fac "
          "| E_C | err can⁰ | err sym | err tetra | err qCLT_fac |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        s = r["sigma_AME"]
        s_ppb = (s / r["B_AME"] * ppb_scale) if (s and r["B_AME"]) else None
        e_can0 = _err(r["B_AME"], r["B_can0"])
        e_sym = _err(r["B_AME"], r["B_sym"])
        e_qclt_fac = _err(r["B_AME"], r["B_qCLT_fac"])
        e_tetra = _err(r["B_AME"], r.get("B_tetra"))
        print(f"| {r['name']} | {r['A']} | {_fmt(r['B_AME'])} | {_sci(s_ppb,11,2)} "
              f"| {_fmt(r['B_can0'])} | {_fmt(r['B_sym'])} | {_fmt(r.get('B_tetra'))} | {_fmt(r['B_qCLT_fac'])} "
              f"| {_fmt(r.get('E_C'))} "
              f"| {_fmt(e_can0,6)} | {_fmt(e_sym,6)} | {_fmt(e_tetra,6)} | {_fmt(e_qclt_fac,6)} "
              f"|")

    # chain ≡ exact-trace validation (rows where the p(3A) trace is feasible)
    val = [(r["name"], r["chain_resid"]) for r in rows
           if r["chain_resid"] is not None]
    if val:
        mx = max(v[1] for v in val)
        print(f"\n  B_sym closed-form chain ≡ exact p(3A) trace: max|Δ| = "
              f"{mx:.1e} MeV over {{{', '.join(v[0] for v in val)}}} "
              f"(n=3A ≤ {args.max_strands}; writhe-normalised on BOTH sides — the "
              f"chain carries the Lean-proved (1−h)^(δe/2) factor and the raw "
              f"trace does not, so comparing them un-normalised measures that "
              f"factor (±0.4909 MeV per unit of d = N−Z) rather than the "
              f"factorisation. Audit 2026-06-16-b-sym-linear-chain-closed-form.md "
              f"predates both the writhe normalisation and convention D). "
              f"Chain used for all A.")

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
    # SU(4) Dynamic Occupancy table REMOVED — see the deprecation note on
    # E_gate above. It reported E_gate / c_lambda / W_lambda, all of which are
    # the same unlicensed construct.

    # 9. TWO-TERM QED & GPMT MODIFIED-DIMENSION DIAGNOSTICS (A=1..4)
    from canonical_mass import (
        proton_qed_self_energy_borromean_mev,
        np_qed_splitting_borromean_conn_mev,
        neutron_mass_two_term_mev,
        gpmt_three_row_cumulants,
        inter_nucleon_pair_charge,
    )
    gpmt_c = gpmt_three_row_cumulants(q0)
    mp_qed_bor = proton_qed_self_energy_borromean_mev(k_weighted=False)
    dm_qed_bor = np_qed_splitting_borromean_conn_mev(weighting="plain")
    mn_2term = neutron_mass_two_term_mev(weighting="plain")
    mn_1term_err_ppb = _as_formattable_mpf((mn_can - mn_) / mn_ * ppb_scale)
    mn_2term_err_ppb = _as_formattable_mpf((mn_2term - mn_) / mn_ * ppb_scale)

    print("\n### Table 9 — Two-Term QED & GPMT Modified-Dimension Diagnostics (A=1..4)")
    print("  Lean modules: `NucleonWeightSpaceTwoTerm`, `USpinColemanGlashowLambdaSigma`, "
          "`GPMTThreeRowCumulantBridge`, `H4GPMTModifiedDimensionCumulants`, `ThreeRowSpringerSYTDerivation`.")
    print(f"  A=1 Borromean V³ QED: M_p^QED,conn = +{mp_qed_bor*kev_scale:.4f} keV | "
          f"Δm_QED^conn(n−p) = {dm_qed_bor*kev_scale:+.4f} keV | "
          f"m_n(1-term) = {mn_can:.7f} MeV ({mn_1term_err_ppb:+.1f} ppb) → "
          f"m_n^two-term = {mn_2term:.7f} MeV ({mn_2term_err_ppb:+.1f} ppb, −70.4% residual).")
    print(f"  GPMT ≥3-row modified dimensions at q₀: d_mod(1,1,1) = {gpmt_c['dMod111']:.6f}, "
          f"d_mod(2,1,1) = {gpmt_c['dMod211']:.6f}, d_mod(1,1,1,1) = +{gpmt_c['dMod1111']:.6f} | "
          f"μ₃^GPMT = +{gpmt_c['mu3GPMT']:.6f} (>0), μ₄^GPMT,H4 = {gpmt_c['mu4GPMT_H4']:.6f} (<0).")
    print("| iso | A | Z | N | Q_pair | B_ext^GPMT(H4) | E₀·B_ext(H4) (MeV) | E_C(CAL-3) (MeV) | Δm_QED^V3 (keV) | two-term note |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|---|")
    for r in rows:
        if r["A"] > 4:
            continue
        A_r, Z_r, N_r = r["A"], r["Z"], r["N"]
        q_pair = inter_nucleon_pair_charge(Z_r)
        if A_r == 1:
            bext_h4 = _as_formattable_mpf(0)
            qed_v3_kev = (mp_qed_bor * kev_scale) if Z_r == 1 else ((mp_qed_bor + dm_qed_bor) * kev_scale)
            note = ("CAL-2 proton pin anchor" if Z_r == 1
                    else f"m_n^2term err {mn_2term_err_ppb:+.1f} ppb (vs {mn_1term_err_ppb:+.1f} ppb 1-term)")
        elif A_r == 2:
            bext_h4 = gpmt_c["BextGPMT_2"]
            qed_v3_kev = (2 * mp_qed_bor + dm_qed_bor) * kev_scale
            note = "μ₂^GPMT = 0 (no ≥3-row ideal in H₂(q))"
        elif A_r == 3:
            bext_h4 = gpmt_c["BextGPMT_3"]
            qed_v3_kev = (Z_r * mp_qed_bor + N_r * (mp_qed_bor + dm_qed_bor)) * kev_scale
            note = ("mirror lo: Q_pair=0, strong core = ³He" if Z_r == 1
                    else "mirror hi: B(³H)−B(³He) = +0.764 MeV AME vs +0.847 MeV E_C")
        else:
            bext_h4 = gpmt_c["BextGPMT_4_H4"]
            qed_v3_kev = (2 * (2 * mp_qed_bor + dm_qed_bor)) * kev_scale
            note = f"H₄ cumulant μ₄^H4 = {gpmt_c['mu4GPMT_H4']:.4f} < 0 (4-body saturation)"
        e0_bext = E0 * bext_h4
        print(f"| {r['name']} | {A_r} | {Z_r} | {N_r} | {q_pair} "
              f"| {_fmt(bext_h4,8,4)} | {_fmt(e0_bext,8,4)} "
              f"| {_fmt(r.get('E_C'),8,4)} | {_fmt(qed_v3_kev,8,4)} | {note} |")

    _print_provenance()
    print("\n  Forms: B_sym=α·ln(tr_free/tr_atom)=α[(Z−1)L_pp+L_pn+(N−1)L_nn] "
          "(exact linear chain, all A) · B_qCLT=α·(A−1)·ℓ̄(D) · "
          "B_qCLT_fac=α·(A−1)·⟨bond-type L⟩. "
          "Defn: algebraic-quantum-volume.md (Vol_alg := tr_M, a naming). The "
          "log-forms are POSITED, not KVC-conditional — see the module "
          "docstring, bean qou-mkm8.")
    _out = sys.stdout.getvalue()
    sys.stdout = _old_stdout
    print(format_md_tables(_out), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
