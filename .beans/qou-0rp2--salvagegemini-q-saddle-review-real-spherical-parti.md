---
# qou-0rp2
title: 'Salvage(gemini q-saddle): review real ''spherical partition algebra'' (arXiv 2402.01890, Ormeno-Bastias/Martin/Ryom-Hansen — NOT Bowman-Orellana) as driver-(x) grounding for nu_SDP'
status: todo
type: task
created_at: 2026-08-02T13:07:40Z
updated_at: 2026-08-02T13:07:40Z
---

## Source
Salvaged from the Gemini "q-deformed saddle-offsets" brainstorm (2026-08-02).
Gemini proposed identifying ν_SDP with the dimension of the idempotent
truncation of the "spherical partition algebra" (its "Option B"), citing
arXiv:2402.01890.

## Verification / CORRECTION
- Paper arXiv:2402.01890 **"On the spherical partition algebra" is REAL**
  (math.RT, 2024). It defines an idempotent subalgebra SP_k of the partition
  algebra P_k via the trivial-rep embedding of S_n.
- **Gemini HALLUCINATED the authors.** Actual authors: **Katherine Ormeño
  Bastías, Paul Martin, Steen Ryom-Hansen** — NOT "Bowman & Orellana".
  (Bowman–Orellana do have partition-algebra work, but not this paper.)
- Therefore Gemini's specific claims ("dimension = cardinality of MacMahon
  bipartite partitions", "Schur–Weyl duality with H_n(q)", "bimodule
  isomorphism to the active SDP constraint set") are **Gemini's paraphrase,
  NOT verified against the actual paper.** Read the real paper before adopting
  any of it.

## Task
1. Read arXiv:2402.01890 (Ormeño Bastías–Martin–Ryom-Hansen). Extract the ACTUAL
   dim SP_k formula and its combinatorial index set (verify or refute the
   "bipartite MacMahon" characterisation Gemini asserted).
2. Assess whether SP_k's dimension can *derive* ν_SDP as a partition-algebra
   count — this is the categorical home already claimed for
   `conj:kashaev-density-equals-sdp-multiplicity` under driver (x)
   "MacMahon-style partition-algebra identities". If it does, it upgrades
   ρ_F=ν_SDP from a 3-point coincidence toward a representation-theoretic count.
3. If it genuinely grounds the count, add ref + a Lean formalization angle
   (finite combinatorics is tractable in Mathlib). If not, record the negative.

## Priority / caveats
- LOWER priority than the 1-loop-torsion probe `qou-r307` (that one is a
  concrete number check; this is a lit-read + structural assessment).
- Anti-laundering: building SP_k in Lean and taking a class instance is NOT a
  proof of ρ_F=ν_SDP. Only a derivation is. Keep the conjecture conditional.
- The "q_0≈1.11 vs classical q=1 rigidity" gap Gemini waved at (its "Option C",
  Kazhdan–Lusztig SDP, arXiv:2604.18894) is NOT beaned: that arXiv id is
  unverified and Gemini could not name its authors — treat as likely
  fabricated until confirmed.

## ASSESSMENT (2026-08-02) — Gemini's coarse Option-B claim REFUTED; only the hard route survives
Read the real paper (uploads/2402.01890v4.pdf, Ormeño Bastías–Martin–Ryom-Hansen).

**What the paper actually proves (Thm 2 + abstract):**
- SP_k = idempotent (trivial-rep) subalgebra of the partition algebra P_k.
- **rk_{C[x]} SP_k = bp_k = #{bipartite partitions of k}** = OEIS **A002774**
  = (1, 2, 9, 31, 109, 339, …).
- For t=n∈ℕ: SP_k(n) decomposes the **k-th symmetric power** of the CS_n
  defining module; the paper gives decomposition numbers + projectives/tiltings
  (quasi-hereditary for all t≠0).

**Refutation of Gemini's specific claim (ν_SDP = dim SP_k = #bipartite):**
- dim SP_k ∈ {2, 9, 31, 109, …} — **never** the multiplicity {1,2}.
- QOU atoms use H_{3A}: deuteron A=2 → k∼6, tritium A=3 → k∼9, where dim SP_k is
  in the **hundreds** (65–300 by the Σp(j)p(k−j) count; A002774 is larger still).
- So ν_SDP is NOT the dimension of the spherical partition algebra. Gemini's
  Option-B *as stated* is FALSE (a coarse category error: whole-algebra dim vs a
  single-block multiplicity).

**What survives (the hard route, NOT refuted):**
- ν_SDP is a single **decomposition number / block multiplicity**, and the
  paper's real content — the Sym^k(CS_n-defining-module) permutation
  decomposition + SP_k(t) decomposition numbers — IS where small integers 1,2
  live. So the only viable Option-B is: identify ν_SDP(atom) with a SPECIFIC
  SP_k(n) decomposition number, via the (still unproven) bimodule iso
  QOU-saturating-Wedderburn-block ↔ SP_k(n) indecomposable. That map is
  unestablished; the paper gives the target multiplicities but not the bridge.

**Verdict:** Option A (1-loop torsion, bean qou-r307) REFUTED; Option B's easy
dimensional form REFUTED; only Option-B-hard (specific-multiplicity via bimodule
iso) and the direct SDP route (bean qou-vd7j) remain for deriving ν_SDP. No route
currently DERIVES ν_SDP∈{1,2} — the conj:kashaev-density-equals-sdp-multiplicity
stays honestly open (single Lean sorry). No fit wired.
