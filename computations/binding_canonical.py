#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
🛑 SUPERSEDED LAW — this module's `B_MeV` is `Q_beta . Delta_tr`, and that law
is REFUTED. It is kept for provenance and comparison; do not quote `B_MeV` as a
binding-energy prediction.

`tr_M` is MULTIPLICATIVE along the chain (closed form: `t_p^Z t_n^N . prod b`)
and binding energy is EXTENSIVE, so a constant times a product cannot be a line.
Measured over the 2548 AME2020 nuclides with MEASURED binding energies, at the
law's OWN optimal scale, the residual p5-p95 spread is **1592x** (238U over-bound
19.6-fold). Worse, `Delta_tr/tr_free = 1 - exp(-S)` exactly, which is within
7.7e-4 of 1 by A = 11: above that, `Delta_tr` does not merely MIS-SCALE the
binding energy, it does not CONTAIN it.

**The replacement**, which consumes the SAME derived bond factors and is forced
rather than chosen (`log` is the unique multiplicative-to-additive map):

    B = E_0 . log( tr_M(W_free) / tr_M(W_atom) )
      = E_0 . [ (Z-1)(-ln b_pp) + (-ln b_pn) + (N-1)(-ln b_nn) ]

implemented in `computations/binding_log_free_energy.py` (bean `lkpl`). p5-p95
spread **1.225x** on the same 2548 nuclides — a ~1300x gain from changing the
FUNCTIONAL, not the constant.

Scale, as ruled 2026-09-05 (brane-tower axioms preferred):
`E_0 = m_e.c_q^2.hbar_q/(1 - hbar_q^2) = 4.227483` MeV. With `delta = [2]_q`
pinned (`qou-xf14`) and 3 strands per nucleon the law is an upper BOUND on
binding for 2547 of 2548 measured nuclides, saturated at the iron peak to 0.6 %;
the sole exception is 4He.

Full record: `docs/audits/2026-09-05-binding-law-arc-synthesis.md`.
Beans: `qou-2pnv` (derive-or-retract, derive half discharged), `qou-gm4q`,
`qou-q7ga`, `qou-xf14`, `qou-qkbp`.

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Atom binding via the CANONICAL Jones-Markov trace.

Wires markov_trace_canonical.tr_M_element (Direction 1 of the
validity audit) into the atom braid-word binding calculation:

  B(Z, N) = E_0 · ( tr_M(W_free) − tr_M(W_atom) )   [signed; categorical]

where tr_M is the Markov-axioms-satisfying trace matching
prop:categorical-mass-markov's explicit values table — NOT the
Plancherel-weighted form used in hecke_core.atom_markov_trace and
mass_at_3A_proper.binding_3A (both deviate from the prop's z).

TRACE CONVENTION: **convention D** (SU(2)/Temperley-Lieb, Jones),
z = q^3/(q^2+1) ≈ 0.612688, y_(1^3) = 0. This module holds no z of its
own — it inherits the default of `markov_trace_canonical.tr_M_element`
(l.318-319 call it without `z`), which is `hecke_symbolic.z_markov`,
switched C -> D on 2026-08-09 (bean qou-wgta item 4). This prose said
"the prop's z = 1/(q^{1/2} + q^{-1/2}) ≈ 0.499" — convention C, excised
by owner ruling the same day. Registry:
docs/coordination/trace-convention-registry.md.

Result is compared to:
  • binding_3A (Plancherel)         — current best H_{3A} path
  • tower_binding_full (H_3 tower)  — current per-gen path
  • AME experimental binding        — ground truth

For small A (D, T, 3He, 4He), the full atom braid word reduces to a
symbolic Hecke element; the canonical trace gives an exact value
in q that we evaluate at q₀ = 1.11.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from markov_trace_canonical import tr_M_element
from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement, HA as H_SYMB, q as q_sym,
)
from mass_at_3A_proper import atom_braid_word_3A
from experimental_constants import Q_NEUTRON_MEV as _Q_BETA_N
# 50-dps sources. `h_q` is only used in _D_HECKE_TOL (1e-9) comparisons and `q0`
# in a sympy subst cast to complex, so neither NEEDS full precision — but
# reading the f64 name is what the NO FLOAT64 directive forbids, and the
# _MP family is a drop-in in both positions.
from q_parameter import Q_MP as q0, HA_MP as h_q  # canonical aliases per AGENTS.md §7
from witness_base import WitnessBuilder  # noqa: E402
# AME 2020 binding-energy comparison targets + proton mass (validation-only,
# NOT calibration inputs — per AGENTS.md §"Canonical derivation chain" the
# 3 calibrations are CAL-1 m_e, CAL-2 P_skew^β, CAL-3 P_avg^π; these AME values
# are used ONLY for the err = pred - AME_B_* comparison in the __main__
# print loop below). Added via PR #1105 (codata_constants AME extension).
from codata_constants import (
    M_P_MEV_VALIDATION,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    ame_binding_mev,
)


# Tolerance for float-to-symbolic conversion of the Hecke `d` coefficient.
# 1e-6 was too coarse to separate the colour-weighted p-n interface (which sits
# 7.190163e-05 from -h/2) from a genuine miss, and there was no branch for it in
# any case. 1e-9 mirrors `atom_nf_symbolic_D._D_HECKE_TOL` and leaves ~7 orders
# of margin on both sides of every target.
_D_HECKE_TOL = 1e-9


