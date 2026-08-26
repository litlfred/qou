---
# qou-thtm
title: 'Faddeev-Niemi |Q_H|^{3/4}: pre-registered test of the non-additive energy class'
status: completed
type: task
priority: normal
created_at: 2026-08-26T03:01:15Z
updated_at: 2026-08-26T03:18:59Z
---

## Verdict (2026-08-26): DEAD, scope (b), two invariants

Prereg committed+pushed BEFORE any numbers: `d3819883225e` (docs/audits/2026-08-26-faddeev-niemi-prereg.md).
Probe: computations/probes/faddeev_niemi_qh34_binding_prereg_probe.py
Audit: docs/audits/2026-08-26-faddeev-niemi-qh34-verdict.md

Every pre-registered refutation criterion fired on every target; the one
post-hoc check that could have rescued the class also refuted.

**S1 (shape), scope (b)** — B = c*A^p gives B/A = c*A^{p-1}, strictly monotone
for p != 1, constant for p = 1; B_AME/A is non-monotone with an interior max at
56Fe (8.7904 MeV/nucleon). The exponent 3/4 was never the issue: the entire
one-parameter power-law family is excluded for every exponent at once.

**S2 (sign), scope (b)** — the Faddeev Hamiltonian is a sum of squares so
c|Q_H|^{3/4} >= 0 identically, but the residual it must supply is mixed-sign
(R(2H) = -0.607 MeV vs R(4He) = +19.616). Same shape as the KL-positivity prune.
NOT anticipated by the prereg; surfaced as the log fit going complex.

Numbers: F1 max rel 8.42; F2 1.967; F3 (2 free params, more freedom than the
hypothesis allows) p = 1.262 — outside the [0.70,0.80] window — and still 210 %
off. On the positive-residual subset F3 gives p = 0.9918, i.e. a volume term,
which is what B_sym already is at too small a coefficient.

NOT claimed: 'no functional of a single global charge can work' is false as
stated (arity conflation). With Q_H free the form is a reparametrisation and
unfalsifiable. Verdict is a disjunction: pinned Q_H excluded, free Q_H not a claim.

Non-additive knot-energy functionals as a CLASS are untouched — one functional
form retired, not an ingredient. GAP-1/GAP-2 unchanged; nothing newly opened.
