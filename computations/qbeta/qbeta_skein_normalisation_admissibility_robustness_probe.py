#!/usr/bin/env python3
"""The published Q_beta form is inadmissible under BOTH live Skein
normalisations -- so `z = 1` is not an artifact of the convention it was
measured in.

WHY THIS PROBE EXISTS.  `qbeta_published_form_is_the_inadmissible_z1_probe`
(#6722) and `qbeta_admissible_line_exhausts_the_choice_probe` (#6763)
established that the framework's published closed form

    Q_beta = m_e * |q^2 - 2q - 1| * (q + 1) / (2 q^3)

is `|tr_M^z(Delta_S)| * E0` at `z = 1`, which is not an admissible Markov
parameter under convention D.  Both were computed with the Hecke bridge
`h = q - 1/q`, i.e. the Skein relation AGENTS.md section 7a mandates.

Bean `qou-8bxv` then measured that a SECOND Skein normalisation is live in
eight content blocks across five chapters, and that the two are not related by
rescaling the bracket:

    (H)  L+ - L-            = (q - 1/q) L0             bridge h = q - 1/q
    (J)  q[L+] - q^-1[L-]   = (u - 1/u) [L0]           bridge s = u - 1/u

with `u = sqrt(q)`.  That raises a direct threat to the earlier conclusion:
if the published form sits at an ADMISSIBLE parameter under (J), then its
inadmissibility is a statement about the convention it was read in, not about
the framework -- and the open decision in `qou-99qc` changes shape.

This probe tests that threat.  It does not survive.

THE TRANSPORT, which is the load-bearing step.  Under (J) the generator has
eigenvalues `u^-1, -u^-3`, so

    sigma_J  =  u^-2 * sigma~(u)

where `sigma~` satisfies the (H) relation in the variable `u`.  The (J) algebra
is therefore the (H) algebra in the square-root variable with the generator
scaled by `u^-2`, and the Markov parameter transports as `zeta = u^-2 * z~`.
Carrying convention D's two roots through that map gives the admissible set
under (J):

    z~ = u            ->   zeta = u^-1                = q^-1/2
    z~ = u^3/(u^2+1)  ->   zeta = markovKernel(u)     = sqrt(q)/(q+1)

The second is EXACTLY `z_C`, the parameter AGENTS.md calls convention C.  That
identity is reported here as an observation with its own check; this probe does
not draw a conclusion from it about the convention-C excision.

SYMBOL NOTE, because the obvious name is taken.  The transported parameter is
written `zeta` here and never `z_J`: bean `qou-qlma` already owns `z_J` for a
DIFFERENT number, the Jones link-invariant parameter
`z_J = (q-1)/(q^1/2 + q^-1/2)^2 = 0.0274199478`, on which an owner decision is
open.  `zeta` at the proton pin is 0.4993203342 -- and note that `1/delta =
0.497290545` sits 0.408 % away from it (bean `qou-98g5`), so this neighbourhood
already holds three numerals that get confused.  Read the definition, not the
glyph.

WHAT IS ALREADY IN THE CORPUS, AND IS NOT CLAIMED HERE AS NEW.  The identity
`z_C(q) = z_D(sqrt q)/q` is a one-line composition of two committed sorry-free
theorems in `QOU/BraidKnot/MarkovConventionSeparation.lean`:

    markovZC_eq_kernel_sqrt      z_C q = markovKernel (sqrt q)     (0 <= q)
    markovZD_eq_sq_mul_kernel    z_D q = q^2 * markovKernel q

with `markovKernel u = u/(u^2+1)`.  That module's header already says D "is not
C with a different letter in it".  This probe re-derives the identity as a
check and adds only an INTERPRETATION of the `q^2`: it is the (H)->(J) Skein
generator rescale.

CONVERGENT WITH `qou-cds1`'s RANK-LABEL READING, AND ITS OBSTRUCTION IS
STRONGER THAN MINE (added after `336a35ff278` landed on main).  That commit
reads the same `q^2` a different way -- `z_N = q^N/[N]_q` is a RANK-indexed
family, `z_2 = z_D`, and `z_C = 1/[2]_sqrt(q)` is in the family for NO N (I
re-derived that independently for N = 1..6).  The two readings are one
mechanism seen from two sides, and the bridge is exact:

    kernel(q) = q/(q^2+1) = 1/[2]_q          (exact)
    markovZD  = q^2 * kernel(q) = q^2/[2]_q  = their z_N at N = 2
    markovZC  = kernel(sqrt q)  = 1/[2]_sqrt(q)

So the `u^-2` generator rescale of the (H)->(J) transport is EXACTLY the
operation that strips the `q^N` numerator -- their sentence "rescaling z_D to
bar-evenness strips the rank label" and this probe's "the q^2 is the Skein
normalisation change" describe the same map.  Theirs names what is LOST
(the rank label, bar-oddness); this one names WHERE the rescale COMES FROM
(a live Skein convention).

**Their obstruction is the better one and supersedes the argument below.**
It is a BLOCK COUNT, not a specialisation point: convention D annihilates the
(1^3) block (`y_(1^3) = 0`; TL_n = H_n/<antisym> kills every partition with
more than two rows) while C does not (`y_(1^3) = 0.022745`), so no
substitution whatever can carry a 3-block trace to a 2-block one.  Cite that
rather than the weaker reading that follows.

WHICH WAY THAT INTERPRETATION CUTS -- against the reading one reaches for
first.  It does NOT rehabilitate convention-C sites.  `z_C(q) = kernel(sqrt q)`
is the (J)-admissible parameter of the Hecke algebra at the variable `sqrt q`,
NOT at `q`.  So a site spelling `z_C(q_0)` is using a correctly-normalised
parameter for the algebra at the WRONG specialisation point, which is why the
corpus is right that such a site is not repairable by substitution
(`qou-cxjq`, `qou-lp5d`, `qou-pmkh`, and the 13 `blocked_on_rederivation`
entries -- 12 distinct files -- of the trace-convention registry, whose own note
says they "cannot be migrated by substituting z_D, because the substitution
changes the site's asserted RESULT").  The interpretation SUPPORTS the excision
and sharpens its reason; it does not soften it.

TWO ARITY GAPS, stated because a reader will otherwise collide with an
existing sorry-free theorem and stop (the `da-arity-conflation` class).

  * `no_kernel_instantiation_is_conventionD (hq : 1 < q) :
     ~ exists u, markovKernel u = markovZD q` binds a single argument `q` on
    the right and quantifies NO rescaling factor.  The transport used here is
    `markovKernel u = markovZD u / u^2` -- the SAME argument on both sides,
    with a rescale.  Different proposition; the theorem excludes pure
    reparametrisation and is untouched by this probe.  Both are checked below.
  * `no_rescaling_of_skein_weights (hplus : c*1 = q) (hminus : c*(-1) = -q^-1)
     : q^2 = 1` quantifies one constant `c` on the BRACKET at a FIXED `q`.
    The map here rescales the GENERATOR by `u^-2` AND substitutes `q = u^2`,
    which is outside those binders.  So "(H) and (J) are not bracket
    rescalings" (bean `qou-8bxv`) and "the (J) algebra is the (H) algebra in
    `u` with the generator scaled" are both true and are not in tension.

TWO READINGS OF THE ELEMENT, because `Delta_S` is convention-laden.  It is
built from typed crossings `(sigma_g + d)` whose shift `d` is a multiple of the
bridge (`d = -h/2` for the one-crossing proton, `d = -h/2, -h` for the
two-crossing neutron -- `qbeta_delta_element_fork_pricing_probe`), so there is
no single (J) counterpart.  Both defensible readings are tested:

  (C-reading)  the element is unchanged: `Delta = h^2/2 - (h/2)(sigma_1+sigma_2)`
               with the shift still written in `h`.  The value family is then
               the SAME set of functions of q under both conventions, and the
               question reduces to a root check on the admissible sets.  This
               reading gives the stronger result: `z = 1` is inadmissible under
               (J) at EVERY q > 1, with no pin needed, whereas under (H) it is
               admissible at the supergolden ratio q^3 = q^2 + 1 and excluded
               only because q_0 is not that point.

  (B-reading)  the shift follows the bridge, `d -> -s/2, -s`, giving
               `Delta^J = s^2/2 - (s/2)(sigma_J1 + sigma_J2)`.  Solved at the
               pin on both sign branches.

NEGATIVE CONTROL.  A probe that reports "no branch is admissible" is worthless
unless it can be shown to detect admissibility when it IS present.  The solver
is therefore re-run against a synthetic target built AT each admissible
parameter, and required to recover that parameter exactly.  Without this check
a bug and a finding are indistinguishable.

SCOPE, per the AGENTS.md refutation rule.
  * The inadmissibility is scope-(b) and the invariant is cited: `z = 1` is not
    a root of the (1^3)-block weight numerator, proved sorry-free in
    `ConventionDAdmissibleRoots.lean`, and transported here by an exact
    algebra map.  A root computation is a degree bound, one of the permitted
    grounds.
  * The ROBUSTNESS claim is scope-(a) and bounded by the two readings: both
    fail, which is evidence and not an exhaustion over every element one could
    write in (J).  The corpus has no (J) version of `Delta_S`; both readings
    here are constructed by this probe and labelled as such.
  * Nothing is wired.  No content block, no c_k, no witness outside this file.

PRECISION.  Every algebraic step is exact sympy over Q(q) or Q(u).  The pin
enters only at readout, as an exact `Rational` from the 50-digit proton string,
printed through mpmath at 50 dps.  No float64 anywhere (AGENTS.md NO-FLOAT64;
probes are not exempt).
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
sys.path.insert(0, str(_COMP))

import _path_bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate import constants as CONST  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def main() -> int:
    mp.mp.dps = 60
    checks: list[dict] = []

    def chk(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        return bool(ok)

    print(__doc__.splitlines()[0])
    print()
    ok = True

    q, zj = sp.symbols("q zj", positive=True)
    u = sp.sqrt(q)
    h = q - 1 / q
    s = u - 1 / u
    E0 = _qbeta_e0.order_zero_scaled(1, q)                       # in units of m_e

    # ---- 1. the transport map, exact ------------------------------------
    zC = sp.sqrt(q) / (q + 1)
    zD = q**3 / (q**2 + 1)
    zeta_adm = {"u^-1": 1 / u, "kernel(u)": u / (u**2 + 1)}

    ok &= chk("transport_carries_z_D_to_u_over_u2_plus_1",
              sp.simplify(zD.subs(q, u) / q - zeta_adm["kernel(u)"]) == 0,
              "z_D(sqrt q)/q - u/(u^2+1) = 0 exactly: convention D's second "
              "root, carried through sigma_J = u^-2 sigma~(u), lands on "
              "u/(u^2+1)")
    ok &= chk("transport_carries_z_equals_q_to_u_inverse",
              sp.simplify(u.subs(q, q) / q - 1 / u) == 0,
              "z~ = u scaled by u^-2 gives u^-1 -- the (J) image of the "
              "augmentation point z = q")
    ok &= chk("the_transported_root_IS_exactly_z_C",
              sp.simplify(zeta_adm["kernel(u)"] - zC) == 0,
              "u/(u^2+1) - sqrt(q)/(q+1) = 0. NOT NEW: this is the one-line "
              "composition of markovZC_eq_kernel_sqrt and "
              "markovZD_eq_sq_mul_kernel, both sorry-free on main in "
              "QOU/BraidKnot/MarkovConventionSeparation.lean. Re-derived here "
              "as a check; the contribution is reading the q^2 rescale as the "
              "(H)->(J) Skein normalisation, not the algebra itself")

    # the map must be a bijection on the two roots, not a collapse
    ok &= chk("the_two_admissible_parameters_stay_DISTINCT_under_transport",
              sp.simplify(zeta_adm["u^-1"] - zeta_adm["kernel(u)"]) != 0,
              "u^-1 != u/(u^2+1) as rational functions -- the transport does "
              "not collapse the two roots into one, which would have made "
              "'no branch matches' vacuous")

    # ---- 1b. the transport's two halves, separated ----------------------
    # sigma_J = u^-2 * sigma~(u) is a SCALAR RESCALE composed with a
    # REPARAMETRISATION q -> u.  They are not the same kind of move and the
    # eigenvalue ratio separates them: a rescale cannot touch it, so every
    # difference between the two Skein normalisations that survives in the
    # ratio is reparametrisation.  Derived here from each relation directly
    # (alpha*L+ + beta*L- + gamma*L0 = 0  =>  alpha*s^2 + gamma*s + beta = 0),
    # NOT assumed.
    xv = sp.symbols("xv")

    def _skein_eigs(alpha, beta, gamma):
        roots = sp.solve(sp.Eq(alpha * xv**2 + gamma * xv + beta, 0), xv)
        return [sp.simplify(r) for r in roots]

    def _ratio(eigs):
        probe_q = sp.Rational(11, 10)
        pos = [r for r in eigs if sp.sign(r.subs(q, probe_q)) == 1]
        neg = [r for r in eigs if r not in pos]
        return sp.simplify(pos[0] / neg[0])

    eigs_H = _skein_eigs(1, -1, -(q - 1 / q))
    eigs_J = _skein_eigs(q, -1 / q, -(sp.sqrt(q) - 1 / sp.sqrt(q)))
    rat_H, rat_J = _ratio(eigs_H), _ratio(eigs_J)

    ok &= chk("H_and_J_generator_ratios_are_MINUS_q2_and_MINUS_q",
              sp.simplify(rat_H + q**2) == 0 and sp.simplify(rat_J + q) == 0,
              "in the SAME variable q: (H) eigenvalues {q, -1/q} ratio -q^2; "
              "(J) eigenvalues {q^-1/2, -q^-3/2} ratio -q. The two Skein "
              "normalisations differ in the ratio, so they are not related by "
              "a rescale alone -- which is the ratio-side restatement of this "
              "probe's separation premise (bean qou-8bxv)")

    ok &= chk("the_u2_rescale_half_of_the_transport_is_INERT_on_the_ratio",
              sp.simplify((eigs_J[0] / u**2) / (eigs_J[1] / u**2)
                          - eigs_J[0] / eigs_J[1]) == 0,
              "(u^-2 a)/(u^-2 b) = a/b for the (J) pair. NOT NEW and NOT "
              "MINE: this is QOU.Mass.KZLevelFromHeckeNormalisation."
              "ratio_invariant, sorry-free over a generic field, landed on "
              "main in 492ad4221f6 (bean qou-d0qq). Recorded here because it "
              "closes the rescale half of sigma_J = u^-2 sigma~(u) with a "
              "Lean proof instead of this probe's arithmetic, leaving the "
              "reparametrisation q -> u as the whole content of the transport")

    # ---- 2. C-reading: reduces to a root check, no pin needed -----------
    # value family under both conventions is {|h^2/2 - h*Z|*E0 : Z}; the
    # published form is at Z = 1 (established in #6722, re-derived here).
    trC = h**2 / 2 - h * zj
    pub_lo = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)      # |published|, q < 1+sqrt2
    ok &= chk("C_reading_published_form_is_the_Z_equals_1_cell",
              sp.simplify(sp.expand(-trC.subs(zj, 1) * E0 - pub_lo)) == 0,
              "|h^2/2 - h| * E0 == published, exact over Q(q) on the branch "
              "1 < q < 1+sqrt(2) where h < 2 -- reproduced here rather than "
              "carried over from #6722")

    # is Z = 1 in either admissible set, as an equation in q?
    def positive_roots(expr):
        return [r for r in sp.solve(sp.Eq(expr, 1), q)
                if r.is_real and sp.N(r) > 1]

    rootsH = {"z=q": positive_roots(q), "z=z_D": positive_roots(zD)}
    rootsJ = {k: positive_roots(v) for k, v in zeta_adm.items()}

    ok &= chk("H_admits_Z_equals_1_ONLY_at_the_supergolden_ratio",
              len(rootsH["z=q"]) == 0 and len(rootsH["z=z_D"]) == 1
              and sp.simplify(rootsH["z=z_D"][0]**3
                              - rootsH["z=z_D"][0]**2 - 1) == 0,
              "under (H), z = 1 is admissible at exactly one q > 1, the root "
              f"of q^3 = q^2 + 1 (supergolden, {mp.nstr(mp.mpf(str(sp.N(rootsH['z=z_D'][0], 30))), 12)}) "
              "-- so the (H) exclusion at q_0 is a PIN fact, not an identity")
    ok &= chk("J_admits_Z_equals_1_at_NO_q_greater_than_1",
              all(len(v) == 0 for v in rootsJ.values()),
              "under (J), neither u^-1 = 1 nor u/(u^2+1) = 1 has a solution "
              "with q > 1 (the second has none at all: q + 1 > sqrt(q) for "
              "every q > 0) -- so on the C-reading the published form is "
              "inadmissible under (J) IDENTICALLY, a strictly stronger "
              "statement than the (H) one")

    # ---- 3. readout at the proton pin -----------------------------------
    q0 = sp.Rational(Q_50_DIGIT_STR)
    m_e = sp.Rational(str(CONST.M_E_MEV))
    Qexp = sp.Rational(str(CONST.Q_NEUTRON_MEV))
    T = Qexp / (_qbeta_e0.order_zero_scaled(m_e, q0))            # |tr| CODATA demands
    P = sp.simplify((pub_lo / E0).subs(q, q0))   # |tr| the PUBLISHED FORM sits at

    def f(e):
        """Exact -> mpf. Rational values go through p/q exactly; the transport
        introduces sqrt(q), so algebraic irrationals fall back to a 60-digit
        mpmath evalf. Neither path touches float64."""
        e = sp.simplify(e)
        if e.is_Rational:
            return mp.mpf(sp.Rational(e).p) / mp.mpf(sp.Rational(e).q)
        return mp.mpf(str(sp.N(e, 60)))

    print(f"\n      |tr| at the PUBLISHED form  P = {mp.nstr(f(P), 20)}")
    print(f"      |tr| CODATA would demand   T = {mp.nstr(f(T), 20)}")
    for k, v in zeta_adm.items():
        print(f"      admissible (J) zeta = {k:12s} = "
              f"{mp.nstr(f(v.subs(q, q0)), 20)}")

    # ---- 3b. the two ARITY GAPS, machine-checked rather than asserted ----
    # (i) the corpus separation theorem must still hold: kernel(u) <= 1/2 and
    #     z_D(q) > 1/2 for q > 1, so NO u sends the kernel to z_D(q). This
    #     probe must not be readable as contradicting a sorry-free theorem.
    kern = zj / (zj**2 + 1)
    ok &= chk("corpus_separation_theorem_STILL_HOLDS_under_this_transport",
              sp.simplify(sp.factor(sp.numer(sp.together(
                  sp.Rational(1, 2) - kern))) - (zj - 1)**2 / 1) == 0
              and f(zD.subs(q, q0)) > mp.mpf("0.5"),
              "1/2 - kernel(u) has numerator (u-1)^2 >= 0, and z_D(q_0) = "
              f"{mp.nstr(f(zD.subs(q, q0)), 12)} > 1/2, so "
              "no_kernel_instantiation_is_conventionD is intact: no real u "
              "sends the kernel to z_D(q). Nothing here contradicts it")

    # (ii) and the transport is a DIFFERENT proposition: same argument, rescaled
    ok &= chk("the_transport_is_a_DIFFERENT_proposition_than_that_theorem",
              sp.simplify(kern.subs(zj, q) - zD / q**2) == 0
              and len([r for r in sp.solve(sp.Eq(kern, zD.subs(q, q0)), zj)
                       if r.is_real]) == 0,
              "kernel(u) = z_D(u)/u^2 holds identically -- SAME argument, "
              "rescaled by u^2 -- while kernel(u) = z_D(q_0) has no real "
              "solution at all. The two differ in exactly the binder the "
              "theorem leaves unquantified, which is why both are true and "
              "the da-arity-conflation trap is avoided rather than tripped")

    # ---- 4. B-reading: solve on both sign branches ----------------------
    # zj is declared positive, which would silently DROP a negative root and
    # make it read as "no solution". Solve over an unrestricted symbol instead:
    # the admissible values are positive, so a negative root cannot be a match,
    # but it must be seen rather than discarded.
    w = sp.Symbol("w")
    trB = s**2 / 2 - s * w
    solB = {}
    for sgn, lab in ((1, "+"), (-1, "-")):
        solB[lab] = [sp.simplify(r) for r in sp.solve(sp.Eq(trB.subs(q, q0),
                                                            sgn * P), w)]

    matches = []
    for lab, vals in solB.items():
        for val in vals:
            for k, za in zeta_adm.items():
                if sp.simplify(val - za.subs(q, q0)) == 0:
                    matches.append((lab, k))
        print(f"      B-reading branch {lab}: zeta = "
              f"{', '.join(mp.nstr(f(v), 20) for v in vals) if vals else 'none'}")

    ok &= chk("B_reading_hits_NO_admissible_parameter_on_either_branch",
              len(matches) == 0 and sum(len(v) for v in solB.values()) == 2,
              "solving s^2/2 - s zeta = +/- published/E0 at the proton pin over "
              "an UNRESTRICTED zeta gives "
              + "; ".join(f"{lab}: " + (", ".join(mp.nstr(f(v), 12) for v in vals)
                                        if vals else "none")
                          for lab, vals in solB.items())
              + " -- two roots, neither equal to u^-1 = 0.9491671528 nor to "
              "u/(u^2+1) = 0.4993203342")

    # ---- 5. NEGATIVE CONTROL: the solver must find admissibility --------
    recovered = {}
    for k, za in zeta_adm.items():
        synthetic = trB.subs(w, za).subs(q, q0)          # target BUILT at za
        sol = sp.solve(sp.Eq(trB.subs(q, q0), synthetic), w)
        recovered[k] = bool(sol) and sp.simplify(sol[0] - za.subs(q, q0)) == 0
    ok &= chk("NEGATIVE_CONTROL_solver_recovers_an_admissible_parameter_when_present",
              all(recovered.values()),
              "re-running the same solve against a target synthesised AT each "
              f"admissible parameter recovers it exactly ({recovered}) -- so "
              "the NONE above is a finding, not a broken matcher")

    # ---- 6. what the (J) admissible parameters would give, in MeV -------
    E0_MeV = _qbeta_e0.order_zero_scaled(m_e, q0)
    Qc = mp.mpf(str(CONST.Q_NEUTRON_MEV))
    rows = []
    for k, za in zeta_adm.items():
        for lab, tr, sym in (("C-reading", trC, zj), ("B-reading", trB, w)):
            val = abs(f(sp.simplify(tr.subs(sym, za).subs(q, q0)) * E0_MeV))
            rows.append({"convention": "J", "reading": lab, "zeta": k,
                         "Q_beta_MeV": mp.nstr(val, 20),
                         "pct_vs_CODATA": mp.nstr((val - Qc) / Qc * 100, 10)})
            print(f"      {lab} at zeta = {k:12s}: Q_beta = "
                  f"{mp.nstr(val, 12)} MeV  ({mp.nstr((val-Qc)/Qc*100, 8)} %)")

    # calibration against the two MERGED results: the same machinery, run on the
    # (H) admissible parameters, must reproduce +12.470 % and -43.157 % exactly.
    # Without this the (J) numbers above are unanchored.
    calib = {}
    for k, za in (("z=q", q), ("z=z_D", zD)):
        v = abs(f(sp.simplify(trC.subs(zj, za).subs(q, q0)) * E0_MeV))
        calib[k] = mp.nstr((v - Qc) / Qc * 100, 10)
        print(f"      calibration (H) at {k:8s}: Q_beta = {mp.nstr(v, 12)} MeV"
              f"  ({calib[k]} %)")
    ok &= chk("CALIBRATION_reproduces_the_merged_H_misses",
              abs(mp.mpf(calib["z=q"]) - mp.mpf("12.470")) < mp.mpf("0.001")
              and abs(mp.mpf(calib["z=z_D"]) + mp.mpf("43.157")) < mp.mpf("0.001"),
              f"(H) at z = q gives {calib['z=q']} % and at z = z_D gives "
              f"{calib['z=z_D']} % -- matching the +12.470 % / -43.157 % of "
              "#6722/#6763 to 3 dp, so the (J) cells above come from machinery "
              "already validated against the merged numbers")

    ok &= chk("no_J_admissible_cell_lands_within_1_pct_of_CODATA",
              all(abs(mp.mpf(r["pct_vs_CODATA"])) > 1 for r in rows),
              "every (J) admissible cell across both readings misses CODATA by "
              f"more than 1 % (min |miss| = "
              f"{mp.nstr(min(abs(mp.mpf(r['pct_vs_CODATA'])) for r in rows), 8)} %) "
              "-- the 0.17 % landing is not recoverable by changing "
              "normalisation, which is the whole question this probe asks")

    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    witness = {
        "name": "qbeta-skein-normalisation-admissibility-robustness",
        "description": (
            "Tests whether the published Q_beta form's inadmissibility (z = 1, "
            "#6722/#6763) is an artifact of the (H) Skein normalisation "
            "AGENTS.md section 7a mandates, given that bean qou-8bxv measured a "
            "second normalisation (J) live in eight content blocks. It is not. "
            "The (J) algebra is the (H) algebra in u = sqrt(q) with the "
            "generator scaled by u^-2, so convention D's roots transport to "
            "zeta = u^-1 and zeta = u/(u^2+1); the second is exactly z_C. Under "
            "the reading that leaves the element unchanged, z = 1 is "
            "inadmissible in (J) at EVERY q > 1 -- stronger than the (H) "
            "result, which excludes it only because q_0 is not the supergolden "
            "root of q^3 = q^2+1. Under the reading that follows the bridge "
            "(d -> -s/2, -s), neither sign branch hits an admissible "
            "parameter. A negative control confirms the solver recovers an "
            "admissible parameter when one is present."),
        "assertions": checks,
        "transport": {
            "sigma_J": "u^-2 * sigma~(u), eigenvalues u^-1 and -u^-3",
            "markov": "zeta = u^-2 * z~",
            "admissible_zeta": {k: str(v) for k, v in zeta_adm.items()},
            "z_C_identity": "z_C(q) = z_D(sqrt q)/q = u/(u^2+1), exact"},
        "supergolden_note": (
            "under (H), z = 1 would be admissible at the supergolden ratio "
            "q^3 = q^2 + 1; q_0 is not that point"),
        "abs_tr_at_published_form": mp.nstr(f(P), 25),
        "abs_tr_CODATA_demands": mp.nstr(f(T), 25),
        "B_reading_solutions": {k: [mp.nstr(f(v), 25) for v in vals]
                                for k, vals in solB.items()},
        "J_admissible_cells": rows,
        "H_calibration_pct": calib,
        "caveats": [
            "Delta_S is convention-laden (its typed-crossing shift d is a "
            "multiple of the bridge), and the corpus has no (J) version of it. "
            "Both readings tested here are CONSTRUCTED by this probe. Both "
            "fail, which is evidence for robustness and not an exhaustion over "
            "every element expressible in (J).",
            "The identity z_C(q) = z_D(sqrt q)/q is NOT new here -- it is the "
            "composition of markovZC_eq_kernel_sqrt and "
            "markovZD_eq_sq_mul_kernel, sorry-free on main. What is new is "
            "reading the q^2 rescale as the (H)->(J) Skein normalisation.",
            "Convergent with qou-cds1 (336a35ff278): kernel(q) = 1/[2]_q "
            "exactly, so markovZD = q^2*kernel(q) IS their rank-indexed "
            "z_N = q^N/[N]_q at N=2, and this probe's u^-2 rescale is exactly "
            "what strips that numerator. Their obstruction is STRONGER and "
            "supersedes the specialisation-point argument: D annihilates the "
            "(1^3) block and C does not, so no substitution carries a 3-block "
            "trace to a 2-block one.",
            "That reading SUPPORTS the convention-C excision and does not "
            "soften it: z_C(q) = kernel(sqrt q) is the (J)-admissible "
            "parameter of the algebra at the variable sqrt q, not at q, so a "
            "z_C site is correctly normalised for the WRONG specialisation "
            "point. This is why such sites are not repairable by substitution "
            "(qou-cxjq, qou-lp5d, qou-pmkh, and the 13 blocked_on_rederivation "
            "entries -- 12 distinct files -- of the trace-convention "
            "registry).",
            "Two arity gaps are checked, not asserted: "
            "no_kernel_instantiation_is_conventionD quantifies no rescaling "
            "factor, and no_rescaling_of_skein_weights binds one constant on "
            "the BRACKET at fixed q while this transport rescales the "
            "GENERATOR and substitutes q = u^2. Both theorems stand.",
            "The symbol z_J is NOT used: bean qou-qlma owns it for a different "
            "number (0.0274199478). The transported parameter is written zeta.",
            "Nothing here changes the published number or picks an option in "
            "bean qou-99qc. It closes one way that decision could have been "
            "dissolved.",
        ],
        "related": [
            "computations/qbeta/qbeta_published_form_is_the_inadmissible_z1_probe.py",
            "computations/qbeta/qbeta_admissible_line_exhausts_the_choice_probe.py",
            "computations/qbeta/qbeta_delta_element_fork_pricing_probe.py",
            "computations/markov/skein_normalisation_two_conventions_audit.py",
            "docs/audits/2026-09-05-two-skein-normalisations-are-live.md",
            "docs/audits/2026-09-05-qbeta-functional-decision-options.md",
            "QOU.QBeta.ConventionDAdmissibleRoots",
            "QOU.BraidKnot.MarkovConventionSeparation",
            "qou-cds1 / 336a35ff278 (C and D are different algebras; z is a rank label)",
            "folio/quantum-observable-universe/lean/QOU/Braiding/SkeinNormalisation.lean",
            "library/li-braid-closures (HOMFLYPT normalisation change, held, uncited)",
        ],
        "source": "beans qou-99qc (robustness) and qou-8bxv (the two normalisations)",
        "scriptFile": Path(__file__).name,
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python+sympy",
        q0_anchor="proton",
        q0_anchor_reason=(
            "The transport map, the admissible sets and the C-reading root "
            "check are exact over Q(q) and pin-free; q0 enters only for the "
            "B-reading solve and the MeV readout cells."),
        q0_value=Q_50_DIGIT_STR)
    out = _HERE / "qbeta-skein-normalisation-admissibility-robustness.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness -> {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
