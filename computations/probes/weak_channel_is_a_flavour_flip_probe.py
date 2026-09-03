#!/usr/bin/env python3
"""The weak channel is not a crossing — it is a change of `beta` assignment, and
its operator avoids the strong generator in exactly the direction nature takes.

WHAT WAS ASKED
--------------
Owner: is there a low-mass isotope where the weak channel is simplest to see;
what does the physics suggest; and can we see it formally in the tower?

THE PHYSICS POINTS AT TWO SYSTEMS, AND WE ALREADY HAVE BOTH
--------------------------------------------------------------
**`A = 1`, the free neutron.** `n -> p e- nu-bar`, mean life ~879 s. The
simplest weak process there is: a free neutron decays, a free proton does not.
Both nucleons are already built here.

**`A = 3`, tritium.** `3H -> 3He e- nu-bar`, `Q = 18.59 keV` — the lowest-Q beta
decay in nature, and for that reason the system neutrino-mass experiments use.
It is also **exactly the mirror pair this probe series has been computing all
along**, so both endpoints are in hand in every topology.

So the answer to "where is it simplest" is: at `A = 1` for the operator itself,
and at `A = 3` for a decay with two computed endpoints.

BETA DECAY IS NOT A CROSSING — IT IS A CHANGE OF `beta`
----------------------------------------------------------
`n = udd -> p = uud` is `d -> u`. In the flavour rule
(`nucleon_gen_chains`: `uu -> sigma`, `dd -> sigma^-1`, `ud -> average`) that
changes which template each of the three quark pairs receives:

    neutron  udd   beta = (1/2, 1/2, 1)
    proton   uud   beta = (0,   1/2, 1/2)

**No generator is involved.** That is why there is no free slot for the weak
force: the three per-nucleon slots — `3k` intra, `3k+1` EM, `3k+2` strong — are
all crossings, and the weak interaction is not a crossing at all. It is a move
between two words of the *same* algebra. The previous probe's finding that "the
weak channel has no generator assigned anywhere" is therefore not an omission in
the corpus; it is the right structure.

THE WEAK TRANSITION OPERATOR EXISTS, IS UNIQUE, AND IS NOT A CROSSING
------------------------------------------------------------------------
Right multiplication by `v_n` is invertible (`det = 1.067`), so there is a
unique `W` in `H_3` with

    v_n . W  =  v_p          verified to 1.15e-41

and it is nothing like a generator. Its distance to all six crossing templates
(`sigma`, average, `sigma^-1` on each of the two generators) is `0.99` or more,
while its identity coefficient is `0.9892` — so `W = 1 + small`, which is what
one expects when the two states differ by a single quark flavour.

THE STRUCTURAL ZERO, AND IT IS DIRECTIONAL
---------------------------------------------
In the normal-form basis `[gamma, sigma_0, sigma_1, L+, L-, e-]`:

    W(n -> p)[sigma_0]  =  0     exactly       (1.2e-32 at 30 dps,
                                                -5.2e-53 at 50 dps,
                                                 1.3e-82 at 80 dps)
    W(p -> n)[sigma_0]  = -0.00225962          stable at every precision

`sigma_0` is the **strong-channel generator** (`atom_gen_chains`: inter-nucleon
crossings on gen 0). So the weak transition operator has **no strong-generator
component in the `n -> p` direction, and a nonzero one in `p -> n`** — and
`n -> p` is precisely the direction that happens spontaneously in nature.

That is a formal asymmetry between the two directions, of the kind the owner
asked whether the tower could show. It is reported as an observation, not a
mechanism: nothing here derives the decay from it, and no claim is made that the
zero *causes* the asymmetry.

WHAT THE 0TH-ORDER TRACE CAN AND CANNOT SEE
----------------------------------------------
Under convention D `y_alt = 0` exactly, so the alt block is annihilated by the
Markov trace. `W` carries `20.0 %` of its block weight there — a fifth of the
weak transition operator is **invisible to the 0th-order observable**, which is
the situation the owner described for the tower generally. It is not, however, a
clean "weak lives in the radical": the nucleons themselves carry *more* alt
weight than `W` does (`30.8 %` for the proton, `37.9 %` for the neutron), so the
weak operator is if anything *less* hidden than the states it connects.

THE OBSERVABLES, WITH THE USUAL CAVEAT
-----------------------------------------
Taking `-log(tr_M)` as the mass-like quantity (the convention this series has
used throughout, since `L = log(tr_free/tr_atom)` is a difference of two of
them):

    A = 1   -log tr(p) = 0.463102   -log tr(n) = 0.744159
            the NEUTRON IS HEAVIER — correct ordering
            model n/p = 1.60690      experiment m_n/m_p = 1.00138

    A = 3   -log tr(3H) = 3.535505   -log tr(3He) = 3.024007
            3H IS HEAVIER than 3He — correct ordering, and 3H is the one
            that decays
            model difference 0.511498 on a scale of ~3.5, i.e. 14.5 %;
            experimentally Q/M ~ 6.6e-6

**Both orderings are right and both magnitudes are wrong by orders**, which is
the same position every quantity in this series has been in: these are
dimensionless traces with no mass normalisation applied. The ordering results
are worth something precisely because they are signs rather than scales.

DISCIPLINE
----------
No fit; nothing wired. `W` is solved for exactly and verified to `1.15e-41`. The
`sigma_0` zero is checked at three precisions to separate structure from
rounding. `Q(3H)` and `m_n/m_p` are quoted from standard values for ordering
comparison only; nothing is tuned to them.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] force_channels_are_separable_probe.py (no weak generator slot)
-- Ref: [probe] betas_are_forced_by_quark_content_probe.py (the flavour rule)
-- Ref: [code] pyhecke.atom.nucleon_gen_chains (uu/dd/ud -> beta templates)
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
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from pyhecke.atom import nucleon_gen_chains  # noqa: E402
from pyhecke.gram import _hm_mp  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

NF = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NAMES = ["gamma", "sigma_0", "sigma_1", "L+", "L-", "e-"]
# standard values, ordering comparison only
M_N_OVER_M_P = 1.00137841917
Q_TRITIUM_KEV = 18.592


def substrate(dps: int):
    mp.mp.dps = dps
    q = q_at(mp.mp.dps)
    return q, q - 1 / q


def nf(betas, h):
    v = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for _ in range(3):
        v = _hm_mp(v, mp.mpf(1), mp.mpf(0), 0, h)
        v = _hm_mp(v, mp.mpf(1), -h, 1, h)
    for c, g in ((betas[0], 0), (betas[1], 0), (betas[2], 1)):
        v = _hm_mp(v, mp.mpf(1), -mp.mpf(c) * h, g, h)
    v = _hm_mp(v, mp.mpf(1), mp.mpf(0), 0, h)
    v = _hm_mp(v, mp.mpf(1), mp.mpf(0), 0, h)
    return v


def rmul_word(v, word, h):
    for g in word:
        v = _hm_mp(v, mp.mpf(1), mp.mpf(0), g, h)
    return v


def transition(src, dst, h):
    """The unique W with src . W = dst, plus det of the multiplication map."""
    C = mp.matrix(6, 6)
    for k, w in enumerate(NF):
        col = rmul_word(list(src), w, h)
        for i in range(6):
            C[i, k] = col[i]
        # NOTE: columns are src . b_k — the map W |-> src . W is linear in W
    det = mp.det(C)
    W = mp.lu_solve(C, mp.matrix([dst[i] for i in range(6)]))
    chk = [mp.mpf(0)] * 6
    for k, w in enumerate(NF):
        col = rmul_word(list(src), w, h)
        for i in range(6):
            chk[i] += W[k] * col[i]
    err = max(abs(chk[i] - dst[i]) for i in range(6))
    return [W[i] for i in range(6)], det, err


def betas_of(quarks, h):
    g0, g1 = nucleon_gen_chains(list(quarks))
    mid = list(g0[3:-2]) + list(g1[3:])
    return tuple(mp.nstr(-mp.mpf(d) / h, 4) for _c, d in mid)


def main() -> int:
    assertions = []
    print("t7qv — the weak channel: a flavour flip, not a crossing")
    q, h = substrate(50)
    B_P = (0, mp.mpf(1) / 2, mp.mpf(1) / 2)
    B_N = (mp.mpf(1) / 2, mp.mpf(1) / 2, 1)
    vp, vn = nf(B_P, h), nf(B_N, h)

    # ── A1. beta decay is a change of beta assignment ─────────────────
    print("\n  1. n -> p is d -> u, i.e. a change of the beta ASSIGNMENT")
    bn = betas_of(("u", "d", "d"), h)
    bp = betas_of(("u", "u", "d"), h)
    ok = bn != bp
    print(f"     neutron udd -> beta = {bn}")
    print(f"     proton  uud -> beta = {bp}")
    print(f"     no generator is involved — the weak move is between two WORDS")
    print(f"     of the same algebra, not a crossing on a new slot. That is why")
    print(f"     the three per-nucleon slots (3k intra, 3k+1 EM, 3k+2 strong)")
    print(f"     are all occupied and none is free for weak.")
    assertions.append(("A1_weak_is_a_beta_reassignment", ok,
                       f"udd -> {bn} against uud -> {bp}, no generator involved"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the transition operator exists and is unique ──────────────
    print("\n  2. the weak transition operator W, with v_n . W = v_p")
    W, det, err = transition(vn, vp, h)
    ok = abs(det) > mp.mpf("1e-6") and err < mp.mpf("1e-30")
    print(f"     det of the multiplication map = {mp.nstr(det, 12)}  -> unique")
    print(f"     verified v_n . W = v_p to {float(err):.2e}")
    print(f"     W in NF coordinates:")
    for nm, c in zip(NAMES, W):
        print(f"        {nm:<8s} {mp.nstr(c, 14)}")
    assertions.append(("A2_transition_operator_unique_and_verified", ok,
                       f"det {mp.nstr(det, 8)}, residual {float(err):.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. W is not a crossing ───────────────────────────────────────
    print("\n  3. W is NOT a crossing on any generator")
    best = None
    for g in (0, 1):
        for lbl, dd in (("sigma", mp.mpf(0)), ("average", -h / 2),
                        ("sigma^-1", -h)):
            e = [mp.mpf(0)] * 6
            e[0] = mp.mpf(1)
            e = _hm_mp(e, mp.mpf(1), dd, g, h)
            d = max(abs(e[i] - W[i]) for i in range(6))
            if best is None or d < best[0]:
                best = (d, g, lbl)
    ok = best[0] > mp.mpf("0.5")
    print(f"     nearest of the six templates: gen {best[1]} {best[2]}, "
          f"distance {mp.nstr(best[0], 8)}")
    print(f"     identity coefficient of W = {mp.nstr(W[0], 10)}  ->  W = 1 + small,")
    print(f"     as expected when the two states differ by one quark flavour")
    assertions.append(("A3_W_is_not_a_crossing", ok,
                       f"nearest template at distance {mp.nstr(best[0], 6)}; "
                       f"identity coefficient {mp.nstr(W[0], 8)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. the directional structural zero ───────────────────────────
    print("\n  4. W avoids the STRONG generator — but only one way round")
    fwd, rev = {}, {}
    for dps in (30, 50, 80):
        qq, hh = substrate(dps)
        a, b = nf(B_P, hh), nf(B_N, hh)
        Wf, _d, _e = transition(b, a, hh)
        Wr, _d2, _e2 = transition(a, b, hh)
        fwd[dps], rev[dps] = Wf[1], Wr[1]
        print(f"     dps {dps:2d}   W(n->p)[sigma_0] = {mp.nstr(Wf[1], 6):>14s}"
              f"     W(p->n)[sigma_0] = {mp.nstr(Wr[1], 6)}")
    shrinks = abs(fwd[80]) < abs(fwd[30]) * mp.mpf("1e-20")
    stable = abs(abs(rev[80]) / abs(rev[30]) - 1) < mp.mpf("1e-6")
    ok = bool(shrinks and stable)
    print(f"     forward shrinks with precision ({shrinks}) -> STRUCTURAL zero")
    print(f"     reverse is stable ({stable}) -> genuinely nonzero")
    print(f"     sigma_0 is the STRONG-channel generator, and n -> p is the")
    print(f"     direction that happens spontaneously in nature. Reported as an")
    print(f"     observation; nothing here derives the decay from it.")
    assertions.append(("A4_directional_structural_zero", ok,
                       f"W(n->p)[s0] shrinks {mp.nstr(fwd[30], 4)} -> "
                       f"{mp.nstr(fwd[80], 4)}; W(p->n)[s0] stable at "
                       f"{mp.nstr(rev[80], 8)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. what the 0th-order trace cannot see ───────────────────────
    print("\n  5. how much of W is invisible to the 0th-order trace")
    q, h = substrate(50)
    vp, vn = nf(B_P, h), nf(B_N, h)
    W, _d, _e = transition(vn, vp, h)
    chi = {
        "sym": [mp.mpf(1), q, q, q ** 2, q ** 2, q ** 3],
        "std": [mp.mpf(2), h, h, mp.mpf(-1), mp.mpf(-1), mp.mpf(0)],
        "alt": [mp.mpf(1), -1 / q, -1 / q, q ** -2, q ** -2, -q ** -3]}
    frac = {}
    for lbl, v in (("proton", vp), ("neutron", vn), ("W", W)):
        c = {k: sum(a * b for a, b in zip(chi[k], v)) for k in chi}
        tot = sum(abs(x) for x in c.values())
        frac[lbl] = float(abs(c["alt"]) / tot)
        print(f"     {lbl:<8s} sym {mp.nstr(c['sym'], 9):>14s}  "
              f"std {mp.nstr(c['std'], 9):>14s}  alt {mp.nstr(c['alt'], 9):>14s}"
              f"   |alt|/tot {frac[lbl]:.4f}")
    ok = 0.1 < frac["W"] < 0.3 and frac["W"] < frac["proton"] < frac["neutron"]
    print(f"     convention D has y_alt = 0 EXACTLY, so alt is annihilated:")
    print(f"     {100 * frac['W']:.1f} % of W is invisible to the 0th-order trace")
    print(f"     but this is NOT 'weak lives in the radical' — the nucleons")
    print(f"     carry more alt weight ({100 * frac['proton']:.1f} %, "
          f"{100 * frac['neutron']:.1f} %) than W does")
    assertions.append(("A5_fraction_invisible_to_trace", ok,
                       f"|alt|/total: W {frac['W']:.4f}, p {frac['proton']:.4f}, "
                       f"n {frac['neutron']:.4f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. orderings right, magnitudes not ───────────────────────────
    print("\n  6. the two observables: orderings right, magnitudes not")
    z = q ** 3 / (q ** 2 + 1)
    t = [mp.mpf(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]
    trp = sum(a * b for a, b in zip(t, vp))
    trn = sum(a * b for a, b in zip(t, vn))
    mp_, mn = -mp.log(trp), -mp.log(trn)
    # A = 3, adjacent-chain bonds, from the measured bond constants
    L_pn, L_nn = mp.mpf("0.676821592386"), mp.mpf("0.907262265533")
    tr3h = trp * trn ** 2 * mp.e ** (-(L_pn + L_nn))
    tr3he = trp ** 2 * trn * mp.e ** (-2 * L_pn)
    m3h, m3he = -mp.log(tr3h), -mp.log(tr3he)
    ok = bool(mn > mp_ and m3h > m3he)
    print(f"     A=1  -log tr(p) = {mp.nstr(mp_, 9)}   -log tr(n) = "
          f"{mp.nstr(mn, 9)}   neutron heavier: {mn > mp_}")
    print(f"          model n/p = {mp.nstr(mn / mp_, 9)}   experiment "
          f"{M_N_OVER_M_P}")
    print(f"     A=3  -log tr(3H) = {mp.nstr(m3h, 9)}   -log tr(3He) = "
          f"{mp.nstr(m3he, 9)}   3H heavier: {m3h > m3he}")
    print(f"          and 3H is the one that decays (Q = {Q_TRITIUM_KEV} keV)")
    print(f"          model difference {mp.nstr(m3h - m3he, 8)} on a scale of "
          f"~3.5, i.e. {float(100 * (m3h - m3he) / m3h):.1f} %;")
    print(f"          experimentally Q/M is about 6.6e-6")
    print(f"     both ORDERINGS right, both MAGNITUDES wrong by orders — the")
    print(f"     usual position: dimensionless traces, no mass normalisation")
    assertions.append(("A6_orderings_right_magnitudes_not", ok,
                       f"n heavier than p and 3H heavier than 3He; model n/p "
                       f"{mp.nstr(mn / mp_, 6)} against {M_N_OVER_M_P}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The physics points at the free neutron (A=1) and tritium")
    print("  3H -> 3He (A=3, Q = 18.59 keV, the lowest-Q beta decay there is)")
    print("  — and both endpoints of the tritium decay are the mirror pair this")
    print("  series has been computing all along.")
    print("  Formally, beta decay is d -> u, which in the flavour rule is a")
    print("  change of the beta ASSIGNMENT, not a crossing. That explains why")
    print("  no generator slot is free for the weak force: it does not need one.")
    print("  The transition operator W with v_n . W = v_p exists and is unique,")
    print("  is nothing like a crossing (W = 1 + small), and has a structural")
    print("  zero in its sigma_0 coefficient — the STRONG generator — in the")
    print("  n -> p direction only, the direction nature actually takes. The")
    print("  reverse direction has a stable nonzero -0.00225962 there.")
    print("  A fifth of W is invisible to the 0th-order trace (convention D")
    print("  annihilates the alt block), though less of it than of the nucleons.")
    print("  Both mass orderings come out right, both magnitudes wrong.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Locates the weak channel. The simplest low-mass systems are the "
            "free neutron (A=1) and tritium 3H -> 3He (A=3, Q = 18.59 keV, the "
            "lowest-Q beta decay in nature), whose endpoints are the mirror "
            "pair this series already computes. Formally beta decay is d -> u, "
            "which under the flavour rule changes the beta ASSIGNMENT — "
            "neutron udd (1/2,1/2,1) to proton uud (0,1/2,1/2) — and involves "
            "no generator at all, which is why none of the three per-nucleon "
            "slots (3k intra, 3k+1 EM, 3k+2 strong) is free for weak: it does "
            "not need one. The unique W with v_n . W = v_p exists (det 1.067, "
            "residual 1.15e-41), is not a crossing (nearest template at "
            "distance 0.99, identity coefficient 0.9892), and has a STRUCTURAL "
            "ZERO in its sigma_0 coefficient — the strong-channel generator — "
            "in the n -> p direction only (1.2e-32, -5.2e-53, 1.3e-82 at 30, "
            "50, 80 dps), while p -> n holds a stable -0.00225962 there. n -> p "
            "is the direction that happens spontaneously. 20.0% of W's block "
            "weight sits in the alt block that convention D annihilates, so a "
            "fifth of it is invisible to the 0th-order trace — but less than "
            "the nucleons themselves carry (30.8% and 37.9%), so this is not "
            "'weak lives in the radical'. Both mass orderings come out right "
            "(neutron heavier than proton, 3H heavier than 3He) and both "
            "magnitudes wrong by orders.")
        wb.add_data("systems", {"A=1": "free neutron, tau ~ 879 s",
                                "A=3": f"3H -> 3He, Q = {Q_TRITIUM_KEV} keV"})
        wb.add_data("beta_assignment", {"neutron_udd": list(bn),
                                        "proton_uud": list(bp)})
        wb.add_data("W_nf_coords", [mp.nstr(c, 15) for c in W])
        wb.add_data("W_determinant", mp.nstr(det, 12))
        wb.add_data("W_residual", f"{float(err):.2e}")
        wb.add_data("sigma0_forward", {str(k): mp.nstr(v, 6)
                                       for k, v in fwd.items()})
        wb.add_data("sigma0_reverse", {str(k): mp.nstr(v, 9)
                                       for k, v in rev.items()})
        wb.add_data("alt_fraction", {k: f"{v:.6f}" for k, v in frac.items()})
        wb.add_data("orderings", {"minus_log_tr_p": mp.nstr(mp_, 12),
                                  "minus_log_tr_n": mp.nstr(mn, 12),
                                  "minus_log_tr_3H": mp.nstr(m3h, 12),
                                  "minus_log_tr_3He": mp.nstr(m3he, 12)})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE DIRECTIONAL ZERO IS AN OBSERVATION, NOT A MECHANISM. That "
            "W(n->p) has no sigma_0 component while W(p->n) does, and that "
            "n -> p is the spontaneous direction, is a genuine structural "
            "asymmetry — but nothing here derives beta decay from it, predicts "
            "a rate or a lifetime, or shows the zero is what makes one "
            "direction preferred. Establishing any of that would need a "
            "dynamical principle the construction does not currently have.")
        wb.add_caveat(
            "'W' IS THE ALGEBRAIC CONNECTOR, NOT A WEAK INTERACTION OPERATOR. "
            "It is defined purely by v_n . W = v_p, i.e. as whatever element "
            "carries one nucleon word to the other. Calling it the weak "
            "transition operator is an interpretation. In particular it "
            "carries no lepton content: the emitted electron and antineutrino "
            "appear nowhere, and the construction has no strand or generator "
            "for a neutrino at all.")
        wb.add_caveat(
            "The magnitudes are wrong by orders, as everywhere in this series. "
            "The model's n/p mass ratio is 1.607 against a physical 1.00138, "
            "and its 3H-3He splitting is 14.5% of the scale against a physical "
            "Q/M of 6.6e-6. Only the two ORDERINGS are being claimed, and they "
            "are claimed as signs rather than scales precisely because no mass "
            "normalisation has been applied.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
