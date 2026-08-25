"""qou-xx9f: the printed data cannot determine the normalisation. Stopping, not fitting.

Bean qou-xx9f. Scope-(a); no fit -- that is the point; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 46). Exact symbolic arithmetic (sympy); no float.

WHERE THIS PICKS UP. Addendum 36 eliminated candidate (1) of qou-xx9f -- the
(287) subscript is a typo for f_1, not a genuine m = 5 fibre -- leaving
candidate (2): an unprinted alpha-dependent normalisation between (281)'s
f_1 and the printed Phi series. The earlier narrowing had found that a
single q^lambda scalar, solved from the x^1 mismatch, CONFIRMS x^2 to ~6
nontrivial 5-adic digits but FAILS x^3 mod 5 -- so the normalisation is a
SERIES with a nonzero h^3 term, not a scalar.

The queued next step was: fit the h^1 and h^3 coefficients, then confirm on
x^3. This probe checks whether that test can exist before running it. It
cannot, and the reason is structural rather than computational.

THE PARAMETER COUNT. With h = log(1 + x) and normalisation exp(A h + B h^3),
expanded in x (exact, sympy):

    x^1 : A                                B-FREE
    x^2 : A(A - 1)/2                       B-FREE
    x^3 : (A^3 - 3A^2 + 2A + 6B)/6         LINEAR IN B

So h^3 first reaches x^3, because h^3 = x^3 + O(x^4). That fixes the whole
epistemic situation:

  * A is determined by x^1.
  * x^2 is then a genuine HELD-OUT prediction of A alone -- and it is the
    test the earlier narrowing already passed, at ~6 nontrivial digits.
  * x^3 introduces B linearly with unit coefficient, so ANY printed x^3 can
    be matched exactly by choosing B. Nothing is held out.

Three printed coefficients, two parameters, and the single genuine test is
already spent. "Fit h^1 and h^3, confirm on x^3" is not a test that exists:
the confirmation slot and the second parameter are the same coefficient.

THE CONTROL THAT MAKES THIS A FINDING, NOT ARITHMETIC. Under the ONE-
parameter model (B = 0) the x^3 coefficient is fully determined by A, so x^3
IS a genuine test there -- and it is the test that FAILED, which is why the
h^3 term was proposed. So the sequence is: 1 parameter, x^3 falsifiable, x^3
refutes it; 2 parameters, x^3 no longer falsifiable. Adding the term to fix
the failure consumes the evidence that detected the failure. That is the
over-fitting boundary, reached exactly here.

AND (288) CANNOT RESCUE IT. GSWZ print the x^200 coefficient at (288), which
would be a spectacular held-out target for a 2-parameter model. It is
unreachable: the input Phi_1 series at (282) is printed only to h^3 (four
terms and an ellipsis), so the quotient cannot be computed past roughly x^3
whatever machinery is applied. The limit is the printed INPUT, not the
compute.

VERDICT. qou-xx9f's remaining item is NOT RESOLVABLE from the printed
source. The fibre identification is settled (Addendum 36); the normalisation
is under-determined by what GSWZ print, and no amount of further computation
changes that. Recorded as a stop, per the standing instruction to stop when
x^3 needs a further parameter rather than to keep adding terms.

HONESTY: this claims only that the PRINTED data cannot discriminate. The
arXiv LaTeX source, or the unprinted Phi_1 coefficients from the authors,
would reopen it immediately. Nothing wired.
"""

import json
import pathlib
import subprocess
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

x, A, Bc = sp.symbols('x A B')
h = sp.log(1 + x)


def coeffs(expr, upto):
    s = sp.series(expr, x, 0, upto + 1).removeO().expand()
    return {k: sp.simplify(s.coeff(x, k)) for k in range(1, upto + 1)}


# ---------------------------------------------------------------- two-parameter
two = coeffs(sp.exp(A * h + Bc * h ** 3), 3)
detail["two_param_coeffs"] = {f"x^{k}": str(sp.factor(v)) for k, v in two.items()}
checks["x1_is_B_free"] = Bc not in two[1].free_symbols
checks["x2_is_B_free"] = Bc not in two[2].free_symbols
checks["x3_depends_on_B"] = Bc in two[3].free_symbols
# B enters x^3 LINEARLY with a nonzero coefficient, so any target is matchable.
dB = sp.simplify(sp.diff(two[3], Bc))
detail["d_x3_d_B"] = str(dB)
checks["x3_is_linear_in_B_with_nonzero_slope"] = (
    sp.simplify(sp.diff(two[3], Bc, 2)) == 0 and dB != 0)
