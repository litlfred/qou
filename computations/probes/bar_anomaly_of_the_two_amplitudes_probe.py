"""The Ocneanu framing ratio IS the bar-anomaly of the Markov parameter, and the
mass/binding amplitude asymmetry is exactly one framing quantum.

BEAN qou-brng, residual (ii).  `QOU.Mass.BrunnianBindingChannel` states the open
item in these words:

    "(ii) why the surviving count channel enters as a *bare integer* while the
     self/mass channel keeps the full q-dimension self-trace `lw`."

and `QOU.Mass.BindingMassRung` states the same thing from the other side --
"it does NOT derive *why* binding lacks the cusp factor".  This probe does not
close either.  What it does is replace a qualitative contrast ("q-dimension vs
integer") with an exact, single-quantity statement, and locate where that one
quantity lives.

DEFINITION.  For a Laurent-type expression X in q, write the BAR ANOMALY

    omega(X)  :=  X / bar(X),        bar : q -> 1/q.

omega(X) = 1 says X is bar-even; omega(X) = -1 says bar-odd.  A monomial
omega = q^k says X carries framing weight, in the sense made precise below.

THE FIVE RESULTS.

(1) bar(z) = z_-, EXACTLY, in convention D.  The negative-crossing loop value
    -- defined in `prop:markov-z-reconciliation` as z_- = z - (q - 1/q), forced
    by the Hecke quadratic relation from the one-sided stabilisation rule -- is
    the BAR CONJUGATE of the Markov parameter.  Consequence:

        a^2  =  z / z_-  =  z / bar(z)  =  omega(z),

    so the Ocneanu FRAMING RATIO is literally the bar-anomaly of z.  The corpus
    proves a^2 = q^4 sorry-free (`QOU.Information.markov_framing_ratio_eq`); what
    is added here is that this ratio is not merely a ratio which happens to be a
    monomial, but the bar-anomaly itself.

(2) It holds for the WHOLE Ocneanu family, with a one-line proof.  For
    z_N = q^N/[N]_q with the symmetric [N]_q = (q^N - q^-N)/(q - q^-1),

        z_N - bar(z_N)  =  (q^N - q^-N)/[N]_q  =  [N]_q * h / [N]_q  =  h

    identically in N.  So the Ocneanu family is exactly the family on which the
    BAR INVOLUTION and the HECKE QUADRATIC RELATION agree about what z_- is.

(3) Convention C fails precisely this, and the failure is sharper than
    "structureless".  z_C = 1/(q^{1/2} + q^{-1/2}) is BAR-EVEN, so bar(z_C) = z_C
    while the Hecke relation forces z_{C,-} = z_C - h /= z_C.  In C the bar
    involution says the negative-crossing loop value equals the positive one.
    This is INDEPENDENT of the empirical figures on record (195.8 ppm on
    tr_M(beta_Bor), -197 ppm on m_p) and independent of the corpus's existing
    structural argument (the log-derivative argument that C's a^2 is not q^t for
    any real t, in `markov-z-reconciliation.md`).  SCOPE: this probe does NOT
    establish that bar(z) = z_- is REQUIRED.  Both conventions satisfy
    tr_M(1) = (z - z_-)/h = 1 and both are admissible.  Whether bar-compatibility
    is a constraint or an aesthetic preference is not settled here.

(4) (1) EXPLAINS why the Ocneanu weights are bar-even.  Under bar the weight
    formula's numerator factor z q^c - z_- q^-c maps to z_- q^-c - z q^c and its
    denominator q^h - q^-h maps to q^-h - q^h: both flip sign, so each cell's
    factor is fixed and w_lambda is bar-even.  That is a CONSEQUENCE of bar(z) = z_-,
    not an independent fact, and it is confirmed numerically against the live
    producer `y_lambda_su_n` at 60 dps.

(5) THE AMPLITUDE ASYMMETRY IS ONE FRAMING QUANTUM.  With a = q^2 the convention-D
    framing quantum:

        omega(lw)          = 1        self-linking weight, bar-even
        omega(M)           = 1        binding multiplier -- ANY integer
        omega(h)           = -1       Hecke deformation, bar-odd
        omega(1/hbar_q^2)  = q^2 = a  the CAL-2 cusp factor: ONE framing quantum
        omega(z_D)         = q^4 = a^2

    so the MASS multiplier lw/hbar_q^2 carries exactly ONE Ocneanu framing quantum
    and the BINDING multiplier carries NONE.  That is the whole of residual (ii),
    as one exponent rather than a qualitative contrast.  And it is sl_2-specific:
    omega(1/hbar_q^2) = a = q^N holds at N = 2 and at no other N, and N = 2 is
    convention D, the sl_2 point of the Ocneanu family.

WHERE THE FRAMING QUANTUM IS NOT.  The obvious mechanism -- "the self channel
carries a writhe, the mutual channel of a Brunnian link has writhe zero
(`brunnian_signedChannel_zero`), so only the self channel is framed" -- does NOT
survive, and this probe records the refutation rather than the story.  The
canonical Borromean braid word is (sigma_1 sigma_2^-1)^3, of exponent sum ZERO,
and the checks below show every H_3 character of it is bar-even.  Since the
Ocneanu weights are bar-even too (result 4), tr_M(beta_Bor) is bar-even and the
trace contributes NO framing weight at all.  The entire anomaly of the mass
amplitude is in hbar_q, which is not a trace object: it enters from CAL-2,
m_mu/m_e = Vol(4_1)/hbar_q^2.

The mechanism behind that bar-evenness is AMPHICHIRALITY, not the exponent sum,
and the probe separates the two.  Bar acts on H_n(q) by sigma -> sigma^-1, with
NO sign: applying bar to sigma^2 = h sigma + 1 gives X^2 = -h X + 1 (h is
bar-odd), and sigma^-2 = -h sigma^-1 + 1 satisfies it while (-sigma^-1) does not.
The signed guess -sigma^-1 is checked and recorded as FAILING, because it is the
natural guess and it is wrong.  So bar sends a braid word to its MIRROR --
verified ENTRYWISE on rho(beta_Bor) -- and the Borromean link is amphichiral,
which is why its character is fixed.  A nonzero exponent sum does NOT by itself
force a bar anomaly: sigma_1 sigma_2 has exponent sum 2 and (2,1)-character the
constant -1, so it would have been a VACUOUS control.  The live control is
sigma_1 itself, whose character is h, bar-ODD.

PRECISION.  Everything here is EXACT symbolic sympy over the ring generated by
s = sqrt(q); there are no floats and no numerics of any kind, so no witness is
emitted and no anchor is read.  (The bar-evenness of the Ocneanu weights was
additionally confirmed against the live producer `y_lambda_su_n(3, q, 2)` at
mp.dps = 60, agreeing at q_0 and 1/q_0 to better than 1e-50, but that check
needs PYTHONPATH wiring and is deliberately not carried here -- result 4 derives
it symbolically instead.)  The exit code is the verdict, matching the sibling
`markov_loop_value_product_and_framing_ratio.py`.

So residual (ii) is RELOCATED, not closed: the question "why does binding lack
the cusp factor" is a question about the CAL-2 calibration, not about the
self-vs-mutual structure of the trace.  Stated as a scope-(a) negative per
AGENTS.md: this construction, alone, does not source the asymmetry from the
writhe.  No invariant is claimed to forbid a writhe-based route in general --
only that the canonical Borromean word cannot supply one, because its writhe is
zero.

CONTROL.  A writhe-bearing braid is checked alongside, so that "bar-even at
beta_Bor" is a measured fact about that word and not a triviality of the setup.

"""

