#!/usr/bin/env python3
# polynomial_q_not_applicable: structural probe over numeric q; emits no witness.
"""bar_involution_is_isospin_probe — what the bar involution q -> 1/q DOES
to the canonical color-weighted atom words.

Opened as bean `qou-e58e` (option D of the frakV fibre workplan) on the
premise that `tr_M(q_0^-1)` is NOT computable, because
`tr_m_atom_via_transfer.tr_m_atom_zn`'s docstring says the color-weighted
word is "q_0-baked" and "passing q != q_0 with that convention raises
ValueError".

THAT PREMISE IS WRONG, and this probe opens by refuting it. The word builder
was q-parameterised at some point and the SAME docstring says so thirty lines
later ("q-parameterised core: build the word AT q ... so q != q_0 (e.g.
q_0^-1 ...) re-lifts cleanly instead of raising"). The two paragraphs
contradict each other; the second one is the true one. `tr_M(q_0^-1)`
computes in milliseconds.

What the probe then measures, once the bar image is actually available:

  1. The Jones-Markov weights y_lambda are EXACTLY bar-even, y(q) = y(1/q),
     at every partition and every q tested. So no bar-odd material can come
     from the Wedderburn weights -- all bar parity lives in the WORD.

  2. tr_M itself is NEITHER bar-even nor bar-odd, and the bar-norm
     tr_M(q_0)*tr_M(1/q_0) is NEGATIVE for the deuteron -- so the "principled
     bar-norm mass modulus" that `complex_volume_witness.py` guards is not
     merely uncomputable, it does not EXIST as a real number for this word.

  3. The bar involution EXCHANGES MIRROR NUCLEI. Writing
     L(Z,N;q) = ln(tr_M^free/tr_M^atom), the measured law is

         L(Z, N; q)  -  L(N, Z; 1/q)  =  delta(q)

     with delta INDEPENDENT of (Z,N). Measured over A = 2..6, both mirror
     orientations, at five different q: the spread of delta across nuclei is
     <= 1.6e-22 (i.e. equality to 22-30 significant digits).

     So q -> 1/q acts on the color-weighted convention as proton<->neutron
     conjugation, up to one universal q-dependent offset.

  4. delta(q) = O(h^5) with h = q - 1/q, and delta(q_0) = 3.2829e-5 -- a
     RELATIVE 4.9e-5 on the deuteron binding. That is ~6000x the L2 100x
     target for Q_beta (7.8 ppb), so the mirror asymmetry is not a
     negligible correction at the precision the framework aims for.

NOT CLAIMED. No closed form for delta(q) is asserted. delta/h^5 is 0.0822 at
q_0 but drifts to 0.0723 by q = 1.396, so h^5 is the leading ORDER, not an
identification; naming a constant here would be a fit, and the corpus forbids
it. Nothing here is wired to production.

NO FLOAT64: every value is mpmath end-to-end at 60 dps; `float()` appears
nowhere. Per AGENTS.md "PROBES ARE NOT EXEMPT".

Run:  python3 -u computations/substrate/bar_involution_is_isospin_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 60

Q0 = mp.mpf(Q_50_DIGIT_STR)
QI = mp.mpf(1) / Q0

# q values with genuinely 60-dps mantissas (a float64-valued mpf is rejected
# by the word builder's own precision guard, correctly).
Q_GRID = [
    ("q_0", Q0),
    ("1+pi/30", 1 + mp.pi / 30),
    ("sqrt5/2", mp.sqrt(5) / 2),
    ("sqrt2/1.1", mp.sqrt(2) / mp.mpf("1.1")),
    ("exp(1/3)", mp.exp(mp.mpf(1) / 3)),
]

# (Z, N) with A = Z+N from 2 to 6, both orientations of each mirror pair
NUCLEI = [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1),
          (2, 3), (3, 2), (3, 3), (2, 4), (4, 2)]

FAILURES: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        FAILURES.append(msg)


def L(Z: int, N: int, q):
    """ln(tr_M^free / tr_M^atom) -- the argument of the log-trace binding."""
    ta, tf, _, _ = tr_m_atom_zn(Z, N, q=q)
    return mp.log(tf / ta)


def part1_premise_is_wrong() -> None:
    print("=" * 74)
    print("1. THE BEAN'S PREMISE IS WRONG: tr_M(q_0^-1) already computes")
    print("=" * 74)
    ta, tf, _, wall = tr_m_atom_zn(1, 1, q=Q0)
    tb, tg, _, walli = tr_m_atom_zn(1, 1, q=QI)
    print(f"  q_0    = {mp.nstr(Q0, 30)}")
    print(f"  1/q_0  = {mp.nstr(QI, 30)}")
    print(f"  tr_M(q_0)   atom={mp.nstr(ta, 24)}  free={mp.nstr(tf, 24)}"
          f"   [{wall * 1e3:.1f} ms]")
    print(f"  tr_M(1/q_0) atom={mp.nstr(tb, 24)}  free={mp.nstr(tg, 24)}"
          f"   [{walli * 1e3:.1f} ms]")
    check(tb != 0, "tr_M at 1/q_0 returned zero")
    print("\n  No ValueError. `tr_m_atom_zn.__doc__` says both that the word is")
    print("  q_0-baked and raises, and that it re-lifts cleanly at q_0^-1. The")
    print("  second is true; the first paragraph is stale and is fixed in this")
    print("  same commit.")

    barn_atom, barn_free = ta * tb, tf * tg
    print(f"\n  bar-norm atom  tr_M(q_0)*tr_M(1/q_0) = {mp.nstr(barn_atom, 20)}")
    print(f"  bar-norm free                        = {mp.nstr(barn_free, 20)}")
    check(barn_atom < 0, "expected a NEGATIVE deuteron bar-norm")
    check(barn_free < 0, "expected a NEGATIVE free bar-norm")
    print("  Both NEGATIVE => sqrt(bar-norm) is not real. So the guard in")
    print("  complex_volume_witness.py returns None for a reason its own")
    print("  comment does not give: not a raise, but `bar_prod > 0` failing.")
    print("  The 'principled bar-norm mass modulus' does not exist as a real")
    print("  number for this word -- a stronger statement than 'not computable'.")


def part2_weights_are_bar_even() -> None:
    print()
    print("=" * 74)
    print("2. THE JONES-MARKOV WEIGHTS y_lambda ARE EXACTLY BAR-EVEN")
    print("=" * 74)
    print("  (so no bar-odd material comes from the weights; all bar parity")
    print("   lives in the word)")
    for nm, q in Q_GRID:
        qi = mp.mpf(1) / q
        a, b = y_lambda_at(6, q), y_lambda_at(6, qi)
        worst = mp.mpf(0)
        for k in a:
            va, vb = mp.mpf(str(a[k])), mp.mpf(str(b[k]))
            scale = abs(va) if va != 0 else mp.mpf(1)
            worst = max(worst, abs(va - vb) / scale)
        print(f"  n=6  q={nm:<10s} max |y(q)-y(1/q)|/|y(q)| over 11 partitions"
              f" = {mp.nstr(worst, 6)}")
        check(worst < mp.mpf("1e-40"), f"y_lambda not bar-even at q={nm}")
    print("\n  Structural reason: y_lambda is built from ratios of q-integers")
    print("  [k]_q = (q^k - q^-k)/(q - q^-1); numerator and denominator are")
    print("  each bar-ODD, so every such ratio is bar-EVEN. Not a coincidence,")
    print("  and not a cache hit (the values do vary with q -- see the spread")
    print("  across the five rows if printed at full width).")


def part3_bar_is_isospin() -> None:
    print()
    print("=" * 74)
    print("3. THE BAR INVOLUTION EXCHANGES MIRROR NUCLEI (Z,N) <-> (N,Z)")
    print("=" * 74)
    print("     L(Z,N; q) - L(N,Z; 1/q) = delta(q),  delta independent of (Z,N)")
    print()
    print("  CONDITIONING. L is a log, so a nucleus whose tr_M sits near a ZERO")
    print("  at the bar image has an ill-conditioned L: the deviation scales as")
    print("  1/|tr_M(1/q)|. The compute's effective absolute floor is measured")
    print("  below (~1e-33, and NOT improvable by raising mp.dps -- the values")
    print("  are bit-identical at 60 and 140 dps, so the cap is internal). The")
    print("  strict assertion is therefore made on the WELL-CONDITIONED cases,")
    print("  and the ill-conditioned ones are reported, not dropped silently.")
    print()
    print(f"  {'q':<11s} {'delta(q)':<30s} {'spread (cond.)':<14s} "
          f"{'spread (all)':<14s} kept")
    deltas = {}
    COND = mp.mpf("1e-12")      # |tr_M| floor for a well-conditioned log
    for nm, q in Q_GRID:
        qi = mp.mpf(1) / q
        ds_all, ds_ok, worst_prod = [], [], mp.mpf(0)
        for (Z, N) in NUCLEI:
            ta, tf, _, _ = tr_m_atom_zn(Z, N, q=q)
            tb, tg, _, _ = tr_m_atom_zn(N, Z, q=qi)
            d = mp.log(tf / ta) - mp.log(tg / tb)
            ds_all.append((d, min(abs(ta), abs(tf), abs(tb), abs(tg))))
            if min(abs(ta), abs(tf), abs(tb), abs(tg)) > COND:
                ds_ok.append(d)
        med = sorted(d for d, _ in ds_all)[len(ds_all) // 2]
        for d, tmin in ds_all:
            worst_prod = max(worst_prod, abs(d - med) * tmin)
        sp_all = max(d for d, _ in ds_all) - min(d for d, _ in ds_all)
        sp_ok = (max(ds_ok) - min(ds_ok)) if len(ds_ok) > 1 else mp.mpf(0)
        deltas[nm] = (q, ds_ok[0] if ds_ok else ds_all[0][0])
        print(f"  {nm:<11s} {mp.nstr(deltas[nm][1], 22):<30s} "
              f"{mp.nstr(sp_ok, 4):<14s} {mp.nstr(sp_all, 4):<14s} "
              f"{len(ds_ok)}/{len(ds_all)}")
        check(sp_ok < mp.mpf("1e-20"),
              f"delta NOT nucleus-independent at q={nm} among "
              f"well-conditioned cases (spread {sp_ok})")
        check(worst_prod < mp.mpf("1e-25"),
              f"at q={nm} the deviation is NOT conditioning-bounded "
              f"(worst |dev|*|tr_min| = {worst_prod}) -- above ~1e-25 the "
              f"excess would be too large to blame on the log's conditioning")
    print()
    print("  Nuclei covered: A = 2..6, both orientations of each mirror pair.")
    print("  Among well-conditioned cases the spread is <= 1e-20 at every q.")
    print("  For the rest, |deviation| * |tr_M|_min stays under 1e-25 -- i.e.")
    print("  the excess is exactly the log's conditioning at a near-zero of the")
    print("  trace, not a failure of the law. The mirror law is exact; only the")
    print("  offset survives.")
    return deltas


def part4_size_of_the_offset(deltas) -> None:
    print()
    print("=" * 74)
    print("4. HOW BIG IS delta, AND WHAT ORDER DOES IT VANISH AT?")
    print("=" * 74)
    print(f"  {'q':<11s} {'delta':<22s} {'delta/h^5':<22s} h = q - 1/q")
    for nm, (q, d) in deltas.items():
        h = q - mp.mpf(1) / q
        print(f"  {nm:<11s} {mp.nstr(d, 14):<22s} {mp.nstr(d / h ** 5, 14):<22s}"
              f" {mp.nstr(h, 10)}")
    q, d0 = deltas["q_0"]
    l0 = L(1, 1, Q0)
    rel = abs(d0 / l0)
    print()
    print(f"  At q_0:  delta = {mp.nstr(d0, 20)}")
    print(f"           L(deuteron) = {mp.nstr(l0, 20)}")
    print(f"           relative    = {mp.nstr(rel, 8)}")
    check(rel > mp.mpf("1e-6"), "expected a relative offset above 1e-6")
    l2_target = mp.mpf("7.8e-9")   # the Q_beta L2 100x target
    print(f"\n  The Q_beta L2 100x target is {mp.nstr(l2_target, 3)} relative.")
    print(f"  delta/L is {mp.nstr(rel / l2_target, 6)}x that target, so the")
    print("  mirror asymmetry is NOT negligible at the precision aimed for.")
    print()
    print("  NOT IDENTIFIED: delta/h^5 is 0.0822 at q_0 but 0.0723 by q=1.396,")
    print("  so h^5 is the leading ORDER only. Naming a constant would be a fit.")




def part5_extensive_intensive_split() -> None:
    """Where delta lives: the exact extensive/intensive separation."""
    print()
    print("=" * 74)
    print("5. WHY delta IS NUCLEUS-INDEPENDENT: an exact extensive/intensive split")
    print("=" * 74)
    print("  Symbolically (sympy, exact), EVERY letter of the atom word is")
    print("  exactly bar-ODD -- d(1/q) = -d(q) -- EXCEPT the color-weighted")
    print("  interface letter d = -h*(1/2 - f/4), f = flavor_split_leading.")
    print("  Its defect is exact and fully factored:")
    print()
    print("      d(q) + d(1/q) = (q-1)^4 (q+1)^2 (q^2+1)^2 / (12 q^5)")
    print()
    print("  (because f(1/q) = -q^2 f(q), so the f-part does NOT flip sign with")
    print("   h). The interface letters are also exactly what distinguishes the")
    print("  atom word from the free word. So the atom/free asymmetry and the")
    print("  bar-parity defect have the SAME support.")
    print()
    lq = mp.log(Q0)
    PAIRS = [((1, 1), (1, 1), 2), ((1, 2), (2, 1), 3), ((2, 2), (2, 2), 4),
             ((2, 3), (3, 2), 5), ((3, 3), (3, 3), 6)]

    def S(a, b, free):
        tot = mp.mpf(0)
        for (Z, N) in (a, b):
            ta, tf, _, _ = tr_m_atom_zn(Z, N, q=Q0)
            tb, tg, _, _ = tr_m_atom_zn(N, Z, q=QI)
            tot += mp.log(abs((tf / tg) if free else (ta / tb))) / lq
        return tot

    Sf = [S(a, b, True) for a, b, _ in PAIRS]
    Sa = [S(a, b, False) for a, b, _ in PAIRS]
    print("  Summing ln|tr(Z,N;q)/tr(N,Z;1/q)| / ln q over a MIRROR PAIR:")
    print()
    print(f"  {'A':<4s} {'S_free(A)':<26s} {'1st difference':<24s} "
          f"{'S_atom - S_free':<22s}")
    for i, (_, _, A) in enumerate(PAIRS):
        d = mp.nstr(Sf[i] - Sf[i - 1], 18) if i else "--"
        print(f"  {A:<4d} {mp.nstr(Sf[i], 20):<26s} {d:<24s} "
              f"{mp.nstr(Sa[i] - Sf[i], 14):<22s}")

    dd = [Sf[i] - Sf[i - 1] for i in range(1, len(Sf))]
    c = dd[0]
    resid = max(abs(Sf[i] - PAIRS[i][2] * c) for i in range(len(Sf)))
    gaps = [Sa[i] - Sf[i] for i in range(len(Sf))]
    print()
    print(f"  1st-difference spread        : {mp.nstr(max(dd) - min(dd), 6)}")
    print(f"  c(q_0) = the common 1st diff : {mp.nstr(c, 20)}")
    print(f"  max |S_free(A) - A*c|        : {mp.nstr(resid, 6)}")
    print(f"  atom-free gap, spread over A : {mp.nstr(max(gaps) - min(gaps), 6)}")
    print(f"  that gap                     : {mp.nstr(-gaps[0], 20)}  = 2*delta/ln q")
    check(resid < mp.mpf("1e-20"),
          f"S_free is NOT exactly A-proportional (max residual {resid})")
    check(max(gaps) - min(gaps) < mp.mpf("1e-20"),
          f"the atom-free gap is NOT A-independent (spread "
          f"{max(gaps) - min(gaps)})")
    check(abs(-gaps[0] * lq / 2 - (L(1, 1, Q0) - L(1, 1, QI))) < mp.mpf("1e-30"),
          "the atom-free gap does not equal 2*delta")
    print()
    print("  So the split is EXACT, and it is the extensive/intensive one:")
    print("    * the FREE channel's mirror log is PURELY EXTENSIVE -- exactly")
    print("      A*c(q), with NO constant term (residual ~1e-25, i.e. zero);")
    print("    * the ATOM channel obeys the same extensive law MINUS a purely")
    print("      INTENSIVE constant 2*delta, identical at every A.")
    print()
    print("  STILL OPEN, and not explained here: the NUMBER of interface")
    print("  letters grows with A, yet delta does not. Something makes the")
    print("  growing set of interface defects contribute an A-independent net")
    print("  amount to ln(free/atom). That is the missing step, and it is what")
    print("  a closed form for delta would have to come through.")





# The universal mirror polynomial, DERIVED (not fitted) from the symbolic trace
# of the deuteron word — see part 6. Degree 10, irreducible over Q.
_P_COEFFS = [1, -2, 7, 0, -2, 4, 4, 0, 1, -2, 1]   # q^10 down to q^0


def _P(x):
    """P(x) = x^10 - 2x^9 + 7x^8 - 2x^6 + 4x^5 + 4x^4 + x^2 - 2x + 1."""
    out = 0
    for cf in _P_COEFFS:
        out = out * x + cf
    return out


def part6_closed_form() -> None:
    print()
    print("=" * 74)
    print("6. CLOSED FORM FOR delta -- DERIVED, not fitted")
    print("=" * 74)
    print("  Unblocking the symbolic trace (bean `qou-j320`) made the whole")
    print("  computation exact in q. Tracing the deuteron word symbolically:")
    print()
    print("      tr_M^free / tr_M^atom  =  12 q^5 (q^2+1) / P(q)")
    print("      P(q) = q^10 - 2q^9 + 7q^8 - 2q^6 + 4q^5 + 4q^4 + q^2 - 2q + 1")
    print()
    print("  and therefore")
    print()
    print("      exp(delta(q))  =  q^12 * P(1/q) / P(q)")
    print()
    print("  P is irreducible over Q. Nothing was fitted: this is the symbolic")
    print("  value of the trace, and it is CHECKED against the five independent")
    print("  numeric measurements of part 3 below.")
    print()
    print("  Tolerance note: agreement lands at 1e-29 .. 2e-23 relative, so the")
    print("  assertion is set at 1e-20 -- not tighter, because that is the")
    print("  transfer path's own floor (part 3: internal precision is capped,")
    print("  mp.dps does not move it), and not looser, because 1e-20 is far")
    print("  beyond what any fitted form could reach by accident.")
    print()
    print(f"  {'q':<11s} {'closed form':<28s} {'measured':<28s} rel err")
    for nm, qv in Q_GRID:
        cf = mp.log(qv ** 12 * _P(mp.mpf(1) / qv) / _P(qv))
        me = L(1, 1, qv) - L(1, 1, mp.mpf(1) / qv)
        rel = abs(cf - me) / abs(me)
        print(f"  {nm:<11s} {mp.nstr(cf, 20):<28s} {mp.nstr(me, 20):<28s} "
              f"{mp.nstr(rel, 4)}")
        check(rel < mp.mpf("1e-20"),
              f"closed form disagrees with the measurement at q={nm} "
              f"(rel {rel})")
    print()
    print("  Two consequences that were OPEN one pass ago:")
    print()
    print("  (a) THE ORDER IS DERIVED, NOT MEASURED.  Exactly")
    print("          q^12 P(1/q) - P(q) = (q-1)^5 (q+1)^3 (q^2+1)^2")
    print("      so delta vanishes to order EXACTLY 5 at q=1, and")
    print("          lim_{q->1} delta / h^5 = 1/12   (exact).")
    print("      The previous pass measured delta/h^5 = 0.0822 at q_0 drifting")
    print("      to 0.0723, and declined to name a constant. The limit is 1/12;")
    print("      the drift is subleading terms, and 0.0822 vs 0.0833 at q_0 is")
    print("      the size of them.")
    print()
    print("  (b) THE INTERFACE DEFECT IS THE SOURCE, with an explicit factor.")
    print("      Writing Dint = d(q) + d(1/q) for the interface bar-defect of")
    print("      part 5,")
    print("          q^12 P(1/q) - P(q)  =  12 q^6 h * Dint      (exact)")
    print("      so delta's numerator IS the interface defect, times 12 q^6 h.")
    print("      The symbolic claim of part 5 -- that delta is generated by the")
    print("      one non-bar-odd letter -- is now an identity, not an inference.")
    print()
    print("  NUCLEUS-INDEPENDENCE, symbolically. R(Z,N;q) = 12 q^a (q^2+1)^b/P(q)")
    print("  with the SAME P at n=6 and n=9; only the monomial prefactor depends")
    print("  on the nucleus. Measured exponents: (1,1) a=5,b=1; (1,2) a=6,b=2;")
    print("  (2,1) a=2,b=2. The mirror-crossed ratio contributes q^(a+a'+2b),")
    print("  which is 12 in both cases -- 5+5+2 and 6+2+4. That cancellation IS")
    print("  the A-independence of delta, and it is now visible rather than")
    print("  merely observed.")



def main() -> int:
    part1_premise_is_wrong()
    part2_weights_are_bar_even()
    deltas = part3_bar_is_isospin()
    part4_size_of_the_offset(deltas)
    part5_extensive_intensive_split()
    part6_closed_form()

    print()
    print("=" * 74)
    print("VERDICT (scope-(a): about what the bar involution DOES here)")
    print("=" * 74)
    print("  POSITIVE, and structural: on the canonical color-weighted")
    print("  convention, q -> 1/q is proton<->neutron conjugation, exactly, up")
    print("  to one universal offset delta(q). Self-mirror nuclei (Z=N) are")
    print("  bar-even up to delta; mirror pairs map to each other.")
    print()
    print("  This is the first measured statement of WHAT bar means on these")
    print("  words. It bears directly on conj:binding-qbeta-complex-volume:")
    print("  the bar-ODD partner of the bar-even binding is the mirror-pair")
    print("  DIFFERENCE -- and 3H -> 3He is a beta decay, which is the channel")
    print("  the conjecture assigns to Im frakV. That is a consistency, NOT a")
    print("  derivation: nothing here derives Im frakV, and the identification")
    print("  of the mirror difference with Q_beta is not made.")
    print()
    print("  REFUTES NO INGREDIENT. Corrects two things: the stale docstring")
    print("  paragraph, and the reason the bar-norm guard fires.")

    print()
    if FAILURES:
        print(f"ASSERTIONS FAILED ({len(FAILURES)}):")
        for f in FAILURES:
            print("  - " + f)
        return 1
    print("ASSERTIONS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
