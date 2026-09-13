# The binding producer's braid words are not level-local, and no trace-preserving reordering makes them so

**Bean:** `qou-hxz4` (parent `qou-vyvt`; continues `qou-sv7h`, the binding-compute scaling wall).
**Question posed:** PR #7160 proved that for a *level-local* word — every seminormal level touched in exactly one contiguous factor — the seminormal character is a dim-free path sum, `χ^λ(T_β) = Σ_{T∈SYT(λ)} Π_j ⟨T|F_j|T⟩`, and shipped [`computations/chi_path_sum_seminormal.py`](../../computations/chi_path_sum_seminormal.py). If the words that `hecke_core_legacy.unified_iterative_correction` (the binding producer, reached via `binding_energy`) hands its Rust kernel were level-local, that path sum would collapse the `O(L·dim²)` wall of `qou-sv7h`. Are they?
**Probe:** [`computations/probes/uic_word_level_locality_probe.py`](../../computations/probes/uic_word_level_locality_probe.py) — 11/11, 29 s wall, `mpmath` at 70 dps, `q` from `Q_50_DIGIT_STR` (proton pin, as a string; `q_at()` returns float64 and is not used). Witness `computations/probes/uic-word-level-locality.witness.json`. Log `/tmp/uic-word-level-locality.log`.

---

## 1. Claim

1. **No.** For every atom (D, T, ³He, ⁴He, ⁵Li) and every partition size `k = 3 … 11`, the word the producer builds is a **single segment covering all `k−1` generators**. The first letter that breaks locality is letter `n_gens + 1` (0-based position `k−1`): `σ_1` recurs after `σ_2 … σ_{k−1}` have all intervened. Every adjacent generator pair `(g, g+1)` interleaves.
2. **No trace-preserving reordering restores it.** Both available trace identities are tested and excluded: (a) every cyclic rotation of every word is single-segment (all `L` rotations, all atoms, all `k`); (b) the `T_w`-support of the word's Hecke element — and of every rotation's, `k ≤ 5` — lies in **no** two-block parabolic product `W_J·W_K` / `W_K·W_J`, which excludes every rewriting by the Hecke relations into ≥ 2 disjoint-interval factors (`k ≤ 7`, scope-(b); `k ≥ 8` not expanded, scope-(a)).
3. **The path-sum on this word is the dense route, not a shortcut.** Fed a single-segment word, `chi_lambda_path_sum` degenerates to the direct seminormal trace at `O(L·dim²)` in pure `mpmath` — measured **23×, 30×, 40× slower** than the Rust kernel `lp_accumulator_step_traces_mpfr` at `k = 6, 7, 8` (dim 16, 35, 90). It reproduces the kernel's numbers (worst relative disagreement `8.6e-50`, the kernel's 50-dps floor), which is what validates the word transcription — and it buys nothing.

**Why, in one sentence.** `_step_chain_generic` embeds all `11A + C(A,2)` crossings of an `A`-nucleon atom into a *fixed* `H_k(q)`, `k ≤ 11`, by cycling the generator index `g mod (k−1)` through every letter of every step; a level-local word needs each nucleon on its own strands (the `3A`-strand `atom_braid_word_3A` family the mass producer uses), which is a **different element** with different traces, not a re-bracketing of this one.

## 2. Evidence

### 2.1 The words, captured by instrumentation (not read off docstrings)

`_lp_kernel_steps` was monkey-patched with a recorder, so the chains below are the exact `(c, d, gen)` triples serialised for the Rust kernel — including the colour-weighted p–n offset `_PN_D_MP = −0.10445824776972628901…` (`bring_color_weighted`, **not** `−h/2 = −0.10453014939781965771…`, 6.9e-4 apart) and the exact nn offset `−ℏ_q`. Every partition of a given `k` receives identical chains, equal to `_step_chain_generic(ordering[i], ordering[:i], k−1)`; `c = 1` throughout, so each letter is `σ_g + d·I` and transcribes to the path-sum's sign-0 form with shift `−d`.

