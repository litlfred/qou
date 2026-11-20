---
# qou-mk7u
title: 'GAP: muon carrier at the Murakami real deformation xi = 2 pi i + u of the 4_1 colored Jones (does a derived u exist?)'
status: todo
type: task
priority: normal
created_at: 2026-11-20T16:00:00Z
updated_at: 2026-11-20T16:00:00Z
parent: qou-6gf9
---

Filed from PR #8573 (`docs/audits/2026-11-20-lepton-self-energy-front.md` §5 item 1).

**Context.** Read literally, CAL-2 `m_mu/m_e = Vol(4_1)/hbar_q^2` is the leading
term of the 4_1 Kashaev log-series at the ROOT OF UNITY e^{2 pi i/N} with
N = 2 pi/hbar_q^2 = 640.019. PR #8573 proves (Lean `MuonKashaevReading.lean`,
sorry-free) and measures (exact Kashaev sum at N = 640, 641) that every
correction of that series is positive (+4.555e7 ppb on m_mu), while the
measured residual needs -211 ppb. Scope (b) for that class.

**The route not attempted.** The substrate q_0 is REAL, not a root of unity.
The held source [murakami-h2011] (`library/arxiv-1102.3530v1`, Thm 1.3) gives
the asymptotics of J_N(4_1; e^{xi/N}) at xi = 2 pi i + u with u real,
0 < u < log((3+sqrt5)/2), governed by the deformed SL(2,C) Chern-Simons
function S(u) and twisted torsion T(u). That is a real deformation of the
leading term with coefficients fixed by topology.

**What would close this honestly.** A corpus-derived value of u (or of the
pair (N, u)) from q_0 BEFORE looking at the residual - e.g. a substrate
identification of the meridian eigenvalue exp(u/2). Choosing u to hit -211 ppb
is a fit and is forbidden (NO FITTING, owner 2026-09-05).

**What is NOT known.** Whether any such identification exists in the corpus;
`grep` for `xi = 2 pi i + u`, `S(u)`, `Murakami.*Thm 1.3` was not run beyond the
library section quoted. Run the six-path corpus-grep first.

Stays clear of the q_0-derivation gate (qou-eic1): q_0 is held fixed.