def _flavor_split_leading_sym(q):
    """Symbolic δ, LEADING term only:  δ(q) = (q−1)²(1−q⁻⁴)/3.

    Deliberately the leading term alone, matching
    `canonical_braid_crossings._avg_color_delta` — which builds the numeric
    crossing this must reproduce — and NOT
    `tr_m_algebraic_q.flavor_split_leading_sym`, which multiplies by a posited
    subleading (1 + ℏ³) and so disagrees by ℏ³ ≈ 9.727e-04 relative at q_0
    (bean `qou-4e5k`).
    """
    return (q - 1) ** 2 * (1 - q ** (-4)) / sp.Integer(3)


def _d_weighted_at_q0() -> float:
    """Numeric `d` of the colour-weighted p-n crossing at q_0.

    Sourced from `canonical_braid_crossings.d_for_ctype`, the module that owns
    ctype knowledge, so this file never carries a second definition of the
    weighting — the `qou-4e5k` failure mode of two copies of one dispatch
    disagreeing about the same crossing.
    """
    from canonical_braid_crossings import d_for_ctype
    return float(d_for_ctype("averaged_weighted", h_q))


def build_atom_symbolic(Z: int, N: int, *, include_inter: bool = True,
                          m_pp: int = 1, m_pn: int = 1,
                          m_nn: int = 1,
                          reduce_every: int = 4,
                          max_terms: int = 50000,
                          ) -> SymbolicHeckeElement:
    """Build atom braid as SymbolicHeckeElement using symbolic q.

    Incremental Gröbner-Shirshov reduction: apply `div.reduce()` after
    every `reduce_every` factors multiplied in, instead of letting
    the flat product expand to millions of terms before a single
    final reduction.  This matches the pattern in
    `nuclear-braid-exact.py::build_nuclear_braid_incremental`.

    Parameters
    ----------
    reduce_every : int
        Number of factors to multiply in between reduction steps.
        Setting this to 1 reduces after every factor (safest, slowest
        per-factor); 4 matches a nucleon intra-shell (two gens × two
        factors); setting it to infinity reproduces the legacy flat
        build (blows up at 4He).  Default 4.
    max_terms : int
        Abort if the intermediate element exceeds this many terms
        after a reduction step.  Matches the nuclear-braid-exact
        default; raises RuntimeError if hit.
    """
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)

    def _factor_from(c_f: float, d_f: float, g: int
                      ) -> SymbolicHeckeElement:
        """Hecke factor c·T_g + d·I as a symbolic element.

        The colour-weighted p-n interface carries d = -h(1/2 - δ/4), which sits
        h·δ/4 = 7.190163e-05 from the colour-BLIND -h/2. This function used to
        have no branch for it at all: with the ±h and ±h/2 windows at 1e-6, the
        weighted crossing missed both and fell through to `sp.nsimplify(d_f)`,
        which freezes a q_0 float into a rational and destroys the q-dependence
        the symbolic path exists to carry.

        That gap is why the closed-form path below was pinned to
        `strict_averaged` — not a considered choice between conventions, but
        the only one this builder could express. It is placed STRUCTURALLY here,
        as in `atom_nf_symbolic_D._factor_from`, which carries the same fix for
        the sibling failure mode (bean `qou-4e5k`: a 1e-3 window that swallowed
        the weighting instead of missing it).
        """
        if abs(c_f) < 1e-12:
            c = sp.Integer(0)
        else:
            c = sp.Integer(1)
        if abs(d_f) < 1e-12:
            d = sp.Integer(0)
        elif abs(d_f - 1.0) < 1e-12:
            d = sp.Integer(1)
        elif abs(d_f + h_q) < _D_HECKE_TOL:
            d = -H_SYMB
        elif abs(d_f - _d_weighted_at_q0()) < _D_HECKE_TOL:
            # Colour-weighted p-n interface: -h(1/2 - δ/4), δ = flavour split.
            d = -H_SYMB * (sp.Rational(1, 2) - _flavor_split_leading_sym(q_sym) / 4)
        elif abs(d_f + h_q / 2) < _D_HECKE_TOL:
            d = -H_SYMB / 2
        else:
            d = sp.nsimplify(d_f)
        return SymbolicHeckeElement({(g,): c, (): d})

    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since_last_reduce = 0
    for (c_f, d_f, g) in word:
        elem = elem * _factor_from(c_f, d_f, g)
        since_last_reduce += 1
        if since_last_reduce >= reduce_every:
            elem, _ = div.reduce(elem, engine='laurent')
            since_last_reduce = 0
            if elem.n_terms() > max_terms:
                raise RuntimeError(
                    f"atom-braid build exceeded max_terms={max_terms} "
                    f"(Z={Z}, N={N}, gen={g}); current terms = "
                    f"{elem.n_terms()}")
    if since_last_reduce > 0:
        elem, _ = div.reduce(elem, engine='laurent')
    return elem


