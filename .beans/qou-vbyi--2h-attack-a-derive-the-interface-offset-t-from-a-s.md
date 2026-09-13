---
# qou-vbyi
title: '2H ATTACK A: derive the interface offset t from a SPACE index (3S1-3D1 tensor channel) - the only route past the proved flavour-only degeneracy'
status: todo
type: task
priority: normal
created_at: 2026-08-25T18:37:51Z
updated_at: 2026-09-12T10:26:56Z
parent: qou-9ot5
---

## 2026-08-25 — this is now one of only TWO surviving routes for 2H

Every braid-word freedom at A=2 is eliminated (docs/audits/2026-08-25-deuteron-attack-c-convergence.md,
follow-up section): interface element (no principled one lands), bridge crossing count
(even m unbinds, odd m needs ~29), topology (chain == complete graph at A=2, one bond),
ordering (one arrangement), multiplicity (forbidden), alpha (pinned by beta-decay),
and any flavour-only mu (exactly degenerate).

Surviving: (1) the functional form B = -alpha*ln|tr_M|, which is POSITED - no derivation,
nothing in Lean, only a notation-table row, and a dead citation; and (2) THIS - a space
index carrying L, the only route past the degeneracy and the only place 3S1-3D1 tensor
mixing can live.


## 2026-08-31 — the PREMISE needs narrowing: a space FACTOR cannot do this

This bean is titled "the only route past the proved flavour-only degeneracy".
Checked before building, and the obvious reading of it -- add a space factor --
does not work. The counter is in `qou-kj4v`'s own sentence:

  "In S-wave Pauli LOCKS spin to isospin (SPACE SYMMETRIC => spin and isospin
   symmetry opposite): S=1 <=> T=0, S=0 <=> T=1."

**Both pn channels are S-wave.** 3S1 and 1S0 are both `S` in the term symbol
2M+1 L_J, i.e. L = 0. So a factor keyed on L takes the SAME value on both, and a
common factor cannot separate what is already equal.

PROVED, axiom-free:
`QOU.QBeta.InterfaceScalar.separable_interface_degenerate` -- for an arbitrary
separable interface fSpin(S) * fIso(T) * fSpace(L), with the Pauli lock as
hypothesis and one and the same `ell` on both sides, the channels are equal for
EVERY fSpace. Not specific to L: it covers any space index entering
multiplicatively and keyed on anything constant across the two channels.
Companion `common_factor_preserves_degeneracy`, also axiom-free.

Guard: `computations/probes/space_index_separability_probe.py` (4/4). Reproduces
this bean cluster's degenerate value 0.18614164195799085217 to 4.8e-21, and
mu+ + mu- = 1 exactly.

## What this does NOT close -- the bean stays open, with a sharper target

The Standard Model's tensor force is a spin-space **COUPLING**, and a product of
a spin function and a space function is exactly what a coupling is not. A
**non-separable** interface -- one whose value depends jointly on (S, L) and does
not factor -- is untouched by the above and is the live shape.

So the construction target is sharper than this bean states: **the space index
must enter as a COUPLING, not as a factor.** That is checkable before anything is
built, which is the point of recording it here.

Also worth separating: 3S1-3D1 mixing IS a genuine L = 0 vs L = 2 admixture
within the deuteron, and a space index is the right home for it. It is simply
not what separates the deuteron from the virtual state -- both of those are
S-wave. The bean currently runs the two together.

Scope (b) for the exclusion, invariant cited (commutativity + a common factor).
The physics input -- both channels S-wave -- is quoted from qou-kj4v, not derived
here; it is standard.

## 2026-09-03 — route 1 (non-separable (S,L) TENSOR coupling) PRUNED as a fix for the sign defect, scope-(b)

The 'live shape' left open above — a non-separable spin-space coupling, the 3S1-3D1 tensor force — cannot fix either A=2 defect. Two invariants, formalized (QOU.QBeta.TensorCouplingSinglet, PR on branch claude/two-nucleon-sign-defect-2026-09-03; exact-sympy companion computations/probes/tensor_coupling_singlet_check_probe.py 13/13):

