---
# qou-lnkT
title: 'Doc fix: "no theorem covers the link case" describes proof status, not the formula reach — and Pandey-Wong contradicts it as written'
status: todo
type: task
priority: normal
tags:
    - documentation
    - one-loop
    - c-sigma
    - consistency
created_at: 2026-08-08T14:07:51Z
updated_at: 2026-08-08T14:07:51Z
---

## The defect

Two audits state flatly that no theorem covers the link case, citing only
Garoufalidis-Yoon:

  * `docs/audits/2026-08-07-one-loop-multicusp-derivation.md:157`
  * `docs/audits/2026-08-08-c-sigma-derivation-status.md` (~line 102)

Meanwhile two Borromean probes call the link reading "theorem-backed" on
Pandey-Wong (`borromean_jones_1loop_torsion.py:50`,
`borromean_nz_adjoint_torsion.py:82`). One part of the corpus says a link result
is theorem-backed while another says no link theorem exists — the
sibling-file contradiction this arc has now hit four times.

## The reconciliation, which no file states

Both are right about different statements, and the sentence needs to say which:

  * **tau_DG = adjoint torsion, for links** — Pandey-Wong arXiv:2308.06643
    ("Geometry of fundamental shadow link complements and applications to the
    1-loop conjecture") verifies the DG 1-loop conjecture for every fundamental
    shadow link complement, which includes the Borromean rings. THEOREM.
  * **the asymptotic prefactor c_sigma ~ |tau|^{-1/2}, for links** — no theorem.
    DGLZ eq (2.3) states the FORM for a general M with a flat G_C bundle,
    unrestricted by cusp number, but it is a one-loop saddle-point derivation
    and not a theorem. So the gap is RIGOUR, and it is missing for 4_1 too — it
    is not link-shaped at all.

Rewriting the line as "no theorem covers the link case" -> "the form is not
theorem-backed at ANY cusp number; what IS theorem-backed for links is
tau_DG = adjoint torsion (Pandey-Wong)" removes the contradiction and stops the
sentence reading as though links need a new formula when they need a proof of an
existing one.

## Also fix while there

`docs/audits/2026-08-07-one-loop-multicusp-derivation.md:157` says "Nothing in
`library/` supplies one" (a multi-cusp reference value). That is now false in a
specific way worth correcting: `library/arxiv-math-0611181v2/0611181v2.pdf` (van der Veen) supplies
the N-power `D = 3 pi` for both the Whitehead link and the Borromean rings, and
its Lemma 4 supplies the constant up to a normalisation now computed in
`computations/probes/one_loop_vdv_constant_closed_form_probe.py`.

## Definition of done

Both audits carry the distinction inline; the two Borromean probes' claim is
either confirmed against the Pandey-Wong scope or narrowed; and the
"nothing in library/" line is corrected.

Audit: `docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`
