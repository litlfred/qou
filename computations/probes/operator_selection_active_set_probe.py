#!/usr/bin/env python3
"""Which `K` is active? The selection LP works at `H_{3A}` — and cannot tell ³H from ³He.

CORRECTION TO MY OWN PRIOR TURN
--------------------------------
`binding_k_convolution_sdp_probe.py` tested PSD-feasibility of `rho_lambda(K)`
and concluded there was no selection principle. **That was the wrong program.**
`binding_k_solver.py` and `binding_link_psd_feasibility_probe.py` route the
reader to the `H_3` PSD feasibility check, but the corpus's actual selection
machinery is the **operator-selection LP with duals** — `nucleus_sdp_assembly.py`
/ `nucleus_real_sdp.py` at `H_{3A}` — where the deliverable is the **active
set**, the Frobenius channels the bound state saturates. Two different programs
share the word "SDP" in this corpus, and the naming collision is what sent the
previous turn down the wrong branch. The PSD findings there stand as stated
about *that* program; they are not findings about selection.

This probe walks the LP route instead, at both levels.

1. AT `H_3` THE CONSTRAINT IS NEAR-VACUOUS, SO THE ACTIVE SET IS EMPTY
------------------------------------------------------------------------
`prop:operator-selection-lp` already records that the *continuous* program is
degenerate: `b_1 = 1` makes the first Frobenius row the objective itself, so the
optimal value is identically `0`, `y_0* = 0`, and the minimisers form a
positive-dimensional face ("which vertex a solver returns is a property of its
pivoting rule"). That is prior work and is not re-argued.

What is measured here is the *integer* program — `nuclear_ilp.py`'s
minimum-length stabilizer search over the operator alphabet
`{sigma_0, sigma_1, sigma_0^-1, sigma_1^-1, pn_0, pn_1}`, which is not subject
to that degeneracy argument because its feasible set is discrete. It is
nonetheless vacuous, for a different reason:

    words of length  1 ..  6:  100.0 % Frobenius-stable
    words of length  8:         99.8 %
    words of length 11:         99.4 %          (nucleon length)

The Frobenius cone contains essentially the whole alphabet. Consequently every
**bound** atom in `nuclear_ilp.py`'s own table, `A = 1 .. 16`, is stable with the
**empty word** — `min |K| = 0` — with every Frobenius row strictly slack
(`min (Gx)_i` runs `0.40 .. 4.44`), so by complementary slackness `y* = 0` and
**the active set is empty**. Nothing is selected, and that script's search
branch is dead code.

The constraint is not *literally* vacuous, and saying so would overstate it:
the **free** constituent product does violate it, first at `O16`
(`min (Gx)_i = -0.618`, `min |K| = 1`). But it is slack for every free product
through `A = 12`, so it has no bite anywhere in the light-isotope range where
Gap #2 lives. Two things follow. The emptiness is **not** an artifact of
`build_atom_nf` already applying the inter-nucleon crossings — the free product
is slack there too. And where the constraint does bite, it is the free product
that fails while the bound atom passes, i.e. the binding crossings are what
restore feasibility — the right sign for the mechanism, just far too high in `A`
to select anything at `A = 2, 3`.

2. AT `H_{3A}` IT DOES WORK — THIS IS THE RIGHT LEVEL
-------------------------------------------------------
`nucleus_sdp_assembly.py` runs the per-nucleus LP at `n = 3A` with
`t_lambda = y_lambda * chi^lambda`, `G_lambda,lambda = y_lambda * dim S^lambda`,
and forbidden blocks where `G_lambda,lambda < 0`. Here the active set is
**non-empty and `y_0* != 0`** — a working selection mechanism, and the one the
knot convolution should be read against. Recorded (committed witnesses, not
re-solved here):

    D    y_0* = -0.014434   7 active: (2,1^4) (2,2,2) (3,3) (4,1,1) (4,2) (5,1) (6)
                            3 negative-norm blocks: (1^6) (2,2,1,1) (3,1,1,1)
    T    y_0* = +0.016550   4 active: (6,3) (7,2) (8,1) (9)
    3He  y_0* = +0.028787   4 active: (6,3) (7,2) (8,1) (9)
    4He  y_0* = +0.003966   6 active: (6,6) (7,5) (8,4) (9,3) (10,2) (11,1)

3. AND HERE IS THE BLOCKER
----------------------------
**`T` and `3He` have the SAME active set.** Identical blocks; the only
difference is `y_0*`, a scalar shadow price. So the mechanism, as implemented,
cannot assign different binding operators to the two `A = 3` isotopes — which is
exactly what Gap #2 needs, and exactly where the census route was refuted for
having no way to distinguish them either.

The corpus states the cause in the witnesses' own `note` field:

> *"Full real SDP needs Phase B color-flavor constraints (LR branching
> `H_{3A} ⊃ (H_3)^Z × (H_3)^N`); this is the bar-fold symmetry-reduced bounded
> baseline."*

The Littlewood–Richardson branching that carries `(Z, N)` — the only thing in
the construction that knows a proton from a neutron — is **not implemented**,
and `binding_cut_entropy_derived_weightings_probe.py` records that the LR
branching data **exists only for the deuteron**. Without it the program sees
`A = 3` and nothing else, so `T` and `3He` are the same problem.

4. THE SAME GAP AT THE BASE OF THE γγ CHAIN
---------------------------------------------
The construction is recursive — `sdp_gamma_gamma_to_qqbar.py` sets out
`γγ → e+e- (H_2)`, `γγ → qq̄ (H_3)`, inner Borromean `B_3`, quark pairs, the
`2·sigma_0` gluon self-coupling, then *"each level adds an LR-embedding step
(Littlewood–Richardson cross-level consistency)"*. The recursion terminates at
the same missing step, and that script says of its own base rung:

> *"the answer is 'yes, 11 is uniquely close to AME but other budgets are
> PSD-feasible too' — so **the SDP is not strict enough**; an additional
> constraint (e.g. minimal `tr_M` complement) is needed to pick out 11
> categorically."*

So at the bottom of the chain the proton's 11-crossing budget is also picked by
closeness to `AME`, not by the program — the same failure mode as the knot
assignments, one level down.

WHAT THIS CHANGES
-----------------
My previous turn concluded "no objective exists". That was aimed at the wrong
program and is withdrawn. The correct statement is narrower and more useful:
**the objective and the duals exist and work at `H_{3A}`; the missing piece is
the LR branching constraint that makes the program depend on `(Z, N)` at all.**
That is a specific, buildable object — cross-level LR consistency, with data
currently present only at `A = 2` — rather than a search for a principle.

No objective is invented and no knot is proposed; the point of the finding is
that the next step is a *constraint*, and which one.

DISCIPLINE
----------
Sections 1 measured here at f64 (sign conclusions on O(1) quantities).
Section 2 is read from committed witnesses (`nucleus-real-sdp-*.witness.json`),
labelled as such and not re-solved. Sections 3-4 quote the corpus's own recorded
notes. No fit; no wiring; no tier change.

-- Ref: [manuscript] bean t7qv; prop:operator-selection-lp;
   nucleus_sdp_assembly.py; sdp_gamma_gamma_to_qqbar.py
"""
from __future__ import annotations

