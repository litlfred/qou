"""Convention-immunity audit of the eps_m / GSWZ programme — measured, and a standing gate against drift.

Beans qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 26).

WHY. The owner ruling of 2026-08-15 makes convention D (z = q^3/(q^2+1))
canonical and excises C, and reaffirms the proton pin. AGENTS.md warns
that the Q_beta c_k ladder is convention-C-frame throughout and has not
been re-derived (bean qou-cds1), so every c_k conclusion is
C-conditional until it is. This probe asks the same question of MY
programme, and answers it by MEASUREMENT rather than by assertion --
following the template of
docs/audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md,
which classifies each pillar VALID-immune / VALID-scoped /
C-CONDITIONAL.

WHAT IS MEASURED (each check can fail, and would fail the moment a
z-dependent or anchor-dependent input were wired into this chain --
that is the point of keeping this as a standing gate):

1. NO TRACE LAYER. No probe in the programme imports pyhecke, a gram
   module, or any Markov-trace machinery. Convention C vs D is a
   statement about the Markov parameter z on the Hecke algebra and the
   Gram form built from it; a chain that never touches that layer
   cannot be C- or D-framed.
2. NO TRACE PARAMETER. The symbols z_C, z_D and the defining
   expressions sqrt(q)/(q+1) and q^3/(q^2+1) appear nowhere.
3. NO SUBSTRATE ANCHOR. No probe references q_parameter, q0, the
   50-digit pin, or qou_substrate. So the 2026-08-07 proton-default
   directive and the R2 reaffirmation are equally inapplicable: the
   chain never evaluates at a substrate modulus at all.
4. THE q THAT DOES APPEAR IS THE QUANTUM VARIABLE, NOT z. Five probes
   carry symbolic Laurent polynomials in q. Under C <-> D it is z that
   changes AS A FUNCTION OF q; q itself is unchanged, so a Laurent
   element in q is the same element in both conventions. Verified
   structurally here: the candidate elements are recomputed and shown
   to be literal Laurent polynomials with integer coefficients, i.e.
   objects of Z[q, 1/q], a ring in which no convention choice is
   expressible.

THE CLASSIFICATION (the deliverable):

  VALID-immune  -- eps_m descent chain, all layers (Addenda 17, 18,
                   21-25): Bloch symbols of the 5_2 trace field,
                   p-adic dilogarithms, Galois descent on cyclotomic
                   fields. No q, no z, no anchor.
  VALID-immune  -- the c_k membership GATES (Addendum 19): exact
                   Laurent / cyclotomic arithmetic; z never enters.
  C-CONDITIONAL -- the PROVENANCE claim attached to those gates, that
                   J_Hopf(q) and [2]_q are "the corpus's named c_k /
                   alpha_EM candidates". That identification comes from
                   the C-frame ladder (qou-cds1). The arithmetic
                   verdicts stand; the label on what the elements ARE
                   needs the C-conditional scope until the ladder is
                   re-derived under D.

HONESTY: this audit does NOT claim the c_k ladder survives convention
D -- that is qou-cds1's question and is untouched here. It claims only
that this programme's own results do not depend on the convention, and
identifies the single place where my merged wording borrowed a
C-framed identification.
"""

import io
import json
import pathlib
import re
import subprocess
import sys
import tokenize

HERE = pathlib.Path(__file__).resolve().parent
PROG = sorted(HERE.glob("gswz_*.py")) + [HERE / "ck_membership_payoff_run_probe.py"]
PROG = [p for p in PROG if p.name != pathlib.Path(__file__).name]

checks = {}
detail = {}
detail["programme_probe_count"] = len(PROG)

def _code_only(text):
    """`text` with every comment and string literal blanked out, spacing kept.

    CORRECTED 2026-08-30, and this is the whole reason the gate was wrong.
    All three text checks below matched against the RAW file, so each of them
    fired on prose that ASSERTS the compliance being checked:

      check 1  gswz_epsm_chi_eigenspace_place_probe.py:285, a q0AnchorReason
               reading "no pyhecke/Gram/Markov import exists in the cone"
               -> matched on the word `pyhecke`
      check 2  twelve line-5 docstrings reading "Convention-immune: no
               Hecke/Gram/Markov import, no z_C/z_D, ..."
               -> matched on `z_C`/`z_D`
      check 3  the witness-emission boilerplate (see below)

    53 hits, 0 real. A detector that cannot tell "imports pyhecke" from "says
    it does not import pyhecke" reports the compliant files as the violations,
    and the more carefully a probe documents its immunity the more certainly it
    is flagged. Same defect fixed the same way in this PR's
    `trm5_zcubed_live_producer_audit` corpus scan, which flagged its own test
    fixtures until string literals were excluded.

    Blanking rather than dropping the tokens keeps line and column positions,
    so the spacing-sensitive Z_TOKENS (`sqrt(q)/(q + 1)` vs `sqrt(q)/(q+1)`)
    still match code that really writes them.
    """
    lines = text.split("\n")
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return text          # unparseable: scan it whole rather than silently pass
    for tok in toks:
        if tok.type not in (tokenize.COMMENT, tokenize.STRING):
            continue
        (r1, c1), (r2, c2) = tok.start, tok.end
        for r in range(r1, min(r2, len(lines)) + 1):
            line = lines[r - 1]
            a = c1 if r == r1 else 0
            b = c2 if r == r2 else len(line)
            lines[r - 1] = line[:a] + " " * max(0, b - a) + line[b:]
    return "\n".join(lines)


