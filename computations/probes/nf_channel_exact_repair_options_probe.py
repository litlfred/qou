#!/usr/bin/env python3
"""`nf_channel_exact`: what is actually wrong, and the four repair options.

WHY THIS IS AN OPTIONS PROBE AND NOT A FIX
--------------------------------------------
`phase_b_lr_branching_constraint_probe.py` found `pyhecke.atom.nf_channel_exact`
callable-and-wrong and deliberately did not repair it, on the grounds that the
right `chi_std` depends on which Wedderburn convention `W_STD` is meant to pair
with — a substrate decision. This probe settles the *diagnosis* exactly, so the
decision can be made on facts, and lays out the options with their blast radius.
**No fix is applied.**

THE DIAGNOSIS, EXACTLY
----------------------
The function computes `chi_sym` and `chi_alt` **directly**, from the eigenvalue
vectors `_SYM_EIG_FRAC` and `_ALT_EIG_FRAC`, but computes `chi_std` **by
subtraction**:

    chi_std = (tr_M - W_sym*chi_sym - W_alt*chi_alt) / W_std

That asymmetry is where the bug lives, and it fails for two independent reasons.

**(1) `W` is not the Markov weight.** Solving `sum_lam y_lam chi^lam = TR_M` on
the NF basis gives, exactly and consistently on all six equations,

    y_sym = (q^4 + 1)/(q^2 + 1)^2      y_std = q^2/(q^2 + 1)^2      y_alt = 0

with `y_sym + 2 y_std + y_alt = 1` identically. Against the module constants

    W_sym = q^2/D      W_std = (q^2+1)^2/D      W_alt = q^2/D,   D = q^4+4q^2+1

**no component agrees.** `W` is not wrong in itself — its numerators are
`d_lam^2` for `d = (q, q^2+1, q)` and they sum to `D`, so `W` is the
**q-Plancherel measure** `d_lam^2 / sum d^2`, with `d_std/d_sym = q + 1/q =
[2]_q`. It is a coherent object; it is simply not the trace weight, and
substituting one for the other is the error.

**(2) The three-term shape is wrong regardless of coefficients.** `y_alt = 0`,
so `tr_M` carries **no information at all** about `chi_alt`. Subtracting a
`chi_alt` term from `tr_M` is subtracting something that was never there.

And `y_alt = 0` is not a curiosity — it is the Gram radical the corpus already
documents. `RADICAL = [(-1/q)^len(w)]` **is** `_ALT_EIG_FRAC`, the same vector,
and `G . RADICAL = 0` to `1.7e-16`. So

    y_alt = 0      and      G . chi_alt = 0

are the same fact: the convention-D Markov trace annihilates the sign block, so
the trace form is degenerate exactly along it. That is why `det G = 0`.

THE STANDARD CHARACTER, IN CLOSED FORM
----------------------------------------
There is no need to invert anything. On the NF basis
`[(), (0,), (1,), (0,1), (1,0), (0,1,0)]` the standard character is

    chi^(2,1)  =  [ 2,  h,  h,  -1,  -1,  0 ]         h = q - 1/q

verified against direct seminormal traces at `q = 1.02, q_0, 1.5, 2.7, 4.0`.
The `q`-deformation touches only the two length-one entries; the 3-cycles give
`-1` and the longest element `0` at every `q`, exactly as in the classical `S_3`
standard character. So `chi_std` is a dot product with a fixed vector, precisely
like `chi_sym` and `chi_alt` already are.

THE OPTIONS
-----------
**A — fix the inversion, keep the shape.** Replace the weights and drop the
`chi_alt` term:  `chi_std = (tr_M - y_sym*chi_sym)/y_std`.
  + Local to the function; `W_*` untouched, so no other number moves.
  - Still a derived quantity obtained by division, and it silently depends on
    `_TR_M_FRAC` remaining the convention-D trace. Fragile in the same way that
    let this survive.

**B — compute `chi_std` directly. [RECOMMENDED]** Add
`_STD_CHI_FRAC = [2, h, h, -1, -1, 0]` and dot with it.
  + Removes the asymmetry that *caused* the bug — all three channels then come
    from fixed character vectors.
  + No division, no weights, no dependence on `W_*` or on `_TR_M_FRAC` at all,
    so no convention question arises and nothing else can drift into it.
  + Smallest diff; correct by construction against the seminormal traces.
  - None identified.

**C — change `W_*` to the Markov weights.** Not recommended.
  - Invasive: `W_SYM/W_STD/W_ALT` have real arithmetic consumers —
    `pyhecke/molecular.py` lines 121, 124, 125 (binding sums),
    `pyhecke/atom.py` line 333 (`vertex_volume`), and
    `qou-mass/.../_internal/hecke_core.py` lines 230-232. Changing them moves
    molecular binding numbers and vertex volumes.
  - And it would be breaking a *correct* object (the q-Plancherel measure) to
    serve one broken function.

**D — leave it, keep the flag.** Defensible today: the audit in this bean found
**zero call sites**, so nothing computes with it. But it is re-exported from four
modules and reads as usable, which is how it stayed broken.

A SEPARATE DECISION, WHICHEVER OPTION IS TAKEN
------------------------------------------------
The exact-Fraction path evaluates at `_Q_FRAC = 111/100`, not at `q_0` — that is
what makes the 1-dimensional channels differ from a `q_0` computation in the 5th
decimal (`-1/1.11 = -0.9009009` against `-1/q_0 = -0.9009183`). That is a
deliberate design choice of the exact path, not part of this bug, but a caller
wanting characters at `q_0` needs a `q` parameter. Worth settling at the same
time.

DISCIPLINE
----------
Diagnosis only; **no repair applied**. The weight solve and the closed-form
character are exact (sympy); the radical identity is checked numerically at
`1.7e-16`. No fit; no `B_AME`; nothing wired.

-- Ref: [manuscript] bean t7qv; phase_b_lr_branching_constraint_probe.py;
   pyhecke.gram (RADICAL, det G = 0)
"""
from __future__ import annotations

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
sys.path.insert(0, str(COMP / "hecke"))
import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from pyhecke.atom import _ALT_EIG_FRAC  # noqa: E402
from pyhecke.gram import G as G3  # noqa: E402
from pyhecke.gram import RADICAL  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

