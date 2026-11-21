#!/usr/bin/env python3
"""Algebraic (q-parameterized) Markov trace  tr_M(q) ∈ ℚ(q).

Resolves the "B_sym is really B_arch — the algebraic object is missing"
observation. The production atom braid word (`atom_braid_word_3A`) bakes the
colour split `flavor_split_leading(q₀)` **numerically** into the p-n
interface crossing, so the symbolic trace via `build_atom_symbolic` carries an
ugly numerical fraction (e.g. `104458189399543/16000000000000000`) instead of a
clean Laurent object. This module keeps the colour δ **symbolic** (its closed
form in q), giving the genuine algebraic trace `tr_M(q) ∈ ℚ(q)` whose
archimedean realization at the substrate q₀ — `B_sym = E₀·ln(tr_free/tr_atom)` —
is what the mass-binding dashboard reports as the (archimedean) `B_sym`.

The atom word uses only:
  * intra-nucleon crossings  c = 1, d ∈ {0, −h/2, −h}   (h = q − q⁻¹)
  * p-p interface  (1, 0) · n-n interface  (1, −h)
  * p-n interface  (1, −h·(½ − δ(q)/4)),  δ(q) = flavor_split_leading(q)
so every factor is `σ_g + d·I` with d a symbolic element of ℚ(q): no q₀ bake.

Verified (see __main__ / witness): `tr_M_algebraic(Z,N).subs(q, q₀)` reproduces
the canonical transfer value `tr_m_atom_zn(Z,N)` to ~1e-50 for D/T —
the algebra is exact and is now evaluated as an exact rational at the 70-digit
q₀. (Until 2026-11-21 q₀ entered as float(Q) and the residual was the ~1e-13
float64 cancellation floor of the degree-O(100) rational.)

THE "~1e-8" IN THE LINE ABOVE USED TO READ AS THE FLOOR, AND IT WAS THE
GROUPED ORDERING (bean `qou-4383`). `build_atom_symbolic_q` laid its intra
letters down as all of `_PROTON_G0` then all of `_PROTON_G1` — which is
*exactly* how `pyhecke.atom.nucleon_word_letters` defines `intra_order=
"grouped"`, since those two constants are the canonical letters **bucketed by
generator** and, as `mass_at_3A_proper` says at its own definition, "cannot
express the interleaving". So the mirror was structurally incapable of the
canonical borromean word no matter what values it read. The deuteron sat
4.23e-01 from the transfer and the witness had been recording that, with
`allPassed: false`, since 2026-09-07. Under `nucleon_word_letters` it closes
to 8.9e-14, so the real evaluation floor is ~5 orders below the old claim —
and the old claim was never a floor at all, it was an ordering defect from an
era when the transfer was grouped too and the two agreed.

This is a generic-q builder ("at least for q like q₀"): pass any `q` (a sympy
Symbol for the full ℚ(q) form, or a numeric value to evaluate there). A true
q-SWEEP of the *observable* still needs Im(q₀)=0 at the archimedean wall — this
module gives the fibre-level algebraic object, not an archimedean continuation.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))


def flavor_split_leading_sym(q):
    """Symbolic `flavor_split_leading(q)` (colour δ):

        δ(q) = (q−1)²(1−q⁻⁴)/3

    This is the LEADING term alone, which is what
    `_li_2_q_util.flavor_split_leading` computes and what
    `canonical_braid_crossings._avg_color_delta` — the source of the numeric
    colour-weighted crossing — carries.

    IT USED TO MULTIPLY BY THE POSITED SUBLEADING (1 + ℏ³), while its docstring
    claimed it matched `_li_2_q_util.flavor_split_leading` "at any q".  It did
    not: the two disagreed by exactly ℏ³ = 9.727037e-04 relative at q_0.  Per
    AGENTS.md the leading term is the proven one and `(1 + ℏ³)` is the *posited*
    subleading correction, carried separately as
    `_li_2_q_util.flavor_split_subleading`; conflating them here silently gave
    every consumer the posited quantity under the proven one's name.

    Measured cost, deuteron `tr_M`: `build_atom_symbolic_q` sat 7.92e-08 from
    the bridge/peel value, and `atom_nf_symbolic_D` (which this now feeds
    correctly) closes to 3.44e-25.  The repo's own witness recorded the
    collision — `tr-m-algebraic-q.witness.json` has carried
    `symbolic_delta_matches_li2q  computed=1.338e-06  tol=1e-12  passed=False`
    since 2026-08-09, with `allPassed: false`, and nothing read it.  Bean
    `qou-4e5k`.

    Callers wanting the subleading form should compose it explicitly rather
    than reintroduce it here.
    """
    return (q - 1) ** 2 * (1 - q ** (-4)) / sp.Integer(3)


def build_atom_symbolic_q(Z: int, N: int, q=None, *, include_inter: bool = True,
                          reduce_every: int = 4, intra_order: str | None = None):
    """q-parameterized atom braid as a reduced `SymbolicHeckeElement`.

    Mirrors `mass_at_3A_proper.atom_braid_word_3A` (canonical
    `bring_color_weighted` convention) but emits symbolic `d` — intra crossings
    mapped by value to {0, −h/2, −h}, interfaces built by TYPE so the p-n colour
    δ stays symbolic (it is numerically indistinguishable from −h/2, so it must
    be placed structurally, not matched).

    `intra_order` defaults to whatever `atom_braid_word_3A` declares canonical,
    read off its signature rather than restated here, so this mirror tracks the
    frame instead of pinning a second copy of it. Pass `"grouped"` only to
    reproduce the legacy word (the falsification leg in `__main__` does).

    THE INTRA LETTERS COME FROM `nucleon_word_letters`, NOT FROM
    `_PROTON_G0`/`_PROTON_G1`. Writing all of `g0` and then all of `g1` — which
    is what this function did until bean `qou-4383` — is not an ordering choice
    that happens to be wrong; it is the *definition* of `intra_order="grouped"`
    in `pyhecke.atom`, so no value fed into that loop shape could have produced
    the canonical word. σ₀ and σ₁ are adjacent and do not commute: the two
    orderings are different elements of H₃(q) whose |tr_M| differ by ~82 % at
    one proton. Any other consumer of those two constants that assembles a word
    by concatenating them has the same defect by construction; the mechanical
    detector is `audits/intra_ordering_structural_assembly_audit.py`.
    """
    from q_parameter import HA as _h_num
    from hecke_symbolic import SymbolicHeckeDivision, SymbolicHeckeElement
    from pyhecke.atom import nucleon_word_letters

    if intra_order is None:
        from canonical_trm_reference import _canonical_ordering
        intra_order = _canonical_ordering()
    if q is None:
        q = sp.Symbol("q", positive=True)
    h = q - 1 / q
    delta = flavor_split_leading_sym(q)
    h_num = float(_h_num)

    def _intra_d(dn: float):
        if abs(dn) < 1e-9:
            return sp.Integer(0)
        if abs(dn + h_num) < 1e-5:
            return -h
        if abs(dn + h_num / 2) < 1e-5:
            return -h / 2
        raise ValueError(f"unmapped intra crossing d={dn} (not in 0,−h/2,−h)")

    A = Z + N
    ordering = ["p"] * Z + ["n"] * N
    factors: list[tuple] = []
    for k, nuc in enumerate(ordering):
        quarks = ["u", "u", "d"] if nuc == "p" else ["u", "d", "d"]
        for _c, d, off in nucleon_word_letters(quarks, intra_order=intra_order):
            factors.append((_intra_d(float(d)), 3 * k + off))
        if include_inter and k < A - 1:
            nxt = ordering[k + 1]
            if nuc == "p" and nxt == "p":
                dd = sp.Integer(0)                              # p-p: σ
            elif nuc == "n" and nxt == "n":
                dd = -h                                         # n-n: σ − h·I
            else:
                dd = -h * (sp.Rational(1, 2) - delta / 4)       # p-n: colour δ symbolic
            factors.append((dd, 3 * k + 2))

    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since = 0
    for d, g in factors:
        elem = elem * SymbolicHeckeElement({(g,): sp.Integer(1), (): d})
        since += 1
        if since >= reduce_every:
            elem, _ = div.reduce(elem, engine="laurent")
            since = 0
    if since:
        elem, _ = div.reduce(elem, engine="laurent")
    return elem


def tr_M_algebraic(Z: int, N: int, q=None, *, include_inter: bool = True,
                   intra_order: str | None = None):
    """Algebraic Markov trace `tr_M(q) ∈ ℚ(q)` of the (Z,N) atom braid."""
    from markov_trace_canonical import tr_M_element
    if q is None:
        q = sp.Symbol("q", positive=True)
    elem = build_atom_symbolic_q(Z, N, q, include_inter=include_inter,
                                 intra_order=intra_order)
    return sp.expand(tr_M_element(elem, 3 * (Z + N), simplify=False))


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true",
                    help="also cross-check ³He (n=9, slower symbolic trace)")
    args = ap.parse_args()

    from q_parameter import Q as Q0
    from tr_m_atom_via_transfer import tr_m_atom_zn
    try:
        from witness_base import WitnessBuilder
    except Exception:
        WitnessBuilder = None

    from canonical_trm_reference import _canonical_ordering
    frame = _canonical_ordering()

    import mpmath as mp
    from q_parameter import Q_50_DIGIT_STR, Q_MP
    from _precision import set_compute_dps, fmt
    set_compute_dps()

    q = sp.Symbol("q", positive=True)
    # Evaluate the exact ℚ(q) form at q₀ as an exact rational, then convert at
    # full precision. Until 2026-11-21 this read `q0 = float(Q0)`, so the
    # cross-check below resolved only to the float64 cancellation floor
    # (~1e-13) of a degree-O(100) rational, not to the 50-dps transfer it is
    # compared with (f64_into_mpmath_audit, F64_CAST).
    q0 = sp.Rational(Q_50_DIGIT_STR)

    def _at_q0(expr):
        return mp.mpf(str(sp.sympify(expr.subs(q, q0)).evalf(mp.mp.dps)))
    atoms = [("D", 1, 1), ("T", 1, 2)] + ([("3He", 2, 1)] if args.full else [])

    rows = []
    print(f"algebraic tr_M(q) ∈ ℚ(q)  — q₀ cross-check vs transfer  (q₀={float(q0):.6f})")
    print(f"  intra-nucleon ordering frame: {frame}")
    for nm, Z, N in atoms:
        ta_q = tr_M_algebraic(Z, N, q, include_inter=True)
        tf_q = tr_M_algebraic(Z, N, q, include_inter=False)
        ta0, tf0 = _at_q0(ta_q), _at_q0(tf_q)
        ta_ref, tf_ref, _, _ = tr_m_atom_zn(Z, N, dps=50)
        ta_ref, tf_ref = mp.mpf(ta_ref), mp.mpf(tf_ref)
        d_atom, d_free = abs(ta0 - ta_ref), abs(tf0 - tf_ref)
        rows.append({"atom": nm, "Z": Z, "N": N,
                     "tr_atom_q0_algebraic": fmt(ta0), "tr_atom_transfer": fmt(ta_ref),
                     "tr_free_q0_algebraic": fmt(tf0), "tr_free_transfer": fmt(tf_ref),
                     "abs_diff_atom": fmt(d_atom), "abs_diff_free": fmt(d_free)})
        diffs_atom_free = (d_atom, d_free)
        rows[-1]["_d"] = diffs_atom_free
        print(f"  {nm:>4}: tr_atom {float(ta0):.9f} vs {float(ta_ref):.9f} (Δ={mp.nstr(d_atom, 3)})  "
              f"tr_free {float(tf0):.9f} vs {float(tf_ref):.9f} (Δ={mp.nstr(d_free, 3)})")

    # δ symbolic matches the production helper at q0
    from _li_2_q_util import flavor_split_leading
    d_delta = abs(_at_q0(flavor_split_leading_sym(q))
                  - mp.mpf(flavor_split_leading(Q_MP)))
    print(f"  δ(q₀): symbolic vs _li_2_q_util  Δ={mp.nstr(d_delta, 3)}")

    # FALSIFICATION: the legacy grouped word must NOT reproduce the transfer.
    # Without this leg the check above passes for two reasons that look alike —
    # the mirror is in the canonical ordering, or the ordering does not matter
    # here — and only the first is true. It matters by 4.2e-01 at the deuteron
    # (bean `qou-4383`); the assertion is a floor, not a tolerance, so a future
    # regression back to the `_PROTON_G0`+`_PROTON_G1` concatenation fails here
    # instead of quietly re-widening the match test.
    gz, gn = atoms[0][1], atoms[0][2]
    g_atom = _at_q0(tr_M_algebraic(gz, gn, q, include_inter=True,
                                   intra_order="grouped"))
    _ta_ref = mp.mpf(rows[0]["tr_atom_transfer"])
    grouped_gap = abs(g_atom - _ta_ref)
    print(f"  falsification: grouped {atoms[0][0]} tr_atom {float(g_atom):.9f} "
          f"vs transfer {float(_ta_ref):.9f} (Δ={mp.nstr(grouped_gap, 3)}, must be ≫ 0)")

    if WitnessBuilder is not None:
        w = WitnessBuilder("tr-m-algebraic-q", engine="sympy")
        w.set_description(
            "Algebraic q-parameterized Markov trace tr_M(q) ∈ ℚ(q): the atom "
            "braid word with the colour split flavor_split_leading(q) kept "
            "SYMBOLIC (vs the production q₀-baked float), so the trace is a clean "
            "Laurent object. Cross-checked: tr_M_algebraic(Z,N).subs(q,q₀) == the "
            "canonical transfer value tr_m_atom_zn(Z,N) to ~1e-50 for D/T(/³He) "
            "(exact-rational evaluation at the 70-digit q₀ vs the 50-dps "
            "transfer; ~1e-13 before 2026-11-21, a float64 floor), in the canonical "
            "intra-nucleon ordering, with the legacy grouped word carried as an "
            "explicit falsification."
        )
        w.add_parameter("q0", fmt(Q_MP))
        w.add_parameter("intra_ordering_frame", frame)
        w.add_data("intra_ordering_frame", frame)
        worst = max(d for r in rows for d in r.pop("_d"))
        w.add_data("rows", rows)
        w.add_assertion(name="algebraic_q0_matches_transfer",
                        computed=worst, expected=mp.mpf(0), tolerance=mp.mpf("1e-9"),
                        source="max |tr_M_algebraic(q₀) − tr_m_atom_zn| over D/T(/³He), "
                               "atom & free words")
        # TOLERANCE WAS 1e-7, AND ITS `source` EXPLAINED AWAY A REAL DEFECT.
        # It read "~1e-8 float64-eval floor of the exact ℚ(q) form vs the
        # 50-dps transfer", and the committed value was 6.88e-08 — 69% of a
        # budget sized to accommodate it. That residual was NOT an evaluation
        # floor: it was `flavor_split_leading_sym` carrying the posited
        # (1 + ℏ³) (see its docstring). With δ corrected the deuteron closes to
        # 3.44e-25, so the "floor" was ~17 orders above the real one. The
        # sibling assertion `symbolic_delta_matches_li2q` had been reporting
        # exactly this since 2026-08-09 at tol 1e-12, failing, unread. A
        # tolerance chosen to fit an unexplained gap converts a detector into a
        # rationalisation. Bean `qou-4e5k`.
        w.add_assertion(name="symbolic_delta_matches_li2q",
                        computed=d_delta, expected=mp.mpf(0), tolerance=mp.mpf("1e-12"),
                        source="flavor_split_leading_sym(q₀) vs _li_2_q_util")
        # THE TOLERANCE ABOVE STAYS AT 1e-9 THOUGH THE MEASUREMENT IS ~1e-50.
        # (It was ~1e-13 until 2026-11-21, when q₀ entered as float(Q); the
        # evaluation is now exact-rational, so the float64 rationale below is
        # history and the 1e-9 is a loose bound, not a fitted one.)
        # That is deliberate and is not the mistake the comment above records:
        # 1e-9 is derived (catastrophic cancellation evaluating a degree-O(100)
        # rational in float64 at q₀ ≈ 1.11, with headroom for the larger atoms),
        # not reverse-engineered from a residual nobody could account for. What
        # guards the ORDERING is the falsification leg below, which fails on a
        # regression the match test alone would keep passing.
        w.add_assertion(
            name="grouped_ordering_is_falsified",
            computed=mp.mpf(1) if grouped_gap > mp.mpf("1e-3") else mp.mpf(0),
            expected=mp.mpf(1), tolerance=mp.mpf(0),
            source=f"|tr_M_algebraic({atoms[0][0]}, grouped) − transfer| = "
                   f"{mp.nstr(grouped_gap, 7)} must exceed 1e-3; the two intra-nucleon "
                   f"orderings are different elements of H_3(q) (bean qou-hu1f)")
        out = w.save()
        print(f"  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
