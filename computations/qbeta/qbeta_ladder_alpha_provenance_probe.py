#!/usr/bin/env python3
"""qbeta_ladder_alpha_provenance_probe.py — where does the ladder's phase
`alpha = (z-1)h/2` actually come from?

WHY THIS PROBE. `qou-cds1` must re-derive the Q_beta `c_k` ladder under
convention D. The prior arc worked INSIDE the form: given
`cos(alpha - u/2)` with `alpha = (z-1)h/2`, which `z` satisfies both the
value and the slope constraint? That search is exhausted
(`qbeta_ladder_alpha_form_filter_probe.py`,
`docs/audits/2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md`),
and its own scope note says the form "must change".

Nobody had asked the prior question: **what derives the form?** The corpus
answers with one citation. The precision-ladder block says

    alpha = (z-1)h/2 is the single-wrap eigenphase on V_(2,1)
    (per conj:q-beta-spectral-bridge)

so this probe reads that source and measures whether it supports the use.

WHAT IT FINDS (scope (a) throughout -- see SCOPE below).

  1. The cited source mentions NO eigenphase, NO V_(2,1), and no phase at
     all. Zero occurrences across its .md, its .lean and its proof block.
  2. In that source `(z-1)h/2` is the FIRST-ORDER COEFFICIENT OF A
     MULTIPLICATIVE RATIO between two forms of the same observable:
         Q_A / Q_B = (1 - h/2)/(1 - zh/2) = 1 + (z-1)h/2 + O(h^2).
     The ladder instead uses the same expression as an ANGLE inside a
     cosine. A ratio coefficient and an angle are different objects.
  3. Measured, that difference is NOT small: the ladder's factor
     `cos(alpha - u/2)` and the bridge's own factor `1 + alpha` differ by
     ~5.4 % (C) / ~4.1 % (D) at the substrate anchor -- in a ladder whose
     later rungs chase ppb.
  4. And no small correction reconciles them: the `delta` solving
     `cos(alpha - delta) = 1 + alpha` is ~-0.38 (C) / ~-0.33 (D) against
     the ladder's actual `u/2 = 0.00426` -- off by ~89x / ~77x AND
     opposite in sign.
  5. Incidentally: `markovZ` in the cited Lean was migrated to D on
     2026-08-26 (`qou-cxjq`) while its own docstring and the .md
     proposition still define z as C. A live doc-vs-body divergence at
     the load-bearing definition.

CONSEQUENCE FOR qou-cds1. "Re-derive under D" cannot mean "recompute
alpha at z_D", because alpha's provenance does not survive inspection in
EITHER convention. The D work must SUPPLY a phase, not convert one. This
also explains why the two-row filter came up empty: it searched for a `z`
inside a form that has no derivation behind it.

SCOPE (a), per AGENTS.md "Before declaring refuted". This measures whether
the CITED ATTRIBUTION supports the ladder's phase term. It does NOT claim
no phase term is derivable, does NOT claim the bridge proposition is
wrong, and does NOT bear on the ladder's numerical performance. The
charitable reading -- that the bridge is cited only for alpha's VALUE and
not its role -- is addressed by assertion 4: the same real number in two
structurally different roles is not a derivation, and no small delta
reconciles the roles.

PRECISION. mpmath end to end at 50 dps, q0 from `q_at(dps)` (proton pin,
the standing default); sympy for the symbolic part. No float64 anywhere.

Bean: qou-cds1.
"""
from __future__ import annotations

import json
import pathlib as _pl
import re
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import sympy as sp                                            # noqa: E402
from mpmath import mp                                         # noqa: E402

from q_parameter import q_at                                  # noqa: E402

DPS = 50
REPO = _COMP.parent
BRIDGE = REPO / "folio/quantum-observable-universe/nuclear-interactions"
BRIDGE_FILES = [
    BRIDGE / "q-beta-spectral-bridge.md",
    BRIDGE / "q-beta-spectral-bridge.lean",
    BRIDGE / "q-beta-spectral-bridge-proof.md",
]
# The three things the ladder's attribution names.
CLAIMED_TERMS = ["eigenphase", "V_{(2,1)}", "V_{2,1}", "(2,1)", "phase"]

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))