Ground-state ordering: D `pn`, T `pnn`, ³He `pnp`, ⁴He `pnpn`, ⁵Li `pnpnp`. Word length `L = 11A + C(A,2)`; per step, 7 `G0` + 4 `G1` intra letters then one inter letter per previous nucleon. Four distinct offsets on the D word: `σ` (`d = 0`), `σ⁻¹` (`d = −h`), averaged (`d = −h/2`), pn (`d = _PN_D_MP`).

Generator sequence of the first step at `k = 4` (`n_gens = 3`): `1 2 3 1 2 3 1 2 3 1 2` — `σ_1` at positions 0, 3, 6, 9.

### 2.2 Per-atom table

| atom | A | L | k range | level-local? | first break (0-based pos, letter) | adjacent pairs interleaving | rotations with > 1 segment | path-sum vs kernel (k ≤ 6) | time, path-sum / kernel |
|---|---|---|---|---|---|---|---|---|---|
| ²H | 2 | 23 | 2…11 | **no** (1 segment, all k ≥ 3) | pos `k−1`, `σ_1` after `σ_2…σ_{k−1}` | `(k−2)/(k−2)` | 0 / 23 | ≤ 4.8e-50 | 0.117 s / 0.006 s (k=6, all λ) |
| ³H | 3 | 36 | 2…11 | **no** | same | all | 0 / 36 | ≤ 4.0e-50 | 0.148 s / 0.010 s |
| ³He | 3 | 36 | 2…11 | **no** | same | all | 0 / 36 | ≤ 6.4e-50 | 0.146 s / 0.009 s |
| ⁴He | 4 | 50 | 2…11 | **no** | same | all | 0 / 50 | ≤ 8.6e-50 | 0.180 s / 0.013 s |
| ⁵Li | 5 | 65 | 2…11 | **no** | same | all | 0 / 65 | not run (kernel cross-check capped at ⁴He) | — |

`k = 2` has a single generator and is trivially one segment (both partitions are 1-dimensional). "Path-sum vs kernel" is the worst relative disagreement over all `λ ⊢ k`, `k = 3 … 6`, between the single-segment path-sum on the transcribed word and the kernel's own final `trace·exp(log_norm)` on the producer's chains.

### 2.3 Rewriting exclusion — support outside every two-block parabolic product

`x = Π_pos (T_{g_pos} + d_pos)` expanded in the `T_w` basis of `H_k(q)` at `q₀` (right multiplication in word order, `T_w T_s = T_{ws}` if `ℓ(ws) > ℓ(w)` else `h·T_w + T_{ws}`). The expansion is validated three ways: the trivial and sign representations reproduce `Π(q + d)` and `Π(−q⁻¹ + d)` at every `k`; at `k = 3` contracting it with the seminormal characters of the `T_w` (Rust `chi_lambdas_braid_mpfr` on reduced words) reproduces the path-sum `χ^λ(x)` to `7.7e-51`.

Minimum, over all `2(k−2)` two-block sets, of the number of support elements outside the set (support = `|coef| > 10⁻⁵⁰·max`):

| atom | k=3 (of 6) | k=4 (of 24) | k=5 (of 120) | k=6 (of 720) | k=7 (of 5040) | rotations (k ≤ 5), min outside |
|---|---|---|---|---|---|---|
| ²H | 2 / 6 | 6 / 18 | 46 / 94 | 334 / 536 | 480 / 836 | 2, 5, 36 |
| ³H | 2 / 6 | 12 / 24 | 72 / 120 | 472 / 712 | 3103 / 4470 | 2, 12, 72 |
| ³He | 2 / 6 | 12 / 24 | 72 / 120 | 476 / 716 | 3356 / 4724 | 2, 12, 71 |
| ⁴He | 2 / 6 | 12 / 24 | 72 / 120 | 480 / 720 | 3600 / 5040 | 2, 12, 72 |
| ⁵Li | 2 / 6 | 12 / 24 | 72 / 120 | 480 / 720 | 3600 / 5040 | 2, 12, 72 |

(`a / b` = elements outside the closest two-block set / support size.) Every entry is positive: no atom, no `k ≤ 7`, no rotation at `k ≤ 5` has its support inside any two-block set.

