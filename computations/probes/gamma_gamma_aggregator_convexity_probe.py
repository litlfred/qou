#!/usr/bin/env python3
"""gamma_gamma_aggregator_convexity_probe.py — does the gamma-gamma assembly
give a NON-AFFINE aggregator, and on which side?  (qou-ix0x, Option 2;
the follow-up bean qou-82mc leaves open)

## The question

Bean `qou-82mc` (completed, sorry-free Lean `AggregatorConvexityDichotomy`)
reduces the `b_3` sign to a **secant comparison on the ray through the origin**:
writing the binding as a function of total bond weight, `B = Phi(m_A . g)`,

    Phi concave through 0  =>  b_3 <= 0     (b3Agg_nonpos_of_concaveOn)
    Phi convex  through 0  =>  b_3 >= 0     (b3Agg_nonneg_of_convexOn)

Both assemblies the corpus has machine-checked are on the CONCAVE side: the
multiplicative/Mayer one is strictly concave (`b_3 < 0`), and the additive
bond-functional sum is AFFINE -- the concave boundary -- giving `b_3 = 0`
exactly.  AME2020 needs `b_3 = +1.4262225 > 0`, and `qou-82mc` measures that
AME's own `Phi` is strictly convex on the `A = 2,3,4` grid.  Its follow-up:

> *"Identify a candidate `Phi` from Hecke-side quantities that is convex at
>  small argument and asymptotically linear."*

`qou-q8vl` records the same route as **"the convexity route, which is
unanalysed here"**.

## Why the gamma-gamma bond is a candidate, and it is derived

`Mass.ProductionChainBondProduct.tr_productionChain_braided` proves
`tr_M(W_atom)/tr_M(W_free) = prod_bonds (z + d_b)` -- a PRODUCT over bonds.
Take logs and the binding is a SUM over bonds: affine in bond count, hence
`b_3 = 0`.  **So the corpus's derived assembly is affine precisely because the
bond product holds.**

The companion probe `gamma_gamma_bond_is_pair_independent_probe` measured that
the gamma-gamma bond `G^3 = (sigma_2 sigma_3^-1)^3` -- fixed by the owner's
2026-09-08 ruling (bean `qou-ales`) -- is OUTSIDE that theorem's hypotheses: its
`sigma_3` lies inside a nucleon block (`StrandLayoutForcesChain.crossesBlocks_iff`:
`3 % 3 = 0` does not cross), and the measured bond factor is pair-DEPENDENT
(spread 4.47e-4 against the template's 1.6e-61), which a bond product forbids.

So the gamma-gamma assembly need not be affine.  **Whether it is, and on which
side, is what this probe measures**, directly at `A = 3`:

    delta := tr_M(W_free . B_0 . B_1) / tr_M(W_free)
             -  [ tr_M(W_free . B_0)/tr_M(W_free) ]
              . [ tr_M(W_free . B_1)/tr_M(W_free) ]

`delta = 0` is exactly the bond product, i.e. an affine log-assembly and
`b_3 = 0`.  `delta != 0` is a non-affine aggregator, and since
`B = -alpha . log(mu)` with `alpha > 0`, a SUPER-multiplicative ratio
(`delta > 0` at `mu > 1`) is a SUB-additive binding -- the CONCAVE side -- while
`delta < 0` is the convex side that `b3Agg_nonneg_of_convexOn` needs.

## Anti-fit

Nothing is tuned or searched.  One bond word, fixed by a ruling made for
reasons unrelated to `b_3`; one layout, fixed by `StrandLayoutForcesChain`; the
sign reading is Lean-proved.  All four nucleon contents of `A = 3` are reported
whatever they say.  The affine case `delta = 0` is the expected outcome and is
reported as a result, not as a failure.

The template `sigma_2` bond is carried as a CONTROL: the bond product is a
theorem for it, so its `delta` must be `0` to working precision.  A non-zero
control would mean the harness is wrong, not the corpus.

PRECISION: mpmath end to end at 60 dps, seeded from `Q_50_DIGIT_STR`.  Proton
pin, convention D.  Only the `y_lambda > 0` blocks are built -- under SU(2)
those are exactly the at-most-two-row partitions, and the omitted blocks
contribute `y_lambda . chi_lambda = 0` EXACTLY, so this is a restriction and
not an approximation.
"""
from __future__ import annotations

import datetime
import json
import os
import subprocess
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from pyhecke.wedderburn import partitions_of  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

DPS = 60
mp.mp.dps = DPS
TOL = mp.mpf("1e-40")


def _head_sha() -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(Path(__file__).resolve().parent), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def vertex_pow(i: int, k: int, h):
    w = []
    for _ in range(k):
        w += [(mp.mpf(1), mp.mpf(0), i), (mp.mpf(1), -h, i + 1)]
    return w


