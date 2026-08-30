#!/usr/bin/env python3
"""The 2026-05-19 TR_M[5] Markov-trace fix never reached `computations/` — five
live producers still carry `z**3`, and the wrong value MASKS the D-frame Gram
singularity.

`docs/audits/2026-05-19-trm5-markov-bug.md` corrected
`tools/pyhecke/python/pyhecke/gram.py`: on the Grobner-Shirshov normal-form
basis of H_3(q), the sixth weight is

    tr_M(sigma_0 sigma_1 sigma_0) = h*z^2 + z ,   h = q - 1/q

and NOT `z^3`. The derivation is three lines of the Markov axioms and is
reproduced in check 1 below. `pyhecke.gram.TR_M` carries the fix. Five
`computations/` producers on the SAME basis do not.

## Why this is not a cosmetic drift

The wrong weight is off by a factor of ~3 at the proton anchor under D, and
~4.4 under C -- not a precision issue, a different number.

More consequential: `pyhecke/gram.py`'s own banner records that the crate's
Rust mirror kept `z*z*z` and notes exactly what that buys --

    "This is what keeps the crate's Gram non-singular, so it has no radical
     and no quotient -- hence the trace fix and the quotient must land
     together (fixing the trace alone drops a singular Gram into a path with
     nothing to handle it)."

Check 3 below measures that on a live producer. `compound_shift_nf.gram_mp`
builds G[i][j] = tr_M(b_i b_j) and feeds it to an LP. With the committed
`z^3` it is rank 6 under BOTH conventions, so the file looks like a clean
z-swap candidate. With the CORRECT weight it is rank 6 under C and **rank 5
under D** -- the singularity that bean qou-cds2 tracks. The trace bug is
what hides it.

Check 4 is the cross-check that ties the two files together: with the correct
weight under C, `compound_shift_nf`'s determinant equals
`gram_h3_det_factorization`'s in magnitude to every digit. They are the same
Gram; they disagreed only because one carries the bug.

## Scope

This is a scope-(a) finding about five named files, not a claim that every
`z**3` in the corpus is wrong -- `z^3` is the correct weight for other
objects, and 14 further hits live under `computations/_deprecated/` and are
out of scope. Each site below was confirmed to use the SAME six-element NF
basis `[(), (0,), (1,), (0,1), (1,0), (0,1,0)]` before being listed.

Run:  PYTHONPATH=computations python3 -u computations/probes/trm5_zcubed_live_producer_audit.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from q_parameter import q_at  # noqa: E402 — proton pin (stem not in ideal_muon)
from witness_base import WitnessBuilder  # noqa: E402

#: (file, line, symbol) -- confirmed on the same NF basis, live (not _deprecated).
LIVE_SITES = [
    ("computations/compound_shift_nf.py", 257, "tr_m_weights_mp"),
    ("computations/electron_sigma_f_chain.py", 107, "TR_M"),
    ("computations/jet_knot_invariants.py", 56, "tr_basis"),
    ("computations/atom_mass_derived.py", 102, "TR_M_3"),
    ("computations/basis_knot_tables.py", 54, "TR_M"),
]

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]


def check1_derivation() -> dict:
    """The Markov axioms give h*z^2 + z, symbolically, with z free."""
    q, z = sp.symbols("q z")
    h = q - 1 / q
    # tr(s0 s1 s0) = tr(s1 s0^2)          [cyclicity]
    #              = tr(s1 (h s0 + 1))    [Hecke: s^2 = h s + 1]
    #              = h tr(s1 s0) + tr(s1)
    #              = h z^2 + z            [Markov: tr(s_i x) = z tr(x)]
    derived = sp.expand(h * z**2 + z)
    return {
        "derived_symbolic": str(derived),
        "equals_z_cubed": bool(sp.simplify(derived - z**3) == 0),
        "difference": str(sp.simplify(sp.factor(z**3 - derived))),
    }


def check2_magnitude(q0) -> dict:
    h = q0 - 1 / q0
    out = {}
    for name, zv in (("C", 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))),
                     ("D", q0**3 / (q0**2 + 1))):
        wrong, right = zv**3, h * zv**2 + zv
        out[name] = {
            "z": mp.nstr(zv, 20),
            "committed_z_cubed": mp.nstr(wrong, 20),
            "correct_h_z2_plus_z": mp.nstr(right, 20),
            "correct_over_committed": mp.nstr(right / wrong, 12),
            "committed_rel_error_pct": mp.nstr((wrong - right) / right * 100, 10),
        }
    return out


def check3_gram_rank(q0) -> dict:
    """The trace bug masks the D Gram singularity in a LIVE producer."""
    import compound_shift_nf as C
    h = q0 - 1 / q0
    zs = {"C": 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0)), "D": q0**3 / (q0**2 + 1)}
    orig = C.tr_m_weights_mp
    rows = {}
    try:
        for zn, zv in zs.items():
            for fixed in (False, True):
                w = [mp.mpf(1), zv, zv, zv**2, zv**2,
                     (h * zv**2 + zv) if fixed else zv**3]
                C.tr_m_weights_mp = lambda dps=50, _w=w: list(_w)
                G = C.gram_mp(50)
                M = mp.matrix([[G[i, j] for j in range(6)] for i in range(6)])
                sv = mp.svd_r(M, compute_uv=False)
                rank = sum(1 for s in sv if abs(s) > mp.mpf(10) ** -30)
                key = f"z_{zn}/{'correct' if fixed else 'committed'}"
                rows[key] = {
                    "det": mp.nstr(mp.det(M), 12),
                    "rank": rank,
                    "min_singular_value": mp.nstr(min(abs(s) for s in sv), 6),
                }
    finally:
        C.tr_m_weights_mp = orig
    return rows


def check4_same_gram(ranks: dict) -> dict:
    """With the CORRECT weight under C, compound_shift_nf's |det| matches the
    independent gram_h3_det_factorization value -- so they are one Gram."""
    u, qs = sp.symbols("u q", positive=True)
    det_u = (-(u - 1) * (u + 1) * (u**3 + u - 1) ** 5 * (u**3 + u**2 + 1) ** 5
             * (u**6 - u**5 + u**4 - u**3 + 2 * u**2 - u + 1)
             * (u**6 + u**5 + 2 * u**4 + u**3 + u**2 + u + 1)
             / (u**10 * (u**2 + 1) ** 12))
    q0s = sp.Float(str(q_at(40)), 40)
    indep = sp.N(det_u.subs(u, sp.sqrt(q0s)), 20)
    mine = mp.mpf(ranks["z_C/correct"]["det"])
    return {
        "gram_h3_det_factorization_at_q0": str(indep),
        "compound_shift_nf_correct_weight_at_q0": mp.nstr(mine, 12),
        "magnitudes_agree": bool(abs(abs(mp.mpf(str(indep))) - abs(mine))
                                 < mp.mpf(10) ** -9),
        "note": ("sign differs by a basis-ordering orientation; the magnitude "
                 "identity is the claim"),
    }


def main() -> int:
    mp.mp.dps = 60
    q0 = q_at(55)

    c1 = check1_derivation()
    c2 = check2_magnitude(q0)
    c3 = check3_gram_rank(q0)
    c4 = check4_same_gram(c3)

    # REGRESSION GUARD, not a live-site scan.
    #
    # This probe was written to ESTABLISH the finding, while all five sites
    # still carried z^3. They were fixed later in the same PR, at which point
    # reading `text[line - 1]` started returning the FIXED lines (and, once
    # explanatory comments shifted the files, unrelated lines entirely) while
    # the payload still said "live sites still on z^3". The witness contradicted
    # itself. Caught when a rebase re-ran the probe.
    #
    # So it now checks what is actually worth checking going forward: that each
    # file carries the CORRECT weight and no longer carries the bug. Keyed on
    # content, not line numbers, so it cannot rot the same way twice.
    sites = []
    repo = HERE.parent.parent
    all_fixed = True
    for path, line, sym in LIVE_SITES:
        text = (repo / path).read_text()
        # the bug: a six-element trace vector ending in a cube of z
        has_bug = any(
            pat in text.replace(" ", "")
            for pat in ("z**2,z**2,z**3", "z*z,z*z,z**3", "z**2,z**2,z**3]")
        )
        has_fix = any(
            pat in text.replace(" ", "")
            for pat in ("h*z**2+z", "h*z*z+z", "h_trm*z**2+z", "_h_trm*z**2+z")
        )
        all_fixed = all_fixed and has_fix and not has_bug
        sites.append({
            "file": path, "symbol": sym,
            "historical_line": line,
            "still_carries_z_cubed": has_bug,
            "carries_h_z2_plus_z": has_fix,
        })

    payload = {
        "description": (
            "The 2026-05-19 TR_M[5] fix (h*z^2 + z, NOT z^3) reached "
            "pyhecke/gram.py and never reached computations/. Five live "
            "producers on the same H_3 NF basis still carry z^3, and the "
            "wrong weight masks the convention-D Gram singularity."
        ),
        "nf_basis": [list(b) for b in NF_BASIS],
        "regression_guard": {
            "note": ("These five carried TR_M[5] = z^3 when this probe was "
                     "written; all five are fixed in the same PR. The check is "
                     "now that the fix HOLDS, keyed on content rather than line "
                     "numbers — the line-keyed version contradicted its own "
                     "payload as soon as the fix landed."),
            "all_five_fixed": all_fixed,
            "sites": sites,
        },
        "check1_markov_derivation": c1,
        "check2_magnitude_at_q0": c2,
        "check3_gram_rank_live_producer": c3,
        "check4_same_gram_as_gram_h3": c4,
        "sequencing_constraint": (
            "pyhecke/gram.py records that the trace fix and the Gram quotient "
            "must land together: fixing the trace alone drops a singular Gram "
            "into a path with nothing to handle it. Check 3 measures exactly "
            "that on compound_shift_nf."
        ),
        "context": {
            "prior_audit": "docs/audits/2026-05-19-trm5-markov-bug.md",
            "beans": ["qou-t9r1", "qou-pmkh", "qou-cds2"],
            "scope": ("(a) scope-limited -- five named files on one basis; not "
                      "a claim about every z**3 in the corpus"),
        },
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    # bean qou-srvu. This audit's own payload calls `all_five_fixed` a
    # REGRESSION GUARD -- "the check is now that the fix HOLDS" -- and check 1
    # is the symbolic derivation the whole audit rests on. Neither reached
    # `assertions[]`, so `save()` emitted `allPassed: true` over an EMPTY list:
    # a regression guard that could not report a regression. No claim is
    # invented and no threshold is chosen here: check 1 is exact sympy
    # (`sp.simplify(derived - z**3) == 0`), and check 4's 1e-9 is the constant
    # already at its own call site, compared at 40 dps -- not float64.
    _b = WitnessBuilder.wrap_legacy(
        "trm5-zcubed-live-producer-audit", payload,
        script_path=__file__, engine="python+mpmath+sympy",
    )
    _b.add_assertion(
        "regression_guard_all_five_fixed", computed=bool(all_fixed),
        expected=True,
        source=("each of the five live producers carries TR_M[5] = h*z^2 + z "
                "and no longer carries z^3. Keyed on file content, not line "
                "numbers"))
    _b.add_assertion(
        "markov_derivation_is_NOT_z_cubed",
        computed=bool(c1["equals_z_cubed"]), expected=False,
        source=("the Markov axioms give tr(s0 s1 s0) = h*z^2 + z symbolically "
                "with z free; it is NOT z^3. This is the audit's premise, "
                "proved by exact sympy simplification, not numerically"))
    _b.add_assertion(
        "same_gram_as_gram_h3",
        computed=bool(c4["magnitudes_agree"]), expected=True,
        source=("with the correct weight, compound_shift_nf's |det| matches "
                "the independent gram_h3_det_factorization value at q0 to the "
                "1e-9 already declared at that call site (40 dps; sign differs "
                "by a basis-ordering orientation, so magnitude is the claim)"))
    out = _b.save()

    print("=== TR_M[5]: the 2026-05-19 fix never reached computations/ ===")
    print(f"  CHECK 1  Markov axioms give     : {c1['derived_symbolic']}")
    print(f"           equals z^3?            : {c1['equals_z_cubed']}   "
          f"(difference {c1['difference']})")
    for k, v in c2.items():
        print(f"  CHECK 2  z_{k}: committed {v['committed_z_cubed'][:12]}  "
              f"correct {v['correct_h_z2_plus_z'][:12]}  "
              f"off by {v['committed_rel_error_pct'][:8]}%")
    print("  CHECK 3  compound_shift_nf Gram (LIVE producer):")
    for k, v in c3.items():
        print(f"           {k:22s} det {v['det']:>16}  rank {v['rank']}/6")
    print(f"  CHECK 4  same Gram as gram_h3?  : {c4['magnitudes_agree']}")
    print(f"  REGRESSION GUARD — all five fixed : {all_fixed}")
    for st in sites:
        flag = "BUG" if st["still_carries_z_cubed"] else ("ok" if st["carries_h_z2_plus_z"] else "??")
        print(f"           [{flag}] {st['file']}  {st['symbol']}")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
