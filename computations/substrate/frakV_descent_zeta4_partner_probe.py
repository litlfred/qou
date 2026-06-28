"""𝔙 fibre-descent — the ζ₄-partner relation + descent gap map (conj:binding-qbeta-complex-volume).

Track-c deepening of the descent conjecture. The merged work established:
  - the §3b descent class ComplexVolumeFibre + cosh/sinh non-vacuous model (#2951);
  - the ζ₄ moderator cosh(z+iπ/2)=i·sinh z (#2941);
  - the observable-level test is degenerate (Im(q₀)=0), so the descent is a FIBRE-level claim (#2951).

This probe verifies the ζ₄-PARTNER relation of the model — the next structural fact — and maps the
remaining gap, confirming the descent stays OPEN (gated on the Q_β keystone). No fit.

(1) ζ₄-partner: V₀(η + iπ/2) = −conj V₀(η) = −cosh η + i·sinh η, where V₀(η)=cosh η + i·sinh η.
    The ζ₄=i rotation NEGATES the bar-even (binding/Re) channel and KEEPS the bar-odd (Q_β/Im)
    channel — the fibre-level signature of how ζ₄ couples the two channels of 𝔙 = Vol + i·CS.
    (Lean: QOU/Mass/ComplexVolumeZeta4Partner.vModel_zeta4_partner, sorry-free.)

(2) descent gap map — what closing conj:binding-qbeta-complex-volume requires, and what's gated.
"""
import json, os

import sympy as sp

eta = sp.symbols("eta", real=True)
I = sp.I


def V0(z):
    return sp.cosh(z) + I * sp.sinh(z)


lhs = sp.simplify(V0(eta + sp.pi / 2 * I))
rhs_conj = sp.simplify(-sp.conjugate(V0(eta)))
rhs_explicit = sp.simplify(-sp.cosh(eta) + I * sp.sinh(eta))
partner_eq_negconj = bool(sp.simplify(lhs - rhs_conj) == 0)
partner_eq_explicit = bool(sp.simplify(lhs - rhs_explicit) == 0)

results = {
    "V0(eta+i*pi/2)": str(lhs),
    "neg_conj_V0(eta)": str(rhs_conj),
    "explicit_-cosh+i*sinh": str(rhs_explicit),
    "partner_eq_neg_conj": partner_eq_negconj,
    "partner_eq_explicit": partner_eq_explicit,
    "lean_cert": "QOU/Mass/ComplexVolumeZeta4Partner.vModel_zeta4_partner (sorry-free)",
    "descent_gap_map": {
        "Re_V_binding": "characterized: q-Hermite/Rogers-Szegő MOMENT, Habiro (q-1)·cyclotomic log-coeff tower (PR #2899/#2929) — NOT closed (no finite low-order q-difference operator; Stages 3-4)",
        "Im_V_qbeta": "GATED: the c_k Habiro element / SW-residue jet-prolongation symbol R(q,ξ) (conj:qdifference-kernel-prolongation-symbol); fitting Φ₂ is the forbidden 'seventh ansatz' (2026-06-09 scope)",
        "single_fibre_V": "OPEN: that Re and Im descend from ONE 𝔙 = E₀·tr_M((Π_free−1)∘ℳ). Established: ζ₄ generator coupling + ζ₄-partner relation + bar-parity class. Missing: both fibre kernels AND their assembly into one trace object.",
        "observable_level": "DEGENERATE (Im(q₀)=0) — must NOT be used to claim closure (numerology guard, #2951).",
    },
}
assertions = {
    "zeta4_partner_eq_neg_conj": partner_eq_negconj,
    "zeta4_partner_eq_explicit_form": partner_eq_explicit,
}
verdict = (
    "ζ₄-PARTNER RELATION VERIFIED (Lean-certified): V₀(η+iπ/2) = −conj V₀(η) = −cosh η + i·sinh η — "
    "the ζ₄=i rotation negates the bar-even (binding/Re) channel and keeps the bar-odd (Q_β/Im) "
    "channel, the fibre-level coupling of 𝔙 = Vol + i·CS. DESCENT STILL OPEN: closing "
    "conj:binding-qbeta-complex-volume needs (i) the binding fibre kernel (characterized, not a "
    "finite low-order operator), (ii) the Q_β fibre kernel (GATED on the SW-residue keystone; Φ₂ fit "
    "forbidden), and (iii) their assembly into one trace object 𝔙. The generator coupling + "
    "ζ₄-partner relation + bar-parity class are proved; the kernel descent is not, and the "
    "observable-level test is degenerate (must not be used to claim closure). Advanced, not closed."
)
witness = {
    "computation": "frakV_descent_zeta4_partner_probe",
    "description": (
        "Verifies the ζ₄-partner relation V₀(η+iπ/2)=−conj V₀(η) of the complex-volume model "
        "(Lean-certified) and maps the remaining gap for conj:binding-qbeta-complex-volume, "
        "confirming the descent stays open (gated on the Q_β keystone)."
    ),
    "discipline": "no fit; sympy symbolic exact; Lean-certified core; descent-OPEN (a)-scoped.",
    "auditOnly": "docs/audits/2026-06-28-frakV-descent-zeta4-partner.md",
    "results": results,
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}
out = os.path.join("computations", "substrate", "frakV-descent-zeta4-partner-probe.witness.json")
with open(out, "w") as f:
    json.dump(witness, f, indent=2)

print(f"V0(η+iπ/2) = {lhs}")
print(f"partner = −conj V0(η)? {partner_eq_negconj};  = −cosh+i·sinh? {partner_eq_explicit}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