def nucleon_block(kind: str, h, offset: int = 0):
    """The 11-letter per-nucleon block of `build_atom_nf` on (offset, offset+1)."""
    one, zero = mp.mpf(1), mp.mpf(0)
    g0, g1 = offset, offset + 1
    w = []
    for _ in range(3):
        w.append((one, zero, g0))
        w.append((one, -h, g1))
    if kind == "p":
        w += [(one, zero, g0), (one, -h / 2, g0), (one, -h / 2, g1)]
    else:
        w += [(one, -h / 2, g0), (one, -h / 2, g0), (one, -h, g1)]
    w += [(one, zero, g0), (one, zero, g0)]
    return w


def word_image(sigmas, dim, word):
    M = mp.eye(dim)
    I = mp.eye(dim)
    for c, d, g in word:
        M = M * (c * sigmas[g] + d * I)
    return M


def trace(M, dim):
    return mp.fsum(M[i, i] for i in range(dim))


def main() -> int:
    t0 = time.time()
    anchor = os.environ.get("QOU_Q0_ANCHOR", "").strip().lower()
    if anchor in ("ideal", "muon", "canonical"):
        raise SystemExit("PROTON-pin producer (owner directive 2026-08-07); "
                         "refusing a muon override")

    q = Q_MP
    h = q - 1 / q
    z_d = q ** 3 / (q ** 2 + 1)
    cache = BlockCacheMP(q, h)

    print(f"gamma-gamma aggregator: affine or not?  proton pin, convention D, {DPS} dps")
    print("=" * 78)
    print(f"  q0  = {Q_50_DIGIT_STR[:34]}...    z_D = {mp.nstr(z_d, 15)}")

    # A = 3 -> 9 strands.  Only y > 0 blocks are built; the rest contribute 0 exactly.
    parts9 = [tuple(p) for p in partitions_of(9)]
    y9 = {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(9, q, 2).items()}
    live = [lam for lam in parts9 if y9[lam] > TOL]
    dropped_max_y = max((abs(y9[lam]) for lam in parts9 if lam not in live), default=mp.mpf(0))
    print(f"  H_9: {len(parts9)} blocks, y > 0 on {len(live)}: {live}")
    print(f"       max |y| among the {len(parts9) - len(live)} dropped blocks: "
          f"{mp.nstr(dropped_max_y, 6)}  (must be 0 -- restriction, not approximation)")

    reps = {}
    for lam in live:
        reps[lam] = seminormal_matrices_mp(lam, cache=cache)
    print(f"  dims: {[reps[lam][1] for lam in live]}   built in {time.time() - t0:.1f}s")

    def tr_m9(word):
        return mp.fsum(y9[lam] * trace(word_image(reps[lam][0], reps[lam][1], word),
                                       reps[lam][1]) for lam in live)

    bonds = {
        "template_s2": lambda i: [(mp.mpf(1), mp.mpf(0), i)],
        "G3": lambda i: vertex_pow(i, 3, h),
    }
    # nucleon k on strands 3k,3k+1,3k+2 -> generators (3k, 3k+1); bridges at 3k+2.
    atoms = {"ppn": ("p", "p", "n"), "pnn": ("p", "n", "n"),
             "ppp": ("p", "p", "p"), "nnn": ("n", "n", "n")}

    print(f"\n  A = 3, bonds at sigma_2 and sigma_5 (StrandLayoutForcesChain: bridges at 3k+2)")
    print(f"  {'atom':>5}{'bond':>13}{'mu_both':>22}{'mu_0 . mu_1':>22}{'delta':>18}  side")
    rows = {}
    for aname, (k0, k1, k2) in atoms.items():
        w_free = (nucleon_block(k0, h, 0) + nucleon_block(k1, h, 3)
                  + nucleon_block(k2, h, 6))
        tr_free = tr_m9(w_free)
        for bname, mk in bonds.items():
            b0, b1 = mk(2), mk(5)
            mu_both = tr_m9(w_free + b0 + b1) / tr_free
            mu_0 = tr_m9(w_free + b0) / tr_free
            mu_1 = tr_m9(w_free + b1) / tr_free
            delta = mu_both - mu_0 * mu_1
            rows[(aname, bname)] = {"tr_free": tr_free, "mu_both": mu_both,
                                    "mu_0": mu_0, "mu_1": mu_1, "delta": delta}
            side = ("AFFINE (bond product holds)" if abs(delta) < TOL
                    else ("super-multiplicative -> CONCAVE side" if delta > 0
                          else "sub-multiplicative -> CONVEX side"))
            print(f"  {aname:>5}{bname:>13}{mp.nstr(mu_both, 18):>22}"
                  f"{mp.nstr(mu_0 * mu_1, 18):>22}{mp.nstr(delta, 10):>18}  {side}")

    ctrl = max(abs(rows[(a, "template_s2")]["delta"]) for a in atoms)
    print(f"\n  CONTROL  worst |delta| for the template bond (bond product is a "
          f"THEOREM for it): {mp.nstr(ctrl, 6)}")
    tmpl_mu = max(abs(rows[(a, 'template_s2')]['mu_both'] - z_d ** 2) for a in atoms)
    print(f"  CONTROL  worst |mu_both(template) - z_D^2|: {mp.nstr(tmpl_mu, 6)}")

    gg_delta = {a: rows[(a, "G3")]["delta"] for a in atoms}
    gg_max = max(abs(v) for v in gg_delta.values())
    sign_str = ", ".join(f"{a}: " + ("+" if gg_delta[a] > 0 else "-") for a in atoms)
    print(f"  gamma-gamma: worst |delta| = {mp.nstr(gg_max, 10)}; signs = {sign_str}")

    a = []
    a.append(("CONTROL: the template bond's delta vanishes -- the bond product is a "
              "theorem for it, so a non-zero control would indict this harness",
              ctrl < TOL))
    a.append(("CONTROL: mu_both(template) = z_D^2 exactly, the two-bond product",
              tmpl_mu < TOL))
    a.append(("the dropped blocks carry y = 0 exactly, so restricting to the "
              "at-most-two-row partitions is exact", dropped_max_y < TOL))
    nonaffine = gg_max > TOL
    # THE RESULT.  This was written as "the assembly is NON-AFFINE" -- my
    # hypothesis -- and the measurement refuted it.  Restated as what is true, so
    # it stays falsifiable: if a future bond word breaks the product, this fires.
    a.append(("THE RESULT: the gamma-gamma assembly is EXACTLY AFFINE -- the bond "
              "product holds for G^3 to the 60-dps floor, so the log-assembly is "
              "additive in bond count and qou-82mc's b_3 is 0, not positive",
              not nonaffine))
    a.append(("and it holds DESPITE G^3 violating ProductionChainBondProduct's "
              "strand-window hypothesis (sigma_3 is inside block 1), so those "
              "hypotheses are SUFFICIENT but not NECESSARY", not nonaffine))
    # The per-content delta signs are at the arithmetic floor (~1e-61) and are
    # therefore ROUND-OFF, not structure.  Asserted so "MIXED" is never read as a
    # finding -- agreement at 1e-61 in 60-dps mpmath is the floor of the
    # arithmetic, not evidence about the mathematics (AGENTS.md, probes rule 4).
    a.append(("the per-content delta signs are round-off, not structure: every "
              "|delta| sits at the same 1e-61 floor as the template CONTROL, so "
              "their signs carry no information and MIXED is noise",
              gg_max <= ctrl * 10 + mp.mpf("1e-58")))

    print("\n  assertions:")
    ok = True
    for name, passed in a:
        ok &= bool(passed)
        print(f"    [{'PASS' if passed else 'FAIL'}] {name}")

    all_pos = all(v > 0 for v in gg_delta.values())
    all_neg = all(v < 0 for v in gg_delta.values())
    verdict = ("AFFINE" if not nonaffine
               else ("CONCAVE side (super-multiplicative)" if all_pos
                     else ("CONVEX side (sub-multiplicative)" if all_neg else "MIXED")))
    print(f"\n  VERDICT: the gamma-gamma aggregator is on the {verdict}.")
    print(f"  qou-82mc needs CONVEX through the origin for b_3 >= 0.")

    w = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath",
        "scriptFile": Path(__file__).name,
        "commitSha": _head_sha(),
        "q0Anchor": "proton",
        "q0AnchorReason": "seeded from Q_50_DIGIT_STR; convention D (z = q^3/(q^2+1))",
        "description": (
            "Measures whether the gamma-gamma-selected bond gives a NON-AFFINE binding "
            "aggregator at A = 3, by comparing the two-bond trace ratio against the "
            "product of the two single-bond ratios. delta = 0 is exactly the bond "
            "product (affine log-assembly, b_3 = 0); delta's sign decides which side of "
            "qou-82mc's convexity dichotomy the assembly sits on. The template sigma_2 "
            "bond is a control for which the bond product is a theorem."
        ),
        "dps": DPS,
        "q0": Q_50_DIGIT_STR,
        "z_D": mp.nstr(z_d, 30),
        "live_blocks": [str(lam) for lam in live],
        "dropped_blocks_max_abs_y": mp.nstr(dropped_max_y, 12),
        "rows": {f"{a_}|{b_}": {k: mp.nstr(v, 30) for k, v in d.items()}
                 for (a_, b_), d in rows.items()},
        "controls": {"template_worst_abs_delta": mp.nstr(ctrl, 12),
                     "template_mu_both_vs_zD_squared": mp.nstr(tmpl_mu, 12)},
        "gamma_gamma_non_affine": bool(nonaffine),
        "verdict": verdict,
        "assertions": [{"name": n, "passed": bool(p)} for n, p in a],
        "allPassed": bool(ok),
    }
    out = Path(__file__).with_name("gamma-gamma-aggregator-convexity.witness.json")
    out.write_text(json.dumps(w, indent=1) + "\n")
    print(f"\n  witness -> {out.relative_to(_ROOT)}")
    print(f"  wall {time.time() - t0:.1f}s")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
