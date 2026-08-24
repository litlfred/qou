"""𝔙 ζ₄ coupling — fibre-level (real) vs observable-level (degenerate): the numerology guard.

Option-2 follow-up to the ζ₄ moderator (QOU/Mass/Zeta4ComplexVolumeModerator, merged): is the
FULL complex-volume observable 𝔙 = Vol + i·CS an exact ζ₄-rotate between Re 𝔙 (binding) and
Im 𝔙 (Q_β)? The existing complex-volume-unification witness already flags the crux:
"Im(q₀) = 0 ⇒ both real; complex structure is fibre-level; that both descend from one fibre 𝔙 is
the OPEN conjecture (conj:binding-qbeta-complex-volume), not proved."

This probe makes the level distinction precise — and GUARDS against the numerology trap of
"closing" the conjecture with an observable-level numerical match:

(1) OBSERVABLE LEVEL is DEGENERATE. At the substrate anchor q₀ is REAL (η = log q₀ real,
    Im(q₀) = 0). The ζ₄ rotation η ↦ η+iπ/2 gives cosh(η+iπ/2) = i·sinh(η) — PURE IMAGINARY for
    real η, so Re(ζ₄-rotate of a real Re-channel) = 0. The two real observables 𝔈_bind and 𝔔_β
    are therefore NOT related by an observable-level ζ₄ rotation (it sends real → imaginary, real
    part 0). Testing "are the observables ζ₄-rotates" numerically is a category error.

(2) FIBRE / GENERATOR LEVEL is where the coupling lives and is EXACT (Lean-certified). The
    ζ₄ moderator cosh(η+iπ/2) = i·sinh(η) IS the precise statement of the corpus assertion that
    Q_β (bar-odd sinh) is the "sinh partner of the bar-even cosh" scale — the bar-even (cosh,
    Re 𝔙) and bar-odd (sinh, Im 𝔙) channels are ζ₄-rotation partners as fibre generators, with
    Φ₄ = q²+1 (the shared binding-L₂ / Q_β-a₁ residue) the ζ₄ = i locus.

VERDICT (scope): the ζ₄ coupling is FIBRE-level and generator-exact; the OBSERVABLE-level
"binding and Q_β are one number under ζ₄" is degenerate (Im(q₀)=0) and must NOT be used to close
conj:binding-qbeta-complex-volume — that descent remains the open conjecture. No fit.
"""

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402
import json, os, sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
import sympy as sp
import mpmath as mp
from qou_substrate import constants as C

eta = sp.symbols("eta", real=True)
I = sp.I
hpi = sp.pi / 2 * I

# (1) observable-level degeneracy: Re of the ζ₄-rotate of a real cosh-channel is 0
rot_cosh = sp.cosh(eta + hpi)                  # = i·sinh(η)
re_part_real_eta = sp.simplify(sp.re(rot_cosh.rewrite(sp.exp)))  # Re for real η
# (Re(i·sinh η) = 0 for real η)
observable_real_part_zero = bool(sp.simplify(re_part_real_eta) == 0)

# numeric: the two real observables are NOT ζ₄-related (rotate gives 0 real part)
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
q0 = mp.mpf(C.Q) if hasattr(C, "Q") else mp.mpf("1.10998")
eta0 = mp.log(q0)
cosh_eta0 = mp.cosh(eta0)                       # bar-even (Re channel) magnitude scale
zeta4_rotate_real_part = mp.re(mp.cosh(eta0 + mp.j * (mp.pi / 2)))  # ~0 (full mpmath precision)

# (2) fibre/generator level: the ζ₄ moderator is exact (re-verified symbolically; Lean-certified)
mod_ok = bool(sp.simplify(sp.cosh(eta + hpi) - I * sp.sinh(eta)) == 0)
# Φ₄ = q²+1 vanishes at ζ₄ = i (the shared residue locus)
qv = sp.symbols("q")
phi4_zeta4 = bool(sp.simplify((qv ** 2 + 1).subs(qv, I)) == 0)

