---
# qou-8d5e
title: Remark interpreting 1108.5286v3.pdf at content/quantum-observable-universe/braids-and-knots/marko…
status: todo
type: task
created_at: 2026-08-08T16:13:05Z
updated_at: 2026-08-08T16:13:05Z
---

The inductive-limit Lean file declares the affine construction 'open R&D content' with no literature pointer. A remark recording what IS known about the affine algebra's trace/homology data — Theorem 2's q-independence and Theorem 1(d)'s trace-separation criterion, with the correction caveat — turns an unscoped open item into one with a stated starting point, without wiring anything.

**From the source**
- Theorem 2 (= Thms 3.4, 3.6, 3.8), §3, stated p.3-4 — For epsilon in C outside sqrt(-1)R^*, HH_*(H(R,q^epsilon)) is isomorphic to the W-invariant algebraic differential forms Omega^*(T~)^W on the extended quotient of the torus by the Weyl group — in particular independent of the parameter q.
  Use here: A q-independence statement for the homological invariants of the affine Hecke algebra, which is the structural backdrop for the inductive-limit trace object the corpus leaves open. It says the trace-theoretic data of the algebra is rigid in q, so any q-dependence QOU observes in a Markov-trace-derived quantity must come from the REPRESENTATION/evaluation side, not from the homology of the algebra — a useful, checkable separation of concerns for the fibre-vs-archimedean distinction AGENTS.md insists on.
- Theorem 1(d),(e), §2, p.3 — For epsilon outside sqrt(-1)R^*, two representations pi(w,i,t,epsilon) and pi(w',i',t',epsilon) have the SAME TRACE iff w = w', i = i' and t, t' lie in one Z_W(w)-orbit; and the collection forms a Q-basis of the Grothendieck group of finite-dimensional H(R,q^epsilon)-representations.
  Use here: A trace-separation criterion: it says precisely which representation data a trace functional can and cannot distinguish. That is the affine analogue of the question QOU's Markov trace answers at finite n (traces separate Wedderburn blocks indexed by partitions), and it is the statement the inductive-limit construction would need in order to know its limiting trace is faithful. Cite with the v3 correction caveat attached.
- Theorem 1(b) + §2.1-2.2, p.16-22 (with the 2021 correction) — The representations of the family H(R,q^epsilon), epsilon in C, come in families depending analytically on epsilon (matrix coefficients conjecturally algebraic in q^{1/2}).
  Use here: An analyticity-in-the-deformation-parameter statement for Hecke representations. This is the affine instance of the fibre-level framing AGENTS.md sets out for c_k(q) — the object is analytic in q at the fibre level, and each substrate anchor is one evaluation of it. It supports that framing with an external theorem rather than an assertion, though it does not establish it for the finite H_n(q) the corpus computes with.

Source: `library/arxiv-1108.5286v3/1108.5286v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