from __future__ import annotations

import sys

import sympy as sp

CHECKS: list[tuple[str, bool]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((label, ok))
    mark = "ok  " if ok else "FAIL"
    print(f"  [{mark}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")


# --- exact setup: s = sqrt(q) so that convention C is expressible too ---------
s = sp.symbols("s", positive=True)
q = s ** 2


def bar(e):
    """The bar involution q -> 1/q, i.e. s -> 1/s."""
    return sp.cancel(sp.together(sp.sympify(e).subs(s, 1 / s)))


def omega(e):
    """Bar anomaly omega(X) = X / bar(X)."""
    return sp.cancel(sp.simplify(sp.sympify(e) / bar(e)))


def zero(e) -> bool:
    return sp.simplify(sp.together(sp.cancel(sp.sympify(e)))) == 0


h = q - 1 / q                      # Hecke deformation
hbar_q = 1 - 1 / q                 # CAL-2 cusp factor
lw = (3 * q ** 2 + 4 + 3 / q ** 2) / 4   # linking_weight_family_a
zD = q ** 3 / (q ** 2 + 1)         # convention D  (QOU.Information.markovZ)
zDneg = zD - h                     # forced by the Hecke quadratic relation
zC = 1 / (s + 1 / s)               # convention C  (excised for mass/binding)
a = q ** 2                         # Ocneanu framing quantum, convention D


def qint_sym(n: int):
    """Symmetric quantum integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return sp.cancel((q ** n - q ** (-n)) / (q - 1 / q))


def main() -> int:
    print()
    print("=" * 74)
    print("  bar-anomaly of the two amplitudes -- bean qou-brng residual (ii)")
    print("=" * 74)
    print()

    # ---- 1. bar(z) = z_- in convention D ------------------------------------
    print("1. The negative-crossing loop value is the bar conjugate of z")
    check("D: bar(z) == z_-  (exactly)", zero(bar(zD) - zDneg),
          f"bar(z_D) = {sp.cancel(bar(zD))}\n"
          f"z_-      = {sp.cancel(zDneg)}")
    check("D: the framing ratio IS the bar-anomaly, a^2 = z/bar(z) = omega(z)",
          zero(sp.cancel(zD / zDneg) - omega(zD)),
          f"omega(z_D) = {omega(zD)} = q^4 = a^2")
    check("D: a^2 = q^4, matching QOU.Information.markov_framing_ratio_eq",
          zero(sp.cancel(zD / zDneg) - q ** 4))
    print()

    # ---- 2. the whole Ocneanu family ----------------------------------------
    print("2. bar(z_N) = z_N - h for the WHOLE family z_N = q^N/[N]_q")
    print("   reason, one line:  z_N - bar(z_N) = (q^N - q^-N)/[N]_q = [N]_q h/[N]_q = h")
    fam_ok = True
    for n in range(1, 9):
        zN = sp.cancel(q ** n / qint_sym(n))
        if not zero(bar(zN) - (zN - h)):
            fam_ok = False
        if not zero(omega(zN) - q ** (2 * n)):
            fam_ok = False
    check("family: bar(z_N) = z_N - h and omega(z_N) = q^{2N}, for N = 1..8", fam_ok,
          "so the Ocneanu family is exactly where the BAR INVOLUTION and the\n"
          "HECKE QUADRATIC RELATION agree about what z_- is")
    check("D is the N = 2 member", zero(sp.cancel(q ** 2 / qint_sym(2)) - zD),
          f"q^2/[2]_q = {sp.cancel(q ** 2 / qint_sym(2))} = z_D")
    print()

    # ---- 3. convention C fails exactly this ---------------------------------
    print("3. Convention C: bar says z_- = z, the Hecke relation says z_- = z - h")
    check("C: z_C is BAR-EVEN", zero(bar(zC) - zC),
          f"bar(z_C) = {sp.cancel(bar(zC))} = z_C")
    check("C: bar(z_C) != z_C - h  (the two disagree)", not zero(bar(zC) - (zC - h)),
          f"bar(z_C) - (z_C - h) = {sp.cancel(bar(zC) - (zC - h))}, which is -(-h) = h != 0")
    check("C: omega(z_C) = 1, so C carries NO framing weight at all",
          zero(omega(zC) - 1),
          "yet its z_- is displaced from z by h -- that is the inconsistency")
    check("BOTH are admissible: tr_M(1) = (z - z_-)/h = 1 in each",
          zero((zD - zDneg) / h - 1) and zero((zC - (zC - h)) / h - 1),
          "SCOPE: this does NOT show bar-compatibility is REQUIRED; see docstring")
    print()

    # ---- 4. bar(z) = z_- explains bar-even Ocneanu weights -------------------
    print("4. bar(z) = z_- forces the Ocneanu weights to be bar-even")
    # Ocneanu weight over a partition: prod over cells of
    #   (z q^c - z_- q^-c) / (q^hook - q^-hook)
    # Under bar, numerator -> z_- q^-c - z q^c = -(num); denominator -> -(den).
    # (content, hook) per cell.  lambda = (2,1) has hooks 3,1,1 -- NOT 3,2,1.
    LAMBDA_3 = {
        "(3)": [(0, 3), (1, 2), (2, 1)],
        "(2,1)": [(0, 3), (1, 1), (-1, 1)],
        "(1,1,1)": [(0, 3), (-1, 2), (-2, 1)],
    }

    def ocneanu_weight(cells):
        return sp.cancel(sp.prod([(zD * q ** c - zDneg * q ** (-c)) / (q ** hk - q ** (-hk))
                                  for c, hk in cells]))

    num_den_ok = True
    for cells in LAMBDA_3.values():
        for c, hk in cells:
            if not zero(bar(zD * q ** c - zDneg * q ** (-c)) + (zD * q ** c - zDneg * q ** (-c))):
                num_den_ok = False
            if not zero(bar(q ** hk - q ** (-hk)) + (q ** hk - q ** (-hk))):
                num_den_ok = False
    check("each cell factor: numerator and denominator are BOTH bar-ODD",
          num_den_ok,
          "numerator  z q^c - z_- q^-c  ->  z_- q^-c - z q^c  = -(itself), USING bar(z) = z_-\n"
          "denominator q^hk - q^-hk     ->  q^-hk - q^hk      = -(itself)\n"
          "so their ratio is bar-EVEN, cell by cell, for every partition")
    weights = {lam: ocneanu_weight(cells) for lam, cells in LAMBDA_3.items()}
    check("every convention-D weight at n = 3 is bar-even",
          all(zero(bar(w) - w) for w in weights.values()),
          "\n".join(f"w_{lam} = {sp.factor(w)}" for lam, w in weights.items()))
    check("and they are the REGISTERED values: [4]_q/[2]_q^3, 1/[2]_q^2, 0",
          zero(weights["(3)"] - qint_sym(4) / qint_sym(2) ** 3)
          and zero(weights["(2,1)"] - 1 / qint_sym(2) ** 2)
          and zero(weights["(1,1,1)"]),
          "w_(1^3) = 0 is the sl_2 row bound, not a coincidence of the trace")
    print()

    # ---- 5. the bar-anomaly table -------------------------------------------
    print("5. The amplitude asymmetry is ONE framing quantum")
    check("omega(lw) = 1            (self-linking weight is bar-even)",
          zero(omega(lw) - 1))
    check("omega(M) = 1             (binding multiplier -- any integer)",
          all(zero(omega(sp.Integer(k)) - 1) for k in (1, 2, 3, 7)))
    check("omega(h) = -1            (Hecke deformation is bar-odd)",
          zero(omega(h) + 1))
    check("omega(1/hbar_q^2) = a    (cusp factor: ONE framing quantum)",
          zero(omega(1 / hbar_q ** 2) - a),
          f"omega(1/hbar_q^2) = {omega(1 / hbar_q ** 2)} = q^2 = a")
    check("omega(z_D) = a^2", zero(omega(zD) - a ** 2))
    check("omega(MASS mult lw/hbar_q^2) = a,  omega(BINDING mult M) = 1",
          zero(omega(lw / hbar_q ** 2) - a) and zero(omega(sp.Integer(3)) - 1),
          "that is residual (ii), as one exponent")
    only_two = [n for n in range(1, 7) if zero(omega(1 / hbar_q ** 2) - q ** n)]
    check("and it is sl_2-specific: omega(1/hbar_q^2) = q^N only at N = 2",
          only_two == [2], f"matching N: {only_two}  (N = 2 is convention D)")
    print()

    # ---- 6. the writhe route does NOT supply it -----------------------------
    print("6. REFUTATION of the writhe route: beta_Bor has exponent sum ZERO")
    # H_3 irreps.  Hecke relation sigma^2 = h sigma + 1, eigenvalues q and -1/q.
    sig1_3 = sp.Matrix([[q]])                     # lambda = (3):     sigma -> q
    sig1_111 = sp.Matrix([[-1 / q]])              # lambda = (1,1,1): sigma -> -1/q
    # lambda = (2,1): 2-dimensional
    sig1_21 = sp.Matrix([[q, 1], [0, -1 / q]])
    sig2_21 = sp.Matrix([[-1 / q, 0], [1, q]])

    def mat_zero(M) -> bool:
        return all(zero(x) for x in sp.Matrix(M))

    I2 = sp.eye(2)
    check("(2,1): Hecke relation sigma^2 = h sigma + 1 holds for both generators",
          mat_zero(sig1_21 ** 2 - (h * sig1_21 + I2))
          and mat_zero(sig2_21 ** 2 - (h * sig2_21 + I2)))
    check("(2,1): braid relation s1 s2 s1 = s2 s1 s2 holds",
          mat_zero(sig1_21 * sig2_21 * sig1_21 - sig2_21 * sig1_21 * sig2_21))

    # canonical Borromean word: (sigma_1 sigma_2^-1)^3, exponent sum 0
    word = [(1, 1), (2, -1)] * 3
    expsum = sum(e for _, e in word)
    check("canonical Borromean word (s1 s2^-1)^3 has exponent sum 0",
          expsum == 0, f"exponent sum = {expsum}  (BORROMEAN_WORD = [1,-2,1,-2,1,-2])")

    def rep_word(wd, g1, g2):
        dim = g1.shape[0]
        M = sp.eye(dim)
        for gen, e in wd:
            g = g1 if gen == 1 else g2
            M = M * (g if e > 0 else g.inv())
        return sp.simplify(M)

    chis = {
        "(3)": sp.cancel(rep_word(word, sig1_3, sig1_3).trace()),
        "(2,1)": sp.cancel(rep_word(word, sig1_21, sig2_21).trace()),
        "(1,1,1)": sp.cancel(rep_word(word, sig1_111, sig1_111).trace()),
    }
    all_even = all(zero(bar(v) - v) for v in chis.values())
    check("EVERY H_3 character of beta_Bor is BAR-EVEN", all_even,
          "\n".join(f"chi_{k}(beta_Bor) = {v}" for k, v in chis.items()))
    check("=> tr_M(beta_Bor) is bar-even: bar-even weights x bar-even characters",
          all_even,
          "so the TRACE contributes no framing weight; the whole anomaly of the\n"
          "mass amplitude is in hbar_q, which enters from CAL-2, not from the trace")

    # WHY beta_Bor comes out bar-even.  Bar acts on H_n(q) by sigma -> sigma^-1,
    # with NO sign: applying bar to sigma^2 = h sigma + 1 gives X^2 = -h X + 1
    # (h is bar-odd), and sigma^-2 = -h sigma^-1 + 1 satisfies exactly that,
    # while (-sigma^-1)^2 = -h sigma^-1 + 1 /= h sigma^-1 + 1 does not.
    # So bar sends a braid word to its MIRROR, and the Borromean link is
    # amphichiral -- which is why its character is fixed.
    check("bar acts on H_3 by sigma -> sigma^-1 (no sign): sigma^-2 = -h sigma^-1 + 1",
          mat_zero(sp.expand(sig1_21.inv() ** 2 - (-h * sig1_21.inv() + I2))),
          "and the sign-carrying alternative FAILS: (-sigma^-1) does not satisfy it")
    check("the signed alternative -sigma^-1 does NOT satisfy the barred relation",
          not mat_zero(sp.expand((-sig1_21.inv()) ** 2 - (-h * (-sig1_21.inv()) + I2))),
          "recorded because it is the natural guess and it is wrong")
    mirror = [(g, -e) for g, e in word]
    check("bar(rho(beta_Bor)) = rho(mirror beta_Bor), ENTRYWISE",
          mat_zero(rep_word(word, sig1_21, sig2_21).applyfunc(bar)
                   - rep_word(mirror, sig1_21, sig2_21)),
          "so bar = mirror on characters; the Borromean link is AMPHICHIRAL,\n"
          "hence its character is bar-fixed -- that is the actual mechanism")

    # CONTROL: a writhe-bearing word must NOT be bar-even, or the test is vacuous.
    # sigma_1 sigma_2 is a poor control -- its (2,1) character is the constant -1.
    # sigma_1 alone (exponent sum 1) has character h, which is bar-ODD.
    ctrl = [(1, 1)]                    # sigma_1, exponent sum +1
    chi_ctrl = sp.cancel(rep_word(ctrl, sig1_21, sig2_21).trace())
    check("CONTROL: the writhe-1 word s1 is NOT bar-even (test is not vacuous)",
          not zero(bar(chi_ctrl) - chi_ctrl),
          f"chi_(2,1)(s1) = {chi_ctrl} = h,  omega = {omega(chi_ctrl)} (bar-ODD)")
    ctrl2 = [(1, 1), (2, 1)]           # sigma_1 sigma_2, exponent sum +2
    chi_ctrl2 = sp.cancel(rep_word(ctrl2, sig1_21, sig2_21).trace())
    check("NOTE: s1 s2 would have been a VACUOUS control -- its character is -1",
          zero(chi_ctrl2 + 1),
          f"chi_(2,1)(s1 s2) = {chi_ctrl2}, bar-even despite exponent sum 2.\n"
          "So a nonzero exponent sum does NOT by itself force a bar anomaly in\n"
          "the character; recorded so the control is not mistaken for a law.")
    print()

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print("=" * 74)
    print(f"  {n_ok}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  The Ocneanu framing ratio a^2 is the bar-anomaly of the")
    print("  Markov parameter, bar(z) = z_-, and that holds for the whole family")
    print("  z_N = q^N/[N]_q while convention C's bar-even z fails it.  Residual")
    print("  (ii) of qou-brng becomes one exponent: the mass amplitude carries")
    print("  omega = a, one framing quantum; the binding amplitude carries")
    print("  omega = 1, none.  It is NOT closed -- and the writhe route is")
    print("  REFUTED as its source (scope (a)): the canonical Borromean word has")
    print("  exponent sum zero and every H_3 character of it is bar-even, so the")
    print("  trace supplies no framing weight.  The anomaly is entirely in the")
    print("  CAL-2 cusp factor hbar_q.  Residual (ii) is relocated to CAL-2.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