def main() -> int:
    mp.dps = DPS
    q = q_at(DPS)

    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    z_C = mp.sqrt(q) / (1 + q)
    z_D = q ** 3 / (q ** 2 + 1)

    print("=" * 78)
    print(" Where does the ladder phase alpha = (z-1)h/2 come from?  (qou-cds1)")
    print("=" * 78)
    print(f"\n  q0 = {mp.nstr(q, 20)}   (proton pin, q_at({DPS}))")
    print(f"  h  = {mp.nstr(h, 14)}   u = b*hbar^2 = {mp.nstr(u, 14)}")

    # ---- 1. what the cited source actually contains -----------------------
    print("\n[1] the cited source: conj:q-beta-spectral-bridge")
    hits: dict[str, int] = {t: 0 for t in CLAIMED_TERMS}
    missing = [p for p in BRIDGE_FILES if not p.exists()]
    for path in BRIDGE_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for t in CLAIMED_TERMS:
            hits[t] += len(re.findall(re.escape(t), text, flags=re.IGNORECASE))
    for t in CLAIMED_TERMS:
        print(f"    {t!r:12} occurrences across .md + .lean + proof: {hits[t]}")
    check(
        "cited_source_names_no_eigenphase",
        not missing and all(v == 0 for v in hits.values()),
        "the ladder attributes alpha to 'the single-wrap eigenphase on V_(2,1) "
        "per conj:q-beta-spectral-bridge'; that source contains zero "
        f"occurrences of any of {CLAIMED_TERMS}"
        + (f" (MISSING FILES: {[p.name for p in missing]})" if missing else ""),
    )

    # ---- 2. in the source, (z-1)h/2 is a ratio coefficient ----------------
    hs, zs = sp.symbols("h z", real=True)
    ratio = (1 - hs / 2) / (1 - zs * hs / 2)
    first_order = 1 + (zs - 1) * hs / 2
    remainder = sp.simplify(ratio - first_order)
    expected = zs * (zs - 1) / 4 * hs ** 2 / (1 - zs * hs / 2)
    matches = sp.simplify(remainder - expected) == 0
    print("\n[2] the source's role for (z-1)h/2 -- a ratio, not an angle")
    print(f"    Q_A/Q_B  = (1-h/2)/(1-zh/2)")
    print(f"    minus (1 + (z-1)h/2) = {sp.simplify(remainder)}")
    print(f"    equals z(z-1)h^2/4 / (1-zh/2) ?  {matches}")
    check(
        "bridge_gives_a_ratio_coefficient_not_an_angle",
        bool(matches),
        "(z-1)h/2 is the first-order term of the multiplicative ratio "
        "Q_A/Q_B = (1-h/2)/(1-zh/2); the O(h^2) remainder is exactly "
        "z(z-1)h^2/4/(1-zh/2), matching the source's own Lean "
        "(bridge_first_order_remainder). It is a ratio coefficient.",
    )

    # ---- 3 & 4. the two roles do not agree, and no small delta fixes it ---
    print("\n[3] the ladder's factor vs the source's own factor")
    rel_diffs: dict[str, mp.mpf] = {}
    deltas: dict[str, mp.mpf] = {}
    for name, z in (("C", z_C), ("D", z_D)):
        alpha = (z - 1) * h / 2
        ladder = mp.cos(alpha - u / 2)
        bridge = 1 + alpha
        rel = (ladder - bridge) / bridge
        rel_diffs[name] = rel
        # delta solving cos(alpha - delta) = 1 + alpha
        delta = alpha - mp.acos(bridge) if abs(bridge) <= 1 else mp.nan
        deltas[name] = delta
        print(f"    convention {name}: z = {mp.nstr(z, 14)}  alpha = {mp.nstr(alpha, 14)}")
        print(f"       ladder  cos(alpha - u/2) = {mp.nstr(ladder, 17)}")
        print(f"       bridge     (1 + alpha)   = {mp.nstr(bridge, 17)}")
        print(f"       relative difference      = {mp.nstr(rel, 10)}"
              f"   ({mp.nstr(abs(rel) * 100, 4)} %)")
        print(f"       delta with cos(alpha-delta) = 1+alpha : {mp.nstr(delta, 12)}")
        print(f"          vs the ladder's actual u/2         : {mp.nstr(u / 2, 12)}")
        print(f"          ratio |delta| / (u/2)              = {mp.nstr(abs(delta) / (u / 2), 6)}")

    check(
        "ladder_factor_differs_from_bridge_factor",
        all(abs(rel_diffs[k]) > mp.mpf("0.01") for k in ("C", "D")),
        f"cos(alpha - u/2) and the source's own (1 + alpha) differ by "
        f"{mp.nstr(abs(rel_diffs['C']) * 100, 4)} % (C) and "
        f"{mp.nstr(abs(rel_diffs['D']) * 100, 4)} % (D) at the substrate "
        f"anchor -- in a ladder whose later rungs chase ppb",
    )
    check(
        "no_small_delta_reconciles_the_two_roles",
        all(abs(deltas[k]) / (u / 2) > 10 and deltas[k] < 0 for k in ("C", "D")),
        f"the delta solving cos(alpha-delta) = 1+alpha is "
        f"{mp.nstr(deltas['C'], 8)} (C) / {mp.nstr(deltas['D'], 8)} (D) against "
        f"the ladder's u/2 = {mp.nstr(u / 2, 8)}: off by "
        f"{mp.nstr(abs(deltas['C']) / (u / 2), 4)}x / "
        f"{mp.nstr(abs(deltas['D']) / (u / 2), 4)}x and opposite in sign, so "
        f"the two roles are not reconciled by any small correction",
    )

    # ---- 5. doc-vs-body convention divergence in the cited Lean ----------
    print("\n[5] incidental: the cited Lean's markovZ")
    lean = (BRIDGE / "q-beta-spectral-bridge.lean").read_text(encoding="utf-8")
    md = (BRIDGE / "q-beta-spectral-bridge.md").read_text(encoding="utf-8")
    body_is_D = "q ^ 3 / (q ^ 2 + 1)" in lean
    doc_is_C = "1 / (√q + 1/√q)" in lean
    md_is_C = "\\sqrt q + 1/\\sqrt q" in md
    print(f"    def body is D  (q^3/(q^2+1))           : {body_is_D}")
    print(f"    its docstring says C (1/(sqrt q+...))  : {doc_is_C}")
    print(f"    the .md proposition defines z as C     : {md_is_C}")
    check(
        "lean_body_and_its_own_doc_disagree_on_convention",
        body_is_D and doc_is_C and md_is_C,
        "markovZ's body was migrated to D on 2026-08-26 (qou-cxjq) while its "
        "own docstring and the .md proposition still define z as convention C "
        "-- a live doc-vs-body divergence at the load-bearing definition",
    )

    # ---- report ---------------------------------------------------------
    print("\n  assertions:")
    for name, ok, detail in results:
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"           {detail}")
    all_passed = all(ok for _, ok, _ in results)
    print(f"\n  allPassed: {all_passed}  ({sum(ok for _, ok, _ in results)}/{len(results)})")

    out = {
        "probe": "qbeta_ladder_alpha_provenance_probe",
        "bean": "qou-cds1",
        "question": "does conj:q-beta-spectral-bridge derive the ladder phase "
                    "alpha = (z-1)h/2, as the precision-ladder block claims?",
        "answer": "no -- it produces (z-1)h/2 as the first-order coefficient of "
                  "a multiplicative form-ratio, names no eigenphase and no "
                  "V_(2,1), and its factor differs from the ladder's by 4-5 % "
                  "with no small delta reconciling them",
        "scope": "(a) -- about the cited attribution, not about whether any "
                 "phase term is derivable",
        "q0": mp.nstr(q, 20),
        "q0_pin": "proton (q_at)", "q0Anchor": "proton",
        "dps": DPS,
        "h": mp.nstr(h, 20),
        "u": mp.nstr(u, 20),
        "conventions": {
            name: {
                "z": mp.nstr(z, 20),
                "alpha": mp.nstr((z - 1) * h / 2, 20),
                "ladder_factor_cos_alpha_minus_u_over_2":
                    mp.nstr(mp.cos((z - 1) * h / 2 - u / 2), 20),
                "bridge_factor_one_plus_alpha": mp.nstr(1 + (z - 1) * h / 2, 20),
                "relative_difference": mp.nstr(rel_diffs[name], 20),
                "delta_reconciling_the_two": mp.nstr(deltas[name], 20),
                "delta_over_u_half": mp.nstr(abs(deltas[name]) / (u / 2), 20),
            }
            for name, z in (("C", z_C), ("D", z_D))
        },
        "cited_source_term_counts": hits,
        "assertions": [
            {"name": n, "passed": ok, "detail": d} for n, ok, d in results
        ],
        "allPassed": all_passed,
    }
    dest = _HERE.parent / "qbeta-ladder-alpha-provenance.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"\n  witness -> {dest.relative_to(REPO)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