def binding_canonical(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                        Q_beta_n_mev: float = float(_Q_BETA_N),
                        reduce_before_trace: bool = True,
                        use_closed_form: bool = False,
                        use_transfer: bool = True,
                        verbose: bool = False,
                        **kwargs) -> dict:
    """Binding via canonical Markov trace.

    B = Q_β(n) · (tr_M(W_free) − tr_M(W_atom)),   [SIGNED categorical
    difference — see the in-body note; the double-modulus form was a
    non-archimedean misuse]
    Q_β(n) = 0.78233341 MeV (free-neutron β-decay Q-value, the **CAL-2
    proxy** — NOT CAL-3; CAL-3 is P_avg^π, exactly as line 69 of this file
    already states. `precision-goals.md` scores Q_β as a *prediction*
    carrying 1248–1279 ppb, not as a calibration input, and
    `three-calibration-inputs-context` forbids "a second hadronic scale".
    Per [`prop:three-calibration-inputs`](../../folio/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)).

    **Naming note (2026-05-17, this branch).** This binding-scale
    parameter is the **β-decay Q-value $Q_\\beta(n)$**, **NOT** the
    canonical energy scale $E_0 = m_e/(q_0(q_0-1)) \\approx 4.186$
    MeV (a different quantity, ~5× larger). Earlier revisions
    misnamed this parameter `E_0`; the value used here is correct
    (the formula in [`prop:categorical-mass-markov`](../../folio/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md)
    requires $Q_\\beta$-scaled dimensionless trace differences),
    only the name was wrong. The function now exposes the parameter
    with its correct identifier. **Dimensional note.** `Q_beta_n_mev`
    enters the formula `B = Q_β(n) · (tr_M(W_free) - tr_M(W_atom))`
    as the **MeV-dimensioned multiplier** of a dimensionless trace
    difference; no further $E_0$ scaling is applied (in particular,
    do *not* multiply the result by `e_0_full_mev()` — that would
    double-scale).

    Callers that previously passed `E_0=...` must update to
    `Q_beta_n_mev=...`. The old keyword is captured by `**kwargs`
    and raises an explicit `AssertionError` with the migration
    message; any other unexpected keyword raises `TypeError`. The
    single internal caller `kahler_lift.py:343` is updated in the
    same commit.
    """
    assert "E_0" not in kwargs, (
        "binding_canonical: the `E_0` keyword is deprecated; the "
        "parameter was misnamed and is now `Q_beta_n_mev` (the "
        "free-neutron β-decay Q-value, NOT the canonical energy "
        "scale E_0 ≈ 4.186 MeV). Pass `Q_beta_n_mev=...` instead."
    )
    if kwargs:
        raise TypeError(
            f"binding_canonical: unexpected keyword arguments "
            f"{sorted(kwargs)}"
        )
    A = Z + N
    n_strands = 3 * A

    # Hoisted to function scope. Two of the three branches below used to
    # `import mpmath as mp` locally, which makes `mp` a function-LOCAL name
    # for the whole body — so the shared tail could reach it on one route and
    # raise `UnboundLocalError` on another. The tail now needs it on every
    # route (it carries the trace through as `mpf` rather than collapsing to
    # binary64), so the import belongs here.
    import mpmath as mp

    # ── Fast path: fine-Bratteli transfer matrix (DEFAULT) ───────
    # Lossless Σ_{λ ⊢ 3A} y_λ χ^λ over ALL p(3A) partitions via the
    # monotone-word transfer matrix — no d_λ wall, no native dep, full
    # 50-dps (the legacy symbolic path below collapses to float64 via
    # complex(sp.N(...)) and lossily nsimplify's the color-weighted δ,
    # so the transfer path is both faster AND more precise here).
    # ~5000× the symbolic tr_M_element path (⁶Li 0.16 s vs ~17 min);
    # transfer ≡ char_fast (full Hoefsmit) to 4.7e-15. Honours the
    # no-truncation precision ruling — ALL partitions kept, the speed is
    # from the transfer sweep, NOT from dropping partitions (see
    # docs/audits/2026-06-10-binding-active-set-compute-optimization.md).
    # use_closed_form=True still takes precedence: it is the
    # strict_averaged-convention path retained for that family of callers
    # (mass_table_comprehensive, binding_factor_f_*, …).
    if use_transfer and not use_closed_form:
        import mpmath as mp
        from tr_m_atom_via_transfer import tr_m_atom_zn
        # The traces carry 50 digits: χ is evaluated at the 50-digit
        # Q_50_DIGIT_STR inside `chi_all_lambda_any(dps=50)`. They are
        # SERIALIZED at that width too, not at the ambient `mp.dps` --
        # `chi_free_via_lr` (imported lazily inside tr_m_atom_zn) calls
        # `set_compute_dps()` at module scope, which raises the global to 70,
        # and `nstr(…, mp.mp.dps)` then printed 20 digits the trace does not
        # have (measured 2026-11-15: tr_M_atom went from 50 to 70 digits on a
        # re-run with no change to this file).
        _TR_DPS = 50
        tr_atom_mp, tr_free_mp, chi_atom, wall = tr_m_atom_zn(
            Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn, dps=_TR_DPS)
        # Signed categorical scalar Δtr = tr_M(W_free) − tr_M(W_atom);
        # Im(q_0)=0 ⇒ real at the substrate anchor. Q_β(n) is the MeV-
        # dimensioned multiplier of the dimensionless trace difference.
        delta_tr = tr_free_mp - tr_atom_mp
        # 🛑 SUPERSEDED: `Q_beta . Delta_tr` is refuted (module banner). Kept for
        # provenance; the live law is E_0 . log(tr_free/tr_atom) in
        # computations/binding_log_free_energy.py.
        B = mp.mpf(str(Q_beta_n_mev)) * delta_tr
        if verbose:
            print(f"  transfer tr_M (all λ={len(chi_atom)}, lossless): "
                  f"atom={mp.nstr(tr_atom_mp, 12)} "
                  f"free={mp.nstr(tr_free_mp, 12)}  {wall:.3f}s")
        return {
            "status": "solved",
            "Z": Z, "N": N, "A": A,
            "tr_M_atom": mp.nstr(tr_atom_mp, _TR_DPS),
            "tr_M_free": mp.nstr(tr_free_mp, _TR_DPS),
            "Q_beta_n_MeV": Q_beta_n_mev,
            # mpf, not `float(B)` — see the note on the shared tail's exit.
            "B_MeV": B,
            # Δtr is the DIMENSIONLESS categorical scalar — pure Hecke trace
            # arithmetic at 50 dps with no experimental input, so it is the part
            # of B that is genuinely precise. Exposed because Q_β CANCELS in any
            # ratio of two B_pred: B(a)/B(b) = Δtr(a)/Δtr(b), so a consumer
            # taking ratios (mirror asymmetries, per-A comparisons) reads the
            # categorical content directly, with no experimental factor in it
            # at all — B_MeV's own precision is capped by Q_β's 8.5e-07
            # relative experimental uncertainty, not by the arithmetic.
            "delta_tr_exact": mp.nstr(delta_tr, _TR_DPS),
            "n_atom_terms": -1,
            "n_free_terms": -1,
            "use_closed_form": False,
            "use_transfer": True,
            "n_partitions": len(chi_atom),
            "wall_sec": wall,
        }

    div = SymbolicHeckeDivision() if reduce_before_trace else None

    # ── Fast path: closed-form tr_M(𝓑_K) (Phase 5q identity) ────
    # When `use_closed_form=True`, skip the symbolic H_{3A} tr_M
    # recursion entirely. The Phase 5c.1 + 5l identity gives
    #   tr_M(𝓑_K)      = tr_M^3(p)^Z · tr_M^3(n)^N · ∏_i f_i(q)
    #   tr_M(𝓑_K^vac) = tr_M^3(p)^Z · tr_M^3(n)^N           (no interfaces)
    # where the H_3 building blocks tr_M^3(p), tr_M^3(n) are computed
    # ONCE at q_0 and reused for every (Z, N). For A=3 this cuts the
    # 5-12 k-op sympy aggregation entirely; for A≥4 it sidesteps the
    # H_{3A} partition sum which is the asymptotic bottleneck per
    # cheat-sheet §5 Migration Backlog #4.
    if use_closed_form:
        try:
            from closed_form_tau_M import closed_form_tau_M
            from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr
            from hecke_core import (
                _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
            )
            import mpmath as mp
            from q_parameter import Q_50_DIGIT_STR

            t0 = time.time()
            q_val = mp.mpf(Q_50_DIGIT_STR)
            # tau_p, tau_n via the Wenzl bridge at H_3 — same
            # entry point as the production atom-level code, with
            # Python fallback when pyhecke_native is unavailable.
            #
            # GROUPED intra-nucleon ordering, deliberately left as it was and
            # now named rather than open-coded (bean `qou-t29k`). Two reasons,
            # and the first is why switching would be churn rather than a fix:
            #
            #   1. THE TAUS CANCEL IN EVERYTHING THAT SURVIVED THE REFUTATION.
            #      Below, `tr_free = tau_p^Z tau_n^N` and `tr_atom =
            #      closed_form_tau_M(..., tau_p, tau_n)`, so the ratio is
            #      `prod f_i(q)` — the bond factors b_pp / b_pn / b_nn are
            #      independent of tau. The live law is the log-RATIO stated in
            #      this module's own header, `B = E_0 log(tr_free/tr_atom)`,
            #      implemented in `binding_log_free_energy.py`. It does not
            #      move under the intra ordering, whichever frame these taus
            #      are in. Only `Delta_tr = tr_free - tr_atom` scales with
            #      them, and that is the REFUTED law this file is marked
            #      "do not quote" for.
            #   2. Re-framing a superseded provenance number makes it stop
            #      matching the record it exists to preserve. The 1592x
            #      residual spread in the header was measured against these
            #      values; changing them would leave that measurement
            #      describing numbers no longer in the file.
            def _nucleon_word(g0, g1):
                from pyhecke.atom import grouped_word_from_chains
                return grouped_word_from_chains(g0, g1)
            tau_p = tr_M_via_wenzl_bridge_mpfr(
                _nucleon_word(_PROTON_G0, _PROTON_G1),
                3, Q_50_DIGIT_STR, dps=50,
            )
            tau_n = tr_M_via_wenzl_bridge_mpfr(
                _nucleon_word(_NEUTRON_G0, _NEUTRON_G1),
                3, Q_50_DIGIT_STR, dps=50,
            )
            # `bring_color_weighted` is canonical (owner ruling 2026-08-15,
            # R3). This call was pinned to `strict_averaged`, justified as
            # matching the symbolic path's literal σ - h/2 factor — a circular
            # justification, since that path could not express the weighting
            # (see `_factor_from` above, now fixed).
            #
            # Verified against an independent path rather than assumed: at the
            # deuteron this returned 0.575090871629810316751633 under
            # `strict_averaged`, which is exactly the colour-BLIND value bean
            # `qou-4e5k` identifies as wrong, and returns
            # 0.575172243917771870826535 under the canonical convention, which
            # is exactly that bean's bridge/peel value. Uniform 1.415e-04
            # relative shift across (Z,N) = (1,1), (1,2), (2,1), (2,2), (3,4).
            tr_atom_mp = closed_form_tau_M(
                Z, N, q_val, tau_p, tau_n,
                pn_convention="bring_color_weighted",
            )
            # Free config = no interface factors → just the constit part.
            tr_free_mp = (mp.mpf(tau_p) ** Z) * (mp.mpf(tau_n) ** N)
            dt = time.time() - t0
            # KEEP the mpf. `complex(float(tr_atom_mp), 0.0)` collapsed a
            # value that `closed_form_tau_M` had just computed at 50 dps
            # down to binary64 — ~34 significant digits discarded one line
            # after they were produced, on the path that
            # `mass_table_comprehensive` and `binding_factor_f_*` take.
            # Both traces are real here by construction (Im(q_0) = 0), so
            # there is nothing a `complex` was carrying: the cast bought
            # only the type the legacy symbolic branch below happens to
            # produce. The shared tail is polymorphic over mpf / mpc /
            # complex (`.real` and `.imag` exist on all three), so the two
            # branches no longer have to agree on a type — only on the
            # interface. `binding_factor_f_sequence.py` documents the
            # downstream cost of the collapse at length: a 16-digit
            # `tr_M_*` string is the double 0.98352601518469637…, not the
            # datum.
            tr_atom = tr_atom_mp
            tr_free = tr_free_mp
            atom_n_terms = -1  # not computed in closed-form path
            free_n_terms = -1
            tr_atom_sym = None
            tr_free_sym = None
        except Exception as e:
            return {"status": "closed_form_error", "error": str(e),
                    "Z": Z, "N": N, "A": A}
    else:
        # ── Legacy symbolic path ──────────────────────────────
        atom_elem = build_atom_symbolic(Z, N, include_inter=True,
                                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        free_elem = build_atom_symbolic(Z, N, include_inter=False,
                                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)

        if reduce_before_trace:
            atom_elem, _ = div.reduce(atom_elem, engine='laurent')
            free_elem, _ = div.reduce(free_elem, engine='laurent')

        if verbose:
            print(f"  atom NF: {atom_elem.n_terms()} terms;  "
                  f"free NF: {free_elem.n_terms()} terms")

        t0 = time.time()
        try:
            # `simplify=False`: skip the `sp.simplify` step in tr_M_element.
            # At A=3 the aggregated total has ~5000-12000 sympy ops; calling
            # `simplify` exceeds 30 minutes (³He) while the recursion itself
            # runs in seconds.  Numerical evaluation at q=q₀ (below) is
            # unaffected.  See #508 Phase 2 part 2.
            tr_atom_sym = tr_M_element(atom_elem, n_strands, simplify=False)
            tr_free_sym = tr_M_element(free_elem, n_strands, simplify=False)
        except (NotImplementedError, RecursionError) as e:
            return {"status": "trace_error", "error": str(e),
                    "Z": Z, "N": N, "A": A,
                    "n_atom_terms": atom_elem.n_terms(),
                    "n_free_terms": free_elem.n_terms()}
        dt = time.time() - t0
        atom_n_terms = atom_elem.n_terms()
        free_n_terms = free_elem.n_terms()

        try:
            tr_atom = complex(sp.N(tr_atom_sym.subs(q_sym, q0)))
            tr_free = complex(sp.N(tr_free_sym.subs(q_sym, q0)))
        except Exception as e:
            return {"status": "eval_error", "error": str(e)}

    tr_atom_r = tr_atom.real if abs(tr_atom.imag) < 1e-6 else tr_atom
    tr_free_r = tr_free.real if abs(tr_free.imag) < 1e-6 else tr_free
    # Categorical binding scalar is the SIGNED trace difference
    #   Δtr = tr_M(W_free) − tr_M(W_atom).
    # The double-modulus form |tr_M(W_free)| − |tr_M(W_atom)| was a
    # non-archimedean misuse (per
    # docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md): it
    # applies the archimedean observation `|·|` to each trace BEFORE the
    # difference, which is neither the signed categorical scalar nor the
    # bar-norm `tr_M·\bar{tr_M}`.  The per-mass positivity observation is
    # a no-op here (both traces are real & positive at q_0 ∈ ℝ), so the
    # signed difference IS the archimedean binding — and it correctly
    # preserves the binding/anti-binding SIGN, which the double-modulus
    # form would distort whenever a trace is negative.
    delta_tr = tr_free_r - tr_atom_r                      # signed categorical scalar
    # Archimedean realization at the substrate anchor: Im(q_0) = 0
    # (the `lusztig_q_0_imaginary_part_zero` constraint), so the physical
    # observable is the real part.  `.real` is taken explicitly (not as a
    # silent collapse) and works uniformly for float / Python-complex /
    # mpmath.mpc (the latter does NOT subclass Python `complex`, so an
    # isinstance guard would be fragile — per Gemini review on PR #1738).
    # `Q_beta_n_mev` arrives as a Python float from most callers. Promote it
    # through its DECIMAL repr, not its binary value, when the trace is exact
    # — matching the transfer path's `mp.mpf(str(Q_beta_n_mev))` — so the two
    # exact routes multiply by the same number. On the legacy symbolic route
    # `delta_tr` is genuinely binary64 (`complex(sp.N(...))` upstream), so the
    # product stays a float and `B_MeV` keeps float64's honest 17 digits
    # rather than being dressed in 50 it does not have.
    _exact = isinstance(delta_tr, (mp.mpf, mp.mpc))
    # 🛑 SUPERSEDED: see the module banner. `Q_beta . Delta_tr` is refuted;
    # the live law is E_0 . log(tr_free/tr_atom).
    B = (mp.mpf(str(Q_beta_n_mev)) if _exact else Q_beta_n_mev) * delta_tr.real
    return {
        "status": "solved",
        "Z": Z, "N": N, "A": A,
        "tr_M_atom": str(tr_atom_r),
        "tr_M_free": str(tr_free_r),
        "Q_beta_n_MeV": Q_beta_n_mev,
        # NOT `float(B)`. On the closed-form route this is an mpf carrying the
        # full trace precision; casting it here re-imposed exactly the binary64
        # collapse the branch above stopped doing. `mpf` is drop-in for every
        # reader in the corpus — it does mixed arithmetic with `float`, formats
        # under `f"{B:.4f}"`, and survives `float(...)` — but it is NOT
        # JSON-serializable, so a caller writing it to a witness must route it
        # through `_precision.fmt` (that is a feature: the cast is now visible
        # at the point where precision is actually being given up).
        "B_MeV": B,
        # Companion to B_MeV on this route too: dimensionless, experiment-free.
        "delta_tr_exact": str(delta_tr),
        "n_atom_terms": atom_n_terms,
        "n_free_terms": free_n_terms,
        "use_closed_form": use_closed_form,
    }


def binding_observe_last(Z: int, N: int, *, dps: int = 50):
    """**Observe-LAST binding variant (DIAGNOSTIC — not a production closure).**

    Sibling to `binding_canonical` (observe-EARLY: the step-5 scalar collapse
    `B_pred = Q_β·(tr_free − tr_atom)`).  This variant carries the per-Wedderburn-
    block q-Reeb phase `θ_λ` to a τ-LAST collapse (step 9), per the observe-last
    reframe (`docs/audits/2026-06-17-singlet-channel-bsym-exploration.md` §6b/§6c):

        θ_λ^X = arccos(χ_λ^X/d_λ)        (|·|≤1, rotation channel)
              | arccosh(|χ_λ^X/d_λ|)     (growth channel)
        B_observe_last = Q_β · Σ_λ y_λ (θ_λ^free − θ_λ^atom)        [additive]

    **STATUS (read before consuming).** The additive collapse above is *refuted*
    as the binding-residual mechanism: small, negative, and SHRINKS with A,
    whereas the documented residual `Δ_λ(K)=B_AME/B_pred ≈ q₀^(10A−5)=q₀^(5(2A−1))`
    is large, positive, and GROWS with A.  A bounded additive phase sum cannot be
    geometric in A; the residual is a **per-object multiplicative q₀⁵** (one factor
    per nucleon + one per inter-nucleon bond), whose categorical derivation from
    the `W_free`/`W_atom` jet–crossing bookkeeping is OPEN (9b workplan H1;
    research-grade Subgoal-2 — must NOT be closed by a fit ansatz, Δ_λ gate).
    This function exposes the observe-last *carrier infrastructure* (the per-λ θ
    vector the canonical step-5 trace collapses), NOT a wired binding closure.
    `residual_law_*` is the EMPIRICAL near-match shown for reference only and is
    deliberately NOT applied to produce a binding number.

    NO FLOAT (owner ruling 2026-06-09): all mpmath at the 50-dps floor; values
    returned as full-precision decimal strings.
    """
    import mpmath as mp
    # Monotone -> the O(A) block transfer; non-monotone -> the general-word
    # kernel. The atom word became non-monotone on 2026-09-05 (`7db032fb48`),
    # which the transfer correctly refuses; bean `qou-wdij`.
    from chi_general_word import chi_all_lambda_any
    from wedderburn_jones_markov import y_lambda_at
    from hecke_characters import specht_dim

    if mp.mp.dps < dps:
        mp.mp.dps = dps
    n = 3 * (Z + N)
    A = Z + N
    qb = mp.mpf(str(_Q_BETA_N))
    q0v = mp.mpf(str(q0))

    def _theta(chi, d):
        r = chi / d
        return mp.acos(r) if abs(r) <= 1 else mp.acosh(abs(r))

    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
    chi_atom = chi_all_lambda_any(
        atom_braid_word_3A(Z, N, include_inter=True), n)
    chi_free = chi_all_lambda_any(
        atom_braid_word_3A(Z, N, include_inter=False), n)
    parts = list(y.keys())
    tr_atom = mp.fsum(y[l] * chi_atom.get(l, mp.mpf(0)) for l in parts)
    tr_free = mp.fsum(y[l] * chi_free.get(l, mp.mpf(0)) for l in parts)
    B_pred = qb * (abs(tr_free) - abs(tr_atom))                 # observe-early

    dim = {l: mp.mpf(specht_dim(l)) for l in parts}
    th = {l: (_theta(chi_free.get(l, mp.mpf(0)), dim[l]),
              _theta(chi_atom.get(l, mp.mpf(0)), dim[l])) for l in parts}
    B_late = qb * mp.fsum(y[l] * (th[l][0] - th[l][1]) for l in parts)  # REFUTED

    resid_exp = 5 * (2 * A - 1)            # 10A−5 = per-object (A nucleons + A−1 bonds)
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n,
        "Q_beta_n_MeV": str(qb),
        "B_pred_observe_early_MeV": str(B_pred),
        "B_observe_last_additive_MeV": str(B_late),    # refuted: small/neg/shrinks
        "per_lambda_theta": {str(list(l)): {"theta_free": str(th[l][0]),
                                            "theta_atom": str(th[l][1])}
                             for l in parts},
        "residual_law_exponent_10A_5": resid_exp,      # reference only (NOT applied)
        "residual_law_factor_q0pow": str(q0v ** resid_exp),
        "status": "DIAGNOSTIC: additive observe-last refuted; per-object q₀⁵ "
                  "closure OPEN (held); carrier infra for the 9b H1 derivation. "
                  "NOT a production binding closure.",
    }