**The `T_{w₀}` coefficient alone is NOT decisive, and this is why the support test is the one used.** A first version of this probe tested only whether the longest element `w₀` appears in the support (it cannot for a ≥ 2-segment product, by length). That coefficient is genuinely zero for ²H at `k = 6` (`6.7e-125` relative) and `k = 7` (support 836 of 5040; the 23-letter deuteron word does not reach `w₀`, whose reduced words have 21 letters with `s_1` six times), and `8.8e-54` for ³H at `k = 7`. A necessary condition that fails to fire is not an exclusion; the support test fires on all of them.

### 2.4 The invariant, stated

*Claim.* If `x = F_1 F_2 ⋯ F_m` (any word order) with `F_i` in the parabolic subalgebra `H_{I_i}` of a generator interval `I_i`, the `I_i` pairwise disjoint and `m ≥ 2`, then `supp_{T_w}(x) ⊆ W_J·W_K` or `⊆ W_K·W_J` for some split `J = [1..j]`, `K = [j+1..k−1]`.

*Proof.* (i) `supp(T_u T_v) ⊆ {u′v′ : u′ ≤ u, v′ ≤ v}` (subword order), by induction on `ℓ(v)`: `T_u T_{vs} = (T_u T_v) T_s` and `T_w T_s ∈ span{T_{ws}, T_w}`. Hence `supp(F_1⋯F_m) ⊆ W_{I_1}⋯W_{I_m}` as a set product. (ii) Adjacent intervals merge (`W_I W_{I′} ⊆ W_{I∪I′}` when `I ∪ I′` is an interval) and non-adjacent intervals commute elementwise (their generators differ by ≥ 2), so any ordered product of ≥ 2 interval parabolics sits inside a two-block product. Step (ii) is also checked **exhaustively by computer** for `k = 3 … 6` (every ordered interval partition, every ordering) — the probe's `reduction` assertion.

Consequently a nonempty `supp(x) \ (W_J W_K)` for every split and both orders excludes every level-local factorisation of `x` with ≥ 2 segments — for the element, hence for every word equal to it under the Hecke relations (the seminormal representation is an algebra homomorphism, so all such words share every `χ^λ`). Each cyclic rotation is a different element (`tr(AB) = tr(BA)` is the identity that licenses it), so rotations are expanded and tested individually.

**Cyclic rotation, the analytic version.** A word splits into ≥ 2 segments only if some prefix and the complementary suffix have disjoint generator sets. Every window of `k−1` consecutive letters of the cyclic word contains all `k−1` generators, and `L = 11A + C(A,2) ≥ 23 > 2(k−1)` for all `k ≤ 11`, so every prefix of length ≥ `k−1` and every suffix of length ≥ `k−1` contain all generators; a split point would need one side shorter than `k−1`, but then the other side still contains every generator including those on the short side. Rotation preserves the window property. The probe confirms it on all `L` rotations of every word.

### 2.5 The degenerate route, timed

| k | λ (largest dim) | dim | L (²H) | path-sum, one λ | Rust kernel, one λ | ratio |
|---|---|---|---|---|---|---|
| 6 | (3,2,1) | 16 | 23 | 0.04 s | 0.002 s | 23× |
| 7 | (4,2,1) | 35 | 23 | 0.24 s | 0.008 s | 30× |
| 8 | (4,2,1,1) | 90 | 23 | 1.72 s | 0.043 s | 40× |

On a single-segment word the orbit BFS reaches all of `SYT(λ)` for every `T`, so `weight(T)` costs `O(L·dim)` and the trace `O(L·dim²)` — the same complexity as the kernel, in `mpmath` instead of MPFR.

### 2.6 A reordering that IS a trace identity, measured for calibration

Reversing the cycle (`g ↦ n_gens − 1 − g`, the diagram automorphism `s_i ↦ s_{k−i} = w₀ s_i w₀`) is conjugation by `T_{w₀}` and must preserve every `χ^λ`. Measured on the kernel at `k = 4, 5, 6` for ²H and ⁴He, all partitions: agreement `≤ 3e-50`. It is a genuine reordering identity — and the reversed word is still cyclic, still single-segment. The `_step_chain_22` docstring's *"characters are independent of which `σ_j` we use because `χ(σ_j) = h` for all `j`"* is true letter by letter and is not a statement about products; the assignment convention is load-bearing for the numbers except under symmetries like this one.

