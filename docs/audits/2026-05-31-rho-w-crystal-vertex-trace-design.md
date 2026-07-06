# 2026-05-31 — ρ_w per-crystal-vertex trace: design note + parameter-free prediction

**Branch:** `claude/rho-w-crystal-vertex-trace-2026-05-31`
**Audience:** anyone evaluating whether the genuine Kashiwara crystal-vertex
trace `ρ_w` closes the Δ_λ gate.
**Status of this note:** written **before** the compute, per the task gate
("state the formula, why it is parameter-free, and what it predicts for the
deuteron Δ_λ with NO tuned constant"). The compute
(`rho_w_crystal_vertex_trace.py`) then confirms the prediction to the digit.

**BLUF.** The genuine per-crystal-vertex trace `ρ_w(K)`, defined from first
principles as the diagonal matrix element of the Hoefsmit/Young seminormal
representation of the atomic braid `β_K` at crystal vertex `w ∈ B(λ) = SYT(λ)`,
is **fully determined and genuinely parameter-free**. Precisely *because* it is
parameter-free, its prediction is forced:

$$
\Delta_\lambda^{\rho_w}(K) \;=\; \sum_{w\in B(\lambda)} n^w_\lambda\,\rho_w(K)
\;=\; \sum_{T\in \mathrm{SYT}(\lambda)} \langle v_T\,|\,\rho_\lambda(\beta_K)\,|\,v_T\rangle
\;=\; \chi^\lambda(\beta_K).
$$

The crystal-vertex trace, summed over the crystal with the canonical
(regular) multiplicities `n^w_λ = 1`, **is identically the Hecke character
`χ^λ(β_K)` already on disk**. It therefore reproduces the same
`B = m_e·|Σ_λ y_λ χ^λ sgn(w₀) f^λ|` value that the 2026-05-29 retraction
already evaluated: **B_pred(D) = 0.380 MeV vs AME 2.225 MeV, −82.9%**;
honest Δ_λ residual **−0.744 m_e predicted vs −4.353 m_e target**, with
**no free parameter**.

**Verdict: ρ_w does NOT close the Δ_λ gate. closure_status = does_not_close.**
This is the genuinely un-tried object made rigorous — and the honest result
is that it carries **no new degree of freedom** beyond the χ^λ already
exhausted. Any "closure" still requires the back-solved `C_knot = 5.852`
(= target/prediction), the exact antipattern the discipline forbids. We do
**not** emit a closure-candidate witness and do **not** author a content
proposition.

---

## 1. What ρ_w SHOULD be (the genuine object, from first principles)

The 2026-05-25 Option-E audit posited

$$
  \Delta_\lambda(K) \;=\; \sum_{w \in \mathcal{B}_\lambda(\mathcal{B}_K)} n^w_\lambda \cdot \rho_w(K),
$$

and listed `ρ_w` as **(NOT EXIST)** — never implemented. The 2026-05-31
Option-E refresh confirmed v6–v9 compute a *global* character sum + a
back-solved scalar, never the per-vertex object. This note implements the
per-vertex object honestly.

**Crystal vertices (type A).** For the Iwahori–Hecke algebra `H_n(q)` of type
`A_{n-1}` acting in the Wedderburn block `λ ⊢ n`, the Kashiwara crystal
`B(λ)` of the irreducible `V_λ` is, as a set, the **standard Young tableaux
of shape λ**:

$$
B(\lambda) \;\cong\; \mathrm{SYT}(\lambda), \qquad |B(\lambda)| \;=\; f^\lambda \;=\; \dim V_\lambda .
$$

(Kashiwara, "On crystal bases"; the type-A `q→0` limit of the seminormal
basis is indexed by SYT — this is exactly the `skew_syt_count` /
`partitions_of` data already in `tools/pyhecke`.) Each tableau `T = w` is one
crystal vertex.

**Per-vertex weight = seminormal diagonal.** The Hoefsmit / Young **seminormal
(orthogonal) representation** `ρ_λ : H_n(q) → \mathrm{End}(V_λ)` has an
orthonormal basis `{v_T : T ∈ SYT(λ)}` on which the Jucys–Murphy elements act
diagonally (`L_k v_T = q^{2 c_T(k)} v_T`, `c_T(k)` = content of the cell
holding `k`), and the generators `σ_i` act by `2×2` blocks coupling
`T ↔ s_i·T` governed by the axial (content) distance. The **genuine
canonical-basis trace at crystal vertex `w = T`** is the diagonal matrix
element of the atomic braid:

$$
\boxed{\;\rho_w(K) \;:=\; \big\langle\, v_T \,\big|\, \rho_\lambda(\beta_K) \,\big|\, v_T \,\big\rangle\;}
\qquad (w = T \in \mathrm{SYT}(\lambda)) .
$$

This is **parameter-free**: every ingredient — the seminormal matrices
`ρ_λ(σ_i)` (Hoefsmit, closed form in `q`), the atomic braid word `β_K`
(fixed by the isotope `(Z,N)`), and the substrate `q_0` — is already
canonical and cached. There is **no scalar to tune, no scale menu, no
multiplicity to choose**.

**Canonical multiplicity.** In the regular (one-copy-per-irrep) Wedderburn
decomposition that defines the Markov trace, each crystal vertex appears with
multiplicity `n^w_λ = 1`. (The Kazhdan–Lusztig `n^w_λ` of the 2026-05-25
formula are the W-graph cell multiplicities; for the *diagonal trace* in a
single irreducible block they are uniformly `1` — the diagonal already counts
each vertex once. Choosing any other integer multiplicity would itself be a
free-parameter injection, which discipline forbids.)

---

## 2. The forced identity (why it cannot close the gap)

The trace of a matrix is the sum of its diagonal. Therefore, with `n^w_λ = 1`,

$$
\Delta_\lambda^{\rho_w}(K)
\;=\; \sum_{w\in B(\lambda)} 1\cdot\rho_w(K)
\;=\; \sum_{T\in\mathrm{SYT}(\lambda)} \langle v_T|\rho_\lambda(\beta_K)|v_T\rangle
\;=\; \mathrm{tr}\,\rho_\lambda(\beta_K)
\;=\; \chi^\lambda(\beta_K).
$$

**The per-crystal-vertex trace, summed over the crystal, is identically the
Hecke character.** This is not a coincidence to be engineered around — it is
the definition of a character as a trace. The "crystal" framing adds genuine
*per-vertex* structure (the individual `ρ_w` are real, computable numbers that
resolve `χ^λ` into `f^λ` summands), but the **sum over the crystal that Δ_λ
requires collapses back to `χ^λ`**, which is already fully used by the
2026-05-26 formula.

Consequently the binding prediction is *forced* to be the one the
2026-05-29 retraction already evaluated:

$$
B^{\rho_w}(K) \;=\; m_e\,\Big|\sum_{\lambda\vdash 3A} y_\lambda\,\Delta_\lambda^{\rho_w}(K)\,\mathrm{sgn}(w_0^{S_{\lambda'}})\,f^\lambda\Big|
\;=\; m_e\,\Big|\sum_\lambda y_\lambda\,\chi^\lambda(\beta_K)\,\mathrm{sgn}(w_0)\,f^\lambda\Big|.
$$

There is **no new degree of freedom** in `ρ_w` that was not already in
`χ^λ`. The per-vertex resolution is informative (it tells us *which crystal
vertices* carry the trace), but it cannot supply the missing 82.9% of the
deuteron binding, because that missing piece is, by construction, orthogonal
to anything expressible as a diagonal trace in the existing irreps.

---

## 3. What ρ_w predicts for the deuteron (parameter-free, stated up front)

Deuteron `(Z,N) = (1,1)`, `A=2`, `n = 6`, 11 partitions of 6. Using the
cached interface-inclusive `χ^λ(β_D)` (`chi-deuteron-h6-at-q0-50dps.witness.json`,
the same cache the retraction used) and the proved factors
`sgn(w_0^{S_{λ'}})`, `f^λ`, `y_λ`:

| Quantity | Predicted value (parameter-free) |
|----------|----------------------------------|
| `Σ_λ y_λ·Δ_λ^{ρ_w}·sgn(w₀)·f^λ`  (= `Σ_λ y_λ·χ^λ·sgn·f^λ`) | **−0.743901** |
| `B^{ρ_w}_pred = m_e·\|Σ\|` | **0.380132 MeV** |
| `B_D^AME` | 2.224566 MeV |
| **rel err** | **−82.91%** |
| Δ_λ residual predicted (`Σ y_λ·χ^λ·sgn·f^λ` in m_e) | **−0.743901 m_e** |
| Δ_λ residual target (`−B_D^AME / m_e`) | **−4.353367 m_e** |
| **captured fraction** | **17.1%** |
| **unaccounted residual** | **−3.609 m_e (82.9%)** |

The only factor that makes `B_pred` reach AME is the back-solve
`C_knot = B_D^AME/(m_e·|Σ|) = 5.852` — i.e. `target/prediction`, the
forbidden antipattern. **We do not apply it.**

**Prediction stated before compute (task gate):** because `Δ_λ^{ρ_w} ≡ χ^λ`,
the script must reproduce the retraction's −82.9% / −0.744 m_e to the digit.
If it does not, there is a bug. (It does — see §4 / the witness.)

---

## 4. Honest verdict (tiered)

| Object | Tier | Note |
|--------|------|------|
| Crystal vertex set `B(λ) = SYT(λ)` | **PROVED** | Kashiwara; `f^λ` via hook-length / `skew_syt_count`. |
| Per-vertex weight `ρ_w = ⟨v_T\|ρ_λ(β_K)\|v_T⟩` | **PROVED / parameter-free** | Hoefsmit seminormal diagonal; genuinely the un-tried object, now computed. |
| Multiplicity `n^w_λ = 1` (regular) | **PROVED** | diagonal trace counts each vertex once; any other choice is a free parameter. |
| `Δ_λ^{ρ_w} = Σ_w ρ_w = χ^λ` | **PROVED identity** | trace = sum of diagonal. **No new freedom.** |
| Deuteron Δ_λ closure | **does_not_close** | parameter-free residual −82.9%; closure needs back-solved `C_knot`. |

**`ρ_w` is genuinely parameter-free, and that is exactly why it fails:** the
honest crystal-vertex trace carries no degree of freedom beyond `χ^λ`, which
the six prior ansätze + the 2026-05-26 retracted claim already exhausted. The
−4.353 m_e deuteron target is **not** reachable from `Σ_λ y_λ χ^λ sgn f^λ`
without the forbidden `target/prediction` scalar.

**This is a valid, important negative result.** It closes the "but the genuine
ρ_w was never tried" loophole: the genuine ρ_w *has* now been defined and
computed from first principles, and it provably collapses to the already-failed
character sum. The Δ_λ gate is **not** closed by Option-E crystal weights;
future work must look outside the diagonal-trace family (e.g. the
interface/branching operator's *off-diagonal* content, per the gating-context
audit's "the q-dependent geometric correction lives inside χ^λ via the
interface operator" — but that is a different object than ρ_w).

---

## 5. What this note/PR deliberately does NOT do

- Does **not** introduce `C_knot`, a scale menu, or any `target/base`
  back-solve. The parameter-free residual is reported as-is.
- Does **not** author a content proposition/remark claiming closure. Per the
  task gate (closure_status = does_not_close), only this design note + the
  honest witness are emitted.
- Does **not** modify the fitted `option_e_v{6,7,8,9}.py` scripts.
- Does **not** assert `n^w_λ ≠ 1` to manufacture freedom — that would be a
  disguised fit.

## Cross-references

- [`docs/audits/2026-05-31-option-e-kashiwara-refresh-assessment.md`](2026-05-31-option-e-kashiwara-refresh-assessment.md) — establishes v6–v9 never implemented `ρ_w`; this note implements it.
- [`docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md`](2026-05-25-option-e-crystal-weight-delta-lambda.md) — original `ρ_w` formula; lists it (NOT EXIST).
- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — Δ_λ gate, six ansätze, 2026-05-29 retraction (D −82.9%).
- [`docs/audits/2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md) — KLR/crystal relaunch criteria.
- `computations/rho_w_crystal_vertex_trace.py` — the parameter-free compute (this PR).
- `computations/chi-deuteron-h6-at-q0-50dps.witness.json` — the χ^λ cache `Δ_λ^{ρ_w}` collapses to.
