#!/usr/bin/env python3
"""Three force channels, three rates, opposite signs — and they are EXACTLY
independent, tested rather than assumed.

WHAT WAS ASKED
--------------
Owner: *"The rates should probably differ based on whether it is em strong or
weak nuclear force. don't necessarily assume that these are independent."*

Both halves are answered here, and they come out opposite ways: the rates differ
enormously — by sign, not just magnitude — while the channels turn out to be
exactly independent, to machine precision, even in the regime where the strong
channel is not additive with *itself*.

THE CORPUS ALREADY LABELS THE CHANNELS BY GENERATOR
------------------------------------------------------
`pyhecke.atom` is explicit. `atom_gen_chains`: *"Inter-nucleon crossings (strong
force, gen 0)"*; `build_atom_nf`: *"Electrons: pe crossing (EM channel,
gen=1)"*. Lifted to the `3A`-strand braid this reads

    generator 3k+2   STRONG   inter-nucleon bond between nucleons k and k+1
    generator 3k+1   EM       electron (pe) crossing on nucleon k
    generator 3k     intra    the nucleon's own first quark-pair slot

**Caveat up front:** `atom_braid_word_3A` — the honest `3A`-strand builder —
contains **no electrons at all**. The EM channel exists only in the collapsed
`H_3` formalisms (`build_atom_nf`, `atom_gen_chains`). Putting one `sigma^-1`
per proton on that proton's own `3k+1` generator is therefore *my* lift of it,
faithful to `hm(nf, 1, -h, 1)` but not something the braid builder does. Every
EM number below inherits that choice.

THE RATE IS SET BY THE GENERATOR, NOT BY beta
------------------------------------------------
The electron crossing is `sigma^-1`, i.e. `beta = 1` — **the same beta the
strong n-n bond carries**. So placing one `beta = 1` crossing on each generator
of `H_9` is a controlled comparison: identical operator, different channel.

    gen 0  +0.437359834237   intra, on a proton
    gen 1  -0.599674300310   EM,    on a proton
    gen 2  +0.907262265533   STRONG
    gen 3  +0.506807726417   intra, on a neutron
    gen 4  -0.784421240488   EM,    on a neutron
    gen 5  +0.907262265533   STRONG
    gen 6  +0.506807726417   intra, on a neutron
    gen 7  -0.784421240488   EM,    on a neutron

**Same beta, opposite sign.** Strong binds (`+0.907`), EM anti-binds (`-0.600`
to `-0.784`), intra binds (`+0.437` to `+0.507`). The owner's expectation is
confirmed as strongly as it could be: the channel, not the crossing branch, sets
the rate.

AND THE CHANNELS DIFFER IN FLAVOUR DEPENDENCE TOO
----------------------------------------------------
    STRONG   flavour-INdependent — gens 2 and 5 agree to 12 digits, although
             one is flanked p-n and the other n-n. The strong bond's value
             depends only on its own `beta`; flavour enters solely through
             which `beta` the flavour rule assigns.
    EM       flavour-dependent — `-0.599674` on a proton, `-0.784421` on a
             neutron, 31 % apart.
    intra    flavour-dependent — `+0.437360` (p) against `+0.506808` (n).

THE CHANNELS ARE EXACTLY INDEPENDENT
---------------------------------------
Not assumed — measured, and in the hardest available case. Recall the strong
channel is **not** additive with itself once a non-adjacent band generator is
present: the residual is `-2.4e-1` at `3H`. Against that,

    3H    strong (all pairs) 2.017810479   EM -0.599674300
          both 1.418136178   sum 1.418136178   interference +6.7e-16
    3He   strong (all pairs) 1.676935518   EM -1.199348601
          both 0.477586918   sum 0.477586918   interference  0.0e+00

**Exactly zero interference**, fifteen orders below the strong sector's own
self-interference in the very same words. So the answer to *"don't necessarily
assume these are independent"* is that they are — the strong channel interferes
with itself and not at all with the EM channel. Multiple electrons are likewise
exactly additive among themselves (`-1.199348601 = 2 x -0.599674300`).

WHICH SETTLES WHAT TO COMPARE AGAINST NUCLEAR BINDING
--------------------------------------------------------
The EM term is large and anti-binding, so including it wrecks the experimental
comparison: `L(3H)/L(3He)` moves from `1.20327` (strong only) to `2.96938` with
electrons, against `1.09896` — because `3He`'s two electrons nearly cancel its
strong binding, `1.676936 - 1.199349 = 0.477587`.

That is not a defect, it is a scope statement. `AME` binding energies are
**nuclear** binding energies and carry no electron content, so the quantity to
compare with them is the **strong channel alone**. This retroactively justifies
the scope of the four preceding probes rather than undermining it: they used
strong-only because the electrons were missing, and strong-only turns out to be
the right comparand. The EM channel belongs to *atomic* mass and would need an
atomic-mass observable to test against.

WHAT IS NOT ADDRESSED
-----------------------
The weak channel. Nothing in `pyhecke.atom` assigns a generator to it, and no
weak crossing appears in any builder, so there is nothing here to measure. If
the weak force has a slot in this scheme it has not been written down.

DISCIPLINE
----------
No fit; nothing wired. Channel labels are quoted from the corpus's own comments,
not invented. The EM lift into the braid is flagged as a choice. `B_AME` is read
for the ratio comparison only.

-- Ref: [manuscript] bean t7qv
-- Ref: [code] pyhecke.atom.atom_gen_chains ("strong force, gen 0"),
   build_atom_nf ("Electrons: pe crossing (EM channel, gen=1)")
-- Ref: [probe] all_pairs_bonds_and_saturation_probe.py (strong self-interference)
-- Ref: [probe] chain_telescopes_and_ordering_sensitivity_probe.py
"""
from __future__ import annotations