import itertools
import json
import random
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

from hecke_core import h  # noqa: E402
from pyhecke.atom import NF_NAMES, check_frobenius  # noqa: E402
from pyhecke.gram import build_atom_nf, hm  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

# nuclear_ilp.py's operator alphabet, verbatim.
OPS = [("s0", 0, 1.0, 0.0), ("s1", 1, 1.0, 0.0),
       ("s0inv", 0, 1.0, -h), ("s1inv", 1, 1.0, -h),
       ("pn0", 0, 1.0, -h / 2), ("pn1", 1, 1.0, -h / 2)]

ATOMS = [(1, 0, "H"), (1, 1, "D"), (1, 2, "T"), (2, 1, "He3"), (2, 2, "He4"),
         (3, 3, "Li6"), (3, 4, "Li7"), (4, 5, "Be9"), (6, 6, "C12"),
         (8, 8, "O16")]

WITNESSES = [("D", "nucleus-real-sdp-deuteron.witness.json"),
             ("T", "nucleus-real-sdp-tritium.witness.json"),
             ("He3", "nucleus-real-sdp-he3.witness.json"),
             ("He4", "nucleus-real-sdp-he4.witness.json")]


def _nucleon(nf, kind):
    """A single nucleon, replicating build_atom_nf's per-nucleon block."""
    for _ in range(3):
        nf = hm(nf, 1, 0, 0)
        nf = hm(nf, 1, -h, 1)
    if kind == "p":
        nf = hm(nf, 1, 0, 0)
        nf = hm(nf, 1, -h / 2, 0)
        nf = hm(nf, 1, -h / 2, 1)
    else:
        nf = hm(nf, 1, -h / 2, 0)
        nf = hm(nf, 1, -h / 2, 0)
        nf = hm(nf, 1, -h, 1)
    return hm(hm(nf, 1, 0, 0), 1, 0, 0)


