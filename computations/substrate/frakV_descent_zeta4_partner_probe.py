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
import json
import os

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

# (1b) The FULL ζ₄ orbit + isotypic decomposition (2026-07-02, bean 5nx8; Lean:
#      vModel_zeta4_sq / vModel_zeta4_cube / vModel_orbit_sum_zero /
#      vModel_sign_isotype_zero / vModel_eq_faithful_sum, sorry-free). The orbit closes
#      (ζ₄²=−1, ζ₄³= channel conjugation), the two NON-faithful isotypes vanish, and the
#      model is exactly the sum of the two FAITHFUL eigencomponents (1±i)/2·e^{±η}
#      (eigenvalues ±i). Constraint on the OPEN single-𝔙 assembly: it must be ζ₄-faithful.
R = sp.pi / 2 * I
orbit = [sp.expand_complex(V0(eta + k * R)) for k in range(4)]
zeta4_sq_eq_neg = bool(sp.simplify(orbit[2] + V0(eta)) == 0)
zeta4_cube_eq_channel_conj = bool(
    sp.simplify(orbit[3] - (sp.cosh(eta) - I * sp.sinh(eta))) == 0)
orbit_sum_zero = bool(sp.simplify(orbit[0] + orbit[1] + orbit[2] + orbit[3]) == 0)
sign_isotype_zero = bool(sp.simplify(orbit[0] - orbit[1] + orbit[2] - orbit[3]) == 0)
faithful_sum_eq = bool(sp.simplify(
    V0(eta) - ((1 + I) / 2 * sp.exp(eta) + (1 - I) / 2 * sp.exp(-eta))) == 0)

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
results["zeta4_orbit_isotypic"] = {
    "zeta4_sq_eq_neg_V0": zeta4_sq_eq_neg,
    "zeta4_cube_eq_channel_conj": zeta4_cube_eq_channel_conj,
    "orbit_sum_zero_trivial_isotype": orbit_sum_zero,
    "sign_isotype_zero": sign_isotype_zero,
    "faithful_sum_(1+i)/2*exp+(1-i)/2*exp(-)": faithful_sum_eq,
    "lean_cert": ("QOU/Mass/ComplexVolumeZeta4Partner: vModel_zeta4_sq, vModel_zeta4_cube, "
                  "vModel_orbit_sum_zero, vModel_sign_isotype_zero, vModel_eq_faithful_sum "
                  "(sorry-free)"),
    "assembly_constraint": ("the open single-𝔙 assembly must be ζ₄-FAITHFUL: a nonzero orbit "
                            "sum (trivial isotype) or sign-isotype component falsifies a "
                            "candidate assembly"),
}
assertions = {
    "zeta4_partner_eq_neg_conj": partner_eq_negconj,
    "zeta4_partner_eq_explicit_form": partner_eq_explicit,
    "zeta4_sq_eq_neg_V0": zeta4_sq_eq_neg,
    "zeta4_cube_eq_channel_conj": zeta4_cube_eq_channel_conj,
    "zeta4_orbit_sum_zero": orbit_sum_zero,
    "zeta4_sign_isotype_zero": sign_isotype_zero,
    "zeta4_faithful_sum_eq": faithful_sum_eq,
}
verdict = (
    "ζ₄-PARTNER RELATION VERIFIED (Lean-certified): V₀(η+iπ/2) = −conj V₀(η) = −cosh η + i·sinh η — "
    "the ζ₄=i rotation negates the bar-even (binding/Re) channel and keeps the bar-odd (Q_β/Im) "
    "channel, the fibre-level coupling of 𝔙 = Vol + i·CS. ORBIT/ISOTYPIC LAYER (2026-07-02, "
    "Lean-certified): the ζ₄ orbit closes (ζ₄²=−1, ζ₄³=channel conjugation), the trivial and sign "
    "isotypes BOTH vanish, and V₀ = (1+i)/2·e^η + (1−i)/2·e^{−η} is exactly the sum of the two "
    "FAITHFUL ±i eigencomponents — so any candidate single-𝔙 assembly must be ζ₄-faithful "
    "(falsifiable structural constraint on the OPEN assembly). DESCENT STILL OPEN: closing "
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
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# Payload carries a top-level `assertions` mapping → stamp (not wrap_legacy) preserves it.
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "frakV-descent-zeta4-partner-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"V0(η+iπ/2) = {lhs}")
print(f"partner = −conj V0(η)? {partner_eq_negconj};  = −cosh+i·sinh? {partner_eq_explicit}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