import math
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

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

from codata_constants import (  # noqa: E402
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from pyhecke.atom import D_PN  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 30
_Q = mp.mpf(str(Q0))
_H = _Q - 1 / _Q
HF = float(_H)
DPN = float(D_PN)
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
_B9 = None


def blocks():
    global _B9
    if _B9 is None:
        parts, y, _c, _d, _m = load_cost("tritium")
        _B9 = [(y[i], [np.asarray(m, dtype=float)
                       for m in build_seminormal_matrices(list(p))[0]])
               for i, p in enumerate(parts)]
    return _B9


def nucleon_word(betas, g0: int, g1: int):
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -betas[0] * HF, g0), (1, -betas[1] * HF, g0),
          (1, -betas[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def bond_cd(a: str, b: str):
    if a == b == "p":
        return (1, 0.0)
    if a == b == "n":
        return (1, -HF)
    return (1, DPN)


def band(d: float):
    return [(1, 0.0, 5), (1, 0.0, 4), (1, 0.0, 3), (1, d, 2),
            (1, -HF, 3), (1, -HF, 4), (1, -HF, 5)]


def trM(word):
    tot = 0.0
    for wt, s in blocks():
        dim = s[0].shape[0]
        m = np.eye(dim)
        for c, dd, g in word:
            m = m @ (c * s[g] + dd * np.eye(dim))
        tot += wt * float(np.trace(m))
    return tot


def setup(order):
    base = []
    for k, x in enumerate(order):
        base += nucleon_word(B_P if x == "p" else B_N, 3 * k, 3 * k + 1)
    tf = trM(base)
    adj = []
    for k in range(len(order) - 1):
        c, d = bond_cd(order[k], order[k + 1])
        adj.append((c, d, 3 * k + 2))
    _c, dfar = bond_cd(order[0], order[-1])
    em = [(1, -HF, 3 * k + 1) for k, x in enumerate(order) if x == "p"]
    return base, tf, adj, band(dfar), em


def main() -> int:
    assertions = []
    print("t7qv — force channels: rates, signs, and independence")
    order_3h = ["p", "n", "n"]
    order_3he = ["p", "n", "p"]
    base, tf, adj, far, em = setup(order_3h)

    def L(w):
        return math.log(tf / trM(w))

    # ── A1. a beta=1 crossing on every generator ──────────────────────
    print("\n  1. same crossing (sigma^-1, beta = 1), every generator")
    per_gen = {}
    for g in range(8):
        per_gen[g] = L(base + [(1, -HF, g)])
        chan = ("STRONG" if g % 3 == 2 else
                "EM   " if g % 3 == 1 else "intra")
        nuc = order_3h[g // 3] if g % 3 != 2 else "-"
        print(f"     gen {g}  L = {per_gen[g]:+.12f}   {chan}   nucleon {nuc}")
    strong = [per_gen[2], per_gen[5]]
    emv = [per_gen[1], per_gen[4], per_gen[7]]
    intra = [per_gen[0], per_gen[3], per_gen[6]]
    ok = (min(strong) > 0 and max(emv) < 0 and min(intra) > 0)
    print(f"     STRONG binds (+), EM ANTI-binds (-), intra binds (+)")
    print(f"     same beta, OPPOSITE SIGN — the generator sets the rate, not beta")
    assertions.append(("A1_same_beta_opposite_sign_by_channel", ok,
                       f"strong {strong[0]:+.6f}, EM {emv[0]:+.6f}..{emv[1]:+.6f}, "
                       f"intra {intra[0]:+.6f}..{intra[1]:+.6f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. flavour dependence differs by channel ─────────────────────
    print("\n  2. flavour dependence differs by channel")
    d_strong = abs(per_gen[2] - per_gen[5])
    d_em = abs(per_gen[1] / per_gen[4] - 1)
    d_intra = abs(per_gen[0] / per_gen[3] - 1)
    ok = d_strong < 1e-12 and d_em > 0.1 and d_intra > 0.1
    print(f"     STRONG gens 2 vs 5 (flanked p-n vs n-n): |d| = {d_strong:.1e}")
    print(f"            -> flavour-INdependent; only its own beta matters")
    print(f"     EM     proton {per_gen[1]:+.9f} vs neutron {per_gen[4]:+.9f}"
          f"   {100 * d_em:.1f} % apart")
    print(f"     intra  proton {per_gen[0]:+.9f} vs neutron {per_gen[3]:+.9f}"
          f"   {100 * d_intra:.1f} % apart")
    assertions.append(("A2_channel_specific_flavour_dependence", ok,
                       f"strong flavour-independent to {d_strong:.1e}; EM "
                       f"{100 * d_em:.1f}% and intra {100 * d_intra:.1f}% "
                       f"flavour-split"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3/A4. exact independence, in the hardest case ────────────────
    print("\n  3. channel independence — tested where STRONG-STRONG fails")
    inter, selfint, chan = {}, {}, {}
    for order, lbl in ((order_3h, "3H"), (order_3he, "3He")):
        b2, tf2, adj2, far2, em2 = setup(order)

        def L2(w):
            return math.log(tf2 / trM(w))

        S = adj2 + far2
        Ls, Le, Lb = L2(b2 + S), L2(b2 + em2), L2(b2 + S + em2)
        inter[lbl] = Lb - (Ls + Le)
        singles = sum(L2(b2 + [a]) for a in adj2) + L2(b2 + far2)
        selfint[lbl] = Ls - singles
        chan[lbl] = (Ls, Le, Lb)
        print(f"     {lbl:<4s} strong(all pairs) {Ls:.12f}  EM {Le:.12f}")
        print(f"          both {Lb:.12f}  sum {Ls + Le:.12f}   "
              f"cross-channel interference {inter[lbl]:+.2e}")
        print(f"          strong-with-ITSELF non-additivity: "
              f"{selfint[lbl]:+.2e}")
    ok = (all(abs(v) < 1e-12 for v in inter.values())
          and all(abs(v) > 1e-2 for v in selfint.values()))
    print(f"     the strong channel interferes with itself and NOT AT ALL with EM")
    print(f"     — fifteen orders apart, in the very same words")
    assertions.append(("A3_channels_exactly_independent", ok,
                       f"cross-channel {[f'{v:+.1e}' for v in inter.values()]} "
                       f"against strong self-interference "
                       f"{[f'{v:+.1e}' for v in selfint.values()]}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    print("\n  4. electrons are additive among themselves")
    b3, tf3, _a, _f, em3 = setup(order_3he)
    L3 = lambda w: math.log(tf3 / trM(w))  # noqa: E731
    one = L3(b3 + [em3[0]])
    two = L3(b3 + em3)
    ok = abs(two - 2 * one) < 1e-12 and len(em3) == 2
    print(f"     3He has Z = {len(em3)} electrons")
    print(f"     one  {one:.12f}   two {two:.12f}   2x one {2 * one:.12f}"
          f"   |d| {abs(two - 2 * one):.1e}")
    assertions.append(("A4_electrons_additive_among_themselves", ok,
                       f"|L(2e) - 2 L(1e)| = {abs(two - 2 * one):.2e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. EM anti-binds ─────────────────────────────────────────────
    print("\n  5. the EM channel ANTI-binds")
    ok = chan["3H"][1] < 0 and chan["3He"][1] < 0
    print(f"     L_EM = {chan['3H'][1]:.9f} (3H, 1 electron), "
          f"{chan['3He'][1]:.9f} (3He, 2)")
    print(f"     L < 0 means tr(atom) > tr(free): the electron makes the system")
    print(f"     HEAVIER. Which is right for atomic mass — an electron carries")
    print(f"     0.511 MeV of mass against ~13.6 eV of EM binding.")
    assertions.append(("A5_em_antibinds", ok,
                       f"L_EM = {chan['3H'][1]:.9f} and {chan['3He'][1]:.9f}, "
                       f"both negative"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. so strong-only is the right comparand ─────────────────────
    print("\n  6. which settles what to compare against nuclear binding")
    e_m = float(AME_B_TRITIUM_MEV_VALIDATION) / float(AME_B_HE3_MEV_VALIDATION)
    r_strong = chan["3H"][0] / chan["3He"][0]
    r_both = chan["3H"][2] / chan["3He"][2]
    ok = abs(r_strong / e_m - 1) < abs(r_both / e_m - 1)
    print(f"     L(3H)/L(3He), strong only    {r_strong:.5f}"
          f"   ({100 * (r_strong / e_m - 1):+.1f} %)")
    print(f"     L(3H)/L(3He), with electrons {r_both:.5f}"
          f"   ({100 * (r_both / e_m - 1):+.1f} %)")
    print(f"     B(3H)/B(3He)                 {e_m:.5f}")
    print(f"     3He's two electrons nearly cancel its strong binding:")
    print(f"        {chan['3He'][0]:.6f} + ({chan['3He'][1]:.6f}) = "
          f"{chan['3He'][2]:.6f}")
    print(f"     AME binding energies are NUCLEAR and carry no electron")
    print(f"     content, so strong-only is the correct comparand. That")
    print(f"     retroactively justifies the scope of the preceding probes.")
    assertions.append(("A6_strong_only_is_the_right_comparand", ok,
                       f"strong-only {r_strong:.5f} "
                       f"({100 * (r_strong / e_m - 1):+.1f}%) beats with-EM "
                       f"{r_both:.5f} ({100 * (r_both / e_m - 1):+.1f}%) "
                       f"against {e_m:.5f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Both halves of the owner's note answered, and they land opposite")
    print("  ways. The rates differ enormously by channel — the SAME crossing")
    print("  (sigma^-1, beta = 1) gives +0.907 on a strong generator, -0.600 to")
    print("  -0.784 on an EM one, +0.437 to +0.507 on an intra one. Opposite")
    print("  signs: strong binds, EM anti-binds. The generator sets the rate,")
    print("  not the crossing branch. Strong is also flavour-INdependent where")
    print("  EM and intra are not.")
    print("  But the channels ARE independent, exactly — cross-channel")
    print("  interference is 6.7e-16 and 0.0, in the very same words where the")
    print("  strong channel interferes with ITSELF at -2.4e-1. Fifteen orders.")
    print("  And that settles a scope question: the EM term is large and")
    print("  anti-binding, so including it wrecks the ratio (2.969 against an")
    print("  experimental 1.099). AME binding is NUCLEAR, so strong-only is the")
    print("  right comparand — which justifies the earlier probes' scope.")
    print("  The weak channel has no generator assigned anywhere in the corpus,")
    print("  so there is nothing to measure for it.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Tests whether the bond falloff rates differ by force channel and "
            "whether the channels are independent. The corpus labels channels "
            "by generator: 3k+2 strong (inter-nucleon), 3k+1 EM (electron pe "
            "crossing), 3k intra. Placing the SAME crossing (sigma^-1, beta = "
            "1, the beta the strong n-n bond carries) on each generator of H_9 "
            "gives +0.907262265533 on strong generators, -0.599674300310 (p) "
            "and -0.784421240488 (n) on EM ones, and +0.437359834237 (p) / "
            "+0.506807726417 (n) on intra ones — same beta, opposite sign, so "
            "the generator sets the rate rather than the crossing branch. "
            "Strong is flavour-independent (gens 2 and 5 agree to 1e-12 though "
            "flanked p-n and n-n) where EM and intra are flavour-split by 31% "
            "and 16%. The channels are EXACTLY independent: cross-channel "
            "interference is +6.7e-16 (3H) and 0.0 (3He) in the very same "
            "words where the strong channel is non-additive with itself at "
            "-2.4e-1 and -1.7e-1, and multiple electrons are additive among "
            "themselves. EM anti-binds, so including it moves L(3H)/L(3He) "
            "from 1.20327 to 2.96938 against an experimental 1.09896; since "
            "AME binding energies are nuclear and carry no electron content, "
            "strong-only is the correct comparand, which justifies the scope "
            "of the preceding probes. The weak channel has no generator "
            "assigned anywhere in the corpus.")
        wb.add_data("channel_map", {"3k+2": "strong (inter-nucleon)",
                                    "3k+1": "EM (electron pe)",
                                    "3k": "intra (quark pair slot)"})
        wb.add_data("beta1_by_generator",
                    {str(g): f"{v:+.12f}" for g, v in per_gen.items()})
        wb.add_data("flavour_split", {"strong": f"{d_strong:.2e}",
                                      "EM_pct": f"{100 * d_em:.2f}",
                                      "intra_pct": f"{100 * d_intra:.2f}"})
        wb.add_data("cross_channel_interference",
                    {k: f"{v:+.3e}" for k, v in inter.items()})
        wb.add_data("strong_self_interference",
                    {k: f"{v:+.3e}" for k, v in selfint.items()})
        wb.add_data("channel_totals",
                    {k: {"strong": f"{v[0]:.12f}", "EM": f"{v[1]:.12f}",
                         "both": f"{v[2]:.12f}"} for k, v in chan.items()})
        wb.add_data("mirror_ratio", {"strong_only": f"{r_strong:.6f}",
                                     "with_EM": f"{r_both:.6f}",
                                     "experiment": f"{e_m:.6f}"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE EM LIFT INTO THE BRAID IS MINE, NOT THE CORPUS'S. "
            "atom_braid_word_3A contains no electrons at all — the EM channel "
            "appears only in the collapsed H_3 formalisms build_atom_nf and "
            "atom_gen_chains, as hm(nf, 1, -h, 1). Placing one sigma^-1 per "
            "proton on that proton's own 3k+1 generator is a faithful reading "
            "of that, but it is a reading. A different placement (a shared "
            "global EM generator, or extra electron strands) would change "
            "every EM number here, though the exact independence is unlikely "
            "to be an artefact of the placement since it survives the "
            "non-commuting all-pairs case.")
        wb.add_caveat(
            "THE WEAK CHANNEL IS NOT ADDRESSED because nothing in the corpus "
            "assigns it a generator or a crossing. The owner's note names "
            "three forces; only two are represented in pyhecke.atom. Whether "
            "the weak force is meant to occupy a slot in this scheme, or is "
            "deliberately absent, is not something this probe can settle.")
        wb.add_caveat(
            "The EM magnitude should not be read as an EM binding energy. "
            "L_EM = -0.5997 per electron is comparable in size to the strong "
            "bond constants, whereas physical atomic binding is ~13.6 eV "
            "against nuclear MeV. If the term is carrying electron REST MASS "
            "(0.511 MeV) rather than EM binding that is roughly the right "
            "scale, but nothing here establishes which, and the dimensionless "
            "traces carry no normalisation that would let one check.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
