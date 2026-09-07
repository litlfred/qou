"""The Lean ordering-invariance is a property of the SUM, not of its terms.

WHAT THE CORPUS ALREADY PROVES
------------------------------
`QOU.Mass.IntraOrdering.chainRatio_eq_of_intra`
(`content/quantum-observable-universe/lean/QOU/Mass/IntraOrderingInvariance.lean`,
sorry-free) proves that the chain ratio cannot see the intra-nucleon ordering:
if the trace factors as `tr_M(W_atom) = F · P` and `tr_M(W_free) = F`, then

    (F₁ · P) / F₁  =  (F₂ · P) / F₂

for ARBITRARY, unrelated `F₁`, `F₂`. No hypothesis links them — in the
measurement they differ by up to 14.325× — so the invariance is cancellation,
not coincidence.

PRIOR WORK, AND WHAT IS ACTUALLY NEW HERE (read this before quoting anything)
-----------------------------------------------------------------------------
`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py` (beans
`qou-hu1f`, `qou-gpb5`) already measured the trace-level half of this, and
measured it BETTER: it reports `tr_M(W_atom)/tr_M(W_free)` identical under the
two orderings to **~1e-60** at 2H, 3H, 3He and 4He, and equal to
`∏ᵢ (z + dᵢ)` under both.  It also carries the `R_quark` factors (3.785 →
14.325), the closed form for why a difference route scales while a log-ratio
route does not, and the finding that the per-GENERATOR factorisation is
grouped-specific.

**So the trace-ratio row below is a coarser re-derivation of a known result, not
a new one.**  It is retained only as the control the per-block row is contrasted
against, and its ~1e-18 is an artefact of HOW it is computed here: this probe
forms `tr_M = Σ_λ y_λ χ_λ` from the cached per-block χ, which loses ~30 digits to
cancellation between mixed-sign terms.  The prior probe gets 1e-60 by not going
through the blocks at all.  **Quote 1e-60, not 1e-18.**

What is new is the row above it.  Neither the Lean nor the prior probe says
anything about **per-block** `χ^λ_atom / χ^λ_free`, because both work with the
trace of a whole word.  That gap is exactly where a false all-clear comes from,
which is why it is worth measuring separately.

WHY THIS PROBE EXISTS
---------------------
That file's header says "**the ratio** cannot see the intra ordering", and an
agent triaging stale consumers will read that and ask "does this consumer use a
ratio?".  That question is the wrong one, and answering it "yes" produces a FALSE
ALL-CLEAR.

The theorem is about the ratio of the aggregate **Markov traces** — each a
`y_λ`-weighted SUM over every partition.  It says nothing about the ratio of
individual `χ^λ`, and the two behave completely differently.

MEASURED — the same atoms, the same partitions, grouped (origin/main) against
borromean (regenerated under the `qou-hu1f` ruling):

    quantity                              max relative change
    per-block χ, absolute                 5.562e+0   (4He)
    per-block ratio χ_atom / χ_free       4.332e+1   (T, at λ=(3,2,2,2))
    aggregate tr_M(atom) / tr_M(free)     5.425e-18  (T)  [prior probe: ~1e-60]

Nineteen orders between the last two rows, on the same underlying numbers.

    D    trace ratio  0.508229789376738961855522  ->  0.508229789376738960877252
    T    trace ratio  0.205135640448649768365013  ->  0.205135640448649767252137
    3He  trace ratio  0.311386312072595651631708  ->  0.311386312072595650363816

THE RESIDUAL IS ~1e-18, NOT ~1e-50, AND THAT IS EXPECTED
---------------------------------------------------------
The χ inputs are 50-dps strings, so an exactly-invariant quantity computed from
them would agree near 1e-50.  It agrees at ~1e-18 because the trace is a sum of
mixed-sign terms far larger than their total: roughly thirty digits are lost to
cancellation before the ratio is taken.  So this is CONSISTENT WITH exact
invariance and is not evidence of it — do not quote 1e-18 as a measurement of
how exact the theorem is.  What it does establish, unambiguously, is the CONTRAST
with 4.332e+1 one row up.

THE CORRECT TRIAGE RULE
-----------------------
For a consumer of the `atom-chi-rust-*` / `chi-<atom>-*` caches:

    uses ONLY tr_M(W_atom)/tr_M(W_free)   -> provably unaffected (the Lean)
    touches ANY per-block quantity        -> affected, even if it forms a ratio

The second line is the one that needed measuring.  It also means the earlier
"64 of 68 consumers are stale" upper bound is NOT loosened by the Lean result:
a per-block consumer is genuinely affected however it combines its blocks.

RELATION TO THE OTHER TWO PROBES IN THIS FAMILY
-----------------------------------------------
`one_dim_reps_are_blind_to_intra_order_probe` — which BLOCKS move (all but the
two 1-dimensional ones).  `rust_and_hoefsmit_chi_agree_on_the_same_word_probe` —
whether two kernels are on the same word.  This one — which DOWNSTREAM
CONSTRUCTIONS survive.  They answer three different questions and none subsumes
another.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401,E402
from mpmath import mp  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

mp.dps = 60

ATOMS = (("D", "atom-chi-rust-d", 6), ("T", "atom-chi-rust-t", 9),
         ("3He", "atom-chi-rust-3he", 9))

# The trace ratio must be invariant to well inside anything a consumer sees.
# Set at 1e-12: nine orders of headroom over the measured ~1e-18, and thirteen
# orders below the smallest per-block move.  Not delicate.
TRACE_TOL = mp.mpf("1e-12")
# A per-block ratio must NOT be invariant -- this direction is the point.
BLOCK_MIN_MOVE = mp.mpf("1.0")


def _at_main(rel: str):
    r = subprocess.run(["git", "show", f"origin/main:{rel}"],
                       capture_output=True, text=True, cwd=ROOT)
    return json.loads(r.stdout) if r.returncode == 0 else None


def _blocks(w, leg):
    return {tuple(x["partition"]): mp.mpf(x["chi_lambda"])
            for x in w["data"][leg]["by_partition"]}


def main() -> int:
    q = mp.mpf(str(Q0))
    rows, failures = [], []
    for atom, stem, n in ATOMS:
        rel = f"computations/{stem}.witness.json"
        old = _at_main(rel)
        newp = ROOT / rel
        if old is None or not newp.exists():
            failures.append(f"{atom}: cannot read both versions of {rel}")
            continue
        new = json.loads(newp.read_text())
        y = y_lambda_su_n(n, q, 2)

        def trace(w, leg):
            s = mp.mpf(0)
            for lam, chi in _blocks(w, leg).items():
                yl = y.get(lam)
                if yl is not None:
                    s += mp.mpf(yl) * chi
            return s

        r_old = trace(old, "atom") / trace(old, "free")
        r_new = trace(new, "atom") / trace(new, "free")
        trace_move = abs(r_old - r_new) / abs(r_old)

        oa, of = _blocks(old, "atom"), _blocks(old, "free")
        na, nf = _blocks(new, "atom"), _blocks(new, "free")
        block_worst, worst_lam = mp.mpf(0), None
        for lam in set(oa) & set(na):
            if not of.get(lam) or not nf.get(lam):
                continue
            a, b = oa[lam] / of[lam], na[lam] / nf[lam]
            if a == 0:
                continue
            d = abs(a - b) / abs(a)
            if d > block_worst:
                block_worst, worst_lam = d, lam

        rows.append((atom, trace_move, block_worst, worst_lam))
        if trace_move > TRACE_TOL:
            failures.append(
                f"{atom}: the AGGREGATE trace ratio moved by {mp.nstr(trace_move, 6)} "
                f"-- chainRatio_eq_of_intra says it cannot, so either the trace does "
                "not factor as intra x interfaces here, or a cache is not what it claims")
        if block_worst < BLOCK_MIN_MOVE:
            failures.append(
                f"{atom}: the per-block ratio moved by only {mp.nstr(block_worst, 6)} "
                "-- if per-block ratios were invariant too, the triage rule this probe "
                "exists to state would be wrong in the SAFE direction")

    print("=" * 78)
    print("INTRA-ORDERING INVARIANCE: the SUM is invariant, its TERMS are not")
    print("=" * 78)
    print(f"  {'atom':5s} {'trace-ratio move':>20s} {'per-block ratio move':>22s}   worst block")
    for atom, tm, bw, lam in rows:
        print(f"  {atom:5s} {mp.nstr(tm, 6):>20s} {mp.nstr(bw, 6):>22s}   {lam}")
    print()
    print("  TRIAGE: uses only tr_M(atom)/tr_M(free) -> provably unaffected (Lean)")
    print("          touches ANY per-block quantity  -> affected, ratio or not")
    print()
    if failures:
        for f in failures:
            print(f"  [FAIL] {f}")
        print(f"\n{len(failures)} FAILED")
        return 1
    print(f"  [PASS] {len(rows)} atoms: trace ratio invariant, per-block ratio not")
    print("\nALL PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