## 3. Implications

- **The #7160 path-sum is not a route past `qou-sv7h`'s wall for this producer.** It cannot be wired in; on this word it is a slower reimplementation of the kernel. Nothing is wired, no flag is added, no recorded number moves.
- **The obstruction is the embedding design, not the word order.** `unified_iterative_correction` accumulates a running product over a fixed partition table (`k ≤ 11`, 193 partitions, dims to 2310, independent of `A`) — that is what makes the word cyclic, and it is also what makes the per-partition scale `C_λ = m_e·H_q(λ)·y_λ·ρ_λ` and the Pass-2 gate well-defined on a fixed index set. A level-local binding word requires each nucleon on its own strands, `n = 3A` (the `atom_braid_word_3A` family already in the mass producer), whose partition set grows with `A` (385 at ⁶Li) and whose traces are those of a **different element**. That is a re-derivation of the binding producer, not an optimisation of it.
- **The remaining cost is where `qou-sv7h` left it**: the Rust kernel's `O(L·dim²)` MPFR accumulation at dims ≤ 2310 (deuterium 942 s kernel-live per `qou-i7ju`; ⁶Li ~4000 s). Speed-ups have to come from the kernel side (bean `qou-sv7h`'s steps 2–4), not from a change of bracketing.
- **Producer docstring.** `_step_chain_22`'s "independent of which `σ_j`" sentence is letter-level only; left as is (wording, not a number — and "ask the owner before changing things").

## 4. Options — with a recommendation marked as judgement

1. **No-op (the default).** Leave the binding producer on its cyclic embedding and the Rust kernel; record this negative. Costs nothing; forecloses nothing; the wall stays at kernel speed.
2. **Re-embed the binding word level-locally** — nucleon `k` on generators `{3k+1, 3k+2}`, bond `σ_{3k+3}`, in `H_{3A}(q)` (the `atom_braid_word_3A` family), and take the traces the accumulator needs from the path-sum (all 385 partitions of ⁶Li in 8.5 s). *What it means:* a new binding producer, not a faster one — a different Hecke element in a different algebra. *What it costs:* a new producer behind a flag, a new partition table (`λ ⊢ 3A`), a decision on what `C_λ` and the Pass-2 gate mean on it. *What it risks:* every recorded binding number (`hadron-knot-table`, the A-series `−7.27 … −8.14`, the `uic_*` probes) moves. *What it commits to:* retiring the cyclic embedding as the binding convention. **Not started here** — it changes the element, and choosing it because it is faster would be the ranking error AGENTS.md warns against; whether the `3A`-strand element is the *right* binding object is the owner's call.
3. **Speed the kernel** — export `dense_dense_mul_mpfr`, exact-chain COO in Rust, `k_exact` policy — the existing `qou-sv7h` plan; orthogonal to this bean.

My judgement: **1 now**; 2 only as an explicit owner-authorised re-derivation. If the owner says nothing, nothing changes and the finding stands as recorded.

## 5. What is NOT established

- Hecke-relation rewriting is excluded only for `k ≤ 7` (expansion cost `k!`); `k = 8 … 11` are scope-(a). The cyclic-rotation exclusion holds at every `k`.
- Conjugation by an arbitrary invertible element of `H_k(q)` is trace-preserving and is **not** tested: selecting a conjugator so that the conjugate is level-local would be choosing an object against a target, not a derivation.
- The reduction lemma's step (ii) is proved by the one-paragraph argument above and checked exhaustively only for `k ≤ 6`; at `k = 7` the argument alone carries it.
- Nothing here says whether the `3A`-strand embedding is the correct binding object; only that it is a different one.

## 6. Verification run

- `python3 -u computations/probes/uic_word_level_locality_probe.py 2>&1 | tee /tmp/uic-word-level-locality.log` → `11/11 checks passed (29 s wall)`, witness written.
- `scripts/precision-gates.sh --changed` — see the PR body for the run record (the first invocation failed preflight on a missing `qou_substrate` install, which is not a gate result).
