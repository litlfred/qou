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
Read the real paper (library/arxiv-2402.01890v4/2402.01890v4.pdf, Ormeño Bastías–Martin–Ryom-Hansen).

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

## OPTION-B-HARD ASSESSMENT (2026-08-02) — GATED on the bridge; no fit permitted
Read the paper's core structure (eq 1.2, Thms 6–7): as (CS_n, SP_k(n))-bimodules,
  **S^k V_n  ≅  ⊕_{λ ∈ Par^sph_{k,n}}  S(λ) ⊗ G_k(λ)**
where S(λ) is the S_n Specht module and G_k(λ) a simple SP_k(n)-module. So the
multiplicity of Specht module S(λ) in the k-th symmetric power of the defining
module V_n **is dim G_k(λ)** — the small integers live here.

**Why this does NOT close ν_SDP (honest, no fit):**
- To identify ν_SDP(atom) with a dim G_k(λ), one must FIRST prove the QOU atom's
  saturating Hecke module (the H_{3A}(q) Wedderburn block the SDP selects) IS the
  Specht summand of some symmetric power S^k V_{n}. That **bridge is unproven**;
  the QOU rep is a Markov-trace-weighted Hecke module, not manifestly a symmetric
  power of a defining module.
- **The multiplicities are generic small integers** — computed mult of Specht in
  Sym^k V_4: k=1→1, k=2→1, k=3→2, k=4→2, k=5→4. {1,2} appear routinely at small
  k. So choosing (k,λ) to hit ν_SDP∈{1,2} WITHOUT the bridge is a FIT (numerology),
  which the three-calibration discipline forbids.

**Verdict:** Option-B-hard is a *genuinely-open, statable* problem, not a closure.
The concrete open bridge: **prove the atom's saturating H_{3A}(q) block ≅ S(λ)⊗G_k(λ)
summand of S^k V_{3A} for a CANONICAL k (not tuned).** Only that iso — derived, not
fitted — would make dim G_k(λ) = ν_SDP a theorem. Until then ν_SDP stays underived;
no SP-based value wired to production. This is the LAST surviving derivational route
for ρ_F=ν_SDP (Option A refuted, Option-B-coarse refuted, direct SDP 0/3558).

## OPTION-B-HARD BRIDGE — REFUTED for the deuteron (2026-08-02, scope-(a))
Attacked the bridge directly (probe `computations/probes/sp_bridge_symmetric_power_test.py`).
Necessary condition at q=1 (H_{3A}(1)=CS_{3A}): the atom's Wedderburn-block
support must equal the S_{3A}-support of some S^k(V_{3A}). Computed S^k(C^6)
decompositions via Murnaghan-Nakayama and compared to the deuteron active support
{(6),(5,1),(4,2),(4,1,1),(3,3),(2,2,2),(2,1,1,1,1)}:

- **(2,1^4)** ∈ Sym^k(C^6) only for **k≥10**; **(3,2,1)** ∈ Sym^k for **all k≥4**.
- So every symmetric power containing (2,1^4) ALSO contains (3,2,1).
- The deuteron contains (2,1^4) but **excludes** (3,2,1) (its forbidden
  self-conjugate block). No k satisfies both ⇒ **the deuteron module is not any
  S^k V_6** under the canonical strand count n=3A. (A non-canonical n would be a fit.)

Also structural: SP_k(n) and H_n(q) are Schur-Weyl centralizers of DIFFERENT dual
pairs (CS_n on S^k V_n vs U_q(gl_m) on tensor space), so no canonical functor
carries a Hecke block to an SP_k(n) module — consistent with the concrete refutation.

**FINAL verdict — all known ρ_F=ν_SDP bridges now closed:**
- Option A (1-loop torsion): REFUTED (qou-r307, |τ|≠integer).
- Option B coarse (dim SP_k): REFUTED (dim=2,9,31,…).
- Option B hard (SP_k(n) decomp via bridge): REFUTED for deuteron (support window
  incompatibility).
- Direct SDP: 0/3558 is an over-determination artifact (qou-vd7j), not a derivation.
No route derives ν_SDP; conj:kashaev-density-equals-sdp-multiplicity stays honestly
open with every known bridge concretely closed. No value wired to production.
