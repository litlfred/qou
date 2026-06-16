# B_sym is a linear-chain binding — closed form + saturation (2026-06-16)

**Status:** audit — positive structural result. Sits beside
[`2026-06-16-binding-undershoot-is-shell-structure.md`](2026-06-16-binding-undershoot-is-shell-structure.md)
(the sibling audit, which established that the `B_sym`→AME residual *changes
sign* and is therefore shell structure, not a uniform law). This audit adds the
**mechanism**: it derives the closed form of `B_sym`, shows it is *exactly* a
linear-chain spanning binding, and identifies the missing physics as **nuclear
saturation** (binding ∝ A, not the chain's per-bond sum and not C(A,2) pairs).
Together they explain *why* the trace over-binds the deuteron and under-binds the
closures, and *why* no bond-count topology can fix it.

**Provenance / caveats.** Numbers are live from the canonical engine
(`tr_m_atom_via_transfer.tr_m_atom_zn`, the fine-Bratteli transfer trace) in the
in-repo `computations/` checkout. α = E₀ = m_e/(q₀(q₀−1)) (CAL-1);
q₀ = 1.1099785955573347 (canonical proton-anchor); binding data = AME2020;
CODATA-2022 masses + 1σ from `codata_constants` / the validation witness.
**EXPLORATORY** — no production rewire, no fit, no witness emitted. Tool:
[`computations/m_sym_error_budget.py`](../../computations/m_sym_error_budget.py)
(`--decompose`, `--bonds`, `--rescore`).

## 1. The closed form: B_sym is an additive linear chain

The bound atom braid `atom_braid_word_3A(Z, N)` orders the strands as
`['p']·Z + ['n']·N` and places an inter-nucleon crossing **only between adjacent
nucleons** (generator `3k+2`). The chain therefore carries exactly

> **(Z−1) p-p bonds · 1 p-n interface bond · (N−1) n-n bonds**  = (A−1) bonds total.

Each crossing sits on a *distinct* generator, so the per-knot trace factorizes
over the bond positions and the log-binding is **exactly additive**:

$$
  B_\mathrm{sym}(Z,N) \;=\; \alpha\big[(Z-1)\,L_{pp} \;+\; L_{pn} \;+\; (N-1)\,L_{nn}\big],
  \qquad L_X = \ln\frac{\mathrm{tr}_M(\text{free})}{\mathrm{tr}_M(\text{1 X-bond})}.
$$

Verified to the 50-dps floor against the exact 3A-strand trace (`--bonds` §B):

| nuc | (Z−1)·b_pp | 1·b_pn | (N−1)·b_nn | Σ (additive) | B_sym (exact trace) | match |
|---|--:|--:|--:|--:|--:|:--:|
| ²H  | 0.000 | 3.890 | 0.000  | 3.8897  | 3.8897  | ✓ |
| ³H  | 0.000 | 3.890 | 5.178  | 9.0677  | 9.0677  | ✓ |
| ³He | 2.907 | 3.890 | 0.000  | 6.7969  | 6.7969  | ✓ |
| ⁴He | 2.907 | 3.890 | 5.178  | 11.9749 | 11.9749 | ✓ |
| ⁶Li | 5.814 | 3.890 | 10.356 | 20.0600 | 20.0600 | ✓ |
| ⁷Li | 5.814 | 3.890 | 15.534 | 25.2380 | 25.2380 | ✓ |

The per-single-bond bindings `b_X = α·L_X` carry the **chirality ordering**

> **b_nn = 5.178  >  b_pn = 3.890  >  b_pp = 2.907  MeV**,

i.e. n-n crossings bind hardest, p-p softest (matching the dashboard bond-type L:
nn = 1.237 > pn = 0.929 > pp = 0.695). Note `b_pn` is exactly the deuteron
`B_sym` — the deuteron *is* the single p-n bond.

## 2. The two misses are the two ends of one linear chain

Because `B_sym` is a fixed (A−1)-bond chain with fixed per-bond strengths, its
two failure modes are forced and opposite:

- **²H over-binds** (B_sym 3.89 vs B_AME 2.22, ratio 0.57). A single p-n bond is
  *stronger* than the real, weakly-bound deuteron. This is the **deuteron
  anomaly** — and it is unavoidable: the chain's p-n quantum is a fixed 3.89 MeV.
- **⁴He under-binds** (11.98 vs 28.30, ratio 2.36). The chain carries 3 adjacent
  bonds where the real, tightly-bound α-particle binds all **C(4,2)=6** pairwise
  bonds (3 missing p-n diagonals) plus the **magic closure**.

This is *not* one bad crossing type — every bond type contributes, and n-n is the
*strongest*. The miss is a **topology** property of the (A−1)-bond chain.

## 3. Re-score: no bond-count topology works — binding saturates in A

Swapping the chain's (A−1) bond count for the fully-connected **C(A,2)** count
(same *derived* per-bond strengths — **not a fit**, only the combinatorial count
changes; `--rescore`):

| nuc | A | B_AME | B_chain | B_allpairs | AME/chain | AME/allpairs |
|---|--:|--:|--:|--:|--:|--:|
| ²H  | 2 | 2.225  | 3.890  | 3.890  | 0.572 | 0.572 |
| ⁴He | 4 | 28.296 | 11.975 | 23.644 | 2.363 | **1.197** |
| ⁶Li | 6 | 31.994 | 20.060 | 59.263 | 1.595 | **0.540** |
| ⁷Li | 7 | 39.245 | 25.238 | 86.466 | 1.555 | **0.454** |

**RMS error (MeV): chain 10.1 → all-pairs 22.5 (worse).** All-pairs *fixes* ⁴He
(2.36 → 1.20) but **over-binds the heavier nuclei by ~2×**, because C(A,2) grows
quadratically while real nuclear binding **saturates ~linearly in A**
(≈ const·A, the empirical ~8 MeV/nucleon plateau). The chain's (A−1) scaling has
the *right* near-linear A-dependence (asymptotically ≈ 4 MeV/nucleon for N=Z) but
~half the coefficient and no closures; all-pairs has the *wrong* quadratic
scaling. This **quantitatively confirms** the sibling audit's refutation of the
C(A,2) combinatorial count, and isolates the missing physics as **saturation +
shell closure**, neither of which is a bond-count.

## 4. The residual is real — error bars rule out "noise"

`Δ_model = m_sym − M_exp = B_AME − B_sym` *exactly* (the unbound `Z·m_p + N·m_n`
cancels). Attaching the prediction error bar (σ_pred ≈ CODATA m_p/m_n ≈ 1e-6 MeV)
to the residual (`--decompose`):

| nuc | Δ = B_AME − B_sym (MeV) | Δ/A | Δ/σ |
|---|--:|--:|--:|
| ²H  | −1.665 | −0.83 | 2.3e6 |
| ³H  | −0.586 | −0.20 | 4.1e5 |
| ³He | +0.921 | +0.31 | 1.0e6 |
| ⁴He | +16.321 | +4.08 | 1.1e7 |
| ⁶Li | +11.934 | +1.99 | 4.6e6 |
| ⁷Li | +14.007 | +2.00 | 2.9e6 |

The sign-change is **10⁵–10⁷σ** significant: it is structurally real, not a
numerical or experimental artifact. So a *uniform* rescale (volume normalization,
colored-Jones, complex-q) provably cannot close it — consistent with the sibling
audit's Option-3 conclusion.

## 5. Conclusion (joins the sibling audit)

`B_sym` is, in closed form, a **linear-chain spanning binding**: a fixed (A−1)
adjacent bonds with fixed chirality-ordered per-bond strengths. This pins the two
failure modes — the deuteron over-bind (single p-n quantum) and the ⁴He
under-bind (chain misses pairs + magic closure) — as opposite ends of one
structure, and shows that **no bond-count topology** (chain or all-pairs) closes
the gap, because the residual is **nuclear saturation + shell structure**, not a
counting choice. The framework's "smooth categorical term + explicit shell
corrections (B_magic first)" treatment is therefore the right shape; the next
lever is a **categorically-derived saturation/shell term**, *not* a 7th uniform
or bond-count ansatz (CLAUDE.md Δ_λ gate).

## References

- [`2026-06-16-binding-undershoot-is-shell-structure.md`](2026-06-16-binding-undershoot-is-shell-structure.md)
  — sibling audit: the residual changes sign ⇒ shell structure (this doc supplies
  the closed-form mechanism + saturation).
- [`computations/m_sym_error_budget.py`](../../computations/m_sym_error_budget.py)
  — the tool (`--decompose`, `--bonds`, `--rescore`).
- `computations/mass_binding_dashboard.py` — the engine (`/dashboard-low`).
- `computations/mass_at_3A_proper.py::atom_braid_word_3A` — the linear-chain braid
  word (the `['p']·Z + ['n']·N` adjacency this audit reads off).
- `computations/magic_A_formula.py` — `B_magic` (the working ⁴He shell correction).
- PR #2343 — the error-budget + decomposition tool.