texts = {p.name: _code_only(p.read_text()) for p in PROG}

# (1) no trace layer
TRACE_IMPORTS = ("pyhecke", "import gram", "from gram", "markov_peel",
                 "MarkovTrace", "markov_trace")
hits1 = sorted(n for n, t in texts.items() if any(k in t for k in TRACE_IMPORTS))
checks["no_markov_or_gram_layer_imported"] = hits1 == []
detail["trace_layer_hits"] = hits1

# (2) no trace parameter
Z_TOKENS = ("z_C", "z_D", "sqrt(q)/(q + 1)", "sqrt(q)/(q+1)",
            "q**3/(q**2 + 1)", "q**3/(q**2+1)")
hits2 = sorted(n for n, t in texts.items() if any(k in t for k in Z_TOKENS))
checks["no_trace_parameter_reference"] = hits2 == []
detail["trace_parameter_hits"] = hits2

# (3) no substrate anchor
#
# CORRECTED 2026-08-30. This matched the keywords against the WHOLE FILE TEXT
# and flagged 39 of 39 programme probes -- every one of them, i.e. the gate was
# firing on its own subject matter. All 39 were false positives from the
# witness-emission boilerplate, and one of the two spellings means the OPPOSITE
# of what the match read it as:
#
#   from qou_substrate.witness import WitnessBuilder   importing the witness
#                                                      WRITER is not using an
#                                                      anchor
#   q0_anchor=False                                    an explicit declaration
#                                                      that the probe IS
#                                                      anchor-free -- evidence
#                                                      FOR this check, counted
#                                                      against it
#
# Nobody saw it because nothing ran this gate: the committed witness recorded
# `no_substrate_anchor_reference: true` with an empty hit list, while a fresh
# run is red. Found by re-running it under the qou-cds2 producer-importability
# drain. The scan is now PER LINE with the boilerplate skipped, so a real
# `from q_parameter import Q`, a `1.10997` literal, or `q0_anchor="proton"`
# still fires. `_selftest_check3` below pins both directions.
ANCHOR = ("q_parameter", "qou_substrate", "Q_50_DIGIT", "1.10997", "q0_anchor")
_BOILERPLATE = (
    re.compile(r"from\s+qou_substrate\.witness\s+import"),
    re.compile(r"^\s*import\s+qou_substrate\b"),
    re.compile(r"q0_anchor\s*=\s*(?:False|None)\b"),
)


def _anchor_lines(text):
    """Lines that reference a substrate anchor for real, boilerplate removed."""
    out = []
    for line in text.split("\n"):
        if not any(k in line for k in ANCHOR):
            continue
        if any(b.search(line) for b in _BOILERPLATE):
            continue
        out.append(line.strip())
    return out


def _selftest_check3():
    """A gate that cannot fire is not a gate. Pin both directions."""
    must_fire = [
        "from q_parameter import Q_50_DIGIT_STR",
        "q0 = mp.mpf('1.10997858275138')",
        'w.save({"q0_anchor": "proton"})',
        "from qou_substrate.constants import q_at",
    ]
    must_not = [
        "from qou_substrate.witness import WitnessBuilder as _WB",
        "        witness, script_path=__file__, engine=None, q0_anchor=False)",
        "        witness, script_path=__file__, engine=None, q0_anchor=None)",
    ]
    for line in must_fire:
        assert _anchor_lines(line), f"check-3 selftest: should fire on {line!r}"
    for line in must_not:
        assert not _anchor_lines(line), f"check-3 selftest: should NOT fire on {line!r}"


_selftest_check3()

hits3 = sorted(n for n, t in texts.items() if _anchor_lines(t))
checks["no_substrate_anchor_reference"] = hits3 == []
detail["substrate_anchor_hits"] = hits3
detail["substrate_anchor_scan"] = (
    "per-line, skipping witness-emission boilerplate (the qou_substrate.witness "
    "import and q0_anchor=False/None, the latter being a declaration OF "
    "anchor-freedom); selftest pins 4 must-fire and 3 must-not-fire lines")