(A) The tensor operator S12(n) = 3(s1.n)(s2.n) - s1.s2 acts as the SCALAR 3(1-|n|^2) on the spin singlet |ud>-|du>, for EVERY n — the singlet is an eigenvector of both s1.s2 (=-3) and (s1.n)(s2.n) (=-|n|^2). So no coupling built from them has an off-diagonal element out of S=0 (at J=0, S=0 has no L=2 partner). pp/nn are pure S=0 by Pauli in S-wave => UNTOUCHED by any tensor coupling, any strength, any direction. The sign defect cannot be reached by this route.

(B) Where the coupling does act (the triplet), 2x2 interlacing: the coupled ground level is STRICTLY below the uncoupled 3S1 level whenever t != 0 (lowerEigen_lt_left_of_ne). Tensor mixing binds the deuteron HARDER; it is already 27.3% over-bound. Wrong direction.

Verdict: route 1 is a dead end for both defects. Not excluded: unbinding as such (the writhe-normalised sigma^{-2k} class unbinds at 6-9x magnitude), the binding law itself, or the pp/nn bond/carrier assignment. The sign is now boxed from every interface-side direction (scalar, separable factor, non-separable coupling); the surviving directions are all outside the interface value. Audit: docs/audits/2026-09-03-tensor-coupling-cannot-unbind-singlet.md. qou-7nwg's T-projector route is complementary and already proved to bind (mu_sum_eq_one).

## CORRECTION 2026-09-03: the 'pp/nn bond/carrier assignment' listed as a survivor in the previous append is NOT open — production bonds are single species-keyed crossings (single_crossing_binds) and species-keyed interfaces are refuted (content_keyed_interface_refuted, 2026-08-09). With the tensor route closed (#6488) and the stacked class closed on ordering (route 3), no in-algebra sign direction remains. Sector status = eight-closures §6: structural change needed.

## 2026-09-08 — R2 'signs first' selected by the owner; and the structural change now has a name. Every in-algebra sign direction is closed (above). The owner's 2026-09-08 ruling — braid words selected by γγ production + confinement SDP at q₀, never census — is the candidate structural change: a pp word SELECTED rather than template-ASSIGNED (uu→σ). Carrier: bean qou-ales. Do not re-attack interface-side routes.



## 2026-09-11 — qou-ales step 3: a SELECTED (not template-assigned) pp bond flips the diproton sign (scope-(a), measured, no AME read)
Probe computations/probes/gamma_gamma_h3_psd_selector_probe.py (branch claude/ales-step3-h3-sdp-selector-2026-09-11, proton pin, 60 dps). The template pp bond sigma_2 is not gamma-gamma-produced (Lean not_gammaGamma_single). Among gamma-gamma bonds (sigma_2 sigma_3^-1)^m on the H_6 interface, the confinement-SDP Frobenius-positivity / quadratic-form readings admit m in {0, 3} (m = 1, 2, 4, 5 fail: chi_(3,3) < 0); the minimal NON-ZERO survivor is m = 3. Under the live log law B = E_0 ln(tr_free/tr_atom) on the full six-strand words: template -> +2.0710 MeV (binds, the known defect); m = 3 -> -0.004469 MeV, UNBOUND; m = 1,2,4,5 -> +3.9..+4.2 MeV. So the sign flips with the selected bond, at 4.5 keV magnitude. Caveats: (a) the LITERAL Matrix.PosSemidef reading admits no non-zero bond at all (a vertex power's (2,1) image is never symmetric; Lean vertex_not_psdFeasible), so the flip lives in the weaker readings; (b) the magnitude is small because (sigma sigma^-1)^3 is within 0.11 of the identity in the (2,1) block at q0 -- tr_atom/tr_free = 1.00106; (c) nothing was compared to a measured diproton value. This is the 'structural change' the 2026-09-03 correction said was needed, measured once; it is not a derivation of the bond.

PR #7192 carries the measurement above.


## 2026-09-12 — PR #7192 merged to main (6a593ed858). The diproton-sign measurement above is now on main (gamma_gamma_h3_psd_selector_probe.py, 8/8; audit 2026-09-11-gamma-gamma-word-selection-step3.md). Scope-(a) stands; the bond that unbinds the diproton is the SELECTED gamma-gamma bond G^3 = (sigma_2 sigma_3^-1)^3 under the form/Frobenius readings, and at q = 1 that bond is the identity (the 3-cycle cubed), which is why the effect is 4.5 keV. Bean stays open: which PSD reading is canonical is an owner call (qou-ales).