results = {
    "observable_level": {
        "q0_real_Im_zero": True,
        "Re(zeta4_rotate_of_cosh_channel)_symbolic": str(re_part_real_eta),
        "Re(zeta4_rotate)_numeric_at_q0": mp.nstr(zeta4_rotate_real_part, mp.mp.dps),
        "degenerate": observable_real_part_zero,
        "reading": "ζ₄-rotation sends a real (Re-channel) quantity to pure imaginary; its real part is 0, so the two real observables 𝔈_bind, 𝔔_β are NOT observable-level ζ₄-rotates. Numerology trap avoided.",
    },
    "fibre_level": {
        "zeta4_moderator_cosh_to_i_sinh_exact": mod_ok,
        "phi4_vanishes_at_zeta4": phi4_zeta4,
        "lean_cert": "QOU/Mass/Zeta4ComplexVolumeModerator.lean (sorry-free)",
        "reading": "cosh ↔ i·sinh under η↦η+iπ/2 is the exact 'Q_β is the bar-odd sinh partner of the bar-even cosh scale' assertion at the fibre/generator level; Φ₄ = ζ₄ locus is the shared binding-L₂ / Q_β-a₁ residue.",
    },
}
assertions = {
    "observable_zeta4_rotation_degenerate_ImQ0_zero": observable_real_part_zero,
    "fibre_zeta4_moderator_exact": mod_ok,
    "phi4_root_is_zeta4": phi4_zeta4,
}
verdict = (
    "ζ₄ COUPLING IS FIBRE-LEVEL (generator-exact, Lean-certified); OBSERVABLE-LEVEL ζ₄-rotation is "
    "DEGENERATE (Im(q₀)=0 ⇒ the rotate of a real Re-channel is pure imaginary, real part 0), so the "
    "two real observables 𝔈_bind and 𝔔_β are NOT observable-level ζ₄-rotates. This GUARDS against "
    "closing conj:binding-qbeta-complex-volume by a numerical observable match (a numerology trap / "
    "fibre-vs-observable level conflation, per the AGENTS.md Im(q) banner). What IS established: the "
    "ζ₄ moderator cosh↦i·sinh is the exact fibre-level form of the corpus 'Q_β = bar-odd sinh "
    "partner of the bar-even cosh scale' assertion, with Φ₄ = q²+1 the shared ζ₄ = i residue locus. "
    "The full descent of binding (Re) and Q_β (Im) from ONE fibre 𝔙 remains the OPEN conjecture — "
    "advanced (generator-level coupling proved) but not closed; closure needs the fibre-level "
    "kernel identification, not an observable match."
)
witness = {
    "computation": "frakV_zeta4_fibre_vs_observable_probe",
    "description": (
        "Distinguishes the fibre-level (exact, Lean-certified) ζ₄ coupling of Re 𝔙 (binding) and "
        "Im 𝔙 (Q_β) from the observable-level test, which is DEGENERATE at the real anchor q₀ "
        "(Im(q₀)=0). Guards against closing conj:binding-qbeta-complex-volume via a numerology "
        "observable match; records that the descent from one fibre 𝔙 stays open."
    ),
    "discipline": "no fit; sympy symbolic + mpmath at q₀; Lean-certified fibre core; numerology-guard (a)-scoped.",
    "auditOnly": "docs/audits/2026-06-28-frakV-zeta4-fibre-vs-observable.md",
    "results": results,
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# Payload carries a top-level `assertions` mapping → stamp (not wrap_legacy) preserves it.
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "frakV-zeta4-fibre-vs-observable-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2)
    f.write("\n")

print(f"(1) observable-level Re(ζ₄-rotate) = {re_part_real_eta}  (degenerate: {observable_real_part_zero})")
print(f"    numeric Re at q₀ = {results['observable_level']['Re(zeta4_rotate)_numeric_at_q0']}")
print(f"(2) fibre ζ₄ moderator exact: {mod_ok};  Φ₄(ζ₄)=0: {phi4_zeta4}")
print(f"\nallPassed = {witness['allPassed']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