def free_product(Z: int, N: int):
    """The constituent product: build_atom_nf WITHOUT inter-nucleon crossings."""
    ordering, pc, nc = [], 0, 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append("p")
            pc += 1
        else:
            ordering.append("n")
            nc += 1
    nf = [1.0, 0, 0, 0, 0, 0]
    for kind in ordering:
        nf = _nucleon(nf, kind)
    for _ in range(Z):
        nf = hm(nf, 1, -h, 1)
    return nf


def frobenius_bite(lengths=(1, 2, 3, 4, 6, 8, 11), cap=2000, seed=7) -> list:
    """What fraction of words in the alphabet satisfy Frobenius positivity?"""
    out = []
    for L in lengths:
        random.seed(seed)
        total = 6 ** L
        exhaustive = total <= cap
        gen = (itertools.product(OPS, repeat=L) if exhaustive
               else (tuple(random.choice(OPS) for _ in range(L))
                     for _ in range(cap)))
        n = stable = 0
        for combo in gen:
            nf = [1.0, 0, 0, 0, 0, 0]
            for _nm, g, c, d in combo:
                nf = hm(nf, c, d, g)
            n += 1
            if check_frobenius(nf)[0]:
                stable += 1
        out.append({"length": L, "sampled": n, "stable": stable,
                    "exhaustive": exhaustive,
                    "pct": f"{100.0 * stable / n:.2f}"})
    return out


def min_length_stabilizer(nf, max_len=3):
    """nuclear_ilp.py's search: shortest word making `nf` Frobenius-stable."""
    if check_frobenius(nf)[0]:
        return 0, ""
    for L in range(1, max_len + 1):
        for combo in itertools.product(OPS, repeat=L):
            t = list(nf)
            for _nm, g, c, d in combo:
                t = hm(t, c, d, g)
            if check_frobenius(t)[0]:
                return L, ".".join(x[0] for x in combo)
    return -1, "NOT FOUND"