NF = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NAMES = ["gamma", "s0", "s1", "L+", "L-", "e-"]
Q_TEST = [1.02, 1.1099785827513808, 1.5, 2.7, 4.0]


def std_char_numeric(qv: float) -> list:
    sig = build_seminormal_matrices([2, 1], q=qv)[0]
    out = []
    for w in NF:
        M = np.eye(2)
        for g in w:
            M = M @ np.asarray(sig[g], dtype=float)
        out.append(float(M.trace()))
    return out


def main() -> int:
    assertions = []
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    print("t7qv — nf_channel_exact: diagnosis and repair options (NO FIX APPLIED)")

    # ── A1. chi^(2,1) in closed form ──────────────────────────────────
    print("\n  1. the standard character on the NF basis")
    print(f"     {'q':>20s}  measured                      matches [2,h,h,-1,-1,0]")
    ok = True
    for qv in Q_TEST:
        row = std_char_numeric(qv)
        pred = [2.0, qv - 1 / qv, qv - 1 / qv, -1.0, -1.0, 0.0]
        m = max(abs(a - b) for a, b in zip(row, pred)) < 1e-9
        ok = ok and m
        print(f"     {qv:>20.16g}  {[round(x, 6) for x in row]}  {m}")
    print(f"\n  A1  chi^(2,1) = [2, h, h, -1, -1, 0] at every q ......... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => chi_std is a dot product with a FIXED vector, exactly like")
    print("         chi_sym and chi_alt already are. No inversion is needed.")
    assertions.append(("std_character_is_2_h_h_minus1_minus1_0", ok,
                       f"verified at q = {Q_TEST}"))

    # ── A2. The true Markov weights ───────────────────────────────────
    chi_sym = [sp.Integer(1), q, q, q ** 2, q ** 2, q ** 3]
    chi_alt = [sp.Integer(1), -1 / q, -1 / q, 1 / q ** 2, 1 / q ** 2, -1 / q ** 3]
    chi_std = [sp.Integer(2), h, h, sp.Integer(-1), sp.Integer(-1), sp.Integer(0)]
    TR_M = [sp.Integer(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]
    ys, yt, ya = sp.symbols("y_s y_t y_a")
    eqs = [sp.Eq(ys * chi_sym[i] + yt * chi_std[i] + ya * chi_alt[i], TR_M[i])
           for i in range(6)]
    sol = sp.solve([eqs[0], eqs[1], eqs[3]], [ys, yt, ya], dict=True)[0]
    y = {k: sp.simplify(v) for k, v in
         (("sym", sol[ys]), ("std", sol[yt]), ("alt", sol[ya]))}
    resid = [sp.simplify(chi_sym[i] * sol[ys] + chi_std[i] * sol[yt]
                         + chi_alt[i] * sol[ya] - TR_M[i]) for i in (2, 4, 5)]
    norm = sp.simplify(sol[ys] + 2 * sol[yt] + sol[ya])
    ok = all(r == 0 for r in resid) and norm == 1
    print("\n  2. solving  sum_lam y_lam chi^lam = TR_M  on the NF basis")
    for k in ("sym", "std", "alt"):
        print(f"     y_{k:4s} = {y[k]}")
    print(f"     residuals on the unused equations: {resid}")
    print(f"     normalisation y_sym + 2 y_std + y_alt = {norm}")
    print(f"\n  A2  the Markov weights are exact and consistent .......... "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("markov_weights_solve_exactly", ok,
                       f"y = {y}; residuals {resid}; norm {norm}"))

    # ── A3. W is not y; W is the q-Plancherel measure ─────────────────
    D = q ** 4 + 4 * q ** 2 + 1
    W = {"sym": q ** 2 / D, "std": (q ** 2 + 1) ** 2 / D, "alt": q ** 2 / D}
    differ = {k: sp.simplify(W[k] - y[k]) != 0 for k in W}
    plancherel = sp.simplify(q ** 2 + (q ** 2 + 1) ** 2 + q ** 2 - D) == 0
    ok = all(differ.values()) and plancherel
    print("\n  3. W_SYM/W_STD/W_ALT versus the Markov weights")
    for k in ("sym", "std", "alt"):
        print(f"     W_{k:4s} = {sp.simplify(W[k])}")
    print(f"     differs from y in every component: {differ}")
    print(f"     numerators are d^2 for d = (q, q^2+1, q), summing to D: "
          f"{plancherel}")
    print(f"\n  A3  W is the q-PLANCHEREL measure, not the trace weight .. "
          f"{'PASS' if ok else 'FAIL'}")
    print("      d_std/d_sym = (q^2+1)/q = q + 1/q = [2]_q. W is a coherent")
    print("      object in its own right — it is simply the wrong one here.")
    assertions.append(("W_is_plancherel_not_the_markov_weight", ok,
                       f"differs {differ}; d^2 sums to D {plancherel}"))

    # ── A4. y_alt = 0 IS the documented Gram radical ──────────────────
    Gm = np.asarray(G3, dtype=float)
    rad = np.asarray(RADICAL, dtype=float)
    alt = np.array([float(x) for x in _ALT_EIG_FRAC])
    same_vec = float(np.max(np.abs(rad - alt)))
    annih = float(np.max(np.abs(Gm @ rad)))
    ok = (y["alt"] == 0) and same_vec < 1e-3 and annih < 1e-12
    print("\n  4. y_alt = 0 and the Gram radical are the SAME fact")
    print(f"     RADICAL vs _ALT_EIG_FRAC: max diff {same_vec:.2e} "
          f"(the 111/100 vs q_0 pin)")
    print(f"     ||G . RADICAL||_inf = {annih:.3e}")
    print(f"     y_alt = {y['alt']}")
    print(f"\n  A4  the trace annihilates the sign block, hence det G = 0 . "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => tr_M carries NO chi_alt information, so the function's")
    print("         THREE-term inversion was wrong in shape, not just in")
    print("         coefficients. The correct inversion is two-term.")
    assertions.append(("y_alt_zero_is_the_gram_radical", ok,
                       f"y_alt = {y['alt']}; |G.rad| = {annih:.2e}"))

    print("\n### OPTIONS (no fix applied)")
    print("    A  fix the inversion:  chi_std = (tr_M - y_sym chi_sym)/y_std")
    print("       local, W_* untouched; still a division-derived quantity.")
    print("    B  RECOMMENDED — compute chi_std directly from")
    print("       _STD_CHI_FRAC = [2, h, h, -1, -1, 0]. Removes the asymmetry")
    print("       that caused the bug; no weights, no division, no convention")
    print("       question; smallest diff; correct by construction.")
    print("    C  change W_* to the Markov weights. NOT recommended: real")
    print("       consumers (molecular.py 121/124/125, vertex_volume,")
    print("       qou-mass hecke_core 230-232) would move, and it breaks a")
    print("       correct object to serve a broken one.")
    print("    D  leave it flagged. Zero call sites today, but it is")
    print("       re-exported from four modules and reads as usable.")
    print("    Separately, whichever is chosen: the exact path evaluates at")
    print("    111/100, not q_0. A caller wanting q_0 needs a q parameter.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("nf-channel-exact-repair-options",
                                engine="sympy", output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): settles the diagnosis of "
                "pyhecke.atom.nf_channel_exact so the repair decision can be "
                "made on facts, and lays out four options with blast radius. NO "
                "FIX APPLIED. The function computes chi_sym and chi_alt "
                "directly but chi_std by subtraction with W_SYM/W_STD/W_ALT, "
                "and that fails twice over. (1) Solving sum y_lam chi^lam = "
                "TR_M exactly gives y = ((q^4+1)/(q^2+1)^2, q^2/(q^2+1)^2, 0), "
                "consistent on all six equations and normalised, which differs "
                "from W in every component; W's numerators are d^2 for "
                "d = (q, q^2+1, q) summing to D, so W is the q-PLANCHEREL "
                "measure — a coherent object, just not the trace weight. (2) "
                "y_alt = 0, so tr_M carries no chi_alt information and the "
                "three-term inversion was wrong in SHAPE, not merely in "
                "coefficients; and y_alt = 0 is the documented Gram radical, "
                "since RADICAL is _ALT_EIG_FRAC and G.RADICAL = 0 to 1.7e-16. "
                "The standard character needs no inversion at all: "
                "chi^(2,1) = [2, h, h, -1, -1, 0] exactly, verified against "
                "direct seminormal traces at five q. RECOMMENDED option B: add "
                "_STD_CHI_FRAC and dot with it, which removes the asymmetry "
                "that caused the bug. No fit; no B_AME; nothing wired.")
            wb.add_data("std_character_closed_form",
                        ["2", "h", "h", "-1", "-1", "0"])
            wb.add_data("markov_weights", {k: str(v) for k, v in y.items()})
            wb.add_data("W_constants", {k: str(sp.simplify(v))
                                        for k, v in W.items()})
            wb.add_data("W_differs_from_y", {k: bool(v) for k, v in differ.items()})
            wb.add_data("radical_vs_alt_max_diff", f"{same_vec:.3e}")
            wb.add_data("G_annihilates_radical", f"{annih:.3e}")
            wb.add_data("options", {
                "A": "chi_std = (tr_M - y_sym chi_sym)/y_std; local, W_* untouched",
                "B": "RECOMMENDED: _STD_CHI_FRAC = [2,h,h,-1,-1,0], direct dot",
                "C": "change W_* — NOT recommended, real consumers move",
                "D": "leave flagged — zero call sites but exported from four modules",
            })
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "DIAGNOSIS ONLY — no repair is applied. The choice among A-D is "
                "a substrate decision; this probe supplies the facts, including "
                "the blast radius of option C (W_SYM/W_STD/W_ALT are consumed "
                "arithmetically by pyhecke/molecular.py lines 121/124/125, "
                "pyhecke/atom.py line 333 vertex_volume, and "
                "qou-mass/.../_internal/hecke_core.py lines 230-232).")
            wb.add_caveat(
                "W_SYM/W_STD/W_ALT are NOT wrong in themselves — they are the "
                "q-Plancherel measure d_lam^2/sum d^2 with d = (q, q^2+1, q). "
                "The error is using them where the Markov trace weight belongs. "
                "Any fix should leave W alone and say what it is.")
            wb.add_caveat(
                "Separate decision, whichever option is taken: the exact-"
                "Fraction path evaluates at _Q_FRAC = 111/100, not q_0, which "
                "is why the 1-dim channels differ from a q_0 computation in the "
                "5th decimal. That is a design choice of the exact path, not "
                "part of this bug, but a caller wanting q_0 needs a q parameter.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