if __name__ == "__main__":
    # AME 2020 binding-energy comparison targets, every one read from the
    # vendored AME2020 table via `codata_constants.ame_binding_mev(Z, A)`
    # (validation-only; not CAL inputs).
    #
    # PR #1105 routed the first four through the AME_B_*_MEV_VALIDATION
    # constants after finding the inline tritium value was a typo
    # (8.481821 for 8.481798). The last three stayed as literals and were
    # each ~500 eV off — a larger error than the typo that prompted the
    # first fix:
    #     6Li  31.994526  vs  31.9939872   (-538.8 eV)
    #     7Li  39.244531  vs  39.2450807   (+549.7 eV)
    #     7Be  37.600350  vs  37.6008409   (+490.9 eV)
    # A hand-typed reference value drifts silently; an accessor call cannot.
    # (2026-08-19, alongside the ame-2020-binding-energies witness becoming
    # producer-backed rather than hand-entered.)
    #
    # 2026-11-15 (NO-FLOAT64, raw-float64 gate): the reference value is READ,
    # so it is carried as the AME table's EXACT decimal text
    # (`ame_2020_binding_energies._binding_mev_exact`, a `Decimal`), not as a
    # `float(...)` of the mpf accessor. The two are asserted equal below, so the
    # registry accessor stays the canonical source and this is only its
    # verbatim serialization (a 9-digit measurement must not be printed as if
    # measured to 50 -- see `draining-raw-float64` / `_binding_mev_exact`).
    from decimal import Decimal
    import mpmath as mp
    from ame_2020_binding_energies import _binding_mev_exact
    from _precision import fmt

    def _mass_and_rel_err(A: int, B_pred, B_AME):
        """M_total and |B_pred - B_AME| / M_total in percent, at 60 dps.

        A function rather than an inline `with mp.workdps(60)` inside the atom
        loop: the import-time-dps audit walks one block level of `__main__`, so
        the inline form (already at 60 dps) read as an mpf built at dps 15.
        """
        with mp.workdps(60):
            M_total = A * M_P_MEV_VALIDATION
            return M_total, abs(B_pred - mp.mpf(str(B_AME))) / M_total * 100

    def _ame_exact(Z: int, A: int, accessor_value) -> Decimal:
        d = _binding_mev_exact(Z, A)
        with mp.workdps(60):
            gap = abs(mp.mpf(str(d)) - accessor_value)
            assert gap <= abs(accessor_value) * mp.mpf("1e-45"), (
                f"Z={Z} A={A}: exact AME decimal {d} disagrees with "
                f"codata_constants accessor {accessor_value}")
        return d

    ATOMS = [
        ("D",    1, 1, _ame_exact(1, 2, AME_B_DEUTERON_MEV_VALIDATION)),
        ("T",    1, 2, _ame_exact(1, 3, AME_B_TRITIUM_MEV_VALIDATION)),
        ("3He",  2, 1, _ame_exact(2, 3, AME_B_HE3_MEV_VALIDATION)),
        ("4He",  2, 2, _ame_exact(2, 4, AME_B_HE4_MEV_VALIDATION)),
        ("6Li",  3, 3, _ame_exact(3, 6, ame_binding_mev(3, 6))),
        # A=7 mirror pair — the SECOND proton-excess test after T/³He (the
        # Z-correction slope test, per the 9b workplan). ⁷Be (Z>N) is the
        # proton-rich member; ⁷Li (N>Z) its mirror. AME2020 binding (MeV).
        ("7Li",  3, 4, _ame_exact(3, 7, ame_binding_mev(3, 7))),
        ("7Be",  4, 3, _ame_exact(4, 7, ame_binding_mev(4, 7))),
    ]

    # Q_beta(n) = M_N - M_P - M_E is a difference of three quoted decimals, so
    # it IS a short exact decimal (0.78233340931). `_Q_BETA_N` is that value as a
    # 60-dps mpf; print it at 30 significant digits with zeros stripped, which
    # recovers the decimal text exactly, and assert that it does (a binary tail
    # surviving here would mean the value was NOT a short decimal after all).
    with mp.workdps(60):
        _Q_BETA_N_TEXT = mp.nstr(_Q_BETA_N, 30)
        # 1e-45, not tighter: the registry parses its ~939-MeV inputs at 50 dps,
        # so the difference carries ~3e-50 of input rounding (measured).
        assert abs(mp.mpf(_Q_BETA_N_TEXT) - _Q_BETA_N) <= mp.mpf("1e-45"), (
            _Q_BETA_N_TEXT)
    # The transfer route evaluates every trace at dps=50 (tr_m_atom_zn's
    # default, also how tr_M_atom / tr_M_free / delta_tr_exact are emitted), so
    # B_MeV and Δm/m are serialized at that width -- no wider.
    _TRACE_DPS = 50
    print("=" * 100)
    print("BINDING via CANONICAL Jones-Markov trace "
          "(prop:categorical-mass-markov)")
    print(f"q₀ = {q0}, Q_β(n) = {float(_Q_BETA_N)} MeV (β-decay Q-value, CAL-2 proxy)")
    print("=" * 100)
    results = []
    print(f"  {'Atom':>6} {'A':>3} {'3A':>3} {'B_AME':>8} "
          f"{'|tr_atom|':>12} {'|tr_free|':>12} "
          f"{'B_pred':>10} {'|Δm/m|%':>9} {'time':>8}")
    print("  " + "-" * 96)
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        r = binding_canonical(Z, N, verbose=False)
        if r.get("status") != "solved":
            print(f"  {name:>6} {A:>3} {3*A:>3}  "
                  f"STATUS: {r.get('status')}: "
                  f"{r.get('error', '')[:60]}")
            results.append(r)
            continue
        tr_a = complex(r["tr_M_atom"].replace("(", "").replace(")", ""))
        tr_f = complex(r["tr_M_free"].replace("(", "").replace(")", ""))
        # Proton mass from codata_constants registry (CODATA 2022, full
        # precision); was hardcoded inline as 938.272.
        M_total, dm = _mass_and_rel_err(A, r["B_MeV"], B_AME)
        print(f"  {name:>6} {A:>3} {3*A:>3} {B_AME:>8.3f} "
              f"{abs(tr_a):>12.6e} {abs(tr_f):>12.6e} "
              f"{r['B_MeV']:>+10.4f} {dm:>8.4f}%")
        # Serialized at the witness boundary as decimal STRINGS (2026-11-15,
        # raw-float64 gate). The previous `float(...)` casts here threw away
        # the trace precision; see `precision_note` for why the digits are
        # arithmetic exactness and the experimental uncertainty is a separate,
        # recorded quantity. `wall_sec` is renamed `elapsed_sec` (a timing,
        # excused by the gate only under an elapsed/dur name).
        row = {k: v for k, v in r.items() if k != "wall_sec"}
        if "wall_sec" in r:
            row["elapsed_sec"] = r["wall_sec"]
        row.update({"atom": name,
                    "Q_beta_n_MeV": _Q_BETA_N_TEXT,
                    "B_MeV": fmt(r["B_MeV"], dps=_TRACE_DPS),
                    "B_AME_MeV": str(B_AME),
                    "delta_m_over_m_pct": fmt(dm, dps=_TRACE_DPS)})
        results.append(row)

    # Coerce sympy/mpmath fragments to JSON-serialisable types so
    # WitnessBuilder.save() (which does strict json.dumps) succeeds.
    #
    # B_MeV is an `mpf` in the returned dict on purpose (see the notes at both
    # return sites); it is serialized above, at the witness boundary, through
    # `fmt` at the trace width. `default=str` below is only a safety net for
    # the remaining sympy/mpmath fragments (the tr_M strings are already str).
    safe_results = json.loads(json.dumps(results, default=str))
    builder = (
        WitnessBuilder("binding-canonical", engine="sympy+mpmath")
        .set_description(
            "Atom binding via the canonical Jones-Markov trace "
            "(Direction 1 of validity audit): matches the prop's "
            "explicit-values table tr_M(σ_0)=z, tr_M(σ_0σ_1)=z², "
            "tr_M(σ_0σ_1σ_0)=hz²+z. Replaces the Plancherel-"
            "weighted trace used in binding_3A and "
            "atom_markov_trace. Binding = Q_β(n)·(tr_M_free − "
            f"tr_M_atom) [SIGNED categorical difference; the double-"
            f"modulus |·|−|·| was a non-archimedean misuse] with "
            f"Q_β(n) = {float(_Q_BETA_N):.8f} MeV (free-"
            "neutron β-decay Q-value, the CAL-2 proxy — NOT CAL-3, "
            "which is P_avg^π; Q_β is a scored prediction, not an input — "
            "NOT the canonical E_0 = m_e/(q_0(q_0-1)) ≈ 4.186 MeV). "
            "DIAGNOSTIC ONLY: predicted B values are 5–40× smaller "
            "than AME because Q_β is the wrong energy scale; the "
            "primary canonical mass-prediction pipeline is "
            "canonical-mass-table-extended.witness.json. This "
            "witness is retained for the Direction 1 validity "
            "audit of the Jones-Markov trace itself."
        )
        .set_audit_only("docs/audits/categorical-vs-fitted-q-decay-ba.md")
        .add_parameter("q0", q0)
        .add_parameter("Q_beta_n_MeV", _Q_BETA_N_TEXT)
        .add_parameter("precision_note", "Two different precisions, kept apart. ARITHMETIC: Q_beta_n_MeV is the exact decimal M_N - M_P - M_E of the quoted CODATA-2022 / AME inputs; B_MeV = Q_beta_n_MeV * delta_tr is that decimal times the 50-dps trace difference, serialized at 50 significant digits, every one determined by those inputs. B_AME_MeV is the AME2020 table's own decimal text, verbatim. delta_m_over_m_pct is computed from these and serialized at 50 digits. EXPERIMENT: Q_beta(n) carries a CODATA uncertainty of 6.664e-07 MeV (8.518e-07 relative), so B_MeV as a PHYSICAL prediction is meaningful only to ~6 significant figures; the extra digits are not a claim of measurement, they are what the arithmetic gives for the quoted inputs. Q_beta cancels in any ratio B(a)/B(b) = delta_tr(a)/delta_tr(b), so ratio consumers should read delta_tr_exact, which has no experimental input at all.")
        .add_data("results", safe_results)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