def main() -> int:
    assertions = []
    print("t7qv — which K does the operator-selection LP make active?")

    # ── A1. The H_3 Frobenius constraint is near-vacuous ──────────────
    bite = frobenius_bite()
    print("\n  1. how much bite does Frobenius positivity have at H_3?")
    for b in bite:
        kind = "exhaustive" if b["exhaustive"] else "sampled"
        print(f"     words of length {b['length']:2d}: {b['stable']}/{b['sampled']}"
              f" stable ({b['pct']}%)  [{kind}]")
    short = [b for b in bite if b["length"] <= 6]
    ok = all(float(b["pct"]) == 100.0 for b in short)
    print(f"\n  A1  every word up to length 6 is Frobenius-stable ........ "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => the cone contains essentially the whole alphabet.")
    assertions.append(("h3_frobenius_constraint_is_near_vacuous", ok,
                       f"{[(b['length'], b['pct']) for b in bite]}"))

    # ── A2. So the active set is empty and min |K| = 0, bound or free ─
    print("\n  2. consequence: the ILP never searches, and nothing is active")
    print(f"     {'atom':>5s} {'min|K| bound':>13s} {'min|K| free':>12s} "
          f"{'min (Gx) bound':>15s} {'min (Gx) free':>14s} {'active':>8s}")
    rows, all_empty, all_zero = [], True, True
    for Z, N, nm in ATOMS:
        nfb = build_atom_nf(Z, N)
        Lb, _wb = min_length_stabilizer(nfb)
        _s, gxb, _v = check_frobenius(nfb)
        if Z + N >= 2:
            nff = free_product(Z, N)
            Lf, _wf = min_length_stabilizer(nff)
            _s2, gxf, _v2 = check_frobenius(nff)
        else:
            Lf, gxf = Lb, gxb
        active = [NF_NAMES[i] for i in range(6) if abs(gxb[i]) < 1e-6]
        all_empty = all_empty and not active
        all_zero = all_zero and Lb == 0 and Lf == 0
        rows.append({"atom": nm, "A": Z + N, "min_K_bound": Lb,
                     "min_K_free": Lf,
                     "min_Gx_bound": f"{float(min(gxb)):.6f}",
                     "min_Gx_free": f"{float(min(gxf)):.6f}",
                     "active_channels": active})
        print(f"     {nm:>5s} {Lb:>13d} {Lf:>12d} {min(gxb):>15.5f} "
              f"{min(gxf):>14.5f} {str(active if active else 'NONE'):>8s}")
    bound_all_zero = all(r["min_K_bound"] == 0 for r in rows)
    ok = bound_all_zero and all_empty
    print(f"\n  A2  every BOUND atom: min |K| = 0, active set EMPTY ...... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      nuclear_ilp.py's search branch is dead code for every nucleus")
    print("      it tabulates, A = 1 .. 16.")
    assertions.append(("h3_bound_atoms_all_have_empty_active_set", ok,
                       f"{[(r['atom'], r['min_K_bound']) for r in rows]}"))

    # The free product is NOT uniformly stable — O16 violates. Report it.
    free_bad = [r for r in rows if r["min_K_free"] != 0]
    light_ok = all(r["min_K_free"] == 0 for r in rows if r["A"] <= 12)
    print(f"\n  A2b the constraint is not LITERALLY vacuous — the free")
    print(f"      product first violates at {free_bad[0]['atom'] if free_bad else 'nowhere'}"
          f" (min (Gx) = {free_bad[0]['min_Gx_free'] if free_bad else 'n/a'}) —")
    print(f"      but it binds NOWHERE in A <= 12 ................... "
          f"{'PASS' if (light_ok and free_bad) else 'FAIL'}")
    print("      So it is slack throughout the light-isotope range where")
    print("      Gap #2 lives, and cannot select there. Where it does bite,")
    print("      it is the FREE product that fails and the BOUND atom that")
    print("      passes — the binding crossings are what restore feasibility.")
    assertions.append(("free_product_binds_only_above_A12", bool(light_ok and free_bad),
                       f"free violations: {[(r['atom'], r['min_Gx_free']) for r in free_bad]}"))

    # ── A3/A4. The H_{3A} level, from committed witnesses ─────────────
    print("\n  3. at H_{3A} the SAME program DOES select (committed witnesses):")
    print(f"     {'atom':>5s} {'y0*':>12s} {'#active':>8s}  active blocks")
    sdp = {}
    for nm, fn in WITNESSES:
        p = COMP / fn
        if not p.exists():
            print(f"     {nm:>5s}  (witness absent)")
            continue
        s = json.load(open(p, encoding="utf-8"))["data"]["positive_norm_subspace_solve"]
        blocks = list(s.get("active_blocks") or [])
        sdp[nm] = {"y0_star": f"{float(s.get('y0_star')):.9f}",
                   "active_blocks": blocks}
        print(f"     {nm:>5s} {float(s.get('y0_star')):>12.6f} {len(blocks):>8d}  "
              f"{' '.join(blocks)}")
    ok = bool(sdp) and all(b["active_blocks"] for b in sdp.values())
    print(f"\n  A3  at H_{{3A}} the active set is NON-empty ................ "
          f"{'PASS' if ok else 'FAIL'}")
    print("      this is the working mechanism, and the right level to read")
    print("      the knot convolution against.")
    assertions.append(("h3A_active_set_is_nonempty", ok,
                       {k: len(v["active_blocks"]) for k, v in sdp.items()}))

    same = ("T" in sdp and "He3" in sdp
            and sdp["T"]["active_blocks"] == sdp["He3"]["active_blocks"])
    print(f"\n  A4  ...but T and He3 get the SAME active set ............. "
          f"{'PASS' if same else 'FAIL'}")
    if same:
        print(f"      both: {' '.join(sdp['T']['active_blocks'])}")
        print(f"      differing only in y0*: T {sdp['T']['y0_star']} vs "
              f"He3 {sdp['He3']['y0_star']}")
    print("      So the program cannot assign different K to the two A=3")
    print("      isotopes — exactly what Gap #2 needs. Cause, per the")
    print("      witnesses' own note: Phase B color-flavor constraints (LR")
    print("      branching H_{3A} > (H_3)^Z x (H_3)^N) are NOT implemented,")
    print("      and the LR data exists only for the deuteron.")
    assertions.append(("T_and_He3_share_an_active_set", same,
                       f"T {sdp.get('T', {}).get('active_blocks')} vs "
                       f"He3 {sdp.get('He3', {}).get('active_blocks')}"))

    print()
    print("### VERDICT: the selection LP is real and works at H_{3A} — non-empty")
    print("    active sets, y0* != 0, strong duality. It is the H_3 layer that is")
    print("    vacuous (whole alphabet feasible, active set empty, min |K| = 0).")
    print("    The blocker is not a missing objective, as I said last turn: it is")
    print("    the missing LR branching constraint that would make the program")
    print("    depend on (Z, N) at all. Until it exists, T and He3 are the same")
    print("    problem to the solver, and no K can distinguish them.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("operator-selection-active-set",
                                engine="python", output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv). Corrects my prior turn, which tested "
                "PSD-feasibility of rho_lambda(K) — the wrong program; the "
                "corpus's selection machinery is the operator-selection LP with "
                "duals, where the deliverable is the ACTIVE SET. Measured: at "
                "H_3 the Frobenius constraint is near-vacuous (100% of alphabet "
                "words up to length 6 are stable, 99.4% at nucleon length 11), "
                "so every nucleus is stable with the EMPTY word, every row is "
                "strictly slack (min (Gx)_i 0.40..4.44) and the active set is "
                "EMPTY — for the bound atom AND the free constituent product "
                "alike, so it is not an artifact of build_atom_nf pre-applying "
                "the inter-nucleon crossings. At H_{3A} the same program DOES "
                "select: non-empty active sets, y0* != 0, strong duality. But T "
                "and He3 get IDENTICAL active blocks {(6,3),(7,2),(8,1),(9)}, "
                "differing only in the scalar y0*, so it cannot assign them "
                "different K — which is what Gap #2 needs. Cause is recorded in "
                "the witnesses themselves: Phase B color-flavor constraints (LR "
                "branching H_{3A} > (H_3)^Z x (H_3)^N) are not implemented and "
                "the LR data exists only for the deuteron. No fit; no objective "
                "invented; no knot proposed.")
            wb.add_data("h3_frobenius_bite", bite)
            wb.add_data("h3_per_atom", rows)
            wb.add_data("h3A_from_committed_witnesses", sdp)
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "Section 2 (H_{3A}) is READ from committed "
                "nucleus-real-sdp-*.witness.json, not re-solved here. Those runs "
                "are the bar-fold symmetry-reduced bounded baseline by their own "
                "note, not the full real SDP.")
            wb.add_caveat(
                "The H_3 measurements are f64. Every conclusion is a sign or a "
                "count on O(1) quantities, so f64 is adequate; declared, not "
                "laundered.")
            wb.add_caveat(
                "The continuous H_3 LP's degeneracy (optimal value identically "
                "0, y0* = 0, minimisers a positive-dimensional face) is PRIOR "
                "work, recorded in prop:operator-selection-lp. What is measured "
                "here is the distinct INTEGER program of nuclear_ilp.py, whose "
                "discrete feasible set escapes that argument but is vacuous for "
                "the separate reason above.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
