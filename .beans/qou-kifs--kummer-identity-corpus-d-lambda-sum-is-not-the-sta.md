---
# qou-kifs
title: 'Kummer identity: corpus D := Lambda-sum is NOT the standard Bloch-Wigner (Im Li_2 + log|z|arg(1-z))'
status: todo
type: task
priority: medium
created_at: 2026-08-08T19:20:00Z
updated_at: 2026-08-08T19:20:00Z
---

Found 2026-08-08 by reading **Neumann–Zagier 1985 §3** (uploaded by the owner
as a scan; readable once `poppler` was installed — see `folio-assistant` PR #85).

## The two definitions

`QOU/Archimedean/BlochWignerLobachevsky.lean` **defines**

    BlochWigner_lob z  :=  Λ(arg z) + Λ(arg 1/(1−z)) + Λ(arg(1−1/z))

The literature's Bloch–Wigner function is a **different expression**:

    D(z) = Im Li₂(z) + log|z| · arg(1 − z)          (N–Z eq. (39))

built from the **dilogarithm**, not from `Λ`. Their equality is **Kummer's
identity** (Lewin, *Polylogarithms*, p. 121 eq. (5.5)), which N–Z invoke
explicitly to pass from

    eq. (37)   Vol(S(z)) = Λ(α) + Λ(β) + Λ(γ)       [Milnor, Thurston Ch. 7]
    eq. (38)   Vol(S(z)) = D(z)

It is a **theorem, not a definitional unfolding**. The corpus has silently
adopted the name of one object for the other.

## Why it matters (and why it has NOT yet caused harm)

Exposure is small — only 2 files mention `BlochWigner_lob`, and the second
(`QOU/Machinery/QDilogarithm.lean`) only *cites* it in prose. **No downstream
theorem has transported a dilogarithm fact onto it.** So this is a naming/status
defect caught early, not a live laundering.

The risk it creates is specific: N–Z, Zagier, and Bloch prove things about
**their** `D` — the five-term relation, functional equations, the `Vol + i·CS`
framing. Any of those cited onto `BlochWigner_lob` would be unjustified until
Kummer is proved. The docstring now says this explicitly.

## Status of the identity: currently UNPROVABLE here

**Mathlib has no polylogarithm or dilogarithm at all** — checked 2026-08-08
across the restored olean tree: zero `*polylog*` / `*dilog*` modules. So
`Im Li₂` cannot even be *written* in this corpus, let alone related to the
Λ-sum. Closing this bean therefore requires either:

* a Mathlib-gap fill defining `Li₂` (a real piece of work — the analytic
  continuation to the cut plane `ℂ \ [1,∞)` is the substantive part, and N–Z
  rely on it); or
* proving Kummer in a `Λ`/`Cl₂`-only formulation that never mentions `Li₂`,
  which may be possible since `Cl₂(θ) = Im Li₂(e^{iθ})` already ties the two on
  the unit circle — the corpus has `BlochWigner_unit_circle` for exactly that
  case. **Extending off `|z| = 1` is the open part.**

The second route is the cheaper one and should be scoped first.

## Evidence they do agree (not assumed blindly)

`computations/qbeta/xi_classical_limit_probe.py` (PR #4769, merged) evaluates
the **dilogarithm** form `polylog(2,z).imag + arg(1−z)·log|z|` and cross-checks
it against the corpus's angle route at the substrate anchor: they match to the
Λ-sum probe's ~1e-6 series accuracy. That is **evidence for Kummer, not a proof
of it** — and it means my own merged probe straddles the two definitions, which
is only safe *because* the cross-check is there.

## Relation to H4 / T2 — a useful factorisation

The H4 target factors cleanly:

    Vol(S(z))  =  D(z)        (GEOMETRIC — the whole of H4/T2, open)
    D(z)       =  Λ-sum       (ANALYTIC  — Kummer, this bean)

Proving Kummer closes the **analytic** factor only. It does **not** shorten H4:
the geometric identification is untouched by it. Recorded so nobody mistakes
"we proved the Bloch–Wigner identity" for progress on the volume theorem.

## Links

* `qou-5gai` H4 / `qou-w3eg` — the geometric factor
* `qou-idvt` T2 — same statement, ideal-tetrahedron side
* N–Z §3, eqs (37)–(39) — `library/1-s20-0040938385900047-main/1-s2.0-0040938385900047-main.pdf`