# (4) the q that appears is the quantum variable: the candidates are
# genuine Laurent polynomials over Z, an object no convention can move.
import sympy as sp

q = sp.symbols("q")
CANDIDATES = {
    "J_hopf": -(q + 1 / q),
    "two_q": q + 1 / q,
    "c3_form2": -2 - (1 - 1 / q) ** 2 * q,
    "D4": sp.expand((q - 1) ** 2 * (1 + q + q**2) / q**2),
}


def is_integer_laurent(f):
    f = sp.cancel(sp.together(sp.expand(f)))
    num, den = sp.fraction(f)
    pd = sp.Poly(den, q)
    if len(pd.monoms()) != 1:          # denominator must be a monomial
        return False
    c = pd.coeffs()[0]
    pn = sp.Poly(num, q)
    return all(sp.Rational(co, c).q == 1 for co in pn.coeffs())


checks["candidates_are_integer_laurent_in_q"] = all(
    is_integer_laurent(f) for f in CANDIDATES.values()
)
# and the two c_3 q-forms are the same element (re-verified here, so
# this gate also catches a transcription drift in either form)
checks["c3_two_forms_still_identical"] = (
    sp.simplify(CANDIDATES["c3_form2"] - CANDIDATES["J_hopf"]) == 0
)

# CONTROL: the gate must be able to fire. A z-dependent element is NOT
# an integer Laurent polynomial in q, and a probe text containing a
# trace import IS detected.
z_D = q**3 / (q**2 + 1)
checks["control_z_is_not_integer_laurent"] = not is_integer_laurent(z_D)
# The control used to be `any(k in "import pyhecke" for k in TRACE_IMPORTS)` --
# a substring test against a literal, which passes without ever touching the
# file scan. That is why it stayed green while all three scans were 100 %
# false-positive. It now runs the real projection, both directions.
_PLANTED_FIRES = "import pyhecke\nz = z_D\nfrom q_parameter import Q\n"
_PLANTED_QUIET = (
    '"""Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D."""\n'
    "# no pyhecke, no q_parameter, no z_D here either\n"
    "from qou_substrate.witness import WitnessBuilder as _WB\n"
    "_WB.wrap_legacy(w, script_path=__file__, engine=None, q0_anchor=False)\n"
)
_fires = _code_only(_PLANTED_FIRES)
_quiet = _code_only(_PLANTED_QUIET)
checks["control_detector_fires_on_planted_text"] = (
    any(k in _fires for k in TRACE_IMPORTS)
    and any(k in _fires for k in Z_TOKENS)
    and bool(_anchor_lines(_fires))
    and not any(k in _quiet for k in TRACE_IMPORTS)
    and not any(k in _quiet for k in Z_TOKENS)
    and not _anchor_lines(_quiet)
)

detail["classification"] = {
    "epsm_descent_chain_addenda_17_18_21_25": "VALID-immune (no q, no z, no anchor)",
    "ck_membership_gates_addendum_19": "VALID-immune (exact Laurent/cyclotomic arithmetic)",
    "ck_candidate_provenance_addendum_19": (
        "C-CONDITIONAL — the identification of J_Hopf and [2]_q as the "
        "corpus's named c_k / alpha_EM candidates comes from the "
        "C-frame ladder (qou-cds1); the gate verdicts are unaffected"
    ),
}

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_program_convention_immunity_probe",
    "engine": "python3-sympy-exact",
    "scriptFile": "gswz_program_convention_immunity_probe.py",
    "commitSha": _sha,
    "beans": ["qou-y3xv", "qou-9p9y"],
    "source": (
        "owner ruling docs/audits/2026-08-15-owner-ruling-convention-d-"
        "proton-color.md; template docs/audits/2026-08-15-c3-refutation-"
        "chain-convention-validity-audit.md; AGENTS.md c_k banner"
    ),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a): MEASURED convention- and anchor-immunity of the "
        "eps_m/GSWZ programme (no Markov/Gram layer, no trace "
        "parameter, no substrate anchor; the q that appears is the "
        "quantum variable and the candidates are integer Laurent "
        "elements). Standing gate: it fires if a z- or anchor-dependent "
        "input is ever wired in. Does NOT claim the c_k ladder survives "
        "convention D (that is qou-cds1); flags the single C-CONDITIONAL "
        "item in my merged wording — the provenance label on the c_k "
        "candidates, not the gate verdicts."
    ),
}
# Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
# opening for write TRUNCATES immediately, so an import that raises inside the
# `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
# is not importable from a bare producer context, which is how 22 witnesses were
# emptied by a single `producer_importability_audit` run.
from qou_substrate.witness import WitnessBuilder as _WB
import os as _os  # noqa: E402 -- provenance stamp
with open(HERE / "gswz_program_convention_immunity.witness.json", "w") as f:
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
