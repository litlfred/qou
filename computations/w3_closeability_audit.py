#!/usr/bin/env python3
"""
w3_closeability_audit.py — is the body-order weight `w_3` CLOSEABLE at all?

Follow-on to `binding_n3_forcing_probe.py` (bean qou-hh9q, audit
docs/audits/2026-08-26-n3-body-order-forcing.md), which established that the two
stated anchors of `conj:binding-manybody-eq-jet-filtration` leave exactly one
free parameter and that A=3 therefore DEFINES the n=3 term rather than testing
it. That result is verified here, not re-derived; this probe asks the next
question (bean qou-1xne):

  Is there ANY route in the corpus that determines `w_3`?

Four candidate routes are examined, each measured rather than asserted:

  R1  the na-Stokes period a_D^(3) itself      — DETERMINED, and it is not w_3
  R2  the SL2 depth-2 recurrence, tau          — CIRCULAR (consumes a_D^(3))
  R3  a third anchor at A>3                    — NONE; each isotope adds at
                                                  least as many unknowns
  R4  the n=4 magic form read as the n=4 TERM  — determines w_3, and REFUTES it
                                                  (unbound tritium)

Everything is mpmath end-to-end at the canonical COMPUTE_DPS; no float64
anywhere, `float()` never appears. Proton q0 pin (owner directive 2026-08-07).

EXPLORATORY — no production wiring, no fitted constant wired anywhere, no
witness emitted, no tier change. Where a number is obtained by inverting data it
is printed as EXTRACTION.
Audit: docs/audits/2026-08-29-w3-closeability.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
sys.path.insert(0, str(HERE / "substrate"))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402 — PROTON pin (owner 2026-08-07)
from experimental_constants import M_E_MEV  # noqa: E402 — CAL-1 registry
from _li_2_q_util import flavor_split_leading  # noqa: E402
from coulomb_energy import R0_FM, alpha_em_hbar_c_mev_fm  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)

Q0 = Q_MP
M_E = mp.mpf(str(M_E_MEV))
ALPHA_HC = mp.mpf(str(alpha_em_hbar_c_mev_fm()))

# AME2020 total binding (MeV) — the comparison boundary, not model input.
B_AME = {"2H": AME_B_DEUTERON_MEV_VALIDATION, "3H": mp.mpf("8.481821"),
         "3He": mp.mpf("7.718058"), "4He": AME_B_HE4_MEV_VALIDATION}
ZA = {"2H": (1, 2), "3H": (1, 3), "3He": (2, 3), "4He": (2, 4)}


# ------------------------------------------------------- na-Stokes SW period
def qint(k: int) -> "mp.mpf":
    return (Q0 ** k - Q0 ** (-k)) / (Q0 - Q0 ** (-1))


def qfac(n: int) -> "mp.mpf":
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def partitions(n: int, m: int | None = None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]


def dimq(lam) -> "mp.mpf":
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d


def a_D(n: int) -> "mp.mpf":
    """na-Stokes SW jet period a_D^(n) = S(n)/n, S(n) = sum_{lam |- n} dim_q lam."""
    return mp.fsum([dimq(l) for l in partitions(n)]) / n


def alpha_E0() -> "mp.mpf":
    """alpha = E_0 = m_e/(q0(q0-1)) — the per-bond energy scale."""
    return M_E / (Q0 * (Q0 - 1))


def L_pn() -> "mp.mpf":
    """Convention-D colour-weighted p-n bond, writhe-normalised (exact mpmath)."""
    h = Q0 - 1 / Q0
    z = Q0 ** 3 / (Q0 ** 2 + 1)
    delta = mp.mpf(str(flavor_split_leading(Q0)))
    t = mp.mpf(1) / 2 - delta / 4
    d_pn = -h * t
    de_pn = 2 * t - 1
    return -mp.log(z + d_pn) - de_pn / 2 * mp.log(1 - h)


def e_coulomb(iso: str) -> "mp.mpf":
    Z, A = ZA[iso]
    if Z < 2:
        return mp.mpf(0)
    return (mp.mpf(3) / 5 * Z * (Z - 1) * ALPHA_HC
            / (mp.mpf(str(R0_FM)) * mp.mpf(A) ** (mp.mpf(1) / 3)))


def pct(x, ref) -> "mp.mpf":
    return (x - ref) / ref * 100


def line(c="-", n=78):
    print(c * n)


def main() -> int:
    print("=" * 78)
    print("IS w_3 CLOSEABLE?  four candidate routes, measured")
    print("bean qou-1xne * proton q0 pin * mpmath end-to-end, no float64")
    print("=" * 78)
    print(f"q0  = {mp.nstr(Q0, 20)}   (proton pin, q_parameter.Q_50_DIGIT_STR)")
    print(f"m_e = {mp.nstr(M_E, 12)} MeV   (CAL-1)")
    print(f"dps = {mp.mp.dps}")

    aD = {n: a_D(n) for n in range(2, 9)}
    alpha = alpha_E0()
    B2_derived = alpha * L_pn()
    w2_derived = B2_derived / (M_E * aD[2])
    w2_ame = B_AME["2H"] / (M_E * aD[2])
    G = mp.catalan
    vol_L6a4 = 8 * G
    B4_magic = mp.mpf(2) * M_E * 4 * vol_L6a4      # rho_F = 2, INPUT HYPOTHESIS

    # ---------------------------------------------------------------- R1
    line("=")
    print("R1 - IS a_D^(3) THE UNKNOWN?  (i.e. is `w_3 free` the same open item)")
    line()
    print("a_D^(n) = S(n)/n is a CLOSED FORM in q and n: a finite sum of q-hook")
    print("dimensions over partitions of n. It has no free parameter, no anchor")
    print("input, and no knot argument. Evaluated at the proton pin:")
    for n in range(2, 7):
        npart = len(list(partitions(n)))
        print(f"   a_D^({n}) = {mp.nstr(aD[n], 14):>16}   ({npart} partitions of {n})")
    print("\nThe q=1 limit is the involution number I(n)/n - the same object the")
    print("corpus's `sw-classical-jet-exactness` proof calls the classical binding")
    print("period, with Lean `involutionNumber_pos`. So a_D^(3) is DETERMINED.")
    print("\nWhat is NOT determined is the WEIGHT multiplying it. Under the")
    print("conjecture's DISPLAYED equation there is no weight (B_n = m_e*a_D^(n)),")
    print("and that reading is refuted at the deuteron:")
    print(f"   {'iso':>5} {'B_pred = m_e*Sum a_D':>22} {'B_AME':>10} {'err':>10}")
    for iso in ("2H", "3H", "4He"):
        A = ZA[iso][1]
        pred = M_E * mp.fsum([aD[n] for n in range(2, A + 1)])
        print(f"   {iso:>5} {mp.nstr(pred, 8):>22} {mp.nstr(B_AME[iso], 8):>10}"
              f" {mp.nstr(pct(pred, B_AME[iso]), 4):>9}%")
    print("\n=> VERDICT R1: `a_D^(3) unknown` and `w_3 free` are DIFFERENT items.")
    print("  a_D^(3) is a computed number; w_3 is the free coefficient in front of")
    print("  it. Counting them as one gap would UNDERCOUNT the open work by one.")

    # ---------------------------------------------------------------- R2
    line("=")
    print("R2 - DOES THE SL2 DEPTH-2 RECURRENCE DETERMINE a_D^(3) OR w_3?")
    line()
    print("`prop:sl2-prolongation-recurrence` states a_D^(n+2) = tau*a_D^(n+1) -")
    print("a_D^(n) with det B = 1, and says tau is \"solvable from three residue")
    print("weights via tau = (a_D^(2) + a_D^(4))/a_D^(3)\".")
    print("\nThat formula is the n=2 instance of the recurrence REARRANGED:")
    print("   a_D^(4) = tau*a_D^(3) - a_D^(2)   <=>   tau = (a_D^(2)+a_D^(4))/a_D^(3)")
    print("so it consumes a_D^(3) as an INPUT. Measured: define tau that way, then")
    print("ask what the recurrence predicts for a_D^(4). The residual is identically")
    print("zero for EVERY value substituted for a_D^(3) - an identity, not a test.")
    print(f"\n   {'a_3 substituted':>18} {'tau implied':>16} {'a_4 residual':>18}")
    for probe_a3 in (aD[3], aD[3] / 2, 3 * aD[3], mp.mpf(1), mp.mpf("0.001")):
        tau_p = (aD[2] + aD[4]) / probe_a3
        resid = tau_p * probe_a3 - aD[2] - aD[4]
        print(f"   {mp.nstr(probe_a3, 10):>18} {mp.nstr(tau_p, 10):>16}"
              f" {mp.nstr(resid, 6):>18}")
    print("\n  Every residual is 0 to the full working precision, by construction.")
    print("  => tau carries NO information about a_D^(3); it is a relabelling of it.")

    tau = (aD[2] + aD[4]) / aD[3]
    print("\nAnd the depth-2 form itself fails past the anchors it was solved on.")
    print(f"tau = {mp.nstr(tau, 12)}; iterate a_D^(n+2) = tau*a_D^(n+1) - a_D^(n)")
    print("from the TRUE a_D^(2), a_D^(3) and compare against the closed form:")
    rec = {2: aD[2], 3: aD[3]}
    print(f"   {'n':>3} {'recurrence':>16} {'closed form S(n)/n':>20} {'err':>10}")
    for n in range(4, 9):
        rec[n] = tau * rec[n - 1] - rec[n - 2]
        print(f"   {n:>3} {mp.nstr(rec[n], 10):>16} {mp.nstr(aD[n], 10):>20}"
              f" {mp.nstr(pct(rec[n], aD[n]), 4):>9}%")
    print("\n  => VERDICT R2: the SL2 route is CIRCULAR at n=3 (tau is defined from")
    print("    a_D^(3)) and, independently, its geometric growth cannot reproduce")
    print("    the super-exponential closed form past n=5. It supplies nothing.")
    print("    Confirms docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md;")
    print("    that refutation is NOT recorded in the proposition block itself.")

    # ---------------------------------------------------------------- R3
    line("=")
    print("R3 - IS THERE A THIRD ANCHOR?  the counting, isotope by isotope")
    line()
    print("Case 3a - FULL TOWER, K-independent weights, summed to n=A.")
    print("Each isotope of mass number A both supplies one datum AND introduces one")
    print("new unknown w_A. The two columns therefore move together, and the model")
    print("is saturated at every order: exactly determined, never predictive.")
    print(f"   {'through A':>10} {'unknowns w_2..w_A':>18} {'isotope data':>13}"
          f" {'predictions':>12} {'vs 2 stated anchors':>20}")
    for A in range(2, 8):
        unk = A - 1
        data = A - 1                       # one datum per mass number 2..A
        print(f"   {A:>10} {unk:>18} {data:>13} {unk - data:>12}"
              f" {unk - 2:>20}")
    print("  Column 4 is zero at every order: adding a heavier isotope buys exactly")
    print("  one more unknown, so the full tower can never test anything - every")
    print("  datum is consumed defining its own w_A. Column 5 is the deficit against")
    print("  the TWO anchors the conjecture actually states as derived (n=2, n=4),")
    print("  and it GROWS with A. Either way there is no third anchor for w_3.")
    print("  And the full-tower reading is independently REFUTED for A>=5")
    print("  (super-exponential a_D^(n) against B/A -> const;")
    print("  binding_wn_multianchor_tower_refute.py, ~+920% at 6Li).")

    print("\nCase 3b - FEW-BODY TRUNCATION (the corpus's own redirect), n_max = 3,")
    print("          B(K) = m_e*[a_2*w_2*M_2(K) + a_3*w_3*M_3(K)].")
    print("Now w_2, w_3 are shared, but each isotope carries its own multiplicity")
    print("pair (M_2, M_3): +1 equation, +2 unknowns. The deficit GROWS:")
    print(f"   {'isotopes':>10} {'unknowns':>10} {'equations':>10} {'free':>6}")
    for k in range(1, 6):
        unk = 2 + 2 * k
        print(f"   {k:>10} {unk:>10} {k:>10} {unk - k:>6}")
    print("  => a truncation only helps if M_n(K) is DERIVED from the canonical")
    print("    braid's topology, not extracted. That derivation is blocked upstream:")
    print("    the deuteron's canonical knot/link is UNDETERMINED - none of the")
    print("    three candidates is admissible (two by component-count arity, one by")
    print("    AME-inversion provenance), docs/audits/2026-08-21-deuteron-knot-")
    print("    assignment-adjudication.md. With no canonical braid there is no")
    print("    bond count, hence no derived M_n.")

    print("\nCase 3c - THE A=3 MIRROR PAIR, and why it is not a second equation.")
    ec = {iso: e_coulomb(iso) for iso in ("3H", "3He")}
    bs = {iso: B_AME[iso] + ec[iso] for iso in ("3H", "3He")}
    print(f"   E_C(3H)  = {mp.nstr(ec['3H'], 8)} MeV  (Z=1, identically 0)")
    print(f"   E_C(3He) = {mp.nstr(ec['3He'], 8)} MeV  (canonical derived r0 = hbar c/m_pi)")
    print(f"   B_strong(3H)  = {mp.nstr(bs['3H'], 10)} MeV")
    print(f"   B_strong(3He) = {mp.nstr(bs['3He'], 10)} MeV")
    print(f"   residual split = {mp.nstr(bs['3H'] - bs['3He'], 6)} MeV"
          f"  = {mp.nstr((bs['3H'] - bs['3He']) / bs['3H'] * 100, 4)}%")
    print("  Under a K-INDEPENDENT w_n both mirror partners give the SAME equation")
    print("  m_e(a_2 w_2 + a_3 w_3) = B_strong, so the pair is ONE equation plus a")
    print("  CONSISTENCY TEST of K-independence - it cannot constrain w_3 twice.")
    print("  Under a K-DEPENDENT w_n(K) they are two equations in two unknowns")
    print("  w_3(3H), w_3(3He) - again no constraint. Either way: no third anchor.")
    print("  The same argument disposes of the mirror SPLITTING as a candidate")
    print("  observable: under K-independence the model splitting is identically 0,")
    print("  so the splitting measures the Coulomb model, not w_3.")

    # ---------------------------------------------------------------- R4
    line("=")
    print("R4 - THE ONE ROUTE THAT WOULD SUPPLY A THIRD EQUATION, AND ITS FATE")
    line()
    print("`prop:magic-A-binding-formula` gives B = rho_F*m_e*A*8G with rho_F = 2.")
    print("Its own statement reads this as the nucleus's TOTAL binding (it is")
    print("compared to B_AME(4He) at +5.87%). But IF it were instead the n=4 TERM")
    print("alone, then A=4 supplies TWO independent facts - the derived term and")
    print("the measured total - and w_3 becomes DETERMINED with A=3 left free as a")
    print("genuine prediction. This is the only such route in the corpus. Test it.")
    print(f"\n   Vol(L6a4) = 8G     = {mp.nstr(vol_L6a4, 12)}")
    print(f"   B_magic            = {mp.nstr(B4_magic, 10)} MeV")
    print(f"   B_AME(4He)         = {mp.nstr(B_AME['4He'], 10)} MeV"
          f"   ({mp.nstr(pct(B4_magic, B_AME['4He']), 4)}%)")
    ec4 = e_coulomb("4He")
    bs4 = B_AME["4He"] + ec4
    print(f"   E_C(4He)           = {mp.nstr(ec4, 8)} MeV")
    print(f"   B_strong(4He)      = {mp.nstr(bs4, 10)} MeV")

    for tag, w2, b4 in (("derived-anchor w_2, AME total", w2_derived, B_AME["4He"]),
                        ("AME-anchor w_2, AME total", w2_ame, B_AME["4He"]),
                        ("derived-anchor w_2, Coulomb-corrected total",
                         w2_derived, bs4)):
        w4 = B4_magic / (M_E * aD[4])
        w3 = (b4 / M_E - aD[2] * w2 - aD[4] * w4) / aD[3]
        b3 = M_E * (aD[2] * w2 + aD[3] * w3)
        print(f"\n   {tag}:")
        print(f"     w_4 = B_magic/(m_e*a_4)  = {mp.nstr(w4, 10)}")
        print(f"     w_3 [DETERMINED, not extracted from A=3] = {mp.nstr(w3, 10)}")
        print(f"     positivity w_3 > 0 ?  {'YES' if w3 > 0 else 'NO'}")
        print(f"     monotone w_2 <= w_3 <= w_4 ?  "
              f"{'YES' if (w2 <= w3 <= w4) else 'NO'}")
        print(f"     => PREDICTION B(3H) = {mp.nstr(b3, 8)} MeV"
              f"   vs B_AME 8.481821  ({mp.nstr(pct(b3, B_AME['3H']), 5)}%)")
        print(f"     tritium bound (B > 0) ? {'YES' if b3 > 0 else 'NO'}")

    print("\n  Note the B(3H) prediction is IDENTICAL in rows 1 and 2: it reduces to")
    print("  B(3H) = B_total(4He) - B_magic, the w_2 terms cancelling. So the")
    print("  refutation does not depend on which n=2 anchor convention is used -")
    print("  it follows from B_magic EXCEEDING the measured 4He total by 5.87%.")
    print("\n  => VERDICT R4, scope (a): reading the magic form as the n=4 TERM does")
    print("    determine w_3 without touching A=3 - and the value it determines is")
    print("    NEGATIVE, violating the conjecture's own positivity/monotone-growth")
    print("    side constraint, and it predicts UNBOUND tritium. The arithmetic is")
    print("    forced: the magic value already EXCEEDS the measured 4He total, so")
    print("    the n=2 and n=3 terms must sum to a negative number.")
    print("    This is a scope-(a) refutation of the READING, not of the magic")
    print("    formula, whose own block reads it as the total. With that reading")
    print("    excluded, no route in the corpus supplies a third equation.")

    # ---------------------------------------------------------------- verdict
    line("=")
    print("VERDICT - IS w_3 CLOSEABLE?")
    line()
    print("NOT with anything now in the corpus. Scope (a) for each route, with one")
    print("scope-(b) exclusion already on main covering the recursion route:")
    print("  R1 a_D^(3) is DETERMINED and is a different object from w_3 - closing")
    print("     it does not close w_3, and the two must not be counted as one gap.")
    print("  R2 the SL2 depth-2 recurrence CONSUMES a_D^(3) to define tau (measured")
    print("     identity above) and its geometric growth is refuted past n=5.")
    print("  R3 no third anchor exists: heavier isotopes bring their own unknowns")
    print("     (full tower), a few-body truncation brings two per isotope, and the")
    print("     A=3 mirror pair is one equation plus a K-independence test.")
    print("  R4 the only reading that would supply a third equation determines w_3")
    print("     negative and predicts unbound tritium.")
    print("\nAlready proved on main, and it is the strongest statement available:")
    print("  QOU.Mass.BindingScalarKernelParityExclusion.no_scalar_kernel_on_carrier")
    print("  (sorry-free) - scope (b), invariant = the non-integral Newton slope 1/2")
    print("  of the rank-2 carrier, equivalently 2u - 2p = 1 unsolvable over Z. No")
    print("  scalar q-difference kernel R(q,x) acts on the carrier at ANY depth, so")
    print("  the conjecture's own stated mechanism for producing the weights cannot")
    print("  produce them. A rank-2 recursion needs TWO base cases, so the n=3 term")
    print("  is a REQUIRED INDEPENDENT INPUT rather than an output.")
    print("  Companion: kernel_coeff_existsUnique (sorry-free) - kernel coefficients")
    print("  and body terms are in bijection, so an unconstrained ansatz")
    print("  reparametrises the unknown, it does not remove it.")
    print("\nSo `w_3 free` is not a gap awaiting a longer computation. It is a")
    print("required boundary condition of a rank-2 problem, and the corpus supplies")
    print("exactly one boundary condition (n=2). Closing it needs a NEW measured or")
    print("derived input, not a rearrangement of the two anchors:")
    print("  (i) a genuinely per-knot period a_D^(n)(K) - no such object exists in")
    print("      computations/ (all ten a_D definitions take body order alone); or")
    print("  (ii) a DERIVED multiplicity M_n(K) from the canonical braid - blocked")
    print("      upstream by the undetermined deuteron knot assignment; or")
    print("  (iii) the second base case supplied by the ramified double cover the")
    print("      exclusion's own scope note names (adjoining q^(1/2), x^(1/2), which")
    print("      separates even from odd body orders) - untried, and the one route")
    print("      not excluded by anything measured here.")
    print("\nA w_3 obtained by inverting AME at A=3 is a FIT. It must be labelled")
    print("one and must not be wired to production as canonical.")
    line("=")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