# h^3 first reaches x^3 -- the structural reason x^1, x^2 are B-free.
h3 = sp.series(h ** 3, x, 0, 5).removeO().expand()
detail["h_cubed_series"] = str(h3)
checks["h_cubed_starts_at_x3"] = (h3.coeff(x, 1) == 0 and h3.coeff(x, 2) == 0
                                  and h3.coeff(x, 3) == 1)

# ---------------------------------------------------------------- one-parameter
one = coeffs(sp.exp(A * h), 3)
detail["one_param_coeffs"] = {f"x^{k}": str(sp.factor(v)) for k, v in one.items()}
# THE CONTROL: under B = 0 the x^3 coefficient IS determined by A, so x^3 is a
# genuine test there. That is the test the earlier narrowing ran, and failed.
checks["control_one_param_x3_is_a_genuine_test"] = all(
    Bc not in one[k].free_symbols for k in (1, 2, 3))
checks["control_one_param_x3_determined_by_A_alone"] = (
    one[3].free_symbols <= {A} and one[3] != 0)

# ---------------------------------------------------------------- the accounting
PRINTED_COEFFS = 3          # x^1, x^2, x^3 in (287)
detail["printed_coefficients_available"] = PRINTED_COEFFS
detail["parameters_in_model"] = 2
detail["genuine_held_out_tests"] = PRINTED_COEFFS - 2
checks["only_one_held_out_test_exists"] = PRINTED_COEFFS - 2 == 1
# ... and it is x^2, which the earlier narrowing already passed.
checks["the_one_test_is_x2_and_is_already_spent"] = (
    Bc not in two[2].free_symbols and Bc in two[3].free_symbols)

# ---------------------------------------------------------------- (288)
# Phi_1 at (282) is printed to h^3 only: four terms then an ellipsis. So the
# quotient cannot be computed past ~x^3 regardless of machinery, and (288)'s
# x^200 coefficient is unreachable. Recorded as a source limit, not a compute
# limit.
PHI1_PRINTED_ORDER = 3
detail["phi1_printed_order_in_h"] = PHI1_PRINTED_ORDER
detail["x200_reachable"] = False
checks["x200_target_is_unreachable_from_printed_inputs"] = (
    PHI1_PRINTED_ORDER < 200)

detail["verdict"] = (
    "NOT RESOLVABLE from the printed source. Three printed coefficients, two "
    "parameters, one genuine held-out test (x^2) -- already passed. x^3 is "
    "linear in the h^3 coefficient, so it cannot test the model that "
    "coefficient was introduced to save: adding the term consumes the "
    "evidence that detected the failure. (288)'s x^200 would be a real "
    "target but is unreachable, because Phi_1 is printed only to h^3. "
    "Stopping rather than fitting, per the standing rule. The arXiv LaTeX "
    "source or the unprinted Phi_1 coefficients would reopen it at once.")

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_287_normalisation_underdetermined_probe",
    "engine": "sympy-exact",
    "q0Anchor": "independent",
    "q0AnchorReason": (
        "Reads no q0. A symbolic parameter count on a power series; the "
        "substrate modulus never enters and no anchor is imported."),
    "scriptFile": "gswz_287_normalisation_underdetermined_probe.py",
    "commitSha": _sha,
    "beans": ["qou-xx9f"],
    "source": ("GSWZ arXiv:2412.04241v2 eqns (281), (282), (287), (288); "
               "Addendum 36 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) STOP, not a fit. The queued step was to fit the h^1 and "
        "h^3 coefficients of the unprinted normalisation and confirm on x^3. "
        "That test does not exist. With h = log(1+x), h^3 first reaches x^3, "
        "so x^1 and x^2 are free of the h^3 coefficient while x^3 is LINEAR "
        "in it with unit slope -- any printed x^3 is matchable exactly. "
        "Three printed coefficients, two parameters, one genuine held-out "
        "test, and that test is x^2, which the earlier narrowing already "
        "passed at ~6 nontrivial digits. The control is what makes this a "
        "finding: under the one-parameter model x^3 IS a genuine test, and "
        "it is the test that failed -- so introducing the h^3 term to repair "
        "the failure consumes the very coefficient that detected it. That is "
        "the over-fitting boundary. (288)'s x^200 coefficient would be a "
        "decisive held-out target but is unreachable, because the input "
        "Phi_1 series at (282) is printed only to h^3; the limit is the "
        "printed INPUT, not the compute. VERDICT: qou-xx9f's remaining item "
        "is not resolvable from the printed source. The arXiv LaTeX source, "
        "or the unprinted Phi_1 coefficients, would reopen it immediately. "
        "Nothing wired."
    ),
}
with open(HERE / "gswz_287_normalisation_underdetermined.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
